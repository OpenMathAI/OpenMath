#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 21 世纪诺贝尔物理学奖得主名录（2001–2025，68 位）。

数据源：
- presentations/21th_century/21st_century/INDEX.md（年份/人名/目录）
- nobel_physics_citations.json（Nobel 官方获奖理由与 country，≥2001 段）
- 各人 page.md frontmatter（wikidata QID）
- greatminds 库（people.has_social_data / has_biography 按 QID 直查）

输出：presentations/21th_century/OpenPhysicist_21st_Century_Nobel_Laureates.md
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAGES = ROOT / "presentations" / "21th_century" / "21st_century"
INDEX = PAGES / "INDEX.md"
SRC = ROOT / "nobel_physics_citations.json"
OUT = ROOT / "presentations" / "21th_century" / "OpenPhysicist_21st_Century_Nobel_Laureates.md"

sys.path.insert(0, str(ROOT.parent / "MySQL"))

# 已立传 / 已 Review / 已社会关系入库（与 20 世纪侧同名机制，按 INDEX 人名精确匹配）
BIOGRAPHIES_DONE: set[str] = set()
REVIEWS_DONE: set[str] = set()

# 库名 → 名单显示中文名
NAME_ZH = {
    "Eric A. Cornell": "埃里克·康奈尔",
    "Wolfgang Ketterle": "沃尔夫冈·克特勒",
    "Carl E. Wieman": "卡尔·维曼",
    "Raymond Davis Jr.": "雷蒙德·戴维斯",
    "Masatoshi Koshiba": "小柴昌俊",
    "Riccardo Giacconi": "里卡尔多·贾科尼",
    "Alexei A. Abrikosov": "阿列克谢·阿布里科索夫",
    "Vitaly L. Ginzburg": "维塔利·金兹堡",
    "Anthony J. Leggett": "安东尼·莱格特",
    "David J. Gross": "戴维·格罗斯",
    "H. David Politzer": "休·波利策",
    "Frank Wilczek": "弗兰克·维尔切克",
    "Roy J. Glauber": "罗伊·格劳伯",
    "John L. Hall": "约翰·霍尔",
    "Theodor W. Hänsch": "特奥多尔·亨施",
    "John C. Mather": "约翰·马瑟",
    "George F. Smoot": "乔治·斯穆特",
    "Albert Fert": "阿尔贝·费尔",
    "Peter Grünberg": "彼得·格林贝格",
    "Yoichiro Nambu": "南部阳一郎",
    "Makoto Kobayashi": "小林诚",
    "Toshihide Maskawa": "益川敏英",
    "Charles Kuen Kao": "高锟",
    "Willard S. Boyle": "威拉德·博伊尔",
    "George E. Smith": "乔治·史密斯",
    "Andre Geim": "安德烈·海姆",
    "Konstantin Novoselov": "康斯坦丁·诺沃肖洛夫",
    "Saul Perlmutter": "索尔·珀尔马特",
    "Brian P. Schmidt": "布莱恩·施密特",
    "Adam G. Riess": "亚当·里斯",
    "Serge Haroche": "塞尔日·阿罗什",
    "David J. Wineland": "戴维·瓦恩兰",
    "François Englert": "弗朗索瓦·恩格勒",
    "Peter W. Higgs": "彼得·希格斯",
    "Isamu Akasaki": "赤崎勇",
    "Hiroshi Amano": "天野浩",
    "Shuji Nakamura": "中村修二",
    "Takaaki Kajita": "梶田隆章",
    "Arthur B. McDonald": "阿瑟·麦克唐纳",
    "David J. Thouless": "大卫·索利斯",
    "F. Duncan M. Haldane": "邓肯·霍尔丹",
    "J. Michael Kosterlitz": "迈克尔·科斯特利茨",
    "Rainer Weiss": "雷纳·韦斯",
    "Barry C. Barish": "巴里·巴里什",
    "Kip S. Thorne": "基普·索恩",
    "Arthur Ashkin": "亚瑟·阿斯金",
    "Gérard Mourou": "热拉尔·穆鲁",
    "Donna Strickland": "唐娜·斯特里克兰",
    "James Peebles": "詹姆斯·皮布尔斯",
    "Michel Mayor": "米歇尔·马约尔",
    "Didier Queloz": "迪迪埃·奎洛兹",
    "Roger Penrose": "罗杰·彭罗斯",
    "Reinhard Genzel": "赖因哈德·根策尔",
    "Andrea Ghez": "安德烈娅·盖兹",
    "Syukuro Manabe": "真锅淑郎",
    "Klaus Hasselmann": "克劳斯·哈塞尔曼",
    "Giorgio Parisi": "乔治·帕里西",
    "Alain Aspect": "阿兰·阿斯佩",
    "John F. Clauser": "约翰·克劳泽",
    "Anton Zeilinger": "安东·蔡林格",
    "Pierre Agostini": "皮埃尔·阿戈斯蒂尼",
    "Ferenc Krausz": "费伦茨·克劳斯",
    "Anne L'Huillier": "安妮·吕利耶",
    "John J. Hopfield": "约翰·霍普菲尔德",
    "Geoffrey Hinton": "杰弗里·辛顿",
    "John Clarke": "约翰·克拉克",
    "Michel H. Devoret": "米歇尔·德沃雷",
    "John M. Martinis": "约翰·马蒂尼斯",
}

