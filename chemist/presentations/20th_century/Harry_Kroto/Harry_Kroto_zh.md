# Harry Kroto（哈里·克罗托）立传提示词

> qid=Q157250 · 1939-10-07 – 2016-04-30 · 英国化学家 · 20 世纪 · 诺贝尔化学奖（1996，三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Harry_Kroto/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。本地 images.txt 已有真实照片 URL：`Sir_Harold_Kroto_at_CSICON_2011.JPG`（2011 年 CSICON 照片）——直接下载 500px 版本使用；另备 C60 结构示意图（`C60_Image_for_Cover_cropped_3.png`）可作核心贡献页插图。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{futbol}\enspace 从星际碳链到足球烯\enspace·\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「足球烯 / 星际尘埃」母题——圆点暗示五边形-六边形拼接的笼面与星际碳链。
5. **表格语义化 + 公式框**（★ Sanger 版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如 `C60`（12 个五边形 + 20 个六边形，足球对称性；激光气化石墨 → 碳蒸气凝聚自发成笼）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Sir Harold (Walter) Kroto，本名 Harold Walter Krotoschiner（中文惯称：哈里·克罗托；FRS；Knight Bachelor）
- **生卒**：1939-10-07 生于英格兰剑桥郡 Wisbech → 2016-04-30 逝于东萨塞克斯郡 Lewes（渐冻人症/ALS 并发症），享年 76
- **国籍**：United Kingdom（英国）
- **身份**：化学家（Sussex 约 40 年 → 2004 起 Florida State University Francis Eppes 讲席教授；1996 诺贝尔化学奖得主）
- **家庭**：父 Heinz、母 Edith Krotoschiner——双亲均生于柏林，1930 年代为逃离纳粹德国以难民身份赴英；父系来自波兰 Bojanowo、母系出自柏林，父为犹太人；姓名源于西里西亚。二战期间父亲曾作为"敌侨"被拘于马恩岛，幼年在 Bolton 由母亲抚养。1955 年父亲将姓改为 Kroto。1963 年娶同在 Sheffield 就读的 Margaret Henrietta Hunter，育二子
- **教育轨迹**：
  - Bolton School（与演员 Ian McKellen 同窗）
  - 童年痴迷 Meccano 金属拼装玩具 + 战后在父亲的气球厂帮工——自认皆有助于科研动手能力
  - University of Sheffield（1958 入学；sixth form 化学老师 Harry Heaney 认定 Sheffield 化学系全英最佳而推荐）
  - 一等荣誉化学 BSc（1961）；分子光谱 PhD（1964）
