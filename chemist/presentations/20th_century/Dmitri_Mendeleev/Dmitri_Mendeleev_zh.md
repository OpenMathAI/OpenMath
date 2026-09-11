# Dmitri Mendeleev（德米特里·门捷列夫）立传提示词 —— 特别篇 · 诺贝尔奖遗珠

> qid=Q9106 · 1834-02-08（N.S.，O.S. 01-27）– 1907-02-02（O.S. 01-20） · 俄国化学家 · 20 世纪
> **定位：特别篇。门捷列夫不是诺贝尔化学奖得主**——他 1905/1906/1907 连续三年被提名（共 9 次），1906 年诺贝尔化学委员会正式推荐他获奖，却因 Arrhenius 反对、以一票之差败给 Moissan。本篇以「诺奖遗珠」为叙事主轴，注明他其实很应该获得这一奖项。
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Dmitri_Mendeleev/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考同项目标杆 Frederick Sanger（Q151564）的立传与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 时间线页 + 语义化 tabularx 表格 + 金色公式框 + 气泡背景，格式完全照搬，内容按本人物填充。

---

## 0. 正文形式说明（参考 Sanger 标杆，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。肖像用 `images/Kramskoy_Mendeleev_01.jpg`（Kramskoi 1878 油画肖像，images.txt 有 250px URL，下载改 500px）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 元素周期的立法者\enspace·\enspace 俄罗斯帝国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。**封面明确标注「特别篇 · 诺贝尔奖遗珠」**（小字注即可，勿喧宾夺主）。
3. **必须有身份信息页**（★ 必做）：左侧头像 + 右侧 2×2 信息网格：生卒、本名（Дмитрий Иванович Менделеев）、国籍、出生地/去世地、教育、博士（Doctor of Science 1865）、师承（Alexander Voskresensky）、核心领域、荣誉。事实取自本地 page.md，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；气泡背景呼应「元素落位」母题——稀疏圆点如元素格子中的原子。
5. **表格语义化 + 公式框**（★ 标杆精髓）：核心贡献页用 `tabularx` 三列表格（问题 | 方法 | 结果），表下配金色边框浅金底公式展示框。1869 年周期表原始片段（Cl/K/Ca、Br/Rb/Sr、I/Cs/Ba 三行原子量表，page.md 实载）可直接做成表格页。
6. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`；引语纪律见 §5。

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Dmitri Ivanovich Mendeleev（Дмитрий Иванович Менделеев；中文惯称：德米特里·伊万诺维奇·门捷列夫）
- **生卒**：1834-02-08 生于西伯利亚 Tobolsk 附近村庄 Verkhnie Aremzyani（O.S. 1834-01-27）→ 1907-02-02 逝于圣彼得堡（O.S. 01-20；流感），享年 72；葬 Literatorskie Mostki 公墓
- **国籍**：Russian Empire（俄罗斯帝国）
- **身份**：化学家（兼物理学家、经济学家；化学讲席教授、度量衡局局长）
- **家庭**：17 个孩子中最小（存活数 13/14 各源有争议，勿写精确存活数——见 §5）；父 Ivan Pavlovich Mendeleev 为中学教师（后失明失业），母 Maria Dmitrievna Kornilieva 出身 Tobolsk 商人家族、重开玻璃厂；父系本姓 Sokolov（神学院惯例改姓 Mendeleev）。两次婚姻：Feozva Nikitichna Leshcheva（1862 结婚，1882 离婚）、Anna Ivanovna Popova（1882 结婚；离婚手续晚于再婚一个月，构成教会法下的重婚争议，此争议被指是他落选俄国科学院的原因之一）；次婚女儿 Lyubov 嫁诗人 Alexander Blok
- **教育轨迹**：Tobolsk 文理中学（13 岁起，父亡、母厂毁于火之后）→ 1850 入 Main Pedagogical Institute（母亲携其横穿俄罗斯赴莫斯科大学被拒后转圣彼得堡）→ 毕业后患肺结核，1855 赴克里米亚任 Simferopol 第一文理中学科学教师 → 1857 痊愈返圣彼得堡 → 1859–1861 海德堡研究液体毛细作用与分光镜 → 1865 圣彼得堡大学 Doctor of Science（论文《On the Combinations of Water with Alcohol》，1865）
- **导师**：Alexander Voskresensky（metadata.json doctoral_advisor 唯一记载；1867 年门捷列夫接替其无机化学讲席）
- **研究领域**：化学（周期律/周期表）、物理化学（溶液、气体膨胀、临界温度）、石油地质、度量衡学、经济学与工业政策

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **西伯利亚少年（1834–1850）**：最小的孩子、父盲厂毁、母亲携子千里求学——「patiently search divine and scientific truth」的母亲教诲（引语见 §5 纪律）。
2. **海德堡岁月（1859–1861）**：毛细作用与分光镜；1861 出版《Organic Chemistry》教科书获 Demidov 奖。
3. **圣彼得堡讲席（1864–1867）**：1864 技术学院教授、1865 国立大学教授并获 Doctor of Science；1867 获终身教职并接替 Voskresenskii 无机化学讲席；至 1871 把圣彼得堡建成国际公认的化学研究中心。
4. **《Principles of Chemistry》与周期律的诞生（1868–1870）**：为写教科书而分类元素时发现模式；1869-03-06 向俄国化学会宣读《The Dependence between the Properties of the Atomic Weights of the Elements》。
5. **周期律八要点（1869）**：按原子量排列呈周期性、原子量决定元素性质、预言未知元素、可据相邻元素修正原子量等（page.md 实载 8 条，表格页可用）。
6. **大预言：eka 系（1869–1886）**：以梵文前缀 eka/dvi/tri 命名缺位元素——eka-aluminium=镓（1875 发现）、eka-silicon=锗（1886 发现）、eka-boron=钪；预言全部应验。
7. **纠正已知值**：铀的化合价 3→6、原子量 120→240（近于今值 238）。
8. **先驱同行**：Newlands 八音律（1864 提出/1865 发表，1887 才获承认）、Lothar Meyer 1864 年 28 元素表（无预言）——门捷列夫的独特处是**预言未知元素 + 纠正已知值**，而非「第一个发现周期性」（见 §5）。
9. **梦的传说**：自称在梦中看见完整元素表（引自 Inostrantzev 的转述——引用时必须注明转述属性）。
10. **俄国化学会创始人与多面手（1868–）**：1868 共创俄国化学会；石油成因主张深部无机成因、助建俄国第一座炼油厂；发明无烟火药 pyrocollodion（1892 组织生产，俄海军未采用）；把米制引入俄国。
11. **度量衡局局长（1893–1907）**：1890-08-17 因学生待遇问题辞去教授；1892/1893 执掌度量衡总局直至去世。
12. **★ 诺奖之争（1905–1907）——本篇核心页**：三年 9 次提名（1905 三次、1906 四次、1907 两次）；1906 年化学委员会正式推荐他获奖，化学分部支持；全院大会上委员会异议者 Peter Klason 提名 Moissan，Arrhenius（非化学委员会成员但在院内影响巨大）力主否决——据同时代人转述，动机是他对电离理论的批评之积怨；激辩后 Moissan 以一票之差胜出；1907 年两次提名再被 Arrhenius 绝对反对所挫。**门捷列夫至死未获诺贝尔奖。**
13. **身后之名**：Chugaev 评语「chemist of genius…」（转述引语，page.md 实载）；101 号元素 mendelevium（Md）、矿物 mendeleevite-Ce（2010）、月球背面环形山 Mendeleev、俄科院门捷列夫金质奖章（1965 起）、Kramskoi（1878）与 Repin（1885）两幅传世肖像、2016 生日 Google doodle。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（帝国深紫 deeppurple） | `#452C63` | 梦与预言的气质——「在梦里看见完整的表」 |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 元素落位的秩序感 / 遗珠之憾 |
| 分类色 1（周期律 badgeTable） | `#2E5A9E` | 蓝 1869 周期表 / 八要点 |
| 分类色 2（预言应验 badgePredict） | `#1B7A43` | 绿 eka 系 / Ga·Ge·Sc |
| 分类色 3（工业与石油 badgePetro） | `#D97B29` | 琥珀 石油/无烟火药/经济 |
| 分类色 4（诺奖之争 badgeNobel） | `#C0395B` | 玫瑰 1905–1907 提名与一票之差 |
| 背景 | `#F7F6F9` | 浅灰白（与标杆一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应元素在周期表格子中的落位。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Cinematic Experience** — Alex-Productions（本地文件 `music_audio/alex-productions/48-QL3O8MUFAm4-Cinematic-Experience.wav`）
- **风格**：电影感 / 宏大 / 高张力
- **匹配理由**：
  - "电影感" 匹配其人生戏剧性——西伯利亚孤儿 → 梦中见表 → 预言成真 → 一票之差与诺奖失之交臂
  - "宏大" 匹配贡献本质——周期律是对整个物质世界的立法，非一人一域之功
  - 与本项目已选曲目不重复（Sanger=Timeless，1901–1910 批次=Expedition/Savage/SEA/Shine Like The Sun/The Flow of Time/Through the Darkness/Tragedy/New Lands/Eternals/Nostalgia）
