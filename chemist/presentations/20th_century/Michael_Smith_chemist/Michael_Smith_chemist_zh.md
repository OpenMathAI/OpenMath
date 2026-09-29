# Michael Smith（迈克尔·史密斯）立传提示词

> qid=Q232289 · 1932-04-26 – 2000-10-04 · 英裔加拿大生物化学家 · 20 世纪 · 诺贝尔化学奖（1993，与 Kary Mullis 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Michael_Smith_chemist/`（page.md + metadata.json + page.html + images.txt；本页为化学家 Michael Smith **消歧义目录**，与材料科学家等其他同名者严格区分）
> 版式基准：**参考 Frederick Sanger（Q151564）立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景，是本次撰写的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像从 `pages/Michael_Smith_chemist/images.txt` 下载至 `images/`；本页 images.txt 资源为 1994 年聚会照等非标准肖像，若不适用则用装饰圆占位并在 Review-1 注明）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{scissors}\enspace 剪开基因的人\enspace·\enspace 加拿大`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍（英格兰出生→1963 入籍加拿大）、出生地/去世地、教育、博士后导师、核心领域、机构、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆），呼应「定点突变」母题——一片均匀圆点中被精准改色的一颗，暗示在基因组任意位点引入确定变异。
5. **表格语义化 + 公式框**（★ Sanger 版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 " "。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Michael Smith（中文惯称：迈克尔·史密斯；CC OBC FRS）
- **生卒**：1932-04-26 生于英格兰兰开夏 Blackpool → 2000-10-04 逝于加拿大不列颠哥伦比亚 Vancouver，享年 68
- **国籍**：British-Canadian——生于英格兰，1956 年移民加拿大，1963 年入籍
- **身份**：生物化学家兼实业家（biochemist and businessman）；定点突变（site-directed mutagenesis）共同发明人
- **家庭**：1960-08-06 于温哥华岛娶 Helen Wood Christie，育三子女 Tom、Ian、Wendy（及三名孙辈），1983 年分居；晚年与伴侣 Elizabeth Raines 在 Vancouver 生活直至去世
- **教育轨迹**：
  - St. Nicholas Church of England School（国立小学；通过 eleven plus 考试获奖学金）
  - Arnold School for Boys（奖学金）
  - University of Manchester（奖学金），化学 BSc → PhD（1956，diols 立体化学）