- **博士**：1964，《The spectra of unstable molecules under high resolution》——**页面未载博士导师姓名，禁写**
- **研究领域**：分子光谱、富勒烯、天体化学；磷碳多重键新化学（phosphaalkene/phosphaalkyne）的开创者之一

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **难民之子（1939–1955）**：柏林出生的双亲、纳粹阴霾下的逃亡、父亲被拘马恩岛——1955 年改姓 Kroto。
2. **Meccano 与气球厂（1940s）**：金属拼装玩具与气球厂帮工练就的空间与动手直觉——日后"把 12 个五边形和 20 个六边形拼成球"的伏笔。
3. **Sheffield 一等荣誉（1958–1964）**：化学 BSc 一等荣誉；博士转向分子光谱（由有机化学经光谱学入量子化学）；学生杂志 *Arrows* 美术编辑、校网球队（两进 UAU 决赛）、学生田径委员会主席（1963–64）；博士期间做出第一批 phosphaalkenes 并研究碳的低价氧化物 O=C=C=C=O。
4. **渥太华与贝尔实验室（1964–1967）**：在 Gerhard Herzberg（NRC Ottawa）分子光谱组做两年博士后；1966–67 于 Bell Laboratories 做拉曼与量子化学。
5. **Sussex 三十年（1967–2004）**：不稳定/亚稳物种光谱研究，开创碳与 S/Se/P 多重键新化学；与 John Nixon 合作用微波谱发现多个新磷物种——phosphaalkene/phosphaalkyne 化学的诞生。
6. **从实验室到星际（1975–）**：升任正教授同年，与 David Walton 合作的长链碳分子研究接入加拿大射电天文观测——这些碳链竟大量存在于星际空间与富碳红巨星外层大气。
7. **1985 年莱斯之行**：基于 Sussex 研究与恒星观测，赴 Rice 大学与 Curl、Smalley 及研究生 Heath、O'Brien、Liu 合作，激光气化石墨模拟红巨星大气化学。
8. **C60 现身**：不但找到想找的长碳链，更发现可自发形成的稳定 C60——12 个五边形 + 20 个六边形、足球对称性；**Kroto 页口径：Kroto 命名 buckminsterfullerene**（网格穹顶概念提示了可能结构）。
9. **转向求证（1985 后）**：C60 的发现使其研究重心从光谱学转向证明 C60 结构概念并开发其化学与材料意涵。
10. **1996 诺贝尔化学奖**：与 Robert Curl、Richard Smalley 共享——官方口径 "for their discovery of fullerenes"（页面实载）；同年获 Knight Bachelor（1996 New Year Honours）。
11. **科学教育与人文主义（1995–2016）**：1995 年共同创立 Vega Science Trust（280+ 部科学影片，2012 年关闭）；2009 年创建 GEOset 全球教育平台；自称"三宗教"——国际特赦主义、无神论与幽默（页面实载原句，可引）；2003 年为 22 位签署 Humanist Manifesto 的诺奖得主之一；2015 年签署 Mainau 气候变化宣言（76 位诺奖得主，COP21 之际交予奥朗德）。
12. **平面设计师克罗托**：因 C60 推迟开艺术设计工作室之梦——Sunday Times 书封设计奖（1964）、Science pour l'Art 奖（1994）、2001 年设计英国化学诺奖邮票、2004 年入选皇家艺术研究院夏季展。
13. **谢幕（2016）**：ALS 并发症逝于 Lewes；Curl 与 Heath 在 *Nature* 讣闻中写其幽默"类似 Monty Python 的促狭"（页面实载）；Sheffield 北校区有 Kroto Innovation Centre 与 Kroto Research Institute。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（星际深青 stellargreen） | `#1E6B52` | 星际碳链到足球烯的绿色旅程（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（分子光谱 badgeSpec） | `#1E4E79` | 蓝微波谱 / 不稳定物种 / 磷碳多重键 |
| 分类色 2（C60 发现 badgeC60） | `#B07A2A` | 琥珀激光石墨 / 足球对称性 |
| 分类色 3（星际连线 badgeAstro） | `#5B2A86` | 紫射电天文 / 红巨星 / 星尘 |
| 分类色 4（教育与设计 badgeEdu） | `#8A1E2D` | 猩红 Vega / GEOset / 邮票设计 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「足球烯 / 星际尘埃」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Daylight** — Alex-Productions（清单指定，文件 `music_audio/alex-productions/44-JoyIRE5k2Yo-Daylight.wav`；不要复制 wav 文件）
- **风格**：明亮 / 上扬 / 好奇心
- **匹配理由**：
  - "白昼" 匹配其公众形象——把科学教育的光带到电视与网络的布道者
  - "明亮" 匹配其审美气质——设计师出身、诺奖邮票设计者的视觉之趣
  - "好奇" 匹配其学术路径——从实验室光谱一路追到星际空间
