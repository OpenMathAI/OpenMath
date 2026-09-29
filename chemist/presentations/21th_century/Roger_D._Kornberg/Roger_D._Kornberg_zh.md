# Roger D. Kornberg（罗杰·科恩伯格）立传提示词

> qid=Q170676 · 1947-04-24（密苏里州圣路易斯）– 在世 · 美国生物化学家 · 21 世纪 · 诺贝尔化学奖（2006，独享——真核转录的分子基础）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Roger_D._Kornberg/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/`）——身份信息页 + 时间线页 + 表格语义化 tabularx + 金边公式框，是本次执行的版式语言。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注；肖像优先取本地 `images.txt`（2016 年 Kornberg 照或 2006 年 Roger.Kornberg.JPG），404 则装饰圆占位。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{dna}\enspace 亲眼看见转录的人\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生年（在世，卒项留白）、本名（Roger David Kornberg）、国籍、出生地、教育、博士、导师、核心领域、荣誉；家庭字段可写"诺奖世家长子"。事实取自本地 infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡呼应「DNA→RNA 的抄写」母题——一串圆点被逐个复制成另一串，暗示转录泡沿 DNA 前进。
5. **表格语义化 + 公式框**（★ 每个核心贡献页必须使用）：`tabularx` 三列表格（表头主色白字、第一列强调色加粗、三列语义化如 问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式框写 DNA→RNA 转录示意与 RNA Pol II 原子结构主题。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Roger David Kornberg（中文惯称：罗杰·科恩伯格）
- **生卒**：1947-04-24 生于密苏里州圣路易斯 → **在世**（卒项一律留白）
- **国籍**：United States（美国）
- **身份**：生物化学家；Stanford University School of Medicine 结构生物学教授；*Annual Review of Biochemistry* 主编（2004–2026，页面原文口径）；Annual Reviews 董事会成员
- **家庭**：犹太家庭；**诺贝尔奖得主 Arthur Kornberg 的长子**（页面原文 "the eldest son of biochemist Arthur Kornberg, who won the Nobel Prize"），母亲 Sylvy Kornberg 也是生物化学家；妻 Yahli Lorch（斯坦福同事，核小体功能研究合作者），育三子女（页面未具名，勿编）
- **教育轨迹**：
  - Harvard University：化学 BS 1967
  - Stanford University：化学物理 PhD 1972（论文 *The Diffusion of Phospholips in Membranes*——以页面原文 *The Diffusion of Phospholipids in Membranes* 为准）
  - 博士后：英国剑桥 MRC Laboratory of Molecular Biology（1970s）
- **导师**：Harden M. McConnell（博士导师，infobox/正文双载）；博士后合作导师 Aaron Klug 与 Francis Crick（MRC）
- **研究领域**：结构生物学、真核转录——核小体（chromatin）、Mediator 共激活复合物、RNA 聚合酶 II 原子结构；早年膜脂动力学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **圣路易斯书香门第（1947）**：诺奖得主 Arthur Kornberg 的长子，母亲 Sylvy 亦是生物化学家——"父子双诺奖"的科学世家（父亲获奖详情页面未载年份奖项，见 §5 红线）。
2. **哈佛化学本科（1967）**：化学 BS 毕业。
3. **斯坦福化学物理博士（1972）**：师从 Harden M. McConnell，研究膜中磷脂的扩散。
4. **flip-flop 命名**：研究生期间发现磷脂在双分子层膜的"翻转"与侧向扩散，因其几年前刚学过电子电路的触发器（flip-flop）而以此命名——衍生出 flippases/floppases 的蛋白命名。
5. **MRC 博士后（1970s）**：随 Aaron Klug 与 Francis Crick 工作——发现**核小体**（nucleosome）：真核细胞核内包装染色体 DNA 的基本蛋白复合物。
6. **200 bp 八聚体**：核小体内约 200 bp DNA 缠绕在组蛋白八聚体上——染色质（chromatin）的结构单元由此确立。
7. **核小体的功能（与 Yahli Lorch）**：启动子上的核小体阻止转录起始——核小体由此被认作**广谱基因阻遏物**。
8. **哈弗医学院（1976）→ 斯坦福（1978）**：1976 年任哈佛医学院生物化学助理教授，1978 年转任斯坦福结构生物学教授至今。
9. **酵母忠实转录系统**：斯坦福团队以面包酵母（简单单细胞真核生物）建立忠实转录系统，从中纯化出转录所需的全部几十种蛋白——这些组分从酵母到人类高度保守。
10. **Mediator 发现**：基因调控信号传向 RNA 聚合酶机器要经一个额外蛋白复合物——团队命名 *Mediator*；诺奖委员会评："真核生物的巨大复杂性正靠组织特异性物质、DNA 增强子与 Mediator 的精细互动实现——Mediator 的发现是理解转录过程真正的里程碑。"（页面转引，可引）
11. **二十年磨一剑**：以研究生时代练就的脂膜功夫在脂双层上培养二维蛋白晶体 → 电镜低分辨图像 → 最终用 X 射线晶体学解出 RNA 聚合酶的**原子分辨率三维结构**。
12. **"转录全流程"成像**：结构延伸到聚合酶与辅助蛋白的复合物；诺奖委员会评："Kornberg 图景真正革命性的一面是它捕捉到了全速进行中的转录——我们看见了 RNA 链的合成，因此看见了 DNA、聚合酶与 RNA 在此过程中的确切位置。"（页面转引，可引）
13. **2006 诺贝尔化学奖（独享）**：理由 "for his studies of the molecular basis of eukaryotic transcription"；同年获 Louisa Gross Horwitz Prize；2009 当选皇家学会外籍院士（ForMemRS）。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（生命绿 lifegreen） | `#146B3A` | 转录与生命的底色（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（核小体 badgeNuc） | `#1B7A43` | 绿 200 bp 八聚体 / 染色质 |
| 分类色 2（转录机器 badgeTxn） | `#2E5A9E` | 蓝 RNA Pol II / Mediator |
| 分类色 3（结构成像 badgeXtal） | `#D97B29` | 琥珀二维晶体 / X 射线原子结构 |
| 分类色 4（膜生物学 badgeLipid） | `#C0395B` | 玫瑰 flip-flop / 磷脂扩散 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（一串圆点复制成另一串），呼应「DNA→RNA 抄写」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Lonesome** — AShamaluevMusic（`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/inspiring-electronic/16-xBLYHNv7C4Q-Lonesome - by AShamaluevMusic ｜ Sad and Emotional Cinematic Music.wav`；**不要复制 wav 文件**，Makefile 按此绝对路径引用）
- **风格**：孤独 / 情绪化弦乐 / 长跑者气质
- **匹配理由**：
  - "二十年磨一剑"的 X 射线攻坚——独享诺奖背后是一个人对抗原子分辨率难题的长跑，Lonesome 的孤独气质正合
  - 情绪化弦乐匹配父子两代诺奖的家族叙事——荣耀之下的个人坚持
  - 结尾落在"亲眼看见转录"的顿悟时刻，音乐由抑转扬
