# Henry Taube（亨利·陶布）立传提示词

> qid=Q235983 · 1915-11-30 – 2005-11-16 · 加拿大裔美国化学家 · 20 世纪 · 诺贝尔化学奖（1983，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Henry_Taube/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + Sanger 式时间线 + 表格语义化 tabularx + 金色公式框 + 气泡背景。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像从 page.md 图注照片取；若下载失败用装饰圆占位并注记）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 电子转移反应的机制大师\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「电子桥 / 电子转移」母题——离散圆点暗示分子间传递电子的桥梁。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化（内界电子转移、Creutz–Taube 配合物 [[Ru(NH₃)₅]₂(C₄H₄N₂)]⁵⁺、配体取代速率与 d 电子组态关联）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Henry Taube（FRSC；中文惯称：亨利·陶布）
- **生卒**：1915-11-30 生于加拿大萨斯喀彻温省 Neudorf → 2005-11-16 逝于美国加州 Palo Alto 自宅，享年 89
- **国籍**：United States（加拿大出生；1942 年归化入籍美国）
- **身份**：化学家 / 大学教师（chemist, university teacher）；Stanford University 教授（1986 年起荣休）
- **家庭**：Neudorf 农家四兄弟中最幼；父母是 1911 年从乌克兰移民萨斯喀彻温的德裔农人，第一语言为低地德语（Low German）；1952 年娶妻子 Mary，育三子女 Karl（加州大学河滨分校人类学家）、Heinrich、Linda；继女 Marianna 1998 年因癌症去世；业余爱好园艺与古典音乐（尤其歌剧）
- **教育轨迹**：
  - 12 岁离家赴 Regina 入 Luther College 完成中学，毕业后留校任 Paul Liefeld 的实验室助手（得以修读大学一年级课程）
  - University of Saskatchewan：BSc 1935、MSc 1937（硕士论文导师 John Spinks；在校曾随 1971 年诺贝尔化学奖得主 Gerhard Herzberg 学习）
  - University of California, Berkeley：PhD 1940（论文 *The interaction of ozone and hydrogen peroxide*；博士导师 William C. Bray）
