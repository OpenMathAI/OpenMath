# Jacobus Henricus van 't Hoff（雅各布斯·亨里克斯·范特霍夫）立传提示词

> qid=Q102822 · 1852-08-30 – 1911-03-01 · 荷兰物理化学家/有机化学家 · 20 世纪 · 诺贝尔化学奖（1901，首位化学诺奖得主，独享）
> 官方获奖理由（总名单措辞）：表彰他因发现化学动力学定律和溶液渗透压定律所作出的杰出贡献
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Jacobus_Henricus_van_t_Hoff/`（page.md + metadata.json + images.txt）
> 版式基准：**参考数学家 Carl Friedrich Gauss（Q6722）的立传提示词与 Beamer 格式**（`mathematician/presentations/19th_century/Carl_Friedrich_Gauss/Carl_Friedrich_Gauss_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次立传的核心版式语言。

---

## 0. 正文形式说明（参考数学家高斯立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/Jacobus_Henricus_van_t_Hoff.jpg`，Wikipedia infobox 1904 年照片，执行阶段下载）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 物理化学的奠基者\enspace·\enspace 荷兰`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox（page.md），不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「分子在空间中的排列 / 溶液中的粒子」母题——不同大小的圆暗示四面体碳原子的三维构型与稀溶液中的溶质粒子。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）——范特霍夫方程、渗透压公式、化学亲和力概念本身就是最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Jacobus Henricus van 't Hoff Jr.（中文惯称：雅各布斯·亨里克斯·范特霍夫）
- **生卒**：1852-08-30 生于荷兰鹿特丹 → 1911-03-01 逝于德意志帝国柏林近郊 Steglitz（肺结核），享年 58
- **国籍**：Kingdom of the Netherlands（荷兰）
- **身份**：物理化学家 / 有机化学家 / 理论化学家（首位诺贝尔化学奖得主；立体化学与物理化学的共同奠基人之一）
- **家庭**：七个孩子中的第三个；父 Jacobus Henricus van 't Hoff Sr. 为医生，母 Alida Kolff van 't Hoff。1878 年娶 Johanna Francina Mees；两女 Johanna Francina（1880–1964）、Aleida Jacoba（1882–1971），两子 Jacobus Henricus III（1883–1943）、Govert Jacob（1889–1918）
- **早年气质**：自幼对科学与自然感兴趣，常参加植物学考察；少年时代醉心诗歌与哲学，视拜伦（Lord Byron）为偶像
- **教育轨迹**（违背父亲意愿选择化学）：
  - 1869 年 9 月入代尔夫特理工学院（Delft University of Technology），1871-07-08 通过毕业考试获化学工艺师学位（三年课程两年修完）
  - 随后入莱顿大学（University of Leiden）学化学
  - 赴德国波恩师从 August Kekulé，又赴巴黎师从 Adolphe Wurtz
  - 1874 年在 Eduard Mulder 指导下获乌得勒支大学（University of Utrecht）博士学位
- **导师**：Eduard Mulder（博士导师，乌得勒支大学）；游学导师：August Kekulé（波恩）、Adolphe Wurtz（巴黎）
- **博士论文**：page.md 未载论文题目——**禁写**
- **研究领域**：物理化学、有机化学、理论化学——立体化学、化学动力学、化学平衡、化学热力学、渗透压、化学亲和力

## 2. 核心叙事亮点（用于 Slide 4–13，约 13 条）

