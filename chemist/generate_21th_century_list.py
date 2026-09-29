#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 nobel_chemistry_citations.json 读取 21 世纪诺贝尔化学奖得主（2001–2025，含获奖理由），
与 20 世纪版（chemist/generate_20th_century_list.py）完全同构，生成含
「获奖理由 / 立传 / Review / 社会关系入库」列的结构化 md。

先运行 fetch_nobel_citations.py 生成 nobel_chemistry_citations.json，再运行本脚本。
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "nobel_chemistry_citations.json"
OUT = ROOT / "presentations" / "21th_century" / "OpenChemist_21th_Century_Nobel_Laureates.md"

# 已立传的化学家（姓名需与获奖者名单精确匹配）。
# 新增立传时在此补充姓名。
BIOGRAPHIES_DONE: set[str] = set()

# 已完成 Review（两轮事实核查）的化学家（姓名需与获奖者名单精确匹配）。
# 完成两轮 Review 后在此补充姓名。
REVIEWS_DONE: set[str] = set()

# 社会关系已入库 greatminds 库的化学家（姓名需与获奖者名单精确匹配）。
# 按 {Name}_zh.md 提示词 §7 清单完成 seed_person.py 入库后在此补充姓名。
SOCIAL_DONE: set[str] = {
    'Aaron Ciechanover',
    'Ada Yonath',
    'Akira Suzuki',
    'Akira Yoshino',
    'Alexey Ekimov',
    'Arieh Warshel',
    'Avram Hershko',
    'Aziz Sancar',
    'Ben Feringa',
    'Benjamin List',
    'Brian Kobilka',
    'Carolyn Bertozzi',
    'Dan Shechtman',
    'David Baker',
    'David W.C. MacMillan',
    'Demis Hassabis',
    'Ei-ichi Negishi',
    'Emmanuelle Charpentier',
    'Eric Betzig',
    'Frances Arnold',
    'Fraser Stoddart',
    'George P. Smith',
    'Gerhard Ertl',
    'Greg Winter',
    'Irwin Rose',
    'Jacques Dubochet',
    'Jean-Pierre Sauvage',
    'Jennifer Doudna',
    'Joachim Frank',
    'John B. Goodenough',
    'John Fenn',
    'John M. Jumper',
    'Karl Barry Sharpless',
    'Koichi Tanaka',
    'Kurt Wüthrich',
    'Louis E. Brus',
    'M. Stanley Whittingham',
    'Martin Chalfie',
    'Martin Karplus',
    'Michael Levitt',
    'Morten P. Meldal',
    'Moungi Bawendi',
    'Omar M. Yaghi',
    'Osamu Shimomura',
    'Paul L. Modrich',
    'Peter Agre',
    'Richard F. Heck',
    'Richard Henderson',
    'Richard R. Schrock',
    'Richard Robson',
    'Robert H. Grubbs',
    'Robert Lefkowitz',
    'Roderick MacKinnon',
    'Roger D. Kornberg',
    'Roger Y. Tsien',
    'Ryōji Noyori',
    'Stefan Hell',
    'Susumu Kitagawa',
    'Thomas A. Steitz',
    'Tomas Lindahl',
    'Venkatraman Ramakrishnan',
    'William E. Moerner',
    'William Standish Knowles',
    'Yves Chauvin',
}

