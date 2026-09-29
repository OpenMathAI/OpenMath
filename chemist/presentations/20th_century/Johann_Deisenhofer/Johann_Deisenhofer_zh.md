# Johann Deisenhofer（约翰·戴森霍弗）立传提示词

> qid=Q76612 · 1943-09-30 生于德国 Zusamaltheim（巴伐利亚）· 在世 · 德裔美籍生物化学家 · 诺贝尔化学奖（1988，与 Robert Huber、Hartmut Michel 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Johann_Deisenhofer/`（page.md + metadata.json + page.html + images.txt）
> ⚠️ **本页为短页面**（仅 infobox + 两节正文），以实载为准、严禁脑补；page.md 无载的生平细节一律留白或仅作版式占位。
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/`）。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）。本页 infobox 与 images.txt 均无真实肖像——封面用**装饰圆占位**（主色实心圆 + 姓名缩写），插图用 images.txt 的 `Photosynthetic_Reaction_Center_Drawing.png`（膜内光合反应中心示意）作核心贡献页插图。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{sun}\enspace 第一个膜蛋白晶体结构\enspace·\enspace 德国 / 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像（装饰圆）+ 右侧 2×2 信息网格：生卒、本名、国籍（Germany + United States 双重公民身份）、出生地、教育（TU München / Max Planck Institute for Biochemistry）、博士导师 Robert Huber、博士 1974、核心领域、任职（UT Southwestern）、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「膜内蛋白复合体 / 原子坐标」母题。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Johann Deisenhofer（中文惯称：约翰·戴森霍弗）
- **生卒**：1943-09-30 生于德国 Zusamaltheim（巴伐利亚，时为 Nazi Germany；在世，death_date 留白）
- **国籍 / 公民身份**：Germany + United States（infobox Citizenship: Germany and United States）
- **身份**：生物化学家、生物物理学家（biochemist / biophysicist；UT Southwestern 教授）
- **家庭**：page.md 无载——身份信息页家庭栏写「页面无载」，禁编造
- **教育轨迹**：
  - 巴伐利亚出生长大
  - Technical University of Munich（慕尼黑工大）博士（1974，研究工作在 Max Planck Institute of Biochemistry, Martinsried 完成）
- **导师**：Robert Huber（infobox Doctoral advisor 明载）
- **博士**：1974 获博士（慕尼黑工大 / 马普生物化学研究所 Martinsried；论文题目页面无载）
- **研究领域**：生物化学、生物物理、X 射线晶体学、光合作用

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **巴伐利亚之子（1943）**：生于二战中的 Zusamaltheim 小村——战后德国一代科学家的普通起点（页面仅载出生地与日期，勿扩写战时经历）。
2. **慕尼黑工大与马普（至 1974）**：在 Max Planck Institute of Biochemistry（Martinsried）完成研究工作，1974 获慕尼黑工大博士学位——师从 Robert Huber。
3. **Huber 结构生物学学派（1974–1988）**：博士毕业后留在马普生物化学研究所持续研究 14 年——Huber 领导的蛋白质晶体学重镇（Huber 1971 起任该所所长）。
4. **膜蛋白结晶的圣杯**：整合膜蛋白（integral membrane protein）因嵌在脂膜中极难结晶——其三维结构长期是晶体学的空白地带（page.md 以 "the first crystal structure of an integral membrane protein" 定位其工作）。
5. **Michel 的结晶突破（1982 前后）**：Hartmut Michel 完成膜蛋白结晶——为 X 射线解析铺平道路。
6. **三人组（1982–1985）**：与 Michel、Huber 用 X 射线晶体学测定光合细菌光合反应中心（photosynthetic reaction center）复合体中**超过 10,000 个原子**的精确排布。
7. **第一个膜蛋白晶体结构**：膜结合的蛋白-辅因子复合体，是光合作用启动环节的关键——史上第一个被解析的整合膜蛋白晶体结构。
8. **光合作用机制的普遍启示**：该研究加深了对光合作用机制的一般理解，并揭示植物与细菌光合过程的相似性。
9. **1986 双奖先声**：与 Michel 同获 Max Delbrück Prize（1986；Michel 篇同载该奖）——诺奖前的学界确认。
10. **1988 诺贝尔化学奖**：与 Hartmut Michel、Robert Huber 共享——"for their determination of the first crystal structure of an integral membrane protein, a membrane-bound complex of proteins and co-factors that is essential to photosynthesis"（page.md 导语口径）。
11. **横渡大西洋（1988）**：诺奖同年加入 Howard Hughes Medical Institute（HHMI）科学团队与 University of Texas Southwestern Medical Center at Dallas 生物化学系教职。
12. **公共科学家**：出任 Scientists and Engineers for America 顾问委员会成员（推动美国政府科学理性）；2003 年成为签署 Humanist Manifesto 的 22 位诺奖得主之一。
13. **执教至今**：现任 UT Southwestern Medical Center 生物物理学系教授。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深海军蓝 deepmarine） | `#16324F` | 膜蛋白晶体结构的深邃秩序（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（晶体学 badgeXray） | `#2E5A9E` | 蓝 X 射线晶体学 / 10,000 原子 |
| 分类色 2（光合作用 badgePhoto） | `#1B7A43` | 绿光合反应中心 / 细菌光合 |
| 分类色 3（膜蛋白 badgeMembrane） | `#D97B29` | 琥珀整合膜蛋白 / 结晶突破 |
| 分类色 4（公共科学 badgeCivic） | `#C0395B` | 玫瑰科学政策 / 人文宣言 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落）——膜内复合体的蛋白-辅因子团簇意象。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Ascension** — Cold Cinema（清单预分配，勿复制 wav 文件，Makefile 引用源路径）
- **文件**：`music_audio/inspiring-electronic/20-gYUC-sXt_8M-Cinematic Dramatic Epic Orchestra Sci-Fi Trailer by Cold Cinema [No Copyright Music] ⧸ Ascension.wav`
- **风格**：科幻预告片式 / 恢弘上扬 / 冷峻
- **匹配理由**：
  - "Ascension"（上升）呼应「原子坐标逐层升起为膜蛋白立体结构」的解析叙事——从二维晶体到三维结构
  - 科幻感匹配 X 射线晶体学「看见不可见」的仪器之美
  - 恢弘段落托住 10,000 原子 + 第一个膜蛋白结构的历史分量
