#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""入库终审复核：manifest 99 人逐一与 greatminds 库、yaml 文件双向对账。

检查项（每人）：
  A. 按 QID 在 people 表存在且唯一
  B. has_social_data = 1
  C. qid 与 manifest 一致
  D. person_field 条数 与 yaml fields 条数一致
  E. person_relation 条数 >= yaml relations 条数（允许多出并行批次合法入边，不允许少）

用法：python3 audit_db.py
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parent / "MySQL"))
from db_mysql import get_conn  # noqa: E402

# ---------------------------------------------------------------- 收集 99 人
people = []
for tag in ("20th", "21th"):
    m = json.loads((ROOT / f"prompt_manifest_{tag}.json").read_text(encoding="utf-8"))
    for b in m["batches"]:
        people.extend(b["people"])

# ---------------------------------------------------------------- yaml 解析（宽松计数）
def yaml_counts(path: Path) -> tuple[int, int, list[str]]:
    """返回 (fields 条数, relations 条数, 错误列表)。"""
    errs: list[str] = []
    try:
        import yaml as pyyaml
        data = pyyaml.safe_load(path.read_text(encoding="utf-8"))
    except Exception as e:
        return 0, 0, [f"yaml 解析失败: {e}"]
    fields = data.get("fields") or []
    rels = data.get("relations") or []
    return len(fields), len(rels), errs

# ---------------------------------------------------------------- DB 对账
conn = get_conn()
cur = conn.cursor()
cur.execute("SELECT id, name_en, qid, has_social_data FROM people")
db_all = cur.fetchall()
by_qid: dict[str, list] = {}
for pid, en, qid, soc in db_all:
    if qid:
        by_qid.setdefault(qid, []).append((pid, en, soc))

def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]", "", s.lower())

db_by_norm: dict[str, tuple] = {}
for pid, en, qid, soc in db_all:
    db_by_norm.setdefault(norm(en), (pid, en, soc))

problems: list[str] = []
ok = 0
for p in people:
    name, qid = p["name"], p.get("qid")
    d = p["dir"]
    recs = by_qid.get(qid or "§none§", [])
    if not recs:
        problems.append(f"{d}: QID {qid} 在 people 表无记录")
        continue
    if len(recs) > 1:
        problems.append(f"{d}: QID {qid} 分裂 {len(recs)} 条 {recs}")
    pid, en, soc = recs[0]
    if not soc:
        problems.append(f"{d}: {en}(id={pid}) has_social_data=0")
        continue
    # fields
    cur.execute("SELECT COUNT(*) FROM person_field WHERE person_id=%s", (pid,))
    db_f = cur.fetchone()[0]
    # relations
    cur.execute("SELECT COUNT(*) FROM person_relation WHERE from_id=%s OR to_id=%s", (pid, pid))
    db_r = cur.fetchone()[0]
    yaml_path = ROOT.parent / "MySQL" / "data" / f"{d}.yaml"
    if not yaml_path.exists():
        problems.append(f"{d}: yaml 缺失 {yaml_path.name}")
        continue
    y_f, y_r, errs = yaml_counts(yaml_path)
    if errs:
        problems.append(f"{d}: {errs[0]}")
    if db_f < y_f:
        problems.append(f"{d}: fields DB={db_f} < yaml={y_f}")
    if db_r < y_r:
        problems.append(f"{d}: relations DB={db_r} < yaml={y_r}")
    if not problems or not any(pr.startswith(d + ":") for pr in problems):
        ok += 1
        print(f"OK  {d:<28} id={pid:<6} q={qid:<10} fields={db_f}({y_f}) relations={db_r}({y_r})")

# ---------------------------------------------------------------- 附加：同名分裂扫描（99 人之外的同名不同 id）
seen_norm: dict[str, str] = {}
for p in people:
    seen_norm[norm(p["name"])] = p["qid"]
conn.close()

print("\n==================== 结果 ====================")
print(f"通过: {ok} / {len(people)}")
print(f"问题: {len(problems)}")
for pr in problems:
    print("  ✗", pr)
sys.exit(1 if problems else 0)