- **时长**：以实际曲目时长为准，不足/超出由 ffmpeg `-shortest` 对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 从星际碳链到足球烯 / Harry Kroto 1939–2016 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  克罗托的一生 — Sanger 式时间线（10 节点：1939→1958→1964→1967→1975→1985→1990→1996→2004→2016）
04  难民之子与 Meccano (1939–1958) — 表格「时间|事件|结果」
05  Sheffield：光谱学起步 (1958–1967) — 表格「时间|事件|结果」（含 Herzberg 博士后与 Bell Labs）
06  Sussex：磷碳新化学 (1967–1985) — 表格「对象|方法|结果」（Nixon 磷物种 / Walton 长碳链）
07  从实验室到星际 (1975–1985) — 表格「对象|观测|结果」（射电天文证实星际碳链 / 红巨星）
08  C60：足球烯的诞生 (1985) — 表格「问题|方法|结果」+ 公式框：C60 = 12 五边形 + 20 六边形
09  1996 诺贝尔化学奖 — 三人共享页（Curl/Smalley Rice + Kroto Sussex）+ 公式框：获奖口径 "for their discovery of fullerenes"
10  科学教育布道者 (1995–2016) — 表格「项目|形式|结果」（Vega 280+ 部 / GEOset / 人文主义三宗教引语）
11  荣誉清单 — Sanger 式「类别|代表|意义」表格（Tilden 1981-82 → Copley 2002 → Knight Bachelor 1996）
12  平面设计师的另一面 — 流程图页（书封 1964 → Science pour l'Art 1994 → 诺奖邮票 2001 → 皇家艺术研究院 2004）
13  遗产与纪念 — Kroto Innovation Centre / Kroto Research Institute + Mainau 宣言 2015
14  结尾 — 「他先在星际找到了碳链，再在地球上把它拼成了球。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1996 共享口径 | 与 **Robert Curl、Richard Smalley** 三人共享；官方口径照页面 "for their discovery of fullerenes" |
| 命名归属 | **三页三口径**：Kroto 页作 **Kroto 命名**（after Buckminster Fuller）、Curl 页作团队命名、Smalley 页作 Smalley 命名——**Kroto 篇按 Kroto 页写 Kroto 命名，勿跨页混写** |
| 本名与改姓 | 本名 **Harold Walter Krotoschiner**（西里西亚来源），**1955 年由父亲改姓 Kroto**——勿写成本人成年后改名 |
| 博士导师 | 页面（infobox 与正文）**未载博士导师姓名**——身份信息页"师承"栏只能填博士后导师 Herzberg，博士导师栏写"页面无载"，**严禁编造 Sheffield 导师** |
| 借装置口径 | Kroto 页作"1985 年 Kroto 联系 Curl 想用 Smalley 的装置"；Smalley 页作"Curl 介绍 Kroto 给 Smalley"——各篇忠于本页，Kroto 篇照本页写 |
| Copley 年份 | 荣誉清单作 **Copley Medal, 2002**（按本地页面；勿凭外部记忆改 2004） |
| Knight Bachelor | **1996 New Year Honours** 授勋——与诺奖同年，勿写成"因诺奖封爵"的另一年份 |
| 无神论内容 | "三宗教"引语与 Humanist Manifesto、Mainau 宣言均为页面明载可写，但保持客观转述；Madoff 引语（"The only mistake Bernie Madoff made was to promise returns in this life."）页面实载可用 |
| Iraq 信件 | 2003 年 Times 公开信由**Joseph Rotblat 执笔**、Kroto 发起组织 12 位英国诺奖得主签署——归属勿反 |
| Europhysics 奖 | 1994 年 HP Europhysics Prize 与 Kraetschmer、Huffman、Smalley 共同获奖（C60 宏量制备验证线）——是共同获奖非诺奖，勿写成"诺奖得主线" |
| 荣誉博士 | 共 42 个荣誉学位（页面列表），其中 Hertfordshire、Exeter 两校因关闭化学系**被退回**——"42 个"为可写事实，"42 位"人数勿写错基数 |
| 同名区分 | Harold Kroto / Harry Kroto 为同一人；勿与 Harold Krotoschiner 歧义化处理；Mario Kroto 等无此人 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q157250 | ✅ |
| name_zh | 哈里·克罗托 | ✅ |
| name_en | Harry Kroto | ✅ |
| birth_date | 1939-10-07 | ✅ |
| death_date | 2016-04-30 | ✅ |
| nationality | United Kingdom | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | molecular spectroscopy（person_field 细分：molecular spectroscopy / fullerene / astrochemistry / phosphaalkene chemistry，带 rank） | ✅ |
| has_biography | false（立传完成后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 同事 / 共同得主 / 门生**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Gerhard Herzberg | 师→生（博士后导师） | 渥太华 NRC 分子光谱组两年博士后 |
| advisor-student | Perdita Barran | Kroto → 学生 | infobox 博士生 |
| colleague | John Nixon | 无向 | Sussex 同事，微波谱发现多个新磷物种 |
| colleague | David Walton | 无向 | Sussex 同事，长链碳分子与射电天文连线 |
| colleague | Robert Curl | 无向 | 1985 年借 Rice 激光装置合作 |
| colleague | Richard Smalley | 无向 | 1985 年 Rice 合作 |
| co-honored | Robert Curl | 无向 | 1996 诺贝尔化学奖共同得主 |
| co-honored | Richard Smalley | 无向 | 1996 诺贝尔化学奖共同得主 |
| spouse | Margaret Henrietta Hunter | 无向 | 1963 年结婚，育二子 |

