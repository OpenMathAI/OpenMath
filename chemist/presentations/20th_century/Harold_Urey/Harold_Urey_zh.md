# Harold Urey（哈罗德·尤里）立传提示词

> qid=Q179777 · 1893-04-29 – 1981-01-05 · 美国物理化学家 · 20 世纪 · 诺贝尔化学奖（1934，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Harold_Urey/`（page.md + metadata.json + page.html + images.txt）

---

## 0. 正文形式说明（参考 Frederick Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。**注意：本地 images.txt 无独立肖像照**（仅签名 SVG、S-1 委员会合影、Miller–Urey 实验图）——执行时先试 Wikipedia REST API `page/summary` 查 infobox 原图（1934 年照 "Urey in 1934" 应存在）；仍 404 则用**装饰圆占位**，或用 S-1 合影（1942）裁左一并加注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 重氢的发现者\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（Harold Clayton Urey）、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「同位素分离」母题——轻重两种圆点成对散布，暗示氢/氘只差一个中子。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）——氘发现页写 Balmer 系蓝移预言与 5 L→1 mL 蒸馏富集，Miller–Urey 页写 CH₄/NH₃/H₂ + 电火花 → 氨基酸。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Harold Clayton Urey（中文惯称：哈罗德·克莱顿·尤里；ForMemRS）
- **生卒**：1893-04-29 生于印第安纳州 Walkerton → 1981-01-05 逝于加利福尼亚州 La Jolla（圣迭戈），享年 87；葬于印第安纳 DeKalb County 的 Fairfield Cemetery
- **国籍**：United States（美国）
- **身份**：物理化学家（physical chemist），同位素研究先驱；曼哈顿计划重要参与者；宇宙化学奠基人之一
- **家庭**：父 Samuel Clayton Urey（学校教师兼 Church of the Brethren 牧师）、母 Cora Rebecca（娘家姓 Reinoehl），德裔家庭；弟 Clarence、妹 Martha；父患肺结核举家迁加州 Glendora 又迁回印第安纳，尤里 6 岁丧父。1926 年娶 Frieda Daum（经蒙大拿同事 Kate Daum 结识，在堪萨斯 Lawrence 其父家成婚）；四子女：Gertrude Bessie（Elizabeth，1927，后为物理学家 Elizabeth Baranger）、Frieda Rebecca（1929）、Mary Alice（1934，出生年恰逢诺贝尔奖，为此缺席斯德哥尔摩典礼）、John Clayton（1939）
- **教育轨迹**：Amish 小学（14 岁毕业）→ Kendallville 高中（1911）→ Earlham College 教师证书，印第安纳乡村小学任教 → 蒙大拿继续任教 → 1914 入 University of Montana，1917 动物学 BS → 一战期间在费城 Barrett Chemical 造 TNT（宗教反战而非从军）→ 战后回蒙大拿任化学讲师 → 1921 入加州大学伯克利分校博士
- **博士**：1923，伯克利；初选铯蒸气电离课题被 Meghnad Saha 更好论文抢先，改写理想气体电离态（后发表于 Astrophysical Journal）
- **导师**：Gilbert N. Lewis（伯克利，热力学）
- **博士后**：1923 美国斯堪的纳维亚基金会奖学金赴哥本哈根 Niels Bohr 研究所——期间遇见 Heisenberg、Kramers、Pauli、George de Hevesy、John Slater；赴德遇见 Einstein 与 James Franck
- **研究领域**：物理化学——同位素、宇宙化学、古气候学、生命起源

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **牧师之子与反战青年（1893–1917）**：Church of the Brethren 教派（反战）家庭；一战以化学工人造 TNT 替代从军——宗教良知与技术报国的第一次平衡。
2. **伯克利与玻尔研究所（1921–1924）**：Lewis 门下读热力学；哥本哈根一年置身量子力学黄金年代——从玻尔身边带回光谱与统计视角。
3. **Hopkins 与量子力学教科书（1924–1929）**：与 Arthur Ruark 合著 *Atoms, Quanta and Molecules*（1930）——最早的英文量子力学教科书之一。
4. **哥伦比亚与氘的预言（1929–1931）**：Giauque 与 Johnston 发现氧的稳定同位素后，Birge 与 Menzel 由原子量差额推知氢应另有重同位素（4500 个氢原子约 1 个重氢）。
5. **氘的发现（1931–1932）**：与 George M. Murphy 由 Balmer 系计算重氢谱线应有 1.1–1.8 Å 蓝移；用哥伦比亚新装 21 英尺光栅摄谱仪；按 Debye 模型推知重氢沸点略高，赴国家标准局 Brickwedde 处蒸馏液氢——5 L 富集到 1 mL、富集 100–200 倍；第一份样品（20 K 蒸发）无信号，第二份（14 K、53 mmHg）重氢 Balmer 线强 7 倍——1932 与 Murphy、Brickwedde 联名发表。
6. **异常样本之谜与重水**：与 NBS 的 Edward W. Washburn 查明首样异常系电解分离致贫化；Aston 修正氢原子量又推翻 Birge–Menzel 推理——但氘的发现成立；电解制纯重水被 Lewis（1933）抢先。
7. **同位素示踪革命**：用 Born–Oppenheimer 近似与 David Rittenberg 计算氢/氘气体性质，推广到碳氮氧化合物富集——生物化学示踪法的全新工具；1932 创办 *Journal of Chemical Physics* 并任首任主编（至 1940）。
8. **1934 诺贝尔化学奖**：官方理由 "for his discovery of heavy hydrogen"——**独享**；因女儿 Mary Alice 出生缺席斯德哥尔摩典礼；同年获 Willard Gibbs Award，1940 获 Davy Medal。
9. **曼哈顿计划（1939–1945）**：世界级同位素分离专家；协调全部同位素分离研究（离心、气体扩散、热扩散、重水）；1941 与 George B. Pegram 率使团赴英协调；1943 出任哥伦比亚 SAM 实验室主任（重水与除 Lawrence 电磁法外的一切浓缩工艺），鼎盛时逾 700 人；K-25 气体扩散厂成为战后初期唯一分离手段；1945-02 力竭交棒 R. H. Crist；获 Medal for Merit（Groves 将军颁发）。
10. **战后芝加哥与古气候学**：核研究所教授、1952 Ryerson 化学教授；发现氧-18/氧-16 分馏随温度变化（0→25 ℃ 变化 1.04 倍）——测定 1 亿年箭石四季温度，开创古气候学；与 Bigeleisen、Mayer 提出 Urey–Bigeleisen–Mayer 同位素分馏方程；获 Arthur L. Day Medal 与 V. M. Goldschmidt Award。
11. **宇宙化学与生命起源**：提出碳酸盐–硅酸盐循环（"Urey reactions"），1952 年 Silliman 讲座成书 *The Planets: Their Origin and Development*；推测原始大气为氨+甲烷+氢；芝加哥博士生 Stanley L. Miller 以电火花实验验证——生成氨基酸（Miller–Urey experiment）。
12. **UCSD 建校与月球（1958–1981）**：65 岁到新成立的 UCSD 任 professor at large，与 Miller、Hans Suess、James R. Arnold 共创化学系（1960）；推动 NASA 无人探月优先；Apollo 11 月岩在 Lunar Receiving Laboratory 由其检验，支持月球与地球同源说；UCSD 期间发表 105 篇论文（47 篇月球主题）；"Urey ratio"（行星内部生热/表面热流比）以他命名。
13. **社会担当**：反对 1946 May-Johnson 法案（防军方控核）、支持 McMahon 法案促成 AEC；世界政府理想；公开为 Rosenberg 夫妇辩护并遭众院非美活动委员会传唤；名言（对 Schmitt 自荐单程登月）"I will go, and I don't care if I don't come back."；"Well, you know I'm not on tenure anymore."（晚年自嘲继续工作）

## 3. 配色方案（主色 + 强调 + 分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（砖红 brickred） | `#9E2B25` | 重氢谱线的深红与岩石行星的大地色（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（同位素 badgeIso） | `#2E5A9E` | 蓝氘 / 重水 / 分离工艺 |
| 分类色 2（宇宙化学 badgeCosmo） | `#8E44AD` | 紫行星起源 / 月岩 / Urey ratio |
| 分类色 3（生命起源 badgeOrigin） | `#1B7A43` | 绿 Miller–Urey / 原始大气 |
| 分类色 4（古气候 badgePaleo） | `#D97B29` | 琥珀氧-18 温度计 / 箭石 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（轻重两种圆点成对出现，四档大小错落），呼应「同位素」的一素两重。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Winds Of Freedom** — Really Slow Motion & Giant Apes（路径 `music_audio/inspiring-electronic/25-l3Fsk4R6eys-...Winds Of Freedom (Epic Heroic Orchestral).wav`）
- **风格**：史诗 / 雄浑 / 长程叙事
- **匹配理由**：
  - "史诗" 匹配其跨度——从氘的谱线到曼哈顿计划再到月球，纵贯半个世纪的科学远征
  - "雄浑" 匹配其公共担当——反战、世界政府、为 Rosenberg 辩护的风骨
  - "自由之风" 暗合战后科学自由与核能公共治理之争
