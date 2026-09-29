# Robert S. Mulliken（罗伯特·S·马利肯）立传提示词

> qid=Q233355 · 1896-06-07 – 1986-10-31 · 美国物理化学家 · 20 世纪 · 诺贝尔化学奖（1966，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Robert_S._Mulliken/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**严格对齐 Frederick Sanger 黄金参照**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.md`）——身份信息页 + 高斯式时间线 + 表格语义化 tabularx + 金色公式展示框 + 气泡背景。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。⚠ 肖像说明：本地 `images.txt` 仅含 1929 年芝加哥合影（Hund,Friedrich_1929_Chicago.jpg，Mulliken 在内）与 logo——**非个人标准肖像**；回退方案：经 Wikipedia REST API `page/summary` 查 infobox 原图名后用 `Commons Special:FilePath/<文件名>?width=600` 下载（curl -A "Mozilla/5.0" + file 验证）；404 则用装饰圆占位，禁用合照裁剪充当肖像。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{atom}\enspace 分子轨道的建筑师\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「电子离域」母题——离散圆点暗示电子不属于某个键，而遍及整个分子。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Robert Sanderson Mulliken（中文惯称：罗伯特·S·马利肯）
- **生卒**：1896-06-07 生于马萨诸塞州 Newburyport → 1986-10-31 逝于弗吉尼亚州 Arlington County 女儿家中（充血性心力衰竭，享年 90），遗体运回芝加哥安葬
- **国籍**：United States（美国）
- **身份**：物理化学家（physical chemist；兼具物理学家身份，两界均认领他）
- **家庭**：父 Samuel Parsons Mulliken 为 MIT 有机化学教授——Mulliken 少年时帮父亲编四卷有机化合物鉴定手册，精通有机化学命名法；幼年即结识物理化学家 Arthur Amos Noyes。1929-12-24 娶 Mary Helen von Noé（芝加哥大学地质学教授 Adolf Carl Noé 之女），育有两女；妻 1975 年先逝
- **教育轨迹**：
  - Newburyport 高中（1913 毕业，科学课程；获父亲当年也得过的 MIT 奖学金）
  - MIT 化学本科，1917 年 B.S.（本科即完成可发表的有机氯化物合成研究；兼修化工课并 touring 化工厂）
  - 芝加哥大学博士，1921 年（汞同位素蒸发分离研究）
- **导师**：William Draper Harkins（frontmatter doctoral_advisor；正文 infobox 无 doctoral advisor 行——PPT 注明取自页面 frontmatter）
- **博士**：1921，汞同位素蒸发分离
- **研究领域**：分子轨道理论、Mulliken 电负性、Mulliken 电荷、Mulliken 布居分析、双原子分子带光谱

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **化学世家（1896）**：MIT 有机化学教授之子——命名法童子功与选择性记忆力。
2. **战时毒气实验室（1917–1918）**：美国参战后赴华盛顿 American University 在 James B. Conant 手下制毒气；九个月后应征入陆军化学战勤务继续同一工作；因实验技术欠佳被灼伤数月，又染重流感，战争结束时仍在住院。
3. **芝加哥博士（1919–1921）**：汞同位素蒸发分离；此后继续该方向，NRC 经费资助。
4. **哈佛深造（1923–）**：从 Frederick A. Saunders 学光谱技术、从 E. C. Kemble 学量子理论；同期结识 J. Robert Oppenheimer、John H. Van Vleck、Harold C. Urey、John C. Slater；在芝加哥上过 Robert A. Millikan 的课（接触旧量子论——听课非师承）。
5. **两赴欧洲（1925/1927）**：与 Schrödinger、Dirac、Heisenberg、de Broglie、Born、Bothe 等新量子力学奠基者共事；受 Friedrich Hund 影响最深。
6. **分子轨道理论诞生（1927）**：与 Hund 合作，把电子赋予「遍及整个分子」的态——MO 理论亦称 **Hund-Mulliken theory**。
7. **VB 与 MO 之争**：1927 Heitler-London 的 H2 计算与 Slater/Pauling 杂化轨道催生价键法（HLSP），一度流行；MO 法（含 John Lennard-Jones 贡献）因激发态计算更灵活，最终超越价键法——正是这一发展使他获 1966 年诺贝尔化学奖。
8. **物理与化学双栖**：1926–1928 任 NYU 物理系教职（"第一次作为物理学家被认可"）；1930 以 Guggenheim Fellow 赴莱比锡与 Heisenberg、Teller、Hund 共事；回芝加哥任副教授、1931 正教授，最终物理、化学两系双聘。
9. **电负性标度（1934）**：定义为原子电离焓与电子亲和能的平均值——与 Pauling 标度不完全对应但大体一致。
10. **最年轻的 NAS 会员（1936）**：当时（at the time）美国国家科学院史上最年轻会员；American Philosophical Society（1940）、American Academy of Arts and Sciences（1965）、皇家学会外籍会员 ForMemRS（1967）。
11. **战时钚项目（1942–1945）**：主持芝加哥大学钚项目信息办公室；战后推导数学公式推进 MO 理论。
12. **酸碱理论（1952）与晚年**：用量子力学分析 Lewis 酸碱反应；1961 任佛罗里达州立大学物理与化学杰出教授，继续分子结构与光谱研究（从双原子分子到大型聚集体）；1985 年退休；1981 年世界文化理事会创始成员。
13. **1966 诺贝尔化学奖与荣誉**：因发展分子轨道方法获奖（官方 citation 英文原句本地页面无载——见 §5）；Peter Debye Award（1963）、Priestley Medal（1983）、Golden Plate Award（1983）。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深青绿 deepteal） | `#0B5351` | 电子云的深海——分子轨道的离域与精确（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（分子轨道 badgeMO） | `#1E4E79` | 蓝 Hund-Mulliken 理论 / MO vs VB |
| 分类色 2（光谱与同位素 badgeSpec） | `#7A3E9D` | 紫 带光谱 / 汞同位素分离 |
| 分类色 3（电负性与酸碱 badgeElec） | `#C0392B` | 红 1934 电负性标度 / Lewis 酸碱 |
| 分类色 4（学院与荣誉 badgeAcad） | `#1B7A43` | 绿 NAS 最年轻 / ForMemRS / Priestley |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「离域电子云」——圆点即弥散在整个分子空间的电子密度。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Daylight** — Alex-Productions（`music_audio/alex-productions/44-JoyIRE5k2Yo-Daylight.wav`；不要复制 wav 文件，make video 时引用路径）
- **风格**：明亮 / 上扬 / 拨云见日
- **匹配理由**：
  - "Daylight" 匹配 MO 理论的命运曲线——从旧量子论与 VB 法的阴影里被冷落多年，终成化学键理论的主流语言
  - 明快节奏匹配美国实验物理化学的务实气质——不玄谈，先算出来
  - 曲名的"天亮"意象呼应其战时毒气岁月后的科学重建人生
