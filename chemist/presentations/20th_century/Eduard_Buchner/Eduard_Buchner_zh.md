# Eduard Buchner（爱德华·布赫纳）立传提示词

> qid=Q43917 · 1860-05-20 – 1917-08-13 · 德国化学家 / 生物化学家 · 20 世纪 · 诺贝尔化学奖（1907，表彰他的生物化学研究，以及他发现无细胞发酵）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Eduard_Buchner/`（page.md + metadata.json + images.txt；images.txt 为空）
> 版式基准：**参考数学家 Carl Friedrich Gauss（Q6722）的立传提示词与 Beamer 格式**（`mathematician/presentations/19th_century/Carl_Friedrich_Gauss/Carl_Friedrich_Gauss_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次重写的核心版式语言。

---

## 0. 正文形式说明（参考数学家高斯立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。Buchner 的 `images.txt` 为空、无真实肖像 URL——封面用**装饰圆占位**（主色实心圆 + `\faIcon{user}` + 姓名首字母 EB），Review-1 时经 Wikipedia REST API / Commons Special:FilePath 回退，404 则维持装饰圆。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 无细胞发酵的发现者\enspace·\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像（或装饰圆）+ 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「压榨 / 浸出」母题——圆点如酵母细胞被研钵破壁后渗出的汁液微滴。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Eduard Buchner（中文惯称：爱德华·布赫纳；德语发音 [ˈeːduaʁt ˈbuːxnɐ]）
- **生卒**：1860-05-20 生于慕尼黑（Munich，巴伐利亚王国）→ 1917-08-13 逝于罗马尼亚 Focșani 野战医院（08-11 中弹，两日后不治），享年 57
- **国籍**：German Empire（德国 / 德意志帝国）
- **身份**：化学家、发酵专家（page.md 称有时被叫作 zymologist）、生物化学家；metadata.json 另载 mineralogist、agronomist、university teacher
- **家庭**：父亲是医生、法医学特聘讲师（Doctor Extraordinary of Forensic Medicine）；兄长为细菌学家 Hans Ernst August Buchner。1900 年娶 Lotte Stahl
- **教育轨迹**（page.md 正文 + metadata.json educated_at）：
  - 1884 起在慕尼黑植物学研究所随 Adolf von Baeyer 学化学、随 Carl Nägeli 学植物学
  - 之后赴埃尔朗根大学（University of Erlangen，今 Erlangen–Nuremberg）与 Otto Fischer（Emil Fischer 的堂兄）共事一段时间
  - 1888 获慕尼黑大学（Ludwig-Maximilians-Universität München）博士学位，导师 **Theodor Curtius**
