# Dudley R. Herschbach（达德利·赫施巴赫）立传提示词

> qid=Q243196 · 1932-06-18 – 在世 · 美国化学家 · 20 世纪 · 诺贝尔化学奖（1986，与 Yuan T. Lee、John C. Polanyi 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Dudley_R._Herschbach/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：参考 `chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`（表格语义化 tabularx + 公式展示框 + 时间线页）。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/Dudley_Herschbach_HD2011_AIC_Gold_Medal_2.jpg` 已就位——2011 年 AIC 金勋章照）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{bolt}\enspace 分子碰撞的导演者\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、国籍、出生地、教育（Stanford/Harvard）、博士导师、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆），母题呼应「交叉分子束 / 两束粒子在对撞点交汇」——两组相向的圆点序列暗示分子束交叉。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化（交叉分子束示意、能量在平动/转动/振动模式间的分配）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Dudley Robert Herschbach（中文惯称：达德利·赫施巴赫）
- **生卒**：1932-06-18 生于加利福尼亚州 San Jose（在世，卒日留白）
- **国籍**：United States（美国）
- **身份**：化学家（Harvard 大学教授；后兼 Texas A&M 物理学教授）
- **家庭**：六个孩子中的长子，乡间长大；妻 Georgene Herschbach（哈佛学院本科教务副院长，主持本科教育委员会至 2009 退休；夫妇多年共同担任 Currier House 院长）；孙女 Erica Jarrell-Searcy 为橄榄球运动员
- **教育轨迹**：
  - Campbell High School（校橄榄球队）
  - Stanford University：获体育与学术两份奖学金、选学术——1954 数学 BS、1955 化学 MS（硕士课题计算气相反应的 Arrhenius A 因子）
  - Harvard University：1956 物理学 AM、1958 化学物理 PhD；1957–1959 获哈佛 Society of Fellows 三年 Junior Fellowship
- **导师**：Edgar Bright Wilson（哈佛博士导师，微波谱学方向）；Stanford 本科新生导师 Harold S. Johnston（聘其为暑期研究助理、高年级亲授化学动力学——引他入门的关键人物）
- **研究领域**：化学——反应动力学（reaction dynamics）、交叉分子束、分子立体动力学（stereodynamics）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **奖学金抉择（1950）**：体育与学术双奖学金选学术——乡间长子走上化学之路；新生导师 Johnston 暑期带教，高年级传授化学动力学。
2. **哈佛化学物理 PhD（1958）**：在 E. Bright Wilson 指导下用微波谱研究分子隧穿分裂；1957–1959 Junior Fellow。
3. **伯克利起步（1959–1963）**：1959 任加州大学伯克利分校化学助理教授、1961 副教授；与研究生 George Kwei、James Norris 建成可供反应散射实验的大型交叉束装置。
4. **K + CH3I：第一次看清元反应（1960s 初）**：结果首次给出基元碰撞的细致图像——KI 产物沿入射 K 原子束反冲的"直接反弹"过程；挑战了"交叉分子束中不会发生碰撞"的流行成见。
5. **K + Br2 与"剥离反应"**：发现热丝表面电离检测器会因此前使用而潜在污染（须预处理方得可靠结果）；改进仪器后观察到 K + Br2 是 KBr 产物向前散射的"剥离反应"。
6. **回哈佛（1963）**：任化学教授；与研究生 Sanford Safron、Walter Miller 继续碱金属—卤化物反应的分子束动力学。
7. **超级机器（1967）**：Yuan T. Lee 以博士后身份加入实验室；Herschbach、Lee 与研究生 Doug MacDonald、Pierre LeBreton 开始建造研究 Cl + Br2 及氢—卤素反应的"supermachine"通用交叉分子束装置。
8. **1986 诺贝尔化学奖**：与 Yuan T. Lee、John C. Polanyi 三人共享，理由 "for their contributions concerning the dynamics of chemical elementary processes"（page.md 口径）；Herschbach 与 Lee 的贡献在交叉分子束实验。
9. **能量分配的读出**：交叉准直气相反应物束，可在产物的平动、转动、振动模式间分配能量——理解反应动力学的关键；两人被认为开创了化学研究的新领域。
10. **分子立体动力学先驱**：测量并以理论诠释角动量及其矢量性质在化学反应动力学中的作用。
11. **跨界研究**：发表逾 400 篇论文；量纲标度理论；证明甲烷可在地球深部地幔高温高压下自发生成（非生物成因烃的证据）；晚年与 Steven Brams 合作研究赞成投票制（approval voting）。
12. **科普与公共服务**：为《辛普森一家》"Treehouse of Horror XIV" 一集献声（给 Frink 教授颁诺贝尔物理学奖）；2010 美国科学与工程节"Lunch with a Laureate"；RSI 杰出讲座系列；Society for Science & the Public 董事会主席（1992–2010）；《原子科学家公报》赞助人委员会成员；2003 年 22 位诺奖得主联名签署《人文主义宣言》之一；鹰级童军与杰出鹰级童军奖（DESA）。
13. **教学人生**：多年讲授哈佛本科普通化学、自述是其"最具挑战性的任务"；2005-09-01 加入 Texas A&M 任物理学教授（每年执教一学期）；设立 Herschbach Medal（双年度分子碰撞动力学会议颁发）。

## 3. 配色方案（主色 + 强调 + 分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深绯红 deep crimson） | `#8A1E2D` | 分子束对撞的能量与张力（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（交叉分子束 badgeBeam） | `#2E5A9E` | 蓝交叉束 / K + CH3I 反弹 |
| 分类色 2（反应动力学 badgeDyn） | `#1B7A43` | 绿能量分配 / 剥离反应 |
| 分类色 3（立体动力学 badgeStereodynamics） | `#D97B29` | 琥珀角动量 / 矢量性质 |
| 分类色 4（教育与公共 badgeEdu） | `#7A5C1E` | 棕科普 / 辛普森 / 童军 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 篇一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），母题「两束粒子相向而行、于对撞点交汇」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Cinematic Experience** — Alex-Productions（清单预置 `music_audio/alex-productions/48-QL3O8MUFAm4-Cinematic-Experience.wav`；执行时按项目惯例软链至本目录，不复制 wav 文件）
- **风格**：电影感 / 铺陈推进 / 能量感
- **匹配理由**：
  - 电影感匹配交叉分子束的"慢镜头"意象——把一次飞秒级碰撞放大成可见的轨迹与角度
  - 推进感匹配"超级机器"从伯克利到哈佛的持续建造与迭代
  - 能量感匹配反应动力学"能量在平动/转动/振动间分配"的母题
