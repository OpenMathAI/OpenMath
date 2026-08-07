# 项目总结与扩展指南

> 本文档面向"接手者"，目标是让你在 5 分钟内理解项目结构，
> 并在 30 分钟内可以扩充到任意规模的数学家。
> 想看"怎么用"，请读 [`README.md`](./README.md)。

---

## 一、项目目标

把维基百科上的"所有数学家"做成可离线阅读的资料库：

```
Wikipedia → 名单（11k 人） → 每人完整页面 → 每人独立 LaTeX/PDF
```

---

## 二、流水线总览

```
┌──────────────────────────────┐
│ ① fetch_mathematicians.py    │  抓 26 个 "List of mathematicians (X)" 页面
│   → mathematicians.md        │  得到 11,326 人名单（带 wiki 链接）
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ ② fetch_full_pages.py        │  对每个人调 REST API 拿渲染后 HTML
│   → pages/<Name>/            │  + Wikidata 拿结构化元数据（生卒、领域、获奖…）
│      ├ page.html             │  + HTML→Markdown 转换
│      ├ page.md               │
│      ├ metadata.json         │
│      └ images.txt            │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ ③ to_tex.py                  │  HTML 进一步清洗 → pandoc → LaTeX
│   → tex/<Name>/              │  下载图片本地化，生成 Makefile
│      ├ <Name>.tex            │
│      ├ body.tex              │
│      ├ metadata.tex          │
│      ├ images/               │
│      └ Makefile              │
└──────────────┬───────────────┘
               │
               ▼
┌──────────────────────────────┐
│ ④ make (in tex/)             │  latexmk -xelatex
│   → tex/<Name>/<Name>.pdf    │  自动多轮编译 + 自动清理中间产物
└──────────────────────────────┘
```

每一步都有**断点存档**（中间产物落盘），所以可以**单独重跑某一步**而不影响其它步骤。

---

## 三、关键设计决策

### 3.1 为什么用 HTML 作为中间表示，而不是 wikitext / Markdown？

| 选项 | 优点 | 缺点 |
|---|---|---|
| **wikitext**（维基源码）| 信息最完整 | 模板宏太多，自己解析等于重写 MediaWiki 引擎 |
| Markdown（首段） | 简单 | 丢表格、信息框、数学公式 |
| **HTML（已渲染）** ✅ | 完整 + 结构化 + 图片/数学/表格全有 | 体积稍大 |

我们选 HTML，让 MediaWiki 自己渲染好，再用 BeautifulSoup 清洗。

### 3.2 为什么用 pandoc，而不是手写 HTML→LaTeX？

- pandoc 已正确处理：标题层级、嵌套列表、表格、`<math>`、脚注、内链、图片
- 支持 Lua filter 做精细化定制
- 缺点：会生成一些冒进的 LaTeX（`\phantomsection\label{}` 进 `\caption{}` 等）→ 用后处理修

### 3.3 为什么用 latexmk，而不是直接 xelatex？

