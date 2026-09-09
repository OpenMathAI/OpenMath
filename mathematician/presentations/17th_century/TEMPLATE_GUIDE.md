# TEMPLATE_GUIDE — 17 世纪数学家立传执行模板（标杆：Johann Bernoulli）

> 所有立传 agent 执行前必读。黄金参照：`17th_century/Johann_Bernoulli/Johann_Bernoulli_zh.tex`（逐帧改写，勿凭空另起炉灶）。

## 1. 目录与文件

每人一个文件夹 `17th_century/<Name>/`，内含：

```
<Name>/
├── <Name>_zh.tex          # 主文件（由 Johann_Bernoulli_zh.tex 逐帧改写）
├── Makefile               # 从 Johann_Bernoulli/Makefile 复制，仅改两行：
│                            MAIN = <Name>_zh
│                            VIDEO_NAME = <Name>_zh
└── images/
    └── <x>_portrait.jpg   # 肖像（见 §3）
```

共享封面：`\input{../../cover/openmath_page.tex}`（无参数，直接复用，勿改）。

## 2. 帧结构（14 帧，与 Johann 完全同构）

| # | 宏名 | 内容 |
|---|---|---|
| 1 | `\openmathslide` | 共享封面（\input，不改） |
| 2 | `\titleslide` | 人物封面：国籍行 + 大标题 + 生卒 + 成就行 + 分隔线 + 四分类 badge + 一句话定位 + 右上肖像 + 底部三要素 |
| 3 | `\profileslide` | 身份信息页（★ 必做）：左肖像 + 右 2×2 信息网格 |
| 4 | `\timelineslide` | 时间线（竖轴 8 个节点，`\foreach \y/\year/\txt`） |
| 5 | `\earlyslide` | 早年与教育（`p{2.2cm}|X|p{3.0cm}` 三列表格） |
| 6–12 | 各人自定义 | 7 个核心贡献/叙事页（`m{3.4cm}|X|p{3.0cm}` 表格 + `\fcolorbox` 公式框，参照提示词 §4） |
| 13 | `\honorslide` | 荣誉与传承（表格，可含 itemize） |
| 14 | `\closingslide` | 终章（两行大字 + 分隔线 + 两行小字 + 底部品牌行 `OpenMathAI`） |

命名惯例：贡献页宏用人物语义名（如 `\primeslide`、`\lawslide`），`\begin{document}` 后按序调用 14 个宏。

## 3. 配色（每个人不同，见提示词 §3）

- 保留 Johann 的结构：`bgmain`、主色、强调色（金 `#C9A227` 沿用）、`badgeA/B/C/D` 四分类色、`coverdark/covermuted/titlecolor/muteddark` 与四个 `panel` 色照抄 Johann 的 RGB 逻辑（主色系浅化做 panel：如 Johann `calcpanel` 是 badgeCalc 的浅底）
- 宏名用通用名（`mainclr`、`accentclr`、`badgeA..badgeD`、`panelA..panelD`），注释里写人物语义（如 `% 主色（法兰西蓝）— 法国`）
- `deckbackground` 气泡背景四圆分别用 badgeA/B/C/D，结构照抄

## 4. 肖像下载（Mac 环境有网络）

```bash
mkdir -p images
# 本地 images.txt 已有 URL 的（优先，250px 可改 500px 提清晰度）：
curl -sL -A "Mozilla/5.0" "https://upload.wikimedia.org/..." -o images/<x>_portrait.jpg
# 本地无肖像的，按序尝试 Commons Special:FilePath（文件名存在则返回图片）：
curl -sL -A "Mozilla/5.0" "https://commons.wikimedia.org/wiki/Special:FilePath/<File%20name>.jpg?width=600" -o images/<x>_portrait.jpg
file images/<x>_portrait.jpg   # 必须验证是 JPEG/PNG 而非 HTML 错误页
```

- 验证失败（HTML/404/小于 5KB）→ 换文件名再试 1–2 次 → 仍失败用**装饰圆占位**：
  把肖像 node 替换为：
  ```latex
  \node[draw=accentclr!50, line width=1.2pt, rounded corners=6pt, fill=white, inner sep=2pt]
    at (...) {\begin{tikzpicture}\clip[rounded corners=4pt] (0,0) rectangle (2.0,2.9);
      \node[font=\fontsize{40}{40}\selectfont, text=accentclr!60] at (1.0,1.45) {\faIcon{user}};\end{tikzpicture}};
  ```
- tex 中引用文件名 `<x>_portrait.jpg`；`\graphicspath{{images/}}`

## 5. 编译循环（最重要）

```bash
cd 17th_century/<Name>
make distclean && make      # latexmk 自动多遍编译
grep -c "Overfull" <Name>_zh.log   # 有则修（<10pt 可接受，超出必须改）
```

- 编译错误逐个修：常见坑 = 中文引号进 LaTeX、未转义 `%&#`、公式框过宽、表格 X 列文字过长溢出
- 每写完 tex 立即 make，看到溢出就修，直到 0 error 且 Overfull 全部 <10pt

## 6. 已知陷阱（前车之鉴，必查）

1. `\enspace` 在 profile 页结构下会丢 P1 顶部元素 → 信息网格内用 `\quad`
2. `remember picture` 需两遍编译（latexmk 自动多遍，勿改单遍）
3. tikzpicture 选项 `[]` 与 `{}` 不匹配会破坏编译
4. `\fontsize{a}{b}\selectfont` 不得有多余反斜杠
5. 代码/正文中的引语用半角引号 `" "`；品牌行统一 `OpenMathAI`
6. 文件统一 LF 行尾
7. **事实红线**：所有事实以对应提示词 md（§1/§2/§5/§7/§8/§9）为准；§5 史实陷阱逐条核对；引语必须是提示词标明的 Wikipedia 原文，勿造伪引语；MD5 级核对生卒/国籍/称号表述
8. 若写作中发现提示词与 pages/<Name>/page.md 冲突，以 page.md 为准并把修正**写回提示词 md**

## 7. 完成标准（每人）

- [ ] `<Name>_zh.pdf` 生成成功，共 14 页
- [ ] 编译 0 error，Overfull 全部 <10pt
- [ ] 封面：国籍行 + 头像（或占位）+ 四 badge + 底部三要素
- [ ] 身份信息页、时间线页、7 贡献页、荣誉页、终章齐备
- [ ] 底部品牌 `OpenMathAI`
- [ ] 事实与提示词 §5 逐条对齐（Review-1 事实终审）
- [ ] 不做视频（mp4 由主控统一安排）
