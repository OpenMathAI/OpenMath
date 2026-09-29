# Roderick MacKinnon（罗德里克·麦金农）立传提示词

> qid=Q211482 · 1956-02-19 生于美国马萨诸塞州 Burlington（在世，卒日留白） · 美国生物物理学家/神经科学家 · 21 世纪 · 诺贝尔化学奖（2003，与 Peter Agre 共享当年奖项，理由各不同）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Roderick_MacKinnon/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 表格语义化 tabularx + 金框公式展示框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。肖像：页面有 "MacKinnon in 2014" 照片但 images.txt 未提取到 URL——执行时先经 Wikipedia REST API `/page/summary/Roderick_MacKinnon` 查 infobox 原图名下载（500px）；404 则用装饰圆占位，并在 Review-1 记录。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{bolt}\enspace 离子通道的摄影者\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素（美国 | Rockefeller University | 钾通道三维结构与选择性机制）。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地、教育（Brandeis BA 1978 / Tufts MD 1982）、博士后导师、核心领域、现任（Rockefeller 分子神经生物学与生物物理实验室主任）、荣誉。事实取自本地 page.md infobox，不得杜撰；在世——卒栏写「在世（1956– ）」。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「离子选择性滤器」母题——离散圆点暗示钾离子列队穿越通道。
5. **表格语义化 + 公式框**（★ 高斯/Sanger 版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）——KcsA 钾通道 X 射线结构、K+ 过而 Na+ 不过的选择性悖论即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Roderick MacKinnon（中文惯称：罗德里克·麦金农）
- **生卒**：1956-02-19 生于马萨诸塞州 Burlington（在世，卒日页面无载——全篇卒处一律留白）
- **国籍**：United States（美国）
- **身份**：生物物理学家、神经科学家、教授（Rockefeller University 分子神经生物学与生物物理实验室主任）；页面亦以其创业身份称 businessman
- **家庭**：在 Brandeis 结识未来的妻子、有机化学家 Alice Lee（亦为工作同事）；infobox 载配偶 Jue Chen（科学家，2017 年结婚）——**页面未载 Alice Lee 与其婚姻变迁细节，勿写「离异」等推断**
- **教育轨迹**：
  - Burlington High School（infobox）；先入 University of Massachusetts Boston，一年后转学 Brandeis University
  - Brandeis University：生物化学 BA（1978），荣誉论文在 Christopher Miller 实验室完成（钙跨膜转运）
  - Tufts University School of Medicine：MD（1982），Boston Beth Israel Hospital 内科训练
- **师承**：Christopher Miller（Brandeis，本科荣誉论文 + 1986 博士后）
- **研究领域**：离子通道——钾通道的结构与选择性机制、X 射线晶体学、膜蛋白结构生物学、分子神经生物学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **马萨诸塞少年（1956）**：生于 Burlington；UMass Boston 一年后转学 Brandeis——转轨的开始。
2. **Miller 实验室（1970s）**：本科荣誉论文做钙跨膜转运——膜通道生涯的起点；同期结识未来的妻子 Alice Lee。
3. **从医与转向（1982–1986）**：Tufts MD 1982、Beth Israel 内科训练；自觉对行医「不满足」（页面转述）——1986 回 Brandeis Miller 实验室做博士后。
4. **哈佛建组（1989）**：助理教授；研究钾通道与蝎毒来源的特异性毒素——由此掌握蛋白纯化与 X 射线晶体学。
5. **Rockefeller（1996）**：教授兼分子神经生物学与生物物理实验室主任——向钾通道结构发起总攻。
6. **通道悖论**：钾通道放行 K+ 却拒绝更小的 Na+——此前几十年的分子架构只有间接推断。
7. **1998 突破**：与同事解析 *Streptomyces lividans*（KcsA）钾通道三维分子结构（X 射线晶体学）——克服了困扰整代人的膜蛋白结构屏障。
8. **选择性滤器**：结合结构与生化实验，精确解释钾通道选择性发生的机制。
9. **同步辐射双站**：获奖研究主要在 Cornell High Energy Synchrotron Source（CHESS）与 Brookhaven 国家实验室 NSLS 完成。
10. **奖项链（1997–2003）**：Newcomb Cleveland Prize（1997）→ W. Alden Spencer（1998）→ Lasker（1999）→ Rosenstiel（2000）→ Gairdner（2001）→ Horwitz（2003）。
11. **2003 诺贝尔化学奖**：与 Peter Agre 共享当年奖项——MacKinnon 因离子通道的结构与运作研究获承认（本人页面表述 "his work on the structure and operation of ion channels"；得奖时正从周末钓鱼返程，从同事处得知消息，页面明载）。
12. **Flex Pharma 创业**：与哈佛医学院神经生物学家 Bruce Bean 共同发明防治肌肉痉挛的膳食补充剂并临床试验，与 Christoph Westphal、Jennifer Cermak 共同创立公司——2015 年 IPO 8600 万美元、2016 推出 HotShot；2018-06 因耐受性问题停止候选药开发、7 月辞任董事。
13. **学术荣誉**：American Philosophical Society 院士（2005）；荷兰皇家艺术与科学院外籍院士（2007）；Bijvoet Medal（2004）；Perl-UNC Prize（2001）；Hodgkin-Huxley-Katz Prize Lecture（infobox 另载）。