- **导师**：博士导师 Theodor Curtius；学习上的老师 Adolf von Baeyer（化学）、Carl Nägeli（植物学）
- **研究领域**：生物化学、发酵（cell-free fermentation、zymase、酶）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **慕尼黑医生之子（1860）**：父亲为医生兼法医学特聘讲师，兄长 Hans 是细菌学家——医学与生命的家庭底色。
2. **双轨求学（1884）**：在慕尼黑植物学研究所同时师从 Baeyer 学化学、Nägeli 学植物学——化学与生命科学的交叉从求学起就已注定。
3. **埃尔朗根插曲**：与 Otto Fischer（Emil Fischer 之堂兄）在埃尔朗根大学共事，随后 1888 年在慕尼黑大学 Theodor Curtius 指导下获博士学位。
4. **Baeyer 实验室（1889–1893）**：1889 年任 Baeyer 有机实验室助教（assistant lecturer），1891 年升讲师。
5. **学院迁徙（1893–1911）**：1893 秋赴基尔大学、1895 任教授；1896 年任图宾根大学分析与药物化学特聘教授（Pechmann 实验室）；1898 年 10 月任柏林农业大学普通化学讲席教授（自行培养全部助手），1900 年获任教资格（habilitation）；1909 转布雷斯劳大学，1911 迁维尔茨堡大学。
6. **1897 年里程碑论文**：《Alkoholische Gährung ohne Hefezellen（无酵母细胞的酒精发酵·初步报道）》，发表于 Berichte der Deutschen Chemischen Gesellschaft 第 30 卷 117–124 页。
7. **无细胞发酵实验（1897）**：干酵母 + 石英 + 硅藻土，用研钵研磨破壁；混合物受潮后压榨，得到的 "press juice"（压榨汁）加入葡萄糖、果糖或麦芽糖后持续冒出 CO₂（有时长达数天）；显微检查证实汁液中**没有活酵母细胞**。
8. **对生机论的又一击**：证明发酵不需要活酵母细胞的存在——生命过程可以离开完整细胞在体外发生，这是生化史上决定性的一步。
9. **分泌假说与其修正**：Buchner 设想酵母细胞把蛋白质（酶）分泌到环境中发酵糖分；后来发现发酵其实发生在酵母细胞**内部**——结论细节有误，实验事实不变。
10. **与 Manasseina 的优先权之争**：Maria Manasseina 声称早一代人已发现无细胞发酵；Buchner 与 Rapp 认为她只是主观确信存在发酵酶、实验证据不令人信服。
11. **1905 Liebig 奖章 → 1907 诺贝尔化学奖**（独享）：获奖工作即上述压榨汁发酵糖实验。
12. **一战从军（1914–1917）**：开战即志愿加入德意志帝国陆军，官至少校（Major），先西线后东线指挥弹药运输队；1916 年 3 月回维尔茨堡大学，1917 年 4 月再度从军。
13. **Focșani 的终结（1917-08-13）**：在罗马尼亚 Focșani（Mărășești 战役）被弹片击中左大腿，两日后卒于野战医院，安葬于 Focșani 德军公墓——诺奖十年后倒在战场。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深琥珀褐 deepamber） | `#5C3A1E` | 酵母压榨汁 / 发酵醪液的醇厚（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（无细胞发酵 badgeCellfree） | `#8C5A2B` | 琥珀 press juice / 1897 论文 |
| 分类色 2（酶与 zymase badgeEnzyme） | `#3E6B4F` | 绿 zymase / 分泌假说 |
| 分类色 3（生机论的终结 badgeVitalism） | `#7A3B5E` | 紫红 vitalism / 优先权之争 |
| 分类色 4（战争与牺牲 badgeWar） | `#555F6E` | 钢灰一战 / Focșani |
| 背景 | `#F7F6F9` | 浅灰白（与高斯一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「破壁渗出」——被研磨的酵母细胞渗出的汁液微滴。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Tragedy** — Alex-Productions（本地文件 `music_audio/alex-productions/80-K5f65-22sY4-Tragedy.wav`）
- **风格**：深色 / 戏剧性 / 悲剧人物
- **匹配理由**：
  - "悲剧人物" 匹配 Buchner 命运的完整弧线——1897 发现无细胞发酵 → 1907 诺奖巅峰 → 1917-08-13 倒在罗马尼亚前线，诺奖十年后卒于战场
  - "深色" 匹配其科学主题——给生机论以沉重一击，终结"发酵必须依赖活体"的古老信条
  - "失败与突破" 匹配优先权之争与分泌假说被修正的曲折
