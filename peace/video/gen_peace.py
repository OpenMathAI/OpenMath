#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Nobel Peace allinone video deck (peace_allinone_zh.tex).

完全复用 physicist/video/gen_physicist.py → turing/video/episode-allinone 的
Beamer 模板（personslide + 封面头像网格 + 双料与大满贯汇总页）。

数据来源：
  - peace/presentations/{20th,21th}_century/OpenPeace_*_Nobel_Laureates.md（年份/姓名/国籍/获奖理由，理由已是中文）
  - peace/presentations/pages/{20th,21th}_century/<Dir>/metadata.json（生卒/机构/QID）
  - 同目录 images.txt（封面与人像页头像，curl 下载，过滤旗帜/签名/图标）
交叉荣誉：greatminds.award_laureate 数据库直查（排除和平奖本身）。

Run: cd peace/video && python3 gen_peace.py
"""
import io
import sys
import json
import os
import re
import shutil
import subprocess
import unicodedata
from concurrent.futures import ThreadPoolExecutor

VID = os.path.dirname(os.path.abspath(__file__))
PRES = os.path.normpath(os.path.join(VID, "..", "presentations"))
EP = os.path.join(VID, "episode-allinone")
IMGDIR = os.path.join(EP, "images")
MAIN = "peace_allinone_zh"

LISTS = [
    (os.path.join(PRES, "20th_century", "OpenPeace_20th_Century_Nobel_Laureates.md"),
     os.path.join(PRES, "pages", "20th_century"), "20th"),
    (os.path.join(PRES, "21th_century", "OpenPeace_21st_Century_Nobel_Laureates.md"),
     os.path.join(PRES, "pages", "21th_century"), "21st"),
]

# 名录名称 ↔ 维基条目名不一致时的显式别名（match_page 用）
ALIAS_PAGE = {
    "Mairead Corrigan": "Mairead Maguire",
    "Friends Service Council": "Quaker Peace and Social Witness",
    "United Nations Peace-Keeping Forces": "United Nations peacekeeping",
    "United Nations Children's Fund (UNICEF)": "UNICEF",
    "Institute of International Law": "Institut de Droit International",
    "Nansen International Office for Refugees": "Office international Nansen pour les réfugiés",
}

COUNTRY_ZH = {
    "United States": "美国", "United Kingdom": "英国", "Germany": "德国", "France": "法国",
    "Switzerland": "瑞士", "Netherlands": "荷兰", "Sweden": "瑞典", "Italy": "意大利",
    "Denmark": "丹麦", "Austria-Hungary": "奥匈帝国", "Austria": "奥地利", "Japan": "日本",
    "Belgium": "比利时", "Norway": "挪威", "Finland": "芬兰", "Poland": "波兰",
    "Argentina": "阿根廷", "Mexico": "墨西哥", "Israel": "以色列", "Ireland": "爱尔兰",
    "Canada": "加拿大", "Russia": "俄罗斯", "Soviet Union": "苏联", "India": "印度",
    "Pakistan": "巴基斯坦", "China": "中国", "Bangladesh": "孟加拉国", "Belarus": "白俄罗斯",
    "Colombia": "哥伦比亚", "Costa Rica": "哥斯达黎加", "Democratic Republic of the Congo": "刚果（金）",
    "East Timor": "东帝汶", "Egypt": "埃及", "Ethiopia": "埃塞俄比亚", "Ghana": "加纳",
    "Guatemala": "危地马拉", "International organization": "国际组织", "Iran": "伊朗",
    "Iraq": "伊拉克", "Kenya": "肯尼亚", "Liberia": "利比里亚", "Myanmar": "缅甸",
    "North Vietnam": "北越", "Palestine": "巴勒斯坦", "Philippines": "菲律宾",
    "South Africa": "南非", "South Korea": "韩国", "Tunisia": "突尼斯", "Ukraine": "乌克兰",
    "Venezuela": "委内瑞拉", "West Germany": "西德", "Yemen": "也门", "Albania": "阿尔巴尼亚",
    "West Germany East Germany": "西德/东德", "Germany West Germany": "德国/西德",
}


def ascii_fold(s):
    s = unicodedata.normalize("NFKD", str(s))
    return "".join(c for c in s if not unicodedata.combining(c))


def norm(s):
    return re.sub(r"[^a-z0-9]", "", ascii_fold(s).lower())


def tokens(s):
    return [t.lower() for t in re.split(r"[^A-Za-z]+", ascii_fold(s)) if len(t) > 1]


def stems(s):
    return set(t[:5] for t in tokens(s))


def esc(s):
    s = str(s).replace("\\", "\\textbackslash{}")
    for ch, rep in (("&", "\\&"), ("%", "\\%"), ("#", "\\#"), ("_", "\\_"),
                    ("{", "\\{"), ("}", "\\}"), ("~", "\\textasciitilde{}"),
                    ("^", "\\textasciicircum{}")):
        s = s.replace(ch, rep)
    return s


def country_zh(c):
    c = c.strip()
    if c in COUNTRY_ZH:
        return COUNTRY_ZH[c]
    parts = re.split(r"\s{2,}|\s*/\s*", c)
    out = [COUNTRY_ZH.get(p, p) for p in parts if p]
    return "/".join(out) if out else c


# ---------------- 数据解析 ----------------

def parse_lists():
    people = []
    for path, _root, cent in LISTS:
        with open(path, encoding="utf-8") as f:
            for line in f:
                if not re.match(r"^\|\s*(?:19|20)\d{2}\s*\|", line):
                    continue
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if len(cells) < 4:
                    continue
                year = int(cells[0])
                raw = cells[1]
                i = raw.rfind("(")
                if i > 0 and raw.endswith(")"):
                    name, zh = raw[:i].strip(), raw[i + 1:-1].strip()
                else:
                    name, zh = raw, ""
                people.append(dict(year=year, name=name, zh=zh, country=cells[2],
                                   citation=cells[3], century=cent,
                                   source_index=len(people)))
    people.sort(key=lambda p: (p["year"], p["source_index"]))
    return people


def load_page_index():
    pages = []
    for _path, root, cent in LISTS:
        if not os.path.isdir(root):
            continue
        for d in sorted(os.listdir(root)):
            mp = os.path.join(root, d, "metadata.json")
            if not os.path.isfile(mp):
                continue
            try:
                meta = json.load(open(mp, encoding="utf-8"))
            except Exception:
                meta = {}
            props = meta.get("properties", {}) or {}
            pages.append(dict(dir=os.path.join(root, d), dname=d, century=cent,
                              name=meta.get("name") or d.replace("_", " "),
                              title=meta.get("title") or meta.get("name") or d.replace("_", " "),
                              year=meta.get("year"),
                              dob=(props.get("date_of_birth") or [""])[0],
                              dod=(props.get("date_of_death") or [""])[0],
                              employer=props.get("employer") or []))
    return pages


def match_page(p, pages):
    alias = ALIAS_PAGE.get(p["name"], "")
    pt = set(tokens(p["name"])) | set(tokens(alias))
    pst = stems(p["name"]) | stems(alias)
    pns = {norm(p["name"])}
    if alias:
        pns.add(norm(alias))
    best, best_s = None, -1.0
    for pg in pages:
        gt = set(tokens(pg["name"])) | set(tokens(pg["dname"].replace("_", " ")))
        gst = stems(pg["name"])
        gn = norm(pg["name"])
        if gn and gn in pns:
            s = 100.0
        elif pst and pst == gst:
            s = 60.0
        elif pt and pt <= gt:
            s = 40.0
        else:
            inter = pst & gst if pst and gst else set()
            if not inter:
                continue
            s = 30.0 * len(inter) / max(len(pst | gst), 1)
            if s < 12.0:
                continue
        if pg["year"] == p["year"]:
            s += 15.0
        elif pg["century"] == p["century"]:
            s += 5.0
        if s > best_s:
            best, best_s = pg, s
    return best if best_s >= 20.0 else None


# ---------- 数据库直查顶级交叉奖项（greatminds.award_laureate） ----------
TOP_AWARDS = {
    23: ("\\nobelchembadge", "诺贝尔化学奖"),
    24: ("\\nobelmedbadge", "诺贝尔生理学或医学奖"),
    25: ("\\nobellitbadge", "诺贝尔文学奖"),
    26: ("\\nobeleconbadge", "诺贝尔经济学奖"),
    857: ("\\nobelpeacebadge", "诺贝尔和平奖"),
    14: ("\\turingbadge", "图灵奖"),
    1: ("\\fieldsbadge", "菲尔兹奖"),
    2: ("\\abelbadge", "阿贝尔奖"),
    3: ("\\wolfmathbadge", "沃尔夫数学奖"),
    243: ("\\wolfbadge", "沃尔夫物理学奖"),
    27: ("\\kyotobadge", "京都奖"),
    28: ("\\shawbadge", "邵逸夫奖"),
    29: ("\\btmathbadge", "数学突破奖"),
    557: ("\\btphysbadge", "基础物理学突破奖"),
    806: ("\\btphysbadge", "特别基础物理学突破奖"),
    674: ("\\btphysbadge", "突破奖"),
    30: ("\\crafoordbadge", "克拉福德奖"),
    15: ("\\millenniumbadge", "千禧科技奖"),
    41: ("\\japanbadge", "日本国际奖"),
    18: ("\\statsbadge", "国际统计学奖"),
    17: ("\\copssbadge", "考普斯会长奖"),
}
SELF_AWARD = 857  # 和平奖本身，本片不作为交叉

# 库外静态交叉（对齐 medal_list_allinone/all_cross_reference.md 第六节）：
# Pauling 化学奖 1954 载于 OpenChemist 侧（award_laureate 尚未全量入库）
STATIC_CROSS = [
    ("Linus Pauling", ("\\nobelchembadge", "诺贝尔化学奖", "1954")),
]


def merge_static_cross(people):
    for p in people:
        items = p.get("cross_items") or []
        for n, item in STATIC_CROSS:
            if stems(p["name"]) == stems(n) or stems(p["name"]) <= stems(n):
                if not any(it[1] == item[1] for it in items):
                    items = sorted(items + [item], key=lambda t: t[2] or "9999")
        p["cross_items"] = items


def build_db_cross(people):
    """库内直查每人顶级交叉奖项；数据库不可用时直接失败。"""
    try:
        sys.path.insert(0, os.path.normpath(os.path.join(VID, "..", "..", "MySQL")))
        from db_mysql import get_conn
        conn = get_conn()
    except Exception as e:
        raise RuntimeError("数据库不可用，拒绝生成不完整的交叉奖项：%s" % e) from e
    qid_by = {}
    for p in people:
        pg = p.get("page")
        if not pg:
            continue
        try:
            qid_by[(p["year"], p["name"])] = (json.load(open(pg["dir"] + "/metadata.json", encoding="utf-8")).get("qid") or "").strip()
        except Exception:
            pass
    cur = conn.cursor()
    cur.execute("SELECT id,qid FROM people")
    pid_by = {r[1]: r[0] for r in cur.fetchall() if r[1]}
    missing_qids = [p["name"] for p in people
                    if not qid_by.get((p["year"], p["name"]))]
    if missing_qids:
        conn.close()
        raise RuntimeError("以下人物缺少 metadata QID，拒绝生成交叉奖项：%s" % ", ".join(missing_qids[:10]))
    missing_people = [p["name"] for p in people
                      if qid_by[(p["year"], p["name"])] not in pid_by]
    if missing_people:
        conn.close()
        raise RuntimeError("以下人物未在 greatminds.people 匹配，拒绝生成交叉奖项：%s" % ", ".join(missing_people[:10]))
    ids = ",".join(str(i) for i in TOP_AWARDS if i != SELF_AWARD)
    n_cross = 0
    for p in people:
        qid = qid_by.get((p["year"], p["name"]))
        rec = pid_by.get(qid) if qid else None
        items = []
        if rec:
            cur.execute("SELECT award_id,year FROM award_laureate WHERE person_id=%s AND award_id IN (%s)" % (rec, ids))
            for aid, yr in cur.fetchall():
                badge, label = TOP_AWARDS[aid]
                items.append((badge, label, str(yr) if yr else ""))
        items.sort(key=lambda t: t[2] or "9999")
        p["cross_items"] = items
        if items:
            n_cross += 1
    conn.close()
    print("DB cross awards: %d people with top-tier crosses" % n_cross)
    return True


def cross_tex(p):
    items = p.get("cross_items") or []
    if not items:
        p["badges_str"] = ""
        return ""
    p["badges_str"] = "\\," + "".join(b + "{}" for b, _, _ in items)
    return " \\enspace ".join("%s{} %s%s" % (b, lab, (" " + y) if y else "") for b, lab, y in items)


# ---------------- 肖像下载 ----------------
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
BAD_FILE = re.compile(r"flag|signature|question_book|map[_\-\. ]|icon|logo|seal|\.svg|\.gif|\.ogg|wiki", re.I)


def curl(url, tries=3):
    import time
    for k in range(tries):
        try:
            r = subprocess.run(["curl", "-sLf", "--max-time", "40", "-A", UA, url],
                               capture_output=True)
            if r.returncode == 0 and r.stdout:
                return r.stdout
        except Exception:
            pass
        time.sleep(1.0 + k)
    return None


def fetch_img(url):
    """下载图片；upload.wikimedia.org 429 限流时走 wsrv.nl 代理兜底。"""
    import time
    data = curl(url, tries=2)
    if data and data[:6] != b"<html " and data[:9] != b"<!DOCTYPE":
        return data
    time.sleep(1.0)
    proxy = "https://wsrv.nl/?url=" + re.sub(r"^https?://", "", url).split("?")[0] + "&w=700"
    data = curl(proxy, tries=2)
    if data and data[:6] != b"<html " and data[:9] != b"<!DOCTYPE":
        return data
    return None


def rest_summary_image(title):
    """Wikipedia REST summary 的 infobox 图（同人像最可靠）。"""
    import urllib.parse
    t = urllib.parse.quote(title.replace(" ", "_"), safe="")
    url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + t
    r = subprocess.run(["curl", "-sLf", "--max-time", "30", "-A", UA, url], capture_output=True)
    if r.returncode != 0 or not r.stdout:
        return None
    try:
        j = json.loads(r.stdout)
    except Exception:
        return None
    if j.get("type") not in ("standard", "disambiguation"):
        return None
    th = (j.get("thumbnail") or {}).get("source") or ""
    oi = (j.get("originalimage") or {}).get("source") or ""
    if th:
        return re.sub(r"/\d{2,4}px-", "/500px-", th)
    return oi or None


def img_probe(data, min_size=8000):
    """Return (ok, ext, ratio) or (False, '', 0)."""
    if not data or len(data) < min_size:
        return False, "", 0
    if data[:2] == b"\xff\xd8":
        ext = "jpg"
    elif data[:8] == b"\x89PNG\r\n\x1a\n":
        ext = "png"
    else:
        return False, "", 0
    try:
        from PIL import Image
        im = Image.open(io.BytesIO(data))
        return True, ext, im.width / max(im.height, 1)
    except Exception:
        return True, ext, 0.8


def candidate_urls(page):
    urls = []
    fp = os.path.join(page["dir"], "images.txt")
    if not os.path.isfile(fp):
        return urls
    for line in open(fp, encoding="utf-8"):
        u = line.strip()
        if not u.startswith("http"):
            continue
        fname = u.split("/")[-1].split("?")[0]
        if BAD_FILE.search(fname):
            continue
        m = re.search(r"/(\d{2,4})px-", u)
        w = int(m.group(1)) if m else 500
        urls.append((fname, w, re.sub(r"/\d{2,4}px-", "/500px-", u)))
    return urls


def save_image(data, dst_base, tier1, max_ratio, min_size=8000):
    if not data or len(data) < min_size:
        return None
    # GIF（如 Commons 老照片动图）转 JPEG 再存
    if data[:3] == b"GIF":
        try:
            from PIL import Image
            im = Image.open(io.BytesIO(data))
            fmt = "JPEG"
            if im.mode in ("P", "RGBA", "LA"):
                im = im.convert("RGB")
            elif im.mode != "RGB":
                im = im.convert("RGB")
            fn = "%s.jpg" % dst_base
            im.save(os.path.join(IMGDIR, fn), fmt, quality=95)
            return fn
        except Exception:
            return None
    ok, ext, ratio = img_probe(data, min_size)
    if not ok:
        return None
    if not tier1 and not (0.45 <= ratio <= 1.25):
        return None
    if ratio > max_ratio:
        return None
    fn = "%s.%s" % (dst_base, ext)
    with open(os.path.join(IMGDIR, fn), "wb") as f:
        f.write(data)
    return fn


def fetch_portrait(p, page, dst_base):
    """Return saved filename (in images/) or None. REST infobox 优先。"""
    import time
    time.sleep(0.3)
    su = rest_summary_image(page["title"])
    data = fetch_img(su) if su else None
    if data:
        fn = save_image(data, dst_base, tier1=True, max_ratio=2.5, min_size=1200)
        if fn:
            return fn
    pt = set(tokens(p["name"]))
    surname = tokens(p["name"])[-1] if tokens(p["name"]) else ""
    scored = []
    for fname, w, u in candidate_urls(page):
        ft = set(tokens(fname))
        overlap = pt & ft
        tier1 = bool(overlap) or (surname and surname in fname.lower())
        score = (20 if tier1 else 0) + 8 * len(overlap) + w / 500.0
        scored.append((score, tier1, u))
    scored.sort(reverse=True)
    tried = 0
    for score, tier1, u in scored:
        if tried >= 4:
            break
        tried += 1
        data = fetch_img(u)
        if not data:
            continue
        fn = save_image(data, dst_base, tier1=tier1, max_ratio=2.5 if tier1 else 999)
        if fn:
            return fn
    return None


def slug_of(name):
    s = re.sub(r"[^a-z]", "", ascii_fold(name).lower())
    return s


# 人工目检判定为非人像的自动抓取结果：禁用自动抓取，等待人工补图（figures/ 仍优先）
BLOCK_IMAGES = {}


def sync_all(people, pages):
    os.makedirs(IMGDIR, exist_ok=True)

    force = bool(os.environ.get("FORCE_IMG"))
    if force:
        for f in os.listdir(IMGDIR):
            if not f.startswith("."):
                os.remove(os.path.join(IMGDIR, f))

    def work(p):
        if p["name"] in BLOCK_IMAGES and not find_figure(p["name"]):
            if os.environ.get("FORCE_IMG"):
                for ext in ("jpg", "jpeg", "png", "webp"):
                    fp = os.path.join(IMGDIR, p["slug"] + "." + ext)
                    if os.path.exists(fp):
                        os.remove(fp)
            return "blocked"
        pg = p.get("page")
        dst = os.path.join(IMGDIR, p["slug"] + ".jpg")
        if os.path.exists(dst) and os.path.getsize(dst) > 0:
            return "keep"
        fig = find_figure(p["name"])
        if fig:
            if fig.lower().endswith(".webp"):
                try:
                    from PIL import Image
                    Image.open(fig).convert("RGB").save(dst, "JPEG", quality=95)
                    return "fig"
                except Exception:
                    pass
            shutil.copy(fig, dst)
            return "fig"
        for ext in ("png", "jpeg", "webp"):
            alt = os.path.join(IMGDIR, p["slug"] + "." + ext)
            if os.path.exists(alt) and os.path.getsize(alt) > 0:
                return "keep-alt"
        if not pg:
            return "no-page"
        fn = fetch_portrait(p, pg, p["slug"])
        return "ok" if fn else "missing"

    with ThreadPoolExecutor(max_workers=3) as ex:
        results = list(ex.map(work, people))
    for p, r in zip(people, results):
        p["img_status"] = r
        p["img_file"] = None
        for ext in ("jpg", "jpeg", "png", "webp"):
            cand = os.path.join(IMGDIR, p["slug"] + "." + ext)
            if os.path.exists(cand) and os.path.getsize(cand) > 0:
                p["img_file"] = p["slug"] + "." + ext
                break
    return sum(1 for p in people if p["img_file"])


FIGURES_DIR = os.path.join(EP, "figures")


def fig_key(fname):
    s = os.path.splitext(fname)[0].replace("_", " ")
    return norm(s)


def find_figure(name):
    if not os.path.isdir(FIGURES_DIR):
        return None
    key = norm(name)
    for f in os.listdir(FIGURES_DIR):
        if f.startswith("."):
            continue
        if fig_key(f) == key:
            return os.path.join(FIGURES_DIR, f)
    return None


def initials(name):
    parts = [p for p in ascii_fold(name).replace("-", " ").split() if p]
    if len(parts) >= 2:
        return "%s.%s." % (parts[0][0], parts[-1][0])
    return parts[0][:2].upper() + "."


# ---------------- 元数据组装 ----------------

def life_str(p):
    pg = p.get("page") or {}
    dob = (pg or {}).get("dob", "") or ""
    dod = (pg or {}).get("dod", "") or ""
    y1 = dob[:4] if re.match(r"^\d{4}", dob) else ""
    y2 = dod[:4] if re.match(r"^\d{4}", dod) else ""
    if y1 and y2:
        try:
            age = int(y2) - int(y1)
            note = "（享年%d岁）" % age if 0 < age < 120 else ""
        except Exception:
            note = ""
        return "%s–%s%s" % (y1, y2, note)
    if y1:
        return y1 + "–"
    return "—"


def inst_str(p):
    emp = (p.get("page") or {}).get("employer") or []
    unique = list(dict.fromkeys(e.strip() for e in emp if e and e.strip()))
    return " · ".join(unique[:2]) if unique else "—"


def age_str(p):
    pg = p.get("page") or {}
    y1 = (pg.get("dob") or "")[:4]
    if re.match(r"^\d{4}$", y1):
        return "约%d岁" % (p["year"] - int(y1))
    return ""


# ---------------- tex 生成 ----------------
HEADER = r"""% Nobel Peace Video — Allinone
% 诺贝尔和平奖全得主合集（1901–2025）
% Beamer layout mirrors physicist/video/episode-allinone（源自 turing allinone）
% Source: peace/presentations 名录 + 离线页面 metadata.json + Wikipedia images
\documentclass[aspectratio=169,14pt]{beamer}
\usetheme{default}\usecolortheme{default}
\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{footline}{\hfill{\scriptsize\color{covermuted}\insertframenumber/\inserttotalframenumber}\hspace{0.4cm}\vspace{0.15cm}}
\usepackage{fontspec}\usepackage{xeCJK}
\setCJKmainfont{PingFang SC}[BoldFont=PingFang SC Semibold]
\xeCJKDeclareCharClass{CJK}{"0370 -> "03FF}
% 越南文等扩展拉丁字母走主字体（Helvetica Neue），避免缺字被静默丢弃
\setmainfont{Helvetica Neue}[BoldFont=Helvetica Neue Bold]
\usepackage{xcolor}\usepackage{tikz}\usepackage{graphicx}\usepackage{adjustbox}\usepackage{fontawesome5}\usepackage{ifthen}\usepackage{amssymb}
\usetikzlibrary{positioning,calc,arrows.meta,shadows}

