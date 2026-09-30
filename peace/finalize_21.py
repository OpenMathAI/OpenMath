#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""21 世纪批次主控收尾：QID 唯一性终检 + stub mathematician 残留清理。"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "MySQL"))
from db_mysql import get_conn  # noqa: E402

m = json.load(open(ROOT / "prompt_manifest_21.json"))
names = sorted({p["name"] for p in m["people"]})

conn = get_conn()
cur = conn.cursor()

# 1) QID 唯一性
ph = ",".join(["%s"] * 36)
cur.execute(
    f"SELECT qid, COUNT(*) c FROM people WHERE qid IN ({ph}) GROUP BY qid HAVING c>1",
    tuple(p["qid"] for p in m["people"]),
)
print("dup qid:", cur.fetchall())

# 2) stub 残留清理
ph2 = ",".join(["%s"] * len(names))
cur.execute(
    f"""SELECT DISTINCT p.id, p.name_en, p.primary_occupation
FROM people p
JOIN person_relation pr ON pr.from_id=p.id OR pr.to_id=p.id
JOIN people laureate ON (laureate.id=pr.from_id OR laureate.id=pr.to_id) AND laureate.id<>p.id
WHERE laureate.name_en IN ({ph2})
  AND p.has_social_data=0 AND p.has_biography=0 AND p.qid IS NULL
  AND p.id BETWEEN 6600 AND 8200""",
    tuple(names),
)
stubs = cur.fetchall()
cleaned = 0
for pid, en, po in stubs:
    cur.execute(
        """SELECT o.name_en FROM person_occupation po JOIN occupations o ON o.id=po.occupation_id
           WHERE po.person_id=%s""",
        (pid,),
    )
    occs = [r[0] for r in cur.fetchall()]
    if "mathematician" in occs:
        cur.execute(
            """DELETE po FROM person_occupation po JOIN occupations o ON o.id=po.occupation_id
               WHERE po.person_id=%s AND o.name_en='mathematician'""",
            (pid,),
        )
        cleaned += 1
        if po == "mathematician":
            cur.execute("UPDATE people SET primary_occupation=NULL WHERE id=%s", (pid,))
conn.commit()
print(f"stubs checked: {len(stubs)}, cleaned: {cleaned}")
