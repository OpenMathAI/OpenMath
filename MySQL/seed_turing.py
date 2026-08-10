#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验/灌入图灵奖得主（turing/turing_award_winners.md，1966–2025 共 81 人）。

总表格式：| 年份 | 得主 | 生卒 | 国籍 | 机构 | 成果 | 备注 |
- 已存在：补 Turing 获奖记录 + 挂 computer scientist 职业（若已有 mathematician 则保留主职）
- 不存在：新增 people，has_biography=0，挂 computer scientist 职业 + Turing 记录
"""
import re
import pymysql
from db_mysql import get_conn
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MD = ROOT.parent / "turing" / "turing_award_winners.md"

# 名字别名：表名 -> 库中已有 name_en
ALIAS = {
    "Alan J. Perlis": "Alan Perlis",
    "Andrew Yao": "Andrew Yao",
    "Tony Hoare": "Tony Hoare",
    "Ronald Rivest": "Ron Rivest",
    "Robert E. Kahn": "Robert Kahn",
    "Whitfield Diffie": "Whitfield Diffie",
    "Martin E. Hellman": "Martin Hellman",
    "David A. Patterson": "David Patterson",
    "Charles W. Bachman": "Charles Bachman",
    "Donald E. Knuth": "Donald Knuth",
    "Edsger W. Dijkstra": "Edsger W. Dijkstra",
    "Richard M. Karp": "Richard Karp",
    "John L. Hennessy": "John Hennessy",
    "Fred Brooks": "Fred Brooks",
}

ROW_RE = re.compile(
    r"^\|\s*(\d{4})\s*\|\s*(?P<name>[^|]+?)\s*\|"
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
    print(f"解析到图灵奖得主: {len(rows)} 人")

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id FROM awards WHERE name_en='ACM A.M. Turing Award'")
    aid = cur.fetchone()[0]
    # computer scientist 职业
    cur.execute("SELECT id FROM occupations WHERE name_en='computer scientist'")
    cs_occ = cur.fetchone()
    if not cs_occ:
        cur.execute("INSERT INTO occupations(name_en, name_zh) VALUES ('computer scientist','计算机科学家')")
        cs_occ = cur.lastrowid
    else:
        cs_occ = cs_occ[0]

    cur.execute("SELECT id, name_en, name_zh, primary_occupation FROM people")
    people = [(pid, en, zh, po, norm(en or ""), norm(zh or ""), tokens_norm(en or ""))
              for pid, en, zh, po in cur.fetchall()]

    def find(name):
        n = norm(name)
        tn = tokens_norm(name)
        for pid, en, zh, po, ne, nz, tz in people:
            if ne == n or nz == n or (tn and tn == tz):
                return pid
        if name in ALIAS:
            an = norm(ALIAS[name])
            for pid, en, zh, po, ne, nz, tz in people:
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
    existing = 0
    for r in rows:
        pid = find(r["name"])
        birth, death = parse_life(r["life"])
        if pid is None:
            cur.execute(
                "INSERT INTO people(name_en, primary_occupation, has_biography, birth_date, death_date) "
                "VALUES (?, 'computer scientist', 0, ?, ?)",
                (r["name"], birth, death),
            )
            pid = cur.lastrowid
            cur.execute("INSERT OR IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (?,?,0)",
                        (pid, cs_occ))
            people.append((pid, r["name"], None, "computer scientist", norm(r["name"]), "", tokens_norm(r["name"])))
            added_people += 1
            print(f"  + 新增(未立传): {r['name']}（{r['year']}）")
        else:
            existing += 1
            # 补生卒（若缺失）
            cur.execute("SELECT birth_date, death_date, primary_occupation FROM people WHERE id=?", (pid,))
            b0, d0, po0 = cur.fetchone()
            if birth and not b0:
                cur.execute("UPDATE people SET birth_date=? WHERE id=?", (birth, pid))
            if death and not d0:
                cur.execute("UPDATE people SET death_date=? WHERE id=?", (death, pid))
            # 挂 computer scientist 职业（追加，不覆盖原有主职）
            cur.execute("SELECT 1 FROM person_occupation WHERE person_id=? AND occupation_id=?",
                        (pid, cs_occ))
            if not cur.fetchone():
                # 追加为次职业（rank 取现有最大+1）
                cur.execute("SELECT COALESCE(MAX(`rank`),0)+1 FROM person_occupation WHERE person_id=?", (pid,))
                rk = cur.fetchone()[0]
                cur.execute("INSERT OR IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (?,?,?)",
                            (pid, cs_occ, rk))

        cur.execute(
            "INSERT OR IGNORE INTO award_laureate(person_id, award_id, year, source) VALUES (?,?,?, 'Turing_award_winners')",
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