- **时长**：以文件实际时长为准，ffmpeg `-shortest` 自动对齐 15 页 × 7 秒

## 4. Slide 规划（15 页，Sanger 同构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 分子轨道的建筑师 / Robert S. Mulliken 1896–1986 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  马利肯的一生 — 高斯式时间线（10 节点：1896→1917→1921→1927→1931→1934→1942→1952→1961→1966）
04  早年：化学教授之子 (1896–1917) — 表格「时间|事件|结果」（命名法童子功/MIT/毒气实验室如实带过）
05  博士与哈佛岁月 (1919–1927) — 表格「时间|事件|结果」（汞同位素→带光谱→欧洲）
06  分子轨道理论 (1927) — 表格「问题|方法|结果」+ 公式框：电子赋予遍及整分子的态（MO vs VB 对照示意）
07  VB/MO 之争与胜利 — 表格「阵营|主张|结局」（Heitler-London/Slater/Pauling vs Hund-Mulliken/Lennard-Jones）
08  电负性标度与酸碱 (1934/1952) — 表格 + 公式框：χ = (I + A)/2
09  双栖学者与战时 (1926–1945) — 表格「阶段|岗位|意义」（NYU 物理/莱比锡/钚项目信息办公室）
10  荣誉 — 高斯式「类别|代表|意义」表格（NAS 1936 当时最年轻 / ForMemRS 1967 / Debye 1963 / Priestley 1983）
11  1966 诺贝尔化学奖 — 独享；间接转述获奖理由（页面无载官方原句，见 §5）+ Priestley 1983
12  晚年与遗产 — 表格（佛罗里达州立 1961 / 世界文化理事会 1981 / Mulliken 布居分析以其名传世）
13  家庭与人格 — 记忆力与命名法轶事 / von Noé 家庭 / 90 岁逝于女儿家中
14  结尾 — 「电子不属于某一条键，而属于整个分子。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1966 诺奖理由 | 官方 citation **英文原句本地 page.md 无载**——禁写原句（如 "for his fundamental work concerning chemical bonds..." 之类页外文本一律禁）；用间接转述"因发展分子轨道方法而获奖"，并注明"页面无载官方原文" |
| 1966 独享 | 1966 为**独享**，无共同得主——勿造 co-honored |
| 师承来源 | 博士导师 William Draper Harkins 仅 frontmatter 载（正文 infobox 无 advisor 行）——PPT 与 yaml 注明"取自页面 frontmatter" |
| Millikan | 在芝加哥**上过** Robert A. Millikan 的课——听课非师承，禁写导师/学生关系 |
| Hund-Mulliken | MO 理论亦称 Hund-Mulliken theory，且 John Lennard-Jones 有贡献——勿独揽；Hund 是"影响最深"者 |
| VB 阵营 | Heitler-London 1927 算 H2；Slater/Pauling 提出杂化轨道——勿写 Pauling 参与 MO 创立 |
| 最年轻 NAS | 1936 当时的组织史上最年轻（at the time）——勿去掉限定写"史上最年轻" |
| 毒气岁月 | 如实写"在 Conant 手下制毒气+应征化学战勤务+灼伤住院"——禁加页外渲染；勿写成"化学武器发明者" |
| 两个 Mulliken 记号 | Mulliken population analysis（布居分析，分子电荷划分）勿与 Mulliken symbols（点群特征标表记号，See also 条目）混淆 |
| 电负性 | 与 Pauling 标度"不完全对应但大体一致"——勿写"取代/推翻 Pauling 标度" |
| 去世地 | Arlington County, Virginia 女儿家中（充血性心力衰竭）——勿写死于芝加哥；遗体运回芝加哥安葬 |
| 妻姓 | Mary Helen **von Noé**（德语腔拼法带 é）——勿与其父 Adolf Carl **Noé** 的拼法混淆 |
| 博士生 | Leona Woods、William Lichten、Nicholas Metropolis 仅 metadata.json 有载，正文 infobox 无——**不予入库**，PPT 禁写 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q233355 | ✅ |
| name_zh | 罗伯特·S·马利肯 | ✅ |
| name_en | Robert S. Mulliken | ✅ |
| birth_date | 1896-06-07 | ✅ |
| death_date | 1986-10-31 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | physical chemist | ✅ |
| field_of_work | physical chemistry（person_field 细分：molecular orbital theory / physical chemistry / theoretical chemistry / spectroscopy，带 rank） | ✅ |
| has_biography | false（立传 Beamer 完成后再置 1） | ✅ |

