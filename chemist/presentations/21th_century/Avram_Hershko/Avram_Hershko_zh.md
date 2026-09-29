# Avram Hershko（阿夫拉姆·赫什科）立传提示词

> qid=Q232302 · 1937-12-31 生于匈牙利 Karcag（在世，卒日留白） · 匈牙利裔以色列生物化学家 · 21 世纪 · 诺贝尔化学奖（2004，与 Aaron Ciechanover、Irwin Rose 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Avram_Hershko/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 表格语义化 tabularx + 金框公式展示框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。肖像：images.txt 无真人照片 URL——执行时先经 Wikipedia REST API `/page/summary/Avram_Hershko` 查 infobox 原图名（页面有 "Hershko in 2023" 照片）下载（500px）；404 则用装饰圆占位，并在 Review-1 记录。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{tag}\enspace 给蛋白质贴上死刑标签的人\enspace·\enspace 匈牙利/以色列`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素（匈牙利→以色列 | Technion | 发现泛素介导的蛋白质降解）。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名 Herskó Ferenc Ábrahám（匈牙利语）、国籍（匈牙利→以色列）、出生地、教育（希伯来大学 MD 1965 / PhD 1969）、博士后、核心领域、现任（Technion 杰出教授 / NYU 兼职）、荣誉。事实取自本地 page.md infobox，不得杜撰；在世——卒栏写「在世（1937– ）」。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「泛素多标签缀合」母题——离散圆点暗示多条泛素链挂上底物蛋白。
5. **表格语义化 + 公式框**（★ 高斯/Sanger 版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）——1980 PNAS「ATP 为蛋白降解所需：蛋白与多肽链多重复缀合」、1995 cyclosome（APC）即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Avram Hershko（中文惯称：阿夫拉姆·赫什科；希伯来文 אברהם הרשקו，转写 Avraham Hershko；匈牙利文本名 **Herskó Ferenc Ábrahám**）
- **生卒**：1937-12-31 生于匈牙利 Karcag（时属匈牙利王国）（在世，卒日页面无载——全篇卒处一律留白）
- **国籍**：Hungary（1937 出生）→ Israel（1950 移民，此后）
- **身份**：生物化学家；Technion（海法）Rappaport 医学院杰出教授、纽约大学 Grossman 医学院杰出兼职教授
- **家庭**：犹太家庭；父 Moshe Hershko、母 Shoshana/Margit 'Manci'（娘家姓 Wulc），双亲皆为教师；兄 Chaim/Laszlo 'Laci'；妻 Judith Leibowitz（1963 年结婚），三子女
- **战争经历**：二战中父亲被征入匈牙利军劳役、后为苏军所俘，家人多年音讯全无；与母亲、兄长被关入 Szolnok 隔都；隔都末期多数犹太人被运往 Auschwitz——全家设法登上开往奥地利集中营的列车，被迫劳役至战争结束；母兄皆幸存，父亲四年后归来
- **教育轨迹**：1950 全家移民以色列耶路撒冷 → Hebrew University of Jerusalem–Hadassah Medical Center：MD 1965、PhD 1969
- **研究领域**：生物化学——泛素介导的蛋白质降解、泛素-蛋白酶体系统、细胞周期调控（cyclosome/APC）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **Karcag 的圣诞前夜（1937-12-31）**：生于匈牙利教师之家，本名 Herskó Ferenc——童年被战争彻底改写。
2. **隔都与集中营（1944–1945）**：Szolnok 隔都末期，全家避开了开往 Auschwitz 的死亡列车、转入奥地利劳役营——母亲、兄长与幼年的他幸存；父亲被征劳役又陷苏军战俘营，四年后归家。
3. **移民以色列（1950）**：定居耶路撒冷——从战争废墟走进新生国家。
4. **希伯来大学双学位（1965/1969）**：MD 1965、PhD 1969（希伯来大学–Hadassah 医学中心）。
5. **UCSF 博士后**：加州大学旧金山分校博士后研究——页面未载导师姓名（勿杜撰）。
6. **扎根 Technion（海法）**：Rappaport 医学院杰出教授——与 Ciechanover 在此完成泛素系统的大部分工作。
7. **1970s 追问**：细胞如何拆掉自己的蛋白？网织红细胞无细胞体系成为突破口。
8. **1980 PNAS 奠基**：与 Ciechanover、Heller、Haas、**Rose** 联名提出 ATP 在蛋白降解中的作用——蛋白与多肽因子多重复缀合；Rose 参与署名，是三人共同工作的实证。
9. **泛素-蛋白酶体系统**：泛素「贴标签」、蛋白酶体执行降解——维持细胞稳态， believed 与癌症、肌肉与神经疾病、免疫与炎症反应的发生发展相关（页面口径 believed to be involved，勿写定论）。
10. **1983–1995 系统解剖**：泛素-蛋白连接酶系统组分的解析（1983）；ATP 依赖的泛素-蛋白缀合物降解（1984）；1995 与团队发现 cyclosome——含周期蛋白选择性泛素连接酶活性的大复合物（后称 APC），在有丝分裂末销毁周期蛋白。
11. **1987–2003 奖项链**：Weizmann 奖（1987）→ 以色列奖生物化学（1994）→ Gairdner（1999）→ Lasker（2000）→ Wolf 医学奖（2001，"the discovery of the ubiquitin system of intracellular protein degradation and the crucial functions of this system in cellular regulation"）→ 美国 NAS 外籍会员（2003）。
12. **2004 诺贝尔化学奖**：与 Ciechanover、Rose 三人共享——发现泛素介导的蛋白质降解；其科学贡献「直接帮助治愈了一位多年挚友的癌症」（页面明载，可一句带过）。
13. **荣誉与传承**：以色列科学院（2000）、美国哲学学会（2005）、Massry 奖/Horwitz 奖/E.B. Wilson 奖章（多与 Varshavsky 共享）；Oramed 制药科学顾问；NYU Grossman 杰出兼职教授。

## 3. 配色方案（高斯/Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（绛紫 plum） | `#52307C` | 历经劫难后的沉静与深挚（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（泛素标签 badgeUb） | `#2E5A9E` | 蓝泛素缀合 / 多聚标签 |
| 分类色 2（蛋白酶体 badgeProt） | `#1B7A43` | 绿降解执行 / 细胞稳态 |
| 分类色 3（细胞周期 badgeCyc） | `#D97B29` | 琥珀 cyclosome / 周期蛋白销毁 |
| 分类色 4（生命历程 badgeLife） | `#C0395B` | 玫瑰匈牙利→以色列 / 战争与新生 |
| 背景 | `#F7F6F9` | 浅灰白（与高斯一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「多条泛素链挂上底物」的缀合图景。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Savage** — Alex-Productions（`music_audio/alex-productions/34-pILVwyuW3jw-Savage.wav`，不要复制 wav 文件，Makefile 里直接引用该路径）
- **风格**：深沉 / 有力量感 / 命运叙事
- **匹配理由**：
  - "命运感" 匹配其早年——隔都、劳役营、父亲四年杳无音讯，一部幸存者的史诗
  - "力量感" 匹配蛋白酶体——细胞内最有力的粉碎机器，被他第一个命名其规则
  - 从劫难到诺贝尔奖的跨度，需要一支能把沉重托举起来的曲子
