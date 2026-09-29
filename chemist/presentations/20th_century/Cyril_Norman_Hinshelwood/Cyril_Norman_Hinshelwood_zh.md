# Cyril Norman Hinshelwood（西里尔·欣谢尔伍德）立传提示词

> qid=Q48986 · 1897-06-19 – 1967-10-09 · 英国物理化学家 · 20 世纪 · 诺贝尔化学奖（1956，与 Nikolay Semyonov 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Cyril_Norman_Hinshelwood/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 高斯式时间线 + 表格语义化 tabularx + 公式展示框，是本次书写的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/` 已就位；若无真实肖像按 Review-1 流程先补图，全部 404 才允许装饰圆占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{tachometer-alt}\enspace 反应速率的度量者\enspace·\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「链式反应 / 级联」母题——圆点连线分支暗示链传递与分支。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Sir Cyril Norman Hinshelwood（中文惯称：西里尔·诺曼·欣谢尔伍德；OM FRS，1948 年受封爵士）
- **生卒**：1897-06-19 生于伦敦 → 1967-10-09 逝于伦敦家中，享年 70
- **国籍**：United Kingdom（英国）
- **身份**：物理化学家、化学动力学（chemical kinetics）权威；1956 年与苏联的 Semyonov 共享诺贝尔化学奖
- **家庭**：父 Norman Macmillan Hinshelwood 为特许会计师（1905 年去世），母 Ethel Frances née Smith；**终身未婚**
- **教育轨迹**：
  - 幼年随家庭在加拿大受教育，1905 年父亲去世后回伦敦，此后一生住在 Chelsea 同一套公寓
  - Westminster City School → Balliol College, Oxford（牛津大学）
- **导师**：Harold B. Hartley（博士导师，infobox 明载；Hinshelwood 还为其画过肖像，现藏皇家学会）
- **研究领域**：物理化学——化学动力学、链式反应、多相催化（Langmuir–Hinshelwood 机理）、细菌细胞的化学动力学
- **雅趣**：通晓七种古典与现代语言；绘画（牛津风景与牛津人物肖像）、收藏中国瓷器、外国文学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **伦敦—加拿大—切尔西（1897–1905）**：会计之子，幼年在加拿大受教育；丧父回国，Chelsea 公寓住了一辈子。
2. **一战炸药厂化学家（1914–1918）**：战争期间在炸药工厂任化学家——与爆炸物动力学的最初接触。
3. **三一学院导师（1921–1937）**：牛津 Trinity College tutor 十六年，奠基其教学与著述。
4. **两本教科书（1926）**：*Thermodynamics for Students of Chemistry* 与 *The Kinetics of Chemical Change* 同年出版——把动力学的语言系统化。
5. **氢氧爆炸与链式反应**：与 Harold Warris Thompson 研究氢氧爆炸反应，描述链式反应（chain reaction）现象——与苏联 Semyonov 的链反应理论遥相呼应。
6. **细菌细胞的化学动力学（1946）**：*The Chemical Kinetics of the Bacterial Cell* 出版——把动力学带进生物学，成为日后抗生素与治疗剂研究的重要基础；1966 年续作 *Growth, Function and Regulation in Bacterial Cells*。
7. **《物理化学的结构》（1951）**：*The Structure of Physical Chemistry*——2005 年由 OUP 重印为 Oxford Classic Texts。
8. **Langmuir–Hinshelwood 机理**：多相催化中反应物吸附于表面为速控步骤的机理以他命名；另有 Lindemann–Hinshelwood 机理。
9. **第二任 Dr Lee's Professor（1937）**：牛津化学讲席教授；1964–67 任帝国理工高级研究员。
10. **皇家学会主席（1955–1960）**：FRS 1929；先后任 Chemical Society、Faraday Society、Royal Society、Classical Association 主席——罕见的"四会主席"。
11. **1956 诺贝尔化学奖（共享）**：与苏联 Nikolay Semyonov 共享，理由 "for their researches into the mechanism of chemical reactions"；诺奖演讲 1956-12-11《Chemical Kinetics in the Past Few Decades》。
12. **荣誉大满贯**：Meldola 1923、Liversidge 1939、Davy 1942、Royal Medal 1947、Longstaff 1948、Faraday Lectureship 1953、Leverhulme 1960、Copley 1962、Dalton 1966；爵士（1948）、OM（1960）。
13. **文物级奖章（1968–2017）**：身后其诺奖奖章 1968 年由遗产方售出、1976 年转手 15,000 美元、2017 年拍卖 128,000 美元——科学纪念品的世纪行情。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深藏青 deepnavy） | `#1E3A5F` | 动力学的严谨与牛津的沉稳（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（化学动力学 badgeKinetics） | `#B4632A` | 琥珀速率方程 / 链式反应 |
| 分类色 2（多相催化 badgeCatalysis） | `#2E5A9E` | 蓝 Langmuir–Hinshelwood 机理 |
| 分类色 3（细菌动力学 badgeBacteria） | `#1B7A43` | 绿细胞生长动力学 |
| 分类色 4（学术领袖 badgeSociety） | `#6E4E7E` | 紫皇家学会主席 / 四会主席 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），圆点链式分支呼应「链引发 → 传递 → 分支」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Falling Apart** — Michael FK & Andy Leech（文件：`music_audio/inspiring-electronic/03-qtNSLNUd1VE-Michael FK & Andy Leech - Falling Apart.wav`；勿复制 wav，视频阶段直接引用路径）
- **风格**：忧郁弦乐 / 碎裂感 / 克制的戏剧性
- **匹配理由**：
  - "碎裂" 匹配其科学母题——爆炸、分解、链式断裂：反应动力学的本质正是旧键"分崩离析"
  - 克制的戏剧性匹配其人格——七种语言、绘画与瓷器的绅士化学家，叙事宜静水深流
  - 忧郁基调呼应其身后意象——终身未婚、奖章流拍又天价，一部安静的世纪尾声
