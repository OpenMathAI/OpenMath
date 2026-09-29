# David Baker（戴维·贝克）立传提示词

> qid=Q3814528 · 1962-10-06 生于西雅图（在世） · 美国生物化学家与计算生物学家 · 21 世纪 · 诺贝尔化学奖（2024，**独得一半**——计算蛋白质设计；另一半由 Hassabis 与 Jumper 因 AlphaFold 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/David_Baker_biochemist/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**对齐 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。肖像可用 `images.txt` 实照 `David_Baker,_2024_Nobel_Prize_Laureate_in_Chemistry.jpg`（2024 诺贝尔周讲座照，250px 改 500px 下载，`curl -A "Mozilla/5.0"` + `file` 验证）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{dna}\enspace` 蛋白质的建筑师`\enspace·\enspace` 美国），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地、教育（Harvard/Berkeley/UCSF 博士后）、博士导师、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「蛋白质折叠」母题——圆点串成的链即氨基酸序列折叠成结构。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）——核心页呈现「序列 → 结构 → 设计」的蛋白质设计循环与 Top7（首个全新折叠的人工蛋白）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：David Baker（中文惯称：戴维·贝克）
- **生卒**：1962-10-06 生于华盛顿州西雅图（在世，页面无卒日）
- **国籍**：United States（美国）
- **身份**：生物化学家、计算生物学家；华盛顿大学 Henrietta and Aubrey Davis 生物化学讲席教授、HHMI 研究员、蛋白质设计研究所（Institute for Protein Design）所长；2024 诺贝尔化学奖（一半）得主
- **家庭**：犹太家庭出身；父 Marshall Baker（物理学家）、母 Marcia（娘家姓 Bourgin，地球物理学家）；妻 Hannele Ruohola-Baker（同校生物化学家），育有二子女
- **教育轨迹**：
  - Garfield High School（西雅图）
  - Harvard University：生物学 BA（1984）
  - University of California, Berkeley：生物化学 PhD（1989），Randy Schekman 实验室（酵母蛋白运输与 trafficking）
  - 博士后：UCSF，David Agard 组生物物理学（1993 完成）
- **研究领域**：computational biology / 蛋白质设计 / 蛋白质结构预测 / molecular engineering

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **科学家之家（1962）**：西雅图犹太家庭，物理学家之父与地球物理学家之母。
2. **哈佛生物学 BA（1984）**：本科转向生命科学。
3. **Schekman 组的酵母岁月（1984–1989）**：Berkeley 生物化学博士，研究酵母蛋白运输与 trafficking——实验生物化学的底子。
4. **Agard 组博士后（1989–1993）**：UCSF 生物物理学，完成结构视角的训练。
5. **入职华盛顿大学（1993）**：医学院生物化学系任教；2000 成为 HHMI 研究员。
6. **Rosetta 算法**：组里发展 ab initio 蛋白质结构预测的 Rosetta——后扩展为蛋白质设计工具、分布式计算项目 Rosetta@home 与电脑游戏 Foldit。
7. **Rosetta Commons**：任 Rosetta Commons 主任——联合多家实验室的结构预测与设计软件共同体；常年参加 CASP 竞赛（ab initio 组别，手动辅助与自动 Rosetta 双轨）。
8. **Top7（2003 前后，★核心）**：设计出第一个具有全新折叠（novel fold）的人工蛋白质 Top7——"从预测走向设计"的宣言，获 2004 Newcomb Cleveland Prize。
9. **AI 化的 Rosetta**：用人工智能发展 RoseTTAFold——结构预测的新版本（页面明载）。
10. **实验组不丢**：虽以计算闻名，仍保持活跃的实验生物化学团队；发表 600+ 篇论文。
11. **蛋白质设计研究所（IPD）**：任所长；2017 获 Open Philanthropy 超 1100 万美元、2021 追加 300 万美元资助。
12. **创业军团**：共同创办十余家生物技术公司——Prospect Genomics（2001 被 Eli Lilly 子公司收购）、Icosavax（2023 被 AstraZeneca 收购）、Sana Biotechnology、Lyell Immunotherapeutics、Xaira Therapeutics、GenBio AI；2019 TED 演讲 "5 challenges we could solve by designing new proteins"。
13. **2024 诺贝尔化学奖（一半）与 2025**：因计算蛋白质设计独得 2024 化学奖一半，另一半归 Hassabis 与 Jumper（AlphaFold）；2024 入选 Time 首届健康领域百人榜；2025 当选 National Academy of Inventors 会士。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深海蓝 deepoceanblue） | `#2A3468` | 蛋白质折叠海洋的深蓝（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（结构预测 badgePredict） | `#1E6E8C` | 青蓝 Rosetta / CASP |
| 分类色 2（蛋白质设计 badgeDesign） | `#B3462E` | 橙红 Top7 / 全新折叠 |
| 分类色 3（众算与游戏 badgeCrowd） | `#2E7D4F` | 绿 Rosetta@home / Foldit |
| 分类色 4（应用与产业 badgeBio） | `#8C2F5B` | 玫红 IPD / 生物技术公司 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「氨基酸链折叠」——圆点链在空间中盘绕成天然与人工的结构。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Expedition** — Alex-Productions（源文件 `music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav`，执行时软链/复制至本目录，不复制 wav 入库）
- **风格**：远征 / 进取 / 编程节拍感的推进
- **匹配理由**：
  - "远征" 匹配其方法论——从预测（CASP 竞赛常年出征）到设计（Top7 登顶无人区）的远征叙事
  - "推进感" 匹配 Rosetta 的计算节拍——分布式计算把全世界的电脑变成他的折叠引擎
  - 开阔的配器匹配产业版图——十余家公司、600+ 论文的"设计蛋白质的一切挑战"
