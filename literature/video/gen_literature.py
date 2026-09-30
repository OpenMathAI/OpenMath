#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Nobel Literature allinone video deck (literature_allinone_zh.tex).

复用 physicist/video/episode-allinone 的 Beamer 模板（personslide + 封面头像网格），
配色改为「酒红 + 墨绿 + 金褐」文学主题（区别于物理学深空蓝）。

数据来源：
  - literature/presentations/{20th,21st}_century/OpenLiterature_*_Nobel_Laureates.md（年份/姓名/国籍/获奖理由，理由已中译）
  - literature/presentations/pages/{20th,21st}_century/<Dir>/metadata.json（生卒/职业/QID）
  - 同目录 images.txt（封面与人像页头像，curl 下载，过滤旗帜/签名/图标）
交叉荣誉：greatminds.award_laureate 数据库直查（文学奖得主的其他顶级奖项）。
缺头像：集中记录在 literature/video/missing_photos.md，占位空文件待人工补图后重跑本脚本。

相对物理版的修正：统计宏（RECORDCOUNT 等）在生成时以真实数字替换（物理版遗留未替换的 bug）。

Run: cd literature/video && python3 gen_literature.py
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
MAIN = "literature_allinone_zh"

LISTS = [
    (os.path.join(PRES, "20th_century", "OpenLiterature_20th_Century_Nobel_Laureates.md"),
     os.path.join(PRES, "pages", "20th_century"), "20th"),
    (os.path.join(PRES, "21st_century", "OpenLiterature_21st_Century_Nobel_Laureates.md"),
     os.path.join(PRES, "pages", "21st_century"), "21st"),
]

COUNTRY_ZH = {
    "United States": "美国", "United Kingdom": "英国", "Germany": "德国", "France": "法国",
    "France Switzerland": "法国/瑞士", "Switzerland United Kingdom": "瑞士/英国",
    "Republic of China": "Republic of China（诺贝尔官方历史口径）",
    "Netherlands": "荷兰", "Sweden": "瑞典", "Italy": "意大利", "Denmark": "丹麦",
    "Austria": "奥地利", "Austria Hungary": "奥匈帝国", "Switzerland": "瑞士", "Japan": "日本",
    "China": "中国", "Canada": "加拿大", "Russia": "俄罗斯", "Soviet Union": "苏联",
    "Russian Empire": "俄罗斯帝国", "India": "印度", "Pakistan": "巴基斯坦", "Australia": "澳大利亚",
    "Ireland": "爱尔兰", "Belgium": "比利时", "Norway": "挪威", "Finland": "芬兰",
    "Poland": "波兰", "Argentina": "阿根廷", "Mexico": "墨西哥", "Israel": "以色列",
    "New Zealand": "新西兰", "Luxembourg": "卢森堡", "Hungary": "匈牙利", "Spain": "西班牙",
    "Lithuania": "立陶宛", "Belarus": "白俄罗斯", "Ukraine": "乌克兰", "Czech Republic": "捷克",
    "Czechoslovakia": "捷克斯洛伐克", "West Germany": "西德", "East Germany": "东德",
    "Germany West Germany": "德国/西德", "United Kingdom China": "英国/中国",
    "United States United Kingdom": "美国/英国", "United Kingdom United States": "英国/美国",
    "United States Germany": "美国/德国", "Germany United States": "德国/美国",
    "United States Italy": "美国/意大利", "Italy United States": "意大利/美国",
    "United States Canada": "美国/加拿大", "Canada United States": "加拿大/美国",
    "France United States": "法国/美国", "United States France": "美国/法国",
    "United States China": "美国/中国", "China United States": "中国/美国",
    "United Kingdom Germany": "英国/德国", "Germany Switzerland": "德国/瑞士",
    "United Kingdom Austria": "英国/奥地利", "Japan United States": "日本/美国",
    "United States Japan": "美国/日本", "Sweden Japan": "瑞典/日本", "France Sweden": "法国/瑞典",
    "Hungary Germany": "匈牙利/德国", "United Kingdom Bangladesh": "英国/孟加拉",
    "Austria Ireland": "奥地利/爱尔兰", "None": "无国籍（无国籍人士）", "Stateless": "无国籍",
    # ---- 文学奖特有国籍 ----
    "Chile": "智利", "Colombia": "哥伦比亚", "Greece": "希腊", "Guatemala": "危地马拉",
    "Iceland": "冰岛", "Egypt": "埃及", "Nigeria": "尼日利亚", "Portugal": "葡萄牙",
    "Saint Lucia": "圣卢西亚", "South Africa": "南非", "South Korea": "韩国",
    "Turkey": "土耳其", "Yugoslavia": "南斯拉夫", "Trinidad and Tobago": "特立尼达和多巴哥",
    "Mauritius": "毛里求斯", "Romania": "罗马尼亚", "Tanzania": "坦桑尼亚",
    "Bulgaria": "保加利亚", "Peru": "秘鲁", "Bosnia and Herzegovina": "波黑",
    "Cape Verde": "佛得角", "Saint Lucia Venezuela": "圣卢西亚/委内瑞拉",
}

CITATION_ZH = {}  # 文学奖名录的获奖理由已是中文，直取原值

# ---------- 静态交叉荣誉兜底（文学奖无既有静态清单，以数据库直查为准） ----------
CROSS_TURING = []
CROSS_WOLF = []


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
                                   citation=CITATION_ZH.get(cells[3], cells[3]),
                                   century=cent, source_index=len(people)))
    people.sort(key=lambda p: (p["year"], p["source_index"]))
    return people


