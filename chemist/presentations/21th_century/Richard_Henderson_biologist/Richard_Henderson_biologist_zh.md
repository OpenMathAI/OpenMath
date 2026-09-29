# Richard Henderson（理查德·亨德森）立传提示词

> qid=Q1678456 · 1945-07-19 –（在世）· 英国分子生物学家 · 21 世纪 · 诺贝尔化学奖（2017，与 Jacques Dubochet、Joachim Frank 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Richard_Henderson_biologist/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/` 取 page.md 首图 2017 年斯德哥尔摩诺奖记者会照片；下载失败用装饰圆占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{atom}\enspace 不必结晶的结构生物学家\enspace·\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「原子级分辨」母题——细密离散圆点暗示最终被逐个看清的蛋白质原子。
5. **表格语义化 + 公式框**（★ 核心版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Richard Henderson（中文惯称：理查德·亨德森；头衔缩写 CH FRS FMedSci HonFRSC）
- **生卒**：1945-07-19 生于苏格兰爱丁堡 → 在世（2026-09 无卒日，年龄留白处理）
- **国籍**：United Kingdom（英国）
- **身份**：英国分子生物学家与生物物理学家；MRC 分子生物学实验室（LMB）名誉研究员；1996–2006 任 LMB 所长
- **家庭**：父亲是面包师（页面实载）；页面无载婚姻与子女信息——禁杜撰
- **教育轨迹**：
  - Newcastleton 小学 → Hawick High School → Boroughmuir High School
  - University of Edinburgh 物理学 BSc（1966，一等荣誉）
  - Corpus Christi College, Cambridge 博士研究生；1969 获剑桥大学 PhD（infobox 论文条目标 1970，年份口径见 §5）
- **导师**：David Mervyn Blow（博士导师，MRC LMB）
- **博士**：1969（正文口径），论文《X-Ray Analysis of α-chymotrypsin: Substrate and Inhibitor Binding》（α-胰凝乳蛋白酶的 X 射线分析：底物与抑制剂结合）
- **研究领域**：结构生物学——冷冻电镜、电子晶体学、膜蛋白结构

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **爱丁堡面包师之子（1945）**：生于战后苏格兰；父亲是面包师——从小学到剑桥的路径没有学术世家的捷径。
2. **物理学一等荣誉（1966）**：爱丁堡大学物理学 BSc 一等荣誉毕业——X 射线与衍射的数学功底先于生物学到来。
3. **博士：胰凝乳蛋白酶（1966–1969）**：在 David Mervyn Blow 指导下于 MRC LMB 做 α-胰凝乳蛋白酶的 X 射线分析——晶体学的正统训练。
4. **耶鲁博士后：钠通道（1970s 初）**：对膜蛋白的兴趣把他带到耶鲁大学研究电压门控钠通道——从此锚定"膜蛋白"这一硬骨头。
5. **重回 LMB 与 Unwin 合作（1975）**：与 Nigel Unwin 用电镜研究膜蛋白细菌视紫红质（bacteriorhodopsin）；1975 年 *Nature* 论文建立低分辨率结构模型——**七次跨膜 α 螺旋**。
6. **1975 论文的范式意义**：证明膜蛋白具有确定的结构、跨膜 α 螺旋真实存在——此前"膜蛋白无法结构化"的悲观一扫而空。
7. **1990 原子模型**：独立继续细菌视紫红质工作，1990 年用电镜晶体学在 *JMB* 发表原子模型——**史上第二个膜蛋白原子模型**；其电子晶体学技术至今仍在使用。
8. **1995 预言**：在 *Quarterly Reviews of Biophysics* 撰文主张单颗粒电镜原则上可达成蛋白质的原子分辨率模型——为二十年后单颗粒冷冻电镜革命画出路线图。
9. **直接电子探测相机**：开创性推动直接电子探测器（direct electron detectors）研发——单颗粒冷冻电镜达成目标的关键硬件拼图。
10. **构象热稳定化与 Heptares（2007）**：与 Chris Tate 共同开发构象热稳定化方法，让任意蛋白在锁定构象下更稳定，解决了多个 GPCR 的结晶；2007 年借助 LifeArc 创办 MRC 衍生公司 Heptares Therapeutics，持续开发 GPCR 靶向药物。
11. **LMB 所长（1996–2006）**：执掌结构生物学的世界重镇十年。
12. **2017 诺贝尔化学奖**：与 Jacques Dubochet、Joachim Frank 共享，官方理由 "for developing cryo-electron microscopy for the high-resolution structure determination of biomolecules in solution"；页面引述诺奖评语——"Thanks to his work, we can look at individual atoms of living nature..."（感谢他的工作，我们能看见生命中的单个原子）；Nobel Lecture 题目 "From Electron Crystallography to Single Particle cryoEM"。
13. **荣誉长廊**：William Bate Hardy Prize（1978）、FRS（1983）、Ernst-Ruska Prize（1981）、Rosenstiel Award（1991）、Louis-Jeantet Prize（1993）、Gregori Aminoff Prize（1999，与 Unwin 共同）、Copley Medal（2016）、Alexander Hollaender Award（2016）、Wiley Prize（2017）、Companion of Honour（2018）、爱丁堡皇家学会 Royal Medal（2018）。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深酒红 deepwine） | `#7A1E28` | 深红色的坚持与突破——二十年打磨一个蛋白的定力（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（电子晶体学 badgeElecCrys） | `#2E7FA8` | 蓝细菌视紫红质 / 七跨膜螺旋 |
| 分类色 2（单颗粒电镜 badgeSP） | `#1B7A43` | 绿原子分辨率预言 |
| 分类色 3（膜蛋白与 GPCR badgeGPCR） | `#D97B29` | 琥珀热稳定化 / Heptares |
| 分类色 4（探测器革命 badgeDetector） | `#C0395B` | 玫瑰直接电子探测相机 |
| 背景 | `#F8F5F5` | 微暖浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「分辨率阶梯——从螺旋到原子」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Through the Darkness** — Audiomachine（文件 `music_audio/inspiring-electronic/14-Trn1cSsY2t8-Audiomachine - Through the Darkness.wav`；不复制 wav 文件）
- **风格**：穿越黑暗的史诗感电影配乐
- **匹配理由**：
  - "穿越黑暗" 直喻其科学叙事——从 1975 低分辨率模型到 1990 原子模型再到 2015 后单颗粒革命，是二十年"在黑暗中推动分辨率极限"的长跑
  - "史诗感" 匹配 LMB 传统的厚重——从 Crick/Perutz 一脉传下的结构生物学圣殿，他是承上启下的掌门（1996–2006 所长）
  - 尾段上扬契合 2017 诺奖的技术大成时刻
