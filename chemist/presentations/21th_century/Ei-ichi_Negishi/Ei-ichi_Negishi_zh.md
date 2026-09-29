# Ei-ichi Negishi（根岸英一）立传提示词

> qid=Q105927 · 1935-07-14 – 2021-06-06 · 日本化学家 · 21 世纪 · 诺贝尔化学奖（2010，与 Richard F. Heck、Akira Suzuki 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Ei-ichi_Negishi/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次执行的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像取 `images/`；infobox 2010 年照片可用；若无真实肖像则用装饰圆占位，图注注明）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 有机锌偶联的建筑师\enspace·\enspace 日本 · 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「有机锌试剂 / C–C 键」母题——离散圆点暗示金属试剂与卤代物在催化剂牵线下的两两相接。
5. **表格语义化 + 公式框**（★ Sanger 版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），Negishi 偶联通式（有机锌 + 有机卤，Pd/Ni 催化 → C–C 键）即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Ei-ichi Negishi（日文 根岸 英一；中文惯称：根岸英一）
- **生卒**：1935-07-14 生于满洲国新京（今中国长春）→ 2021-06-06 逝于美国印第安纳州 Indianapolis，享年 85
- **国籍**：United States / Japan（frontmatter 双国籍；infobox 出生叙事为日侨家庭）
- **身份**：化学家；普渡大学 Herbert C. Brown 杰出教授；Negishi-Brown 研究所所长
- **家庭**：父任职南满洲铁道；1945-11 战后举家迁回日本；1959 年娶大学合唱团相识的 Sumire Suzuki（2018 年意外去世），两女；爱钢琴与指挥（2015 Pacifichem 闭幕式曾指挥乐队）
- **教育轨迹**：少年随父辗转哈尔滨（8 年）→ 仁川 → 京畿（今首尔）→ 日本；湘南高中 → 东京大学（1958 毕业）→ 富布莱特奖学金赴美 → University of Pennsylvania（PhD 1963，师从 Allan R. Day）
- **导师**：Allan R. Day（博士导师）；Herbert C. Brown（Purdue 博士后导师，1979 诺贝尔化学奖）
- **博士论文**：*Basic cleavage of arylsulfonamides, the synthesis of some bicyclic compounds derived from piperazine which contain bridgehead nitrogen atoms*（1963）
- **研究领域**：有机化学——过渡金属催化偶联（有机锌）、有机锆化学、ZACA 反应

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **满洲出生的日侨之子（1935）**：生于新京（今长春），随父辗转哈尔滨、仁川、京畿——童年在漂泊中度过。
2. **战后归日与跳级（1945–1953）**：1945-11 迁回日本；成绩优异跳级入名校湘南高中。
3. **17 岁入东京大学（1953）**：1958 毕业后进入帝人（Teijin）做高分子化学研究。
4. **富布莱特赴美（1960）**：Fulbright–Smith–Mundt Fellowship 出国，UPenn 读博（1963，Allan R. Day 门下）；1962–63 获 UPenn Harrison Fellowship。
5. **无法回日本任教的转折（1966）**：本想回日本大学任教却找不到职位，从帝人辞职、赴普渡做博士后——人生最大弯路成就一生事业。
6. **Brown 门下（1966–1972）**：随 1979 年诺奖得主 Herbert C. Brown 做博士后与讲师——有机硼与金属试剂的炼狱式训练。
7. **雪城大学助理教授（1972）**：在此开启毕生的过渡金属催化反应研究，1979 升副教授。
8. **重返普渡（1979）**：同年正教授；后任 Herbert C. Brown 杰出教授、Negishi-Brown 研究所所长。
9. **Negishi 偶联**：有机锌化合物与有机卤化物在钯或镍催化下缩合成 C–C 键产物——三大钯催化偶联之一。
10. **不申请专利的选择**：自述"如果不申请专利，所有人都能轻易使用我们的成果"（page.md 载原文转述）——技术 freely 扩散到制药业，据估计制药业四分之一的反应用到该技术。
11. **Negishi 试剂与 ZACA**：二氯二茂锆还原所得 Zr(C₅H₅)₂ 称 Negishi 试剂（氧化环化用）；另发展 ZACA 反应与有机铝/有机锆偶联。
12. **2010 诺贝尔化学奖**：与 Heck、Suzuki 共享 "for palladium catalyzed cross couplings in organic synthesis"；同年获日本文化勋章与文化功劳者。
13. **严谨的门风与晚年**：论文 400+ 篇，以实验室记录严整著称（要求学生先评估粗反应混合物再分离）；2019 退休；2021-06-06 于 Indianapolis 去世，享年 85，家属计划 2022 年归葬日本。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深紫 deepviolet） | `#5B2A86` | 有机锌试剂的深紫基调 / 金属有机的神秘（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（Negishi 偶联 badgeNeg） | `#2E5A9E` | 蓝有机锌 × 有机卤，Pd/Ni 催化 |
| 分类色 2（金属试剂谱系 badgeZr） | `#1B7A43` | 绿 Negishi 试剂 / ZACA / 有机铝 |
| 分类色 3（制药影响 badgePharma） | `#D97B29` | 琥珀制药业 1/4 反应 / 无专利 |
| 分类色 4（师承 badgeBrown） | `#C0395B` | 玫瑰 Brown 门下 / Tour 门生 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「两两相接的偶联节点」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Mirage** — Notan Nigres（文件 `music_audio/inspiring-electronic/04-5gcb94jhG1I-...Mirage (Audio).wav`；不要复制 wav 文件）
- **风格**：缥缈而克制 / 电子氛围 / 渐进式律动
- **匹配理由**：
  - "Mirage"（海市蜃楼）匹配其人生弯路——想回日本任教而不得的"幻影"，转过身才在普渡遇见真正的事业
  - 缥缈渐进的氛围匹配有机锌试剂"温和而不张扬"的气质——三大偶联中最低调的一支
  - 渐进律动匹配从东京到宾州到印第安纳的一路向西
