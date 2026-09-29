# Glenn T. Seaborg（格伦·西奥多·西博格）立传提示词

> qid=Q48973 · 1912-04-19 – 1999-02-25 · 美国化学家 · 20 世纪 · 诺贝尔化学奖（1951，与 Edwin McMillan 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Glenn_T._Seaborg/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 时间线页 + 表格语义化 tabularx + 金色公式展示框 + 气泡背景，是本次撰写的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（候选肖像：`Seaborg_in_lab_-_restoration.jpg` 1950 年实验室照，或 `SeaborgJFK.jpg` 与肯尼迪合影——优先实验室单人照）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{atom}\enspace 周期表的开拓者\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士导师（两位）、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「周期表逐格点亮」的母题——圆点像锕系系列在周期表下方新增的一整行格位。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）——锕系概念（actinide series 置于 lanthanide series 之下）与十种元素的发现序列是全篇视觉锚点。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Glenn Theodore Seaborg（中文惯称：格伦·西奥多·西博格；⚠️ 正文 Early life 载出生名为 Glen Theodore Erickson Seaborg，infobox 作 Glen Theodore Seaborg——11 岁时自行把 Glen 改拼为 Glenn；「Erickson」中名来自母系，正文口径为准并注记）
- **生卒**：1912-04-19 生于密歇根州 Ishpeming → 1999-02-25 逝于加州 Lafayette 自宅，享年 86（恰在他发现钚 58 年零 2 天后）
- **国籍**：United States（美国；瑞典移民家庭，家中说瑞典语，母系源自 Pemer 家族）
- **身份**：化学家（chemist）、大学教授（university teacher）、核物理学家（nuclear physicist，infobox occupation）——核化学巨擘
- **家庭**：父 Herman Theodore (Ted) Seaborg、母 Selma Olivia Erickson Seaborg；妹 Jeanette 小两岁；1942 年娶 Helen Griggs（Ernest Lawrence 的秘书——战时分居两地，返程途中在加州 Caliente 临时下车，因小城无市政厅又北上 25 英里到 Pioche，坐邮车完婚，证婚人是书记员与清洁工）；七子女，长子 Peter Glenn 1997 年卒（孪生姐妹 Paulette 婴儿期夭折），另有 Lynne、David、Steve、Eric、Dianne
- **教育轨迹**：Jordan High School（Watts；1929 届榜首）→ UCLA（BA 1933，化学；打工谋生：码头装卸工、Firestone 实验室助理）→ UC Berkeley（MA、PhD 1937）
- **导师**：George Ernest Gibson 与 Gilbert Newton Lewis（infobox「Doctoral advisors」并列两位）
- **博士论文**：*The Interaction of Fast Neutrons with Lead*（1937；文中首创 "nuclear spallation" 一词）
- **研究领域**：核化学（nuclear chemistry）——超铀元素、锕系概念、核医学同位素

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **瑞典移民之子（1912）**：生于 Ishpeming 铁矿区，幼年随家迁洛杉矶县 Home Gardens（后并入 South Gate）；家中说瑞典语，母亲一度劝他去当记账员。
2. **Reid 老师的启蒙**：直到十一年级才爱上科学——Jordan High School 的化学与物理老师 Dwight Logan Reid 点燃了他；1929 年以全班第一毕业。
3. **半工半读的 UCLA 岁月（1929–1933）**：码头装卸工与 Firestone 实验室助理挣出学费；1933 年 UCLA 化学学士；专业化学兄弟会 Alpha Chi Sigma 成员。
4. **伯克利双导师（1933–1937）**：博士论文研究快中子与铅的相互作用，首创 "nuclear spallation" 术语；同时为导师 Lewis 做湿法化学，与其合著三篇酸碱理论论文。
5. **Hahn 的书与「差一点」（1930s）**：研读 Otto Hahn 的《Applied Radiochemistry》深受影响；后闻裂变可能——兴奋又懊恼，因为自己的研究路线本可能先撞见这一发现。
6. **核医学先驱（1937–1938）**：与 John Livingood（合作五年）、Fred Fairbrother 制得铁-59（1937，用于血红蛋白研究）；1938 年共同制得**碘-131**——至今用于甲状腺疾病治疗，多年后据信延长了他母亲的寿命。
7. **接棒 McMillan：钚的诞生（1940–1941）**：McMillan 发现 93 号元素镎后奔赴战时工作，Seaborg 征得同意接手 94 号元素研究；1941 年 2 月经氘轰击铀制得**钚-239**；1941-03-28 与 Emilio Segrè、Joseph W. Kennedy 证明钚**可裂变**——曼哈顿计划路线决策的关键判据；Gilman Hall 307 室 1966 年被定为国家历史地标。
8. **芝加哥冶金实验室（1942–1945）**：1942-04-19（31 岁生日当天）抵芝加哥；1942-08-20 首次分离出可称量的钚-239（9 月 10 日称重）；设计多级化学流程分离浓缩钚，经 Oak Ridge 放大、Hanford 全量产——为内爆弹 Fat Man 供料。
9. **锕系概念（1944–1945）**：把锕系元素排入周期表**镧系之下**的新格局——现代周期表因此重绘为今日形态；进而预言 transactinide、superactinide 系列与「稳定岛」超重核。
10. **十种元素与一百种同位素**：钚、镅、锔、锫、锎、锿、镄、钔、锘、𨭎（seaborgium）十元素的主持或共同发现者；发现超铀元素同位素 100 余种；镅、锔两项**化学元素专利**史无前例——镅用于烟雾探测器，晚年带来可观的专利收入。
11. **1951 诺贝尔化学奖**：与 Edwin McMillan 共享（超铀元素化学）；此后约 50 个荣誉博士学位；《吉尼斯世界纪录》曾载他为《美国名人录》条目最长者。
12. **seaborgium：在世命名第一人（1994/1997）**：106 号元素以他命名——史上**第一个以在世者命名并获官方通过**的元素（曾引发命名争议）；他自述（page.md 英文原句可溯源）："This is the greatest honor ever bestowed upon me—even better, I think, than winning the Nobel Prize..."
13. **公民科学家（1961–1999）**：1958–1961 任伯克利校长第二任（放开校园政治言论禁令，为 1964 自由言论运动铺路）；1961–1971 任美国原子能委员会（AEC）主席——历仕 Truman 至 Clinton 十位总统的核政策顾问；签署 Franck 报告，参与 Limited Test Ban Treaty 谈判团、推动 NPT 与 CTBT；1972 AAAS 主席、1976 美国化学会会长；1980 年用 Bevalac 把数千颗铋-209 原子嬗变为金——「近乎点石成金」但成本不可行；1983 参与 Reagan 时代《A Nation at Risk》教育报告；1998-08-24 在波士顿中风，1999-02-25 于 Lafayette 逝去。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深绯红 deepcrimson） | `#7A1E28` | 核化学的庄重与元素发现的时代重量（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（超铀元素 badgeTU） | `#2E5A9E` | 蓝钚与超铀十元素 |
| 分类色 2（锕系概念 badgeAc） | `#B8860B` | 金锭周期表重排 / 锕系系列 |
| 分类色 3（核医学 badgeMed） | `#1B7A43` | 绿碘-131 / 铁-59 |
| 分类色 4（公共事务 badgeAEC） | `#4A3A6B` | 紫原子能委员会 / 军控外交 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「周期表逐格点亮」——新增的锕系一行。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Through the Darkness** — Audiomachine（文件：`music_audio/inspiring-electronic/14-Trn1cSsY2t8-Audiomachine - Through the Darkness.wav`；**不要复制 wav 文件**）
- **风格**：史诗 / 庄重 / 穿越黑暗的行进感
- **匹配理由**：
  - "穿越黑暗" 匹配其时代——战时保密、冷战阴影中把周期表推进到未知元素
  - "史诗" 匹配体量——十种元素、锕系概念、AEC 十年，一人贯穿半个世纪的原子时代
  - "庄重" 匹配其公民科学家气质——从实验室到条约谈判桌的公共担当
