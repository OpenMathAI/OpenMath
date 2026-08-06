# 数学家立传工作指南

> 基于 Grothendieck 制作全过程总结，供后续为其他数学家立传参考。
> 最后更新：2026-08-03

---

## 一、目录结构

每位数学家的 Beamer 演示文稿放在独立的子目录中：

```
/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/
├── fetch_full_pages.py        ← 下载 Wikipedia 页面的脚本
├── fetch_mathematicians.py    ← 采集数学家名单的脚本
├── mathematicians.md          ← 全量数学家名单
├── pages/                     ← Wikipedia 页面本地存档
│   ├── INDEX.md
│   ├── Alexander_Grothendieck/
│   │   ├── page.md
│   │   ├── page.html
│   │   ├── metadata.json
│   │   └── images.txt
│   └── ...
├── presentations/             ← Beamer 演示文稿
│   ├── 数学家立传工作指南.md     ← 本文档
│   └── grothendieck/
│       ├── Alexander_Grothendieck_zh.tex
│       ├── Makefile
│       └── images/
│           ├── portrait.jpg
│           └── ...
├── gauss/
│   └── ...
└── hilbert/
    └── ...
```

`music_audio/` 目录（音乐库，与 presentations 同级）：

```
/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/
├── curated_tracks.md           ← ★ 精选曲目汇总（选曲必读）
├── download_guide.md           ← YouTube 音乐下载操作指南
├── .gitignore                  ← 排除 *.wav / *.mp3 / *.flac
├── alex-productions/            ← Alex-Productions 史诗/纪录片风格
├── beethoven-karajan/           ← 贝多芬交响乐全集（Karajan 指挥）
├── inspiring-electronic/        ← 电子/电影/情感风格合辑
├── lakey-inspired/              ← LAKEY INSPIRED 轻电子/Chill
└── pop-mixed/                   ← 流行/混合风格
```

> **背景音乐工作机制**：每位数学家的 Makefile 中有 `BGM = $(wildcard *.wav)`。将选好的 `.wav` 文件复制到该数学家的子目录下，`make video` 时自动混入。`.wav` 不入 git（已在 .gitignore 排除）。

---

## 二、工具链与编译

### 2.1 必需工具

| 工具 | 用途 |
|------|------|
| XeLaTeX | 中英混排编译引擎 |
| `latexmk` | 自动多轮编译 |
| `pdftoppm` | PDF → PNG 导出 (`make images`) |
| `ffmpeg` | 幻灯片视频合成 (`make video`) |
| `PingFang SC` | 中文正文字体 (macOS 自带) |
| `Helvetica Neue` | 英文正文字体 (macOS 自带) |
| `fontawesome5` | 图标 (⭐ 🔬 📚 等) |

### 2.2 Makefile 关键目标

```makefile
make              # 编译 PDF
make images       # 导出每页为 600dpi PNG
make video        # 合成 MP4 视频（每页 7 秒）
make clean        # 清理中间文件
make distclean    # 清理中间文件 + PDF + 图片 + 视频
```

**注意事项：**
- `latexmk` 需要跑两次才能正确生成交叉引用和页码
- 编译后删除 `.nav` `.snm` `.xdv` 避免残留
- 同一 Makefile 可直接复制到新数学家子目录，只需修改 `MAIN` 变量

---

## 三、Beamer 模板关键结构

### 3.1 文件骨架

```
\documentclass[aspectratio=169,14pt]{beamer}   ← 16:9 宽屏
\usetheme{default}\usecolortheme{default}
\setbeamertemplate{navigation symbols}{}        ← 隐藏导航按钮
\setbeamertemplate{footline}{...}               ← 页脚页码

\usepackage{fontspec}           ← 字体
\usepackage{xeCJK}              ← 中文
\usepackage{tikz}               ← 矢量绘图（核心！）
\usepackage{graphicx}
\usepackage{fontawesome5}       ← 图标

\graphicspath{{images/}}        ← 图片根目录

% ===== 配色定义 =====
% ===== 辅助命令 (\plainbar, \deckbackground, \sectiontitle) =====
% ===== 逐页 \newcommand =====

\begin{document}
\slide1
\slide2
...
\end{document}
```

### 3.2 配色体系

每个数学家应设计**专属主色调**（反映人物气质）：

| 数学家 | 主色方案 |
|--------|---------|
| Grothendieck | 深靛蓝紫 `#3B2A6B` + 金 `#C9A227`（教皇、权威）|
| Euler | 建议：深蓝 + 古典金 |
| Riemann | 建议：墨绿 + 银灰 |

需要定义以下色彩层级：

| 用途 | 变量名 | 说明 |
|------|--------|------|
| 背景 | `bgmain` | 整篇底色 |
| 主色 | `coverprimary` | 标题、主文本 |
| 强调色 | `coveraccent` | 分隔线、点缀 |
| 深色文本 | `coverdark` | 正文主要文本 |
| 浅色文本 | `covermuted` | 辅助信息、说明 |
| 四色标识 | `badgescheme`, `badgetopos`, `badgecoh`, `badgemot` | 四个核心概念分类色 |
| 面板色 | `purplepanel`, `amberpanel`, `greenpanel`, `bluepanel`, `goldpanel`, `graypanel` | 信息面板背景 |

### 3.3 三个核心辅助命令

```latex
% 底部装饰线（多数页面使用）
\plainbar

% 封面/结尾背景（圆点 + 网格 + 底部线）
\deckbackground

% 统一样式的标题区（金色分隔线）
\sectiontitle{主标题}{斜体副标题}
```

### 3.4 OpenMath 项目首页（★ 统一使用 cover 模板）

**所有数学家的 Beamer 演示文稿，第 0 页（OpenMath 项目首页）必须使用统一的 cover 模板，禁止各自内嵌。**

**模板位置：**

```
mathematician/presentations/cover/
├── OpenMath_Cover.tex   ← 独立单页封面 (80行, 自包含)
└── Makefile             ← pdf / clean / distclean
```

**使用方法：**

```latex
% 在 \begin{document} 中直接 \input 该模板，不要自行重写
% 注意：需要引入模板所需的配色变量（见下方）
\begin{document}
\input{../cover/OpenMath_Cover.tex}  % ← 第 0 页
\openmathslide                       % ← 如果模板内未直接执行
% ... 后续页面 ...
\end{document}
```

**或者更简单的方式** — 直接从模板复制 `\openmathslide` 定义到自己的 tex 文件中（preamble 配色部分与模板保持一致即可）。

**模板包含的设计要素（不可修改）：**

| 元素 | 说明 |
|:--|:--|
| 标题 | "OpenMath已开放源码" |
| 副标题 | "为 10,000+ 位数学家立传" |
| 6 大特性 | 10,000+ 数学家 / 人物生平 / 数学贡献 / 荣誉与传承 / 数学谱系 / 开放共建 |
| 6 个彩色图标 | `\faBook` 亮青绿 / `\faMap` 亮青 / `\faTh` 靛蓝 / `\faTrophy` 暖金 / `\faGlobe` 青绿 / `\faFlask` 暖灰褐 |
| 引言框 | "数学史，不应该只存在于少数人的书架上。" |
| GitHub CTA | `Star OpenMath · github.com/OpenMathAI/OpenMath` |
| 底部 | 版权提示行 |

