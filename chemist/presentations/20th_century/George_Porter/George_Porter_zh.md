# George Porter（乔治·波特）立传提示词

> qid=Q106762 · 1920-12-06 – 2002-08-31 · 英国化学家 · 20 世纪 · 诺贝尔化学奖（1967，与 Eigen、Norrish 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/George_Porter/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**严格对齐 Frederick Sanger 黄金参照**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.md`）——身份信息页 + 高斯式时间线 + 表格语义化 tabularx + 金色公式展示框 + 气泡背景。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。⚠ 肖像说明：本地 `images.txt` 仅含 Wikiquote/Commons logo——**无现成肖像**；回退方案：经 Wikipedia REST API `page/summary` 查 infobox 原图名后用 `Commons Special:FilePath/<文件名>?width=600` 下载（curl -A "Mozilla/5.0" + file 验证；页面外部链接载 National Portrait Gallery 有其肖像合集，可作线索）；404 则装饰圆占位。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{sun}\enspace 一束阳光的历史\enspace·\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「一束阳光」母题——闪光光解与光合作用的共同意象（其 1976 年皇家研究院圣诞讲座即名 The Natural History of a Sunbeam）。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：George Porter, Baron Porter of Luddenham, OM, FRS, FRSE（中文惯称：乔治·波特；尊称 The Right Honourable The Lord Porter of Luddenham）
- **生卒**：1920-12-06 生于南约克郡 Stainforth（近 Thorne，当时属 West Riding of Yorkshire）→ 2002-08-31 逝，享年 81。⚠ 去世地点正文 infobox **无载**（metadata.json 载 Canterbury 但正文无载——禁写地点，或注明"metadata 有载正文无载，不予采用"）
- **国籍**：United Kingdom（英国）
- **身份**：化学家（chemist；皇家研究院院长、皇家学会主席、上议院终身贵族）
- **家庭**：1949 年娶 Stella Jean Brooke。其余家庭成员本页无载——禁写
- **教育轨迹**：
  - Thorne Grammar School
  - University of Leeds（奖学金入学；化学一等学位 BSc）——本科受教于 Meredith Gwynne Evans，他称之为"我遇到过的最杰出的化学家"
  - Emmanuel College, Cambridge（PhD 1949）；后为 Emmanuel College Fellow
- **导师**：Ronald George Wreyford Norrish（博士导师；1949 论文 *The study of free radicals produced by photochemical means*）
- **博士**：1949，光化学方法产生的自由基研究
- **研究领域**：photochemistry、chemical kinetics、光合作用光反应、公众理解科学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **约克郡少年（1920）**：Stainforth 矿区小镇出身，Thorne Grammar School 起步，奖学金叩开利兹大学。
2. **战争岁月**：二战服役于皇家海军志愿预备队（Royal Naval Volunteer Reserve）。
3. **师从诺里什**：战后入剑桥随 Ronald George Wreyford Norrish 做研究——这一工作最终使师徒二人同榜诺奖。
4. **闪光光解与自由基（1947–1949）**：发展 flash photolysis 技术获取短寿命分子物种的信息——**提供了自由基存在的首批证据**（first evidence of free radicals）。
5. **人造纤维研究所（1953–1954）**：任 British Rayon Research Association 助理主任，研究染色纤维素织物在日光下的光脆损（phototendering）。
6. **谢菲尔德岁月（1954–1965）**：任 Sheffield 大学化学教授——用系里车间设计制作的设备做闪光光解；期间参与 "Eye on Research" 电视节目。
7. **皇家研究院（1966–）**：任 Fullerian Professor of Chemistry 并出任皇家研究院（Royal Institution）院长；任内推动成立 Applied Photophysics 公司，将其实验室技术仪器化。
8. **1967 诺贝尔化学奖**：与 Manfred Eigen、Ronald George Wreyford Norrish 共享；同年任 University College London 客座教授。
9. **光合作用与氢经济**：用闪光光解技术细究光合作用光反应——并对氢经济（hydrogen economy）的应用前景大力倡导。
10. **公众理解科学**：倡导 "not-yet-applied science"（尚未应用的科学）；1985 任英国科学促进会（British Association）主席、科学公众理解委员会（COPUS）创始主席。
11. **讲座人生**：1976 皇家研究院圣诞讲座 *The Natural History of a Sunbeam*；1978 牛津 Romanes Lecture "Science and the human purpose"；1988 Dimbleby Lecture "Knowledge itself is power"；1990–1993 Gresham College 天文学讲座。
12. **皇家学会主席（1985–1990）**：1979 美国艺术与科学院、1986 美国哲学学会外籍/外籍会员；FRS（1960）。
13. **荣誉链与身后**：knighted（1972）→ Order of Merit（1989）→ 终身贵族 Baron Porter of Luddenham（Kent 郡 Luddenham，1990-07-16 就任）；Davy Medal（1971）、Kalinga Prize（1976）、Rumford Medal（1978）、Faraday Lectureship Prize（1980）、Michael Faraday Prize（1991）、Ellison-Cliffe Medal（1991）、Copley Medal（1992）；Leicester 大学 Chancellor（1984–1995）；2001 年 Leicester 化学系大楼命名 George Porter Building；著 *Chemistry for the Modern World*（1962）、*Chemistry in Microtime*（1996）。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深翠绿 deepemerald） | `#1E5631` | 一束阳光穿过绿叶——闪光光解与光合作用的共同母题（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（闪光光解 badgeFlash） | `#1E4E79` | 蓝 flash photolysis / 自由基证据 |
| 分类色 2（光合作用 badgePhotoSyn） | `#D97B29` | 琥珀 光反应 / 氢经济 |
| 分类色 3（皇家研究院 badgeRI） | `#8B1A1A` | 皇家研究院院长 / 圣诞讲座 / 科学传播 |
| 分类色 4（荣誉与贵族 badgeHonor） | `#6B4C9A` | 紫 OM / 终身贵族 / Copley |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「一束阳光」——光脉冲照亮分子世界的瞬间。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**With Me** — Alex-Productions（`music_audio/alex-productions/83-DXAblXgCK-k-With-Me.wav`；不要复制 wav 文件，make video 时引用路径）
- **风格**：温暖 / 同行感 / 亲和
- **匹配理由**：
  - "With Me" 的同行感匹配师徒传承——师从 Norrish、1967 同榜诺奖的化学佳话
  - 亲和气质匹配其"公众科学家"面向——圣诞讲座、Dimbleby 讲座、COPUS，把科学带给大众
  - 明快中段留给皇家研究院岁月——科学家、院长、上议员的多重身份同行一生
