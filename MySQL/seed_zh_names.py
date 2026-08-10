#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 OpenMath_20th_Century_Comprehensive_Ranking.md 提取中文名并更新 people。

格式三种：
- '**陈省身**'                  -> name_zh=陈省身, name_en=陈省身
- '**I.M. Gelfand** (盖尔范德)'  -> name_zh=盖尔范德, name_en=I.M. Gelfand
- '**高木贞治** (Takagi Teiji)'  -> name_zh=高木贞治, name_en=Takagi Teiji

匹配：优先按英文名（name_en）归一化匹配库中 person；库中无英文名时按 name_zh。
"""
import re
import unicodedata
from pathlib import Path

from db_mysql import get_conn

MD = Path(__file__).resolve().parent.parent / "mathematician" / "figures" / "OpenMath_20th_Century_Comprehensive_Ranking.md"

CJK = re.compile(r"[\u4e00-\u9fff]")
PAREN = re.compile(r"\((.*?)\)")
ROW_RE = re.compile(r"^\|\s*\d+\s*\|\s*(?:\d+|无)\s*\|\s*(?P<name>.+?)\s*\|")


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def parse_names():
    """返回 [(name_zh, name_en), ...]"""
    out = []
    for line in MD.read_text(encoding="utf-8").splitlines():
        m = ROW_RE.match(line)
        if not m:
            continue
        raw = m.group("name").strip()
        pm = PAREN.search(raw)
        core = raw[: pm.start()].strip().strip("*").strip() if pm else raw.strip("*").strip()
        extra = pm.group(1).strip() if pm else ""
        if CJK.search(core):
            out.append((core, extra or None))       # 中文为主
        elif extra and CJK.search(extra):
            out.append((extra, core))               # 英文为主，括号中文
        else:
            out.append((None, core))                # 纯英文
    return out


def main():
    pairs = parse_names()
    cn = [(zh, en) for zh, en in pairs if zh]
    print(f"解析到 {len(pairs)} 人，其中含中文名 {len(cn)} 人")

    conn = get_conn()
    cur = conn.cursor()

    # 库中 people 索引
    cur.execute("SELECT id, name_en, name_zh FROM people")
    people = [(pid, en, zh, norm(en or ""), norm(zh or "")) for pid, en, zh in cur.fetchall()]
    by_en = {ne: (pid, en, zh) for pid, en, zh, ne, nz in people if ne}
    by_zh = {nz: (pid, en, zh) for pid, en, zh, ne, nz in people if nz}

    updated = 0
    skipped = []
    for zh, en in cn:
        pid = None
        # 1) 按英文名匹配
        if en:
            pid = by_en.get(norm(en), (None,))[0]
        # 2) 按中文名匹配（库中 name_zh 已是中文）
        if pid is None and zh:
            pid = by_zh.get(norm(zh), (None,))[0]
        # 3) 库中 name_en 就是中文（如陈省身）——按中文名匹配 name_en
        if pid is None and zh:
            for i, (_, en2, _) in enumerate(people):
                if en2 and norm(en2) == norm(zh):
                    pid = people[i][0]
                    break
        if pid is None:
            skipped.append(f"{zh}（{en or '?'}）")
            continue

        # 更新 name_zh（若为空或与英文不同），name_en 若为纯中文则用英文回填
        cur.execute("SELECT name_en, name_zh FROM people WHERE id=%s", (pid,))
        cur_en, cur_zh = cur.fetchone()
        new_zh = zh if (cur_zh is None or cur_zh == cur_en) else cur_zh
        cur.execute("UPDATE people SET name_zh=%s WHERE id=%s", (new_zh, pid))
        if cur.rowcount:
            updated += 1
            print(f"  ✓ {cur_en or '?'} -> 中文名 {zh}")

    conn.commit()
    print(f"\n更新中文名: {updated} 人")
    if skipped:
        print("未匹配（库中无此人）:", ", ".join(skipped))
    conn.close()


if __name__ == "__main__":
    main()
