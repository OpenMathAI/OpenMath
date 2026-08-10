#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""建立国家/政权字典（countries）并灌入人物国籍（person_nationality）。

数据源：mathematician/pages/*/metadata.json 的 nationality 多值字段。
- 43 种国籍/政权（含历史政权：Soviet Union、Weimar Republic、Kingdom of Prussia...）
- is_current=0 为历史政权，successor 指向现代后继国（可按现代国归一过滤）
- person_nationality 多对多：一人多国籍，rank 保留 Wikidata 顺序
"""
import json
import re
import unicodedata
from pathlib import Path

import pymysql
from db_mysql import get_conn

PAGES = Path(__file__).resolve().parent.parent / "mathematician" / "pages"


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()

# 国籍/政权 -> (is_current, successor, iso, name_zh)
# 历史政权 successor 指向现代国名（须存在于本表或为标准名）
COUNTRY_MAP = {
    # --- 现代国家 ---
    "United States": (1, None, "US", "美国"),
    "France": (1, None, "FR", "法国"),
    "Germany": (1, None, "DE", "德国"),
    "United Kingdom": (1, None, "GB", "英国"),
    "Russia": (1, None, "RU", "俄罗斯"),
    "Austria": (1, None, "AT", "奥地利"),
    "Finland": (1, None, "FI", "芬兰"),
    "Switzerland": (1, None, "CH", "瑞士"),
    "China": (1, None, "CN", "中国"),
    "People's Republic of China": (1, None, "CN", "中华人民共和国"),
    "Czechoslovakia": (0, "Czechia", "CZ", "捷克斯洛伐克"),
    "Norway": (1, None, "NO", "挪威"),
    "Poland": (1, None, "PL", "波兰"),
    "Hungary": (1, None, "HU", "匈牙利"),
    "India": (1, None, "IN", "印度"),
    "Australia": (1, None, "AU", "澳大利亚"),
    "Sweden": (1, None, "SE", "瑞典"),
    "Belgium": (1, None, "BE", "比利时"),
    "Kingdom of the Netherlands": (1, None, "NL", "荷兰王国"),
    # --- 历史政权（successor -> 现代国）---
    "Kingdom of Prussia": (0, "Germany", None, "普鲁士王国"),
    "German Empire": (0, "Germany", None, "德意志帝国"),
    "German Reich": (0, "Germany", None, "德意志国"),
    "Weimar Republic": (0, "Germany", None, "魏玛共和国"),
    "Nazi Germany": (0, "Germany", None, "纳粹德国"),
    "Kingdom of Hanover": (0, "Germany", None, "汉诺威王国"),
    "Kingdom of Bavaria": (0, "Germany", None, "巴伐利亚王国"),
    "Confederation of the Rhine": (0, "Germany", None, "莱茵邦联"),
    "Russian Empire": (0, "Russia", None, "俄罗斯帝国"),
    "Russian Socialist Federative Soviet Republic": (0, "Russia", None, "俄罗斯苏维埃联邦社会主义共和国"),
    "Russian Soviet Federative Socialist Republic": (0, "Russia", None, "俄罗斯苏维埃联邦社会主义共和国"),
    "Soviet Union": (0, "Russia", None, "苏联"),
    "Ukrainian Soviet Socialist Republic": (0, "Ukraine", None, "乌克兰苏维埃社会主义共和国"),
    "Reichskommissariat Ukraine": (0, "Ukraine", None, "乌克兰总督辖区"),
    "Austria–Hungary": (0, "Austria", None, "奥匈帝国"),
    "Cisleithania": (0, "Austria", None, "奥地利-西里西亚"),
    "British Raj": (0, "India", None, "英属印度"),
    "Dominion of India": (0, "India", None, "印度自治领"),
    "Grand Duchy of Finland": (0, "Finland", None, "芬兰大公国"),
    "Second Polish Republic": (0, "Poland", None, "波兰第二共和国"),
    "Old Swiss Confederacy": (0, "Switzerland", None, "旧瑞士邦联"),
    "Tang dynasty": (0, "China", None, "唐朝"),
    "Eastern Han": (0, "China", None, "东汉"),
    "statelessness": (0, None, None, "无国籍"),
}


def main():
    conn = get_conn()
    cur = conn.cursor()

    # 1) 建 countries 字典
    cur.execute("SELECT name_en FROM countries")
    existing = {r[0] for r in cur.fetchall()}
    added = 0
    for name, (is_cur, succ, iso, zh) in COUNTRY_MAP.items():
        if name not in existing:
            cur.execute(
                "INSERT INTO countries(name_en, name_zh, is_current, successor, iso) VALUES (%s,%s,%s,%s,%s)",
                (name, zh, is_cur, succ, iso),
            )
            added += 1
    conn.commit()
    print(f"countries: 新增 {added}（总 {len(COUNTRY_MAP)}）")

    # 2) pages 目录 -> metadata 姓名索引（归一化）
    dir_norms = {}
    for d in PAGES.iterdir():
        if d.is_dir():
            mf = d / "metadata.json"
            if mf.exists():
                try:
                    m = json.loads(mf.read_text(encoding="utf-8"))
                    nm = m.get("name")
                    if nm:
                        dir_norms.setdefault(norm(nm), d.name)
                except Exception:
                    pass

    # 3) 载入 people，按姓名匹配 pages 目录（不依赖 local_dir）
    cur.execute("SELECT id, name_en, name_zh FROM people")
    people = cur.fetchall()

    meta_nats = {}
    for pid, en, zh in people:
        if not en and zh:
            en = zh
        dname = dir_norms.get(norm(en))
        if not dname:
            continue
        mf = PAGES / dname / "metadata.json"
        try:
            m = json.loads(mf.read_text(encoding="utf-8"))
            nats = m.get("properties", {}).get("nationality", [])
            if nats:
                meta_nats[pid] = nats
        except Exception:
            pass
    conn.commit()
    print(f"有国籍 metadata 的人: {len(meta_nats)}")

    # 4) 灌入 person_nationality
    cur.execute("SELECT name_en, id FROM countries")
    cid_map = {n: i for n, i in cur.fetchall()}
    added_rel = 0
    unknown = set()
    for pid, nats in meta_nats.items():
        for rank, nat in enumerate(nats):
            if nat in cid_map:
                try:
                    cur.execute(
                        "INSERT IGNORE INTO person_nationality(person_id, country_id, `rank`) VALUES (%s,%s,%s)",
                        (pid, cid_map[nat], rank),
                    )
                    if cur.rowcount:
                        added_rel += 1
                except pymysql.err.IntegrityError:
                    pass
            else:
                unknown.add(nat)
    conn.commit()
    print(f"person_nationality 新增: {added_rel} 条")
    if unknown:
        print("未匹配国籍:", unknown)
    cur.execute("SELECT COUNT(*) FROM person_nationality")
    print(f"person_nationality 总数: {cur.fetchone()[0]}")
    conn.close()


if __name__ == "__main__":
    main()
