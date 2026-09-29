# Omar M. Yaghi（奥马尔·亚吉）立传提示词

> qid=Q743252 · 1965-02-09 生于约旦安曼 · 在世 · 美国化学家（约旦/沙特/美国三重公民）· 诺贝尔化学奖（2025，与 Richard Robson、Susumu Kitagawa 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Omar_M._Yaghi/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：对齐 `chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}` 黄金骨架（表格语义化 tabularx + 公式展示框 + 时间线页 + 身份信息页）。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/Omar_M._Yaghi,_2025_Nobel_laurate_in_chemistry.jpg`，2025 诺贝尔演讲个人照，已就位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{grid-4}\enspace 网状化学的开创者\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（عمر مُؤنس ياغي / Omar Mwannes Yaghi）、国籍（三重）、出生地、教育、博士导师、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和网格方阵（稀疏方形网格点阵），呼应「网状化学 / 框架格点」母题。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如 MOF-5、SBU、COF-5 结构式与比表面积。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`；中文名「奥马尔·亚吉」。

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Omar Mwannes Yaghi（عمر مُؤنس ياغي；中文惯称：奥马尔·亚吉）
- **生卒**：1965-02-09 生于约旦安曼（在世）
- **国籍**：约旦 + 美国 + 沙特三重公民（infobox Citizenship: Jordanian, Saudi, American；2021 年获沙特国籍）——叙事口径以美国为主
- **身份**：化学家、大学教师；网状化学（reticular chemistry）开创者
- **家庭**：出身巴勒斯坦难民家庭——1948 年阿以战争期间从雅法与耶路撒冷之间的 Masmiya（Al-Masmiyya al-Kabira）逃亡至安曼；幼年全家多个孩子挤住一间房、房中还养着牲畜、清洁水匮乏
- **教育轨迹**：
  - 15 岁（父辈鼓励、几乎不懂英语）赴美
  - 1983 Hudson Valley Community College AS（数学与科学）
  - 1985 State University of New York at Albany 化学学士
  - 1990 University of Illinois at Urbana-Champaign 博士（论文：非水介质中多氧钒酸盐的合成、结构与反应性）
- **导师**：博士导师 Walter G. Klemperer（UIUC）；博士后导师 Richard H. Holm（Harvard，NSF 博士后 1990–1992）
- **职业轨迹**：Arizona State University 助理教授（1992–1998）→ University of Michigan Robert W. Parry 讲席教授（1999–2006）→ UCLA Christopher S. Foote 讲席教授兼 Irving and Jean Stone 物质科学讲席（2007–2012）→ UC Berkeley James and Neeltje Tretter 讲席教授（2012–2026，2025-05 晋升 University Professor——加州大学系统最高荣誉）
- **研究领域**：网状化学——MOFs、COFs、ZIFs、分子编织；清洁能源应用（储氢/储甲烷、碳捕集、沙漠空气取水）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **1965 年生于安曼**：巴勒斯坦难民家庭之子，童年与牲畜同屋、取水困难——「缺水」成为其日后空气取水研究的远因。
2. **15 岁孤身赴美（1980）**：几乎不懂英语，从社区学院 Hudson Valley 读起。
3. **社区学院到名校（1983–1990）**：AS → SUNY Albany 学士 → UIUC 博士（Klemperer 组，多氧钒酸盐）。
4. **Harvard 博士后（1990–1992）**：NSF 博士后研究员，师从无机化学家 Richard H. Holm。
5. **1995 强键结晶突破**：学界公认「化学上不可行」的设想被实现——用强键（金属离子 + 羧酸根等带电有机连接体）成功结晶金属有机结构，网状化学诞生。
6. **1998 次级构建单元（SBUs）**：引入金属-羧酸簇作为 SBU，构筑坚固且永久多孔的框架，并由气体吸附等温线证实。
7. **1999 MOF-5**：实现超高孔隙率，MOF 由实验室奇物变成可设计的材料平台——本批三人中「系统化与命名普及」的代表。
8. **2005 COF 开创**：发表共价有机框架开创性论文，首批二维 COF（COF-1 / COF-5），B–C–O 强共价键骨架，孔径 7–27 Å。
9. **2007 三维 COF 首次实现**：突破长期实践与概念障碍。
10. **ZIFs 与分子编织**：开创沸石咪唑酯框架设计合成；实现首个原子分子尺度编织材料 COF-505。
11. **应用版图**：储氢/储甲烷、碳捕集、沙漠空气取水（低品位热驱动）；2000–2010 年全球被引第二的化学家（Thomson Reuters 口径）。
12. **创业与转身（2020–2026）**：2020 创办 Atoco（碳捕集与空气取水）、2021 共同创办 H2MOF（储氢）；2026-07 离开 UC Berkeley，赴清华大学领导 AI 材料科学研究所（Yaghi Science Initiative）。
13. **2025 诺贝尔化学奖**：与 Robson、Kitagawa 共享；同年当选中国科学院外籍院士、Princeton 荣誉博士。

