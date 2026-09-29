# Greg Winter（格雷格·温特）立传提示词

> qid=Q1545000 · 1951-04-14 –（在世）· 英国 · 诺贝尔化学奖（2018，与 George P. Smith 共享一半；Frances Arnold 获另一半）· 本地数据源：`chemist/presentations/21th_century/pages/Greg_Winter/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：对齐 `chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}` 高斯式骨架——表格语义化 tabularx + 公式展示框 + 时间线页 + 气泡背景。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像用本地 `images.txt` 首图 Greg Winter 2018 斯德哥尔摩诺奖记者会照；下载失败则装饰圆占位并在 Review 注明）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{dna}\enspace 使抗体成为药物的工程师\enspace·\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（Gregory Paul Winter）、国籍、出生地（Leicester）、教育（Royal Grammar School / Trinity College）、博士导师（Brian S. Hartley）、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「抗体 — 展示库」母题——离散圆点暗示噬菌体文库中被筛选的万千变体。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配金色边框浅金底公式展示框（`\fcolorbox` + minipage），如「鼠抗体 → 人源化抗体 → 全人抗体」递进式或 Campath-1H/HUMIRA 药物条目。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Sir Gregory Paul Winter（中文惯称：格雷格·温特；头衔 CBE FRS FMedSci，2004 年受封 Knight Bachelor）
- **生卒**：1951-04-14 生于英格兰莱斯特郡 Leicester（在世，卒日留白）
- **国籍**：United Kingdom（英国）
- **身份**：分子生物学家（molecular biologist）、生物化学家；以治疗性单克隆抗体工作闻名
- **教育轨迹**：
  - Royal Grammar School, Newcastle upon Tyne（中学）
  - Trinity College, Cambridge 自然科学，1973 年毕业（MA）
  - PhD 1977，MRC Laboratory of Molecular Biology，论文《The amino acid sequence of tryptophanyl tRNA synthetase from Bacillus stearothermophilus》
- **博士导师**：Brian S. Hartley（★ 页面 infobox 实载；frontmatter 的 Alan Fersht 与 infobox 冲突，以 infobox 为准，见 §5）
- **博士后**：Imperial College London 一期、剑桥大学遗传学研究所（Institute of Genetics）一期
- **研究领域**：生物化学——蛋白质/核酸测序、抗体工程（人源化与全人抗体）、噬菌体展示
- **任职**：研究生涯几乎全部在 MRC Laboratory of Molecular Biology（LMB）与 MRC Centre for Protein Engineering（CPE）：1981 年起任 LMB 课题组组长；1994–2006 任蛋白质与核酸化学部主任；2006–2011 任 LMB 副主任（2007–2008 代理主任）；1990–2010（CPE 2010 并入 LMB）任 CPE 副主任；2012-10-02 至 2019 任 Trinity College, Cambridge 院长（Master）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **莱斯特起步（1951）**：生于英格兰莱斯特，Royal Grammar School 接受教育，1973 年剑桥 Trinity College 自然科学毕业。
2. **测序出身（1977）**：博士课题是嗜热脂肪芽孢杆菌色氨酰 tRNA 合成酶的氨基酸序列测定——经典的蛋白质测序训练，与 LMB 测序传统一脉相承。
3. **重返 LMB（1981）**：博士后（Imperial College、剑桥遗传学研究所）后回到 LMB 任课题组组长，继续深耕蛋白质与核酸测序。
4. **抗体之谜（1980s）**：关注"所有抗体共享同一基本结构、仅微小变化决定特异性"这一思想—— targeting 特异性与恒定骨架可分离。
5. **前驱工作（1984）**：Köhler 与 Milstein 因在 LMB 发现单克隆抗体技术获 1984 诺贝尔奖——但鼠源单抗会被人体免疫系统迅速灭活，临床应用受限。
6. **人源化（1986）**：开创"人源化"鼠单抗技术——把鼠抗体的互补决定区移植到人抗体骨架上，规避抗鼠免疫反应。
7. **Campath-1H**：人源化技术用于 LMB 与剑桥科学家开发的 Campath-1H（alemtuzumab），最终获批用于多发性硬化与慢性淋巴细胞白血病。
8. **噬菌体展示（1990s）**：用噬菌体展示技术把抗体**完全人源化**——在噬菌体文库中体外筛选全人抗体，绕过免疫动物。
9. **创立 CAT（1989）**：创立 Cambridge Antibody Technology，抗体工程领域最早的生物技术公司之一；其发现的 D2E7 经 Abbott 开发为 HUMIRA（adalimumab，抗 TNF alpha）——世界首个全人抗体药物，2017 年销售额超 180 亿美元，成为全球最畅销药物。
10. **CAT 易主（2006）**：Cambridge Antibody Technology 被 AstraZeneca 以 7.02 亿英镑收购；人源化单抗构成今天上市抗体药物的多数，包括 Keytruda（pembrolizumab）等重磅药。
11. **Domantis 与 Bicycle（2000–）**：2000 年创立 Domantis 主攻结构域抗体（只用抗体的活性片段），2006 年 12 月被 GlaxoSmithKline 以 2.3 亿英镑收购；再创 Bicycle Therapeutics 开发共价疏水核小蛋白模拟物。
12. **2018 诺贝尔化学奖**：2018-10-03 与 George P. Smith 共享一半（表彰抗体噬菌体展示工作），Frances Arnold 以酶的定向进化获另一半；诺奖演讲《Harnessing Evolution to Make Medicines》（2018-12-08）。
13. **荣誉满载**：FRS（1990）、CBE（1997）、Knight Bachelor（2004）、Royal Medal（2011，表彰蛋白质工程与治疗性单抗的开创性工作及发明家/企业家贡献）、Copley Medal（2024）；Trinity College 院长（2012–2019）。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深砖红 brickred） | `#9E2B25` | 沉稳学术红——LMB 传统与临床转化的厚重（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（人源化 badgeHum） | `#1E5631` | 绿——1986 人源化 / Campath-1H |
| 分类色 2（噬菌体展示 badgePhage） | `#16324F` | 藏青——噬菌体文库 / 全人抗体 |
| 分类色 3（产业转化 badgeBio） | `#B26A00` | 琥珀——CAT / Domantis / Bicycle |
| 分类色 4（荣誉 badgeHonor） | `#5B2A86` | 紫——FRS / Royal Medal / Copley |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「抗体文库中被筛选的离散克隆」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Ascension** — Cold Cinema（文件 `music_audio/inspiring-electronic/20-gYUC-sXt_8M-...Ascension.wav`，不要复制 wav）
- **风格**：科幻感弦乐推进 / 上升 / 史诗
- **匹配理由**：
  - "Ascension（上升）"匹配温特的阶梯式跃迁——测序 → 人源化 → 全人抗体 → 亿级市场；
  - 弦乐的层叠推进匹配噬菌体文库中逐轮筛选富集的意象；
  - 尾段的释然感匹配 "从 LMB 实验室到病床边的漫长一跃"。
