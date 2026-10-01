#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""通用版：从诺奖得主 page.md 的 infobox Awards 行解析「奖项 (年份)」对，
get_or_create 进 awards 表并写入 award_laureate（幂等）。

对齐 chemist/ingest_chemist_awards.py 的全部经验：
- year 取不到落 0（award_laureate.year NOT NULL，NULL 会被 INSERT IGNORE 静默丢弃）；
- FRAGMENTS/JUNK/CANONICAL 三级过滤，归一奖项按人去重；
- source='page_infobox'。

用法：python3 ingest_laureate_awards.py [medicine|literature|economics|peace]
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from db_mysql import get_conn  # noqa: E402

OM = Path(__file__).resolve().parent.parent

NOISE_PAT = re.compile(r"honorary doctor|honoris causa", re.I)
FRAGMENTS = {
    "Chemistry", "Medicine", "Physiology or Medicine", "Physics",
    "Physiology", "Literature", "Economic Sciences", "Peace",
    "Nanoscience", "Biopharmaceutical Science",
    "Award", "Science Award", "TED", "TÜBİTAK", "Class",
}
JUNK = {
    "Soddy crater", "Jerome Karle", "Knighted", "OM", "IEEE",
    # 医学/文学/经济/和平侧实抓发现的碎片与误配
    "posthumous", "below", "list", "several others", "AC", "FAA", "APA",
    "China", "Biology", "Biotechnology", "FRS (2020)", "2003", "2022",
    "Winifred Holtby", "A Pale View of Hills", "Pico Mirandola",
    "Knight Grand Cross", "University of Louisville", "Bocconi University",
    "American Philosophical Society", "Pontifical Academy of Sciences",
    "Lifetime Achievement Award",
}
# 末尾带括号年份的残片（如 "FRS (2020)"、"Nobel Prize in Literature (1971)"）
TRAILING_YEAR_PAT = re.compile(r"\s*\(\d{4}\)\s*$")
# 纯年份/QID 形奖项名（解析碎片）
DEGENERATE_PAT = re.compile(r"^(Q\d+|\d{4})$")

NOBEL_MED = "Nobel Prize in Physiology or Medicine"
NOBEL_LIT = "Nobel Prize in Literature"
NOBEL_ECO = "Nobel Memorial Prize in Economic Sciences"
NOBEL_PEA = "Nobel Peace Prize"

PROJECTS = {
    "medicine": dict(
        manifests=[
            ("medic/prompt_manifest_20th.json", "batches", "people", "name_en",
             "medic/presentations/pages/20th_century"),
            ("medic/prompt_manifest_21th.json", "batches", "people", "name_en",
             "medic/presentations/pages/21th_century"),
        ],
        alias={},
        canonical={"Nobel Prize": NOBEL_MED,
                   "Nobel Prize for Physiology or Medicine": NOBEL_MED,
                   "Nobel Prize in Medicine": NOBEL_MED},
    ),
    "literature": dict(
        manifests=[
            ("literature/prompt_batches_lit.json", "batches", "members", "name",
             "literature/presentations/pages/20th_century"),
            ("literature/prompt_batches_lit_21st.json", "batches", "members", "name",
             "literature/presentations/pages/21st_century"),
        ],
        alias={"Paul von Heyse": "Paul Heyse"},
        canonical={"Nobel Prize": NOBEL_LIT,
                   "Nobel Prize for Literature": NOBEL_LIT},
    ),
    "economics": dict(
        manifests=[
            ("economics/prompt_manifest_20th.json", "batches", "people", "name",
             "economics/presentations/pages/20th_century"),
            ("economics/prompt_manifest_21th.json", "batches", "people", "name",
             "economics/presentations/pages/21th_century"),
        ],
        alias={
            "Alvin E. Roth": "Alvin Eliot Roth",
            "Gary Becker": "Gary S. Becker",
            "John Forbes Nash Jr.": "John Forbes Nash",
            "Paul Romer": "Paul M. Romer",
            "Robert Lucas, Jr.": "Robert Lucas",
            "W. Arthur Lewis": "Arthur Lewis",
        },
        canonical={"Nobel Prize": NOBEL_ECO,
                   "Nobel Memorial Prize": NOBEL_ECO,
                   "Nobel Prize in Economics": NOBEL_ECO,
                   "Nobel Prize in Economic Sciences": NOBEL_ECO},
    ),
    "peace": dict(
        manifests=[
            ("peace/prompt_manifest.json", "top", "people", "name",
             "peace/presentations/pages/20th_century"),
            ("peace/prompt_manifest_21.json", "top", "people", "name",
             "peace/presentations/pages/21th_century"),
        ],
        alias={
            "Lord Boyd-Orr": "John Boyd Orr",
            "John Raleigh Mott": "John Mott",
            "United Nations Children's Fund (UNICEF)": "United Nations Children's Fund",
            "Wangari Muta Maathai": "Wangari Maathai",
        },
        canonical={"Nobel Prize": NOBEL_PEA},
    ),
}


