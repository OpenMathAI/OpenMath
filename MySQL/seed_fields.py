#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""给 people 灌入研究领域（fields + person_field）。

数据源 1（首选，结构化）：mathematician/pages/*/metadata.json 的 Wikidata field_of_work。
数据源 2（补充）：OpenMath 20 世纪排名文件的「核心标签」关键词提取（仅当 metadata 缺失时）。

人名匹配：归一化（去标点/空白/变音符）+ 别名映射表。
"""
import json
import re
import pymysql
from db_mysql import get_conn
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAGES = ROOT.parent / "mathematician" / "pages"
MD = ROOT.parent / "mathematician" / "figures" / "OpenMath_20th_Century_Comprehensive_Ranking.md"

# 排名文件名（简写/中文）-> metadata.json 标准名
ALIAS = {
    "J.-P. Serre": "Jean-Pierre Serre",
    "G.H. Hardy": "G. H. Hardy",
    "R.A. Fisher": "Ronald Fisher",
    "Richard Bellman": "Richard E. Bellman",
    "陈省身": "Shiing-Shen Chern",
    "Kurt Gödel": "Kurt Godel",
}

# 标签提取漏网之鱼：规范化名 -> 领域（手动补充）
MANUAL_FIELDS = {
    "renethom": ["cobordism theory", "singularity theory"],
    "shimuragoro": ["number theory", "algebraic geometry"],
    "anwhitehead": ["mathematical logic", "algebra", "philosophy"],
    "oskarperron": ["matrix theory", "number theory"],
    "fukuharamasuo": ["mathematics"],
}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s\-\'\.\(\)·]", "", s).lower()


def get_field_of_work():
    """{规范化名: [field, ...]}"""
    out = {}
    for d in PAGES.iterdir():
        if not d.is_dir():
            continue
        mf = d / "metadata.json"
        if not mf.exists():
            continue
        try:
            meta = json.loads(mf.read_text(encoding="utf-8"))
        except Exception:
            continue
        name = meta.get("name")
        fields = meta.get("properties", {}).get("field_of_work", [])
        if name and fields:
            out[norm(name)] = [f for f in fields if f]
    return out


def extract_from_tags():
    """排名文件标签 -> {规范化名: [field, ...]}（启发式关键词）"""
    KEYWORDS = {
        "微分几何": ["differential geometry"], "黎曼几何": ["differential geometry"],
        "整体微分几何": ["differential geometry"], "低维拓扑": ["topology"],
        "代数几何": ["algebraic geometry"], "复分析": ["complex analysis"],
        "泛函分析": ["functional analysis"], "偏微分方程": ["partial differential equations"],
        "偏微分": ["partial differential equations"], "PDE": ["partial differential equations"],
        "数论": ["number theory"], "解析数论": ["number theory"], "代数数论": ["number theory"],
        "类域论": ["number theory"], "素数定理": ["number theory"], "模形式": ["number theory"],
        "拓扑": ["topology"], "代数拓扑": ["algebraic topology"], "点集拓扑": ["topology"],
        "群论": ["group theory"], "有限单群": ["group theory"],
        "表示论": ["representation theory"], "李群": ["Lie group theory"],
        "概率论": ["probability theory"], "概率": ["probability theory"],
        "动力系统": ["dynamical systems"], "遍历理论": ["ergodic theory"],
        "调和分析": ["harmonic analysis"], "实分析": ["mathematical analysis"],
        "数学分析": ["mathematical analysis"], "分析": ["mathematical analysis"],
        "信息论": ["information theory"], "数理逻辑": ["mathematical logic"],
        "逻辑": ["mathematical logic"], "集合论": ["set theory"],
        "范畴论": ["category theory"], "同调代数": ["homological algebra"],
        "同调": ["homological algebra"], "算子": ["operator theory"],
        "代数": ["algebra"], "变分法": ["calculus of variations"],
        "控制论": ["cybernetics"], "博弈论": ["game theory"],
        "测度论": ["measure theory"], "K理论": ["K-theory"],
        "随机过程": ["probability theory"], "随机分析": ["probability theory"],
        "马尔可夫": ["probability theory"], "积分方程": ["integral equations"],
        "流体力学": ["fluid dynamics"], "天体力学": ["celestial mechanics"],
        "数值": ["numerical analysis"], "计算方法": ["numerical analysis"],
        "数学物理": ["mathematical physics"], "量子": ["mathematical physics"],
        "计算机科学": ["computer science"], "可计算性": ["computability theory"],
        "计算理论": ["theoretical computer science"], "统计": ["statistics"],
        "应用数学": ["applied mathematics"], "几何": ["geometry"],
        "组合": ["combinatorics"], "动力系统与统计力学": ["dynamical systems", "statistical mechanics"],
    }
    tag_re = re.compile(
        r"^\|\s*\d+\s*\|\s*(?:\d+|无)\s*\|\s*(?P<name>.+?)\s*\|"
        r"\s*(?P<awards>[^|]*?)\s*\|"
        r"\s*(?P<tag>[^|]*?)\s*\|"
    )
    out = {}
    for line in MD.read_text(encoding="utf-8").splitlines():
        m = tag_re.match(line.strip())
        if not m:
            continue
        name = re.sub(r"\*\*", "", m.group("name")).strip()
        # 去掉括号注释（如 'I.M. Gelfand** (盖尔范德)' 里的中文注释）
        pm = re.search(r"\((.*?)\)", name)
        if pm:
            name = name[: pm.start()].strip()
        tag = m.group("tag")
        hits = [kw for kw in KEYWORDS if kw in tag]
        if hits:
            out[norm(name)] = list(dict.fromkeys(f for kw in hits for f in KEYWORDS[kw]))
    return out


def main():
    conn = get_conn()
    cur = conn.cursor()

    wikidata_fields = get_field_of_work()
    tag_fields = extract_from_tags()
    print(f"metadata field_of_work 人数: {len(wikidata_fields)} · 标签提取人数: {len(tag_fields)}")

    # 载入 people 名册
    cur.execute("SELECT id, name_en, name_zh FROM people")
    people = []
    for pid, en, zh in cur.fetchall():
        people.append((pid, en, zh, norm(en), norm(zh or "")))

    matched_wd = matched_tag = 0
    unmatched = []
    for pid, en, zh, n_en, n_zh in people:
        fields = None
        # 1) metadata（规范化名 或 别名）
        if n_en in wikidata_fields:
            fields = wikidata_fields[n_en]
        elif ALIAS.get(en) and norm(ALIAS[en]) in wikidata_fields:
            fields = wikidata_fields[norm(ALIAS[en])]
        elif zh and n_zh in wikidata_fields:
            fields = wikidata_fields[n_zh]
        src = "wikidata"
        # 2) 标签补充
        if not fields:
            if n_en in tag_fields:
                fields = tag_fields[n_en]
                src = "tag"
            elif zh and n_zh in tag_fields:
                fields = tag_fields[n_zh]
                src = "tag"
        # 3) 手动补充
        if not fields:
            if n_en in MANUAL_FIELDS:
                fields = MANUAL_FIELDS[n_en]
                src = "manual"
            elif zh and n_zh in MANUAL_FIELDS:
                fields = MANUAL_FIELDS[n_zh]
                src = "manual"
        if not fields:
            unmatched.append(en or zh)
            continue
        # 写 fields + person_field
        for f in fields:
            cur.execute("SELECT id FROM fields WHERE name_en=?", (f,))
            fid = cur.fetchone()
            if not fid:
                cur.execute("INSERT INTO fields(name_en) VALUES (?)", (f,))
                fid = cur.lastrowid
            else:
                fid = fid[0]
            cur.execute("INSERT OR IGNORE INTO person_field(person_id, field_id, `rank`) VALUES (?,?,0)",
                        (pid, fid))
        if src == "wikidata":
            matched_wd += 1
        else:
            matched_tag += 1

    conn.commit()
    print(f"来自 Wikidata: {matched_wd} · 来自标签: {matched_tag} · 未匹配: {len(unmatched)}")
    if unmatched:
        print("未匹配:", ", ".join(unmatched))
    cur.execute("SELECT COUNT(*) FROM fields")
    print(f"fields 总数: {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(*) FROM person_field")
    print(f"person_field 总数: {cur.fetchone()[0]}")
    conn.close()


if __name__ == "__main__":
    main()
