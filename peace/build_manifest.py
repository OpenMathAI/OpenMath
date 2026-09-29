#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""构建 OpenPeace 提示词/入库分批清单。

产出：
  peace/prompt_manifest.json   （people 全量 104 条 + batches 21 批）
  数据源：presentations/Nobel_Peace_Laureates_20th_21st_Century.md（wiki title）
          + peace_list_data.py（中文名/国籍）+ pages/*/metadata.json（qid）
          + greatminds 库预查（db_id/db_name_en/db_social）

用法：python3 build_manifest.py
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

# 主色轮转（24 色，批内不重复；取自历批沉淀）
COLORS = ["#16324F", "#372A75", "#7A1E28", "#1B4D3E", "#37474F", "#8C1515",
          "#0E4D64", "#4E342E", "#0F4C5C", "#2A4B7C", "#283593", "#145C54",
          "#5C3A1E", "#14324F", "#17435B", "#1E4D3B", "#52307C", "#37548D",
          "#7E1E23", "#0B5351", "#2F4470", "#750014", "#1B4D6B", "#46356B"]

# BGM 轮转（24 曲 + 本地路径，取自 music_audio/curated_tracks.md）
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

# DATA 姓名 → 中文名/国籍
DATA_MAP = {}
for y, (e, z, l) in DATA.items():
    if y > 2000:
        continue
    for ne, nz, ctry in l:
        DATA_MAP[ne] = {"name_zh": nz, "country": ctry, "year": y}
        # 兼容清单 md 里去掉尾括号注记的形式（如 UNICEF 行姓名列无 "(UNICEF)"）
        stripped = re.sub(r"\s*\([^)]*\)$", "", ne).strip()
        if stripped and stripped not in DATA_MAP:
            DATA_MAP[stripped] = DATA_MAP[ne]

# 人工对齐：DATA 显示名 ≠ 维基标题/页面 frontmatter name 的条目
ALIAS = {
    "Institute of International Law": "Institute of International Law",
    "Permanent International Peace Bureau": "International Peace Bureau",
    "International Committee of the Red Cross": "International Committee of the Red Cross",
    "Nansen International Office for Refugees": "Nansen International Office for Refugees",
    "Office of the United Nations High Commissioner for Refugees": "United Nations High Commissioner for Refugees",
    "League of Red Cross Societies": "International Federation of Red Cross and Red Crescent Societies",
    "United Nations Children's Fund (UNICEF)": "UNICEF",
    "International Labour Organization": "International Labour Organization",
    "International Physicians for the Prevention of Nuclear War": "International Physicians for the Prevention of Nuclear War",
    "United Nations Peace-Keeping Forces": "Peacekeeping",
    "Pugwash Conferences on Science and World Affairs": "Pugwash Conferences on Science and World Affairs",
    "International Campaign to Ban Landmines": "International Campaign to Ban Landmines",
    "Médecins Sans Frontières": "Médecins Sans Frontières",
    "The Viscount Cecil of Chelwood": "Robert Cecil, 1st Viscount Cecil of Chelwood",
    "Sir Austen Chamberlain": "Austen Chamberlain",
    "Sir Norman Angell": "Norman Angell",
    "Lord Boyd-Orr": "John Boyd Orr",
    "George Catlett Marshall Jr.": "George Marshall",
    "Tenzin Gyatso, 14th Dalai Lama": "Dalai Lama",
    "Lê Đức Thọ": "Lê Đức Thọ",
    "Kim Dae-jung": "Kim Dae-jung",
}


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
        if century != "20th":
            continue
        m = pat.match(s)
        if not m:
            continue
        year = int(m.group(1))
        name = m.group(2).strip()
        href = m.group(3).strip()
        title = unquote(href.rstrip("/").split("/wiki/")[-1]).replace("_", " ")
        rows.append({"year": year, "name": name, "title": title})
    return rows


def db_lookup(cur, name: str) -> dict:
    """先精确，再 LIKE token。返回 db_id/db_name_en/db_qid/db_social。"""
    cur.execute("SELECT id,name_en,qid,has_social_data FROM people WHERE name_en=%s", (name,))
    r = cur.fetchone()
    if not r and "'" not in name:
        token = name.split()[0] if len(name.split()) > 1 else name
        if len(token) >= 5:
            cur.execute(
                "SELECT id,name_en,qid,has_social_data FROM people WHERE name_en LIKE %s",
                (f"%{token}%",))
            cand = cur.fetchall()
            low = name.lower()
            for pid, en, qid, soc in cand:
                if en.lower() == low:
                    r = (pid, en, qid, soc)
                    break
    if r:
        return {"db_id": r[0], "db_name_en": r[1], "db_qid": r[2], "db_social": r[3]}
    return {"db_id": None, "db_name_en": None, "db_qid": None, "db_social": 0}


def main() -> int:
    rows = parse_list()
    seen: dict[str, dict] = {}
    for r in rows:
        t = r["title"]
        if t in seen:
            seen[t]["years"].append(r["year"])
            continue
        dm = DATA_MAP.get(r["name"])
        if dm is None:
            # 尝试别名表反查
            dm = None
            for k, v in ALIAS.items():
                if v == r["name"] or k == r["name"]:
                    dm = DATA_MAP.get(k)
                    if dm:
                        break
        assert dm, f"DATA 中找不到 {r['name']!r}（title={t}）"
        seen[t] = {
            "name": r["name"], "title": t, "years": [r["year"]],
            "name_zh": dm["name_zh"], "country": dm["country"], "first_year": r["year"],
        }

    from db_mysql import get_conn
    conn = get_conn()
    cur = conn.cursor()

    people = []
    for i, (title, info) in enumerate(sorted(seen.items(), key=lambda kv: kv[1]["first_year"])):
        pdir = ROOT / "presentations" / "pages" / "20th_century" / safe_dirname(title)
        meta = pdir / "metadata.json"
        qid = None
        if meta.exists():
            qid = json.loads(meta.read_text(encoding="utf-8")).get("qid")
        db = db_lookup(cur, info["name"])
        color = COLORS[i % len(COLORS)]
        bgm = BGM_ORDER[i % len(BGM_ORDER)]
        people.append({
            "name": info["name"],
            "dir": safe_dirname(title),
            "wiki_title": title,
            "year": info["first_year"],
            "years": info["years"],
            "name_zh": info["name_zh"],
            "country": info["country"],
            "qid": qid,
            "is_org": info["country"] == "International organization" or info["name"] in {
                "Institute of International Law", "Friends Service Council",
                "American Friends Service Committee", "Amnesty International",
                "Grameen Bank", "Memorial", "Centre for Civil Liberties", "Nihon Hidankyo"},
            "page_md": str(pdir / "page.md"),
            "prompt_md": f"peace/presentations/20th_century/{safe_dirname(title)}/{safe_dirname(title)}_zh.md",
            "yaml": f"MySQL/data/{safe_dirname(title)}.yaml",
            "main_color": color,
            "bgm": bgm,
            "bgm_path": f"/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/{BGM_FILES[bgm]}",
            **db,
            "need_prompt": True,
            "need_relations": db["db_social"] == 0,
        })

    # 分批：5 人/批
    batches = []
    size = 5
    for bi in range(0, len(people), size):
        batches.append({
            "batch": f"peace-batch-{bi // size + 1:02d}",
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
    (ROOT / "prompt_manifest.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print("people:", len(people), " batches:", len(batches))
    print("orgs:", out["orgs"], " individuals:", out["individuals"])
    print("db existing:", sum(1 for p in people if p["db_id"]))
    no_qid = [p["name"] for p in people if not p["qid"]]
    print("no qid:", no_qid)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
