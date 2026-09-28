# 物理学家立传提示词（William Lawrence Bragg）

> 本文件是 OpenPhysicist「人物专属立传提示词」，以 Kenneth G. Wilson 标杆结构为骨架，为 William Lawrence Bragg（1915 诺贝尔物理学奖，史上最年轻科学诺奖得主）定制。
> 凡标注 `【模板通用】` 的部分原样复用；标注 `【人物专属】` 的部分已按本人物替换。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Sir William Lawrence Bragg CH OBE MC FRS（威廉·劳伦斯·布拉格爵士）。
- **设计哲学**：物理学家立传必须有「身份信息页」与结构化「研究领域」表达；本篇叙事重心是**25 岁的天才洞察 + 分子生物学的奠基**——与同批次的 William Henry Bragg（父亲）成对，两篇互引但各写各人视角。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Sir William Lawrence Bragg（1890-03-31 生于南澳大利亚阿德莱德 ~ 1971-07-01 逝于英格兰 Ipswich，享年 81 岁）
- **气质关键词**：**最年轻的诺奖得主、布拉格定律的提出者、分子生物学的铺路人** —— 1915 诺贝尔物理学奖获奖理由（与父亲共享）：
  > "for their services in the analysis of crystal structure by means of X-rays"（因他们利用 X 射线分析晶体结构的功绩）
- **设计母题**：**原子平面间的反射（reflections between atomic planes）**。以布拉格定律的几何光路、晶面层叠与蛋白晶体的视觉语言贯穿全篇。
- **本地数据源**：`physicist/presentations/20th_century/20th_century/William_Lawrence_Bragg/page.md`（Wikipedia 全文，事实基准已核对）
- **参考模板**：
  - 提示词标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`
  - 物理学家成品参照：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：研究领域（第 4 步）与社会关系（第 4.5 步）已随提示词同步入库 greatminds 库（MySQL），无需重复整理。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 本地 Wikipedia 已就位：`20th_century/20th_century/William_Lawrence_Bragg/` 下已有 `page.html` / `page.md` / `metadata.json` / `images.txt`（无需再下载）
- ⬜ **待下载头像**：images.txt 已有 `William_Lawrence_Bragg.jpeg`（1930 年肖像）与 `Lawrence_Bragg,_January_1967.png`，250px 改 500px 下载（建议 1930 肖像）
- 事实基准（已按本地 page.md 核对）：
  - 生卒：1890-03-31 生于 Adelaide ~ 1971-07-01 卒于 Ipswich（Waldringfield 附近医院），享年 81 岁，葬于 Trinity College, Cambridge
  - 国籍：澳大利亚出生的英国人（frontmatter nationality: United Kingdom / Australia）
  - 家庭：父 William Henry Bragg（1885 年起任阿德莱德大学 Elder 数学物理教授）；母 Gwendoline Todd（南澳政府天文学家 Charles Todd 之女）；弟 Robert 1915-09-02 死于加里波利战役
  - 教育：Queen's School, North Adelaide（1900）→ St Peter's College 五年 → 16 岁入阿德莱德大学（数学/化学/物理），1908 毕业 → 1909 入剑桥 Trinity College（肺炎卧床赴考仍获数学大奖学金），后转物理，1912 一等 Natural Sciences Tripos；1914 Trinity Fellow & Natural Sciences 讲师
  - 学术导师（frontmatter/infobox）：J. J. Thomson 与其父 William Henry Bragg
  - 1912 顿悟：河边散步想到晶体中平行原子面对 X 射线的相干反射 → 布拉格方程；父亲造分光计测面间距；父报告成果时归功"他的儿子"但未列为合作作者，给他 "some heartaches"
  - 一战：皇家骑炮兵少尉（Leicestershire 炮兵），1915 转 Royal Engineers 研究炮位声测距（热线空气波探测器；协作 C. G. Darwin、Tucker、Robinson、Andrade、Hemming）；获 Military Cross、OBE，三次 Mentioned in dispatches
  - 1915-11 父子获诺贝尔物理学奖——25 岁，**至今最年轻的科学类诺奖得主**（截至 2025）
  - 1919–1937 曼彻斯特 Victoria 大学 Langworthy 物理教授（接替迁往剑桥的 Rutherford）；与 R. W. James 测反射 X 射线绝对能量；1920s 末引入 Fourier 变换；1930-31 赴慕尼黑休整做研究
  - 1937–1938 国家物理实验室（NPL）第 3 任院长；1938 接任去世的 Rutherford 出任剑桥卡文迪什教授/实验室主任（把实验室重组为 6–12 人研究组）
  - 卡文迪什与分子生物学：收留无导师的难民学生 Max Perutz（血红蛋白衍射）→ 1947 说服 MRC 建立 MRC 分子生物学实验室（Perutz、John Kendrew）；1960 肌红蛋白结构解析；Watson & Crick 1953-02 报告 DNA 双螺旋，Bragg 1953-04-08 在 Solvay 会议宣布（未获报道）、05-14 在 Guy's Hospital 演讲促成 05-15 News Chronicle 报道；提名 Crick/Watson/Wilkins 获 1962 生医诺奖；Rosalind Franklin 的 photograph 51 证明双螺旋（Franklin 死于授奖前）
  - 皇家研究所：1938 起自然哲学教授；1953–1966 入驻（Fullerian 化学教授 1954–66、Davy-Faraday 实验室主任、院长 1965–66、Emeritus 1966）；1965 溶菌酶结构解析（D. C. Phillips）；重振周五晚间讲座
  - 战后任国际晶体学联合会首任主席；研究金属结构（X 射线 + 电子显微镜）
  - 关键荣誉：Matteucci 1915、Nobel 1915、Hughes 1931、Royal Medal 1946、Copley 1966；FRS 1921；1941 Knight Bachelor、1967 Companion of Honour
  - 家庭：1921 娶 Alice Hopkinson，四子（工程师 Stephen Bragg 后任 Brunel 副校长；女儿 Patience 嫁物理诺奖得主 G. P. Thomson 之子）
  - 趣闻：贝类收藏家（500 余种，新种乌贼 Sepia braggi 以他命名）；在伦敦兼职园丁未被认出
  - 纪念：IOP 的 Lawrence Bragg Medal（1967 起）、澳洲 Bragg Gold Medal（1992 起）

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/20th_century/` 下使用 `William_Lawrence_Bragg/` 并建 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制 `Kenneth_G_Wilson/Makefile`，设置 `MAIN=William_Lawrence_Bragg_zh`、`VIDEO_NAME=William_Lawrence_Bragg_zh`

