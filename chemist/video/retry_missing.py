#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Retry missing portraits for chemist allinone via wsrv.nl proxy (bypass 429).

upload.wikimedia.org 429 限流时的兜底：wsrv.nl 图片代理。
用法：cd chemist/video && python3 retry_missing.py
补齐后重跑 gen_chemist.py 即可自动检测并使用。
"""
import io
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse

VID = os.path.dirname(os.path.abspath(__file__))
PRES = os.path.normpath(os.path.join(VID, "..", "presentations"))
EP = os.path.join(VID, "episode-allinone")
IMGDIR = os.path.join(EP, "images")
MISSING_MD = os.path.join(VID, "missing_photos.md")

LISTS = [
    (os.path.join(PRES, "20th_century", "OpenChemist_20th_Century_Nobel_Laureates.md"),
     os.path.join(PRES, "20th_century", "pages")),
    (os.path.join(PRES, "21th_century", "OpenChemist_21th_Century_Nobel_Laureates.md"),
     os.path.join(PRES, "21th_century", "pages")),
]

UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")
BAD_FILE = re.compile(r"flag|signature|question_book|map[_\-\. ]|icon|logo|seal|\.svg|\.gif|\.ogg|wiki", re.I)


def ascii_fold(s):
    s = __import__("unicodedata").normalize("NFKD", str(s))
    return "".join(c for c in s if not __import__("unicodedata").combining(c))


def tokens(s):
    return [t.lower() for t in re.split(r"[^A-Za-z]+", ascii_fold(s)) if len(t) > 1]


def slug_of(name):
    return re.sub(r"[^a-z]", "", ascii_fold(name).lower())


def curl(url, tries=2, timeout=45):
    for k in range(tries):
        try:
            r = subprocess.run(["curl", "-sLf", "--max-time", str(timeout), "-A", UA, url],
                               capture_output=True)
            if r.returncode == 0 and r.stdout:
                return r.stdout
        except Exception:
            pass
        time.sleep(0.8 + k)
    return None


def wsrv(url, width=700):
    u = url.split("?")[0]
    return "https://wsrv.nl/?url=" + urllib.parse.quote(u[len("https://"):], safe="") + "&w=%d" % width


def probe(data, min_size=8000):
    if not data or len(data) < min_size:
        return None
    if data[:2] == b"\xff\xd8":
        ext = "jpg"
    elif data[:8] == b"\x89PNG\r\n\x1a\n":
        ext = "png"
    else:
        return None
    try:
        from PIL import Image
        im = Image.open(io.BytesIO(data))
        return ext, im.width / max(im.height, 1)
    except Exception:
        return ext, 0.8


def save(data, base, tier1):
    pr = probe(data)
    if not pr:
        return None
    ext, ratio = pr
    if not tier1 and not (0.45 <= ratio <= 1.25):
        return None
    if ratio > 2.5:
        return None
    fn = "%s.%s" % (base, ext)
    # JFIF density 1x1 会致 xelatex "Dimension too large"，统一归一 72dpi
    path = os.path.join(IMGDIR, fn)
    with open(path, "wb") as f:
        f.write(data)
    subprocess.run(["sips", "-s", "dpiHeight", "72", "-s", "dpiWidth", "72", path],
                   capture_output=True)
    return fn


def candidates(images_txt, name):
    out = []
    if not os.path.isfile(images_txt):
        return out
    pt = set(tokens(name))
    surname = tokens(name)[-1] if tokens(name) else ""
    for line in open(images_txt, encoding="utf-8"):
        u = line.strip()
        if not u.startswith("http"):
            continue
        fname = urllib.parse.unquote(u.split("/")[-1].split("?")[0])
        if BAD_FILE.search(fname):
            continue
        m = re.search(r"/(\d{2,4})px-", u)
        w = int(m.group(1)) if m else 500
        ft = set(tokens(fname))
        overlap = pt & ft
        tier1 = bool(overlap) or (surname and surname in fname.lower())
        score = (20 if tier1 else 0) + 8 * len(overlap) + w / 500.0
        big = re.sub(r"/(\d{2,4})px-", "/500px-", u)
        out.append((score, tier1, big))
    out.sort(reverse=True)
    return out


def missing_names():
    names = []
    for line in open(MISSING_MD, encoding="utf-8"):
        m = re.match(r"^\| \d{4} \| (.+?) \| `episode-allinone/images/([a-z]+)\.jpg` \| `(.+?)` \|", line.strip())
        if m:
            names.append((m.group(1), m.group(3)))
    return names


def main():
    os.makedirs(IMGDIR, exist_ok=True)
    todo = missing_names()
    print("retry targets:", len(todo))
    ok = 0
    for i, (name, page_rel) in enumerate(todo):
        base = slug_of(name) or "laureate"
        for ext in ("jpg", "jpeg", "png", "webp"):
            p = os.path.join(IMGDIR, base + "." + ext)
            if os.path.exists(p) and os.path.getsize(p) > 0:
                break
        else:
            got = fetch_one(name, os.path.join(PRES, page_rel), base)
            if got:
                ok += 1
                print("[%d/%d] %s -> %s" % (i + 1, len(todo), name, got))
            else:
                print("[%d/%d] %s -> STILL MISSING" % (i + 1, len(todo), name))
        time.sleep(0.3)
    print("recovered:", ok)


def fetch_one(name, page_dir, base):
    urls = candidates(os.path.join(page_dir, "images.txt"), name)
    tried = 0
    for score, tier1, u in urls:
        if tried >= 5:
            break
        for cand in (u, wsrv(u)):
            tried += 1 if cand == u else 0
            data = curl(cand)
            if data:
                fn = save(data, base, tier1)
                if fn:
                    return fn
            time.sleep(0.2)
    # REST summary thumbnail 经代理
    t = urllib.parse.quote(name.replace(" ", "_"), safe="")
    api = "https://en.wikipedia.org/api/rest_v1/page/summary/" + t
    r = subprocess.run(["curl", "-sLf", "--max-time", "30", "-A", UA, api], capture_output=True)
    if r.returncode == 0 and r.stdout:
        try:
            j = json.loads(r.stdout)
            th = (j.get("thumbnail") or {}).get("source") or ""
            if th:
                th = re.sub(r"/\d{2,4}px-", "/500px-", th)
                for cand in (th, wsrv(th)):
                    data = curl(cand)
                    if data:
                        fn = save(data, base, tier1=True)
                        if fn:
                            return fn
        except Exception:
            pass
    return None


if __name__ == "__main__":
    main()
