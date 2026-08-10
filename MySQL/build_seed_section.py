#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 db/schema.sql 提取字典种子段，转换为 MySQL 语法（反引号列名），
插入到 schema_mysql.sql 的视图段之前。"""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT.parent / "db" / "schema.sql"
DST = ROOT / "schema_mysql.sql"


def build_seed():
    src = SRC.read_text(encoding="utf-8")
    start = src.index("-- ---- 关系类型字典 ----")
    end = src.index("-- ============================================================================\n-- 视图：人物关系")
    seed = src[start:end].strip()
    out = []
    for ln in seed.split("\n"):
        m = re.match(r"^INSERT INTO (\w+) \((.+)\) VALUES$", ln)
        if m:
            tbl = m.group(1)
            cols = ", ".join("`" + c.strip() + "`" for c in m.group(2).split(","))
            out.append(f"INSERT INTO `{tbl}` ({cols}) VALUES")
        else:
            out.append(ln)
    return "\n".join(out)


def insert_seed():
    seed = build_seed()
    dst = DST.read_text(encoding="utf-8")
    anchor = "-- ----------------------------------------------------------------------------\n-- 视图：人物关系（双向）"
    # 找 MySQL 版里的视图段起点
    m = re.search(r"-- ----------------------------------------------------------------------------\n-- 视图：人物关系", dst)
    if not m:
        raise SystemExit("schema_mysql.sql 中未找到视图锚点")
    insert_at = m.start()
    new = dst[:insert_at] + seed + "\n\n" + dst[insert_at:]
    DST.write_text(new, encoding="utf-8")
    print(f"已插入种子段（{len(seed.splitlines())} 行）到 schema_mysql.sql")


if __name__ == "__main__":
    insert_seed()
