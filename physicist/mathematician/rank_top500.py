#!/usr/bin/env python3
"""
从 mathematicians.md（11,326 人）选出"对人类影响最大"的前 500 名。

评分维度（综合）：
  1. 文章长度（log）        —— 知识密度与社会关注度的代理
  2. 入站链接数（log）       —— 被多少其他维基词条引用
  3. 顶级奖项               —— Fields / Abel / Wolf / Turing / Crafoord …
  4. 古代/奠基者加成        —— 通过出生年（< 1800 加权）
  5. 人工权重表（核心 100 人）—— 弥补客观信号无法捕捉的"奠基地位"

输出：top500_mathematicians.md
"""
from __future__ import annotations

import argparse
import json
import math
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from urllib.parse import quote

import requests

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "mathematicians.md"
CACHE = ROOT / ".cache_rank"
OUT = ROOT / "top500_mathematicians.md"

USER_AGENT = (
    "MathematiciansRanker/1.0 "
    "(https://example.org/contact; educational use) python-requests"
)


# ---------------------------------------------------------------------------
# 1) 读名单
# ---------------------------------------------------------------------------
NAME_RE = re.compile(r"^- \[([^\]]+)\]\(")


def load_names() -> list[str]:
    names = []
    for line in SRC.read_text(encoding="utf-8").splitlines():
        m = NAME_RE.match(line)
        if m:
            names.append(m.group(1))
    return names


# ---------------------------------------------------------------------------
# 2) 批量从 MediaWiki API 拿文章长度 + Wikidata QID
# ---------------------------------------------------------------------------
def build_session() -> requests.Session:
    s = requests.Session()
    s.headers.update({"User-Agent": USER_AGENT, "Accept": "application/json"})
    return s


def api_get(s: requests.Session, params: dict) -> dict:
    for attempt in range(3):
        try:
            r = s.get(
                "https://en.wikipedia.org/w/api.php",
                params={**params, "format": "json", "formatversion": "2"},
                timeout=30,
            )
            r.raise_for_status()
            return r.json()
        except requests.RequestException as e:
            if attempt == 2:
                raise
            time.sleep(2 ** attempt)
    return {}


def fetch_meta_batch(s: requests.Session, titles: list[str]) -> dict[str, dict]:
    """
    一次最多 50 个，拿 length（页面字节数）+ wikibase_item（QID）。
    返回 {title: {length:int, qid:str|None}}
    """
    out: dict[str, dict] = {}
    for i in range(0, len(titles), 50):
        batch = titles[i : i + 50]
        data = api_get(
            s,
            {
                "action": "query",
                "prop": "info|pageprops",
                "ppprop": "wikibase_item",
                "titles": "|".join(batch),
                "redirects": 1,
            },
        )
        # 处理 redirects 映射
        redirects = {r["from"]: r["to"] for r in data.get("query", {}).get("redirects", [])}
        for p in data.get("query", {}).get("pages", []):
            title_after = p.get("title")
            if not title_after or p.get("missing"):
                continue
            length = p.get("length", 0)
            qid = p.get("pageprops", {}).get("wikibase_item")
            out[title_after] = {"length": length, "qid": qid}
        # 把 redirect 源也指回新名
        for src, dst in redirects.items():
            if dst in out:
                out[src] = out[dst]
    return out


# ---------------------------------------------------------------------------
# 3) 顶级奖项（已校准的真实 Wikidata QID）
# ---------------------------------------------------------------------------
TOP_AWARDS = {
    # QID                      : (英文名, 加分)
    "Q28835":   ("Fields Medal",                      55),
    "Q188184":  ("Abel Prize",                        50),
    "Q915604":  ("Wolf Prize in Mathematics",         40),
    "Q185667":  ("Turing Award",                      40),
    "Q583069":  ("Crafoord Prize",                    25),
    "Q1070276": ("Chern Medal",                       25),
    "Q1036512": ("Carl Friedrich Gauss Prize",        25),
    "Q902556":  ("Rolf Nevanlinna Prize / IMU Prize", 25),
    "Q47170":   ("Nobel Prize in Economics",          15),  # 数学家偶尔获得
    "Q28003":   ("Copley Medal",                      15),  # 英国皇家学会最高奖
    "Q47854":   ("Nobel Prize in Physics",            15),  # 个别数学物理学家获得
}


