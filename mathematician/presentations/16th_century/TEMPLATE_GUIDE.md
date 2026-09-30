# TEMPLATE_GUIDE — 16 世纪数学家立传执行模板（标杆：17 世纪 Johann Bernoulli）

> 所有立传 agent 执行前必读。黄金参照：`../17th_century/1667–Johann_Bernoulli/Johann_Bernoulli_zh.tex`（逐帧改写，勿凭空另起炉灶）。
> 事实基准：各人 `pages/<Name>/page.md`（与提示词 md§5 冲突时以 page.md 为准，并把修正写回提示词 md）。
> 人物专属要求：各人 `{生年}–{Name}/{Name}_zh.md`（§3 配色、§4 Slide 规划、§5 史实陷阱、§7 关系清单）。

## 1. 目录与文件

每人一个文件夹 `16th_century/{生年}–{Name}/`（已存在，内含提示词 md），需补齐：

```
{生年}–{Name}/
├── <Name>_zh.tex          # 主文件（由 Johann_Bernoulli_zh.tex 逐帧改写）
├── Makefile               # 从 17th_century/1667–Johann_Bernoulli/Makefile 复制，仅改两行：
│                            MAIN = <Name>_zh
│                            VIDEO_NAME = <Name>_zh
├── <Name>_zh.md           # 提示词（Review 修正写回此处）
└── images/
    └── <x>_portrait.jpg   # 肖像（见 §3）
```

- 共享封面：`\input{../../cover/openmath_page.tex}`（无参数，直接复用，勿改）。
- 目录名含 `–`（EN DASH U+2013）与变音字符（如 `Niccolò`/`François`/`Viète`），shell 操作务必加引号。
- 文件统一 LF 行尾。

## 2. 帧结构（14 页，与 Johann 完全同构）

| # | 宏名 | 内容 |
|---|---|---|
| 1 | `\openmathslide` | 共享封面（\input，不改） |
| 2 | `\titleslide` | 人物封面：国籍行 + 大标题 + 生卒 + 成就行 + 分隔线 + 四分类 badge + 一句话定位 + 右上肖像 + 底部三要素 |
| 3 | `\profileslide` | 身份信息页（★ 必做）：左肖像 + 右 2×2 信息网格 |
| 4 | `\timelineslide` | 时间线（竖轴 8 个节点，`\foreach \y/\year/\txt`，分隔符必须 ASCII 逗号） |
| 5 | `\earlyslide` | 早年与教育（`p{2.2cm}|X|p{3.0cm}` 三列表格） |
| 6–12 | 各人自定义 | 7 个核心贡献/叙事页（`m{3.4cm}|X|p{3.0cm}` 表格 + `\fcolorbox` 公式框） |
| 13 | `\honorslide` | 荣誉与传承（表格，可含 itemize） |
| 14 | `\closingslide` | 终章（两行大字 + 分隔线 + 两行小字 + 底部品牌行 `OpenMathAI`） |

- 命名惯例：贡献页宏用人物语义名（如 `\cubicslide`、`\complexslide`），`\begin{document}` 后按序调用 14 个宏。
- 提示词 §4 若规划 13 页（如 Ferrari/Bombelli），则第 6–12 区段取 6 页，总页数 13 页亦可接受；**页数与提示词 §4 一致**为准。

## 3. 配色与肖像

- 配色：按提示词 §3 的「主色 + 强调色（金 `#C9A227`）+ 四分类色」实现。宏名用通用名（`mainclr`、`accentclr`、`badgeA..badgeD`、`panelA..panelD`），注释写人物语义。`deckbackground` 气泡四圆分别用 badgeA/B/C/D，结构照抄 Johann。
- 肖像：**以 `PORTRAITS.md` 中已核实结论为准**（主控已逐一经 Wikipedia REST API 核验），URL 直接下载：

```bash
mkdir -p "images"
curl -sL -A "Mozilla/5.0" "<PORTRAITS.md 中的 URL>" -o "images/<x>_portrait.jpg"
file "images/<x>_portrait.jpg"   # 必须为 JPEG/PNG 且 >5KB，否则换 Special:FilePath 重试
```

- `PORTRAITS.md` 标注「无肖像」者**必须**用装饰圆占位（禁止拿书影、雕像、墓碑、文献扉页冒充头像）：

```latex
\node[draw=accentclr!50, line width=1.2pt, rounded corners=6pt, fill=white, inner sep=2pt]
  at (...) {\begin{tikzpicture}\clip[rounded corners=4pt] (0,0) rectangle (2.0,2.9);
    \node[font=\fontsize{40}{40}\selectfont, text=accentclr!60] at (1.0,1.45) {\faIcon{user}};\end{tikzpicture}};
```

- tex 中引用文件名 `<x>_portrait.jpg`；`\graphicspath{{images/}}`；图注写明肖像来源/年代/「传为」等限定语。

## 4. 编译循环（最重要）

```bash
cd "16th_century/{生年}–{Name}"
make distclean && make      # latexmk 自动多遍编译（remember picture 需两遍）
grep -c "Overfull" <Name>_zh.log   # 有则修（<10pt 可接受，超出必须改）
```

- 每写完 tex 立即 make，看到溢出就修，直到 0 error 且 Overfull 全部 <10pt。
- 取真实日志做溢出检查时，**取完必须重新 `make`**（单遍 xelatex 会破坏 remember picture 定位）。

## 5. 已知陷阱（前车之鉴，必查）

1. `\enspace` 在 profile 页结构下会丢 P1 顶部元素 → 信息网格内用 `\quad`
2. `remember picture` 需两遍编译（latexmk 自动多遍，勿改单遍）
3. tikzpicture 选项 `[]` 与 `{}` 不匹配会破坏编译
4. `\fontsize{a}{b}\selectfont` 不得有多余反斜杠
5. 文本模式希腊字母（α β γ）缺字 → 必须进数学模式 `$\alpha$`；带圈数字 ①-④ 需 `\xeCJKDeclareCharClass{CJK}{"2460->"2473}`；★（U+2605）在 lmsans-oblique 缺字
6. `\newcommand` 宏名含数字会被截断（命名勿带数字）
7. `\foreach` 条目的分隔符必须是 ASCII 逗号，中文逗号会吞条目
8. tabularx 的 X 列内禁用 `\\` 换行，须用 `\newline`
9. 表格页安全负间距：顶部 `-0.35 ~ -0.55cm`、`\arraystretch 0.60~0.82`、公式框前 `-0.3cm`；条目多时用 `\itemsep -2.5pt`、`\topsep 0pt`
10. 引语只允许用提示词标明的 page.md 原文；中文引号不进 LaTeX 代码（引号用半角 `"`）
11. 事实红线：生卒/国籍/称号逐条对照提示词 §5 与 page.md；**无载禁写**（尤其：禁编造导师、禁编造年份、禁编造直接引语）
12. 肖像若与提示词 §3 记录不同，以 `PORTRAITS.md` 为准并把更新写回提示词 md

## 6. 完成标准（每人）

- [ ] `<Name>_zh.pdf` 生成成功（页数与提示词 §4 一致）
- [ ] 编译 0 error，Overfull 全部 <10pt
- [ ] 封面：国籍行 + 肖像（或装饰圆）+ 四 badge + 底部三要素
- [ ] 身份信息页、时间线页、贡献页、荣誉页、终章齐备
- [ ] 底部品牌 `OpenMathAI`
- [ ] 事实与提示词 §5 逐条对齐（Review-1 事实终审，修正写回提示词 md）
- [ ] 不做视频（mp4 由主控统一安排）
