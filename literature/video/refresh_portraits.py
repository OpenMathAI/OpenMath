#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""用 Wikipedia 词条页首图（REST summary infobox）刷新全部头像。

- figures/ 人工校准图优先，跳过不覆盖；
- REST 抓取失败时保留现有文件（wsrv.nl 反代兜底一轮）；
- 新图成功时删除该 slug 的旧扩展名文件，避免残留。
"""
import os
import time
import gen_literature as g


def main():
    people = g.parse_lists()
    pages = g.load_page_index()
    for p in people:
        p["page"] = g.match_page(p, pages)
    used = set()
    for p in people:
        base = g.slug_of(p["name"]) or "laureate"
        while base in used:
            base += "x"
        used.add(base)
        p["slug"] = base
    os.makedirs(g.IMGDIR, exist_ok=True)
    updated, kept, failed = [], [], []
    for p in people:
        if g.find_figure(p["name"]):
            kept.append(p["name"] + " (figures)")
            continue
        if not p["page"]:
            failed.append(p["name"] + " (no page)")
            continue
        time.sleep(1.1)
        su = g.rest_summary_image(p["page"]["title"])
        data = g.curl(su, tries=2) if su else None
        if not data and su:
            data = g.curl("https://wsrv.nl/?url=" + su.split("https://", 1)[1].split("?utm")[0] + "&w=700", tries=2)
        dst_base = os.path.join(g.IMGDIR, p["slug"])
        fn = g.save_image(data, dst_base, tier1=True, max_ratio=2.5, min_size=1200) if data else None
        if fn:
            # 清掉旧扩展名残留
            for ext in ("jpg", "jpeg", "png", "webp"):
                old = dst_base + "." + ext
                if old != os.path.join(g.IMGDIR, fn) and os.path.exists(old):
                    os.remove(old)
            updated.append(p["name"])
        else:
            have = any(os.path.exists(dst_base + "." + ext) and
                       os.path.getsize(dst_base + "." + ext) > 0
                       for ext in ("jpg", "jpeg", "png", "webp"))
            (kept if have else failed).append(p["name"] + ("" if have else " (MISS)"))
    print("updated %d" % len(updated))
    print("kept %d" % len(kept))
    print("missing %d: %s" % (len(failed), ", ".join(failed)))


if __name__ == "__main__":
    main()
