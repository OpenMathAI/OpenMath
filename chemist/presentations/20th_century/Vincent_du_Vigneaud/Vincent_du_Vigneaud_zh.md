# Vincent du Vigneaud（文森特·迪维尼奥）立传提示词

> qid=Q33128 · 1901-05-18 – 1978-12-11 · 美国生物化学家 · 20 世纪 · 诺贝尔化学奖（1955，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Vincent_du_Vigneaud/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 高斯式时间线 + 表格语义化 tabularx + 公式展示框，是本次书写的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/` 已就位；若无真实肖像按 Review-1 流程先补图，全部 404 才允许装饰圆占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{dna}\enspace 第一个合成的肽激素\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「肽链 / 环肽」母题——圆点串环暗示氨基酸残基连成催产素环肽。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Vincent du Vigneaud（中文惯称：文森特·迪维尼奥；法裔，姓氏保留法语小写前缀 du）
- **生卒**：1901-05-18 生于伊利诺伊州芝加哥 → 1978-12-11 逝于纽约州 White Plains，享年 77
- **国籍**：United States（美国）
- **身份**：生物化学家（biochemist）；1955 年诺贝尔化学奖——第一个多肽激素的全合成（催产素）
- **家庭**：法裔；父 Alfred du Vigneaud 为发明家兼机械师，母 Mary Theresa；1924-06-12 在大学打工做侍者时结识 Zella Zon Ford，同年结婚；妻先于 1977 年去世，他一年后病逝
- **教育轨迹**：
  - Schurz High School（1918 年完成中学）；高中时因新朋友邀他做含硫炸药实验而与硫结缘
  - 一战期间高年级生须下农场劳动，在伊利诺伊 Caledonia 附近挤奶——一度想当农民
  - 姐姐 Beatrice 劝他入伊利诺伊大学香槟分校（UIUC）读化学工程，第一年发现兴趣在化学，转化学专业
  - 1924 硕士（MS）→ 杜邦公司短暂任职 → 1925 入罗切斯特大学读博
  - 1927 博士（论文 *The Sulfur of Insulin*）
- **导师**：John R. Murlin（罗切斯特大学博士导师，infobox 明载）
- **研究领域**：生物化学——含硫化合物、肽与蛋白质、肽激素（催产素/加压素）、生物素、转甲基作用

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **芝加哥之子（1901）**：发明家父亲的儿子；高中朋友的"含硫炸药实验"点燃一生与硫的缘分。
2. **农场与转轨（1918–1922）**：战时农场挤奶想务农，被姐姐 Beatrice 劝回 UIUC；自述发现 "it was chemistry rather than engineering that appealed to me most"——特别着迷与医药物质相关的有机化学。
3. **两位引路人（1920s 初）**：Carl Shipp Marvel 与 Howard B. Lewis 的课程令他记住他们对硫 "extremely enthusiastic"；1924 年 Marvel 为他在费城总医院安排助理生物化学家职位（条件是替他制备 10 磅铜铁试剂 cupferron 作路费交换）。
4. **胰岛素之硫（1925–1927）**：罗切斯特大学 Murlin 组博士论文 *The Sulfur of Insulin*——从胰岛素的硫切入生物化学。
5. **霍普金斯与欧洲游学（1927–1929）**：随 John Jacob Abel 做博士后（Johns Hopkins 医学院）；National Research Council Fellow 赴欧——德累斯顿 Kaiser Wilhelm 皮革研究所随 Max Bergmann 与 Leonidas Zervas，爱丁堡随 George Barger。
6. **UIUC 教授（1929–1932）**：回母校任教授。
7. **乔治华盛顿与康奈尔（1932–1967）**：1932 入 George Washington University 医学院；1938 转康奈尔医学院（纽约），直到 1967 荣休；退休后在伊萨卡康奈尔大学任职。
8. **含硫世界（1930s–1940s）**：在胰岛素、生物素（biotin）、转甲基作用（transmethylation）、青霉素上的研究为他建立声誉。
9. **催产素与加压素（1950s）**：阐明并合成催产素（oxytocin）与加压素（vasopressin）两种垂体后叶肽激素——催产素成为第一个被合成的多肽激素（诺奖理由口径）。
10. **首个肽构效关系**：对催产素/加压素开展系列结构-活性关系研究——页面称 "perhaps the first of their type for peptides"。
11. **1955 诺贝尔化学奖（独享）**：官方理由 "for his work on biochemically important sulphur compounds, especially for the first synthesis of a polypeptide hormone"；诺奖演讲 1955-12-12《A Trail of Sulfa Research: From Insulin to Oxytocin》。
12. **荣誉满载**：Nichols Medal（1945）、Lasker 基础医学研究奖（1948）、Willard Gibbs Award（1956）、NAS 与美国哲学学会（1944）、AAAS（1948）、John Scott Award、Remsen Award；UIUC 时期（1930）加入 Alpha Chi Sigma 荣誉化学 fraternity。
13. **晚年（1974–1978）**：1974 年中风被迫退休；1977 妻去世，1978-12-11 随逝于 White Plains；学术轨迹总结成书 *A Trail of Research in Sulphur Chemistry and Metabolism and Related Fields*。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（绛紫 royal purple） | `#5B2A86` | 肽化学的精密与垂体激素的神秘（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（含硫化学 badgeSulfur） | `#B4632A` | 琥珀胰岛素之硫 / 生物素 |
| 分类色 2（肽激素 badgeOxytocin） | `#2E5A9E` | 蓝催产素 / 加压素 |
| 分类色 3（构效关系 badgeSAR） | `#1B7A43` | 绿结构-活性关系 |
| 分类色 4（代谢与转甲基 badgeMetab） | `#6E4E7E` | 紫转甲基 / 新陈代谢 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），圆点成环呼应「环肽 + 侧链」的催产素拓扑。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Winds Of Freedom** — Really Slow Motion & Giant Apes（文件：`music_audio/inspiring-electronic/25-l3Fsk4R6eys-Really Slow Motion & Giant Apes - Winds Of Freedom (Epic Heroic Orchestral).wav`；勿复制 wav，视频阶段直接引用路径）
- **风格**：英雄式管弦 / 开阔 / 上升感
- **匹配理由**：
  - "自由之风" 匹配"第一次"的开拓感——第一个被合成的多肽激素，为肽合成时代开路
  - 英雄管弦匹配其轨迹——从农场挤奶少年到诺奖领奖台，是被姐姐与师长一路托举的上升弧线
  - 开阔气质匹配其学术谱系——Abel、Bergmann、Zervas、Barger 一脉相承的肽化学传承
