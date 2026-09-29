# Richard Willstätter（理查德·维尔施泰特）立传提示词

> qid=Q77072 · 1872-08-13 – 1942-08-03 · 德国化学家 · 20 世纪 · 诺贝尔化学奖（1915，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Richard_Willstätter/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页 + 气泡背景。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/` 就位后使用；无真实肖像则用装饰圆占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{leaf}\enspace 植物色素的解码者\enspace·\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「色素分子 / 光合作用」母题——绿色系圆点暗示叶绿素捕获的光。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（对象 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Richard Martin Willstätter（中文惯称：理查德·维尔施泰特；FRS(For) FRSE）
- **生卒**：1872-08-13 生于巴登大公国卡尔斯鲁厄（德意志帝国）→ 1942-08-03 逝于瑞士 Muralto（洛迦诺附近），心脏病，享年 69（生日后 10 天）
- **国籍**：Germany（德国；1939 年移居瑞士）
- **身份**：有机化学家（organic chemist；植物色素结构研究）
- **家庭**：犹太家庭；父 Maxwell (Max) Willstätter 为纺织品商人，母 Sophie Ulmann。1903 年娶 Sophie Leser（1908 年妻子去世；育有 2 个孩子）——注意：母亲与妻子同名 Sophie，行文须区分
- **教育轨迹**：
  - 卡尔斯鲁厄文理中学 → 全家迁纽伦堡后入当地 Technical School
  - 18 岁入慕尼黑大学（Ludwig-Maximilians-Universität München）学科学，在此一待 15 年
- **导师**：Alfred Einhorn（博士论文指导）；Adolf von Baeyer（mentor，1916 年维尔施泰特回慕尼黑继任其教席）
- **博士**：1894，论文主题为可卡因（cocaine）的结构
- **研究领域**：有机化学——生物碱、植物色素（叶绿素/花果色素）、酶反应机理

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **卡尔斯鲁厄犹太商人之家（1872）**：纺织品商人之子，少年时代随家迁纽伦堡。
2. **慕尼黑的 15 年（1890 起）**：18 岁入慕尼黑大学化学系，从学生到教员。
3. **可卡因结构（1894 博士）**：师从 Alfred Einhorn，博士论文研究可卡因结构；继而研究其他生物碱并合成数种。
4. **讲席阶梯（1896–1902）**：1896 年任 Lecturer，1902 年任副教授（Professor extraordinarius，无教席教授）。
5. **转赴 ETH 苏黎世（1905）**：任教授，开始研究植物色素叶绿素，首先测定其经验式。
6. **柏林与威廉皇帝化学研究所（1912）**：任柏林大学教授兼威廉皇帝化学研究所所长，研究花与果实色素；定居科学家云集的 Dahlem。
7. **叶绿素 a 与 b（柏林时期）**：证明叶绿素是两种化合物的混合物——chlorophyll a 与 chlorophyll b。
8. **1915 诺贝尔化学奖**：表彰其对植物色素（包括叶绿素）结构的研究；诺奖演讲 1920-06-03 *On Plant Pigments*。
9. **一战：选择防护而非毒气（1915）**：挚友 Fritz Haber 邀其参加毒气研发，他拒绝研制毒物、只同意做防护——与同事研制三层滤毒罐（可吸收敌方所有毒气），至 1917 年量产三千万只，获二级铁十字勋章。
10. **回慕尼黑继任 Baeyer（1916）**：接替导师 Baeyer 的教席。
11. **酶反应机理（1920 年代）**：大量工作确立酶是化学物质而非生物有机体；但直到生命尽头他仍拒绝接受酶是蛋白质。
12. **以退休抗议反犹（1934）**：作为对日益猖獗的反犹主义的抗议宣布退休；校方、学生与部长的挽留均未动摇这位 53 岁科学家；此后隐居慕尼黑，仅靠助手电话报告结果继续研究；1933 年曾为《Juden im deutschen Kulturbereich》作序，1934-12 该书印本全部被柏林国家警察查抄。
13. **流亡与自传（1939–1942）**：1939 年才离开德国移居瑞士，在 Muralto 度过最后三年撰写自传 *Aus meinem Leben*（德文版 1949 年出版，英译 *From My Life* 1965）；1965 年其就读过的纽伦堡学校更名为 Willstätter-Gymnasium 以志纪念。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深靛蓝 deepindigo） | `#14324F` | 光谱深处的色素蓝（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（生物碱 badgeAlkaloid） | `#2E5A9E` | 蓝可卡因结构与生物碱合成 |
| 分类色 2（叶绿素 badgeChloro） | `#1B7A43` | 绿叶绿素 a/b 与光合色素 |
| 分类色 3（花果色素 badgePetal） | `#D97B29` | 琥珀花青素 / 果实色素 |
| 分类色 4（酶学 badgeEnzyme） | `#C0395B` | 玫瑰酶反应机理 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「色素捕获光线」的意象。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**SEA** — Alex-Productions（文件 `music_audio/alex-productions/92-WEqfdRXU3IU-SEA.wav`，勿复制 wav）
- **风格**：辽阔 / 沉思 / 带挽歌气质
- **匹配理由**：
  - "辽阔" 匹配叶绿素与植物色素的宏大自然意象——从可卡因生物碱到光合色素的研究版图
  - "沉思" 匹配其晚年——以退休抗议反犹、隐居著述的孤独与尊严
  - "挽歌气质" 匹配一生的悲剧弧线——诺奖巅峰与 1942 年流亡客死瑞士
