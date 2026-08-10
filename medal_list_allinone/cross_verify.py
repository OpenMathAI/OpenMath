#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全量交叉验证：Fields(目录名) × Wolf/Abel/Chern(页面表格) × Turing(页面表格)"""
import os
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).parent
FIELDS_PAGES = ROOT.parent / "Fields_Medal" / "pages"
AWARD_PAGES = ROOT / "pages"


def norm(x: str) -> str:
    x = unicodedata.normalize("NFKD", x)
    x = "".join(c for c in x if not unicodedata.combining(c))
    x = re.sub(r'[\'\-\.]', '', x)
    x = x.replace("von Neumann", "vonneumann")
    return re.sub(r'\s+', '', x).lower()


def fields_laureates() -> dict[str, str]:
    d = {}
    for y in os.listdir(FIELDS_PAGES):
        if not y.isdigit():
            continue
        for n in os.listdir(FIELDS_PAGES / y):
            if (FIELDS_PAGES / y / n).is_dir():
                d[norm(n)] = n.replace("_", " ")
    return d


def page_names(rel: str) -> dict[str, str]:
    p = AWARD_PAGES / rel
    if not p.exists():
        return {}
    html = p.read_text(encoding="utf-8", errors="ignore")
    d = {}
    for m in re.finditer(r'<t[dh][^>]*>(.*?)</t[dh]>', html, re.S | re.I):
        txt = re.sub(r'<[^>]+>', ' ', m.group(1))
        txt = re.sub(r'[\[\]0-9"]', '', txt).strip()
        txt = re.sub(r'\s+', ' ', txt).strip()
        if re.match(r'^[A-Z][\w\-\'\.]*(?:\s[A-Z][\w\-\'\.]*){0,4}$', txt) and " " in txt:
            if not re.search(r'(Prize|Award|Medal|University|Institute|Academy|Society|Soviet|German|United|France|Russia|Hungary|Argentina|Japan|Israel|Norway|Sweden|Denmark|Netherlands|Italy|China|India|Finland|Poland|Belgium|Iran|Brazil|Australia|Canada|Egypt|Singapore|Taiwan|Korea|Czech|Austria|Switzerland|Ireland|Romania|Ukraine|Turkey|Greece|Serbia|Bulgaria|Nationality|Citation|Year|Laureates|Recipients|Winners|Fields)', txt):
                d[norm(txt)] = txt
    return d


def intersect(fields: dict, other: dict, label: str):
    keys = fields.keys() & other.keys()
    if not keys:
        return
    print("=== Fields ∩ %s (%d)" % (label, len(keys)))
    for k in sorted(keys):
        print("   %s   (%s)" % (fields[k], other[k]))


def main():
    fields = fields_laureates()
    print("Fields laureates (from dir):", len(fields))
    wolf = page_names("math_top/Wolf Prize in Mathematics/index.html")
    abel = page_names("math_top/Abel Prize/index.html")
    chern = page_names("math_top/Chern Medal/index.html")
    print("Wolf page names:", len(wolf), "| Abel:", len(abel), "| Chern:", len(chern))
    intersect(fields, wolf, "Wolf")
    intersect(fields, abel, "Abel")
    intersect(fields, chern, "Chern")


if __name__ == "__main__":
    main()
