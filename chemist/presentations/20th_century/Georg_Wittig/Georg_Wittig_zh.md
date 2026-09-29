# Georg Wittig（格奥尔格·维蒂希）立传提示词

> qid=Q77171 · 1897-06-16 – 1987-08-26 · 德国化学家 · 20 世纪 · 诺贝尔化学奖（1979，与 Herbert C. Brown 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Georg_Wittig/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传模板**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/` 内若缺，先按常规流程下载 Wikipedia 肖像，404 则装饰圆占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 磷叶立德的炼金术士\enspace·\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、国籍、出生地/去世地、教育（Tübingen / Marburg）、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「碳负离子 / 叶立德」母题——正负成对的圆点暗示 ylide 的偶极结构。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如 Wittig 反应通式：醛/酮 + 磷叶立德 → 烯烃。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Georg Wittig（中文惯称：格奥尔格·维蒂希；德语发音 [ˈɡeː.ɔʁk ˈvɪ.tɪç]）
- **生卒**：1897-06-16 生于柏林（德意志帝国） → 1987-08-26 逝于海德堡（西德），享年 90
- **国籍**：Germany（德国）
- **身份**：化学家（chemist；1979 诺贝尔化学奖得主）
- **家庭**：出生后不久随家迁往卡塞尔，父亲任教于应用艺术高等学校；1931 年娶 Waltraud Ernst（Auwers 课题组的同事）
- **教育轨迹**：
  - 卡塞尔读中学
  - 1916 入 University of Tübingen 学化学
  - 应征入伍，任黑森-卡塞尔骑兵中尉；1918–1919 为协约国战俘
  - 战后因大学人满为患难以复学——直接向马尔堡有机化学教授 Karl von Auwers 请愿得以复学
  - 三年后在 Marburg 获有机化学 PhD
- **导师**：Karl von Auwers（博士导师；亦是其任教资格 habilitation 的导师）
- **任教资格**：1926 年在马尔堡完成 habilitation
- **研究领域**：有机化学——碳负离子化学、有机磷化学、立体化学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **世纪之交的柏林（1897）**：生于德意志帝国首都，随父迁卡塞尔——德国化学黄金年代的亲历者。
2. **从战壕到实验室（1916–1919）**：入学次年即被征召入伍任骑兵中尉；1918–1919 沦为协约国战俘。
3. **一纸请愿（1919–1923）**：战后复学无门，直接向 Karl von Auwers 请愿，得以在马尔堡复学，三年后获有机化学博士。
4. **执教之路（1926–1931）**：Auwers 劝其走学术道路，1926 完成 habilitation；期间与同在 Auwers 门下做 habilitation 的 **Karl Ziegler** 结为挚友。
5. **一本专著换一个讲席（1931–1932）**：写成 400 页立体化学专著；Auwers 的继任者 **Hans Meerwein** 因 impressed by 此书而接受他为讲师。1931 与 Waltraud Ernst 结婚。
6. **布伦瑞克的艰难岁月（1932–1937）**：Karl Fries 邀其任 TU Braunschweig 教授；纳粹试图清除 Fries，Wittig 与之同舟共济（showed solidarity）。
7. **弗莱堡与碳负离子化学（1937–1944）**：**Hermann Staudinger** 邀其赴弗莱堡——部分因为他在立体化学专著中支持了 Staudinger 备受批评的大分子学说；碳负离子化学的基石在弗莱堡时期奠定。
8. **图宾根黄金期（1944–1956）**：接替 Wilhelm Schlenk 出任图宾根有机化学主任；**Wittig 反应在内的绝大多数工作在图宾根完成**。
9. **Wittig 反应**：用磷叶立德（phosphonium ylides）把醛/酮变成烯烃——今日有机合成最常用的 C=C 构建方法之一。
10. **海德堡的例外任命（1956）**：年近六十被任命为海德堡大学有机化学主任（接替 Karl Freudenberg），当时即属破例；新建系馆 + 与 BASF 的紧密联系促成此行。
11. **不只是 Wittig 反应**：苯基锂（phenyllithium）的制备；1,2- 与 2,3-Wittig 重排；directed ortho metalation；ate complex；超价分子；四苯硼酸钾。
12. **实验大师（1967 退休）**：1967 退休后仍留在海德堡工作、论文发表到 1980；同行公认他是 consummate experimenter——对实验现象观察入微，却极少关心理论/机理。
13. **1979 诺贝尔化学奖**：与 Herbert C. Brown 共享（维蒂希=磷、布朗=硼）；官方理由 "for their development of the use of boron- and phosphorus-containing compounds, respectively, into important reagents in organic synthesis"（见其诺奖演讲标题）。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深紫 royalviolet） | `#52307C` | 德国化学传统的庄重与磷化学的深邃（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（Wittig 反应 badgeWit） | `#2E5A9E` | 蓝磷叶立德 → 烯烃 |
| 分类色 2（重排反应 badgeRearr） | `#8C4A2E` | 赭 1,2-/2,3-Wittig 重排 |
| 分类色 3（碳负离子 badgeCarb） | `#1B7A43` | 绿苯基锂 / 弗莱堡基石 |
| 分类色 4（立体化学 badgeStereo） | `#C0395B` | 玫瑰 400 页专著 / 观察者的手艺 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「叶立德偶极」正负成对的圆点几何。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Nostalgia** — Alex-Productions（文件 `music_audio/alex-productions/86-5ETNuoDcBg4-Nostalgia.wav`，不复制 wav）
- **风格**：怀旧 / 温厚 / 世纪回望
- **匹配理由**：
  - "怀旧" 匹配其跨越 90 年的生命——从德意志帝国到联邦德国，横贯两次大战的德国化学世纪
  - "温厚" 匹配其气质——实验大师、挚友 Ziegler、与 Fries 同舟共济的老派学人风骨
  - "世纪回望" 匹配叙事结构——战俘 → 请愿复学 → 五所大学 → 82 岁高龄的诺奖