- **时长**：以实际文件为准，视频合成用 ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 反应速率的度量者 / Cyril Norman Hinshelwood 1897–1967 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  欣谢尔伍德的一生 — 时间线（10 节点：1897→1905→1914→1921→1926→1937→1946→1951→1956→1967）
04  早年：从加拿大到切尔西 (1897–1914) — 表格「时间|事件|结果」
05  一战炸药厂与牛津讲席 (1914–1937) — 表格「时间|事件|结果」
06  动力学双书 (1926) — 表格「著作|内容|影响」+ 公式框：速率常数 Arrhenius 型 k=Ae^(-Ea/RT)
07  氢氧爆炸与链式反应 — 表格「体系|现象|解释」+ 公式框：链分支示意
08  细菌细胞的化学动力学 (1946) — 表格「对象|方法|意义」
09  Langmuir–Hinshelwood 机理 — 表格「步骤|速控|对手机理」+ 公式框：表面吸附速控示意
10  1956 诺贝尔化学奖 — 与 Semyonov 共享、理由原文、双城记（牛津 vs 莫斯科）
11  四会主席与荣誉大满贯 — 「类别|代表|意义」表格 + itemize 荣誉清单
12  绅士化学家 — 七种语言 / 绘画（Hartley 肖像藏皇家学会）/ 中国瓷器 / 终身未婚
13  遗产 — 动力学教科书谱系（Laidler 等）+ 奖章拍卖插曲 + 命名机理沿用至今
14  结尾 — 「万物皆有其速，而他为其立法。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1956 诺奖 | **共享**（与 Nikolay Semyonov）；官方措辞 "for their researches into the mechanism of chemical reactions"——勿写"独享"或"链反应全归他"（分支链理论主体在 Semyonov） |
| 两人分工 | 页面对 Hinshelwood 的定位是"反应机理研究"（氢氧爆炸链反应、动力学方法），Semyonov 是"化学链反应理论"（分支链/燃烧）——勿把两人工作写混 |
| 生卒日 | 1897-06-19 / 1967-10-09（逝于家中）——享年 70 |
| 博士导师 | Harold B. Hartley（infobox 与正文两处明载）——勿与 Harold Warris Thompson（氢氧爆炸合作者）混淆，两位 Harold 勿串 |
| 诺奖演讲日期 | 1956-12-11《Chemical Kinetics in the Past Few Decades》——勿写 12-10 |
| 学生口径 | infobox Doctoral students 仅 Sydney Brenner、Alan Eddy、John E. M. Midgley 三人；Keith J. Laidler 在 "Other notable students (postdoc)"——Brenner 后成分子生物学诺奖得主（2002），勿写"化学诺奖门生" |
| 获奖 | 必须用页面口径 "second Dr. Lee's Professor"；勿写"首任" |
| 未婚 | 页面明载 never married——禁编造配偶或子嗣 |
| 语言 | "fluent in seven classical and modern languages"——勿写成"精通七门外语"以外的具体清单（页面未列明） |
| 奖章拍卖 | 1968 遗产售出 → 1976 $15,000 → 2017 $128,000——三个数字与年份勿混 |
| 获奖时机构 | 牛津（Dr Lee's Professor）；1964–67 才转帝国理工 senior research fellow——勿写"帝国理工获奖" |
| 引语口径 | 本地页面**无直接引语**——全篇用间接转述，Wikiquote 链接内容不作为事实来源 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q48986 | ✅ |
| name_zh | 西里尔·欣谢尔伍德 | ✅ |
| name_en | Cyril Norman Hinshelwood | ✅ |
| birth_date | 1897-06-19 | ✅ |
| death_date | 1967-10-09 | ✅ |
| nationality | United Kingdom | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | physical chemistry（person_field 细分：chemical kinetics / physical chemistry / heterogeneous catalysis / reaction network theory，带 rank） | ✅ |

