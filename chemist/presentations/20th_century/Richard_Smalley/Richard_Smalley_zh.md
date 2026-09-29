# Richard Smalley（理查德·斯莫利）立传提示词

> qid=Q106746 · 1943-06-06 – 2005-10-28 · 美国化学家 · 20 世纪 · 诺贝尔化学奖（1996，三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Richard_Smalley/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。本地 images.txt 无可用肖像（仅 Wikiquote 图标）：先经 Wikipedia REST API `page/summary` 查 infobox 实际文件名下载，404 则用装饰圆占位（图注须如实）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{atom}\enspace 纳米世界的布道者\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「纳米碳管 / 原子簇」母题——圆点暗示团簇束流与纳米管阵列。
5. **表格语义化 + 公式框**（★ Sanger 版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如 `C60`（20 个六边形 + 12 个五边形，足球结构；Smalley 页口径：剪拼六边形悟出足球结构并命名以致敬 Buckminster Fuller）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Richard Errett Smalley（中文惯称：理查德·斯莫利；Rice 大学 Gene and Norman Hackerman 化学/物理/天文讲席教授；参议院决议称其 "Father of Nanotechnology"）
- **生卒**：1943-06-06 生于俄亥俄州 Akron（美国）→ 2005-10-28 逝于得州 Houston（M.D. Anderson Cancer Center；白血病——页面注明有 non-Hodgkin's lymphoma 与 chronic lymphocytic leukemia 两种报道口径），享年 62
- **国籍**：United States（美国）
- **身份**：化学家（Rice University 教授；1996 诺贝尔化学奖得主；纳米技术旗手）
- **家庭**：四兄妹中最幼，在密苏里州 Kansas City 长大；父 Frank Dudley Smalley Jr.（农机行业期刊 *Implement and Tractor* 的 CEO）、母 Esther Rhoads Smalley（Richard 青少年时完成 BA，深受数学家 Norman N. Royall Jr. 影响并向儿子传递科学之爱）、舅母 Sara Jane Rhoads（早期女性化学家，引其入化学之门并建议就读 Hope College）。四次婚姻：Judith Grace Sampieri（1968–78）、Mary L. Chapieski（1980–94）、JoNell M. Chauvin（1997–98）、Deborah Sheffield（2005）；二子 Chad Richard Smalley（1969-06-08 生）、Preston Reed Smalley（1997-08-08 生）
- **教育轨迹**：
  - Hope College（两年，化学强校，舅母建议）
  - University of Michigan（BS 1965；本科在 Raoul Kopelman 实验室做研究；学业间隙在工业界工作，形成其独特管理风格）
  - Princeton University（PhD 1973）
