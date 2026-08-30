#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""从 greatminds 数据库导出所有 has_social_data=1 的人物 → data/*.yaml。

这是「YAML 化重构」的迁移工具：把已入库的存量数据（原 174 个 seed 脚本的产物）
统一导出为 data/ 目录下的 YAML 数据文件，供通用引擎 seed_person.py 重新入库。

用法:
  python3 export_db_to_yaml.py            # 导出到 data/
  python3 export_db_to_yaml.py --out /tmp/data
  python3 export_db_to_yaml.py --limit 5  # 只导出前 5 个（调试用）
"""
import argparse
import json
import os
import re
import sys

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from db_mysql import get_conn


def strip_marker(note):
    """去掉「[XXX-材料待展开] / [材料待展开]」等前缀，让 yaml 里的 note 干净。"""
    if not note:
        return note
    note = re.sub(r"^\[[^\]]*材料待展开[^\]]*\]\s*", "", note)
    note = re.sub(r"^\[[^\]]*待展开[^\]]*\]\s*", "", note)
    return note.strip()


def parse_variants(raw):
    """name_variants 可能是 JSON 字符串或逗号分隔，统一转列表。"""
    if not raw:
        return None
    raw = raw.strip()
    if raw.startswith("["):
        try:
            v = json.loads(raw)
            return v if isinstance(v, list) and v else None
        except Exception:
            pass
    parts = [p.strip() for p in raw.split(",") if p.strip()]
    return parts or None


def drop_none(obj):
    """递归移除 dict 中值为 None 的键，让 yaml 更干净。"""
    if isinstance(obj, dict):
        return {k: drop_none(v) for k, v in obj.items() if v is not None}
    if isinstance(obj, list):
        return [drop_none(x) for x in obj]
    return obj


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="data")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    os.makedirs(args.out, exist_ok=True)
    conn = get_conn()
    cur = conn.cursor()

    # ---- 字典表 id -> (name_en, name_zh) ----
    def dict_map(table):
        cur.execute("SELECT id, name_en, name_zh FROM " + table)
        return {r[0]: (r[1], r[2]) for r in cur.fetchall()}

    occ = dict_map("occupations")
    fld = dict_map("fields")
    cty = dict_map("countries")
    inst = dict_map("institutions")
    awd = dict_map("awards")

    # ---- 主角：has_social_data=1 ----
    cur.execute("SELECT id FROM people WHERE has_social_data=1 ORDER BY name_en")
    ids = [r[0] for r in cur.fetchall()]
    if args.limit:
        ids = ids[: args.limit]
    print("共导出 %d 位主角" % len(ids))

    for pid in ids:
        cur.execute(
            "SELECT qid, name_en, name_zh, name_variants, gender, birth_date, "
            "death_date, description, primary_occupation, has_biography "
            "FROM people WHERE id=%s",
            (pid,),
        )
        (qid, name_en, name_zh, nv, gender, bd, dd, desc, prim, has_bio) = cur.fetchone()

        d = {"name_en": name_en}
        if qid:
            d["qid"] = qid
        if name_zh:
            d["name_zh"] = name_zh
        variants = parse_variants(nv)
        if variants:
            d["name_variants"] = variants
        if gender:
            d["gender"] = gender
        if bd:
            d["birth_date"] = bd
        if dd:
            d["death_date"] = dd
        if desc:
            d["description"] = desc
        if prim:
            d["primary_occupation"] = prim
        d["has_biography"] = bool(has_bio)

        # occupations
        cur.execute(
            "SELECT occupation_id, `rank` FROM person_occupation WHERE person_id=%s ORDER BY `rank`",
            (pid,),
        )
        oc = []
        for oid, rk in cur.fetchall():
            en, zh = occ.get(oid, ("?", None))
            it = {"name_en": en, "rank": rk}
            if zh:
                it["name_zh"] = zh
            oc.append(it)
        if oc:
            d["occupations"] = oc

        # fields
        cur.execute(
            "SELECT field_id, `rank` FROM person_field WHERE person_id=%s ORDER BY `rank`",
            (pid,),
        )
        fs = []
        for fid, rk in cur.fetchall():
            en, zh = fld.get(fid, ("?", None))
            it = {"name_en": en, "rank": rk}
            if zh:
                it["name_zh"] = zh
            fs.append(it)
        if fs:
            d["fields"] = fs

        # nationalities
        cur.execute(
            "SELECT country_id, `rank`, era_note FROM person_nationality WHERE person_id=%s ORDER BY `rank`",
            (pid,),
        )
        ns = []
        for cid, rk, era in cur.fetchall():
            en, zh = cty.get(cid, ("?", None))
            it = {"name_en": en, "rank": rk}
            if zh:
                it["name_zh"] = zh
            if era:
                it["era_note"] = era
            ns.append(it)
        if ns:
            d["nationalities"] = ns

        # institutions
        cur.execute(
            "SELECT inst_id, relation, start_year, end_year FROM person_institution "
            "WHERE person_id=%s ORDER BY start_year",
            (pid,),
        )
        ins = []
        for iid, rel, sy, ey in cur.fetchall():
            en, zh = inst.get(iid, ("?", None))
            it = {"name_en": en, "relation": rel}
            if zh:
                it["name_zh"] = zh
            if sy:
                it["start_year"] = sy
            if ey:
                it["end_year"] = ey
            ins.append(it)
        if ins:
            d["institutions"] = ins

        # awards
        cur.execute(
            "SELECT award_id, year, share_type, note FROM award_laureate WHERE person_id=%s ORDER BY year",
            (pid,),
        )
        as_ = []
        for aid, yr, share, note in cur.fetchall():
            en, zh = awd.get(aid, ("?", None))
            it = {"name_en": en, "year": yr}
            if zh:
                it["name_zh"] = zh
            if share and share != "独享":
                it["share_type"] = share
            if note:
                it["note"] = note
            as_.append(it)
        if as_:
            d["awards"] = as_

        # relations（双向）
        cur.execute(
            "SELECT from_id, to_id, relation_type, note FROM person_relation "
            "WHERE from_id=%s OR to_id=%s ORDER BY relation_type",
            (pid, pid),
        )
        rels = []
        for frm, to, rt, note in cur.fetchall():
            if frm == pid:
                other = to
                is_from = True
            else:
                other = frm
                is_from = False
            cur.execute("SELECT name_en, name_zh FROM people WHERE id=%s", (other,))
            row = cur.fetchone()
            person_name = row[0] if row else "?"
            it = {"type": rt, "person": person_name}
            note = strip_marker(note)
            if note:
                it["note"] = note
            # 有向关系方向
            if rt == "advisor-student":
                it["direction"] = "student" if is_from else "advisor"
            elif rt == "parent-child":
                it["direction"] = "child" if is_from else "parent"
            rels.append(it)
        if rels:
            d["relations"] = rels

        d = drop_none(d)

        # 文件名：安全化 name_en（纯中文时回退用 qid）
        fname = re.sub(r"[^A-Za-z0-9]+", "_", name_en).strip("_")
        if not fname:
            fname = qid or ("person_" + str(pid))
        fname += ".yaml"
        fpath = os.path.join(args.out, fname)
        with open(fpath, "w", encoding="utf-8") as f:
            yaml.safe_dump(
                d, f, allow_unicode=True, sort_keys=False, default_flow_style=False,
                width=120,
            )
        print("  " + fname + "  <- " + name_en)

    conn.close()
    print("=== 导出完成 → " + args.out + " ===")


if __name__ == "__main__":
    main()