# 获奖者英文名 → 中文名（诺贝尔化学奖得主常用中译）。
NAME_ZH = {
    "William Standish Knowles": "威廉·斯坦迪什·诺尔斯",
    "Ryōji Noyori": "野依良治",
    "Karl Barry Sharpless": "卡尔·巴里·夏普莱斯",
    "John Fenn": "约翰·芬恩",
    "Koichi Tanaka": "田中耕一",
    "Kurt Wüthrich": "库尔特·维特里希",
    "Peter Agre": "彼得·阿格雷",
    "Roderick MacKinnon": "罗德里克·麦金农",
    "Aaron Ciechanover": "阿龙·切哈诺沃",
    "Avram Hershko": "阿夫拉姆·赫什科",
    "Irwin Rose": "欧文·罗斯",
    "Yves Chauvin": "伊夫·肖万",
    "Robert H. Grubbs": "罗伯特·格拉布",
    "Richard R. Schrock": "理查德·施罗克",
    "Roger D. Kornberg": "罗杰·科恩伯格",
    "Gerhard Ertl": "格哈德·埃特尔",
    "Osamu Shimomura": "下村脩",
    "Martin Chalfie": "马丁·查尔菲",
    "Roger Y. Tsien": "钱永健",
    "Venkatraman Ramakrishnan": "文卡特拉曼·拉马克里希南",
    "Thomas A. Steitz": "托马斯·施泰茨",
    "Ada Yonath": "阿达·约纳特",
    "Richard F. Heck": "理查德·赫克",
    "Ei-ichi Negishi": "根岸英一",
    "Akira Suzuki": "铃木章",
    "Dan Shechtman": "达尼埃尔·谢赫特曼",
    "Robert Lefkowitz": "罗伯特·莱夫科维茨",
    "Brian Kobilka": "布赖恩·科比尔卡",
    "Martin Karplus": "马丁·卡普拉斯",
    "Michael Levitt": "迈克尔·莱维特",
    "Arieh Warshel": "亚利耶·瓦谢尔",
    "Eric Betzig": "埃里克·贝齐格",
    "Stefan Hell": "斯特凡·黑尔",
    "William E. Moerner": "威廉·莫尔纳",
    "Tomas Lindahl": "托马斯·林达尔",
    "Paul L. Modrich": "保罗·莫德里奇",
    "Aziz Sancar": "阿齐兹·桑贾尔",
    "Jean-Pierre Sauvage": "让-皮埃尔·索瓦日",
    "Fraser Stoddart": "弗雷泽·斯托达特",
    "Ben Feringa": "伯纳德·费林加",
    "Jacques Dubochet": "雅克·杜博歇",
    "Joachim Frank": "约阿希姆·弗兰克",
    "Richard Henderson": "理查德·亨德森",
    "Frances Arnold": "弗朗西丝·阿诺德",
    "George P. Smith": "乔治·史密斯",
    "Greg Winter": "格雷格·温特",
    "John B. Goodenough": "约翰·古迪纳夫",
    "M. Stanley Whittingham": "斯坦利·惠廷厄姆",
    "Akira Yoshino": "吉野彰",
    "Emmanuelle Charpentier": "埃玛纽埃勒·沙尔庞捷",
    "Jennifer Doudna": "珍妮弗·道德纳",
    "Benjamin List": "本亚明·利斯特",
    "David W.C. MacMillan": "大卫·麦克米伦",
    "Carolyn Bertozzi": "卡罗琳·贝尔托齐",
    "Morten P. Meldal": "莫滕·梅尔达尔",
    "Moungi Bawendi": "蒙吉·巴文迪",
    "Louis E. Brus": "路易斯·布鲁斯",
    "Alexey Ekimov": "阿列克谢·叶基莫夫",
    "David Baker": "戴维·贝克",
    "Demis Hassabis": "德米斯·哈萨比斯",
    "John M. Jumper": "约翰·江珀",
    "Susumu Kitagawa": "北川进",
    "Richard Robson": "理查德·罗布森",
    "Omar M. Yaghi": "奥马尔·亚吉",
}

