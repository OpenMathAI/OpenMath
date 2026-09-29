#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成 chem-batch 分配清单 prompt_manifest.json：
123 位 1911-2000 得主（提示词 + 入库）按年代 5 人/批；
1901-1910 十位 + Mendeleev 仅入库（2 批）。
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
db_map = json.loads((ROOT / "prompt_db_map.json").read_text(encoding="utf-8"))

MA = Path(__file__).resolve().parent.parent / "music_audio"

BGM = {
    "New Lands": MA / "alex-productions/74-oK8HN0FsZmc-New-Lands.wav",
    "Timeless": MA / "alex-productions/42-SyPUvzEkPyc-Timeless.wav",
    "PAST": MA / "alex-productions/89-geyy8_WXDK0-PAST.wav",
    "Nostalgia": MA / "alex-productions/86-5ETNuoDcBg4-Nostalgia.wav",
    "Awaken": MA / "alex-productions/36-aqLUvpAdLNQ-Awaken.wav",
    "SEA": MA / "alex-productions/92-WEqfdRXU3IU-SEA.wav",
    "Expedition": MA / "alex-productions/33--_CEmB_dHpA-Expedition.wav",
    "The Flow of Time": MA / "alex-productions/35-jqIDnltiDRI-The-Flow-of-Time.wav",
    "Daylight": MA / "alex-productions/44-JoyIRE5k2Yo-Daylight.wav",
    "Savage": MA / "alex-productions/34-pILVwyuW3jw-Savage.wav",
    "Tragedy": MA / "alex-productions/80-K5f65-22sY4-Tragedy.wav",
    "With Me": MA / "alex-productions/83-DXAblXgCK-k-With-Me.wav",
    "Eternals": MA / "alex-productions/76-V5T_kW2PH_s-Eternals.wav",
    "Cinematic Experience": MA / "alex-productions/48-QL3O8MUFAm4-Cinematic-Experience.wav",
    "Lonesome": MA / "inspiring-electronic/16-xBLYHNv7C4Q-Lonesome - by AShamaluevMusic ｜ Sad and Emotional Cinematic Music.wav",
    "Nostalgy": MA / "inspiring-electronic/17-_DA0mdtL-jI-Nostalgy - by AShamaluevMusic ｜ Sad Cinematic Music For Videos, Documentaries & Films.wav",
    "Through the Darkness": MA / "inspiring-electronic/14-Trn1cSsY2t8-Audiomachine - Through the Darkness.wav",
    "Last Hope": MA / "inspiring-electronic/24-ie5iLcdKiqk-Victor Cooper - Last Hope (Dramatic Powerful Epic Copyright Free Music).wav",
    "Empire Collapse": MA / "inspiring-electronic/12-NTuSqFy4Stc-Cinematic Dramatic Epic Drone Orchestra Film by Cold Cinema [No Copyright Music] ⧸ Empire Collapse.wav",
    "Ascension": MA / "inspiring-electronic/20-gYUC-sXt_8M-Cinematic Dramatic Epic Orchestra Sci-Fi Trailer by Cold Cinema [No Copyright Music] ⧸ Ascension.wav",
    "The Invisible Light": MA / "inspiring-electronic/19-tGxXsgSKPiQ-Documentary Cinematic by Infraction [No Copyright Music] ⧸ The Invisible Light.wav",
    "Winds Of Freedom": MA / "inspiring-electronic/25-l3Fsk4R6eys-Really Slow Motion & Giant Apes - Winds Of Freedom (Epic Heroic Orchestral).wav",
    "Falling Apart": MA / "inspiring-electronic/03-qtNSLNUd1VE-Michael FK & Andy Leech - Falling Apart.wav",
    "Mirage": MA / "inspiring-electronic/04-5gcb94jhG1I-Notan Nigres - Mirage (Audio).wav",
    "Shine Like The Sun": MA / "inspiring-electronic/15-w6kT1BfvETI-Really Slow Motion - Shine Like The Sun (Epic Beautiful Uplifting).wav",
    "Pathfinder": MA / "inspiring-electronic/23-GiwYLGgJw7w-Ghostwriter Music - Pathfinder (Composed by Daniel Beijbom - Recorded in Budapest).wav",
}

