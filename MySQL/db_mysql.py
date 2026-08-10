#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""greatminds MySQL 连接模块（pymysql）。

提供：
- get_conn(): 返回 pymysql 连接（cursorclass=CompatCursor，自动适配 SQLite 语法）
- CompatCursor: 自动转换 SQLite 语法 -> MySQL：
    ?              -> %s（参数占位符）
    INSERT OR IGNORE -> INSERT IGNORE
    INSERT OR REPLACE -> REPLACE INTO
"""
import pymysql
import pymysql.cursors

DB_CONFIG = dict(
    host="127.0.0.1",       # 仅本机，不对外
    port=3306,
    user="root",
    password="",
    database="greatminds",
    charset="utf8mb4",
)


class CompatCursor(pymysql.cursors.Cursor):
    """兼容 SQLite 语法的 Cursor（返回 tuple 行，与 sqlite3 默认一致）"""

    def execute(self, query, args=None):
        q = query.replace("INSERT OR IGNORE", "INSERT IGNORE") \
                 .replace("INSERT OR REPLACE", "REPLACE")
        # 仅当有参数时才替换占位符（无参查询保持原样）
        if args is not None:
            q = q.replace("?", "%s")
        return super().execute(q, args)

    def executemany(self, query, args):
        q = query.replace("INSERT OR IGNORE", "INSERT IGNORE") \
                 .replace("INSERT OR REPLACE", "REPLACE")
        return super().executemany(q, args)


class CompatDictCursor(pymysql.cursors.DictCursor):
    """兼容 SQLite 语法的 Cursor（返回 dict 行，等价 sqlite3.Row）"""

    def execute(self, query, args=None):
        q = query.replace("INSERT OR IGNORE", "INSERT IGNORE") \
                 .replace("INSERT OR REPLACE", "REPLACE")
        if args is not None:
            q = q.replace("?", "%s")
        return super().execute(q, args)


def get_conn():
    return pymysql.connect(cursorclass=CompatCursor, autocommit=False, **DB_CONFIG)
