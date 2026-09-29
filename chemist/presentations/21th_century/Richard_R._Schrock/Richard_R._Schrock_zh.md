# Richard R. Schrock（理查德·施罗克）立传提示词

> qid=Q202159 · 1945-01-04（印第安纳州 Berne）– 在世 · 美国化学家 · 21 世纪 · 诺贝尔化学奖（2005，与 Yves Chauvin / Robert H. Grubbs 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Richard_R._Schrock/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/`）——身份信息页 + 时间线页 + 表格语义化 tabularx + 金边公式框，是本次执行的版式语言。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注；肖像优先取本地 `images.txt`（2012 年第 44 届国际化学奥林匹克开幕式照），404 则装饰圆占位。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 钼与钨上的金属碳双键\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生年（在世，卒项留白）、本名（Richard Royce Schrock）、国籍、出生地、教育、博士、导师、核心领域、荣誉。事实取自本地 infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡呼应「金属=碳双键」母题——双圆点以粗线相连，暗示金属卡宾。
5. **表格语义化 + 公式框**（★ 每个核心贡献页必须使用）：`tabularx` 三列表格（表头主色白字、第一列强调色加粗、三列语义化如 问题 | 催化剂 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式框画 Schrock 催化剂原型 (R"O)₂(R'N)Mo(CHR)。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Richard Royce Schrock（中文惯称：理查德·施罗克）
- **生卒**：1945-01-04 生于印第安纳州 Berne → **在世**（卒项一律留白）
- **国籍**：United States（美国）
- **身份**：化学家；MIT Frederick G. Keyes 化学讲席教授（1989 起，现为荣休教授）；2018 年起回母校 UC Riverside 任 Distinguished Professor 兼 George K. Helmkamp Founder's Chair；XiMo 公司共同创办人
- **家庭**：1971 年娶 Nancy Carlson，育二子 Andrew 与 Eric；Nancy Schrock 曾任 MIT 图书馆 Thomas F. Peterson Jr. 特藏管理员（2006–2013）；全家居马萨诸塞州 Winchester
- **教育轨迹**：
  - Mission Bay High School（加州圣地亚哥）
  - University of California, Riverside：BA 1967
  - Harvard University：PhD 1971，师从 John A. Osborn（论文 *Synthesis and study of some Group VIII transition metal catalysts*，1972 编目）
  - 博士后：University of Cambridge，与 Jack Lewis 合作
- **导师**：John A. Osborn（博士导师）；Jack Lewis（博士后导师，infobox "Other academic advisors" 明载）
- **研究领域**：有机化学、烯烃复分解反应——烷基亚烷基/次烷基配合物、金属杂环丁烷中间体、固氮机理与单分子固氮催化剂

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **印第安纳 Berne（1945）**：生于小城 Berne，在加州圣地亚哥 Mission Bay High School 完成中学教育。
2. **UC Riverside 本科（1967）**：BA 毕业；本科在 James Pitts 实验室的研究经历为他打下科研底子（2018 年他引此回忆回母校执教）。
3. **哈佛博士（1971）**：师从 John A. Osborn，研究第 VIII 族过渡金属催化剂。
4. **剑桥博士后**：随 Jack Lewis 在 University of Cambridge 做博士后研究——把金属–配体化学的功底再打深一层。
5. **杜邦岁月（1972–1975）**：1972 年受雇于 DuPont，在特拉华州 Wilmington 实验站 George Parshall 组工作——工业催化一线。
6. **MIT 就任（1975）**：加入 MIT 教员，1980 年升正教授，1989 年起任 Frederick G. Keyes 化学讲席教授，现为荣休教授。
7. **1974 α-氢消除**：发现 α 氢消除反应——由烷基配合物制备亚烷基（alkylidene）配合物、由亚烷基制备次烷基（alkylidyne）配合物。
8. **打开黑箱**：在 MIT 成为第一个阐明所谓"黑箱"复分解催化剂结构与机理的人——与 Chauvin 的理论描述互相印证。
9. **分子级设计**：证明经配体变化可大量制备钼/钨亚烷基与次烷基配合物——催化剂从此可以在分子层面按需设计。
10. **金属杂环丁烷**：大量工作证明 metallacyclobutanes 是烯烃复分解的关键中间体、metallacyclobutadienes 是炔烃复分解的关键中间体——为 Chauvin 机理补上实证。
11. **Schrock 催化剂与固氮**：原型催化剂 (R"O)₂(R'N)Mo(CHR)（R=叔丁基、R'=2,6-二异丙苯基、R"=C(Me)(CF₃)₂）已商品化（Sigma-Aldrich、XiMo）；复分解之外还研究固氮机理、开发模拟固氮酶的单分子催化剂（由二氮合成氨）。
12. **2005 诺贝尔化学奖**：与 Robert H. Grubbs、Yves Chauvin 共享——表彰其在烯烃复分解（有机合成技术）领域的工作；诺奖演讲 *Multiple Metal-Carbon Bonds for Catalytic Metathesis Reactions*。
13. **落叶归根（2018）**：回母校 UC Riverside 任 Distinguished Professor 兼 George K. Helmkamp Founder's Chair——自言期待"把 UCR 给我的一些东西还给 UCR"（页面引语，可引）；另为美国艺术与科学院、国家科学院院士，2007 年入选哈佛 Board of Overseers。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（林绿 forest） | `#175E54` | 钼钨金属卡宾的冷峻与生机（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（金属卡宾 badgeCarbene） | `#1B7A43` | 绿 Mo=W 亚烷基 / Schrock 卡宾 |
| 分类色 2（复分解机理 badgeMeta） | `#2E5A9E` | 蓝金属杂环丁烷 / 黑箱破译 |
| 分类色 3（固氮 badgeN2） | `#D97B29` | 琥珀二氮 / 固氮酶模拟 |
| 分类色 4（MIT 岁月 badgeMIT） | `#C0395B` | 玫瑰 Cambridge→DuPont→MIT 之路 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（双圆粗线相连），呼应「金属=碳双键」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Cinematic Experience** — Alex-Productions（`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/alex-productions/48-QL3O8MUFAm4-Cinematic-Experience.wav`；**不要复制 wav 文件**，Makefile 按此绝对路径引用）
- **风格**：开阔 / 电影感 / 步步推进
- **匹配理由**：
  - 电影感的推进节奏匹配 1974 α-氢消除 → 机理实证 → 分子级催化剂设计的一步步阶梯
  - 开阔基调匹配在世得主仍活跃（MIT→UC Riverside→XiMo）的"未完待续"
  - 与 Chauvin 篇（With Me）、Grubbs 篇（Eternals）形成 2005 三人组的气质分工：理论者温润、转化者恢弘、实验者笃行