- **时长**：以曲目实际时长为准，ffmpeg `-shortest` 自动对齐 15 页 ≈ 105 秒。

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 使抗体成为药物的工程师 / Greg Winter 1951– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/出生地/教育/博士导师/领域/荣誉）
03  温特的一生 — 高斯式时间线（10 节点：1951→1973→1977→1981→1986→1989→2000→2012→2018→2024）
04  测序出身 (1951–1981) — 表格「时间|事件|结果」（RGS→Trinity→Hartley 博士→LMB 组长）
05  单抗困境 (1984–1986) — 表格「问题|方法|结果」+ 公式框：鼠抗体 → 人源化抗体（CDR 移植）
06  Campath-1H (1980s–) — 表格「挑战|合作|结果」（多发性硬化 / CLL 获批）
07  噬菌体展示与全人抗体 (1990s) — 表格「问题|方法|结果」+ 公式框：噬菌体文库筛选循环
08  HUMIRA 奇迹 (1989–2006) — 表格「公司|药物|结果」（CAT→D2E7→Abbott→$18B/2017）
09  连续创业者 (2000–) — 表格「公司|方向|结果」（Domantis £230M→GSK；Bicycle Therapeutics）
10  治疗抗体的版图 — 四分类遗产盒（人源化单抗 / 全人单抗 / Keytruda 等重磅药 / 产业生态）
11  荣誉与治理 — 高斯式「类别|代表|意义」表格（FRS 1990 / Royal Medal 2011 / Copley 2024 / Trinity Master 2012–2019）
12  2018 诺贝尔化学奖 — 共享结构图解：Smith+Winter（一半，噬菌体展示）× Arnold（另一半，定向进化）
13  遗产：进化为人所用 — 表格「理念|实践|意义」+ 公式框：诺奖演讲标题 Harnessing Evolution to Make Medicines
14  结尾 — 「让进化为药物工作。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 博士导师冲突 | infobox 与正文均作 **Brian S. Hartley**（1977 论文 supervised by）；frontmatter `doctoral_advisor` 写 Alan Fersht 系噪声——**以 infobox 为准**，Fersht 不入库 |
| 2018 共享结构 | Winter 与 **George P. Smith 共享一半**（噬菌体展示），Frances Arnold 获**另一半**（酶的定向进化）——勿写"三人平分"或"三人因同一工作获奖" |
| 获奖理由口径 | 本地 page.md 仅载转述口径 "for his work on phage displays for antibodies"；官方引文原句（phage display of peptides and antibodies）**页面无载**——Beamer 用页面转述口径并标注，勿杜撰官方英文原句 |
| 人源化年份 | 人源化技术 **1986**（正文 "credited with the invention of techniques to both humanize (1986) and, later, to fully humanize using phage display"）——勿写成同一年发明两者 |
| 单抗先驱归属 | 单克隆抗体技术是 **Köhler 与 Milstein**（1984 诺奖，LMB）；温特的角色是**人源化与全人化**——勿把单抗发明记在温特名下 |
| HUMIRA 归属 | HUMIRA 由 **CAT 发现（D2E7）、Abbott 开发上市**；"world's first fully human antibody" 是页面明载口径；$18 billion 是 **2017 年销售额** |
| CAT 收购价 | AstraZeneca 2006 年以 **£702m** 收购 CAT；GSK 2006 年 12 月以 **£230 million** 收购 Domantis——两个数字勿混 |
| Master 任期 | 2012-10-02 就任 Trinity College Master，至 **2019**；勿写至今 |
| Copley 年份 | **2024**；Royal Medal **2011**；Knight Bachelor **2004**、CBE **1997**——年份勿错位 |
| 在世口径 | 1951-04-14 生，在世——卒日/享年一律留白，勿杜撰 |
| 引语红线 | 本地 page.md 无直接引语——全文不得出现引号内"原话"，诺奖演讲标题 *Harnessing Evolution to Make Medicines* 是外部链接条目所载标题，只作页面标题引用不作引语 |
| metadata-only 禁入 | frontmatter `educated_at` 的 Royal Grammar School、awards 列表中的 Scheele Award (1994)/King Faisal (1995)/William B. Coley (1999) 等正文有载可写；但 frontmatter 无正文对应的荣誉（如 Princess of Asturias、Gairdner、Wilhelm Exner 2015 有正文载）需逐条核对——**仅写正文或 infobox 明载者** |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q1545000 | ✅ |
| name_zh | 格雷格·温特 | ✅ |
| name_en | Greg Winter | ✅（页面标题规范名；清单 db_id 为空） |
| birth_date | 1951-04-14 | ✅ |
| death_date | （空，在世） | ✅ |
| nationality | United Kingdom | ✅ |
| primary_occupation | molecular biologist | ✅ |
| field_of_work | biochemistry（person_field 细分：biochemistry / antibody engineering / protein engineering / molecular biology，带 rank） | ✅ |
| has_biography | false（Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**★红线：只收 page.md 正文或 infobox 明载的关系；metadata-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Brian S. Hartley | 师→生（博士导师） | 1977 剑桥/LMB 博士，色氨酰 tRNA 合成酶测序 |
| co-honored | George P. Smith | 无向 | 2018 诺贝尔化学奖共同得主（共享一半，噬菌体展示） |
| co-honored | Frances Arnold | 无向 | 2018 诺贝尔化学奖共同得主（获另一半，定向进化） |