- **时长**：以实际曲目时长为准，ffmpeg `-shortest` 自动对齐 15 页 × 7 秒 ≈ 105 秒

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 有机锌偶联的建筑师 / Ei-ichi Negishi 1935–2021 + 四色 badge + 右上头像 + 国籍行（日本 · 美国）
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  根岸的一生 — Sanger 式时间线（10 节点：1935→1945→1958→1960→1963→1966→1972→1979→2010→2021）
04  满洲与战后岁月 (1935–1953) — 表格「时间|地点|结果」
05  东大与帝人 (1953–1966) — 表格「阶段|方向|结果」
06  富布莱特与 UPenn (1960–1963) — 表格「奖学金|方向|结果」+ 公式框：芳基磺酰胺碱裂解 / 双环哌嗪合成
07  普渡：Brown 门下 (1966–1972) — 表格「职位|训练|结果」
08  雪城与重返普渡 (1972–1979) — 表格「时期|转向|结果」
09  Negishi 偶联 — 表格「问题|方法|结果」+ 公式框：R–ZnX + R'–X，Pd/Ni 催化 → R–R'
10  无专利的哲学家 — 表格「选择|理由|影响」+ 公式框：制药业约 1/4 反应使用该技术
11  Negishi 试剂与 ZACA — 表格「体系|反应|用途」+ 公式框：Zr(C₅H₅)₂
12  2010 诺贝尔化学奖 — 公式框：官方理由 "for palladium catalyzed cross couplings in organic synthesis"；文化勋章 / 文化功劳者
13  家人与晚年 — 四分类遗产盒（Sumire 与 2018 / 两女 / 钢琴与指挥 / 2021 谢幕）
14  结尾 — 「把金属的手，借给碳与碳的相逢。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2010 诺奖口径 | 与 Heck、Suzuki **三人共享**；官方理由原文 "for palladium catalyzed cross couplings in organic synthesis"（page.md 明载）；勿写"独享" |
| 年代分工 | Heck 反应 1960s 末；Negishi（有机锌）与 Suzuki（有机硼）偶联 1970s——三大偶联**试剂路线不同**，勿混写 |
| 出生地 | 生于满洲国新京（今长春）——如实写"今中国长春"，勿写"日本出生"；1945-11 战后迁回日本；此后行程（哈尔滨/仁川/京畿）按正文时间轴 |
| 国籍 | frontmatter 双国籍 United States / Japan；infobox 无国籍行——封面写"日本 · 美国"双籍，勿只写其一 |
| 博士后导师 | Herbert C. Brown（Purdue 1966–）是**博士后**导师；博士导师是 UPenn 的 Allan R. Day——两行并列勿混；Brown 1979 年诺奖 |
| 专利 | "不申请专利"的理由为 page.md 转述原句（"If we did not obtain a patent, we thought that everyone could use our results easily."）——可引用原文；"制药业 1/4 反应"是"据估计"（estimated），须保留估计口径 |
| 无关诺奖者 | 南部阳一郎 2010-11-12 出席庆祝会（同乡·东大校友·美国中西部日本诺奖得主）——**庆祝事件不入库**，正文亦不必展开 |
| 妻子 | Sumire Suzuki（婚前姓 Suzuki，与共同得主铃木章**毫无亲属关系**——三重同名陷阱！）；1959 结婚；2018 年 3 月走失意外去世（低体温症，有帕金森病与高血压既往史）——**叙述须克制简短**（一两句），禁猎奇化展开 |
| 门生 | infobox Doctoral students 仅 **James M. Tour** 一人；其余人物页面无载不入库 |
| 死亡地点 | 逝于 Indianapolis, Indiana；美国境内未办葬礼，家属计划 2022 年归葬日本——勿写"葬于日本"已成事实 |
| 引语红线 | 可引原文仅"不申请专利"理由一句；其余叙述均为间接转述 |
| 奖项年份 | A. R. Day Award 1996 / 化学会奖 1997 / McCoy 1998 / ACS 有机金属奖 1998 / 文化勋章 2010——年份与 frontmatter 交叉核对，勿串年 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q105927 | ✅（新建 #NEW） |
| name_zh | 根岸英一 | ✅ |
| name_en | Ei-ichi Negishi（page.md 规范名） | ✅ |
| birth_date | 1935-07-14 | ✅ |
| death_date | 2021-06-06 | ✅ |
| nationality | United States（rank 0）+ Japan（rank 1） | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | organic chemistry（person_field 细分：cross-coupling / organozinc chemistry / organometallic chemistry / organic synthesis，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 同事 / 共同得主 / 门生 / 家人**（★红线：只收 page.md 正文或 infobox 明载的关系）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Allan R. Day | 师→生（博士导师） | UPenn PhD 1963（1996 年其获奖项 A. R. Day Award 同名，仅并列事实） |
| advisor-student | Herbert C. Brown | 师→生（博士后导师） | Purdue 1966–1972；1979 诺贝尔化学奖（库内已有记录） |
| advisor-student | James M. Tour | 生→师（学生） | infobox Doctoral students |
| co-honored | Richard F. Heck | 无向 | 2010 诺贝尔化学奖共同得主 |
| co-honored | Akira Suzuki | 无向 | 2010 诺贝尔化学奖共同得主 |
| spouse | Sumire Suzuki | 无向 | 1959 结婚；2018 意外去世 |

