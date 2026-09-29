#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 nobel_literature_citations.json 读取 21 世纪诺贝尔文学奖得主（2001–2025，含获奖理由），
参考 20 世纪侧文档形式，生成含「获奖理由 / 立传 / Review / 社会关系入库」列的结构化 md。

先运行 fetch_nobel_citations.py 生成 nobel_literature_citations.json，再运行本脚本。
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "nobel_literature_citations.json"
OUT = ROOT / "presentations" / "21st_century" / "OpenLiterature_21st_Century_Nobel_Laureates.md"

# 已立传 / 已 Review / 已社会关系入库（与 20 世纪侧同名机制，按获奖者姓名精确匹配）
BIOGRAPHIES_DONE: set[str] = set()
REVIEWS_DONE: set[str] = set()
# 已完成社会关系入库（研究领域 + 社会关系写入 greatminds 库）的文学家。
# 2026-09-29 批次（lit21-bios-2026，5 批 agent）已全部入库，此处按 citations json 全量置位。
def _relations_done() -> set[str]:
    try:
        data = json.loads((ROOT / "nobel_literature_citations.json").read_text(encoding="utf-8"))
        return {r["name"] for r in data if r.get("year") and r["year"] > 2000}
    except Exception:
        return set()

RELATIONS_DONE: set[str] = _relations_done()

# 库名 → 名单显示中文名
NAME_ZH = {
    "Vidiadhar Surajprasad Naipaul": "V. S. 奈保尔",
    "V. S. Naipaul": "V. S. 奈保尔",
    "Imre Kertész": "伊姆雷·凯尔泰斯",
    "John Maxwell Coetzee": "约翰·马克斯韦尔·库切",
    "J. M. Coetzee": "约翰·马克斯韦尔·库切",
    "Elfriede Jelinek": "埃尔弗里德·耶利内克",
    "Harold Pinter": "哈罗德·品特",
    "Orhan Pamuk": "奥尔罕·帕慕克",
    "Doris Lessing": "多丽丝·莱辛",
    "Jean-Marie Gustave Le Clézio": "让-马里·古斯塔夫·勒克莱齐奥",
    "J. M. G. Le Clézio": "让-马里·古斯塔夫·勒克莱齐奥",
    "Herta Müller": "赫塔·米勒",
    "Mario Vargas Llosa": "马里奥·巴尔加斯·略萨",
    "Tomas Tranströmer": "托马斯·特兰斯特勒默",
    "Mo Yan": "莫言",
    "Alice Munro": "艾丽丝·门罗",
    "Patrick Modiano": "帕特里克·莫迪亚诺",
    "Svetlana Alexievich": "斯韦特兰娜·阿列克西耶维奇",
    "Bob Dylan": "鲍勃·迪伦",
    "Kazuo Ishiguro": "石黑一雄",
    "Olga Tokarczuk": "奥尔加·托卡尔丘克",
    "Peter Handke": "彼得·汉德克",
    "Louise Glück": "露易丝·格丽克",
    "Abdulrazak Gurnah": "阿卜杜勒拉扎克·古尔纳",
    "Annie Ernaux": "安妮·埃尔诺",
    "Jon Fosse": "约恩·福瑟",
    "Han Kang": "韩江",
    "László Krasznahorkai": "拉斯洛·克拉斯诺霍尔卡伊",
}