- **时长**：以实际 wav 为准，> 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 给蛋白质贴上死刑标签的人 / Avram Hershko 1937– + 四色 badge + 右上头像 + 国籍行（匈牙利/以色列）
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名 Herskó Ferenc/国籍/出生地/教育/博士后/任职/领域/荣誉）
03  赫什科的一生 — Sanger 式时间线（10 节点：1937→1944→1950→1965→1969→1970s→1980→1995→2001→2004）
04  战争中的童年 (1937–1950) — 表格「时间|事件|结果」（隔都/劳役营/父亲归来；克制陈述）
05  耶路撒冷与医学 (1950–1969) — 表格「时间|事件|结果」（MD 1965 / PhD 1969）
06  追问：细胞如何拆蛋白？(1970s) — 表格「问题|体系|结果」+ 公式框：网织红细胞无细胞体系
07  1980 PNAS 奠基 — 表格「问题|方法|结果」+ 公式框：ATP 依赖的多重复缀合（五作者含 Rose 注记）
08  泛素-蛋白酶体系统 — 表格「组分|功能|意义」
09  从缀合到 cyclosome (1983–1995) — 表格「阶段|发现|结果」+ 公式框：cyclosome 销毁周期蛋白
10  2004 诺贝尔化学奖 — 金框页（与 Ciechanover、Rose 三人共享；发现泛素介导的蛋白质降解）+ 「挚友癌症获治」一句
11  奖项链 (1987–2003) — 高斯式「类别|代表|意义」表格（Weizmann/以色列奖/Gairdner/Lasker/Wolf 2001 原句）
12  共同获奖者网络 — 表格「人物|共享奖项|年份」（Varshavsky 多奖 / Ciechanover / Leo Sachs 2002 EMET）
13  传承与暮年 — 表格（NYU 兼职 / Oramed 顾问 / 以色列科学院 2000 / APS 2005）
14  结尾 — 「被战争拆散的，与被细胞拆解的，他都懂。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2004 奖项口径 | **三人共享**：Hershko、Aaron Ciechanover、Irwin Rose——发现泛素介导的蛋白质降解；与 Ciechanover 互指一致、Rose 用规范名 "Irwin Rose"（对方在 chem21-batch-03，防分裂） |
| 官方 citation | **本地页面未载官方 citation 英文全句**——可用的页面表述为 "for the discovery of ubiquitin-mediated protein degradation"（Hershko 页 §Biography 口径）；勿编造官方单人全句 |
| 博士导师 | 页面只载 MD 1965 / PhD 1969（希伯来大学–Hadassah），**未载博士导师姓名**——勿建 advisor-student；UCSF 博士后导师页面无姓名（勿杜撰） |
| 战争叙述 | 隔都 Szolnok、避开 Auschwitz 转往奥地利劳役营、父亲苏军战俘四年——严格按页面；**勿加页面无载的细节**（如具体营名、亲戚遇害人数）；语气克制 |
| Rose 参与署名 | 1980 PNAS 五作者含 Irwin Rose——三人合作有实证；但**勿写 Rose「发明/主导」**，页面未载分工 |
| Varshavsky 关系 | 与 Alexander Varshavsky 共享 Gairdner 1999 / Lasker 2000 / Sloan 2000 / Horwitz 2001 / Massry 2001 / Wolf 2001 / E.B. Wilson 2002——**非诺奖 co-honored**，note 须注明是哪些奖项；页面未载二人合作论文——勿写「合作者」 |
| Wolf 奖引语 | 2001 Wolf Prize 理由 "the discovery of the ubiquitin system of intracellular protein degradation and the crucial functions of this system in cellular regulation."（页面明载可引） |
| 同名区分 | 与 Raz Hershko（1998 年生，以色列柔道欧锦赛冠军/奥运选手）**同姓无关**（页面 See also 暗示勿混淆）——不建关系、正文勿提 |
| 疾病关联 | 癌症等疾病关联是 "**believed to be involved**"——勿写定论；「治愈挚友癌症」仅一句客观（页面明载） |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q232302 | ✅ |
| name_zh | 阿夫拉姆·赫什科 | ✅ |
| name_en | Avram Hershko | ✅ |
| birth_date | 1937-12-31 | ✅ |
| death_date | （在世，留空） | ✅ |
| nationality | Hungary（rank 0，1937–1950）/ Israel（rank 1，1950–） | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry（person_field 细分：ubiquitin-mediated protein degradation / biochemistry / cell cycle regulation，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后由主控置 1） | ✅ |

