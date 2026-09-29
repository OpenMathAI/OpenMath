# John Kendrew（约翰·肯德鲁）立传提示词

> qid=Q232295 · 1917-03-24 – 1997-08-23 · 英国生物化学家与晶体学家 · 20 世纪 · 诺贝尔化学奖（1962，与 Max Perutz 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/John_Kendrew/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像按 `images.txt` / REST API 下载；404 则装饰圆占位并注明）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{atom}\enspace 第一个看清蛋白质原子的人\enspace·\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「晶体衍射点」母题——离散圆点暗示 X 射线衍射图上的衍射斑。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式/结构数据即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：John Cowdery Kendrew（中文惯称：约翰·肯德鲁；头衔缩写 CBE FRS，1974 年获下级勋位爵士 Knight Bachelor）
- **生卒**：1917-03-24 生于英格兰牛津 → 1997-08-23 逝于英格兰剑桥，享年 80
- **国籍**：United Kingdom（英国）
- **身份**：生物化学家、晶体学家、科学管理家（biochemist and crystallographer）
- **家庭**：父 Wilfrid George Kendrew 为牛津大学气候学 reader（讲师级），母 Evelyn May Graham Sandburg 为艺术史学家；1948 年娶 Elizabeth Jarvie（娘家姓 Gorvin），1956 年离异，无存活子女；后与艺术家 Ruth Harris 为伴侣
- **教育轨迹**：
  - Dragon School（牛津预备学校）
  - Clifton College（布里斯托尔，1930–1936）
  - Trinity College, Cambridge（1936 以 Major Scholar 入学，1939 化学毕业）
  - 博士：1949，《X-ray studies of certain crystalline proteins: the crystal structure of foetal and adult sheep haemoglobins and of horse myoglobin》
- **导师**：Max Perutz（1945 年主动投奔 Cavendish 实验室；博士学术顾问）
- **军事经历**：二战初期做反应动力学研究，后入 Air Ministry Research Establishment 研究雷达；1940 起在皇家空军总部做运筹研究；1941-09-17 授 squadron leader，1944-06-08 荣誉 wing commander，1945-06-05 退役
- **研究领域**：晶体学——血红素蛋白（肌红蛋白）X 射线晶体学、蛋白质三维结构

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **学术家庭（1917）**：牛津气候学家与艺术史学家之子——科学与人文双重底色。
2. **战争转向（1939–1945）**：从反应动力学到雷达再到空军运筹研究；战争期间对生化问题兴趣日增，决定研究蛋白质结构。
3. **投奔 Perutz（1945）**：到剑桥 Cavendish 实验室找 Max Perutz；呼吸生理学家 Joseph Barcroft 建议他做成年/胎羊血红蛋白对比晶体学研究。
4. **Peterhouse Fellow 与 MRC 单元（1947）**：当选 Peterhouse Fellow；MRC 在 Lawrence Bragg 领导下设立「生物系统分子结构研究单元」——分子生物学重镇的起点。
5. **从血红蛋白到肌红蛋白**：羊血红蛋白做到当时条件极限后，转向只有其四分之一大小的肌红蛋白；马心原料晶体太小，意识到潜水哺乳动物储氧组织更有前景，一次偶遇从秘鲁搞到一大块鲸肉——鲸肌红蛋白给出大而衍射干净的晶体。
6. **相位问题破局（1953）**：Perutz 发现多同晶置换法（MIR）可解衍射相位问题——比较天然晶体与重金属浸泡晶体的衍射图。
7. **6 Å → 2 Å（1957–1959）**：1957 年得 6 Å（0.6 nm）电子密度图；1959 年建成 2 Å（0.2 nm）分辨率的原子模型——1958 年 Nature 论文《A three-dimensional model of the myoglobin molecule obtained by x-ray analysis》。
8. **1962 诺贝尔化学奖**：与 Max Perutz 共享，表彰他们在 Cavendish 实验室对含血红素蛋白结构的研究——Kendrew 测定储存氧的肌红蛋白；两人用 X 射线晶体学测定了**第一批蛋白质原子结构**。
9. **血红素基团定位（1954–1956）**：肌红蛋白物种特异性（1954）、咪唑复合物与血红素位置（1955）、血红素取向与多肽链方向（1956）系列 Nature 论文。
10. **肌红蛋白序列（1961）**：与 Watson、Strandberg、Dickerson 等发表抹香鲸肌红蛋白氨基酸序列并与血红蛋白序列比对——序列与结构互证。
11. **EMBO 与 JMB（1963）**：欧洲分子生物学组织创始人之一；创办《Journal of Molecular Biology》并多年任主编；1967 当选美国生物化学家学会 Fellow。
12. **EMBL 首任所长（1974）**：成功劝说各国政府在海德堡建立欧洲分子生物学实验室（EMBL）并出任首任所长；同年受封爵士；1974–1979 大英博物馆 Trustee，1974–1988 历任国际科学理事会（ICSU）秘书长、副主席、主席。
13. **晚年与身后（1981–2010）**：1981–1987 任牛津 St John's College 院长；遗嘱将遗赠用于发展中国家学生科学/音乐奖学金；2010-10-16 该院 Kendrew Quadrangle 正式启用；2020 年 Paul M. Wassarman 传记《A Place in History》出版。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深紫 deepviolet） | `#372A75` | 蛋白质晶体学的深邃与精密（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（肌红蛋白 badgeMyo） | `#4A3A9E` | 蓝紫鲸肌红蛋白 2 Å 原子模型 |
| 分类色 2（X 射线晶体学 badgeXray） | `#1B6B8F` | 青 MIR 相位 / 衍射图 |
| 分类色 3（血红素蛋白 badgeHeme） | `#B0432A` | 砖红血红素基团 / 羊血红蛋白 |
| 分类色 4（科学组织 badgeOrg） | `#2E6B4F` | 绿 EMBO / EMBL / ICSU |
| 背景 | `#F7F6F9` | 浅灰白（与高斯一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应 X 射线衍射图上的离散衍射斑。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Nostalgia** — Alex-Productions（`music_audio/alex-productions/86-5ETNuoDcBg4-Nostalgia.wav`，不要复制 wav 文件，Makefile 直接引用该路径）
- **风格**：怀旧 / 沉静 / 纪录片
- **匹配理由**：
  - "怀旧" 匹配其事业底色——从战时雷达到鲸肉晶体，一段旧日实验室的slow science
  - "沉静" 匹配晶体学工作的性质——数年只为一幅 2 Å 电子密度图
  - "纪录片" 匹配传记叙事——牛津 → 剑桥 → 肌红蛋白 → EMBL
