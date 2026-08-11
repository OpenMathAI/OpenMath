#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Review 第 4 层：生成 109 位数学家社会关系 Review 验收报告。"""
import sys

sys.path.insert(0, "/Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL")
from db_mysql import get_conn


def main():
    conn = get_conn()
    cur = conn.cursor()

    # 全部 109 位（rankings Top50 + 51_108 + 手动补的 Kodaira/Faltings）
    cur.execute("SELECT DISTINCT person_id FROM rankings")
    ids = {r[0] for r in cur.fetchall()}
    ids |= {550, 125}

    report = []
    pass_cnt = 0
    for pid in sorted(ids):
        cur.execute("""SELECT name_en, name_zh, qid, birth_date, death_date,
                   (SELECT COUNT(*) FROM person_nationality pn WHERE pn.person_id=p.id) AS nat,
                   (SELECT COUNT(*) FROM person_occupation po WHERE po.person_id=p.id) AS occ,
                   (SELECT COUNT(*) FROM person_field pf WHERE pf.person_id=p.id) AS fld,
                   (SELECT COUNT(*) FROM person_institution pi WHERE pi.person_id=p.id) AS inst,
                   (SELECT COUNT(*) FROM award_laureate al WHERE al.person_id=p.id) AS aw,
                   (SELECT COUNT(*) FROM person_relation pr WHERE pr.from_id=p.id OR pr.to_id=p.id) AS rel,
                   p.has_biography, p.has_social_data
                   FROM people p WHERE p.id=%s""", (pid,))
        r = cur.fetchone()
        if not r:
            report.append(f"| {pid} | 缺失 | - | - | - | - | - | - | - | ❌ |")
            continue
        (en, zh, qid, bd, dd, nat, occ, fld, inst, aw, rel, bio, social) = r
        # 已核实 Wikipedia 确无重大奖项的人（metadata 无 award_received）视为奖项项通过
        no_award_whitelist = {16, 31, 76, 77, 102, 104}
        aw_ok = aw > 0 or pid in no_award_whitelist
        ok = bool(qid and bd and nat and occ and fld and inst and aw_ok and rel and social)
        if ok:
            pass_cnt += 1
        report.append(
            f"| {pid} | {en} | {zh or '-'} | {qid or '-'} | {bd or '-'} | "
            f"国{nat}/职{occ}/域{fld}/机{inst} | 奖{aw} | 关系{rel} | "
            f"立传{'✅' if bio else '🔲'} | {'✅' if social else '❌'} |"
        )

    print(f"# 109 位 20 世纪数学家社会关系 Review 报告")
    print(f"\n**通过率: {pass_cnt}/{len(ids)} ({pass_cnt*100//len(ids)}%)**\n")
    print("| id | name_en | name_zh | qid | 生卒 | 维度(国/职/域/机) | 奖项 | 关系 | 立传 | 社会数据 |")
    print("|---|---|---|---|---|---|---|---|---|---|")
    for line in report:
        print(line)

    conn.close()


if __name__ == "__main__":
    main()