## 3. 配色方案（高斯/Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深紫罗兰 deepviolet） | `#372A75` | 晶体衍射的深与锐（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（钾通道 badgeK） | `#2E5A9E` | 蓝 KcsA 结构 / 选择性滤器 |
| 分类色 2（晶体学 badgeXTAL） | `#1B7A43` | 绿 X 射线晶体学 / CHESS+NSLS |
| 分类色 3（神经科学 badgeNeuro） | `#D97B29` | 琥珀神经系统与心脏 / 蝎毒素 |
| 分类色 4（转化创业 badgeFlex） | `#C0395B` | 玫瑰 Flex Pharma / Bean 合作 |
| 背景 | `#F7F6F9` | 浅灰白（与高斯一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「K+ 离子列队穿越选择性滤器」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**The Flow of Time** — Alex-Productions（`music_audio/alex-productions/35-jqIDnltiDRI-The-Flow-of-Time.wav`，不要复制 wav 文件，Makefile 里直接引用该路径）
- **风格**：流转 / 大气 / 时间纵深
- **匹配理由**：
  - "时间纵深" 匹配通道本质——离子流过毫秒级的孔道，而结构的解析横跨 MD 转科研的二十年
  - "流转" 匹配离子电流——神经系统与心脏的节律，正是时间之流
  - 医生转科学家再兼创业者的多重身份，配乐带人生长河感
- **时长**：以实际 wav 为准，> 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 离子通道的摄影者 / Roderick MacKinnon 1956– + 四色 badge + 右上头像 + 国籍行（美国）
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士后/任职/领域/荣誉）
03  麦金农之路 — Sanger 式时间线（10 节点：1956→1978→1982→1986→1989→1996→1998→2001→2003→2015/2018）
04  Brandeis 起点：Miller 实验室 (1974–1982) — 表格「时间|事件|结果」
05  从 MD 到博士后 (1982–1989) — 表格「阶段|转折|结果」
06  哈佛与 Rockefeller (1989–1998) — 表格「阶段|方法|结果」+ 公式框：K+ 过 / Na+ 拒的选择性悖论
07  1998 结构突破 — 表格「问题|方法|结果」+ 公式框：KcsA 钾通道 X 射线结构
08  选择性滤器机制 — 表格「观察|解释|意义」
09  2003 诺贝尔化学奖 — 金框页（离子通道结构与运作；与 Agre 共享当年奖项、理由各不同标注）+ 奖项链表格（1997–2003）
10  荣誉与院士 — 高斯式「类别|代表|意义」表格（APS 2005 / 荷兰皇家外籍 2007 / Bijvoet 2004 / Perl-UNC 2001）
11  Flex Pharma — 高斯 FFT 页式流程图（与 Bean 共同发明 → 2015 IPO $86M → 2016 HotShot → 2018 停止与辞任）
12  转化的启示 — 表格「人物|角色|结果」（Bean / Westphal / Cermak）
13  科学之外的麦金农 — 表格（钓鱼得知诺奖消息的页面记载；Interview by Harry Kroto / Nobel Lecture 链接意象）+ 家庭信息页字段（Alice Lee / Jue Chen 2017）
14  结尾 — 「让电流有了形状，让孔道有了肖像。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2003 奖项口径 | 与 Peter Agre **共享当年奖项**（Agre 页载共享理由 "discoveries concerning channels in cell membranes"），但**两人理由不同**：MacKinnon=离子通道的结构与运作——co-honored 关系可建，note 注明「理由各不同」 |
| 官方 citation | **本人页面未载官方 citation 英文原句**——只可用页面表述 "his work on the structure and operation of ion channels"，或引 Agre 页的共享理由；勿编造 "for structural and mechanistic studies of ion channels" 之类 |
| 「第一个」禁写 | 页面仅说结构解析"克服了数十年来阻挠多数尝试的障碍"——**勿写「第一个解析的离子通道/膜蛋白结构」**（页面无此断言） |
| KcsA 来源 | *Streptomyces lividans*（放线菌）——勿写"来自人类" |
| 同步辐射 | 获奖研究在 **CHESS（Cornell）与 NSLS（Brookhaven）**——勿写 Rockfeller 本地完成 |
| 学位口径 | Brandeis BA 1978 + Tufts MD 1982——**无 PhD**（页面无载，勿杜撰博士） |
| 婚姻 | 页面仅载 Brandeis 结识 "future wife" Alice Lee（有机化学家、工作同事）；infobox 配偶 Jue Chen（2017–）——**勿写「离婚/前妻」推断**，两处各自按页面表述 |
| Flex Pharma 结局 | 2018-06 停止候选药开发（耐受性问题）+ 7 月辞任董事——写足结局，勿只写 IPO 光鲜面 |
| businessman | 页面称 "biophysicist, neuroscientist, and businessman"——创业内容客观带过，不渲染 |
| 引语红线 | 本地页面**无直接引语**——全篇不得出现带引号的「原话」，钓鱼轶事用转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q211482 | ✅ |
| name_zh | 罗德里克·麦金农 | ✅ |
| name_en | Roderick MacKinnon | ✅ |
| birth_date | 1956-02-19 | ✅ |
| death_date | （在世，留空） | ✅ |
| nationality | United States | ✅ |
| primary_occupation | biophysicist | ✅ |
| field_of_work | biochemistry（person_field 细分：ion channels / structural biology / X-ray crystallography / neuroscience，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后由主控置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 合作者 / 共同得主 / 配偶**（仅 page.md 正文或 infobox 明载者；metadata.json 无关系字段，无 metadata-only 禁入库项）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Christopher Miller | 师→生 | Brandeis 本科荣誉论文（钙转运）+ 1986 博士后导师 |
| colleague | Bruce Bean | 无向 | 哈佛医学院神经生物学家；共同发明防痉挛膳食补充剂并共同创立 Flex Pharma |
| colleague | Christoph Westphal | 无向 | Flex Pharma 共同创始人 |
| colleague | Jennifer Cermak | 无向 | Flex Pharma 共同创始人 |
| co-honored | Peter Agre | 无向 | 2003 诺贝尔化学奖共享当年奖项；理由各不同（MacKinnon 离子通道 / Agre 水通道） |
| spouse | Alice Lee | 无向 | Brandeis 结识的配偶、有机化学家、工作同事（页面表述 "future wife"） |
| spouse | Jue Chen | 无向 | 科学家，2017 年结婚（infobox） |