1. **鹿特丹医生之子（1852）**：七个孩子中的第三个；少年诗人气质——醉心诗歌与哲学、以拜伦为偶像，最终却违背父愿选择化学。
2. **代尔夫特的快进（1869–1871）**：三年制课程两年修完，1871-07-08 取得化学工艺师学位——技术与理论的双重底色由此奠定。
3. **游学欧陆（1871–1874）**：莱顿 → 波恩 Kekulé 门下 → 巴黎 Wurtz 门下 → 1874 乌得勒支大学 Eduard Mulder 指导下获博士。
4. **四面体碳原子（1874）**：以碳原子四个键指向正四面体顶点解释旋光性——立体化学的奠基之作；荷兰文小册子 1874 年秋发表（**早于博士学位三个月**），次年 5 月出法文小书 *La chimie dans l'espace*；与法国化学家 Joseph Le Bel **同年各自独立**提出，共享荣誉（Le Bel–Van 't Hoff rule）。
5. **预测轴手性（1875）**：正确预测丙二烯（allenes）与累积烯烃（cumulenes）的结构及其轴手性——理论超前于实验数十年的典范。
6. **Kolbe 的怒斥与迟到承认**：理论最初被学界普遍忽视，Kolbe 曾撰文尖刻嘲讽（"骑上珀伽索斯"一段，原文见 page.md，可引）；约 1880 年起因 Wislicenus、Viktor Meyer 等重要化学家的支持而获得承认。
7. **《化学动力学研究》（1884）**：*Études de Dynamique chimique*——用图解法测定反应级数，把热力学定律应用于化学平衡，并引入化学亲和力的现代概念。
8. **稀溶液与气体的类比（1886）**：证明稀溶液的行为与气体遵循高度相似的数学规律——渗透压理论的核心洞察。
9. **《物理化学杂志》创刊（1887）**：与 Ostwald（导言另载 Arrhenius）在莱比锡创办 *Zeitschrift für physikalische Chemie*——该学科第一份专门期刊，物理化学作为学科成型的标志。
10. **支持电离理论（1889）**：研究 Arrhenius 的电解质电离理论，并为 Arrhenius 方程提供物理依据。
11. **移居柏林（1896）**：任普鲁士科学院教授；对 Stassfurt 盐矿沉积的研究是普鲁士化学工业的重要贡献；1896–1911 在柏林大学结束职业生涯。
12. **1901 首位诺贝尔化学奖**：独享；官方理由 "for his] discovery of the laws of chemical dynamics and osmotic pressure in solutions"（表彰他因发现化学动力学定律和溶液渗透压定律所作出的杰出贡献）；1901-12-13 诺贝尔演讲《渗透压与化学平衡》。
13. **身后之名**：以他命名——Van 't Hoff equation、Van 't Hoff factor、Le Bel–Van 't Hoff rule；2021-05-14 小行星 34978 van 't Hoff 以他命名（Palomar–Leiden 巡天 1977 年发现）；自认获得首个化学诺奖是其生涯的顶点。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深孔雀蓝 deeppetrol） | `#0E4D64` | 溶液 / 渗透压 / 物理化学的液体气质——沉稳而有深度（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签）——首位化学诺奖 |
| 分类色 1（立体化学 badgeStereo） | `#4C5FD5` | 蓝四面体碳 / 手性 / La chimie dans l'espace |
| 分类色 2（化学动力学 badgeKinetics） | `#1B7A43` | 绿反应级数 / Études de Dynamique chimique |
| 分类色 3（溶液与渗透压 badgeOsmotic） | `#0E7C7B` | 青稀溶液定律 / 范特霍夫方程 / 范特霍夫因子 |
| 分类色 4（学科建制 badgeDiscipline） | `#C0395B` | 玫瑰《物理化学杂志》创刊 / 柏林时期 |
| 背景 | `#F7F6F9` | 浅灰白（与高斯一致） |

- **选择理由**：深孔雀蓝取自「溶液」的视觉直觉——渗透压、稀溶液定律是 van 't Hoff 获奖理由的核心意象，又与已用人物主色（深藏青 #1E3A5F、京都红等）区分明显。
- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「四面体构型 / 溶液中的粒子」的三维分布。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Expedition** — Alex-Productions（本地文件 `music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav`）
- **风格**：探索 / 远征 / 史诗
- **匹配理由**：
  - "远征" 匹配其生涯轨迹——鹿特丹 → 代尔夫特 → 莱顿 → 波恩 → 巴黎 → 乌得勒支 → 阿姆斯特丹 → 柏林，一路向未知领域的学术远征
  - "探索" 匹配其贡献本质——四面体碳（分子空间）、渗透压（溶液定律）、化学动力学，每一次都是在没有地图的领域开路
  - 模板 §5.3 明确将 van 't Hoff 列为「探索/远征」气质的推荐人选（Expedition）
