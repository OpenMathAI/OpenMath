#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""补全 8 位已立传数学家的数据库全字段（对应工作指南 §21.5 核对表）。

覆盖 8 人：Hilbert / Poincaré / von Neumann / Noether / Kolmogorov / Weyl / Grothendieck / Weil

补全内容：
1) occupations 字典 + person_occupation（副职业，rank 排序）
2) institutions 字典 + person_institution（education/employment，年份来自提示词/page.md）
3) awards 字典（历史奖项）+ award_laureate
   ★ 原则：只收「与人物同时代 + 有分量」的正式奖项；
     不收晚于人物的现代奖、政治勋章（苏联勋章）、名誉学位、资助类（Guggenheim）
4) 修正 Weyl 国籍（删除 Wikidata 误带的 Switzerland）

幂等：全部 INSERT IGNORE + 唯一键防重。
"""
import re
import unicodedata

from db_mysql import get_conn

# ---------------------------------------------------------------- 职业定义
# (name_en, name_zh) —— 仅补字典缺失的
NEW_OCCUPATIONS = [
    ("university teacher",        "大学教师"),
    ("historian of mathematics",  "数学史家"),
    ("logician",                  "逻辑学家"),
    ("philosopher of science",    "科学哲学家"),
    ("topologist",                "拓扑学家"),
    ("polymath",                  "博学家"),
    ("consultant",                "顾问"),
]

# 每人职业（rank 排序，0=主职业）—— 键为 occupations.name_en
PERSON_OCCUPATIONS = {
    "David Hilbert":          ["mathematician", "physicist", "philosopher", "logician", "university teacher"],
    "Henri Poincaré":         ["mathematician", "physicist", "philosopher", "astronomer", "engineer", "topologist", "writer", "university teacher"],
    "John von Neumann":       ["mathematician", "physicist", "computer scientist", "economist", "university teacher"],
    "Emmy Noether":           ["mathematician", "physicist", "university teacher"],
    "Andrey Kolmogorov":      ["mathematician", "computer scientist", "statistician", "physicist", "university teacher"],
    "Hermann Weyl":           ["mathematician", "physicist", "philosopher", "university teacher"],
    "Alexander Grothendieck": ["mathematician", "university teacher"],
    "André Weil":             ["mathematician", "historian of mathematics", "university teacher"],
}

# ---------------------------------------------------------------- 机构定义
# (name_en, name_zh, relation, start_year, end_year)  relation: education / employment
# 年份取自提示词时间线 / page.md；不确定则 None
PERSON_INSTITUTIONS = {
    "David Hilbert": [
        ("University of Königsberg", "柯尼斯堡大学", "education", None, None),
        ("Collegium Fridericianum",  "腓特烈学院",   "education", None, None),
        ("Wilhelmsgymnasium",        "威廉中学",     "education", None, None),
        ("Heidelberg University",    "海德堡大学",   "education", None, None),
        ("University of Königsberg", "柯尼斯堡大学", "employment", 1886, 1895),
        ("University of Göttingen",  "哥廷根大学",   "employment", 1895, 1943),
    ],
    "Henri Poincaré": [
        ("École Polytechnique",      "巴黎综合理工学院", "education", None, None),
        ("Mines ParisTech",          "巴黎矿业学院",     "education", None, None),
        ("University of Paris",      "巴黎大学",         "education", None, None),
        ("University of Caen Normandy", "卡昂大学",     "employment", 1879, 1881),
        ("University of Paris",      "巴黎大学",         "employment", 1881, 1912),
        ("Corps des Mines",          "矿业军团",         "employment", 1881, 1912),
        ("Bureau des Longitudes",    "经度局",           "employment", 1893, 1912),
    ],
    "John von Neumann": [
        ("Fasori Gimnázium",            "法索里中学",        "education", None, None),
        ("Eötvös Loránd University",    "厄特沃什·罗兰大学",  "education", None, None),
        ("ETH Zurich",                  "苏黎世联邦理工学院", "education", None, None),
        ("Frederick William University Berlin", "柏林腓特烈·威廉大学", "education", None, None),
        ("University of Göttingen",     "哥廷根大学",         "education", None, None),
        ("Frederick William University Berlin", "柏林腓特烈·威廉大学", "employment", 1926, 1930),
        ("University of Hamburg",       "汉堡大学",           "employment", 1929, 1930),
        ("Princeton University",        "普林斯顿大学",       "employment", 1930, 1933),
        ("Institute for Advanced Study","普林斯顿高等研究院", "employment", 1933, 1957),
        ("Los Alamos National Laboratory", "洛斯阿拉莫斯国家实验室", "employment", 1943, 1955),
    ],
    "Emmy Noether": [
        ("University of Erlangen-Nuremberg", "埃尔朗根-纽伦堡大学", "education", None, None),
        ("University of Göttingen",          "哥廷根大学",         "education", None, None),
        ("Heidelberg University",            "海德堡大学",         "education", None, None),
        ("University of Erlangen-Nuremberg", "埃尔朗根-纽伦堡大学", "employment", 1907, 1915),
        ("University of Göttingen",          "哥廷根大学",         "employment", 1915, 1933),
        ("Bryn Mawr College",                "布林莫尔学院",       "employment", 1933, 1935),
    ],
    "Andrey Kolmogorov": [
        ("Lomonosov Moscow State University", "莫斯科国立大学", "education", None, None),
        ("Lomonosov Moscow State University", "莫斯科国立大学", "employment", 1931, 1987),
    ],
    "Hermann Weyl": [
        ("University of Göttingen",          "哥廷根大学",         "education", None, None),
        ("Ludwig Maximilian University of Munich", "慕尼黑大学",  "education", None, None),
        ("Christianeum",                     "克里斯蒂安中学",     "education", None, None),
        ("University of Göttingen",          "哥廷根大学",         "employment", 1908, 1913),
        ("ETH Zurich",                       "苏黎世联邦理工学院", "employment", 1913, 1930),
        ("University of Göttingen",          "哥廷根大学",         "employment", 1930, 1933),
        ("Institute for Advanced Study",     "普林斯顿高等研究院", "employment", 1933, 1951),
    ],
    "Alexander Grothendieck": [
        ("University of Montpellier",        "蒙彼利埃大学",        "education", None, None),
        ("École Normale Supérieure",         "巴黎高等师范学院",    "education", None, None),
        ("Nancy-Université",                 "南锡大学",            "education", None, None),
        ("National Center for Scientific Research", "法国国家科学研究中心", "employment", 1950, 1953),
        ("Institut des Hautes Études Scientifiques", "高等科学研究院 (IHÉS)", "employment", 1958, 1970),
        ("University of Montpellier",        "蒙彼利埃大学",        "employment", 1973, 1988),
    ],
    "André Weil": [
        ("École Normale Supérieure",         "巴黎高等师范学院",    "education", None, None),
        ("University of Paris",              "巴黎大学",            "education", None, None),
        ("University of Göttingen",          "哥廷根大学",          "education", None, None),
        ("Aligarh Muslim University",        "阿里格尔穆斯林大学",  "employment", 1930, 1932),
        ("University of Strasbourg",         "斯特拉斯堡大学",      "employment", 1933, 1939),
        ("Haverford College",                "哈弗福德学院",        "employment", 1941, 1945),
        ("University of São Paulo",          "圣保罗大学",          "employment", 1945, 1947),
        ("University of Chicago",            "芝加哥大学",          "employment", 1947, 1958),
        ("Institute for Advanced Study",     "普林斯顿高等研究院",  "employment", 1958, 1976),
    ],
}

# ---------------------------------------------------------------- 奖项定义
# 新增 awards 字典（name_en, name_zh, award_type, tier, org, established）
NEW_AWARDS = [
    ("Lobachevsky Prize",                 "罗巴切夫斯基奖",          "math_hist", 2, "Kazan University", 1897),
    ("Bolyai Prize",                      "波尔约奖",                "math_hist", 2, "Hungarian Academy of Sciences", 1905),
    ("Foreign Member of the Royal Society", "英国皇家学会外籍院士",   "honor", None, "Royal Society", 1660),
    ("Gold Medal of the Royal Astronomical Society", "皇家天文学会金质奖章", "honor", None, "Royal Astronomical Society", 1824),
    ("Sylvester Medal",                   "西尔维斯特奖章",          "math_hist", 2, "Royal Society", 1901),
    ("Matteucci Medal",                   "马泰乌奇奖章",            "honor", None, "Italian Society of Sciences", 1868),
    ("Bruce Medal",                       "布鲁斯奖章",              "honor", None, "Astronomical Society of the Pacific", 1898),
    ("Bôcher Memorial Prize",             "博赫尔纪念奖",            "math_hist", 2, "American Mathematical Society", 1923),
    ("Medal for Merit",                   "功绩勋章",                "honor", None, "United States", 1942),
    ("Medal of Freedom",                  "自由勋章",                "honor", None, "United States", 1945),
    ("Enrico Fermi Award",                "恩里科·费米奖",           "honor", None, "US Department of Energy", 1956),
    ("Carl-Gustaf Rossby Research Medal", "罗斯比研究奖章",           "honor", None, "American Meteorological Society", 1953),
    ("Ackermann–Teubner Memorial Award",  "阿克曼-托伊布纳纪念奖",   "math_hist", 2, "Universität Leipzig", 1912),
    ("Balzan Prize",                      "巴尔赞奖",                "cross", 6, "Balzan Foundation", 1956),
    ("Josiah Willard Gibbs Lectureship",  "吉布斯讲座",              "honor", None, "American Mathematical Society", 1923),
    ("Pour le Mérite for Sciences and Arts", "功勋勋章（科学与艺术）", "honor", None, "Kingdom of Prussia", 1842),
    ("Émile Picard Medal",                "埃米尔·皮卡德奖章",       "math_hist", 2, "French Academy of Sciences", 1943),
    ("Leroy P. Steele Prize",             "斯蒂尔奖",                "math_hist", 2, "American Mathematical Society", 1970),
    ("Barnard Medal for Meritorious Service to Science", "巴纳德奖章", "honor", None, "Columbia University", 1895),
]

# 每人获奖：(award_name_en, year, note) —— year 来自 page.md infobox
PERSON_AWARDS = {
    "David Hilbert": [
        ("Lobachevsky Prize", 1903, None),
        ("Bolyai Prize", 1910, None),
        ("Foreign Member of the Royal Society", 1928, None),
        ("Member of the National Academy of Sciences", 1907, "国际院士 (International Member)"),
    ],
    "Henri Poincaré": [
        ("Gold Medal of the Royal Astronomical Society", 1900, None),
        ("Sylvester Medal", 1901, None),
        ("Matteucci Medal", 1905, None),
        ("Bolyai Prize", 1905, None),
        ("Bruce Medal", 1911, None),
    ],
    "John von Neumann": [
        ("Bôcher Memorial Prize", 1938, None),
        ("Medal for Merit", 1946, None),
        ("Medal of Freedom", 1956, None),
        ("Enrico Fermi Award", 1956, None),
        ("Carl-Gustaf Rossby Research Medal", 1957, None),
    ],
    "Emmy Noether": [
        ("Ackermann–Teubner Memorial Award", 1932, "数学界对女性学者的罕见认可"),
    ],
    "Andrey Kolmogorov": [
        ("Balzan Prize", 1962, None),
        ("Foreign Member of the Royal Society", 1964, None),
        ("Lobachevsky Prize", 1986, None),
        # Wolf 1980 已入库（seed_wolf_prize.py），此处幂等跳过
    ],
    "Hermann Weyl": [
        ("Lobachevsky Prize", 1927, None),
        ("Foreign Member of the Royal Society", 1931, None),
        ("Member of the National Academy of Sciences", 1941, None),
        ("Josiah Willard Gibbs Lectureship", 1948, None),
        ("Pour le Mérite for Sciences and Arts", 1955, None),
    ],
    "Alexander Grothendieck": [
        ("Émile Picard Medal", 1977, None),
        ("Crafoord Prize", 1988, "拒绝领奖 (declined)"),
        # Fields 1966 已入库（seed_fields_medal.py）
    ],
    "André Weil": [
        ("Foreign Member of the Royal Society", 1966, None),
        ("Leroy P. Steele Prize", 1980, None),
        ("Barnard Medal for Meritorious Service to Science", 1980, None),
        ("Kyoto Prize", 1994, "京都奖（基础科学类）"),
        # Wolf 1979 已入库（seed_wolf_prize.py）
    ],
}


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def main():
    conn = get_conn()
    cur = conn.cursor()

    # ---- 0) 8 人 id 索引 ----
    cur.execute("SELECT id, name_en FROM people")
    by_en = {norm(n): p for p, n in cur.fetchall() if n}
    pids = {name: by_en.get(norm(name)) for name in PERSON_OCCUPATIONS}
    missing = [n for n, p in pids.items() if p is None]
    if missing:
        print("⚠ 库中缺失人物:", missing)
    for n, p in pids.items():
        if p:
            print(f"  目标: {n} (id={p})")

    # ---- 1) occupations 字典 + person_occupation ----
    cur.execute("SELECT id, name_en FROM occupations")
    occ_ids = {n: i for i, n in cur.fetchall()}
    for en, zh in NEW_OCCUPATIONS:
        if en not in occ_ids:
            cur.execute("INSERT INTO occupations(name_en, name_zh) VALUES (%s,%s)", (en, zh))
            occ_ids[en] = cur.lastrowid
            print(f"  + occupations: {en} ({zh})")
    n_occ = 0
    for person, occs in PERSON_OCCUPATIONS.items():
        pid = pids[person]
        for rank, occ in enumerate(occs):
            if occ not in occ_ids:
                print(f"  ⚠ occupations 字典缺失: {occ}（跳过 {person} 的该职业）")
                continue
            cur.execute(
                "INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,%s)",
                (pid, occ_ids[occ], rank),
            )
            if cur.rowcount:
                n_occ += 1
    print(f"  → 新增 person_occupation: {n_occ} 条")

    # ---- 2) institutions 字典 + person_institution ----
    cur.execute("SELECT id, name_en FROM institutions")
    inst_ids = {n: i for i, n in cur.fetchall()}
    n_inst = 0
    for person, insts in PERSON_INSTITUTIONS.items():
        pid = pids[person]
        for en, zh, rel, sy, ey in insts:
            if en not in inst_ids:
                cur.execute("INSERT INTO institutions(name_en, name_zh) VALUES (%s,%s)", (en, zh))
                inst_ids[en] = cur.lastrowid
                print(f"  + institutions: {en} ({zh})")
            cur.execute(
                "INSERT IGNORE INTO person_institution(person_id, inst_id, relation, start_year, end_year) "
                "VALUES (%s,%s,%s,%s,%s)",
                (pid, inst_ids[en], rel, sy, ey),
            )
            if cur.rowcount:
                n_inst += 1
    print(f"  → 新增 person_institution: {n_inst} 条")

    # ---- 3) awards 字典 + award_laureate ----
    cur.execute("SELECT id, name_en FROM awards")
    award_ids = {n: i for i, n in cur.fetchall()}
    for en, zh, atype, tier, org, est in NEW_AWARDS:
        if en not in award_ids:
            cur.execute(
                "INSERT INTO awards(name_en, name_zh, award_type, tier, org, established) VALUES (%s,%s,%s,%s,%s,%s)",
                (en, zh, atype, tier, org, est),
            )
            award_ids[en] = cur.lastrowid
            print(f"  + awards: {en} ({zh})")
    n_award = 0
    for person, aws in PERSON_AWARDS.items():
        pid = pids[person]
        for award, year, note in aws:
            if award not in award_ids:
                print(f"  ⚠ awards 字典缺失: {award}（跳过 {person}）")
                continue
            cur.execute(
                "INSERT IGNORE INTO award_laureate(person_id, award_id, year, note, source) "
                "VALUES (%s,%s,%s,%s,'Wikipedia infobox')",
                (pid, award_ids[award], year, note),
            )
            if cur.rowcount:
                n_award += 1
                print(f"    → {person}: {award} {year}")
    print(f"  → 新增 award_laureate: {n_award} 条")

    # ---- 4) 修正 Weyl 国籍（删除 Wikidata 误带 Switzerland）----
    if pids.get("Hermann Weyl"):
        cur.execute("SELECT id FROM countries WHERE name_en='Switzerland'")
        row = cur.fetchone()
        if row:
            cur.execute(
                "DELETE FROM person_nationality WHERE person_id=%s AND country_id=%s",
                (pids["Hermann Weyl"], row[0]),
            )
            print(f"  → 已删除 Weyl 的 Switzerland 国籍关联 (affected={cur.rowcount})")

    conn.commit()

    # ---- 汇总 ----
    cur.execute("SELECT COUNT(*) FROM occupations");  print(f"occupations 总数: {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(*) FROM person_occupation"); print(f"person_occupation 总数: {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(*) FROM institutions"); print(f"institutions 总数: {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(*) FROM person_institution"); print(f"person_institution 总数: {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(*) FROM awards"); print(f"awards 总数: {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(*) FROM award_laureate"); print(f"award_laureate 总数: {cur.fetchone()[0]}")
    conn.close()


if __name__ == "__main__":
    main()