# 123 位 1911-2000 得主（年代序）
PROMPT_PEOPLE = [
    ("Marie Curie", 1911), ("Victor Grignard", 1912), ("Paul Sabatier", 1912),
    ("Alfred Werner", 1913), ("Theodore William Richards", 1914),
    ("Richard Willstätter", 1915), ("Fritz Haber", 1918), ("Walther Nernst", 1920),
    ("Frederick Soddy", 1921), ("Francis William Aston", 1922),
    ("Fritz Pregl", 1923), ("Richard Adolf Zsigmondy", 1925),
    ("Theodor Svedberg", 1926), ("Heinrich Otto Wieland", 1927),
    ("Adolf Windaus", 1928), ("Arthur Harden", 1929),
    ("Hans von Euler-Chelpin", 1929), ("Hans Fischer", 1930),
    ("Carl Bosch", 1931), ("Friedrich Bergius", 1931),
    ("Irving Langmuir", 1932), ("Harold Urey", 1934),
    ("Frédéric Joliot-Curie", 1935), ("Irène Joliot-Curie", 1935),
    ("Peter Debye", 1936), ("Norman Haworth", 1937), ("Paul Karrer", 1937),
    ("Richard Kuhn", 1938), ("Adolf Butenandt", 1939), ("Leopold Ružička", 1939),
    ("George de Hevesy", 1943), ("Otto Hahn", 1944),
    ("Artturi Ilmari Virtanen", 1945), ("James B. Sumner", 1946),
    ("John Howard Northrop", 1946), ("Wendell Meredith Stanley", 1946),
    ("Robert Robinson", 1947), ("Arne Tiselius", 1948), ("William Giauque", 1949),
    ("Otto Diels", 1950), ("Kurt Alder", 1950),
    ("Edwin McMillan", 1951), ("Glenn T. Seaborg", 1951),
    ("Archer Martin", 1952), ("Richard Laurence Millington Synge", 1952),
    ("Hermann Staudinger", 1953), ("Linus Pauling", 1954),
    ("Vincent du Vigneaud", 1955), ("Cyril Norman Hinshelwood", 1956),
    ("Nikolay Semyonov", 1956), ("Alexander R. Todd", 1957),
    ("Jaroslav Heyrovský", 1959), ("Willard Libby", 1960), ("Melvin Calvin", 1961),
    ("Max Perutz", 1962), ("John Kendrew", 1962),
    ("Karl Ziegler", 1963), ("Giulio Natta", 1963), ("Dorothy Hodgkin", 1964),
    ("Robert Burns Woodward", 1965), ("Robert S. Mulliken", 1966),
    ("Manfred Eigen", 1967), ("Ronald George Wreyford Norrish", 1967),
    ("George Porter", 1967), ("Lars Onsager", 1968),
    ("Derek Barton", 1969), ("Odd Hassel", 1969),
    ("Luis Federico Leloir", 1970), ("Gerhard Herzberg", 1971),
    ("Christian B. Anfinsen", 1972), ("Stanford Moore", 1972),
    ("William Howard Stein", 1972), ("Ernst Otto Fischer", 1973),
    ("Geoffrey Wilkinson", 1973), ("Paul Flory", 1974),
    ("John Cornforth", 1975), ("Vladimir Prelog", 1975),
    ("William Lipscomb", 1976), ("Ilya Prigogine", 1977),
    ("Peter D. Mitchell", 1978), ("Herbert C. Brown", 1979),
    ("Georg Wittig", 1979), ("Paul Berg", 1980), ("Walter Gilbert", 1980),
    ("Kenichi Fukui", 1981), ("Roald Hoffmann", 1981), ("Aaron Klug", 1982),
    ("Henry Taube", 1983), ("Robert Bruce Merrifield", 1984),
    ("Herbert A. Hauptman", 1985), ("Jerome Karle", 1985),
    ("Dudley R. Herschbach", 1986), ("Yuan T. Lee", 1986), ("John Polanyi", 1986),
    ("Donald J. Cram", 1987), ("Jean-Marie Lehn", 1987),
    ("Charles J. Pedersen", 1987), ("Johann Deisenhofer", 1988),
    ("Robert Huber", 1988), ("Hartmut Michel", 1988),
    ("Sidney Altman", 1989), ("Thomas Cech", 1989),
    ("Elias James Corey", 1990), ("Richard R. Ernst", 1991),
    ("Rudolph A. Marcus", 1992), ("Kary Mullis", 1993), ("Michael Smith", 1993),
    ("George Andrew Olah", 1994), ("Paul J. Crutzen", 1995),
    ("Mario J. Molina", 1995), ("F. Sherwood Rowland", 1995),
    ("Robert Curl", 1996), ("Harry Kroto", 1996), ("Richard Smalley", 1996),
    ("Paul D. Boyer", 1997), ("John E. Walker", 1997),
    ("Jens Christian Skou", 1997), ("Walter Kohn", 1998), ("John Pople", 1998),
    ("Ahmed Zewail", 1999), ("Alan J. Heeger", 2000),
    ("Alan MacDiarmid", 2000), ("Hideki Shirakawa", 2000),
]

