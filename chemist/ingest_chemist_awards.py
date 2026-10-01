#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从化学家 page.md 的 infobox Awards 行解析「奖项 (年份)」对，
get_or_create 进 awards 表并写入 award_laureate（幂等）。

对齐 MySQL/ingest_physicist_awards.py 的先例（Marie Curie 1911 即该脚本所入）：
- 年份取不到的按 year=NULL 入库（仍可查"得过什么奖"）；
- source='page_infobox'；
- 仅滤除 honorary doctorate 类学位条目（非奖项）。
数据源：chemist/prompt_manifest{,_21}.json 的 batches[].people[]（dir/db_qid/db_name_en
定位 page.md 与 person_id），pages 根为 presentations/{20th,21th}_century/pages。
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "MySQL"))
from db_mysql import get_conn  # noqa: E402

OM = Path(__file__).resolve().parent.parent
PAGES_ROOTS = [
    (OM / "chemist" / "prompt_manifest.json", OM / "chemist" / "presentations" / "20th_century" / "pages"),
    (OM / "chemist" / "prompt_manifest_21.json", OM / "chemist" / "presentations" / "21th_century" / "pages"),
]

NOISE_PAT = re.compile(r"honorary doctor|honoris causa", re.I)
# 解析碎片：infobox 里「XX Prize in Nanoscience (2018)」类链接拆开后剩下的裸字段词
FRAGMENTS = {
    "Chemistry", "Medicine", "Nanoscience", "Biopharmaceutical Science",
    "Award", "Science Award", "TED", "TÜBİTAK", "Class",
}
# 解析垃圾：陨石坑/人名/爵位缩写等（曾入库已删，加黑名单防复建）
JUNK = {"Soddy crater", "Jerome Karle", "Knighted", "OM", "IEEE"}
# 奖项名归一：infobox 变体写法 → 库内规范名
CANONICAL = {
    "Nobel Prize for Chemistry": "Nobel Prize in Chemistry",
    "Nobel Prize": "Nobel Prize in Chemistry",
}

# manifest db_name_en → 库内规范名（people.name_en）
ALIAS = {
    "Dorothy Hodgkin": "Dorothy Crowfoot Hodgkin",
    "Alan MacDiarmid": "Alan G. MacDiarmid",
}

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
    for m in re.finditer(
        r"\[([^\]]+)\]\([^)]*\)\s*(?:\((\d{4}(?:\s*[–/-]\s*\d{2,4})?)\))?", text
    ):
        name = m.group(1).strip()
        year = m.group(2)
        if name and len(name) < 120:
            out.append((name, year))
            spans.append((m.start(), m.end()))

    def in_link(pos):
        return any(s <= pos < e for s, e in spans)

    for m in re.finditer(r"([A-Z][A-Za-z'’ .·-]{2,80}?)\s*\((\d{4})\)", text):
        if in_link(m.start()):
            continue
        name = m.group(1).strip().rstrip("-– ")
        if name and len(name) > 3 and not name.lower().startswith(("born", "died")):
            out.append((name, m.group(2)))
    return out


def person_id(qid, name_en):
    if qid:
        cur.execute("SELECT id FROM people WHERE qid=%s", (qid,))
        r = cur.fetchone()
        if r:
            return r[0]
    cur.execute("SELECT id FROM people WHERE name_en=%s", (name_en,))
    r = cur.fetchone()
    return r[0] if r else None


def norm_year(y):
    """取不到年份返回 0（award_laureate.year 是 NOT NULL，NULL 会被 INSERT IGNORE 静默丢弃；
    库内已有 year=0 先例，如早年 NAS 行）。"""
    if not y:
        return 0
    m = re.match(r"(\d{4})", y.replace("–", "-"))
    return int(m.group(1)) if m else 0


def flatten(manifest_path):
    man = json.loads(Path(manifest_path).read_text(encoding="utf-8"))
    if "people" in man:
        return man["people"]
    people = []
    for b in man.get("batches", []):
        people.extend(b.get("people", []))
    return people


def process(manifest_path, pages_root):
    stats = dict(persons=0, awards_new=0, rows_inserted=0, rows_skip=0, no_awards=[])
    for p in flatten(manifest_path):
        db_name = p.get("db_name_en") or p.get("name")
        db_name = ALIAS.get(db_name, db_name)
        pid = person_id(p.get("db_qid"), db_name)
        if not pid:
            stats["no_awards"].append((db_name, "person not found"))
            continue
        page = pages_root / p["dir"] / "page.md"
        if not page.exists():
            stats["no_awards"].append((db_name, f"page.md missing: {page.name}"))
            continue
        text = page.read_text(encoding="utf-8")
        m = re.search(r"\|\s*Awards\s*\|(.*?)(?=\n\||\n\n)", text, re.S)
        cell = m.group(1) if m else ""
        pairs = []
        for n, y in parse_awards(cell):
            if NOISE_PAT.search(n) or n in FRAGMENTS or n in JUNK:
                continue
            pairs.append((CANONICAL.get(n, n), y))
        if not pairs:
            stats["no_awards"].append((db_name, "no awards parsed"))
            continue
        stats["persons"] += 1
        for name, year in pairs:
            aid, created = get_or_create_award(name)
            stats["awards_new"] += int(created)
            y = norm_year(year)
            if name in CANONICAL.values():
                # 归一奖项（如 infobox 只写 "Nobel Prize"）按人去重，防 year=0 冗余行
                cur.execute(
                    "SELECT COUNT(*) FROM award_laureate WHERE person_id=%s AND award_id=%s",
                    (pid, aid),
                )
            else:
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
            if cur.rowcount:
                stats["rows_inserted"] += 1
            else:
                stats["rows_ignored"] = stats.get("rows_ignored", 0) + 1
        conn.commit()
    return stats


for man_path, root in PAGES_ROOTS:
    s = process(man_path, root)
    print(root.parent.name, ":", s)

cur.execute("SELECT COUNT(*) FROM award_laureate WHERE source='page_infobox'")
print("page_infobox rows total:", cur.fetchone()[0])