- **时长**：以实际曲目时长为准，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 不必结晶的结构生物学家 / Richard Henderson 1945– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/领域/荣誉）
03  亨德森的一生 — 时间线（10 节点：1945→1966→1969→1973→1975→1990→1995→1996→2007→2017）
04  早年：面包师之子到爱丁堡 (1945–1966) — 表格「时间|事件|结果」
05  博士：Blow 与晶体学正统 (1966–1973) — 表格「时间|事件|结果」
06  耶鲁与膜蛋白 (1970s) — 表格「对象|问题|转向」
07  细菌视紫红质：1975 Nature — 表格「问题|方法|结果」+ 公式框：七次跨膜 α 螺旋
08  1990 原子模型 — 表格「挑战|方法|意义」+ 公式框：电子晶体学
09  1995 预言与直接探测器 — 表格「主张|路径|兑现」
10  热稳定化与 Heptares (2007) — 表格「方法|对象|转化」
11  2017 诺贝尔化学奖 — 表格「三人|分工|理由」+ 公式框：官方获奖理由英文原句（三人共享同一理由）
12  LMB 所长与学术谱系 — 表格「角色|时期|意义」（所长 1996–2006 / Blow 导师 / Unwin 合作者 / 门生群体）
13  荣誉长廊 — 高斯式「类别|代表|意义」表格 + itemize 荣誉清单
14  结尾 — 「不必结晶，原子自现。」（自撰收束句，非引语）
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2017 三人分工 | Henderson＝首张膜蛋白电子密度图（1975 七跨膜模型）/1990 原子模型/推动技术极限，Dubochet＝玻璃化制样、Frank＝单颗粒算法——勿混淆；三人共享**同一句**官方理由 |
| 获奖理由 | "for developing cryo-electron microscopy for the high-resolution structure determination of biomolecules in solution"——develop 非 invent |
| "第二个"原子模型 | 1990 细菌视紫红质模型是**史上第二个**膜蛋白原子模型（页面原文 "the second ever"）——勿写成第一个 |
| 博士年份 | 正文 "obtained his PhD degree from the University of Cambridge in 1969"；infobox 论文条目 (1970)——正文页写 1969 并加注 infobox 口径 |
| Hardy Prize | 奖项清单列 1978（"1978 Awarded the William Bate Hardy Prize"）——亮点 13 草稿中"1987 前实为 1978"系笔误来源，终版一律写 **1978** |
| 门生列表 | 页面 "Post-docs and PhD students" 一节混合列出 10 人（Agard/Bullough/Grigorieff/Grisshammer/Kunji/Rosenthal/Rubinstein/Schertler/Tate/Unger），**未逐一明载博士师生关系**——一律不入关系库（Tate 以 colleague 入库） |
| 同名区分 | 本篇是生物学家 Richard Henderson（Q1678456，born 1945）——与页面语境中其他 Henderson 无关；DB 目录名用 Richard_Henderson_biologist 防撞 |
| 引言口径 | 诺奖评语 "Thanks to his work, we can look at individual atoms of living nature..." 为页面引用句，可整句引用并标注为诺奖评语；无其他原话引语 |
| 兴趣爱好 | 山地徒步、皮划艇、好酒（页面 Other positions 节实载）——轶事可轻用，勿喧宾夺主 |
| 访谈 | Jim Al-Khalili《The Life Scientific》BBC Radio 4，2018-02 首播——背景信息勿写成年份错误 |
| 公司角色 | Heptares 由 Henderson 与 Tate 借 LifeArc 帮助创办——两人共同创办，勿写成 Henderson 一人 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q1678456 | ✅ |
| name_zh | 理查德·亨德森 | ✅ |
| name_en | Richard Henderson | ✅ |
| birth_date | 1945-07-19 | ✅ |
| death_date | （在世，留空） | ✅ |
| nationality | United Kingdom | ✅ |
| primary_occupation | molecular biologist | ✅ |
| field_of_work | structural biology（person_field 细分见下表） | ✅ |