> Köhler 与 Milstein 是页面叙事中的技术先驱（1984 诺奖），但与温特**无明载直接关系**（师承/同事均无载）——**不予入库**。Campath/HUMIRA 相关企业人物、Trinity 前后任（Martin Rees、Sally Davies）均非个人合作关系——不予入库。对手方规范名 "George P. Smith"、"Frances Arnold" 与 batch-09 互指一致（防分裂 stub）。

## 8. 奖项清单

- Nobel Prize in Chemistry（2018，与 George P. Smith 共享一半；Frances Arnold 获另一半）
- Colworth Medal（1986）；EMBO Member（1987）
- Louis-Jeantet Prize for Medicine（1989）
- Scheele Award（1994）；King Faisal International Prize for Medicine — Molecular Immunology（1995）
- William B. Coley Award，Cancer Research Institute（1999）
- CBE（1997）；Knight Bachelor（2004）
- FRS（1990）；FMedSci；EMBO
- Royal Medal（2011，"for his pioneering work in protein engineering and therapeutic monoclonal antibodies, and his contributions as an inventor and entrepreneur"——页面明载引文）
- Wilhelm Exner Medal（2015）；Prince Mahidol Award（2016）
- Copley Medal（2024）；Golden Plate Award，American Academy of Achievement（2025）
- The Times 'Science Power List'（2020）