- **时长**：执行时用 ffprobe 核对 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 蛋白质的建筑师 / David Baker 1962– + 四色 badge + 右上头像 + 国籍行（美国）
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/出生地/教育/博士导师/博士后/领域/荣誉）
03  贝克的一生 — 时间线（10 节点：1962→1984→1989→1993→2000→2003→2017→2019→2024→2025）
04  科学家之子 (1962–1984) — 表格「时间|事件|结果」（西雅图/Garfield HS/哈佛）
05  Schekman 组：酵母蛋白运输 (1984–1989) — 表格「阶段|内容|结果」+ 博士论文 Reconstitution of Intercompartmental Protein Transport in Yeast Extracts
06  博后与入职华盛顿大学 (1989–2000) — 表格「阶段|内容|结果」（Agard/HHMI）
07  Rosetta 与 CASP (1990s–2000s) — 表格「问题|方法|结果」+ Rosetta Commons
08  Top7：第一个全新折叠 (★核心) — 表格「问题|方法|结果」+ 公式框：序列 → 结构 → 设计循环；2004 Newcomb Cleveland Prize
09  众包折叠：Rosetta@home 与 Foldit — 表格「项目|机制|结果」
10  RoseTTAFold 与 AI 时代 — 表格「工具|特点|结果」
11  蛋白质设计研究所与创业 — 表格「机构/公司|事件|结果」（IPD/Open Philanthropy/十余家公司）
12  荣誉清单 — 「类别|代表|意义」表格 + itemize（Overton 2002 / Feynman 2004 / Breakthrough 2021 / BBVA 2022 / Nobel 2024）
13  2024 诺奖：一半的疆界 — 流程图：Baker（设计，一半）‖ Hassabis+Jumper（AlphaFold，一半）；NAS/NAE 双院士
14  结尾 — 「既然读懂了折叠，就开始书写折叠。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2024 诺奖结构 | 贝克**独得一半**（计算蛋白质设计）；另一半由 **Hassabis 与 Jumper** 共享（AlphaFold）——勿写"三人平分"或"与 Hassabis/Jumper 同一理由共享" |
| 获奖理由口径 | 页面 intro 作 "for his work on computational protein design"、奖项节作 "awarded half of the Nobel Prize...for his work on protein design"；官方口径（主控任务单）"for computational protein design"——全篇统一"计算蛋白质设计"，勿写"因 AlphaFold 获奖" |
| 页面口径张力 | intro 的 "shared 2024 Nobel Prize" 指该奖整体在三位得主间分享，不代表贝克与他人共享同一半——表述时以"独得一半"为准 |
| 同名消歧义 | 本目录 David_Baker_(biochemist) 是消歧义页——与英国 basketball/football 等其他 David Baker 无关；库内 Alan Baker/H. F. Baker 等数学家亦无关 |
| 双导师口径 | 博士导师 **Randy Schekman**（Berkeley）；**David Agard** 是 UCSF 博士后导师（infobox Other academic advisors）——勿混为共同博士导师 |
| 博士论文 | Reconstitution of Intercompartmental Protein Transport in Yeast Extracts（1989）——酵母蛋白运输，与蛋白质设计无关，是"转行前传" |
| Top7 表述 | "the first artificial protein with a novel fold"——首个**全新折叠**的人工蛋白；勿写成"第一个人工蛋白" |
| 机构口径 | UW + HHMI 双任职、IPD 所长；NAS 与 NAE **双院士**（页面明载 member of both）——勿漏 |
| 家庭成员 | 妻 Hannele Ruohola-Baker 是 UW 生物化学家（infobox Spouse）；父母职业照实写（Marshall/Marcia）——勿编造更多家族细节 |
| 页面无载禁写 | 页面无诺奖演说引语、无子女姓名、无 Rosetta@home 志愿者数量——一律不写；全文不编引语，TED 演讲标题 "5 challenges we could solve by designing new proteins" 是页面明载题目可用 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q3814528 | ✅ |
| name_zh | 戴维·贝克 | ✅ |
| name_en | David Baker | ✅ |
| birth_date | 1962-10-06 | ✅ |
| death_date | （在世，留空） | ✅ |
| nationality | United States | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | protein design（person_field 细分：protein design / protein structure prediction / computational biology / molecular engineering，带 rank） | ✅ |
| has_biography | false（Beamer 立传完成后再置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 博士后**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Randy Schekman | 师→生（博士导师） | Berkeley 生物化学博士，酵母蛋白运输 |
| advisor-student | David Agard | 师→生（博士后导师） | UCSF 生物物理学博士后（infobox Other academic advisors） |

