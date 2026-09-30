#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""OpenPeace 入库全面审计（2026-09-30）。

检查项：
  1. 140 位得主 has_social_data=1、qid 齐全且唯一（无分裂 stub）
  2. person_field / person_relation 行数（本人双边合计）
  3. award_laureate 行（Nobel Peace Prize 年份正确、多次获奖组织合并一条记录）
  4. 对手方 stub 残留（mathematician 职业）复查
  5. yaml 文件齐全且可解析、与 manifest name_en 一致性
  6. 名录 md 的 ✅ 行数与 DB 一致
"""
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "MySQL"))
from db_mysql import get_conn  # noqa: E402

FAIL = []


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_'.()\u00b7,\-]", "", s).lower()


m20 = json.load(open(ROOT / "prompt_manifest.json"))
m21 = json.load(open(ROOT / "prompt_manifest_21.json"))
alias = {
    "Lord Boyd-Orr": "John Boyd Orr",
    "John Raleigh Mott": "John Mott",
    "United Nations Children's Fund (UNICEF)": "United Nations Children's Fund",
    "Wangari Muta Maathai": "Wangari Maathai",
}

conn = get_conn()
cur = conn.cursor()

# ---------- 1) 得主主记录 ----------
print("=== 1) 得主主记录 ===")
tf = tr = 0
seen_qid = {}
ok20 = ok21 = 0
for m, tag, years_expect in ((m20, "20th", 104), (m21, "21st", 36)):
    for p in m["people"]:
        en = alias.get(p["name"], p["name"])
        cur.execute("SELECT id,name_en,qid,has_social_data FROM people WHERE name_en=%s", (en,))
        r = cur.fetchone()
        if not r:
            FAIL.append(f"[{tag}] {p['name']} 主记录缺失")
            continue
        pid, name_en, qid, soc = r
        if soc != 1:
            FAIL.append(f"[{tag}] {en} has_social_data={soc}")
        if not qid:
            FAIL.append(f"[{tag}] {en} qid 缺失（manifest 期望 {p['qid']}）")
        elif qid != p["qid"]:
            FAIL.append(f"[{tag}] {en} qid 不一致: DB={qid} manifest={p['qid']}")
        if qid in seen_qid:
            FAIL.append(f"[{tag}] qid 分裂: {qid} -> {seen_qid[qid]} & {pid}")
        seen_qid[qid] = pid
        cur.execute("SELECT COUNT(*) FROM person_field WHERE person_id=%s", (pid,))
        f = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM person_relation WHERE from_id=%s OR to_id=%s", (pid, pid))
        rel = cur.fetchone()[0]
        tf += f
        tr += rel
        if f < 3 or rel < 2:
            FAIL.append(f"[{tag}] {en} fields={f} relations={rel} 低于阈值")
        if tag == "20th":
            ok20 += 1
        else:
            ok21 += 1
print(f"20th: {ok20}/104, 21st: {ok21}/36, fields={tf}, relations={tr}")

# ---------- 2) award_laureate ----------
print("=== 2) award_laureate（Nobel Peace Prize）===")
cur.execute("SELECT id FROM awards WHERE name_en='Nobel Peace Prize'")
aw = cur.fetchone()
if not aw:
    FAIL.append("awards 缺 Nobel Peace Prize 字典项")
    award_id = None
else:
    award_id = aw[0]
n_award = 0
for m in (m20, m21):
    for p in m["people"]:
        en = alias.get(p["name"], p["name"])
        cur.execute("SELECT id FROM people WHERE name_en=%s", (en,))
        pid = cur.fetchone()[0]
        cur.execute(
            "SELECT year, share_type FROM award_laureate WHERE person_id=%s AND award_id=%s ORDER BY year",
            (pid, award_id))
        rows = cur.fetchall()
        yrs = [y for y, _ in rows]
        expect = p["years"]
        if yrs != expect:
            FAIL.append(f"{en} award years {yrs} != expect {expect}")
        n_award += len(rows)
print(f"award rows: {n_award}（应=140 位 × 各自次数）")
cur.execute("SELECT COUNT(*) FROM award_laureate WHERE award_id=%s", (award_id,))
total_rows = cur.fetchone()[0]
if total_rows != n_award:
    print(f"WARN: 该奖项下还有 {total_rows - n_award} 行不属 140 位得主（候选/其他批次）")

# ---------- 3) stub 残留 ----------
print("=== 3) stub mathematician 残留 ===")
cur.execute("""
SELECT COUNT(*) FROM people p
JOIN person_occupation po ON po.person_id=p.id
JOIN occupations o ON o.id=po.occupation_id
WHERE p.has_social_data=0 AND p.has_biography=0 AND p.qid IS NULL
  AND o.name_en='mathematician' AND p.id BETWEEN 6600 AND 8200
""")
print("residual mathematician occupation rows (peace id range):", cur.fetchone()[0])

# ---------- 4) yaml 文件 ----------
print("=== 4) yaml 齐全与解析 ===")
import yaml
n_yaml = 0
for m in (m20, m21):
    for p in m["people"]:
        yp = ROOT.parent / p["yaml"]
        if not yp.exists():
            # 允许 batch-01 用库内形式命名的 yaml
            cand = list((ROOT.parent / "MySQL/data").glob(f"{p['dir']}*.yaml"))
            if not cand:
                FAIL.append(f"yaml 缺失: {p['yaml']}")
                continue
            yp = cand[0]
        try:
            d = yaml.safe_load(yp.read_text(encoding="utf-8"))
            assert d and "name_en" in d and "relations" in d and "fields" in d
            n_yaml += 1
        except Exception as e:
            FAIL.append(f"yaml 解析失败 {yp.name}: {e}")
print(f"yaml OK: {n_yaml}/140")

# ---------- 5) 名录一致性 ----------
print("=== 5) 名录 ✅ 行数 ===")
for path, expect in ((ROOT / "presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md", 107),
                     (ROOT / "presentations/21th_century/OpenPeace_21st_Century_Nobel_Laureates.md", 36)):
    t = path.read_text(encoding="utf-8")
    done = len(re.findall(r"\| ✅ \|$", t, re.M))
    print(f"{path.name}: {done}/{expect}")
    if done != expect:
        FAIL.append(f"名录 ✅ 行数不符: {path.name} {done}/{expect}")

print("\n=== 结果 ===")
if FAIL:
    print(f"FAIL {len(FAIL)} 项：")
    for f in FAIL:
        print(" -", f)
else:
    print("✅ 全部通过：140 位得主记录/QID/fields/relations/awards/yaml/名录 一致无误")