- **时长对齐**：BGM 略短于 slides 总时长时 ffmpeg `-shortest` 自动对齐
- **注意**：wav 复制在执行立传阶段进行（`cp` 到 `Eduard_Buchner/` 子目录），本提示词阶段不复制

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 无细胞发酵的发现者 / Eduard Buchner 1860–1917 + 四色 badge + 右上头像（或装饰圆）+ 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  布赫纳的一生 — 高斯式时间线（10 节点：1860→1884→1888→1893→1897→1900→1905→1907→1909→1917）
04  早年：慕尼黑医生之子 (1860–1884) — 表格「时间|事件|结果」
05  求学与师承：Baeyer、Nägeli 与 Curtius (1884–1889) — 表格「阶段|老师|收获」
06  无细胞发酵实验 (1897) — 表格「问题|方法|结果」+ 公式框：press juice + 糖 → CO₂（无活细胞）
07  生机论的黄昏与 1907 诺奖 — 表格「旧观念|新事实|影响」+ 公式框：1907 诺贝尔化学奖（独享）
08  学院生涯与迁徙 (1889–1911) — 表格「年份|机构|职务」（Kiel/Tübingen/柏林农大/Breslau/Würzburg）
09  学说细节：分泌假说 vs 细胞内发酵 — 表格「观点|提出者|后续裁定」
10  优先权之争：Manasseina — 表格「人物|主张|裁定」
11  荣誉 — 高斯式「类别|代表|意义」表格（Liebig Medal 1905 / Nobel 1907）
12  一战与牺牲 (1914–1917) — 表格「年份|经历|结果」（西线→东线、Major、Focșani 中弹）
13  遗产：生物化学的诞生 — 四分类遗产盒 + 公式框：cell-free system 概念的源头
14  结尾 — 金句收束（关于「离开活细胞，生命化学依然运转」的忠实转述，不杜撰引语）
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| **博士导师冲突（P0）** | page.md infobox 与正文均为 **Theodor Curtius**（1888 慕尼黑博士）；metadata.json `doctoral_advisor` 写的是 Adolf von Baeyer——**冲突时以 page.md 为准**，博士导师写 Curtius；Baeyer 记为 1884 年起学化学的老师与 1889 年任职的实验室主人 |
| 1907 独享 | 1907 诺贝尔化学奖为 Buchner **一人独得**，page.md 无共享者——勿添加共同得主 |
| 诺奖理由措辞 | 中文照总名单：**"表彰他的生物化学研究，以及他发现无细胞发酵"**；勿写"发现酶"或"发明发酵" |
| zymase 争议禁写 | 与拜耳（Bayer 染料公司）实验室的 "但醇" 之争、Störmann 等具体争议人物，**page.md 均无载——禁写**；page.md 只在 Known for 中出现 zymase 一词，其化学细节不得展开杜撰 |
| 分泌假说被修正 | Buchner 设想酵母**向环境分泌**蛋白质发酵糖；后来发现发酵发生在细胞**内部**——可写且必须写准方向，勿写反 |
| Manasseina 之争 | 她声称早一代发现无细胞发酵；Buchner 与 Rapp 认为其"主观确信存在发酵酶、实验证据不令人信服"——只写 page.md 这一层，勿再加戏 |
| 卒日细节 | 1917-08-11 在 Focșani 被弹片击中**左大腿**，**两日后**（08-13）卒于野战医院；卒于 **Battle of Mărășești**；安葬 Focșani 德军公墓——三个细节勿混淆（勿写"当场死亡"、勿写右腿） |
| 从军时间线 | 1914 开战即志愿参军 → 官至少校 Major → 西线后东线指挥弹药运输队 → 1916-03 回维尔茨堡 → 1917-04 再度从军——年份顺序勿倒置 |
| Büchner 器具陷阱 | Büchner flask / Büchner funnel 纪念的是工业化学家 **Ernst Büchner**，**不是** Eduard Buchner——立传中禁写"以他命名" |
| 机构对照 | metadata.json `employer` 写 Humboldt-Universität zu Berlin，page.md 写 **Agricultural University of Berlin**（柏林农业大学，1898 讲席）——以 page.md 为准 |
| 任职年份链 | 1889 LMU 助教 → 1891 LMU 讲师 → 1893 秋 Kiel → 1895 Kiel 教授 → 1896 Tübingen 特聘教授 → 1898-10 柏林农大讲席、1900 habilitation → 1909 Breslau → 1911 Würzburg——勿压缩或调序 |
| 迁徙地名 | Breslau 1945 年改组为 Wrocław——page.md 有载，可加注；勿写成"今克拉科夫"等 |
| 论文年份 | 1897 初步报道（Ber. 30: 117–124）；1899 与 Rudolf Rapp 的后续论文（Ber. 32: 2086–2094）——两条均在 Publications 有载，年份勿混淆 |
| 引语纪律 | 中文引号内禁止出现任何"布赫纳原话"——page.md 正文**没有任何直接引语**，一律间接转述（含获奖理由） |
| 享年口径 | 1860-05-20 至 1917-08-13，享年 57（infobox 标 aged 57）——勿写 58 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q43917 | ✅ |
| name_zh | 爱德华·布赫纳 | ✅ |
| name_en | Eduard Buchner | ✅ |
| birth_date | 1860-05-20 | ✅ |
| death_date | 1917-08-13 | ✅ |
| nationality | German Empire | ✅ |
| primary_occupation | chemist / biochemist | ✅ |
| field_of_work | chemistry, biochemistry（person_field 细分建议：fermentation / biochemistry / enzyme，带 rank） | ✅ |
| has_biography | 1 | ✅ 执行立传后置 1 |

## 7. 社会关系入库清单

