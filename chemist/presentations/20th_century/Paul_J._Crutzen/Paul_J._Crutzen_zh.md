# Paul J. Crutzen（保罗·克鲁岑）立传提示词

> qid=Q135139 · 1933-12-03 – 2021-01-28 · 荷兰气象学家与大气化学家 · 20 世纪 · 诺贝尔化学奖（1995，与 Mario J. Molina、F. Sherwood Rowland 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Paul_J._Crutzen/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景，是本次撰写的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像从 `pages/Paul_J._Crutzen/images.txt` 下载至 `images/`，404 则用装饰圆占位并在 Review-1 注明）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{cloud}\enspace 读懂臭氧层的人\enspace·\enspace 荷兰`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（Paul Jozef Crutzen）、国籍、出生地/去世地、教育、博士导师、核心领域、机构、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆），呼应「平流层臭氧层」母题——一层包裹地球的稀薄圆点带，脆弱而关键。
5. **表格语义化 + 公式框**（★ Sanger 版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 " "。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Paul Jozef Crutzen（中文惯称：保罗·约瑟夫·克鲁岑；荷兰语发音 [pʌul ˈjoːzəf ˈkrʏtsə(n)]）
- **生卒**：1933-12-03 生于荷兰阿姆斯特丹 → 2021-01-28 逝于德国美因茨，享年 87
- **国籍**：Netherlands（荷兰；metadata 并列 Germany——长期定居美因茨）
- **身份**：气象学家与大气化学家（meteorologist and atmospheric chemist）；「人类世」（Anthropocene）一词的推广者
- **家庭**：Anna（娘家姓 Gurk）与 Josef Crutzen 之子；1958-02 娶芬兰大学生 Terttu Soininen（1956 年相识），同年 12 月生长女（Ilona，随 1959 年 7 月迁斯德哥尔摩的记载），1964-03 生次女
- **教育轨迹**：
  - 阿姆斯特丹小学（1940 入学，战时辗转上课；1944–45 「饥饿之冬」）
  - Hogere Burgerschool（高等市民学校，1951 毕业；通法英德三语）
  - 高等职业教育学校土木工程（学费较低；奖学金无着落的现实选择）
  - Stockholm University（气象学 PhD，1968）
- **导师**：Bert Bolin 与 Georg Witt（博士导师双值，infobox 明载）
- **博士**：1968，《Determination of parameters appearing in the "dry" and the "wet" photochemical theories for ozone in the stratosphere》
- **研究领域**：大气化学、平流层臭氧、生物地球化学循环与气候、核冬天、人类世

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **战时童年（1933–1951）**：1940 年德国入侵荷兰同年入学；战争末期经历「饥饿之冬」，同窗死于饥荒或疾病——和平与环境的底色由此而来。
2. **土木工程师（1951–1958）**：考试分不够大学奖学金，读土木工程，1954 入阿姆斯特丹桥梁建设局；服兵役后 1958 随妻赴瑞典 Gävle。
3. **程序员叩门（1959）**：看到斯德哥尔摩大学气象系招程序员，应聘成功，7 月携妻女赴斯德哥尔摩——人生转折点。
4. **世界最快的计算机（1959–1963）**：斯德哥尔摩大学拥有 BESK 与其后继 Facit EDB（当时世界最快）；参与早期数值天气预报模型编程，自研热带气旋模型；1960 年 TIROS 气象卫星图像验证了理论。
5. **半工半读的 PhD（1963–1968）**：以数学、统计与气象学结合的论文开题；约 1965 应美国科学家之请协助建立平流层/中间层/低热层氧同素（O、O₂、O₃）分布数值模型——进入臭氧光化学。
6. **1968 博士论文**：平流层臭氧「干」「湿」光化学理论的参数确定，建议研究氮氧化物（NOx）；论文广受好评，获 ESRO（ESA 前身）资助赴牛津 Clarendon Laboratory 博士后。
7. **N₂O 与 NOx（1970）**：指出土壤细菌产生的稳定长寿命气体 N₂O 可存续到平流层转化为 NO；化肥使用增加可能推高平流层 NO，进而损伤臭氧层——**人类活动影响平流层臭氧**的先声。
8. **超音速客机之争（1971）**：与 Harold Johnston（各自独立）提出拟议中的 SST 机群（数百架 Boeing 2707）在低平流层的 NO 排放将损耗臭氧层（后续分析对此担忧有争议，页面明载）。
9. **1974 预印本时刻**：收到 Rowland 与 Molina 关于氯氟甲烷破坏臭氧层论文的预印本，立即建立模型，预测照当前使用速度臭氧将严重损耗。
10. **美因茨岁月（1980–）**：任马克斯·普朗克化学研究所大气化学系研究员；并兼任 Scripps 海洋学研究所、首尔国立大学、Georgia Tech 长期 adjunct、斯德哥尔摩大学气象系研究教授；1997–2002 任乌得勒支大学高层大气学（aeronomy）教授。
11. **核冬天（1982）**：与 John W. Birks 合著首篇核冬天论文《The atmosphere after a nuclear war: Twilight at noon》——城市与森林大火的黑烟遮蔽阳光、地表强降温；1991 年又与同僚对科威特油井火提出「显著核冬天式效应」假说。
12. **人类世（2000）**：与 Eugene F. Stoermer 在 IGBP Newsletter 41 提议以 anthropocene 命名当前地质时代，建议起点为 18 世纪后半叶（与瓦特蒸汽机 1784 印记相合）。
13. **1995 诺贝尔化学奖**：与 Mario Molina、Frank Sherwood Rowland 共享，"for their work in atmospheric chemistry, particularly concerning the formation and decomposition of ozone"；其研究促成消耗臭氧层化学品禁令——马普学会主席 Stratmann 评价为「诺奖基础研究直接催生全球政治决定的空前范例」。2006 年发表气候工程（平流层撒硫颗粒）争议性专文；h-index 151（Google Scholar，截至 2021）。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深海绿 deepsea） | `#0B5351` | 平流层的深邃与臭氧的冷绿（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（臭氧化学 badgeOzone） | `#1E7A6F` | 青 N₂O→NO / O₃ 光化学 |
| 分类色 2（数值模拟 badgeModel） | `#37548D` | 蓝 BESK / 数值模型 |
| 分类色 3（核冬天 badgeWinter） | `#7E1E23` | 暗红 Twilight at noon |
| 分类色 4（人类世 badgeAnthro） | `#C9722A` | 赭石 Anthropocene / 气候工程 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「臭氧层」——包裹行星的稀薄点阵。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Awaken** — Alex-Productions（清单指定 `music_audio/alex-productions/36-aqLUvpAdLNQ-Awaken.wav`，不要复制 wav 文件，由 Makefile 侧引用）
- **风格**：渐亮 / 觉醒 / 呼吁
- **匹配理由**：
  - "Awaken" 匹配主题——臭氧研究唤醒世界对消耗臭氧层化学品的警觉，最终促成禁令
  - "觉醒" 匹配人类世——命名一个新的地质意识：人类已成为地质营力
  - "渐亮" 匹配其人生弧线——从桥梁工地到世界最快计算机旁的程序员，再到诺贝尔领奖台
