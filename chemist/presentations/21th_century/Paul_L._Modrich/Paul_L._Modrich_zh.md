# Paul L. Modrich（保罗·莫德里奇）立传提示词

> qid=Q7151888 · 1946-06-13 – 在世 · 美国生物化学家 · 21 世纪 · 诺贝尔化学奖（2015，与 Aziz Sancar、Tomas Lindahl 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Paul_L._Modrich/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 表格语义化 tabularx + 金色公式框 + 时间线页，是本次执行的版式语言。

---

## 0. 正文形式说明（参考桑格立传模板，★ 硬性要求）

1. **封面有头像位**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。本地 `images.txt` **无真实肖像**——用主色装饰圆占位（圆内放 `\faIcon{dna}` 图标），并在图注注明「装饰圆占位 · 页面无肖像」。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{book-open}\enspace DNA 的复制校对者\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素（杜克大学 / HHMI · 错配修复 · 2015 诺贝尔化学奖）。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像（装饰圆）+ 右侧 2×2 信息网格，至少含：生卒、本名 Paul Lawrence Modrich、国籍、出生地 Raton, New Mexico、教育（MIT / Stanford）、博士导师 Robert Lehman、核心领域 DNA mismatch repair、机构（Duke / HHMI）、荣誉。事实取自本地 page.md，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「校对 / 纠错」母题——成对出现的圆点暗示错配碱基对被逐一识别、修正。
5. **表格语义化 + 公式框**（★ 桑格版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Paul Lawrence Modrich（中文惯称：保罗·L·莫德里奇）
- **生卒**：1946-06-13 生于美国新墨西哥州 Raton → 在世（页面无卒日，全篇留白处理）
- **国籍**：United States（美国）
- **身份**：生物化学家（biochemist）；杜克大学 James B. Duke 生物化学教授、霍华德·休斯医学研究所（HHMI）研究员
- **家庭**：父 Laurence Modrich 为 Raton 高中生物教师兼篮球/橄榄球/网球教练，母 Margaret McTurk；有一弟 Dave；血统为克罗地亚、黑山、德意志与苏格兰-爱尔兰混合——祖父辈 19 世纪末自克罗地亚沿海移民美国；1980 年娶科学家同行 Vickers Burdett
- **教育轨迹**：
  - Raton High School，1964 年毕业（同年获 Regeneron Science Talent Search，时称 Westinghouse）
  - 1968 麻省理工学院（MIT）B.S.
  - 1973 斯坦福大学 Ph.D.（论文 *Structure, mechanism and biological role of E. coli DNA ligase*）
  - 1973–1974 哈佛医学院 Charles C. Richardson 实验室博士后（一年）
- **导师**：Robert Lehman（斯坦福博士导师）
- **研究领域**：DNA 错配修复（DNA mismatch repair）——链指向错配修复的生化机制；亦以「Modrich–Lehman unit」知名（DNA 连接酶活性度量单位）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **新墨西哥小城（1946）**：生物教师之子在 Raton 长大；高中毕业之年即获全国性科学奖（Regeneron Science Talent Search, 1964）。
2. **MIT 起点（1968）**：本科化学训练，随后西赴斯坦福。
3. **DNA 连接酶博士（1973）**：斯坦福 Lehman 门下测定 E. coli DNA 连接酶的结构、机制与生物学角色；两人的姓氏后来合成酶学度量单位「Modrich–Lehman unit」。
4. **哈佛博士后（1973–1974）**：在 DNA 复制名家 Charles C. Richardson 实验室一年，完成复制方向的训练。
5. **伯克利教职（1974）**：任加州大学伯克利分校化学系助理教授。
6. **转战杜克（1976）**：加入杜克大学，此后学术生涯四十余年扎根于此。
7. **错配修复的「校对员」模型**：其实验室证明 DNA 错配修复像 copyeditor 一样工作，防止 DNA 聚合酶的复制错误——把 Meselson 早先提出的「错配可被识别」假说落到生化实验。
8. **大肠杆菌先行（1970s–1980s）**：以生化实验系统研究 E. coli 错配修复，鉴定相关蛋白组分与链指向机制。
9. **迈向人类（1990s）**：实验室转而寻找人类细胞中的错配修复蛋白——错配修复缺陷与癌症（遗传性非息肉病性结直肠癌等）的关联由此获得生化基础。
10. **HHMI 研究员（1995）**：自 1995 年起任霍华德·休斯医学研究所研究员。
11. **2015 诺贝尔化学奖**：与 Aziz Sancar、Tomas Lindahl 共享——三人分别厘清错配修复、核苷酸切除修复与碱基切除修复，合起来是「DNA 修复的机制学研究」。
12. **三院与学会**：美国艺术与科学院会士，美国国家医学院与美国国家科学院院士。
13. **教学与传承**：以 James B. Duke Professor 身份在杜克执教至今；杜克大学 2016 年授予其北卡罗来纳州公共服务奖体系中的州级荣誉（North Carolina Award），2017 年赴布尔诺主讲 Mendel Lecture。