> **禁入库名单**（事件性提及或页面无载，不入库）：Yoichiro Nambu（2010-11-12 庆祝会出席，同乡校友事件）；Teijin / Syracuse 等机构同事未具名；两女未具名；学生群体仅收 Tour 一人。

## 8. 奖项清单

- Nobel Prize in Chemistry（2010，与 Heck / Suzuki 共享）
- A. R. Day Award, ACS Philadelphia Section（1996）
- Chemical Society of Japan Award（1997）
- Herbert N. McCoy Award（1998）
- American Chemical Society Award for Organometallic Chemistry（1998）
- ACS Award for Creative Work in Synthetic Organic Chemistry（2010）
- Alexander von Humboldt Senior Researcher Award（1998–2000）
- Sigma Xi Award, Purdue University（2003）；Yamada–Koga Prize（2007）；Charles University Gold Medal（2007）
- Sir Edward Frankland Prize Lectureship（2000）
- Fray International Sustainability Award, SIPS（2015）
- Person of Cultural Merit（2010）；Order of Culture 文化勋章（2010）
- Sagamore of the Wabash（2011）；Order of the Griffin, Purdue（2011）
- Guggenheim Fellowship（1986）；Fulbright–Smith–Mundt Fellowship（1960–61）；Harrison Fellowship, UPenn（1962–63）

## 9. 机构清单

- 教育：湘南高中 → University of Tokyo（1958）→ University of Pennsylvania（PhD 1963）
- 产业：Teijin（实习起，高分子化学，1958–1966）
- 博士后/讲师：Purdue University（1966 博士后；1968–1972 讲师）
- 任职：Syracuse University 助理教授（1972）/ 副教授（1979）→ Purdue University 正教授（1979–）；Herbert C. Brown Distinguished Professor；Negishi-Brown Institute 所长；2019 退休
- 名誉：UPenn 荣誉理学博士（2011）；美国艺术与科学院 Fellow（2011）；美国国家科学院外籍院士（2014）；RSC 荣誉会士（2012）

## 10. 终审清单

- [x] 生卒 1935-07-14 / 2021-06-06，享年 85，出生地新京（今长春）、去世地 Indianapolis
- [x] 2010 三人共享（Heck / Suzuki）表述准确；诺奖理由英文原文口径正确
- [x] 双导师并列：Day（博士）/ Brown（博士后）——方向与年代无误
- [x] Sumire Suzuki 与 Akira Suzuki 同名区分明确（夫妻 vs 共同得主）
- [x] "制药业 1/4 反应"保留估计口径；无专利理由为页面原句
- [x] 妻子 2018 意外去世叙述克制简短；Nambu 事件不入库
- [x] 引语红线：仅"不申请专利"一句原文
- [x] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Ei-ichi_Negishi/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/` 内真实肖像已就位，否则装饰圆占位并注明
- [ ] **国籍**：封面顶部明示"日本 · 美国"双籍
- [ ] **引语核对**：中文引号内原话必须能在 page.md 找到；无原话一律改间接转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 2010 另两篇（Heck、Suzuki）口径互查：共享得主名、诺奖理由、年代分工一致
