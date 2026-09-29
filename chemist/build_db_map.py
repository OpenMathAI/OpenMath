#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 20 世纪化学诺奖得主 -> greatminds 库存量记录对照清单 prompt_db_map.json。"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "MySQL"))
from db_mysql import get_conn

ROOT = Path(__file__).resolve().parent

NAMES = [
    # (名单英文名, pages 目录名)
    ("Marie Curie", "Marie_Curie"),
    ("Victor Grignard", "Victor_Grignard"),
    ("Paul Sabatier", "Paul_Sabatier_chemist"),
    ("Alfred Werner", "Alfred_Werner"),
    ("Theodore William Richards", "Theodore_William_Richards"),
    ("Richard Willstätter", "Richard_Willstätter"),
    ("Fritz Haber", "Fritz_Haber"),
    ("Walther Nernst", "Walther_Nernst"),
    ("Frederick Soddy", "Frederick_Soddy"),
    ("Francis William Aston", "Francis_William_Aston"),
    ("Fritz Pregl", "Fritz_Pregl"),
    ("Richard Adolf Zsigmondy", "Richard_Adolf_Zsigmondy"),
    ("Theodor Svedberg", "Theodor_Svedberg"),
    ("Heinrich Otto Wieland", "Heinrich_Otto_Wieland"),
    ("Adolf Windaus", "Adolf_Windaus"),
    ("Arthur Harden", "Arthur_Harden"),
    ("Hans von Euler-Chelpin", "Hans_von_Euler-Chelpin"),
    ("Hans Fischer", "Hans_Fischer"),
    ("Carl Bosch", "Carl_Bosch"),
    ("Friedrich Bergius", "Friedrich_Bergius"),
    ("Irving Langmuir", "Irving_Langmuir"),
    ("Harold Urey", "Harold_Urey"),
    ("Frédéric Joliot-Curie", "Frédéric_Joliot-Curie"),
    ("Irène Joliot-Curie", "Irène_Joliot-Curie"),
    ("Peter Debye", "Peter_Debye"),
    ("Norman Haworth", "Norman_Haworth"),
    ("Paul Karrer", "Paul_Karrer"),
    ("Richard Kuhn", "Richard_Kuhn"),
    ("Adolf Butenandt", "Adolf_Butenandt"),
    ("Leopold Ružička", "Leopold_Ružička"),
    ("George de Hevesy", "George_de_Hevesy"),
    ("Otto Hahn", "Otto_Hahn"),
    ("Artturi Ilmari Virtanen", "Artturi_Ilmari_Virtanen"),
    ("James B. Sumner", "James_B._Sumner"),
    ("John Howard Northrop", "John_Howard_Northrop"),
    ("Wendell Meredith Stanley", "Wendell_Meredith_Stanley"),
    ("Robert Robinson", "Robert_Robinson_organic_chemist"),
    ("Arne Tiselius", "Arne_Tiselius"),
    ("William Giauque", "William_Giauque"),
    ("Otto Diels", "Otto_Diels"),
    ("Kurt Alder", "Kurt_Alder"),
    ("Edwin McMillan", "Edwin_McMillan"),
    ("Glenn T. Seaborg", "Glenn_T._Seaborg"),
    ("Archer Martin", "Archer_Martin"),
    ("Richard Laurence Millington Synge", "Richard_Laurence_Millington_Synge"),
    ("Hermann Staudinger", "Hermann_Staudinger"),
    ("Linus Pauling", "Linus_Pauling"),
    ("Vincent du Vigneaud", "Vincent_du_Vigneaud"),
    ("Cyril Norman Hinshelwood", "Cyril_Norman_Hinshelwood"),
    ("Nikolay Semyonov", "Nikolay_Semyonov"),
    ("Alexander R. Todd", "Alexander_R._Todd"),
    ("Jaroslav Heyrovský", "Jaroslav_Heyrovský"),
    ("Willard Libby", "Willard_Libby"),
    ("Melvin Calvin", "Melvin_Calvin"),
    ("Max Perutz", "Max_Perutz"),
    ("John Kendrew", "John_Kendrew"),
    ("Karl Ziegler", "Karl_Ziegler"),
    ("Giulio Natta", "Giulio_Natta"),
    ("Dorothy Hodgkin", "Dorothy_Hodgkin"),
    ("Robert Burns Woodward", "Robert_Burns_Woodward"),
    ("Robert S. Mulliken", "Robert_S._Mulliken"),
    ("Manfred Eigen", "Manfred_Eigen"),
    ("Ronald George Wreyford Norrish", "Ronald_George_Wreyford_Norrish"),
    ("George Porter", "George_Porter"),
    ("Lars Onsager", "Lars_Onsager"),
    ("Derek Barton", "Derek_Barton"),
    ("Odd Hassel", "Odd_Hassel"),
    ("Luis Federico Leloir", "Luis_Federico_Leloir"),
    ("Gerhard Herzberg", "Gerhard_Herzberg"),
    ("Christian B. Anfinsen", "Christian_B._Anfinsen"),
    ("Stanford Moore", "Stanford_Moore"),
    ("William Howard Stein", "William_Howard_Stein"),
    ("Ernst Otto Fischer", "Ernst_Otto_Fischer"),
    ("Geoffrey Wilkinson", "Geoffrey_Wilkinson"),
    ("Paul Flory", "Paul_Flory"),
    ("John Cornforth", "John_Cornforth"),
    ("Vladimir Prelog", "Vladimir_Prelog"),
    ("William Lipscomb", "William_Lipscomb"),
    ("Ilya Prigogine", "Ilya_Prigogine"),
    ("Peter D. Mitchell", "Peter_D._Mitchell"),
    ("Herbert C. Brown", "Herbert_C._Brown"),
    ("Georg Wittig", "Georg_Wittig"),
    ("Paul Berg", "Paul_Berg"),
    ("Walter Gilbert", "Walter_Gilbert"),
    ("Kenichi Fukui", "Kenichi_Fukui"),
    ("Roald Hoffmann", "Roald_Hoffmann"),
    ("Aaron Klug", "Aaron_Klug"),
    ("Henry Taube", "Henry_Taube"),
    ("Robert Bruce Merrifield", "Robert_Bruce_Merrifield"),
    ("Herbert A. Hauptman", "Herbert_A._Hauptman"),
    ("Jerome Karle", "Jerome_Karle"),
    ("Dudley R. Herschbach", "Dudley_R._Herschbach"),
    ("Yuan T. Lee", "Yuan_T._Lee"),
    ("John Polanyi", "John_Polanyi"),
    ("Donald J. Cram", "Donald_J._Cram"),
    ("Jean-Marie Lehn", "Jean-Marie_Lehn"),
    ("Charles J. Pedersen", "Charles_J._Pedersen"),
    ("Johann Deisenhofer", "Johann_Deisenhofer"),
    ("Robert Huber", "Robert_Huber"),
    ("Hartmut Michel", "Hartmut_Michel"),
    ("Sidney Altman", "Sidney_Altman"),
    ("Thomas Cech", "Thomas_Cech"),
    ("Elias James Corey", "Elias_James_Corey"),
    ("Richard R. Ernst", "Richard_R._Ernst"),
    ("Rudolph A. Marcus", "Rudolph_A._Marcus"),
    ("Kary Mullis", "Kary_Mullis"),
    ("Michael Smith", "Michael_Smith_chemist"),
    ("George Andrew Olah", "George_Andrew_Olah"),
    ("Paul J. Crutzen", "Paul_J._Crutzen"),
    ("Mario J. Molina", "Mario_J._Molina"),
    ("F. Sherwood Rowland", "F._Sherwood_Rowland"),
    ("Robert Curl", "Robert_Curl"),
    ("Harry Kroto", "Harry_Kroto"),
    ("Richard Smalley", "Richard_Smalley"),
    ("Paul D. Boyer", "Paul_D._Boyer"),
    ("John E. Walker", "John_E._Walker"),
    ("Jens Christian Skou", "Jens_Christian_Skou"),
    ("Walter Kohn", "Walter_Kohn"),
    ("John Pople", "John_Pople"),
    ("Ahmed Zewail", "Ahmed_Zewail"),
    ("Alan J. Heeger", "Alan_J._Heeger"),
    ("Alan MacDiarmid", "Alan_MacDiarmid"),
    ("Hideki Shirakawa", "Hideki_Shirakawa"),
    # 1901-1910 已有提示词，仅需入库
    ("Jacobus Henricus van 't Hoff", "Jacobus_Henricus_van_t_Hoff"),
    ("Hermann Emil Fischer", "Hermann_Emil_Fischer"),
    ("Svante Arrhenius", "Svante_Arrhenius"),
    ("William Ramsay", "William_Ramsay"),
    ("Adolf von Baeyer", "Adolf_von_Baeyer"),
    ("Henri Moissan", "Henri_Moissan"),
    ("Eduard Buchner", "Eduard_Buchner"),
    ("Ernest Rutherford", "Ernest_Rutherford"),
    ("Wilhelm Ostwald", "Wilhelm_Ostwald"),
    ("Otto Wallach", "Otto_Wallach"),
    # 特别篇
    ("Dmitri Mendeleev", "Dmitri_Mendeleev"),
]