- **时长**：以实际文件为准 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 钼与钨上的金属碳双键 / Richard R. Schrock 1945– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生年/在世留白、本名、国籍、教育、博士、导师、出生地/领域/荣誉）
03  施罗克之路 — Sanger 式时间线（10 节点：1945→1967→1971→1972→1974→1975→1980→1989→2005→2018）
04  早年：Berne 与圣地亚哥 (1945–1967) — 表格「时间|事件|结果」
05  哈佛与剑桥 (1967–1972) — 表格「阶段|导师|收获」
06  杜邦与 MIT (1972–1980) — 表格「阶段|环境|转折」
07  1974 α-氢消除 — 表格「问题|发现|意义」+ 公式框：烷基→亚烷基→次烷基链式制备
08  打开黑箱 — 表格「黑箱|实证|结果」
09  金属杂环丁烷与分子级设计 — 表格「中间体|反应|证据」+ 公式框：Schrock 催化剂原型 (R"O)2(R'N)Mo(CHR)
10  固氮与单分子催化 — 表格「问题|方法|结果」+ 固氮酶模拟
11  2005 诺贝尔化学奖 — 表格「人物|金属|贡献」（Chauvin 机理 / Schrock Mo,W / Grubbs Ru）
12  荣誉 — Sanger 式「类别|代表|意义」表格（NAS/AAAS 院士、ForMemRS 2008、Wilkinson Medal 2002、Basolo 2007 等）
13  产业与归根 — Sanger FFT 页式流程图（XiMo 2010 → Verbio 收购 → 2018 UC Riverside）+ UCR 引语框
14  结尾 — 「把黑箱拆开，把催化剂写成分子的语言。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 在世口径 | 1945-01-04 生，**在世**——封面、身份页、时间线卒项一律留白，勿写卒年 |
| 官方获奖理由 | **page.md 未载 2005 官方 citation 整句**——按页面口径写"因其对有机化学烯烃复分解反应的贡献共享 2005 诺奖"（intro 原句口径），勿杜撰整句 citation |
| 三人分工 | Chauvin = 机理（1970s 初）；Schrock = 钼/钨催化剂（1974 α-氢消除起步）；Grubbs = 钌催化剂——年份与金属勿混 |
| Parshall 身份 | George Parshall 是 DuPont 实验站的**组长**——用 colleague，勿写成博士/博士后导师 |
| Jack Lewis 身份 | 博士后导师，infobox "Other academic advisors (post doctoral)" 明载——勿与博士导师 Osborn 混 |
| Schrock 卡宾 | Schrock carbenes（早期/亲核性卡宾）以其名命名——勿与 Fischer 卡宾的命名混淆叙述（页面未提 Fischer） |
| XiMo 口径 | 2010 年与 Boston College 教授 Amir Hoveyda 共同创办（外链明载），总部瑞士、现属 Verbio AG——勿写成"MIT 衍生" |
| UCR 引语 | "My experience as an undergraduate at UCR..." 为页面明载引语，可引；其余叙述勿编引号 |
| Bazan 写法 | infobox 作 Guillermo Bazan（metadata 作 Guillermo C. Bazan）——以 infobox 为准入库 |
|metadata 噪声| metadata employer 含 DuPont Experimental Station / Cambridge——任职口径以正文 1972–1975 DuPont、1975– MIT 为准 |
| 卒项留白 | awards 表、时间线、身份页出现"卒"字段时全部留白，勿写"—"以外的猜测 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q202159 | ✅ |
| name_zh | 理查德·施罗克 | ✅ |
| name_en | Richard R. Schrock | ✅（新建记录，库内无同名） |
| birth_date | 1945-01-04 | ✅ |
| death_date | （在世，留空） | ✅ |
| nationality | United States | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | chemistry（metadata 口径）；person_field 细分见下 | ✅ |
| has_biography | false（Beamer 立传后置 1） | ✅ |

person_field 细分（rank 表）：

| rank | field | 说明 |
|---|---|---|
| 0 | olefin metathesis | 2005 诺奖工作：钼/钨催化剂 |
| 1 | organometallic chemistry | 金属–碳多重键化学 |
| 2 | alkylidene complexes | α-氢消除与亚烷基/次烷基配合物 |
| 3 | dinitrogen fixation | 固氮机理与固氮酶模拟 |

## 7. 社会关系入库清单

**师长 / 同事 / 配偶**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | John A. Osborn | 师→生（博士导师） | 哈佛博士导师，1971 |
| advisor-student | Jack Lewis | 师→生（博士后导师） | 剑桥博士后，infobox Other academic advisors |
| colleague | George Parshall | 无向 | DuPont 实验站组长（1972–1975） |
| colleague | Amir Hoveyda | 无向 | 2010 共同创办 XiMo 公司 |
| spouse | Nancy Carlson | 无向 | 1971 年结婚，育二子 |

**共同得主（2005 三人两两互指）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Yves Chauvin | 无向 | 2005 诺贝尔化学奖共同得主 |
| co-honored | Robert H. Grubbs | 无向 | 2005 诺贝尔化学奖共同得主 |

**门生（infobox 明载）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Guillermo Bazan | Schrock → 学生（博士） | infobox 博士生 |
| advisor-student | Christopher C. Cummins | Schrock → 学生（博士） | infobox 博士生 |
| advisor-student | Geoffrey Cloke | Schrock → 学生（博士后） | infobox Post-docs |

> **禁入库名单**：James Pitts（UCR 本科实验导师，仅引语提及）、Nancy Schrock 职务信息（非关系）、Verbio/Sigma-Aldrich（公司）。metadata doctoral_student 仅 Guillermo C. Bazan 一条，与 infobox 同人，无 metadata-only 增补。

## 8. 奖项清单

- ACS Award in Organometallic Chemistry（1985）；Harrison Howe Award（1990）；Alexander von Humboldt Award（1995）
- ACS Award in Inorganic Chemistry（1996）；Bailar Medal（1998）；ACS Cope Scholar Award（2001）
- Sir Geoffrey Wilkinson Lecturer and Medalist（2002）；Sir Edward Frankland Prize Lecturer（2004）
- August Wilhelm von Hofmann Medal（德国化学会，2005）；Nobel Prize in Chemistry（2005，共享）
- F. Albert Cotton Award in Synthetic Inorganic Chemistry（2006）；Theodore Richards Medal（2006）
- Basolo Medal（2007）；Foreign Member of the Royal Society，ForMemRS（2008）
- University of Sussex 化学图书馆以其命名（2013）；Schrock carbenes 以其名命名
- Paracelsus Prize、Rennes I 与 Zaragoza 荣誉博士（年份页面无载，勿写年份）

## 9. 机构清单

- 教育：Mission Bay High School（圣地亚哥）；University of California, Riverside（BA 1967）；Harvard University（PhD 1971）
- 任职：University of Cambridge（博士后，与 Jack Lewis）；DuPont Experimental Station（Wilmington，1972–1975，Parshall 组）；MIT（1975 加入，1980 正教授，1989 起 Frederick G. Keyes 讲席教授，现为荣休教授）；UC Riverside（2018 起 Distinguished Professor 兼 George K. Helmkamp Founder's Chair）
- 产业：XiMo, inc.（2010 与 Amir Hoveyda 共同创办，瑞士，现属 Verbio AG）
- 学术团体：American Academy of Arts and Sciences；National Academy of Sciences；Harvard Board of Overseers（2007）

## 10. 终审清单

- [x] 在世口径：卒项三处留白一致
- [x] 2005 三人共享 + 三人分工（机理/钼钨/钌）表述准确；citation 整句页面无载未杜撰
- [x] Parshall = 组长（colleague）、Jack Lewis = 博士后导师，不混
- [x] 1974 α-氢消除年份与链式制备表述准确
- [x] XiMo 2010 与 Hoveyda 共同创办、瑞士公司现属 Verbio
- [x] Bazan 以 infobox 写法入库；metadata 噪声未入库
- [x] 品牌 OpenMathAI、半角引号、封面国籍行、身份信息页齐备
- [x] `make distclean && make` 0 错误（Beamer 执行时验证）

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Richard_R._Schrock/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/` 已就位（真实照片或装饰圆占位，图注如实）
- [ ] **国籍**：封面顶部明示美国；**在世留白**三处一致
- [ ] **引语核对**：仅 UCR 回归引语带引号，可在原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一；Schrock 催化剂化学式排版正常
- [ ] 与 21 世纪批次其他篇格式对齐
