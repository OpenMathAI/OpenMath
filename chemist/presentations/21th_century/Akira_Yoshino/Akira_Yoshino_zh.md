# Akira Yoshino（吉野彰）立传提示词

> qid=Q4701206 · 1948-01-30 –（在世）· 日本 · 诺贝尔化学奖（2019，与 John B. Goodenough、M. Stanley Whittingham 共享）· 本地数据源：`chemist/presentations/21th_century/pages/Akira_Yoshino/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：对齐 `chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}` 高斯式骨架——表格语义化 tabularx + 公式展示框 + 时间线页 + 气泡背景。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像用本地 `images.txt` 首图 Akira Yoshino 2019 照；下载失败则装饰圆占位并在 Review 注明）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{battery-full}\enspace 锂离子电池的诞生\enspace·\enspace 日本`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。封面上可加日文原名「吉野 彰」小字注。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、日文原名（吉野 彰）、国籍、出生地（大阪府吹田市）、教育（京都大学 BS/MS、大阪大学 Dr.Eng.）、任职（旭化成 / 明城大学）、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「碳阳极 — 离子」母题——离散圆点暗示石油焦碳材料中容纳锂离子的空隙。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配金色边框浅金底公式展示框（`\fcolorbox` + minipage），如 1983 原型（LiCoO₂ 阴极 + 聚乙炔阳极）→ 1985 原型（碳质阳极）的演进式。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Akira Yoshino（吉野 彰，Yoshino Akira；中文惯称：吉野彰）
- **生卒**：1948-01-30 生于大阪府吹田市（Suita, Osaka Prefecture；在世，卒日留白）
- **国籍**：Japan（日本）
- **身份**：化学家、工程师、发明家；旭化成（Asahi Kasei）Fellow（2017 年起 Honorary Fellow）；名城大学（Meijo University, Nagoya）教授
- **教育轨迹**：
  - 大阪市立北野高中（Kitano High School，1966 毕业）
  - 京都大学工学部：BS（1970）、MS（1972）
  - 大阪大学：Dr.Eng.（工学博士，2005）