- **时长**：对齐 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 第一个看清蛋白质原子的人 / John Kendrew 1917–1997 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  肯德鲁的一生 — 高斯式时间线（10 节点：1917→1936→1939→1945→1947→1953→1959→1962→1974→1997）
04  早年：牛津与战争 (1917–1945) — 表格「时间|事件|结果」
05  Cavendish：投奔 Perutz (1945–1947) — 表格「时间|事件|结果」
06  肌红蛋白攻坚 (1953–1959) — 表格「问题|方法|结果」+ 公式框：6 Å(1957) → 2 Å(1959) 原子模型
07  1962 诺贝尔化学奖（与 Perutz 共享） — 表格「人物|对象|结果」+ 公式框：第一批蛋白质原子结构
08  血红素与序列 (1954–1961) — 表格「对象|方法|结果」
09  科学组织家 (1963–1988) — 表格「组织|角色|结果」（EMBO/JMB/EMBL/ICSU）
10  师承与传承 — 表格「人物|方向|结果」（Perutz/导师；Huxley/Stryer/学生；Watson/博士后）
11  荣誉与纪念 — 高斯式「类别|代表|意义」表格（Royal Medal 1965、爵士 1974、Kendrew Quadrangle 2010）
12  EMBL 与欧洲科学 — 高斯式流程图（1974 劝建 → 海德堡 → 首任所长 → 欧洲结构生物学网络）
13  遗产：看清蛋白质的世界 — 四分类遗产盒 + 公式框：肌红蛋白 153 残基的结构启示
14  结尾 — 「在原子尺度上，生命第一次显形。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 诺奖官方获奖理由 | **page.md 无官方英文 citation 原文**（"for their studies of the structures of globular proteins" 页面无载，禁写）；可用正文口径：`for determining the first atomic structures of proteins using X-ray crystallography`（正文原句）与 intro 句（Cavendish 实验室含血红素蛋白结构研究） |
| 共享方向 | 1962 与 **Max Perutz 共享**（同门师生同奖——Perutz 既是导师又是共同得主，两行关系并存）；Perutz 解血红蛋白、Kendrew 解肌红蛋白，勿混 |
| "第一个"口径 | 正文明载 "determining the first atomic structures of proteins"（第一批蛋白质原子结构）——可写；勿扩大成"第一个看到生物分子" |
| 鲸肉来源 | "a chance encounter led to his acquiring a large chunk of whale meat from Peru"（偶遇+秘鲁），勿写成系统考察采购 |
| 相位问题归属 | MIR 多同晶置换法是 **Perutz 1953** 发现——勿写成 Kendrew 的功绩 |
| 军衔细节 | 1941 squadron leader（实授）、1944 honorary wing commander（荣誉）、1945-06-05 退役——勿写成"空军司令" |
| 博士年份 | 战后 **1949** 获 PhD（论文含羊血红蛋白与马肌红蛋白）——勿写 1945 |
| 博士生口径 | infobox Doctoral students = **Hugh Huxley、Lubert Stryer** 两人；James D. Watson 是 other notable students（**postdoc**）——Watson 不入师承关系 |
| 婚姻 | Elizabeth Jarvie 1948–1956 **离异**、无存活子女；Ruth Harris 是伴侣非配偶——勿写"白头偕老" |
| 机构混淆 | EMBO（1963 共同创建，组织）≠ EMBL（1974 劝建实验室并任所长）≠ JMB（他创办的期刊）；St John's College 是**牛津**的（1981–87 院长），勿与剑桥 St John's（他本科学院是剑桥 Trinity）混淆 |
| Royal Medal | 1965 年（infobox Awards 明载）——勿写 1962 |
| metadata 噪声 | metadata.json doctoral_student 仅 Hugh Huxley 一人；Lubert Stryer 以 **page.md infobox** 为准入库 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q232295 | ✅ |
| name_zh | 约翰·肯德鲁 | ✅ |
| name_en | John Kendrew（库内既有记录 #2067 的精确形式） | ✅ |
| birth_date | 1917-03-24 | ✅ |
| death_date | 1997-08-23 | ✅ |
| nationality | United Kingdom | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | crystallography（person_field 细分：X-ray crystallography / protein crystallography / structural biology / myoglobin，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 学生 / 共同得主 / 同事**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Max Perutz | 师→生（博士导师） | 1945 投奔 Cavendish，1949 获 PhD |
| co-honored | Max Perutz | 无向 | 1962 诺贝尔化学奖共同得主 |
| advisor-student | Hugh Huxley | 肯德鲁→学生 | infobox 博士生，肌肉收缩蛋白晶体学 |
| advisor-student | Lubert Stryer | 肯德鲁→学生 | infobox 博士生 |
| colleague | James D. Watson | 无向 | infobox other notable students（博士后） |
| colleague | William Lawrence Bragg | 无向 | 1947 起 MRC 生物系统分子结构研究单元主任（入库用库内规范全名 #2060） |
| other | Joseph Barcroft | 无向 | 呼吸生理学家，建议其做成年/胎羊血红蛋白对比晶体学研究 |
| spouse | Elizabeth Jarvie | 无向 | 1948 结婚，1956 离异（娘家姓 Gorvin） |