- **注意**：**不要复制 wav 文件**——wav 复制在执行立传阶段进行（`cp` 到本目录后 `make video` 自动检测）

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 物理化学的奠基者 / Jacobus Henricus van 't Hoff 1852–1911 + 四色 badge + 右上头像 + 国籍行（荷兰）
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  范特霍夫的一生 — 高斯式时间线（10 节点：1852 鹿特丹 → 1869 代尔夫特 → 1874 博士+四面体论文 → 1875 La chimie dans l'espace → 1884 Études → 1887 Zeitschrift 创刊 → 1893 Davy Medal → 1896 移居柏林 → 1901 首位化学诺奖 → 1911 逝于 Steglitz）
04  早年：医生之家的诗人少年 (1852–1869) — 表格「时间|事件|结果」
05  求学之路：代尔夫特与欧陆游学 (1869–1874) — 表格「时间|事件|结果」
06  四面体碳原子 (1874–1875) — 表格「问题|方法|结果」+ 公式框：正四面体构型 / Le Bel–Van 't Hoff rule
07  Kolbe 的批评与迟到承认 (1874–1880) — 表格「批评|回应|结果」（Kolbe 原文引语 + Wislicenus/Viktor Meyer 支持）
08  《化学动力学研究》(1884) — 表格「问题|方法|结果」+ 公式框：反应级数图解法 / 化学亲和力现代概念
09  稀溶液与渗透压 (1886–1887) — 表格「问题|方法|结果」+ 公式框：范特霍夫方程（van 't Hoff equation）
10  物理化学的建制化 (1887–1889) — 表格「事件|伙伴|结果」（Zeitschrift 创刊 / Arrhenius 电离理论支持）
11  柏林时期 (1896–1911) — 表格「职务|工作|结果」（普鲁士科学院 / Stassfurt 盐矿 / 柏林大学）
12  荣誉 — 高斯式「类别|代表|意义」表格（Nobel 1901 / Davy 1893 与 Le Bel 共享 / ForMemRS 1897 / Helmholtz 1911 + 荣誉博士清单）
13  遗产 — 四分类遗产盒 + 公式框：范特霍夫因子 / 小行星 34978 van 't Hoff（2021）
14  结尾 — 金句页（建议从其贡献本质提炼：「化学第一次被安放进三维空间。」——此为编者提炼的结语，非其原话，不得加引号呈现为引语）
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 四面体碳归属 | **1874 年与 Joseph Le Bel 同年各自独立提出**，共享荣誉（Le Bel–Van 't Hoff rule）——勿写范特霍夫一人首创，也勿写 Le Bel 首创 |
| 1874/1875 出版顺序 | 荷兰文小册子 **1874 年秋**（早于博士学位三个月）→ 法文小书 *La chimie dans l'espace* **次年 5 月（1875）** → 德译本 1877——三个年份勿混，博士（1874）在前还是在后要写清"早于学位三个月" |
| 诺奖理由 | 官方措辞：发现化学动力学定律和溶液渗透压定律（"discovery of the laws of chemical dynamics and osmotic pressure in solutions"）；Career 段另有 "for his work with solutions" 的简写——以 intro 官方措辞为准，勿泛化成"因渗透压工作获奖" |
| 首位化学诺奖 | 1901 年**独享**，是**第一任**诺贝尔化学奖得主——勿写"与其他人共享首届" |
| 《物理化学杂志》创刊人 | 导言载 **Van 't Hoff、Arrhenius 和 Ostwald 三人** 1887 年创办；Career 段只写"他与 Ostwald 创办"——建议按导言写三人共创，勿写成"与 Ostwald 两人"独家 |
| 与 Arrhenius 关系 | page.md 仅载：他研究了 Arrhenius 的电解质电离理论、1889 年为 Arrhenius 方程提供物理依据——**是支持与论证，正文无"论战"记载**；勿杜撰"与 Arrhenius 论战"情节 |
| Kolbe 引语 | Kolbe 嘲讽原文在 page.md 有完整英文原文（"骑上珀伽索斯/chemical Parnassus"段），可整段引用；除此之外**无任何范特霍夫本人直接引语**——中文引号内不得出现无法在 page.md 溯源的"原话" |
| 阿姆斯特丹教授职位 | 教的是**化学、矿物学与地质学**三科，后任化学系主任，任职近 18 年——勿只写"化学教授" |
| 柏林职务 | 1896 年任**普鲁士科学院**教授（Prussian Academy of Sciences），职业生涯**在柏林大学结束（至 1911）**；metadata employer 另列 Humboldt/Frederick William——勿笼统写"1896 年任柏林大学教授"而不区分机构 |
| 乌得勒支兽医学校 | 早年只能在 Utrecht 的 **Veterinary School**（兽医学院）找到教职任化学与物理讲师——勿写成"乌得勒支大学教授" |
| 去世地与死因 | 1911-03-01 逝于柏林近郊 **Steglitz**，**死于肺结核**，享年 58——勿写"逝于鹿特丹"或漏掉死因 |
| Davy Medal | 1893 年**与 Le Bel 共同获得**——勿写独得 |
| 博士论文题目 | page.md 与 metadata.json 均未载博士论文题目——**禁写** |
| 学生名单 | page.md 正文 infobox 的 Doctoral students 仅 **Ernst Cohen** 一人，另有 Other notable students **Frederick G. Donnan**；metadata.json `doctoral_student` 另列 7 人（Harold A. Wilson、P.C.F. Frowein、Albertus van Bijlert、Gerrit Hondius Boldingh、Johannes Jacobus van Laar、Wilder Dwight Bancroft）但正文无载——入库口径见 §7，Beamer 正文学生页只写有正文依据者 |
| 名字拼写 | 荷兰语姓氏 van 't Hoff 含空格与省字符（van 空 't 空 Hoff）；文件名用 `Jacobus_Henricus_van_t_Hoff`（无省字符）——tex 中姓名勿写成 "Van't Hoff" 或 "vant Hoff" |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q102822 | ✅ |
| name_zh | 雅各布斯·亨里克斯·范特霍夫 | ✅ |
| name_en | Jacobus Henricus van 't Hoff | ✅ |
| birth_date | 1852-08-30 | ✅ |
| death_date | 1911-03-01 | ✅ |
| nationality | Kingdom of the Netherlands | ✅ |
| primary_occupation | chemist（metadata 另含 physicist/stereochemist 等带 rank） | ✅ |
| field_of_work | physical chemistry / organic chemistry（metadata；person_field 细分：stereochemistry / chemical kinetics / osmotic pressure / chemical thermodynamics，带 rank） | ✅ |
| has_biography | 1（执行立传后置 1） | 🔲 待置 |