- **启蒙**：小学时老师建议读法拉第《The Chemical History of a Candle》（蜡烛的化学史），点燃了对原本不感兴趣的化学的好奇
- **大学因缘**：京都大学期间修读过福井谦一（Kenichi Fukui）的课程——福井是首位获诺贝尔化学奖的东亚裔得主（页面明载口径）
- **博士导师**：页面无载——**留白，禁杜撰**
- **研究领域**：电化学——锂离子电池、导电聚合物、功能材料

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **吹田出生（1948）**：生于大阪府吹田市（占领时期日本）；1966 年毕业于大阪北野高中。
2. **法拉第的蜡烛（小学）**：老师推荐法拉第《蜡烛的化学史》，让原本对化学无感的少年萌生无数疑问——科学启蒙的原点。
3. **京都大学（1966–1972）**：工学学士（1970）与硕士（1972）；修读过福井谦一的课程（首位东亚裔诺贝尔化学奖得主）。
4. **入职旭化成（1972）**：硕士毕业即进入旭化成，**全部非学术生涯都在这一家公司**——日本企业研究者的典型路径。
5. **聚乙炔起步（1981）**：开始用聚乙炔做充电电池研究；聚乙炔是白川英树发现的导电聚合物（白川因此获 2000 诺贝尔化学奖）。
6. **1983 原型**：以 LiCoO₂ 为阴极、聚乙炔为阳极制作原型可充电池——阳极材料本身不含锂、充电时锂离子从 LiCoO₂ 阴极迁入阳极——**现代锂离子电池的直接前身**。
7. **1985 碳阳极突破**：聚乙炔真密度低（高容量需大体积）且不稳定，改用特定晶体结构的碳质材料为阳极，制成**第一个锂离子电池原型**并获基础专利——"这就是当今锂离子电池的诞生"（页面口径）。
8. **安全验证（1986）**：委托试制一批 LIB 原型；美国交通部（DOT）依据其安全测试数据出具信函，认定该电池与金属锂电池**不同类**——产业化的关键通行证。
9. **工程化三件套**：开发铝箔集流体（钝化层实现高电压低成本）、功能隔膜、PTC 正温度系数保护器件；发明**卷绕结构**（coil-wound）——在有机电解液低电导率下提供大电极面积与大电流放电。
10. **商业化（1991–1992）**：Sony 1991 年、A&T Battery（旭化成与东芝合资）1992 年先后将此构型 LIB 商业化；1992 年吉野出任离子电池产品开发经理，1994 年任 A&T Battery 技术开发经理。
11. **企业内晋升线**：1982 年进入川崎实验室；2003 年旭化成 Fellow；2005 年任自家实验室总经理；2017 年起任名城大学教授、旭化成 Honorary Fellow。
12. **2019 诺贝尔化学奖**：与 M. Stanley Whittingham、John B. Goodenough 共享（表彰锂离子电池的发展）；诺奖演讲《Brief History and Future of Lithium-ion Batteries》（2019-12-08）；被媒体称 "The father of lithium-ion batteries"（Chemistry World 2018 标题口径）。
13. **荣誉满载**：紫绶褒章（2004）、Global Energy Prize（2013）、Charles Stark Draper Prize（2014）、日本国际奖 Japan Prize（2018）、欧洲发明奖（2019）、文化勋章（2019）、VinFuture Prize（2023）。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（靛青 indigo） | `#1E3A5F` | 工程学的严谨与企业的耐心（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（聚乙炔前传 badgePoly） | `#1B7A43` | 绿——导电聚合物 / 1983 原型 |
| 分类色 2（碳阳极突破 badgeCarbon） | `#16324F` | 藏青——1985 原型 / 基础专利 |
| 分类色 3（工程化与商业化 badgeEng） | `#B26A00` | 琥珀——卷绕结构 / Sony 1991 / A&T 1992 |
| 分类色 4（荣誉 badgeHonor） | `#7E1E23` | 绯红——紫绶褒章 / 文化勋章 / Nobel |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「碳微晶结构中容纳锂离子的空隙」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Falling Apart** — Michael FK & Andy Leech（文件 `music_audio/inspiring-electronic/03-qtNSLNUd1VE-...Falling Apart.wav`，不要复制 wav）
- **风格**：情绪钢琴 / 内省 / 温柔的坚定
- **匹配理由**：
  - 曲名 "Falling Apart" 反其意用之——正是聚乙炔"撑不住"（低密度、不稳定）让位给碳材料，拆解旧方案才诞生新电池；
  - 钢琴的内省气质匹配吉野"一家公司做一件事 40 年"的沉静长期主义；
  - 中段的明亮上扬匹配 1991 商业化后"口袋里的革命"铺满世界。