# 官方获奖理由中译（key = _norm_citation 后的英文原文）
CITATION_ZH = {
    "For the achievement of Bose-Einstein condensation in dilute gases of alkali atoms, and for early fundamental studies of the properties of the condensates.":
        "表彰他们成功实现碱金属原子稀薄气体中的玻色–爱因斯坦凝聚，并对凝聚体性质进行了早期基础研究",
    "For pioneering contributions to astrophysics, in particular for the detection of cosmic neutrinos.":
        "表彰他们在天体物理学领域的开创性贡献，尤其是宇宙中微子的探测",
    "For pioneering contributions to astrophysics, which have led to the discovery of cosmic X-ray sources.":
        "表彰他们在天体物理学领域的开创性贡献，这些贡献促成了宇宙 X 射线源的发现",
    "For pioneering contributions to the theory of superconductors and superfluids.":
        "表彰他们在超导体和超流体理论上的开创性贡献",
    "For the discovery of asymptotic freedom in the theory of the strong interaction.":
        "表彰他们发现强相互作用理论中的渐近自由",
    "For his contribution to the quantum theory of optical coherence.":
        "表彰他对光学相干的量子理论的贡献",
    "For their contributions to the development of laser-based precision spectroscopy, including the optical frequency comb technique.":
        "表彰他们对基于激光的精密光谱学发展的贡献，包括光学频率梳技术",
    "For their discovery of the blackbody form and anisotropy of the cosmic microwave background radiation.":
        "表彰他们发现宇宙微波背景辐射的黑体形态和各向异性",
    "For the discovery of Giant Magnetoresistance.":
        "表彰他们发现巨磁阻效应",
    "For the discovery of the mechanism of spontaneous broken symmetry in subatomic physics.":
        "表彰他发现亚原子物理中自发对称性破缺的机制",
    "For the discovery of the origin of the broken symmetry which predicts the existence of at least three families of quarks in nature.":
        "表彰他们发现对称性破缺的起源，该理论预言了自然界中至少存在三代夸克",
    "For groundbreaking achievements concerning the transmission of light in fibers for optical communication.":
        "表彰他们在光学通信领域光纤传输方面取得的开创性成就",
    "For the invention of an imaging semiconductor circuit - the CCD sensor.":
        "表彰他们发明了成像半导体电路——CCD 传感器",
    "For groundbreaking experiments regarding the two-dimensional material graphene.":
        "表彰他们在二维材料石墨烯方面开展的开创性实验",
    "For the discovery of the accelerating expansion of the Universe through observations of distant supernovae.":
        "表彰他们通过观测遥远超新星，发现宇宙的加速膨胀",
    "For ground-breaking experimental methods that enable measuring and manipulation of individual quantum systems.":
        "表彰他们突破性的实验方法，使测量和操控单个量子系统成为可能",
    "For the theoretical discovery of a mechanism that contributes to our understanding of the origin of mass of subatomic particles, and which recently was confirmed through the discovery of the predicted fundamental particle, by the ATLAS and CMS experiments at CERN's Large Hadron Collider.":
        "表彰他们从理论上发现一种有助于理解亚原子粒子质量起源的机制，并经 CERN 大型强子对撞机 ATLAS 与 CMS 实验通过发现所预言的基本粒子而近期得到证实",
    "For the invention of efficient blue light-emitting diodes which has enabled bright and energy-saving white light sources.":
        "表彰他们发明高效蓝色发光二极管，催生出明亮而节能的白色光源",
    "For the discovery of neutrino oscillations, which shows that neutrinos have mass.":
        "表彰他们发现中微子振荡，表明中微子具有质量",
    "For theoretical discoveries of topological phase transitions and topological phases of matter.":
        "表彰他们拓扑相变和物质拓扑相方面的理论发现",
    "For decisive contributions to the LIGO detector and the observation of gravitational waves.":
        "表彰他们对 LIGO 探测器的决定性贡献以及引力波的观测",
    "For the optical tweezers and their application to biological systems.":
        "表彰他发明光镊及其在生物系统中的应用",
    "For their method of generating high-intensity, ultra-short optical pulses.":
        "表彰他们产生高强度超短光脉冲的方法",
    "For theoretical discoveries in physical cosmology.":
        "表彰他在物理宇宙学方面的理论发现",
    "For the discovery of an exoplanet orbiting a solar-type star.":
        "表彰他们发现围绕类太阳恒星运行的系外行星",
    "For the discovery that black hole formation is a robust prediction of the general theory of relativity.":
        "表彰他发现黑洞形成是广义相对论的稳健预言",
    "For the discovery of a supermassive compact object at the centre of our galaxy.":
        "表彰他们发现银河系中心的超大质量致密天体",
    "For the physical modelling of Earth's climate, quantifying variability and reliably predicting global warming.":
        "表彰他们建立地球气候的物理模型，量化其变率并可靠地预测全球变暖",
    "For the discovery of the interplay of disorder and fluctuations in physical systems from atomic to planetary scales.":
        "表彰他发现从原子到行星尺度物理系统中无序与涨落的相互作用",
    "For experiments with entangled photons, establishing the violation of Bell inequalities and pioneering quantum information science.":
        "表彰他们用纠缠光子进行实验，证伪贝尔不等式并开创量子信息科学",
    "For experimental methods that generate attosecond pulses of light for the study of electron dynamics in matter.":
        "表彰他们创造用于研究物质中电子动力学的阿秒光脉冲实验方法",
    "For foundational discoveries and inventions that enable machine learning with artificial neural networks.":
        "表彰他们基于人工神经网络实现机器学习的基础性发现和发明",
    "For the discovery of macroscopic quantum mechanical tunnelling and energy quantisation in an electric circuit.":
        "表彰他们发现电路中的宏观量子隧穿和能量量子化",
}

