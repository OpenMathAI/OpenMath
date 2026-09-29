# Tomas Lindahl（托马斯·林达尔）立传提示词

> qid=Q1886068 · 1938-01-28 生于瑞典斯德哥尔摩 · 在世 · 瑞典/英国双国籍 · 诺贝尔化学奖（2015，与 Modrich/Sancar 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Tomas_Lindahl/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：参考 `chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.md` §0-§11 结构标杆（高斯式：身份信息页 + 时间线 + 表格语义化 + 公式框）。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像取 `pages/Tomas_Lindahl/images.txt`；下载失败用装饰圆占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{dna}\enspace DNA 脆性的守望者\enspace·\enspace 瑞典 / 英国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名 Tomas Robert Lindahl、国籍（Swedish, naturalised British 双重国籍）、出生地、教育（Karolinska）、领域、任职、荣誉。事实取自本地 page.md infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「DNA 修复」母题——断口被小圆点逐个缝合的视觉隐喻。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（损伤 | 机制 | 意义）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化（碱基切除修复 BER 流程、DNA 双螺旋稳定性等）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Tomas Robert Lindahl（中文惯称：托马斯·林达尔；头衔缩写 FRS FMedSci）
- **生卒**：1938-01-28 生于斯德哥尔摩 Kungsholmen 岛 · 在世
- **国籍**：瑞典（Swedish），后入籍英国（naturalised British，双重国籍——infobox 明载）
- **身份**：瑞典-英国双重背景的科学家，专攻癌症研究（cancer research）；弗朗西斯·克里克研究所荣休科学家
- **家庭**：父 Folke Robert Lindahl、母 Ethel Hulda Hultberg（page.md 未载配偶子女——留白，勿编造）
- **教育轨迹**：
  - Karolinska Institutet（卡罗林斯卡学院，斯德哥尔摩）：1967 PhD（论文 *On the structure and stability of nucleic acids in solution*）；1970 取得 MD 学位资格
- **博士后**：普林斯顿大学、洛克菲勒大学（page.md 未点名博士后导师——留白）
- **研究领域**：DNA 修复、癌症研究——碱基切除修复、DNA 糖基化酶、DNA 连接酶、甲基转移酶

## 2. 核心叙事亮点（约 13 条）

1. **斯德哥尔摩少年（1938）**：生于 Kungsholmen 岛——从 Karolinska 起步的医学生命科学之路。
2. **核酸溶液结构博士（1967）**：Karolinska 博士论文研究溶液中核酸的结构与稳定性——「DNA 并不永恒稳定」的问题意识由此发端。
3. **MD 学位（1970）**：同校取得医学学位资格——研究始终带着医学视野。
4. **新大陆博士后**：普林斯顿大学与洛克菲勒大学博士后训练。
5. **哥德堡教授（1978–1982）**：任哥德堡大学医化学教授。
6. **移居英国（1981）**：加入帝国癌症研究基金（ICRF，今 Cancer Research UK）任研究员。
7. **Clare Hall 首任所长（1986–2005）**：创建并执掌 ICRF Clare Hall 实验室（赫特福德郡）近二十年——2015 年起并入弗朗西斯·克里克研究所；本人研究至 2009。
8. **哺乳动物 DNA 连接酶第一次**：FRS 当选证书记载——**第一个分离出哺乳动物 DNA 连接酶**。
9. **DNA 糖基化酶的发现**：FRS 证书——描述了一类「完全出乎意料的新酶群」：DNA 糖基化酶，作为碱基切除修复（BER）的介导者。
10. **甲基转移酶与 ada 基因**：发现哺乳细胞中独特的一类甲基转移酶，介导 DNA 烷基化的适应反应，并证明其表达受 ada 基因调控。
11. **Bloom 综合征与 EBV**：阐明 Bloom 综合征的分子缺陷是 DNA 连接酶 I 缺失；首次描述淋巴样细胞中闭环双链病毒 DNA（EBV 转化机制）。
12. **2015 诺贝尔化学奖**：与美国化学家 Paul L. Modrich、土耳其化学家 Aziz Sancar 共享，官方理由 "for mechanistic studies of DNA repair"（DNA 修复的机制研究）。
13. **英国科学最高褒奖**：皇家学会 Royal Medal（2007，引文盛赞其原创性、广度与持久影响）与 Copley Medal（2010）；2018 当选美国科学院外籍院士；2015-12-08 发表诺贝尔演讲 *The Intrinsic Fragility of DNA*。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（藏蓝 navyblue） | `#2A3468` | 核酸双螺旋的深蓝（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（碱基切除修复 badgeBer） | `#1B7A43` | 绿 DNA 糖基化酶 / BER |
| 分类色 2（连接酶与 ligase badgeLig） | `#2E5A9E` | 蓝 DNA 连接酶 I / Bloom 综合征 |
| 分类色 3（烷基化适应 badgeAda） | `#D97B29` | 琥珀甲基转移酶 / ada 基因 |
| 分类色 4（癌症研究 badgeCancer） | `#C0395B` | 玫瑰 Clare Hall / 化疗药物设计 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「修复断口被逐点缝合」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Daylight** — Alex-Productions（`music_audio/alex-productions/44-JoyIRE5k2Yo-Daylight.wav`，勿复制 wav，Makefile 直接引用路径）
- **风格**：明亮 / 治愈 / 渐进上扬
- **匹配理由**：
  - "Daylight" 匹配「DNA 天生脆性、但细胞自带修复之光」的叙事核心——修复即天亮
  - 渐进上扬匹配其学术轨迹——Karolinska → 哥德堡 → Clare Hall 建制化 → 77 岁诺奖
  - 治愈感匹配癌症研究的人文底色（更选择性化疗药物的愿景）
