# Martin Karplus（马丁·卡普拉斯）立传提示词

> qid=Q903471 · 1930-03-15 生于维也纳 – 2024-12-28 逝于马萨诸塞州剑桥（享年 94）· 奥地利/美国理论化学家 · 诺贝尔化学奖（2013，与 Michael Levitt、Arieh Warshel 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Martin_Karplus/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 表格语义化 tabularx + 金色公式框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像从本地 `images.txt` 列表下载，如 2013 斯德哥尔摩发布会照；下载失败用装饰圆占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{atom}\enspace 跨尺度的模拟者\enspace·\enspace 奥地利/美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士导师、研究领域、任职、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「多尺度」母题——大圆为量子世界、中圆为分子动力学、小圆为宏观体系，圆点跨尺度嵌套。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），Karplus 方程 J(φ) 即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Martin Karplus（德语发音 [ˈmaʁtiːn ˈkaʁplʊs]；中文惯称：马丁·卡普拉斯）
- **生卒**：1930-03-15 生于维也纳（当时为奥地利第一共和国）→ 2024-12-28 逝于马萨诸塞州剑桥家中，享年 94
- **国籍**：Austria / United States（infobox Citizenship：American, Austrian；yaml 双国籍分 rank）
- **身份**：理论化学家——哈佛大学 Theodore William Richards 化学教授；法国 CNRS 与斯特拉斯堡大学共建的生物物理化学实验室主任
- **家庭**：维也纳 "intellectual and successful secular Jewish family"；1938 年 3 月 Anschluss（德奥合并）数日后举家逃离纳粹占领——先在苏黎世与法国 La Baule 辗转数月，后移民美国；祖父 Johann Paul Karplus（1866–1936）为维也纳大学精神病学教授；伯外祖母 Eugenie Goldstern 为民族学家、殁于大屠杀；弟 Robert Karplus 为国际知名物理学家与科学教育家（UC Berkeley）；侄 Andrew Karplus 为俄勒冈州立大学生物化学与生物物理教授；婚姻姻亲叔父为社会学家/哲学家 Theodor W. Adorno、物理学家 Robert von Lieben 之伯侄孙；娶 Marci，育三子女（未具名）
- **教育轨迹**：
  - Harvard College：化学与物理 BA（1951）
  - California Institute of Technology：PhD（1953，导师 Linus Pauling）；论文《A quantum-mechanical discussion of the bifluoride ion》（infobox 系于 1954）
  - University of Oxford：NSF 博士后（1953–1955，与 Charles Coulson 合作）