% ===== 配色：和平绿 + 红十字红 + 颁奖金（区别于物理深空蓝/图灵紫）=====
\definecolor{bgmain}{RGB}{246,249,246}
\definecolor{coverprimary}{HTML}{2D6A4F}
\definecolor{coveraccent}{HTML}{B03A2E}
\definecolor{coveramber}{HTML}{C9922A}
\definecolor{coverpurple}{HTML}{1F6E6E}
\definecolor{coverdark}{HTML}{14251C}
\definecolor{covermuted}{HTML}{5F6B64}
\definecolor{coverlight}{HTML}{E7F1EA}
\definecolor{DeepPurpleAccent}{HTML}{4A148C}
\definecolor{titlecolor}{RGB}{20,37,28}
\definecolor{muteddark}{RGB}{88,100,92}
\definecolor{bluepanel}{RGB}{224,238,229}
\definecolor{redpanel}{RGB}{247,227,224}
\definecolor{goldpanel}{RGB}{247,239,219}
\definecolor{purplepanel}{RGB}{221,235,235}
\definecolor{graypanel}{RGB}{238,240,238}
\setbeamercolor{background canvas}{bg=bgmain}

\providecommand{\personhonors}{}
\newcounter{pmark}%
% ---- 交叉身份汇总页：居中标题模板（源自 turing allinone）----
\def\framesubject{}
\setbeamertemplate{frametitle}{%
  \vspace{8pt}%
  \centering
  {\fontsize{13}{15}\selectfont\bfseries\color{coverprimary}\insertframetitle}\par\vspace{3pt}
  {\footnotesize\color{mutedgray}\framesubject}\par\vspace{4pt}
  \textcolor{coverlight}{\rule{0.95\textwidth}{0.6pt}}%
  \vspace{-6pt}%
}
\definecolor{mutedgray}{RGB}{120,120,120}
\colorlet{chemclr}{coverpurple!80}
\colorlet{medclr}{coveraccent!80}
\colorlet{litclr}{coverprimary!75}
\colorlet{econclr}{covermuted}
\colorlet{physclr}{coveramber!75}
\colorlet{turingclr2}{coverprimary!80}
\colorlet{wolfclr}{coveramber}
\colorlet{btclr}{coverpurple}
\colorlet{shawclr}{coveramber}
\colorlet{crafoordclr}{coveraccent}
\colorlet{japanclr}{coveraccent!75}
\colorlet{millclr}{covermuted}
\colorlet{fieldsclr}{coveramber}
\colorlet{abelclr}{coveraccent}
\colorlet{wolfmathclr}{coveramber}
\colorlet{kyotoclr}{coverprimary}
\colorlet{statsclr}{coverpurple}
\colorlet{copssclr}{covermuted}

