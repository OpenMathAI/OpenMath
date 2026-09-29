# Robert Huber（罗伯特·胡贝尔）立传提示词

> qid=Q76623 · 1937-02-20 生于德国慕尼黑 · 在世 · 德国生物化学家 · 诺贝尔化学奖（1988，与 Johann Deisenhofer、Hartmut Michel 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Robert_Huber/`（page.md + metadata.json + page.html + images.txt）
> ⚠️ **本页 images.txt 为空**；infobox 载 "Robert Huber in 2010" 照片但文件名未导出——执行时从 page.html 查文件名经 Commons Special:FilePath 下载（250px 改 500px），404 则装饰圆占位。
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/`）。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）。优先从 page.html 查 infobox "Robert Huber in 2010" 图文件名经 Commons 下载；404 则**装饰圆占位**（主色实心圆 + 姓名缩写）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{dna}\enspace 欧洲最丰产的蛋白质晶体学实验室\enspace·\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：左侧头像 + 右侧 2×2 信息网格：生卒、本名、国籍、出生地、教育（Humanistisches Karls-Gymnasium / TU München）、博士（ForMemRS 证书口径）、核心领域、任职（马普生物化学研究所所长 1971–）、学生（Budisa / Colman）、荣誉。事实取自本地 Wikipedia infobox 与正文，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「蛋白质结构 / 电子密度」母题。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页 `tabularx` 三列表格（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Robert Huber（中文惯称：罗伯特·胡贝尔；ForMemRS）
- **生卒**：1937-02-20 生于慕尼黑（在世，death_date 留白）
- **国籍**：Germany（德国）
- **身份**：生物化学家、诺贝尔奖得主、蛋白质晶体学家
- **家庭**：父 Sebastian 为银行出纳员（bank cashier）；已婚、四子女（正文明载；妻子与子女名字页面无载——不入库）
- **教育轨迹**：
  - 1947–1956 就读慕尼黑 Humanistisches Karls-Gymnasium
  - 后入慕尼黑 Technische Hochschule（今 TU München）学化学，1960 获文凭（diploma）
  - 留校从事用晶体学解析有机化合物结构的研究
- **博士**：ForMemRS 选举证书口径——博士论文解决了困扰化学家的**重要昆虫激素（证书原文作 "edtyson"，即 ecdysone 蜕皮激素）的化学结构式**（见 §5 陷阱行；博士年份与论文题目 page.md 正文无载）
- **导师**：page.md 无载——身份信息页写「页面无载」，禁编造
- **研究领域**：生物化学、蛋白质晶体学、结构生物学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **慕尼黑银行家之子（1937）**：生于慕尼黑，父 Sebastian 为银行出纳——战后人文中学（humanistisches Gymnasium）九年奠基。
2. **TU München（至 1960）**：化学文凭毕业，留校转向晶体学——用 X 射线解析有机化合物结构的技术底座。
3. **昆虫激素结构（博士论文）**：ForMemRS 证书载其博士论文解决了让化学家久攻不下的重要昆虫激素化学结构式——结构生物学的开手棋。
4. **摇蚊幼体血红蛋白（早期成名作）**：证书载其证明摇蚊（Chironomus）幼体血红蛋白的多肽链三级折叠与 Kendrew 的抹香鲸肌红蛋白惊人相似——**首次表明该折叠在演化中被保留**。
5. **胰蛋白酶抑制剂与过渡态**：解析胰蛋白酶抑制剂结构，并证明其与胰蛋白酶的复合物**模拟了酶底物的四面体过渡态**；此后系统解析蛋白酶、酶原及其抑制剂，成为该领域世界权威。
6. **代表结构群**：前羧肽酶原（procarboxypeptidase，揭示酶激活机制）、凝血酶-水蛭素复合物（thrombin–hirudin，揭示水蛭毒素抑制凝血的分子机制）、柠檬酸合酶（citrate synthase，诱导契合构象变化范例）、免疫球蛋白片段（首个补体激活 F 片段结构，也是首个 Fab 可变域与恒定域结构）、含铜电子传递蛋白（抗坏血酸氧化酶等）与金属酶、钙结合蛋白 annexins。
7. **执掌马普（1971）**：出任 Max Planck Institute for Biochemistry（Martinsried）所长（director），团队发展蛋白质晶体学方法——证书称之为「欧洲最丰产的蛋白质晶体学实验室」。
8. **光合反应中心（1982–1985）**：与 Michel、Deisenhofer 合作——结晶紫色细菌（purple bacteria）光合膜内蛋白，三人用 X 射线晶体学解析其结构；证书并载同期还解析了蓝藻捕光蛋白藻青蛋白（phycocyanin）结构。
9. **第一次看见光合作用的结构本体**：结构首次揭示执行光合整体功能的结构实体——并可平移理解蓝藻及高等植物叶绿体中本质相同的光合作用。
10. **1988 诺贝尔化学奖**：与 Johann Deisenhofer、Hartmut Michel 三人共享——「首次结晶膜内光合重要蛋白并随后用 X 射线晶体学解析其结构」。
11. **约 400 篇论文**：证书结语 "Huber has published some 400 papers"——半个多世纪的持续产出。
12. **多所大学后期任职（2005/2006）**：2005 起在 Duisburg-Essen 大学医学-生物技术中心研究；2006 应邀在 Cardiff University 兼职（part-time）领衔结构生物学建设。
13. **百科全书编辑**：《Encyclopedia of Analytical Chemistry》创始编辑之一；Otto Warburg 奖章（1977）、Sir Hans Krebs 奖章（1992）、Pour le Mérite（1993）、皇家学会外籍院士（ForMemRS 1999）等荣誉集大成。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深青蓝 deepteal） | `#0E4D64` | 蛋白质晶体学的精确与冷静（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（蛋白酶与抑制剂 badgeProt） | `#2E5A9E` | 蓝胰蛋白酶抑制剂 / 免疫球蛋白 |
| 分类色 2（光合膜蛋白 badgePhoto） | `#1B7A43` | 绿光合反应中心 / 藻青蛋白 |
| 分类色 3（金属与电子传递 badgeMetal） | `#D97B29` | 琥珀含铜蛋白 / 锌配位 / annexins |
| 分类色 4（演化与折叠 badgeFold） | `#C0395B` | 玫瑰摇蚊血红蛋白 / 演化保守折叠 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落）——电子密度云与蛋白团簇意象。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**The Invisible Light** — Infraction（清单预分配，勿复制 wav 文件，Makefile 引用源路径）
- **文件**：`music_audio/inspiring-electronic/19-tGxXsgSKPiQ-Documentary Cinematic by Infraction [No Copyright Music] ⧸ The Invisible Light.wav`
- **风格**：纪录片 / 电影感 / 内敛推进
- **匹配理由**：
  - "The Invisible Light"（不可见之光）正是 X 射线晶体学的诗意别名——用不可见的射线看见不可见的结构
  - 纪录片质感匹配其「约 400 篇论文」的长期主义学术生涯
  - 内敛推进的段落结构呼应从有机晶体学到膜蛋白结构的一甲子纵深
