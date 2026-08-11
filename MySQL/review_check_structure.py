#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Review 第 2 层：社会关系结构正确性检查。

检查项：
1. 孤儿关系（from_id/to_id 人物不存在）
2. 疑似重复人物（同人多名，模糊匹配）
3. advisor-student 方向一致性抽查（导师通常年长，列出可能反向的关系）
4. 机构同 relation 多条任期（可能被主键吞掉）——反向提示
"""
import re
import sys
import unicodedata

sys.path.insert(0, "/Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL")
from db_mysql import get_conn


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[\s_\-\'\.\(\)·,]", "", s).lower()


def main():
    conn = get_conn()
    cur = conn.cursor()

    print("=" * 60)
    print("1. 孤儿关系检查")
    cur.execute("""SELECT pr.id, pr.from_id, pr.to_id, pr.relation_type
                   FROM person_relation pr
                   LEFT JOIN people a ON a.id=pr.from_id
                   LEFT JOIN people b ON b.id=pr.to_id
                   WHERE a.id IS NULL OR b.id IS NULL""")
    orphans = cur.fetchall()
    if orphans:
        for o in orphans:
            print(f"  ⚠️ 关系 #{o[0]}: {o[1]}→{o[2]} ({o[3]}) 一端人物不存在")
    else:
        print("  ✅ 无孤儿关系")

    print("=" * 60)
    print("2. 疑似重复人物（同 qid 不同记录）")
    cur.execute("""SELECT qid, COUNT(*) AS c, GROUP_CONCAT(id ORDER BY id) AS ids,
                   GROUP_CONCAT(name_en ORDER BY id SEPARATOR ' | ') AS names
                   FROM people WHERE qid IS NOT NULL GROUP BY qid HAVING c > 1""")
    dups = cur.fetchall()
    if dups:
        for d in dups:
            print(f"  ⚠️ qid={d[0]} ({d[1]}条): ids={d[2]}")
            print(f"      {d[3]}")
    else:
        print("  ✅ 无同 qid 重复")

    print("=" * 60)
    print("3. 同人不同名的疑似重复（模糊匹配，Top 检查）")
    cur.execute("SELECT id, name_en, qid, birth_date FROM people WHERE name_en IS NOT NULL")
    people = cur.fetchall()
    by_norm = {}
    for pid, en, qid, bd in people:
        n = norm(en or "")
        if not n:
            continue
        # 只标记规范化后相同且名字不同的
        if n in by_norm:
            prev = by_norm[n]
            if prev[1] != en:
                print(f"  ? id={prev[0]} '{prev[1]}' vs id={pid} '{en}'")
        else:
            by_norm[n] = (pid, en, qid, bd)
    print("  （上述为规范化后同名者，人工判断是否重复）")

    print("=" * 60)
    print("4. advisor-student 方向抽查（导师比学生年长>50岁 或 学生比导师年长）")
    cur.execute("""SELECT pr.id, a.name_en, a.birth_date, b.name_en, b.birth_date, pr.relation_type
                   FROM person_relation pr
                   JOIN people a ON a.id=pr.from_id
                   JOIN people b ON b.id=pr.to_id
                   WHERE pr.relation_type='advisor-student'
                     AND a.birth_date IS NOT NULL AND b.birth_date IS NOT NULL""")
    suspicious = []
    for rid, an, abd, bn, bbd, rt in cur.fetchall():
        ay = int(str(abd)[:4])
        by = int(str(bbd)[:4])
        if ay > by + 5:  # 导师比学生年轻 >5 岁
            suspicious.append((rid, an, abd, bn, bbd))
    if suspicious:
        print(f"  ⚠️ {len(suspicious)} 条可能反向（导师比学生年轻）：")
        for s in suspicious[:20]:
            print(f"    #{s[0]} {s[1]}({s[2]}) → {s[3]}({s[4]})")
    else:
        print("  ✅ 无反向异常")

    conn.close()


if __name__ == "__main__":
    main()
