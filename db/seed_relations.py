#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""灌入人物社会关系（person_relation），并补充关系涉及但不在库中的人物。

示例关系：
- 哈代 ↔ 拉马努金：师生（advisor-student，哈代 → 拉马努金）
- 哈代 ↔ Littlewood：合作者（collaborator，无向）
- 祖冲之 → 祖暅之：父子（parent-child）

缺失人物（祖冲之、祖暅之）先加入 people，再建立关系。
"""
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DB = ROOT / "greatminds.db"

# 待补充人物：(name_en, name_zh, occupation_en, has_biography)
NEW_PEOPLE = [
    ("Zu Chongzhi", "祖冲之", True),   # presentations/Zu_Chongzhi 已立传
    ("Zu Gengzhi", "祖暅之", False),   # 祖暅之（祖暅定理），未立传
]

# 关系：(from_name, to_name, relation_key, note, directed)
RELATIONS = [
    ("G.H. Hardy", "Srinivasa Ramanujan", "advisor-student",
     "哈代是拉马努金的导师/伯乐，1914 年将拉马努金邀请至剑桥", 1),
    ("G.H. Hardy", "J.E. Littlewood", "collaborator",
     "哈代与李特尔伍德长期合作（Hardy–Littlewood 学派）", 0),
    ("Zu Chongzhi", "Zu Gengzhi", "parent-child",
     "祖冲之是祖暅之的父亲；父子合著《缀术》", 1),
]


def find(cur, name):
    cur.execute("SELECT id FROM people WHERE name_en=? OR name_zh=?", (name, name))
    row = cur.fetchone()
    return row[0] if row else None


def main():
    conn = sqlite3.connect(DB)
    conn.execute("PRAGMA foreign_keys = ON")
    cur = conn.cursor()

    # 1) 补充缺失人物
    for en, zh, has_bio in NEW_PEOPLE:
        if find(cur, en) is None:
            cur.execute(
                "INSERT INTO people(name_en, name_zh, primary_occupation, has_biography) VALUES (?,?,?,?)",
                (en, zh, "mathematician", 1 if has_bio else 0),
            )
            pid = cur.lastrowid
            cur.execute("INSERT OR IGNORE INTO person_occupation(person_id, occupation_id, rank) "
                        "SELECT ?, id, 0 FROM occupations WHERE name_en='mathematician'", (pid,))
            print(f"新增人物: {en}（{zh}）")
        else:
            print(f"人物已存在: {en}")

    # 2) 灌入关系
    added = 0
    for f, t, rel, note, directed in RELATIONS:
        fid = find(cur, f)
        tid = find(cur, t)
        if not fid or not tid:
            print(f"⚠ 跳过关系（人物缺失）: {f} → {t}（{rel}）")
            continue
        # 无向关系按 id 大小归一存储（MIN→MAX），避免重复
        if not directed and fid > tid:
            fid, tid = tid, fid
        cur.execute(
            "INSERT OR IGNORE INTO person_relation(from_id, to_id, relation_type, note, source) "
            "VALUES (?,?,?,?, 'seed_relations.py')",
            (fid, tid, rel, note),
        )
        if cur.rowcount:
            added += 1
            print(f"关系已建: {f} → {t}（{rel}）")

    conn.commit()
    print(f"\n新增关系: {added} 条")
    cur.execute("SELECT COUNT(*) FROM person_relation")
    print(f"person_relation 总数: {cur.fetchone()[0]}")
    cur.execute("SELECT COUNT(*) FROM people")
    print(f"people 总数: {cur.fetchone()[0]}")
    conn.close()


if __name__ == "__main__":
    main()