- **时长**：以实际文件为准 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 欧洲最丰产的蛋白质晶体学实验室 / Robert Huber 1937– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士论文口径/领域/任职/学生/家庭口径/荣誉）
03  胡贝尔的一生 — 高斯式时间线（10 节点：1937→1956→1960→1971→1977→1982→1985→1988→1999→2006）
04  慕尼黑与 TU München (1937–1960) — 表格「时间|事件|结果」
05  博士论文：昆虫激素与摇蚊血红蛋白 — 表格「问题|方法|结果」+ 公式框：演化保守的三级折叠（Chironomus Hb ≈ Kendrew 肌红蛋白）
06  执掌马普 (1971) — 表格「机构|方法|地位」（Martinsried 蛋白质晶体学方法学）
07  蛋白酶世界权威 — 表格「对象|结构|揭示」（胰蛋白酶抑制剂/前羧肽酶原/凝血酶-水蛭素/柠檬酸合酶）
08  免疫与金属蛋白 — 表格「对象|结构|意义」（免疫球蛋白片段/含铜电子传递蛋白/annexins）
09  光合反应中心 (1982–1985) — 表格「问题|方法|结果」+ 公式框：紫色细菌光合膜蛋白复合体
10  1988 诺贝尔化学奖 — 表格「得主|贡献|机构」（三人共享）+ 获奖口径
11  ForMemRS 证书精读 — 高斯式「段落|贡献|意义」表格（证书逐段语义化）
12  后期版图 (2005–2006) — 高斯 FFT 页式流程图（Duisburg-Essen / Cardiff）
13  遗产：欧洲结构生物学重镇 — 四分类遗产盒 + "some 400 papers"
14  结尾 — 「从激素到光合膜，一甲子把生命催化成看得见的结构。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1988 诺奖口径 | 三人共享（Deisenhofer、Michel、Huber）；贡献口径「首次结晶紫色细菌膜内光合重要蛋白 + X 射线解析其结构」；官方精确 citation 本地页面无载，禁杜撰全句 |
| ForMemRS 证书拼写 | 证书原文作 "edtyson"（昆虫激素）——正文写「证书原文如此，即 ecdysone 蜕皮激素」并加注；勿直接改写不加注，也勿照抄不解释 |
| 蓝绿藻学名 | 证书原文 "blue-green alga Mastiglocadus laminosus"——正文用「蓝藻（蓝绿藻）」并保留证书原文学名；与现代拼写差异照原文加注 |
| 博士年份/题目 | page.md 正文无博士年份与论文题目——身份页博士栏只写证书口径的结构式成果，禁编造年份 |
| 博士导师 | page.md 全篇无载——禁写；与 Deisenhofer 的关系是**反向**（Huber 是导师） |
| Rhodopseudomonas viridis | 证书载反应中心菌种名 "Rhodopseudomonas viridis"——保留学名，勿与他种混写 |
| 藻青蛋白归属 | 证书把 phycocyanin 结构计入 1988 共享成果叙述——引用按证书口径；勿写成 Huber 个人独立成果 |
| 学生关系 | infobox 明载 Doctoral students: **Nediljko Budisa**；Other notable students: **Peter Colman（postdoc）**——Colman 是博士后，note 写明；其余学生名单（Wikidata）无载不入库 |
| 家庭 | 「已婚、四子女」可写（正文明载）；妻子姓名与子女信息无载——禁编造、不入库 |
| 机构名 | "Technische Hochschule"（1960 文凭）即今 Technical University of Munich——首次出现加注「今慕尼黑工大」 |
| 三机构并行 | 1971 马普所长、2005 Duisburg-Essen、2006 Cardiff——三段时间线勿倒置；Cardiff 是 part-time |
| 中文引语 | 可整句引用仅 ForMemRS 选举证书两处（"the most productive protein crystallography laboratory in Europe" 与 "Huber has published some 400 papers"）；其余间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q76623 | ✅ |
| name_zh | 罗伯特·胡贝尔 | ✅ |
| name_en | Robert Huber | ✅ |
| birth_date | 1937-02-20 | ✅ |
| death_date | （在世，留白） | ✅ |
| nationality | Germany | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry（person_field 细分见下表） | ✅ |
| has_biography | 0（待 Beamer 后置 1） | ✅ |