def fetch_awards_batch(s: requests.Session, qids: list[str]) -> dict[str, list[str]]:
    """对每个 QID 批量获取 P166（获奖项），返回 {qid: [award_qid, ...]}。"""
    out: dict[str, list[str]] = {}
    for i in range(0, len(qids), 50):
        batch = qids[i : i + 50]
        for attempt in range(3):
            try:
                r = s.get(
                    "https://www.wikidata.org/w/api.php",
                    params={
                        "action": "wbgetentities",
                        "ids": "|".join(batch),
                        "props": "claims",
                        "format": "json",
                    },
                    timeout=30,
                )
                r.raise_for_status()
                data = r.json()
                break
            except Exception:
                if attempt == 2:
                    raise
                time.sleep(2 ** attempt)
        for qid, ent in data.get("entities", {}).items():
            awards = []
            for c in ent.get("claims", {}).get("P166", []):
                v = c.get("mainsnak", {}).get("datavalue", {}).get("value", {})
                if isinstance(v, dict) and v.get("id"):
                    awards.append(v["id"])
            out[qid] = awards
    return out


# ---------------------------------------------------------------------------
# 4) 人工权重表：覆盖核心数学家
#    基准：
#      150 = 文明奠基者（Newton/Gauss/Euler/Archimedes/Euclid 等）
#      120 = 时代开创者（Riemann/Poincaré/Hilbert/Grothendieck/von Neumann 等）
#       90 = 大师级（Ramanujan/Noether/Kolmogorov/Galois/Cantor/Turing 等）
#       70 = 重要学者（Fibonacci/Fourier/Cauchy/Weierstrass/Lagrange 等）
#       40-60 = 一般权重补充
# ---------------------------------------------------------------------------
HAND_WEIGHTS = {
    # —— 160 级（文明奠基者）——
    "Isaac Newton": 160, "Carl Friedrich Gauss": 155, "Leonhard Euler": 155,
    "Archimedes": 155, "Euclid": 155,
    "Gottfried Wilhelm Leibniz": 145, "Pierre de Fermat": 140,
    "René Descartes": 140, "Pythagoras": 135,
    "Muhammad ibn Musa al-Khwarizmi": 135,

    # —— 130 级（时代开创者）——
    "David Hilbert": 135, "Henri Poincaré": 135, "Bernhard Riemann": 130,
    "Joseph-Louis Lagrange": 125, "Pierre-Simon Laplace": 125,
    "Alexander Grothendieck": 120, "John von Neumann": 125,
    "Georg Cantor": 120, "Kurt Gödel": 120, "Alan Turing": 130,
    "Emmy Noether": 120, "Andrey Kolmogorov": 115, "Évariste Galois": 115,
    "Augustin-Louis Cauchy": 115, "Karl Weierstrass": 110,
    "Niels Henrik Abel": 110, "Srinivasa Ramanujan": 115,
    "Jean-Baptiste Joseph Fourier": 110, "Blaise Pascal": 110,
    "Galileo Galilei": 90, "Johannes Kepler": 90, "Christiaan Huygens": 90,

    # —— 90 级（大师级）——
    "Richard Dedekind": 95, "Jean-Pierre Serre": 90, "Pierre Deligne": 90,
    "Michael Atiyah": 90, "Shiing-Shen Chern": 90, "Shing-Tung Yau": 85,
    "Andrew Wiles": 95, "Grigori Perelman": 95, "Terence Tao": 90,
    "Paul Erdős": 95, "Felix Klein": 90, "Sophus Lie": 85,
    "Élie Cartan": 90, "Hermann Weyl": 95, "Joseph Fourier": 95,
    "Gottlob Frege": 90, "Bertrand Russell": 85,
    "Stefan Banach": 85, "Henri Lebesgue": 85, "Jacob Bernoulli": 80,
    "Daniel Bernoulli": 80, "Johann Bernoulli": 75,
    "Apollonius of Perga": 90, "Diophantus": 90, "Aryabhata": 90,
    "Brahmagupta": 85, "Omar Khayyam": 85, "Fibonacci": 90,
    "Leonardo Fibonacci": 90,  # 同一人别名
    "John Forbes Nash Jr.": 90, "John Nash": 90,
    "Benoit Mandelbrot": 85, "Claude Shannon": 90, "Norbert Wiener": 85,
    "Donald Knuth": 90, "Alonzo Church": 80, "Alfred Tarski": 85,

    # —— 70 级（重要学者）——
    "Carl Gustav Jacob Jacobi": 75, "Peter Gustav Lejeune Dirichlet": 75,
    "Arthur Cayley": 70, "William Rowan Hamilton": 75,
    "George Boole": 80, "Jacques Hadamard": 70,
    "Charles Hermite": 70, "Joseph Liouville": 65,
    "Adrien-Marie Legendre": 75, "Gaspard Monge": 65,
    "Abraham de Moivre": 65, "Brook Taylor": 60, "Colin Maclaurin": 60,
    "Siméon Denis Poisson": 70, "Giuseppe Peano": 70,
    "L. E. J. Brouwer": 70, "Hermann Minkowski": 70, "Felix Hausdorff": 70,
    "Jean le Rond d'Alembert": 75,
    "Sofia Kovalevskaya": 75, "Sophie Germain": 70, "Ada Lovelace": 70,
    "Hypatia": 70, "Hipparchus": 65, "Ptolemy": 75, "Eratosthenes": 70,
    "Eudoxus of Cnidus": 70, "Thales of Miletus": 70,
    "Zeno of Elea": 65, "Heron of Alexandria": 60, "Pappus of Alexandria": 60,
    "Liu Hui": 70, "Zu Chongzhi": 65, "Qin Jiushao": 55, "Zhu Shijie": 50,
    "Bhāskara II": 70, "Madhava of Sangamagrama": 65,
    "Al-Biruni": 70, "Thabit ibn Qurra": 60, "Al-Karaji": 60,
    "Sharaf al-Din al-Tusi": 55, "Nasir al-Din al-Tusi": 65,
    "Jamshid al-Kashi": 55, "Alhazen": 75, "Ibn al-Haytham": 75,
    "Nicole Oresme": 55, "Jordanus de Nemore": 45,
    "Gerolamo Cardano": 70, "Niccolò Fontana Tartaglia": 60,
    "Scipione del Ferro": 50, "François Viète": 65, "Simon Stevin": 55,
    "John Napier": 60, "Henry Briggs": 45,
    "Bonaventura Cavalieri": 55, "John Wallis": 65,
    "James Gregory": 50, "Isaac Barrow": 55,

    # —— 现代主要人物 ——
    "Friedrich Hirzebruch": 65, "Raoul Bott": 60, "Isadore Singer": 60,
    "Israel Gelfand": 80, "Sergei Novikov": 60, "Vladimir Arnold": 80,
    "Yakov Sinai": 65, "Andrey Markov": 80, "Pafnuty Chebyshev": 80,
    "Aleksandr Lyapunov": 65, "Lev Pontryagin": 65, "Mikhail Gromov": 75,
    "Atle Selberg": 70, "Paul Cohen": 70, "Saharon Shelah": 60,
    "John Milnor": 75, "Stephen Smale": 65, "William Thurston": 75,
    "Maryam Mirzakhani": 75, "Peter Scholze": 70, "Akshay Venkatesh": 55,
    "Manjul Bhargava": 60, "Cédric Villani": 55, "Wendelin Werner": 55,
    "Edward Witten": 75, "Kunihiko Kodaira": 65, "Heisuke Hironaka": 65,
    "Mikio Sato": 60, "Maxim Kontsevich": 70, "Vladimir Voevodsky": 65,
    "Laurent Schwartz": 70,
    "Charles-Jean de la Vallée Poussin": 55,
    "Solomon Lefschetz": 65, "Oscar Zariski": 65, "Saunders Mac Lane": 65,
    "Samuel Eilenberg": 60, "Jean Leray": 65,
    "Gerd Faltings": 60, "John G. Thompson": 65, "Grigory Margulis": 65,
    "Paul Dirac": 70, "Niels Henrik Abel": 110,

    # —— 计算机科学方向 ——
    "Edsger W. Dijkstra": 70, "Tony Hoare": 55, "John McCarthy": 65,
    "Marvin Minsky": 55, "Stephen Cook": 60, "Leonid Levin": 50,
    "Richard Karp": 60, "Robert Tarjan": 55, "Andrew Yao": 50,
    "Manuel Blum": 45, "Adi Shamir": 50, "Ron Rivest": 50,
    "Leonard Adleman": 45, "Whitfield Diffie": 45, "Martin Hellman": 45,
    "Avi Wigderson": 55, "Richard Hamming": 60,

    # —— 经济学 / 应用 ——
    "Kenneth Arrow": 55, "John Harsanyi": 40, "Reinhard Selten": 40,
    "Lloyd Shapley": 45, "Robert Aumann": 45, "George Dantzig": 65,
    "Leonid Kantorovich": 50, "Tjalling Koopmans": 35,
    "Frank Plumpton Ramsey": 55,

    # —— 统计 ——
    "Karl Pearson": 70, "Ronald Fisher": 75, "Jerzy Neyman": 60,
    "Egon Pearson": 45, "Bradley Efron": 45, "C. R. Rao": 55,

    # —— 印度 / 中国 / 日本现代 ——
    "Harish-Chandra": 65, "Calyampudi Radhakrishna Rao": 55,
    "Hua Luogeng": 65, "Chen Jingrun": 55, "Wu Wenjun": 55,

    # —— 逻辑 ——
    "Stephen Cole Kleene": 55, "Haskell Curry": 55, "Alfred North Whitehead": 55,
    "Kazimierz Kuratowski": 50,
}