- **导师**：页面未载博士导师（Manchester PhD 导师无载，禁写）；博士后导师 Har Gobind Khorana（1956 起，不列颠哥伦比亚研究理事会）
- **博士**：1956，《Studies in the stereochemistry of diols and their derivatives》
- **研究领域**：核酸化学、寡核苷酸合成、定点突变、分子生物学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **Blackpool 的奖学金少年（1932–1950s）**：国立小学出身，靠 eleven plus 与两笔奖学金一路读到 Manchester 化学系——彼时英国国立学校孩子极少走学术路。
2. **Manchester 博士（–1956）**：diols 立体化学；1956 年毕业即移民加拿大。
3. **Khorana 门下（1956–1960）**：不列颠哥伦比亚研究理事会博士后，随 Khorana 发展核苷酸合成新技术——彼时 DNA 刚被确认为遗传物质。
4. **随师迁威斯康星（1960）**：Khorana 受聘 University of Wisconsin–Madison 酶研究所，Smith 随行数月。
5. **回归温哥华（1960s）**：任加拿大渔业研究委员会（FRB）温哥华站高级科学家、化学部主任——研究鲑鱼洄游与嗅觉线索，但主线始终是核酸合成（获美国公共卫生署研究基金）；同时在 UBC 生物化学系兼副教授、动物系荣誉教授。
6. **进入 UBC（1966）**：受聘加拿大医学研究理事会研究助理，在 UBC 生物化学系工作。
7. **Sanger 实验室学术休假（1975–1976）**：赴英国 MRC 分子生物学实验室 Fred Sanger 组——置于基因组织与基因组测序研究最前沿，归时已是世界领先的分子生物学家。
8. **定点突变诞生（1977–1978）**：1977 年团队证实其理论；1978 年与前 Sanger 组学术休假同事 Clyde A. Hutchison III 提出 "oligonucleotide-directed site-directed mutagenesis"，论文 "Mutagenesis at a Specific Position in a DNA Sequence" 发表于 JBC——解决了「高效判定单突变基因效应」的问题。
9. **技术的谱系**：定点突变成为 PCR 与合成生物学的先导技术（页面原表述：progenitor technique for PCR, Site-Directed Mutagenesis and Synthetic Biology）——从囊性纤维化基因治疗到工业酶改造的广泛应用（页面列举块）。
10. **科学管理者（1981–1999）**：1981 创办 ZymoGenetics（Seattle，与华盛顿大学 Earl W. Davie、Benjamin D. Hall 合作；后被 Bristol-Myers Squibb 收购）；1986任UBC医学院分子遗传中心主任；1987 创办 UBC 生物技术实验室并任主任（1987–1995）；PENCE（蛋白质工程卓越中心网络）创始科学领导人；1999 年促成 BC 癌症研究基金会资助的基因组测序中心（今 Michael Smith Genome Sciences Centre）。
11. **1993 诺贝尔化学奖**：因发展寡核苷酸定点突变与 Kary Mullis（PCR 发明人）共享。
12. **慷慨**：将诺奖奖金一半捐给精神分裂症遗传学研究，另一半捐给 BC Science World 与加拿大女性科技工作者协会；1999 年 Royal Bank Award 的配套奖金捐给 BC 癌症基金会。
13. **身后**：2001 Michael Smith Foundation for Health Research 创立；2004 UBC 生物技术实验室更名 Michael Smith Laboratories、加拿大 Michael Smith Genome Sciences Centre 与曼彻斯特大学 Michael Smith Building 以其命名；2004 传记《No Ordinary Mike》出版。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深靛蓝 deepindigo） | `#2A3468` | 核酸化学的严谨深靛（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（定点突变 badgeSDM） | `#4A5FA8` | 蓝寡核苷酸引物 / 精准变异 |
| 分类色 2（Khorana 学脉 badgeKhorana） | `#1B7A43` | 绿核苷酸合成学脉 |
| 分类色 3（管理者与创业 badgeOrg） | `#D97B29` | 琥珀 UBC / ZymoGenetics / PENCE |
| 分类色 4（遗产 badgeLegacy） | `#C0395B` | 玫瑰捐赠 / 以其命名的研究机构 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「定点突变」——众点之中精准改写一点。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**PAST** — Alex-Productions（清单指定 `music_audio/alex-productions/89-geyy8_WXDK0-PAST.wav`，不要复制 wav 文件，由 Makefile 侧引用）
- **风格**：怀旧 / 沉静 / 回望
- **匹配理由**：
  - "PAST" 匹配叙事的时间纵深——从 Blackpool 国立小学到 Manchester、Khorana、Sanger，一路是回望来路的学脉故事
  - "沉静" 匹配其气质——慷慨、低调、把奖金几乎全数捐出的实干者
  - "怀旧" 匹配结尾页——2000 年离世后四座机构以其命名，过去与未来在命名处相遇