**person_field 细分（rank 表）**：

| rank | name_en | name_zh |
|---|---|---|
| 0 | cryo-electron microscopy | 冷冻电子显微镜 |
| 1 | electron crystallography | 电子晶体学 |
| 2 | membrane protein structure | 膜蛋白结构 |
| 3 | structural biology | 结构生物学 |

## 7. 社会关系入库清单

**师长 / 同事 / 共同得主**（★红线：只收 page.md 正文或 infobox 明载；metadata-only 一律不入库）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | David Mervyn Blow | 师→生（博士导师） | MRC LMB，α-胰凝乳蛋白酶 X 射线分析 |
| colleague | Nigel Unwin | 无向 | 1975 *Nature* 细菌视紫红质合作者；1999 Gregori Aminoff Prize 共同得主 |
| colleague | Christopher G. Tate | 无向 | 构象热稳定化共同开发者；2007 共同创办 Heptares Therapeutics |
| co-honored | Jacques Dubochet | 无向 | 2017 诺贝尔化学奖共同得主 |
| co-honored | Joachim Frank | 无向 | 2017 诺贝尔化学奖共同得主 |

> **禁入库名单**（"Post-docs and PhD students" 一节混合列出、未逐一明载师生关系）：David Agard、Per Bullough、Nikolaus Grigorieff、Reinhard Grisshammer、Edmund Kunji、Peter Rosenthal、John Rubinstein、Gebhard Schertler、Vinzenz Unger（Tate 除外，以 colleague 入库）。父亲（面包师，未具名）不入库。metadata.json properties 无额外关系字段。

## 8. 奖项清单

- Nobel Prize in Chemistry（2017，与 Dubochet/Frank 共享）
- William Bate Hardy Prize（1978）
- Ernst-Ruska Prize for Electron Microscopy（1981）
- Fellow of the Royal Society，FRS（1983）
- Sir Hans Krebs Medal，Federation of European Biochemical Societies（1984）
- Lewis S. Rosenstiel Award（1991）
- Louis-Jeantet Prize for Medicine（1993）
- Foreign Associate of the US National Academy of Sciences（1998）
- Founder Fellow of the Academy of Medical Sciences，FMedSci（1998）
- Gregori Aminoff Prize（1999，与 Nigel Unwin 共同）
- Honorary Fellow of Corpus Christi College / Honorary Member of the British Biophysical Society（2003）
- Distinguished Scientist Award and Fellow, Microscopy Society of America（2005）
- Honorary DSc, University of Edinburgh（2008）
- Copley Medal，Royal Society（2016）
- Alexander Hollaender Award in Biophysics（2016）
- Wiley Prize（2017）；HonFRSC（2017）
- Member of the Order of the Companions of Honour，CH（2018 Birthday Honours）
- Royal Medal of the Royal Society of Edinburgh（2018）；Honorary DSc, University of Leeds（2019）

## 9. 机构清单

- 教育：Newcastleton primary / Hawick High School / Boroughmuir High School；University of Edinburgh（BSc Physics 1966 一等荣誉）；Corpus Christi College, Cambridge（PhD 1969，Blow 指导）
- 任职：MRC Laboratory of Molecular Biology（1973– 至今；所长 1996–2006）；Yale University 博士后（钠通道）；UC Berkeley Miller Institute 访问教授（1993 春）；Heptares Therapeutics Ltd 共同创办（2007，与 Tate，经 LifeArc/MRCT 支持）
- 转化成果：构象热稳定化方法 → 多个 GPCR 结构解析 → GPCR 靶向药物管线

## 10. 终审清单

- [ ] 生卒 1945-07-19 / 在世留白；出生地 Edinburgh
- [ ] 2017 三人共享同一句官方理由；三人分工表述准确
- [ ] 1990 = 史上第二个膜蛋白原子模型；1975 = 七次跨膜螺旋（与 Unwin）
- [ ] 博士年份 1969（正文）+ infobox 1970 双口径注记；Hardy Prize 1978
- [ ] 门生 10 人不入关系库；Tate 以 colleague 入库
- [ ] 诺奖评语引句标注来源；结尾句非引语
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Richard_Henderson_biologist/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/` 肖像就位（2017 斯德哥尔摩记者会照片；失败用装饰圆）
- [ ] **国籍**：封面顶部明示英国
- [ ] **引语核对**：诺奖评语为唯一可直接引用整句；其余一律间接转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 黄金参照）对齐