## 7. 社会关系入库清单

**师长 / 合作者 / 学术对手**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Eduard Mulder | 师→生（博士导师） | 1874 年乌得勒支大学博士 |
| advisor-student | August Kekulé | 师→生（游学导师） | 波恩时期师从，非博士导师 |
| advisor-student | Adolphe Wurtz | 师→生（游学导师） | 巴黎时期师从，非博士导师 |
| colleague | Wilhelm Ostwald | 无向 | 1887 年共创《物理化学杂志》 |
| colleague | Svante Arrhenius | 无向 | 支持其电离理论；1889 年为其方程提供物理依据；导言载亦为期刊共创人 |
| co-honored | Joseph Le Bel | 无向 | 1874 年各自独立提出四面体碳；1893 年共获 Davy Medal |
| competitor | Hermann Kolbe | 无向 | 1870 年代末撰文尖锐批评四面体学说 |

**门生（van 't Hoff → 学生）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Ernst Cohen | van 't Hoff → 学生 | page.md 正文 infobox Doctoral students 唯一一人 |
| advisor-student | Frederick G. Donnan | van 't Hoff → 学生 | 正文列为 Other notable students（非博士门下列名） |

> metadata.json `doctoral_student` 另含 Harold A. Wilson、Pieter Coenraad Frederik Frowein、Albertus van Bijlert、Gerrit Hondius Boldingh、Johannes Jacobus van Laar、Wilder Dwight Bancroft 六人，但 **page.md 正文无载**——如入库按 metadata 口径可一并收录，note 必须注明"仅 Wikidata/metadata 有载"；Beamer 正文学生页只用 Ernst Cohen 与 Donnan。

## 8. 奖项清单

