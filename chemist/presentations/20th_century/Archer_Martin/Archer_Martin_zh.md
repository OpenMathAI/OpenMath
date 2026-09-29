# Archer Martin（阿彻·约翰·波特·马丁）立传提示词

> qid=Q48977 · 1910-03-01 – 2002-07-28 · 英国化学家 · 20 世纪 · 诺贝尔化学奖（1952，与 Richard Laurence Millington Synge 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Archer_Martin/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 时间线页 + 表格语义化 tabularx + 金色公式展示框 + 气泡背景，是本次撰写的核心版式语言。
> ⚠️ 数据源提示：本页 page.md 较短（infobox + 四个小节），**一切以实载为准，页面无载的事实一律禁写**（尤其教育细节、博士信息、发表年表）。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。⚠️ 本地 images.txt 为空、page.md 无肖像图——**用装饰圆占位**，图注写「肖像暂缺·装饰占位」。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{vial}\enspace 色谱法的发明者\enspace·\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧装饰圆 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育（Bedford School / Peterhouse）、配偶、核心领域、荣誉。**本页无博士导师字段——信息网格不设师承项**。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「色谱分离」母题——大小错落的圆点像固定相上渐次展开的色带。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）——分配色谱原理（分配系数 K 与两相中的浓度比）与 Rf 值示意是全篇视觉锚点。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Archer John Porter Martin（中文惯称：阿彻·约翰·波特·马丁；CBE FRS）
- **生卒**：1910-03-01 生于伦敦 → 2002-07-28 逝于英格兰赫里福德郡 Llangarron，享年 92
- **国籍**：United Kingdom（英国；英格兰）
- **身份**：化学家 / 生物化学家（biochemist, chemist, university teacher）——分配色谱法发明人
- **家庭**：父为全科医生（GP）；1943 年娶 Judith Bagenal（1918–2006），育二子三女；晚年患阿尔茨海默病
- **教育轨迹**：Bedford School → Peterhouse, Cambridge（⚠️ page.md 无载本科专业细节、无博士/导师信息——一律禁写）
- **导师**：**页面无载**——禁写
- **研究领域**：生物化学（biochemistry）——维生素 E 与 B2 的部分方面、分配色谱、纸色谱、气液色谱

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **伦敦医生之子（1910）**：生于伦敦，父亲是全科医生——与同时代多数化学家一样，家庭的实用主义底色早早养成。
2. **Bedford 到 Peterhouse**：先后就读 Bedford School 与剑桥 Peterhouse——英式古典教育与科学训练的交汇。
3. **早年科研轨迹**：先在物理化学实验室工作，后转入 Dunn Nutritional Laboratory（ Dunn 营养实验室）——从物化转向生化的第一站。
4. **利兹岁月（1938）**：1938 年转入利兹的 Wool Industries Research Institution（羊毛工业研究机构）——在这里遇见 Synge，也在这里孕育了分配色谱法。
5. **分离氨基酸的难题**：他在分离氨基酸的工作中发展出**分配色谱法**（partition chromatography）——让混合物在两液相间按分配系数各行其道。
6. **Boots 与 MRC（1946–1952）**：1946–1948 任 Boots Pure Drug Company 生化部主任；1948 加入医学研究委员会（MRC）；1952 年出任国立医学研究所（NIMR）物理化学部主任，1956–1959 任化学顾问。
7. **纸色谱**：Known for 三项之一——与分配色谱同源的纸上分离技术，让生化实验室人人可用。
8. **气液色谱（1954）**：与 Anthony T. James 合作发表 "Gas-Liquid Chromatography: A Technique for the Analysis and Identification of Volatile Materials"——挥发性物质分析从此改观；实验在 Mill Hill 的 NIMR 完成。
9. **第九篇论文的奇迹**：一生仅发表约 70 篇论文——远少于典型诺奖得主；但**第九篇论文**就包含了最终赢得诺贝尔奖的工作。
10. **1950 FRS**：当选皇家学会会士（FRS）——诺奖两年之前。
11. **1952 诺贝尔化学奖**：与 Richard Laurence Millington Synge 共享，获奖理由为**分配色谱法的发明**——一项「方法学」诺奖：他们没有发现新物质，而是给了所有人更好的眼睛。
12. **Citation for Chemical Breakthrough（2016）**：1954 年与 James 的气液色谱论文获美国化学会化学史分会「化学突破引文奖」，授予 Mill Hill 旧址（2016 年起为 Francis Crick Institute）。
13. **大器不晚，晚景淡然**：1959 John Price Wetherill Medal、1960 CBE、1963 皇家学会 Leverhulme Medal；自 Sussex 大学退休后任休斯顿大学与洛桑联邦理工（EPFL）访问教授；休斯顿方面 1979 年（69 岁）以「发表不足」将其从化学系名单除名——他自己早已把最重要的论文写完了；2002-07-28 逝于 Llangarron。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深酒红 deepwine） | `#8A1E2D` | 色带在固定相上晕开的沉稳之红（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（分配色谱 badgePC） | `#2E5A9E` | 蓝分配系数 / 两相分离 |
| 分类色 2（气液色谱 badgeGC） | `#D97B29` | 琥珀气相色谱 / James 合作 |
| 分类色 3（生物化学 badgeBio） | `#1B7A43` | 绿氨基酸 / 维生素 E·B2 |
| 分类色 4（晚年·访问教授 badgeLate） | `#6B4E9E` | 紫 Sussex / Houston / EPFL |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「色带展开」——色谱柱里渐次分离的组分。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Last Hope** — Victor Cooper（文件：`music_audio/inspiring-electronic/24-ie5iLcdKiqk-Victor Cooper - Last Hope (Dramatic Powerful Epic Copyright Free Music).wav`；**不要复制 wav 文件**）
- **风格**：戏剧性 / 有力量 / 史诗感
- **匹配理由**：
  - "Last Hope（最后的希望）" 匹配其方法论立场——当分离提纯是当时生化研究的瓶颈时，色谱法就是那根救命稻草
  - "戏剧性" 匹配叙事反差——70 篇论文的「低产者」凭第九篇论文摘得诺奖
  - "史诗感" 匹配技术遗产——分配色谱与气液色谱至今仍是分析化学的两大支柱
