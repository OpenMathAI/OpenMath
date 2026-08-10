#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""交叉信息验证：数据库生成的交叉结果 vs medal_list_allinone/all_cross_reference.md 期望值。

对每类交叉，输出数据库实际名单，并与文档期望对比：
- ✅ 完全一致（名单逐人相同）
- ⚠️ 数据库多出（文档未列）
- ⚠️ 数据库缺失（文档已列）
"""
from db_mysql import get_conn

# name_en 归一化别名（库中缩写/名序差异 → 文档标准名）
NAME_CANON = {
    "J.-P. Serre": "Jean-Pierre Serre",
    "Kodaira Kunihiko": "Kunihiko Kodaira",
}


def canon(name):
    return NAME_CANON.get(name, name)


# 文档期望（all_cross_reference.md）：交叉类型 -> 期望名单（库中 name_en）
EXPECT = {
    "F+W+A 三奖": ["Jean-Pierre Serre", "John Milnor", "John G. Thompson", "Pierre Deligne", "Grigory Margulis"],
    "F+W 双奖": ["Lars Ahlfors", "Atle Selberg", "Kunihiko Kodaira", "Lars Hörmander", "Stephen Smale",
                 "Sergei Novikov", "David Mumford", "Charles Fefferman", "Shing-Tung Yau", "Simon Donaldson", "Vladimir Drinfeld"],
    "W+A": ["Peter Lax", "Lennart Carleson", "Jacques Tits", "Mikhail Gromov", "Andrew Wiles", "Robert Langlands",
            "Yakov Sinai", "László Lovász", "John Tate", "Hillel Furstenberg", "Dennis Sullivan", "Luis Caffarelli",
            "John Milnor", "Pierre Deligne", "John G. Thompson", "Grigory Margulis", "Jean-Pierre Serre"],
    "F+A": ["Michael Atiyah", "Gerd Faltings"],
    "W+C": ["Phillip Griffiths"],
    "A+C": ["Louis Nirenberg", "Masaki Kashiwara"],
    "Turing+Nobel": ["Herbert A. Simon", "Geoffrey Hinton"],
    "Turing+Wolf": ["Charles H. Bennett", "Gilles Brassard", "Adi Shamir"],
    "Turing+Kyoto": ["Donald E. Knuth", "John McCarthy", "Andrew Yao", "Richard M. Karp", "Tony Hoare",
                     "Ivan Sutherland", "Alan Kay"],
    "Turing+Gödel": ["Shafi Goldwasser", "Silvio Micali", "Avi Wigderson"],
    "Turing+Hamming/Shannon": ["Richard Hamming", "Whitfield Diffie", "Martin E. Hellman", "Charles H. Bennett"],
    "Turing+Japan": ["Marvin Minsky", "Dennis Ritchie", "Ken Thompson", "Vint Cerf"],
    "Turing+Nevanlinna": ["Robert Tarjan", "Leslie Valiant", "Avi Wigderson"],
    "Turing+Marconi": ["Ronald Rivest", "Vint Cerf", "Whitfield Diffie", "Martin E. Hellman", "Robert Metcalfe"],
    "Turing+vonNeumann": ["Ivan Sutherland", "Barbara Liskov", "Leslie Lamport"],
}

# 各交叉的奖项判定（award_name_en 集合）
# 用 count-of-set 判定「恰好/至少」
QUERIES = {
    "F+W+A 三奖": {"set": ["Fields Medal", "Wolf Prize in Mathematics", "Abel Prize"], "mode": "all3"},
    "F+W 双奖": {"set": ["Fields Medal", "Wolf Prize in Mathematics", "Abel Prize"], "mode": "FW_only"},
    "W+A": {"set": ["Fields Medal", "Wolf Prize in Mathematics", "Abel Prize"], "mode": "has_W_has_A"},
    "F+A": {"set": ["Fields Medal", "Wolf Prize in Mathematics", "Abel Prize"], "mode": "FA_only"},
    "W+C": {"set": ["Wolf Prize in Mathematics", "Chern Medal"], "mode": "all2"},
    "A+C": {"set": ["Abel Prize", "Chern Medal"], "mode": "all2"},
    "Turing+Nobel": {"set": ["ACM A.M. Turing Award", "Nobel Prize in Physics", "Nobel Memorial Prize in Economic Sciences"], "mode": "T_and_anyNobel"},
    "Turing+Wolf": {"set": ["ACM A.M. Turing Award", "Wolf Prize in Mathematics", "Wolf Prize in Physics"], "mode": "T_and_anyWolf"},
    "Turing+Kyoto": {"set": ["ACM A.M. Turing Award", "Kyoto Prize"], "mode": "all2"},
    "Turing+Gödel": {"set": ["ACM A.M. Turing Award", "Gödel Prize"], "mode": "all2"},
    "Turing+Hamming/Shannon": {"set": ["ACM A.M. Turing Award", "IEEE Richard W. Hamming Medal", "Claude E. Shannon Award"], "mode": "T_and_anyHS"},
    "Turing+Japan": {"set": ["ACM A.M. Turing Award", "Japan Prize"], "mode": "all2"},
    "Turing+Nevanlinna": {"set": ["ACM A.M. Turing Award", "Rolf Nevanlinna Prize"], "mode": "all2"},
    "Turing+Marconi": {"set": ["ACM A.M. Turing Award", "Marconi Prize"], "mode": "all2"},
    "Turing+vonNeumann": {"set": ["ACM A.M. Turing Award", "IEEE John von Neumann Medal"], "mode": "all2"},
}


def get_person_awards(cur):
    """person_id -> {award_name_en: [years]}"""
    cur.execute("""
        SELECT p.id, a.name_en, al.year
        FROM award_laureate al
        JOIN awards a ON a.id = al.award_id
        JOIN people p ON p.id = al.person_id
    """)
    d = {}
    for pid, an, yr in cur.fetchall():
        d.setdefault(pid, {}).setdefault(an, []).append(yr)
    return d


def matches(pa, spec):
    """判定 person_awards 是否满足交叉条件"""
    s = spec["set"]
    mode = spec["mode"]
    names = set(pa.keys())
    if mode == "all3":
        return all(n in names for n in s)
    if mode == "FW_only":
        return "Fields Medal" in names and "Wolf Prize in Mathematics" in names and "Abel Prize" not in names
    if mode == "FA_only":
        return "Fields Medal" in names and "Abel Prize" in names and "Wolf Prize in Mathematics" not in names
    if mode == "has_W_has_A":
        return "Wolf Prize in Mathematics" in names and "Abel Prize" in names
    if mode == "all2":
        return all(n in names for n in s)
    if mode == "T_and_anyNobel":
        return "ACM A.M. Turing Award" in names and any(n in names for n in ["Nobel Prize in Physics", "Nobel Memorial Prize in Economic Sciences"])
    if mode == "T_and_anyWolf":
        return "ACM A.M. Turing Award" in names and any(n in names for n in ["Wolf Prize in Mathematics", "Wolf Prize in Physics"])
    if mode == "T_and_anyHS":
        return "ACM A.M. Turing Award" in names and any(n in names for n in ["IEEE Richard W. Hamming Medal", "Claude E. Shannon Award"])
    return False


def main():
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("SELECT id, name_en FROM people")
    id2name = dict(cur.fetchall())
    awards = get_person_awards(cur)
    conn.close()

    total_ok = total_warn = 0
    for label, spec in QUERIES.items():
        actual = sorted(canon(id2name[pid]) for pid in awards if matches(awards[pid], spec))
        expect = sorted(EXPECT.get(label, []))
        missing = sorted(set(expect) - set(actual))
        extra = sorted(set(actual) - set(expect))
        if not missing and not extra:
            status = "✅ PASS"
            total_ok += 1
        else:
            status = "⚠️ DIFF"
            total_warn += 1
        print(f"{status}  {label}  (DB {len(actual)} / 文档 {len(expect)})")
        if missing:
            print(f"       ❌ 文档有但DB缺: {missing}")
        if extra:
            print(f"       ➕ DB有但文档未列: {extra}")
        print(f"       DB实际: {actual}")
    print(f"\n总计: {total_ok} PASS / {total_warn} DIFF")


if __name__ == "__main__":
    main()
