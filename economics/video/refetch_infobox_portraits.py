#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Re-download portraits from each laureate's Wikipedia entry page (infobox first image).

- 只替换 gen_economics.py 自动下载的头像；人工放置（git 新增/figures/覆盖）的跳过。
- 数据源：economics/presentations/pages/{20th_century,21th_century}/<Dir>/page.html 的
  `<td class="infobox-image">` 首个 <img>，250px 缩略图升级为 500px 下载。
- 校验：PIL 可开、尺寸合理、宽高比 0.4–1.4（近似人像），失败保留原图。

Run: cd economics/video && python3 refetch_infobox_portraits.py
"""
import os
import re
import sys
import shutil

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_economics as g

VID = os.path.dirname(os.path.abspath(__file__))
IMGDIR = os.path.join(VID, "episode-allinone", "images")

# 人工放置/覆盖过的头像（勿动）：git 新增 35 张 + 就地覆盖 3 张 + daletmortensen 手改
USER_MADE = {
    "abhijitbanerjee", "amartyasen", "benbernanke", "bengtholmstrom",
    "christopherapissarides", "christopherasims", "claudiagoldin", "clivegranger",
    "daronacemoglu", "davidcard", "douglasdiamond", "elinorostrom", "estherduflo",
    "georgestigler", "gerarddebreu", "harrymarkowitz", "jamesheckman", "jamesmeade",
    "jeantirole", "johnharsanyi", "josephstiglitz", "joshuaangrist", "mertonmiller",
    "oliverewilliamson", "paulmilgrom", "peterdiamond", "philiphdybvig",
    "ragnarfrisch", "robertbwilson", "robertjshiller", "simonjohnson",
    "theodoreschultz", "warthurlewis", "williamnordhaus", "williamvickrey",
    "edwardcprescott", "georgeakerlof", "johnforbesnashjr", "daletmortensen",
}

INFOBOX_IMG = re.compile(r'infobox-image[^>]*>\s*<[^>]*>?\s*(?:<a[^>]*>)?\s*<img[^>]+src="([^"]+)"', re.S)
FALLBACK_IMG = re.compile(r'<table[^>]+class="[^"]*infobox[^"]*"[^>]*>.*?<img[^>]+src="([^"]+)"', re.S)


def infobox_thumb(html):
    m = INFOBOX_IMG.search(html) or FALLBACK_IMG.search(html)
    if not m:
        return None
    src = m.group(1)
    if src.startswith("//"):
        src = "https:" + src
    return re.sub(r"/\d{2,4}px-", "/500px-", src)


def main():
    people = g.parse_lists()
    pages = g.load_page_index()
    ok = fail = skip = 0
    for p in people:
        slug = g.slug_of(p["name"])
        pg = g.match_page(p, pages)
        if slug in USER_MADE:
            skip += 1
            continue
        if not pg:
            fail += 1
            print("no-page %s" % slug)
            continue
        hp = os.path.join(pg["dir"], "page.html")
        if not os.path.isfile(hp):
            fail += 1
            print("no-html %s" % slug)
            continue
        try:
            html = open(hp, encoding="utf-8", errors="ignore").read()
        except Exception:
            fail += 1
            continue
        url = infobox_thumb(html)
        if not url:
            fail += 1
            print("no-infobox-img %s (%s)" % (slug, pg["dname"]))
            continue
        data = g.curl(url, tries=3)
        ok_img, ext, ratio = g.img_probe(data, min_size=3000)
        if not ok_img or not (0.4 <= ratio <= 1.4):
            fail += 1
            print("bad-image %s ratio=%.2f" % (slug, ratio))
            continue
        # 覆盖该 slug 的全部旧文件，统一写成探测出的扩展名
        for other in os.listdir(IMGDIR):
            if os.path.splitext(other)[0] == slug:
                os.remove(os.path.join(IMGDIR, other))
        with open(os.path.join(IMGDIR, "%s.%s" % (slug, ext)), "wb") as f:
            f.write(data)
        ok += 1
        print("ok %s -> %s.%s (ratio %.2f)" % (p["name"], slug, ext, ratio))
    print("done: ok=%d skip(user-made)=%d fail=%d" % (ok, skip, fail))


if __name__ == "__main__":
    main()
