#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""解析中文维基百科条目引言，更新 people 的中文名/称号/生卒。

输入格式（每行一条，或粘贴整段）：
    大卫·希尔伯特（德语：David Hilbert，1862年1月23日—1943年2月14日），德国数学家，被誉为"现代数学之父"。
提取：
    name_zh       = 大卫·希尔伯特（「（」前内容）
    name_en       = David Hilbert（括号内「德语：/英语：/俄语：」后的第一段）
    birth/death   = 1862-01-23 / 1943-02-14（中文日期 → ISO）
    name_variants = 现代数学之父（「誉为"…"」中的称号，追加到已有值）

用法：
    python3 parse_zh_wiki.py --file zh_names.txt
    python3 parse_zh_wiki.py --text "大卫·希尔伯特（德语：David Hilbert，…）"
"""
import argparse
import json
import re
from pathlib import Path

from db_mysql import get_conn

# 语言前缀：匹配「X语：」
LANG_RE = re.compile(r"^(?:[A-Za-z\u4e00-\u9fff]+语)[：:]\s*")
# 称号：「誉为"…"」或「被誉为"…"」
HONOR_RE = re.compile(r"(?:被?誉为|被称为|人称|尊称|号称)[\u201c\"「『]([^」」\u201d\"』]+)[\u201d\"」』]")
# 日期：YYYY年M月D日
DATE_RE = re.compile(r"(\d{4})年(\d{1,2})月(\d{1,2})日")
# 年份跨度：YYYY年—YYYY年
YEAR_SPAN_RE = re.compile(r"(\d{4})年(?:[—\-－~至])+(\d{4})年")


def to_iso(y, m, d):
    return f"{int(y):04d}-{int(m):02d}-{int(d):02d}"


def parse_entry(text):
    """返回 dict(name_zh, name_en, birth, death, honor)"""
    text = text.strip().lstrip("-•* \t")
    # 中文全名：括号前
    m = re.search(r"[（(]", text)
    name_zh = text[: m.start()].strip() if m else text.strip()
    name_en = None
    birth = death = None
    if m:
        # 括号内容：X语：English Name，日期…
        paren = text[m.start() + 1: re.search(r"[）)]", text).start()]
        # 语言前缀后的英文名（到第一个逗号/顿号）
        pm = LANG_RE.search(paren)
        rest = paren[pm.end():] if pm else paren
        en_part = re.split(r"[，,、；;]", rest)[0].strip()
        if en_part and not re.search(r"\d", en_part):
            name_en = en_part
        # 日期
        dm = DATE_RE.search(paren)
        if dm:
            birth = to_iso(*dm.groups())
        ym = YEAR_SPAN_RE.search(paren)
        if ym:
            death = f"{int(ym.group(2)):04d}-12-31" if "年" in ym.group(2) and not re.search(r"\d+月", ym.group(2)) else None
        # 若 death 未解析出，尝试第二个日期
        dates = DATE_RE.findall(paren)
        if len(dates) >= 2:
            birth = to_iso(*dates[0])
            death = to_iso(*dates[1])
    # 称号
    honor = None
    hm = HONOR_RE.search(text)
    if hm:
        honor = hm.group(1).strip()
    return {"name_zh": name_zh, "name_en": name_en, "birth": birth, "death": death, "honor": honor}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--file", default=None, help="文本文件路径（每行一条）")
    ap.add_argument("--text", default=None, help="直接传入文本")
    args = ap.parse_args()

    if args.text:
        lines = [args.text]
    elif args.file:
        lines = [l for l in Path(args.file).read_text(encoding="utf-8").splitlines() if l.strip()]
    else:
        print("需要 --file 或 --text")
        return

    conn = get_conn()
    cur = conn.cursor()

    # people 索引（按英文名 + 中文名）
    cur.execute("SELECT id, name_en, name_zh FROM people")
    people = cur.fetchall()

    updated = 0
    skipped = []
    for line in lines:
        d = parse_entry(line)
        if not d["name_zh"]:
            continue
        pid = None
        # 匹配：优先按英文名（若提供），再按 name_zh 匹配已有中文名
        if d["name_en"]:
            for i, (p, en, zh) in enumerate(people):
                if en and en.lower() == d["name_en"].lower():
                    pid = p
                    break
        if pid is None:
            for p, en, zh in people:
                if zh and zh == d["name_zh"]:
                    pid = p
                    break
        if pid is None:
            skipped.append(d["name_zh"])
            continue

        # 更新：name_zh / name_variants（称号追加）/ birth / death
        cur.execute("SELECT name_zh, name_variants, birth_date, death_date FROM people WHERE id=%s", (pid,))
        cz, cv, cb, cd = cur.fetchone()
        new_zh = d["name_zh"] if d["name_zh"] else cz
        new_var = None
        if d["honor"]:
            existing = set()
            if cv:
                try:
                    existing = set(json.loads(cv)) if cv.startswith("[") else {cv}
                except Exception:
                    existing = {cv}
            existing.add(d["honor"])
            new_var = json.dumps(sorted(existing), ensure_ascii=False)
        cur.execute(
            "UPDATE people SET name_zh=COALESCE(%s,name_zh), name_variants=COALESCE(%s,name_variants), "
            "birth_date=COALESCE(%s,birth_date), death_date=COALESCE(%s,death_date) WHERE id=%s",
            (new_zh or None, new_var, d["birth"], d["death"], pid),
        )
        if cur.rowcount or new_var:
            updated += 1
            print(f"  ✓ {d['name_en'] or d['name_zh']} -> 中文名={new_zh or cz} 称号={d['honor']} {d['birth']}–{d['death']}")

    conn.commit()
    print(f"\n处理 {len(lines)} 条，更新 {updated} 人")
    if skipped:
        print("未匹配到库中人物:", ", ".join(skipped))
    conn.close()


if __name__ == "__main__":
    main()