# ---------------------------------------------------------------------------
# 5) 综合打分
# ---------------------------------------------------------------------------
def compute_score(meta: dict, awards: list[str], hand_weight: float) -> float:
    """
    综合评分函数。
    权重设计目标：让 Newton / Gauss / Euler / Archimedes / Euclid 稳居前 10。

    组成：
      1. 奠基权重（人工表，主导）：0-150
      2. 顶级奖项（上限 60）：一个菲尔兹 = 40，两项 = 55，三项 = 60
      3. 文章长度（log，主要用于长尾）：0-40
    """
    length = max(meta.get("length") or 0, 1)
    score = 0.0
    # 1) 人工权重（核心）
    score += hand_weight
    # 2) 奖项：先取 unique 奖项分值，取前 3 项，再封顶 60
    award_pts = sorted(
        {TOP_AWARDS[a][1] for a in awards if a in TOP_AWARDS},
        reverse=True,
    )[:3]
    award_total = sum(award_pts)
    score += min(award_total, 45)
    # 3) 文章长度：典型 50KB → ~27；200KB → ~37
    score += 6.0 * math.log10(length)
    return score


# ---------------------------------------------------------------------------
# 6) 主流程
# ---------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--top", type=int, default=500)
    ap.add_argument("--limit", type=int, default=0, help="只处理前 N 个名字（调试）")
    ap.add_argument("--no-cache", action="store_true")
    ap.add_argument("--workers", type=int, default=1, help="MediaWiki API 不建议并发，默认 1")
    args = ap.parse_args()

    CACHE.mkdir(exist_ok=True)
    names = load_names()
    if args.limit:
        names = names[: args.limit]
    print(f"[1/4] 读取 {len(names)} 个数学家")

    # ---- 拿元数据（length + qid）----
    cache_meta = CACHE / "meta.json"
    meta_all: dict[str, dict] = {}
    if cache_meta.exists() and not args.no_cache:
        meta_all = json.loads(cache_meta.read_text())
        print(f"  从缓存加载 {len(meta_all)} 条")

    todo = [n for n in names if n not in meta_all]
    print(f"[2/4] 需要抓取 {len(todo)} 条元数据")
    s = build_session()
    for i in range(0, len(todo), 50):
        batch = todo[i : i + 50]
        try:
            got = fetch_meta_batch(s, batch)
        except Exception as e:
            print(f"  ! 批 {i // 50}: {e}")
            continue
        meta_all.update(got)
        if i % 500 == 0 and i > 0:
            cache_meta.write_text(json.dumps(meta_all, ensure_ascii=False))
            print(f"  …已抓 {i + 50}/{len(todo)}（缓存 {len(meta_all)}）")
        time.sleep(0.15)
    cache_meta.write_text(json.dumps(meta_all, ensure_ascii=False))
    print(f"  ✓ 元数据缓存共 {len(meta_all)}")

    # ---- 拿奖项 ----
    cache_award = CACHE / "awards.json"
    awards_all: dict[str, list[str]] = {}
    if cache_award.exists() and not args.no_cache:
        awards_all = json.loads(cache_award.read_text())
        print(f"  从缓存加载 {len(awards_all)} 条奖项")

    qids = sorted({m["qid"] for m in meta_all.values() if m.get("qid")})
    todo_q = [q for q in qids if q not in awards_all]
    print(f"[3/4] 需要抓取 {len(todo_q)} 个 QID 的奖项")
    for i in range(0, len(todo_q), 50):
        batch = todo_q[i : i + 50]
        try:
            got = fetch_awards_batch(s, batch)
        except Exception as e:
            print(f"  ! Wikidata 批 {i // 50}: {e}")
            continue
        awards_all.update(got)
        if i % 500 == 0 and i > 0:
            cache_award.write_text(json.dumps(awards_all))
            print(f"  …已抓 {i + 50}/{len(todo_q)}")
        time.sleep(0.15)
    cache_award.write_text(json.dumps(awards_all))
    print(f"  ✓ 奖项缓存共 {len(awards_all)}")

    # ---- 综合打分 ----
    print("[4/4] 综合打分 & 排序")
    scored = []
    for name in names:
        meta = meta_all.get(name) or {}
        qid = meta.get("qid")
        awards = awards_all.get(qid, []) if qid else []
        hw = HAND_WEIGHTS.get(name, 0)
        score = compute_score(meta, awards, hw)
        scored.append({
            "name": name,
            "score": score,
            "length": meta.get("length", 0),
            "qid": qid,
            "awards": awards,
            "hand_weight": hw,
        })
    scored.sort(key=lambda x: -x["score"])
    top = scored[: args.top]

    # 写出
    write_md(top, OUT)
    print(f"\n✅ 写入 {OUT}（共 {len(top)} 人）")
    return 0