- **时长**：以实际文件为准 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 亲眼看见转录的人 / Roger D. Kornberg 1947– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生年/在世留白、本名、国籍、教育、博士、导师、出生地/领域/荣誉）
03  科恩伯格之路 — Sanger 式时间线（10 节点：1947→1967→1972→1974→1976→1978→1990s→2001→2006→在世）
04  诺奖世家长子 (1947–1967) — 表格「时间|事件|结果」（父亲 Arthur 诺奖得主、母亲 Sylvy 生物化学家）
05  斯坦福与 flip-flop (1967–1972) — 表格「问题|发现|命名」+ 公式框：磷脂 flip-flop 与侧向扩散
06  MRC 与核小体发现 (1970s) — 表格「合作者|对象|发现」+ 公式框：约 200 bp DNA 缠绕组蛋白八聚体
07  核小体是阻遏物 (与 Lorch) — 表格「假设|实验|结论」
08  酵母忠实转录系统 — 表格「体系|方法|结果」（几十种蛋白、酵母→人保守）
09  Mediator 的发现 — 表格「问题|方法|意义」+ 引语框：诺奖委员会"里程碑"评语
10  二十年磨一剑：Pol II 原子结构 — 表格「阶段|方法|分辨率」+ 公式框：二维晶体→电镜→X 射线
11  2006 诺贝尔化学奖（独享）— 表格「理由|对象|意义」+ citation 原句框
12  荣誉 — Sanger 式「类别|代表|意义」表格（Gairdner 2000 / Welch 2001 / Harvey 1997 / Horwitz 2006 / ForMemRS 2009 等）
13  科恩伯格父子 — Sanger FFT 页式流程图（父 Arthur 诺奖 → 子 Roger 2006 化学奖 → 家族科学传承）
14  结尾 — 「生命抄写自己时，他站在旁边看清了每一个字母。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 父亲获奖详情 | page.md 只写 Arthur Kornberg "who won the Nobel Prize"——**页面未载年份与奖项类别**，禁写 1959、禁写"生理学或医学奖"（页面无载）；只写"诺贝尔奖得主 Arthur Kornberg 长子" |
| 共享结构 | 2006 **独享**——勿写共享 |
| 获奖理由口径 | intro 口径 "for his studies of the process by which genetic information from DNA is copied to RNA"，获奖理由句 "the molecular basis of eukaryotic transcription"（页面引号原句，可引）；两条诺奖委员会评语为页面转引，注明出处 |
| 论文名 | PhD 论文页面正文作 *The Diffusion of Phospholipids in Membranes*（infobox 链接文字有一处 Phospholips 排印差）——以 Phospholipids 为准 |
| 在世口径 | 1947-04-24 生，**在世**——封面、身份页、时间线卒项一律留白 |
| Grant Jensen | metadata doctoral_student 含 Grant Jensen，页面无——**禁入库** |
| 同框照人物 | 2006 年美国诺奖得主合影（Fire/Smoot/Mello/Mather 等）只是照片图注——**不构成关系，不入库**；正文不展开合影中的其他人物 |
| 产业职务 | 公司顾问/董事（Cocrystal、ChromaDex、StemRad、Oplon、Pacific Biosciences、Teva 等）只列机构页一句，勿展开商业细节 |
| 主编年份 | *Annual Review of Biochemistry* 主编"2004–2026"为页面原文口径——照写勿改 |
| flip-flop | 命名来由是"几年前学过电子电路触发器"——勿写成"借自生物学"；flippases/floppases 是**由该术语衍生**的蛋白命名 |
| Mediator 命名 | 是 Kornberg 团队"自行命名"（dubbed）——勿写成学界先有此名 |
| 引语红线 | 仅三条可引：获奖理由句 + 两条诺奖委员会评语（均页面带引号）——其余一律间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q170676 | ✅ |
| name_zh | 罗杰·科恩伯格 | ✅ |
| name_en | Roger D. Kornberg | ✅（新建记录，库内无同名；父 Arthur Kornberg 库内 id 3780） |
| birth_date | 1947-04-24 | ✅ |
| death_date | （在世，留空） | ✅ |
| nationality | United States | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | structural biology / biochemistry（metadata 口径）；person_field 细分见下 | ✅ |
| has_biography | false（Beamer 立传后置 1） | ✅ |

