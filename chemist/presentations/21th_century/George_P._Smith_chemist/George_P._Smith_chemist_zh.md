# George P. Smith（乔治·P·史密斯）立传提示词

> qid=Q56868017 · 1941-03-10 –（在世）· 美国生物学家 · 21 世纪 · 诺贝尔化学奖（2018，与 Frances Arnold、Greg Winter 共享：Arnold 独享一半"定向演化"，Smith 与 Winter 共享另一半"噬菌体展示"）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/George_P._Smith_chemist/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/` 取 page.md 首图 2018 年 12 月斯德哥尔摩诺奖记者会照片；下载失败用装饰圆占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 培养皿里的简单进化\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（George Pearson Smith）、国籍、出生地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「噬菌体展示」母题——圆点表面伸出的小突起，暗示肽段被展示在丝状噬菌体外壳上。
5. **表格语义化 + 公式框**（★ 核心版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：George Pearson Smith（中文惯称：乔治·P·史密斯）
- **生卒**：1941-03-10 生于美国康涅狄格州诺沃克（Norwalk）→ 在世（2026-09 无卒日，年龄留白处理）
- **国籍**：United States（美国）
- **身份**：美国生物学家；密苏里大学（哥伦比亚校区）生物科学 Curators' Distinguished 荣休教授
- **家庭**：配偶 Marjorie Sable（infobox 明载）；正文提及妻子犹太背景与家庭（其原话 "I'm not religious or Jewish by birth. But my wife is Jewish and our sons are bar-mitzvahed..."——实载引语）；无其他具名家庭信息，禁杜撰
- **教育轨迹**：
  - Phillips Academy（frontmatter educated_at 载）
  - Haverford College 生物学 AB
  - 毕业后做了一年中学教师与实验室技术员
  - Harvard University 细菌学与免疫学 PhD（1970，论文《The variation and adaptive expression of antibodies》）
- **导师**：Edgar Haber（博士导师，infobox 明载）
- **博士**：1970，哈佛大学，细菌学与免疫学
- **研究领域**：生物化学、生物学——噬菌体展示、抗体工程

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **诺沃克少年（1941）**：生于康涅狄格州诺沃克；战前一代美国孩子的朴素起点。
2. **哈弗福德生物学 AB**：小文理学院的生物学训练； Phillips Academy 的中学底色。
3. **中学教师与实验员的一年**：本科毕业没有直奔名校——先教中学、做实验员；一年后重归学术，这条"非典型路径"是他人生的注脚。
4. **哈佛博士（1970）**：细菌学与免疫学，抗体多样性与适应性表达——研究的正是后来噬菌体展示要服务的问题域（抗体）。
5. **威斯康星博士后（1970s）**：与未来的诺贝尔生理学或医学奖得主 **Oliver Smithies**（2007）共事——在大师实验室里学做"把技术做成工具"。
6. **落户密苏里（1975）**：加入密苏里大学（哥伦比亚校区）教职——此后一生未离开的"一座大学一生"。
7. **杜克的一年（1983–1984）**：学术休假赴杜克大学与 Robert Webster 合作——**正是在这一年开始了通向诺贝尔奖的工作**（页面原文口径）。
8. **噬菌体展示（1985）**：把目标蛋白序列人工插入丝状噬菌体的外壳蛋白基因（基因 III 融合），使蛋白质表达在噬菌体**外面**——基因型与表型在同一颗粒上"合体"；1985 年论文首次描述。
9. **"培养皿里的简单进化"（Nobel Lecture 题目）**：Phage Display: Simple Evolution in a Petri Dish——展示 + 筛选的循环就是试管里的定向进化，与 Arnold 的定向演化哲学在 2018 年同台。
10. **技术影响**：噬菌体展示成为抗体工程与蛋白质组学筛选的基石工具——治疗性抗体（如全人源抗体平台）均以此为大树之根（间接转述技术地位，页面以"best known for"表述其代表性）。
11. **2018 诺贝尔化学奖**：与 Greg Winter 共享一半奖金（"for the phage display of peptides and antibodies"），另一半归 Frances Arnold（定向演化）；颁奖时他从教 40 余年仍在密苏里。
12. **荣誉台阶**：密苏里大学 Curators' Professor（2000）、AAAS Fellow（2001）、ASM Promega 生物技术研究奖（2007）、美国国家科学院院士（2020）、密苏里文理学院首届 Mizzou Medal of Distinction（2023）。
13. **公共关怀**：巴以公民权利平等倡导者、BDS 运动支持者（页面实载）——**本篇只作事实性注记或完全略过，不展开不评论**；宗教与家庭表述仅限页面原话，不引申。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（赭红 ochrered） | `#A63A2B` | 深赭红的务实与大学城的朴素——用四十年的耐心造一把钥匙（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（噬菌体展示 badgePhage） | `#2E7FA8` | 蓝基因 III 融合 / 外壳展示 |
| 分类色 2（抗体工程 badgeAntibody） | `#1B7A43` | 绿筛选与亲和成熟 |
| 分类色 3（免疫学根基 badgeImmunol） | `#D97B29` | 琥珀哈佛抗体研究 |
| 分类色 4（简单进化 badgeEvo） | `#C0395B` | 玫瑰培养皿里的进化循环 |
| 背景 | `#F7F6F4` | 微暖浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「噬菌体颗粒与其表面展示的肽段」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Empire Collapse** — Cold Cinema（文件 `music_audio/inspiring-electronic/12-NTuSqFy4Stc-Cinematic Dramatic Epic Drone Orchestra Film by Cold Cinema [No Copyright Music] ⧸ Empire Collapse.wav`；不复制 wav 文件）
- **风格**：戏剧性史诗 Drone 管弦，宏大而有压迫感的开合
- **匹配理由**：
  - "帝国的崩塌" 作为隐喻——噬菌体展示宣告了纯理性设计的局限：让进化筛选代替人脑设计，旧范式让位
  - "Drone 的绵长低音" 匹配密苏里大学城四十年的安静坚守——长期主义者的低音声部
  - 戏剧性高潮对应 2018 年 77 岁获诺奖的全批五人中年龄最长者时刻