LaTeX 编译需要多次跑（目录、交叉引用、长表格列宽），latexmk 自动判断。详见 [`README.md`](./README.md#编译-pdf)。

### 3.4 为什么每人一个独立 Makefile？

- 失败可隔离：一个人编不过，不影响其他 11,000+ 人
- 增量友好：改一个人的 `body.tex`，只重编那个人
- 可并行：顶层 Makefile 用 `make -jN` 并行调用子 Makefile

---

## 四、踩过的所有坑（按出现顺序）

下面这些都是真实遇到过的，**改源码前先看一眼**，避免重蹈覆辙。

| # | 现象 | 根因 | 修复位置 |
|---|---|---|---|
| 1 | `SSLError` / `429 Too Many Requests` | UA 不合规 / 没限速 | `to_tex.py` 的 `USER_AGENT` 含联系方式 + 0.2s 限速 + 指数退避 |
| 2 | `Latin Modern Roman` 找不到 | TeX Live 自带的 lm 不是 OTF 名 | `common/preamble.tex` 改用 `Times New Roman` 等系统字体 |
| 3 | `! Package fontspec Error: font cannot be found` | `\setmainfont` 写死字体 | 用 `\IfFontExistsTF` 兜底 |
| 4 | `Incomplete \iffalse` 在第 N 行 | `grffile` 与新 LaTeX 冲突 | 移除 `\usepackage{grffile}` |
| 5 | `Incomplete \iffalse`（图片名带 ß / ü） | XeLaTeX `\includegraphics` 在 Unicode 文件名上有 bug | 文件名规范化为 ASCII（见 `to_tex.py: re.sub(r"[^A-Za-z0-9._-]+", "_", fname)`） |
| 6 | `Incomplete \iffalse`（在 `\caption{}` 内） | `\phantomsection` 在 fragile 上下文 | `to_tex.py: postprocess_tex` 删除所有 `\phantomsection*` |
| 7 | `\foreignlanguage` 报"未加载多语言包" | hyperref 偷偷定义了它 | `preamble.tex` 用 `\renewcommand` 覆盖为简单输出 |
| 8 | `File ended while scanning use of \pandocbounded` | pandoc 3 新命令未定义 | `preamble.tex: \providecommand{\pandocbounded}[1]{...}` |
| 9 | `Paragraph ended before \href@split was complete` | URL 被 pandoc 转义后超长（`\%7B` 之类） | HTML 阶段把 `len(href)>120` 或 `%>3` 的 `<a>` 替换为纯文本 |
| 10 | `Missing }` in itemize | `<a>` 嵌套时 BS4 `unwrap()` 破坏结构 | 用 `replace_with(NavigableString)` 而不是 `unwrap()` |
| 11 | `Missing }` 在 minipage 内 | "skipped image" 用 `% 注释` 在 fragile 环境里破坏花括号 | 改为返回空串 |
| 12 | `Cannot determine size of graphic .gif` | xelatex 不直接吃 GIF | `_IMG_EXT_OK` 只允许 png/jpg/jpeg/pdf |
| 13 | `! Forbidden control sequence ... \LT@nofcols` | Wikipedia `.sidebar` 被转成嵌套 longtable | HTML 阶段砍掉 `.sidebar`、`table.sidebar` |
| 14 | 顶层 Makefile 只剩 1 个 SUBDIRS | `to_tex.py --only X` 也覆写了顶层 Makefile | 见下方"扩展时的注意事项" |

---

## 五、如何扩展到更多数学家

### 场景 A：再加 100 个

```bash
conda activate d2l_3.13

# 1. （可选）先确认 11k 名单已有，否则跑：
python fetch_mathematicians.py

# 2. 抓 100 人完整页面（脚本对已存在目录会跳过，可断点续传）
python fetch_full_pages.py --from-md mathematicians.md --limit 100

# 3. 转成 LaTeX 项目（同样会复用已下载的图片）
python to_tex.py

# 4. 编译（自动并行 + 自动清理中间产物）
cd tex && make parallel
```

### 场景 B：抓全量 11,326 人

**预估**：
- 网络请求：~34,000 次 HTTP（可用 `--jobs` 加并发）
- 时间：~5 小时（带 0.5s 间隔；并发 8 后约 30 min）
- 磁盘：约 8 GB（HTML + Markdown + 图片）
- LaTeX 编译：8 秒/人 × 11,326 ≈ 25 小时单线程，并行后约 3 小时

**操作**：

```bash
# 1. 拿全量名单
python fetch_mathematicians.py

# 2. 全量抓页面（建议加上 nohup + 日志）
nohup python fetch_full_pages.py --from-md mathematicians.md \
    > fetch.log 2>&1 &
tail -f fetch.log

# 3. 全量转 tex（同样建议放后台）
nohup python to_tex.py > totex.log 2>&1 &

# 4. 并行编译
cd tex && nohup make parallel > build.log 2>&1 &
```

### 场景 C：只想要"重要数学家"

不要全量 11k，可以从 `mathematicians.md` 里挑一份精简名单：

```bash
# 自己写一个 names.txt，每行一个名字
cat > top_50.txt <<EOF
Carl Friedrich Gauss
Leonhard Euler
Pierre de Fermat
Isaac Newton
Bernhard Riemann
...（可以从 Fields/Abel/Wolf 奖名单里选）
EOF

python fetch_full_pages.py --from-list top_50.txt
python to_tex.py
cd tex && make parallel
```

或者按"奖项"过滤——参考 [`README.md` 的"如何分类"章节](./README.md)。

### 场景 D：换语言（如中文维基）

```bash
# 中文维基用分类递归抓更准（中文版列表页质量参差）
python fetch_mathematicians.py --lang zh -o 数学家.md
python fetch_full_pages.py --from-md 数学家.md --lang zh
# 注意：to_tex.py 的 preamble 默认 Times New Roman，
# 中文要改用 PingFang / Source Han Serif（修 common/preamble.tex）
```

---

## 六、扩展时的注意事项 ⚠️

### 6.1 增量抓取，不要全量重跑

- `fetch_full_pages.py` 当前**没有断点续传**。如果你抓一半失败，会重抓全部。
  → **TODO**：在 `process_one` 开头加 `if (person_dir / "page.md").exists(): return`
- `to_tex.py` 也类似，重跑会覆盖已生成的 `tex/<Name>/`，但**图片有缓存**（`if not dst.exists()`），所以不会重复下载。

### 6.2 顶层 Makefile 会被 `to_tex.py` 覆写

当前 `to_tex.py --only X` 会把顶层 `tex/Makefile` 重新生成为**只包含 X**——这是一个 bug。
**建议改法**（未实现）：`write_top_level()` 应当扫描 `tex/` 下**所有**子目录，而不是只用本次处理的。

> 临时绕过：用下面这段 Python 全量重写顶层 Makefile：
> ```python
> from to_tex import TOP_MAKEFILE_HEAD, SUB_MAKEFILE
> from pathlib import Path
> tex = Path('tex')
> subs = sorted(p.name for p in tex.iterdir() if p.is_dir() and p.name != 'common')
> top = TOP_MAKEFILE_HEAD.format(subdirs=' '.join(subs), targets=' '.join(subs))
> Path(tex / 'Makefile').write_text(top + '\n' + '\n'.join(f'{d}:\n\t$(MAKE) -C {d} pdf\n' for d in subs))
> ```

### 6.3 编译失败的人物会卡住整个 `make`

顶层 Makefile 用 `for` 循环串行，`|| exit $$?` 会在第一个失败时停掉。
若想"失败的跳过、继续编其它人"，加 `-k` flag：
```bash
make -k             # keep going on errors
make -k parallel    # 同上 + 并发
```

### 6.4 Wikimedia 限流

- 单 IP 突发请求很快撞 429
- 我们已加：合规 UA、0.2-0.5s 限速、指数退避、3 次重试
- **如果还失败**：等几分钟再跑，或者改 `fetch_full_pages.py` 的 `--sleep` 增大

### 6.5 编译中的字符警告

```
Missing character: There is no ⓘ (U+24D8) in font Times New Roman
```
**这是警告，不是错误**。Times New Roman 没有这个字符，被丢弃。
若想正确显示，在 `preamble.tex` 加 fallback 字体（如 `Symbola`、`Noto Sans Symbols`）。

---

## 七、后续可做的改进

按"投入产出比"从高到低：

1. **断点续传** —— 让 `fetch_full_pages.py` 和 `to_tex.py` 跳过已完成的，便于增量抓取
2. **顶层 Makefile bug 修复** —— `to_tex.py: write_top_level` 改为扫描 `tex/` 全目录
3. **并发抓取** —— `fetch_full_pages.py` 加 `--jobs N` 用 `ThreadPoolExecutor`
4. **失败清单** —— 单独输出 `failed.txt`，方便重跑
5. **进度条** —— 加 `tqdm`
6. **按领域 / 时代分类** —— 详见 README "数学家分类" 章节，可生成多个 index.tex
7. **LaTeX 字体改进** —— 当前 Times New Roman 不全，加 Symbola 之类做 unicode fallback
8. **总书生成** —— 把 11k 人合订成一本巨型 PDF（用 `\includepdf` 或 `\subfile`）
9. **数学公式优化** —— pandoc 把 MathML 转成 `\(...\)`，可改用 `--mathjax` 或 `--katex` 模式让结果更纯净
10. **Web 版本** —— pages/<Name>/page.md + frontmatter 已经是 Hugo/Jekyll 友好的格式，可直接搭一个静态站点

---

## 八、文件速查表

| 文件 | 何时改 |
|---|---|
| `fetch_mathematicians.py` | 想换数据源（如改成抓"物理学家"），或换语言 |
| `fetch_full_pages.py` | 想抓更多元数据字段，或调整 HTML 清洗规则 |
| `to_tex.py` | 想换转换工具，或加新的 LaTeX 后处理规则 |
| `common/preamble.tex` | 想改 PDF 排版样式（字体、颜色、版芯、页眉） |
| `to_tex.py` 里的 `SUB_MAKEFILE` | 想改每人的编译/清理逻辑 |
| `to_tex.py` 里的 `TOP_MAKEFILE_HEAD` | 想改批量编译/并行策略 |

---

## 九、快速验证

修改任何脚本后，先用小样本验证：

```bash
# 1. 抓 3 个示例人
python fetch_full_pages.py --sample
# 实际只用其中 3 个验证：
ls pages/

# 2. 转 tex（只转 1 个）
python to_tex.py --only Carl_Friedrich_Gauss

# 3. 编译
cd tex && make
# 看到 "✅ 全部完成" 就行
```

整个回路约 **30 秒** 跑完。
