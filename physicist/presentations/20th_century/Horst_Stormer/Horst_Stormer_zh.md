# Horst L. Störmer（霍斯特·施特默）立传提示词

> qid=Q71015 · 1949-04-06 –（在世）· 德裔美国物理学家 · 20 世纪 · 1998 诺贝尔物理学奖
> 本地 Wikipedia 数据源：`physicist/presentations/20th_century/20th_century/Horst_L._Störmer/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家标杆 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**。物理学家立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。⚠️ `images.txt` **无任何人物照片**（仅 Wikiquote/Commons 图标）——**封面头像用装饰圆占位**（`\IfFileExists` 条件包含 + `\faIcon{user}\enspace Portrait` 兜底）；Review-1 时优先尝试补真实肖像（可试 Commons `Special:FilePath` 检索 "Horst Störmer" / "Horst Ludwig Störmer" 类文件名，404 或返回 HTML 即换名或保持占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 德国 / 美国入籍`——封面主徽章写「德国」，身份页注"已入籍美国"），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。⚠️ 总名单国籍列标 United States，与 page.md（德国法兰克福出生、后入籍美国）不一致——以 page.md 为准并在陷阱表注明，总名单修正留待批量任务。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色（诺奖金）+ 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「二维电子气 / 强磁场中的电子海洋」母题。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Horst Ludwig Störmer（德语发音 [ˈhɔʁst ˈluːtvɪç ˈʃtœʁmɐ]）
- **生卒**：1949-04-06 生于德国法兰克福美因河畔（Frankfurt am Main）；在世（death_date 留白）
- **国籍**：德国（生于法兰克福）；**已入籍美国**（page.md 明载 naturalized US citizen）
- **身份**：物理学家、诺奖得主、哥伦比亚大学荣休教授
- **家庭**：在法国格勒诺布尔做博士研究期间结识 Dominique Parchet，与其结婚，数年后离婚——page.md 仅此一载，其余家庭信息禁写
- **成长与教育轨迹**：
  - 在法兰克福附近的小镇 Sprendlingen（今属 Dreieich）长大
  - 1967 年毕业于 Neu-Isenburg 的 Goetheschule
  - 先入达姆施塔特工业大学（TH Darmstadt）读**建筑工学**，后转法兰克福歌德大学——因错过物理注册期**先读数学再转物理**；在 Werner Martienssen 实验室完成 Diploma，导师 Eckhardt Hoenig，同门还有**未来的诺奖得主 Gerd Binnig**
  - 博士阶段赴法国格勒诺布尔，在法国 CNRS 与德国马普固体研究所合办的高磁场实验室做研究；由斯图加特大学（University of Stuttgart）授予 **1977 年博士**，导师 Hans-Joachim Queisser，论文主题为**强磁场下电子-空穴液滴的研究**
- **博士导师**：Hans-Joachim Queisser；**博士生**：Jun Zhu
- **研究领域**：物理（半导体物理、二维电子系统、分数量子霍尔效应）
- **任职轨迹**：博士后在贝尔实验室（Bell Labs）工作 **20 年**（诺奖实验在此完成）→ 哥伦比亚大学 **I. I. Rabi 物理学与应用物理学讲席教授** → 2011 年荣休（professor emeritus）

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **战后德国的少年（1949–1967）**：法兰克福出生、Sprendlingen 长大；Goetheschule 毕业。
2. **专业三连跳的求学者**：建筑工学（达姆施塔特）→ 数学（错过物理注册期）→ 物理（法兰克福歌德大学）——每一跳都通向最终的方向。
3. **Martienssen 实验室与 Binnig 同门**：Diploma 期间的同伴 Gerd Binnig 后来也获诺贝尔奖（1986，扫描隧道显微镜）——一间实验室走出两位诺奖得主。
4. **格勒诺布尔的高磁场岁月**：法德合办高磁场实验室（CNRS + 马普固体研究所）——强磁场实验的训练场，也是他结识第一任妻子 Dominique Parchet 的地方；1977 年斯图加特大学博士。
5. **贝尔实验室（1977 起，20 年）**：移居美国；半导体二维电子系统研究的主场。
6. **调制掺杂（modulation doping，"与诺奖同等重要"的发明）**：page.md 明载 "Perhaps as important as the work for which he won the Nobel prize is his invention of modulation doping"——制造**极高迁移率二维电子系统**的方法；正是它使分数量子霍尔效应的后续观测成为可能。
7. **分数量子霍尔效应的实验发现（1981-10，本篇核心页）**：page.md 明载由 Störmer 与 Tsui 于 **1981 年 10 月**在 **MIT Francis Bitter 高磁场实验室**的实验中发现（⚠️ Tsui 篇与总名单口径为 1982——跨篇差异，见陷阱表）。
8. **一年之内：Laughlin 的理论解释**：实验发现后不到一年，Robert Laughlin 给出理论解释（1983，Laughlin 波函数）——三人三段式完成"发现新量子流体"的完整叙事。
9. **1998 年诺贝尔物理学奖**：获奖理由 "for their discovery of a new form of quantum fluid with fractionally charged excitations"（总名单中文：表彰他们发现具有分数电荷激发的新型量子流体）；与 Daniel Tsui、Robert Laughlin 共享；获奖时实验所引用的工作在贝尔实验室完成；Nobel 演讲 1998-12-08 *The Fractional Quantum Hall Effect*。
10. **哥伦比亚大学 I. I. Rabi 讲席教授**：贝尔 20 年后转 academia——执掌以著名物理学家命名的讲席（与 Rabi 立传篇形成呼应页）。
11. **美国哲学会（2006）与荣休（2011）**：2006 年入选 American Philosophical Society；2011 年以 professor emeritus 荣休。
12. **荣誉长廊**：Buckley 凝聚态奖（1984，与 Tsui 共享）、Franklin 奖章（1998）、诺奖（1998）、德国联邦十字勋章指挥官级（Klung Wilhelmy 科学奖等 metadata 补充）。