- **时长**：以文件实际时长为准，ffmpeg `-shortest` 自动对齐 15 页 × 7 秒

## 4. Slide 规划（15 页，Sanger 同构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 一束阳光的历史 / George Porter 1920–2002 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  波特的一生 — 高斯式时间线（10 节点：1920→1940s→1949→1954→1966→1967→1972→1985→1990→2002）
04  约克郡与战争岁月 (1920–1945) — 表格「时间|事件|结果」（Stainforth/Leeds 奖学金/RNVR 服役）
05  师从诺里什 (1945–1949) — 表格「问题|方法|结果」+ 公式框：闪光光解捕捉自由基（示意）
06  闪光光解 — 表格 + 实物细节（Sheffield 系车间自制设备）
07  人造纤维研究所 (1953–1954) — 表格（phototendering/工业与科学的交汇）
08  皇家研究院院长 (1966–) — 表格（Fullerian Professor/Applied Photophysics/圣诞讲座 1976）
09  1967 诺贝尔化学奖 — 三人共享（本篇=闪光光解与自由基方向）；与 Eigen 篇 citation 口径一致
10  光合作用与氢经济 — 表格「对象|方法|愿景」
11  公众理解科学 — 表格「场合|演讲|信息」（COPUS/Romanes 1978/Dimbleby 1988/Gresham 天文 1990-93）
12  荣誉链 — 高斯式「类别|代表|意义」表格（1972 骑士→1989 OM→1990 终身贵族；Davy 1971→Copley 1992）
13  皇家学会主席与晚年 — 1985–1990 双主席（BRSA+RS 同年）/Leicester Chancellor/2001 George Porter Building/2002 逝
14  结尾 — 「科学的价值，在于它尚未被应用之时。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 去世地点 | 正文 infobox 只载日期（2002-08-31）**无地点**；metadata.json 载 Canterbury——正文无载，禁写地点（如需注明"metadata 有载、正文无载，不予采用"） |
| 师徒同奖 | Porter 博士导师 Norrish，1967 师徒同榜（与 Eigen 三人共享）——表述准确；师承关系由本篇 yaml 入库（本页明载），Norrish 侧不入 |
| Meredith Gwynne Evans | Leeds **本科**授课老师（"我遇到过的最杰出的化学家"）——勿写"博士导师" |
| 自由基表述 | "provided the first evidence of free radicals"——提供自由基存在的**首批证据**；勿放大为"发现自由基" |
| 政治身份 | metadata occupation 有 politician——实为上议院终身贵族（life peer，1990）；勿写成政党政治人物 |
| 荣誉顺序 | knighted 1972 → OM 1989 → life peer 1990-07-16（Baron Porter of Luddenham, of Luddenham in the County of Kent）——顺序勿乱 |
| 双主席同年 | 1985 同年任 British Association 主席与（1985-1990）皇家学会主席——如实并列勿混 |
| Gresham 讲座 | 1990–1993 讲座主题是**天文学**——勿写成化学 |
| 诺贝尔口径 | 与 Eigen 篇 citation 表述统一（本页正文仅写"awarded … along with …"无原句） |
| 博士生 | 正文 infobox 载 James Robert Durrant、Graham Fleming 两人；metadata 仅载短名 "James Durrant"——入库用全名 James Robert Durrant，不建短名 stub |
| 引语 | "most brilliant chemist he had ever met"（关于 Meredith Gwynne Evans）及三个演讲标题（"Science and the human purpose"/"Knowledge itself is power"/"The Natural History of a Sunbeam"）均页面实载可引；其余无引语 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q106762 | ✅ |
| name_zh | 乔治·波特 | ✅ |
| name_en | George Porter | ✅ |
| birth_date | 1920-12-06 | ✅ |
| death_date | 2002-08-31 | ✅ |
| nationality | United Kingdom | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | photochemistry（person_field 细分：photochemistry / chemical kinetics / flash photolysis / photosynthesis，带 rank） | ✅ |
| has_biography | false（立传 Beamer 完成后再置 1） | ✅ |