- **研究领域**：理论化学——化学动力学、量子化学、生物大分子分子动力学模拟、核磁共振（NMR）自旋-自旋耦合理论
- **学术家族树**：1955 年以来指导逾 200 名研究生与博士后

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **逃离维也纳（1938）**：Anschluss 数日后全家出逃，经苏黎世、法国 La Baule 辗转赴美——犹太知识分子家庭的流亡底色。
2. **17 岁发表第一篇论文**：尚在中学/本科阶段即有学术首秀（页面明载 "published his first academic paper when he was 17 years old"）。
3. **哈佛本科（1951）**：Harvard College 化学与物理双料 BA。
4. **Caltech 与 Pauling（1951–1953）**：师从诺奖得主 Linus Pauling 攻读博士；据 Pauling 本人说，Karplus "was [his] most brilliant student"（其最出色的学生）。
5. **牛津博士后（1953–1955）**：NSF fellow，与量子化学家 Charles Coulson 合作。
6. **执教三级跳（1955–1966）**：UIUC（1955–1960）→ 哥伦比亚大学（1960–1965）→ 哈佛化学系（1966–），此后哈佛任教近六十年。
7. **Karplus 方程**：质子 NMR 中耦合常数 J 与二面角的关联式（J-coupling），以他的名字命名——NMR 解析蛋白质结构的理论基石之一；他在 NMR 与电子自旋共振领域影响深远。
8. **MRC LMB 访问（1969–1970）**：访问剑桥 MRC 分子生物学实验室结构研究部——与结构生物学前沿接轨。
9. **1970 年 Warshel 来访**：博士后 Arieh Warshel 加入哈佛组；两人写出用经典物理模拟原子核与部分电子、用量子力学处理其余电子的计算机程序——QM/MM 思想雏形。
10. **1974 视网膜醛论文**：Karplus、Warshel 及合作者发表基于此类建模的论文，成功模拟视觉关键分子视网膜醛（retinal）的形状变化。
11. **CHARMM**：其小组发起并协调开发 CHARMM 分子动力学程序——生物大分子模拟的支柱软件。
12. **2013 诺贝尔化学奖**：与 Michael Levitt、Arieh Warshel 共享，官方理由 "the development of multiscale models for complex chemical systems"——三人中他是唯一的物理化学/理论化学出身（多尺度模型主线），与 Levitt（结构生物学/大分子模拟）、Warshel（QM/MM 量化路线）分工不同，勿混。
13. **晚年与身后**：1996 年起在法国 Louis Pasteur 大学（斯特拉斯堡）建组；2020 出版自传《Spinach on the Ceiling: The Multifaceted Life of a Theoretical Chemist》；2024-12-28 于剑桥家中逝世，享年 94；另痴迷摄影（个人摄影网站见页面外链）。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深海蓝 deepteal） | `#0F4C5C` | 理论化学的深潭与哈佛深红的冷静衬底（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（多尺度模型 badgeMulti） | `#2E5A9E` | 蓝 QM/MM / 多尺度模型 |
| 分类色 2（NMR 理论 badgeNMR） | `#1B7A43` | 绿 Karplus 方程 / J-coupling |
| 分类色 3（分子动力学 badgeMD） | `#D97B29` | 琥珀 CHARMM / 大分子模拟 |
| 分类色 4（流亡与家族 badgeFamily） | `#7A4A2B` | 赭石维也纳流亡 / 学术家族 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落）——多尺度嵌套：大圆包小圆，量子—分子—宏观三个尺度在同一画面中共存。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**PAST** — Alex-Productions（文件 `89-geyy8_WXDK0-PAST.wav`，**勿复制 wav 文件**）
- **风格**：回望 / 追忆 / 带暖意的怀旧
- **匹配理由**：
  - "PAST（往昔）" 对应其人生弧线——1938 年逃离维也纳的童年、1950 年代的量子学徒岁月，直到 2024 年谢幕
  - "追忆" 匹配理论家的思维方式——用数学回望分子过去的运动轨迹，与自传《Spinach on the Ceiling》的回望基调同构
  - "暖意" 匹配其学术家族——200 余名门生、CHARMM 社群与斯特拉斯堡双栖生涯