def norm(s):
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = re.sub(r"[\s_'.()\u00b7,\-]", "", s)
    return s.lower()


import unicodedata  # noqa: E402

conn = get_conn()
cur = conn.cursor()
cur.execute("SELECT id, name_en, qid, has_social_data, has_biography FROM people")
people = cur.fetchall()
by_exact = {}
by_norm = {}
for pid, en, qid, soc, bio in people:
    if en:
        by_exact[en] = {"id": pid, "name_en": en, "qid": qid, "social": soc, "bio": bio}
        by_norm.setdefault(norm(en), []).append(by_exact[en])

out = {}
missing = []
for name, dirname in NAMES:
    hits = None
    if name in by_exact:
        hits = [by_exact[name]]
    else:
        hits = by_norm.get(norm(name), [])
    if len(hits) == 1:
        out[name] = {"dir": dirname, "db": hits[0]}
    elif len(hits) == 0:
        out[name] = {"dir": dirname, "db": None}
        missing.append(name)
    else:
        out[name] = {"dir": dirname, "db": hits}
        missing.append(name + " (多记录!)")

Path(ROOT / "prompt_db_map.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8"
)
print("总人数:", len(NAMES), " 无库记录:", len([m for m in missing if '多记录' not in m]))
for m in missing:
    print(" -", m)
# 打印所有已有库记录的
print("\n== 已有库记录（须复用/回填 QID）==")
for name, dirname in NAMES:
    v = out[name]
    db = v["db"]
    if isinstance(db, dict):
        print(f"  {name} -> #{db['id']} qid={db['qid']} social={db['social']} bio={db['bio']}")
    elif isinstance(db, list):
        print(f"  {name} -> 多记录: {db}")
