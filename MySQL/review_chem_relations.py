#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""化学侧入库关系审查：结构瑕疵 + 语义抽查。只读，不改库。"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from db_mysql import get_conn

conn = get_conn()
cur = conn.cursor()

UNDIRECTED = {"colleague", "collaborator", "co-honored", "spouse", "sibling",
              "controversy", "rival", "other", "influence", "competitor"}

issues = {k: [] for k in
          ["A_自环", "B_无向未归一", "C_无向反向重复", "D_师生方向可疑", "E_亲子方向可疑",
           "F_cohonored_年份不符", "G_共享组缺边", "H_化学家误标数学家"]}

cur.execute("SELECT id, from_id, to_id, relation_type, note FROM person_relation")
rels = cur.fetchall()
cur.execute("SELECT id, name_en, birth_date, death_date, primary_occupation, has_social_data FROM people")
people = {r[0]: r for r in cur.fetchall()}
cur.execute("SELECT person_id, o.name_en FROM person_occupation po JOIN occupations o ON o.id=po.occupation_id")
occ = {}
for pid, oen in cur.fetchall():
    occ.setdefault(pid, []).append(oen)

def byear(pid):
    b = people[pid][2] if pid in people else None
    if not b:
        return None
    s = str(b)
    return int(s[:4]) if len(s) >= 4 and s[:4].isdigit() else None

# A 自环
for rid, f, t, rt, note in rels:
    if f == t:
        issues["A_自环"].append((rid, f, rt, (note or "")[:40]))

# B 无向类型未按 from<to 归一
for rid, f, t, rt, note in rels:
    if rt in UNDIRECTED and f > t:
        issues["B_无向未归一"].append((rid, f, t, rt))

# C 无向类型同对反向重复
seen = {}
for rid, f, t, rt, note in rels:
    if rt in UNDIRECTED:
        key = (min(f, t), max(f, t), rt)
        if key in seen:
            issues["C_无向反向重复"].append((seen[key], rid, key))
        seen[key] = rid

# D advisor-student：导师(from)出生年不应晚于学生(to)出生年-10
for rid, f, t, rt, note in rels:
    if rt == "advisor-student" and f in people and t in people:
        bf, bt = byear(f), byear(t)
        if bf and bt and bf > bt - 10:
            issues["D_师生方向可疑"].append((rid, people[f][1], bf, people[t][1], bt, (note or "")[:40]))

# E parent-child：父(from)出生年不应晚于子(to)出生年-12
for rid, f, t, rt, note in rels:
    if rt == "parent-child" and f in people and t in people:
        bf, bt = byear(f), byear(t)
        if bf and bt and bf > bt - 12:
            issues["E_亲子方向可疑"].append((rid, people[f][1], bf, people[t][1], bt, (note or "")[:40]))

# 化学诺奖得主（名单英文名 + 年份）
chem = {}
for src in ["../chemist/prompt_db_map.json", "../chemist/prompt_db_map_21.json"]:
    p = Path(__file__).resolve().parent / src
    data = json.loads(p.read_text(encoding="utf-8"))
    for name, v in data.items():
        db = v["db"] if isinstance(v.get("db"), dict) else None
        chem[name] = db["id"] if db else None

# 名录英文姓名->年份（从 citations json）
cites = json.loads((Path(__file__).resolve().parent / "../chemist/nobel_chemistry_citations.json").read_text(encoding="utf-8"))
name_years = {}
for r in cites:
    name_years.setdefault(r["name"], set()).add(r["year"])

# F co-honored 语义抽查：双方是否共享任一化学诺奖年份
for rid, f, t, rt, note in rels:
    if rt != "co-honored":
        continue
    nf = people[f][1] if f in people else "?"
    nt = people[t][1] if t in people else "?"
    yf = name_years.get(nf, set())
    yt = name_years.get(nt, set())
    if yf and yt and not (yf & yt):
        issues["F_cohonored_年份不符"].append((rid, nf, sorted(yf), nt, sorted(yt), (note or "")[:50]))

# G 共享组缺边：同一年多人均分同一理由的组内两两应均有 co-honored
by_year_cite = {}
for r in cites:
    by_year_cite.setdefault((r["year"], r["citation"]), []).append(r["name"])
missing_edges = []
for (year, cite), names in by_year_cite.items():
    if len(names) < 2:
        continue
    ids = [chem.get(n) for n in names]
    if any(i is None for i in ids):
        continue
    for i in range(len(ids)):
        for j in range(i + 1, len(ids)):
            a, b = min(ids[i], ids[j]), max(ids[i], ids[j])
            cur.execute("SELECT COUNT(*) FROM person_relation WHERE relation_type='co-honored' AND from_id=%s AND to_id=%s", (a, b))
            if cur.fetchone()[0] == 0:
                missing_edges.append((year, names[i], names[j]))
issues["G_共享组缺边"] = missing_edges

# H 化学诺奖得主被自动 stub 误标 mathematician（且非其真实职业主记录）
for name, pid in chem.items():
    if pid and occ.get(pid) and "mathematician" in occ[pid] and people[pid][4] != "mathematician":
        issues["H_化学家误标数学家"].append((pid, name, occ[pid]))

print("=" * 60)
for k, v in issues.items():
    print(f"\n### {k}: {len(v)} 条")
    for x in v[:20]:
        print("  ", x)
    if len(v) > 20:
        print(f"   ... 共 {len(v)} 条")
