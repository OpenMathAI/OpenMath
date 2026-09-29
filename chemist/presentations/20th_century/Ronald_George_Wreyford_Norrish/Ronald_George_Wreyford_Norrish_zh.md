# Ronald George Wreyford Norrish（罗纳德·乔治·雷福德·诺里什）立传提示词

> qid=Q235834 · 1897-11-09 – 1978-06-07 · 英国化学家 · 20 世纪 · 诺贝尔化学奖（1967，与 Eigen、Porter 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Ronald_George_Wreyford_Norrish/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**严格对齐 Frederick Sanger 黄金参照**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.md`）——身份信息页 + 高斯式时间线 + 表格语义化 tabularx + 金色公式展示框 + 气泡背景。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。⚠ 肖像说明：本地 `images.txt` 为**空**——无现成肖像；回退方案：经 Wikipedia REST API `page/summary` 查 infobox 原图名后用 `Commons Special:FilePath/<文件名>?width=600` 下载（curl -A "Mozilla/5.0" + file 验证）；404 则装饰圆占位。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{camera}\enspace 闪光中的分子世界\enspace·\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。⚠ 本页无配偶/子女记载——身份网格不放家庭字段，如实留白。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「闪光瞬间」母题——一束光点亮黑暗中的分子。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Ronald George Wreyford Norrish，FRS（中文惯称：罗纳德·乔治·雷福德·诺里什）
- **生卒**：1897-11-09 生于剑桥 → 1978-06-07 逝于剑桥，享年 80（生卒同城——一生几乎都在剑桥）
- **国籍**：United Kingdom（英国）
- **身份**：化学家（chemist；剑桥物理化学系主任）
- **家庭**：父亲鼓励他自建小实验室——在自家花园棚屋里搭建并供给全部化学品；这套装置现藏科学博物馆（含铜水箱 copper water tank）。配偶/子女：**本页无载——禁写**
- **教育轨迹**：
  - The Perse School（剑桥）
  - Emmanuel College, Cambridge（BA、PhD）；1915 年获 Emmanuel Foundation Scholarship
  - 博士论文 *Radiation and chemical reactivity*（1924）
- **导师**：Eric Rideal（博士导师；infobox "former student of Eric Rideal"）
- **研究领域**：光化学（photochemistry）、气相动力学（gas kinetics）、闪光光解（flash photolysis）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **剑桥化学少年（1897–）**：自幼痴迷化学——常在剑桥大学化学实验室楼下走上走下，羡慕所有仪器。
2. **花园棚屋实验室**：父亲为其搭建花园棚屋实验室并供给化学品；少年参加《Pharmaceutical Journal》组织的混合物分析竞赛，常获奖——装置今藏科学博物馆。
3. **虚报年龄参军（1915）**：获 Emmanuel 奖学金后，给年龄"加了一点"加入皇家野战炮兵（Royal Field Artillery），任少尉（Lieutenant）——先驻爱尔兰，后上西线。
4. **战俘（1918）**：军事档案记载皇家炮兵二级中尉 Norrish 于 1918-03-21 被列为失踪（被俘）——一战战俘。
5. **失落的一代**：晚年感伤地评论，他在剑桥的许多同代人和潜在竞争对手没能活过那场战争。
6. **重返剑桥（1925）**：任 Emmanuel College Research Fellow；后成为剑桥大学物理化学系主任（Head of the Department of Physical Chemistry）。
7. **天才实验家**：实验室功力在同代人中出挑——"unusually gifted and energetic experimentalist"，在光化学与气相动力学做出重要进展。
8. **Norrish 反应**：以他命名的光化学反应（本页仅列名词，机理细节页外无载——禁展开）。
9. **Trommsdorff–Norrish 效应**：聚合自加速（autoacceleration）效应（本页仅列名词——禁展开）。
10. **闪光光解（flash photolysis）**：发展该技术——以高强度短脉冲闪光打碎分子、捕捉短寿命中间体。
11. **1967 诺贝尔化学奖**："As a result of the development of flash photolysis"，与 Manfred Eigen、George Porter 共享——表彰对极快化学反应的研究；诺奖演讲 *Some Fast Reactions in Gases Studied by Flash Photolysis and Kinetic Spectroscopy*（1967-12-11）。
12. **指导 Rosalind Franklin**：在剑桥指导后来成为 DNA 研究者、Watson 与 Crick 同事的 Rosalind Franklin——两人之间有过一些冲突（页面原载，客观带过）。
13. **荣誉链**：FRS（1936）、Davy Medal（1958）、Faraday Lectureship Prize（1965）、Nobel（1967）、Meldola Medal、Liversidge Award、Longstaff Prize、皇家学会 Bakerian Medal、巴黎大学荣誉博士（后五项页面未给年份——禁编）。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深剑桥绿 deepcambridge） | `#146B3A` | 剑桥园地与光化学——棚屋实验室到诺奖讲堂（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（闪光光解 badgeFlash） | `#C0392B` | 红 flash photolysis / 动力学光谱 |
| 分类色 2（光化学 badgePhoto） | `#D97B29` | 琥珀 Norrish 反应 / Trommsdorff–Norrish 效应 |
| 分类色 3（气相动力学 badgeGas） | `#1E4E79` | 蓝 气相快反应 / 自由基中间体 |
| 分类色 4（战争岁月 badgeWar） | `#4A4A4A` | 灰 西线 / 战俘 / 失落的一代 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「闪光瞬间」——黑暗中被一束光点亮的分子。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Tragedy** — Alex-Productions（`music_audio/alex-productions/80-K5f65-22sY4-Tragedy.wav`；不要复制 wav 文件，make video 时引用路径）
- **风格**：深沉 / 悲怆 / 迟来的荣光
- **匹配理由**：
  - "Tragedy" 匹配其一生的底色——西线与战俘营，许多同代人与潜在竞争对手死于战争，他带着这份感伤走完科学之路
  - 悲怆之后的明亮段落留给 1967 诺奖——69 岁的迟来加冕，闪光光解终被世界看见
  - 全片克制不煽情，符合英式化学家的内敛气质