person_field 细分（rank 表）：

| rank | field | 说明 |
|---|---|---|
| 0 | eukaryotic transcription | 2006 诺奖工作：分子基础 |
| 1 | structural biology | RNA Pol II 原子结构 |
| 2 | chromatin & nucleosome | 核小体发现与功能 |
| 3 | biochemistry | 转录系统生化重建 |

## 7. 社会关系入库清单

**家庭（parent-child 不写 direction，按 from<to 约定入库）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| parent-child | Arthur Kornberg | 不写（无向约定） | 父亲，诺贝尔奖得主（页面未载年份奖项）；库内既有记录 id 3780 |
| parent-child | Sylvy Kornberg | 不写（无向约定） | 母亲，生物化学家 |
| spouse | Yahli Lorch | 无向 | 妻子；合作证明启动子上的核小体阻止转录起始 |

**师长**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Harden M. McConnell | 师→生（博士导师） | 斯坦福化学物理博士导师，1972 |
| advisor-student | Aaron Klug | 师→生（博士后导师） | 剑桥 MRC 博士后合作（库内 Q190626） |
| advisor-student | Francis Crick | 师→生（博士后导师） | 剑桥 MRC 博士后合作 |

> **禁入库名单**：Grant Jensen（metadata-only doctoral_student）、三名子女（页面未具名）、2006 合影人物（Andrew Fire/George Smoot/Craig Mello/John C. Mather——同框非关系）、Dick Cheney（合影中的政治人物，禁入库禁成段展开）、各公司（产业职务非学术关系）。metadata doctoral_advisor 仅 Harden M. McConnell，与正文一致，无 metadata-only 增补。

