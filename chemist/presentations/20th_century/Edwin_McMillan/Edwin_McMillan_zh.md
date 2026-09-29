# Edwin McMillan（埃德温·麦克米伦）立传提示词

> qid=Q19009 · 1907-09-18 – 1991-09-07 · 美国物理学家 · 20 世纪 · 诺贝尔化学奖（1951，与 Glenn T. Seaborg 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Edwin_McMillan/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 时间线页 + 表格语义化 tabularx + 金色公式展示框 + 气泡背景，是本次撰写的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（候选肖像：`Mcmillan-edwin_m.jpg` 洛斯阿拉莫斯徽章照，或 1951 年与 Lawrence 合影 `HD.1A.009_...jpg` 裁左——McMillan 在左侧）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{atom}\enspace 第一个超铀元素的发现者\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士导师、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「元素周期表向未知延伸」的母题——离散圆点暗示 93 号、94 号元素在周期表末尾的逐一点亮。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）——镎的生成链 `²³⁸U + n → ²³⁹U →(β⁻, 23 min) ²³⁹Np →(β⁻, 2.355 d) ²³⁹Pu` 是全篇视觉锚点（page.md 明载此反应链）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Edwin Mattison McMillan（中文惯称：埃德温·麦克米伦）
- **生卒**：1907-09-18 生于加州 Redondo Beach → 1991-09-07 逝于加州 El Cerrito 自宅，享年 83（⚠️ frontmatter 死亡日期另有噪声值 `1991-00-00`，以正文 09-07 为准）
- **国籍**：United States（美国）
- **身份**：物理学家（physicist）、大学教授（university teacher）——**物理学家获诺贝尔化学奖**
- **家庭**：父 Edwin Harbaugh McMillan 为医生（其双胞胎叔叔及母亲三位兄弟亦为医生），母 Anna Marie née Mattison；妹 Catherine Helen——其子 **John Clauser 是 McMillan 的外甥，2022 年诺贝尔物理学奖得主**（叙事可用，关系不入库）
- **婚姻**：1941-06-07 于 New Haven 娶 Elsie Walford Blumer（耶鲁医学院荣休院长 George Blumer 之女；其妹 Mary 是 Lawrence 的妻子）；三子女 Ann Bradford、David Mattison、Stephen Walker
- **教育轨迹**：Pasadena 多所中小学（1913–1924 毕业于 Pasadena High School）→ Caltech（1924 入学，家仅一英里；BS 1928、MS 1929；本科曾与 Linus Pauling 合作研究项目）→ Princeton（PhD 1933，正式接受日期 1933-01-12）
- **导师**：Edward Condon（博士导师）
- **博士论文**：*Deflection of a Beam of HCl Molecules in a Non-Homogeneous Electric Field*（1933）
- **研究领域**：超铀元素化学、核化学、加速器物理（回旋加速器/同步加速器）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **医生世家（1907）**：生于加州 Redondo Beach，1908 年迁 Pasadena——父辈两代行医，他却走向了物理。
2. **家门口的 Caltech（1924–1929）**：家离 Caltech 仅一英里；BS（1928）、MS（1929）；本科研究项目与 Linus Pauling 合作。
3. **普林斯顿博士（1933）**：师从 Edward Condon，论文为 HCl 分子束在非均匀电场中的偏转——分子束实验练出的仪器功夫受用终身。
4. **NRC 博士后与伯克利（1932–1935）**：国家研究委员会奖学金入伯克利辐射实验室（Lawrence 1931 年创建）；最初想测质子磁矩，被 Otto Stern 与 Immanuel Estermann 抢先——转身投入回旋加速器事业。
5. **仪器大师（1935–1941）**：1935 任讲师，贡献 "shimming" 磁场匀场技术；与 M. Stanley Livingston 发现**氧-15**（正电子发射体）；1936 助理教授、1941 副教授；1940 与 Samuel Ruben 发现**铍-10**（半衰期约 139 万年）。
6. **镎的发现·起点（1939–1940）**：Hahn/Strassmann 1939 年发现核裂变后，McMillan 用 37 英寸回旋加速器中子轰击铀——除裂变产物外得到 23 分钟（铀-239）与 2.3 天两个放射性同位素；他判断后者是 93 号元素。
7. **与 Segrè 的「失败」（1939）**：与锝发现者 Emilio Segrè 合作，按「93 号元素类似铼」的旧理论检验，误判为稀土样裂变产物——论文标题即《An Unsuccessful Search for Transuranium Elements》；McMillan 复盘后用还原剂条件下的 HF 反应确证非稀土。
8. **与 Abelson 确证（1940-05）**：Carnegie 研究所的 Philip Abelson 到访伯克利合作——2.3 天同位素化学性质不像任何已知元素而近于铀；1940-05-27 在《Physical Review》发表《Radioactive Element 93》；随即命名 **neptunium**（铀以天王星得名，海王星紧随其后）。
9. **战时转身（1940–1942）**：镎发现后旋即奔赴战争工作——MIT 辐射实验室微波雷达（1941 与 Alvarez、Dowding 同机验证探测潜望镜）→ 海军声纳实验室（polyscope 未成，但潜艇声纳训练装置获专利）——**正因他离场，Seaborg 才接手发现了钚**。
10. **曼哈顿计划（1942–1945）**：1942-09 受 Oppenheimer 招募；11 月同赴新墨西哥选址，与 Oppenheimer、John H. Manley 共拟洛斯阿拉莫斯技术楼规格；招募 Feynman、Robert R. Wilson 等人；任枪法武器副主任（Parsons 之下）——Thin Man 因钚-240 自发裂变被弃，改型 Little Boy（铀-235）；兼内爆测量 G-3 组组长；1945-07-16 在场见证 Trinity 核试验。
11. **同步加速器（1945）**：战后提出「相位稳定性原理」与同步加速器设计——Veksler 1944 年已独立发表同一原理；两人通信结谊，1963 年共享 **Atoms for Peace Award**；1946 升正教授；1947 申请、1952 获 synchrocyclotron 专利。
12. **实验室掌门（1954–1973）**：1954 副所长、1958 副所长转正——Lawrence 去世后继任所长直至 1973 退休；1970 实验室分立后任 Lawrence Berkeley Laboratory 所长；1968–1971 任美国国家科学院主席（1947 当选院士）。
13. **迟来的化学诺奖（1951）与晚年**：1951 与 Glenn Seaborg 共享诺贝尔化学奖（超铀元素化学）；1990 获国家科学奖章；1984 首次中风，1991-09-07 因糖尿病并发症逝于 El Cerrito 自宅；诺金奖章藏于美国国家历史博物馆（Smithsonian）。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深墨绿 deepverdant） | `#2F5D50` | 超铀元素于周期表尽头生长的沉稳之绿（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（超铀元素 badgeNp） | `#2E5A9E` | 蓝镎与锕系 / 93 号元素 |
| 分类色 2（加速器物理 badgeAcc） | `#D97B29` | 琥珀同步加速器 / 相位稳定性 |
| 分类色 3（曼哈顿计划 badgeMP） | `#5C3A21` | 褐洛斯阿拉莫斯 / 枪法与内爆 |
| 分类色 4（伯克利 badgeBerkeley） | `#8A2A4A` | 玫瑰辐射实验室 / Lawrence 师门 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「周期表向未知延伸」——圆点像逐一点亮的新元素格位。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Nostalgy** — AShamaluevMusic（文件：`music_audio/inspiring-electronic/17-_DA0mdtL-jI-Nostalgy - by AShamaluevMusic ｜ Sad Cinematic Music For Videos, Documentaries & Films.wav`；**不要复制 wav 文件**）
- **风格**：怀旧 / 忧伤 / 纪录片
- **匹配理由**：
  - "怀旧" 匹配其人生弧线——从家门口的 Caltech 少年到曼哈顿计划的枪法掌门，时代在身后翻页
  - "纪录片" 匹配叙事密度——发现镎、离场战时、洛斯阿拉莫斯、同步加速器、执掌伯克利，五个时代段落
  - "忧伤" 匹配尾声——晚年中风、糖尿病并发症中逝去，安静谢幕
