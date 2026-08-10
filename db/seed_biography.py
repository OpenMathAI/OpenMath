#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""扫描 mathematician/presentations/ 目录，标记已立传的数学家（has_biography=1）。

目录名与 people.name_en 存在格式差异（下划线/连字符/缩写），用归一化匹配：
  Jean_Pierre_Serre   -> J.-P. Serre
  G_H_Hardy           -> G.H. Hardy
  Shiing_Shen_Chern   -> Shiing-Shen Chern
"""
import re
import sqlite3
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DB = ROOT / "greatminds.db"
PRES = ROOT.parent / "mathematician" / "presentations"

# 已知目录名 -> people.name_en 的别名映射（归一化后仍匹配不上的兜底）
DIR_ALIAS = {
    "Andre_Weil": "André Weil",
    "Elie_Cartan": "Élie Cartan",
    "Jean_Pierre_Serre": "J.-P. Serre",
    "G_H_Hardy": "G.H. Hardy",
    "R_A_Fisher": "Ronald Fisher",
    "Richard_Bellman": "Richard E. Bellman",
    "Shiing_Shen_Chern": "Shiing-Shen Chern",
    "Kurt_Godel": "Kurt Gödel",
    "Lars_Hormander": "Lars Hörmander",
    "Liu_Hui": "Liu Hui",
    "Zu_Chongzhi": "Zu Chongzhi",
    "Hua_Loo-Keng": "Hua Loo-Keng",
}

# 中文名 -> 目录名（people.name_en 为中文时用）
CN_DIR_ALIAS = {
    "陈省身": "Shiing_Shen_Chern",
    "祖冲之": "Zu_Chongzhi",
}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)]", "", s).lower()


def main():
    if not PRES.is_dir():
        print(f"目录不存在: {PRES}")
        return

    # 收集已立传目录名（排除封面/通用文件）
    biographed = {}
    for d in PRES.iterdir():
        if not d.is_dir():
            continue
        if d.name in ("cover", "prompts"):
            continue
        # 目录里有 .pdf 或 .tex 才算真正立传（排除空目录）
        has_output = any(p.suffix.lower() in (".pdf", ".tex", ".mp4") for p in d.iterdir())
        if has_output:
            biographed[norm(d.name)] = d.name
            # 目录名别名：目录名归一化到人名归一化的额外键
            if d.name in DIR_ALIAS:
                biographed.setdefault(norm(DIR_ALIAS[d.name]), d.name)
    print(f"presentations 已立传目录: {len(biographed)}")

    conn = sqlite3.connect(DB)
    cur = conn.cursor()
    cur.execute("SELECT id, name_en, name_zh FROM people")
    people = cur.fetchall()

    matched = 0
    matched_dirkeys = set()
    for pid, en, zh in people:
        if not en and zh:
            en = zh
        keys = {norm(en)}
        if zh:
            keys.add(norm(zh))
        # 中文名 -> 目录名别名
        if zh and zh in CN_DIR_ALIAS:
            keys.add(norm(CN_DIR_ALIAS[zh]))
        hit_key = next((k for k in keys if k in biographed), None)
        if hit_key:
            cur.execute("UPDATE people SET has_biography=1 WHERE id=?", (pid,))
            matched += 1
            matched_dirkeys.add(hit_key)

    conn.commit()
    print(f"已标记 has_biography=1: {matched} 人")
    # 报告真正未匹配的立传目录（按目录原始名判断；别名键命中即算该目录匹配）
    matched_dirs = {v for k, v in biographed.items() if k in matched_dirkeys}
    unmatched_dirs = sorted(set(v for v in biographed.values()) - matched_dirs)
    if unmatched_dirs:
        print("presentations 中未匹配到 people 的目录（人名不在库中或需补别名）:")
        for u in unmatched_dirs:
            print("  -", u)
    conn.close()


if __name__ == "__main__":
    main()