- **时长**：以曲目实际时长为准，ffmpeg `-shortest` 自动对齐 15 页 ≈ 105 秒。

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 锂离子电池的诞生 / Akira Yoshino 吉野 彰 1948– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/日文原名/国籍/出生地/教育/任职/领域/荣誉）
03  吉野彰的一生 — 高斯式时间线（10 节点：1948→1966→1970→1972→1981→1983→1985→1986→1991→2019）
04  法拉第的蜡烛 (1948–1972) — 表格「时间|事件|结果」（吹田→北野高中→京都 BS/MS→福井谦一课程）
05  旭化成的探索者 (1972–1981) — 表格「岗位|方向|转折」（探索性研究团队→聚乙炔应用→转向电池）
06  1983 原型 — 表格「阴极|阳极|意义」+ 公式框：LiCoO2 阴极 + 聚乙炔阳极（锂离子迁移方向）
07  1985 碳阳极突破 — 表格「问题|方法|结果」+ 公式框：碳质阳极替代聚乙炔 → LIB 基础专利
08  安全通行证 (1986) — 表格「验证|机构|结果」（原型批试制→US DOT 信函→与金属锂电池区分）
09  工程化三件套 — 表格「部件|创新|作用」+ 公式框：卷绕结构（大电极面积 × 高电流放电）
10  商业化 (1991–1992) — 表格「公司|年份|市场」（Sony→A&T Battery→手机与笔记本电脑）
11  企业研究者的四十年 — 高斯式「阶段|职位|贡献」表格（1982 川崎实验室→1992 经理→2003 Fellow→2005 实验室 GM→2017 名城大学教授）
12  2019 诺贝尔化学奖 — 共享结构图解：Whittingham（TiS2 初代）× Goodenough（LixCoO2 正极）× Yoshino（碳阳极商用化）
13  遗产：口袋里的革命 — 四分类遗产盒 + 公式框：从手机到笔记本电脑（页面 intro 口径）+ 诺奖演讲标题
14  结尾 — 「一根蜡烛点燃的化学史，最终点亮了世界。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 获奖理由口径 | 本地 page.md 未载官方理由英文原句——本篇引 2019 官方理由 "for the development of lithium-ion batteries" 时**注明口径来源**（本批 Whittingham 页面明载）；Beamer 正文可只写"表彰锂离子电池的发展" |
| LiCoO₂ 发现归属 | 页面载 LiCoO₂ "discovered in 1979 by Godshall et al. at Stanford, and John Goodenough and Koichi Mizushima at Oxford"——**1979（发现）/ 1980（Goodenough 页论文发表）双口径并存**，吉野篇按页面写 1979 且列出双方归属，勿写"吉野发现 LiCoO₂" |
| 阳极演变 | **1983 聚乙炔阳极原型 → 1985 碳质阳极原型**——聚乙炔低密度+不稳定是换材料的动因；勿写成"1985 用聚乙炔" |
| 无博士导师 | 京都大学只有 BS/MS；**Dr.Eng. 2005 来自大阪大学且页面无载导师**——身份页博士导师栏留白，禁杜撰；"1972 入职时是硕士"口径 |
| 白川英树 | 聚乙炔的发现者是白川英树（2000 诺奖）——是**材料来源**非师生/同事关系；influence 关系仅记"其发现的聚乙炔是吉野电池阳极起点"，勿写"受白川指导" |
| 福井谦一 | 页面仅载"修读过其课程"——influence 类型弱关系；福井是"首位东亚裔诺贝尔化学奖得主"为页面明载口径 |
| DOT 信函 | 美国交通部信函说的是 LIB **与金属锂电池不同**（基于 1986 原型安全测试数据）——勿写成"批准上市" |
| 商业化归属 | Sony 1991、A&T Battery 1992 两个年份两条线；A&T 是旭化成与 Toshiba 的合资公司——勿写成"吉野在 Sony 工作" |
| 任职口径 | 全部非学术生涯在旭化成；2017 年起名城大学教授 + 旭化成 Honorary Fellow——勿写"从旭化成退休" |
| 在世口径 | 1948-01-30 生，在世——卒日/享年一律留白 |
| 引语红线 | 本地 page.md 无第一人称直接引语——全文不得出现引号内"原话"；"This was the birth of the current lithium-ion battery" 是页面叙述句，可作转述不作引语 |
| metadata-only 禁入 | frontmatter `award_received` 中 Person of Cultural Merit / Yamazaki-Teiichi Prize（2011 正文有载）等逐条核对；frontmatter `educated_at` 有 "University of Osaka" 与 "Osaka Prefectural Kitano High School" 均与正文对应——但**无任何可入库的人际关系**（ spouse/学生均页面无载） |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q4701206 | ✅ |
| name_zh | 吉野彰 | ✅ |
| name_en | Akira Yoshino | ✅（页面标题规范名；清单 db_id 为空） |
| birth_date | 1948-01-30 | ✅ |
| death_date | （空，在世） | ✅ |
| nationality | Japan | ✅ |
| primary_occupation | chemist | ✅（intro 口径 Japanese chemist；engineer 入 occupations） |
| field_of_work | electrochemistry（person_field 细分：electrochemistry / lithium-ion battery / chemistry，带 rank） | ✅ |
| has_biography | false（Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**★红线：只收 page.md 正文或 infobox 明载的关系；metadata-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | Kenichi Fukui | 无向 | 京都大学期间修读其课程；页面口径"首位东亚裔诺贝尔化学奖得主"（库内既有记录，沿用规范名） |
| influence | Hideki Shirakawa | 无向 | 其发现的导电聚合物聚乙炔是吉野 1981 年起充电电池研究的阳极起点；白川 2000 年获诺贝尔化学奖（库内既有记录，沿用规范名） |
| co-honored | John B. Goodenough | 无向 | 2019 诺贝尔化学奖共同得主（LixCoO2 正极） |
| co-honored | M. Stanley Whittingham | 无向 | 2019 诺贝尔化学奖共同得主（TiS2 初代可充锂电） |

