#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Review 第 1 层修复：补齐 109 位数学家社会关系数据缺口。

修复内容：
1. 4 位 Top50 数学家 qid 缺失（Serre/Cartan/陈省身/Fisher）
2. 51-57 段数学家缺失的 国籍/职业/领域/机构
3. 部分人物缺失的奖项
4. rankings 缺记录（Kodaira #53、Faltings #109）
"""
import sys

sys.path.insert(0, "/Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL")
from db_mysql import get_conn

# ---- 1. qid 补齐 ----
QID_FIX = {
    12: "Q212063",   # J.-P. Serre
    15: "Q274639",   # Élie Cartan
    29: "Q328131",   # 陈省身 Shiing-Shen Chern
    32: "Q216723",   # R.A. Fisher
}

# ---- 2. 国籍（person_nationality）----
NAT = {
    54: [("United States", 0)],              # Lefschetz（出生俄帝国，后美国）
    55: [("France", 0)],                      # Thom
    436: [("Soviet Union", 0), ("Russian Empire", 1)],  # Gelfand
    500: [("Japan", 0)],                      # Takagi
    550: [("Japan", 0)],                      # Kodaira
}

# ---- 3. 职业（person_occupation）----
OCC = {
    436: [("mathematician", 0)],
    500: [("mathematician", 0)],
    550: [("mathematician", 0)],
}

# ---- 4. 领域（person_field）----
FIELDS = {
    436: [("functional analysis", 0), ("representation theory", 1), ("integral geometry", 2)],
    500: [("algebraic number theory", 0), ("number theory", 1)],
    550: [("algebraic geometry", 0), ("complex manifold", 1), ("complex analysis", 2)],
}

# ---- 5. 机构（person_institution）----
INST = {
    54: [("Princeton University", "employment", 1924, 1953)],       # Lefschetz
    55: [("University of Strasbourg", "employment", 1964, None)],   # Thom
    56: [("Massachusetts Institute of Technology", "employment", 1919, 1960)],  # Wiener
    57: [("University of Cambridge", "employment", 1914, 1919)],    # Ramanujan（Trinity）
    436: [("Lomonosov Moscow State University", "employment", None, None),
          ("Steklov Institute of Mathematics", "employment", None, None)],      # Gelfand
    500: [("University of Tokyo", "employment", None, None)],       # Takagi
    550: [("University of Tokyo", "employment", None, None),
          ("Princeton University", "employment", None, None)],      # Kodaira
}

# ---- 6. 奖项（award_laureate）----
AWARDS = {
    54: [("Bôcher Memorial Prize", 1924), ("National Medal of Science", 1964)],  # Lefschetz
    56: [("National Medal of Science", 1963)],                                    # Wiener
    57: [("Fellow of the Royal Society", 1918)],                                  # Ramanujan
    64: [("Lobachevsky Prize", 0)],                                               # Schur
}

# ---- 7. rankings 补记录 ----
RANKINGS_FIX = [
    (550, "OpenMath_20th_Century_51_108", 53),   # Kodaira #53
    (125, "OpenMath_20th_Century_51_108", 109),   # Faltings #109
]


def main():
    conn = get_conn()
    cur = conn.cursor()

    def occ_id(name):
        cur.execute("SELECT id FROM occupations WHERE name_en=%s", (name,))
        r = cur.fetchone()
        return r[0] if r else None

    def nat_id(name):
        cur.execute("SELECT id FROM countries WHERE name_en=%s", (name,))
        r = cur.fetchone()
        return r[0] if r else None

    def field_id(name):
        cur.execute("SELECT id FROM fields WHERE name_en=%s", (name,))
        r = cur.fetchone()
        return r[0] if r else None

    def inst_id(name):
        cur.execute("SELECT id FROM institutions WHERE name_en=%s", (name,))
        r = cur.fetchone()
        return r[0] if r else None

    def award_id(name):
        cur.execute("SELECT id FROM awards WHERE name_en=%s", (name,))
        r = cur.fetchone()
        return r[0] if r else None

    # ---- 1. qid ----
    for pid, q in QID_FIX.items():
        cur.execute("UPDATE people SET qid=%s WHERE id=%s AND qid IS NULL", (q, pid))
        print(f"  ✓ #{pid} qid -> {q}")

    # ---- 2. 国籍 ----
    for pid, lst in NAT.items():
        for cname, rank in lst:
            cid = nat_id(cname)
            if cid:
                cur.execute("INSERT IGNORE INTO person_nationality(person_id, country_id, `rank`) VALUES (%s,%s,%s)",
                            (pid, cid, rank))
                print(f"  ✓ #{pid} 国籍 + {cname}")
            else:
                print(f"  ! #{pid} 国家不存在: {cname}")

    # ---- 3. 职业 ----
    for pid, lst in OCC.items():
        for oname, rank in lst:
            oid = occ_id(oname)
            if oid:
                cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,%s)",
                            (pid, oid, rank))
                print(f"  ✓ #{pid} 职业 + {oname}")

    # ---- 4. 领域 ----
    for pid, lst in FIELDS.items():
        for fname, rank in lst:
            fid = field_id(fname)
            if fid:
                cur.execute("INSERT IGNORE INTO person_field(person_id, field_id, `rank`) VALUES (%s,%s,%s)",
                            (pid, fid, rank))
                print(f"  ✓ #{pid} 领域 + {fname}")
            else:
                print(f"  ! #{pid} 领域不存在: {fname}")

    # ---- 5. 机构 ----
    for pid, lst in INST.items():
        for iname, rel, sy, ey in lst:
            iid = inst_id(iname)
            if iid:
                cur.execute(
                    "SELECT 1 FROM person_institution WHERE person_id=%s AND inst_id=%s AND relation=%s",
                    (pid, iid, rel))
                if not cur.fetchone():
                    cur.execute(
                        "INSERT IGNORE INTO person_institution(person_id, inst_id, relation, start_year, end_year) "
                        "VALUES (%s,%s,%s,%s,%s)", (pid, iid, rel, sy, ey))
                    print(f"  ✓ #{pid} 机构 + {iname} ({rel})")
                else:
                    print(f"  = #{pid} 机构已存在 {iname}")
            else:
                print(f"  ! #{pid} 机构不存在: {iname}")

    # ---- 6. 奖项 ----
    for pid, lst in AWARDS.items():
        for aname, year in lst:
            aid = award_id(aname)
            if aid:
                cur.execute(
                    "INSERT IGNORE INTO award_laureate(person_id, award_id, `year`, share_type, source, note) "
                    "VALUES (%s,%s,%s,'独享','Review-fix',%s)",
                    (pid, aid, year, None if year else "年份待查"))
                print(f"  ✓ #{pid} 奖项 + {aname} ({year})")
            else:
                print(f"  ! #{pid} 奖项不存在: {aname}")

    # ---- 7. rankings ----
    for pid, list_key, rank in RANKINGS_FIX:
        cur.execute("SELECT 1 FROM rankings WHERE list_key=%s AND `rank`=%s", (list_key, rank))
        if not cur.fetchone():
            cur.execute("INSERT INTO rankings(list_key, `rank`, person_id, status) VALUES (%s,%s,%s,'🔲')",
                        (list_key, rank, pid))
            print(f"  ✓ rankings + #{pid} {list_key} rank={rank}")
        else:
            print(f"  = rankings 已存在 #{pid} {list_key} rank={rank}")

    conn.commit()
    conn.close()
    print("\n修复完成")


if __name__ == "__main__":
    main()
