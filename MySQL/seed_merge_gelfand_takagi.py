#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""合并同名重复人物：早期名序/缩写占位 → 立传版规范名。

- Gelfand: id=51 'I.M. Gelfand'(占位) → id=436 'Israel Gelfand'(立传)
  （51 含 Wolf 1978 奖 + Top50 排名 + Kolmogorov 导师关系，迁移至 436）
- Takagi:  id=52 'Takagi Teiji'(占位) → id=500 'Teiji Takagi'(立传)
  （52 含 Top50 排名 + Hilbert 导师关系，迁移至 500）

幂等：INSERT IGNORE + 迁移后删除占位（若已删除则跳过）。
"""
from db_mysql import get_conn

MERGES = [
    # (占位 id, 立传 id)
    (51, 436),
    (52, 500),
]


def main():
    conn = get_conn()
    cur = conn.cursor()
    for src, dst in MERGES:
        cur.execute("SELECT COUNT(*) FROM people WHERE id=%s", (src,))
        if not cur.fetchone()[0]:
            print(f"  {src} 已不存在，跳过")
            continue
        # 迁移关联数据（INSERT IGNORE 幂等）
        for tbl, cols in [
            ("award_laureate", "person_id, award_id, year, note, source"),
            ("rankings", "person_id, list_key, `rank`, orig_rank, tag, status"),
        ]:
            cur.execute(f"INSERT IGNORE INTO {tbl} ({cols}) SELECT {cols} FROM {tbl} WHERE person_id=%s", (src,))
        # 迁移社会关系（重映射 src→dst）
        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "SELECT CASE WHEN from_id=%s THEN %s ELSE from_id END, "
            "CASE WHEN to_id=%s THEN %s ELSE to_id END, relation_type, note, source "
            "FROM person_relation WHERE from_id=%s OR to_id=%s",
            (src, dst, src, dst, src, src),
        )
        # 清理占位
        for tbl in ("person_occupation", "person_relation", "person_nationality",
                    "person_institution", "person_field", "award_laureate", "rankings"):
            cur.execute(f"DELETE FROM {tbl} WHERE person_id=%s", (src,))
        cur.execute("DELETE FROM person_relation WHERE from_id=%s OR to_id=%s", (src, src))
        cur.execute("DELETE FROM people WHERE id=%s", (src,))
        print(f"  合并 {src} → {dst} 完成")
    conn.commit()
    for pid in [436, 500, 550]:
        cur.execute("SELECT name_en FROM people WHERE id=%s", (pid,))
        row = cur.fetchone()
        if row:
            cur.execute("SELECT COUNT(*) FROM person_relation pr WHERE pr.from_id=%s OR pr.to_id=%s", (pid, pid))
            print(f"  {row[0]} (id={pid}) 关系数: {cur.fetchone()[0]}")
    conn.close()


if __name__ == "__main__":
    main()
