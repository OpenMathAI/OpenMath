#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""构建 OpenPeace 21 世纪提示词/入库分批清单（2001–2025，36 位）。

产出：peace/prompt_manifest_21.json
数据源与 build_manifest.py 相同，世纪切换为 21th（pages 路径 peace/presentations/pages/21th_century/）。

用法：python3 build_manifest_21.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent
OM = ROOT.parent
sys.path.insert(0, str(OM / "peace"))
sys.path.insert(0, str(OM / "MySQL"))

from peace_list_data import DATA  # noqa: E402

LIST_MD = ROOT / "presentations" / "Nobel_Peace_Laureates_20th_21st_Century.md"

COLORS = ["#16324F", "#372A75", "#7A1E28", "#1B4D3E", "#37474F", "#8C1515",
          "#0E4D64", "#4E342E", "#0F4C5C", "#2A4B7C", "#283593", "#145C54",
          "#5C3A1E", "#14324F", "#17435B", "#1E4D3B", "#52307C", "#37548D",
          "#7E1E23", "#0B5351", "#2F4470", "#750014", "#1B4D6B", "#46356B"]

BGM_FILES = {
    "New Lands": "alex-productions/74-oK8HN0FsZmc-New-Lands.wav",
    "Timeless": "alex-productions/42-SyPUvzEkPyc-Timeless.wav",
    "PAST": "alex-productions/89-geyy8_WXDK0-PAST.wav",
    "Nostalgia": "alex-productions/86-5ETNuoDcBg4-Nostalgia.wav",
    "Awaken": "alex-productions/36-aqLUvpAdLNQ-Awaken.wav",
    "SEA": "alex-productions/92-WEqfdRXU3IU-SEA.wav",
    "Expedition": "alex-productions/33--_CEmB_dHpA-Expedition.wav",
    "The Flow of Time": "alex-productions/35-jqIDnltiDRI-The-Flow-of-Time.wav",
    "Daylight": "alex-productions/44-JoyIRE5k2Yo-Daylight.wav",
    "Savage": "alex-productions/34-pILVwyuW3jw-Savage.wav",
    "Tragedy": "alex-productions/80-K5f65-22sY4-Tragedy.wav",
    "With Me": "alex-productions/83-DXAblXgCK-k-With-Me.wav",
    "Eternals": "alex-productions/76-V5T_kW2PH_s-Eternals.wav",
    "Cinematic Experience": "alex-productions/48-QL3O8MUFAm4-Cinematic-Experience.wav",
    "Lonesome": "inspiring-electronic/16-xBLYHNv7C4Q-Lonesome - by AShamaluevMusic ｜ Sad and Emotional Cinematic Music.wav",
    "Nostalgy": "inspiring-electronic/17-_DA0mdtL-jI-Nostalgy - by AShamaluevMusic ｜ Sad Cinematic Music For Videos, Documentaries & Films.wav",
    "Through the Darkness": "inspiring-electronic/14-Trn1cSsY2t8-Audiomachine - Through the Darkness.wav",
    "Last Hope": "inspiring-electronic/24-ie5iLcdKiqk-Victor Cooper - Last Hope (Dramatic Powerful Epic Copyright Free Music).wav",
    "Empire Collapse": "inspiring-electronic/12-NTuSqFy4Stc-Cinematic Dramatic Epic Drone Orchestra Film by Cold Cinema [No Copyright Music] ⧸ Empire Collapse.wav",
    "Ascension": "inspiring-electronic/20-gYUC-sXt_8M-Cinematic Dramatic Epic Orchestra Sci-Fi Trailer by Cold Cinema [No Copyright Music] ⧸ Ascension.wav",
    "The Invisible Light": "inspiring-electronic/19-tGxXsgSKPiQ-Documentary Cinematic by Infraction [No Copyright Music] ⧸ The Invisible Light.wav",
    "Winds Of Freedom": "inspiring-electronic/25-l3Fsk4R6eys-Really Slow Motion & Giant Apes - Winds Of Freedom (Epic Heroic Orchestral).wav",
    "Falling Apart": "inspiring-electronic/03-qtNSLNUd1VE-Michael FK & Andy Leech - Falling Apart.wav",
    "Mirage": "inspiring-electronic/04-5gcb94jhG1I-Notan Nigres - Mirage (Audio).wav",
}
BGM_ORDER = list(BGM_FILES)

# 21 世纪仅（起始序号错开 20 世纪轮转，避免相邻两篇撞同款）
OFFSET = 104

DATA_MAP = {}
for y, (e, z, l) in DATA.items():
    if y <= 2000:
        continue
    for ne, nz, ctry in l:
        DATA_MAP[ne] = {"name_zh": nz, "country": ctry, "year": y}
        stripped = re.sub(r"\s*\([^)]*\)$", "", ne).strip()
        if stripped and stripped not in DATA_MAP:
            DATA_MAP[stripped] = DATA_MAP[ne]

# DATA 显示名 ≠ 维基标题 的别名（key=DATA 名 → value=wiki title）
ALIAS = {
    "Intergovernmental Panel on Climate Change": "Intergovernmental Panel on Climate Change",
}