# 各项目通用变体名归一（get_or_create 前应用）
NAME_CANONICAL = {
    "Royal Society Copley Medal": "Copley Medal",
    "National Academy of Sciences": "Member of the National Academy of Sciences",
    "Turing Award": "ACM A.M. Turing Award",
}


def get_or_create_award(cur, name_en):
    cur.execute("SELECT id FROM awards WHERE name_en=%s", (name_en,))
    r = cur.fetchone()
    if r:
        return r[0], False
    cur.execute("INSERT INTO awards (name_en, name_zh, award_type) VALUES (%s,%s,'award')",
                (name_en, name_en))
    return cur.lastrowid, True


def parse_awards(text):
    out, spans = [], []
    for m in re.finditer(
        r"\[([^\]]+)\]\([^)]*\)\s*(?:\((\d{4}(?:\s*[–/-]\s*\d{2,4})?)\))?", text
    ):
        n = m.group(1).strip()
        if n and len(n) < 120:
            out.append((n, m.group(2)))
            spans.append((m.start(), m.end()))

    def in_link(pos):
        return any(s <= pos < e for s, e in spans)

    for m in re.finditer(r"([A-Z][A-Za-z'’ .·-]{2,80}?)\s*\((\d{4})\)", text):
        if in_link(m.start()):
            continue
        n = m.group(1).strip().rstrip("-– ")
        if n and len(n) > 3 and not n.lower().startswith(("born", "died")):
            out.append((n, m.group(2)))
    return out


def norm_year(y):
    if not y:
        return 0
    m = re.match(r"(\d{4})", y.replace("–", "-"))
    return int(m.group(1)) if m else 0


def canonical_nobel(project_canonical, name):
    """Nobel 变体智能归一：剥尾缀年份，按学科关键词映射到本项目诺奖规范名。
    覆盖："Nobel Prize..."、"Nobel Memorial Prize..."、年份前缀（"2010 Nobel Peace Prize"）。"""
    n = TRAILING_YEAR_PAT.sub("", name).strip()
    if n in project_canonical.values():
        return n
    if re.search(r"Nobel", n, re.I):
        low = n.lower()
        target = None
        if "chemis" in low:
            target = "Nobel Prize in Chemistry"
        elif "medic" in low or "physiol" in low:
            target = NOBEL_MED
        elif "litera" in low:
            target = NOBEL_LIT
        elif "memorial" in low or "econ" in low:
            target = NOBEL_ECO
        elif "peace" in low:
            target = NOBEL_PEA
        elif "physic" in low:
            target = "Nobel Prize in Physics"
        else:
            target = next(iter(project_canonical.values()))
        # 仅当目标属于本项目可归一族时归并（避免把别人的诺奖错归本项目）
        if target in set(project_canonical.values()) | {
            "Nobel Prize in Chemistry", "Nobel Prize in Physics",
            NOBEL_MED, NOBEL_LIT, NOBEL_ECO, NOBEL_PEA,
        }:
            return target
    return n


def flatten_people(man_path, container_key, people_key):
    man = json.loads(Path(man_path).read_text(encoding="utf-8"))
    if container_key == "top":
        return man.get(people_key, [])
    people = []
    batches = man.get(container_key, [])
    if isinstance(batches, list):
        for b in batches:
            people.extend(b.get(people_key, []))
    else:
        for b in batches.values():
            people.extend(b.get(people_key, []))
    return people