# 获奖理由（Citation）英文原文 → 中文翻译（诺贝尔奖官方获奖理由中译）。
CITATION_ZH = {
    "for their work on chirally catalysed hydrogenation reactions":
        "表彰他们在手性催化氢化反应方面的工作",
    "for his work on chirally catalysed oxidation reactions":
        "表彰他在手性催化氧化反应方面的工作",
    "for the development of methods for identification and structure analyses of biological macromolecules, [especially] for their development of soft desorption ionisation methods for mass spectrometric analyses of biological macromolecules":
        "表彰他们开发了生物大分子的鉴定与结构分析方法，尤其是开发了生物大分子质谱分析中的软解吸电离方法",
    "for the development of methods for identification and structure analyses of biological macromolecules, [especially] for his development of nuclear magnetic resonance spectroscopy for determining the three-dimensional structure of biological macromolecules in solution":
        "表彰他开发了生物大分子的鉴定与结构分析方法，尤其是开发了用核磁共振波谱测定溶液中生物大分子三维结构的方法",
    "for discoveries concerning channels in cell membranes, [especially] for the discovery of water channels":
        "表彰他们发现了细胞膜中的通道，尤其是发现了水通道",
    "for discoveries concerning channels in cell membranes, [especially] for structural and mechanistic studies of ion channels":
        "表彰他们发现了细胞膜中的通道，尤其是对离子通道的结构与机理研究",
    "for the discovery of ubiquitin -mediated protein degradation":
        "表彰他们发现了泛素介导的蛋白质降解",
    "for the development of the metathesis method in organic synthesis":
        "表彰他们发展了有机合成中的复分解方法",
    "for his studies of the molecular basis of eukaryotic transcription":
        "表彰他对真核转录的分子基础的研究",
    "for his studies of chemical processes on solid surfaces":
        "表彰他对固体表面化学过程的研究",
    "for the discovery and development of the green fluorescent protein, GFP":
        "表彰他们发现并发展了绿色荧光蛋白（GFP）",
    "for studies of the structure and function of the ribosome":
        "表彰他们对核糖体结构和功能的研究",
    "for palladium-catalyzed cross couplings in organic synthesis":
        "表彰他们在有机合成中的钯催化交叉偶联",
    "for the discovery of quasicrystals":
        "表彰他发现了准晶体",
    "for studies of G-protein-coupled receptors":
        "表彰他们对 G 蛋白偶联受体的研究",
    "for the development of multiscale models for complex chemical systems":
        "表彰他们为复杂化学系统发展了多尺度模型",
    "for the development of super-resolved fluorescence microscopy":
        "表彰他们发展了超分辨荧光显微技术",
    "for mechanistic studies of DNA repair":
        "表彰他们对 DNA 修复机理的研究",
    "for the design and synthesis of molecular machines":
        "表彰他们设计并合成了分子机器",
    "for developing cryo-electron microscopy for the high-resolution structure determination of biomolecules in solution":
        "表彰他们开发了冷冻电子显微镜技术，实现了溶液中生物分子的高分辨率结构测定",
    "for the directed evolution of enzymes":
        "表彰她实现了酶的定向演化",
    "for the phage display of peptides and antibodies":
        "表彰他们实现了多肽和抗体的噬菌体展示技术",
    "for the development of lithium ion batteries":
        "表彰他们发展了锂离子电池",
    "for the development of a method for genome editing":
        "表彰她们开发了一种基因组编辑方法",
    "for the development of asymmetric organocatalysis":
        "表彰他们发展了不对称有机催化",
    "for the development of click chemistry and bioorthogonal chemistry":
        "表彰他们发展了点击化学和生物正交化学",
    "for the discovery and synthesis of quantum dots":
        "表彰他们发现并合成了量子点",
    "for computational protein design":
        "表彰他实现了计算蛋白质设计",
    "for protein structure prediction":
        "表彰他们实现了蛋白质结构预测",
    "for the development of metal–organic frameworks":
        "表彰他们发展了金属有机框架",
}


def _norm_citation(s: str) -> str:
    """规范化获奖理由文本：折叠空白、去掉标点前空格，使其与字典 key 对齐。"""
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"\s+([.,;:])", r"\1", s)
    return s


def _norm_country(s: str) -> str:
    """折叠国籍中的多余空白（如 'Romanian  German'）。"""
    return re.sub(r"\s+", " ", s or "").strip()