## 3. 配色方案（桑格式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（斯文蓝 steelblue） | `#37548D` | 错配修复的分子精确与冷静（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（错配修复 badgeMMR） | `#1F6F8B` | 青蓝·复制校对员 / 链指向机制 |
| 分类色 2（DNA 连接酶 badgeLig） | `#8C6A2F` | 琥珀·Modrich–Lehman unit / 斯坦福岁月 |
| 分类色 3（人类 MMR 与癌症 badgeCan） | `#A63A2B` | 砖红·从大肠杆菌到人类 / 癌症关联 |
| 分类色 4（诺奖与荣誉 badgeHonor） | `#2E5A9E` | 皇家蓝·2015 斯德哥尔摩 / 三院院士 |
| 背景 | `#F7F6F9` | 浅灰白（与桑格版一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），成对圆点暗示「错配 → 修正」的校对过程。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Savage** — Alex-Productions（`music_audio/alex-productions/34-pILVwyuW3jw-Savage.wav`；不要复制 wav 文件，Makefile 里直接引用原路径）
- **风格**：紧凑 / 冷峻 / 侦探式的机制拆解
- **匹配理由**：
  - 「冷峻」匹配错配修复研究的气质——不是戏剧性发现，而是四十年把一条修复通路逐个蛋白拆开
  - 「侦探式」匹配「copyeditor」叙事——在三十亿碱基对里揪出复制错误
  - 「紧凑」匹配时间线页节奏——Raton → MIT → Stanford → Berkeley → Duke → HHMI → 斯德哥尔摩
- **时长**：按 Makefile 默认 `-shortest` 对齐 15 页即可

