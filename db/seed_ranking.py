#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""灌入 20 世纪数学巨匠排名（mathematician/figures/OpenMath_20th_Century_Comprehensive_Ranking.md）
到 greatminds.db：people + rankings + 奖项关联（award_laureate）。

奖项名映射到 awards 字典表；奖项缺失时自动补入 awards 表（award_type=math_top 或 honor）。
"""
import re
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DB = ROOT / "greatminds.db"
MD = ROOT.parent / "mathematician" / "figures" / "OpenMath_20th_Century_Comprehensive_Ranking.md"

# 排名文件中奖项缩写 -> awards.name_en（标准名）
AWARD_MAP = {
    "Fields": "Fields Medal",
    "Wolf": "Wolf Prize in Mathematics",
    "Abel": "Abel Prize",
    "Chern Medal": "Chern Medal",
    "诺贝尔文学奖": "Nobel Prize in Literature",
}

ROW_RE = re.compile(
    r"^\|\s*(\d+)\s*\|\s*(\d+|无)\s*\|\s*(?P<name>.+?)\s*\|"
    r"\s*(?P<awards>[^|]*?)\s*\|"
    r"\s*(?P<tag>[^|]*?)\s*\|"
    r"\s*(?P<bio>[^|]*?)\s*\|"
    r"\s*(?P<review>[^|]*?)\s*\|"
)

# 名称中括号里的罗马音/中文注释
PAREN_RE = re.compile(r"\((.*?)\)")
CJK_RE = re.compile(r"[\u4e00-\u9fff]")


def split_name(field: str):
    """'**高木贞治** (Takagi Teiji)' -> (name_zh='高木贞治', name_en='Takagi Teiji')
    '**I.M. Gelfand** (盖尔范德)'   -> (name_zh='盖尔范德', name_en='I.M. Gelfand')
    '**David Hilbert**'             -> (name_zh=None, name_en='David Hilbert')"""
    m = PAREN_RE.search(field)
    core = field[: m.start()].strip() if m else field.strip()
    core = core.strip("*").strip()
    extra = m.group(1).strip() if m else ""
    if CJK_RE.search(core):
        return core, extra or None          # 中文名为主，括号是英文
    return extra or None, core              # 英文名为主，括号是中文


def parse_award_cell(text: str):
    """'Fields 1954 · Wolf 2000 · Abel 2003' -> [('Fields Medal', 1954), ...]"""
    out = []
    text = text.strip()
    if not text or text == "—":
        return out
    for part in re.split(r"[·;；,]", text):
        part = part.strip()
        if not part:
            continue
        m = re.match(r"^(.*?)(\d{4})\s*$", part)
        if not m:
            continue
        key, year = m.group(1).strip(), int(m.group(2))
        full = AWARD_MAP.get(key)
        if full:
            out.append((full, year))
    return out


def parse_md():
    rows = []
    current_list = None
    for line in MD.read_text(encoding="utf-8").splitlines():
        if "Top 50" in line or line.startswith("## 二"):
            current_list = "OpenMath_20th_Century_Top50"
            continue
        if "未进入本榜前 50" in line or "重排" in line or line.startswith("## 补"):
            current_list = "OpenMath_20th_Century_51_108"
            continue
        m = ROW_RE.match(line)
        if not m:
            continue
        rank = int(m.group(1))
        orig = None if m.group(2) == "无" else int(m.group(2))
        name_zh, name_en = split_name(m.group("name"))
        awards = parse_award_cell(m.group("awards"))
        rows.append({
            "list": current_list, "rank": rank, "orig": orig,
            "name_zh": name_zh, "name_en": name_en,
            "awards": awards,
            "tag": m.group("tag").strip(),
            "bio": m.group("bio").strip(),
            "review": m.group("review").strip(),
        })
    return rows


def main():
    rows = parse_md()
    print(f"解析到 {len(rows)} 位数学家")
    conn = sqlite3.connect(DB)
    conn.execute("PRAGMA foreign_keys = ON")
    cur = conn.cursor()

    # 确保 occupation: mathematician 存在
    cur.execute("SELECT id FROM occupations WHERE name_en='mathematician'")
    occ_id = cur.fetchone()
    if not occ_id:
        cur.execute("INSERT INTO occupations(name_en, name_zh) VALUES ('mathematician','数学家')")
        occ_id = cur.lastrowid
    else:
        occ_id = occ_id[0]

    inserted = updated = 0
    award_created = 0
    for r in rows:
        # upsert people（以 name_en 为唯一键；中文名优先取中文）
        en, zh = r["name_en"], r["name_zh"]
        if not en and zh:
            en = zh  # 纯中文名兜底
        cur.execute("SELECT id FROM people WHERE name_en=?", (en,))
        pid = cur.fetchone()
        if pid:
            pid = pid[0]
            cur.execute("UPDATE people SET name_zh=COALESCE(?, name_zh) WHERE id=?", (zh, pid))
            updated += 1
        else:
            cur.execute(
                "INSERT INTO people(name_en, name_zh, primary_occupation) VALUES (?,?, 'mathematician')",
                (en, zh),
            )
            pid = cur.lastrowid
            inserted += 1

        # occupation 关联
        cur.execute("INSERT OR IGNORE INTO person_occupation(person_id, occupation_id, rank) VALUES (?,?,0)",
                    (pid, occ_id))

        # ranking
        if r["list"]:
            cur.execute(
                "INSERT OR REPLACE INTO rankings(person_id, list_key, rank, orig_rank, tag, status) VALUES (?,?,?,?,?,?)",
                (pid, r["list"], r["rank"], r["orig"], r["tag"], f"{r['bio']}/{r['review']}"),
            )

        # awards
        for full, year in r["awards"]:
            cur.execute("SELECT id FROM awards WHERE name_en=?", (full,))
            aid = cur.fetchone()
            if not aid:
                cur.execute(
                    "INSERT INTO awards(name_en, name_zh, award_type, tier) VALUES (?,?, 'math_top', NULL)",
                    (full, full),
                )
                aid = cur.lastrowid
                award_created += 1
            else:
                aid = aid[0]
            cur.execute(
                "INSERT OR IGNORE INTO award_laureate(person_id, award_id, year, source) VALUES (?,?,?, 'OpenMath_20th_Century_Ranking')",
                (pid, aid, year),
            )

    conn.commit()
    print(f"新增 people: {inserted} · 更新: {updated} · 补建 awards: {award_created}")
    cur.execute("SELECT COUNT(*) FROM people")
    print(f"people 总数: {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(*) FROM award_laureate")
    print(f"award_laureate 总数: {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(*) FROM rankings")
    print(f"rankings 总数: {cur.fetchone()[0]}")
    conn.close()


if __name__ == "__main__":
    main()