- **时长**：以实际文件为准；略短于 slides 总时长时 ffmpeg `-shortest` 自动对齐；wav 复制在执行立传阶段进行（`cp` 到本目录，Makefile `BGM = $(wildcard *.wav)` 自动检测）

## 4. Slide 规划（15 页，标杆式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 把元素排成一张表的人 / Dmitri Mendeleev 1834–1907 + 四色 badge + 右上头像 + 国籍行 + 「特别篇 · 诺奖遗珠」小注
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  门捷列夫的一生 — 时间线（10 节点：1834→1850→1861→1865→1869→1871→1875/1886→1890→1893→1905-07→1907）
04  西伯利亚少年 (1834–1850) — 表格「时间|事件|结果」（17 子最小/父盲厂毁/千里求学/母亲教诲）
05  求学与漂泊 (1850–1865) — 表格「时间|事件|结果」（师范学院/肺结核赴克里米亚/海德堡/Demidov 奖/博士）
06  周期律的诞生 (1868–1871) — 表格「背景|方法|结果」+ 1869 原始三行原子量表（Cl/K/Ca、Br/Rb/Sr、I/Cs/Ba）+ 公式框：周期律八要点（节选）
07  大预言 (eka 系) — 表格「缺位|预言名|应验」+ 公式框：eka-aluminium→Ga(1875)、eka-silicon→Ge(1886)、eka-boron→Sc + 铀值修正
08  先驱与同行 — 表格「人物|工作|与门捷列夫关系」（Newlands/Meyer）——独特处=预言+纠错，勿写「第一个发现周期性」
09  圣彼得堡学派与多面手 — 表格「领域|工作|意义」（化学会 1868/教科书/溶液/临界温度）
10  石油与工业 — 表格「问题|主张|结果」（无机成因/第一座炼油厂/pyrocollodion/米制）
11  度量衡与晚年 (1890–1907) — 表格「时间|事件|结果」（1890 辞职/1893 度量衡局/至死在任）
12  ★ 诺奖之争 (1905–1907) — 表格「年份|提名|结果」+ 金色重点框：1906 委员会推荐→Klason 提名 Moissan→Arrhenius 反对→一票之差；「其实很应该获得」的定论由 page.md 实载事实支撑，禁加主观渲染词
13  遗产与纪念 — 四分类遗产盒（mendelevium/mendeleevite-Ce/月球环形山/金质奖章）+ Chugaev 评语框
14  结尾 — 金句：元素各有其位，而历史终究为他留了位置。（叙述题记，非引语；生卒年行 + 品牌 OpenMathAI）
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| **非得主红线** | 门捷列夫**从未获得诺贝尔奖**——全篇禁写「诺贝尔化学奖得主」；封面/身份页/结尾用「特别篇 · 诺奖遗珠」定位；总名单（OpenChemist_20th_Century_Nobel_Laureates.md）不含此人，metadata.json 的 `year: 1906` 是诺奖投票年而非获奖年 |
| 1906 一票之差 | 化学委员会**正式推荐** Mendeleev 获 1906 奖；Klason 是委员会内的异议者提名 Moissan；Arrhenius 非化学委员会成员但影响力大、力主否决——「积怨动机」据 contemporaries 转述，引用时须保留转述属性 |
| 提名次数 | 1905/1906/1907 三年共 **9 次提名**（3+4+2）；1907 两次被 Arrhenius「绝对反对」挫败——勿写「多次提名」笼统带过，也不要写错分解数 |
| 生卒双历 | 1834-02-08（O.S. 01-27）生；1907-02-02（O.S. 01-20）卒——新旧历勿混，正文用新历、可括注旧历 |
| 兄弟排行 | 17 个孩子中**最小**；存活数 13/14 各源有争议（Nature/Gordin 笔误事件），勿写精确存活数 |
| **伏特加神话（禁写）** | 「门捷列夫定下伏特加 40% 标准」是流行讹传——40% 标准早在 1843 年（他 9 岁）已由政府颁布；其度量衡机构只管度量衡不管生产标准；1865 论文只讨论 70% 以上医用酒精浓度，他从未写过伏特加。Beamer 一旦提及必须以辟谣形式出现，否则干脆不提 |
| 周期表非独作 | Newlands（1864 八音律）、Lothar Meyer（1864 28 元素表）先于或同期——门捷列夫的独特处是**预言未知元素 + 纠正已知原子量**，勿写「第一个发现元素周期性」 |
| 梦的引语 | 「I saw in a dream…」是 **Inostrantzev 转述**（as quoted by Inostrantzev）——引用必须注明转述，勿写成传记性事实 |
| Te/I 倒置 | 碲/碘按原子量应倒序，他**排对了位置但解释错了**（坚持认为当时原子量测错了）——勿写他「预见同位素」 |
| 以太/氪光假说 | aether 与 coronium 假说（比氢轻的两种元素）是**失败假说**——可作「思想家的大胆与局限」提及，勿神化 |
| 临终引语 | "Doctor, you have science, I have faith" **可能是 Jules Verne 语录**（page.md 明注 possibly）——引用必须带存疑注记，或改间接转述 |
| 石油警句 | 「烧石油当燃料如同烧钞票烧厨房炉灶」是 **credited remark**（转述）——注明转述属性 |
| 重婚争议 | 与 Anna 再婚时离婚手续未满教会七年要求——可写（它解释了俄科院落选），但只作背景事实，勿道德化渲染 |
| 母亲教诲引语 | "patiently search divine and scientific truth" 是 page.md 实载引语，可用 |
| Chugaev 评语 | "a chemist of genius, first-class physicist…" 为 Chugaev 对门捷列夫的评语，page.md 实载，可用但注明出自 Chugaev |
| 他评 | 他本人对 Arrhenius 电离理论的批评促成了 1906 的悲剧——两条事实线（学术批评→个人积怨→诺奖否决）因果按 page.md 措辞，勿添油加醋 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q9106 | ✅ |
| name_zh | 德米特里·伊万诺维奇·门捷列夫 | ✅ |
| name_en | Dmitri Mendeleev | ✅ |
| birth_date | 1834-02-08（O.S. 1834-01-27） | ✅ |
| death_date | 1907-02-02（O.S. 1907-01-20） | ✅ |
| nationality | Russian Empire | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | chemistry（person_field 细分：periodic law / physical chemistry / petroleum geology / metrology，带 rank） | ✅ |
| nobel_laureate | **0（非得主，特别篇）** | ✅ |
| has_biography | 执行立传后置 1 | 🔲 |