- **时长**：以实际曲目时长为准，超过 15 页 × 7 秒由 ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 磷叶立德的炼金术士 / Georg Wittig 1897–1987 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  维蒂希的一生 — 时间线（10 节点：1897→1916→1918→1926→1932→1937→1944→1956→1979→1987）
04  早年：从柏林到战俘营 (1897–1919) — 表格「时间|事件|结果」
05  马尔堡：一纸请愿 (1919–1931) — 表格「困境|转机|结果」+ Auwers/Ziegler/Meerwein
06  立体化学专著与漂泊讲席 (1931–1944) — 表格「地点|机缘|结果」（Braunschweig/Freiburg/Tübingen）
07  Wittig 反应 — 表格「问题|方法|结果」+ 公式框：RCHO + Ph₃P=CHR' → RCH=CHR'
08  多面的贡献 — 表格「贡献|内容|意义」（phenyllithium/1,2-/2,3-重排/ate complex/超价分子）
09  1979 诺贝尔化学奖 — 表格「人物|元素|贡献」+ 公式框：维蒂希=磷、布朗=硼
10  实验大师的哲学 — 表格「特质|表现|结果」（观察入微/不重机理/发文至 1980）
11  荣誉清单 — 「类别|代表|意义」表格（含 itemize 荣誉清单）
12  海德堡岁月 — 流程图页（1956 例外任命 → BASF 合作 → 1967 退休 → 荣誉扎堆）
13  遗产：烯烃合成的日常工具 — 四分类遗产盒 + 公式框：Wittig 反应在合成中的地位
14  结尾 — 「把磷叶立德交给合成化学家，他就还你一座烯烃的桥梁。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1979 诺奖口径 | 官方 citation "for their development of the use of boron- and phosphorus-containing compounds, respectively, into important reagents in organic synthesis"——维蒂希对应**磷**、布朗对应**硼**；**共享**勿写独享 |
| frontmatter 噪声 | metadata 的 field_of_work 含 "mathematics"、occupation 含 "mathematician"——属 Wikidata 噪声，主身份以 **chemist** 为准，勿写成数学家 |
| 复学方式 | 战后是**直接向 Karl von Auwers 请愿**得以复学——勿写"重新报考" |
| 博士导师与 habilitation 导师同为 Auwers | 一人双角色，表述勿拆成两人 |
| Meerwein 接纳原因 | 是因为**400 页立体化学专著**给他留下深刻印象——勿写成其他原因 |
| Staudinger 邀请原因 | 部分因为维蒂希在专著中**支持其备受批评的大分子学说**——因果链照原文 |
| 纳粹时期 | 仅写"与被逼退的 Fries 同舟共济（showed solidarity）"——勿扩写成反纳粹事迹 |
| Wittig 反应完成地 | 绝大多数工作（含 Wittig 反应）在**图宾根**完成——勿写弗莱堡或海德堡 |
| 退休与发表 | 1967 退休、论文发表到 1980——勿写 1967 年即停止研究 |
| 荣誉年份 | Otto Hahn Prize 1967、Paul Karrer Gold Medal 1972、诺贝尔 1979——年份照 infobox；Sorbonne 荣誉博士 1956 |
| 同名区分 | 1,2-/2,3-Wittig 重排与 Wittig 反应是**三类不同反应**，勿混为一谈；Karl Ziegler（1963 诺奖）此处仅是挚友关系 |
| 师承链 | 博士生 Werner Tochtermann、Ulrich Schöllkopf 仅 infobox 明载二人——勿添加其他人 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q77171 | ✅ |
| name_zh | 格奥尔格·维蒂希 | ✅ |
| name_en | Georg Wittig | ✅ |
| birth_date | 1897-06-16 | ✅ |
| death_date | 1987-08-26 | ✅ |
| nationality | Germany | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | chemistry（person_field 细分：organic chemistry / organophosphorus chemistry / carbanion chemistry / stereochemistry，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 同事 / 共同得主**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Karl von Auwers | 师→生（博士导师 + habilitation 导师） | 战俘归来后经其直接请求复学 |
| colleague | Karl Ziegler | 无向 | 同在 Auwers 门下做 habilitation，结为挚友 |
| colleague | Hans Meerwein | 无向 | Auwers 继任者，因立体化学专著接受其为讲师 |
| colleague | Hermann Staudinger | 无向 | 1937 邀其赴弗莱堡任教 |
| colleague | Karl Theophil Fries | 无向 | 1932 邀其任布伦瑞克教授；纳粹时期与之同舟共济 |
| co-honored | Herbert C. Brown | 无向 | 1979 诺贝尔化学奖共同得主（维蒂希=磷、布朗=硼） |