### 第 3 步：收集图片 【人物专属】

- ⬜ 肖像见第 0 步（images.txt 已有两张）；插图：`Lawrence_Bragg_Blue_Plaque_Manchester.jpg`（曼彻斯特蓝牌，images.txt 已有）

### 第 4 步：研究领域 【模板通用，人物专属内容】

**W. L. Bragg 的研究领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | x-ray crystallography | X 射线晶体学 | 布拉格定律与结构解析，1915 诺奖核心 | 核心页 |
| 1 | crystal structure analysis | 晶体结构分析 | 硅酸盐到傅里叶方法 | 核心页 |
| 2 | x-ray spectroscopy | X 射线波谱学 | 与父共测反射 X 射线绝对能量 | 曼彻斯特页 |
| 3 | protein crystallography | 蛋白质晶体学 | 血红蛋白/肌红蛋白/溶菌酶、MRC LMB | 卡文迪什页 |
| 4 | physics of metals | 金属物理 | 战后金属结构研究 | 皇家研究所页 |

### 第 4.5 步：社会关系 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Joseph John Thomson | 师→生 | 剑桥导师（frontmatter doctoral_advisor；infobox academic advisors） |
| advisor-student | William Henry Bragg | 师→生 | 父亲兼导师（frontmatter doctoral_advisor；阿德莱德亲授，剑桥研究合作者） |
| parent-child | William Henry Bragg | 无向 | 父亲 |
| co-honored | William Henry Bragg | 无向 | 1915 年诺贝尔物理学奖共同得主（史上唯一父子共享） |
| advisor-student | Max Perutz | 生 | 卡文迪什研究助手，血红蛋白 X 射线衍射，MRC 分子生物学实验室创建成员 |
| advisor-student | John Kendrew | 生 | MRC 分子生物学实验室成员（肌红蛋白结构） |
| spouse | Alice Hopkinson | 无向 | 1921 年结婚，育四子 |

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：明澈、锐利、生长
- **配色**：晶体森绿（主色 `#1E5B3A`）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeA` 布拉格定律 — 翡翠绿 `#2E8B57`
  - `badgeB` 结构分析 — 湖蓝 `#2E7D9A`
  - `badgeC` 蛋白质晶体学 — 暖橙 `#D07A2E`
  - `badgeD` 卡文迪什时代 — 石板蓝 `#3E5C76`