- **时长**：以文件实际时长为准（须 > 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐）

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 第一个超铀元素的发现者 / Edwin McMillan 1907–1991 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/出生地/去世地/教育/博士导师/领域/荣誉）
03  麦克米伦的一生 — Sanger 式时间线（10 节点：1907→1924→1933→1935→1940→1942→1945→1951→1958→1991）
04  医生世家与 Caltech (1907–1929) — 表格「时间|事件|结果」
05  普林斯顿与伯克利 (1930–1939) — 表格「阶段|机构|产出」（Condon 博士 / NRC / shimming / 氧-15 / 铍-10）
06  镎的发现 (1939–1940) — 表格「问题|方法|结果」+ 公式框：²³⁸U(n,β⁻)²³⁹Np(β⁻)²³⁹Pu 反应链
07  与 Segrè 的失败与 Abelson 的确证 — 表格「回合|结论|意义」（Unsuccessful Search → Radioactive Element 93）
08  战时：雷达、声纳与洛斯阿拉莫斯 (1940–1945) — 表格「阶段|任务|结果」
09  同步加速器 (1945–1952) — 表格「原理|设计|结果」+ 公式框：相位稳定性原理 · Veksler 并行 · Atoms for Peace 1963
10  1951 诺贝尔化学奖 — 表格「理由|口径|意义」（与 Seaborg 共享，超铀元素化学）
11  掌门岁月与荣誉 (1954–1991) — Sanger 式「类别|代表|意义」表格（NAS 主席 1968–71 / 国家科学奖章 1990）
12  外甥 John Clauser — 表格「人物|关系|结果」（妹妹 Catherine Helen 之子；2022 物理诺奖——一门两代诺奖）
13  遗产：从 93 号到锕系时代 — 四分类遗产盒 + 公式框：镎-钚接力 → 锕系系列分类（1945，Abelson 合作成果延伸）
14  结尾 — 「周期表没有终点，他只是替它翻开了下一页。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 获奖理由口径 | page.md 实载 "for their discoveries in the chemistry of the transuranium elements"；⚠️ Seaborg 页面同项多 "first" 一词（"chemistry of the first transuranium elements"）——**两篇各忠于本人页面**，勿互改；官方口径以诺贝尔官网为准 |
| 物理学家获化学奖 | McMillan 是 physicist（infobox occupation），因超铀元素**化学**获 1951 化学奖——勿改称化学家 |
| 镎 vs 钚 | 镎（93 号）归 McMillan（与 Abelson 确证）；钚（94 号）是 Seaborg 接力发现——勿混 |
| 先错后对 | 与 Segrè 的 1939 论文标题《An Unsuccessful Search for Transuranium Elements》——如实写「先误判后纠正」的曲折，勿隐去 |
| 同步加速器 | Veksler **1944 年已独立发表**同一原理，McMillan 1945 独立提出——勿写 McMillan「首创/独占」；1963 两人共享 Atoms for Peace Award |
| 死亡日期 | 1991-09-07（frontmatter 有 `1991-00-00` 噪声值，以正文为准）；死因糖尿病并发症；卒地 El Cerrito 自宅 |
| 家族关系 | 外甥 John Clauser（2022 物理诺奖）是 page.md 明载事实，可入叙事——**但亲属关系不入库（见 §7）** |
| 招募人员 | 「招募 Feynman、Robert R. Wilson」是正文明载——属组织工作叙述，不作为入库关系（见 §7） |
| Thin Man | 因钚-240 自发裂变（Segrè 组检测）被弃，枪法仅用于铀-235（Little Boy）——因果链如实，勿写「他设计了 Little Boy 的全部」 |
| 引语 | page.md **无 McMillan 直接引语**——中文引号内禁编造「原话」；可用的只有文献标题与奖项名称 |
| 肖像 | `Mcmillan-edwin_m.jpg`（徽章照）或 `HD.1A.009`（与 Lawrence 合影，McMillan 在左，裁左）——须核对图注 |
| 日期噪声 | frontmatter 生卒均含 `*-00-00` 噪声第二值——一律取正文 1907-09-18 / 1991-09-07 |
| 同名区分 | 库内另有 Brockway McMillan / Kenneth L. McMillan / William L. McMillan——本篇只用 `Edwin McMillan`（库内 #2387 既有形式） |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q19009 | ✅（复用库内 #2387 stub 回填） |
| name_zh | 埃德温·麦克米伦 | ✅ |
| name_en | Edwin McMillan | ✅（库内既有精确形式） |
| birth_date | 1907-09-18 | ✅ |
| death_date | 1991-09-07 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | physicist | ✅ |
| field_of_work | chemistry（person_field 细分：transuranium elements / nuclear chemistry / accelerator physics / nuclear physics，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 共同得主 / 合作者**（★红线：只收 page.md 正文或 infobox 明载的关系）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Edward Condon | 师→生（博士导师） | 1933 普林斯顿博士（HCl 分子束电场偏转）；库内 #2297 |
| co-honored | Glenn T. Seaborg | 无向 | 1951 诺贝尔化学奖共同得主（超铀元素化学）；库内 #2396 |
| co-honored | Vladimir Veksler | 无向 | 1963 Atoms for Peace Award 共同得主（同步加速器原理各自独立提出） |
| colleague | Philip Abelson | 无向 | 1940 合作确证 93 号元素，合著《Radioactive Element 93》（Physical Review 1940-05-27） |
| colleague | Emilio Segrè | 无向 | 1939 合作「失败」检索、1941 起在钚可裂性上再续合作 |
| colleague | M. Stanley Livingston | 无向 | 共同发现氧-15；库内 #2388 |
| colleague | Samuel Ruben | 无向 | 1940 共同发现铍-10（半衰期约 139 万年）；库内 #2398 |
| colleague | Ernest Lawrence | 无向 | 1932 年加入其创建的伯克利辐射实验室；1958 年 Lawrence 去世后继任所长；库内 #1951 |
| colleague | J. Robert Oppenheimer | 无向 | 1942 受其招募加入曼哈顿计划，同赴新墨西哥选址、共拟洛斯阿拉莫斯规格；库内 #355 |
| spouse | Elsie Walford Blumer | 配偶 | 1941-06-07 结婚，育三子女 |

