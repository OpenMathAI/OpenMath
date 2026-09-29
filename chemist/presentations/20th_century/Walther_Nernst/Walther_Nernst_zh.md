# Walther Nernst（瓦尔特·能斯特）立传提示词

> qid=Q57125 · 1864-06-25 – 1941-11-18 · 德国物理化学家 · 20 世纪 · 诺贝尔化学奖（1920，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Walther_Nernst/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页 + 气泡背景。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/` 就位后使用；page.md 实载 1889 年照片与 1912 年 Max Liebermann 所绘肖像可供选图）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{thermometer-half}\enspace 热力学第三定律之父\enspace·\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）——紫蓝圆点暗示「绝对零度的熵」母题。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）——能斯特方程与热定理是天然的公式框素材。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Walther Hermann Nernst（中文惯称：瓦尔特·能斯特；FRS For）
- **生卒**：1864-06-25 生于西普鲁士 Briesen（今波兰 Wąbrzeźno）→ 1941-11-18 逝于下西里西亚 Zibelle（今波兰 Niwica），享年 77
- **国籍**：Germany（生于普鲁士王国）
- **身份**：物理化学家兼物理学家（热力学 / 电化学 / 固态物理）
- **家庭**：父 Gustav Nernst（1827–1888）为乡村法官，母 Ottilie Nerger（1833–1876）；三姐一弟，三姐死于霍乱。1892 年娶 Emma Lohmeyer，育 2 子 3 女；两个儿子均死于一战；三个女儿中两个嫁给犹太人，纳粹上台后分别移居英国与巴西
- **教育轨迹**：Graudenz 小学 → 苏黎世大学（1883 起本科，物理与数学）→ 柏林大学（间中断）→ 回苏黎世 → 格拉茨大学（在 Boltzmann 系，实际由 Albert von Ettingshausen 指导写论文）→ 维尔茨堡大学（师从 Friedrich Kohlrausch，1887 年获博士学位）→ 莱比锡大学（1889 年 habilitation）
- **导师**：Friedrich Kohlrausch（维尔茨堡，博士论文答辩处）；Ludwig Boltzmann（格拉茨，infobox Other academic advisors）
- **博士**：1887（维尔茨堡大学）
- **研究领域**：物理化学——热力学（第三定律）、电化学（能斯特方程）、电效应、固态物理

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **西普鲁士法官之子（1864）**：乡村法官之家，少年丧母。
2. **格拉茨双效应（在学期间）**：与 Ettingshausen 共同发现 Ettingshausen 效应与 Nernst 效应——磁场垂直于温度梯度中的金属导体产生电位差（及逆效应）。
3. **莱比锡物理化学系（1889 habilitation）**：Ostwald 招募他进入莱比锡大学第一个物理化学系任助手，研究溶液中电流的热力学——与 van 't Hoff、Arrhenius 同建新领域的地基。
4. **能斯特方程（1887/1889）**：推导跨膜离子浓度不等时产生电位差的方程，今广泛用于细胞生理学与神经生物学。
5. **哥廷根与《理论化学》**：短暂执教海德堡后赴哥廷根；慕尼黑曾向他抛出讲席，普鲁士政府为留人在哥廷根专设教席；所著 *Theoretical Chemistry* 被译成英、法、俄文。
6. **能斯特灯（Nernst glower）**：稀土氧化物灯丝的固体辐射体，售价一百万马克（明智放弃版税——不久钨丝充气灯问世）；至今仍是红外光谱学的重要光源；用这笔财富 1898 年买下毕生 18 辆汽车中的第一辆与五百多公顷猎场。
7. **新热定理（1905）**：提出"New Heat Theorem"——温度趋近绝对零度时熵趋于零而自由能保持高于零——后发展为热力学第三定律；使化学家能从热量测定推算反应自由能与平衡点。Theodore Richards 曾指控他窃取想法，但发现权几乎公认归 Nernst。
8. **低温比热与爱因斯坦（1910 前后）**：实验室发现低温下比热显著下降；与 Einstein 1909 年低温比热量子理论预言吻合——Nernst 专程赴苏黎世拜访当时尚不知名的 Einstein，留下"Einstein must be a clever fellow if the great Nernst comes all the way from Berlin to Zürich to talk to him."的时代注脚。
9. **缔造威廉皇帝学会（1911）**：说服威廉皇帝斥资 1100 万马克创立 Kaiser Wilhelm Gesellschaft。
10. **首届索尔维会议（1911）**：与 Max Planck 共同组织布鲁塞尔第一届索尔维会议。
11. **一战（1914–1918）**：签署《九三宣言》；以志愿司机兵团参军；催泪弹想法的试验观察者之一正是 Fritz Haber（哈伯主张改放毒气云）；获二级与一级铁十字及功勋勋章（Pour le Mérite）；任陆军科学顾问研制炸药（高氯酸胍）与迫击炮；曾面谏德皇警告美国参战潜力，被 Ludendorff 斥为"无能的胡说"。
12. **1920 诺贝尔化学奖**：表彰其在热化学上的工作（heat theorem；1921 年 12 月 12 日发表诺奖演讲 *Studies in Chemical Thermodynamics*）；同年因列入协约国战犯名单曾举家短暂避居国外。
13. **柏林晚年（1921–1933）**：柏林大学校长（1921–1922）；创办机构渠道资助青年科学家；婉拒出任驻美大使；两度不愉快的帝国物理技术研究所所长（"平庸与文牍的混合物"）；1924 年任柏林物理化学研究所所长；1930 年与 Bechstein、Siemens 合作发明电钢琴 Neo-Bechstein-Flügel（电子拾音放大，实为钢琴家，常为 Einstein 的小提琴伴奏）；1933 年拒绝填写种族出身表格、为被解职犹太同僚去向奔走；1937 年赴牛津领荣誉学位；1941 年逝于 Zibelle，遗骨最终与 Planck、Hahn、von Laue 比邻葬于哥廷根。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深紫蓝 royalviolet） | `#372A75` | 绝对零度与熵的深紫（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（热力学 badgeThermo） | `#2E5A9E` | 蓝第三定律 / 新热定理 |
| 分类色 2（电化学 badgeElectro） | `#1B7A43` | 绿能斯特方程 / 膜电位 |
| 分类色 3（发明 badgeLamp） | `#D97B29` | 琥珀能斯特灯 / 电钢琴 |
| 分类色 4（组织者 badgeSolvay） | `#C0395B` | 玫瑰索尔维会议 / 威廉皇帝学会 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落）——冷色渐变圆点暗示「温度趋近绝对零度」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**The Flow of Time** — Alex-Productions（文件 `music_audio/alex-productions/35-jqIDnltiDRI-The-Flow-of-Time.wav`，勿复制 wav）
- **风格**：时间流逝 / 宏大叙事 / 理性冷峻
- **匹配理由**：
  - "时间流逝" 匹配热力学第三定律的核心意象——温度、熵与不可逆过程
  - "宏大叙事" 匹配其组织者身份——索尔维会议、威廉皇帝学会、为爱因斯坦造椅
  - "理性冷峻" 匹配其"最大熵状态"的书桌与发明家气质