DB_ONLY = [
    ("Jacobus Henricus van 't Hoff", "1901"),
    ("Hermann Emil Fischer", "1902"),
    ("Svante Arrhenius", "1903"),
    ("William Ramsay", "1904"),
    ("Adolf von Baeyer", "1905"),
    ("Henri Moissan", "1906"),
    ("Eduard Buchner", "1907"),
    ("Ernest Rutherford", "1908"),
    ("Wilhelm Ostwald", "1909"),
    ("Otto Wallach", "1910"),
    ("Dmitri Mendeleev", "特别篇"),
]

# 主色轮转（24 色循环，同批不撞色）
PALETTE = ["#1E3A5F", "#16324F", "#0E4D64", "#123C5B", "#0F4C5C", "#14324F",
           "#283593", "#372A75", "#46356B", "#52307C", "#2A3468", "#37548D",
           "#0B5351", "#175E54", "#146B3A", "#1E5631", "#1E6B52", "#2F5D50",
           "#7A1E28", "#8A1E2D", "#A63A2B", "#9E2B25", "#7E1E23", "#5B2A86"]

track_names = list(BGM.keys())
batches = []

# 25 批 × 5 人 = 125 槽位（123 人 + 余量）
n_batch = (len(PROMPT_PEOPLE) + 4) // 5
for i in range(n_batch):
    chunk = PROMPT_PEOPLE[i * 5:(i + 1) * 5]
    people = []
    for j, (name, year) in enumerate(chunk):
        info = db_map[name]
        db = info["db"] if isinstance(info["db"], dict) else None
        track = track_names[(i * 5 + j) % len(track_names)]
        color = PALETTE[(i * 5 + j) % len(PALETTE)]
        people.append({
            "name": name,
            "dir": info["dir"],
            "year": year,
            "db_id": db["id"] if db else None,
            "db_name_en": db["name_en"] if db else None,
            "db_qid": db["qid"] if db else None,
            "db_social": db["social"] if db else 0,
            "bgm": track,
            "bgm_path": str(BGM[track]),
            "main_color": color,
        })
    batches.append({
        "batch": f"chem-batch-{i + 1:02d}",
        "mode": "prompt+db",
        "people": people,
    })

# 仅入库 2 批
for k in range(2):
    chunk = DB_ONLY[k * 5:(k + 1) * 5]
    people = []
    for name, year in chunk:
        info = db_map[name]
        db = info["db"] if isinstance(info["db"], dict) else None
        people.append({
            "name": name, "dir": info["dir"], "year": year,
            "db_id": db["id"] if db else None,
            "db_name_en": db["name_en"] if db else None,
            "db_qid": db["qid"] if db else None,
            "db_social": db["social"] if db else 0,
            "bgm": None, "bgm_path": None, "main_color": None,
        })
    batches.append({
        "batch": f"chem-batch-db-{k + 1:02d}",
        "mode": "db-only",
        "people": people,
    })

out = {"total_prompt": len(PROMPT_PEOPLE), "total_db_only": len(DB_ONLY), "batches": batches}
(ROOT / "prompt_manifest.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("批次数:", len(batches))
for b in batches:
    print(b["batch"], b["mode"], [p["name"] for p in b["people"]])