- **时长**：以实际文件为准，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，00–14）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — DNA 脆性的守望者 / Tomas Lindahl 1938– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/出生地/教育/领域/任职/荣誉）
03  林达尔的一生 — 高斯式时间线（10 节点：1938→1967→1970→1978→1981→1986→2007→2010→2015→2018）
04  早年与 Karolinska (1938–1970) — 表格「时间|事件|结果」
05  博士后与哥德堡 (1970s–1982) — 表格「阶段|方向|结果」
06  移居英国与 Clare Hall (1981–2005) — 表格「机构|角色|结果」（ICRF→CRUK→Crick Institute 演化线）
07  DNA 的内在脆性 — 表格「旧观念|发现|意义」+ 公式框：DNA 自发损伤与修复恒态
08  碱基切除修复：糖基化酶 — 表格「损伤|酶|结果」+ 公式框：BER 流程示意
09  连接酶、甲基转移酶与 ada — 表格「对象|发现|结果」（哺乳 DNA 连接酶第一人 / Bloom 综合征 / ada 调控）
10  2015 诺贝尔化学奖 — 三人共享页（Lindahl / Modrich / Sancar）+ citation 原句公式框
11  三条修复路线分工 — 表格「人物|路线|结果」（Lindahl=碱基切除修复；Modrich=错配修复；Sancar=光复活与核苷酸切除修复——分工勿混）
12  荣誉全景 — 高斯式「类别|代表|意义」表格（FRS 1988 / Royal Medal 2007 / Copley 2010 / NAS 2018）
13  遗产：克里克研究所与化疗未来 — 四分类遗产盒（Crick Institute 并入 / 更选择性化疗药物愿景 / 诺奖演讲）
14  结尾 — 「生命把 DNA 写了四十亿年，也修了四十亿年。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2015 获奖理由 | 官方原句 "for mechanistic studies of DNA repair"；三人**共享**（Lindahl / Modrich / Sancar），勿写独享 |
| 三人分工 | **Lindahl = 碱基切除修复（BER）/ DNA 糖基化酶**；**Modrich = 错配修复**；**Sancar = 光复活与核苷酸切除修复**——三条路线勿混，方向勿张冠李戴 |
| 国籍口径 | Swedish, naturalised British（**双重国籍**）——勿写「放弃瑞典籍」；页面 description 作 Swedish biologist，正文作 Swedish-British scientist |
| 共同得主定性 | page.md 口径：American chemist Paul L. Modrich、Turkish chemist Aziz Sancar——国别限定词勿写错 |
| 获奖年龄 | 2015 获奖时 77 岁（1938 年生）——如写须现场核算，勿写错 |
| 博士导师 | **page.md 未载博士导师姓名**——留白，勿编造；博士后机构（Princeton/Rockefeller）亦未点名导师 |
| FRS 证书引文 | 是瑞典皇家学会……注意：是**英国**皇家学会（Royal Society）当选证书；引文可引用但须注明出处为 FRS certificate of election |
| Bloom 综合征拼写 | page.md 原文作 "Blooms syndrome [sic]"——行文写 Bloom 综合征即可，勿照抄 sic |
|机构演化线 | ICRF（1981 加入）→ 今 Cancer Research UK；Clare Hall Laboratories 2015 年起并入 Francis Crick Institute——演化方向勿倒置 |
| 退休口径 | Clare Hall 所长至 2005，**研究持续至 2009**；现为 Crick 荣休科学家——勿写「2005 全面退休」 |
| 引语红线 | 直接引语仅限：皇家奖章引文（"making fundamental contributions..."）与瑞典科学院宣布句（page.md 已载）——此外全部间接转述 |
| 中文译名 | 托马斯·林达尔；Sancar 中文惯称「阿齐兹·桑贾尔」（本篇行文可提及） |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q1886068 | ✅ |
| name_zh | 托马斯·林达尔 | ✅ |
| name_en | Tomas Lindahl | ✅ |
| birth_date | 1938-01-28 | ✅ |
| death_date | null（在世） | ✅ |
| nationality | Sweden / United Kingdom（rank 0/1，era_note：后入籍英国双重国籍） | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | chemistry, DNA repair（person_field 细分见下表） | ✅ |
| has_biography | false（Beamer 立传后置 1） | ✅ |

