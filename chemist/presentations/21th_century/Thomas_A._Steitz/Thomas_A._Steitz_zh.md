# Thomas A. Steitz（托马斯·A·施泰茨）立传提示词

> qid=Q109559 · 1940-08-23 – 2018-10-09 · 美国生物化学家 · 21 世纪 · 诺贝尔化学奖（2009，与 Venkatraman Ramakrishnan、Ada Yonath 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Thomas_A._Steitz/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次执行的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/` 已就位；若无真实肖像则用装饰圆占位，图注注明）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{dna}\enspace 读出核糖体原子结构的人\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「晶体 / 原子分辨率」母题——离散圆点暗示晶体学中被逐个定位的原子。
5. **表格语义化 + 公式框**（★ Sanger 版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化（如 50S 亚基 1.5 万余原子分辨率结构、肽酰转移酶中心）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Thomas Arthur Steitz（中文惯称：托马斯·A·施泰茨）
- **生卒**：1940-08-23 生于美国威斯康星州密尔沃基 → 2018-10-09 逝于康涅狄格州 Branford（胰腺癌治疗并发症），享年 78
- **国籍**：United States（美国）
- **身份**：生物化学家 / 结构生物学家；耶鲁大学分子生物物理与生物化学 Sterling 教授；霍华德·休斯医学研究所（HHMI）研究员
- **家庭**：1970 年与 Joan A. Steitz（著名分子生物学家，同为耶鲁 Sterling 教授）结婚；一子 Jon，孙辈 Adam 与 Maddy；居 Branford, Connecticut
- **教育轨迹**：Wauwatosa East High School → Lawrence University（Appleton, 威斯康星；化学本科，1962）→ Harvard University（生物化学与分子生物学博士，1966）
- **导师**：William N. Lipscomb, Jr.（博士导师；1976 诺贝尔化学奖）；infobox 另列 Other academic advisor：David M. Blow
- **博士论文**：*The 6Å crystal structure of carboxypeptidase A*（infobox 系年 1967；正文作 1966 年获 PhD——见 §5 年份陷阱）
- **研究领域**：生物结晶学（bio-crystallography）——X 射线晶体学、结构生物学、核糖体结构
- **生活**：喜好滑雪、徒步与园艺；常办 Halloween 家庭派对（讣闻轶事，正文一笔即可）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **密尔沃基之子（1940）**：生于威斯康星州密尔沃基，本地报纸后以 "Inquisitiveness of Milwaukee native leads to a Nobel Prize" 追踪其诺奖。
2. **Lawrence 大学化学本科（1962）**：小校起步；2010 年 6 月母校将化学楼命名为 Thomas A. Steitz Hall of Science。
3. **Harvard / Lipscomb 门下（1962–1966）**：先完成小分子甲基乙烯磷酸盐结构训练，继而参与测定羧肽酶 A 与天冬氨酸氨甲酰转移酶（ATCase）——均为当时最大的原子分辨率结构。
4. **MRC LMB 博士后（1967–1970）**：以 Jane Coffin Childs Fellow 身份在英国剑桥分子生物学实验室（LMB）做博士后——结构生物学的世界中心。
5. **伯克利风波（1970）**：短暂任 UC Berkeley 助理教授，因校方不肯给妻子 Joan 教职（仅因她是女性）而辞职——科学伉俪共进退。
6. **双双加盟耶鲁（1970）**：Tom 与 Joan 同时加入耶鲁教职；后任分子生物物理与生物化学 Sterling 教授、HHMI 研究员。
7. **50S 大亚基原子结构（2000）**：与 Peter Moore 用 X 射线晶体学测定嗜盐古菌 *Haloarcula marismortui* 核糖体 50S 大亚基原子结构，发表于 *Science*。
8. **核糖体是核酶**：Gairdner 奖（2007）理由明载——证明肽酰转移酶（EC 2.3.2.12）是 RNA 催化的反应；蛋白质合成催化核心不含蛋白酶。
9. **抗生素抑制机制**：揭示抗生素抑制肽酰转移酶功能的机制，为结构导向的抗菌药物设计铺路。
10. **从结构到药厂**：核糖体抗生素公司 Rib-X Pharmaceuticals 联合创始人（后更名 Melinta Therapeutics）。
11. **2009 诺贝尔化学奖**：与 Venkatraman Ramakrishnan、Ada Yonath 共享 "for studies of the structure and function of the ribosome"。
12. **荣誉序列**：Sir Hans Krebs Medal（2000）、Keio Medical Science Prize（2006）、Gairdner（2007）、诺贝尔奖（2009）、英国皇家学会外籍院士 ForMemRS（2011）。
13. **门生与晚年**：infobox Notable students 载 Nenad Ban（50S 结构核心成员）；2018-10-09 因胰腺癌治疗并发症逝世，享年 78。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（砖红 brickred） | `#A63A2B` | 晶体学衍射图谱的暖色基调 / Sterling 教授的学术分量（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（核糖体结构 badgeRibo） | `#2E5A9E` | 蓝 50S 大亚基 / 原子模型 |
| 分类色 2（催化机制 badgeRibozyne） | `#1B7A43` | 绿肽酰转移酶 / 核酶 |
| 分类色 3（抗生素 badgeAbx） | `#D97B29` | 琥珀抗生素结合位点 / Rib-X |
| 分类色 4（师承与传承 badgeLegacy） | `#C0395B` | 玫瑰 Lipscomb 门下 / Nenad Ban |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「晶体 / 原子」的离散点阵排列。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**The Invisible Light** — Infraction（文件 `music_audio/inspiring-electronic/19-tGxXsgSKPiQ-...The Invisible Light.wav`；不要复制 wav 文件，Makefile 里直接引用原路径/软链）
- **风格**：纪录片式 / 冷峻而温暖 / 结构感强的电子氛围
- **匹配理由**：
  - "invisible light" 与 X 射线晶体学天然互文——看不见的光，照出看不见的原子
  - 纪录片气质匹配其叙事：密尔沃基 → Lawrence → Harvard → LMB → 耶鲁 → 50S 原子结构 → 诺贝尔奖
  - 冷峻克制的电子氛围匹配结构生物学「精确、冷静、直抵原子」的工作气质