**允许自定义的部分（必须与数学家配色一致）：**

- 底部横线和填充色使用该数学家的 `coverprimary` / `coveraccent`
- 引言框颜色使用该数学家的 `goldpanel`

**为什么要统一：**

1. **品牌一致性** — 每套 Beamer 的第 0 页都传达同一个 OpenMath 品牌
2. **维护效率** — 文案或链接变更时，只需改 cover 模板一处
3. **减少重复代码** — 避免每个数学家 tex 文件中重复 ~50 行相同的 openmathslide 定义
4. **图标彩色** — 模板中的 6 个图标已各自独立配色，直接复用即可

> ⚠️ **禁止**自行重写 `\openmathslide`。如果模板需要微调（如配色适配），应在模板中完成，而非在每个数学家文件中单独修改。

### 3.5 封面国籍徽章（★ 强制规则）

**每个数学家的封面页必须显式展示国籍信息，以国籍徽章形式出现在封面上。**

#### 位置要求

国籍信息必须出现在以下至少两处：

| 位置 | 说明 |
|:--|:--|
| **封面中段**（tagline 与 badge 行之间） | 国籍标识行：`\faIcon{globe}\enspace 国籍A $\rightarrow$ 国籍B`，字号 8.5pt |
| **封面底部栏**（`\faIcon{medal}` 行） | 底部信息行末尾，用 `\|` 分隔 |
| **早期生平幻灯**（"早年"页） | 出生地后紧跟括号注明当时所属国家/帝国 |

#### 国籍书写规则

- **按当时所在实体写**：例如奥匈帝国出生→奥匈帝国，而非直接写后来的国家
- **写明演变路径**：国籍A → 国籍B，例如 `苏联 → 俄罗斯`、`俄国 → 苏联`、`奥匈帝国 → 波兰第二共和国`
- **海外移民/逃难应注明年份**：例如 `奥地利 → 美国（1948年入籍）`

#### 示例

| 数学家 | 封面国籍标识 |
|--------|------------|
| Vladimir Arnold | `\faIcon{globe}\enspace 苏联 $\rightarrow$ 俄罗斯` |
| Igor Shafarevich | `苏联 → 俄罗斯` (底部) |
| Stefan Banach | `奥匈帝国 → 波兰第二共和国` |
| Kurt Gödel | `奥地利 → 美国（1948年入籍）` |
| John von Neumann | `匈牙利 → 美国（1937年入籍）` |

#### 提示词中的国籍表述

在每个数学家的立传提示词中，封面描述部分必须包含：
```
- **国籍**: 主权实体A → 主权实体B（封面显式展示：{{国旗图标}} 主权实体A → 主权实体B）
```

---

## 四、史实审查清单（★ 最重要的经验）

> **核心教训：第一版几乎必然存在史实错误，必须经过多轮核查。**

### 4.1 常见史实陷阱

| 类型 | 示例（Grothendieck） | 教训 |
|------|---------------------|------|
| **年份边界** | 无国籍：1945→1940→最终确认为 1945–1971 | 多来源交叉验证，必要时用区间表述 |
| **因果夸张** | IHÉS "为他而建" → 实际是 Dieudonné 提条件 | 不编造戏剧性，查机构官方历史 |
| **事件的精确性质** | "拒领菲尔兹奖" → "拒赴莫斯科领奖" | 查清是拒绝奖项本身还是拒绝出席 |
| **时间混淆** | 1966 Fields Medal 和 1967 河内之行混为同年 | 拆分事件，各自标注确年份 |
| **理论归属过度** | Tôhoku 论文是六运算唯一源头 → 实际是后续发展 | 查清理论发展的真实时间线和贡献者 |
| **出版年份** | Récoltes et Semailles 2022 年出版 → 2021 年 | 查出版社官网、权威数据库 |
| **手稿年份** | Les Dérivateurs (1987) → (1990–91) | 学术机构数据库 (MacTutor、MathSciNet) 优先 |

### 4.2 史实审查方法论

```
第一遍自查：Wikipedia / MacTutor 核对关键日期
第二遍外审：数学史专家或深度爱好者挑错
第三遍精修：针对每个数字、每个引号逐条确认
第四遍微调：最终年份措辞（区间 vs. 精确年份）
```

**重要原则：**
- **宁可模糊不可编造** — 不确定就用"约"、"据传记记载"、"在此前后"
- **区分事实与叙事** — "建立机器"比"铺平证明之路"更准确
- **措辞留余地** —"深刻影响"优于"直通"，"系统性的推广"优于"自动成立"

---

## 五、术语翻译规范

### 5.1 最高优先级：避免概念性错误

| 英文 | ❌ 错误译法 | ✅ 正确译法 | 原因 |
|------|-----------|-----------|------|
| anabelian geometry | 非阿贝尔几何 | **远阿贝尔几何** | an- + abelian ≠ non-abelian |
| tame topology | 驯化拓扑 | **温和拓扑** | 更自然的数学文献译法 |
| regular polyhedra | 正则多面体 | **正多面体** | regular polygon = 正多边形 |
| topological tensor products | 张量积 | **拓扑张量积** | 博士论文原题关键词 |
| Schemes | - | **概形** | 中文标准译法 |
| Topos | - | **拓扑斯** | 中文标准译法 |
| Motives | - | **动机** | 中文标准译法 |
| étale cohomology | - | **平展上同调** | 中文标准译法 |
| crystalline cohomology | - | **晶体上同调** | 中文标准译法 |
| derived category | - | **导出范畴** | 中文标准译法 |

### 5.2 外文全称展示策略

凡是缩写，首次出现时给出全称 + 法文/英文原文：

| 缩写 | 处理方式 |
|------|---------|
| IHÉS | `Institut des Hautes Études Scientifiques` |
| ENS | `École Normale Supérieure` |
| EGA | `Éléments de Géométrie Algébrique` |
| SGA | `Séminaire de Géométrie Algébrique` |
| FGA | `Fondements de la Géométrie Algébrique` |

**地名同样需要双语：**

| 中文 | 外文 |
|------|------|
| 蒙彼利埃 | Montpellier |
| 南锡 | Nancy |

### 5.3 中英双行展示模式

对于概念列表（如"十二个伟大思想"），推荐每个方框拆为两行：

```
{中文术语\\
English term}
```

而非混排在同一行。

---

## 六、TikZ 布局实战经验

### 6.1 微调元素位置

TikZ 使用物理单位（cm、pt），不依赖屏幕像素。微调时以 **0.1cm ≈ 3–4pt** 为基准步长即可。

### 6.2 溢出问题的统一修复策略

当页面底部或元素间出现溢出/重叠时，按以下优先级处理（从轻到重）：