- **时长**：执行时核对，不足 15 页 × 7 秒则循环或 ffmpeg 对齐

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 重氢的发现者 / Harold Urey 1893–1981 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  尤里的一生 — 高斯式时间线（10 节点：1893→1917→1923→1929→1932→1934→1943→1952→1958→1981）
04  早年：牧师之家与反战青年 (1893–1921) — 表格「时间|事件|结果」
05  伯克利与哥本哈根 (1921–1929) — 表格「阶段|导师/环境|收获」
06  氘的发现 (1931–1932) — 表格「问题|方法|结果」+ 公式框：Balmer 蓝移预言 + 5L→1mL 富集
07  1934 诺贝尔化学奖 — 官方理由原句 "for his discovery of heavy hydrogen" + 表格「奖项|年份|意义」
08  曼哈顿计划：同位素分离总协调 (1939–1945) — 表格「路线|负责人/工艺|结果」（SAM 700 人 / K-25）+ Medal for Merit
09  芝加哥：古气候学开创 (1946–1958) — 表格「问题|方法|结果」+ 公式框：氧-18 分馏 1.04 倍 / Urey–Bigeleisen–Mayer 方程
10  Miller–Urey 实验 (1952–1953) — 表格「假说|实验|结果」+ 公式框：CH₄+NH₃+H₂ +电火花→氨基酸
11  UCSD 与月球 (1958–1981) — 高斯 FFT 页式流程图（建系 1960 → 说服 NASA → Apollo 11 月岩 → 同源说）
12  社会担当 — 表格「议题|立场|结果」（May-Johnson/McMahon、世界政府、Rosenberg 案）
13  遗产与命名 — 四分类遗产盒 + 命名清单（Urey 陨石坑 / 4716 Urey / H. C. Urey Prize / Urey Hall / Urey ratio）
14  结尾 — 「从一克重水里，读出地球与星辰的历史。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1934 诺奖理由 | 官方措辞 "for his discovery of heavy hydrogen"（重氢的发现），**独享**——勿写"发现重水"获奖（重水是后续工作，且制纯重水被 Lewis 抢先） |
| 氘发现署名 | 1932 论文为 Urey + **George M. Murphy + Ferdinand Brickwedde** 三人联名——勿只写尤里一人 |
| 首样异常 | 第一份 20 K 样品**无**富集信号，第二份 14 K/53 mmHg 样品线强 7 倍——异常根源是电解致贫化（与 Washburn 查明）+ Aston 修正氢原子量；勿写"一次成功" |
| 博士课题 | 初选铯蒸气电离被 **Meghnad Saha** 抢发，改做理想气体电离态——勿漏这一波折 |
| 缺席典礼 | 因女儿 Mary Alice 出生**拒绝出席**斯德哥尔摩典礼——勿写"未受邀" |
| 曼哈顿角色 | 协调同位素分离（含重水），SAM 实验室主任，1945-02 力竭离任交棒 **R. H. Crist**；K-25 建成于其离任前（1944 屏障量产/1945-03 投产）——时间线勿倒置 |
| S-1 合影 | 1942 Bohemian Grove 合影人物为 Urey/Lawrence/Conant/Briggs/Murphree/Compton——仅作插图图注，不因此页入 S-1 全员关系 |
| 学生名单 | infobox Doctoral students 仅 **Stanley Miller、Harmon Craig、Mildred Cohn、Gerald Wasserburg** 四人；Ralph Buchsbaum 是 colleague 非 student——勿混 |
| Edward W. Washburn | 全名 Edward Wight Washburn，NBS 物理化学家——与尤里共同查异常、试制重水；勿与同名他人混淆 |
| 政治争议 | 为 Rosenberg 夫妇公开辩护并遭 HUAC 传唤——客观一句带过，不加立场渲染；曼哈顿计划只写史实不展开杀伤评价 |
| 生年口径 | 1893-04-29（infobox 与正文一致）；metadata frontmatter 另有 "1893-00-00" 噪声值——弃用 |
| 引语红线 | 可用引语仅三条：获奖理由、"I will go, and I don't care if I don't come back."（Schmitt 转述）、"Well, you know I'm not on tenure anymore."；其余一律间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q179777 | ✅（回填至既有 stub #2111） |
| name_zh | 哈罗德·尤里 | ✅ |
| name_en | Harold Urey | ✅（用 db_name_en 精确形式） |
| birth_date | 1893-04-29 | ✅ |
| death_date | 1981-01-05 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | physical chemist | ✅ |
| field_of_work | isotopes（person_field 细分：isotopes / cosmochemistry / paleoclimatology / origin of life，带 rank） | ✅ |
| has_biography | false（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 合作者 / 门生**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Gilbert N. Lewis | 师→生（博士导师） | 伯克利热力学，1923 PhD |
| advisor-student | Stanley Miller | 尤里→学生 | 芝加哥博士生；Miller–Urey 实验 |
| advisor-student | Harmon Craig | 尤里→学生 | infobox doctoral students |
| advisor-student | Mildred Cohn | 尤里→学生 | infobox doctoral students |
| advisor-student | Gerald Wasserburg | 尤里→学生 | infobox doctoral students |
| colleague | George M. Murphy | 无向 | 1932 共同发表氘的发现（谱线计算） |
| colleague | Ferdinand Brickwedde | 无向 | NBS 液氢蒸馏富集，1932 联名论文 |
| colleague | Edward W. Washburn | 无向 | 查明首样异常、合作电解制重水 |
| colleague | David Rittenberg | 无向 | Born–Oppenheimer 近似计算同位素气体性质 |
| colleague | Arthur Ruark | 无向 | 1930 合著 Atoms, Quanta and Molecules |
| colleague | Rudolph Schoenheimer | 无向 | 哥伦比亚同位素示踪同事 |
| colleague | Ralph Buchsbaum | 无向 | 氧-18 古气候团队同事 |
| colleague | Hans Suess | 无向 | UCSD 化学系共同创建者（1960） |
| colleague | James R. Arnold | 无向 | UCSD 化学系共同创建者；UCSD Urey 讲席首任 |
| colleague | George B. Pegram | 无向 | 1941 共率赴英使团协调原子弹合作 |
| colleague | George Kistiakowsky | 无向 | 提议气体扩散法路线 |
| other | Enrico Fermi | 无向 | 尤里协助流亡科学家（含费米）赴美安顿 |
| other | Leslie Groves | 无向 | 曼哈顿计划总监向尤里颁发 Medal for Merit |