- **导师**：William C. Bray（博士）；John Spinks（硕士论文）
- **研究领域**：无机化学——氧化还原反应机制、内界电子转移（inner sphere electron transfer）、配位化学、同位素示踪

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **乌克兰德裔农家子（1915）**：萨斯喀彻温 Neudorf 农场，低地德语是母语；自述前 21 年农场生活教他「亲近自然、自律完成必要的工作」（page.md 实载引语）。
2. **Luther College 起步（约 1927–）**：12 岁离家求学，毕业后以实验室助理身份换取大学课程——与恩师 Paul Liefeld 的名字日后同列纪念奖学金。
3. **萨斯喀彻温大学（1935–1937）**：BSc/MSc；硕士论文导师 John Spinks；随 Gerhard Herzberg 学习。
4. **Berkeley 博士（1940）**：师从 William C. Bray，研究溶液中二氧化氯与过氧化氢的光分解。
5. **战时与早期教职（1941–1946）**：Berkeley 讲师 → Cornell 讲师与助理教授；二战期间服务于 National Defense Research Committee（NDRC）。
6. **Chicago 岁月（1946–1961）**：助理教授 → 正教授；1956–1959 任化学系主任（自述不喜欢行政）；被安排开设高等无机化学课程——因教科书资料匮乏而转向配位化学。
7. **1952 年 Chemical Reviews 关键论文**：首次揭示**配体取代速率与金属 d 电子组态的关联**；《Science》在其获诺奖后称此文为 "one of the true classics in inorganic chemistry"；论文构思于 1940 年代末学术休假。
8. **"化学桥"的洞见**：分子间电子转移经由一种"化学桥"（chemical bridge）而非此前以为的简单电子交换——解释了相似金属离子反应速率的差异；这正是**内界电子转移**机制。
9. **Ru 与 Os 的选择**：研究钌与锇——两者高背键合（back bonding）能力是研究分子间电子转移的关键。
10. **Creutz–Taube 配合物**：与研究生 Carol Creutz 共同成为 [[Ru(NH₃)₅]₂(C₄H₄N₂)]⁵⁺ 的命名来源——混合价态研究的标志性体系。
11. **Stanford 与 1983 诺贝尔化学奖（独享）**：1961 起执教 Stanford；官方理由 "for his work on the mechanisms of electron transfer reactions, especially in metal complexes"；诺奖演讲 "Electron Transfer between Metal Complexes – Retrospective"（1983-12-08 受奖，Ingvar Lindqvist 致辞）；获奖后笑谈副作用——学生上课更专心了。
12. **加拿大之子的双纪录**：第二位获诺贝尔奖的加拿大出生化学家（第一位 William Giauque），至今唯一出生于萨斯喀彻温省的诺奖得主；1997 年萨斯喀彻温大学建立 Taube 与 Herzberg 的诺贝尔桂冠广场。
13. **不倦的实验室老兵**：荣休后研究持续到 2001 年，此后仍每天到实验室直到 2005 年辞世；600 余篇论文、指导 250 余名学生；同行 Jim Collman 称其 "a scientist's scientist"（间接转述）。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深绿 forest green） | `#1E5631` | 配位场与金属配合物的沉稳（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（电子转移 badgeET） | `#2E5A9E` | 蓝内界电子转移 / 化学桥 |
| 分类色 2（配位化学 badgeCoord） | `#D97B29` | 琥珀配体取代 / d 电子组态 |
| 分类色 3（同位素示踪 badgeIsotope） | `#C0395B` | 玫瑰 O-18 与放射性氯示踪 |
| 分类色 4（教育与传承 badgeMentor） | `#1B7A43` | 绿 250 余名学生 / Creutz–Taube 配合物 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「电子桥 / 分子间传递」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Savage** — Alex-Productions（`music_audio/alex-productions/34-pILVwyuW3jw-Savage.wav`；执行 Beamer 时复制为本目录 `Savage.wav`，勿直接引用外部路径）
- **风格**：沉稳有力 / 前行感 / 大器晚成
- **匹配理由**：
  - "沉稳有力" 匹配其科研风格——600 余篇论文、68 年学术生涯的持续攻坚
  - "前行感" 匹配内界电子转移的意象——电子经由化学桥一步步传递
  - "大器晚成" 匹配其诺奖叙事——1952 年关键论文获奖时已 30 年，68 岁方得诺奖，得奖后仍每天进实验室直到人生终点
