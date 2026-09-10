# William Ramsay（威廉·拉姆齐）立传提示词

> qid=Q950726 · 1852-10-02 – 1916-07-23 · 英国（苏格兰）化学家 · 诺贝尔化学奖（1904）
> 诺奖理由（总名单 OpenChemist_20th_Century_Nobel_Laureates.md 措辞）：**表彰他发现空气中的惰性气体元素，并确定它们在元素周期表中的位置**
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/William_Ramsay/`（page.md + metadata.json + images.txt）
> 版式基准：**参考数学家 Carl Friedrich Gauss（Q6722）的立传提示词与 Beamer 格式**（`mathematician/presentations/19th_century/Carl_Friedrich_Gauss/Carl_Friedrich_Gauss_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次立传的核心版式语言。

---

## 0. 正文形式说明（参考数学家高斯立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像下载见 §11 Review-1 指引——images.txt 无肖像 URL，需回退流程）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 空气中隐藏的一族元素\enspace·\enspace 英国（苏格兰）`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「稀有气体」母题——稀疏、离散、彼此几乎不作用的惰性圆点，正是氦氖氪氙在空气中的存在方式。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）——本人物公式少，用「周期表零族片段」「气体密度差异」等结构化展示框替代数学公式（公式框内可放元素符号排布 Ar/He/Ne/Kr/Xe/Rn 与对应发现年份，样式与公式框一致）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Sir William Ramsay, KCB FRS FRSE（中文惯称：威廉·拉姆齐；1902 年受封 KCB，称 Sir——与拒爵位的桑格相反，他确实被授爵）
- **生卒**：1852-10-02 生于苏格兰格拉斯哥 Clifton Street 2 号（乔治式三层带地下室联宅，少年时迁往 Hillhead 区 Oakvale Place 1 号）→ 1916-07-23 逝于英格兰白金汉郡 High Wycombe，享年 63；葬于 Hazlemere 教区教堂
- **死因**：鼻癌（nasal cancer）
- **国籍**：United Kingdom of Great Britain and Ireland（英国）；苏格兰化学家（metadata description：Scottish chemist）
- **身份**：化学家、教授；惰性气体（noble gases）发现者；Ramsay grease 以他命名；occupation 另含 historian、archaeologist（metadata）
- **家庭**：父亲 William C. Ramsay 为土木工程师与测量员，母亲 Catherine Robertson；**叔父是地质学家 Sir Andrew Ramsay**。1881 年娶 Margaret Johnstone Marshall（娘家姓 Buchanan，George Stevenson Buchanan 之女）；一女 Catherine Elizabeth（Elska）、一子 William George（40 岁去世）。晚年居于白金汉郡 Hazlemere 直至去世
- **教育轨迹**：
  - Glasgow Academy 就读；随后本已师从格文（Govan）造船商 Robert Napier 当学徒，却改而投身化学
  - 1866 年入格拉斯哥大学，1869 年毕业；随后随化学家 Thomas Anderson 做实践训练
  - 赴德国图宾根大学（University of Tübingen）师从 Wilhelm Rudolph Fittig，获 PhD