- **时长**：以文件实际时长为准（须 > 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐）

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 周期表的开拓者 / Glenn T. Seaborg 1912–1999 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/出生地/去世地/教育/双导师/领域/荣誉）
03  西博格的一生 — Sanger 式时间线（10 节点：1912→1929→1933→1937→1941→1942→1945→1951→1961→1999）
04  瑞典移民与 Watts (1912–1933) — 表格「时间|事件|结果」
05  伯克利双导师与核医学 (1933–1940) — 表格「对象|产出|意义」+ 公式框：nuclear spallation / 碘-131
06  钚的诞生 (1940–1942) — 表格「问题|方法|结果」+ 公式框：1941-03-28 可裂性判定 · Gilman 307 室
07  芝加哥与曼哈顿计划 (1942–1945) — 表格「阶段|任务|结果」（可称量钚-239 → Hanford 量产）
08  锕系概念 — 表格「旧格局|新格局|意义」+ 公式框：actinide 系列置于 lanthanide 之下的周期表示意
09  十种元素与 seaborgium — 表格「元素|年份|角色」+ 公式框：seaborgium 命名引语原文框
10  1951 诺贝尔化学奖 — 表格「理由|口径|意义」（与 McMillan 共享，超铀元素化学）
11  AEC 与公民科学家 (1958–1971) — 表格「职务|作为|意义」（校长/AEC 主席/LTBT·NPT/两学会会长）
12  铋变金与稳定岛 (1980–1999) — 表格「设想|实验|结果」+ 公式框：Bi-209 → Au-197 嬗变
13  遗产：从镎到 106 号 — 四分类遗产盒 + 公式框：周期表锕系行示意 · 《A Nation at Risk》
14  结尾 — 「他给元素周期表添了一整行，也给科学添了公民的分量。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 获奖理由口径 | page.md 实载 "for 'their discoveries in the chemistry of the first transuranium elements'"；⚠️ McMillan 页面同项无 "first"——**两篇各忠于本人页面**，勿互改；官方口径以诺贝尔官网为准 |
| 本名 | 出生名 Glen Theodore（正文另有 Erickson 中名，母系来源）——11 岁自改拼写 Glenn；勿写成「父母改名」 |
| 博士导师 | infobox「Doctoral advisors」**并列 Gibson 与 Lewis 两位**——勿只写一人；与 Lewis 合作酸碱理论三篇论文 |
| 钚的时间线 | 1941-02 制得 Pu-239；**1941-03-28** 与 Segrè、Kennedy 证明可裂；1942-08-20 首次分离可称量、09-10 称重——三个日期勿混 |
| 死亡日期 | 1999-02-25，逝于 Lafayette 自宅；「发现钚 58 年零 2 天之后」暗示发现日 1941-02-23——页面只明载「February 1941」，勿倒推写死具体发现日 |
| seaborgium | 第一个以在世者命名并获官方通过的元素（第二个是 2016 年 oganesson）；命名曾 "proved controversial"——如实写，勿写成「无争议」 |
| 元素角色 | 钚镅锔锫为 lead discoverer，锎锿镄钔锘𨭎为 co-discoverer——主从勿混 |
| 政治内容 | AEC/Khrushchev 签约照、Nixon/Ehrlichman 冲突、Zalman Shapiro 泄密疑案——Shapiro 段建议一笔带过或略写；LTBT/NPT 军控贡献可正面陈述 |
| 引语 | 三处 page.md 实载英文原句可用：seaborgium 命名感言、"There is a beauty in discovery..."、瑞典方言 toast 自述；除此之外中文引号内禁编造「原话」 |
| 肖像 | `Seaborg_in_lab_-_restoration.jpg`（1950 实验室单人照）优先；与肯尼迪/与 Dixy Lee Ray 合影非肖像照，裁剪须核对图注 |
| 同名区分 | 门生 Geoffrey Wilkinson（infobox「Other notable students」；1973 化学诺奖）与图灵奖侧的 James H. Wilkinson 无关；门生 Joseph W. Kennedy 勿与美国总统 JFK 混淆 |
| 姻亲 | 妻 Helen 是 Lawrence 的秘书、McMillan 之妻 Elsie 的连襟关系（Lawrence 夫人是 Elsie 之妹）——仅背景叙述，姻亲不入库 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q48973 | ✅（复用库内 #2396 stub 回填） |
| name_zh | 格伦·西奥多·西博格 | ✅ |
| name_en | Glenn T. Seaborg | ✅（库内既有精确形式） |
| birth_date | 1912-04-19 | ✅ |
| death_date | 1999-02-25 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | nuclear chemistry（person_field 细分：nuclear chemistry / transuranium elements / actinide concept / nuclear medicine，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 门生 / 共同得主 / 合作者**（★红线：只收 page.md 正文或 infobox 明载的关系）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | George Ernest Gibson | 师→生（博士导师之一） | 1937 伯克利博士（快中子与铅） |
| advisor-student | Gilbert Newton Lewis | 师→生（博士导师之一） | 1930s 合作酸碱理论三篇论文 |
| advisor-student | Ralph A. James | 西博格→学生 | infobox Doctoral students；镅/锔共同发现者（合作者 R.A. James） |
| advisor-student | Joseph W. Kennedy | 西博格→学生 | infobox Doctoral students；1941 共同证明钚可裂 |
| advisor-student | Arthur Wahl | 西博格→学生 | infobox Doctoral students |
| advisor-student | Elizabeth Rauscher | 西博格→学生 | infobox Doctoral students |
| advisor-student | Margaret Melhase | 西博格→学生 | infobox Other notable students |
| advisor-student | Geoffrey Wilkinson | 西博格→学生 | infobox Other notable students；1973 诺贝尔化学奖得主 |
| co-honored | Edwin McMillan | 无向 | 1951 诺贝尔化学奖共同得主；库内 #2387 |
| colleague | Emilio Segrè | 无向 | 1941-03-28 共同证明钚可裂（另有 Kennedy） |
| colleague | John Livingood | 无向 | 1937–1942 五年合作；共同制得铁-59、碘-131 |
| colleague | Albert Ghiorso | 无向 | 多种超铀元素共同发现者；seaborgium 命名的主要推动者 |
| colleague | Ernest Lawrence | 无向 | 伯克利辐射实验室回旋加速器；其秘书 Helen 后成 Seaborg 之妻；库内 #1951 |
| colleague | J. Robert Oppenheimer | 无向 | 伯克利同事；Seaborg 常向他请教物理问题；库内 #355 |
| influence | Otto Hahn | 影响→被影响 | 其教材《Applied Radiochemistry》对 Seaborg 研究方向影响重大；库内 #2055 |
| influence | Frederick Soddy | 影响→被影响 | 承其同位素研究脉络，参与发现 100 余种同位素 |
| spouse | Helen Griggs | 配偶 | 1942 年结婚（Pioche 邮车婚礼），育七子女 |