- **导师**：Elliot R. Bernstein（博士导师，Princeton）
- **博士**：1973，《The lower electronic states of 1,3,5 (sym)-triazine》；1973–76 于 University of Chicago 随 Donald Levy 与 Lennard Wharton 做博士后（超声束流激光光谱学先驱）
- **研究领域**：物理化学（无机/半导体团簇形成、脉冲分子束、飞行时间质谱）→ 富勒烯 → 碳纳米管与纳米技术

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **家学三源（1943–1965）**：父亲的工业与机械、母亲的科学之爱、舅母的化学实验室——三位一体启蒙，舅母引其入 Hope College。
2. **从 Hope 到 Michigan（1961–1965）**：两年 Hope College 转学 Michigan，1965 BS；工业界打工练出的管理风格日后带出大团队。
3. **Princeton 博士（1965–1973）**：三嗪（sym-triazine）低电子态研究，师从 Elliot R. Bernstein。
4. **芝加哥超声束流（1973–1976）**：随 Levy 与 Wharton 开创超声束流激光光谱——为团簇实验铺路。
5. **落户 Rice（1976–1990）**：1976 加入 Rice；1979 年参与创建 Rice Quantum Institute（1986–96 任主席）；1982 获 Gene and Norman Hackerman 讲席；1990 兼物理系教授；NAS（1990）与美国艺术与科学院（1991）院士。
6. **团簇纲领**：脉冲分子束 + 飞行时间质谱研究无机/半导体团簇的形成——正是这套本领让 C60 得以现形。
7. **Curl 引线**：Robert Curl 介绍他结识 Harry Kroto，共解天文尘埃之谜（R Coronae Borealis 等老星抛出的富碳尘埃）。
8. **足球之悟（1985）**：剪拼六边形纸样三维成球——悟出 C60 为 20 个六边形 + 12 个五边形的足球结构；**Smalley 页口径：命名 C60 亦归 Smalley**（致敬以网格穹顶闻名的建筑师 Buckminster Fuller）。
9. **诺奖三论文**：*Nature*（1985-11-14，"C60: Buckminsterfullerene"）→ *JACS*（1985，镧内嵌富勒烯）→ *J. Phys. Chem.*（1986，大碳团簇反应性与烟灰形态关联）。
10. **四人未列名**：研究生 Heath、Liu、O'Brien 参与了获诺奖的工作，但诺奖只可列三人；Smalley 在诺奖演讲中提及 Heath 与 O'Brien——Heath 后任 Caltech 教授。
11. **纳米技术旗手（1990s–2005）**：1990 年参与创建 CNST（1996 任所长）；HiPco 高压 CO 法批量制高质量纳米管；创办 Carbon Nanotechnologies Inc.；实验室口号 "If it ain't tubes, we don't do it"（页面实载，可引）；身后 CNST 更名 Richard E. Smalley Institute，2015 年与 RQI 合并为 Smalley-Curl Institute。
12. **与 Drexler 的论战**：公开质疑分子装配器，提出 "fat fingers" 与 "sticky fingers" 两难；忧心 "gray goo" 之说损害纳米技术公众支持；两人书信往还刊于 *C&EN*（页面实载原词，可引）。
13. **最后的呐喊（1999–2005）**：1999 确诊癌症；化疗期间仍赴国会作证，推动《21 世纪纳米技术研究与发展法》（2003-12-03 总统签署）；"The Terawatt Challenge" 与 "Top Ten Problems of Humanity"（能源居首）；口号 "Be a scientist, save the world"（页面实载，可引）；晚年重拾信仰——页面实载原句 "I now think the answer is very simple: it's true. God did create the universe about 13.7 billion years ago..."；逝后参议院决议致敬其 "Father of Nanotechnology"。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（纳米深绿 nanogreen） | `#2F5D50` | 碳纳米管与分子工程的深色（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（团簇与谱学 badgeCluster） | `#1E4E79` | 蓝分子束 / 飞行时间质谱 |
| 分类色 2（C60 发现 badgeC60） | `#B07A2A` | 琥珀足球之悟 / 诺奖三论文 |
| 分类色 3（纳米旗手 badgeNano） | `#5B2A86` | 紫 HiPco / CNST / NNI |
| 分类色 4（能源与呐喊 badgeEnergy） | `#8A1E2D` | 猩红 Terawatt Challenge / 国会作证 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「纳米碳管 / 原子簇束流」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Savage** — Alex-Productions（清单指定，文件 `music_audio/alex-productions/34-pILVwyuW3jw-Savage.wav`；不要复制 wav 文件）
- **风格**：有力 / 紧张 / 攻坚感
- **匹配理由**：
  - "有力" 匹配其战斗气质——从团簇攻坚到国会作证，一生高歌猛进
  - "紧张" 匹配与 Drexler 的公开论战与 "If it ain't tubes, we don't do it" 的偏执专注
  - "攻坚" 匹配 1999 年后带病推动立法的最后一战