**家庭**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Frieda Daum | 无向 | 1926 年结婚（堪萨斯 Lawrence） |
| parent-child | Elizabeth Baranger | 尤里→孩子 | 长女 Gertrude Bessie（Elizabeth），后为知名物理学家 |

> **禁入库名单**（metadata.json-only 或页面仅带过、无实质互动载述）：Werner Heisenberg / Hans Kramers / Wolfgang Pauli / George de Hevesy / John C. Slater / Albert Einstein / James Franck（玻尔所与德国行"遇见"，无合作载述）、T. I. Taylor（redlink 同事）、Ernest Lawrence / Arthur H. Compton / James B. Conant / Lyman J. Briggs / Eger V. Murphree（仅 S-1 合影图注同框）、Meghnad Saha（课题竞争，非关系）、William Giauque / Herrick L. Johnston / Raymond Birge / Donald Menzel / Francis William Aston（领域背景人物）、Kate Daum（介绍人）、Clarence / Martha（手足无独立载述）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1934，独享）
- Willard Gibbs Award（1934）
- Davy Medal（1940）
- Franklin Medal（1943）
- Medal for Merit（1946）
- Fellow of the Royal Society（ForMemRS，1947）
- J. Lawrence Smith Medal（1962）
- National Medal of Science（1964）
- Gold Medal of the Royal Astronomical Society（1966）
- Golden Plate Award（1966）
- Priestley Medal（1973）
- V. M. Goldschmidt Award（1975）
- Arthur L. Day Medal（Geological Society of America）
- American Philosophical Society 与美国国家科学院院士（1934）；美国物理学会会士