def main() -> int:
    if not SRC.exists():
        print(f"✗ 缺少获奖理由数据：{SRC}")
        print("  请先运行：python3 fetch_nobel_citations.py")
        return 1

    data = json.loads(SRC.read_text(encoding="utf-8"))
    # 仅保留 21 世纪（2001–2025）
    rows = [r for r in data if r.get("year") and 2001 <= r["year"] <= 2025]
    rows.sort(key=lambda r: r["year"])

    total_items = len(rows)
    names = [r["name"] for r in rows]
    unique_people = set(names)

    # 两度获奖者
    cnt = Counter(names)
    double = {k for k, v in cnt.items() if v > 1}

    # 女性获奖者（21 世纪）
    women = {"Ada Yonath", "Frances Arnold", "Emmanuelle Charpentier", "Jennifer Doudna"}

    # 国籍分布
    country_counter = Counter(_norm_country(r["country"]) for r in rows)

    # 立传 / Review / 社会关系入库状态（去重计数，避免两度获奖者被重复统计）
    done_count = len({r["name"] for r in rows if r["name"] in BIOGRAPHIES_DONE})
    review_count = len({r["name"] for r in rows if r["name"] in REVIEWS_DONE})
    social_count = len({r["name"] for r in rows if r["name"] in SOCIAL_DONE})

    lines: list[str] = []
    lines.append("# 21 世纪诺贝尔化学奖得主 — OpenChemist 名录\n")
    lines.append(
        "> **本名录收录 2001–2025 年诺贝尔化学奖得主，共 %d 项 / %d 位。**\n"
        ">\n"
        "> 从 Knowles 与 Noyori 的手性催化到 Baker/Hassabis/Jumper 的蛋白质结构预测：四分之一个世纪，化学奖见证了化学与生命科学、材料科学的深度融合。\n"
        ">\n"
        "> 获奖理由为诺贝尔奖官方获奖理由（中文翻译）；「立传」表示是否已生成立传 Beamer，「Review」表示是否已完成事实核查，「社会关系入库」表示是否已按提示词 §7 清单将社会关系入库 greatminds 库。\n"
        ">\n"
        "> 数据来源：英文维基百科「List of Nobel laureates in Chemistry」。\n"
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
        country = _norm_country(r["country"]) or "—"
        citation_en = _norm_citation(r["citation"])
        citation = CITATION_ZH.get(citation_en, citation_en).replace("|", "/")  # 转义表格竖线
        bio = "✅" if name in BIOGRAPHIES_DONE else "🔲"
        review = "✅" if name in REVIEWS_DONE else "🔲"
        social = "✅" if name in SOCIAL_DONE else "🔲"
        lines.append("| %d | %s | %s | %s | %s | %s | %s |" % (r["year"], name_display, country, citation, bio, review, social))

    lines.append("\n---\n")
    lines.append("\n## 二、统计说明\n")
    lines.append("\n- **获奖年份跨度**：2001–2025")
    lines.append("- **获奖总项数**：%d 项" % total_items)
    lines.append("- **获奖总人数**：%d 位" % len(unique_people))
    lines.append("- **已立传**：%d 位（%s）" % (done_count, "、".join(sorted(BIOGRAPHIES_DONE)) if BIOGRAPHIES_DONE else "暂无"))
    lines.append("- **已 Review**：%d 位（%s）" % (review_count, "、".join(sorted(REVIEWS_DONE)) if REVIEWS_DONE else "暂无"))
    lines.append("- **社会关系已入库**：%d 位（%s）" % (social_count, "、".join(sorted(SOCIAL_DONE)) if SOCIAL_DONE else "暂无"))
    if double:
        lines.append("- **两度获奖者**：" + "、".join(sorted(double)) + "（继 Frederick Sanger 之后第二位两度获诺贝尔化学奖者）")
    if women:
        w = [x for x in sorted(women) if x in unique_people]
        if w:
            lines.append("- **女性获奖者**（21 世纪）：" + "、".join(w))

    lines.append("\n### 国籍分布\n")
    lines.append("\n| 国籍 | 人数 |")
    lines.append("|------|:--:|")
    for c, n in country_counter.most_common():
        lines.append("| %s | %d |" % (c, n))

    lines.append("\n---\n")
    lines.append(
        "\n> **这不是一份排名，而是一部仍在书写的化学历程：每一项获奖都标记着人类对自然认识的一次跃迁。**\n"
    )

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("wrote:", OUT)
    print("总项数:", total_items, "总人数:", len(unique_people), "两度获奖:", sorted(double))
    print("已立传:", done_count, "位", "已 Review:", review_count, "位")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
