#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""合并 person_relation 分裂记录：把 stub 的关系改指到 main，撞键的删除，最后删 stub。"""
from db_mysql import get_conn

PAIRS = [
    # (keep_id, stub_id, 说明)
    (2135, 1947, "Robert Millikan stub -> Robert Andrews Millikan"),
    (1941, 2031, "Arthur Compton stub -> Arthur Holly Compton"),
    (355, 1950, "Robert Oppenheimer stub -> J. Robert Oppenheimer"),
    (2241, 1901, "John Ashworth Ratcliffe stub -> J. A. Ratcliffe"),
]

conn = get_conn()
cur = conn.cursor()
for keep, stub, note in PAIRS:
    cur.execute(
        "SELECT id, from_id, to_id, relation_type FROM person_relation "
        "WHERE from_id=%s OR to_id=%s",
        (stub, stub),
    )
    rows = cur.fetchall()
    deleted = moved = 0
    for rid, frm, to, rtype in rows:
        other = to if frm == stub else frm
        # 该行另一端
        cur.execute(
            "SELECT COUNT(*) FROM person_relation WHERE id<>%s AND relation_type=%s "
            "AND ((from_id=%s AND to_id=%s) OR (from_id=%s AND to_id=%s))",
            (rid, rtype, keep, other, other, keep),
        )
        if cur.fetchone()[0] > 0:
            cur.execute("DELETE FROM person_relation WHERE id=%s", (rid,))
            deleted += 1
        else:
            if frm == stub:
                cur.execute("UPDATE person_relation SET from_id=%s WHERE id=%s", (keep, rid))
            else:
                cur.execute("UPDATE person_relation SET to_id=%s WHERE id=%s", (keep, rid))
            moved += 1
    cur.execute("DELETE FROM person_occupation WHERE person_id=%s", (stub,))
    cur.execute("DELETE FROM person_field WHERE person_id=%s", (stub,))
    cur.execute("DELETE FROM people WHERE id=%s", (stub,))
    conn.commit()
    print(f"[{note}] moved={moved} deleted={deleted} stub {stub} removed")

# 复验
for keep, stub, note in PAIRS:
    cur.execute("SELECT COUNT(*) FROM people WHERE id=%s", (stub,))
    gone = cur.fetchone()[0] == 0
    cur.execute(
        "SELECT COUNT(*) FROM person_relation WHERE from_id=%s OR to_id=%s", (keep, keep)
    )
    rel = cur.fetchone()[0]
    print(f"keep {keep}: stub_gone={gone} relations={rel}")