- **时长核对**：执行时确认音轨时长 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，00–14）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 分子碰撞的导演者 / Dudley R. Herschbach 1932– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/国籍/出生地/教育/博士导师/领域/荣誉）
03  赫施巴赫之路 — 时间线（10 节点：1932→1954→1955→1956→1958→1959→1963→1967→1986→2005）
04  早年：乡间长子与奖学金抉择 (1932–1955) — 表格「时间|事件|结果」（Campbell/Stanford/Johnston 带教）
05  哈佛化学物理 (1956–1959) — 表格「时间|事件|结果」（Wilson 门下微波谱/Junior Fellow）+ 公式框：隧穿分裂
06  伯克利：交叉束装置 (1959–1963) — 表格「问题|方法|结果」（Kwei/Norris 大装置）
07  K + CH3I：看清元反应 (1960s) — 表格「问题|方法|结果」+ 公式框：直接反弹 vs 剥离反应
08  超级机器 (1967–) — 表格「人物|工作|成果」（Lee/MacDonald/LeBreton；Cl+Br2、氢+卤素）
09  1986 诺奖 — 表格「三人|方法|贡献」+ 公式框：交叉分子束 = 平动/转动/振动能量分配（与 Lee、Polanyi 共享）
10  立体动力学与跨界研究 — 表格「方向|内容|意义」（角动量/量纲标度/地幔甲烷/赞成投票）
11  讲台与荧幕 — 双栏页：普通化学"最具挑战的任务" / 辛普森一家献声 / Lunch with a Laureate
12  荣誉清单 — 「类别|代表|意义」表格（含 itemize：诺奖/国家科学奖章 1991/各奖章/Fellow 头衔）
13  遗产：反应动力学的新领域 — 四分类遗产盒 + Herschbach Medal + 400+ 论文
14  结尾 — 「把一次碰撞，放慢成一幅可以被阅读的画。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 获奖理由口径 | page.md 措辞 "for their contributions concerning the dynamics of chemical elementary processes"；勿改写成诺贝尔官网其他变体 |
| 三人共享方向 | Herschbach 与 Lee 做**交叉分子束实验**；Polanyi 做**红外化学发光**——两种方法勿混；三人共享同一理由 |
| 与 Lee 的关系 | Lee 1967 年以 **postdoctoral student（博士后）** 身份入组——是博士后导师关系而非博士导师，note 必须写明"博士后" |
| 双奖学金 | Stanford 给的是体育 + 学术两份奖学金，**选了学术**——勿写成"体育特长生" |
| 学位年份 | Stanford：BS 1954（数学）/ MS 1955（化学）；Harvard：AM 1956（物理）/ PhD 1958（化学物理）——四个年份勿混 |
| K + Br2 检测器 | 发现热丝检测器**污染问题**并预处理——这是实验可靠性的关键一环，勿写成"发明了检测器" |
| 在世 | 1932-06-18 生、**在世**——卒日、享年一律留白 |
| 地幔甲烷 | 是"甲烷可在地幔高温高压下自发形成"的研究结论与非生物成因烃的指示——勿写成"推翻化石燃料理论" |
| 辛普森一家 | 献声一集、给 Professor Frink 颁**诺贝尔物理学奖**——是客串演出不是获奖；勿写成讽刺事件 |
| 引语 | page.md 仅 "collisions do not occur in crossed molecular beams"（他所挑战的流行观点）与 "most challenging assignment"（本科教学自述）两处引号语境——前者是他人成见、须标注语境，不可当作 Herschbach 自述 |
| 名字缩写 | 常用缩写 **Dudley R. Herschbach**（R. = Robert）；文本可写全名 Dudley Robert Herschbach |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q243196 | ✅ |
| name_zh | 达德利·赫施巴赫 | ✅ |
| name_en | Dudley R. Herschbach | ✅ |
| birth_date | 1932-06-18 | ✅ |
| death_date | （空——在世） | ✅ |
| nationality | United States | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | chemistry（person_field 细分：chemical kinetics / reaction dynamics / crossed molecular beams / molecular stereodynamics，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Edgar Bright Wilson | 师→生（博士导师） | 哈佛化学物理 PhD（1958），微波谱研究分子隧穿分裂 |
| advisor-student | Harold S. Johnston | 师→生（本科导师） | Stanford 新生导师，聘为暑期研究助理、高年级亲授化学动力学 |
| advisor-student | Richard N. Zare | 师→生（学生） | infobox 博士生；合作 1964 光解能量分配论文 |
| advisor-student | Seong Keun Kim | 师→生（学生） | infobox 博士生 |
| advisor-student | Timothy Clark Germann | 师→生（学生） | infobox 博士生 |
| advisor-student | Yuan T. Lee | 师→生（博士后导师） | 1967 年以博士后身份入组，共建通用交叉分子束"supermachine" |
| co-honored | Yuan T. Lee | 无向 | 1986 诺贝尔化学奖共同得主（交叉分子束） |
| co-honored | John C. Polanyi | 无向 | 1986 诺贝尔化学奖共同得主（红外化学发光） |
| spouse | Georgene Herschbach | 无向 | 哈佛学院本科教务副院长；Currier House 共同院长 |
| colleague | Steven Brams | 无向 | 合作研究赞成投票制（approval voting） |

