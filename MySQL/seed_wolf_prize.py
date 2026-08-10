#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验/灌入沃尔夫数学奖得主（Wolf_Prize/wolf_prize_winners.md，1978–2024 共 68 位）。

逻辑（同 seed_fields_medal.py）：
- 解析得主表（年份 + 姓名 + 生卒 + 国籍 + 机构），跳过「—」未颁发行
- 已存在于 people：补 Wolf 获奖记录（若缺）；年份以本表为准（覆盖排名来源的旧年份）
- 不存在：新增 people，has_biography=0（未立传），挂 mathematician 职业 + Wolf 获奖记录
"""
import re
import pymysql
from db_mysql import get_conn
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MD = ROOT.parent / "Wolf_Prize" / "wolf_prize_winners.md"

# 名字别名：表名 -> 库中已有 name_en（归一化无法对齐时用）
ALIAS = {
    "Israel Gelfand": "I.M. Gelfand",
    "Shiing-Shen Chern": "陈省身",
    "Kunihiko Kodaira": "Kodaira Kunihiko",
    "Mikio Sato": "Sato Mikio",
    "Shing-Tung Yau": "Shing-Tung Yau",
    "Jean-Pierre Serre": "J.-P. Serre",
    "René Thom": "René Thom",
    "Rene Thom": "René Thom",
}

ROW_RE = re.compile(
    r"^\|\s*(?P<year>\d{4}(?:/\d{2,4})?)\s*\|\s*(?P<name>[^|]+?)\s*\|"
    r"\s*(?P<life>[^|]*?)\s*\|"
    r"\s*(?P<nat>[^|]*?)\s*\|"
    r"\s*(?P<inst>[^|]*?)\s*\|"
)


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def tokens_norm(s: str) -> frozenset:
    s = unicodedata.normalize("NFKD", s)
    toks = {re.sub(r"[\W_]", "", t).lower() for t in s.split()}
    return frozenset(t for t in toks if t)


def clean_name(raw: str) -> str:
    """去掉括号注释：'Shiing-Shen Chern (陈省身)' -> 'Shiing-Shen Chern'"""
    m = re.search(r"\((.*?)\)", raw)
    if m:
        return raw[: m.start()].strip()
    return raw.strip()


def parse_rows():
    rows = []
    for line in MD.read_text(encoding="utf-8").splitlines():
        m = ROW_RE.match(line)
        if not m:
            continue
        name = clean_name(m.group("name"))
        if not name or name == "—":
            continue  # 未颁发行
        y = m.group("year")
        year = int(y.split("/")[0])  # 1996/97 -> 1996
        rows.append({
            "year": year,
            "raw_year": m.group("year"),
            "name": name,
            "life": m.group("life").strip(),
            "nat": m.group("nat").strip(),
            "inst": m.group("inst").strip(),
        })
    return rows


def main():
    rows = parse_rows()
    print(f"解析到沃尔夫奖得主: {len(rows)} 人")

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id FROM awards WHERE name_en='Wolf Prize in Mathematics'")
    aid = cur.fetchone()[0]

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

    def parse_life(life):
        m = re.match(r"^(\d{4})-(\d{4}|)$", life)
        if m:
            return m.group(1), m.group(2) or None
        return None, None

    added_people = 0
    added_awards = 0
    updated_awards = 0
    existing = 0
    valid_pids = set()
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
            cur.execute("INSERT OR IGNORE INTO person_occupation(person_id, occupation_id, `rank`) "
                        "SELECT ?, id, 0 FROM occupations WHERE name_en='mathematician'", (pid,))
            people.append((pid, r["name"], None, norm(r["name"]), "", tokens_norm(r["name"])))
            added_people += 1
            print(f"  + 新增(未立传): {r['name']}（{r['raw_year']}）")
        else:
            existing += 1
            cur.execute("SELECT birth_date, death_date FROM people WHERE id=?", (pid,))
            b0, d0 = cur.fetchone()
            if birth and not b0:
                cur.execute("UPDATE people SET birth_date=? WHERE id=?", (birth, pid))
            if death and not d0:
                cur.execute("UPDATE people SET death_date=? WHERE id=?", (death, pid))

        # Wolf 获奖记录：无则插入，有则年份对齐本表（权威来源）
        cur.execute("SELECT year FROM award_laureate WHERE person_id=? AND award_id=?", (pid, aid))
        row = cur.fetchone()
        if row is None:
            cur.execute(
                "INSERT INTO award_laureate(person_id, award_id, year, source) VALUES (?,?,?, 'Wolf_Prize_winners')",
                (pid, aid, r["year"]),
            )
            added_awards += 1
        elif row[0] != r["year"]:
            cur.execute("UPDATE award_laureate SET year=?, source='Wolf_Prize_winners' WHERE person_id=? AND award_id=?",
                        (r["year"], pid, aid))
            updated_awards += 1
            print(f"  ~ 年份修正: {r['name']} Wolf {row[0]} -> {r['year']}")
        valid_pids.add(pid)

    conn.commit()
    # 清理：Wolf 记录中 person_id 不属于 Wolf 表 68 人的（如排名来源误标的 Lefschetz 1978）
    removed = 0
    cur.execute("""
        SELECT al.person_id, p.name_en FROM award_laureate al
        JOIN people p ON p.id=al.person_id
        WHERE al.award_id=?
    """, (aid,))
    for pid, nm in cur.fetchall():
        if pid not in valid_pids:
            cur.execute("DELETE FROM award_laureate WHERE person_id=? AND award_id=?", (pid, aid))
            removed += 1
            print(f"  ~ 清理错误 Wolf 记录: {nm}")
    conn.commit()
    print(f"\n已存在: {existing} · 新增人物: {added_people} · 新增获奖: {added_awards} · 年份修正: {updated_awards} · 清理错误: {removed}")
    cur.execute("SELECT COUNT(*) FROM people")
    print(f"people 总数: {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(*) FROM award_laureate")
    print(f"award_laureate 总数: {cur.fetchone()[0]}")
    conn.close()


if __name__ == "__main__":
    main()