- **时长**：以实际文件为准，视频合成用 ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 第一个肽激素的合成者 / Vincent du Vigneaud 1901–1978 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  迪维尼奥的一生 — 时间线（10 节点：1901→1918→1924→1927→1928→1929→1932→1938→1955→1978）
04  早年：农场少年与化学转轨 (1901–1922) — 表格「时间|事件|结果」
05  UIUC 与两位引路人 (1920s) — 表格「人物|影响|结果」（Marvel/Lewis；费城职位与 10 磅 cupferron 轶事）
06  胰岛素之硫 (1925–1927) — 表格「问题|方法|结果」+ 公式框：胰岛素含硫研究视角
07  欧洲游学 (1927–1929) — 表格「地点|导师|收获」（Abel→Bergmann/Zervas→Barger）
08  含硫世界 (1930s–1940s) — 表格「对象|发现|意义」（胰岛素/生物素/转甲基/青霉素）
09  催产素合成 (1950s) — 表格「问题|方法|结果」+ 公式框：催产素环肽拓扑
10  1955 诺贝尔化学奖 — 获奖理由原文 + 独享标注 + 诺奖演讲标题
11  荣誉清单 — 「类别|代表|意义」表格 + itemize（Lasker 1948/Gibbs 1956/NAS 1944 等）
12  构效关系与学术传承 — 表格「人物|方向|结果」（Simmonds 学生；肽构效关系开山）
13  遗产：从肽激素到合成时代 — 四分类遗产盒 + 学术谱系（Abel 一脉）
14  结尾 — 「从一个硫原子出发，抵达生命的激素。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1955 诺奖 | **独享**；官方措辞 "for his work on biochemically important sulphur compounds, especially for the first synthesis of a polypeptide hormone"——"第一个被合成的多肽激素"指**催产素** |
| 全合成年份 | 本地页面**未载**催产素合成的具体年份——禁写 1953 等年份，页面无载即留白 |
| 加压素排序 | 页面 Known for 写 "synthesis of oxytocin and vasopressin"——两者都合成，但诺奖理由特指第一个多肽激素（催产素）；勿写两者获奖先后（页面无载） |
| AVP gene | 页面一句 "via manipulating the AVP gene" 属叙述噪声（与其 1950s 工作语境不符）——禁写基因操作，只写"阐明与合成" |
| 姓氏写法 | du Vigneaud（小写 du + 大写 V）——勿写 Du Vigneaud / DuVigneaud |
| 导师只有一位 | 博士导师 John R. Murlin（罗切斯特）；Abel 是博士后导师、Bergmann/Zervas/Barger 是游学合作者——勿混入"博士导师" |
| Marvel 角色 | Marvel 是 UIUC 课程引路人 + 职位引荐者（10 磅 cupferron 换路费轶事页面明载），**非博士导师** |
| 学生仅一人 | infobox Doctoral students 仅 **Sofia Simmonds** 一人——勿扩写其他学生 |
| 农场轶事 | 一战下农场（Caledonia 挤奶）→ 想当农民 → 姐姐 Beatrice 劝学化学——页面明载可写，勿加"挤奶启发催产素"之类虚构因果 |
| 结局口径 | 1974 中风退休、1977 妻去世、1978-12-11 病逝——三件事时序勿乱 |
| 机构顺序 | UIUC（教授）→ GWU（1932）→ Cornell Medical College NYC（1938–1967）→ Cornell Ithaca（退休后）——勿写"1967 前一直在伊萨卡" |
| 引语口径 | 页面可引仅两处：转学位自述段（chemistry rather than engineering）与 Lewis/Marvell 'extremely enthusiastic about sulfur'；其余"名言"禁写 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q33128 | ✅ |
| name_zh | 文森特·迪维尼奥 | ✅ |
| name_en | Vincent du Vigneaud | ✅ |
| birth_date | 1901-05-18 | ✅ |
| death_date | 1978-12-11 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry（person_field 细分：biochemistry / peptide synthesis / sulfur biochemistry / hormone chemistry，带 rank） | ✅ |