> **禁入库名单**：研究生 George Kwei、James Norris、Sanford Safron、Walter Miller、Doug MacDonald、Pierre LeBreton（正文提及但非 infobox 博士生名录，防噪声不入库）；孙女 Erica Jarrell-Searcy（亲属非学术关系）；《人文主义宣言》22 位联名者（集体事件）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1986，与 Lee、Polanyi 共享）
- National Medal of Science（1991）
- ACS Award in Pure Chemistry（1965）
- Linus Pauling Medal（1978）
- RSC Michael Polanyi Medal（1981）
- Irving Langmuir Award in Chemical Physics（1983）
- American Institute of Chemists Gold Medal（2011）
- Distinguished Eagle Scout Award（DESA）
- Guggenheim Fellowship；荣誉博士（University of Toronto、Harvard University）
- Fellow：美国艺术与科学院、美国国家科学院、美国哲学学会、英国皇家化学会
- Herschbach Medal（本人设立，双年度分子碰撞动力学会议颁发）

## 9. 机构清单

- 教育：Campbell High School；Stanford University（BS 1954 / MS 1955）；Harvard University（AM 1956 / PhD 1958；Junior Fellow 1957–1959）
- 任职：University of California, Berkeley（1959 助理教授 / 1961 副教授）；Harvard University（1963 化学教授，后为 emeritus）；Texas A&M University（2005-09-01 起物理学教授，每年一学期）；Freiburg University（frontmatter 机构列有载）
- 公职：Society for Science & the Public 董事会主席（1992–2010）；Center for Arms Control and Non-Proliferation 董事；《原子科学家公报》赞助人委员会

## 10. 终审清单

- [ ] 生卒 1932-06-18 / 在世留白；出生地 San Jose, California
- [ ] 四个学位年份（1954/1955/1956/1958）与学科口径准确
- [ ] 1986 三人共享、获奖理由按 page.md 口径；Herschbach/Lee=交叉分子束、Polanyi=红外化学发光
- [ ] Lee 是博士后导师（1967）非博士导师
- [ ] K+CH3I 反弹 / K+Br2 剥离与检测器污染表述准确
- [ ] "collisions do not occur" 引语标注为他方成见语境；无编造引语
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 `pages/Dudley_R._Herschbach/page.md` 逐页对照 Beamer tex 全部事实
- [ ] 头像：AIC Gold Medal 2011 照已就位
- [ ] 国籍：封面明示美国
- [ ] 编译验证：`make distclean && make`
- [ ] Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox≤10pt、hbox≤50pt）
- [ ] 身份信息页布局与 Sanger 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐

---

> **名单状态**：由 chem-batch-19 批次产出提示词与数据入库；立传与 Review 列由主控统一收尾。