- **时长**：以文件实际时长为准（> 15 页 × 7 秒 ≈ 105 秒即可），ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 读懂臭氧层的人 / Paul J. Crutzen 1933–2021 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士导师/出生地/去世地/领域/机构/荣誉）
03  克鲁岑的一生 — 时间线（10 节点：1933→1951→1959→1968→1970→1974→1980→1982→1995→2000）
04  战时童年与土木工程 (1933–1958) — 表格「时间|事件|结果」
05  斯德哥尔摩：程序员入行 (1959–1968) — 表格「阶段|工具|结果」+ 公式框：O/O₂/O₃ 光化学箱式模型
06  N₂O 与平流层 NOx (1970–1971) — 表格「问题|链条|结论」+ 公式框：N₂O → NO → 破坏 O₃
07  1974 预印本时刻 — 表格「事件|回应|意义」（Rowland/Molina 预印本 → 立即建模）
08  美因茨与三个舞台 (1980–1996) — 表格「机构|角色|领域」（MPIC / Scripps / Utrecht）
09  核冬天 (1982) — 表格「假设|机理|预言」+ 公式框：黑烟遮阳 → 地表降温
10  1995 诺贝尔化学奖 — 表格「得主|贡献|结果」（三人共享；臭氧的生成与分解）
11  人类世 (2000) — 表格「概念|提议|起点」（与 Stoermer；18 世纪后半叶 / 1784）
12  晚年论争与荣誉 — 表格「类别|代表|意义」（Tyler 1989 / ForMemRS 2006 / Lomonosov 2019；气候工程专文 2006）
13  遗产 — 四分类遗产盒 + 公式框：诺奖基础研究 → 全球禁令的空前范例（Stratmann 评价）
14  结尾 — 「人类第一次，把自己写进了地质年代表。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 获奖口径 | 1995 三人**共享**（Molina、Rowland）；官方理由页面原句 "for their work in atmospheric chemistry, particularly concerning the formation and decomposition of ozone"——Crutzen 的份额是**氮氧化物/臭氧形成与分解**，勿写「因发现 CFC 破坏臭氧」（那是 Molina/Rowland 的工作） |
| 双博士导师 | infobox 明载 **Bert Bolin 与 Georg Witt** 两人——勿只写一人 |
| 1971 SST | 是 Crutzen 与（独立地）Harold Johnston 提出；页面明载「后续分析对这一担忧有争议」——须带争议注记，勿写成定论 |
| 1991 科威特油火 | 页面作「假设（hypothesized）将产生显著核冬天式效应」——是假说，勿写成「验证」 |
| 人类世起点 | Crutzen 与 Stoermer 提议**18 世纪后半叶**（与瓦特蒸汽机 1784 相合），并自知存在其他提议（有人主张全新世整体）——勿写成定论年份 |
| 国籍 | 荷兰人（页面口径 Dutch）；metadata 并列 Germany（长期定居美因茨）——封面与 yaml 主写 Netherlands，Germany 作 rank 1 注明定居 |
| 职业起点 | 是**土木工程出身的程序员**，非科班气象学家——勿写成「自幼立志大气科学」；「饥饿之冬」可客观陈述 |
| 核冬天 | 首篇论文 1982 与 **John W. Birks** 合著；「nuclear winter」概念是 Crutzen 与同僚推动——勿把 1991 科威特假说当成 1982 论文内容 |
| h-index | 151（Google Scholar）/ 110（Scopus），**截至 2021**——两口径勿混 |
| 引语红线 | 可引用（页面原文）：诺奖理由句、人类世提议段（"we propose the latter part of the 18th century..."）、Stratmann 身后评价句、诺奖演讲题名 "My Life with O3, NOx and Other YZOxs"；中文引号内不得出现无法在 page.md 溯源的「原话」 |
| 个人生活 | 1956 相识 Terttu Soininen、1958-02 结婚；两女（1958-12 与 1964-03；迁瑞典时携幼女 Ilona 的记载与 1958-12 出生并行不悖）——年份以页面两处口径为准，勿加第三名子女 |
| 政治署名 | 70 名诺奖得主联名反对路易斯安那州创设主义法、2003 署名人本宣言——可客观一句带过，不渲染 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q135139 | ✅ |
| name_zh | 保罗·克鲁岑 | ✅ |
| name_en | Paul J. Crutzen | ✅ |
| birth_date | 1933-12-03 | ✅ |
| death_date | 2021-01-28 | ✅ |
| nationality | Netherlands（rank 0）/ Germany（rank 1，长期定居美因茨） | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | atmospheric chemistry（person_field 细分：atmospheric chemistry / meteorology / ozone layer / climate change，带 rank） | ✅ |
| has_biography | false（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 家人 / 同事 / 共同得主 / 门生**（★ 只收 page.md 正文或 infobox 明载的关系）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Bert Bolin | 师→生（博士导师） | 斯德哥尔摩大学气象系（infobox 双导师之一） |
| advisor-student | Georg Witt | 师→生（博士导师） | 斯德哥尔摩大学（infobox 双导师之一） |
| advisor-student | Johannes Lelieveld | 生→师（学生） | infobox Doctoral students |
| advisor-student | Deliang Chen | 生→师（学生） | infobox Doctoral students |
| spouse | Terttu Soininen | 无向 | 1956 相识，1958-02 结婚；两女 |
| colleague | Harold Johnston | 无向 | 1971 各自独立提出 SST 的 NO 排放损耗臭氧层 |
| colleague | John W. Birks | 无向 | 1982 合著首篇核冬天论文 "Twilight at noon" |
| colleague | Eugene F. Stoermer | 无向 | 2000 共同提议「人类世」术语（IGBP Newsletter 41） |
| co-honored | Mario J. Molina | 无向 | 1995 诺贝尔化学奖共同得主（CFC-臭氧） |
| co-honored | F. Sherwood Rowland | 无向 | 1995 诺贝尔化学奖共同得主（CFC-臭氧） |