## 9. 机构清单

- 教育：Royal Grammar School, Newcastle upon Tyne；Trinity College, Cambridge（MA 1973、PhD 1977）
- 博士后：Imperial College London；University of Cambridge Institute of Genetics
- 任职：MRC Laboratory of Molecular Biology（1981 课题组组长；1994–2006 蛋白质与核酸化学部主任；2006–2011 副主任，2007–2008 代理主任）；MRC Centre for Protein Engineering 副主任（1990–2010 并入 LMB）
- 治理：Master of Trinity College, Cambridge（2012-10-02–2019）
- 创业：Cambridge Antibody Technology（1989 联合创办，2006 被 AstraZeneca £702m 收购）；Domantis（2000 创办，2006-12 被 GSK £230m 收购）；Bicycle Therapeutics（创办）；Covagen 科学顾问委员会、Biosceptre SAB 主席

## 10. 终审清单

- [x] 生卒 1951-04-14 / 在世留白；出生地 Leicester
- [x] 博士导师 Brian S. Hartley（infobox 口径；frontmatter Alan Fersht 不采用）
- [x] 2018 共享结构：Smith+Winter 一半 / Arnold 另一半；获奖理由用页面转述口径并标注
- [x] 人源化 1986、全人化经噬菌体展示（later）；单抗发明归 Köhler/Milstein
- [x] CAT £702m（AstraZeneca）/ Domantis £230m（GSK）/ HUMIRA 2017 销售额 $18B 数字各归其位
- [x] Royal Medal 2011 引文为页面明载；全文无杜撰引语
- [x] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Greg_Winter/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：优先本地 `images.txt` 中的 2018 斯德哥尔摩诺奖记者会照；404 则装饰圆占位
- [ ] 国籍：封面顶部明示英国
- [ ] 引语核对：全文不得出现无法溯源的引号原话（Royal Medal 引文除外，页面明载）
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 Sanger 及 21 世纪批次既有格式对齐
