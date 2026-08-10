#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""将 SQLite greatminds.db 的全部数据迁移到 MySQL greatminds 库。

步骤：
1. 读取 SQLite 所有表
2. 按表导出为 MySQL INSERT 语句（INSERT IGNORE，处理转义）
3. 写入 data_mysql.sql，由 mysql 客户端执行
"""
import re
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DB = ROOT.parent / "db" / "greatminds.db"
OUT = ROOT / "data_mysql.sql"

# 导出顺序：字典表在前，关系表在后（外键依赖）
TABLES = [
    "people", "occupations", "fields", "awards",
    "institutions", "relation_types", "episodes", "badge_defs",
    "person_occupation", "person_field", "award_laureate",
    "person_institution", "person_relation", "rankings",
]


def mysql_escape(v):
    """SQLite 字符串 -> MySQL 字符串字面量"""
    return v.replace("\\", "\\\\").replace("'", "''").replace("\n", "\\n")


def dump_table(cur, table):
    cur.execute(f"SELECT * FROM {table}")
    cols = [d[0] for d in cur.description]
    rows = cur.fetchall()
    if not rows:
        return []
    col_list = ", ".join(f"`{c}`" for c in cols)
    lines = []
    for row in rows:
        vals = []
        for v in row:
            if v is None:
                vals.append("NULL")
            elif isinstance(v, (int, float)):
                vals.append(str(v))
            else:
                vals.append(f"'{mysql_escape(str(v))}'")
        lines.append(f"  ({', '.join(vals)})")
    # 分批插入，避免超长语句
    return [f"INSERT IGNORE INTO `{table}` ({col_list}) VALUES\n" + ",\n".join(lines) + ";", ""]


def main():
    conn = sqlite3.connect(DB)
    cur = conn.cursor()

    # 读取各表行数
    print("SQLite 表数据量：")
    for t in TABLES:
        n = cur.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
        print(f"  {t}: {n}")

    out = ["SET NAMES utf8mb4;", "SET FOREIGN_KEY_CHECKS = 0;", ""]
    for t in TABLES:
        out += dump_table(cur, t)
    out.append("SET FOREIGN_KEY_CHECKS = 1;")
    out.append("")

    OUT.write_text("\n".join(out), encoding="utf-8")
    print(f"\n已生成 {OUT}（{OUT.stat().st_size} 字节）")


if __name__ == "__main__":
    main()