| 优先级 | 手段 | 效果 | 何时用 |
|:--:|------|------|------|
| 1 | **删除装饰元素** (`\plainbar`, `\deckbackground` 等) | 释放 ~0.4cm 底部空间 | 最先尝试，对页面信息无损 |
| 2 | **缩小 inner sep** (9pt→5pt→3pt) | 边框收紧，释放内部空间 | 面板内容刚好超出一点点 |
| 3 | **缩小内容字号** | 减少行数，缩小行高 | 多行文字导致的溢出 |
| 4 | **减少空行间距** (`\\[2pt]` → `\\[1pt]`) | 微调，释放 ~0.1–0.3cm | 缩字号后仍差一点 |
| 5 | **缩小底部面板字号 + inner sep** | 对底部面板单独压缩 | 前面手段仍不够 |
| 6 | **上移节点 y 坐标** | 整体抬高 | 最后手段，容易打破整页视觉平衡 |

**核心原则：**
- 先删装饰 → 再缩边框 → 再缩字号 → 最后调坐标
- 调坐标是最粗暴的手段，先试完所有更优雅的手段
- 如果调坐标后视觉不平衡，宁可考虑拆分为两页

### 6.3 拥挤页面处理

当内容过多导致视觉拥挤时：

| 手段 | 效果 |
|------|------|
| 去掉 `\deckbackground` 网格和圆点 | 视觉清爽 |
| 增加 y 间距 | 元素间呼吸感 |
| 缩小字号 + 增大行距 | 信息密度可控 |
| 金句面板宽度收窄 (13→12cm) | 页边留白 |
| 双列布局间距加大 | 左右分明 |

### 6.4 序号圆圈与文字重叠修复

```
圆圈位置: xshift=-0.06cm   (让圆圈坐落在方框左边缘)
文字缩进: \hspace{0.95em}  (给圆圈留出空间)
```

---

## 七、多轮迭代中的崩溃修复

### 7.1 缺失闭合括号

大段 `replace_in_file` 操作时，最容易**意外删掉 `}` 或 `\end{tikzpicture}`**。

**预防措施：**
```
每次大段替换后立即编译验证
编译失败 → 用 python 脚本统计 begin/end 配对
```

```python
# 快速诊断工具
python3 -c "
with open('file.tex') as f:
    content = f.read()
for env in ['frame','tikzpicture','center','columns']:
    begins = content.count('\\\\begin{' + env + '}')
    ends   = content.count('\\\\end{'   + env + '}')
    if begins != ends:
        print(f'{env}: begin={begins}, end={ends} *** MISMATCH ***')
"
```

### 7.2 特殊字符转义

`replace_in_file` 要求 old_string 和 new_string 中的**反斜杠、引号等保持原样**，不需额外转义。但以下情况要小心：

- `\\` 在 Python/JSON 中会被二次转义
- 中文引号 `"` `"` (全角) 与 `"` (半角) 不同
- `–` (en-dash) ≠ `-` (hyphen) ≠ `---` (em-dash)

---

## 八、Git 工作流建议

### 8.1 Commit 策略

```
每个数学家的子目录独立成 commit
标题格式: "add presentations/{name}: Beamer deck for {Name}"
```

### 8.2 Rebase 合并

多次微调后，将相邻 commits 合并成一个：

```bash
# 假设要将顶部 5 个 commit 合并为 1 个
git reset --soft HEAD~5
git commit -m "consolidate: complete {Name} presentation"
```

**注意：** 合并后的 commit message 不要出现 "squash" 字样。

---

## 九、项目首页模板

每个数学家的演示文稿开头应插入统一的 OpenMath 项目首页：

```
\newcommand{\openmathslide}{%
\begin{frame}[plain]
  % 纯净浅色背景
  % 标题: OpenMath已开放源码
  % 副标题: 为 10,000+ 位数学家立传
  % 描述段
  % 六个特性双列
  % 金句
  % CTA: ⭐ Star · github.com/OpenMathAI/OpenMath
\end{frame}
}
```

然后：

```latex
\begin{document}
\openmathslide     ← 项目首页
\titleslide        ← 该数学家封面
...
\end{document}
```

---

## 十、Wikipedia 页面下载（前置步骤）

> **在开始写 Beamer 之前，必须先将该数学家的 Wikipedia 页面下载到本地。**
> 这是所有内容的事实基础，也是史实审查的起点。

### 10.1 脚本位置

```
/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/fetch_full_pages.py
```

### 10.2 输出目录

```
/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/
```

### 10.3 每个数学家生成的文件

```
pages/{Name}/
├── page.md           ← Wikipedia 正文 Markdown（含 YAML frontmatter）
├── page.html         ← 原始 HTML 备份
├── metadata.json     ← Wikidata 元数据（生卒、国籍、领域、获奖、导师等）
└── images.txt        ← 页面内所有图片 URL 清单
```

同时在 `pages/INDEX.md` 自动生成索引入口。

### 10.4 用法

```bash
cd /Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician

# 依赖安装（首次）
pip install requests beautifulsoup4 markdownify

# 示例：抓 5 位著名数学家（测试用）
python3 fetch_full_pages.py --sample

# 从 mathematicians.md 批量抓取（与上一步生成的人名列表联动）
python3 fetch_full_pages.py --from-md mathematicians.md --limit 20

# 从纯文本名单抓取（每行一个人名）
python3 fetch_full_pages.py --from-list names.txt
```

### 10.5 metadata.json 包含的字段

| 字段 | 说明 | 示例 |
|------|------|------|
| `name` | 数学家姓名 | `"Alexander Grothendieck"` |
| `qid` | Wikidata 条目 ID | `"Q134146"` |
| `label` | Wikidata 标签 | `"Alexander Grothendieck"` |
| `description` | 一句话描述 | `"French mathematician (1928–2014)"` |
| `date_of_birth` | 出生日期 | `"1928-03-28"` |
| `date_of_death` | 逝世日期 | `"2014-11-13"` |
| `nationality` | 国籍 | `["France"]` |
| `field_of_work` | 研究领域 | `["algebraic geometry", ...]` |
| `doctoral_advisor` | 博士导师 | `["Laurent Schwartz"]` |
| `doctoral_student` | 博士生 | `["Pierre Deligne", ...]` |
| `educated_at` | 教育经历 | `["University of Montpellier", ...]` |
| `employer` | 任职机构 | `["Institut des Hautes Études Scientifiques", ...]` |
| `award_received` | 获奖 | `["Fields Medal (1966)", ...]` |

### 10.6 下载后必做

```
1. 打开 page.md，速读全文，建立时间线和关键事件清单
2. 核对 metadata.json 的日期（生卒、获奖年份等）
3. 从 images.txt 中挑选高质量图片（portrait + 3–5 张辅助图片）
4. 交叉验证：MacTutor、MathSciNet、机构官网
```

---

## 十一、推荐制作流程（从零到成品）