- **时长对齐**：ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 电子转移的机制大师 / Henry Taube 1915–2005 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/国籍/出生地/去世地/教育/博士/师承/领域/荣誉）
03  陶布的一生 — Sanger 式时间线（10 节点：1915→1935→1940→1946→1952→1961→1983→1986→2001→2005）
04  萨斯喀彻温农家子 (1915–1937) — 表格「时间|事件|结果」
05  Berkeley 与战时岁月 (1940–1946) — 表格「时间|事件|结果」
06  1952 关键论文 — 表格「问题|方法|结果」+ 公式框：配体取代速率 ∝ d 电子组态
07  内界电子转移：化学桥 — 表格「旧观念|新洞见|结果」+ 公式框：化学桥机制
08  1983 诺贝尔化学奖（独享） — 表格「主题|内容|意义」+ 官方理由公式框
09  Creutz–Taube 配合物 — 表格「对象|组成|意义」+ 公式框：[[Ru(NH₃)₅]₂(C₄H₄N₂)]⁵⁺
10  门生如林 — 表格「人物|方向|结果」（Friedman/Plane/Olson/Robson/Creutz/Ford）
11  荣誉清单 — Sanger 式「类别|代表|意义」表格（NMS 1976 / Priestley 1985 / FRS 1988 / 两度 Guggenheim）
12  Stanford 与萨斯喀彻温的纪念 — Sanger FFT 页式流程图（Stanford 讲席 → 1997 Nobel Laureate Plaza → Luther College 纪念奖学金）
13  遗产：无机化学的经典 — 四分类遗产盒 + 公式框：内界电子转移机制普适性
14  结尾 — 「电子不是跳过去的，是沿着桥走过去的。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1983 独享 | 诺贝尔化学奖 **独享**（无共同得主）——勿写共享 |
| 获奖理由 | "for his work on the mechanisms of electron transfer reactions, especially in metal complexes"——逐字对照 page.md；intro 段作 "in the mechanisms"（连字符异），以 Awards 段口径为准，勿混写 |
| 两个"第二" | 第二位加拿大出生化学诺奖得主（第一位 **William Giauque**）+ 至今唯一萨斯喀彻温出生诺奖得主——两个表述勿混淆或合并 |
| 国籍 | 加拿大出生、**1942 年归化入籍美国**；nationalities 写 United States（rank 0）+ Canada（rank 1）；勿写"美籍加拿大人"以外自创口径 |
| 双导师 | **Bray（博士，Berkeley 1940）+ Spinks（硕士论文，萨斯喀彻温）**——两行入库，note 注明 MSc；Herzberg 只是"随其学习"（studied with），用 influence 非 advisor-student |
| 内界机制 | 核心洞见是"化学桥"（chemical bridge）式的**中间步骤**——勿写成"电子直接交换被否定"以外的自行发挥；"inner sphere electron transfer" 是 infobox Known for 口径 |
| 1952 论文 | 发表于 **Chemical Reviews**、1940 年代末学术休假期间构思、诺奖时已 30 年——《Science》评语 "one of the true classics in inorganic chemistry" 可直引 |
| Creutz–Taube | 与研究生 **Carol Creutz** 共同命名；配合物式 [[Ru(NH₃)₅]₂(C₄H₄N₂)]⁵⁺——勿写错电荷与配体 |
| 学生规模 | "over 600 publications"、"over 250 students"（截至 1997 的表述）——勿写成"600 名学生" |
| 引语 | 可直引仅限：萨斯喀彻温前 21 年自述段、Collman 与 Gray 的英文评语、Taube 自述"primary flaw"（valence bond 视角局限）；**其余中文引号内容一律间接转述** |
| 妻子 | 1952 年娶 Mary（页面未载姓氏——勿编造）；子 Karl 为 UC Riverside 人类学家（page.md 明载）；继女 Marianna 1998 年去世 |
| 任职时间线 | Cornell –1946 → Chicago 1946–1961（系主任 1956–1959）→ Stanford 1961–1986 荣休、研究至 2001、每天到实验室至 2005——勿错置 |
| 同名区分 | Henry Taube 与 1992 诺奖得主 Rudolph A. Marcus（电子转移理论另一支）——See also 提及但非共同得主，勿写成共享 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q235983 | ✅ |
| name_zh | 亨利·陶布 | ✅ |
| name_en | Henry Taube | ✅ |
| birth_date | 1915-11-30 | ✅ |
| death_date | 2005-11-16 | ✅ |
| nationality | United States（rank 0，1942 归化）/ Canada（rank 1，出生） | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | inorganic chemistry（person_field 细分：inorganic chemistry / electron transfer / coordination chemistry / chemical kinetics，带 rank） | ✅ |
| has_biography | 0（立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 学生 / 家人**（只收 page.md 正文或 infobox 明载；metadata-only 一律不入库）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | William C. Bray | 师→生（博士导师） | Berkeley PhD 1940 |
| advisor-student | John Spinks | 师→生（硕士论文导师） | University of Saskatchewan MSc 1937 |
| advisor-student | Harold Friedman | Taube → 学生 | infobox Doctoral students |
| advisor-student | Robert A. Plane | Taube → 学生 | infobox Doctoral students |
| advisor-student | Maynard Olson | Taube → 学生 | infobox Doctoral students |
| advisor-student | Richard Robson | Taube → 学生 | infobox Other notable students |
| advisor-student | Carol Creutz | Taube → 学生 | 研究生；Creutz–Taube 配合物共同命名 |
| advisor-student | Peter Ford | Taube → 学生 | page.md 明载 former student |
| influence | Gerhard Herzberg | 影响 | 萨斯喀彻温大学随其学习；1971 诺贝尔化学奖得主 |
| spouse | Mary | 无向 | 1952 年结婚（页面未载姓氏） |

