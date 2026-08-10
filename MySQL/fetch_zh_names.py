#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""为缺中文名的人补中文名：
1. 先从 mathematician/pages/*/metadata.json 补 qid（46 人）
2. 再调用 Wikidata API 按 qid 批量拉中文 label（wblabelen? 实际为中文 label：wbgetentities + languages=zh）
3. 更新 people.name_zh
"""
import json
import re
import time
import unicodedata
import urllib.request
from pathlib import Path

from db_mysql import get_conn

PAGES = Path(__file__).resolve().parent.parent / "mathematician" / "pages"
API = "https://www.wikidata.org/w/api.php"
HEADERS = {"User-Agent": "OpenMathAI/1.0 (academic research; local DB enrich)"}


def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def fetch_zh_labels(qids):
    """按 qid 批量拉中文 label。返回 {qid: zh_label}"""
    out = {}
    batch = 50
    for i in range(0, len(qids), batch):
        chunk = qids[i:i + batch]
        url = (API + "?action=wbgetentities&ids=" + "|".join(chunk)
               + "&props=labels&languages=zh&format=json")
        req = urllib.request.Request(url, headers=HEADERS)
        try:
            with urllib.request.urlopen(req, timeout=20) as resp:
                data = json.loads(resp.read().decode("utf-8"))
            for qid, ent in data.get("entities", {}).items():
                lbl = ent.get("labels", {}).get("zh", {}).get("value")
                if lbl:
                    out[qid] = lbl
        except Exception as e:
            print(f"  ⚠ 批次 {i//batch} 失败: {e}")
        time.sleep(0.5)  # 限流
    return out


def main():
    conn = get_conn()
    cur = conn.cursor()

    # 1) pages 目录索引（名字 -> qid）
    paged = {}
    for d in PAGES.iterdir():
        if not d.is_dir():
            continue
        mf = d / "metadata.json"
        if not mf.exists():
            continue
        try:
            m = json.loads(mf.read_text(encoding="utf-8"))
            if m.get("qid"):
                paged[norm(m.get("name", ""))] = m["qid"]
        except Exception:
            pass

    # 2) 缺中文名的人
    cur.execute("SELECT id, name_en, qid FROM people WHERE name_zh IS NULL")
    need = cur.fetchall()
    print(f"缺中文名: {len(need)}")

    # 3) 补 qid（从 pages）+ 收集待拉取 qid
    to_fetch = set()
    qid_filled = 0
    for pid, en, qid in need:
        if not qid and en and norm(en) in paged:
            cur.execute("UPDATE people SET qid=%s WHERE id=%s", (paged[norm(en)], pid))
            qid_filled += 1
            qid = paged[norm(en)]
        if qid:
            to_fetch.add(qid)
    conn.commit()
    print(f"从 pages 补 qid: {qid_filled} 人")

    # 4) 拉中文 label
    to_fetch = sorted(to_fetch)
    print(f"待拉取 qid: {len(to_fetch)}")
    labels = fetch_zh_labels(to_fetch)
    print(f"获得中文名: {len(labels)}")

    # 5) 回填
    updated = 0
    cur.execute("SELECT id, qid FROM people WHERE name_zh IS NULL")
    for pid, qid in cur.fetchall():
        if qid and qid in labels:
            cur.execute("UPDATE people SET name_zh=%s WHERE id=%s", (labels[qid], pid))
            updated += 1
    conn.commit()
    print(f"回填中文名: {updated} 人")

    cur.execute("SELECT COUNT(*) FROM people WHERE name_zh IS NULL")
    print(f"仍缺中文名: {cur.fetchone()[0]} 人")
    conn.close()


if __name__ == "__main__":
    main()
