#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全量奖项补录 —— 对已立传的 11 人（id 1-11）按 §21.2.4「全部收录」原则补齐 metadata 中的全部获奖记录。

覆盖：Hilbert / Poincaré / von Neumann / Noether / Kolmogorov / Weyl / Grothendieck / Weil / Turing / Gödel / Banach

原则（§21.2.4）：
- metadata award_received 全部收录，含追授（如 Banach White Eagle 2018）、政治勋章（苏联勋章）、名誉类（Guggenheim）
- award_type 承担分类过滤职责，不做入库剔除
- 年份：优先 YEAR_HINTS（page.md/提示词已知）；未知置 0，note 标注「年份待查」

幂等：INSERT IGNORE。
"""
import glob
import json
import os
import re
import unicodedata

from db_mysql import get_conn

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "mathematician", "pages")

# (人名, 奖项名) -> 年份；未列出且不在库中的年份置 0（待查）
YEAR_HINTS = {
    ("David Hilbert", "Goethe Medal for Art and Science"): 1932,
    ("John von Neumann", "Navy Distinguished Civilian Service"): 1946,
    ("John von Neumann", "Albert Einstein Award"): 1956,
    ("Andrey Kolmogorov", "Stalin Prize"): 1941,
    ("Andrey Kolmogorov", "Lenin Prize"): 1965,
    ("Hermann Weyl", "Pour le Mérite for Sciences and Arts order"): 1955,
    ("Stefan Banach", "Order of the White Eagle"): 2018,
}

# 中文名翻译（仅对新补字典的奖项）
TRANSLATE = {
    "Pour le Mérite for Sciences and Arts order": "功勋勋章（科学与艺术）",
    "Poncelet Prize": "彭赛列奖",
    "Cothenius Medal": "科特尼乌斯奖章",
    "Bavarian Maximilian Order for Science and Art": "巴伐利亚马克西米利安科学与艺术勋章",
    "Goethe Medal for Art and Science": "歌德艺术与科学奖章",
    "Legion of Honour": "荣誉军团勋章",
    "Royal Order of the Polar Star": "北极星勋章",
    "Concours général": "全国会考奖（Concours général）",
    "Jean Reynaud Prize": "让·雷诺奖",
    "Navy Distinguished Civilian Service": "海军杰出文职服务奖",
    "Silliman Memorial Lectures": "西利曼纪念讲座",
    "Financial Times Person of the Year": "金融时报年度人物",
    "Fellow of the Institute of Mathematical Statistics": "数理统计学会会士",
    "Fellow of the Econometric Society": "计量经济学会会士",
    "Stalin Prize": "斯大林奖",
    "Lenin Prize": "列宁奖",
    "Order of Lenin": "列宁勋章",
    "Hero of Socialist Labour": "社会主义劳动英雄",
    "Order of the October Revolution": "十月革命勋章",
    "Order of the Patriotic War, 1st class": "一级卫国战争勋章",
    "Order of the Red Banner of Labour": "劳动红旗勋章",
    "Helmholtz Medal": "亥姆霍兹奖章",
    "P.L. Chebyshev Gold Medal": "契比雪夫金质奖章",
    "Fellow of the American Physical Society": "美国物理学会会士",
    "Arnold-Reymond Prize": "阿诺德-雷蒙奖",
    "Cours Peccot": "佩科课程奖",
    "Guggenheim Fellowship": "古根海姆研究基金",
    "Prix Francoeur": "弗朗科尔奖",
    "honorary doctorate": "荣誉博士",
}

# 忽略的通用尾词（用于复用字典已有项，如字典 "Pour le Mérite for Sciences and Arts" 与 metadata "…order"）
TAIL_WORDS = [" order", " award", " medal", " prize", " for sciences and arts"]


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def main():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("SELECT id, name_en FROM people WHERE id<=50 ORDER BY id")
    people = cur.fetchall()

    cur.execute("SELECT id, name_en FROM awards")
    award_ids = {norm(n): (i, n) for i, n in cur.fetchall()}

    cur.execute("SELECT person_id, award_id FROM award_laureate")
    have = set(cur.fetchall())

    added_award = 0
    added_laureate = 0
    unknown_year = []
    no_zh = []

    # pages 目录名与库中 name_en 不一致的别名映射
    DIR_ALIAS = {
        "J.-P. Serre": "Jean-Pierre Serre",
        "陈省身": "Shiing-Shen Chern",
        "R.A. Fisher": "Ronald Fisher",
        "G.H. Hardy": "G.H. Hardy",
        "J.E. Littlewood": "J.E. Littlewood",
        "L.E.J. Brouwer": "L.E.J. Brouwer",
    }

    for pid, name_en in people:
        # 定位 pages 目录（按 norm 匹配；失败时尝试别名）
        cand_name = DIR_ALIAS.get(name_en, name_en)
        pdir = None
        for cand in glob.glob(os.path.join(ROOT, "*")):
            if norm(os.path.basename(cand)) == norm(cand_name):
                pdir = cand
                break
        if pdir is None:
            print(f"⚠ 无 pages 目录: {name_en}")
            continue
        meta_path = os.path.join(pdir, "metadata.json")
        if not os.path.exists(meta_path):
            print(f"⚠ 无 metadata.json: {name_en}")
            continue
        try:
            awards = json.load(open(meta_path)).get("properties", {}).get("award_received", [])
        except Exception as e:
            print(f"⚠ 解析失败 {name_en}: {e}")
            continue
        if not awards:
            continue
        print(f"\n== {name_en} (id={pid}): {len(awards)} 项")
        for aw in awards:
            if not isinstance(aw, str):
                continue
            key = norm(aw)
            # 匹配字典：精确 -> 去尾词
            aid, match_en = None, None
            if key in award_ids:
                aid, match_en = award_ids[key]
            else:
                for tw in TAIL_WORDS:
                    cand = aw
                    if cand.endswith(tw) and cand != tw.strip():
                        cand2 = cand[: -len(tw)]
                        k2 = norm(cand2)
                        if k2 in award_ids:
                            aid, match_en = award_ids[k2]
                            break
            if aid is None:
                # 补字典
                zh = TRANSLATE.get(aw, aw)
                cur.execute(
                    "INSERT INTO awards(name_en, name_zh, award_type, tier) VALUES (%s,%s,'honor',NULL)",
                    (aw, zh),
                )
                aid = cur.lastrowid
                award_ids[key] = (aid, aw)
                award_ids[norm(aw + " award")] = (aid, aw)
                added_award += 1
                if zh == aw:
                    no_zh.append(aw)
                print(f"  + 字典: {aw} ({zh})")
            if (pid, aid) in have:
                print(f"  · 已有: {match_en or aw}")
                continue
            year = YEAR_HINTS.get((name_en, aw), YEAR_HINTS.get(aw, 0))
            note = None
            if year == 0:
                year = 0
                note = "年份待查（metadata 无年份）"
                unknown_year.append(f"{name_en}: {aw}")
            cur.execute(
                "INSERT IGNORE INTO award_laureate(person_id, award_id, year, note, source) "
                "VALUES (%s,%s,%s,%s,'metadata award_received')",
                (pid, aid, year, note),
            )
            if cur.rowcount:
                added_laureate += 1
                have.add((pid, aid))
                print(f"  → +奖: {match_en or aw} ({year})")

    conn.commit()
    print("\n" + "=" * 50)
    print(f"新增字典: {added_award} · 新增获奖: {added_laureate}")
    if unknown_year:
        print(f"\n⚠ 年份待查 ({len(unknown_year)}):")
        for u in unknown_year:
            print("   ", u)
    if no_zh:
        print(f"\n⚠ 待补中文名 ({len(no_zh)}):")
        for z in no_zh:
            print("   ", z)
    cur.execute("SELECT COUNT(*) FROM awards"); print(f"awards 总数: {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(*) FROM award_laureate"); print(f"award_laureate 总数: {cur.fetchone()[0]}")
    conn.close()


if __name__ == "__main__":
    main()