> **禁入库名单**（page.md 明载但判定为噪声/非入库关系）：John Clauser（外甥，亲属关系不入库）；Richard Feynman、Robert R. Wilson（仅「招募人员」叙述，非合作研究关系）；Otto Stern、Immanuel Estermann（仅质子磁矩测量争先，无实质关系）；Melba Phillips（Oppenheimer–Phillips 过程解释者，间接）；William S. Parsons、George Kistiakowsky、Seth Neddermeyer（曼哈顿计划组织关系，非研究合作）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1951，与 Glenn Seaborg 共享）
- Atoms for Peace Award（1963，与 Vladimir Veksler 共享）
- Golden Plate Award（1964，American Academy of Achievement）
- National Medal of Science（1990）
- Member of the National Academy of Sciences（1947；主席 1968–1971）
- American Philosophical Society（1952）；American Academy of Arts and Sciences（1962）
- Fellow of the American Physical Society（infobox）；声纳训练装置专利等 9 项美国专利（1946–1960）

## 9. 机构清单

- 教育：Pasadena High School（1924 毕业）；California Institute of Technology（BS 1928、MS 1929）；Princeton University（PhD 1933）
- 任职：Berkeley Radiation Laboratory（1932/33 加入；1935 讲师、1936 助理教授、1941 副教授、1946 正教授）；MIT Radiation Laboratory（1940–1941 雷达）；Navy Radio and Sound Laboratory（1941 声纳）；Los Alamos Laboratory（1942–1945 曼哈顿计划）；Radiation Laboratory 副所长（1954）→ 所长（1958–1973；1970 后任 Lawrence Berkeley Laboratory 所长）；1974–75 CERN 访问（g-2 μ 子磁矩实验）

## 10. 终审清单

- [ ] 生卒 1907-09-18 / 1991-09-07，享年 83，出生地 Redondo Beach、去世地 El Cerrito
- [ ] 1951 与 Seaborg 共享表述准确；获奖理由两页口径差异已注记
- [ ] 镎（McMillan+Abelson）与钚（Seaborg）归属未混；「先错后对」曲折如实
- [ ] 同步加速器 Veksler 并行发明表述准确；Atoms for Peace 1963 共享
- [ ] 外甥 Clauser 入叙事不入库；引语零编造
- [ ] 引用全部可在本地 page.md 原文溯源；中文引号内无编造原话
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误、溢出达标

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 page.md 逐页对照 Beamer tex 全部事实
- [ ] 头像：核对所选肖像图注（徽章照 or 与 Lawrence 合影裁左）
- [ ] 国籍：封面顶部明示美国
- [ ] 引语核对：无直接引语，检查无编造引号内容
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一；反应链公式框排版检查
- [ ] 与化学家侧既有格式（Sanger 黄金骨架）对齐

---

> **名单状态**：由 chem-batch-09 执行；`chemist/generate_20th_century_list.py` 由主控统一收尾，本篇不改动。