> 吉野页面**无导师、无配偶、无学生**记载——relations 仅 4 条是诚实值（勿为凑数入库）。对手方规范名 "John B. Goodenough"、"M. Stanley Whittingham" 与本批两人互指一致。Fukui/Shirakawa 沿用库内既有记录 Kenichi Fukui（id 3736）/Hideki Shirakawa（id 3638）。2023 VinFuture Prize 本页未列共同得主名——Martin Green/Rachid Yazami 的 co-honored 行只入 Whittingham 篇 yaml，本篇**不入**。

## 8. 奖项清单

- 化学技术奖，日本化学会（1998）
- 电池分会技术奖，The Electrochemical Society（1999）
- 市村产业奖励赏·功绩赏（2001）
- 文部科学大臣表彰·科学技术奖（开发部门，2003）
- 紫绶褒章（2004，日本政府）
- 山崎贞一赏（2011）；C&C 奖（NEC C&C 财团，2011）
- IEEE Medal for Environmental and Safety Technologies（2012）
- Global Energy Prize（2013）
- Charles Stark Draper Prize（2014）
- 日本国际奖 Japan Prize（2018）
- European Inventor Award（2019）
- Nobel Prize in Chemistry（2019，与 Whittingham/Goodenough 共享）
- 文化勋章（2019）；Asian Scientist 100（2019、2020）；VinFuture Prize（2023）

## 9. 机构清单

- 教育：大阪府立北野高中（1966）；京都大学（BS 1970、MS 1972，工学）；大阪大学（Dr.Eng. 2005）
- 企业：旭化成株式会社（1972–；探索性研究团队→1982 川崎实验室→1992 离子电池产品开发经理→1994 A&T Battery 技术开发经理→2003 Fellow→2005 自家实验室总经理→2017 Honorary Fellow）；A&T Battery Corp.（旭化成与东芝合资）
- 学术：名城大学（名古屋，2017– 教授）

## 10. 终审清单

- [x] 生卒 1948-01-30 / 在世留白；出生地吹田市；日文原名吉野 彰
- [x] 无博士导师（大阪大学 Dr.Eng. 2005，页面无载导师）——留白
- [x] 1983 聚乙炔阳极原型 / 1985 碳阳极原型演变正确；LiCoO₂ 1979 双归属口径注明
- [x] Sony 1991 / A&T Battery 1992 商业化两线分开；DOT 信函口径准确
- [x] 2019 三人共享；官方理由原句注明取自 Whittingham 页面口径
- [x] Fukui/Shirakawa 用 influence 弱关系且沿用库内记录；relations 仅 4 条诚实值
- [x] 全文无杜撰引语；"father of lithium-ion batteries" 作媒体标题口径
- [x] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Akira_Yoshino/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：优先本地 `images.txt` 中 2019 年照片；404 则装饰圆占位
- [ ] 国籍：封面顶部明示日本；日文原名「吉野 彰」在封面与身份页出现
- [ ] 引语核对：全文不得出现无法溯源的引号原话
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一；化学式（LiCoO₂、聚乙炔 (CH)ₓ）一律数学模式
- [ ] 与 Sanger 及 21 世纪批次既有格式对齐；与 Goodenough/Whittingham 两篇共享页口径互查