## 3. 配色方案

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（半导体深青） | `#1D4E5F` | 半导体二维电子系统的深海 / 强磁场中的电子海洋 |
| 强调色（诺奖金） | `#C9A227` | 诺贝尔奖 / 尊崇 |
| 分类色 1（调制掺杂 — 蓝） | `#3A6EA5` | modulation doping / 高迁移率二维电子气 |
| 分类色 2（分数量子霍尔 — 玫瑰） | `#A83A5A` | FQHE 实验发现 / MIT Bitter 实验室 |
| 分类色 3（德法求学 — 靛蓝） | `#4C5FD5` | 达姆施塔特 / 法兰克福 / 格勒诺布尔 / 斯图加特 |
| 分类色 4（哥伦比亚传承 — 琥珀） | `#C08A2A` | I. I. Rabi 讲席 / 荣誉与公共科学 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落）叠加**若干平行细线**，呼应「二维电子气——电子被约束在平面内、强磁场下形成量子流体」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：管弦 / 探索 / 远征（从德国到法国到美国的科学远征）
- **选定曲目**：Ghostwriter Music **Pathfinder**（管弦 / 探索，来自 inspiring-electronic 合辑备选），匹配"建筑→数学→物理、德国→法国→美国"的开辟者足迹与高磁场实验室的探索气质。
- **落地文件**：`physicist/presentations/20th_century/Horst_Stormer/Pathfinder.wav`（复制自 `music_audio/inspiring-electronic/` 目录下 Pathfinder 对应 wav，不入 git）。
- **匹配理由**：施特默的叙事是一条"开路者"轨迹——调制掺杂为 FQHE 铺路、二维电子气为一个新领域奠基；探索气质贴合；与本批次其余五人曲目不重复。

## 3.6 研究领域表（数据库入库用，第 4 步）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | condensed matter physics | 凝聚态物理 | 固体物理实验研究的主领域 | 身份页 |
| 1 | semiconductor physics | 半导体物理 | 贝尔实验室 20 年的研究主场 | 贝尔页 |
| 2 | two-dimensional electron systems | 二维电子系统 | 调制掺杂造出极高迁移率体系 | 调制掺杂页 |
| 3 | fractional quantum Hall effect | 分数量子霍尔效应 | 与 Tsui 的实验发现（1981-10），1998 诺奖核心 | 核心贡献页 |
| 4 | modulation doping | 调制掺杂 | 「与诺奖同等重要」的发明 | 核心页 |

## 3.7 术语清单（第 9 步审查用）

| 英文 | 中文 | 风险 |
|------|------|------|
| modulation doping | 调制掺杂 | page.md 谨慎措辞 "Perhaps as important as…" 照抄 |
| fractional quantum Hall effect | 分数量子霍尔效应 | 实验发现=Störmer+Tsui，勿写独自发现 |
| two-dimensional electron system | 二维电子系统 | 强磁场下的量子流体载体 |
| electron hole droplets | 电子-空穴液滴 | 博士论文主题（强磁场下） |
| Francis Bitter High Magnetic Field Lab | （MIT）弗朗西斯·比特高磁场实验室 | 1981-10 实验地 |
| I. I. Rabi professor | 拉比讲席教授 | 哥伦比亚大学讲席，以诺奖得主 I. I. Rabi 命名 |
| professor emeritus | 荣休教授 | 2011 荣休 |
| naturalized US citizen | 已入籍美国 | 国籍口径：封面德国、身份页注入籍 |
| Goetheschule Neu-Isenburg | 新伊森堡歌德学校 | 1967 毕业勿与法兰克福混淆 |
| Bell Labs | 贝尔实验室 | 约 20 年，诺奖实验所引工作在此完成 |