WOMEN = {"Donna Strickland", "Andrea Ghez", "Anne L'Huillier"}


def _norm_citation(s: str) -> str:
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"\s+([.,;:])", r"\1", s)
    s = re.sub(r"\s*-\s*", "-", s)  # 连字符两侧空格归一（如 laser -based → laser-based）
    return s


def parse_index() -> list[dict]:
    rows = []
    for m in re.finditer(r"- (\d{4}) — \[(.+?)\]\((.+?)/page\.md\)", INDEX.read_text(encoding="utf-8")):
        rows.append({"year": int(m.group(1)), "name": m.group(2).strip(), "dir": m.group(3)})
    return rows


def load_citations() -> dict[tuple[int, str], dict]:
    data = json.loads(SRC.read_text(encoding="utf-8"))
    out = {}
    for x in data:
        if x["year"] >= 2001:
            out[(x["year"], x["name"])] = x
    return out


def page_qid(directory: str) -> str | None:
    p = PAGES / directory / "page.md"
    if not p.exists():
        return None
    m = re.search(r'^wikidata:\s*"?([Qq]\d+)"?', p.read_text(encoding="utf-8"), re.M)
    return m.group(1) if m else None


def db_flags(qid: str | None, name: str) -> tuple[str, str]:
    """返回（立传旗标、社会关系入库旗标）。匹配次序：QID → 精确名 → 规范化名。"""
    bio, rel = "🔲", "🔲"
    try:
        from db_mysql import get_conn

        conn = get_conn()
        cur = conn.cursor()
        row = None
        if qid:
            cur.execute("SELECT has_biography, has_social_data FROM people WHERE qid=%s", (qid,))
            row = cur.fetchone()
        if row is None:
            cur.execute("SELECT has_biography, has_social_data FROM people WHERE name_en=%s", (name,))
            row = cur.fetchone()
        if row is None:
            n = re.sub(r"[^a-z]", "", name.lower())
            cur.execute(
                "SELECT has_biography, has_social_data, name_en FROM people "
                "WHERE primary_occupation='physicist'"
            )
            for r in cur.fetchall():
                if re.sub(r"[^a-z]", "", (r[2] or "").lower()) == n:
                    row = (r[0], r[1])
                    break
        if row:
            bio = "✅" if row[0] else "🔲"
            rel = "✅" if row[1] else "🔲"
    except Exception as e:  # 库不可用时降级为 🔲
        print("WARN db:", e)
    return bio, rel