- **时长**：以实际文件为准 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 第一个膜蛋白晶体结构 / Johann Deisenhofer 1943– + 四色 badge + 右上装饰圆头像 + 国籍行
02  身份信息页（★ 必做）— 左装饰圆 + 右 2×2 信息网格（生卒/本名/双重公民身份/出生地/教育/博士导师/博士/领域/任职/荣誉）
03  戴森霍弗的一生 — 高斯式时间线（10 节点：1943→1974→1982→1985→1986→1988→1988 达拉斯→2003→在世→遗产）
04  巴伐利亚到慕尼黑 (1943–1974) — 表格「阶段|内容|结果」（短页面实载：出生 + TU München/马普 Martinsried + 1974 博士）
05  Huber 学派 (1974–1988) — 表格「环境|方法|传统」（马普生物化学研究所蛋白质晶体学）
06  膜蛋白结晶之难 — 表格「问题|原因|既有困境」+ 公式框：整合膜蛋白 = 蛋白 + 辅因子 + 脂膜
07  三人组 (1982–1985) — 表格「人物|途径|贡献」（Michel / Deisenhofer / Huber 三人共同用 X 射线晶体学测定）+ 公式框：>10,000 atoms
08  光合反应中心结构 — 表格「层级|内容|意义」+ Photosynthetic_Reaction_Center_Drawing.png 插图
09  1988 诺贝尔化学奖 — 表格「得主|贡献|机构」（三人共享）+ 获奖口径
10  横渡大西洋：HHMI 与 UT Southwestern (1988) — 表格「节点|内容|结果」
11  公共科学家 — 高斯式「类别|代表|意义」表格（SEA 顾问 / 2003 Humanist Manifesto 22 诺奖得主之一）
12  1986 双奖先声 — Max Delbrück Prize（1986，与 Michel 同获奖口径）+ Otto Bayer Award（metadata 载）
13  遗产：膜蛋白结构生物学 — 四分类遗产盒（方法学 / 光合机制 / 后续膜蛋白结构井喷 / 德美桥梁）
14  结尾 — 「看见 10,000 个原子的排布，光合作用从此有了结构语言。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 短页面红线 | 本页 page.md 仅 infobox + Early life and education + Career 三块——**无载一律留白**：家庭/婚姻/子女/中学/本科细节全禁编造 |
| 1988 诺奖口径 | 三人共享；page.md 口径 "for their determination of the first crystal structure of an integral membrane protein, a membrane-bound complex of proteins and co-factors that is essential to photosynthesis"——从 page.md 导语句口径，禁另编 citation 全句 |
| 三人分工 | page.md 未做明细分工表，Slide 07 只能写「三人共同用 X 射线晶体学测定」，勿脑补各自角色 |
| 双重公民身份 | infobox "Citizenship: Germany and United States"——写「德国/美国双重公民身份」，勿单写「美国化学家」 |
| 博士导师 | Robert Huber（infobox Doctoral advisor）——1988 三人中是**师生兼共同得主**关系，两条关系分开入库 |
| 博士年份 | 1974（page.md "earned his doctorate ... in 1974"）；论文题目页面无载——禁编造 |
| Max Planck 机构名 | Early life 节作 "Max Planck Institute of Biochemistry"（Martinsried）——与 Huber 篇 "Max Planck Institute for Biochemistry" 拼写差异为来源原文，正文统一用其中一种并加注 |
| Max Delbrück Prize | 1986（page.md Awards 行）；infobox 拼写 Max Delbruck/Delbrück 不一——以正字 Delbrück 为准 |
| 达拉斯入职年份 | 1988（"until 1988, when he joined HHMI and the faculty of UT Southwestern"）——诺奖同年，两事勿写成因果 |
| Humanist Manifesto | 2003 年为 22 位签署诺奖得主之一——"one of 22 Nobel Laureates" 口径照写 |
| 中文引语 | page.md 无直接引语，全篇禁用引号原话，一律间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q76612 | ✅ |
| name_zh | 约翰·戴森霍弗 | ✅ |
| name_en | Johann Deisenhofer | ✅ |
| birth_date | 1943-09-30 | ✅ |
| death_date | （在世，留白） | ✅ |
| nationality | Germany（rank 0）+ United States（rank 1） | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry（person_field 细分见下表） | ✅ |
| has_biography | 0（待 Beamer 后置 1） | ✅ |

