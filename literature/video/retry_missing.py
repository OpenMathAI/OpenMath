#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""对 missing_photos.md 中缺席的肖像做一轮 REST summary 重试（幂等，只补缺失）。"""
import os
import gen_literature as g


def main():
    people = g.parse_lists()
    pages = g.load_page_index()
    for p in people:
        p["page"] = g.match_page(p, pages)
    # 与主脚本一致的 slug 分配
    used = set()
    for p in people:
        base = g.slug_of(p["name"]) or "laureate"
        while base in used:
            base += "x"
        used.add(base)
        p["slug"] = base
    os.makedirs(g.IMGDIR, exist_ok=True)
    got, still = [], []
    for p in people:
        have = any(os.path.exists(os.path.join(g.IMGDIR, p["slug"] + "." + ext)) and
                   os.path.getsize(os.path.join(g.IMGDIR, p["slug"] + "." + ext)) > 0
                   for ext in ("jpg", "jpeg", "png", "webp"))
        if have:
            continue
        if not p["page"]:
            still.append(p["name"])
            continue
        import time
        time.sleep(1.2)
        su = g.rest_summary_image(p["page"]["title"])
        data = g.curl(su, tries=3) if su else None
        if not data and su:
            # upload/thumb.wikimedia.org 429 时的 wsrv.nl 反代兜底
            import time
            time.sleep(1.5)
            data = g.curl("https://wsrv.nl/?url=" + su.split("https://", 1)[1].split("?utm")[0] + "&w=700", tries=2)
        fn = g.save_image(data, os.path.join(g.IMGDIR, p["slug"]), tier1=True,
                          max_ratio=2.5, min_size=1200) if data else None
        if fn:
            got.append("%s -> %s" % (p["name"], fn))
        else:
            # 兜底：images.txt 候选第一张
            cands = g.candidate_urls(p["page"])
            for _s, tier1, u in sorted(cands, reverse=True)[:3]:
                data = g.curl(u)
                fn = g.save_image(data, os.path.join(g.IMGDIR, p["slug"]), tier1=True,
                                  max_ratio=2.5, min_size=1200) if data else None
                if fn:
                    got.append("%s -> %s (images.txt)" % (p["name"], fn))
                    break
            else:
                still.append(p["name"])
    print("fetched %d:" % len(got))
    for line in got:
        print("  +", line)
    print("still missing %d: %s" % (len(still), ", ".join(still)))


if __name__ == "__main__":
    main()