- **时长**：以实际曲目时长为准，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 热力学第三定律之父 / Walther Nernst 1864–1941 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  能斯特的一生 — Sanger 式时间线（10 节点：1864→1887→1889→1893→1905→1911→1914→1920→1930→1941）
04  早年与求学：苏黎世—格拉茨—维尔茨堡 (1864–1887) — 表格「城市|师从|收获」+ 公式框：Nernst 效应
05  莱比锡与哥廷根 (1889–1905) — 表格「人物|事件|结果」（Ostwald 招募 / Göttingen 专席）
06  能斯特方程 (1889) — 表格「问题|推导|应用」+ 公式框：E = E° + (RT/zF)·ln(a_ion/a_out)
07  能斯特灯与百万马克 (1897) — 表格「发明|原理|结局」+ 红外光谱光源
08  新热定理 (1905) — 表格「问题|表述|意义」+ 公式框：T→0 时 S→0（第三定律）
09  低温比热与爱因斯坦 (1910) — 表格「实验|理论|拜访」（Einstein must be a clever fellow...）
10  索尔维与威廉皇帝学会 (1911) — 表格「机构|伙伴|资本」（Planck / 1100 万马克）
11  一战 (1914–1918) — 表格「职务|工作|争议」（铁十字×2、Pour le Mérite；催泪弹与 Haber）
12  1920 诺贝尔化学奖 — 表格「理由|演讲|年份」（热化学；1921-12-12 演讲；战犯名单风波）
13  柏林晚年与电钢琴 (1921–1941) — 表格「职务|发明|立场」（校长 / Neo-Bechstein / 1933 拒填表格）
14  结尾 — 「在绝对零度，熵归于寂静。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 诺奖年份 | **1920 年诺贝尔化学奖**（infobox 与正文一致），1921-12-12 发表诺奖演讲 *Studies in Chemical Thermodynamics*；**独享**；理由口径为热化学（thermochemistry）/ 热定理 |
| 两位导师 | 博士论文在**维尔茨堡 Kohlrausch** 指导下答辩（infobox Doctoral advisor）；**Boltzmann** 是格拉茨的 Other academic advisor（论文实际由 Ettingshausen 指导）——三人分工勿混 |
| Ettingshausen | 博士论文实际指导者是 **Albert von Ettingshausen**，两人共同发现两效应——勿把效应全部归 Boltzmann |
| 第三定律表述 | 1905 年提出"New Heat Theorem"：T→0 时熵趋于零、自由能保持高于零；使化学家能由热测推算自由能——勿写成"绝对零度不可达到"的现代表述（page.md 未载） |
| Richards 指控 | Theodore Richards 指其窃取想法，但发现权"几乎普遍公认"归 Nernst——客观并置，勿写成定论 |
| Haber 关系 | Nernst 的是**催泪弹**想法，试验观察者 Haber 主张改放毒气云——勿写成"Nernst 提出毒气战" |
| 签署九三宣言 | 1914 签署《九三宣言》支持德军——明载可写，与 1933 年反对纳粹的立场并置呈现 |
| 战犯名单 | 1920 年列入协约国战犯名单而短暂避居国外——明载 |
| 墓地三迁 | 遗骨三次安葬，最终葬于哥廷根 Planck / Hahn / von Laue 墓旁——比邻不等于合葬 |
| 博士门生 | infobox Doctoral students 九人（Simon / Abegg / Langmuir / Andrussow / Bonhoeffer / Lindemann / Duane / Maltby / Eucken）明载可入库；**Other notable students 八人（Lewis / Bodenstein 等）非博士门生，防噪声不入库** |
| 引语红线 | 可用引语仅限 page.md 明载：Einstein "childlike vanity" / "state of maximum entropy" / "Einstein must be a clever fellow..." / Ludendorff "incompetent nonsense" / 新闻稿 "completely unmusical"；中文引号内不得出现其他无源"原话" |
| 电钢琴 | 与 Bechstein、Siemens 合作（1930）——发明人是 Nernst 本人（与爱因斯坦伴奏轶事并置），新闻稿称其"完全不通音律"实为不实 |
| 品牌口径 | 结尾页品牌写 `OpenMathAI`；引号半角 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q57125 | ✅ |
| name_zh | 瓦尔特·能斯特 | ✅ |
| name_en | Walther Nernst（库内既有记录 id=2225，精确复用回填 QID） | ✅ |
| birth_date | 1864-06-25 | ✅ |
| death_date | 1941-11-18 | ✅ |
| nationality | Germany | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | physical chemistry（person_field 细分见下表） | ✅ |