**家庭 / 门生**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Waltraud Ernst | 无向 | 1931 结婚，Auwers 课题组成员 |
| advisor-student | Werner Tochtermann | Wittig → 学生 | 博士生（infobox） |
| advisor-student | Ulrich Schöllkopf | Wittig → 学生 | 博士生（infobox） |

> **禁入库名单**：Wilhelm Schlenk、Karl Freudenberg（仅"接任/继任"职务关系，非个人关系）；Karl Freudenberg 亦非师承。metadata.json 无其他 page.md 未载关系。

## 8. 奖项清单

- Nobel Prize in Chemistry（1979，与 Herbert C. Brown 共享）
- Otto Hahn Prize for Chemistry and Physics（1967）
- Paul Karrer Gold Medal（1972）
- Great Cross with Star and Sash of the Order of Merit of the Federal Republic of Germany（联邦德国大十字勋章，年份未载）
- Dannie Heineman Prize；Adolf-von-Baeyer Gold Medal；Karl Ziegler Prize；Roger Adams Award in Organic Chemistry（年份未载）
- 荣誉博士：Sorbonne / University of Paris（1956）

## 9. 机构清单

- 教育：University of Tübingen（1916 入学）→ University of Marburg（复学，PhD、habilitation 1926）
- 任职：University of Marburg 讲师（Meerwein 任内）→ TU Braunschweig 教授（1932–，Karl Fries 邀请）→ University of Freiburg（1937–，Staudinger 邀请）→ University of Tübingen 有机化学主任（1944–，接替 Wilhelm Schlenk）→ University of Heidelberg 有机化学主任（1956–，接替 Karl Freudenberg；1967 退休后仍工作至 1980）
- 产业联系：BASF（海德堡时期的紧密合作关系）

## 10. 终审清单

- [ ] 生卒 1897-06-16 / 1987-08-26，享年 90，出生地柏林、去世地海德堡
- [ ] 1979 共享（Brown）表述准确；磷/硼分工清楚
- [ ] 博士导师 Auwers 一人双角色（PhD + habilitation）表述准确
- [ ] Wittig 反应完成地为图宾根；海德堡 1956 例外任命口径准确
- [ ] frontmatter "mathematician" 噪声未被写入正文
- [ ] 1,2-/2,3-重排与 Wittig 反应三类反应未混淆
- [ ] 引语全部可在本地 Wikipedia 原文溯源（页面无直接引语，全部间接转述）
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Georg_Wittig/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：下载 Wikipedia 肖像（250px→500px；404 用 REST API 查 infobox 原图名；仍失败装饰圆占位）
- [ ] **国籍**：封面顶部明示德国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（无原文一律间接转述）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox≤10pt、hbox≤50pt）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 黄金骨架）对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾，本文件不改动总名单。
> **最重要的事：每写一页就 make，看到溢出就修。**
