# James Joseph Sylvester（詹姆斯·约瑟夫·西尔维斯特）立传提示词

> qid=Q310781 · 1814-09-03 – 1897-03-15 · 英国数学家 · 19 世纪
> 本地 Wikipedia 数据源：`mathematician/presentations/19th_century/pages/James_Joseph_Sylvester/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**，而非纯数学家版式。这意味着在数学家立传基础上，增加以下**物理学家格式硬性要求**：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（若 Wikipedia 有头像照片，从 `images.txt` 或 infobox 下载到 `images/`；无则用装饰圆 `\faIcon{user}` 占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，至少含：生卒、本名、国籍、出生地、师承、教育、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：采用「主色 + 强调色 + 三~四分类色」配色；背景用柔和气泡（稀疏大块实心圆）呼应数学结构的「矩阵 / 不变量」母题。
5. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：James Joseph Sylvester（本名 James Joseph，随兄移民美国后改姓 Sylvester，中文惯称：西尔维斯特）
- **生卒**：1814-09-03 生于伦敦 → 1897-03-15 逝于伦敦，享年 82
- **国籍**：United Kingdom of Great Britain and Ireland（英国）
- **身份**：数学家（矩阵理论、不变量理论、组合学、配分理论）
- **家庭**：父 Abraham Joseph（犹太商人）；终身未婚，无子女；热爱诗歌
- **教育轨迹**：
  - 14 岁师从 Augustus De Morgan（伦敦大学）
  - 1831 年入剑桥圣约翰学院（导师 John Hymers）
  - 1837 年剑桥 tripos 考试第二（因犹太身份不能宣誓三十九条信纲，**未获学位**）
  - 1841 年获都柏林三一学院 BA 与 MA
- **导师**：John Hymers、Augustus De Morgan
- **研究领域**：代数、矩阵理论、不变量理论、组合学、数论

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **矩阵理论的奠基者（最著名贡献）**：1850 年**创造"matrix"（矩阵）一词**，是矩阵理论的奠基者之一。
2. **创造数学术语**：创造了 "matrix"（矩阵）、"graph"（图，网络意义）、"discriminant"（判别式）、"totient"（欧拉 φ 函数）等沿用至今的术语。
3. **与 Cayley 的长期合作**：在攻读律师资格时结识 Arthur Cayley，两人长期合作，在不变量理论与矩阵理论做出重大贡献。
4. **Sylvester 惯性定律**：矩阵理论中的基本结果（实对称矩阵正负惯性指数在合同变换下不变）。
5. **Sylvester–Gallai 定理**：离散几何中的经典结果（平面上非共线的有限点集中必存在一条只经过两点的直线）。
6. **配分理论**：整数配分（partition）理论的贡献，Sylvester 序列。
7. **犹太身份受挫（生平叙事）**：因犹太身份多次受阻——剑桥 tripos 第二却未获学位（不能宣誓信纲）；1843 年被哥伦比亚学院拒绝教授职位（又因犹太身份）。
8. **美国数学的奠基者**：1876 年任约翰霍普金斯大学首任数学教授（美国大学第一位犹太教授是 1841 年弗吉尼亚大学），1878 年创办《美国数学杂志》（American Journal of Mathematics），领导了 19 世纪下半叶美国数学。
9. **支持女性数学家**：1878 年力排众议支持 Christine Ladd-Franklin 成为其学生。
10. **荣誉**：Royal Medal（1861）、Copley Medal（1880，英国皇家学会最高奖）、De Morgan Medal（1887）、FRS；1901 年英国皇家学会设立 Sylvester Medal 纪念他。

## 3. 配色方案（参考 Wilson 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（英国深蓝） | `#1F3A93` | 英伦理性 |
| 强调色（数学金） | `#C9A227` | 矩阵 / 尊崇 |
| 分类色 1（矩阵/不变量 — 靛蓝） | `#4C5FD5` | 矩阵 / 惯性定律 |
| 分类色 2（组合/配分 — 青绿） | `#0E7C7B` | Sylvester 序列 / 配分 |
| 分类色 3（术语创造 — 琥珀） | `#E07B30` | matrix / graph / discriminant |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「矩阵 / 不变量」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`
> （本次执行无法直接读取音乐库目录，具体 wav 文件名与本地路径需在执行立传时从 `curated_tracks.md` 选定，以下给出风格定调与候选方向。）

- **风格定调**：**古典庄重 / 诗意坚韧**（犹太身份受挫却成就斐然的坚韧与诗人气质）
- **匹配理由**：
  - 西尔维斯特因犹太身份屡屡受挫，却成为矩阵理论奠基者、美国数学奠基者——需**庄重、坚韧、有诗意**的配乐
  - "诗意" 匹配其热爱诗歌（出版《诗律》The Laws of Verse）
  - "坚韧" 匹配其跨越宗教歧视的奋斗
- **候选方向**（执行时从音乐库核对具体曲目，优先古典/庄重/诗意风格）：
  - 首选：古典 / 庄重 / 诗意风格曲目（呼应诗人气质）
  - 备选：历史感深沉 / 坚韧曲目（呼应宗教歧视下的奋斗）
  - 时长需 ≥ 12 页 × 7 秒 ≈ 84 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（约 12 页，正文采用 Wilson 式结构）

1. **封面**（`\titleslide`）：大标题「矩阵理论的奠基者 · 美国数学的奠基者」+ 西尔维斯特 1814–1897 + 右上头像 + 国籍行 + 底部三要素状态栏 + 分类 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右信息网格（生卒 / 本名 / 国籍 / 出生地 / 师承 / 教育 / 荣誉 / 核心领域）
3. **核心贡献概览**（`\hookslide`）：矩阵与不变量 / 组合与配分 / 术语创造 / 生平 四分类
4. **早年与犹太身份**（1814–1841）：伦敦、De Morgan、剑桥 tripos 第二未获学位、都柏林三一学院
5. **矩阵理论与不变量理论**（核心贡献页）：matrix 一词、惯性定律
6. **与 Cayley 的合作**（核心叙事页）：攻读律师时结识、不变量理论
7. **Sylvester–Gallai 定理与组合学**（核心贡献页）：离散几何、配分理论
8. **创造数学术语**（核心贡献页）：matrix、graph、discriminant、totient
9. **美国数学的奠基**（核心叙事页）：约翰霍普金斯、美国数学杂志、支持 Ladd-Franklin
10. **学术生涯**：弗吉尼亚大学、伍尔维奇皇家军事学院、牛津 Savilian 教授
11. **荣誉与诗意人生**：Royal Medal、Copley Medal、Sylvester Medal、诗律
12. **终章**：82 岁、从矩阵到美国数学的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **矩阵一词**：Sylvester 1850 年创造 "matrix" 一词——是"创造术语"，但矩阵理论是 Sylvester 与 Cayley 共同奠基，勿写 Sylvester 独创建矩阵理论。
- **"graph" 与 "discriminant"**：Sylvester 创造 "graph"（网络意义）与 "discriminant" 术语——是术语创造者，勿写他"发明了图论"（图论概念早已有之）。
- **犹太身份受挫**：剑桥 tripos 第二但因不能宣誓三十九条信纲未获学位（1837）；1843 年因犹太身份被哥伦比亚学院拒绝——是"宗教歧视"，客观表述。
- **美国第一位犹太教授**：1841 年任弗吉尼亚大学教授，是**美国大学第一位犹太教授**——但仅任职 4 个月即因课堂事件离职（学生用棍棒打他，他持剑杖反击，误以为杀死学生）。
- **与 Cayley 合作**：是在攻读律师资格时结识 Cayley（Sylvester 为精算工作需法律学位）——是"学法律时结识"，勿写两人同门。
- **终身未婚**：Sylvester 终身未婚，无子女，无恋爱记录——如实写。
- **诗人身份**：热爱诗歌，出版《诗律》（The Laws of Verse），数学论文常引用古典诗歌——可作叙事点。
- **无肖像**：`images.txt` 仅含 Speaker Icon，无 Sylvester 本人肖像，封面头像需用装饰圆占位。
- **国籍**：United Kingdom of Great Britain and Ireland，今英国——封面用「英国」。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q310781 | 待写入 |
| name_zh | 西尔维斯特（或 詹姆斯·约瑟夫·西尔维斯特） | 待写入 |
| name_en | James Joseph Sylvester | 待写入 |
| birth_date | 1814-09-03 | 待写入 |
| death_date | 1897-03-15 | 待写入 |
| nationality | United Kingdom | 待写入 |
| primary_occupation | mathematician | 待写入 |
| field_of_work | algebra / matrix theory / combinatorics | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20）

- **导师**：John Hymers、Augustus De Morgan
- **合作者**：Arthur Cayley（长期合作，不变量理论、矩阵理论）
- **美国友人**：Benjamin Peirce（哈佛数学家）、Joseph Henry（普林斯顿物理学家）
- **学生**：William Pitt Durfee、George B. Halsted、Washington Irving Stringham、Christine Ladd-Franklin（支持其成为学生）

## 8. 奖项清单

- Royal Medal（皇家奖章，1861）
- Copley Medal（科普利奖章，1880，英国皇家学会最高奖）
- De Morgan Medal（德摩根奖章，1887）
- Fellow of the Royal Society（1839）
- 1901 年英国皇家学会设立 Sylvester Medal 纪念他（身后纪念）

## 9. 机构清单

- 教育：St John's College, Cambridge（剑桥圣约翰学院）、Trinity College, Dublin（都柏林三一学院）、University College London、Liverpool Royal Institution
- 任职：Johns Hopkins University（1876 首任数学教授）、University of London、University of Virginia（1841）、Royal Military Academy, Woolwich（1855–1869）、University of Oxford（1883 Savilian 几何教授）、Equity and Law Life Assurance Society

## 10. 终审清单

- [ ] 生卒 1814-09-03 / 1897-03-15，享年 82，出生地伦敦
- [ ] matrix 一词"1850 创造、与 Cayley 共同奠基矩阵理论"表述准确
- [ ] graph/discriminant"术语创造"表述准确
- [ ] 犹太身份"宗教歧视"客观表述
- [ ] 美国第一位犹太教授"1841 弗吉尼亚、4 个月离职"表述准确
- [ ] 与 Cayley"学法律时结识"表述准确
- [ ] 终身未婚、诗人身份表述准确
- [ ] 头像确认（无肖像则装饰圆占位）
- [ ] 国籍用「英国」现代对应
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/James_Joseph_Sylvester/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：无肖像，用装饰圆占位
- [ ] **国籍**：封面顶部徽章明示英国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪数学家（Kummer / Liouville / Hamilton）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