**门生（Baker → 学生，源自 infobox）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Richard Bonneau | Baker → 学生 | infobox Doctoral students 明载 |
| advisor-student | Brian Kuhlman | Baker → 学生 | infobox Other notable students（post-doc） |
| advisor-student | Tanja Kortemme | Baker → 学生 | infobox Other notable students（post-doc） |
| advisor-student | Jens Meiler | Baker → 学生 | infobox Other notable students（post-doc） |

**家庭 / 共同得主**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Hannele Ruohola-Baker | 无向 | UW 生物化学家，育有二子女 |
| co-honored | Demis Hassabis | 无向 | 2024 诺贝尔化学奖另一半（AlphaFold）共同得主 |
| co-honored | John M. Jumper | 无向 | 2024 诺贝尔化学奖另一半（AlphaFold）共同得主；规范名 John M. Jumper（下一批入库时回填 QID） |

> 注：对手方 Schekman/Agard/Bonneau/Kuhlman/Kortemme/Meiler/Ruohola-Baker 均为库内新建 stub，按本表规范全名建。
> 父母 Marshall Baker / Marcia Baker：正文一句带过（物理学家/地球物理学家），**从严不予入库**（可选：Review 若认为应入库，以 parent-child 补）。

## 8. 奖项清单

- Overton Prize（2002）；Sackler International Prize in Biophysics（2008）
- Newcomb Cleveland Prize（2004）；Feynman Prize in Nanotechnology（2004）
- Breakthrough Prize in Life Sciences（2021）
- Wiley Prize（2022）；BBVA Foundation Frontiers of Knowledge Award（2022，"Biology and Biomedicine"）
- Nobel Prize in Chemistry（2024，独得一半——计算蛋白质设计）
- Beckman Young Investigators Award；Packard Fellowship；TED Audacious Prize（页面 infobox 载）
- NAS 院士；NAE 院士；American Academy of Arts and Sciences Fellow（2009）；AAAS Fellow；NAI Fellow（2025）
- Time 首届健康百人榜（2024）

## 9. 机构清单

- 教育：Garfield High School（西雅图）；Harvard University（BA 1984，生物学）；UC Berkeley（PhD 1989，生物化学，Schekman 组）；UCSF（博士后，Agard 组，1993 完成）
- 任职：University of Washington School of Medicine 生物化学系（1993–，Henrietta and Aubrey Davis Endowed Professor；兼任 genome sciences/bioengineering/chemical engineering/CS/physics adj.）；HHMI 研究员（2000–）；Institute for Protein Design 所长；Rosetta Commons 主任
- 创业：Prospect Genomics / Icosavax / Sana Biotechnology / Lyell Immunotherapeutics / Xaira Therapeutics / GenBio AI 等

## 10. 终审清单

- [ ] 生卒 1962-10-06 西雅图（在世）；犹太家庭/父母职业照实
- [ ] 博士导师 Schekman / 博士后导师 Agard 双轨口径无误
- [ ] Top7 = 首个全新折叠人工蛋白；2004 Newcomb Cleveland Prize
- [ ] 2024 诺奖"独得一半"口径准确；另一半 Hassabis+Jumper（AlphaFold）
- [ ] Rosetta/Rosetta@home/Foldit/RoseTTAFold 四者定位不混
- [ ] 全文无编造引语；TED 演讲标题为页面明载
- [ ] `make distclean && make` 编译通过，0 错误，vbox≤10pt / hbox≤50pt

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/David_Baker_biochemist/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：下载 images.txt 的 2024 诺贝尔周实照；失败则装饰圆占位并注记
- [ ] 国籍：封面明示"美国"
- [ ] 引语核对：全文无直接引语（页面无人物引语）——检查无编造"原话"
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox≤10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐；结尾品牌 OpenMathAI

---

> **名单状态**：`chemist/generate_21th_century_list.py` 更新由主控统一收尾，本文件不改动生成器。
