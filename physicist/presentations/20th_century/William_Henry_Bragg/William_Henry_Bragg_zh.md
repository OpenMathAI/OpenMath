# 物理学家立传提示词（William Henry Bragg）

> 本文件是 OpenPhysicist「人物专属立传提示词」，以 Kenneth G. Wilson 标杆结构为骨架，为 William Henry Bragg（1915 诺贝尔物理学奖，X 射线晶体结构分析）定制。
> 凡标注 `【模板通用】` 的部分原样复用；标注 `【人物专属】` 的部分已按本人物替换。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Sir William Henry Bragg（威廉·亨利·布拉格爵士）。
- **设计哲学**：物理学家立传必须有「身份信息页」与结构化「研究领域」表达；本篇叙事重心是**父子科学家的"最非凡合作"**——与同批次的 William Lawrence Bragg（儿子）成对，两篇互引但各写各人视角。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Sir William Henry Bragg OM KBE FRS（1862-07-02 生于英格兰 Westward, Cumberland ~ 1942-03-12 逝于伦敦，享年 79 岁）
- **气质关键词**：**数学出身的实验家、父子诺奖的另一半、皇家研究所的传灯人** —— 1915 诺贝尔物理学奖获奖理由（与儿子共享）：
  > "for their services in the analysis of crystal structure by means of X-rays"（因他们利用 X 射线分析晶体结构的功绩）
- **设计母题**：**双晶（father and son, one beam）**。以 X 射线分光计、双晶面反射与两代人的协作意象贯穿全篇。
- **本地数据源**：`physicist/presentations/20th_century/20th_century/William_Henry_Bragg/page.md`（Wikipedia 全文，事实基准已核对）
- **参考模板**：
  - 提示词标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`
  - 物理学家成品参照：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：研究领域（第 4 步）与社会关系（第 4.5 步）已随提示词同步入库 greatminds 库（MySQL），无需重复整理。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ 本地 Wikipedia 已就位：`20th_century/20th_century/William_Henry_Bragg/` 下已有 `page.html` / `page.md` / `metadata.json` / `images.txt`（无需再下载）
- ⬜ **待下载头像**：images.txt 无正脸肖像（infobox「1915 年像」未入库，仅签名照）→ 用 Wikipedia REST API `page/summary` 查 infobox 原图名下载（404 则装饰圆占位）
- 事实基准（已按本地 page.md 核对）：
  - 生卒：1862-07-02 生于 Westward, Cumberland ~ 1942-03-12 卒于伦敦，享年 79 岁（frontmatter 死亡字段有 03-10/03-12 噪声，以正文/infobox 03-12 为准）
  - 国籍：英国
  - 家庭：父 Robert John Bragg（商船军官兼农场主），母 Mary Wood（牧师之女）7 岁去世，由叔父（同名 William Bragg）在 Market Harborough 抚养
  - 教育：Market Harborough 文法学校 → King William's College（马恩岛）→ Trinity College, Cambridge（获 exhibition 奖学金）：1884 毕业（第三 Wrangler）、1885 数学 Tripos 一等
  - 博士导师/数学导师：Edward Routh（frontmatter/infobox 明载 academic advisor）
  - 任职：1885 受聘阿德莱德大学 Elder 数学与物理教授（1886 初到任，在澳 23 年）；1909–1915 利兹大学 Cavendish 物理教授；1915 UCL Quain 物理教授；1923 皇家研究所 Fullerian 化学教授兼 Davy Faraday 研究实验室主任；1935–1940 皇家学会第 46 任主席
  - 澳洲岁月：1895 Rutherford 途经来访（终生友谊之始）；1896-05-29 在阿德莱德演示 X 射线透视；1897-09-21 澳洲首次公开无线电报演示；1898 访 Marconi；1904 Dunedin 演讲（气体电离理论）→ 三年内入选皇家学会 FRS（1907）；1904-12 发表镭 α 射线分类论文，同刊与学生 Richard Kleeman 合作电离曲线论文；著《Studies in Radioactivity》（1912）
  - 1908 年底乘 SS Waratah 号回英（次年该船失踪，1911 年沉船调查中作证稳心低于重心）；任内阿德莱德学生数近翻两番（quadruple）
  - 利兹岁月：发明 X 射线分光计；与剑桥研究生的儿子 Lawrence 共同创立 X 射线晶体学
  - 一战：1915-07 入海军部发明与研究委员会；1915-09 次子 Robert 死于加里波利；1916 任 Aberdour 水听器研究站科学主管（改进定向水听器），1918-01 任海军部反潜研究主管——英军 sonar 实用化；借鉴 Lawrence 的炮位声测距
  - 皇家研究所：1919/1923/1925/1931 四度圣诞讲座（《The World of Sound》《Concerning the Nature of Things》《Old Trades and New Knowledge》《The Universe of Life》）
  - 二战：1940 年名列纳粹黑皮书（入侵英国后逮捕的 2300 人名单）
  - 关键荣誉：Matteucci 1915、Nobel 1915（与子共享）、Rumford 1916、Copley 1930、Franklin 1930、Faraday 1936、John J. Carty 1939；FRS 1907；1920 KBE、1931 Order of Merit
  - 家庭：1889 在阿德莱德娶 Gwendoline Todd（水彩画家，南澳政府天文学家 Charles Todd 之女），三子：Gwendolen、Lawrence、Robert（Robert 死于加里波利）；亲自教 Lawrence（阿德莱德大学）
  - 爱好：网球、高尔夫、长曲棍球（将 lacrosse 引入南澳）、国际象棋
  - 1942-03-12 心力衰竭卒于伦敦

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/20th_century/` 下使用 `William_Henry_Bragg/` 并建 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制 `Kenneth_G_Wilson/Makefile`，设置 `MAIN=William_Henry_Bragg_zh`、`VIDEO_NAME=William_Henry_Bragg_zh`

