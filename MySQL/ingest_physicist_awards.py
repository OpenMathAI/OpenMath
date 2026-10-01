#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从物理学家 page.md 的 infobox Awards 行解析「奖项 (年份)」对，
get_or_create 进 awards 表并写入 award_laureate（幂等，INSERT IGNORE）。

数据源：20 世纪 161 人 + 21 世纪 68 人的 page.md（manifest 的 QID 定位 person_id）。
年份取不到的奖项按 year=NULL 入库（仍可查"得过什么奖"）。
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from db_mysql import get_conn

OM = Path("/Users/ericksun/workspace/codebuddy/OpenMathAI")
P20 = OM / "physicist" / "presentations" / "20th_century" / "20th_century"
P21 = OM / "physicist" / "presentations" / "21th_century" / "21st_century"

conn = get_conn()
cur = conn.cursor()


def get_or_create_award(name_en):
    cur.execute("SELECT id FROM awards WHERE name_en=%s", (name_en,))
    r = cur.fetchone()
    if r:
        return r[0], False
    cur.execute("INSERT INTO awards (name_en, name_zh, award_type) VALUES (%s,%s,'award')",
                (name_en, name_en))
    return cur.lastrowid, True


def parse_awards(text):
    """从 Awards 单元格提取 (award_name, year or None)。链接形式 + 纯文本形式。"""
    out = []
    spans = []
    # 链接形式：[Name](url "title") 可选紧跟 (YYYY) 或 (YYYY/YY、1994/5)
    for m in re.finditer(
        r"\[([^\]]+)\]\([^)]*\)\s*(?:\((\d{4}(?:\s*[–/-]\s*\d{2,4})?)\))?", text
    ):
        name = m.group(1).strip()
        year = m.group(2)
        if name and len(name) < 120:
            out.append((name, year))
            spans.append((m.start(), m.end()))
    # 纯文本形式：非链接区域内的 Name (YYYY)（如 "Nobel Prize (2018)"）
    def in_link(pos):
        return any(s <= pos < e for s, e in spans)
    for m in re.finditer(r"([A-Z][A-Za-z'’ .·-]{2,80}?)\s*\((\d{4})\)", text):
        if in_link(m.start()):
            continue
        name = m.group(1).strip().rstrip("-– ")
        if name and len(name) > 3 and not name.lower().startswith(("born", "died")):
            out.append((name, m.group(2)))
    return out


def person_id_by_qid(qid, fallback_name):
    cur.execute("SELECT id FROM people WHERE qid=%s", (qid,))
    r = cur.fetchone()
    if r:
        return r[0]
    cur.execute("SELECT id FROM people WHERE name_en=%s", (fallback_name,))
    r = cur.fetchone()
    return r[0] if r else None


def norm_year(y):
    if not y:
        return None
    m = re.match(r"(\d{4})", y.replace("–", "-"))
    return int(m.group(1)) if m else None


def process(manifest_path, pages_root):
    man = json.loads(Path(manifest_path).read_text(encoding="utf-8"))
    stats = dict(persons=0, awards_new=0, rows_inserted=0, rows_skip=0, no_awards=[])
    for p in man["people"]:
        pid = person_id_by_qid(p["qid"], p["name_en"])
        if not pid:
            stats["no_awards"].append((p["name_en"], "person not found"))
            continue
        page = pages_root / p["dir"] / "page.md"
        if not page.exists():
            stats["no_awards"].append((p["name_en"], "page.md missing"))
            continue
        text = page.read_text(encoding="utf-8")
        # 取 infobox 的 Awards 行（| Awards | ... |，可能跨行直到下一个 |** 或表格结束）
        m = re.search(r"\|\s*Awards\s*\|(.*?)(?=\n\||\n\n)", text, re.S)
        cell = m.group(1) if m else ""
        pairs = parse_awards(cell)
        if not pairs:
            stats["no_awards"].append((p["name_en"], "no awards parsed"))
            continue
        stats["persons"] += 1
        for name, year in pairs:
            aid, created = get_or_create_award(name)
            stats["awards_new"] += int(created)
            y = norm_year(year)
            cur.execute(
                "SELECT COUNT(*) FROM award_laureate WHERE person_id=%s AND award_id=%s "
                "AND ((year=%s) OR (year IS NULL AND %s IS NULL))",
                (pid, aid, y, y),
            )
            if cur.fetchone()[0]:
                stats["rows_skip"] += 1
                continue
            cur.execute(
                "INSERT IGNORE INTO award_laureate (person_id, award_id, year, source) "
                "VALUES (%s,%s,%s,'page_infobox')",
                (pid, aid, y),
            )
            stats["rows_inserted"] += 1
        conn.commit()
    return stats


s20 = process(OM / "physicist" / "prompt_manifest.json", P20)
s21 = process(OM / "physicist" / "prompt_manifest_21st.json", P21)
print("20th:", s20)
print("21st:", s21)

cur.execute("SELECT COUNT(*) FROM award_laureate")
print("award_laureate total:", cur.fetchone()[0])
cur.execute("SELECT COUNT(DISTINCT person_id) FROM award_laureate")
print("distinct persons:", cur.fetchone()[0])