- **时长**：以文件实际时长为准（> 15 页 × 7 秒 ≈ 105 秒即可），ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 剪开基因的人 / Michael Smith 1932–2000 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/国籍变迁/教育/博士后导师/出生地/去世地/领域/机构/荣誉）
03  史密斯的一生 — 时间线（10 节点：1932→1956→1960→1966→1975→1978→1987→1993→1999→2000）
04  Blackpool 到 Manchester (1932–1956) — 表格「时间|事件|结果」
05  Khorana 门下 (1956–1965) — 表格「阶段|地点|工作」+ 公式框：核苷酸→寡核苷酸→基因
06  渔业站与 UBC (1960–1975) — 表格「岗位|研究|结果」（鲑鱼与核酸并行）
07  Sanger 实验室学术休假 (1975–1976) — 表格「背景|内容|结果」
08  定点突变 (1977–1978) — 表格「问题|方法|结果」+ 公式框：寡核苷酸引物引入单点突变（JBC 1978）
09  技术的谱系与应用 — 表格「领域|应用|意义」（基因治疗/受体/工业酶；PCR 与合成生物学的先导）
10  1993 诺贝尔化学奖 — 表格「人物|贡献|结果」（与 Kary Mullis 共享；引语=FRS 证书段）
11  科学管理者 — 表格「机构|角色|时间」（ZymoGenetics 1981 / 分子遗传中心 1982·1986 / 生物技术实验室 1987 / PENCE / 基因组测序中心 1999）
12  慷慨 — 表格「奖金流向|受益方|意义」（精神分裂症遗传学 / Science World / SCWIST / BC 癌症基金会）
13  身后与遗产 — 表格「年份|命名|主体」（2001 基金会 / 2004 三处更名 / 2005 Smith-Yuen）
14  结尾 — 「在基因组的任意一处，写下你想要的那个字母。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 同名区分 | 本页是**化学家** Michael Smith（Blackpool 出生的英裔加拿大人）——勿与材料科学家等其他同名者混淆；论文/机构全加 chemistry 语境限定 |
| 获奖口径 | 1993 与 Kary Mullis **共享**；Smith 的贡献是**定点突变**，Mullis 是 **PCR**——两人工作不同，勿混；本地页面无诺奖官方 citation 原句，勿杜撰 |
| 学历年份 | Manchester BSc → PhD **1956**（diols 立体化学）——勿写其他年份 |
| 博士导师 | **页面无载**，禁写；只写博士后导师 Har Gobind Khorana（1956 起） |
| 国籍 | 生于英格兰 → 1956 移加 → **1963 入籍**；「British-Canadian」口径；勿只写 Canada 或只写英国 |
| Sanger 关系 | 1975–1976 学术休假于 Sanger 实验室 + 1978 合作者 Hutchison 来自「前 Sanger 组」——是**同事/合作**关系，勿写成师承 |
| 定点突变年份 | 1977 团队证实理论；**1978** 论文发表（JBC）——勿写 1975 或 1980 |
| ZymoGenetics | 1981 创办（Seattle）；与 **Earl W. Davie、Benjamin D. Hall**（University of Washington）合作；后被 Bristol-Myers Squibb 收购——三创始人口径 |
| 奖金去向 | 一半→精神分裂症遗传学研究；另一半→BC Science World + 加拿大女性科技工作者协会；1999 Royal Bank Award 配套→BC 癌症基金会——勿笼统写「捐给科研」 |
| 机构时间线 | Peter Wall 杰出教授为 **1996**（奖项清单又见 1994 年 UBC Peter Wall 称号条目，按页面两处口径择一并在 §8 注明出处）；基因组测序中心 1999 年成立、2004 年更名 Michael Smith Genome Sciences Centre——勿倒置 |
| 引语红线 | 可引用（页面原文）：FRS 当选证书段；中文引号内不得出现无法在 page.md 溯源的「原话」；「第一次/唯一」类断言页面未载禁写 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q232289 | ✅ |
| name_zh | 迈克尔·史密斯 | ✅ |
| name_en | Michael Smith | ✅（页面规范名；目录 Michael_Smith_chemist 消歧义） |
| birth_date | 1932-04-26 | ✅ |
| death_date | 2000-10-04 | ✅ |
| nationality | Canada（rank 0）/ United Kingdom（rank 1，出生） | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry（person_field 细分：site-directed mutagenesis / oligonucleotide synthesis / molecular biology / nucleic acid chemistry，带 rank） | ✅ |
| has_biography | false（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 同事 / 共同得主**（★ 只收 page.md 正文或 infobox 明载的关系）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Har Gobind Khorana | 师→生（博士后导师） | 1956 起于不列颠哥伦比亚研究理事会；1960 随其迁 Wisconsin |
| colleague | Frederick Sanger | 无向 | 1975–1976 于 MRC LMB Sanger 组学术休假；Hutchison 系前 Sanger 组同事 |
| colleague | Clyde A. Hutchison III | 无向 | 1978 定点突变论文共同作者（JBC） |
| colleague | Earl W. Davie | 无向 | 1981 共同创办 ZymoGenetics（University of Washington） |
| colleague | Benjamin D. Hall | 无向 | 1981 共同创办 ZymoGenetics（University of Washington） |
| co-honored | Kary Mullis | 无向 | 1993 诺贝尔化学奖共同得主（PCR） |
| spouse | Helen Wood Christie | 无向 | 1960-08-06 结婚，1983 分居；三子女 Tom、Ian、Wendy |

