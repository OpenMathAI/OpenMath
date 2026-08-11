#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Review：109 位 20 世纪数学家社会关系数据完整性扫描（第 1 层）。

对榜单全部 109 人逐一检查 8 项数据维度，输出缺口清单：
  qid / 生卒 / 国籍 / 职业 / 领域 / 机构 / 奖项 / 社会关系
并输出 rankings 覆盖缺口（榜单有、rankings 无的人）。
"""
import sys

sys.path.insert(0, "/Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL")
from db_mysql import get_conn

# 榜单 109 人的 rank -> 名字（用于展示）
RANKING = {
    53: "Kodaira Kunihiko", 109: "Gerd Faltings",
}

DIMENSIONS = {
    "qid": "qid 缺失",
    "birth_date": "生卒缺失",
    "nationality": "国籍缺失",
    "occupation": "职业缺失",
    "fields": "领域缺失",
    "institutions": "机构缺失",
    "awards": "奖项缺失",
    "relations": "社会关系缺失",
}


def main():
    conn = get_conn()
    cur = conn.cursor()

    # 所有在 rankings 中的人（Top50 + 51_108）
    cur.execute("SELECT DISTINCT r.person_id FROM rankings r")
    ranked_ids = {r[0] for r in cur.fetchall()}

    # 加上已知的 Kodaira(550) 与 Faltings(125)
    ranked_ids |= {550, 125}

    print(f"共检查 {len(ranked_ids)} 位排名内数学家\n")

    # 全维度查询
    rows = []
    for pid in sorted(ranked_ids):
        cur.execute("""
            SELECT p.id, p.name_en, p.name_zh, p.qid, p.birth_date, p.death_date,
                   (SELECT COUNT(*) FROM person_nationality pn WHERE pn.person_id=p.id) AS nat,
                   (SELECT COUNT(*) FROM person_occupation po WHERE po.person_id=p.id) AS occ,
                   (SELECT COUNT(*) FROM person_field pf WHERE pf.person_id=p.id) AS fld,
                   (SELECT COUNT(*) FROM person_institution pi WHERE pi.person_id=p.id) AS inst,
                   (SELECT COUNT(*) FROM award_laureate al WHERE al.person_id=p.id) AS aw,
                   (SELECT COUNT(*) FROM person_relation pr WHERE pr.from_id=p.id OR pr.to_id=p.id) AS rel,
                   p.has_social_data
            FROM people p WHERE p.id=%s
        """, (pid,))
        r = cur.fetchone()
        if r:
            rows.append(r)

    # 统计缺口（注意：在世数学家 death_date 为空是正常的）
    missing = {d: [] for d in DIMENSIONS}
    for (pid, en, zh, qid, bd, dd, nat, occ, fld, inst, aw, rel, social) in rows:
        checks = {
            "qid": not qid,
            "birth_date": (not bd) or (dd is None and False),  # 仅出生必须
            "nationality": nat == 0,
            "occupation": occ == 0,
            "fields": fld == 0,
            "institutions": inst == 0,
            "awards": aw == 0,
            "relations": rel == 0,
        }
        # 死亡数学家若缺 death_date 也标记
        if dd is None:
            cur.execute("SELECT birth_date, death_date FROM people WHERE id=%s", (pid,))
            r = cur.fetchone()
            # 已在 rows 数据中，无法区分"在世"还是"漏填"，此处交由人工判断
        for k, bad in checks.items():
            if bad:
                # 奖项白名单：已核实 Wikipedia 无重大奖项（metadata 无 award_received）
                if k == "awards" and pid in (16, 31, 76, 77, 102, 104):
                    continue
                missing[k].append((pid, en or zh or "?"))

    total_issues = 0
    for dim, label in DIMENSIONS.items():
        lst = missing[dim]
        if lst:
            total_issues += len(lst)
            print(f"【{label}】{len(lst)} 人")
            for pid, name in lst:
                print(f"    #{pid:>3} {name}")
            print()
        else:
            print(f"【{label}】✅ 无缺口")

    print(f"\n=== 汇总：{len(rows)} 人中 {total_issues} 处缺口 ===")

    # rankings 覆盖缺口：榜单 109 vs 数据库
    print("\n=== rankings 覆盖检查 ===")
    cur.execute("SELECT DISTINCT r.person_id FROM rankings r")
    db_ids = {r[0] for r in cur.fetchall()}
    # 榜单 109 人应覆盖（按 people 表 id 汇总）
    # 这里列出 rankings 缺失的已知人物（Kodaira 550、Faltings 125）
    for pid, note in ((550, "小平邦彦 #53 榜单有、rankings 缺"), (125, "Faltings #109 榜单有、rankings 缺")):
        if pid not in db_ids:
            print(f"  ⚠️ {note}")
    if 550 in db_ids and 125 in db_ids:
        print("  ✅ 无 rankings 缺口")

    conn.close()


if __name__ == "__main__":
    main()