- **时长**：以实际曲目时长为准，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 植物色素的解码者 / Richard Willstätter 1872–1942 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  维尔施泰特的一生 — Sanger 式时间线（10 节点：1872→1894→1905→1912→1915→1916→1934→1939→1942→1965）
04  早年：卡尔斯鲁厄与纽伦堡 (1872–1890) — 表格「时间|事件|结果」
05  慕尼黑的 15 年：可卡因与生物碱 (1890–1905) — 表格「对象|方法|结果」+ 公式框：博士论文·可卡因结构
06  ETH 苏黎世：叶绿素经验式 (1905–1912) — 表格「问题|方法|结果」
07  柏林与威廉皇帝研究所：叶绿素 a/b (1912–1915) — 表格「发现|证据|意义」+ 公式框：叶绿素 = a + b
08  1915 诺贝尔化学奖 — 表格「理由|演讲|时间」（1920-06-03 On Plant Pigments）
09  一战：三层滤毒罐 (1915–1917) — 表格「抉择|设计|结果」（防护而非毒气；三千万只；二级铁十字）
10  回慕尼黑与酶学研究 (1916–1930s) — 表格「问题|结论|未竟」+ 公式框：酶 = 化学物质（但拒绝「酶 = 蛋白质」）
11  以退休抗议 (1933–1934) — 表格「事件|回应|后果」（作序查抄 / 挽留无效）
12  流亡 Muralto 与自传 (1939–1942) — 表格「阶段|内容|出版」
13  遗产：从生物碱到光合色素 — 四分类遗产盒（生物碱 / 叶绿素 / 花果色素 / 酶学）+ Willstätter-Gymnasium
14  结尾 — 「他为绿色世界写下了化学的注脚。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1915 诺奖口径 | 官方表述为对植物色素（包括叶绿素）结构的研究（page.md 正文口径）；**独享**；诺奖演讲为 1920-06-03 *On Plant Pigments*——勿杜撰其他获奖理由原句 |
| 防毒面具 | 他**拒绝研制毒气、只做防护**（三层滤毒罐吸收敌方毒气）——勿写"参与开发毒气" |
| 酶的结论 | 确立**酶是化学物质而非生物有机体**；但**终生拒绝接受酶是蛋白质**——勿写"证明酶是蛋白质" |
| 两位导师 | 博士论文指导为 **Alfred Einhorn**；Baeyer 是 mentor 且 1916 年由他**继任其慕尼黑教席**——两人并列，勿混 |
| 叶绿素 a/b | 叶绿素是 a 与 b 两种化合物的混合物，结论出自**柏林时期（1912 后）**——勿系于 ETH 时期（ETH 时期为经验式测定） |
| 退休与流亡年份 | **1934** 年以退休抗议反犹（仍居慕尼黑）；**1939** 年才移居瑞士——勿写 1934 年流亡 |
| 两个 Sophie | 母亲 **Sophie Ulmann**、妻子 **Sophie Leser**（1903 结婚，1908 去世，2 个孩子）——勿混淆 |
| 去世地 | 1942-08-03 逝于瑞士 Muralto（洛迦诺附近），心脏病，享年 69——勿与出生地卡尔斯鲁厄混淆 |
| 生卒双值 | 页面实载 1872-08-13 / 1942-08-03（享年 69；去世在生日后 10 天）——按此单一口径 |
| 序言查抄 | 1933 年为《Juden im deutschen Kulturbereich》作序、1934-12 被柏林国家警察查抄——客观陈述，勿加渲染 |
| 自传出版 | 德文版 **1949** 年出版（身后），英译 1965——勿写生前出版 |
| 引语红线 | page.md 仅有 Nobel biography 转述 "Expressions of confidence..." 一句英文叙述——中文引号内不得出现任何无源"原话"，一律间接转述 |
| 品牌口径 | 结尾页品牌写 `OpenMathAI`；引号半角 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q77072 | ✅ |
| name_zh | 理查德·维尔施泰特 | ✅ |
| name_en | Richard Willstätter | ✅ |
| birth_date | 1872-08-13 | ✅ |
| death_date | 1942-08-03 | ✅ |
| nationality | Germany（1939 后居瑞士，nationalities 增 Switzerland rank 1） | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | organic chemistry（person_field 细分见下表） | ✅ |