## 7. 社会关系入库清单

**合作者 / 共同得主 / 配偶 / 家人**（仅 page.md 正文或 infobox 明载者；metadata.json 无关系字段，无 metadata-only 禁入库项）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Aaron Ciechanover | 无向 | Technion 长期合作者；1980/1983/1984 等共同论文 |
| co-honored | Aaron Ciechanover | 无向 | 2004 诺贝尔化学奖共同得主；2000 Lasker、2002 EMET 亦共享 |
| co-honored | Irwin Rose | 无向 | 2004 诺贝尔化学奖共同得主；1980 PNAS 共同作者（规范名 Irwin Rose，对方在 chem21-batch-03） |
| co-honored | Alexander Varshavsky | 无向 | 多项奖项共同得主（1999 Gairdner、2000 Lasker、2000 Sloan、2001 Horwitz/Massry/Wolf、2002 E.B. Wilson）——非诺奖 |
| co-honored | Leo Sachs | 无向 | 2002 EMET 生命科学奖共同得主（与 Ciechanover 三人） |
| spouse | Judith Leibowitz | 无向 | 妻，1963 年结婚 |
| parent-child | Moshe Hershko | 父→子 | 父，教师；二战劳役/战俘四年归家 |
| parent-child | Shoshana Wulc | 母→子 | 母，教师；页面作 Shoshana/Margit 'Manci'（娘家姓 Wulc） |
| sibling | Chaim Hershko | 兄→弟 | 兄，匈牙利名 Laszlo 'Laci'；隔都/劳役营共同幸存 |

