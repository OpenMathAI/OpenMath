#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""greatminds 库一致性审计（2026-09-29）：数据不一致 + 跨奖查询便利性。"""
import re
from collections import Counter, defaultdict
from db_mysql import get_conn

conn = get_conn()
cur = conn.cursor()
issues = []


def q(sql, args=None):
    cur.execute(sql, args or ())
    return cur.fetchall()


print("=" * 60)
print("A. 孤儿行 / 引用完整性")
print("=" * 60)
a1 = q("SELECT COUNT(*) FROM award_laureate al LEFT JOIN people p ON p.id=al.person_id WHERE p.id IS NULL")[0][0]
a2 = q("SELECT COUNT(*) FROM award_laureate al LEFT JOIN awards a ON a.id=al.award_id WHERE a.id IS NULL")[0][0]
a3 = q("SELECT COUNT(*) FROM person_field pf LEFT JOIN people p ON p.id=pf.person_id WHERE p.id IS NULL")[0][0]
a4 = q("SELECT COUNT(*) FROM person_field pf LEFT JOIN fields f ON f.id=pf.field_id WHERE f.id IS NULL")[0][0]
a5 = q("SELECT COUNT(*) FROM person_relation r LEFT JOIN people p ON p.id=r.from_id WHERE p.id IS NULL")[0][0]
a6 = q("SELECT COUNT(*) FROM person_relation r LEFT JOIN people p ON p.id=r.to_id WHERE p.id IS NULL")[0][0]
a7 = q("SELECT COUNT(*) FROM person_relation WHERE from_id=to_id")[0][0]
for label, v in [("award_laureate→people 缺", a1), ("award_laureate→awards 缺", a2),
                 ("person_field→people 缺", a3), ("person_field→fields 缺", a4),
                 ("relation→from 缺", a5), ("relation→to 缺", a6), ("自环关系", a7)]:
    flag = "⚠️" if v else "✅"
    print(f"  {flag} {label}: {v}")
    if v:
        issues.append(f"{label}: {v}")

print()
print("=" * 60)
print("B. 同一人物同奖项同年份重复行（多年份获奖不视为重复）")
print("=" * 60)
dup = q("""SELECT al.person_id, p.name_en, a.name_en, al.year, COUNT(*) c
FROM award_laureate al JOIN people p ON p.id=al.person_id JOIN awards a ON a.id=al.award_id
GROUP BY al.person_id, al.award_id, al.year HAVING c>1
ORDER BY c DESC, p.name_en LIMIT 30""")
if dup:
    for r in dup:
        print(f"  ⚠️ {r[1]} | {r[2]} | year={r[3]} (x{r[4]})")
        issues.append(f"同年重复行: {r[1]} {r[2]} {r[3]}")
else:
    print("  ✅ 无同年重复")

print()
print("=" * 60)
print("C. 同 QID 多记录 / 同名多记录（全库）")
print("=" * 60)
dupq = q("SELECT qid, COUNT(*) c, GROUP_CONCAT(name_en) FROM people WHERE qid IS NOT NULL GROUP BY qid HAVING c>1 LIMIT 20")
for r in dupq:
    print(f"  ⚠️ QID {r[0]} x{r[2]}: {r[1]}")
    issues.append(f"同QID多记录 {r[0]}: {r[1]}")
if not dupq:
    print("  ✅ 无同 QID 重复")
# 规范化名重复（不同 QID 或无 QID 但同名同人风险）
norm_dup = q("""SELECT LOWER(name_en) n, COUNT(*) c, GROUP_CONCAT(id), GROUP_CONCAT(IFNULL(qid,'-')) FROM people GROUP BY LOWER(name_en) HAVING c>1 ORDER BY c DESC LIMIT 15""")
print(f"  同名（大小写归一）组数: {len(norm_dup)}（人工判断是否同人）")
for r in norm_dup[:8]:
    print(f"    {r[0]}: ids={r[2]} qids={r[3]}")

print()
print("=" * 60)
print("D. has_social_data / has_biography 标志位与实际数据一致性")
print("=" * 60)
bad_rel = q("SELECT id,name_en FROM people WHERE has_social_data=1 AND id NOT IN (SELECT DISTINCT person_id FROM person_field)")
bad_rel2 = q("SELECT id,name_en FROM people WHERE has_social_data=1 AND id NOT IN (SELECT from_id FROM person_relation UNION SELECT to_id FROM person_relation)")
bad_bio = q("SELECT id,name_en FROM people WHERE has_biography=1 AND has_social_data=0")
data_no_flag = q("""SELECT id,name_en FROM people p WHERE p.has_social_data=0
 AND (EXISTS(SELECT 1 FROM person_field pf WHERE pf.person_id=p.id HAVING COUNT(*)>=3)
      OR EXISTS(SELECT 1 FROM person_relation r WHERE (r.from_id=p.id OR r.to_id=p.id) HAVING COUNT(*)>=3))""")