## 3. 配色方案（主色 + 强调 + 分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（森林绿 forestgreen） | `#1E5631` | 网状框架的秩序与生长（表头 / 公式文本） |
| 强调色（香槟金，coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（网状化学 badgeRetic） | `#2E5A9E` | 蓝强键结晶 / 连接体设计 |
| 分类色 2（MOF badgeMOF） | `#1B7A43` | 绿 MOF-5 / SBU / 永久多孔 |
| 分类色 3（COF/ZIF badgeCOF） | `#D97B29` | 琥珀共价框架 / 分子编织 |
| 分类色 4（人生轨迹 badgePath） | `#C0395B` | 玫瑰安曼→社区学院→伯克利 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和网格方阵（稀疏方形格点，四档大小错落），暗示网状化学的周期性框架格点。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**With Me** — Alex-Productions（文件 `music_audio/alex-productions/83-DXAblXgCK-k-With-Me.wav`；不要复制 wav 到本目录）
- **风格**：温暖 / 同行 / 逆风生长的陪伴感
- **匹配理由**：
  - "同行" 匹配其人生弧线——从与牲畜同屋的难民儿童到诺奖讲台，一路有师友相伴（Klemperer、Holm）
  - "温暖" 匹配其研究志业——把「缺水」的童年记忆变成「沙漠空气取水」的技术
  - "逆风生长" 匹配 15 岁孤身赴美、从社区学院起步的轨迹
- **时长**：以实际曲目时长为准，ffmpeg `-shortest` 自动对齐 15 页 × 7 秒

## 4. Slide 规划（15 页，00–14）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 网状化学的开创者 / Omar M. Yaghi 1965– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍三重/教育/博士导师/领域/现职/荣誉）
03  亚吉的一生 — 时间线（10 节点：1965→1980→1983→1990→1995→1998→1999→2005→2012→2025）
04  安曼童年与赴美 (1965–1983) — 表格「时间|事件|结果」
05  求学之路 (1983–1992) — 表格「阶段|导师|结果」+ 公式框：多氧钒酸盐
06  1995 强键结晶 — 表格「成见|突破|结果」+ 公式框：金属离子 + 有机连接体
07  SBU 与 MOF-5 (1998–1999) — 表格「问题|方法|结果」+ 公式框：MOF-5 超高孔隙率
08  COF/ZIF 与分子编织 (2005–) — 表格「框架|键型|结果」+ 公式框：COF-5 结构与比表面积
09  2025 诺贝尔化学奖 — 表格「三人|方向|分工」（Robson 概念 / Kitagawa 柔性 / Yaghi 系统化）
10  应用版图：从储氢到取水 — 四分类应用盒 + 公式框：2000–2010 被引第二化学家
11  创业与荣誉年表 — 高斯式「类别|代表|意义」表格（Wolf 2018 / Balzan 2024 / 诺奖 2025 / Atoco / H2MOF）
12  从伯克利到清华 (2026) — 流程图页（只写事实）
13  遗产：把框架装进世界 — 公式框 + 总结
14  结尾 — 「把分子连成框架，让框架盛下清水与未来。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 国籍口径 | 三重公民：Jordanian + Saudi + American（2021 获沙特国籍）；叙事以 **American** 为主、其余按实载并列——勿只写美国 |
| 巴勒斯坦背景 | 按 page.md 中性实写：巴勒斯坦难民家庭、1948 年战争逃离 Masmiya；**不加政治评论、不展开阿以冲突叙事** |
| 2026 赴清华 | 只写事实（2026-07 离开 UC Berkeley，领导清华 AI 材料研究所、创办 Yaghi Science Initiative）；页面中 "Analysts and media outlets characterized..." 的地缘评论段**禁转述禁引用** |
| MOF 首创归属 | MOF 是配位聚合物的子类（IUPAC 口径，1959 年首报配位聚合物；Tomic 1965、Hoskins & Robson 1989 皆早于 Yaghi）——Yaghi 的贡献是**强键结晶（1995）、SBU（1998）、MOF-5（1999）与系统化普及**，勿写「发明 MOF 概念」 |
| 三人分工 | Robson（1990 前驱性概念）/ Kitagawa（柔性多孔）/ Yaghi（MOF-5 等系统化与命名普及）——勿混 |
| 2025 获奖理由 | 页面口径 "for this work"（指 MOF 与网状化学）；官方完整英文原句页面无载，**禁止杜撰整句** |
| 被引排名 | 「2000–2010 全球被引第二化学家」须注明 **Thomson Reuters 分析**口径 |
| 数字口径 | MOF-177 比表面积 5640 m²/g、COF-108 密度 0.17 g·cm⁻³、COF-1/5 比表面积 711/1590 m²/g——引用时逐项核对，勿互换 |
| 家庭细节 | 幼年「与牲畜同屋、清洁水匮乏」为页面明载，可用但保持克制；妻离子女页面无载**禁写** |
| 生年月日 | 1965-02-09，安曼——metadata 与 infobox 一致 |
| 全名 | Omar **Mwannes** Yaghi（عمر مُؤنس ياغي）——中间名勿写错 |
| 同名区分 | 对手方规范名 **Richard Robson**、**Susumu Kitagawa**——yaml/关系表必须用这两形式，防分裂 stub |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q743252 | ✅ |
| name_zh | 奥马尔·亚吉 | ✅ |
| name_en | Omar M. Yaghi | ✅ |
| birth_date | 1965-02-09 | ✅ |
| death_date | （在世，留空） | ✅ |
| nationality | United States（rank 0）+ Jordan（rank 1，出生于安曼）+ Saudi Arabia（rank 2，2021 年授予） | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | reticular chemistry / metal-organic frameworks / covalent organic frameworks / organometallic chemistry（person_field 带 rank） | ✅ |
| has_biography | false（立传完成后再置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 共同得主**（全部为 page.md 正文或 infobox 明载）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Walter G. Klemperer | 师→生（博士导师） | UIUC 博士（1990，多氧钒酸盐） |
| advisor-student | Richard H. Holm | 师→生（博士后导师） | 1990–1992 Harvard NSF 博士后 |
| co-honored | Richard Robson | 无向 | 2025 诺贝尔化学奖共同得主 |
| co-honored | Susumu Kitagawa | 无向 | 2025 诺贝尔化学奖共同得主 |