> **禁入库名单（metadata.json-only）**：doctoral_student 含 Thomas J. Meyer，正文 infobox 无——**不予入库**。Jim Collman 与 Harry Gray 仅系评语来源人物（colleagues remember 语段），非明载直接合作关系，不入库。Paul Liefeld 是中学阶段实验室雇主/恩师，关系类型超出白名单语境，不入库（在 §9 机构与时间线页呈现）。William Giauque 仅系"第一位加拿大出生化学诺奖得主"的并列叙述，非关系，不入库。

## 8. 奖项清单

- Nobel Prize in Chemistry（1983，独享）
- William H. Nichols Medal（1971）；ACS Award in Inorganic Chemistry（1955 表彰同位素研究）
- National Academy of Sciences 院士（1959）；American Academy of Arts and Sciences（1961）；American Philosophical Society（1981）
- National Medal of Science（1976，卡特总统颁发；"in recognition of contributions to the understanding of reactivity and reaction mechanisms in inorganic chemistry"）
- Welch Award in Chemistry（1983）；NAS Award in Chemical Sciences（1983）
- Priestley Medal（1985，ACS 最高荣誉）
- Guggenheim Fellowship 两度（1949、1955）；Golden Plate Award（1965）
- Foreign Member of the Royal Society, FRS（1988）；Fellow of the Royal Society of Canada, FRSC；Fellow of the Australian Academy of Science
- Willard Gibbs Award；Centenary Prize；Remsen Award；Oesper Award；Glenn T. Seaborg Award for Nuclear Chemistry；National Order of Scientific Merit
- 荣誉学位：University of Saskatchewan（1973）、University of Chicago（1983）、Polytechnic Institute of New York（1984）、SUNY Stony Brook（1985）、University of Guelph（1987）、Seton Hall（1988）、Debrecen（1988）、Northwestern（1990）等
- 1981 年 World Cultural Council 创始成员

## 9. 机构清单

- 教育：Luther College（Regina，中学 + 实验室助理）、University of Saskatchewan（BSc 1935、MSc 1937）、University of California, Berkeley（PhD 1940）
- 任职：Berkeley 讲师（–1941）→ Cornell University（讲师/助理教授，–1946；战时 NDRC）→ University of Chicago（1946–1961，系主任 1956–1959）→ Stanford University（1961–1986，教授；1986 荣休，研究至 2001）；Los Alamos National Laboratory 顾问（1956–1970s）
- 纪念：Nobel Laureate Plaza, University of Saskatchewan（1997，与 Herzberg 并列）；Luther College 年度纪念奖学金（Taube 与 Paul Liefeld 并列）；Progress in Inorganic Chemistry 第 30 卷致敬专辑 "An Appreciation of Henry Taube"；Stanford 纪念研讨系列（Taube 作首讲）

## 10. 终审清单

- [ ] 生卒 1915-11-30 / 2005-11-16（享年 89），出生地 Neudorf（萨斯喀彻温）、去世地 Palo Alto 自宅
- [ ] 1983 **独享**、获奖理由逐字对照 page.md（Awards 段口径）
- [ ] 国籍：1942 归化美国；两个"第二/唯一"表述准确
- [ ] Bray（PhD）+ Spinks（MSc）双行入库；Herzberg 用 influence
- [ ] Creutz–Taube 配合物式与电荷无误；"chemical bridge" 机制表述准确
- [ ] 引语仅 page.md 实载三处可直引；其余全为间接转述
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Henry_Taube/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：`images/` 肖像已就位或装饰圆占位并注记
- [ ] 国籍：封面顶部明示美国（加拿大出生）
- [ ] 引语核对：仅三处 page.md 实载英文原句可直引
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐

---

> **名单状态**：由主控统一更新 `chemist/generate_20th_century_list.py`（执行者不改）。