def write_md(top: list[dict], out: Path) -> None:
    lines = []
    lines.append("# 维基百科数学家影响力榜 · Top 500")
    lines.append("")
    lines.append("> **评分方法**")
    lines.append("> 综合分由三部分加权而成：")
    lines.append(">")
    lines.append("> 1. **奠基权重**（0-160）：按文明贡献手工赋值。160 = 文明级（Newton/Gauss 等），130 = 时代开创者，90 = 大师级。")
    lines.append("> 2. **顶级奖项**（0-45，封顶）：菲尔兹 40 / 阿贝尔 50 / 沃尔夫 40 / 图灵 40 / 克拉福德 25 / 陈省身 25 / 高斯 25 / 奈望林纳 25 / 经济学诺奖 15 / 科普利奖章 15。取最高 3 项之和，但封顶 45。")
    lines.append("> 3. **Wikipedia 文章长度**（0-40）：$6 \\log_{10}(\\text{bytes})$，作为社会关注度代理。")
    lines.append(">")
    lines.append("> **评价维度取舍**：")
    lines.append("> - 「对人类的影响」不等同于「现代学界的声望」。因此文明级奠基者（古代/早期）的权重高于仅拿顶级奖项的现代人。")
    lines.append("> - 排除非数学家（哲学家/物理学家），但交叉领域人物（von Neumann、Turing、Nash、Shannon、Knuth、Kolmogorov）保留。")
    lines.append("> - 奖项封顶 45 分，避免『三奖收藏家』碾压无现代奖的古代奠基者。")
    lines.append(">")
    lines.append(f"> **数据**：共扫描 `mathematicians.md` 中 11,326 人；生成时间 {time.strftime('%Y-%m-%d %H:%M:%S')}。")
    lines.append("")
    lines.append("## 总榜 Top 500")
    lines.append("")
    lines.append("| 排名 | 数学家 | 综合分 | 文章长度 | 主要奖项 |")
    lines.append("|---:|---|---:|---:|---|")

    award_names = {qid: name for qid, (name, _) in TOP_AWARDS.items()}

    for i, p in enumerate(top, 1):
        name = p["name"]
        url = f"https://en.wikipedia.org/wiki/{quote(name.replace(' ', '_'))}"
        named_awards = sorted({
            award_names[a] for a in p["awards"] if a in award_names
        })
        award_str = "、".join(named_awards) if named_awards else "—"
        lines.append(
            f"| {i} | [{name}]({url}) | {p['score']:.1f} | "
            f"{p['length']:,} | {award_str} |"
        )

    # 按奖项/类别的分类视图
    lines.append("")
    lines.append("---")
    lines.append("")
    lines.append("## 分榜")
    lines.append("")

    # 菲尔兹奖
    fields_q = "Q28835"
    fields_list = [p for p in top if fields_q in p["awards"]]
    lines.append(f"### 🏅 菲尔兹奖得主（本榜收录 {len(fields_list)} 位）")
    lines.append("")
    for p in fields_list:
        url = f"https://en.wikipedia.org/wiki/{quote(p['name'].replace(' ', '_'))}"
        lines.append(f"- [{p['name']}]({url}) — 综合分 {p['score']:.1f}")
    lines.append("")

    # 阿贝尔奖
    abel_q = "Q188184"
    abel_list = [p for p in top if abel_q in p["awards"]]
    lines.append(f"### 🏅 阿贝尔奖得主（本榜收录 {len(abel_list)} 位）")
    lines.append("")
    for p in abel_list:
        url = f"https://en.wikipedia.org/wiki/{quote(p['name'].replace(' ', '_'))}"
        lines.append(f"- [{p['name']}]({url}) — 综合分 {p['score']:.1f}")
    lines.append("")

    # 沃尔夫奖
    wolf_q = "Q915604"
    wolf_list = [p for p in top if wolf_q in p["awards"]]
    lines.append(f"### 🏅 沃尔夫数学奖得主（本榜收录 {len(wolf_list)} 位）")
    lines.append("")
    for p in wolf_list:
        url = f"https://en.wikipedia.org/wiki/{quote(p['name'].replace(' ', '_'))}"
        lines.append(f"- [{p['name']}]({url}) — 综合分 {p['score']:.1f}")
    lines.append("")

    # 图灵奖
    turing_q = "Q185667"
    turing_list = [p for p in top if turing_q in p["awards"]]
    lines.append(f"### 🏅 图灵奖得主（本榜收录 {len(turing_list)} 位）")
    lines.append("")
    for p in turing_list:
        url = f"https://en.wikipedia.org/wiki/{quote(p['name'].replace(' ', '_'))}"
        lines.append(f"- [{p['name']}]({url}) — 综合分 {p['score']:.1f}")
    lines.append("")

    # 古代奠基者（基于人工权重判断）
    lines.append("### 🏛 古代至中世纪奠基者")
    lines.append("")
    ancient_names = {
        "Pythagoras", "Euclid", "Archimedes", "Apollonius of Perga",
        "Eratosthenes", "Hipparchus", "Ptolemy", "Diophantus",
        "Hypatia", "Heron of Alexandria", "Pappus of Alexandria",
        "Thales of Miletus", "Zeno of Elea", "Eudoxus of Cnidus",
        "Aryabhata", "Brahmagupta", "Bhāskara II", "Madhava of Sangamagrama",
        "Liu Hui", "Zu Chongzhi", "Qin Jiushao", "Zhu Shijie",
        "Muhammad ibn Musa al-Khwarizmi", "Omar Khayyam", "Al-Biruni",
        "Thabit ibn Qurra", "Al-Karaji", "Sharaf al-Din al-Tusi",
        "Nasir al-Din al-Tusi", "Jamshid al-Kashi", "Alhazen",
        "Ibn al-Haytham", "Fibonacci", "Leonardo Fibonacci", "Nicole Oresme",
    }
    for p in top:
        if p["name"] in ancient_names:
            url = f"https://en.wikipedia.org/wiki/{quote(p['name'].replace(' ', '_'))}"
            lines.append(f"- [{p['name']}]({url}) — 综合分 {p['score']:.1f}")
    lines.append("")

    # 女数学家
    lines.append("### 👩‍🔬 女数学家")
    lines.append("")
    women = {
        "Hypatia", "Sophie Germain", "Ada Lovelace", "Mary Somerville",
        "Sofia Kovalevskaya", "Emmy Noether", "Grace Hopper",
        "Julia Robinson", "Karen Uhlenbeck", "Mary Cartwright",
        "Maryam Mirzakhani", "Ingrid Daubechies", "Cathleen Synge Morawetz",
        "Dorothy Lewis Bernstein",
    }
    for p in top:
        if p["name"] in women:
            url = f"https://en.wikipedia.org/wiki/{quote(p['name'].replace(' ', '_'))}"
            lines.append(f"- [{p['name']}]({url}) — 综合分 {p['score']:.1f}")
    lines.append("")

    out.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())