## 4. Slide 规划（15 页，桑格式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — DNA 的复制校对者 / Paul L. Modrich 1946– + 四色 badge + 右上头像占位 + 国籍行「美国」
02  身份信息页（★ 必做）— 左头像占位 + 右 2×2 信息网格（生卒/本名/国籍/出生地/教育/博士导师/领域/机构/荣誉）
03  莫德里奇的一生 — 桑格式时间线（10 节点：1946→1964→1968→1973→1974→1976→1993→1995→2015→2016）
04  早年：新墨西哥生物教师之子 (1946–1968) — 表格「时间|事件|结果」
05  MIT → Stanford：DNA 连接酶 (1968–1974) — 表格「阶段|内容|结果」+ 公式框：Modrich–Lehman unit
06  错配修复：复制校对员 (1976–1990s) — 表格「问题|方法|结果」+ 公式框：错配修复 = 防聚合酶出错
07  链指向机制：从大肠杆菌出发 (1980s) — 表格「挑战|方法|结果」
08  从大肠杆菌到人类 (1990s–) — 表格「问题|方法|结果」+ 公式框：MMR 缺陷 ↔ 癌症易感
09  2015 诺贝尔化学奖 — 公式框：官方获奖理由 "for mechanistic studies of DNA repair"（与 Sancar / Lindahl 共享，三人三条修复通路）
10  师承与同行 — 表格「人物|方向|结果」（Lehman / C.C. Richardson / Meselson / Vickers Burdett）
11  荣誉与学会 — 桑格式「类别|代表|意义」表格 + itemize 荣誉清单（Pfizer 1983 / Mott 1996 / Pasarow 1998 / NAS 1993）
12  杜克与 HHMI — 桑格 LMB 页式流程图（1976 入杜克 → 1995 HHMI → James B. Duke Professor → 2017 Mendel Lecture）
13  遗产：基因组忠实复制的第一道防线 — 四分类遗产盒 + 公式框：错配修复守护突变率
14  结尾 — 「每一次忠实的复制，背后都有一位不知疲倦的校对者。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2015 获奖理由 | 官方口径 "for mechanistic studies of DNA repair"（本页行文作 "their mechanistic studies of DNA repair"）；三人各管一条通路——Modrich=错配修复、Sancar=核苷酸切除修复/光复活、Lindahl=碱基切除修复，**勿互相张冠李戴** |
| 共享口径 | 2015 为**三人共享**，勿写「独享」或「两人共享」；对 Lindahl/Sancar 一律用规范全名 Tomas Lindahl / Aziz Sancar |
| 在世口径 | 页面无卒日——全篇生卒写 1946-06-13 – 在世，**禁止编造卒年** |
| 博士导师 | 斯坦福博士导师是 **Robert Lehman**（论文 1973 *Structure, mechanism and biological role of E. coli DNA ligase*）；MIT 只是本科——勿把本科院校写成博士单位 |
| 博士后一年 | 1973–1974 在 **Charles C. Richardson**（哈佛医学院）实验室做博士后一年——勿与杜克的「Richardson」混淆成另一人 |
| Meselson 定位 | Matthew Meselson 是**早先提出错配可被识别假说**的先行者，Modrich 是用生化实验证实者——勿写成「师生」或「合作者」 |
| Modrich–Lehman unit | 是 **DNA 连接酶活性的度量单位**（以两人姓氏命名）——勿写成「共同发现连接酶」 |
| 任职顺序 | 1974 伯克利助理教授 → 1976 杜克 → 1995 HHMI——勿写成「先杜克后伯克利」 |
| 奖项年份 | Regeneron Science Talent Search 1964（高中）；Pfizer Award in Enzyme Chemistry 1983；NAS 院士 1993；Mott Prize 1996；Pasarow 1998；Nobel 2015；North Carolina Award 2016；Kornberg–Berg 终身成就奖 2016；Mendel Lecture 2017——年份勿混 |
| 家庭成员 | 父母 Laurence Modrich / Margaret McTurk、弟弟 Dave：**页面明载但仅作背景，不入库**；妻 Vickers Burdett 是「fellow scientist」，1980 结婚——勿写其具体研究方向（页面无载） |
| 引语红线 | 本页**无任何直接引语**——中文引号内不得出现无法在 page.md 溯源的「原话」，一律间接转述 |
| 插图 | images.txt 为空：封面用装饰圆占位；正文可用文字版式页，勿从外部抓图 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q7151888 | ✅ |
| name_zh | 保罗·莫德里奇 | ✅ |
| name_en | Paul L. Modrich | ✅ |
| birth_date | 1946-06-13 | ✅ |
| death_date | 空（在世） | ✅ |
| nationality | United States | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | DNA mismatch repair（person_field 细分见下表，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

**person_field 细分 rank 表**：

| name_en | rank | name_zh |
|---|---|---|
| DNA mismatch repair | 0 | DNA 错配修复 |
| biochemistry | 1 | 生物化学 |
| DNA repair | 2 | DNA 修复 |
| chemistry | 3 | 化学 |

## 7. 社会关系入库清单

