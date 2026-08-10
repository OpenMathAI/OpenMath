#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""批量输出 people 的 metadata.json 关键字段摘要 + page.md Awards/Institutions 行。
用法: python3 summarize_meta.py "name1" "name2" ...
"""
import json
import os
import re
import sys
import unicodedata

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "mathematician", "pages")

KEYS = ["occupation", "nationality", "date_of_birth", "date_of_death", "field_of_work",
        "doctoral_advisor", "doctoral_student", "educated_at", "employer",
        "award_received", "place_of_birth", "place_of_death", "notable_work"]


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def main():
    for name in sys.argv[1:]:
        pdir = None
        for cand in os.listdir(ROOT):
            if norm(cand) == norm(name):
                pdir = os.path.join(ROOT, cand)
                break
        if pdir is None:
            print(f"### {name}\n⚠ 无 pages 目录\n" + "=" * 60)
            continue
        meta_path = os.path.join(pdir, "metadata.json")
        print(f"### {name}  ({os.path.basename(pdir)})")
        if os.path.exists(meta_path):
            try:
                d = json.load(open(meta_path))
                print(f"qid={d.get('qid')} label={d.get('label')}")
                print(f"desc={d.get('description')}")
                props = d.get("properties", {})
                for k in KEYS:
                    if props.get(k):
                        print(f"  {k}: {', '.join(props[k])}")
            except Exception as e:
                print(f"  ERR {e}")
        page_path = os.path.join(pdir, "page.md")
        if os.path.exists(page_path):
            for line in open(page_path, encoding="utf-8"):
                if re.match(r"^\| (Awards|Institutions|Education|Alma mater) \|", line):
                    print(f"  [infobox] {line.strip()}")
        print("=" * 60)


if __name__ == "__main__":
    main()