- **时长**：以实际曲目时长为准，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 培养皿里的简单进化 / George P. Smith 1941– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/领域/荣誉）
03  史密斯的一生 — 时间线（10 节点：1941→1963→1970→1975→1983→1985→2000→2007→2018→2023）
04  早年：诺沃克到哈弗福德 (1941–1963) — 表格「时间|事件|结果」
05  中学教师与哈佛博士 (1963–1970) — 表格「时间|事件|结果」
06  威斯康星与密苏里 (1970–1975) — 表格「站点|同伴|收获」（Smithies 博士后 / 密苏里落户）
07  杜克转折 (1983–1984) — 表格「问题|合作|起点」
08  噬菌体展示 (1985) — 表格「问题|方法|结果」+ 公式框：基因 III 融合 → 肽段展示于噬菌体外壳
09  展示-筛选循环 — 表格「步骤|机制|意义」+ 公式框：培养皿里的简单进化
10  2018 诺贝尔化学奖 — 表格「得主|份额|理由」+ 公式框："for the phage display of peptides and antibodies"（与 Winter 共享一半；Arnold 独享另一半）
11  密苏里与荣誉 — 表格「类别|代表|意义」（Curators' Professor/NAS 2020/Mizzou Medal 2023）
12  公共关怀 — 克制的事实页（公民权利倡导；一笔带过或留白处理）
13  遗产：一把钥匙打开抗体工程 — 四分类遗产盒
14  结尾 — 「最简单的进化，长出最深的根。」（自撰收束句，非引语）
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 获奖份额 | 2018 Smith 与 Greg Winter **共享另一半**（1/4+1/4），Frances Arnold **独享另一半**（1/2）——勿写成"三人平分"或"Smith 独享" |
| 官方理由 | Smith/Winter 的半句是 "for the phage display of peptides and antibodies"；Arnold 的半句是 "for the directed evolution of enzymes"——两句勿混 |
| 同名区分 | 本篇是 **George Pearson Smith**（Q56868017，生物学家，密苏里）——与 2009 物理诺奖得主 **George E. Smith**（CCD）完全无关；叙述与 DB 均用 "George P. Smith" 防撞 |
| 1985 奠基 | 1985 年首次描述噬菌体展示（肽段融合丝状噬菌体基因 III）——年份与"首次描述"口径须准；勿写成"发明抗体药物" |
| 杜克年份 | 1983–1984 学年在杜克大学与 Robert Webster 合作——"开始了通向诺奖的工作"是页面原文口径 |
| Smithies 关系 | 威斯康星博士后在 **Oliver Smithies**（2007 诺贝尔生理学或医学奖）实验室——"future Nobel laureate" 是页面原文；勿把 Smithies 写成博士导师 |
| 政治敏感 | 巴以公民权利 / BDS 立场为页面实载，但涉及地缘政治——**一律不展开、不评论，正文建议完全略过**；宗教表述仅限原话引用场景或跳过 |
| 引语 | "I'm not religious or Jewish by birth. But my wife is Jewish..." 为页面实载原话，可整句引用；Nobel Lecture 题目可引用；其余无原文一律转述 |
| 博后头衔 | Workplaces 列 Postdoctoral Scholar, University of Wisconsin–Madison——机构口径写 University of Wisconsin（Madison） |
| 职业跨度 | 1975 年入职密苏里至 2018 获奖 43 年——"四十年教龄"级表述取整时勿超页面实载细节 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q56868017 | ✅ |
| name_zh | 乔治·P·史密斯 | ✅ |
| name_en | George P. Smith | ✅ |
| birth_date | 1941-03-10 | ✅ |
| death_date | （在世，留空） | ✅ |
| nationality | United States | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry（person_field 细分见下表） | ✅ |