NATIONAL_ORGS = {"Grameen Bank", "Tunisian National Dialogue Quartet",
                 "Memorial", "Centre for Civil Liberties", "Nihon Hidankyo"}


def safe_dirname(name: str) -> str:
    return re.sub(r"[^\w\-\.]+", "_", name).strip("_") or "unnamed"


def parse_list() -> list[dict]:
    rows = []
    century = None
    pat = re.compile(r"^\|\s*(\d{4})\s*\|\s*\[([^\]]+)\]\((https://en\.wikipedia\.org/wiki/[^\s]+?)\)\s*\|\s*([^|]+)\|")
    for line in LIST_MD.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s.startswith("## 20 世纪"):
            century = "20th"
            continue
        if s.startswith("## 21 世纪"):
            century = "21st"
            continue
        if century != "21st":
            continue
        m = pat.match(s)
        if not m:
            continue
        rows.append({
            "year": int(m.group(1)), "name": m.group(2).strip(),
            "title": unquote(m.group(3).rstrip("/").split("/wiki/")[-1]).replace("_", " "),
        })
    return rows


def db_lookup(cur, name: str) -> dict:
    cur.execute("SELECT id,name_en,qid,has_social_data FROM people WHERE name_en=%s", (name,))
    r = cur.fetchone()
    if not r and "'" not in name:
        token = name.split()[0] if len(name.split()) > 1 else name
        if len(token) >= 5:
            cur.execute(
                "SELECT id,name_en,qid,has_social_data FROM people WHERE name_en LIKE %s",
                (f"%{token}%",))
            low = name.lower()
            for pid, en, qid, soc in cur.fetchall():
                if en.lower() == low:
                    r = (pid, en, qid, soc)
                    break
    if r:
        return {"db_id": r[0], "db_name_en": r[1], "db_qid": r[2], "db_social": r[3]}
    return {"db_id": None, "db_name_en": None, "db_qid": None, "db_social": 0}


def main() -> int:
    rows = parse_list()
    print("21st rows:", len(rows))
    seen: dict[str, dict] = {}
    for r in rows:
        t = r["title"]
        if t in seen:
            seen[t]["years"].append(r["year"])
            continue
        dm = DATA_MAP.get(r["name"])
        assert dm, f"DATA 中找不到 {r['name']!r}（title={t}）"
        seen[t] = {"name": r["name"], "years": [r["year"]],
                   "name_zh": dm["name_zh"], "country": dm["country"], "first_year": r["year"]}

    from db_mysql import get_conn
    conn = get_conn()
    cur = conn.cursor()

    people = []
    for i, (title, info) in enumerate(sorted(seen.items(), key=lambda kv: kv[1]["first_year"])):
        pdir = ROOT / "presentations" / "pages" / "21th_century" / safe_dirname(title)
        meta = pdir / "metadata.json"
        qid = None
        if meta.exists():
            qid = json.loads(meta.read_text(encoding="utf-8")).get("qid")
        db = db_lookup(cur, info["name"])
        color = COLORS[(i + OFFSET) % len(COLORS)]
        bgm = BGM_ORDER[(i + OFFSET) % len(BGM_ORDER)]
        is_org = info["country"] == "International organization" or info["name"] in NATIONAL_ORGS
        people.append({
            "name": info["name"],
            "dir": safe_dirname(title),
            "wiki_title": title,
            "year": info["first_year"],
            "years": info["years"],
            "name_zh": info["name_zh"],
            "country": info["country"],
            "qid": qid,
            "is_org": is_org,
            "page_md": str(pdir / "page.md"),
            "prompt_md": f"peace/presentations/21th_century/{safe_dirname(title)}/{safe_dirname(title)}_zh.md",
            "yaml": f"MySQL/data/{safe_dirname(title)}.yaml",
            "main_color": color,
            "bgm": bgm,
            "bgm_path": f"/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/{BGM_FILES[bgm]}",
            **db,
            "need_prompt": True,
            "need_relations": db["db_social"] == 0,
        })

    batches = []
    size = 5
    for bi in range(0, len(people), size):
        batches.append({
            "batch": f"peace21-batch-{bi // size + 1:02d}",
            "mode": "prompt+db",
            "people": people[bi:bi + size],
        })

    out = {
        "total": len(people),
        "individuals": sum(1 for p in people if not p["is_org"]),
        "orgs": sum(1 for p in people if p["is_org"]),
        "batches": batches,
        "people": people,
    }
    (ROOT / "prompt_manifest_21.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print("people:", len(people), " batches:", len(batches))
    print("orgs:", out["orgs"], " individuals:", out["individuals"])
    print("db existing:", sum(1 for p in people if p["db_id"]))
    for p in people:
        if p["db_id"]:
            print("  reuse:", p["name"], "->", p["db_id"], p["db_name_en"], "social=", p["db_social"])
    no_qid = [p["name"] for p in people if not p["qid"]]
    print("no qid:", no_qid)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