> **不建项说明**：页面正文无其他明载师承（无博士导师——MacKinnon 无 PhD）；Jue Chen 条目信息仅 infobox 一句，照录入但 note 从简。

## 8. 奖项清单

- Nobel Prize in Chemistry（2003，与 Agre 共享当年奖项；口径见 §5）
- Newcomb Cleveland Prize（1997）
- W. Alden Spencer Award（1998）
- Albert Lasker Award for Basic Medical Research（1999）
- Rosenstiel Award（2000）
- Canada Gairdner International Award（2001）
- Perl-UNC Prize（2001）
- Louisa Gross Horwitz Prize（2003）
- Bijvoet Medal（2004）
- Michael and Kate Bárány Award；Hodgkin-Huxley-Katz Prize Lecture（infobox 另载）
- American Philosophical Society 院士（2005）
- 荷兰皇家艺术与科学院外籍院士（2007）

## 9. 机构清单

- 教育：UMass Boston（一年）→ Brandeis University（BA 生物化学 1978；Christopher Miller 实验室荣誉论文）→ Tufts University School of Medicine（MD 1982；Beth Israel Hospital 内科训练）
- 任职：Brandeis Miller 实验室博士后（1986–）→ Harvard University 助理教授（1989–）→ The Rockefeller University（1996–，教授、Laboratory of Molecular Neurobiology and Biophysics 主任）
- 产业：Flex Pharma 共同创始人（与 Bean / Westphal / Cermak；2015 IPO；2018 停止药物开发、辞任董事）

## 10. 终审清单

- [ ] 生卒 1956-02-19 / 在世留白，出生地 Burlington, Massachusetts
- [ ] 2003 与 Agre 共享奖项、理由各不同；citation 口径（页面表述 + Agre 页共享理由）逐字准确，无编造官方原句
- [ ] 无「第一个解析通道结构」断言；KcsA = *Streptomyces lividans*；CHESS/NSLS 表述准确
- [ ] 无 PhD 口径准确；婚姻两处各按页面表述、无「离婚」推断
- [ ] Flex Pharma 含 2018 结局；引语零白名单（全篇转述）
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Roderick_MacKinnon/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：REST API 查 infobox 原图下载（500px）；404 则装饰圆占位并记录
- [ ] **国籍**：封面顶部明示美国
- [ ] **引语核对**：本篇应无引号原话（页面无直接引语）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 21 世纪批次各篇格式对齐
