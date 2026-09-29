#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 greatminds 库生成 20 世纪诺奖物理得主交叉关系报告 cross_awards_from_db.md。"""
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, "/Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL")
from db_mysql import get_conn

ROOT = Path("/Users/ericksun/workspace/codebuddy/OpenMathAI/physicist")
man = json.loads((ROOT / "prompt_manifest.json").read_text(encoding="utf-8"))
qids = {p["qid"]: p for p in man["people"]}          # qid -> person
# 库内 name_en -> manifest name（含别名形式，如 C. F. Powell / C. F. Powell?）
conn = get_conn()
cur = conn.cursor()

def person(pid):
    cur.execute("SELECT name_en, qid FROM people WHERE id=%s", (pid,))
    return cur.fetchone()

cur.execute("SELECT from_id, to_id, relation_type, note FROM person_relation")
coh, adv, col, spo = defaultdict(list), [], defaultdict(list), []
for frm, to, t, note in cur.fetchall():
    a, b = person(frm), person(to)
    if not a or not b:
        continue
    if a[1] in qids and b[1] in qids:
        na, nb = a[0], b[0]
        pair = tuple(sorted([na, nb]))
        if t == "co-honored":
            coh[pair].append(note)
        elif t == "advisor-student":
            adv.append((na, nb, note))
        elif t == "spouse":
            spo.append((na, nb, note))
        else:
            col[pair].append((t, note))

# 按诺奖年份分组 co-honored（note 里抽 19xx）
import re
byyear = defaultdict(set)
for (na, nb), notes in coh.items():
    years = re.findall(r"(19\d\d)", " ".join(notes))
    y = years[0] if years else "????"
    byyear[y].add((na, nb, " / ".join(notes)))

lines = []
lines.append("# 20 世纪诺贝尔物理学奖得主交叉关系报告（数据库直查版）")
lines.append("")
lines.append("> 生成时间：2026-09-28 · 数据源：greatminds 库 person_relation / person_field")
lines.append("> 范围：161 位 20 世纪（1901–2000）诺贝尔物理学奖得主两两之间的已入库关系")
lines.append("> 入库口径：仅收各人 page.md 明载关系（metadata-only 一律不入库）；查询脚本见文末")
lines.append("")
lines.append("## 一、共享诺奖 / 同届关系网（co-honored）")
lines.append("")
lines.append(f"共 **{sum(len(v) for v in coh.values())} 条**得主两两 co-honored 关系（去重后 {len(coh)} 对），按诺奖年份分组：")
lines.append("")
for y in sorted(k for k in byyear if k != "????"):
    lines.append(f"### {y}")
    lines.append("")
    for na, nb, note in sorted(byyear[y]):
        lines.append(f"- {na} ↔ {nb} —— {note}")
    lines.append("")

lines.append("## 二、得主之间的师承关系（advisor-student，双向去重后）")
lines.append("")
seen = set()
for na, nb, note in adv:
    key = tuple(sorted([na, nb]))
    if key in seen:
        continue
    seen.add(key)
    lines.append(f"- {na} → {nb} —— {note}")
lines.append(f"")
lines.append(f"共 {len(seen)} 对。")
lines.append("")

lines.append("## 三、得主之间的同事 / 合作 / 争议 / 影响 / 配偶关系")
lines.append("")
for (na, nb), items in sorted(col.items()):
    for t, note in items:
        zh = {"colleague": "同事/合作", "controversy": "争议", "influence": "影响", "rival": "竞争", "spouse": "配偶", "parent-child": "亲子"}.get(t, t)
        lines.append(f"- {na} ↔ {nb}（{zh}）—— {note}")
lines.append("")
if spo:
    lines.append("### 得主夫妻档")
    lines.append("")
    seen = set()
    for na, nb, *_ in spo:
        key = tuple(sorted([na, nb]))
        if key in seen:
            continue
        seen.add(key)
        lines.append(f"- {na} ↔ {nb}")
    lines.append("")

lines.append("## 四、复现查询（MySQL）")
lines.append("")
lines.append("```sql")
lines.append("-- 得主两两 co-honored（两端的 people.qid 都在 161 人清单内）")
lines.append("SELECT pa.name_en, pb.name_en, r.note")
lines.append("FROM person_relation r")
lines.append("JOIN people pa ON pa.id = r.from_id")
lines.append("JOIN people pb ON pb.id = r.to_id")
lines.append("WHERE r.relation_type = 'co-honored'")
lines.append("  AND pa.qid IN (SELECT qid FROM people WHERE primary_occupation='physicist' AND has_social_data=1)")
lines.append("  AND pb.qid IN (SELECT qid FROM people WHERE primary_occupation='physicist' AND has_social_data=1);")
lines.append("")
lines.append("-- 得主师承链（导师→学生，双方均为 161 人清单）")
lines.append("SELECT pa.name_en AS advisor, pb.name_en AS student")
lines.append("FROM person_relation r")
lines.append("JOIN people pa ON pa.id = r.from_id")
lines.append("JOIN people pb ON pb.id = r.to_id")
lines.append("WHERE r.relation_type = 'advisor-student';")
lines.append("```")
lines.append("")

out = ROOT / "cross_awards_from_db.md"
out.write_text("\n".join(lines), encoding="utf-8")
print("written:", out)
print("co-honored pairs:", len(coh), "| advisor pairs:", len(set(tuple(sorted([a,b])) for a,b,_ in adv)), "| colleague-type pairs:", len(col), "| spouse:", len(set(tuple(sorted([a,b])) for a,b,*_ in spo)))