- **背景母题**：层叠晶面间的反射光束逐层增强，呼应"原子平面间的反射"

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + `draw=coveraccent!50` 细边框）。
2. 封面明示国籍（澳大利亚出生的英国人）；底部状态栏给出 `国籍 | 机构 | 主要奖项`。
3. 必须有身份信息页（左头像 + 右信息网格）。
4. 结尾页品牌统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，15 页】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 最年轻的诺奖得主 / William Lawrence Bragg 1890–1971 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — 布拉格定律 / 结构分析 / 分子生物学 / 金属物理
04  阿德莱德少年 (1890–1908) — 16 岁入大学、贝类收藏、Sepia braggi
05  剑桥 (1909–1912) — 肺炎赴考、转物理、Trinity Fellow
06  1912：河边顿悟（核心贡献页，公式框放布拉格定律 nλ=2d·sinθ，注明为布拉格定律标准式）
07  父子协作 — 分光计测量、"his son" 未署名的心结
08  1915：最年轻诺奖 — 25 岁、加里波利之痛、MC 与 OBE
09  一战声测距 — 热线探测器、C. G. Darwin 等协作
10  曼彻斯特 (1919–1937) — Langworthy 讲席、绝对能量测量、Fourier 方法
11  卡文迪什时代 (1938–1953) — 重组研究组、Perutz 与血红蛋白
12  DNA 的 1953 — Solvay 宣布、News Chronicle 报道、1962 提名
13  MRC 分子生物学实验室与皇家研究所 (1947–1966) — 肌红蛋白、溶菌酶
14  遗产 + 结尾 — X 射线结构分析与 28 项诺奖、Lawrence Bragg Medal
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页参照标杆 `\profileslide`。
- 头部宏整体复用 `Kenneth_G_Wilson_zh.tex` 骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make`，`pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**W. L. Bragg 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 最年轻纪录 | 25 岁获奖（1915），**至今仍是所有科学类诺奖最年轻得主**（截至 2025），勿写成"物理学最年轻"或加"曾" |
| 诺奖理由 | "for **their** services..."父子共享、至今唯一亲子共享诺奖；获奖消息与兄长阵亡几乎同时（1915-09-02 / 1915-11），叙事层次勿乱 |
| 布拉格定律归属 | 物理洞察是儿子 1912 年河边顿悟；父亲承担装置与测量；父亲论文归功"his son"却未列合作作者（"some heartaches" 原文明载可写），勿写成父亲独立提出或完全代笔 |
| 剑桥入学 | 1909 年肺炎卧床赴考仍获数学大奖学金——可写，勿改成"因病落榜后特批" |
| NPL 任期 | 1937–1938 仅一年（行政会务挤占研究），勿拉长 |
| 卡文迪什继任 | 1938 年接的是 Rutherford 的教席（第 5 任卡文迪什教授），勿写成接 Thomson |
| DNA 角色 | Bragg 是宣布者（Solvay 1953-04-08）与 1962 年提名者，**不是双螺旋共同发现者**；Franklin photograph 51 与"未获奖"表述需严谨 |
| 姻亲区分 | 女儿嫁的是 G. P. Thomson（1937 诺奖）之子；G. P. Thomson 是 J. J. Thomson 之子——两对"诺奖父子"勿混 |
| 名字区分 | 父 W. H. Bragg / 子 W. L. Bragg，通称 Lawrence Bragg；本篇主角是 W. L. |
| 学位口径 | 剑桥本科 1912（Natural Sciences Tripos 一等），无传统博士学位；J. J. Thomson 与父亲是"学术导师"（infobox Academic advisors）口径 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Bragg's law / Bragg equation | 布拉格定律/方程 | nλ=2d·sinθ |
| plane of atoms | 原子平面 | 反射几何的核心 |
| diffraction | 衍射 | 相干条件 |
| sound ranging | 声测距 | 一战炮位定位 |
| hot wire air wave detector | 热线空气波探测器 | 低频炮声解决方案 |
| Fourier transform | 傅里叶变换 | 1920s 末结构分析方法 |
| haemoglobin / myoglobin / lysozyme | 血红蛋白/肌红蛋白/溶菌酶 | 蛋白质晶体学三部曲 |
| double helix | 双螺旋 | DNA 1953 |
| photograph 51 | 51 号照片 | Franklin 的证据 |
| cryo-electron microscopy | 冷冻电镜 | 其路线的后续发展 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Shine Like The Sun** — Really Slow Motion（史诗 / 美丽 / 振奋，`music_audio/inspiring-electronic/15-w6kT1BfvETI-...Shine Like The Sun.wav`）
- **匹配理由**: "光明振奋"匹配 25 岁天才的灵光乍现与 X 射线照亮原子世界的意象；史诗感收束于分子生物学的世纪遗产。
- **批内查重**: batch 2 内无人复用此曲。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/20th_century/20th_century/William_Lawrence_Bragg/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架/源码参照 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/William_Lawrence_Bragg.yaml` | 已入库的领域/关系数据 |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