**person_field 细分（rank 表）**：

| name_en | rank | name_zh |
|---|---|---|
| physical chemistry | 0 | 物理化学 |
| thermodynamics | 1 | 热力学 |
| electrochemistry | 2 | 电化学 |
| solid-state physics | 3 | 固态物理 |

## 7. 社会关系入库清单

**师长 / 门生 / 同事 / 家人**（★红线：只收 page.md 正文或 infobox 明载的关系）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Friedrich Kohlrausch | 师→生（博士导师） | 维尔茨堡，1887 年博士论文答辩 |
| advisor-student | Ludwig Boltzmann | 师→生（格拉茨学术导师） | infobox Other academic advisors |
| advisor-student | Francis Simon | 生→师（博士门生） | infobox Doctoral students |
| advisor-student | Richard Abegg | 生→师（博士门生） | infobox Doctoral students |
| advisor-student | Irving Langmuir | 生→师（博士门生） | 1932 年诺贝尔化学奖得主 |
| advisor-student | Leonid Andrussow | 生→师（博士门生） | infobox Doctoral students |
| advisor-student | Karl Friedrich Bonhoeffer | 生→师（博士门生） | infobox Doctoral students |
| advisor-student | Frederick Lindemann | 生→师（博士门生） | Cherwell 子爵 |
| advisor-student | William Duane | 生→师（博士门生） | infobox Doctoral students |
| advisor-student | Margaret Eliza Maltby | 生→师（博士门生） | infobox Doctoral students |
| advisor-student | Arnold Eucken | 生→师（博士门生） | infobox Doctoral students |
| colleague | Albert von Ettingshausen | 无向 | 格拉茨共事，共同发现 Ettingshausen 与 Nernst 效应 |
| colleague | Wilhelm Ostwald | 无向 | 招募其入莱比锡第一个物理化学系任助手 |
| colleague | Jacobus Henricus van 't Hoff | 无向 | 莱比锡同事，共建物理化学新领域 |
| colleague | Svante Arrhenius | 无向 | 莱比锡同事，共建物理化学新领域 |
| colleague | Max Planck | 无向 | 1911 共同组织首届索尔维会议；联手为爱因斯坦设讲席 |
| colleague | Albert Einstein | 无向 | 1909 苏黎世造访；为其争取柏林讲席；钢琴小提琴合奏之友 |
| colleague | Fritz Haber | 无向 | 一战催泪弹试验观察者；同签九三宣言 |
| spouse | Emma Lohmeyer | 无向 | 1892 结婚，育 2 子 3 女；两子死于一战 |

