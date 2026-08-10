#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验/灌入阿贝尔奖得主（Abel_Prize/abel_prize_laureates.md，2003–2026 共 29 人）。

数据源：
- 总表「年份 | 得主(可多人) | ...」：年份 + 共享关系
- 维基链接表「年份 | 得主 | <url>」：每人一行、官方拼写（权威名字）

逻辑（同 seed_fields_medal.py）：
- 已存在：补 Abel 获奖记录（若缺）
- 不存在：新增 people，has_biography=0，挂 mathematician 职业 + Abel 记录
"""
import re
import pymysql
from db_mysql import get_conn
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MD = ROOT.parent / "Abel_Prize" / "abel_prize_laureates.md"

# 名字别名：表名 -> 库中已有 name_en
ALIAS = {
    "Jean-Pierre Serre": "J.-P. Serre",
    "Mikhail Gromov": "Mikhail Gromov",
    "John F. Nash Jr.": "John F. Nash Jr.",
    "Gregory Margulis": "Grigory Margulis",   # Wikipedia 用 Gregory，库中用 Grigory
}

# 维基表：| 年份 | 得主 | <url> |
WIKI_RE = re.compile(
    r"^\|\s*(\d{4})\s*\|\s*([^|]+?)\s*\|\s*<(https?://[^>]+)>\s*\|"
)


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def tokens_norm(s: str) -> frozenset:
    s = unicodedata.normalize("NFKD", s)
    toks = {re.sub(r"[\W_]", "", t).lower() for t in s.split()}
    return frozenset(t for t in toks if t)


def parse_rows():
    """从维基链接表解析：[(year, name, url)]，29 人。"""
    rows = []
    in_wiki = False
    for line in MD.read_text(encoding="utf-8").splitlines():
        if line.startswith("## 维基百科链接"):
            in_wiki = True
            continue
        if in_wiki:
            m = WIKI_RE.match(line.strip())
            if m:
                rows.append({
                    "year": int(m.group(1)),
                    "name": m.group(2).strip(),
                    "url": m.group(3).strip(),
                })
    return rows


def main():
    rows = parse_rows()
    print(f"解析到阿贝尔奖得主: {len(rows)} 人")

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id FROM awards WHERE name_en='Abel Prize'")
    aid = cur.fetchone()[0]

    cur.execute("SELECT id, name_en, name_zh, wiki_url FROM people")
    people = [(pid, en, zh, url, norm(en or ""), norm(zh or ""), tokens_norm(en or ""))
              for pid, en, zh, url in cur.fetchall()]

    def find(name):
        n = norm(name)
        tn = tokens_norm(name)
        for pid, en, zh, url, ne, nz, tz in people:
            if ne == n or nz == n or (tn and tn == tz):
                return pid
        if name in ALIAS:
            an = norm(ALIAS[name])
            for pid, en, zh, url, ne, nz, tz in people:
                if ne == an:
                    return pid
        return None

    added_people = 0
    added_awards = 0
    existing = 0
    for r in rows:
        pid = find(r["name"])
        if pid is None:
            cur.execute(
                "INSERT INTO people(name_en, primary_occupation, has_biography, wiki_url) "
                "VALUES (?, 'mathematician', 0, ?)",
                (r["name"], r["url"]),
            )
            pid = cur.lastrowid
            cur.execute("INSERT OR IGNORE INTO person_occupation(person_id, occupation_id, `rank`) "
                        "SELECT ?, id, 0 FROM occupations WHERE name_en='mathematician'", (pid,))
            people.append((pid, r["name"], None, r["url"], norm(r["name"]), "", tokens_norm(r["name"])))
            added_people += 1
            print(f"  + 新增(未立传): {r['name']}（{r['year']}）")
        else:
            existing += 1
            # 回填 wiki_url（若缺失）
            cur.execute("UPDATE people SET wiki_url=COALESCE(wiki_url, ?) WHERE id=?", (r["url"], pid))

        cur.execute(
            "INSERT OR IGNORE INTO award_laureate(person_id, award_id, year, source) VALUES (?,?,?, 'Abel_Prize_laureates')",
            (pid, aid, r["year"]),
        )
        if cur.rowcount:
            added_awards += 1

    conn.commit()
    print(f"\n已存在: {existing} · 新增人物: {added_people} · 新增获奖: {added_awards}")
    cur.execute("SELECT COUNT(*) FROM people")
    print(f"people 总数: {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(*) FROM award_laureate")
    print(f"award_laureate 总数: {cur.fetchone()[0]}")
    conn.close()


if __name__ == "__main__":
    main()