def doc_stats(people):
    unique = {norm(p["name"]) for p in people}
    years = {p["year"] for p in people}
    by_century = {}
    for p in people:
        by_century[p["century"]] = by_century.get(p["century"], 0) + 1
    return {
        "records": len(people),
        "unique_people": len(unique),
        "award_years": len(years),
        "20th_records": by_century.get("20th", 0),
        "21st_records": by_century.get("21st", 0),
    }


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
                              employer=props.get("employer") or [],
                              occupation=props.get("occupation") or []))
    return pages


def match_page(p, pages):
    pt = set(tokens(p["name"]))
    pst = stems(p["name"])
    pn = norm(p["name"])
    best, best_s = None, -1.0
    for pg in pages:
        gt = set(tokens(pg["name"])) | set(tokens(pg["dname"].replace("_", " ")))
        gst = stems(pg["name"])
        gn = norm(pg["name"])
        if pn and pn == gn:
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


def match_cross(p):
    pst = stems(p["name"])
    out = []
    for n in CROSS_TURING:
        if pst == stems(n) or pst <= stems(n):
            out.append("\\turingbadge{} 图灵奖 2018")
            break
    for n, yr in CROSS_WOLF:
        if pst == stems(n) or pst <= stems(n):
            out.append("\\wolfbadge{} 沃尔夫物理学奖 " + yr)
            break
    return " \\enspace ".join(out)


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


def static_cross_items(p):
    items = []
    pst = stems(p["name"])
    for n in CROSS_TURING:
        if pst == stems(n) or pst <= stems(n):
            items.append(("\\turingbadge", "图灵奖", "2018"))
            break
    for n, yr in CROSS_WOLF:
        if pst == stems(n) or pst <= stems(n):
            items.append(("\\wolfbadge", "沃尔夫物理学奖", yr))
            break
    return items


def build_db_cross(people):
    """库内直查每人顶级交叉奖项；数据库不可用或 QID 不完整时直接失败。"""
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
    ids = ",".join(str(i) for i in TOP_AWARDS)
    n_cross = 0
    for p in people:
        qid = qid_by.get((p["year"], p["name"]))
        rec = pid_by.get(qid) if qid else None
        items = []
        if rec:
            cur.execute("SELECT award_id,year FROM award_laureate WHERE person_id=%s AND award_id IN (%s) AND award_id<>25" % (rec, ids))
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


def cross_tex(p, db_ok):
    if db_ok:
        items = p.get("cross_items") or []
        if not items:
            p["badges_str"] = ""
            return ""
        p["badges_str"] = ("\\," if items else "") + "".join(b + "{}" for b, _, _ in items)
        return " \\enspace ".join("%s{} %s%s" % (b, lab, (" " + y) if y else "") for b, lab, y in items)
    items = static_cross_items(p)
    if not items:
        p["badges_str"] = ""
        return ""
    p["badges_str"] = "".join(b + "{}" for b, _, _ in items)
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
    data = curl(su, tries=2) if su else None
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
        data = curl(u)
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
BLOCK_IMAGES = {
    # 首版暂无已证实的坏图；人工目检后在此登记（键=名录姓名），防止自动抓取回归
}


def sync_all(people, pages):
    os.makedirs(IMGDIR, exist_ok=True)
    used = set()
    for p in people:
        base = slug_of(p["name"]) or "laureate"
        while base in used:
            base += "x"
        used.add(base)
        p["slug"] = base

    force = bool(os.environ.get("FORCE_IMG"))
    if force:
        for f in os.listdir(IMGDIR):
            if not f.startswith("."):
                os.remove(os.path.join(IMGDIR, f))

    def work(p):
        # 禁用清单仅阻止自动抓取（防坏图回归）；已有有效图片一律保留
        if p["name"] in BLOCK_IMAGES and not find_figure(p["name"]):
            # 禁用名单始终阻止自动抓取；仅 FORCE_IMG 时清理已有文件
            if os.environ.get("FORCE_IMG"):
                for ext in ("jpg", "jpeg", "png", "webp"):
                    fp = os.path.join(IMGDIR, p["slug"] + "." + ext)
                    if os.path.exists(fp):
                        os.remove(fp)
            return "blocked"
        pg = p.get("page")
        dst = os.path.join(IMGDIR, p["slug"] + ".jpg")
        # 已有有效文件则跳过（figures 人工校准图优先，同 turing 约定）
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
        # 不覆盖非同名占位（如已有人工放置的 .png）
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
        return "%s–%s" % (y1, y2)
    if y1:
        return y1 + "–"
    return ""