**师长 / 合作者 / 亲属 / 争议方**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Theodor Curtius | 师→生（博士导师） | 1888 慕尼黑大学博士（page.md infobox 与正文一致） |
| advisor-student | Adolf von Baeyer | 师→生（化学学习 / 实验室） | 1884 随其学化学；1889 任其有机实验室助教（metadata 误记为博士导师，以 page.md 为准） |
| advisor-student | Carl Nägeli | 师→生（植物学） | 1884 同在慕尼黑植物学研究所随学 |
| advisor-student | Otto Fischer | 师→生（短期共事） | 埃尔朗根大学期间；Emil Fischer 之堂兄 |
| colleague | Rudolf Rapp | 无向 | 1899 无细胞发酵后续论文合作者；共同回应 Manasseina |
| competitor | Maria Manasseina | 无向 | 无细胞发酵优先权之争（其证据被裁定不令人信服） |
| other | Hans Ernst August Buchner | 无向（兄长） | 细菌学家 |
| other | Lotte Stahl | 无向（配偶） | 1900 年结婚 |

> metadata.json `doctoral_advisor` 仅列 Adolf von Baeyer，与 page.md infobox（Theodor Curtius）冲突——以 page.md 为准入库（上表已按 page.md 处理）。

## 8. 奖项清单

- Liebig Medal（1905）
- Nobel Prize in Chemistry（1907，独享；理由：表彰他的生物化学研究，以及他发现无细胞发酵）

> metadata.json `award_received` 与 page.md infobox 一致，仅此两项，勿增补。

## 9. 机构清单

- 教育：Ludwig-Maximilians-Universität München（1888 博士）；University of Erlangen（与 Otto Fischer 共事；metadata 另载 Technical University of Munich，正文无展开，仅列不入叙事）；慕尼黑植物学研究所（1884，Baeyer / Nägeli）
- 任职：LMU 有机实验室助教（1889）→ 讲师（1891）→ Kiel University（1893 秋赴任，1895 教授）→ University of Tübingen（1896，分析与药物化学特聘教授，Pechmann 实验室）→ Agricultural University of Berlin（1898-10 普通化学讲席教授，1900 habilitation）→ University of Breslau（1909，今 Wrocław）→ University of Würzburg（1911）
- 命名机构：**无**——Büchner flask / funnel 纪念 Ernst Büchner，与本人无关（§5 已列陷阱）；1897 论文与 Nobel Lecture（1907-12-11，Cell-Free Fermentation）见 page.md External links

## 10. 终审清单

- [x] 生卒 1860-05-20 / 1917-08-13，享年 57，出生地慕尼黑、去世地 Focșani 野战医院
- [x] 博士导师 Theodor Curtius（非 Baeyer——metadata 冲突已按 page.md 裁定）
- [x] 1907 诺奖独享、理由中文措辞照总名单
- [x] 无细胞发酵实验流程（石英 + 硅藻土 + 研钵 → 压榨汁 → 加糖 → CO₂ 数天 → 显微镜无活细胞）逐项核对
- [x] 分泌假说→细胞内发酵的方向未写反
- [x] Büchner flask/funnel 归属 Ernst Büchner，未误写
- [x] 从军时间线（1914 志愿 → Major → 西线东线 → 1916-03 回校 → 1917-04 再从军 → 08-11 中弹 → 08-13 卒）未倒置
- [x] 机构年份链（1889/1891/1893/1895/1896/1898/1900/1909/1911）与 page.md 一致
- [x] 无任何中文引号内的"原话"（page.md 无直接引语）
- [x] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [x] **结合本地 Wikipedia**：读取 `pages/Eduard_Buchner/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [x] **头像**：`images.txt` 为空、无肖像 URL——执行 **Wikipedia REST API（page/summary 查 infobox 原图名）或 Commons `Special:FilePath/<文件名>?width=600` 回退**；404/HTML 则用装饰圆占位（主色 #5C3A1E 实心圆 + EB 首字母）
- [x] **国籍**：封面顶部明示德国（German Empire）
- [x] **引语核对**：本篇**不应出现任何引号内原话**；获奖理由用总名单中文措辞
- [x] **编译验证**：`make distclean && make`
- [x] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [x] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [x] 身份信息页布局与高斯模板对齐（左头像 + 右 2×2 网格）
- [x] 中文标点 / 断行 / 间距统一
- [x] 与化学家侧（Frederick Sanger）及数学家侧（高斯）既有格式对齐

---

> **名单状态**：本提示词已完成；Beamer 立传待执行。`chemist/generate_20th_century_list.py` 的 `BIOGRAPHIES_DONE` **暂不更新**（执行立传完成后再同步）。
> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