- **时长**：以文件实际时长为准，ffmpeg `-shortest` 自动对齐 15 页 × 7 秒

## 4. Slide 规划（15 页，Sanger 同构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 闪光中的分子世界 / Ronald G. W. Norrish 1897–1978 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉；家庭字段如实留白）
03  诺里什的一生 — 高斯式时间线（10 节点：1897→1915→1918→1924→1925→1936→1958→1965→1967→1978）
04  庭园实验室的少年 (1897–1915) — 表格「时间|事件|结果」（Perse School/棚屋实验室/分析竞赛）
05  西线与战俘 (1915–1918) — 表格（虚报年龄/Royal Field Artillery/1918-03-21 被俘）+「失落的一代」
06  重返剑桥与博士 (1924–1925) — 表格（Rideal 门下/Radiation and chemical reactivity/Research Fellow）
07  光化学与气相动力学 — 表格「问题|方法|结果」+ 公式框：闪光光解原理示意（短脉冲闪光→短寿命中间体→动力学光谱）
08  Norrish 反应与自加速效应 — 名词框（页面仅列名，禁展开机理）+ 实验家评语
09  物理化学系主任岁月 — 表格（系主任/光化学与气相动力学进展）
10  1967 诺贝尔化学奖 — 三人共享（本篇=闪光光解方向）；citation 用 Eigen 页面口径统一表述；诺奖演讲标题
11  指导 Rosalind Franklin — 客观一页（指导关系+页面原载"有过一些冲突"；禁戏剧化）
12  荣誉 — 高斯式「类别|代表|意义」表格（FRS 1936/Davy 1958/Faraday 1965/Nobel 1967/其余无年份项留空）
13  遗产 — 科学博物馆藏品 / 闪光光解的传承（Porter 篇呼应）/ 1978 逝于剑桥
14  结尾 — 「一束光，把看不见的反应照亮了一瞬。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1967 共享口径 | Norrish 因**闪光光解**的发展获奖（页面原句 as a result of the development of flash photolysis）；Eigen=弛豫法——三人方向勿混；官方 citation 英文原句本页无载，统一采用三人共享的间接转述（与 Eigen 篇口径一致） |
| 战俘日期 | 军事档案载 1918-03-21 被列为失踪（被俘）——日期可写；"一战战俘"如实；勿加战俘营生活细节（页外） |
| 失落的一代 | "许多同代人与潜在竞争对手未能活过战争"是其晚年感伤评论——**间接转述**，勿加引号当原话 |
| Franklin 关系 | 剑桥指导 + "experienced some conflict with her"——页面原载可写；勿写师生反目戏剧化、勿写 Franklin DNA 争议与死因（本页无载） |
| 名词页外禁展开 | Norrish reaction、Trommsdorff–Norrish effect 本页仅列名词——禁写 I 型/II 型机理等页外内容 |
| 婚姻子女 | 本页**无载**——禁写配偶/家庭；身份信息页如实留白 |
| 无年份奖项 | Meldola Medal、Liversidge Award、Longstaff Prize、Bakerian Medal、巴黎大学荣誉博士——页面未给年份，一律留空禁编 |
| Porter 师承 | Porter 页载其博士导师为 Norrish，但**本页正文无载**——Norrish yaml 不入库 Porter 学生关系（由 Porter 侧入库），本篇 §7 注明 |
| 博士生 | metadata.json 载 David Husain、George Porter——正文 infobox 无博士生行——**均不予入库** |
| 生卒同城 | 1897 生于剑桥、1978 逝于剑桥——勿写"卒于伦敦"等页外地点 |
| 头衔 | FRS（1936）；infobox 头行为 "FRS"——勿写爵士/贵族头衔（页面无载） |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q235834 | ✅ |
| name_zh | 罗纳德·乔治·雷福德·诺里什 | ✅ |
| name_en | Ronald George Wreyford Norrish | ✅ |
| birth_date | 1897-11-09 | ✅ |
| death_date | 1978-06-07 | ✅ |
| nationality | United Kingdom | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | photochemistry（person_field 细分：photochemistry / chemical kinetics / flash photolysis，带 rank） | ✅ |
| has_biography | false（立传 Beamer 完成后再置 1） | ✅ |