OCC_ZH = {
    "poet": "诗人", "writer": "作家", "novelist": "小说家", "playwright": "剧作家",
    "essayist": "散文家", "philosopher": "哲学家", "journalist": "记者", "translator": "翻译家",
    "short story writer": "短篇小说家", "literary critic": "文学评论家", "critic": "评论家",
    "historian": "历史学家", "diplomat": "外交官", "lawyer": "律师", "poet lawyer": "诗人·律师",
    "poet_diplomat": "诗人外交官", "politician": "政治人物", "screenwriter": "编剧",
    "librettist": "剧词作者", "biographer": "传记作家", "composer": "作曲家",
    "singer-songwriter": "歌手·词曲作者", "musician": "音乐人", "university teacher": "大学教师",
    "autobiographer": "自传作家", "children's writer": "儿童文学作家", "physician": "医生",
    "linguist": "语言学家", "orientalist": "东方学家", "theologian": "神学家",
    "literary": "文学家", "satirist": "讽刺作家", "memoirist": "回忆录作家",
    "aphorist": "格言作家", "dramaturge": "戏剧顾问", "songwriter": "词曲作者",
    "singer": "歌手", "actor": "演员", "stage actor": "舞台演员", "scholar": "学者",
    "opinion journalist": "时评记者", "prose writer": "散文作家", "epigrammatist": "警句作家",
    "parodist": "戏仿作家", "fairy tale": "童话作家", "novella writer": "中篇小说家",
    # ---- 全量补充（pages metadata 实测取值）----
    "author": "作家", "intellectual": "思想家", "professor": "教授", "sociologist": "社会学家",
    "psychologist": "心理学家", "economist": "经济学家", "mathematician": "数学家",
    "chemist": "化学家", "engineer": "工程师", "anthropologist": "人类学家",
    "archaeologist": "考古学家", "classical archaeologist": "古典考古学家",
    "philologist": "语文学家", "germanist": "日耳曼学者", "lexicographer": "词典编纂家",
    "librarian": "图书馆员", "archivist": "档案学者", "editor": "编辑",
    "newspaper editor": "报纸编辑", "scientific editor": "科学编辑", "editing staff": "编辑",
    "publisher": "出版人", "bookseller": "书商", "columnist": "专栏作家",
    "correspondent": "通讯记者", "reporter": "记者", "war correspondent": "战地记者",
    "broadcaster": "播音员", "radio personality": "电台名人", "disc jockey": "唱片骑师",
    "narrator": "朗读者", "audiobook narrator": "有声书朗读者",
    "literary historian": "文学史家", "literary scholar": "文学学者",
    "legal historian": "法律史家", "oral historian": "口述史学家", "chronicler": "编年史家",
    "jurist": "法学家", "judge": "法官", "ambassador": "大使", "consul": "领事",
    "statesperson": "政治家", "head of government": "政府首脑", "member of parliament": "议员",
    "minister": "部长·牧师", "diplomatist": "外交官",
    "military officer": "军官", "military personnel": "军人", "soldier": "军人",
    "resistance fighter": "抵抗运动成员", "freedom fighter": "自由战士",
    "french resistance fighter": "法国抵抗运动成员", "revolutionary": "革命者",
    "militant": "活动人士", "pacifist": "和平主义者", "peace activist": "和平活动家",
    "human rights defender": "人权捍卫者", "social reformer": "社会改革家",
    "social critic": "社会评论家", "socialist": "社会主义者", "public figure": "公众人物",
    "teacher": "教师", "school teacher": "中小学教师", "volksschule teacher": "国民学校教师",
    "lecturer": "讲师", "docent": "讲师", "visiting docent": "客座讲师", "pedagogue": "教育家",
    "academic": "学者", "missionary": "传教士", "altar server": "辅祭",
    "mystic": "神秘主义者", "astrologer": "占星家", "esotericist": "神秘学作家",
    "artist": "艺术家", "painter": "画家", "sculptor": "雕塑家", "illustrator": "插画家",
    "graphic artist": "平面艺术家", "printmaker": "版画家", "wood engraver": "木刻家",
    "draftsperson": "制图员", "designer": "设计师", "costume designer": "服装设计师",
    "scenographer": "舞台美术师", "photographer": "摄影师", "video artist": "视频艺术家",
    "visual artist": "视觉艺术家", "cinematographer": "电影摄影师",
    "film director": "电影导演", "director": "导演", "filmmaker": "电影人",
    "film producer": "电影制片人", "film actor": "电影演员", "film screenwriter": "电影编剧",
    "television actor": "电视演员", "television writer": "电视编剧",
    "theatre director": "戏剧导演", "theatre manager": "剧院经理", "theatre critic": "戏剧评论家",
    "music critic": "音乐评论家", "musicologist": "音乐学家", "pianist": "钢琴家",
    "guitarist": "吉他手", "record producer": "唱片制作人", "lyricist": "作词人",
    "art critic": "艺术评论家", "art collector": "艺术收藏家", "art historian": "艺术史家",
    "epistemologist": "认识论学者", "metaphysician": "形而上学家",
    "analytic philosopher": "分析哲学家", "natural philosopher": "自然哲学家",
    "philosopher of language": "语言哲学家", "philosopher of science": "科学哲学家",
    "logician": "逻辑学家", "historian of classical antiquity": "古典史学家",
    "numismatist": "钱币学家", "epigrapher": "碑铭学家",
    "political writer": "政治作家", "travel writer": "游记作家", "traveler": "旅行家",
    "diarist": "日记作家", "satirical novelist": "讽刺小说家",
    "science fiction writer": "科幻作家", "young adult author": "青年文学作家",
    "translator of William Shakespeare": "莎士比亚译者", "translator-interpreter": "翻译·口译",
    "esperantist": "世界语者", "mechanic": "机械师", "civil engineer": "土木工程师",
    "bank teller": "银行职员", "donor": "捐助人", "founder": "创立者", "benefactor": "慈善家",
    "philanthropist": "慈善家", "association football player": "足球运动员",
    "cricketer": "板球运动员", "estate agent": "地产经纪人",
}


