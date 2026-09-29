# Martin Chalfie（马丁·查尔菲）立传提示词

> qid=Q106699 · 1947-01-15 生于芝加哥（在世） · 美国生物化学家、神经生物学家 · 21 世纪 · 诺贝尔化学奖（2008，与 Shimomura / Tsien 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Martin_Chalfie/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 表格语义化 tabularx + 金色公式框 + 时间线页，是本篇的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像用 `images/` 目录本地文件，若缺省用装饰圆占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{lightbulb}\enspace 让基因发光的人\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（Martin Lee Chalfie）、国籍、出生地、教育、博士导师、核心领域、机构、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「绿色荧光点亮细胞」母题——散落的绿点象征 GFP 标记下的活细胞。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如 GFP 作为基因表达标记的原理。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Martin Lee Chalfie（中文惯称：马丁·查尔菲）
- **生卒**：1947-01-15 生于伊利诺伊州芝加哥（**在世**，页面无卒日）
- **国籍**：United States（美国）
- **身份**：美国科学家，哥伦比亚大学 University Professor（全校最高教席）；神经生物学家
- **家庭**：芝加哥长大；父 Eli Chalfie（1910–1996）为吉他手，母 Vivian Chalfie（娘家姓 Friedlen，1913–2005）经营服装店；外祖父 Meyer L. Friedlen 幼年自莫斯科移民芝加哥；祖父母 Benjamin 与 Esther 自 Brest-Litovsk 来美，犹太家庭。娶 Tulle Hazelrigg（后同在哥伦比亚任教）；1992 年 7 月得女 Sarah
- **教育轨迹**：
  - Niles East High School
  - 1965 入哈佛大学，原拟读数学，因融合化学、数学与生物之趣转生化
  - 三年级暑假在哈佛 Klaus Weber 实验室做研究（挫败体验，一度立志离开生物学）
  - 高年级修法律、戏剧、俄国文学课程；1969 毕业（BA）
  - 1971 夏在耶鲁 Jose Zadunaisky 实验室做出首篇论文，重拾信心
  - 回哈佛师从 Robert Perlman，1977 获神经生物学 PhD（论文 *Regulation of catecholamine biosynthesis and secretion in a rat pheochromocytoma*）