> **禁入库名单（metadata.json-only 或防噪声）**：James R. Heath、Sean C. O'Brien、Yuan Liu（合作研究生/红链，Kroto 页仅一句提及）；Alan Marshall、Naresh Dalal、Tony Cheetham（FSU 研究合作仅一句带过，防噪声）；Wolfgang Kraetschmer、Don Huffman（仅 1994 Europhysics Prize 共同获奖，非合作关系）；Richard Dawkins、Joseph Rotblat、Ian McKellen（传记关联人物，非学术关系）；两名儿子（未具名细节）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1996，与 Curl/Smalley 共享）
- Knight Bachelor（1996 New Year Honours）
- Tilden Lecturer/Prize, Royal Society of Chemistry（1981–82）
- Fellow of the Royal Society，FRS（1990）
- International Prize for New Materials, American Physical Society（1992，与 Curl/Smalley 共享）
- Italgas Prize for Innovation in Chemistry（1992）
- Longstaff Medal, Royal Society of Chemistry（1993）
- Hewlett Packard Europhysics Prize（1994，与 Kraetschmer/Huffman/Smalley 共享）
- Carbon Medal, American Carbon Society（1997，与 Curl/Smalley 共享）
- Dalton Medal, Manchester Literary and Philosophical Society（1997）
- Blackett Lectureship, Royal Society（1999）
- Faraday Award and Lecture, Royal Society（2001）
- Erasmus Medal, Academia Europaea（2002）
- Copley Medal, Royal Society（2002，按本地页面）
- Golden Plate Award（2002）；Order of Cherubini, Torino（2005）
- Foreign Associate of the National Academy of Sciences（2007）；Kavli Lecturer（2007）
- National Historic Chemical Landmark（2010）；Citation for Chemical Breakthrough Award（2015）
- Michael Faraday Prize；James C. McGroddy Prize for New Materials；EPS Europhysics Prize；IET Kelvin Lecture（metadata 列出——与正文条目合并核对后再写年份）

## 9. 机构清单

- 教育：Bolton School → University of Sheffield（BSc 1961、PhD 1964）
- 任职：NRC Ottawa（Herzberg 组博士后）→ Bell Laboratories（1966–67）→ University of Sussex（1967–2004，1975 正教授，约 40 年）→ Florida State University（2004–，Francis Eppes 讲席教授）
- 服务：Royal Society of Chemistry 主席（2002–2004）；Vega Science Trust（1995 共同创立，2012 关闭）；GEOset（2009）
- 命名遗产：Sheffield 北校区 Kroto Innovation Centre 与 Kroto Research Institute

## 10. 终审清单

- [x] 生卒 1939-10-07 / 2016-04-30，享年 76，出生地 Wisbech、去世地 Lewes（ALS 并发症）
- [x] 1996 三人共享（Curl/Smalley）表述准确；命名归属按 Kroto 页"Kroto 命名"口径
- [x] 博士导师"页面无载"已注明，仅写博士后导师 Herzberg
- [x] 本名 Krotoschiner 与 1955 年改姓表述准确
- [x] Copley 2002、Knight Bachelor 1996 New Year Honours 年份口径准确
- [x] 引语全部可在本地 Wikipedia 原文找到（三宗教、Madoff、Curl/Heath 讣闻评语）
- [x] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Harry_Kroto/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：CSICON 2011 照片已就位（images.txt 实载 URL），图注如实
- [ ] **国籍**：封面顶部明示英国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（三宗教、Madoff、Monty Python 评语）
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