- **时长**：以实际曲目时长为准，不足/超出由 ffmpeg `-shortest` 对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 纳米世界的布道者 / Richard Smalley 1943–2005 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  斯莫利的一生 — Sanger 式时间线（10 节点：1943→1965→1973→1976→1979→1985→1990→1996→2003→2005）
04  早年：家学三源 (1943–1965) — 表格「人物|影响|结果」（父/母/舅母）
05  Princeton 与芝加哥 (1965–1976) — 表格「时间|事件|结果」
06  团簇纲领 (1976–1985) — 表格「对象|方法|结果」（脉冲分子束 / TOF 质谱 / 半导体团簇）
07  C60：足球之悟 (1985) — 表格「问题|方法|结果」+ 公式框：C60 = 20 六边形 + 12 五边形 · 三篇诺奖论文
08  1996 诺贝尔化学奖 — 三人共享页（Smalley/Curl 同校 + Kroto 异校）+ 公式框：获奖口径
09  纳米技术旗手 (1990–2005) — 表格「举措|内容|结果」（CNST / HiPco / CNI / 口号引语）
10  与 Drexler 的论战 — 表格「立场|论据|影响」（fat fingers / sticky fingers / gray goo / C&EN 书信）
11  荣誉清单 — Sanger 式「类别|代表|意义」表格（Langmuir 1991 → Franklin 1996 → Seaborg 2002）
12  最后的呐喊 (1999–2005) — 国会立法流程图页（Wyden 提案 → 参众两院 → 2003-12-03 签署）+ Top Ten 清单
13  遗产与纪念 — Smalley Institute → Smalley-Curl Institute（2015）+ 参议院 "Father of Nanotechnology" 决议
14  结尾 — 「他教会我们：从一团碳蒸气里，也能看见一个产业的黎明。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1996 共享口径 | 与 **Robert Curl（Rice 同校）、Harold Kroto（Sussex）** 三人共享；官方口径照页面 "the discovery of a new form of carbon, buckminsterfullerene" |
| 命名归属 | **三页三口径**：Smalley 页作 **Smalley 命名**（He was also responsible for the name）、Curl 页作团队命名、Kroto 页作 Kroto 命名——**Smalley 篇按 Smalley 页写，勿跨页混写** |
| 足球结构数据 | Smalley 页作 **20 个六边形 + 12 个五边形**（先后顺序与 Kroto 页相反）——照本页口径 |
| 死因口径 | 白血病，页面明言 **variously reported**（non-Hodgkin's lymphoma 与 chronic lymphocytic leukemia 两说并存）——须如实并列，勿单取一说 |
| "Father of Nanotechnology" | 是**美国参议院决议的致敬语**（crediting him as）——引用时注明出处，勿写成官方头衔 |
| 四次婚姻 | 页面明载四段婚姻与两个儿子——身份信息页如实并写，勿隐去或只写一段；DB 不入库（见 §7） |
| 宗教转向 | 晚年信仰段落为页面明载、原句可溯源；呈现保持客观（页面同时记载其葬礼由 Old Earth creationist Hugh Ross 致辞），勿作褒贬 |
| Drexler 论战 | "fat fingers problem" / "sticky fingers problem" 为页面原词；论战形式为 C&EN **point-counterpoint 书信**——勿写成法庭/学术仲裁 |
| Top Ten 清单 | 顺序固定：Energy 第一、Water 第二……Population 第十——排序勿乱；与联合国 Ten Threats 是页面提示的"可比较"关系，勿写成"对标官方文件" |
| 立法细节 | Bill 189 由参议员 **Ron Wyden** 于 2003-01-16 提出参院版；参院 11-18 通过、众院次日 405–19 通过、12-03 总统签署为 Public Law 108-153——数字与日期照页面 |
| Heath/Liu/O'Brien | 参与获诺奖工作但未列名；Smalley 诺奖演讲提及 Heath 与 O'Brien——如实并写，勿升格 |
| 学位路径 | Hope College（两年）→ University of Michigan BS 1965 → Princeton PhD 1973——**无硕士学位记载**，勿补写 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q106746 | ✅ |
| name_zh | 理查德·斯莫利 | ✅ |
| name_en | Richard Smalley | ✅ |
| birth_date | 1943-06-06 | ✅ |
| death_date | 2005-10-28 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | fullerene（person_field 细分：fullerene / nanotechnology / physical chemistry / laser spectroscopy，带 rank） | ✅ |
| has_biography | false（立传完成后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 同事 / 共同得主 / 论战**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Elliot R. Bernstein | 师→生（博士导师） | Princeton，sym-triazine 低电子态 |
| advisor-student | Donald Levy | 师→生（博士后导师） | 芝加哥 1973–76，超声束流激光光谱 |
| influence | Sara Jane Rhoads | 无向 | 舅母、早期女性化学家，引其入化学并建议 Hope College |
| colleague | Robert Curl | 无向 | Rice 同事，Curl 引其结识 Kroto |
| colleague | Harry Kroto | 无向 | 1985 年合作发现 C60 |
| colleague | James R. Heath | 无向 | C60 论文合作研究生，后任 Caltech 教授，诺奖演讲中提及 |
| co-honored | Robert Curl | 无向 | 1996 诺贝尔化学奖共同得主 |
| co-honored | Harry Kroto | 无向 | 1996 诺贝尔化学奖共同得主 |
| other | K. Eric Drexler | 无向 | 分子装配器公开论战（C&EN point-counterpoint 书信） |