- **导师**：Robert L. Perlman（博士导师）
- **研究领域**：神经生物学（neurobiology）——*C. elegans* 触觉神经元发育与功能、GFP 基因表达标记

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **芝加哥吉他手之子（1947）**：服装店与吉他的家庭，犹太移民第三代。
2. **泳池边的队长（1965–1969）**：哈佛游泳队队长，获 Harold S. Ulen 奖杯（表彰领导力、体育精神与团队协作）；诺奖公布后其大一室友回忆 "He would always identify himself as a swimmer"（page.md 明载）。
3. **实验室挫败（1968）**：三年级暑假在 Klaus Weber 实验室的失败让他一度决定告别生物学——"It was so disheartening to completely fail that I decided I shouldn't be in biology."（对室友语，page.md 明载）。
4. **漂泊与重返（1969–1971）**：毕业后卖过裙子、教过康涅狄格 Hamden Hall 中学；1971 夏在耶鲁 Zadunaisky 实验室发表首篇论文。
5. **哈佛博士（1971–1977）**：师从 Robert Perlman 研究儿茶酚胺生物合成的调控，1977 获神经生物学博士。
6. **LMB 岁月（1977–1982）**：在剑桥 MRC 分子生物学实验室随 Sydney Brenner 与 John Sulston 做博士后；1985 三人合著 *C. elegans* 触觉神经环路论文。
7. **落脚哥伦比亚（1982）**：离开 LMB 加入哥伦比亚大学生物科学系，继续 *C. elegans* 触觉突变体研究。
8. **1988 年的转折点**：Paul Brehm 一场关于发光生物的研讨会让他初闻 GFP——其 GFP 之路由此开启（page.md 明载溯源）。
9. **1992 年里程碑**：关键实验落地，发表 "Green Fluorescent Protein as a Marker for Gene Expression"（Science）——GFP 从此成为活体基因表达的通用标记；该文位列分子生物学与遗传学领域被引最高的 20 篇论文之列。
10. **咖啡条件**：他引用妻子 Tulle Hazelrigg 未发表的研究成果，条件是连续一个月每晚煮咖啡、做饭、倒垃圾（page.md 明载的趣事，克制叙述）。
11. **睡过诺奖电话（2008）**：接获诺奖电话时在睡觉；醒来上网查名单，自嘲 "Okay, who's the schnook that got the Prize this time?"——发现"那个傻瓜"就是自己（page.md 原载）。
12. **2008 诺贝尔化学奖（三人共享）**：与下村脩、Roger Y. Tsien 共享 "for the discovery and development of the green fluorescent protein, GFP"；同获 E. B. Wilson Medal（与 Tsien 共享）。
13. **迟来的荣誉与担当**：American Academy of Arts and Sciences（2003）、NAS（2004）、Rosenstiel Award（2006，与 Tsien 共享）、AAAS Fellow（2007）、Institute of Medicine（2009）、Golden Goose Award（2012）、罗蒙诺索夫金质奖章（2018）、帕尔马大学物理学荣誉学位（2023-07-04）；2015 签署《气候变化梅瑙宣言》。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（荧光苔绿 deepgfp） | `#2F5D50` | GFP 荧光的沉稳苔绿——标记技术点亮生命的母题（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（线虫神经 badgeWorm） | `#5B4A2F` | 褐 *C. elegans* 触觉神经环路 |
| 分类色 2（GFP 标记 badgeMarker） | `#1B7A43` | 绿 GFP 基因表达标记 |
| 分类色 3（哈佛岁月 badgeHarvard） | `#7A1E28` | 绛红哈佛求学与博士岁月 |
| 分类色 4（LMB 剑桥 badgeLMB） | `#2C5F8A` | 蓝 MRC LMB 博士后岁月 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「荧光点亮下的细胞群落」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Last Hope** — Victor Cooper（文件 `music_audio/inspiring-electronic/24-ie5iLcdKiqk-Victor Cooper - Last Hope (Dramatic Powerful Epic Copyright Free Music).wav`；不要复制 wav 文件，Makefile 直接引用）
- **风格**：戏剧性 / 渐强 / 希望感
- **匹配理由**：
  - "希望" 匹配其弧线——从实验室挫败、漂泊教中学，到 1988 年一场研讨会重燃研究之火
  - "戏剧性渐强" 呼应 GFP 技术从一次报告到改变全生物学的爆发
  - "Last Hope" 暗合 GFP 作为"最后一根稻草"式的技术转机（他自己也一度放弃生物学）

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 让基因发光的人 / Martin Chalfie 1947– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士导师/领域/机构/荣誉）
03  查尔菲的一生 — Sanger 式时间线（10 节点：1947→1965→1969→1971→1977→1982→1988→1992→2008→2023）
04  芝加哥少年与哈佛游泳队长 (1947–1969) — 表格「时间|事件|结果」
05  挫败与漂泊 (1969–1971) — 表格「时间|事件|结果」
06  哈佛博士与 LMB 岁月 (1971–1982) — 表格「时间|事件|结果」（Perlman / Brenner / Sulston）
07  线虫触觉神经环路 (1982–1988) — 表格「问题|方法|结果」+ 公式框：触觉神经元 mec 突变体路径
08  GFP：从研讨会到 Science (1988–1992) — 表格「问题|方法|结果」+ 公式框：GFP 作为基因表达标记
09  2008 诺贝尔化学奖 — 公式框：获奖理由原句 + 三人分工（发现 / 表达 / 发展）+ 睡过电话趣事
10  哥伦比亚实验室 — 高斯式流程图（*C. elegans* 模型 → 神经发育 → 100+ 论文 / 25+ 高引）
11  荣誉长廊 — Sanger 式「类别|代表|意义」表格（NAS / Rosenstiel / E.B. Wilson / 罗蒙诺索夫金章 itemize）
12  家庭与趣事 — 表格「人物|关系|故事」（Tulle 咖啡条件 / 女儿 Sarah / 游泳队长）
13  遗产：点亮生命科学 — 四分类遗产盒 + 公式框：GFP 论文引用与 Golden Goose
14  结尾 — 「有时，照亮世界的火花来自一场偶然听到的报告。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2008 获奖 | **三人共享**（Shimomura / Chalfie / Tsien）；获奖理由 "for the discovery and development of the green fluorescent protein, GFP"；Chalfie 的分工是 **表达与作为基因表达标记的应用**——勿写"发现 GFP"（那是下村 1962） |
| Rosenstiel / E.B. Wilson | 2006 Rosenstiel 与 2008 E. B. Wilson Medal 均 **与 Roger Y. Tsien 共享**——勿写独享 |
| 挫败经历 | 三年级暑假在 **Klaus Weber** 实验室的失败（哈佛）；首篇论文来自 1971 夏 **Jose Zadunaisky** 实验室（耶鲁）——两人勿混 |
| 博士导师 | **Robert L. Perlman**（哈佛，1977 神经生物学博士）；Brenner/Sulston 是博士后合作者非导师 |
| LMB 年份 | 博士后至 1982 离开 LMB；三人合著触觉神经环路论文是 **1985**（离开后发表）——勿写"在 LMB 期间发表" |
| GFP 溯源 | 1988 **Paul Brehm** 研讨会 → 1992 关键实验与 Science 论文——勿写"1988 开始实验" |
| 本名 | Martin **Lee** Chalfie；父 Eli（吉他手）母 Vivian（服装店）——勿与他混淆 |
| 女儿 | Sarah，1992 年 7 月出生——勿写成年份不详 |
| 引语 | 仅可用 page.md 原载三处：Klaus Weber 失败自述、室友 "swimmer" 评价、schnook 自嘲——其余一律间接转述 |
| 在世 | 1947-01-15 生，**在世**（页面无卒日），"享年/卒于"禁写 |
| 犹太家庭背景 | 客观一句带过（祖辈移民与信仰），不做扩展 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q106699 | ✅ |
| name_zh | 马丁·查尔菲 | ✅ |
| name_en | Martin Chalfie | ✅ |
| birth_date | 1947-01-15 | ✅ |
| death_date | （在世，留空） | ✅ |
| nationality | United States | ✅ |
| primary_occupation | neuroscientist | ✅ |
| field_of_work | neurobiology（person_field 细分见下表） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