## 7. 社会关系入库清单

**★红线：只收 page.md 正文或 frontmatter 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Ronald George Wreyford Norrish | 师→生 | 剑桥博士导师；1949 论文（光化学法产生的自由基）；1967 师徒同榜诺奖 |
| advisor-student | James Robert Durrant | Porter→学生 | 正文 infobox doctoral student（全名，防短名 stub） |
| advisor-student | Graham Fleming | Porter→学生 | 正文 infobox doctoral student |
| influence | Meredith Gwynne Evans | 无向 | Leeds 本科授业恩师；被 Porter 称为"我遇到过的最杰出的化学家" |
| co-honored | Manfred Eigen | 无向 | 1967 诺贝尔化学奖共同得主 |
| co-honored | Ronald George Wreyford Norrish | 无向 | 1967 诺贝尔化学奖共同得主（兼博士导师） |
| spouse | Stella Jean Brooke | 无向 | 1949 结婚 |

> **metadata-only 禁入库名单**：metadata.json 的 "James Durrant" 为 James Robert Durrant 的短名，不另建 stub；其余 employer/award 无人物关系。

## 8. 奖项清单

- Nobel Prize in Chemistry（1967，与 Eigen、Norrish 共享）
- Corday-Morgan Prize（1955）
- Fellow of the Royal Society，FRS（1960）
- Davy Medal（1971）
- Knight Bachelor（1972）
- Kalinga Prize（1976）
- Rumford Medal（1978）
- American Academy of Arts and Sciences（1979 当选）
- Faraday Lectureship Prize（1980）
- American Philosophical Society（1986 当选）
- Order of Merit，OM（1989）
- Life peerage，Baron Porter of Luddenham（1990-07-16）
- Michael Faraday Prize（1991）；Ellison-Cliffe Medal（1991）
- Copley Medal（1992）
- Tilden Prize、Melchett Medal、Remsen Award、Liversidge Award、Longstaff Prize、皇家学会 Bakerian Medal（frontmatter 载，页面未给年份——禁编）
- 荣誉学位：Heriot-Watt University（1971）；University of Lille-I；University of Bath 荣誉法学博士（1995）

## 9. 机构清单

- 教育：Thorne Grammar School；University of Leeds（BSc）；Emmanuel College / University of Cambridge（PhD 1949；后为 Emmanuel Fellow）
- 战时：Royal Naval Volunteer Reserve
- 任职：British Rayon Research Association 助理主任（1953–1954）；University of Sheffield 教授（1954–1965）；皇家研究院 Fullerian Professor of Chemistry 兼院长（1966–）；University College London 客座教授（1967–）；University of Leicester Chancellor（1984–1995）
- 创办：Applied Photophysics（仪器公司）；COPUS（科学公众理解委员会，创始主席）
- 纪念：University of Leicester George Porter Building（2001 命名）

## 10. 终审清单

- [ ] 生卒 1920-12-06 / 2002-08-31，享年 81；去世地点如实留白（正文无载）
- [ ] 1967 三人共享表述准确，与 Eigen/Norrish 篇口径互指一致
- [ ] 师承链准确：Leeds 本科受教 Meredith Gwynne Evans → Cambridge 博士导师 Norrish
- [ ] "首批自由基证据"表述未放大；Sheffield 车间自制设备细节保留
- [ ] 荣誉顺序 1972 骑士→1989 OM→1990 终身贵族准确；双主席年份准确
- [ ] Gresham 讲座=天文学；演讲标题三处逐字与页面一致
- [ ] 引语核对：引号文本仅限页面实载（Evens 评语与三个演讲标题），其余改间接转述
- [ ] 正文采用 Sanger 同构：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误，vbox≤10pt / hbox≤50pt

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/George_Porter/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：REST API 回退下载结果核对；404 则装饰圆占位并在 §0 注记
- [ ] 国籍：封面顶部明示英国
- [ ] 引语核对：任何引号文本必须在 Wikipedia 原文找到
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox<10pt / hbox<50pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式及同批 Eigen/Norrish 篇章口径一致（三人互指一致）