- **时长**：以文件实际时长为准（须 > 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐）

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 色谱法的发明者 / Archer Martin 1910–2002 + 四色 badge + 装饰圆 + 国籍行
02  身份信息页（★ 必做）— 左装饰圆 + 右 2×2 信息网格（生卒/本名/国籍/出生地/去世地/教育/配偶/领域/荣誉）
03  马丁的一生 — Sanger 式时间线（10 节点：1910→1938→1941→1943→1946→1948→1950→1952→1954→2002）
04  伦敦与剑桥 (1910–1938) — 表格「时间|事件|结果」
05  利兹：与 Synge 的相遇 (1938–1946) — 表格「问题|方法|结果」+ 公式框：分配系数 K = Cs/Cm
06  分配色谱法 — 表格「问题|方法|结果」+ 公式框：两相分配分离原理示意
07  诺奖（1952）— 表格「理由|口径|意义」（与 Synge 共享「发明分配色谱法」）
08  气液色谱 (1954) — 表格「合作者|技术|影响」+ 公式框：GLC 原理 · 2016 Citation for Chemical Breakthrough
09  纸色谱与生化应用 — 表格「对象|技术|结果」（氨基酸 / 维生素 E·B2 / 羊毛角蛋白——羊毛角蛋白项为 Synge 侧应用，仅作共同工作背景）
10  MRC 与 NIMR 岁月 (1948–1959) — 表格「机构|职务|年份」
11  荣誉与「低产」 — Sanger 式「类别|代表|意义」表格（Nobel 1952 / FRS 1950 / Wetherill 1959 / CBE 1960 / Leverhulme 1963）+ 70 篇论文与第九篇的对照
12  退休与访问教授 — 表格「机构|角色|结果」（Sussex / Houston / EPFL；1979 除名如实叙述）
13  遗产：给所有人更好的眼睛 — 四分类遗产盒 + 公式框：色谱家族谱系（分配→纸→气液→HPLC）
14  结尾 — 「他没有发现新物质，他给了化学一双新的眼睛。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 获奖理由 | page.md 口径 "shared the 1952 Nobel Prize in Chemistry for the invention of partition chromatography"（与 Synge 共享）——勿写「发明色谱法」泛称，勿写独享 |
| 博士/导师 | page.md **无载**博士信息与导师——禁写；身份信息页不设师承字段 |
| 出生地上矛盾 | infobox 无出生地细节，正文载 Born London——以正文「伦敦」为准 |
| 国籍口径 | frontmatter nationality 有 United Kingdom 与 United Kingdom of Great Britain and Ireland 双值（1910 年生）——yaml 取 United Kingdom；文中写「英格兰化学家（English chemist）」忠实原文 |
| 气液色谱年份 | 1954 年与 James 的论文是 page.md 明载口径——勿写成 1940s |
| 70 篇与第九篇 | "only 70 in all" / "his ninth paper contained the work that would eventually win him the Nobel Prize"——忠实原文，勿演绎成「一生只发了 70 篇就被除名」 |
| 1979 除名 | 休斯顿大学 69 岁时因发表不足将其除名——page.md 明载，如实叙述、不评论 |
| 配偶 | Judith Bagenal（1918–2006），1943 结婚，二子三女——勿把 Synge 的妻子 Ann 混入 |
| 引语 | page.md **无 Martin 直接引语**——中文引号内禁编造「原话」 |
| 肖像 | images.txt 为空——装饰圆占位，图注「肖像暂缺」 |
| 羊毛角蛋白 | "wool keratin" 应用是 Synge FRS 引用语中的表述——Martin 篇只写「分配色谱应用于蛋白质组成与结构问题」，不展开 |
| 同名区分 | 诺奖官方页 Archer J.P. Martin；本篇全篇用 Archer John Porter Martin / Archer Martin，勿与其他 Martin 混 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q48977 | ✅ |
| name_zh | 阿彻·约翰·波特·马丁 | ✅ |
| name_en | Archer Martin | ✅（frontmatter 名，与 Synge 篇对手方名一致，防分裂） |
| birth_date | 1910-03-01 | ✅ |
| death_date | 2002-07-28 | ✅ |
| nationality | United Kingdom | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry（person_field 细分：biochemistry / partition chromatography / gas-liquid chromatography / paper chromatography，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**共同得主 / 合作者 / 配偶**（★红线：只收 page.md 正文或 infobox 明载的关系）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Richard Laurence Millington Synge | 无向 | 1952 诺贝尔化学奖共同得主（发明分配色谱法） |
| colleague | Anthony T. James | 无向 | 合作发明气液色谱法，1954 年论文（2016 获 Citation for Chemical Breakthrough Award） |
| spouse | Judith Bagenal | 配偶 | 1943 年结婚，育二子三女 |