> 注：metadata.json `date_of_birth` 含噪声（["1834-01-27","1834-02-07","1834-00-00","1834-02-08"]）、`date_of_death` 含双历噪声（["1907-01-20","1907-02-02"]）——以 page.md 正文（新历 02-08 / 02-02 + O.S. 括注）为准。

## 7. 社会关系入库清单

**师长 / 同行 / 争论对象**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Alexander Voskresensky | 师→生（博士导师/讲席前任） | 1867 门捷列夫接替其无机化学讲席 |
| colleague | Lothar Meyer | 无向 | 1864 年 28 元素表先于门捷列夫发表、1869 后数月发表几乎相同的表——同期独立 |
| other | John Newlands | 无向 | 1864 八音律先驱，1887 才获承认 |
| colleague | Otto von Böhtlingk | 无向 | 梵文学家挚友；eka 命名致敬 Pāṇini |
| competitor | Svante Arrhenius | 无向 | 1906–1907 诺奖否决的关键反对者（积怨源于门捷列夫对电离理论的批评） |
| co-honored | Henri Moissan | 无向 | 1906 一票之差的竞争对手（Moissan 获奖） |
| colleague | Adolf von Baeyer / Alfred Werner | 无向 | 1900 柏林科学院 200 周年合影同框（page.md 图注实载） |