## 7. 社会关系入库清单

**★红线：只收 page.md 正文或 frontmatter 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Eric Rideal | 师→生 | 博士导师；infobox "former student of Eric Rideal"；1924 论文 Radiation and chemical reactivity |
| advisor-student | Rosalind Franklin | Norrish→学生 | 剑桥指导；页面原载两人有过一些冲突 |
| co-honored | Manfred Eigen | 无向 | 1967 诺贝尔化学奖共同得主 |
| co-honored | George Porter | 无向 | 1967 诺贝尔化学奖共同得主 |

> **metadata-only 禁入库名单**：David Husain、George Porter（doctoral_student 仅 metadata.json，本页正文无博士生行）——不予入库。Porter 的师承关系由 George Porter 侧 yaml 入库（其页面明载 research supervised by Norrish）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1967，与 Eigen、Porter 共享）
- Fellow of the Royal Society，FRS（1936）
- Davy Medal（1958）
- Faraday Lectureship Prize（1965）
- Meldola Medal and Prize（页面无年份）
- Liversidge Award（页面无年份）
- Longstaff Prize（页面无年份）
- Royal Society Bakerian Medal（页面无年份）
- 巴黎大学荣誉博士（doctor honoris causa，页面无年份）

## 9. 机构清单

- 教育：The Perse School（剑桥）；Emmanuel College, Cambridge（1915 Foundation Scholarship；BA、PhD 1924）
- 战时：Royal Field Artillery 少尉（爱尔兰→西线；1918-03-21 被俘）
- 任职：University of Cambridge——Emmanuel College Research Fellow（1925）→ 物理化学系主任（Head of the Department of Physical Chemistry）
- 藏品：少年花园棚屋实验装置今藏伦敦科学博物馆（Science Museum collections，含铜水箱）

## 10. 终审清单

- [ ] 生卒 1897-11-09 / 1978-06-07，享年 80，生卒同城剑桥
- [ ] 1967 三人共享表述准确；本篇方向=闪光光解，与 Eigen（弛豫法）不混
- [ ] 1918-03-21 被俘日期与"一战战俘"表述准确；"失落的一代"为间接转述
- [ ] Franklin 关系客观（指导+冲突），无戏剧化与页外细节
- [ ] Norrish reaction / Trommsdorff–Norrish effect 仅列名词，无页外机理
- [ ] 婚姻/子女如实留白；无年份奖项未编造年份
- [ ] 引语核对：任何引号文本必须在 page.md 溯源（本页几乎无直接引语），否则改间接转述
- [ ] 正文采用 Sanger 同构：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误，vbox≤10pt / hbox≤50pt

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Ronald_George_Wreyford_Norrish/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：REST API 回退下载结果核对；404 则装饰圆占位并在 §0 注记
- [ ] 国籍：封面顶部明示英国
- [ ] 引语核对：任何引号文本必须在 Wikipedia 原文找到
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox<10pt / hbox<50pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式及同批 Eigen/Porter 篇章口径一致（三人互指一致）
