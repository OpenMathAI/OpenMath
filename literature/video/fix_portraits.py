#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""对 REST/抓图得到非人像的得主，从 Wikimedia Commons 搜索人像补图。

写入 figures/<Name>.jpg（figures 优先级最高），并删除 images/ 旧文件。
候选过滤：排除纪念碑/雕像/铭牌/房屋/旗帜/签名/图标等。
"""
import io
import json
import os
import re
import subprocess
import sys
import time
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_literature as g

UA = g.UA
BAD_WORDS = re.compile(
    r"monument|statue|grav|tomb|plaque|memorial|house|museum|building|street|avenue|"
    r"school|library|theatre|theater|stamp|coin|banknote|award|medal|certificate|"
    r"diploma|letter|document|manuscript|book|cover|signature|flag|logo|icon|map|"
    r"signature|bust|crowd|funeral|wedding|group|with (his |her )?wife|and wife|"
    r"\.svg|\.pdf|\.djvu|\.ogg", re.I)

# name -> (搜索词列表)
TARGETS = {
    "Jacinto Benavente": ["Jacinto Benavente retrato", "Jacinto Benavente portrait", "Jacinto Benavente"],
    "William Butler Yeats": ["W.B. Yeats portrait", "William Butler Yeats portrait", "William Butler Yeats 1911"],
    "Grazia Deledda": ["Grazia Deledda ritratto", "Grazia Deledda portrait", "Grazia Deledda"],
    "Thomas Mann": ["Thomas Mann portrait", "Thomas Mann 1929", "Thomas Mann"],
    "Sinclair Lewis": ["Sinclair Lewis portrait", "Sinclair Lewis 1930"],
    "Pearl S. Buck": ["Pearl Buck portrait", "Pearl S. Buck 1972", "Pearl Buck"],
    "François Mauriac": ["François Mauriac portrait", "François Mauriac"],
    "Winston Churchill": ["Winston Churchill Karsh", "Winston Churchill 1941 portrait", "Sir Winston Churchill portrait"],
    "Juan Ramón Jiménez": ["Juan Ramón Jiménez retrato", "Juan Ramón Jiménez portrait", "Juan Ramón Jiménez"],
    "Albert Camus": ["Albert Camus portrait", "Albert Camus 1957", "Albert Camus"],
}


def commons_search(q, limit=8):
    url = ("https://commons.wikimedia.org/w/api.php?action=query&list=search&srnamespace=6&format=json&srlimit=%d&srsearch=%s"
           % (limit, urllib.parse.quote(q)))
    r = subprocess.run(["curl", "-sL", "--max-time", "30", "-A", UA, url], capture_output=True)
    if r.returncode != 0 or not r.stdout:
        return []
    try:
        return [x["title"] for x in json.loads(r.stdout)["query"]["search"]]
    except Exception:
        return []


def thumb_url(title, width=500):
    url = ("https://commons.wikimedia.org/w/api.php?action=query&titles=%s&prop=imageinfo&iiprop=url&iiurlwidth=%d&format=json"
           % (urllib.parse.quote(title), width))
    r = subprocess.run(["curl", "-sL", "--max-time", "30", "-A", UA, url], capture_output=True)
    if r.returncode != 0 or not r.stdout:
        return None
    try:
        pages = json.loads(r.stdout)["query"]["pages"]
        info = list(pages.values())[0].get("imageinfo") or [{}]
        return info[0].get("thumburl")
    except Exception:
        return None


def probe(data):
    ok, ext, ratio = g.img_probe(data, 15000)
    return (ok, ext, ratio) if ok else (False, "", 0)


def main():
    figdir = g.FIGURES_DIR
    os.makedirs(figdir, exist_ok=True)
    done, skipped = [], {}
    for name, queries in TARGETS.items():
        if g.find_figure(name):
            skipped[name] = "figures 已有"
            continue
        got = None
        for q in queries:
            if got:
                break
            time.sleep(1.0)
            for title in commons_search(q):
                fname = title.replace("File:", "")
                if BAD_WORDS.search(fname) or g.BAD_FILE.search(fname):
                    continue
                # 文件名应含姓氏，避免同名街道等漏网
                surname = name.split()[-1]
                if ascii_fold(surname).lower() not in ascii_fold(fname).lower():
                    continue
                time.sleep(1.0)
                tu = thumb_url(title)
                data = g.curl(tu, tries=2) if tu else None
                if not data and tu:
                    data = g.curl("https://wsrv.nl/?url=" + tu.split("https://", 1)[1].split("?utm")[0] + "&w=700", tries=2)
                if not data:
                    continue
                ok, ext, ratio = probe(data)
                if not ok or not (0.45 <= ratio <= 1.3):
                    continue
                dst = os.path.join(figdir, "%s.%s" % (name, ext))
                with open(dst, "wb") as f:
                    f.write(data)
                got = dst
                break
        if got:
            done.append("%s -> %s" % (name, os.path.basename(got)))
        else:
            skipped[name] = "无合格候选"
    print("done %d" % len(done))
    for d in done:
        print("  +", d)
    for k, v in skipped.items():
        print("  ! %s: %s" % (k, v))


def ascii_fold(s):
    import unicodedata
    s = unicodedata.normalize("NFKD", str(s))
    return "".join(c for c in s if not unicodedata.combining(c))


if __name__ == "__main__":
    main()