% 交叉奖项徽标（数据库直查顶级奖项）
\newcommand{\nobelchembadge}{\raisebox{0.55ex}{\tiny\color{coveramber}$\clubsuit$\kern-0.5pt C}}
\newcommand{\nobelmedbadge}{\raisebox{0.55ex}{\tiny\color{coveraccent}$\clubsuit$\kern-0.5pt M}}
\newcommand{\nobellitbadge}{\raisebox{0.55ex}{\tiny\color{coverpurple}$\clubsuit$\kern-0.5pt L}}
\newcommand{\nobeleconbadge}{\raisebox{0.55ex}{\tiny\color{coverprimary}$\clubsuit$\kern-0.5pt E}}
\newcommand{\nobelpeacebadge}{\raisebox{0.55ex}{\tiny\color{coveramber}$\clubsuit$\kern-0.5pt P}}
\newcommand{\turingbadge}{\raisebox{0.55ex}{\tiny\color{coverpurple}$\blacktriangle$\kern-0.5pt T}}
\newcommand{\fieldsbadge}{\raisebox{0.55ex}{\tiny\color{coveramber}$\bigstar$\kern-0.5pt F}}
\newcommand{\abelbadge}{\raisebox{0.55ex}{\tiny\color{coveraccent}$\bigstar$\kern-0.5pt A}}
\newcommand{\wolfmathbadge}{\raisebox{0.55ex}{\tiny\color{coveramber}$\bigstar$\kern-0.5pt M}}
\newcommand{\wolfbadge}{\raisebox{0.55ex}{\tiny\color{coveramber}$\bigstar$\kern-0.5pt W}}
\newcommand{\kyotobadge}{\raisebox{0.55ex}{\tiny\color{coverprimary}$\blacklozenge$\kern-0.5pt K}}
\newcommand{\shawbadge}{\raisebox{0.55ex}{\tiny\color{coveramber}$\blacklozenge$\kern-0.5pt S}}
\newcommand{\btphysbadge}{\raisebox{0.55ex}{\tiny\color{coverpurple}$\bigstar$\kern-0.5pt B}}
\newcommand{\btmathbadge}{\raisebox{0.55ex}{\tiny\color{coverpurple}$\bigstar$\kern-0.5pt M2}}
\newcommand{\crafoordbadge}{\raisebox{0.55ex}{\tiny\color{coverprimary}$\diamond$\kern-0.5pt C}}
\newcommand{\millenniumbadge}{\raisebox{0.55ex}{\tiny\color{coveraccent}$\blacklozenge$\kern-0.5pt M}}
\newcommand{\japanbadge}{\raisebox{0.55ex}{\tiny\color{coveraccent}$\heartsuit$\kern-0.5pt J}}
\newcommand{\statsbadge}{\raisebox{0.55ex}{\tiny\color{coverpurple}$\blacktriangle$\kern-0.5pt S}}
\newcommand{\copssbadge}{\raisebox{0.55ex}{\tiny\color{covermuted}$\diamondsuit$\kern-0.5pt C}}