# 官方获奖理由中译（key = (年份字符串, 姓名)）
CITATION_ZH = {
    ("2001", "Vidiadhar Surajprasad Naipaul"): "表彰其将敏锐的叙事与不屈的审视融于著作之中，促使我们看到被压抑的历史之存在",
    ("2002", "Imre Kertész"): "表彰其写作在历史的野蛮专断面前，维护了个体脆弱的经验",
    ("2003", "John Maxwell Coetzee"): "表彰其以无数种面貌描绘了局外人的惊人卷入",
    ("2004", "Elfriede Jelinek"): "表彰其小说与戏剧中声音与反声音的音乐般流动，以非凡的语言激情揭示了社会陈词滥调的荒诞及其压制力量",
    ("2005", "Harold Pinter"): "表彰其戏剧揭开日常闲谈之下的深渊，强行闯入压迫的封闭房间",
    ("2006", "Orhan Pamuk"): "表彰其在探寻故乡城市忧郁灵魂的途中，为文化的冲突与交织发现了新的象征",
    ("2007", "Doris Lessing"): "表彰这位女性经验的史诗作家，以怀疑、火焰与远见之力使分裂的文明接受审视",
    ("2008", "Jean-Marie Gustave Le Clézio"): "表彰这位新出发、诗意冒险与感官狂喜的作者，在主流文明之外与之下探索人性",
    ("2009", "Herta Müller"): "表彰其以诗的凝练与散文的坦率，描绘了被剥夺者的风景",
    ("2010", "Mario Vargas Llosa"): "表彰其权力结构的图谱，以及其对个人的抗拒、反叛与失败的有力刻画",
    ("2011", "Tomas Tranströmer"): "表彰其通过凝练而透澈的意象，让我们以崭新的方式接近现实",
    ("2012", "Mo Yan"): "表彰其以魔幻现实主义融合民间故事、历史与当代",
    ("2013", "Alice Munro"): "当代短篇小说大师",
    ("2014", "Patrick Modiano"): "表彰其记忆的艺术，唤起了最难以把握的人类命运，揭示了被占领时期的生命世界",
    ("2015", "Svetlana Alexievich"): "表彰其复调式写作，是我们时代苦难与勇气的纪念碑",
    ("2016", "Bob Dylan"): "表彰其在伟大的美国歌曲传统中创造了全新的诗意表达",
    ("2017", "Kazuo Ishiguro"): "表彰其以巨大情感力量的小说，揭示了我们与世界虚幻联结感之下的深渊",
    ("2018", "Olga Tokarczuk"): "表彰其叙事想象力，以百科全书式的激情将跨越边界表现为一种生命形式",
    ("2019", "Peter Handke"): "表彰其以语言的巧思探索人类经验之边缘与特质的有力作品",
    ("2020", "Louise Glück"): "表彰其无可误认的诗之声，以朴素的美使个体的存在具有普遍性",
    ("2021", "Abdulrazak Gurnah"): "表彰其对殖民主义之影响与难民之命运的毫不妥协而富于同情的洞察——那横亘于文化与大陆之间的鸿沟",
    ("2022", "Annie Ernaux"): "表彰其以勇气与临床般的敏锐，揭示个人记忆的根源、隔阂与集体桎梏",
    ("2023", "Jon Fosse"): "表彰其创新的戏剧与散文，为不可言说者发出了声音",
    ("2024", "Han Kang"): "表彰其浓烈的诗性散文直面历史创伤，暴露出人类生命的脆弱",
    ("2025", "László Krasznahorkai"): "表彰其引人入胜而富于远见的作品，在末世般的恐惧中重申了艺术的力量",
}

# 女性获奖者（21 世纪）
WOMEN = {
    "Elfriede Jelinek",
    "Doris Lessing",
    "Herta Müller",
    "Alice Munro",
    "Svetlana Alexievich",
    "Louise Glück",
    "Olga Tokarczuk",
    "Annie Ernaux",
    "Han Kang",
}

# 国籍列切分用的国家/地区词表（含多词国名；匹配时忽略大小写，要求词边界）。
COUNTRY_VOCAB = [
    "Trinidad and Tobago", "United Kingdom", "United States", "Soviet Union",
    "South Korea", "South Africa", "Saint Lucia", "West Germany", "Austria-Hungary",
    "Czechoslovakia", "Switzerland", "Netherlands", "Yugoslavia", "Guatemala",
    "France", "Germany", "Norway", "Spain", "Poland", "Italy", "Sweden",
    "Belgium", "Denmark", "India", "Ireland", "Chile", "Finland", "Iceland",
    "Israel", "Greece", "Japan", "Australia", "Austria", "Colombia", "Nigeria",
    "Egypt", "Mexico", "Portugal", "Turkey", "Hungary", "Canada", "Bulgaria",
    "Romania", "Mauritius", "Peru", "China", "Tanzania", "Belarus", "Stateless",
]


def clean_country(s: str) -> str:
    """清洗国籍列：去掉脚注与括号（语言/出生地），再按国家词表切分多国籍串。"""
    if not s:
        return ""
    s = re.sub(r"\[\s*\d+\s*\]", "", s)
    s = re.sub(r"\([^)]*\)", " ", s)
    s = s.strip()
    out: list[str] = []
    i = 0
    while i < len(s):
        hit = None
        for c in COUNTRY_VOCAB:
            if s[i:].lower().startswith(c.lower()):
                j = i + len(c)
                if j == len(s) or s[j] == " ":
                    hit = c
                    break
        if hit:
            if not out or out[-1] != hit:
                out.append(hit)
            i += len(hit)
        else:
            i += 1
    return " / ".join(out) if out else s


