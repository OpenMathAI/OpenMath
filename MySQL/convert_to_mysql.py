#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把 db/ 下的 seed_*.py 与 export_people.py 从 sqlite3 改造为 pymysql（MySQL 版）。

转换规则：
- import sqlite3  -> from db_mysql import get_conn
- DB = ROOT/...   -> 删除（连接由 get_conn 提供）
- sqlite3.connect(DB) -> get_conn()
- conn.execute("PRAGMA foreign_keys = ON") -> 删除
- datetime('now','localtime') -> NOW()
"""
import re
from pathlib import Path

DB_DIR = Path(__file__).resolve().parent.parent / "db"
OUT_DIR = Path(__file__).resolve().parent
FILES = [
    "seed_ranking.py", "seed_fields.py", "seed_biography.py",
    "seed_relations.py", "seed_fields_medal.py", "seed_wolf_prize.py",
    "seed_abel_prize.py", "seed_chern_medal.py", "seed_turing.py",
    "seed_copss.py", "export_people.py",
]


def convert(src: str) -> str:
    # 1) 头部：import
    s = re.sub(r"^import sqlite3\n", "import pymysql\nfrom db_mysql import get_conn\n", src, flags=re.M)
    # 2) 删除 DB = ROOT / "greatminds.db" 行
    s = re.sub(r"^DB = ROOT /\s*\"greatminds\.db\"\n", "", s, flags=re.M)
    # 3) 连接
    s = s.replace("conn = sqlite3.connect(DB)", "conn = get_conn()")
    # 4) PRAGMA 行
    s = re.sub(r"^\s*conn\.execute\(\"PRAGMA foreign_keys = ON\"\)\n", "", s, flags=re.M)
    # 5) export_people 中的链式连接 + NOW()
    s = s.replace(
        "sqlite3.connect(DB).execute('SELECT datetime(\\'now\\',\\'localtime\\')').fetchone()[0]",
        "get_conn().execute('SELECT NOW()').fetchone()[0]",
    )
    # 6) sqlite3.Row（字典式访问）-> pymysql DictCursor
    s = s.replace(
        "conn = sqlite3.connect(DB)\n    conn.row_factory = sqlite3.Row\n    cur = conn.cursor()",
        "conn = get_conn()\n    cur = conn.cursor(pymysql.cursors.DictCursor)",
    )
    # 6b) 连接已替换但 row_factory 残留
    s = s.replace("conn = get_conn()\n    conn.row_factory = sqlite3.Row\n    cur = conn.cursor()",
                  "conn = get_conn()\n    cur = conn.cursor(pymysql.cursors.DictCursor)")
    # 兜底：其他残留 sqlite3
    s = s.replace("sqlite3.connect(DB)", "get_conn()")
    return s


def main():
    for name in FILES:
        p = DB_DIR / name
        if not p.exists():
            print(f"跳过（不存在）: {name}")
            continue
        out = convert(p.read_text(encoding="utf-8"))
        (OUT_DIR / name).write_text(out, encoding="utf-8")
        # 校验无残留
        rest = [ln for ln in out.splitlines() if "sqlite3" in ln or "PRAGMA" in ln or 'greatminds.db"' in ln]
        status = "⚠ 有残留" if rest else "OK"
        print(f"{name}: {status}")
        for r in rest:
            print(f"    {r.strip()}")
    print("\n完成。文件已写入:", OUT_DIR)


if __name__ == "__main__":
    main()