### 第 3 步：收集图片 【人物专属】

- ⬜ 肖像见第 0 步（REST API 回退）；插图：`Bragg_plaque_leeds.jpg`（利兹纪念铭牌，images.txt 已有）、X 射线分光计照（Commons `X-ray spectrometer, 1912. (9660569929).jpg`）

### 第 4 步：研究领域 【模板通用，人物专属内容】

**W. H. Bragg 的研究领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | x-ray crystallography | X 射线晶体学 | 与子共同创立，1915 诺奖核心 | 核心页 |
| 1 | x-ray spectroscopy | X 射线波谱学 | 发明 X 射线分光计 | 核心页 |
| 2 | radioactivity | 放射性 | α 射线吸收与分类、《Studies in Radioactivity》 | 澳洲页 |
| 3 | electromagnetism | 电磁学 | 澳洲早期的物理兴趣方向 | 澳洲页 |
| 4 | mathematical physics | 数学物理 | 第三 Wrangler、Adelaide 数学物理教授 | 早年页 |

### 第 4.5 步：社会关系 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Edward Routh | 师→生 | 剑桥数学导师（frontmatter doctoral_advisor） |
| parent-child | William Lawrence Bragg | 无向 | 独子（存活的科学继承人），1915 诺奖父子共享 |
| co-honored | William Lawrence Bragg | 无向 | 1915 年诺贝尔物理学奖共同得主（史上唯一父子共享） |
| advisor-student | William Lawrence Bragg | 生 | 在阿德莱德大学亲自授课，后为剑桥研究合作者 |
| colleague | Ernest Rutherford | 无向 | 1895 年阿德莱德相识，终生挚友 |
| advisor-student | Richard Kleeman | 生 | 学生，1904 年合作发表镭 α 射线电离曲线论文 |
| advisor-student | William Astbury | 生 | 知名学生（infobox 明载） |
| advisor-student | Kathleen Lonsdale | 生 | 知名学生（infobox 明载） |
| advisor-student | John Bernal | 生 | 知名学生（infobox 明载） |
| spouse | Gwendoline Todd | 无向 | 1889 年结婚，天文学家 Charles Todd 之女，育三子 |

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：沉稳、传承、分光
- **配色**：勃艮第深红（主色 `#6E2436`）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeA` X 射线晶体学 — 石板蓝 `#3E5C76`
  - `badgeB` X 射线波谱学 — 铜金 `#B07D2B`
  - `badgeC` 放射性 — 苔绿 `#4A6B4F`
  - `badgeD` 皇家研究所 — 象牙白调 `#8A7F6E`
