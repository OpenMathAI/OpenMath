# Wikipedia 数学家工具集

从维基百科抓取数学家信息，转换为 Markdown / LaTeX / PDF。

## 完整流水线

```
Wikipedia API
    ↓ fetch_mathematicians.py     (列表索引：~11,000 人)
mathematicians.md
    ↓ fetch_full_pages.py         (每人完整页面：HTML + Markdown + Wikidata 元数据)
pages/<Name>/{page.html, page.md, metadata.json, images.txt}
    ↓ to_tex.py                   (HTML → LaTeX，下载图片，生成 Makefile)
tex/<Name>/{<Name>.tex, body.tex, metadata.tex, images/, Makefile}
    ↓ make                        (xelatex 编译)
tex/<Name>/<Name>.pdf
```

## 环境

```bash
# Python 依赖
conda activate d2l_3.13
pip install -r requirements.txt

# 系统依赖（macOS）
brew install pandoc          # HTML → LaTeX
brew install --cask mactex   # 提供 xelatex / latexmk
```

## 三个脚本

### 1. `fetch_mathematicians.py` — 抓所有数学家清单

```bash
python fetch_mathematicians.py                        # 输出 mathematicians.md
python fetch_mathematicians.py --with-summary         # 附带每人首段简介
python fetch_mathematicians.py --lang zh -o 数学家.md  # 中文维基
```

### 2. `fetch_full_pages.py` — 抓每位数学家的完整页面

```bash
python fetch_full_pages.py --sample                   # 5 位著名数学家（示例）
python fetch_full_pages.py --from-md mathematicians.md --limit 100
python fetch_full_pages.py --from-list names.txt
```

每人产出：
- `page.html` — Wikipedia 渲染后的 HTML（已清洗 + 链接绝对化）
- `page.md`   — Markdown 正文 + YAML frontmatter（生卒、领域、获奖等）
- `metadata.json` — Wikidata 结构化元数据
- `images.txt` — 页面所有图片 URL 清单

### 3. `to_tex.py` — 转换为 LaTeX 项目

```bash
python to_tex.py                  # 转换 pages/ 下所有人
python to_tex.py --only Gauss     # 只转换名字含 "Gauss" 的
python to_tex.py --limit 5
python to_tex.py --no-images      # 不下载图片（编译时需联网）
```

每人产出 `tex/<Name>/`：
- `<Name>.tex`   — 主文件（`\documentclass + \input{body.tex}`）
- `body.tex`     — pandoc 从 HTML 转换的正文
- `metadata.tex` — 由 metadata.json 生成的 `\renewcommand`
- `images/`      — 下载的图片（离线可编译）
- `Makefile`     — 子 Makefile

并生成顶层 `tex/Makefile` 和 `tex/index.tex`。

## 编译 PDF

```bash
cd tex
make            # 串行编译所有人
make parallel   # 用 `-jN` 并行编译（N=CPU核数）
make clean      # 清掉中间文件，保留 PDF
make distclean  # 清掉所有产物（含 PDF）

# 单独编译某一位
make -C Carl_Friedrich_Gauss
```

每个子目录的 Makefile：

```makefile
all: $(NAME).pdf            # latexmk -xelatex
clean: # 清掉 .aux / .log / .out 等
distclean: # 也清掉 PDF
```

## 已知问题与设计取舍

| 问题 | 解决方式 |
|---|---|
| Wikimedia 对图片下载的 429 限流 | UA 加联系方式 + 指数退避重试 + 限速 |
| URL 过长导致 `\href@split` 错误 | HTML 阶段把 URL >120 或 %>3 的 `<a>` 替换为纯文本 |
| `\phantomsection\label{}` 在 `\caption{}` 内触发 `\iffalse` 错 | 在 body.tex 后处理中删除所有 `\phantomsection*` |
| `\foreignlanguage{english}{...}`（hyperref 强制要求 babel） | preamble 里 `\renewcommand` 简单输出第二参数 |
| `\pandocbounded` 命令未定义 | preamble providecommand 兜底 |
| `grffile` 与新 LaTeX 冲突触发 iffalse | 移除 `\usepackage{grffile}` |
| GIF / SVG / WebP 图片 xelatex 不直接支持 | 下载白名单只含 png/jpg/pdf，其它直接跳过 |
| 文件名带 ß / ü / ö 等 Unicode 触发 iffalse | 文件名只保留 ASCII |
| 引用文献末尾的超长 URL（带大量 %xx 编码） | 同上：HTML 阶段已退化为纯文本 |
| pandoc 把 References 章节也转换 | HTML 阶段直接砍掉 References / External links / See also 等 |

## 样例输出（5 位示例）

| 数学家 | PDF 大小 | 页数 |
|---|---|---|
| Carl Friedrich Gauss | 1.1 MB | 36 |
| Emmy Noether         | 563 KB | 30 |
| Leonhard Euler       | 453 KB | 22 |
| Alexander Grothendieck | 253 KB | 17 |
| Bernhard Riemann     | 121 KB | ~10 |

## 自定义样式

修改 `common/preamble.tex` 后，运行 `make clean && make` 即可全量重编。
顶层 `to_tex.py` 在每次运行时会把 `common/preamble.tex` 复制到 `tex/common/`。