## 7. 社会关系入库清单

**师长 / 门生 / 合作者**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | John R. Murlin | 师→生（博士导师） | 罗切斯特大学，1927 论文 The Sulfur of Insulin |
| advisor-student | Sofia Simmonds | du Vigneaud → 学生 | infobox Doctoral students 唯一博士生 |
| other | John Jacob Abel | 无向 | 1927–28 Johns Hopkins 博士后导师 |
| colleague | Max Bergmann | 无向 | 1928–29 德累斯顿 Kaiser Wilhelm 皮革研究所合作（NRC Fellow） |
| colleague | Leonidas Zervas | 无向 | 同上，德累斯顿时期合作者 |
| colleague | George Barger | 无向 | 1928–29 爱丁堡大学医学院合作 |
| colleague | Carl Shipp Marvel | 无向 | UIUC 课程引路人，1924 为其安排费城总医院职位 |
| spouse | Zella Zon Ford | 无向 | 1924-06-12 相识同年结婚；先于 1977 年去世 |

> **禁入库名单**（页面无载或仅语境提及）：Howard B. Lewis（课程影响者，页面仅一句提及，非直接师承/合作）；家人（父 Alfred、母 Mary Theresa、姐 Beatrice）非学术关系不入库。

## 8. 奖项清单

- Nobel Prize in Chemistry（1955，独享）
- William H. Nichols Medal（1945）
- Albert Lasker Award for Basic Medical Research（1948）
- Willard Gibbs Award（1956）
- John Scott Award；Remsen Award
- 美国国家科学院院士（1944）；美国哲学学会（1944）；American Academy of Arts and Sciences（1948）
- Alpha Chi Sigma 荣誉化学 fraternity（1930，UIUC）

## 9. 机构清单

- 教育：Carl Schurz High School（–1918）、University of Illinois Urbana-Champaign（BS、MS 1924）、University of Rochester（PhD 1927）
- 任职：DuPont（1924 短暂）、Philadelphia General Hospital（1924–25 助理生物化学家）、University of Rochester（1925–27 博士）、Johns Hopkins（1927–28 博士后）、UIUC 教授（1929–1932）、George Washington University 医学院（1932–1938）、Cornell Medical College 纽约（1938–1967，1967 荣休）、Cornell University Ithaca（退休后）
- 诺奖时机构：Cornell Medical College（纽约）

## 10. 终审清单

- [ ] 生卒 1901-05-18 / 1978-12-11（享年 77），出生地 Chicago、去世地 White Plains
- [ ] 1955 独享、获奖理由用官方原文；"第一个多肽激素"=催产素；合成年份页面无载即留白
- [ ] 博士导师仅 Murlin；Abel=博士后、Bergmann/Zervas/Barger=游学合作、Marvel=引路人
- [ ] 博士生仅 Sofia Simmonds 一人
- [ ] 机构时序 UIUC→GWU→Cornell NYC→Cornell Ithaca 无错位
- [ ] AVP gene 噪声句不进 Beamer
- [ ] 引语均可溯源（自述段、extremely enthusiastic about sulfur）
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Vincent_du_Vigneaud/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：`images/` 肖像就位与图注核对（infobox 有 "du Vigneaud in 1955" 照）
- [ ] 国籍：封面顶部明示美国
- [ ] 引语核对：引语必须在 Wikipedia 原文找到（获奖理由、自述段）
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 黄金骨架）对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾，本提示词不改动该文件。
> **数据入库**：yaml 见 `MySQL/data/Vincent_du_Vigneaud.yaml`（新建记录 NEW，含 4 fields / 8 relations）。