## 9. 机构清单

- 教育：Earlham College（教师证书）、University of Montana（BS 1917）、University of California, Berkeley（PhD 1923）；博士后 Niels Bohr Institute（1923–1924）
- 任职：Johns Hopkins University（1924–1929 research associate）→ Columbia University（1929 副教授；1943–1945 SAM 实验室主任）→ Institute for Nuclear Studies / University of Chicago（Ryerson 教授 1952）→ 牛津访问教授（1956–1957）→ UCSD（1958 professor at large；1970–1981 emeritus）
- 命名遗产：月球 Urey 陨石坑、小行星 4716 Urey、H. C. Urey Prize（AAS 行星科学）、Harold C. Urey Middle School（Walkerton）、Urey Hall（UCSD）、Harold C. Urey Lecture Hall（蒙大拿大学）

## 10. 终审清单

- [ ] 生卒 1893-04-29 / 1981-01-05，享年 87，出生地 Walkerton、去世地 La Jolla
- [ ] 1934 独享、理由 "for his discovery of heavy hydrogen" 原句表述准确
- [ ] 氘发现三人联名（Urey/Murphy/Brickwedde）；首样异常与 Aston 修正表述准确
- [ ] 博士课题 Saha 波折、缺席典礼缘由表述准确
- [ ] 曼哈顿时间线（1941 使团→1943 SAM→1945-02 交棒）准确
- [ ] 学生四人名单与 Buchsbaum colleague 口径准确
- [ ] 引语仅三条白名单且可在 page.md 溯源
- [ ] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Harold_Urey/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：REST API 查 "Urey in 1934" infobox 原图；404 则装饰圆占位（勿误用签名图当肖像）
- [ ] **国籍**：封面顶部明示美国
- [ ] **引语核对**：三条白名单引语必须在 Wikipedia 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Frederick_Sanger_zh.tex）对齐