## 7. 社会关系入库清单

**★红线：只收 page.md 正文或 frontmatter 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | William Draper Harkins | 师→生 | 博士导师（frontmatter doctoral_advisor；芝加哥大学读博 1919-1921） |
| colleague | Friedrich Hund | 无向 | 1927 合作发展分子轨道理论（Hund-Mulliken theory）；1930 莱比锡再共事 |
| colleague | Werner Heisenberg | 无向 | 1930 Guggenheim Fellow 访莱比锡大学共事 |
| colleague | Edward Teller | 无向 | 1930 Guggenheim Fellow 访莱比锡大学共事 |
| colleague | James B. Conant | 无向 | 一战在 American University 于 Conant 领导下制毒气 |
| spouse | Mary Helen von Noé | 无向 | 1929-12-24 结婚，育两女 |

> **metadata-only 禁入库名单**：Leona Woods、William Lichten、Nicholas Metropolis（doctoral_student 仅 metadata.json）；Robert A. Millikan（仅"上过他的课"，非师承）；Harvard 时期的 Oppenheimer/Van Vleck/Urey/Slater 仅为"结识"，无实质关系记载——均不入库。

## 8. 奖项清单

- Nobel Prize in Chemistry（1966，独享）
- Peter Debye Award in Physical Chemistry（1963）
- Priestley Medal（1983）
- Golden Plate Award of the American Academy of Achievement（1983）
- Guggenheim Fellowship（1930；frontmatter 载）
- Willard Gibbs Award（frontmatter 载，页面未给年份——禁编年份）
- National Academy of Sciences（1936，当时史上最年轻会员）
- American Philosophical Society（1940）
- American Academy of Arts and Sciences（1965）
- Foreign Member of the Royal Society，ForMemRS（1967）
- World Cultural Council 创始成员（1981）

## 9. 机构清单

- 教育：Newburyport 高中（–1913）；MIT（BS 化学 1917）；University of Chicago（PhD 1921）；Harvard（NRC 资助深造，光谱 + 量子理论）
- 任职：American University（一战毒气实验室）；University of Chicago（副教授→1931 正教授→物理化学双聘）；New York University 物理系（1926–1928）；莱比锡大学（1930 Guggenheim）；Florida State University（1961 Distinguished Professor of Physics and Chemistry，1985 退休）
- 身后：安葬于芝加哥

## 10. 终审清单

- [ ] 生卒 1896-06-07 / 1986-10-31，享年 90，出生地 Newburyport、去世地 Arlington County（女儿家中）
- [ ] 1966 独享表述准确；获奖理由为间接转述且注明"页面无载官方原文"
- [ ] 博士导师 Harkins 注明"取自 frontmatter"；Millikan 听课非师承
- [ ] Hund-Mulliken 命名与 Lennard-Jones 贡献表述准确；VB/MO 之争叙事无翻案
- [ ] "当时最年轻 NAS 会员"保留 at the time 限定
- [ ] 毒气岁月如实且不渲染；两个 Mulliken 记号不混淆
- [ ] 引语核对：本篇正文基本无直接引语——若有引号文本须在 page.md 溯源，否则改间接转述
- [ ] 正文采用 Sanger 同构：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误，vbox≤10pt / hbox≤50pt

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Robert_S._Mulliken/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：REST API 回退下载结果核对（非合照裁剪）；404 则装饰圆占位并在 §0 注记
- [ ] 国籍：封面顶部明示美国
- [ ] 引语核对：任何引号文本必须在 Wikipedia 原文找到
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox<10pt / hbox<50pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger/Fischer 等）对齐