**person_field 细分 rank 表**：

| rank | field_en | field_zh |
|---|---|---|
| 0 | DNA repair | DNA 修复 |
| 1 | base excision repair | 碱基切除修复 |
| 2 | cancer research | 癌症研究 |
| 3 | medical chemistry | 医化学 |

## 7. 社会关系入库清单

**共同得主**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Paul L. Modrich | 无向 | 2015 诺贝尔化学奖共同得主（美国化学家，错配修复） |
| co-honored | Aziz Sancar | 无向 | 2015 诺贝尔化学奖共同得主（土耳其化学家，光复活与核苷酸切除修复） |

> **禁入库名单**（page.md 未载个人关系）：博士导师与博士后导师（页面无载姓名）、Folke Robert Lindahl / Ethel Hulda Hultberg（父母，家庭背景）、Epstein-Barr 病毒（研究对象非人）、皇家学会/各机构人士（仅制度性荣誉）。Lindahl relations=2 为**诚实值**——页面仅明载两位共同得主。

## 8. 奖项清单

- Nobel Prize in Chemistry（2015，与 Modrich/Sancar 共享；诺奖演讲 2015-12-08 *The Intrinsic Fragility of DNA*）
- EMBO Member（1974）
- Fellow of the Royal Society, FRS（1988）
- Founding Fellow of the Academy of Medical Sciences, FMedSci（1998）
- Royal Medal, Royal Society（2007）
- Copley Medal, Royal Society（2010）
- Prix International de l'INSERM（metadata 有载）
- Croonian Medal and Lecture（metadata 有载）
- H. M. The King's Medal（metadata 有载）
- Member, Norwegian Academy of Science and Letters
- Foreign Associate, US National Academy of Sciences（2018）
- Honorary doctor, University of Gothenburg（metadata 有载）
- Fellow of the AACR Academy（metadata 有载）

## 9. 机构清单

- 教育：Karolinska Institutet（PhD 1967；MD 1970）
- 任职：Princeton University / Rockefeller University 博士后 → University of Gothenburg 医化学教授（1978–1982）→ Imperial Cancer Research Fund（1981 加入，今 Cancer Research UK）→ Clare Hall Laboratories 首任所长（1986–2005，Hertfordshire）→ Francis Crick Institute（2015 并入；荣休科学家；研究至 2009）

## 10. 终审清单

- [x] 生卒 1938-01-28 / 在世；出生地斯德哥尔摩 Kungsholmen
- [x] 2015 三人共享表述准确；citation 英文原句完整
- [x] 三条修复路线分工（BER / MMR / NER+光复活）表述准确
- [x] 国籍双值（瑞典 + 入籍英国双重国籍）表述准确
- [x] 博士导师留白不编造；FRS 证书引文有出处
- [x] 引语仅限 page.md 已载两处（Royal Medal 引文 / 瑞典科学院宣布句）
- [x] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 读取 `pages/Tomas_Lindahl/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：按 images.txt 下载，404 则装饰圆占位
- [ ] 国籍：封面明示「瑞典 / 英国」
- [ ] 引语核对：仅两处已载引语，其余间接转述
- [ ] 编译验证：`make distclean && make`
- [ ] Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger/高斯模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 2015 三人共享另两篇（Modrich / Sancar，batch-08）口径交叉对齐