> **禁入库名单**：父亲（GP，亲属不入库）；page.md 无载导师/门生/博士信息；metadata.json 亦无额外可入关系——本篇无其他禁入项。

## 8. 奖项清单

- Nobel Prize in Chemistry（1952，与 Richard Synge 共享）
- Fellow of the Royal Society（1950）
- John Price Wetherill Medal（1959）
- Leverhulme Medal（1963，皇家学会）
- Commander of the Order of the British Empire，CBE（1960）
- John Scott Award（infobox award_received，年份页面无载——勿写具体年份）
- Citation for Chemical Breakthrough Award（2016，ACS 化学史分会授予 1954 GLC 论文/机构）

## 9. 机构清单

- 教育：Bedford School；Peterhouse, Cambridge
- 任职：Physical Chemistry Laboratory（早期）；Dunn Nutritional Laboratory；Wool Industries Research Institution, Leeds（1938–）；Boots Pure Drug Company 生化部主管（1946–1948）；Medical Research Council（1948–）；NIMR 物理化学部主任（1952）、化学顾问（1956–1959）；University of Sussex（退休前）；University of Houston 访问教授（1979 年被除名）；EPFL 访问教授

## 10. 终审清单

- [ ] 生卒 1910-03-01 / 2002-07-28，享年 92，出生地伦敦、去世地 Llangarron
- [ ] 1952 与 Synge 共享、理由「发明分配色谱法」表述准确
- [ ] 气液色谱 1954+James；纸色谱、分配色谱并列 Known for
- [ ] 无博士/导师信息杜撰；70 篇与第九篇论文口径忠实
- [ ] 1979 休斯顿除名如实叙述；引语零编造
- [ ] 引用全部可在本地 page.md 原文溯源；中文引号内无编造原话
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误、溢出达标

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 page.md 逐页对照 Beamer tex 全部事实（页面短，重点核对无外溢）
- [ ] 头像：确认装饰圆占位 + 图注「肖像暂缺」
- [ ] 国籍：封面顶部明示英国
- [ ] 引语核对：无直接引语，检查无编造引号内容
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（本页无师承字段，其余对齐）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 黄金骨架）对齐

---

> **名单状态**：由 chem-batch-09 执行；`chemist/generate_20th_century_list.py` 由主控统一收尾，本篇不改动。
