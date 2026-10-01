#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""合并奖项变体 + 清理垃圾条目（幂等）。"""
from db_mysql import get_conn

conn = get_conn()
cur = conn.cursor()

def merge_award(keep, dup):
    """把 dup 的 laureate 行并入 keep：撞 (person,year) 键的删，其余改指；删 dup。"""
    cur.execute("SELECT person_id, year FROM award_laureate WHERE award_id=%s", (dup,))
    rows = cur.fetchall()
    moved = deleted = 0
    for pid, y in rows:
        cur.execute("SELECT COUNT(*) FROM award_laureate WHERE award_id=%s AND person_id=%s AND year<=>%s",
                    (keep, pid, y))
        if cur.fetchone()[0]:
            cur.execute("DELETE FROM award_laureate WHERE award_id=%s AND person_id=%s AND year<=>%s",
                        (dup, pid, y))
            deleted += 1
        else:
            cur.execute("UPDATE award_laureate SET award_id=%s WHERE award_id=%s AND person_id=%s AND year<=>%s",
                        (keep, dup, pid, y))
            moved += 1
    cur.execute("DELETE FROM awards WHERE id=%s", (dup,))
    conn.commit()
    print(f"merge {dup} -> {keep}: moved={moved} deleted={deleted}")
    # 若合并后 keep 出现同人同年重复（源行本就并存），按组去重保留有年份行
    cur.execute("""SELECT person_id, COUNT(*) c FROM award_laureate WHERE award_id=%s
                   GROUP BY person_id HAVING c>1""", (keep,))
    for pid, c in cur.fetchall():
        cur.execute("""SELECT year FROM award_laureate WHERE award_id=%s AND person_id=%s
                       ORDER BY year=0, year""", (keep, pid))
        years = [r[0] for r in cur.fetchall()]
        real = [y for y in years if y and y != 0]
        if len(years) > 1 and real:
            # 有真实年份时删掉 year=0 的未知行；否则保留（真实连获）
            if 0 in years:
                cur.execute("DELETE FROM award_laureate WHERE award_id=%s AND person_id=%s AND year=0",
                            (keep, pid))
                print(f"  dedup person {pid}: removed year=0 dup")
    conn.commit()

# 1) 图灵奖变体 → ACM A.M. Turing Award(14)
merge_award(14, 463)   # A.M. Turing Award
merge_award(14, 316)   # ACM Turing Award
merge_award(14, 839)   # Turing Award
# 2) National Medal of Science 变体 → 35
merge_award(35, 322)   # U.S. National Medal of Science
merge_award(35, 765)   # US National Medal of Science
# 3) NAS 变体 → 37
merge_award(37, 738)   # National Academy of Sciences
# 4) Wolf Prize 泛称(676)：按人归入 Mathematics(3) / Physics(243)
cur.execute("""SELECT al.person_id, p.name_en FROM award_laureate al
               JOIN people p ON p.id=al.person_id WHERE al.award_id=676""")
for pid, name in cur.fetchall():
    cur.execute("""SELECT COUNT(*) FROM person_field pf JOIN fields f ON f.id=pf.field_id
                   WHERE pf.person_id=%s AND (f.name_en LIKE '%%physic%%' OR f.name_en LIKE '%%condensed%%'
                         OR f.name_en LIKE '%%particle%%' OR f.name_en LIKE '%%optics%%')""", (pid,))
    is_phys = cur.fetchone()[0] > 0
    target = 243 if is_phys else 3
    cur.execute("SELECT COUNT(*) FROM award_laureate WHERE award_id=%s AND person_id=%s", (target, pid))
    if cur.fetchone()[0]:
        cur.execute("DELETE FROM award_laureate WHERE award_id=676 AND person_id=%s", (pid,))
        print(f"wolf 676: {name} dup -> removed")
    else:
        cur.execute("UPDATE award_laureate SET award_id=%s WHERE award_id=676 AND person_id=%s", (target, pid))
        print(f"wolf 676: {name} -> {'Physics(243)' if is_phys else 'Math(3)'}")
conn.commit()
cur.execute("DELETE FROM awards WHERE id=676")
conn.commit()

# 5) 垃圾单字/残缺奖项：Prize(853)、AC(790)
for junk in (853, 790):
    cur.execute("SELECT person_id, name_en FROM award_laureate al JOIN awards a ON a.id=al.award_id WHERE a.id=%s", (junk,))
    who = cur.fetchall()
    cur.execute("DELETE FROM award_laureate WHERE award_id=%s", (junk,))
    cur.execute("DELETE FROM awards WHERE id=%s", (junk,))
    print(f"junk {junk} removed, affected persons: {who}")
conn.commit()

# 6) 解析重复：year=0 与真实年份并存的三条 NAS 行已在 merge 中去重，这里终检
cur.execute("""SELECT p.name_en, a.name_en, GROUP_CONCAT(IFNULL(al.year,0)) FROM award_laureate al
JOIN people p ON p.id=al.person_id JOIN awards a ON a.id=al.award_id
GROUP BY al.person_id, al.award_id HAVING COUNT(*)>1 AND SUM(year=0)>0 AND SUM(year>0)>0""")
left = cur.fetchall()
print("残余 0+真年并存:", left)