```
第 0 步：下载 Wikipedia 页面 → pages/{Name}/  ★ 前置必须
          ↓  阅读 page.md 全文，逐段标记关键事件
          ↓  核对 metadata.json 的日期、导师、学生、获奖
第 1 步：建立目录 (presentations/{name}/)
第 2 步：复制 Makefile，修改 MAIN 变量
第 3 步：收集图片 (portrait + 3–5 张辅助图片)
第 4 步：阅读 Wikipedia / MacTutor / 机构官网，建立时间线
          ↓  参考 §十四「17 个进阶陷阱」逐条自检
第 5 步：设计配色方案（反映人物气质，须与已有人物配色区分）
第 6 步：编写骨干 slide (封面 → 生平 → 数学 → 遗产 → 结尾)
第 7 步：逐页填充内容，每页编译验证
第 8 步：第一轮史实审查（§四 + §十四清单，至少 2 轮自查）
第 9 步：术语审查（§五，重点查概念性错误）
第 10 步：布局微调（§六+§十三，溢出检查、间距调整、视觉审查）
第 11 步：插入 OpenMath 项目首页
第 12 步：编译 → 生成图片 → 视觉逐页确认
第 13 步：★ Wikipedia 本地文档终审（§十七） — 对照 page.md 全面 review
          ↓  事实错误、术语翻译、重大遗漏、结构性错误、编译告警
          ↓  修复所有 P0 问题，评估 P1/P2 问题
第 14 步：最终编译 → git commit
第 15 步（可选）：make images → make video → 配 BGM
```

---

## 十二、常见错误的速查表

| 症状 | 原因 | 解决 |
|------|------|------|
| `File ended while scanning` | 缺失 `}` 或 `\end{tikzpicture}` | 用脚本统计 begin/end 配对 |
| 底部溢出 | 页面内容太长 | 删 `\plainbar` → 调 y 坐标 → 缩字号 |
| 序号与文字重叠 | xshift 太靠右 | xshift 改负值 + hspace 增大 |
| 编译两次页码相同 | `latexmk -c` 清除了 .aux | 确保跑两次 xelatex |
| 中文显示为方块 | CJK 字体未安装 | macOS: 确认 PingFang SC 可用 |
| replace_in_file 匹配失败 | 引号、en-dash 等字符不一致 | 直接从文件复制 old_string |

---

## 十三、通过 LaTeX 告警检测重叠与溢出 ★

> **核心发现：TikZ 节点间重叠（视觉上看得出）≠ LaTeX 能直接报错。**  
> LaTeX 只能检测到"内容超出页面边界"的溢出，无法检测"两个节点在页面内部相互重叠"。  
> 因此需要**告警分析 + 视觉审查**双管齐下。

### 13.1 两类问题的检测方式对比

| 问题类型 | LaTeX 能检测？ | 告警形式 | 示例 |
|---------|:--:|---------|------|
| **水平溢出** (文字超出页面右边界) | ✅ 能 | `Overfull \hbox (XXpt too wide)` | URL 过长、无断行点的长串英文 |
| **垂直溢出** (内容超出页面底部) | ✅ 能 | `Overfull \vbox (XXpt too high)` | 4~5 个堆叠面板 + 底部引用框超过页面高度 |
| **TikZ 节点间重叠** (两个 node 视觉上压住对方) | ❌ 不能 | 无告警 | 就职演讲页、黎曼猜想页 — 堆叠 item node 间距过小 |
| **底部元素与页脚重叠** | ⚠️ 部分 | `Overfull \vbox` + 视觉确认 | Göttingen 教授页 — 底部面板与 `\plainbar` 重叠 |

### 13.2 告警分析流程

每次编译后执行以下命令：

```bash
# 只抓告警行，快速扫描
xelatex -interaction=nonstopmode file.tex 2>&1 | grep "Overfull"

# 输出示例：
# Overfull \hbox (153.06781pt too wide) in paragraph at lines 614--614
# Overfull \vbox (57.07875pt too high) detected at line 625
```

**解读规则：**

| 告警类型 | 严重度 | 含义 | 处理优先级 |
|---------|------|------|----------|
| `Overfull \hbox` < 20pt | 低 | 极轻微溢出，通常不可见 | 可忽略 |
| `Overfull \hbox` > 50pt | 高 | URL 或长英文单词未断行 | 必须修复 |
| `Overfull \vbox` < 5pt | 低 | 极轻微底部溢出 | 可忽略 |
| `Overfull \vbox` > 10pt | **严重** | 页面内容明显超出底部 | **必须修复** |

### 13.3 行号定位法

`at lines XXX--XXX` 指向的是页面调用命令所在行。以黎曼为例：

```
L614 → \hookslide          # Overfull hbox 153pt (URL 过长)
L619 → \maptheoremslide    # Overfull hbox 111pt (长文本无断行)
L620 → \habilitationslide  # Overfull vbox (4 item + 底部面板过高)
L625 → \hypothesisslide    # Overfull vbox 57pt (4 panel 严重溢出)
```

### 13.4 垂直溢出的标准修复

**详见 §6.2「溢出问题的统一修复策略」**，优先级从轻到重：删装饰 → 缩 inner sep → 缩字号 → 减空行 → 调坐标。

### 13.5 黎曼修复实测数据

| Slide | 问题 | 告警 | 修复前 y 跨度 | 修复后 y 跨度 | 缩减 |
|-------|------|------|-------------|-------------|------|
| 就职演讲 (habilitationslide) | 4 item + 底部面板重叠 | vbox 22pt | 5.15cm | 4.75cm | −8% |
| 黎曼猜想 (hypothesisslide) | 4 panel 底行与页脚重叠 | vbox 57pt | 5.05cm | 4.35cm | −14% |
| Göttingen 教授 (professorshipslide) | 4 item + 引语面板溢出 | vbox 12pt | 5.90cm | 5.40cm | −8% |
| 黎曼映射定理 (maptheoremslide) | 长文本无断行 | hbox 111pt | — | — | 插入 `\\` 断行 |

### 13.6 视觉审查：必须人工确认的盲区

LaTeX **无法检测**但肉眼可见的问题：

| 盲区类型 | 表象 | 确认方法 |
|---------|------|---------|
| 节点间距离过近 | 两个面板的文字几乎贴在一起 | 生成 PDF 逐页翻看 |
| 文字被裁切 | 面板内文字末尾被截断 | 打开 PDF 检查每个 panel |
| 颜色/对比度问题 | 浅色文字在浅底色上不可见 | 在普通屏幕（非 Retina）上查看 |
| TikZ 内部元素碰撞 | 箭头、圆圈与文字重叠 | 逐页检查 tikzpicture 中的 node 位置 |

**推荐工具链**：
```bash
make images          # 导出每页为 600dpi PNG
# 在 Finder 中快速翻看 images/slide_*.png
# 发现可疑页面 → 回到 tex 源码精确定位
```

---

> **关键经验：Overfull vbox 告警是检测"内容过多导致溢出"的最高效手段。**  
> 如果某页的 vbox 告警 > 10pt，说明该页必定存在肉眼可见的溢出或重叠，必须修复。  
> hbox 告警通常来自未断行的长 URL 或英文单词，在 Beamer tikz 环境中多数无害。

---

## 十四、史实校正的进阶陷阱（★ 来自黎曼实战的新教训）

> 第一版做完后，邀请数学史背景的审阅者逐页挑错，暴露了大量 Grothendieck 模板未曾触及的问题。  
> 这些不是低级错误，而是**看似合理、实则必须深究的进阶陷阱**。

### 14.1 "N 篇论文"的计数陷阱

