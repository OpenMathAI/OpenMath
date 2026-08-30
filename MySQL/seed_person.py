#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""通用人物入库引擎：读取 YAML 数据文件，幂等写入 greatminds 数据库。

取代原先 174 个 seed_*_full.py / seed_*_relations.py 脚本。

用法:
  python3 seed_person.py data/euler.yaml            # 单个人物
  python3 seed_person.py --all data/                # 批量入库整个目录
  python3 seed_person.py data/euler.yaml --dry-run  # 仅解析预览，不写库
"""
import argparse
import os
import re
import sys
import unicodedata

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_mysql import get_conn


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_'.()\u00b7,\-]", "", s).lower()


# ---------------- 字典表 get-or-create ----------------

def get_or_create(table, name_en, name_zh=None):
    """通用字典表 get-or-create：occupations / fields / institutions。"""
    cur = get_or_create.cur
    cur.execute("SELECT id FROM " + table + " WHERE name_en=%s", (name_en,))
    r = cur.fetchone()
    if r:
        if name_zh:
            cur.execute(
                "UPDATE " + table + " SET name_zh=%s WHERE id=%s AND (name_zh IS NULL OR name_zh='')",
                (name_zh, r[0]),
            )
        return r[0], False
    if name_zh:
        cur.execute(
            "INSERT INTO " + table + " (name_en, name_zh) VALUES (%s,%s)", (name_en, name_zh)
        )
    else:
        cur.execute("INSERT INTO " + table + " (name_en) VALUES (%s)", (name_en,))
    return cur.lastrowid, True


def get_or_create_country(name_en, name_zh=None):
    cur = get_or_create.cur
    cur.execute("SELECT id FROM countries WHERE name_en=%s", (name_en,))
    r = cur.fetchone()
    if r:
        return r[0], False
    cur.execute(
        "INSERT INTO countries(name_en, name_zh) VALUES (%s,%s)", (name_en, name_zh)
    )
    return cur.lastrowid, True


def get_or_create_award(name_en, name_zh=None):
    cur = get_or_create.cur
    cur.execute("SELECT id FROM awards WHERE name_en=%s", (name_en,))
    r = cur.fetchone()
    if r:
        return r[0], False
    cur.execute(
        "INSERT INTO awards(name_en, name_zh, award_type) VALUES (%s,%s,'award')",
        (name_en, name_zh or name_en),
    )
    return cur.lastrowid, True


# ---------------- 人物主记录 ----------------

def upsert_person(cur, d):
    """按 qid 或 name_en 定位人物，INSERT 或 UPDATE。返回 (pid, created)。"""
    pid = None
    if d.get("qid"):
        cur.execute("SELECT id FROM people WHERE qid=%s", (d["qid"],))
        r = cur.fetchone()
        if r:
            pid = r[0]
    if pid is None:
        cur.execute("SELECT id FROM people WHERE name_en=%s", (d["name_en"],))
        r = cur.fetchone()
        if r:
            pid = r[0]

    nv = d.get("name_variants")
    if isinstance(nv, list):
        nv = ", ".join(nv)

    fields = {
        "name_en": d["name_en"],
        "name_zh": d.get("name_zh"),
        "gender": d.get("gender"),
        "birth_date": d.get("birth_date"),
        "death_date": d.get("death_date"),
        "description": d.get("description"),
        "primary_occupation": d.get("primary_occupation"),
        "has_biography": 1 if d.get("has_biography") else 0,
        "has_social_data": 1,
    }
    if d.get("qid"):
        fields["qid"] = d["qid"]
    if nv:
        fields["name_variants"] = nv

    if pid is None:
        cols = list(fields.keys())
        vals = [fields[c] for c in cols]
        cur.execute(
            "INSERT INTO people (" + ",".join(cols) + ") VALUES (" + ",".join(["%s"] * len(cols)) + ")",
            vals,
        )
        return cur.lastrowid, True
    sets = ", ".join(k + "=%s" for k in fields)
    cur.execute("UPDATE people SET " + sets + " WHERE id=%s", tuple(fields.values()) + (pid,))
    return pid, False


# ---------------- 各关联表 ----------------

def link_occupations(cur, pid, items):
    for it in items:
        en = it if isinstance(it, str) else it["name_en"]
        zh = None if isinstance(it, str) else it.get("name_zh")
        rank = 0 if isinstance(it, str) else it.get("rank", 0)
        oid, _ = get_or_create("occupations", en, zh)
        cur.execute(
            "INSERT INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,%s) "
            "ON DUPLICATE KEY UPDATE `rank`=VALUES(`rank`)",
            (pid, oid, rank),
        )


def link_fields(cur, pid, items):
    for it in items:
        en = it if isinstance(it, str) else it["name_en"]
        zh = None if isinstance(it, str) else it.get("name_zh")
        rank = 0 if isinstance(it, str) else it.get("rank", 0)
        fid, _ = get_or_create("fields", en, zh)
        cur.execute(
            "INSERT INTO person_field(person_id, field_id, `rank`) VALUES (%s,%s,%s) "
            "ON DUPLICATE KEY UPDATE `rank`=VALUES(`rank`)",
            (pid, fid, rank),
        )


def link_nationalities(cur, pid, items):
    for i, it in enumerate(items):
        if isinstance(it, str):
            en, zh, rank, era = it, None, i, None
        else:
            en = it["name_en"]
            zh = it.get("name_zh")
            rank = it.get("rank", i)
            era = it.get("era_note")
        cid, _ = get_or_create_country(en, zh)
        cur.execute(
            "INSERT INTO person_nationality(person_id, country_id, `rank`, era_note) VALUES (%s,%s,%s,%s) "
            "ON DUPLICATE KEY UPDATE `rank`=VALUES(`rank`), era_note=VALUES(era_note)",
            (pid, cid, rank, era),
        )


def link_institutions(cur, pid, items):
    for it in items:
        if isinstance(it, str):
            en, zh, rel, sy, ey = it, None, "employment", None, None
        else:
            en = it["name_en"]
            zh = it.get("name_zh")
            rel = it.get("relation", "employment")
            sy = it.get("start_year")
            ey = it.get("end_year")
        iid, _ = get_or_create("institutions", en, zh)
        cur.execute(
            "INSERT INTO person_institution(person_id, inst_id, relation, start_year, end_year) "
            "VALUES (%s,%s,%s,%s,%s) "
            "ON DUPLICATE KEY UPDATE start_year=VALUES(start_year), end_year=VALUES(end_year)",
            (pid, iid, rel, sy, ey),
        )


def link_awards(cur, pid, items):
    for it in items:
        if isinstance(it, str):
            en, zh, year, share, note = it, None, 0, "独享", None
        else:
            en = it["name_en"]
            zh = it.get("name_zh")
            year = it.get("year", 0)
            share = it.get("share_type", "独享")
            note = it.get("note")
        aid, _ = get_or_create_award(en, zh)
        cur.execute(
            "INSERT IGNORE INTO award_laureate(person_id, award_id, year, share_type, source, note) "
            "VALUES (%s,%s,%s,%s,'yaml',%s)",
            (pid, aid, year, share, note),
        )


def link_relations(cur, pid, items, by_en, by_zh):
    """社会关系。direction: advisor(对方是导师) / student(对方是学生) / 空(无向)。"""
    occ_id = get_or_create("occupations", "mathematician", "数学家")[0]
    for it in items:
        rt = it["type"]
        name = it["person"]
        note = it.get("note")
        direction = it.get("direction")

        other = by_en.get(norm(name)) or by_zh.get(norm(name))
        if other is None:
            cur.execute(
                "INSERT INTO people(name_en, primary_occupation, has_biography) VALUES (%s,'mathematician',0)",
                (name,),
            )
            other = cur.lastrowid
            cur.execute(
                "INSERT IGNORE INTO person_occupation(person_id, occupation_id, `rank`) VALUES (%s,%s,0)",
                (other, occ_id),
            )
            by_en[norm(name)] = other

        if rt == "advisor-student":
            if direction == "advisor":
                f, t = other, pid
            elif direction == "student":
                f, t = pid, other
            else:
                f, t = sorted([pid, other])
        elif rt == "parent-child":
            if direction == "parent":
                f, t = other, pid
            elif direction == "child":
                f, t = pid, other
            else:
                f, t = sorted([pid, other])
        else:
            f, t = sorted([pid, other])

        cur.execute(
            "INSERT IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (%s,%s,%s,%s,'yaml')",
            (f, t, rt, note),
        )


# ---------------- 单个人物处理 ----------------

def process_one(cur, d, by_en, by_zh, dry_run=False):
    pid, created = upsert_person(cur, d)
    if dry_run:
        return pid, created

    if d.get("occupations"):
        link_occupations(cur, pid, d["occupations"])
    if d.get("fields"):
        link_fields(cur, pid, d["fields"])
    if d.get("nationalities"):
        link_nationalities(cur, pid, d["nationalities"])
    if d.get("institutions"):
        link_institutions(cur, pid, d["institutions"])
    if d.get("awards"):
        link_awards(cur, pid, d["awards"])
    if d.get("relations"):
        link_relations(cur, pid, d["relations"], by_en, by_zh)
    return pid, created


# ---------------- 入口 ----------------

def main():
    ap = argparse.ArgumentParser(description="通用人物入库引擎")
    ap.add_argument("paths", nargs="*", help="YAML 文件或目录")
    ap.add_argument("--all", action="store_true", help="入库指定目录下所有 yaml")
    ap.add_argument("--dry-run", action="store_true", help="仅解析预览，不写库")
    args = ap.parse_args()

    files = []
    for p in args.paths:
        if os.path.isdir(p):
            files += [os.path.join(p, f) for f in sorted(os.listdir(p)) if f.endswith((".yaml", ".yml"))]
        else:
            files.append(p)
    if not files:
        if os.path.isdir("data"):
            files = [os.path.join("data", f) for f in sorted(os.listdir("data")) if f.endswith((".yaml", ".yml"))]
    if not files:
        print("用法: python3 seed_person.py data/xxx.yaml  或  python3 seed_person.py --all data/")
        sys.exit(1)

    conn = get_conn()
    cur = conn.cursor()
    get_or_create.cur = cur

    cur.execute("SELECT id, name_en, name_zh FROM people")
    by_en, by_zh = {}, {}
    for pid, en, zh in cur.fetchall():
        if en:
            by_en[norm(en)] = pid
        if zh:
            by_zh[norm(zh)] = pid

    for fp in files:
        with open(fp, encoding="utf-8") as f:
            d = yaml.safe_load(f)
        if not d or "name_en" not in d:
            print("  SKIP " + fp + " (缺 name_en)")
            continue
        pid, created = process_one(cur, d, by_en, by_zh, dry_run=args.dry_run)
        tag = "NEW" if created else "UPD"
        print("  " + tag + " #" + str(pid).ljust(5) + " " + d["name_en"] + "  <- " + os.path.basename(fp))

    if not args.dry_run:
        conn.commit()
        print("=== COMMITTED ===")
    else:
        conn.rollback()
        print("=== DRY-RUN (未写库) ===")
    conn.close()


if __name__ == "__main__":
    main()