> **禁入库名单**（metadata-only 或非个人实质关系）：Ruth Harris（晚年伴侣，白名单无对应类型）、Paul M. Wassarman（传记作者）、Elizabeth Jarvie 之外的家属均无载。metadata.json 的 doctoral_student 仅 Hugh Huxley，Stryer/Watson 以 page.md infobox 为准入库。

## 8. 奖项清单

- Nobel Prize in Chemistry（1962，与 Max Perutz 共享）
- Commander of the Order of the British Empire，CBE
- Fellow of the Royal Society，FRS
- Royal Medal（1965）
- Knight Bachelor（1974）
- William Procter Prize for Scientific Achievement
- EMBO Membership；Honorary member of the British Biophysical Society
- Honorary doctor of the University of Madrid Complutense
- Fellow of the American Society of Biological Chemists（1967）

## 9. 机构清单

- 教育：Dragon School（牛津）、Clifton College（1930–1936）、Trinity College, Cambridge（1936 入学，1939 化学毕业）、PhD 1949（Cambridge）
- 任职：Cavendish Laboratory（1945–）；Peterhouse Fellow（1947–）；MRC 生物系统分子结构研究单元（1947–，Bragg 领导）；Davy-Faraday Laboratory, Royal Institution Reader（1954–）；MRC Laboratory of Molecular Biology；EMBL 首任所长（1974–）；St John's College, Oxford 院长（1981–1987）
- 其他：RAF（1941–1945）；大英博物馆 Trustee（1974–1979）；ICSU 秘书长/副主席/主席（1974–1988）；《Journal of Molecular Biology》创始主编

## 10. 终审清单

- [x] 生卒 1917-03-24 / 1997-08-23，享年 80，出生地牛津、去世地剑桥
- [x] 1962 与 Perutz 共享（同门师生同奖，双关系并存）；官方 citation 原文页面无载已标注
- [x] MIR 归 Perutz（1953）；6 Å 图 1957、2 Å 原子模型 1959、Nature 论文 1958
- [x] PhD 1949；军衔 squadron leader（1941 实授）/ honorary wing commander（1944 荣誉）
- [x] EMBO（1963）/ JMB（创办）/ EMBL（1974 首任所长）三组织不混；St John's 是牛津
- [x] 博士生 Huxley/Stryer 入库、Watson 以博士后同事入库
- [x] 婚姻 1948–1956 离异、无存活子女；Ruth Harris 不入库
- [x] 引语全部可在本地 Wikipedia 原文找到（正文口径获奖理由句、"a chance encounter... whale meat from Peru"）
- [x] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 衍射斑气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/John_Kendrew/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：按 `images.txt` 下载并核验（KendrewMyoglobin.jpg 是工作照可作插图；肖像 404 则装饰圆占位）
- [ ] **国籍**：封面顶部明示英国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（获奖理由正文口径句、鲸肉偶遇句）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与高斯模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 骨架）对齐

---

> **名单状态**：由主控统一更新 `chemist/generate_20th_century_list.py`，本文件不改总表。