| 陷阱 | 黎曼案例 | 教训 |
|------|---------|------|
| 用整数断言"只有 N 篇论文" | "只有 10 篇论文" | 论文计数本身就有争议（已发表、未发表、合著、讲义），整数会变成可被攻击的靶子 |
| 正确写法 | "短短 39 年，留下十余篇奠基性工作" | 用"十余篇""主要著作""开创性论文"等非精确计数，气势不减、史实更稳 |

### 14.2 "第一"断言陷阱

| 陷阱 | 黎曼案例 | 教训 |
|------|---------|------|
| "第一次严格定义……" | 黎曼积分 ≠ 第一次严格积分定义（Cauchy 已有） | 19 世纪数学很少有严格的"第一"，多来源交叉验证后再下断言 |
| "第一个将拓扑不变量与……联系起来" | 亏格与函数空间维数的联系 | 去掉"第一个"，改为"里程碑式成就" |
| 正确写法 | "提供了深远的概念框架""是一个里程碑式的成就" | 用"核心贡献""深刻影响了"替代"第一次""第一个" |

### 14.3 年份标注的精确性陷阱

| 陷阱 | 黎曼案例 | 教训 |
|------|---------|------|
| 在标题中标注（不准确的）年份 | "黎曼映射定理 (1851)" | 1851 是博士论文年份，不是定理正式发表年份。标题里的年份会误导观众以为是发表时间 |
| 正确做法 | 标题去掉年份 → `黎曼映射定理：复分析的几何革命` | 除非能确认定理的正式发表日期，否则标题中不标年份；年份放正文中用"思想形成于……"表述 |

### 14.4 机构/学术术语的准确性陷阱

| 陷阱 | 黎曼案例 | 教训 |
|------|---------|------|
| "向哲学系提交了三道就职演讲题目" | 1854 年 6 月 10 日发表的是教授资格演讲 (Habilitationsvortrag) | 涉及德国大学制度（Habilitation、Privatdozent 等）的术语需要精确查证 |
| 正确写法 | "发表教授资格演讲 (Habilitationsvortrag)" | 机构名称、学术职称、学位制度 —— 严格查证原文术语 |

### 14.5 不可靠史料的引用陷阱

| 陷阱 | 黎曼案例 | 教训 |
|------|---------|------|
| "据目击者记载，他离开讲座时……" | Gauss 对黎曼演讲的反应 | 这类"目击者记载"的史料可靠性在数学史学界常有争议 |
| 正确写法 | "高斯罕见地激动不已，对黎曼思想的深度给予了高度评价 —— 这一场景在数学史上广为传颂。" | 承认史实存在，但不引述不可靠的细节；用"广为传颂"而非"据记载" |

### 14.6 伪引语陷阱（★★★ 最危险）

| 陷阱 | 黎曼案例 | 教训 |
|------|---------|------|
| 中文引号内的"黎曼原话" | "当然，我希望给出严格的证明，但在几次徒劳的尝试后，我暂时搁置了这一目标……" | 这类中文引语非常像现代文学化改写，不是黎曼的原文；数学史读者会直接质疑 |
| 正确写法 | "黎曼在论文中指出，他希望证明这一命题，但当时未能完成。" | **不要给数学家的中文引语加引号。** 用间接引语转述。如果一定要引用，请查德文/英文原文。 |

**黄金规则：**
- 中文引号 `""` 内的内容必须能在原文中找到对应原话
- 不确定 → **用间接引语，不加引号**
- 来自二手科普书的"名言"大概率是文学加工

### 14.7 人物时间线错误陷阱

| 陷阱 | 黎曼案例 | 教训 |
|------|---------|------|
| "他的工具后来被 Abel、Jacobi、Frobenius、Weil 等人发展……" | Abel (1802–1829) 和 Jacobi (1804–1851) 都比黎曼 (1826–1866) 早 | 写"后来被……发展"时，必须逐一核实每个人物的生卒年份 |
| 正确写法 | "黎曼继承并重新组织了 Abel、Jacobi 等人关于阿贝尔积分和周期函数的工作" | 区分前辈和后来者，正确使用"继承""发展为""推广到"等动词 |
| "他的学生 Gustav Roch" | Roch 并非黎曼的正式博士生 | 查 Wikidata 的 `doctoral_student` 字段。更准确说"与黎曼学派有关的数学家" |

### 14.8 科学措辞的过度简化陷阱

| 陷阱 | 黎曼案例 | 教训 |
|------|---------|------|
| "弯曲时空 = 引力。这不是诗，这是黎曼几何。" | GR 使用的是 pseudo-Riemannian / Lorentzian geometry | 科普式金句适合视频，但建议在数学上留余地 |
| 正确写法 | "广义相对论将引力描述为四维时空的几何结构，黎曼几何正是其数学语言。" | 区分"正定黎曼几何"与"拟黎曼几何"；至少不把等式写得过于绝对 |
| "素数分布 = ζ(s) 的零点分布！" | 太绝对 | 改为"素数分布的精细误差，与 ζ(s) 非平凡零点的位置密切相关。" |
| "C 上的代数曲线 = 紧黎曼面" | 一般代数曲线可能有奇点、非紧 | 改为"光滑射影复代数曲线对应于紧黎曼面" |

### 14.9 可更新数据的处理（★ 与 §15.4 统一结论）

| 陷阱 | 黎曼案例 | 教训 |
|------|---------|------|
| 固定写"前 $10^{13}$ 个零点已验证" | 随着计算能力增长，这个数字每年都在变化 | 任何随时间变化的数字都应避免固定数值 |
| 半修正写法 | "前万亿级乃至更高数量级的零点" | "万亿级"仍然在暗示一个量级，专业读者仍会追问"到底多少" |
| **最终正确写法** | "大量低位零点已通过计算验证位于临界线上，但有限计算不能代替证明。" | 用"大量""持续增长的"等非量化表述，彻底避开数字争议 |

**规则：不要固定任何一个随时间变化的数字。** 用"大量""持续增长的""不断推进的"等表述。
### 14.10 医学史细节的措辞

| 陷阱 | 黎曼案例 | 教训 |
|------|---------|------|
| "1862 年确诊肺结核" | 19 世纪医学诊断不如现代精确 | 改"被诊断为"或"健康状况急剧恶化，被认为患有肺结核" |
| 地名的史实完整性 | "小镇 Selasca" | 写为"Selasca（今意大利韦尔巴尼亚附近）"，或查证当时所属政区 |

### 14.11 多余脚注陷阱

| 陷阱 | 黎曼案例 | 教训 |
|------|---------|------|
| 从 Grothendieck 模板继承的 `\node[anchor=south]` 小字注释 | "共形映射 (conformal mapping) · 复分析中最优美的定理之一"、"黎曼的很多工作最初以物理问题为动机……" | 模板中的脚注模式不一定适用于每个数学家的每页 |
| 什么情况可以用脚注 | 术语密集、需要额外解释的页面 | 判断标准：删除这行脚注后，页面信息是否完整？如果完整 → 删 |
| 什么情况不应加脚注 | 页面本身三个面板已经解释清楚 | 画蛇添足只会导致溢出或视觉拥挤 |

### 14.12 结尾页的叙事升级经验

> **教训：不要停留在"你能证明黎曼猜想吗？"这种传统励志。**

