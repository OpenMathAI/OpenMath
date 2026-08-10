#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 mathematician/presentations/<Name>/*_zh.tex 提取中文名+称号，更新 people。

tex 标题格式（统一）：%  称号：中文名 (English Name)
例：%  数学之王：大卫·希尔伯特 (David Hilbert)
    %  抽象代数之母：埃米·诺特 (Emmy Noether)

提取：
    name_zh       = 中文名（「：」后、括号前）
    name_en       = 括号内英文名
    name_variants = 称号（JSON 数组追加，如 "现代数学之父"）
"""
import argparse
import json
import re
import unicodedata
from pathlib import Path

from db_mysql import get_conn

PRES = Path(__file__).resolve().parent.parent / "mathematician" / "presentations"


def _norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.]", "", s).lower()

# 匹配标题行：%  称号：中文名 (English Name)
# 称号=「：」前；中文名=「：」后括号前；英文名=括号内
TITLE_RE = re.compile(
    r"^%\s*([\u4e00-\u9fff·A-Za-z0-9 ]+?)[：:]\s*"
    r"([\u4e00-\u9fff·]+)\s*[（(]\s*([^）)]+)[）)]",
    re.MULTILINE,
)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=10, help="处理前 N 个目录（按字母序）")
    ap.add_argument("--dirs", default=None, help="指定目录名（逗号分隔），替代 --n")
    args = ap.parse_args()

    # 默认：库中 id 前 N 人的 name_en -> 匹配 presentations 目录
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, name_en FROM people ORDER BY id LIMIT %s", (args.n,))
    target_names = [en for _, en in cur.fetchall()]

    pres_dir_by_norm = {}
    for d in PRES.iterdir():
        if d.is_dir():
            pres_dir_by_norm[_norm(d.name)] = d.name

    dirs = []
    for en in target_names:
        key = _norm(en or "")
        if key in pres_dir_by_norm:
            dirs.append(pres_dir_by_norm[key])
        else:
            print(f"  ⚠ 无对应 presentations 目录: {en}")
    if args.dirs:
        dirs = [x.strip() for x in args.dirs.split(",")]
    print(f"处理目录: {dirs}")

    cur.execute("SELECT id, name_en, name_zh, name_variants FROM people")
    people = cur.fetchall()
    people_by_id = {p[0]: {"en": p[1], "zh": p[2], "variants": p[3]} for p in people}

    # 目录名 -> tex 文件
    for dn in dirs:
        d = PRES / dn
        texs = list(d.glob("*_zh.tex"))
        if not texs:
            print(f"  ⚠ 无 _zh.tex: {dn}")
            continue
        txt = texs[0].read_text(encoding="utf-8", errors="replace")
        m = TITLE_RE.search(txt)
        if not m:
            print(f"  ⚠ 标题未匹配: {dn}")
            continue
        honor, zh, en = m.group(1).strip(), m.group(2).strip(), m.group(3).strip()
        en = en.split(",")[0].strip()

        # 匹配库中 person（按英文名）
        pid = None
        en_norm = re.sub(r"[\s\'\.\-]", "", en).lower()
        for p, rec in people_by_id.items():
            pe = rec["en"]
            if pe and re.sub(r"[\s\'\.\-]", "", pe).lower() == en_norm:
                pid = p
                break
        if pid is None:
            print(f"  ⚠ 未匹配库中人物: {en}（{zh}）")
            continue

        # 更新 name_zh（若空） + name_variants（称号追加）
        rec = people_by_id[pid]
        new_var = rec["variants"]
        if honor:
            existing = set()
            if rec["variants"]:
                try:
                    existing = set(json.loads(rec["variants"])) if rec["variants"].startswith("[") else {rec["variants"]}
                except Exception:
                    existing = {rec["variants"]}
            existing.add(honor)
            new_var = json.dumps(sorted(existing), ensure_ascii=False)
        cur.execute(
            "UPDATE people SET name_zh=COALESCE(%s,name_zh), name_variants=COALESCE(%s,name_variants) WHERE id=%s",
            (zh, new_var, pid),
        )
        # 更新缓存
        people_by_id[pid]["zh"] = zh
        if new_var:
            people_by_id[pid]["variants"] = new_var
        print(f"  ✓ {en} -> 中文名={zh} 称号={honor}")

    conn.commit()
    cur.execute("SELECT COUNT(*) FROM people WHERE name_zh IS NOT NULL")
    print(f"\n现有中文名人数: {cur.fetchone()[0]}")
    conn.close()


if __name__ == "__main__":
    main()