def main() -> int:
    if not SRC.exists():
        print(f"✗ 缺少获奖理由数据：{SRC}")
        print("  请先运行：python3 fetch_nobel_citations.py")
        return 1

    data = json.loads(SRC.read_text(encoding="utf-8"))
    # 仅保留 21 世纪（2001–2025）
    rows = [r for r in data if r.get("year") and r["year"] > 2000]
    rows.sort(key=lambda r: r["year"])

    total_items = len(rows)
    names = [r["name"] for r in rows]
    unique_people = set(names)

    # 两度获奖者（21 世纪暂无）
    cnt = Counter(names)
    double = {k for k, v in cnt.items() if v > 1}

    # 国籍分布
    country_counter = Counter(clean_country(r["country"]) for r in rows)

    # 立传 / Review / 社会关系入库 状态
    done_count = sum(1 for r in rows if r["name"] in BIOGRAPHIES_DONE)
    review_count = sum(1 for r in rows if r["name"] in REVIEWS_DONE)
    relations_count = sum(1 for r in rows if r["name"] in RELATIONS_DONE)

    lines: list[str] = []
    lines.append("# 21 世纪诺贝尔文学奖得主 — OpenLiterature 名录\n")
    lines.append(
        "> **本名录收录 2001–2025 年诺贝尔文学奖得主，共 %d 项 / %d 位。**\n"
        ">\n"
        "> 从奈保尔的流离书写到韩江的历史创伤：四分之一个世纪里，文学奖持续追问个体记忆、殖民伤疤与文明裂隙。\n"
        ">\n"
        "> 获奖理由为诺贝尔奖官方获奖理由（中文翻译）；「立传」表示是否已生成立传 Beamer，「Review」表示是否已完成事实核查，「社会关系入库」表示是否已将研究领域与社会关系写入 greatminds 数据库（people / person_relation / person_field）。\n"
        ">\n"
        "> 数据来源：英文维基百科「List of Nobel laureates in Literature」。\n"
        % (total_items, len(unique_people))
    )
    lines.append("---\n")

    lines.append("\n## 一、完整名单（按年份）\n")
    lines.append("\n| 年份 | 获奖者 | 国籍 | 获奖理由 | 立传 | Review | 社会关系入库 |")
    lines.append("|:--:|------|------|------|:--:|:--:|:--:|")
    for r in rows:
        name = r["name"]
        zh = NAME_ZH.get(name)
        name_display = f"{name} ({zh})" if zh else name
        country = clean_country(r["country"]) or "—"
        citation = CITATION_ZH.get((str(r["year"]), name), r["citation"])
        citation = re.sub(r"\s+", " ", citation).replace("|", "/").strip().strip('"')
        bio = "✅" if name in BIOGRAPHIES_DONE else "🔲"
        review = "✅" if name in REVIEWS_DONE else "🔲"
        relation = "✅" if name in RELATIONS_DONE else "🔲"
        lines.append("| %d | %s | %s | %s | %s | %s | %s |" % (r["year"], name_display, country, citation, bio, review, relation))

    lines.append("\n---\n")
    lines.append("\n## 二、统计说明\n")
    lines.append("\n- **获奖年份跨度**：2001–2025")
    lines.append("- **获奖总项数**：%d 项" % total_items)
    lines.append("- **获奖总人数**：%d 位" % len(unique_people))
    lines.append("- **已立传**：%d 位（%s）" % (done_count, "、".join(sorted(BIOGRAPHIES_DONE)) if BIOGRAPHIES_DONE else "暂无"))
    lines.append("- **已 Review**：%d 位（%s）" % (review_count, "、".join(sorted(REVIEWS_DONE)) if REVIEWS_DONE else "暂无"))
    lines.append("- **已社会关系入库**：%d 位（%s）" % (relations_count, "、".join(sorted(RELATIONS_DONE)) if RELATIONS_DONE else "暂无"))
    if double:
        lines.append("- **两度获奖者**：" + "、".join(sorted(double)))
    if WOMEN:
        w = [x for x in sorted(WOMEN) if x in unique_people]
        if w:
            lines.append("- **女性获奖者**（21 世纪，%d 位）：%s" % (len(w), "、".join(w)))

    lines.append("\n### 国籍分布\n")
    lines.append("\n| 国籍 | 人数 |")
    lines.append("|------|:--:|")
    for c, n in country_counter.most_common():
        lines.append("| %s | %d |" % (c, n))

    lines.append("\n---\n")
    lines.append(
        "\n> **这不是一份排名，而是一段正在展开的文学当下：每一项获奖都标记着我们时代自我理解的一次刷新。**\n"
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("wrote:", OUT)
    print("总项数:", total_items, "总人数:", len(unique_people), "两度获奖:", sorted(double))
    print("已立传:", done_count, "位", "已 Review:", review_count, "位", "已社会关系入库:", relations_count, "位")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