| 旧结尾 | 新结尾 | 升级思路 |
|--------|--------|---------|
| "39年生命，10篇论文……黎曼猜想仍在等待它的征服者——你，会是那个人吗？" | "黎曼留下的真正遗产，不只是黎曼猜想。而是一种思想：把数变成函数，把函数变成空间，把空间变成几何。" | 从"挑战读者"升级为"总结思想"——更符合"数学家人物志"的高级感 |

**结尾页的核心原则：** 不只是列举贡献，而是提炼出这位数学家**改变了数学提问方式**的那个思想。

### 14.13 面板间距均匀化

| 问题 | 解决方法 |
|------|---------|
| 多个 item node 的中心 y 坐标间距相同，但视觉上不均匀 | 因为文字行数不同（有的 1 行、有的 2 行），等中心间距 ≠ 等空隙 |
| 正确做法 | **按白色空隙（节点底部到下一节点顶部的距离）为目标均分**，而非按中心坐标均分。两行文字的节点需要上移补偿 |

---

> **关键教训：Grothendieck 模板的成功不代表复制给其他数学家就没有问题。**  
> 每一位数学家的史实背景不同，审阅者最好是"熟悉该数学家但不熟悉本项目的数学史读者"。  
> 他们往往能一眼看到你自己发现不了的问题。

---

## 十五、第二轮史实校改与视频制作经验（★ 来自黎曼的深度教训）

> 第一轮史实校改解决了"明显错误"。第二轮暴露了更深层的问题：不是错，而是**不够稳**。  
> 这些问题不会被普通观众发现，但会被数学家或数学史读者一眼抓住。

### 15.1 "稳" vs "对" —— 专业读者不只看你错没错

| 第一轮问题类型 | 第二轮问题类型 | 本质区别 |
|-------------|-------------|---------|
| 年份标错 (1851) | 标题中标注误导性年份 | "对"不一定"稳" |
| Abel/Jacobi 时间线颠倒 | "后来被…发展"措辞暗示的因果关系 | 措辞的微妙暗示 |
| 伪引语 | 对 Gauss 评价的中文引号 | 引号=声称原文 |
| "10篇论文" | "每一篇都改变了数学"→"深刻改变现代数学" | 宣传化 vs 纪录片化 |

**核心教训：**
- 第一轮解决"factually wrong"（事实错误）
- 第二轮解决"professionally unstable"（专业上站不住）
- 第二轮的关键词是：**引号必须对应原文、禁止过度宣传化、区分现代语言与历史语言**

### 15.2 数学语言的"历史意识"陷阱

> **不能用 21 世纪的数学语言包装 19 世纪的数学家。**

| 现代语言 | 历史准确表述 | 为何重要 |
|---------|------------|---------|
| "黎曼面是 1 维复流形" | "今天我们称之为黎曼面。在现代语言中，它是一个一维复流形。" | 黎曼本人不会用"复流形"这个公理化概念 |
| "黎曼直接建立了 Abelian variety 理论" | "黎曼的工作为后来 Jacobian 簇、Abelian 簇等核心理论奠定了重要基础。" | Abelian variety 是 20 世纪的成熟理论 |
| "提出 Riemann theta function" | "研究了阿贝尔积分、周期矩阵与 theta 函数之间的关系" | theta 函数不是黎曼从零发明的 |

**判断标准：** 这位数学家活着的时候，这个术语/概念是否存在？如果不存在 → 加"今天我们称之为…"或"为后来…奠定基础"。

### 15.3 传记轶事 vs 史实 —— 加"据传"

黎曼立传中遇到了多个经典传记轶事，处理原则：

| 轶事 | 处理方式 |
|------|---------|
| Legendre《数论》六天读完 | "据传，黎曼仅用六天便读完并掌握了这部 859 页的巨著。" |
| Gauss 离开讲座时的评语 | 不引"目击者记载"，改为"高斯罕见地激动不已……这一场景在数学史上广为传颂。" |
| 黎曼关于黎曼猜想的原话 | 不引中文引号，改为"黎曼在论文中指出，他希望证明这一命题，但当时未能完成。" |

**规则：** 只要不是来自原始文献（论文、书信、同时代可靠记载），就加"据传"或改用间接叙述。

### 15.4 伪精确数字陷阱

| 错误写法 | 正确写法 | 原因 |
|---------|---------|------|
| "前 $10^{13}$ 个零点已验证" | "大量低位零点已通过计算验证位于临界线上" | 计算验证数字每年都在变化 |
| "前万亿级乃至更高数量级的零点" | 同上 | "万亿级"仍然在暗示一个量级，不够模糊 |

**规则：** 不要固定任何一个随时间变化的数字。用"大量""持续增长的"等非量化表述。

### 15.5 溢出修复的实战教训

黎曼几何页（geoslide）反复溢出，验证了 §6.2 统一策略的优先级正确性：先收边框（inner sep 9→3pt）→ 再缩字号（7.2→5.2pt）→ 最后才调 y 坐标。详见 §6.2。

### 15.6 封面设计的迭代勇气

黎曼封面经历了三次迭代：

| 版本 | 设计 | 结果 |
|:--:|------|------|
| v1 | 大字标题 + 肖像 + 四色badge + "他改变了…" | 基础版 |
| v2 | 罗曼·罗兰引语 → 1826-1866 → 39年 → "他没有机会成为自己的影子" → 标题 | 文学性强但布局拥挤 |
| v3 | **回退到 v1** | 最终版 |

**教训：** 
- v2 的罗兰引语设计非常适合视频文案，但放在一页 Beamer 里太拥挤
- **好创意如果破坏了页面可读性，就应该回退。** 不是每个好想法都适合当前格式
- v2 的叙事智慧保留在了视频文案中（首尾呼应），只是不在封面页上展示

### 15.7 音乐选择经验