**person_field 细分（rank 表）**：

| rank | name_en | name_zh |
|---|---|---|
| 0 | phage display | 噬菌体展示 |
| 1 | antibody engineering | 抗体工程 |
| 2 | biochemistry | 生物化学 |
| 3 | immunology | 免疫学 |

## 7. 社会关系入库清单

**师长 / 同事 / 共同得主 / 家庭**（★红线：只收 page.md 正文或 infobox 明载；metadata-only 一律不入库）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Edgar Haber | 师→生（博士导师） | Harvard 细菌学与免疫学博士（1970） |
| advisor-student | Oliver Smithies | 师→生（博士后导师） | University of Wisconsin 博士后；Smithies 后获 2007 诺贝尔生理学或医学奖 |
| colleague | Robert Webster | 无向 | 1983–1984 杜克大学学术休假合作者；噬菌体展示工作的起点 |
| co-honored | Frances Arnold | 无向 | 2018 诺贝尔化学奖（Arnold 独享另一半） |
| co-honored | Greg Winter | 无向 | 2018 诺贝尔化学奖（共享同一半，理由 "for the phage display of peptides and antibodies"；规范名 "Greg Winter"，与下一批 Winter 篇互指一致） |
| spouse | Marjorie Sable | 无向 | 配偶（infobox 明载） |

> **禁入库名单**（页面无具名学术关系）：儿子们（仅宗教表述中提及，未具名学术信息）、杜克与密苏里的其他同事（未具名）。metadata.json properties 无额外关系字段（仅 doctoral_advisor: Edgar Haber，已入库）。

## 8. 奖项清单

- Nobel Prize in Chemistry（2018，与 Greg Winter 共享一半；Frances Arnold 独享另一半）
- University of Missouri Curators' Professor（2000）
- Fellow of the American Association for the Advancement of Science，AAAS（2001）
- American Society for Microbiology Promega Biotechnology Research Award（2007）
- Member of the United States National Academy of Sciences，NAS（2020）
- Inaugural Mizzou Medal of Distinction，University of Missouri College of Arts and Sciences（2023）

## 9. 机构清单

- 教育：Phillips Academy；Haverford College（生物学 AB）；Harvard University（PhD 1970，细菌学与免疫学，Edgar Haber 指导）
- 任职：中学教师与实验室技术员（一年）；University of Wisconsin–Madison 博士后（Smithies 实验室）；University of Missouri 教授（1975–，Curators' Distinguished Professor Emeritus）；Duke University 访问教授（1983–1984，Robert Webster 实验室）

## 10. 终审清单

- [ ] 生卒 1941-03-10 / 在世留白；出生地 Norwalk, CT
- [ ] 2018 份额结构：Arnold 1/2 + Smith/Winter 各 1/4；两句官方理由不混
- [ ] 与 George E. Smith（2009 物理）严格区分；全篇用 "George P. Smith"
- [ ] 1985 首次描述噬菌体展示；1983–1984 杜克起点口径
- [ ] Smithies 为博士后导师（非博士导师）；Haber 为博士导师
- [ ] BDS/宗教内容不展开不评论；引语仅限页面原话
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/George_P._Smith_chemist/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/` 肖像就位（2018 斯德哥尔摩记者会照片；失败用装饰圆）
- [ ] **国籍**：封面顶部明示美国
- [ ] **引语核对**：宗教原话与 Nobel Lecture 题目可引用；其余一律间接转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 黄金参照）对齐
