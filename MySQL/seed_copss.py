#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""校验/灌入 COPSS 会长奖得主（COPSS/copss_winners.md，1981–2026 共 46 人）。

总表格式：| 年份 | 得主 | 生卒年 | 机构 | 研究方向 | 备注 |
- 华人得主（9 位）补充中文名（name_zh）
- occupation = statistician（统计学家）
- 已存在：补 COPSS 记录；不存在：新增 has_biography=0
"""
import re
import pymysql
from db_mysql import get_conn
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent
MD = ROOT.parent / "COPSS" / "copss_winners.md"

# 华人得主：英文名 -> 中文名
CN_NAMES = {
    "Tze Leung Lai": "黎子良",
    "Wing Hung Wong": "黄永康",
    "Jianqing Fan": "范剑青",
    "Xiao-Li Meng": "孟晓犁",
    "Jun Liu": "刘军",
    "Xihong Lin": "林希虹",
    "T. Tony Cai": "蔡天文",
    "Samuel Kou": "寇星昌",
    "Weijie Su": "苏炜杰",
}

# 只匹配「历届得主总表」：| 年份 | 得主 | 生卒年(如 1940- / -) | 机构 | ... |
ROW_RE = re.compile(
    r"^\|\s*(\d{4})\s*\|\s*(?P<name>[^|]+?)\s*\|"
    r"\s*(?P<life>\d{4}-(?:\d{4})?|-)\s*\|"
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
        if not name or name == "—":
            continue
        life = m.group("life").strip()
        rows.append({
            "year": int(m.group(1)),
            "name": name,
            "life": life,
            "inst": m.group("inst").strip(),
            "zh": CN_NAMES.get(name),
        })
    return rows


def main():
    rows = parse_rows()
    print(f"解析到 COPSS 得主: {len(rows)} 人")

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id FROM awards WHERE name_en='COPSS Presidents'' Award'")
    aid = cur.fetchone()[0]
    cur.execute("SELECT id FROM occupations WHERE name_en='statistician'")
    occ = cur.fetchone()
    if not occ:
        cur.execute("INSERT INTO occupations(name_en, name_zh) VALUES ('statistician','统计学家')")
        occ = cur.lastrowid
    else:
        occ = occ[0]

    cur.execute("SELECT id, name_en, name_zh FROM people")
    people = [(pid, en, zh, norm(en or ""), norm(zh or ""), tokens_norm(en or ""))
              for pid, en, zh in cur.fetchall()]

    def find(name):
        n = norm(name)
        tn = tokens_norm(name)
        for pid, en, zh, ne, nz, tz in people:
            if ne == n or nz == n or (tn and tn == tz):
                return pid
        return None

    def parse_life(life):
        m = re.match(r"^(\d{4})-(\d{4}|)$", life)
        if m:
            return m.group(1), m.group(2) or None
        return None, None  # "-" 表示未知

    added_people = 0
    added_awards = 0
    existing = 0
    for r in rows:
        pid = find(r["name"])
        birth, death = parse_life(r["life"])
        if pid is None:
            cur.execute(
                "INSERT INTO people(name_en, name_zh, primary_occupation, has_biography, birth_date, death_date) "
                "VALUES (?,?, 'statistician', 0, ?, ?)",
                (r["name"], r["zh"], birth, death),
            )
            pid = cur.lastrowid
            cur.execute("INSERT OR IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (?,?,0)",
                        (pid, occ))
            people.append((pid, r["name"], r["zh"], norm(r["name"]), norm(r["zh"] or ""), tokens_norm(r["name"])))
            added_people += 1
            print(f"  + 新增(未立传): {r['name']}{'（' + r['zh'] + '）' if r['zh'] else ''}（{r['year']}）")
        else:
            existing += 1
            cur.execute("SELECT birth_date, death_date, name_zh FROM people WHERE id=?", (pid,))
            b0, d0, zh0 = cur.fetchone()
            if birth and not b0:
                cur.execute("UPDATE people SET birth_date=? WHERE id=?", (birth, pid))
            if death and not d0:
                cur.execute("UPDATE people SET death_date=? WHERE id=?", (death, pid))
            if r["zh"] and not zh0:
                cur.execute("UPDATE people SET name_zh=? WHERE id=?", (r["zh"], pid))
            # 追加 statistician 职业
            cur.execute("SELECT 1 FROM person_occupation WHERE person_id=? AND occupation_id=?", (pid, occ))
            if not cur.fetchone():
                cur.execute("SELECT COALESCE(MAX(`rank`),0)+1 FROM person_occupation WHERE person_id=?", (pid,))
                rk = cur.fetchone()[0]
                cur.execute("INSERT OR IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (?,?,?)",
                            (pid, occ, rk))

        cur.execute(
            "INSERT OR IGNORE INTO award_laureate(person_id, award_id, year, source) VALUES (?,?,?, 'COPSS_winners')",
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