> **音乐库位置**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/`
> **精选曲目汇总**：`music_audio/curated_tracks.md`（★ 选曲前必读）
> **使用方法**：从音乐库中复制选定的 `.wav` 文件到该数学家的子目录下，`make video` 自动检测 `*.wav` 并混入。

#### 音乐库概览

| 来源 | 目录 | 风格 | 曲目数 | 适合场景 |
|------|------|------|:--:|------|
| Alex-Productions | `alex-productions/` | 史诗/纪录片/沉稳 | 14 精选 | 宏大叙事、时间线、人物回顾 |
| Beethoven · Karajan | `beethoven-karajan/` | 古典交响乐 | 5 部完整交响曲 | 里程碑、结尾升华、古典气质 |
| Inspiring Electronic | `inspiring-electronic/` | 电子/电影/情感 | 11 精选 | 悲剧人物、现代感、攻克难题 |
| LAKEY INSPIRED | `lakey-inspired/` | 轻电子/Chill | 12 首 | 轻松段落、过渡页 |

#### 选曲原则

- 不是所有数学家都需要 epic/heroic 风格
- 音乐气质应与数学家气质匹配（而非简单选择"好听"的）
- 优先从 `curated_tracks.md` 的精选列表中挑选
- BGM 时长略短于 slides 总时长时，ffmpeg `-shortest` 自动对齐

#### 按数学家气质推荐

| 数学家气质 | 推荐来源 | 推荐曲目示例 | 理由 |
|-----------|---------|------------|------|
| **史诗/英雄/教皇** (Grothendieck, Hilbert) | Alex-Productions | New Lands, Expedition | 宏大开阔，匹配"改变数学史"的气质 |
| **深沉/克制/理性** (Riemann, Gödel) | Alex-Productions, Beethoven | Timeless, PAST, Symphony No.7 | 内敛的深度，而非宏伟征服 |
| **温暖/人文/咖啡馆** (Banach, Serre) | Alex-Productions | Nostalgia, With Me | 温和怀旧，匹配人文气质 |
| **悲剧/黑暗/孤独** (Turing, Cantor) | Inspiring Electronic | Lonesome, Through the Darkness | 暗色调，情感深沉 |
| **探索/远征** (Grothendieck, Weil) | Alex-Productions | Expedition, Eternals | 远征式叙事，数学探索 |
| **古典/庄严** (Euler, Gauss) | Beethoven · Karajan | Symphony No.3 "Eroica", No.9 | 古典音乐的庄严与永恒 |
| **现代/科技/计算机** (von Neumann, Turing) | Inspiring Electronic | Falling Apart, Mirage | 电子质感，现代感 |
| **鼓舞/突破/年轻天才** (Galois, early Kolmogorov) | Alex-Productions | Awaken, Daylight | 明亮轻快，天才之光 |
| **苏联/厚重/力量** (Kolmogorov, Gelfand) | Beethoven · Karajan | Symphony No.5 | 力量与秩序的厚重感 |

#### 实战案例

| 数学家 | 选用音乐 | 来源 | 理由 |
|--------|---------|------|------|
| Grothendieck | New Lands | alex-productions | 教皇气质的数学革命者 |
| Riemann | Timeless | alex-productions | 克制天才、猜想永恒、39岁静默离世 |
| Banach | Nostalgia | alex-productions | 波兰咖啡馆的温暖与战争的伤痕 |
| Gödel | PAST | alex-productions | 深邃理性、维也纳知识分子的庄重 |
| Turing | Lonesome | inspiring-electronic | 冷峻、暗色中的光芒、悲剧英雄 |

#### 操作步骤

```bash
# 1. 打开 curated_tracks.md，根据数学家的气质挑选曲目
# 2. 复制选定的 .wav 到该数学家的子目录
cp /Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav \
   /Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/riemann/

# 3. make video 自动检测并使用
cd /Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/riemann/
make video
```

### 15.8 多轮校改的心态管理

> **不要盲从审阅意见，但也不要出于防御心态拒绝合理的批评。**

| 场景 | 黎曼案例 | 处理原则 |
|------|---------|---------|
| 审阅者建议改变叙事结构 | 罗兰引语封面设计 | 尝试后回退——尝试是尊重，回退是判断 |
| 审阅者指出措辞过度 | "每一篇都改变了数学" | 采纳——这是专业读者的真实感受 |
| 审阅者建议删除引号 | Gauss 评语、黎曼原话 | **坚决采纳**——引号是专业读者的红线 |
| 审阅者认可已有设计 | Riemann-Roch、39岁措辞 | "已很好，无需改"——不必为改而改 |

**黄金规则：如果三条独立审阅意见都指向同一个问题，那几乎一定需要修。如果只有一条，可以判断后决定。**

---

> **关键教训：第二轮校改的本质是从"没有错误"到"经得起专业审视"。**  
> 第一轮要做到 90 分，第二轮要做到 98 分。那 8 分的差距，就是"会被专业读者挑出来"的部分。



---

## 十六、Wikipedia 本地文档终审（★ 第 13 步必做）

> **核心原则：Beamer 写完后，必须回到本地 Wikipedia 存档（page.md + metadata.json），逐项对照审核。**
> 这一步不是"再读一遍"，而是系统性地、逐页逐字地交叉验证。
> 
> 为什么这一步必须放在最后？因为写作过程中会引入大量细节——日期、人名、术语、引语——
> 只有写完全部页面后，才能以"第三方审阅者"的视角来审视这些细节是否与 Wikipedia 一致。

### 16.1 终审清单

| # | 检查项 | 方法 | 高危信号 |
|:--:|------|------|---------|
| 1 | **事实性错误** | Beamer 中每个日期/人名/机构，与 page.md 逐条对照 | 任何与 Wikipedia 不一致的年份、地名、人名 |
| 2 | **翻译/术语错误** | 将 Beamer 中所有数学术语与 Wikipedia 英文原词对照 | 概念性误译（如 regular polyhedra → 正则多面体而非正多面体） |
| 3 | **重大遗漏** | 扫描 Wikipedia 目录，列出 page.md 覆盖的主要成就；对比 Beamer 是否都涉及 | 该数学家的标志性专著/定理在 Beamer 中只字未提 |
| 4 | **结构性错误** | 检查幻灯片时间线是否按生平顺序，同一时期的成就是否被拆散到不相邻的页面 | 时间跳跃混乱、因果倒置 |
| 5 | **编译告警** | 分析 `Overfull \hbox` 和 `Overfull \vbox`，判断是否有可见溢出 | vbox > 10pt 或 hbox > 50pt |
| 6 | **引语来源** | Beamer 中每个加引号的句子，必须在 page.md 或可靠来源中找到对应原文 | **中文引号内的任何句子无法在 Wikipedia 中找到** |
| 7 | **年份精确性** | 尤其注意 slide 标题中出现的年份——它们会被观众当作"正式发表年份" | 写作年份 ≠ 发表年份，初版年份 ≠ 修订版年份 |
| 8 | **人物关系** | metadata.json 的 `doctoral_advisor` / `doctoral_student` / `employer` 与 Beamer 表述一致 | 把"合作者"写成"学生"，把"访问学者"写成"教授" |
| 9 | **荣誉/获奖** | metadata.json 的 `award_received` 与封面页、遗产页一致 | 遗漏重大奖项，或奖项年份标错 |
| 10 | **出版年份** | Wikipedia 书目栏中的出版年份与 Beamer 中标注的年份一致 | 初版与再版年份混淆（如 Weyl 的《经典群》1939 而非 1938） |

### 16.2 终审执行流程

```
1. 打开 pages/{Name}/page.md，从头到尾逐段阅读
2. 同时打开 Beamer .tex 源码，逐页对照
3. 发现不一致 → 标注优先级（P0/P1/P2）
4. 全部扫描完毕 → 先修复所有 P0，再评估 P1，P2 可选
5. 修复后重新编译 → 确认零错误
```

### 16.3 优先级定义

| 优先级 | 定义 | 示例 |
|:--:|------|------|
| 🔴 P0 | **事实错误** — 会导致专业读者一眼看出错误 | 出版年份标错、遗漏关键教育经历、人物关系写错 |
| 🟡 P1 | **来源存疑/模糊** — 不一定是错的但经不起推敲 | 无法验证的引语、模糊的年份表述、可能被误解的措辞 |
| 🟢 P2 | **重要遗漏** — 缺了不会错，但补上会更好 | 未提及的标志性著作、可选轶事、深入背景 |
| ⚪ P3 | **可选补充** — 锦上添花 | 衍生影响（如 Weyl 半金属）、冷门趣闻 |

### 16.4 输出格式

终审完成后，输出一份结构化的 Review 报告：

```markdown
## 🔍 {Name} Beamer — Wikipedia 本地文档终审