- **博士论文**：《Investigations in the Toluic and Nitrotoluic Acids》（甲苯甲酸与硝基甲苯甲酸研究）
- **研究领域**：化学——有机化学（早期）、氮氧化物、气体、惰性气体；原子量测定

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **弃船从化（1852–1866）**：工程师与测量员之子，本已许给格文造船厂当学徒，却转身投考格拉斯哥大学化学——1866 年入学、1869 年毕业。
2. **图宾根的有机化学训练（1870s）**：随 Fittig 研究甲苯甲酸与硝基甲苯甲酸获 PhD；回格拉斯哥任 Anderson 的助手（Anderson College）。
3. **首个杂芳环全合成（1876）**：从乙炔与氢氰酸在铁管炉中合成吡啶——首个杂芳香族化合物的合成，早于一切惰性气体工作。
4. **布里斯托尔（1879–1887）**：1879 年任 University College, Bristol 化学教授，1881 年兼任该校校长（Principal），同时兼顾有机化学与气体的活跃研究；1885–1890 年间发表多篇氮氧化物论文，为后续工作练就手艺。
5. **执掌 UCL 化学讲席（1887）**：接替 Alexander Williamson 出任伦敦大学学院化学教授——他最负盛名的发现全部在 UCL 完成。
6. **Rayleigh 的一堂课（1894-04-19 夜）**：Rayleigh 讲座指出化学法制氮与空气分离氮的密度差异；简短交谈后两人决定联手追查。8 月，Ramsay 告知 Rayleigh：已分离出空气中的新重组分，几乎无化学反应活性。
7. **命名"氩"（1894）**：以希腊语"懒惰"（lazy）一词命名为 argon——一个不肯化合的元素。
8. **氦落地（1890s）**：分离出氦——此前它只在太阳光谱中被观测到，从未在地球上找到。
9. **与 Travers 三连发现（随后数年）**：与 Morris Travers 合作发现氖、氪、氙；五种大气惰性元素齐备，周期表由此开辟新的一族。
10. **氡（1910）**：分离并表征了氡——惰性气体工作的晚期收官。
11. **1904 双奖之夜**：Ramsay 获**诺贝尔化学奖**；同氩之谊的 Rayleigh 同年获**诺贝尔物理学奖**——一桩发现、两个奖项、两个学科。诺奖演讲 "The Rare Gases of the Atmosphere"（1904-12-12）。
12. **科学外交与晚年**：1893–1902 与英国化学家 Emily Aston 合作矿物分析与原子量测定（含非缔合液体混合物的分子表面能论文）；1899 入选美国哲学会、1904 入选美国国家科学院；任印度科学理工学院顾问，建议院址设班加罗尔；1911–1912 任英国科学促进会主席。
13. **身后**：Notting Hill Arundel Gardens 12 号蓝牌铭记其生平；Hazlemere 有以他命名的 Sir William Ramsay School；Westminster Abbey 唱诗席北廊立 Charles Hartwell 所作纪念碑；1923 年 UCL 以 Ramsay Memorial Fund 创设化学工程系与讲席；2019-10-02 Google 以 Doodle 纪念其 167 岁诞辰。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（苏格兰蓝 scotblue） | `#2A4B7C` | 高地深空与稀薄气体的静穆（表头 / 展示框文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（展示框边线、字段标签） |
| 分类色 1（氩 badgeAr） | `#3A5F8A` | 蓝氩 / 空气中的新组分 / Rayleigh 合作 |
| 分类色 2（氦 badgeHe） | `#B07D2B` | 金棕氦 / 太阳光谱落地的元素 |
| 分类色 3（氖氪氙 badgeNKX） | `#2E8B6E` | 绿氖氪氙 / 与 Travers 的三连发现 / 周期表新族 |
| 分类色 4（氡与晚期工作 badgeRn） | `#8A3B5C` | 玫瑰红氡 / 1910 收官 / 放射性气体 |
| 背景 | `#F7F7F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「稀有气体」——占空气极小份额、彼此几乎不作用的惰性圆点。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Shine Like The Sun** — Really Slow Motion（`music_audio/inspiring-electronic/15-w6kT1BfvETI-Really Slow Motion - Shine Like The Sun (Epic Beautiful Uplifting).wav`）
- **风格**：史诗 / 美丽 / 振奋
- **匹配理由**：
  - 标题直击其发现中最浪漫的一幕——**氦先在太阳光谱中被观测到，再由 Ramsay 从地球上分离**："Shine Like The Sun" 即太阳光谱落地的化学注脚
  - "振奋" 匹配 1904 双奖之夜——一项氩的发现同源分出物理、化学两座诺奖，是他事业的顶点
  - "美丽" 匹配周期表开族的叙事——五种惰性元素逐一入位，零族在表格上徐徐点亮
- **时长**：以实际文件为准；略短于 slides 总时长时 ffmpeg `-shortest` 自动对齐
- **注**：wav 复制在执行立传阶段进行（`cp` 到本目录，Makefile `BGM = $(wildcard *.wav)` 自动检测）

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 空气中隐藏的一族元素 / William Ramsay 1852–1916 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  拉姆齐的一生 — 高斯式时间线（10 节点：1852→1866→1876→1887→1894→1895→1902→1904→1910→1916；氖氪氙与氦的年份 page.md 未载，勿标具体年份，见 §5）
04  早年：从造船学徒到化学（1852–1876） — 表格「时间|事件|结果」（Glasgow Academy/Napier 学徒未从/格拉斯哥大学/Anderson 训练）
05  图宾根与有机化学年代（1870s–1887） — 表格「阶段|工作|意义」（Fittig 博士论文/吡啶全合成 1876/布里斯托尔与氮氧化物）
06  1894 年 4 月 19 日夜：Rayleigh 的一堂课 — 表格「线索|追问|结果」（密度差异→联手→新惰性组分→命名 argon = 希腊语"懒惰"）
07  一族元素齐备：氦·氖·氪·氙 — 表格「元素|合作者|意义」（氦：太阳光谱→落地；Ne/Kr/Xe：与 Travers）+ 元素排布展示框
08  氡（1910）与周期表零族 — 表格「问题|方法|结果」+ 展示框：周期表零族片段（He/Ne/Ar/Kr/Xe/Rn 位置）
09  1904：一桩发现、两座诺奖 — 表格「人物|奖项|理由」（Ramsay 化学奖 / Rayleigh 物理学奖；措辞照总名单）+ 诺奖演讲 1904-12-12
10  合作者与门生 — 表格「人物|方向|结果」（Travers/Aston/门生 Baly、Dobbie、Heyrovský——Heyrovský 后获诺奖事 page.md 无载，勿写）
11  荣誉与衔级 — 高斯式「类别|代表|意义」表格（Davy 1895、Nobel 1904、Matteucci 1907、Elliott Cresson 1913、KCB 1902、FRS、Pour le Mérite）
12  科学外交 — 表格「事项|时间|结果」（印度科学理工学院顾问·建议班加罗尔 / 英国科学促进会主席 1911–12 / NAS 1904、哲学会 1899）
13  遗产：蓝牌·学校·纪念碑 — 四分类遗产盒（周期表零族 / UCL 化学工程系 1923 / Sir William Ramsay School 与蓝牌 / Westminster Abbey 纪念碑·Google Doodle 2019）
14  结尾 — 「空气从不空无一物——惰性一族，静候百年。」（自拟金句，非引语）
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1904 两个奖项勿混 | Ramsay 获 1904 **诺贝尔化学奖**；Rayleigh 因氩的发现获**同年诺贝尔物理学奖**——切勿写成"两人共享化学奖"或"Ramsay 得物理学奖" |
| 诺奖理由措辞 | 总名单官方措辞「表彰他发现空气中的惰性气体元素，并确定它们在元素周期表中的位置」；英文原文 "in recognition of his services in the discovery of the inert gaseous elements in air"——注意理由限定 **in air（空气中）**，勿把氡（非空气组分）也算进获奖理由 |
| 氦的表述 | page.md 只说他分离出"此前仅在太阳光谱中被观测到、从未在地球上找到"的氦——**未载 Janssen/Lockyer 及发现年份**，勿写"1895 年发现氦"或引入天文学家姓名 |
| 氖氪氙勿写独享 | 氖、氪、氙是**与 Morris Travers 合作**发现（"In the following years"）——勿写 Ramsay 独自发现；且 page.md **未给具体年份**，勿标 1898 |
| 氩的发现归属 | 1894-04-19 Rayleigh 讲座后二人**联手**追查密度差异；Ramsay 分离出新组分并命名 argon（希腊语"懒惰"）——勿写成 Rayleigh 或 Ramsay 单方发现氩 |
| 氡年份 | 1910 年"分离并表征"氡——勿写成"发现零族第五元素"或与获奖理由捆绑 |
| 吡啶 1876 | 从乙炔 + 氢氰酸铁管炉合成吡啶，是**首个杂芳香族化合物合成**——与惰性气体无关，勿混入获奖理由；勿写"合成第一个芳香族化合物" |
| 布里斯托尔年份出入 | 正文写 **1879** 年任 University College, Bristol 化学教授、1881 年兼任校长；infobox 机构年限为 Bristol (1880–87)——以正文 1879 为准，并在 §5 注明此内部出入 |
| 博士生名单冲突 | 正文 infobox 门生为 **Baly、Dobbie、Heyrovský** 三人；metadata.json `doctoral_student` 为 **Morris Travers**，与正文不一致——**以 page.md 为准**：三人入库为门生，Travers 入库为长期合作者（colleague），冲突写明。另：Heyrovský 后获 1959 诺奖一事 page.md **无载**，勿写 |
| 受封骑士 | 1902 年加冕荣誉名单获 KCB，1902-10-24 由 Edward VII 于白金汉宫授衔——**他是 Sir**，与桑格拒爵相反；勿写"拒绝爵位"或漏写 KCB |
| 海水提金（敏感） | 1905 年背书 Industrial and Engineering Trust Ltd. 从海水提金，公司**从未产出任何金**——轶事可略过；若写须照实含"失败"结局，不得洗成"商业远见" |
| metadata 日期噪声 | metadata.json `date_of_birth` 含 "1852-00-00"、`date_of_death` 含 "1918-07-23"（错误噪声）——以 page.md **1852-10-02 / 1916-07-23** 为准 |
| 死因与葬地 | 鼻癌，逝于 High Wycombe，葬 Hazlemere 教区教堂——勿写"逝于伦敦"或死因含糊 |
| 引语纪律 | page.md 几乎无直接引语（可溯源者仅 argon 词源自希腊语"懒惰"一事的叙述）；诺奖理由为官方文件引文。其余一律间接转述，中文引号内禁止无源"原话" |
| 国籍口径 | metadata nationality 为 "United Kingdom of Great Britain and Ireland"、description 为 Scottish chemist；总名单列 **British**——封面写"英国（苏格兰）"，数据库 nationality 用 United Kingdom |
| 家族混淆 | 叔父 Sir Andrew Ramsay 是**地质学家**；子 William George 40 岁去世——勿把叔父写成父亲、勿漏"侄"关系方向 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q950726 | ✅ |
| name_zh | 威廉·拉姆齐 | ✅ |
| name_en | William Ramsay | ✅ |
| birth_date | 1852-10-02（metadata 另有 1852-00-00 噪声，弃用） | ✅ |
| death_date | 1916-07-23（metadata 另有 1918-07-23 噪声，弃用；以 page.md 为准） | ✅ |
| nationality | United Kingdom（总名单口径 British） | ✅ |
| primary_occupation | chemist（metadata 兼 professor/historian/archaeologist，主导口径 chemist） | ✅ |
| field_of_work | chemistry（person_field 细分：noble gases / inorganic chemistry / organic chemistry，带 rank） | ✅ |
| has_biography | 1 | ✅ 入库时置 1 |

## 7. 社会关系入库清单

**师长 / 合作者 / 同年双奖**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Wilhelm Rudolph Fittig | 师→生（博士导师） | 图宾根大学；甲苯甲酸与硝基甲苯甲酸论文 |
| advisor-student | Thomas Anderson | 师→生（实践训练导师） | 格拉斯哥训练，后任其助手（Anderson College） |
| colleague | John William Strutt, 3rd Baron Rayleigh | 无向 | 1894-04-19 讲座引出氩的合作发现 |
| co-honored | Lord Rayleigh | 无向 | 同年（1904）诺奖：Ramsay 化学奖、Rayleigh 物理学奖，同源氩 |
| colleague | Morris Travers | 无向 | 氖、氪、氙的共同发现者；metadata 记其为 doctoral_student，与正文 infobox 不一致——**按正文入库为合作者** |
| colleague | Emily Aston | 无向 | 1893–1902 矿物分析与原子量测定合作 |
| colleague | Alexander Williamson | 无向 | 1887 年接替其 UCL 化学讲席（前任） |
| advisor-student | Edward Charles Cyril Baly | 拉姆齐→学生 | 正文 infobox 门生 |
| advisor-student | James Johnston Dobbie | 拉姆齐→学生 | 正文 infobox 门生 |
| advisor-student | Jaroslav Heyrovský | 拉姆齐→学生 | 正文 infobox 门生（其 1959 诺奖 page.md 无载，note 不写） |
| other | Sir Andrew Ramsay | 无向 | 叔父，地质学家 |

## 8. 奖项清单

- Nobel Prize in Chemistry（1904）
- Davy Medal（1895）
- Leconte Prize（1895）
- Barnard Medal for Meritorious Service to Science（1895）
- Longstaff Prize（1897）
- Matteucci Medal（1907）
- Elliott Cresson Medal（1913）
- Knight Commander of the Order of the Bath，KCB（1902 加冕荣誉，1902-10-24 授衔）
- Fellow of the Royal Society，FRS；Honorary Fellow of the Royal Society of Edinburgh（metadata.json）
- Pour le Mérite for Sciences and Arts（metadata.json）
- August Wilhelm von Hofmann Medal（metadata.json）
- 荣誉博士：克拉科夫雅盖隆大学（metadata.json）
- International Member, U.S. National Academy of Sciences（1904）；American Philosophical Society（1899）；Honorary Member, Physics Association, Frankfurt（metadata.json）

## 9. 机构清单

- 教育：Glasgow Academy；Robert Napier 学徒（格文，未从）；University of Glasgow（1866 入学，1869 毕业）；Anderson College（Anderson 门下实践）；University of Tübingen（PhD，Fittig）
- 任职：University of Glasgow / Anderson College 助手（1870s）；University College, Bristol 化学教授（1879）兼校长（1881，infobox 机构年限 1880–87）；University College London 化学讲席教授（1887–1913，接替 Williamson）
- 命名机构/纪念：Sir William Ramsay School（Hazlemere）；UCL 化学工程系与讲席（1923，Ramsay Memorial Fund 资助）；Arundel Gardens 12 号蓝牌；Westminster Abbey 纪念碑（Charles Hartwell 作）；Ramsay grease（以其命名的物质）

## 10. 终审清单

- [ ] 生卒 1852-10-02 / 1916-07-23，享年 63，出生地格拉斯哥、去世地 High Wycombe、葬 Hazlemere；metadata 日期噪声已弃用
- [ ] 1904 Ramsay 化学奖 / Rayleigh 物理学奖——两奖勿混；诺奖理由照总名单措辞且限定 "in air"
- [ ] 氦：只有"太阳光谱→地面分离"表述，无 Janssen/Lockyer、无年份；氖氪氙与 Travers 共享且不标年份
- [ ] 氩：1894-04-19 讲座、联手追查、Ramsay 命名——归属准确
- [ ] 氡 1910 分离并表征，不并入获奖理由
- [ ] 吡啶 1876 首个杂芳香族合成，与获奖理由分离
- [ ] 布里斯托尔 1879（正文）vs infobox 1880–87 出入已注明
- [ ] 门生三人（Baly/Dobbie/Heyrovský）+ Travers 作合作者；metadata 冲突已注明；Heyrovský 诺奖事未写
- [ ] KCB 1902 受衔（Sir），未写成拒爵
- [ ] 引语全部可在 page.md 找到原文；其余全部间接转述
- [ ] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 展示框（周期表零族）+ 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/William_Ramsay/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：images.txt **无肖像 URL**（仅诺奖证书照与蓝牌照，均禁作肖像）——按回退流程：先以 Wikipedia REST API `page/summary` 查 infobox 原图文件名（图注 "Ramsay in 1904" 表明存在 1904 年肖像照），再以 Commons `Special:FilePath/<文件名>?width=600` 下载（尝试 "William Ramsay.jpg" 等变体）；404/返回 HTML 则换文件名；仍失败则**装饰圆占位**。下载后 `file` 验证为 JPEG
- [ ] **国籍**：封面顶部明示英国（苏格兰）
- [ ] **引语核对**：中文引号内禁止无源"原话"（argon 词源叙述与诺奖理由为仅有的可引点）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox ≤10pt、hbox ≤50pt 可接受）
- [ ] 身份信息页布局与高斯模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一；引号用半角
- [ ] 与化学家侧既有格式（Sanger 版式）及数学家侧（高斯）对齐

---

> **名单状态**：本提示词已完成；Beamer 立传**待执行**。`chemist/generate_20th_century_list.py` 的 `BIOGRAPHIES_DONE` **暂不更新**（执行立传完成后再同步）。
> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