**门生**：page.md 正文与 metadata.json 均无 doctoral_student 记载——**不设门生清单，不虚构**。

## 8. 奖项清单

- Demidov Prize（1861，彼得堡科学院，因《Organic Chemistry》）
- Davy Medal（1882，Royal Society）
- Faraday Lectureship Prize（1889）
- Foreign Member of the Royal Society，ForMemRS（1892）
- Copley Medal（1905，Royal Society）
- Royal Swedish Academy of Sciences 院士（1905）；American Philosophical Society 国际会员
- 多枚圣安德烈/圣安娜/圣弗拉基米尔等帝国勋章（metadata.json 有载，Beamer 归并为一行即可，勿逐一展开）
- **身后**：Mendeleev Golden Medal（俄科院，1965 起）；mendelevium（Md, 101）与矿物 mendeleevite-Ce（2010）以他命名；月球背面环形山 Mendeleev
- **诺奖**：1905/1906/1907 三年 9 次提名，未获奖（1906 一票之差）——奖项页必须保留此行作为本篇主轴

## 9. 机构清单

- 教育：Tobolsk Gymnasium（1847/1850 前）→ Main Pedagogical Institute（1850–1855）→ 圣彼得堡大学（Doctor of Science 1865）
- 任职：Simferopol 第一文理中学科学教师（1855–1857）→ 海德堡（1859–1861 自主研究）→ 圣彼得堡技术学院教授（1864）→ 圣彼得堡大学副教授→教授（1865–1867 获终身教席，1890-08-17 辞职）→ 俄国度量衡总局局长（1893–1907，至死在任；1892 先执掌档案与度量衡）
- 创始：俄国化学会共同创始人（1868）；助建俄国第一座炼油厂
- 命名机构：D. I. Mendeleev Institute for Metrology（圣彼得堡）；D. Mendeleyev University of Chemical Technology（莫斯科）；圣彼得堡十二学院楼内 Memorial Museum Apartment