person_field 细分 rank 表：

| name_en | rank | name_zh |
|---|---|---|
| biochemistry | 0 | 生物化学 |
| crystallography | 1 | 晶体学 |
| protein crystallography | 2 | 蛋白质晶体学 |

## 7. 社会关系入库清单

**学生 / 共同得主**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Johann Deisenhofer | Huber→学生 | 博士生（1974，Martinsried）；1988 共享诺奖 |
| advisor-student | Nediljko Budisa | Huber→学生 | infobox Doctoral students |
| advisor-student | Peter Colman | Huber→学生 | infobox Other notable students（postdoc）——note 注明博士后 |
| co-honored | Johann Deisenhofer | 无向 | 1988 诺贝尔化学奖共同得主（与 advisor 关系并行两条） |
| co-honored | Hartmut Michel | 无向 | 1988 诺贝尔化学奖共同得主 |

> metadata.json-only 一律不入库。本页禁入库名单：Kendrew（证书提及其肌红蛋白为对照物，非直接关系）。博士导师 page.md 无载，无关系可入；家庭（妻/子女）不入库。

## 8. 奖项清单

- Otto Warburg Medal（1977）
- Nobel Prize in Chemistry（1988，与 Deisenhofer、Michel 共享）
- Sir Hans Krebs Medal（1992）
- Pour le Mérite for Sciences and Arts（1993）
- Foreign Member of the Royal Society，ForMemRS（1999；选举证书为重要文献）
- Emil-von-Behring-Prize；Richard Kuhn Medal；Bavarian Maximilian Order for Science and Art（metadata 载，年份以官方页面为准）
- Great Cross with Star and Sash of the Order of Merit of the Federal Republic of Germany（联邦德国大十字绶带功绩勋章，metadata 载）
- 荣誉博士：巴塞罗那自治大学、清华大学、克拉科夫雅盖隆大学、巴塞罗那大学、里斯本 NOVA 大学、鲁汶天主教大学（metadata 载）
- EMBO 会员（metadata 载）

## 9. 机构清单

- 教育：Humanistisches Karls-Gymnasium（1947–1956）→ Technische Hochschule München（今 TU München，1960 文凭）
- 任职：TU München（1960 起，晶体学研究）；Max Planck Institute for Biochemistry, Martinsried 所长（1971–）；University of Duisburg-Essen 医学-生物技术中心（2005–）；Cardiff University 结构生物学领衔（2006–，兼职）
- 编辑：《Encyclopedia of Analytical Chemistry》创始编辑之一

## 10. 终审清单

- [ ] 生卒 1937-02-20（慕尼黑）/ 在世留白
- [ ] 1988 三人共享（Deisenhofer、Michel）表述准确；获奖理由不杜撰全句
- [ ] ForMemRS 证书 "edtyson" 处理方式正确（原文照录 + ecdysone 加注）
- [ ] 博士年份/题目/导师均按无载留白处理
- [ ] Budisa（博士生）/ Colman（博士后）入库区分清楚
- [ ] 1971 马普 / 2005 Duisburg-Essen / 2006 Cardiff 时间线准确
- [ ] 证书引语仅两处白名单，其余间接转述
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Robert_Huber/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：infobox "in 2010" 图经 page.html 查名下载；404 则装饰圆占位
- [ ] 国籍：封面顶部明示德国
- [ ] 引语核对：仅 ForMemRS 证书两处整句 + 其余间接转述
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐

---

> **名单状态**：`chemist/prompt_manifest.json` chem-batch-20 · Robert Huber（1988，BGM The Invisible Light，主色 #0E4D64）。
> **开始执行。每完成一步向主控汇报。**