> **禁入库名单**：E. A. Tomic（文献史提及 1965 年研究，非个人关系）；Hoskins（系 Robson 合作者，与 Yaghi 无个人关系记载）；Tsinghua/UC 各机构同事未具名。metadata.json 与正文 infobox 一致，无额外 metadata-only 人名。

## 8. 奖项清单（节选，全表见 page.md Honors）

- Solid State Chemistry Award, ACS & Exxon（1998）
- Sacconi Medal, Italian Chemical Society（2004）
- MRS Medal / Newcomb Cleveland Prize / DOE Hydrogen Program Award（2007）
- ACS Chemistry of Materials Award / Izatt-Christensen International Award（2009）
- RSC Centenary Prize（2010）
- King Faisal International Prize in Chemistry / Mustafa Prize（2015）
- Albert Einstein World Award of Science（2017）
- BBVA Foundation Frontiers of Knowledge Award / Wolf Prize in Chemistry（2018）
- Gregori Aminoff Prize（2019）
- Wilhelm Exner Medal（2023）
- Tang Prize / Balzan Prize / Ernest Solvay Prize（2024）
- Nobel Prize in Chemistry（2025，三人共享）
- IUPAC-Soong Prize / Von Hippel Award / Princeton 荣誉博士（2025）
- 外籍会士与院士：美国文理科学院会士、美国国家科学院院士、德国 Leopoldina 院士、中国科学院外籍院士（2025）

## 9. 机构清单

- 教育：Hudson Valley Community College（AS 1983）、SUNY Albany（BS 1985）、University of Illinois Urbana-Champaign（MS、PhD 1990）
- 博士后：Harvard University（1990–1992，NSF fellow，Richard H. Holm 组）
- 任职：Arizona State University（1992–1998）→ University of Michigan（Robert W. Parry Professor，1999–2006）→ UCLA（2007–2012）→ UC Berkeley（2012–2026，Tretter Chair；2025 University Professor）
- 兼任：Lawrence Berkeley National Laboratory 附属科学家、Molecular Foundry 主任（2012–2013）、Berkeley Global Science Institute 创始主任
- 2026：清华大学讲席教授，领导 AI 材料科学研究所（Yaghi Science Initiative）；清华大学荣誉教授（2022 起）
- 创业：Atoco（2020）、H2MOF（2021 共同创办）

## 10. 终审清单

- [ ] 生卒 1965-02-09 / 在世，出生地安曼；全名 Omar Mwannes Yaghi
- [ ] 国籍三重口径（美国为主 + 约旦 + 沙特 2021）准确
- [ ] 2025 三人共享表述准确；三人分工无张冠李戴；无「发明 MOF 概念」表述
- [ ] 1995/1998/1999/2005/2007 年份链准确；数字口径（MOF-177 等）逐项核对
- [ ] 巴勒斯坦难民背景中性实写、无政治评论；2026 清华只写事实
- [ ] 博士导师 Klemperer 与博士后导师 Holm 区分准确；Tomic/Hoskins 未入关系库
- [ ] 被引排名注明 Thomson Reuters 口径
- [ ] 无引语杜撰；品牌 OpenMathAI；表格语义化 + 公式框 + 网格背景

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 `pages/Omar_M._Yaghi/page.md` 逐页对照 Beamer tex 全部事实
- [ ] 头像核对（2025 诺贝尔演讲个人照）
- [ ] 引语核对：页面无直接引语，全篇不得出现引号原话
- [ ] 编译验证：`make distclean && make` 0 错误
- [ ] Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] Overfull/Underfull 检查（vbox ≤10pt、hbox ≤50pt）
- [ ] 身份信息页布局与 Sanger 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐

---

> **名单状态**：`chemist/generate_21th_century_list.py` 由主控统一收尾，本文件不改动清单脚本。