## 10. 终审清单

- [ ] 生卒 1834-02-08（O.S. 01-27）/ 1907-02-02（O.S. 01-20），享年 72，出生地 Verkhnie Aremzyani、去世地圣彼得堡（流感）
- [ ] 全篇无「诺贝尔奖得主」表述；1906 委员会推荐 / 一票之差 / Arrhenius 反对（含转述属性）表述准确
- [ ] 提名分解 3+4+2=9 次准确；1907 两次均被否
- [ ] eka 系对应准确：eka-aluminium→Ga(1875)、eka-silicon→Ge(1886)、eka-boron→Sc
- [ ] Newlands/Meyer 先驱地位不抹杀；门捷列夫独特处=预言+纠错
- [ ] 伏特加神话不出现（或以辟谣形式出现）；梦/临终语/石油警句均带转述或存疑注记
- [ ] 兄弟排行写「17 个孩子中最小」，不写精确存活数
- [ ] 引语全部可在 page.md 找到原文（母亲教诲、梦中表、Chugaev 评语、临终语——后两处带属性注记）
- [ ] 正文采用标杆式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误，vbox≤10pt、hbox≤50pt

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Dmitri_Mendeleev/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/Kramskoy_Mendeleev_01.jpg`（Kramskoi 1878 油画，images.txt 有 URL，250px→500px）；备选 Repin 1885（`Medeleeff_by_repin.jpg`，可作遗产页插图）；禁用父母画像（MendeleevaMD/MendeleevIP）、Anna 画像、奖章图作主肖像
- [ ] **国籍**：封面顶部明示俄罗斯帝国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（获奖理由不存在——本篇无诺奖理由行，封面副题改用「周期律」表述）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox≤10pt、hbox≤50pt）
- [ ] 身份信息页布局与标杆对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与标杆 Frederick Sanger 及 1901–1910 批次格式对齐

---

> **名单状态**：本篇为**特别篇（诺奖遗珠）**，不在 134 位得主名单内；`chemist/generate_20th_century_list.py` 不含 Dmitri Mendeleev，**不更新**。人物提示词已完成、Beamer 立传待执行。
> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