def main() -> int:
    if not SRC.exists():
        print("missing", SRC)
        return 1
    cites = load_citations()
    rows = parse_index()
    # 匹配 citation（按 (year,name) 精确；Ashkin 已在 json 中修复）
    for r in rows:
        c = cites.get((r["year"], r["name"]))
        if c is None:  # 宽松匹配：同年同人名包含
            cands = [v for (y, n), v in cites.items() if y == r["year"] and n.split()[-1] in r["name"]]
            c = cands[0] if len(cands) == 1 else None
        r["country"] = c["country"] if c else None
        r["citation_en"] = c["citation"] if c else None

    total_items = len(rows)
    unique_people = sorted({r["name"] for r in rows})
    country_counter = Counter(r["country"] for r in rows if r["country"])

    # DB 状态
    rel_done_names = []
    for r in rows:
        r["qid"] = page_qid(r["dir"])
        bio, rel = db_flags(r["qid"], r["name"])
        r["bio"], r["rel"] = bio, rel
        if rel == "✅":
            rel_done_names.append(r["name"])

    lines = []
    lines.append("# 21 世纪诺贝尔物理学奖得主 — OpenPhysicist 名录")
    lines.append("")
    lines.append(
        "> **本名录收录 2001–2025 年诺贝尔物理学奖得主，共 %d 项 / %d 位。**" % (total_items, len(unique_people))
    )
    lines.append(">")
    lines.append(
        "> 从宇宙中微子到引力波，从石墨烯到人工神经网络：进入新世纪，物理学奖持续拓展人类认知的边界。\n"
        ">\n"
        "> 获奖理由为诺贝尔奖官方获奖理由（中文翻译）；「立传」表示是否已生成立传 Beamer，「Review」表示是否已完成事实核查，「社会关系入库」表示是否已将研究领域与社会关系写入 greatminds 数据库（people / person_relation / person_field）。\n"
        ">\n"
        "> 数据来源：英文维基百科「List of Nobel laureates in Physics」+ Nobel 官方获奖理由；国籍列沿用 Nobel 官方 country 口径。"
    )
    lines.append("---")

    lines.append("\n## 一、完整名单（按年份）\n")
    lines.append("\n| 年份 | 获奖者 | 国籍 | 获奖理由 | 立传 | Review | 社会关系入库 |")
    lines.append("|:--:|------|------|------|:--:|:--:|:--:|")
    for r in rows:
        zh = NAME_ZH.get(r["name"])
        name_display = f"{r['name']} ({zh})" if zh else r["name"]
        citation = CITATION_ZH.get(_norm_citation(r["citation_en"] or ""), r["citation_en"] or "—").replace("|", "/")
        review = "🔲"
        lines.append(
            "| %d | %s | %s | %s | %s | %s | %s |"
            % (r["year"], name_display, r["country"] or "—", citation, r["bio"], review, r["rel"])
        )

    lines.append("\n---\n")
    lines.append("\n## 二、统计说明\n")
    lines.append("\n- **获奖年份跨度**：2001–2025")
    lines.append("- **获奖总项数**：%d 项" % total_items)
    lines.append("- **获奖总人数**：%d 位" % len(unique_people))
    done = sorted(set(BIOGRAPHIES_DONE))
    lines.append("- **已立传**：%d 位（%s）" % (len(done), "、".join(done) if done else "暂无"))
    lines.append("- **已 Review**：%d 位（暂无）")
    lines[-1] = "- **已 Review**：0 位（暂无）"
    lines.append("- **已社会关系入库**：%d 位（随 20 世纪批次作为关系对手方/交叉得主部分入库：%s）" % (len(set(rel_done_names)), "、".join(sorted(set(rel_done_names)) or ["暂无"])))
    women = [w for w in sorted(WOMEN) if w in unique_people]
    if women:
        lines.append("- **女性获奖者**（21 世纪）：" + "、".join(women))

    lines.append("\n### 国籍分布\n")
    lines.append("\n| 国籍 | 人数 |")
    lines.append("|------|:--:|")
    for c, n in country_counter.most_common():
        lines.append("| %s | %d |" % (c, n))

    lines.append("\n---\n")
    lines.append(
        "\n> **这不是一份排名，而是一部仍在书写的物理学历程：每一项获奖都标记着人类对自然认识的一次跃迁。**\n"
    )

    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("wrote:", OUT)
    print("总项数:", total_items, "总人数:", len(unique_people))
    print("已社会关系入库:", len(set(rel_done_names)), "位")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