> metadata.json-only 的关系（如各荣誉学位授予方、联名信其他签署人）**不予入库**。

## 8. 奖项清单

- Nobel Prize in Chemistry（1995，与 Molina、Rowland 共享）
- NOAA Outstanding Publication Award（1976）；Rolex-Discover Scientist of the Year（1984）
- Leó Szilárd Lectureship Award, "Physics in the Publics Interest", American Physical Society（1985）；Fellow of the American Geophysical Union（1986）
- Tyler Prize for Environmental Achievement（1989）；Volvo Environment Prize（1991）
- Corresponding Member, Royal Netherlands Academy of Arts and Sciences（1990）；Global Ozone Award, UNEP（1995）
- Foreign Member of the Royal Society, ForMemRS（2006）；American Philosophical Society 国际成员（2007）
- Foreign Member, Russian Academy of Sciences（1999）；Lomonosov Gold Medal（2019）；Royal Netherlands Chemical Society 荣誉成员（2017）
- 多所大学荣誉博士（Burgundy、Joseph Fourier、Ca' Foscari、Tel Aviv、Liège、Louvain、Athens 等）；Max Planck Research Award；German Environmental Prize；Humboldt Prize；Commander of the Order of the Netherlands Lion

## 9. 机构清单

- 教育：阿姆斯特丹小学与 Hogere Burgerschool（–1951）；高等职业教育土木工程；Stockholm University（PhD 1968）
- 任职：斯德哥尔摩大学气象系（程序员 1959 起 → 研究教授）；牛津 Clarendon Laboratory 博士后（ESRO，1968 后）；NOAA / Colorado State University（1970s，含 1976 NOAA 奖）；马克斯·普朗克化学研究所大气化学系（1980–，美因茨）；Scripps Institution of Oceanography（UCSD）；首尔国立大学；Georgia Tech 长期 adjunct professor；Utrecht University 高层大气学教授（1997–2002）；皇家瑞典科学院成员、英国皇家学会外籍成员

## 10. 终审清单

- [ ] 生卒 1933-12-03 / 2021-01-28，享年 87，出生地阿姆斯特丹、去世地美因茨
- [ ] 1995 三人共享表述准确；Crutzen 份额（NOx/臭氧形成分解）与 Molina/Rowland（CFC）未混
- [ ] 双博士导师 Bolin + Witt；1968 论文题名准确
- [ ] N₂O→NO 链条与 SST 争议注记准确；核冬天 1982 Birks、人类世 2000 Stoermer
- [ ] h-index 两口径（151/110）与时间基准（2021）未混
- [ ] 引语全部可在本地 Wikipedia 原文找到
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Paul_J._Crutzen/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/` 肖像已就位或装饰圆占位（注明理由）
- [ ] **国籍**：封面顶部明示荷兰
- [ ] **引语核对**：诺奖理由句、人类世提议段、Stratmann 评价句须在 Wikipedia 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger、Kary_Mullis 等）对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 的更新由主控统一收尾（本提示词不直接改动）。
> **最重要的事：每写一页就 make，看到溢出就修。**