def process(conn, cfg, project):
    cur = conn.cursor()
    canonical = cfg["canonical"]
    alias = cfg["alias"]
    stats = dict(persons=0, awards_new=0, rows_inserted=0, rows_skip=0, no_awards=[])
    for man_rel, container_key, people_key, name_key, pages_rel in cfg["manifests"]:
        man_path = OM / man_rel
        pages_root = OM / pages_rel
        for p in flatten_people(man_path, container_key, people_key):
            nm = p.get(name_key) or p.get("name_en") or p.get("name")
            nm = alias.get(nm, nm)
            cur.execute("SELECT id FROM people WHERE qid=%s", (p.get("qid"),))
            r = cur.fetchone()
            if not r:
                cur.execute("SELECT id FROM people WHERE name_en=%s", (nm,))
                r = cur.fetchone()
            if not r:
                stats["no_awards"].append((nm, "person not found"))
                continue
            pid = r[0]
            page = pages_root / p["dir"] / "page.md"
            if not page.exists():
                stats["no_awards"].append((nm, f"page.md missing: {p['dir']}"))
                continue
            text = page.read_text(encoding="utf-8")
            m = re.search(r"\|\s*Awards\s*\|(.*?)(?=\n\||\n\n)", text, re.S)
            cell = m.group(1) if m else ""
            pairs = []
            for n, y in parse_awards(cell):
                if NOISE_PAT.search(n) or n in FRAGMENTS or n in JUNK:
                    continue
                if DEGENERATE_PAT.match(n):
                    # 纯年份/QID：把年份信息交给 y，奖项名丢弃
                    if re.fullmatch(r"\d{4}", n) and not y:
                        y = n
                    continue
                # 名内嵌年份（如 "Nobel Prize in Literature (1971)"）剥出并作为年份源
                tm = TRAILING_YEAR_PAT.search(n)
                if tm and not y:
                    y = tm.group(0).strip("() ")
                n2 = canonical_nobel(canonical, n)
                n2 = NAME_CANONICAL.get(n2, n2)
                if project == "medicine" and n2 == "Wolf Prize":
                    n2 = "Wolf Prize in Medicine"
                if n2 in FRAGMENTS or n2 in JUNK or NOISE_PAT.search(n2):
                    continue
                transformed = n2 != n or n in canonical
                pairs.append((n2, y, transformed))
            if not pairs:
                stats["no_awards"].append((nm, "no awards parsed"))
                continue
            stats["persons"] += 1
            for name, year, transformed in pairs:
                aid, created = get_or_create_award(cur, name)
                stats["awards_new"] += int(created)
                y = norm_year(year)
                # 本项目诺奖：年份缺失(y=0)时按人去重（防 year=0 冗余行）；有年份按人+年去重
                if name in canonical.values() and (transformed or y == 0):
                    cur.execute(
                        "SELECT COUNT(*) FROM award_laureate WHERE person_id=%s AND award_id=%s",
                        (pid, aid))
                else:
                    cur.execute(
                        "SELECT COUNT(*) FROM award_laureate WHERE person_id=%s AND award_id=%s "
                        "AND ((year=%s) OR (year=0 AND %s=0) OR (year IS NULL AND %s IS NULL))",
                        (pid, aid, y, y, y))
                if cur.fetchone()[0]:
                    stats["rows_skip"] += 1
                    continue
                cur.execute(
                    "INSERT IGNORE INTO award_laureate (person_id, award_id, year, source) "
                    "VALUES (%s,%s,%s,'page_infobox')",
                    (pid, aid, y))
                if cur.rowcount:
                    stats["rows_inserted"] += 1
                else:
                    stats["rows_skip"] += 1
            conn.commit()
    return stats


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in PROJECTS:
        print("usage: python3 ingest_laureate_awards.py [medicine|literature|economics|peace]")
        sys.exit(1)
    project = sys.argv[1]
    conn = get_conn()
    s = process(conn, PROJECTS[project], project)
    print(project, ":", s)