> **禁入库名单**（page.md 明载但判定为噪声/非入库关系）：Enrico Fermi（同在芝加哥冶金实验室，正文仅「Fermi 组随后将铀-238 转为钚-239」，无直接合作叙述）；John W. Gofman、Raymond W. Stoughton（铀-233 共同鉴定合作者——正文明载但若入库噪声过大，可与 Review 商定；本篇按「三人合作一句带过」处理不入库）；Fred Fairbrother（铁-59 合作者，一次性提及）；Darleane C. Hoffman（引注作者非关系）；Edward J. Lofgren（Pemer 家族谱系趣味，无学术关系）；七名子女（亲属不入库）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1951，与 Edwin McMillan 共享）
- ACS Award in Pure Chemistry（1947）；Member of the National Academy of Sciences（1948）
- Centenary Prize（1956）；Perkin Medal（1957）；Enrico Fermi Award（1959）
- Swedish-American of the Year（1962）；Franklin Medal（1963）
- Willard Gibbs Award（1966）；Priestley Medal（1979）
- Foreign Member of the Royal Society（1985）；Vannevar Bush Award（1988）
- National Medal of Science（1991）；National Inventors Hall of Fame（2005 追授）
- 法国荣誉军团勋章（Knight of the Legion of Honour）；皇家北极星勋章（Royal Order of the Polar Star）
- 约五十个荣誉博士学位；美国哲学学会（1952）、美国艺术与科学院（1958）；AAAS 会士、CSI Pantheon of Skeptics（2011）