- Nobel Prize in Chemistry（1901，首位，独享）
- Davy Medal，Royal Society（1893，与 Joseph Le Bel 共同获得）
- Knight of the French Legion of Honour（1894）
- Pour le Mérite（1895）
- Foreign Member of the Royal Society，ForMemRS（1897）
- Helmholtz Medal，Prussian Academy of Sciences（1911）
- Senator in the Kaiser-Wilhelm-Gesellschaft（1911）
- Member of the Royal Netherlands Academy of Arts and Sciences（1885；1892 起荣誉会员）
- Honorary Member：Manchester Literary and Philosophical Society（1892）、British Chemical Society（伦敦）、American Chemical Society（1898）、Académie des Sciences（巴黎，1905）、Netherlands Chemical Society（1908）、Physics Association Frankfurt（metadata 载，年份无）
- Member of the American Philosophical Society（1904）
- 荣誉博士：Harvard 与 Yale（1901）、Victoria University / University of Manchester（1903）、University of Heidelberg（1908）
- Bavarian Maximilian Order for Science and Art（metadata 载，年份无）

## 9. 机构清单

- 教育：Delft University of Technology（1869–1871，化学工艺师）、University of Leiden、University of Bonn（Kekulé）、University of Paris（Wurtz）、University of Utrecht（PhD 1874，Eduard Mulder）
- 任职：Veterinary College in Utrecht（化学与物理讲师）；University of Amsterdam（化学、矿物学、地质学教授近 18 年，后任化学系主任）；Prussian Academy of Sciences（1896 教授）；University of Berlin（1896–1911）
- 以他命名：Van 't Hoff equation、Van 't Hoff factor、Le Bel–Van 't Hoff rule；小行星 34978 van 't Hoff（2021-05-14 命名）

## 10. 终审清单

- [x] 生卒 1852-08-30 / 1911-03-01，享年 58，出生地鹿特丹、去世地柏林 Steglitz、死于肺结核
- [x] 1901 首位化学诺奖**独享**；获奖理由用总名单措辞「表彰他因发现化学动力学定律和溶液渗透压定律所作出的杰出贡献」
- [x] 四面体碳 1874 与 Le Bel 同年各自独立；Davy Medal 1893 与 Le Bel 共享
- [x] 1874 荷兰文小册子早于博士三个月；*La chimie dans l'espace* 为 1875 法文本
- [x] 《物理化学杂志》1887 三人共创（Van 't Hoff / Arrhenius / Ostwald）
- [x] 与 Arrhenius 仅"支持/论证"关系，无"论战"情节；无载禁写
- [x] 阿姆斯特丹三科教授（化学/矿物学/地质学）；1896 普鲁士科学院；兽医学校职衔准确
- [x] 博士论文题目不出现；学生页只用有正文依据者（本次 15 页未设独立学生页，Cohen/Donnan 未写错）
- [x] 引语全部可在本地 page.md 原文找到（仅 Kolbe 评语为唯一直接引语）
- [x] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误（Overfull 仅 hbox 5.8pt / vbox 0.4-0.9pt，均达标）

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Jacobus_Henricus_van_t_Hoff/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [x] **头像（已执行 ✅）**：已按 images.txt URL（250px→500px）下载 infobox 1904 年照片至 `images/Jacobus_Henricus_van_t_Hoff.jpg`（JPEG 500×763 验证通过）；封面/身份页图注统一用 "Van 't Hoff (1852–1911)" 与 "Van 't Hoff in 1904"——注：完整姓名小字注 "Jacobus Henricus van 't Hoff (…)" 会超出封面右缘，已改短。**执行期新陷阱（Review-2 复用）**：①荣誉页三行 itemize 表格默认 topsep 会致 vbox 超 20pt——须 `\setlength{\topsep}{0pt}\setlength{\partopsep}{0pt}` + arraystretch 0.65 + 列宽 2.4/2.6cm 压缩；②表格单元格长句避免行尾孤字（如"…博士学位"拆出"位"字），改写句式规避
- [ ] **国籍**：封面顶部明示荷兰（Kingdom of the Netherlands）
- [ ] **引语核对**：中文引号内只允许出现 Kolbe 评语的原文（英文）或其忠实翻译；其余一律间接转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox ≤10pt、hbox ≤50pt 可接受）
- [ ] 身份信息页布局与高斯模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一；荷兰姓氏 "van 't Hoff" 断行不断开
- [ ] 与数学家侧（高斯）及化学家侧既有格式对齐（Sanger 版）

---

> **名单状态**：本提示词已完成；Beamer 立传**待执行**。`chemist/generate_20th_century_list.py` 的 `BIOGRAPHIES_DONE` **暂不更新**（立传完成后由主流程同步）。
> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