def occ_str(p):
    props = ((p.get("page") or {}).get("occupation")) or []
    unique = list(dict.fromkeys(str(o).strip() for o in props if o and str(o).strip()))
    out = [OCC_ZH.get(o, o) for o in unique[:3]]
    return " · ".join(out) if out else "作家"


def age_str(p):
    pg = p.get("page") or {}
    y1 = (pg.get("dob") or "")[:4]
    if re.match(r"^\d{4}$", y1):
        return "约%d岁" % (p["year"] - int(y1))
    return ""


# ---------------- tex 生成 ----------------
HEADER = r"""% Nobel Literature Video — Allinone
% 诺贝尔文学奖全得主合集（1901–2025）
% Beamer layout mirrors physicist/video/episode-allinone
% Source: literature/presentations 名录 + 离线页面 metadata.json + Wikipedia images
\documentclass[aspectratio=169,14pt]{beamer}
\usetheme{default}\usecolortheme{default}
\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{footline}{\hfill{\scriptsize\color{covermuted}\insertframenumber/\inserttotalframenumber}\hspace{0.4cm}\vspace{0.15cm}}
\usepackage{fontspec}\usepackage{xeCJK}
\setCJKmainfont{PingFang SC}[BoldFont=PingFang SC Semibold]
\xeCJKDeclareCharClass{CJK}{"0370 -> "03FF}
% 希腊字母（μ τ 等）走中文字体，避免 lmsans8 缺字被静默丢弃
\setmainfont{Helvetica Neue}[BoldFont=Helvetica Neue Bold]
\usepackage{xcolor}\usepackage{tikz}\usepackage{graphicx}\usepackage{adjustbox}\usepackage{fontawesome5}\usepackage{ifthen}\usepackage{amssymb}
\usetikzlibrary{positioning,calc,arrows.meta,shadows}

% ===== 配色：酒红 + 墨绿 + 金褐（文学主题，区别于物理学深空蓝/图灵紫/菲尔兹金）=====
\definecolor{bgmain}{RGB}{249,246,240}
\definecolor{coverprimary}{HTML}{6B2737}
\definecolor{coveraccent}{HTML}{1F5C4D}
\definecolor{coveramber}{HTML}{A8762A}
\definecolor{coverpurple}{HTML}{3C4A6B}
\definecolor{coverdark}{HTML}{241A1E}
\definecolor{covermuted}{HTML}{6E6259}
\definecolor{coverlight}{HTML}{EFE7DA}
\definecolor{DeepPurpleAccent}{HTML}{4A148C}
\definecolor{titlecolor}{RGB}{36,26,30}
\definecolor{muteddark}{RGB}{104,94,86}
\definecolor{bluepanel}{RGB}{226,234,228}
\definecolor{redpanel}{RGB}{246,228,224}
\definecolor{goldpanel}{RGB}{247,240,219}
\definecolor{purplepanel}{RGB}{224,229,238}
\definecolor{graypanel}{RGB}{238,240,244}
\setbeamercolor{background canvas}{bg=bgmain}

\providecommand{\personhonors}{}
\newcounter{pmark}%
\newcommand{\recordcount}{RECORDCOUNT}
\newcommand{\personcount}{PERSONCOUNT}
\newcommand{\awardyearcount}{AWARDYEARCOUNT}
\newcommand{\twentiethrecordcount}{TWENTIETHRECORDCOUNT}
\newcommand{\twentyfirstrecordcount}{TWENTYFIRSTRECORDCOUNT}
% ---- 双料与大满贯页：居中标题模板（源自 turing allinone）----
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
\colorlet{wolfclr}{coverprimary}
\colorlet{btclr}{coverpurple}
\colorlet{shawclr}{coveramber}
\colorlet{crafoordclr}{coveraccent}
\colorlet{japanclr}{coveraccent!75}
\colorlet{chemclr}{coverpurple!80}
\colorlet{medclr}{coveraccent!80}
\colorlet{econclr}{coverprimary!70}
\colorlet{peaceclr}{coveramber!75}
\colorlet{turingclr2}{coverprimary!80}
\colorlet{millclr}{covermuted}

% 交叉奖项徽标：★W 沃尔夫物理学奖 · ▲T 图灵奖
\newcommand{\wolfbadge}{\raisebox{0.55ex}{\tiny\color{coveramber}$\bigstar$\kern-0.5pt W}}
\newcommand{\turingbadge}{\raisebox{0.55ex}{\tiny\color{coverpurple}$\blacktriangle$\kern-0.5pt T}}
% --- 数据库直查顶级交叉奖项徽标 ---
\newcommand{\nobelchembadge}{\raisebox{0.55ex}{\tiny\color{coveramber}$\clubsuit$\kern-0.5pt C}}
\newcommand{\nobelmedbadge}{\raisebox{0.55ex}{\tiny\color{coveraccent}$\clubsuit$\kern-0.5pt M}}
\newcommand{\nobellitbadge}{\raisebox{0.55ex}{\tiny\color{coverpurple}$\clubsuit$\kern-0.5pt L}}
\newcommand{\nobeleconbadge}{\raisebox{0.55ex}{\tiny\color{coverprimary}$\clubsuit$\kern-0.5pt E}}
\newcommand{\nobelpeacebadge}{\raisebox{0.55ex}{\tiny\color{coveramber}$\clubsuit$\kern-0.5pt P}}
\newcommand{\fieldsbadge}{\raisebox{0.55ex}{\tiny\color{coveramber}$\bigstar$\kern-0.5pt F}}
\newcommand{\abelbadge}{\raisebox{0.55ex}{\tiny\color{coveraccent}$\bigstar$\kern-0.5pt A}}
\newcommand{\wolfmathbadge}{\raisebox{0.55ex}{\tiny\color{coveramber}$\bigstar$\kern-0.5pt M}}
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
      {\fontsize{7}{8.5}\selectfont\bfseries\color{coverprimary!70!black} 职业}\enspace{\fontsize{7}{8.5}\selectfont\color{coverdark!85} #8}
    };
  \end{tikzpicture}
\end{column}
\begin{column}{0.38\textwidth}
  \begin{tikzpicture}
    \node[draw=coverprimary!35, fill=bluepanel, rounded corners=5pt, inner sep=7pt, text width=3.8cm, align=left] {
      {\fontsize{8.2}{10}\selectfont\bfseries\color{coverprimary!82!black} 核心贡献}\par\vspace{3pt}
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
    year_str = "%d 年（获奖时 %s 岁）" % (p["year"], age) if age else "%d 年" % p["year"]
    contrib = esc(p["citation"])
    return ("\\newcommand{\\%s}{\\gdef\\personhonors{%s}\\gdef\\personbookmark{%d · %s %s}\\personslide\n"
            "  {%s}{%s}\n"
            "  {%s}{%s}\n"
            "  {%s}{%s}{%s}{%s}\n"
            "  {%s}}\n" % (
                p["slug"], p["honors_tex"],
                p["year"], esc(p["name"]), esc(p["zh"] or ""),
                esc(p["name"]) + (p["badges_tex"] or ""), esc(p["zh"] or p["name"]),
                img, credit,
                esc(year_str), esc(life_str(p)), esc(country_zh(p["country"])), esc(occ_str(p)),
                contrib))


# ---------- 交叉身份总览页（参考 turing allinone 双料与大满贯页） ----------
SUMMARY_ROWS = [  # (row_key, badge, 显示名, 合并的 (badge,label) 集合)
    ("wolf",  "\\wolfbadge",      "沃尔夫物理学奖", {("Wolf Prize in Physics",)}),
    ("bt",    "\\btphysbadge",    "基础物理学突破奖（含特别）", {("Breakthrough Prize",), ("Breakthrough Prize in Fundamental Physics",), ("Special Breakthrough Prize in Fundamental Physics",)}),
]


def build_summary_rows(people):
    """按奖项聚合：返回 [(badge, label, count, [按年排序的姓氏], note)]。"""
    merge = {"突破奖": "bt", "基础物理学突破奖": "bt", "特别基础物理学突破奖": "bt"}
    meta = {
        "wolf": ("\\wolfbadge", "沃尔夫物理学奖", ""),
        "bt": ("\\btphysbadge", "基础物理学突破奖", "含特别"),
        "shaw": ("\\shawbadge", "邵逸夫奖", ""),
        "crafoord": ("\\crafoordbadge", "克拉福德奖", ""),
        "japan": ("\\japanbadge", "日本国际奖", ""),
        "chem": ("\\nobelchembadge", "诺贝尔化学奖", ""),
        "med": ("\\nobelmedbadge", "诺贝尔生理学或医学奖", ""),
        "econ": ("\\nobeleconbadge", "诺贝尔经济学奖", ""),
        "peace": ("\\nobelpeacebadge", "诺贝尔和平奖", ""),
        "turing": ("\\turingbadge", "图灵奖", ""),
        "mill": ("\\millenniumbadge", "千禧科技奖", ""),
    }
    cats = {}
    for p in people:
        for badge, label, yr in (p.get("cross_items") or []):
            key = merge.get(label, {"沃尔夫物理学奖": "wolf", "邵逸夫奖": "shaw",
                                    "克拉福德奖": "crafoord", "日本国际奖": "japan",
                                    "诺贝尔化学奖": "chem", "诺贝尔生理学或医学奖": "med",
                                    "诺贝尔经济学奖": "econ", "诺贝尔和平奖": "peace",
                                    "图灵奖": "turing",
                                    "千禧科技奖": "mill"}.get(label))
            if not key:
                continue
            cats.setdefault(key, {})[(p["name"], yr)] = badge
    rows = []
    for key in ["wolf", "bt", "shaw", "crafoord", "japan", "chem", "med", "econ", "peace", "turing", "mill"]:
        if key not in cats:
            continue
        badge, label, note = meta[key]
        entries = sorted(cats[key].items(), key=lambda kv: (kv[0][1] or "9999", kv[0][0]))
        surnames = []
        for (n, y), b in entries:
            toks = n.replace("-", " ").replace("'", " ").split()
            if toks[-1] == "Jr":
                surnames.append(toks[-2] + " Jr.")
            elif toks[-2:] == ["de", "Gennes"] or toks[-2:] == ["von", "Laue"] or toks[-2:] == ["der", "Waals"]:
                surnames.append(" ".join(toks[-2:]))
            else:
                surnames.append(toks[-1])
        rows.append((badge, label, len(entries), surnames, note))
    return rows


def cross_summary_slide(rows):
    """turing 双料与大满贯页同款：纯色 chip + text=col!70!black + 0.55 等距行。"""
    chip_style = {
        "沃尔夫物理学奖": ("$\\bigstar$", "wolfclr"),
        "基础物理学突破奖": ("$\\bigstar$", "btclr"),
        "邵逸夫奖": ("$\\blacklozenge$", "shawclr"),
        "克拉福德奖": ("$\\diamond$", "crafoordclr"),
        "日本国际奖": ("$\\heartsuit$", "japanclr"),
        "诺贝尔化学奖": ("$\\clubsuit$", "chemclr"),
        "诺贝尔生理学或医学奖": ("$\\clubsuit$", "medclr"),
        "诺贝尔经济学奖": ("$\\clubsuit$", "econclr"),
        "诺贝尔和平奖": ("$\\clubsuit$", "peaceclr"),
        "图灵奖": ("$\\blacktriangle$", "turingclr2"),
        "千禧科技奖": ("$\\blacklozenge$", "millclr"),
    }

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
        "    at (-3.60,%.2f) {首届\\;\\; Sully Prudhomme\\;(1901)};\n"
        % (bar_bot, bar_top, bar_top - 0.10))
    nodes.append(
        "  \\node[anchor=north, text width=3.7cm, align=center,\n"
        "        font=\\fontsize{4.5}{5.5}\\selectfont\\bfseries, text=coverprimary]\n"
        "    at (0.00,%.2f) {\\awardyearcount 届\\;\\; \\recordcount 条记录 / \\personcount 位独立得主};\n"
        "  \\node[anchor=north, text width=3.7cm, align=center,\n"
        "        font=\\fontsize{4.5}{5.5}\\selectfont\\bfseries, text=coverprimary]\n"
        "    at (3.60,%.2f) {拒领\\;\\; Pasternak 1958 · Sartre 1964};\n"
        % (bar_top - 0.10, bar_top - 0.10))
    body = "\n".join(nodes)
    return ('''\\begin{frame}{双料与大满贯 · 诺贝尔文学奖得主身份总览}
\\pdfbookmark[1]{双料与大满贯 · 交叉身份总览}{crosssummary}
\\vspace{-4pt}
\\centering
\\begin{tikzpicture}
'''+body+r'''
\end{tikzpicture}
\end{frame}

''')


def make_cover(people):
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
    tagline = "从 %s 到 %s · 世界文学群像与跨奖交叉得主一览" % (people[0]["name"], people[-1]["name"])
    tex = r'''\newcommand{\coverslide}{%%
\begin{frame}[plain]
\pdfbookmark[1]{封面 · 诺贝尔文学奖 1901–2025}{cover}
\begin{tikzpicture}[remember picture, overlay]
  \fill[coverprimary!6] (current page.north west) rectangle (current page.south east);
  \fill[coveraccent!10] (current page.south east) ++(-2.3,-1.7) circle (2.0cm);
  \fill[coveramber!14] (current page.north east) ++(-2.4,1.4) circle (1.2cm);
  \fill[coverpurple!10] (current page.north west) ++(3.0,-1.0) circle (0.9cm);
  \node[anchor=center, font=\fontsize{17}{22}\selectfont\bfseries, text=coverdark]
    at ([yshift=3.35cm]current page.center) {诺贝尔文学奖：文字的百年回声（1901–2025）};
  \node[anchor=center, font=\fontsize{12}{15}\selectfont, text=coverprimary!85!black]
    at ([yshift=2.50cm]current page.center) {Nobel Prize in Literature · \recordcount 条记录 / \personcount 位得主};
  \draw[coverprimary, line width=1.4pt] ([yshift=1.90cm, xshift=-5.2cm]current page.center)
    -- ([yshift=1.90cm, xshift=5.2cm]current page.center);
  \node[anchor=center, font=\fontsize{9.5}{12.5}\selectfont\bfseries, text=coveramber!58!black]
    at ([yshift=1.58cm]current page.center) {TAGLINE};
''' + grid_tikz + r'''
  \node[anchor=center, font=\fontsize{10}{12}\selectfont\bfseries, text=DeepPurpleAccent]
    at ([yshift=1.12cm]current page.center) {\faIcon{medal}\enspace Nobel Prize in Literature\enspace|\enspace 1901–2025 · 全 \personcount 位得主};
\end{tikzpicture}
\end{frame}
}
'''
    return tex.replace("TAGLINE", tagline)


def intro_slide(legend_lines, stats, missing_years):
    legend_tex = " \\\\\r\n    ".join(legend_lines)
    scale_txt = ("1901 年首颁（Sully Prudhomme）；至 2025 年共评奖 %d 个年份、%d 条记录，"
                 "涉及 %d 位独立作家。1904 年曾由 Frédéric Mistral 与 José Echegaray 两人共享，"
                 "为文学奖史上唯一一次。"
                 % (stats["award_years"], stats["records"], stats["unique_people"]))
    decline_txt = ("Boris Pasternak（1958）与 Jean-Paul Sartre（1964）婉拒领奖；"
                   "Erik Axel Karlfeldt（1931）为身后追授。")
    if missing_years:
        gap_txt = ("%d 个年份未颁奖（%s），遵循遗嘱「宁缺毋滥」。"
                   % (len(missing_years), " · ".join(str(y) for y in missing_years)))
    else:
        gap_txt = "本统计区间内每个年份均有颁奖。"
    if legend_lines:
        legend_node = r'''  \node[draw=coverpurple!40, fill=purplepanel, rounded corners=5pt, inner sep=7pt, text width=7.6cm, align=left, anchor=north west] at (0.30,3.05) {%%
    {\fontsize{8}{9.5}\selectfont\bfseries\color{coverpurple!82!black} 交叉荣誉 · 徽标一览}\par\vspace{3pt}
    {\fontsize{6.6}{12.8}\selectfont\color{coverdark!84} LEGENDPLACEHOLDER}};
'''
    else:
        legend_node = r'''  \node[draw=coverpurple!40, fill=purplepanel, rounded corners=5pt, inner sep=7pt, text width=7.6cm, align=left, anchor=north west] at (0.30,3.05) {%%
    {\fontsize{8}{9.5}\selectfont\bfseries\color{coverpurple!82!black} 从普吕多姆到克拉斯诺霍尔卡伊}\par\vspace{3pt}
    {\fontsize{7}{9}\selectfont\color{coverdark!84} 诗歌、小说、戏剧与歌词：文学奖的年轮横跨一个多世纪，\\授予「在文学领域创作出具有理想倾向的最佳作品的人」。}};
'''
    tex = r'''\newcommand{\introslide}{%%
\begin{frame}
\pdfbookmark[1]{认识诺贝尔文学奖}{intro}
\plainbar
\sectiontitle{认识诺贝尔文学奖}{Nobel Prize in Literature · 1901–2025}
\vspace{0.05cm}
\begin{center}
\begin{tikzpicture}
  \node[draw=coverprimary!40, fill=bluepanel, rounded corners=5pt, inner sep=7pt, text width=6.4cm, align=left, anchor=north west] at (-7.05,3.05) {%%
    {\fontsize{8}{9.5}\selectfont\bfseries\color{coverprimary!82!black} 规模}\\[2pt]
    {\fontsize{7}{8.5}\selectfont\color{coverdark!84} SCALETXT}};
  \node[draw=coveraccent!40, fill=redpanel, rounded corners=5pt, inner sep=7pt, text width=6.4cm, align=left, anchor=north west] at (-7.05,1.10) {%%
    {\fontsize{8}{9.5}\selectfont\bfseries\color{coveraccent!82!black} 拒领与追授}\\[2pt]
    {\fontsize{7}{8.5}\selectfont\color{coverdark!84} DECLINETXT}};
  \node[draw=coveramber!45, fill=goldpanel, rounded corners=5pt, inner sep=7pt, text width=6.4cm, align=left, anchor=north west] at (-7.05,-0.85) {%%
    {\fontsize{8}{9.5}\selectfont\bfseries\color{coveramber!70!black} 空缺年份}\\[2pt]
    {\fontsize{7}{8.5}\selectfont\color{coverdark!84} GAPTXT}};
''' + legend_node + r'''\end{tikzpicture}
\end{center}
\end{frame}
}
'''
    return (tex.replace("LEGENDPLACEHOLDER", legend_tex)
               .replace("SCALETXT", esc(scale_txt))
               .replace("DECLINETXT", esc(decline_txt))
               .replace("GAPTXT", esc(gap_txt)))


def section_slide(name, sub, note):
    return ('\\newcommand{\\%s}{\\sectionpageslide\n'
            '  {%s}\n  {%s}\n  {%s}\n'
            '  {Nobel Prize in Literature · 1901–2025}\n}\n' % (name, sub, note, ""))


def ending_slide():
    return (r"""\newcommand{\closingslide}{%
\begin{frame}[plain]
\begin{tikzpicture}[remember picture, overlay]
  \fill[coverprimary!7] (current page.north west) rectangle (current page.south east);
\pdfbookmark[1]{结语}{ending}
  \fill[coveramber!12] (current page.north east) ++(-2.4,1.4) circle (1.6cm);
  \fill[coverpurple!10] (current page.south west) ++(3.0,-1.0) circle (1.2cm);
  \node[anchor=center, font=\fontsize{22}{28}\selectfont\bfseries, text=coverdark]
    at ([yshift=1.10cm]current page.center) {文字不朽，思想长明};
  \draw[coveramber, line width=1.4pt] ([yshift=0.15cm, xshift=-4.6cm]current page.center)
    -- ([yshift=0.15cm, xshift=4.6cm]current page.center);
  \node[anchor=center, font=\fontsize{10.5}{14}\selectfont, text=coverprimary!85!black]
    at ([yshift=-0.75cm]current page.center) {谨以此片致敬 1901–2025 全部 \personcount 位独立诺贝尔文学奖得主};
  \node[anchor=center, font=\fontsize{8.5}{11.5}\selectfont\itshape, text=covermuted]
    at ([yshift=-1.70cm]current page.center) {他们的每一次书写，都在为人类留下共同的记忆。};
  \node[anchor=south, font=\scriptsize, text=coverdark!40]
    at ([yshift=0.38cm]current page.south) {\faIcon{medal}\enspace Nobel Prize in Literature · 1901–2025};
\end{tikzpicture}
\end{frame}
}
""")


def write_missing_md(people):
    missing = [p for p in people if not p["img_file"]]
    lines = ["# Nobel Literature Video Series — Missing Portrait Checklist", "",
             "> Source: `literature/presentations/pages/{20th,21st}_century/<Dir>/images.txt`（自动下载 %s）" % "2026-09-30",
             "> 共 %d 位得主中 **%d 位** 缺真人肖像，待人工补图。" % (len(people), len(missing)), "",
             "## 缺照片得主", "",
             "| 年份 | 得主 | 占位文件 | 页面目录 | 备注 |",
             "|---|---|---|---|---|"]
    for p in missing:
        d = (p.get("page") or {}).get("dir", "—")
        reason = BLOCK_IMAGES.get(p["name"], "images.txt 无匹配人像（已过滤旗帜/签名/图标），或候选图下载失败")
        lines.append("| %d | %s | `episode-allinone/images/%s.jpg` | `%s` | %s |"
                     % (p["year"], p["name"], p["slug"], os.path.relpath(d, PRES), reason))
    lines += ["",
              "## 如何补图", "",
              "1. 从 Wikipedia Commons / 官方主页 / Nobel 官网下载真人肖像（建议宽 ≥ 250px）。"
              "亦可把人工校准图放入 `literature/video/episode-allinone/figures/`（文件名为人物英文名，如 `Albert Camus.jpg`，优先级最高）。",
              "2. 保存为 `.jpg`（首选）/`.jpeg`/`.png`/`.webp`，命名与下表占位文件同名（扩展名可不同），放入 `literature/video/episode-allinone/images/`。",
              "3. 重新运行 `python3 gen_literature.py`（自动检测非空文件并使用），再 `make pdf && make video`。", "",
              "## 当前状态", "",
              "- 总得主：**%d 位**（1901–2025）" % len(people),
              "- 真人肖像在位：**%d 位**" % (len(people) - len(missing)),
              "- 缺肖像（占位）：**%d 位**" % len(missing)]
    with open(os.path.join(VID, "missing_photos.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print("missing_photos.md: %d missing / %d total" % (len(missing), len(people)))


MAKEFILE = r"""# Makefile for Nobel Literature allinone video.
MAIN        = literature_allinone_zh
VIDEO_NAME  = literature_allinone_zh
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
    print("laureates: %d, page dirs: %d" % (len(people), len(pages)))
    unmatched = []
    for p in people:
        pg = match_page(p, pages)
        p["page"] = pg
        if not pg:
            unmatched.append(p["name"])
    if unmatched:
        print("WARN unmatched page dirs (%d): %s" % (len(unmatched), ", ".join(unmatched[:10])))
    db_ok = build_db_cross(people)
    for p in people:
        p["honors_tex"] = cross_tex(p, db_ok)
        p["badges_tex"] = p["badges_str"]
    n_img = sync_all(people, pages)
    print("portraits in place: %d / %d" % (n_img, len(people)))
    write_missing_md(people)

    os.makedirs(EP, exist_ok=True)
    stats = doc_stats(people)
    years_awarded = {p["year"] for p in people}
    missing_years = [y for y in range(1901, 2026) if y not in years_awarded]
    hdr = (HEADER
           .replace("RECORDCOUNT", str(stats["records"]))
           .replace("PERSONCOUNT", str(stats["unique_people"]))
           .replace("AWARDYEARCOUNT", str(stats["award_years"]))
           .replace("TWENTIETHRECORDCOUNT", str(stats["20th_records"]))
           .replace("TWENTYFIRSTRECORDCOUNT", str(stats["21st_records"])))
    out = [hdr]
    out.append(make_cover(people))
    # 徽标图例：按 TOP_AWARDS 顺序收集本片涉及的 (badge,label) 及人次
    legend_lines = []
    for aid, (badge, label) in TOP_AWARDS.items():
        cnt = sum(1 for q in people for it in (q.get("cross_items") or []) if it[0] == badge and it[1] == label)
        if cnt:
            legend_lines.append("%s{} %s · %d 位" % (badge, label, cnt))
    out.append(intro_slide(legend_lines, stats, missing_years))
    summary_rows = build_summary_rows(people)
    summary_tex = cross_summary_slide(summary_rows) if summary_rows else ""
    out.append(section_slide("twentiethslide",
                             "第一乐章 · 20 世纪（1901–2000）",
                             "从普吕多姆到格拉斯 · %d 条记录" % stats["20th_records"]))
    out.append(section_slide("twentyfirstslide",
                             "第二乐章 · 21 世纪（2001–2025）",
                             "从奈保尔到克拉斯诺霍尔卡伊 · %d 条记录" % stats["21st_records"]))
    out.append(ending_slide())
    out.append("\n% ========== SLIDES (chronological) ==========\n")
    for p in people:
        out.append(person_tex(p))
    out.append("\n% ========== MAIN ==========\n\\begin{document}\n")
    out.append("\\coverslide\n\\introslide\n")
    body = [summary_tex]
    cur = None
    for p in people:
        if p["century"] != cur:
            cur = p["century"]
            body.append("\\%sslide" % ("twentieth" if cur == "20th" else "twentyfirst"))
        body.append("\\%s" % p["slug"])
    out.append("\n".join(body) + "\n")
    out.append("\\closingslide\n\\end{document}\n")
    tex = os.path.join(EP, MAIN + ".tex")
    with open(tex, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print("wrote", tex)
    with open(os.path.join(EP, "Makefile"), "w", encoding="utf-8") as f:
        f.write(MAKEFILE)
    # BGM 软链（同 turing 约定）
    wav = os.path.join(EP, "awaken.wav")
    if not os.path.lexists(wav):
        os.symlink("../../../music_audio/bgm.wav", wav)


if __name__ == "__main__":
    main()