- **背景母题**：单束 X 射线在两片平行晶面上分裂反射的几何光路，呼应"父子一束光"

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + `draw=coveraccent!50` 细边框）。
2. 封面明示国籍；底部状态栏给出 `国籍 | 机构 | 主要奖项`。
3. 必须有身份信息页（左头像 + 右信息网格）。
4. 结尾页品牌统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，14 页】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 父子一束光 / William Henry Bragg 1862–1942 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — X 射线分光计 / 晶体结构分析 / 放射性 / 声呐
04  坎伯兰少年与剑桥 (1862–1885) — 7 岁丧母、第三 Wrangler、Routh 门下
05  阿德莱德二十三年 (1885–1908) — 数学物理教授、X 光演示、无线电报
06  放射性研究 (1904–1912) — Dunedin 演讲、镭 α 射线、Kleeman 合作、FRS
07  利兹：分光计与晶格（核心贡献页，公式框放布拉格定律 nλ=2d·sinθ，注明为布拉格定律标准式）
08  父子共享 1915 — "for their services"、史上唯一父子诺奖
09  一战与声呐 — 水听器、反潜研究、痛失次子 Robert
10  皇家研究所传灯 (1923–1942) — Davy Faraday 实验室、四度圣诞讲座
11  皇家学会主席 (1935–1940) — 战备科学、黑皮书名单
12  门生谱系 — Lawrence、Kleeman、Astbury、Lonsdale、Bernal
13  遗产 + 结尾 — Bragg 环形山、Bragg Gold Medal、利兹 Bragg 楼
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页参照标杆 `\profileslide`。
- 头部宏整体复用 `Kenneth_G_Wilson_zh.tex` 骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make`，`pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**W. H. Bragg 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 卒日 | 1942-03-12（frontmatter 有 03-10 噪声，以正文/infobox 为准） |
| 诺奖理由 | "for **their** services in the analysis of crystal structure by means of X-rays"，父子共享、史无前例且至今唯一（任何领域的亲子共享诺奖），行文务必用"共同/父子"口径 |
| 布拉格定律归属 | Bragg's law 主要是 Lawrence 1912 年的物理洞察（父亲承认"归功于他的儿子"却未列合作者）；父亲的关键角色是发明分光计并承担实验测量，两者勿颠倒 |
| 出身口径 | 剑桥数学出身（第三 Wrangler），1885 年赴澳时"物理知识有限、多为应用数学"，是后来才转向物理实验，勿写成"物理学家赴任" |
| 澳洲身份 | 在澳 23 年、 Elder 数学物理教授；radioactivity 研究使他三年内入选 FRS（1907），勿写成诺奖前默默无闻 |
| 儿子名字 | 本篇写 William Henry（父）；William Lawrence（子）另有专篇，引用时用全名或 W. H. / W. L. 区分，勿与 G. P. Thomson 家族混 |
| 次子 | Robert 1915-09 死于加里波利，与同年 11 月诺奖同年，叙事注意情感层次，勿写成 Lawrence 之死 |
| 声呐贡献 | 一战反潜（水听器/声测距）是其重要实务功绩，勿略去，也勿拔高为"声呐发明人"（英国 sonar 实用化的科学主管） |
| 黑皮书 | 1940 年列入纳粹黑皮书名单，属 W. H. Bragg 页内容（Max von Laue 页无此载），勿跨篇混用 |
| Waratah | 1908 年乘 Waratah 号回英、1911 年为该船失踪作证（稳心判断），细节可作轶事但勿编造结论 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Bragg's law | 布拉格定律 | nλ=2d·sinθ，洞察主要属子 |
| x-ray spectrometer | X 射线分光计 | W. H. 发明 |
| x-ray crystallography | X 射线晶体学 | 父子共创学科 |
| wrangler | 剑桥数学荣誉甲等（Wrangler） | 第三 Wrangler |
| radioactivity | 放射性 | α 射线分类 |
| hydrophone | 水听器 | 一战反潜 |
| sound ranging | 声测距 | 炮位定位 |
| sonar | 声呐 | 英军实用化主管 |
| metacentre | 稳心 | Waratah 作证 |
| Christmas Lectures | 皇家研究所圣诞讲座 | 四度主讲 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **The Flow of Time** — Alex-Productions（时间感 / 纪录片，`music_audio/alex-productions/35-jqIDnltiDRI-The-Flow-of-Time.wav`）
- **匹配理由**: "时间感"匹配父与子两代人、从维多利亚数学到 20 世纪 X 射线的时代跨度；纪录片气质匹配皇家研究所传灯人的一生。
- **批内查重**: batch 2 内无人复用此曲。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/20th_century/20th_century/William_Henry_Bragg/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架/源码参照 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/William_Henry_Bragg.yaml` | 已入库的领域/关系数据 |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
