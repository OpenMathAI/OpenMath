#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""导出 greatminds.db 中全部人物及其关联信息到 Markdown，供人工复查。

两种格式：
- 默认（每节一人）：基本信息 / 职业 / 研究领域 / 奖项 / 排名 / 关系
- --one-line（一人一行表格）：排名 | 姓名 | 英文名 | 生卒 | 主导职业 | 领域 | 奖项 | 标签

输出：db/people_full.md（或 --out 指定）
"""
import argparse
import pymysql
from db_mysql import get_conn, CompatDictCursor
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "people_full.md"



def _now():
    c = get_conn()
    cur = c.cursor()
    cur.execute('SELECT NOW()')
    v = cur.fetchone()[0]
    c.close()
    return v
def q(cur, sql, args=()):
    cur.execute(sql, args)
    return cur.fetchall()


def collect(cur, people):
    """为每个人收集关联数据，返回增强后的列表。"""
    people = [dict(p) for p in people]
    for p in people:
        pid = p["id"]
        p["occupations"] = q(cur, """
            SELECT o.name_en, o.name_zh, po.`rank` FROM person_occupation po
            JOIN occupations o ON o.id=po.occupation_id WHERE po.person_id=? ORDER BY po.`rank`
        """, (pid,))
        p["fields"] = q(cur, """
            SELECT f.name_en, f.name_zh FROM person_field pf
            JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=? ORDER BY f.name_en
        """, (pid,))
        p["awards"] = q(cur, """
            SELECT a.name_zh, a.name_en, al.year, al.note FROM award_laureate al
            JOIN awards a ON a.id=al.award_id WHERE al.person_id=? ORDER BY al.year
        """, (pid,))
        p["rankings"] = q(cur, """
            SELECT r.`rank`, r.orig_rank, r.tag, r.status FROM rankings r
            WHERE r.person_id=? ORDER BY r.`rank`
        """, (pid,))
    return people


def render_sections(people):
    """每节一人（默认格式）。"""
    lines = ["# 人物信息总览（greatminds.db 导出）", ""]
    lines.append(f"> 导出时间：{_now()}")
    lines.append(f"> 人物总数：**{len(people)}**")
    lines.append("> 说明：字段为空表示数据尚未采集（可后续抓取 Wikidata 补全）。")
    lines.append("")
    for p in people:
        pid = p["id"]
        name = p["name_zh"] or p["name_en"]
        if p["name_zh"] and p["name_zh"] != p["name_en"]:
            name = f"{p['name_zh']}（{p['name_en']}）"
        lines += [f"## {name}", ""]

        lines.append("### 基本信息")
        lines.append("")
        lines.append("| 字段 | 值 |")
        lines.append("|---|---|")
        for k, zh in [("qid", "qid"), ("name_en", "英文名"), ("name_zh", "中文名"),
                      ("gender", "性别"), ("birth_date", "出生"), ("death_date", "逝世"),
                      ("description", "描述"), ("primary_occupation", "主导职业")]:
            v = p[k]
            if v:
                lines.append(f"| {zh} | {v} |")
        lines.append("")

        if p["occupations"]:
            lines.append(f"### 职业（{len(p['occupations'])}）")
            lines.append("")
            for o in p["occupations"]:
                zh = f"（{o['name_zh']}）" if o["name_zh"] else ""
                lines.append(f"- {o['name_en']}{zh}" + ("（主）" if o["rank"] == 0 else ""))
            lines.append("")

        if p["fields"]:
            lines.append(f"### 研究领域（{len(p['fields'])}）")
            lines.append("")
            for f in p["fields"]:
                zh = f"（{f['name_zh']}）" if f["name_zh"] else ""
                lines.append(f"- {f['name_en']}{zh}")
            lines.append("")

        if p["awards"]:
            lines.append(f"### 奖项（{len(p['awards'])}）")
            lines.append("")
            lines.append("| 奖项 | 年份 | 备注 |")
            lines.append("|---|---|---|")
            for a in p["awards"]:
                lines.append(f"| {a['name_zh']}（{a['name_en']}） | {a['year']} | {a['note'] or ''} |")
            lines.append("")

        if p["rankings"]:
            lines.append("### 排名")
            lines.append("")
            for r in p["rankings"]:
                orig = f"（原榜 #{r['orig_rank']}）" if r["orig_rank"] else ""
                lines.append(f"- **#{r['rank']}**{orig}")
                if r["tag"]:
                    lines.append(f"  - 标签：{r['tag']}")
                if r["status"] and r["status"] != "/":
                    lines.append(f"  - 状态：{r['status']}")
            lines.append("")

        lines += ["---", ""]
    return lines


def _row_fields(p):
    """抽取一行记录的各字段（供 one-line / tsv 共用）。"""
    rank = ""
    tag = ""
    if p["rankings"]:
        r0 = p["rankings"][0]
        rank = str(r0["rank"])
        tag = r0["tag"] or ""
    name = p["name_zh"] or p["name_en"]
    life = ""
    if p["birth_date"] or p["death_date"]:
        life = f"{p['birth_date'] or '?'}–{p['death_date'] or '?'}"
    occ = "、".join(o["name_zh"] or o["name_en"] for o in p["occupations"] if o["rank"] == 0) \
          or p["primary_occupation"] or ""
    fds = "；".join(f["name_en"] for f in p["fields"])
    aws = "；".join(f"{a['name_zh']} {a['year']}" for a in p["awards"])
    return [rank, name, p["name_en"] or "", life, occ, fds, aws, tag]


def render_oneline(people):
    """一人一行 Markdown 表格（便于复查对比；长列在渲染时可能折行）。"""
    lines = ["# 人物信息总览 · 一人一行（greatminds.db 导出）", ""]
    lines.append(f"> 导出时间：{_now()}")
    lines.append(f"> 人物总数：**{len(people)}**")
    lines.append("> 说明：领域/奖项为多值，用 `；` 分隔；空字段表示尚未采集。")
    lines.append("")
    lines.append("| # | 姓名 | 英文名 | 生卒 | 主导职业 | 研究领域 | 奖项 | 标签 |")
    lines.append("|---|---|---|---|---|---|---|---|")
    for p in people:
        cells = [c.replace("|", "\\|").replace("\n", " ") for c in _row_fields(p)]
        lines.append("| " + " | ".join(cells) + " |")
    return lines


def render_tsv(people):
    """一人一行 TSV（tab 分隔）——每条记录物理上是一行，可直接导入 Excel/复查。"""
    header = ["#", "姓名", "英文名", "生卒", "主导职业", "研究领域", "奖项", "标签"]
    lines = ["\t".join(header)]
    for p in people:
        cells = [c.replace("\t", " ").replace("\n", " ") for c in _row_fields(p)]
        lines.append("\t".join(cells))
    return lines


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(OUT))
    ap.add_argument("--only", default=None, help="只导出名字包含此子串的人")
    ap.add_argument("--one-line", action="store_true", help="一人一行表格格式（Markdown）")
    ap.add_argument("--tsv", action="store_true", help="一人一行 TSV 格式（tab 分隔，物理一行，Excel 友好）")
    args = ap.parse_args()

    conn = get_conn()
    cur = conn.cursor(CompatDictCursor)

    people = q(cur, """
        SELECT p.*,
               (SELECT MIN(r.`rank`) FROM rankings r WHERE r.person_id=p.id) AS best_rank
        FROM people p
        ORDER BY best_rank IS NULL, best_rank, p.name_en
    """)
    if args.only:
        people = [p for p in people if args.only.lower() in (p["name_en"] or "").lower()
                  or (p["name_zh"] or "").lower() in args.only.lower()]

    people = collect(cur, people)

    if args.tsv:
        lines = render_tsv(people)
    elif args.one_line:
        lines = render_oneline(people)
    else:
        lines = render_sections(people)

    Path(args.out).write_text("\n".join(lines), encoding="utf-8")
    fmt = "tsv" if args.tsv else ("one-line" if args.one_line else "sections")
    print(f"已导出 {len(people)} 人 → {args.out} ({fmt})")


if __name__ == "__main__":
    main()