**person_field 细分 rank 表**：

| rank | field_en | field_zh |
|---|---|---|
| 0 | neurobiology | 神经生物学 |
| 1 | cell biology | 细胞生物学 |
| 2 | biochemistry | 生物化学 |
| 3 | developmental biology | 发育生物学 |

## 7. 社会关系入库清单

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Robert L. Perlman | 师→生（博士导师） | 哈佛博士导师，1977 获神经生物学博士 |
| colleague | Sydney Brenner | 无向 | 剑桥 MRC LMB 博士后合作者 |
| colleague | John Sulston | 无向 | LMB 博士后合作者，1985 合著 *C. elegans* 触觉神经环路论文 |
| colleague | Klaus Weber | 无向 | 哈佛三年级暑假在其实验室做研究 |
| colleague | Jose Zadunaisky | 无向 | 1971 夏耶鲁实验室研究，产出其首篇论文 |
| co-honored | Osamu Shimomura | 无向 | 2008 诺贝尔化学奖共同得主 |
| co-honored | Roger Y. Tsien | 无向 | 2008 诺贝尔化学奖共同得主（Rosenstiel 2006 与 E.B. Wilson 2008 亦共享） |
| spouse | Tulle Hazelrigg | 无向 | 妻子，后同在哥伦比亚大学任教 |

> Paul Brehm（1988 研讨会讲者）是 GFP 之路的触发者，但非合作关系，**不入库**；metadata.json 无博士生字段。

## 8. 奖项清单

- Nobel Prize in Chemistry（2008，与 Shimomura / Tsien 三人共享）
- E. B. Wilson Medal, American Society for Cell Biology（2008，与 Tsien 共享）
- Lewis S. Rosenstiel Award, Brandeis University（2006，与 Tsien 共享）
- Golden Goose Award（2012）
- Lomonosov Gold Medal（2018）
- American Academy of Arts and Sciences 院士（2003）；National Academy of Sciences 院士（2004）；Institute of Medicine（2009）；AAAS Fellow（2007）
- Honorary degree in physics, University of Parma（2023）
- Foreign Member of the Royal Society（英国皇家学会外籍会士，infobox 载）

## 9. 机构清单

- 教育：Niles East High School；Harvard University（BA 1969；PhD 1977 神经生物学）；Yale University（1971 夏研究）
- 任职：Harvard（博士）、MRC Laboratory of Molecular Biology（博士后，至 1982）、Columbia University 生物科学系（1982–，University Professor）；剑桥 University of Cambridge（LMB 期间关联机构）
- 妻 Tulle Hazelrigg 后亦任教哥伦比亚大学

## 10. 终审清单

- [x] 生卒 1947-01-15，在世留白；出生地芝加哥
- [x] 2008 三人共享；获奖理由原句忠实；发现/表达/发展三人分工准确
- [x] 博士导师 Perlman；Brenner/Sulston 为 LMB 博士后合作者（非导师）
- [x] Klaus Weber（哈佛挫败）与 Zadunaisky（耶鲁首篇论文）勿混
- [x] 引语仅三处 page.md 原载（挫败自述 / swimmer / schnook）
- [x] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Martin_Chalfie/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：`images/` 目录 2018 年照片就位（缺省装饰圆占位）
- [ ] 国籍：封面顶部明示美国
- [ ] 引语核对：引语必须在 page.md 原文找到（三处原载）
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 黄金参照）对齐