> **禁入库名单（metadata.json-only 或防噪声）**：Lennard Wharton（红链，博士后合作者之一）；Sean C. O'Brien、Yuan Liu（红链/仅一句提及）；Raoul Kopelman（本科实验室一句）；四位配偶与两名儿子（正文虽明载但防噪声不入库）；Malcolm Gillis、Norman Hackerman（机构与讲席冠名人物）；Hugh Ross（葬礼致辞者）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1996，与 Curl/Kroto 共享）
- Harold W. Dodds Fellow, Princeton（1973）；Alfred P. Sloan Fellow（1978–80）
- Fellow of the American Physical Society（1987）；Fellow of the AAAS（2003）
- Irving Langmuir Prize in Chemical Physics, APS（1991）
- Popular Science Magazine Grand Award（1991）
- APS International Prize for New Materials（1992，与 Curl/Kroto 共享）
- Ernest O. Lawrence Memorial Award, DOE（1992）
- Welch Award in Chemistry（1992）
- Auburn-G.M. Kosolapoff Award（1992）；Southwest Regional Award, ACS（1992）
- William H. Nichols Medal, ACS New York Section（1993）；John Scott Award, City of Philadelphia（1993）
- Hewlett-Packard Europhysics Prize, EPS（1994，与 Kraetschmer/Huffman/Kroto 共享）
- Harrison Howe Award, ACS Rochester（1994）；Madison Marshall Award, ACS North Alabama（1995）
- Franklin Medal, The Franklin Institute（1996）
- Distinguished Civilian Public Service Award, Department of the Navy（1997）；American Carbon Society Medal（1997）
- Top 75 Distinguished Contributors, C&EN（1998）；Glenn T. Seaborg Medal, UCLA（2002）
- Lifetime Achievement Award, Small Times Magazine（2003）
- Distinguished Alumni Award, Hope College（2005）；SPIE 50th Anniversary Visionary Award（2005）
- National Historic Chemical Landmark（2010）；Citation for Chemical Breakthrough Award（2015）
- Franklin Medal 与 John Scott Award、Richtmyer Memorial Lecture Award（metadata 列出，正文年份以 §8 各条为准）

## 9. 机构清单

- 教育：Hope College（两年）→ University of Michigan（BS 1965）→ Princeton University（PhD 1973）
- 任职：University of Chicago（博士后 1973–76）→ Rice University（1976–；1982 Gene and Norman Hackerman 讲席；1990 兼物理系教授）
- 创建/服务：Rice Quantum Institute（1979 参与创建，1986–96 主席）；Center for Nanoscale Science and Technology（1990 参与创建，1996 所长）；Carbon Nanotechnologies Inc.
- 命名遗产：Richard E. Smalley Institute for Nanoscale Science and Technology（2005 身后更名）→ Smalley-Curl Institute（2015 合并）

## 10. 终审清单

- [x] 生卒 1943-06-06 / 2005-10-28，享年 62，出生地 Akron、去世地 Houston M.D. Anderson
- [x] 死因两说（non-Hodgkin's lymphoma / CLL）如实并列
- [x] 1996 三人共享（Curl/Kroto）表述准确；命名与足球数据按 Smalley 页口径
- [x] "Father of Nanotechnology" 注明为参议院决议致敬语
- [x] 四次婚姻如实呈现且 DB 不入库；Drexler 论战用页面原词
- [x] 引语全部可在本地 Wikipedia 原文找到（口号、Terawatt、Be a scientist、晚年信仰原句）
- [x] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Richard_Smalley/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：按 §0.1 回退处理（REST API → 装饰圆），图注如实
- [ ] **国籍**：封面顶部明示美国
- [ ] **引语核对**：口号与信仰原句必须在 Wikipedia 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐（对照 Frederick_Sanger_zh.tex）

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾，本提示词不改总名单。
> **最重要的事：每写一页就 make，看到溢出就修。**