## 8. 奖项清单

- 1981 Eli Lilly Award in Biological Chemistry；1982 Passano Award；1990 Ciba-Drew Award
- 1997 Harvey Prize（Technion）；2000 Gairdner Foundation International Award
- 2001 Hoppe-Seyler Award（德国生化与分子生物学学会）；2001 Welch Award in Chemistry
- 2002 ASBMB-Merck Award；2002 Pasarow Award（癌症研究）；2002 Grand Prix Charles-Leopold Mayer
- 2003 EMBO Member；2003 Massry Prize
- 2005 Alfred P. Sloan, Jr. Prize（GM 癌症研究基金会）；2006 Dickson Prize（匹兹堡大学）
- 2006 Nobel Prize in Chemistry（**独享**）；2006 Louisa Gross Horwitz Prize
- 2008 American Philosophical Society；2009 Foreign Member of the Royal Society（ForMemRS）
- 2012 Ruppin Academic Center Honorary Fellow；Umeå University 荣誉博士；AACR Academy / AAAS Fellow（年份页面无载，勿写）

## 9. 机构清单

- 教育：Harvard University（化学 BS 1967）；Stanford University（化学物理 PhD 1972）；MRC Laboratory of Molecular Biology（剑桥，博士后 1970s）
- 任职：Harvard Medical School（1976，生物化学助理教授）；Stanford University School of Medicine（1978–，结构生物学教授）；*Annual Review of Biochemistry* 主编（2004–2026）；Annual Reviews 董事会
- 产业顾问/董事：Cocrystal Discovery（主席）、ChromaDex（主席）、StemRad、Oplon（主席）、Pacific Biosciences（顾问委员会）；董事：OphthaliX、Protalix BioTherapeutics、Can-Fite BioPharma、Simploud、Teva Pharmaceutical Industries

## 10. 终审清单

- [x] 2006 独享表述准确；获奖理由与两条委员会评语均页面转引可溯源
- [x] 父亲叙事只写"诺奖得主长子"，年份/奖项类别（页面无载）未写
- [x] 在世口径：卒项三处留白一致
- [x] 核小体 ~200 bp/八聚体、flip-flop 命名来由、Mediator 团队命名表述准确
- [x] 主编年份 2004–2026 照页面原文
- [x] parent-child 不写 direction；Grant Jensen 与合影人物禁入库已注
- [x] 品牌 OpenMathAI、半角引号、封面国籍行、身份信息页齐备
- [x] `make distclean && make` 0 错误（Beamer 执行时验证）

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Roger_D._Kornberg/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/` 已就位（真实肖像或装饰圆占位，图注如实）
- [ ] **国籍**：封面顶部明示美国；**在世留白**三处一致
- [ ] **引语核对**：获奖理由句 + 两条委员会评语均可在 page.md 找到原文
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一；DNA→RNA 示意排版正常
- [ ] 与 21 世纪批次其他篇格式对齐