**师长 / 同行 / 共同得主 / 家人**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Robert Lehman | 师→生（博士导师） | 斯坦福博士导师，1973 论文 E. coli DNA 连接酶；连接酶活性单位以两人姓氏命名 |
| colleague | Charles C. Richardson | 无向 | 1973–1974 哈佛医学院博士后东家 |
| influence | Matthew Meselson | 无向 | 早先提出错配可被识别的假说，Modrich 以生化实验证实 |
| co-honored | Aziz Sancar | 无向 | 2015 诺贝尔化学奖共同得主 |
| co-honored | Tomas Lindahl | 无向 | 2015 诺贝尔化学奖共同得主 |
| spouse | Vickers Burdett | 无向 | 1980 结婚，同为科学家 |

> **禁入库名单**（页面明载但不入库）：父 Laurence Modrich、母 Margaret McTurk、弟 Dave（家庭成员，非学术关系）；各类奖项命名者（Arthur Kornberg、Paul Berg——仅出现在奖项名称中，非本人关系）。 metadata.json 中无额外关系字段。

## 8. 奖项清单

- Regeneron Science Talent Search（1964）
- Camille Dreyfus Teacher-Scholar Awards（1977）
- Pfizer Award in Enzyme Chemistry（1983）
- Member of the National Academy of Sciences（1993）
- Charles S. Mott Prize（General Motors 癌症研究奖，1996）
- Robert J. and Claire Pasarow Foundation Medical Research Award（1998）
- Feodor Lynen Medal（2000）
- American Cancer Society Medal of Honor（2005）
- Nobel Prize in Chemistry（2015，与 Sancar / Lindahl 共享）
- North Carolina Award（2016）
- Arthur Kornberg and Paul Berg Lifetime Achievement Award in Biomedical Sciences（2016）
- Mendel Lecture（2017）
- 会士/院士：American Academy of Arts and Sciences 会士；National Academy of Medicine 院士；National Academy of Sciences 院士

## 9. 机构清单

- 教育：Raton High School（1964 毕业）、MIT（B.S. 1968）、Stanford University（Ph.D. 1973）、哈佛医学院博士后（1973–1974，C.C. Richardson 实验室）
- 任职：University of California, Berkeley 化学系助理教授（1974–1976）；Duke University（1976–，James B. Duke Professor of Biochemistry）；Howard Hughes Medical Institute 研究员（1995–）

## 10. 终审清单

- [ ] 生卒 1946-06-13 – 在世（全篇无卒日留白一致）；出生地 Raton, New Mexico
- [ ] 2015 三人共享（Sancar / Lindahl）表述准确；获奖理由 "for mechanistic studies of DNA repair" 口径准确
- [ ] 三人分工不串位：Modrich=错配修复、Sancar=NER/光复活、Lindahl=BER
- [ ] 博士导师 Robert Lehman（Stanford 1973）；博士后 C.C. Richardson（Harvard Medical School 1973–74）
- [ ] 任职顺序 1974 Berkeley → 1976 Duke → 1995 HHMI 准确
- [ ] Modrich–Lehman unit 语义准确（连接酶活性单位）
- [ ] 全篇无编造引语；"第一次/唯一"类断言均未出现
- [ ] 正文采用桑格式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make pdf` 编译通过，0 错误、vbox≤10pt、hbox≤50pt

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Paul_L._Modrich/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：装饰圆占位（页面无肖像），图注注明
- [ ] 国籍：封面顶部明示美国
- [ ] 引语核对：本篇无引语——若 tex 中出现引号内英文原话须删改
- [ ] 编译验证：`make distclean && make pdf`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox<10pt、hbox<50pt 可接受）
- [ ] 身份信息页布局与桑格模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批（Sancar / Sauvage / Stoddart / Feringa）及桑格既有格式对齐

---

> **名单状态**：`chemist/generate_21th_century_list.py` 由主控统一收尾，执行者不改。
> **数据事实来源唯一**：`chemist/presentations/21th_century/pages/Paul_L._Modrich/page.md`；页面无载的数据如实标注「页面无载」，禁止编造。