## 9. 机构清单

- 教育：Jordan High School（1929）；UCLA（BA 1933）；UC Berkeley（MA、PhD 1937）
- 任职：UC Berkeley（1939 讲师、1941 助理教授、1945 教授；1954–1961 辐射实验室副主任；1958–1961 第二任校长；AEC 后回任 University Professor；Lawrence Hall of Science 主席）；University of Chicago 冶金实验室（1942–1945，曼哈顿计划）；Atomic Energy Commission 主席（1961-03-01 – 1971-08-16，Kennedy 提名、历仕三总统）；AAAS 主席（1972）；美国化学会会长（1976）
- 命名机构：Glenn T. Seaborg Trail（马里兰州 Germantown AEC 总部步道）；Glenn T. Seaborg Center（北密歇根大学）；Glenn T. Seaborg Medal（UCLA）；瑞典裔美国会 Local Lodge Glenn T. Seaborg No. 719（1991）

## 10. 终审清单

- [ ] 生卒 1912-04-19 / 1999-02-25，享年 86，出生地 Ishpeming、去世地 Lafayette
- [ ] 1951 与 McMillan 共享表述准确；「first transuranium elements」口径差异已注记
- [ ] 钚三日期（1941-02 / 1941-03-28 / 1942-08-20）未混；Gilman 307 室地标
- [ ] 锕系概念重排周期表表述准确；十元素主从角色未混
- [ ] seaborgium「在世命名第一人 + 有争议」如实；引语三句均可溯源
- [ ] 双导师 Gibson+Lewis 并列；门生以 infobox 为准；禁入库名单执行
- [ ] 政治内容客观克制（Shapiro 段略写或略过）
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误、溢出达标

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 page.md 逐页对照 Beamer tex 全部事实（页面较长，分段核对）
- [ ] 头像：核对实验室单人照图注
- [ ] 国籍：封面顶部明示美国
- [ ] 引语核对：三处英文原句必须在 page.md 原文找到
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一；周期表示意与公式框排版检查
- [ ] 与化学家侧既有格式（Sanger 黄金骨架）对齐

---

> **名单状态**：由 chem-batch-09 执行；`chemist/generate_20th_century_list.py` 由主控统一收尾，本篇不改动。