### 🔴 事实性错误 (需修复)
| # | 位置 | 当前内容 | 问题 | 修正 |
|---|------|------|------|------|

### 🟡 来源存疑/术语审查
| # | 位置 | 当前内容 | 问题 | 修正 |
|---|------|------|------|------|

### 🟢 重要遗漏
| # | 遗漏内容 | Wikipedia 记载 | 建议 |
|---|------|------|------|

### 🟠 结构性/叙事性问题
| # | 位置 | 问题 | 建议 |
|---|------|------|------|

### 📊 逐页对照
| # | 标题 | 事实准确性 | 遗漏 | 评价 |
|---|------|:--:|:--:|------|

### 📋 修复优先级汇总
| 优先级 | 数量 | 类型 |
|:--:|:--:|------|
| 🔴 P0 | N | ... |
| 🟡 P1 | N | ... |
| 🟢 P2 | N | ... |
| ⚪ P3 | N | ... |
```

### 16.5 实战案例：Weyl 终审发现

以下是从 Weyl 实际终审中摘录的典型发现，展示各类问题长什么样：

| 优先级 | 发现 | 位置 |
|:--:|------|------|
| 🔴 P0 | 《经典群》出版年份标为 1938，Wikipedia 标注 [1939] | Slide 11 标题 |
| 🔴 P0 | 只写"哥廷根大学求学"，Wikipedia 明确记载也在慕尼黑大学学习 | Slide 3 正文 |
| 🟡 P1 | 引语"我不是离开德国——德国离开了我"在 Wikipedia 中无记载，实为 Thomas Mann 名言 | Slide 8 正文 |
| 🟡 P1 | 《数学与自然科学哲学》标注 1949，实际初版为 1927 | Slide 14 标题 |
| 🟢 P2 | *Raum, Zeit, Materie* (1918) — Weyl 标志性广义相对论教材，Wikipedia 目录独立条目，Beamer 未提及 | 新增至 Slide 5 |
| 🟢 P2 | *Das Kontinuum* (1918) — 数学基础奠基作，Wikipedia 独立章节，Beamer 未提及 | 新增至 Slide 7 |
| 🟠 结构化 | Slide 5 将 Weyl 方程(1929)和规范变换量子重解释(1929)混在同一节点讨论 | Slide 5 拆分 |

> **关键教训：即使是最认真撰写的第一版，终审也必然会发现 P0 级别的问题。这不是能力问题，而是人类注意力的事实——写作时关注叙事，审阅时关注事实，两者需要不同的心智模式。**

---

## 十七、给下一位数学家的快速启动清单

> 不重读 900+ 行指南也能开始。这是一个精简到一页的 checklist。

### 动手前

- [ ] 阅读本指南 **第四节（史实审查清单）** — 最重要的一节
- [ ] 阅读本指南 **第十四节（进阶陷阱）** — 避免第一轮就踩坑
- [ ] 阅读本指南 **第十五节（第二轮校改）** — 了解"不稳"是什么
- [ ] 阅读本指南 **第十六节（Wikipedia 终审）** — 了解写完后的系统审核方法

### 制作中

- [ ] **第 0 页（OpenMath 首页）必须使用统一模板 `cover/OpenMath_Cover.tex`**，禁止自行重写。详见 §3.4
- [ ] 使用现有的 prompts（如 `外尔立传提示词.md`、`韦伊立传提示词.md`）作为新对话的初始提示词模板（替换人名、路径、配色）
- [ ] 参照 `grothendieck/` 或 `weyl/` 或 `weil/` 下的完整源码
- [ ] 每写完一页立即编译
- [ ] 溢出处理：删装饰 → 缩 inner sep → 缩字号 → 调坐标（不要一上来就调坐标）
- [ ] 配色优先反映人物气质，而非随机选择

### 史实自检（任何数学家通用的红线）

| 绝对不要 | 正确做法 |
|---------|---------|
| 中文引号内写数学家"原话" | 间接引语；有原文才加引号 |
| 声称"第一次/第一个" | "核心贡献""里程碑式成就" |
| 标题中标注无法确认的年份 | 年份放正文，标题保留核心概念 |
| 固定写具体计算验证数字 | "大量""持续推进的" |
| "只有 N 篇论文" | "十余篇奠基性工作""主要著作" |
| 用 21 世纪术语包装 19 世纪数学家 | "今天我们称之为…""为后来…奠定基础" |

### Wikipedia 终审（★ 提交前必做）

- [ ] 打开 `pages/{Name}/page.md`，逐段阅读全文
- [ ] 对照 page.md 逐页检查 Beamer：
  - 日期（生卒、获奖、出版年份）
  - 机构（大学名、研究所名、拼写是否正确）
  - 人名（导师、学生、合作者、关系是否正确）
  - 引语（引号内的句子能否在 Wikipedia 中找到）
- [ ] 扫描 Wikipedia 目录 → 是否有重要著作/定理在 Beamer 中遗漏
- [ ] 分析编译告警 → vbox > 10pt 或 hbox > 50pt 必须修复
- [ ] 输出 Review 报告（按 §16.4 格式），标注 P0/P1/P2 优先级
- [ ] 修复所有 P0 → 重新编译 → 确认零错误 → git commit

### 审阅

- [ ] 找一位"熟悉该数学家但没参与本项目"的人审阅（如不可行，则严格按 §16 自行终审）
- [ ] 三条独立意见指向同一问题 → 必改
- [ ] **引号问题** 审阅者提出 → 坚决改
- [ ] 可以尝试审阅者的建议，也可以回退

### 制作视频

- [ ] 打开 `music_audio/curated_tracks.md`，根据数学家的气质挑选曲目（见 §15.7 按气质推荐表）
- [ ] 将选定的 `.wav` 复制到该数学家子目录下
- [ ] BGM 略短于 slides 总时长时，用 `ffmpeg -shortest` 对齐
- [ ] `make video` 验证最终效果

---

> **提示词模板：** `prompts/Hermann_Weyl_zh.md` 和 `prompts/Andre_Weil_zh.md` 是最新的提示词模板（已融合第十四、十五节的核心教训），位于 `prompts/` 目录下。
> 为下一位数学家立传时，复制其中一个文件，替换：
> - 人名、生卒年份、Wikipedia 路径
> - 配色方案（§3.2）
> - 第 4 步的时间线阶段划分
> - 第 6 步的 slide 序列规划
> - **音乐选择**（§15.7）：参照 `music_audio/curated_tracks.md` 按数学家气质选曲
> 
> 已在提示词中融合了伪引语、年代标注、音乐选择、史实陷阱等核心教训。

---

> **最后的话：** 为数学家立传，本质是"史实精修 + 数学深化"的迭代过程。  
> 第一版必然有错，关键是建立严谨的核查流程，让每一轮迭代都比上一轮更接近真相。  
> **写完不是终点，终审才是。** 对照本地 Wikipedia 逐页审核（§16），是区分"看起来不错"和"经得起专业审视"的那一步。