person_field 细分 rank 表：

| name_en | rank | name_zh |
|---|---|---|
| biochemistry | 0 | 生物化学 |
| biophysics | 1 | 生物物理学 |
| X-ray crystallography | 2 | X 射线晶体学 |
| photosynthesis | 3 | 光合作用 |

## 7. 社会关系入库清单

**师长 / 共同得主**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Robert Huber | 师→生（博士导师） | 慕尼黑工大/马普生物化学研究所（Martinsried），1974 博士 |
| co-honored | Robert Huber | 无向 | 1988 诺贝尔化学奖共同得主（与 advisor 关系并行两条） |
| co-honored | Hartmut Michel | 无向 | 1988 诺贝尔化学奖共同得主 |

> metadata.json-only 一律不入库。本页禁入库名单：Scientists and Engineers for America / Humanist Manifesto 签署群体（组织与群体非个人关系）。家庭/婚姻 page.md 无载，无关系可入。1982–1985 三人合作已由 co-honored 覆盖，不另建 colleague 行。

## 8. 奖项清单

- Max Delbrück Prize（1986）
- Nobel Prize in Chemistry（1988，与 Michel、Huber 共享）
- Golden Plate Award of the American Academy of Achievement（1989）
- Otto Bayer Award（metadata 载，年份以官方页面为准）
- Knight Commander's Cross of the Order of Merit of the Federal Republic of Germany（联邦德国功绩勋章指挥官十字，metadata 载）
- X-ray badge（metadata 载， Wikimedia 徽章类，不入正文奖项表）

## 9. 机构清单

- 教育：Technical University of Munich（博士 1974，研究于 Max Planck Institute of Biochemistry, Martinsried）
- 任职：Max Planck Institute of Biochemistry（Martinsried，1974–1988）；Howard Hughes Medical Institute 科学团队（1988–）；University of Texas Southwestern Medical Center at Dallas 生物化学系（1988–）→ 生物物理学系教授（现任）
- 其他：Scientists and Engineers for America 顾问委员会

## 10. 终审清单

- [ ] 生卒 1943-09-30（Zusamaltheim）/ 在世留白
- [ ] 1988 三人共享（Michel、Huber）表述准确；获奖理由按 page.md 导语口径
- [ ] 博士导师 Robert Huber + 师生兼共同得主双关系入库正确
- [ ] 双重公民身份（Germany + United States）表述准确
- [ ] 10,000 原子、1982–1985、HHMI/UT Southwestern 1988 年份准确
- [ ] 家庭/婚姻等无载项全部留白，无编造
- [ ] 引语全篇间接转述（page.md 无直接引语）
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Johann_Deisenhofer/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：本页无真实肖像——装饰圆占位；Photosynthetic_Reaction_Center_Drawing.png 作插图
- [ ] 国籍：封面顶部明示德国 / 美国
- [ ] 引语核对：全篇无引号原话（间接转述）
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像/装饰圆 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐

---

> **名单状态**：`chemist/prompt_manifest.json` chem-batch-20 · Johann Deisenhofer（1988，BGM Ascension，主色 #16324F）。
> **开始执行。每完成一步向主控汇报。**