## 4. Slide 规划（约 15 页，Wilson 式结构）

1. **封面**（`\titleslide`）：顶部标签「分数量子霍尔效应 · 德国」+ 施特默 1949– + 右上头像（装饰圆占位）+ 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍·入籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **核心贡献概览**（`\hookslide`）：调制掺杂 / 分数量子霍尔效应实验发现 / 哥伦比亚讲席 / 荣誉传承
4. **战后德国少年**（1949–1967）：法兰克福、Sprendlingen、Goetheschule
5. **建筑→数学→物理的求学三连跳**（1967–1977）：达姆施塔特、法兰克福（错过注册先读数学）、Martienssen 实验室、与 Binnig 同门
6. **格勒诺布尔高磁场岁月**：法德合办实验室、Queisser 门下电子-空穴液滴博士论文（1977）
7. **贝尔实验室二十年**：移居美国、半导体二维电子系统
8. **调制掺杂（核心页一）**：极高迁移率二维电子系统、"与诺奖同等重要"的发明、为 FQHE 观测铺路
9. **分数量子霍尔效应的实验发现（核心页二）**：1981-10 MIT Francis Bitter 实验室、与 Tsui 合作（跨篇年份差异注）
10. **1998 年诺贝尔物理学奖**：官方理由（总名单中文：表彰他们发现具有分数电荷激发的新型量子流体）；与 Tsui、Laughlin 共享；Nobel 演讲 *The Fractional Quantum Hall Effect*
11. **哥伦比亚大学 I. I. Rabi 讲席教授**：从工业实验室到 academia、以拉比命名的讲席（与 Rabi 篇呼应）
12. **美国哲学会与荣休**（2006 / 2011）：入籍美国、晚年学术生涯
13. **荣誉长廊**：Buckley（1984）/ Franklin（1998）/ 诺奖（1998）/ 联邦十字勋章等编年
14. **传承**：博士生 Jun Zhu、与 Tsui / Laughlin 的三段式叙事回顾
15. **结尾**：在世、"先造出电子高速公路、再发现新量子流体的人"的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **发现年份跨篇差异（本篇最大陷阱）**：Störmer page.md 明载实验发现于 **"October 1981"**（MIT Francis Bitter 高磁场实验室）；**Tsui page.md 与总名单口径为 "1982"**；而 Störmer page.md 另一处又写"1982 年发现后不到一年 Laughlin 解释"。**本篇以本人 page.md 的 "October 1981" 为主表述，并加注"一说 1982"；与 Tsui 篇（以 1982 为主、注 1981-10）形成互注**，Review 时三篇（含 Laughlin 篇）口径必须一致。
- **诺奖份额禁写**：三人获奖的**具体份额比例 page.md 无载**——禁写"Störmer+Tsui 共享三分之二 / Laughlin 得三分之一"或任何比例；统一"三人共享"。总名单亦未载份额（简报中"共享三分之二"说法无数据源支撑，勿采用）。
- **国籍口径**：page.md 载德国出生 + 已入籍美国；总名单国籍列标 United States——**以 page.md 为准**：封面写「德国」、身份页注"已入籍美国"；勿写"美国物理学家施特默"。总名单修正留待批量任务（连同 Esaki/Bednorz 等）。
- **"被限制行走"轶事禁写**：page.md **无载**任何童年被家人限制行走的轶事——禁写（简报"若有"——核实结果为无）。
- **调制掺杂定位**：page.md 用 "Perhaps as important as…" 的谨慎措辞——照抄其语气，勿拔高为"最重要发明"或贬为"附带成果"。
- **发现归属精确**：FQHE 实验发现 = **Störmer + Tsui**（两人合作）；Laughlin 是理论解释——勿写"施特默独自发现"或"三人共同实验"。
- **整数量子霍尔效应禁混**：IQHE 属 von Klitzing（1985 诺奖），Störmer page.md 未提——正文禁写对比段落，最多在陷阱表自我提醒。
- **婚姻表述克制**：page.md 仅载格勒诺布尔结识 Dominique Parchet、结婚、数年后离婚——如实一句带过，勿扩展。
- **Buckley 奖年份**：Störmer page.md 载 **1984**（与 Tsui 篇一致，为两人共享）；**勿与 Laughlin 的 1986 Buckley 混同**（那是劳克林个人获奖）。
- **达姆施塔特专业**：建筑工学（architectural engineering）——勿写成"建筑学/土木"之外的发散表述；"先数学后物理"的原因（错过物理注册期）照 page.md。
- **Gerd Binnig 同门**：page.md 明载 Diploma 期间与 Binnig 同在 Martienssen 实验室——可写"同门未来的诺奖得主"，勿写成"师兄弟/合作发表"。
- **在世人物**：无卒日，death_date 留白；结尾页写"1949–"勿补卒年。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q71015 | 待写入 |
| name_zh | 霍斯特·施特默 | 待写入 |
| name_en | Horst L. Störmer | 待写入 |
| birth_date | 1949-04-06 | 待写入 |
| death_date | （空，在世） | 待写入 |
| nationality | Germany（生于法兰克福；已入籍美国——总名单国籍列 United States 待修正） | 待写入 |
| primary_occupation | physicist | 待写入 |
| field_of_work | physics（半导体、二维电子系统、FQHE） | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Hans-Joachim Queisser
- **Diploma 导师**：Eckhardt Hoenig（法兰克福，可选入库，注明层级）
- **同门**：Gerd Binnig（Martienssen 实验室，同为诺奖得主——colleague 类）
- **co-honored（同届共享）**：Daniel C. Tsui（普林斯顿，实验合作者）、Robert B. Laughlin（斯坦福，理论解释者）——1998 诺贝尔物理学奖三人共享
- **实验搭档**：Daniel C. Tsui（贝尔实验室 FQHE 实验；另共享 1984 Buckley 奖）
- **博士生**：Jun Zhu
- **机构继任关系**：哥伦比亚大学 I. I. Rabi 讲席（讲席命名来源 I. I. Rabi 可作 note）