## 7. 社会关系入库清单

**师长 / 门生 / 合作者 / 共同得主**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Harold B. Hartley | 师→生（博士导师） | 牛津；Hinshelwood 后为其绘肖像（藏皇家学会） |
| advisor-student | Sydney Brenner | Hinshelwood → 学生 | infobox Doctoral students；后获 2002 诺贝尔生理学或医学奖 |
| advisor-student | Alan Eddy | Hinshelwood → 学生 | infobox Doctoral students |
| advisor-student | John E. M. Midgley | Hinshelwood → 学生 | infobox Doctoral students |
| other | Keith J. Laidler | 无向 | 博士后（infobox Other notable students），后为动力学教科书名家 |
| colleague | Harold Warris Thompson | 无向 | 合作研究氢氧爆炸反应、描述链式反应现象 |
| co-honored | Nikolay Semyonov | 无向 | 1956 诺贝尔化学奖共同得主 |

> **禁入库名单**（页面无载或仅语境提及）：Herbert Blakiston（仅为其画像对象）、Trinity College/Oxford 无关自然人；页面未载其父母之外的任何亲属。共同得主方向须与 Semyonov 侧 yaml 互指一致（双方均用全名 Cyril Norman Hinshelwood / Nikolay Semyonov）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1956，与 Semyonov 共享）
- Meldola Medal and Prize（1923）；Liversidge Award（1939）
- Davy Medal（1942）；Royal Medal（1947）
- Longstaff Prize（1948）；Faraday Lectureship Prize（1953）
- Leverhulme Medal（1960）；Copley Medal（1962）；Dalton Medal（1966，曼彻斯特文学哲学学会）
- Knight Bachelor（1948）；Order of Merit（1960）
- FRS（1929）；Royal Society 会长（1955–1960）
- Chemical Society / Faraday Society / Classical Association 会长；Manchester Lit & Phil 荣誉会员（1960）
- 美国艺术与科学院、美国国家科学院、美国哲学学会外籍院士

## 9. 机构清单

- 教育：加拿大（幼年）、Westminster City School、Balliol College, Oxford
- 任职：一战炸药厂化学家；Trinity College, Oxford tutor（1921–1937）；Dr Lee's Professor of Chemistry, Oxford（1937–，第二任）；Imperial College London 高级研究员（1964–1967）
- 政务：英国政府多个科学顾问委员会

## 10. 终审清单

- [ ] 生卒 1897-06-19 / 1967-10-09（享年 70），生卒地均为伦敦
- [ ] 1956 共享（Semyonov）、理由用官方原文口径；两人工作分工不混
- [ ] 博士导师 Harold B. Hartley；合作者 Harold Warris Thompson——两位 Harold 不串
- [ ] 博士生三人 + Laidler postdoc 口径准确
- [ ] 终身未婚、七种语言、绘画与瓷器表述准确
- [ ] 奖章拍卖三段数字准确（1968/1976/2017）
- [ ] 全篇无直接引语（页面无载）
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Cyril_Norman_Hinshelwood/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：`images/` 肖像就位与图注核对；404 则 REST API 查 infobox 原图
- [ ] 国籍：封面顶部明示英国
- [ ] 引语核对：页面无直接引语——确认全篇为间接转述
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 黄金骨架）对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾，本提示词不改动该文件。
> **数据入库**：yaml 见 `MySQL/data/Cyril_Norman_Hinshelwood.yaml`（新建记录 NEW，含 4 fields / 7 relations）。