> metadata.json-only 的关系（页面正文未载的荣誉学位授予方等）**不予入库**。

## 8. 奖项清单

- Nobel Prize for Chemistry（1993，与 Kary B. Mullis 共享）
- UBC Jacob Biely Faculty Research Prize（1977）；Canadian Biochemical Society Boehringer Mannheim Prize（1981）
- Fellow of the Royal Society of Canada（1981）；Science Council of British Columbia Gold Medal（1984）
- Fellow of the Royal Society, FRS（1986）；Gairdner Foundation International Award for Chemistry（1986）；UBC Killam Research Prize（1986）
- Genetics Society of Canada Award of Excellence（1988）；G. Malcolm Brown Award（1989）
- Flavelle Medal, Royal Society of Canada（1992）
- Manning Innovation Awards Principal Award（1994）；Order of British Columbia（1994）；Golden Plate Award（1994）
- Companion of the Order of Canada（1995）；BC Biotechnology Award for Innovation and Achievement（1999）；Royal Bank Award（1999）
- 荣誉学位若干（页面列举 Laval 等）；Canadian Medical Hall of Fame（metadata）

## 9. 机构清单

- 教育：St. Nicholas Church of England School、Arnold School for Boys、University of Manchester（BSc、PhD 1956）
- 任职：不列颠哥伦比亚研究理事会（博士后，1956–1960）；University of Wisconsin–Madison 酶研究所（1960，随 Khorana）；加拿大渔业研究委员会温哥华站（高级科学家、化学部主任）；UBC 医学院生物化学系（1966 起，教授）；ZymoGenetics 创始人（1981，Seattle）；UBC 分子遗传中心主任（1986）；UBC 生物技术实验室创始主任（1987–1995）；PENCE 创始科学领导人；UBC Peter Wall Distinguished Professor of Biotechnology（1996）；BC 癌症研究中心基因组测序中心创始主任（1999）
- 命名机构：Michael Smith Foundation for Health Research（2001）、Michael Smith Laboratories（UBC，2004）、Canada's Michael Smith Genome Sciences Centre（2004）、Michael Smith Building（University of Manchester，2004）

## 10. 终审清单

- [ ] 生卒 1932-04-26 / 2000-10-04，享年 68，出生地 Blackpool、去世地 Vancouver
- [ ] 1993 与 Kary Mullis 共享表述准确；两人贡献方向（定点突变 vs PCR）未混
- [ ] 博士导师页面无载禁写；博士后导师 Khorana 口径准确
- [ ] 定点突变论文 1978（JBC）；ZymoGenetics 1981 三创始人
- [ ] 奖金捐助三分法表述准确；机构命名年份（2001/2004）准确
- [ ] 引语全部可在本地 Wikipedia 原文找到（FRS 证书段）
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Michael_Smith_chemist/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/` 肖像已就位或装饰圆占位（注明理由）
- [ ] **国籍**：封面顶部明示加拿大（British-Canadian 口径）
- [ ] **引语核对**：FRS 证书段须在 Wikipedia 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger、Kary_Mullis 等）对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 的更新由主控统一收尾（本提示词不直接改动）。
> **最重要的事：每写一页就 make，看到溢出就修。**