## 8. 奖项清单

- 诺贝尔物理学奖（1998，与 Tsui、Laughlin 共享）
- Oliver E. Buckley Condensed Matter Prize（1984，与 Tsui 共享）
- The Benjamin Franklin Medal, Franklin Institute（1998）
- Klung Wilhelmy Science Award（metadata 有载，年份 page.md 未给）
- 德国联邦功绩十字勋章指挥官级（Knight Commander's Cross of the Order of Merit of the Federal Republic of Germany，metadata 有载）
- Fellow of the American Physical Society（metadata 有载）
- 法兰克福物理协会荣誉会员（metadata 有载）
- American Philosophical Society（2006，page.md 明载）

## 9. 机构清单

- 教育：Goetheschule Neu-Isenburg（1967）、达姆施塔特工业大学（建筑工学，未完成）、法兰克福歌德大学（数学→物理，Diploma @Martienssen 实验室）、斯图加特大学（PhD 1977）
- 博士研究地：格勒诺布尔高磁场实验室（法国 CNRS + 德国马普固体研究所合办）
- 任职：贝尔实验室（约 20 年）→ 哥伦比亚大学 I. I. Rabi 物理学与应用物理学讲席教授 → 2011 荣休

## 10. 终审清单

- [ ] 生卒 1949-04-06 / 在世留白，出生地 Frankfurt am Main
- [ ] FQHE 发现"1981-10（本人 page.md）+ 注 1982 跨篇差异"表述准确
- [ ] 诺奖份额比例未出现（三人共享表述）
- [ ] 授奖页用总名单官方理由"发现具有分数电荷激发的新型量子流体"
- [ ] 国籍口径：封面德国、身份页注入籍美国、陷阱表注明总名单待修
- [ ] 调制掺杂"Perhaps as important"语气保留
- [ ] 无"限制行走"轶事、无 IQHE 对比段落（page.md 无载）
- [ ] Buckley 1984（与 Tsui 共享）与 Laughlin 1986 未混淆
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像（装饰圆占位）+ 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `20th_century/Horst_L._Störmer/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：装饰圆占位；优先尝试补真实肖像（Commons 检索失败即保持占位）
- [ ] **国籍**：封面顶部徽章明示德国（身份页注入籍美国）
- [ ] **引语核对**：引语必须在 page.md 找到原文（本篇可加引号的原文极少，一律间接转述为主）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一（半角引号 " "）
- [ ] 与同世纪物理学家（Heisenberg / Rabi / Wilson）格式对齐；与同批 Tsui / Laughlin 篇口径互查（1998 三人叙事、FQHE 发现年份、Buckley 年份三处一致；与 Rabi 篇互查 I. I. Rabi 讲席呼应页）

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