> **不建项说明**：博士导师与 UCSF 博士后导师页面均无姓名；论文合著者 H. Heller / E. Leshinsky / D. Ganoth / E. Eytan / Y. Reiss / A.L. Haas 等为一次性合著不入库；Raz Hershko（柔道运动员）同姓无关勿建。

## 8. 奖项清单

- Nobel Prize in Chemistry（2004，与 Ciechanover、Rose 三人共享；口径见 §5）
- Weizmann Prize for Sciences（1987）
- Israel Prize in Biochemistry（1994）
- Canada Gairdner International Award（1999，与 Varshavsky）
- Alfred P. Sloan Jr. Prize（2000，与 Varshavsky）
- Albert Lasker Award for Basic Medical Research（2000，与 Ciechanover、Varshavsky）
- Israel Academy of Sciences and Humanities 院士（2000）
- Louisa Gross Horwitz Prize（2001，与 Varshavsky）
- Massry Prize（2001，与 Varshavsky）
- Wolf Prize in Medicine（2001，与 Varshavsky；理由原句见 §5）
- EMET Prize, Life Sciences（2002，与 Ciechanover、Leo Sachs）
- E.B. Wilson Medal（2002，与 Varshavsky）
- Foreign Associate，美国 National Academy of Sciences（2003）
- American Philosophical Society 院士（2005）
- Schleiden Medal；EMBO Membership（infobox 另载）

## 9. 机构清单

- 教育：Hebrew University of Jerusalem–Hadassah Medical Center（MD 1965、PhD 1969）
- 博士后：University of California, San Francisco
- 任职：Technion, Haifa——Rappaport Faculty of Medicine 杰出教授（现任）；New York University Grossman School of Medicine 杰出兼职教授
- 产业：Oramed Pharmaceuticals 科学顾问委员会

## 10. 终审清单

- [ ] 生卒 1937-12-31 / 在世留白；出生地 Karcag（时属匈牙利王国）；本名 Herskó Ferenc Ábrahám
- [ ] 国籍双条 Hungary→Israel 带年份口径
- [ ] 2004 三人共享（Ciechanover/Rose）表述准确；无编造官方 citation；1980 PNAS 五作者含 Rose
- [ ] 战争经历严格按页面、语气克制；无杜撰细节
- [ ] Varshavsky 关系 note 注明是哪些奖项（非诺奖）；Raz Hershko 同名区分落实
- [ ] 疾病关联 believed 口径；Wolf 2001 理由原句逐字准确
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Avram_Hershko/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：REST API 查 infobox 原图下载（500px）；404 则装饰圆占位并记录
- [ ] **国籍**：封面顶部明示匈牙利/以色列双条
- [ ] **引语核对**：Wolf 2001 理由原句为唯一整句引语
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 21 世纪批次各篇格式对齐