> 禁入库名单（metadata-only / 噪声防入）：Gilbert N. Lewis、Max Bodenstein、Robert von Lieben、Kurt Mendelssohn、Theodor Wulf、Emil Bose、Hermann Irving Schlesinger、Claude Hudson（infobox "Other notable students" 栏，非博士门生，防噪声不入库）；Albert von Ettingshausen 之外的其他格拉茨人物无；Theodore W. Richards（窃取想法指控属争议性说法，无对应关系类型，不入库）；Ignatz Urban（以 Nernstia 属命名致意，非双向关系）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1920，独享）
- Pour le Mérite for Sciences and Arts（1917）；Pour le Mérite（一战军功）
- Iron Cross 第二级与第一级（一战）
- Franklin Medal（1928）
- Bunsen Medal
- Fellow of the Royal Society（For.Mem.RS）
- Honorary membership, Manchester Literary and Philosophical Society（1910-04-05）
- 牛津大学荣誉学位（1937）
- National Inventors Hall of Fame；Silliman Memorial Lectures

## 9. 机构清单

- 教育：University of Zürich（1883–）→ Friedrich Wilhelm University Berlin → University of Graz（Boltzmann 系）→ University of Würzburg（PhD 1887）→ Leipzig University（habilitation 1889）
- 任职：Leipzig 助理（1889–）→ Heidelberg 短暂执教 → Göttingen 教授（政府专设讲席，18 年）→ Friedrich Wilhelm University Berlin（1905–；1921–22 校长；1924 任物理化学研究所所长）→ Physikalisch-Technische Reichsanstalt 所长（两度不愉快）
- 组织：Kaiser Wilhelm Society 创立推手（1911，初始资本 1100 万马克）；首届索尔维会议共同组织者（1911）
- 身后：葬于哥廷根（与 Planck / Hahn / von Laue 比邻）；植物属 Nernstia（1923，Ignatz Urban 命名）纪念

## 10. 终审清单

- [ ] 生卒 1864-06-25 / 1941-11-18，享年 77，出生地 Briesen（今 Wąbrzeźno）、去世地 Zibelle（今 Niwica）
- [ ] 1920 独享；理由热化学；诺奖演讲 1921-12-12
- [ ] 导师 Kohlrausch（博士）+ Boltzmann（学术导师）+ Ettingshausen（论文实际指导）三人分工准确
- [ ] 第三定律表述按 page.md（S→0、自由能高于零）；Richards 指控客观并置
- [ ] 一战与 1933 拒填种族表格的立场对比准确；Haber 关系为催泪弹观察者
- [ ] 博士门生 9 人 vs Other notable students 8 人的入库边界正确
- [ ] 引语全部可在 page.md 溯源，无源处一律间接转述
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Walther_Nernst/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/` 肖像就位（1889 年照片 / 1912 Liebermann 肖像）或装饰圆占位
- [ ] **国籍**：封面顶部明示德国
- [ ] **引语核对**：引语必须在 page.md 原文找到，否则改间接转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox<10pt、hbox<50pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger）对齐

---

> **名单状态**：本提示词由 chem-batch-02 批次生成；`chemist/generate_20th_century_list.py` 由主控统一收尾，勿改动。