- **时长核对**：以 ffmpeg `-shortest` 自动对齐 15 页 × 7 秒 ≈ 105 秒的幻灯时长

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 跨尺度的模拟者 / Martin Karplus 1930–2024 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士导师/领域/任职/荣誉）
03  卡普拉斯的一生 — Sanger 式时间线（10 节点：1930→1938→1951→1953→1955→1966→1970→1974→2013→2024）
04  维也纳与流亡 (1930–1938) — 表格「时间|事件|结果」（Anschluss 出逃、学术家族）
05  从哈佛到 Caltech (1951–1955) — 表格「阶段|导师|产出」+ Pauling "most brilliant student"
06  执教岁月：UIUC→Columbia→Harvard (1955–1966) — 表格「机构|年份|方向」
07  Karplus 方程与 NMR 理论 — 表格「问题|理论|影响」+ 公式框：J 与二面角的 Karplus 方程
08  1970 转折：与 Warshel 的经典-量子程序 — 表格「问题|方法|结果」+ 公式框：QM/MM 思想示意
09  视网膜醛与 CHARMM (1974–) — 表格「对象|技术|结果」+ 公式框：多尺度模型层级
10  2013 诺贝尔化学奖 — 表格「奖项|年份|理由」+ 公式框：for multiscale models（三人共享，Karplus 分工线）
11  师门与传承 — 表格「人物|方向|结果」（Brooks/Brunger/McCammon/Schulten 等，200 余名门生）
12  哈佛与斯特拉斯堡双城记 — 机构流程图（Caltech → Oxford → UIUC → Columbia → Harvard → Strasbourg）
13  遗产：从 H+H2 到生物分子 — 四分类遗产盒 + 公式框：诺奖演讲主题 "From H+H2 to Biomolecules"
14  结尾 — 「用经典与量子两支笔，写尽分子的过去与未来。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2013 获奖口径 | 与 Michael Levitt、Arieh Warshel **三人共享**；官方理由 "the development of multiscale models for complex chemical systems"（页面明载）——勿写独享、勿漏 Warshel |
| 三人分工 | Karplus 是三人中唯一的**物理化学/理论化学**出身（多尺度模型主线）；Levitt 偏结构生物学大分子模拟、Warshel 偏 QM/MM 量化路线——分工勿混，奖项归属勿交叉错写 |
| 博士年份 | 正文 "completed his PhD in 1953"；infobox 论文条目系于 1954——《A quantum-mechanical discussion of the bifluoride ion》——正文写 1953，论文年份如引用须加注 |
| 博士导师 | Linus Pauling（Caltech）——正文与 infobox 一致；"most brilliant student" 是 **Pauling 的评价**（据页面转述），引用时注明出处属性 |
| 流亡叙事 | 1938 年 3 月 Anschluss 数日后逃离、经苏黎世与 La Baule 辗转赴美——页面明载可写；纳粹/大屠杀背景（Eugenie Goldstern 之死）客观一笔即可，勿渲染 |
| 家庭成员 | 弟 Robert Karplus（sibling，可入库）；祖父/伯外祖母/姻亲叔父 Adorno/侄 Andrew 均为家族叙事——**不入库**（见 §7） |
| 门生名单 | "Notable students and postdocs" 段共 14 人（含 Warshel）——入库以该段为准，勿从其他来源扩充；"supervised more than 200" 是总数口径 |
| Charles Coulson | 牛津 NSF 博士后合作（1953–1955）——页面用词 "worked with"，记 colleague 勿记博士导师 |
| Warshel 双重身份 | Warshel 既是 1970 年加入哈佛组的博士后（advisor-student），又是 2013 共同得主（co-honored）——两条关系并存 |
| 在世/卒日 | 2024-12-28 逝于马萨诸塞州剑桥家中、享年 94——勿写其他日期；封面 "1930–2024" |
| 中文译名 | 惯称「马丁·卡普拉斯」，勿用「卡尔普拉斯」等其他形式 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q903471 | ✅ |
| name_zh | 马丁·卡普拉斯 | ✅ |
| name_en | Martin Karplus（库内既有记录 #3851 精确复用） | ✅ |
| birth_date | 1930-03-15 | ✅ |
| death_date | 2024-12-28 | ✅ |
| nationality | Austria（rank 0）+ United States（rank 1） | ✅ |
| primary_occupation | theoretical chemist | ✅ |
| field_of_work | theoretical chemistry（person_field 细分：theoretical chemistry / NMR spectroscopy / molecular dynamics / quantum chemistry，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 同事 / 家人 / 门生 / 共同得主**（★红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Linus Pauling | 师→生 | Caltech 博士导师，1953 年获 PhD；Pauling 称其 "most brilliant student" |
| colleague | Charles Coulson | 无向 | 牛津 NSF 博士后合作（1953–1955） |
| colleague | Arieh Warshel | 无向 | 长期合作者，1974 视网膜醛论文共同作者 |
| advisor-student | Arieh Warshel | 师→生 | 1970 年加入哈佛组的博士后，共同写出经典-量子程序 |
| co-honored | Arieh Warshel | 无向 | 2013 诺贝尔化学奖共同得主 |
| co-honored | Michael Levitt | 无向 | 2013 诺贝尔化学奖共同得主 |
| spouse | Marci | 无向 | 妻子，育三子女 |
| sibling | Robert Karplus | 无向（from<to） | 弟弟，UC Berkeley 物理学家与科学教育家 |
| advisor-student | Bernard R. Brooks | 师→生 | Notable students and postdocs（NIH） |
| advisor-student | Charles L. Brooks III | 师→生 | Notable students and postdocs（密歇根大学） |
| advisor-student | Axel T. Brunger | 师→生 | Notable students and postdocs（斯坦福） |
| advisor-student | J. Andrew McCammon | 师→生 | Notable students and postdocs（UCSD；与 Karplus 及 Gelin 发表首个 BPTI 分子动力学模拟） |
| advisor-student | P. T. Narasimhan | 师→生 | Notable students and postdocs（UIUC；Shanti Swarup Bhatnagar 奖得主） |
| advisor-student | B. Montgomery Pettitt | 师→生 | Notable students and postdocs（UTMB / Baylor） |
| advisor-student | Benoît Roux | 师→生 | Notable students and postdocs（芝加哥大学） |
| advisor-student | Andrej Šali | 师→生 | Notable students and postdocs（UCSF） |
| advisor-student | Klaus Schulten | 师→生 | Notable students and postdocs（UIUC） |
| advisor-student | Jeremy C. Smith | 师→生 | Notable students and postdocs（橡树岭国家实验室） |
| advisor-student | David J. States | 师→生 | Notable students and postdocs（UTHealth Houston） |
| advisor-student | Eugene Shakhnovich | 师→生 | Notable students and postdocs（哈佛） |
| advisor-student | Alexander D. MacKerell Jr. | 师→生 | Notable students and postdocs（马里兰大学） |
| advisor-student | John Kuriyan | 师→生 | Notable students and postdocs（范德堡大学） |

