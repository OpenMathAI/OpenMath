#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验/灌入菲尔兹奖得主（Fields_Medal/fields_medal_winners.md，1936–2026 共 68 位）。

逻辑：
- 解析得主表（年份 + 姓名 + 生卒 + 国籍 + 机构）
- 已存在于 people：补 Fields Medal 获奖记录（若缺）
- 不存在：新增 people，has_biography=0（未立传），挂 mathematician 职业 + Fields 获奖记录
"""
import re
import sqlite3
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DB = ROOT / "greatminds.db"
MD = ROOT.parent / "Fields_Medal" / "fields_medal_winners.md"

# 名字别名：md 表名 -> 库中已有 name_en（归一化无法对齐时用）
ALIAS = {
    "Jean-Pierre Serre": "J.-P. Serre",
    "Kunihiko Kodaira": "Kodaira Kunihiko",
    "René Thom": "René Thom",
    "Lars Hörmander": "Lars Hörmander",
    "Rene Thom": "René Thom",
    "Lars Hormander": "Lars Hörmander",
}

ROW_RE = re.compile(
    r"^\|\s*(\d{4})\s*\|\s*[^|]*?\s*\|\s*(?P<name>[^|]+?)\s*\|"
    r"\s*(?P<life>[^|]*?)\s*\|"
    r"\s*(?P<nat>[^|]*?)\s*\|"
    r"\s*(?P<inst>[^|]*?)\s*\|"
)


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def tokens_norm(s: str) -> frozenset:
    """无序 token 集合（处理 'Kunihiko Kodaira' vs 'Kodaira Kunihiko'）"""
    s = unicodedata.normalize("NFKD", s)
    toks = {re.sub(r"[\W_]", "", t).lower() for t in s.split()}
    return frozenset(t for t in toks if t)


def parse_rows():
    rows = []
    for line in MD.read_text(encoding="utf-8").splitlines():
        m = ROW_RE.match(line)
        if not m:
            continue
        name = m.group("name").strip()
        if not name:
            continue
        rows.append({
            "year": int(m.group(1)),
            "name": name,
            "life": m.group("life").strip(),
            "nat": m.group("nat").strip(),
            "inst": m.group("inst").strip(),
        })
    return rows


def main():
    rows = parse_rows()
    print(f"解析到菲尔兹奖得主: {len(rows)} 人")

    conn = sqlite3.connect(DB)
    conn.execute("PRAGMA foreign_keys = ON")
    cur = conn.cursor()

    cur.execute("SELECT id FROM awards WHERE name_en='Fields Medal'")
    aid = cur.fetchone()
    if not aid:
        cur.execute("INSERT INTO awards(name_en,name_zh,award_type,tier) VALUES ('Fields Medal','菲尔兹奖','math_top',1)")
        aid = cur.lastrowid
    else:
        aid = aid[0]

    # 载入 people 索引
    cur.execute("SELECT id, name_en, name_zh FROM people")
    people = [(pid, en, zh, norm(en or ""), norm(zh or ""), tokens_norm(en or "")) for pid, en, zh in cur.fetchall()]

    def find(name):
        n = norm(name)
        tn = tokens_norm(name)
        for pid, en, zh, ne, nz, tz in people:
            if ne == n or nz == n or (tn and tn == tz):
                return pid
        if name in ALIAS:
            an = norm(ALIAS[name])
            for pid, en, zh, ne, nz, tz in people:
                if ne == an:
                    return pid
        return None

    # 解析生卒
    def parse_life(life):
        m = re.match(r"^(\d{4})-(\d{4}|)$", life)
        if m:
            return m.group(1), m.group(2) or None
        return None, None

    added_people = 0
    added_awards = 0
    existing = 0
    for r in rows:
        pid = find(r["name"])
        birth, death = parse_life(r["life"])
        if pid is None:
            cur.execute(
                "INSERT INTO people(name_en, primary_occupation, has_biography, birth_date, death_date) "
                "VALUES (?, 'mathematician', 0, ?, ?)",
                (r["name"], birth, death),
            )
            pid = cur.lastrowid
            cur.execute("INSERT OR IGNORE INTO person_occupation(person_id, occupation_id, rank) "
                        "SELECT ?, id, 0 FROM occupations WHERE name_en='mathematician'", (pid,))
            people.append((pid, r["name"], None, norm(r["name"]), "", tokens_norm(r["name"])))
            added_people += 1
            print(f"  + 新增(未立传): {r['name']}（{r['year']}）")
        else:
            existing += 1
            # 补全生卒（若缺失）
            cur.execute("SELECT birth_date, death_date FROM people WHERE id=?", (pid,))
            b0, d0 = cur.fetchone()
            if birth and not b0:
                cur.execute("UPDATE people SET birth_date=? WHERE id=?", (birth, pid))
            if death and not d0:
                cur.execute("UPDATE people SET death_date=? WHERE id=?", (death, pid))

        # 奖项记录
        cur.execute(
            "INSERT OR IGNORE INTO award_laureate(person_id, award_id, year, source) VALUES (?,?,?, 'Fields_Medal_winners')",
            (pid, aid, r["year"]),
        )
        if cur.rowcount:
            added_awards += 1

    conn.commit()
    print(f"\n已存在: {existing} · 新增人物: {added_people} · 新增获奖记录: {added_awards}")
    cur.execute("SELECT COUNT(*) FROM people")
    print(f"people 总数: {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(*) FROM award_laureate")
    print(f"award_laureate 总数: {cur.fetchone()[0]}")
    conn.close()


if __name__ == "__main__":
    main()