- **时长**：以实际曲目时长为准，ffmpeg `-shortest` 自动对齐 15 页 × 7 秒 ≈ 105 秒

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 读出核糖体原子结构的人 / Thomas A. Steitz 1940–2018 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  施泰茨的一生 — Sanger 式时间线（10 节点：1940→1962→1966→1967→1970→2000→2006→2007→2009→2018）
04  早年：密尔沃基与 Lawrence (1940–1962) — 表格「时间|事件|结果」
05  Harvard：Lipscomb 门下的大结构 (1962–1967) — 表格「阶段|课题|结果」+ 公式框：羧肽酶 A / ATCase
06  LMB 博士后与伯克利风波 (1967–1970) — 表格「地点|经历|结果」
07  耶鲁岁月：从酶到核糖体 (1970–1999) — 表格「时期|转向|结果」
08  50S 大亚基原子结构 (2000) — 表格「问题|方法|结果」+ 公式框：H. marismortui 50S 亚基
09  核糖体是核酶 + 抗生素机制 — 表格「问题|方法|结果」+ 公式框：肽酰转移酶 = RNA 催化 · 2009 诺奖
10  结构导向制药：Rib-X → Melinta — Sanger FFT 页式流程图（结构 → 位点 → 药物设计 → 公司）
11  荣誉 — Sanger 式「类别|代表|意义」表格（Krebs 2000 / Keio 2006 / Gairdner 2007 / Nobel 2009 / ForMemRS 2011）
12  科学伉俪：Tom 与 Joan Steitz — 表格「人物|领域|结果」（双 Sterling 教授 / 伯克利风波 / 一子 Jon）
13  门生与遗产 — 四分类遗产盒 + 公式框：Steitz Hall of Science（2010）/ Nenad Ban
14  结尾 — 「把生命的合成工厂，一个原子一个原子地看清楚。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2009 诺奖口径 | 与 Ramakrishnan、Yonath **三人共享**；官方理由原文 "for studies of the structure and function of the ribosome"；勿写"独享"或遗漏共同得主 |
| PhD 年份 | 正文作 1966 年获 PhD；infobox 论文条目系年 1967——**以正文 1966 为准**，论文年份如需引用须注明 infobox 口径 |
| Lipscomb 名字 | William N. Lipscomb, Jr.（1976 诺贝尔化学奖）；infobox Doctoral advisor 写全名，正文链接作 William Lipscomb——库内规范记录为 "William Lipscomb"，入库用后者 |
| 博士课题顺序 | 先做小分子训练任务（甲基乙烯磷酸盐），再参与羧肽酶 A 与 ATCase——"each the largest atomic structure determined in its time" 是 page.md 原文，可引用 |
| 伯克利辞职 | page.md 明载：校方不接受妻子 Joan 入教职"because she was a woman"，他因此辞职——可写，措辞客观，勿加工成"控诉叙事" |
| 50S 物种 | 嗜盐古菌 *Haloarcula marismortui*；与 **Peter Moore** 合作、2000 年发表于 *Science*——勿写成一人完成或写错物种 |
| 肽酰转移酶 | "RNA 催化" 口径出自 2007 Gairdner 奖理由（page.md 原文），勿改写成"蛋白质催化"或把 Gairdner 理由当诺贝尔理由 |
| 其他学术导师 | infobox 载 David M. Blow（Other academic advisors）；正文只明载 LMB 博士后经历（1967–1970），未明言 Blow 指导该段——note 措辞勿绑定 |
| 妻子 | Joan A. Steitz 是本人（婚后随夫姓）的著名分子生物学家、耶鲁 Sterling 教授——勿写成"同姓巧合"或混淆为另一人 |
| 门生入库 | infobox Notable students 仅 **Nenad Ban** 一人；其余人物（如 Ramsey 类）页面无载，**不予入库** |
| 公司名 | Rib-X Pharmaceuticals **现为 Melinta Therapeutics**（page.md 原文 "now"）——勿写成两家公司并列 |
| 引语红线 | 页面正文几乎没有第一人称引语；Private life 节的 Halloween 段是讣闻叙述——中文引号内不得出现无法溯源的"原话" |
| 中名 | Thomas **Arthur** Steitz——身份信息页本名行写全名 |
| 死因 | 胰腺癌**治疗并发症**（complications during treatment of pancreatic cancer），Branford, Connecticut——勿简写成"胰腺癌去世" |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q109559 | ✅（复用库内 #3703 回填） |
| name_zh | 托马斯·A·施泰茨 | ✅ |
| name_en | Thomas A. Steitz（库内 #3703 既有形式） | ✅ |
| birth_date | 1940-08-23 | ✅ |
| death_date | 2018-10-09 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | biochemist（修正库内误值 mathematician） | ✅ |
| field_of_work | crystallography（person_field 细分：X-ray crystallography / structural biology / ribosome / molecular biophysics，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 同事 / 共同得主 / 家人**（★红线：只收 page.md 正文或 infobox 明载的关系）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | William Lipscomb | 师→生（博士导师） | Harvard 博士导师；1976 诺贝尔化学奖（库内既有边幂等去重） |
| advisor-student | David M. Blow | 师→生（其他学术导师） | infobox Other academic advisors |
| advisor-student | Nenad Ban | 生→师（学生） | infobox Notable students；50S 结构核心成员 |
| colleague | Peter Moore (chemist) | 无向 | 共同测定 50S 大亚基原子结构（2000 Science） |
| co-honored | Venkatraman Ramakrishnan | 无向 | 2009 诺贝尔化学奖共同得主 |
| co-honored | Ada Yonath | 无向 | 2009 诺贝尔化学奖共同得主 |
| spouse | Joan A. Steitz | 无向 | 分子生物学家、耶鲁 Sterling 教授；一子 Jon |