\newcommand{\plainbar}{%
\begin{tikzpicture}[remember picture, overlay]
  \fill[coverdark, opacity=0.06] (current page.south west) rectangle ([yshift=0.4cm]current page.south east);
  \draw[coverprimary, opacity=0.40, line width=0.8pt] ([yshift=0.4cm]current page.south west) -- ([yshift=0.4cm]current page.south east);
\end{tikzpicture}%
}

% 底部交叉荣誉边框
\newcommand{\honorbar}[1]{%
  \begin{tikzpicture}[remember picture, overlay]
    \node[anchor=south, draw=coverprimary!55, fill=coverlight, rounded corners=6pt,
          inner xsep=8pt, inner ysep=5pt, yshift=0.65cm, text=coverdark!85] at (current page.south) {%
      \fontsize{7.5}{9.5}\selectfont\bfseries{\color{coverprimary} 其他殊荣}\enspace #1};
  \end{tikzpicture}%
}

\newcommand{\sectiontitle}[2]{%
\vspace{-0.52cm}
\begin{center}
  {\fontsize{20}{24}\selectfont\bfseries\color{titlecolor} #1}\\[2pt]
  {\fontsize{7.5}{9.5}\selectfont\itshape\color{muteddark} #2}
\end{center}
\vspace{0.06cm}
}

% ---- Person slide: #1 name #2 subtitle #3 img/none #4 credit/缩写 #5 获奖(年+岁) #6 life #7 country #8 inst #9 contribution ----
\newcommand{\personslide}[9]{%
\begin{frame}
\stepcounter{pmark}%
\pdfbookmark[2]{\personbookmark}{pb\arabic{pmark}}%
\plainbar
\vspace{-0.45cm}
\begin{center}
  {\fontsize{22}{26}\selectfont\bfseries\color{coverdark} #1}\\[2pt]
  {\fontsize{9.5}{11.5}\selectfont\color{muteddark} #2}
\end{center}
\vspace{0.1cm}
\begin{columns}[c]
\begin{column}{0.20\textwidth}
  \centering
  \ifthenelse{\equal{#3}{none}}{%
    \begin{tikzpicture}
      \node[circle, fill=coverprimary!12, draw=coverprimary!38, minimum size=2.6cm]
        {\fontsize{16}{19}\selectfont\bfseries\color{coverprimary!75!black} #4};
    \end{tikzpicture}
    {\par\vspace{1pt}\fontsize{6.2}{7.2}\selectfont\color{covermuted} 暂无公开照片\par}
  }{%
    \begin{tikzpicture}
      \node[draw=coverprimary!28, line width=0.7pt, fill=white, rounded corners=3pt, inner sep=2.5pt, drop shadow={shadow xshift=0.5pt, shadow yshift=-0.5pt, opacity=0.12}] {
        \includegraphics[width=2.2cm,height=2.7cm,keepaspectratio]{#3}
      };
    \end{tikzpicture}
  }
\end{column}
\begin{column}{0.40\textwidth}
  \begin{tikzpicture}
    \node[fill=goldpanel, rounded corners=4pt, inner xsep=6pt, inner ysep=5pt, text width=4.0cm, align=left] {
      {\fontsize{7}{8.5}\selectfont\bfseries\color{coverprimary!70!black} 获奖}\enspace{\fontsize{7}{8.5}\selectfont\color{coverdark!85} #5}\\[2.5pt]
      {\fontsize{7}{8.5}\selectfont\bfseries\color{coverprimary!70!black} 生卒}\enspace{\fontsize{7}{8.5}\selectfont\color{coverdark!85} #6}\\[2.5pt]
      {\fontsize{7}{8.5}\selectfont\bfseries\color{coverprimary!70!black} 国别}\enspace{\fontsize{7}{8.5}\selectfont\color{coverdark!85} #7}\\[2.5pt]
      {\fontsize{7}{8.5}\selectfont\bfseries\color{coverprimary!70!black} 机构}\enspace{\fontsize{7}{8.5}\selectfont\color{coverdark!85} #8}
    };
  \end{tikzpicture}
\end{column}
\begin{column}{0.38\textwidth}
  \begin{tikzpicture}
    \node[draw=coverprimary!35, fill=bluepanel, rounded corners=5pt, inner sep=7pt, text width=3.8cm, align=left] {
      {\fontsize{8.2}{10}\selectfont\bfseries\color{coverprimary!82!black} 获奖理由}\par\vspace{3pt}
      {\fontsize{7}{8.5}\selectfont\color{coverdark!84} #9}
    };
  \end{tikzpicture}
\end{column}
\end{columns}
\if\relax\detokenize\expandafter{\personhonors}\relax\else\honorbar{\personhonors}\fi
\end{frame}
}

% ---- 章节分隔页 ----
\newcommand{\sectionpageslide}[4]{%
\begin{frame}[plain]
\begin{tikzpicture}[remember picture, overlay]
  \fill[coverprimary!7] (current page.north west) rectangle (current page.south east);
\stepcounter{pmark}%
\pdfbookmark[1]{#1}{bm\arabic{pmark}}%
  \fill[coveramber!12] (current page.south east) ++(-2.3,-1.7) circle (2.0cm);
  \fill[coverpurple!10] (current page.north west) ++(3.0,-1.0) circle (1.1cm);
  \node[anchor=center, font=\fontsize{26}{32}\selectfont\bfseries, text=coverdark]
    at ([yshift=1.10cm]current page.center) {#1};
  \draw[coveramber, line width=1.4pt] ([yshift=0.05cm, xshift=-4.6cm]current page.center)
    -- ([yshift=0.05cm, xshift=4.6cm]current page.center);
  \node[anchor=center, font=\fontsize{13}{16}\selectfont, text=coverprimary!85!black]
    at ([yshift=-0.75cm]current page.center) {#2};
  \node[anchor=center, font=\fontsize{9.5}{12.5}\selectfont\itshape, text=covermuted]
    at ([yshift=-1.85cm]current page.center) {#3};
  \node[anchor=south, font=\scriptsize, text=coverdark!40]
    at ([yshift=0.38cm]current page.south) {#4};
\end{tikzpicture}
\end{frame}
}
"""


def person_tex(p):
    img = "images/" + p["img_file"] if p["img_file"] else "none"
    credit = "Wikipedia" if p["img_file"] else initials(p["name"])
    age = age_str(p)
    year_str = "%d 年（获奖时 %s）" % (p["year"], age) if age else "%d 年" % p["year"]
    contrib = esc(p["citation"])
    if len(p["citation"]) > 90:
        contrib = "{\\fontsize{6}{7.2}\\selectfont " + contrib + "}"
    return ("\\newcommand{\\%s}{\\gdef\\personhonors{%s}\\gdef\\personbookmark{%d · %s %s}\\personslide\n"
            "  {%s}{%s}\n"
            "  {%s}{%s}\n"
            "  {%s}{%s}{%s}{%s}\n"
            "  {%s}}\n" % (
                p["macro"], p["honors_tex"],
                p["year"], esc(p["name"]), esc(p["zh"] or ""),
                esc(p["name"]) + (p["badges_tex"] or ""), esc(p["zh"] or p["name"]),
                img, credit,
                esc(year_str), esc(life_str(p)), esc(country_zh(p["country"])), esc(inst_str(p)),
                contrib))


# ---------- 交叉身份汇总页（双料与大满贯） ----------
CHIP_STYLE = {
    "诺贝尔化学奖": ("$\\clubsuit$", "chemclr"),
    "诺贝尔生理学或医学奖": ("$\\clubsuit$", "medclr"),
    "诺贝尔文学奖": ("$\\clubsuit$", "litclr"),
    "诺贝尔经济学奖": ("$\\clubsuit$", "econclr"),
    "诺贝尔物理学奖": ("$\\clubsuit$", "physclr"),
    "图灵奖": ("$\\blacktriangle$", "turingclr2"),
    "菲尔兹奖": ("$\\bigstar$", "fieldsclr"),
    "阿贝尔奖": ("$\\bigstar$", "abelclr"),
    "沃尔夫数学奖": ("$\\bigstar$", "wolfmathclr"),
    "沃尔夫物理学奖": ("$\\bigstar$", "wolfclr"),
    "京都奖": ("$\\blacklozenge$", "kyotoclr"),
    "邵逸夫奖": ("$\\blacklozenge$", "shawclr"),
    "基础物理学突破奖": ("$\\bigstar$", "btclr"),
    "特别基础物理学突破奖": ("$\\bigstar$", "btclr"),
    "突破奖": ("$\\bigstar$", "btclr"),
    "数学突破奖": ("$\\bigstar$", "btclr"),
    "克拉福德奖": ("$\\diamond$", "crafoordclr"),
    "千禧科技奖": ("$\\blacklozenge$", "millclr"),
    "日本国际奖": ("$\\heartsuit$", "japanclr"),
    "国际统计学奖": ("$\\blacktriangle$", "statsclr"),
    "考普斯会长奖": ("$\\diamondsuit$", "copssclr"),
}
BADGE_BY_LABEL = {label: badge for badge, label in TOP_AWARDS.values() if label in CHIP_STYLE}
ROW_ORDER = list(BADGE_BY_LABEL.keys())
ORG_TAILS = {"cross", "union", "bank", "programme", "agency", "committee", "bureau",
             "fund", "council", "quartet", "organization", "organisation", "society",
             "forces", "nations", "welfare", "office", "movement"}


def build_summary_rows(people):
    cats = {}
    for p in people:
        for badge, label, yr in (p.get("cross_items") or []):
            if label not in CHIP_STYLE:
                continue
            cats.setdefault(label, {})[(p["name"], yr)] = badge
    rows = []
    for label in ROW_ORDER:
        if label not in cats:
            continue
        entries = sorted(cats[label].items(), key=lambda kv: (kv[0][1] or "9999", kv[0][0]))
        surnames = []
        for (n, y), b in entries:
            toks = n.replace("-", " ").replace("'", " ").split()
            if len(toks) >= 2 and toks[-1].lower() in ORG_TAILS:
                surnames.append(" ".join(toks[-2:]))
            else:
                surnames.append(toks[-1])
        rows.append((BADGE_BY_LABEL[label], label, len(entries), surnames, ""))
    return rows


def cross_summary_slide(rows, n_years, n_records, n_people):
    if not rows:
        return ""
    chip_style = CHIP_STYLE

    def split_names(names, limit=60):
        lines, cur = [], ""
        for n in names:
            cand = n if not cur else cur + "·" + n
            if len(cand) > limit and cur:
                lines.append(cur)
                cur = n
            else:
                cur = cand
        if cur:
            lines.append(cur)
        return ["\\;·\\;".join(l.split("·")) for l in lines]

    nodes = []
    y = 0.0
    for badge, label, cnt, names, note in rows:
        sym, col = chip_style[label]
        body_lines = split_names(names)
        chip_text = "%s\\;\\; %s人" % (label, cnt)
        for j, bl in enumerate(body_lines):
            nodes.append(
                "  \\node[anchor=north west, text width=8.0cm, align=left,\n"
                "        font=\\fontsize{5.5}{6.5}\\selectfont, text=%s!70!black]\n"
                "    at (-1.70,%.2f) {%s};\n"
                % (col, y - j * 0.28, bl))
        nodes.append(
            "  \\node[fill=%s, rounded corners=4pt, text width=3.5cm, minimum height=0.55cm,\n"
            "        inner sep=0pt, align=center, anchor=north west] at (-5.4,%.2f)\n"
            "    {\\fontsize{5.5}{6.5}\\selectfont\\bfseries\\color{white}%s\\;\\; %s};\n"
            % (col, y, sym, chip_text))
        y -= 0.28 * len(body_lines) + 0.30
    bar_top = y - 0.25
    bar_bot = y - 0.75
    nodes.append(
        "  \\fill[coverlight, rounded corners=4pt] (-5.5,%.2f) rectangle (5.6,%.2f);\n"
        "  \\node[anchor=north, text width=3.7cm, align=center,\n"
        "        font=\\fontsize{4.5}{5.5}\\selectfont\\bfseries, text=coverprimary]\n"
        "    at (-3.60,%.2f) {首届\\;\\; Henry Dunant \\& Frédéric Passy\\;(1901)};\n"
        % (bar_bot, bar_top, bar_top - 0.10))
    nodes.append(
        "  \\node[anchor=north, text width=3.7cm, align=center,\n"
        "        font=\\fontsize{4.5}{5.5}\\selectfont\\bfseries, text=coverprimary]\n"
        "    at (0.00,%.2f) {%d 个颁奖年份\\;\\; %d 条记录 / %d 位获奖者};\n"
        "  \\node[anchor=north, text width=3.7cm, align=center,\n"
        "        font=\\fontsize{4.5}{5.5}\\selectfont\\bfseries, text=coverprimary]\n"
        "    at (3.60,%.2f) {唯一拒奖\\;\\; Lê Đức Thọ\\;(1973)};\n"
        % (bar_top - 0.10, n_years, n_records, n_people, bar_top - 0.10))
    body = "\n".join(nodes)
    return ('''\\begin{frame}{双料与大满贯 · 诺贝尔和平奖得主身份总览}
\\pdfbookmark[1]{双料与大满贯 · 交叉身份总览}{crosssummary}
\\vspace{-4pt}
\\centering
\\begin{tikzpicture}
''' + body + r'''
\end{tikzpicture}
\end{frame}

''')


def make_cover(people, n_records, n_people, n_years):
    W, H, GAP = 0.40, 0.46, 0.04
    COLS = 24
    rows = (len(people) + COLS - 1) // COLS
    total_h = (rows - 1) * (H + GAP)
    start_x = -((COLS - 1) * (W + GAP)) / 2.0
    start_y = total_h / 2.0
    cy = -1.85
    grid = ['  \\node[anchor=center] at ([yshift=%.2fcm]current page.center) {' % cy,
            '    \\begin{tikzpicture}[scale=1]']
    for i, p in enumerate(people):
        r, c = i // COLS, i % COLS
        x = start_x + c * (W + GAP)
        y = start_y - r * (H + GAP)
        if p["img_file"]:
            grid.append('      \\node[inner sep=0pt, draw=coverprimary!22, line width=0.2pt] at (%.2f,%.2f) {'
                        '\\includegraphics[width=%scm,height=%scm,keepaspectratio]{images/%s}};'
                        % (x, y, W, H, p["img_file"]))
        else:
            grid.append('      \\node[circle, fill=coverprimary!8, draw=coverprimary!30, '
                        'minimum size=%scm, inner sep=0pt] at (%.2f,%.2f) {'
                        '\\fontsize{5}{6}\\selectfont\\color{covermuted} %s};'
                        % (min(W, H) * 0.9, x, y, initials(p["name"])))
    grid.append('    \\end{tikzpicture}')
    grid.append('  };')
    grid_tikz = "\n".join(grid)
    return (r'''\newcommand{\coverslide}{%%
\begin{frame}[plain]
\pdfbookmark[1]{封面 · 诺贝尔和平奖 1901–2025}{cover}
\begin{tikzpicture}[remember picture, overlay]
  \fill[coverprimary!6] (current page.north west) rectangle (current page.south east);
  \fill[coveraccent!10] (current page.south east) ++(-2.3,-1.7) circle (2.0cm);
  \fill[coveramber!14] (current page.north east) ++(-2.4,1.4) circle (1.2cm);
  \fill[coverpurple!10] (current page.north west) ++(3.0,-1.0) circle (0.9cm);
  \node[anchor=center, font=\fontsize{17}{22}\selectfont\bfseries, text=coverdark]
    at ([yshift=3.35cm]current page.center) {诺贝尔和平奖：橄榄枝的世纪（1901–2025）};
  \node[anchor=center, font=\fontsize{12}{15}\selectfont, text=coverprimary!85!black]
    at ([yshift=2.50cm]current page.center) {Nobel Peace Prize · %d 条记录 / %d 位获奖者（含机构）};
  \draw[coverprimary, line width=1.4pt] ([yshift=1.90cm, xshift=-5.2cm]current page.center)
    -- ([yshift=1.90cm, xshift=5.2cm]current page.center);
  \node[anchor=center, font=\fontsize{9.5}{12.5}\selectfont\bfseries, text=coveramber!58!black]
    at ([yshift=1.58cm]current page.center) {从 Henry Dunant 到 Nihon Hidankyo · 人道主义者与机构一个多世纪的和平接力};
''' + grid_tikz + r'''
  \node[anchor=center, font=\fontsize{10}{12}\selectfont\bfseries, text=DeepPurpleAccent]
    at ([yshift=1.12cm]current page.center) {\faIcon{medal}\enspace Nobel Peace Prize\enspace|\enspace 1901–2025 · 全 %d 个颁奖年份};
\end{tikzpicture}
\end{frame}
}
''') % (n_records, n_people, n_years)


def intro_slide(legend_lines, n_records, n_people, n_years):
    if legend_lines:
        legend_tex = " \\\\\n    ".join(legend_lines)
    else:
        legend_tex = "本片得主暂无其他顶级奖项交叉记录"
    return (r'''\newcommand{\introslide}{%%
\begin{frame}
\pdfbookmark[1]{认识诺贝尔和平奖}{intro}
\plainbar
\sectiontitle{认识诺贝尔和平奖}{Nobel Peace Prize · 1901–2025}
\vspace{0.05cm}
\begin{center}
\begin{tikzpicture}
  \node[draw=coverprimary!40, fill=bluepanel, rounded corners=5pt, inner sep=7pt, text width=6.4cm, align=left, anchor=north west] at (-7.05,3.05) {%%
    {\fontsize{8}{9.5}\selectfont\bfseries\color{coverprimary!82!black} 规模}\\[2pt]
    {\fontsize{7}{8.5}\selectfont\color{coverdark!84} 1901 年首颁（Henry Dunant 与 Frédéric Passy 共获）；至 2025 年共评奖 ''' + str(n_years) + r''' 个年份、''' + str(n_records) + r''' 条记录，涉及 ''' + str(n_people) + r''' 位获奖者（含机构），本片全收录。}};
  \node[draw=coveraccent!40, fill=redpanel, rounded corners=5pt, inner sep=7pt, text width=6.4cm, align=left, anchor=north west] at (-7.05,0.55) {%%
    {\fontsize{8}{9.5}\selectfont\bfseries\color{coveraccent!82!black} 多次获奖与特殊记录}\\[2pt]
    {\fontsize{7}{8.5}\selectfont\color{coverdark!84} 红十字国际委员会三度获奖（1917 · 1944 · 1963）；\\联合国难民署两度获奖（1954 · 1981）。\\黎德寿 1973 年拒绝领奖，迄今唯一。}};
  \node[draw=coverpurple!40, fill=purplepanel, rounded corners=5pt, inner sep=7pt, text width=7.6cm, align=left, anchor=north west] at (0.30,3.05) {%%
    {\fontsize{8}{9.5}\selectfont\bfseries\color{coverpurple!82!black} 交叉荣誉 · 徽标一览}\par\vspace{3pt}
    {\fontsize{6.6}{12.8}\selectfont\color{coverdark!84} ''' + legend_tex + r'''}};
  \node[draw=coveramber!45, fill=goldpanel, rounded corners=5pt, inner sep=7pt, text width=7.6cm, align=left, anchor=north west] at (0.30,1.10) {%%
    {\fontsize{8}{9.5}\selectfont\bfseries\color{coveramber!70!black} 空缺年份}\\[2pt]
    {\fontsize{6.8}{8.2}\selectfont\color{coverdark!84} 19 个年份未颁奖（1914–16 · 1918 · 1923–24 · 1928 · 1932 ·\\1939–43 · 1948 · 1955–56 · 1966–67 · 1972），\\多因两次世界大战与冷战僵局。}};
\end{tikzpicture}
\end{center}
\end{frame}
}
''')


def section_slide(name, sub, note):
    return ('\\newcommand{\\%s}{\\sectionpageslide\n'
            '  {%s}\n  {%s}\n  {%s}\n'
            '  {Nobel Peace Prize · 1901–2025}\n}\n' % (name, sub, note, ""))


def ending_slide(n_people):
    return (r"""\newcommand{\closingslide}{%
\begin{frame}[plain]
\begin{tikzpicture}[remember picture, overlay]
  \fill[coverprimary!7] (current page.north west) rectangle (current page.south east);
\pdfbookmark[1]{结语}{ending}
  \fill[coveramber!12] (current page.north east) ++(-2.4,1.4) circle (1.6cm);
  \fill[coverpurple!10] (current page.south west) ++(3.0,-1.0) circle (1.2cm);
  \node[anchor=center, font=\fontsize{22}{28}\selectfont\bfseries, text=coverdark]
    at ([yshift=1.10cm]current page.center) {橄榄枝长青，和平代代相传};
  \draw[coveramber, line width=1.4pt] ([yshift=0.15cm, xshift=-4.6cm]current page.center)
    -- ([yshift=0.15cm, xshift=4.6cm]current page.center);
  \node[anchor=center, font=\fontsize{10.5}{14}\selectfont, text=coverprimary!85!black]
    at ([yshift=-0.75cm]current page.center) {谨以此片致敬 1901–2025 全部 """ + str(n_people) + r""" 位诺贝尔和平奖获奖者与机构};
  \node[anchor=center, font=\fontsize{8.5}{11.5}\selectfont\itshape, text=covermuted]
    at ([yshift=-1.70cm]current page.center) {每一次对暴力的拒绝，都是对人类尊严的重申。};
  \node[anchor=south, font=\scriptsize, text=coverdark!40]
    at ([yshift=0.38cm]current page.south) {\faIcon{medal}\enspace Nobel Peace Prize · 1901–2025};
\end{tikzpicture}
\end{frame}
}
""")


def write_missing_md(people):
    missing = [p for p in people if not p["img_file"]]
    lines = ["# Nobel Peace Video Series — Missing Portrait Checklist", "",
             "> Source: `peace/presentations/pages/{20th,21th}_century/<Dir>/images.txt`（自动下载）",
             "> 共 %d 条记录 / %d 位获奖者中 **%d 位** 缺真人肖像，待人工补图。" % (len(people), len({norm(p['name']) for p in people}), len(missing)), "",
             "## 缺照片获奖者", "",
             "| 年份 | 获奖者 | 占位文件 | 页面目录 | 备注 |",
             "|---|---|---|---|---|"]
    for p in missing:
        d = (p.get("page") or {}).get("dir", "—")
        reason = BLOCK_IMAGES.get(p["name"], "images.txt 无匹配人像（已过滤旗帜/签名/图标），或候选图下载失败")
        lines.append("| %d | %s | `episode-allinone/images/%s.jpg` | `%s` | %s |"
                     % (p["year"], p["name"], p["slug"], os.path.relpath(d, PRES), reason))
    lines += ["",
              "## 如何补图", "",
              "1. 从 Wikipedia Commons / 官方主页 / Nobel 官网下载真人肖像（建议宽 ≥ 250px）。"
              "亦可把人工校准图放入 `peace/video/episode-allinone/figures/`（文件名为人物英文名，如 `Henry Dunant.jpg`，优先级最高）。",
              "2. 保存为 `.jpg`（首选）/`.jpeg`/`.png`/`.webp`，命名与下表占位文件同名（扩展名可不同），放入 `peace/video/episode-allinone/images/`。",
              "3. 重新运行 `python3 gen_peace.py`（自动检测非空文件并使用），再 `make pdf && make video`。", "",
              "## 当前状态", "",
              "- 总获奖者：**%d 位**（含机构，1901–2025）" % len({norm(p['name']) for p in people}),
              "- 真人肖像在位：**%d 条记录**" % (len(people) - len(missing)),
              "- 缺肖像（占位）：**%d 条记录**" % len(missing)]
    with open(os.path.join(VID, "missing_photos.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print("missing_photos.md: %d missing / %d total" % (len(missing), len(people)))


MAKEFILE = r"""# Makefile for Nobel Peace allinone video.
MAIN        = peace_allinone_zh
VIDEO_NAME  = peace_allinone_zh
OUTPUT_DIR  = output
IMAGES_DIR  = $(OUTPUT_DIR)/images
SLIDES_TXT  = $(OUTPUT_DIR)/slides.txt
DURATION    = 7
BGM         = $(wildcard *.wav)
LATEXMK     = latexmk
PDFTOPPM    = pdftoppm
FFMPEG      = ffmpeg
PYTHON      = python3

.PHONY: all pdf images video clean distclean
all: pdf

pdf: $(MAIN).pdf
$(MAIN).pdf: $(MAIN).tex
	$(LATEXMK) -xelatex -synctex=0 -interaction=nonstopmode $(MAIN).tex || \
	  (rm -f $(MAIN).fdb_latexmk && $(LATEXMK) -xelatex -synctex=0 -interaction=nonstopmode -f $(MAIN).tex)
	$(LATEXMK) -c $(MAIN).tex

images: $(IMAGES_DIR)/.done
$(IMAGES_DIR)/.done: $(MAIN).pdf
	@mkdir -p $(IMAGES_DIR)
	$(PDFTOPPM) -png -r 600 $(MAIN).pdf $(IMAGES_DIR)/slide
	@cd $(IMAGES_DIR) && for f in slide-*.png; do mv "$$f" "$$(echo $$f | sed 's/-/_/')"; done 2>/dev/null || true
	@touch $@

$(SLIDES_TXT): $(IMAGES_DIR)/.done
	@$(PYTHON) -c "\
	import os; \
	imgs = sorted([f for f in os.listdir('$(IMAGES_DIR)') if f.endswith('.png')]); \
	lines = []; \
	[lines.extend(['file ' + 'images/' + f, 'duration $(DURATION)']) for f in imgs]; \
	lines.append('file ' + 'images/' + imgs[-1]); \
	open('$(SLIDES_TXT)', 'w').write(chr(10).join(lines) + chr(10)); \
	print(f'  slides.txt: {len(imgs)} slides x $(DURATION)s = {len(imgs)*$(DURATION)}s')"

video: $(OUTPUT_DIR)/$(VIDEO_NAME).mp4
$(OUTPUT_DIR)/$(VIDEO_NAME).mp4: $(SLIDES_TXT)
	@mkdir -p $(OUTPUT_DIR)
	@rm -f $(OUTPUT_DIR)/$(VIDEO_NAME).tmp.mp4 $(OUTPUT_DIR)/$(VIDEO_NAME).mp4
ifeq ($(strip $(BGM)),)
	$(FFMPEG) -y -f concat -safe 0 -i $(SLIDES_TXT) \
	  -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -profile:v high -pix_fmt yuv420p \
	  -crf 15 -preset medium -r 24 $(OUTPUT_DIR)/$(VIDEO_NAME).tmp.mp4
else
	$(FFMPEG) -y -f concat -safe 0 -i $(SLIDES_TXT) -stream_loop -1 -i "$(firstword $(BGM))" \
	  -vf "pad=ceil(iw/2)*2:ceil(ih/2)*2" -c:v libx264 -profile:v high -pix_fmt yuv420p \
	  -crf 15 -preset medium -r 24 -c:a aac -b:a 192k -shortest $(OUTPUT_DIR)/$(VIDEO_NAME).tmp.mp4
endif
	@mv $(OUTPUT_DIR)/$(VIDEO_NAME).tmp.mp4 $(OUTPUT_DIR)/$(VIDEO_NAME).mp4
	@cp $(OUTPUT_DIR)/$(VIDEO_NAME).mp4 $(VIDEO_NAME).mp4
	@echo "==== Done: $(VIDEO_NAME).mp4 ===="

clean:
	$(LATEXMK) -c $(MAIN).tex 2>/dev/null || true
	rm -f $(MAIN).{aux,log,toc,out,nav,snm,fls,fdb_latexmk,xdv}
	rm -f $(SLIDES_TXT) $(IMAGES_DIR)/.done c.log

distclean: clean
	rm -f $(MAIN).pdf
	rm -rf $(IMAGES_DIR)
	rm -f $(OUTPUT_DIR)/$(VIDEO_NAME).mp4 $(VIDEO_NAME).mp4
"""


def main():
    people = parse_lists()
    pages = load_page_index()
    print("laureate records: %d, page dirs: %d" % (len(people), len(pages)))
    unmatched = []
    for p in people:
        pg = match_page(p, pages)
        p["page"] = pg
        if not pg:
            unmatched.append("%d %s" % (p["year"], p["name"]))
    if unmatched:
        print("WARN unmatched page dirs (%d): %s" % (len(unmatched), "; ".join(unmatched)))

    # 图像 slug 按姓名去重（同姓名多条记录共享头像文件）；宏名加后缀保证唯一
    used = set()
    slug_by_key = {}
    for p in people:
        key = norm(p["name"])
        if key not in slug_by_key:
            base = slug_of(p["name"]) or "laureate"
            while base in used:
                base += "x"
            used.add(base)
            slug_by_key[key] = base
        p["slug"] = slug_by_key[key]

    # 每条记录唯一宏名（同姓名多条记录追加后缀 A/B…）
    seen = {}
    for p in people:
        cnt = seen.get(p["slug"], 0)
        seen[p["slug"]] = cnt + 1
        p["macro"] = p["slug"] + ("" if cnt == 0 else chr(ord("A") + cnt - 1))

    build_db_cross(people)
    merge_static_cross(people)
    for p in people:
        p["honors_tex"] = cross_tex(p)
        p["badges_tex"] = p["badges_str"]
    n_img = sync_all(people, pages)
    print("portraits in place: %d / %d records" % (n_img, len(people)))
    write_missing_md(people)

    n_records = len(people)
    n_people = len({norm(p["name"]) for p in people})
    n_years = len({p["year"] for p in people})
    n20 = sum(1 for p in people if p["century"] == "20th")
    n21 = sum(1 for p in people if p["century"] == "21st")

    os.makedirs(EP, exist_ok=True)
    out = [HEADER]
    out.append(make_cover(people, n_records, n_people, n_years))
    legend_lines = []
    for label in ROW_ORDER:
        badge = BADGE_BY_LABEL[label]
        cnt = sum(1 for q in people for it in (q.get("cross_items") or []) if it[1] == label)
        if cnt:
            legend_lines.append("%s{} %s · %d 位" % (badge, label, cnt))
    out.append(intro_slide(legend_lines, n_records, n_people, n_years))
    out.append(section_slide("twentiethslide",
                             "第一乐章 · 20 世纪（1901–2000）",
                             "从红十字国际委员会到金大中 · %d 条记录" % n20))
    out.append(section_slide("twentyfirstslide",
                             "第二乐章 · 21 世纪（2001–2025）",
                             "从联合国到 Nihon Hidankyo · %d 条记录" % n21))
    out.append(ending_slide(n_people))
    out.append("\n% ========== SLIDES (chronological) ==========\n")
    for p in people:
        out.append(person_tex(p))
    out.append("\n% ========== MAIN ==========\n\\begin{document}\n")
    out.append("\\coverslide\n\\introslide\n")
    body = []
    cur = None
    for p in people:
        if p["century"] != cur:
            cur = p["century"]
            body.append("\\%sslide" % ("twentieth" if cur == "20th" else "twentyfirst"))
        body.append("\\%s" % p["macro"])
    out.append("\n".join(body) + "\n")
    out.append("\\closingslide\n\\end{document}\n")
    tex = os.path.join(EP, MAIN + ".tex")
    with open(tex, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print("wrote", tex)
    with open(os.path.join(EP, "Makefile"), "w", encoding="utf-8") as f:
        f.write(MAKEFILE)
    # BGM 软链（同 physicist 约定）
    wav = os.path.join(EP, "bgm.wav")
    if not os.path.lexists(wav):
        os.symlink("../../../music_audio/bgm.wav", wav)


if __name__ == "__main__":
    main()