> **禁入库名单**（家族叙事或非本人直接关系）：祖父 Johann Paul Karplus、伯外祖母 Eugenie Goldstern、姻亲叔父 Theodor W. Adorno、伯侄孙 Robert von Lieben、侄 Andrew Karplus、Jean-François Lefèvre（斯特拉斯堡 NMR 实验室东家，仅 sabbatical 提及）、三名子女（未具名）。

## 8. 奖项清单

- Nobel Prize in Chemistry（2013，与 Michael Levitt、Arieh Warshel 共享）
- National Academy of Sciences 院士（1967）
- Irving Langmuir Award（1987）
- ACS Award in Theoretical Chemistry（1993）
- Royal Netherlands Academy of Arts and Sciences 外籍会员（1991）
- Foreign Member of the Royal Society，ForMemRS（2000）
- Christian B. Anfinsen Award（2001）
- Linus Pauling Award（2004）
- International Academy of Quantum Molecular Science 会员
- Guggenheim Fellowship；Commander of the Legion of Honour（法国荣誉军团军官级勋章）；Austrian Decoration for Science and Art；维也纳大学荣誉博士与维也纳荣誉市民；ACS Award for Computers in Chemical and Pharmaceutical Research（frontmatter 载）

## 9. 机构清单

- 教育：Harvard College（BA 1951，化学+物理）；California Institute of Technology（PhD 1953，Pauling 指导）；University of Oxford（NSF 博士后 1953–1955，Coulson）
- 任职：University of Illinois Urbana-Champaign（1955–1960）；Columbia University（1960–1965）；Harvard University 化学系（1966–，Theodore William Richards 教授）；Louis Pasteur University 教授（1996，斯特拉斯堡建组；1992–1995 两度 sabbatical）；CNRS–斯特拉斯堡大学生物物理化学实验室主任
- 访问：MRC Laboratory of Molecular Biology 结构研究部（1969–1970）
- 出版：自传《Spinach on the Ceiling》（2020）；教材《Atoms and Molecules》（1970，与 Porter）

## 10. 终审清单

- [ ] 生卒 1930-03-15 / 2024-12-28（剑桥家中，享年 94）表述准确
- [ ] 2013 **三人共享**（Karplus/Levitt/Warshel），官方理由 "the development of multiscale models for complex chemical systems" 表述准确
- [ ] 三人分工（Karplus=理论化学/多尺度主线）表述准确，勿交叉错写
- [ ] 博士 1953（正文）与论文条目 1954（infobox）年份张力已加注
- [ ] Karplus 方程、QM/MM 程序（1970 Warshel）、视网膜醛（1974）、CHARMM 四大成果时序准确
- [ ] "most brilliant student" 归属 Pauling 的评价；门生 14 人与页面名单一一对应
- [ ] 引语核对——"was [his] most brilliant student" 与诺奖理由均有原文出处；无杜撰引语
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Martin_Karplus/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：从 `images.txt` 列表下载（2013 斯德哥尔摩发布会照优先），失败用装饰圆占位
- [ ] **国籍**：封面顶部明示奥地利/美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（诺奖理由、"most brilliant student"），否则改间接转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 黄金骨架）对齐

---

> **名单状态**：`chemist/generate_21th_century_list.py` 由主控统一收尾，本提示词不直接改动总名单。
> **最重要的事：每写一页就 make，看到溢出就修。**