**person_field 细分（rank 表）**：

| name_en | rank | name_zh |
|---|---|---|
| organic chemistry | 0 | 有机化学 |
| plant pigments | 1 | 植物色素 |
| alkaloid chemistry | 2 | 生物碱化学 |
| enzymology | 3 | 酶学 |

## 7. 社会关系入库清单

**师长 / 学生 / 同事 / 家人**（★红线：只收 page.md 正文或 infobox 明载的关系）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Alfred Einhorn | 师→生（博士论文指导） | 慕尼黑化学系，1894 可卡因结构博士论文 |
| advisor-student | Adolf von Baeyer | 师→生（mentor） | 导师；1916 维尔施泰特回慕尼黑继任其教席 |
| advisor-student | Jean Piccard | 生→师（博士门生） | infobox Doctoral students 唯一在列 |
| colleague | Fritz Haber | 无向 | 挚友；1915 邀其参与毒气项目，他只做防护（三层滤毒罐） |
| spouse | Sophie Leser | 无向 | 1903 结婚，1908 年妻子去世，育 2 子女 |

> 禁入库名单（metadata-only）：metadata.json 未载其他社会关系，无此情形；本篇无 metadata-only 冲突项。注意 Adolf von Baeyer（1905 诺奖得主）在库内已有规范记录，yaml 对手方名用 `Adolf von Baeyer`。

## 8. 奖项清单

- Nobel Prize in Chemistry（1915，独享）
- Faraday Lectureship Prize（1927）
- Davy Medal（1932）
- Willard Gibbs Award（1933）
- Pour le Mérite for Sciences and Arts
- Bavarian Maximilian Order for Science and Art；Adolf-von-Baeyer Gold Medal
- Bressa Prize；Goethe Medal for Art and Science
- Fellow of the Royal Society（For.Mem.RS）
- 荣誉博士：University of Manchester、ETH Zürich、Goethe University Frankfurt、University of Halle-Wittenberg
- Iron Cross Second Class（1917，三层滤毒罐之防护工作）

## 9. 机构清单

- 教育：Karlsruhe Gymnasium → Nuremberg Technical School → Ludwig-Maximilians-Universität München（1890 入学，1894 博士）
- 任职：慕尼黑大学（Lecturer 1896 / 副教授 1902）→ ETH Zürich 教授（1905–1912）→ 柏林大学教授兼威廉皇帝化学研究所所长（1912–1916）→ 慕尼黑大学教授（1916，继任 Baeyer；1934 退休抗议）
- 纪念：Willstätter-Gymnasium（纽伦堡，1965 更名）

## 10. 终审清单

- [ ] 生卒 1872-08-13 / 1942-08-03，享年 69，出生地卡尔斯鲁厄、去世地 Muralto
- [ ] 1915 独享；获奖理由为植物色素（含叶绿素）结构研究；诺奖演讲 1920-06-03
- [ ] 导师 Einhorn + Baeyer 双列；博士生仅 Jean Piccard
- [ ] 防毒面具为防护性工作（拒制毒气）；1934 退休抗议、1939 移居瑞士的年份区分
- [ ] 酶 = 化学物质、但拒绝「酶是蛋白质」的结论区分
- [ ] 母亲 Sophie Ulmann 与妻子 Sophie Leser 区分
- [ ] 引语全部可在 page.md 溯源，无源处一律间接转述
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Richard_Willstätter/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/` 肖像就位或装饰圆占位
- [ ] **国籍**：封面顶部明示德国（1939 后居瑞士可注）
- [ ] **引语核对**：引语必须在 page.md 原文找到，否则改间接转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox<10pt、hbox<50pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger）对齐

---

> **名单状态**：本提示词由 chem-batch-02 批次生成；`chemist/generate_20th_century_list.py` 由主控统一收尾，勿改动。