for label, lst in [("flag=1 但无 person_field", bad_rel), ("flag=1 但无任何关系", bad_rel2),
                   ("has_biography=1 但 social=0", bad_bio), ("有数据但 flag=0", data_no_flag)]:
    print(f"  {'⚠️' if lst else '✅'} {label}: {len(lst)}")
    for r in lst[:5]:
        print(f"     {r}")
    if lst:
        issues.append(f"{label}: {len(lst)}")

print()
print("=" * 60)
print("E. 奖项名变体（同奖异名，跨奖查询杀手）")
print("=" * 60)
variants = q("""SELECT a1.id, a1.name_en, a2.id, a2.name_en, COUNT(DISTINCT al1.person_id), COUNT(DISTINCT al2.person_id)
FROM awards a1 JOIN awards a2 ON a1.id<a2.id
JOIN award_laureate al1 ON al1.award_id=a1.id
JOIN award_laureate al2 ON al2.award_id=a2.id
WHERE REPLACE(LOWER(a1.name_en),' ','') LIKE CONCAT('%%',REPLACE(LOWER(a2.name_en),' ',''),'%%')
   OR REPLACE(LOWER(a2.name_en),' ','') LIKE CONCAT('%%',REPLACE(LOWER(a1.name_en),' ',''),'%%')
GROUP BY a1.id, a1.name_en, a2.id, a2.name_en
HAVING COUNT(DISTINCT al1.person_id)>0 AND COUNT(DISTINCT al2.person_id)>0
ORDER BY COUNT(DISTINCT al1.person_id)+COUNT(DISTINCT al2.person_id) DESC LIMIT 20""")
if variants:
    for r in variants:
        print(f"  ⚠️ [{r[0]}]{r[1]} ({r[4]}人) <-> [{r[2]}]{r[3]} ({r[5]}人)")
        issues.append(f"奖项变体: {r[1]} <-> {r[3]}")
else:
    print("  ✅ 未发现包含关系的变体对")

print()
print("=" * 60)
print("F. 跨奖查询便利性")
print("=" * 60)
nozh = q("SELECT COUNT(*) FROM awards WHERE name_zh IS NULL OR name_zh='' OR name_zh=name_en")[0][0]
total = q("SELECT COUNT(*) FROM awards")[0][0]
print(f"  {'⚠️' if nozh else '✅'} awards 中文名缺失: {nozh}/{total}")
year0 = q("SELECT COUNT(*) FROM award_laureate WHERE year=0")[0][0]
ynull = q("SELECT COUNT(*) FROM award_laureate WHERE year IS NULL")[0][0]
print(f"  ℹ️ year=0（年份未标）: {year0} 行；year IS NULL: {ynull} 行")
# 三奖及以上得主视图是否存在便捷查询
multi3 = q("""SELECT p.name_en, COUNT(DISTINCT al.award_id) c FROM award_laureate al
JOIN people p ON p.id=al.person_id GROUP BY al.person_id, p.name_en HAVING c>=3 ORDER BY c DESC LIMIT 10""")
print(f"  ℹ️ ≥3 奖得主 top10（v_multi_award 未区分获奖类型/会士类荣誉）：")
for r in multi3:
    print(f"     {r[0]}: {r[1]} 项")
idx = q("SHOW INDEX FROM award_laureate")
idx_cols = {(i[2], i[4]) for i in idx}
print(f"  ℹ️ award_laureate 索引: {sorted({i[4] for i in idx})}")
nobel_rows = q("""SELECT a.name_en, COUNT(DISTINCT al.person_id) FROM awards a
LEFT JOIN award_laureate al ON al.award_id=a.id
WHERE a.id IN (22,23,24,25,26,857) GROUP BY a.id, a.name_en""")
print("  ℹ️ Nobel 六奖覆盖：")
for r in nobel_rows:
    print(f"     {r[0]}: {r[1]} 人")

print()
print("=" * 60)
print(f"共发现 {len(issues)} 处需处理")
for i in issues:
    print("  -", i)
