#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""交叉荣誉回填：依据 medal_list_allinone/all_cross_reference.md（权威交叉表，含年份）。

把数学四大奖交叉、图灵奖交叉、COPSS 交叉中缺失的 award_laureate 记录补入数据库。
- 数据源：all_cross_reference.md（1936–2026 权威交叉名录）
- 人物匹配 people 表（name_en，含别名），缺失则占位
- 补 awards 字典（Wolf Prize in Physics 等缺失项）
- 幂等：INSERT IGNORE
- 验证：回填后运行 verify_cross_awards.py 与文档逐条比对
"""
import json
import re
import unicodedata

from db_mysql import get_conn

# 需补的奖项字典（name_en, name_zh, award_type, tier, org, established）
NEW_AWARDS = [
    ("Wolf Prize in Physics", "沃尔夫物理学奖", "honor", None, "Wolf Foundation", 1978),
    ("Nobel Prize in Physics", "诺贝尔物理学奖", "nobel", 1, "Nobel Foundation", 1901),
    ("Nobel Memorial Prize in Economic Sciences", "诺贝尔经济学奖", "nobel", 1, "Nobel Foundation", 1968),
    ("Japan Prize", "日本国际奖", "honor", None, "Japan Prize Foundation", 1985),
    ("IEEE John von Neumann Medal", "IEEE 冯·诺依曼奖章", "honor", None, "IEEE", 1990),
    ("EATCS Award", "EATCS 奖", "honor", None, "European Association for Theoretical Computer Science", 1984),
    ("Rumelhart Prize", "鲁梅哈特奖", "honor", None, "Gatsby Foundation", 2001),
    ("National Medal of Technology and Innovation", "美国国家技术奖章", "honor", None, "United States", 1980),
    ("Gödel Prize", "哥德尔奖", "cs", 2, "ACM SIGACT/EATCS", 1993),
    ("Rolf Nevanlinna Prize", "内万林纳奖", "cs", 2, "IMU", 1982),
    ("Claude E. Shannon Award", "IEEE 香农奖", "cs", 2, "IEEE Information Theory Society", 1972),
    ("IEEE Richard W. Hamming Medal", "IEEE 汉明奖章", "honor", None, "IEEE", 1986),
    ("Marconi Prize", "马可尼奖", "cs", 2, "Marconi Society", 1975),
    ("International Prize in Statistics", "国际统计学奖", "statistics", 2, "COPSS/ASA/ISI/IBS/IMS/ICSA/IBSP", 2016),
]

# 交叉数据：库中 name_en -> [(award_name_en, year, note)]  （year=0 表示年份待查）
CROSS = {
    # ===== §一 数学四大奖交叉（含年份核对） =====
    "Jean-Pierre Serre": [("Wolf Prize in Mathematics", 2000, None), ("Abel Prize", 2003, "首届阿贝尔奖")],
    "John Milnor": [("Wolf Prize in Mathematics", 1989, None), ("Abel Prize", 2011, None)],
    "John G. Thompson": [("Wolf Prize in Mathematics", 1992, None), ("Abel Prize", 2008, None)],
    "Pierre Deligne": [("Wolf Prize in Mathematics", 2008, None), ("Abel Prize", 2013, None)],
    "Grigory Margulis": [("Wolf Prize in Mathematics", 2005, None), ("Abel Prize", 2020, None)],
    "Lars Ahlfors": [("Wolf Prize in Mathematics", 1981, None)],
    "Atle Selberg": [("Wolf Prize in Mathematics", 1986, None)],
    "Kunihiko Kodaira": [("Fields Medal", 1954, None), ("Wolf Prize in Mathematics", 1984, None)],
    "Lars Hörmander": [("Wolf Prize in Mathematics", 1988, None)],
    "Stephen Smale": [("Wolf Prize in Mathematics", 2006, None)],
    "Sergei Novikov": [("Fields Medal", 1970, None), ("Wolf Prize in Mathematics", 2005, None)],
    "David Mumford": [("Wolf Prize in Mathematics", 2008, None)],
    "Charles Fefferman": [("Fields Medal", 1978, None), ("Wolf Prize in Mathematics", 2017, None)],
    "Shing-Tung Yau": [("Wolf Prize in Mathematics", 2010, None)],
    "Simon Donaldson": [("Fields Medal", 1986, None), ("Wolf Prize in Mathematics", 2020, None)],
    "Vladimir Drinfeld": [("Fields Medal", 1990, None), ("Wolf Prize in Mathematics", 2018, None)],
    "Peter Lax": [("Wolf Prize in Mathematics", 1987, None), ("Abel Prize", 2005, None)],
    "Lennart Carleson": [("Wolf Prize in Mathematics", 1992, None), ("Abel Prize", 2006, None)],
    "Jacques Tits": [("Wolf Prize in Mathematics", 1993, None), ("Abel Prize", 2008, None)],
    "Mikhail Gromov": [("Wolf Prize in Mathematics", 1993, None)],
    "Andrew Wiles": [("Wolf Prize in Mathematics", 1995, None), ("Abel Prize", 2016, None)],
    "Robert Langlands": [("Wolf Prize in Mathematics", 1995, None), ("Abel Prize", 2018, None)],
    "Yakov Sinai": [("Wolf Prize in Mathematics", 1996, None), ("Abel Prize", 2014, None)],
    "László Lovász": [("Wolf Prize in Mathematics", 1999, None), ("Abel Prize", 2021, None)],
    "John Tate": [("Wolf Prize in Mathematics", 2002, None), ("Abel Prize", 2010, None)],
    "Hillel Furstenberg": [("Wolf Prize in Mathematics", 2006, None), ("Abel Prize", 2020, None)],
    "Dennis Sullivan": [("Wolf Prize in Mathematics", 2010, None), ("Abel Prize", 2022, None)],
    "Luis Caffarelli": [("Wolf Prize in Mathematics", 2012, None), ("Abel Prize", 2023, None)],
    "Michael Atiyah": [("Abel Prize", 2004, None)],
    "Gerd Faltings": [("Fields Medal", 1986, None), ("Abel Prize", 2026, None)],
    "Phillip Griffiths": [("Wolf Prize in Mathematics", 2008, None), ("Chern Medal", 2014, None)],
    "Louis Nirenberg": [("Chern Medal", 2010, "首届陈省身奖章"), ("Abel Prize", 2015, None)],
    "Masaki Kashiwara": [("Chern Medal", 2018, None), ("Abel Prize", 2025, None)],
    # ===== §二 图灵奖交叉 =====
    "Avi Wigderson": [("Gödel Prize", 2009, None), ("Rolf Nevanlinna Prize", 1994, None)],
    "Herbert A. Simon": [("Nobel Memorial Prize in Economic Sciences", 1978, None)],
    "Geoffrey Hinton": [("Nobel Prize in Physics", 2024, "与 John Hopfield 共享")],
    "Charles H. Bennett": [("Wolf Prize in Physics", 2018, None), ("Claude E. Shannon Award", 2020, None)],
    "Gilles Brassard": [("Wolf Prize in Physics", 2018, None), ("Fellow of the Royal Society", 2013, None)],
    "Adi Shamir": [("Fellow of the Royal Society", 2018, None)],
    "Donald E. Knuth": [("Kyoto Prize", 1996, None)],
    "John McCarthy": [("Kyoto Prize", 1988, None)],
    "Andrew Yao": [("Kyoto Prize", 2021, None)],
    "Richard M. Karp": [("Kyoto Prize", 2008, None), ("National Medal of Science", 1996, None), ("EATCS Award", 2000, None)],
    "Tony Hoare": [("Kyoto Prize", 2000, None)],
    "Ivan Sutherland": [("Kyoto Prize", 2004, None), ("IEEE John von Neumann Medal", 1998, None)],
    "Alan Kay": [("Kyoto Prize", 2004, None)],
    "Shafi Goldwasser": [("Gödel Prize", 1993, "首届哥德尔奖（零知识证明）"), ("Gödel Prize", 2001, "第二次获奖（PCP）"), ("Member of the National Academy of Sciences", 0, None)],
    "Silvio Micali": [("Gödel Prize", 1993, "首届哥德尔奖（零知识证明）"), ("Member of the National Academy of Sciences", 0, None)],
    "Richard Hamming": [("IEEE Richard W. Hamming Medal", 1988, None)],
    "Whitfield Diffie": [("IEEE Richard W. Hamming Medal", 2010, None), ("Marconi Prize", 2000, None)],
    "Martin E. Hellman": [("IEEE Richard W. Hamming Medal", 2010, None), ("Marconi Prize", 2000, None)],
    "Marvin Minsky": [("Japan Prize", 1990, None)],
    "Dennis Ritchie": [("Japan Prize", 2011, None), ("National Medal of Technology and Innovation", 1998, None)],
    "Ken Thompson": [("Japan Prize", 2011, None), ("National Medal of Technology and Innovation", 1998, None)],
    "Vint Cerf": [("Japan Prize", 2008, None), ("Marconi Prize", 1998, None), ("National Medal of Technology and Innovation", 1997, None)],
    "Robert Tarjan": [("Rolf Nevanlinna Prize", 1982, None)],
    "Leslie Valiant": [("Rolf Nevanlinna Prize", 1986, None), ("EATCS Award", 2008, None)],
    "Ronald Rivest": [("Marconi Prize", 2007, None)],
    "Robert Metcalfe": [("Marconi Prize", 2003, None), ("National Medal of Technology and Innovation", 2003, None)],
    "Barbara Liskov": [("IEEE John von Neumann Medal", 2004, None)],
    "Leslie Lamport": [("IEEE John von Neumann Medal", 2008, None)],
    "John Backus": [("National Medal of Science", 1975, None)],
    "William Kahan": [("National Medal of Science", 1989, None)],
    "Judea Pearl": [("National Medal of Science", 2014, None), ("Rumelhart Prize", 2011, None)],
    "Yann LeCun": [("National Medal of Science", 2023, None), ("Member of the National Academy of Sciences", 2021, None)],
    "Yoshua Bengio": [("Fellow of the Royal Society", 2024, None)],
    "Jack Dongarra": [("National Medal of Science", 2020, None), ("Fellow of the Royal Society", 2019, None)],
    "Tim Berners-Lee": [("Fellow of the Royal Society", 2001, None), ("Member of the National Academy of Sciences", 2009, None)],
    # ===== §三 COPSS 交叉 =====
    "David L. Donoho": [("Gauss Prize", 2018, "ICIAM 最高奖"), ("Shaw Prize", 2013, None)],
}


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def main():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id, name_en, name_zh FROM people")
    people = [(p, en, zh, norm(en or ""), norm(zh or "")) for p, en, zh in cur.fetchall()]
    by_en = {ne: p for p, en, zh, ne, nz in people if ne}
    by_zh = {nz: p for p, en, zh, ne, nz in people if nz}

    cur.execute("SELECT id, name_en FROM awards")
    award_ids = {n: i for i, n in cur.fetchall()}
    for en, zh, atype, tier, org, est in NEW_AWARDS:
        if en not in award_ids:
            cur.execute("INSERT INTO awards(name_en, name_zh, award_type, tier, org, established) VALUES (%s,%s,%s,%s,%s,%s)",
                        (en, zh, atype, tier, org, est))
            award_ids[en] = cur.lastrowid
            print(f"  + awards: {en} ({zh})")

    cur.execute("SELECT id FROM occupations WHERE name_en='mathematician'")
    occ_id = cur.fetchone()[0]

    created = added = skipped_person = skipped_award = 0
    for name, awards in CROSS.items():
        pid = by_en.get(norm(name)) or by_zh.get(norm(name))
        if pid is None:
            cur.execute("INSERT INTO people(name_en, primary_occupation, has_biography) VALUES (%s,'mathematician',0)", (name,))
            pid = cur.lastrowid
            cur.execute("INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)", (pid, occ_id))
            by_en[norm(name)] = pid
            created += 1
            print(f"  + 占位: {name}")
        for award, year, note in awards:
            if award not in award_ids:
                print(f"  ⚠ awards 缺失: {award}（{name}）")
                skipped_award += 1
                continue
            if year == 0:
                note = "年份待查"
            cur.execute(
                "INSERT IGNORE INTO award_laureate(person_id, award_id, year, note, source) VALUES (%s,%s,%s,%s,'medal_list_allinone/all_cross_reference.md')",
                (pid, award_ids[award], year, note),
            )
            if cur.rowcount:
                added += 1
                print(f"    → {name}: {award} {year}")
    conn.commit()

    print(f"\n新建人物: {created} · 新增获奖记录: {added} · 缺失奖项跳过: {skipped_award}")
    cur.execute("SELECT COUNT(*) FROM award_laureate")
    print(f"award_laureate 总数: {cur.fetchone()[0]}")
    conn.close()


if __name__ == "__main__":
    main()