> **禁入库名单**（页面无载，仅 metadata/推断，一律不建关系）：Jon（儿子，仅 Private life 载名字，父子关系非 page.md 关系语义范畴、无独立条目价值）、Walter Keller 等任何未具名合作者、Halloween 派对宾客等讣闻人物。Rosenstiel Award / Newcomb Cleveland Prize / Pfizer Award in Enzyme Chemistry 仅 frontmatter 列出、正文无共同得主信息——无 co-honored 行。

## 8. 奖项清单

- Nobel Prize in Chemistry（2009，与 Ramakrishnan / Yonath 共享）
- Sir Hans Krebs Medal（2000）
- Keio Medical Science Prize（2006）
- Canada Gairdner International Award（2007；理由含肽酰转移酶 RNA 催化与抗生素抑制机制）
- Newcomb Cleveland Prize（frontmatter 载）
- Pfizer Award in Enzyme Chemistry（frontmatter 载）
- Rosenstiel Award（frontmatter 载）
- Foreign Member of the Royal Society，ForMemRS（2011）
- Sterling Professor（耶鲁讲席教授头衔）
- Honorary Doctorate of University of Buenos Aires；honorary doctor of the University of Bordeaux（frontmatter 载）
- Fellow of the American Association for the Advancement of Science（frontmatter 载）

## 9. 机构清单

- 教育：Wauwatosa East High School → Lawrence University（1962，化学）→ Harvard University（PhD 1966）
- 任职：UC Berkeley 助理教授（短暂，1970 前辞职）→ Yale University（1970– ，Sterling Professor）→ HHMI 研究员
- 访问：Göttingen Macy Fellow（1976–1977）；Caltech Fairchild Scholar（1984–1985）
- 博士后：MRC Laboratory of Molecular Biology（1967–1970，Jane Coffin Childs Fellow）
- 企业：Rib-X Pharmaceuticals 联合创始人（今 Melinta Therapeutics）
- 命名机构：Lawrence University 化学楼 Thomas A. Steitz Hall of Science（2010-06）

## 10. 终审清单

- [x] 生卒 1940-08-23 / 2018-10-09，享年 78，出生地 Milwaukee、去世地 Branford
- [x] 2009 三人共享（Ramakrishnan / Yonath）表述准确；诺奖理由英文原文口径正确
- [x] PhD 1966（正文）；羧肽酶 A / ATCase "当时最大原子结构"表述有据
- [x] 50S 亚基 = *H. marismortui*、与 Peter Moore 合作、2000 Science——三要素齐全
- [x] Gairdner 2007 理由与诺贝尔理由不混用
- [x] 伯克利辞职原因客观转述，无引语杜撰
- [x] 门生仅 Nenad Ban；禁入库名单已注明
- [x] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Thomas_A._Steitz/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/` 内真实肖像已就位，否则装饰圆占位并注明
- [ ] **国籍**：封面顶部明示美国
- [ ] **引语核对**：中文引号内原话必须能在 page.md 找到；无原话一律改间接转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 2009 另两篇（Ramakrishnan、Yonath）口径互查：共享得主名、诺奖理由一致
