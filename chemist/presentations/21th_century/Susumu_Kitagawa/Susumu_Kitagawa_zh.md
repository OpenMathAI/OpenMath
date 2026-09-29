# Susumu Kitagawa（北川进）立传提示词

> qid=Q11401680 · 1951-07-04 生于日本京都 · 在世 · 日本化学家 · 诺贝尔化学奖（2025，与 Richard Robson、Omar M. Yaghi 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Susumu_Kitagawa/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：对齐 `chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}` 黄金骨架（表格语义化 tabularx + 公式展示框 + 时间线页 + 身份信息页）。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/Susumu_Kitagawa_20251008.jpg`，2025-10-08 京都大学诺奖记者会个人照，已就位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{cube}\enspace 柔性多孔晶体的建筑师\enspace·\enspace 日本`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（北川 進）、国籍、出生地、教育、博士、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和孔洞圆阵（稀疏空心/实心圆错落），呼应「多孔框架的孔道」母题。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如配位聚合物吸附、软多孔晶体变换。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`；中文语境可用汉字名「北川进」。

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Susumu Kitagawa（北川 進；中文惯称：北川进），FRS
- **生卒**：1951-07-04 生于日本京都（在世）
- **国籍**：Japan（日本）
- **身份**：化学家、大学教师；京都大学 iCeMS 特任教授（Distinguished Professor）
- **家庭**：页面无载，禁写
- **教育轨迹**：京都大学本科 → 1979 京都大学博士（hydrocarbon chemistry，烃类化学）
- **导师**：页面无载（metadata 亦无 doctoral_advisor 字段），禁写
- **职业轨迹**：
  - 1979 任 Kindai University（近畿大学）助理教授；1983 讲师；1988 副教授
  - 1986–1987 Texas A&M University 博士后（F. Albert Cotton 组）
  - 1992 Tokyo Metropolitan University 无机化学教授
  - 1996 City University of New York 客座教授
  - 1998 回京都大学，合成化学与生物化学系无机功能化学教授
  - 2007 共同创办 iCeMS（Institute for Integrated Cell-Material Sciences），任创始副所长；2013–2023 所长
  - 2024 任京都大学研究推进担当副学长（Executive Vice-President for Research Promotion）
  - 2011–2023 日本学术会议成员及协作成员
- **研究领域**：配位化学——有机无机杂化化合物、多孔配位聚合物、金属有机框架（MOFs）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **1951 年生于京都**：战后日本成长的一代化学家，一生与京都结缘。
2. **京都大学一以贯之（1979）**：本科与博士（烃类化学）均出自京都大学。
3. **近畿大学起步（1979–1992）**：助理教授 → 讲师（1983）→ 副教授（1988），十三年积累。
4. **海外历练（1986–1987）**：Texas A&M 博士后，师从无机化学名家 F. Albert Cotton。
5. **东京都立大学教授（1992）**：无机化学讲席教授。
6. **回归京都（1998）**：任无机功能化学教授，奠定此后研究主阵地。
7. **1997 关键证明**：在 Fujita（1994）与 Yaghi（1995）发现之后，证明配位聚合物结构具有气体吸附性质——功能多孔材料发展的关键一环。
8. **1997 开创性报告**：多孔配位聚合物（MOF）用于小分子吸附的 seminal 论文。
9. **2004 早期综述**：系统梳理功能多孔配位聚合物，确立领域框架。
10. **2009 「软多孔晶体」**：提出 soft porous crystals——化学或物理刺激下发生大规模结构可逆变换的柔性框架，是本批三人中「柔性 MOF」方向的代表。
11. **iCeMS 共同创办（2007）**：细胞-材料交叉研究所创始副所长，2013–2023 任所长。
12. **2025 诺贝尔化学奖**：与 Richard Robson、Omar M. Yaghi 共享，表彰金属有机框架分子构建基元的奠基性工作。
13. **日本最高荣誉（2025）**：获文化功劳者（Person of Cultural Merit）与文化勋章（Order of Culture）。

## 3. 配色方案（主色 + 强调 + 分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深绿 deepgreen） | `#175E54` | 多孔框架的生机与柔性晶体的韧性（表头 / 公式文本） |
| 强调色（香槟金，coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（配位化学 badgeCoord） | `#2E5A9E` | 蓝配位聚合物 / 金属节点 |
| 分类色 2（多孔材料 badgePore） | `#1B7A43` | 绿 MOF 孔道 / 气体吸附 |
| 分类色 3（软晶体 badgeSoft） | `#D97B29` | 琥珀 soft porous crystals / 柔性变换 |
| 分类色 4（学术轨迹 badgePath） | `#C0395B` | 玫瑰近畿→东京→京都的轨迹 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和孔洞圆阵（稀疏空心圆与实心圆错落，四档大小），暗示 MOF 规整孔道与客体分子。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Savage** — Alex-Productions（文件 `music_audio/alex-productions/34-pILVwyuW3jw-Savage.wav`；不要复制 wav 到本目录）
- **风格**：沉稳有力 / 结构感 / 大器晚成的厚积薄发
- **匹配理由**：
  - "结构感" 匹配 MOF 研究——金属节点与有机连接体的规整骨架
  - "厚积薄发" 匹配其轨迹——1979 年起四十余年配位化学积累，2025 年 74 岁摘得诺奖
  - "沉稳" 匹配关西学人的低调与长期主义
- **时长**：以实际曲目时长为准，ffmpeg `-shortest` 自动对齐 15 页 × 7 秒

## 4. Slide 规划（15 页，00–14）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 柔性多孔晶体的建筑师 / 北川進 1951– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/领域/现职/荣誉）
03  北川进的一生 — 时间线（10 节点：1951→1979→1986→1992→1997→1998→2007→2009→2016→2025）
04  京都起点与近畿岁月 (1951–1992) — 表格「时间|事件|结果」
05  海外历练与回归京都 (1986–1998) — 表格「阶段|研究|结果」
06  多孔配位聚合物 (1997–2004) — 表格「问题|方法|结果」+ 公式框：配位聚合物气体吸附
07  软多孔晶体 (2009) — 表格「概念|机制|意义」+ 公式框：刺激响应结构变换
08  2025 诺贝尔化学奖 — 表格「三人|方向|分工」（Robson 概念 / Kitagawa 柔性 / Yaghi 系统化）
09  iCeMS 与交叉研究 (2007–2024) — 流程图页
10  荣誉年表 — 高斯式「类别|代表|意义」表格（紫绶褒章 / 学士院奖 / Solvay / FRS / 文化勋章）
11  日本学术会议与学界服务 (2011–2023) — 表格页
12  传承与意义 — 四分类遗产盒（气体存储 / 分离 / 传感 / 柔性器件）
13  遗产：孔道里的功能世界 — 公式框 + 总结
14  结尾 — 「框架有孔，孔里有世界。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2025 获奖结构 | 三人**共享**（Kitagawa / Robson / Yaghi）；获奖理由官方完整英文原句页面无载，**禁止杜撰整句**，用页面转述口径 "foundational work on molecular building blocks for metal-organic frameworks" |
| 首创归属 | 页面明载 Kitagawa 1997 的工作 "Following the discoveries of Makoto Fujita (1994) and Omar M. Yaghi (1995)"——**勿写 Kitagawa 首创 MOF**；其贡献是证明气体吸附性质与柔性框架方向 |
| Fujita 关系 | Makoto Fujita 仅出现在研究脉络叙述（1994 年发现），非个人交往记载——**不入社会关系库** |
| 博士导师 | 页面与 metadata 均无导师姓名——**禁写禁入库** |
| 柔性分工 | 本批三人分工口径：Robson（1990 前驱性概念）、Kitagawa（柔性多孔 MOF / soft porous crystals）、Yaghi（MOF-5 等系统化与命名普及）——勿互相张冠李戴 |
| 单位名称 | Kindai University（近畿大学）；Tokyo Metropolitan University（东京都立大学）；勿写「明治/近畿」混淆 |
| iCeMS 职务 | 2007 共同创办、创始**副**所长；2013–2023 任所长；2024 任副学长——三段勿混 |
| Order of Culture | 2025 同年先获文化功劳者（Person of Cultural Merit）再获文化勋章（Order of Culture）——两件事并列勿混 |
| 生年月日 | 1951-07-04，京都——metadata 与 infobox 一致 |
| 引语 | 页面无直接引语——全篇不得出现引号原话 |
| 同名区分 | 对手方规范名 **Richard Robson**、**Omar M. Yaghi**——yaml/关系表必须用这两形式（勿写 Omar Yaghi），防分裂 stub |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q11401680 | ✅ |
| name_zh | 北川进 | ✅ |
| name_en | Susumu Kitagawa | ✅ |
| birth_date | 1951-07-04 | ✅ |
| death_date | （在世，留空） | ✅ |
| nationality | Japan | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | coordination chemistry / metal-organic frameworks / porous coordination polymers / inorganic chemistry（person_field 带 rank） | ✅ |
| has_biography | false（立传完成后再置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 共同得主**（全部为 page.md 正文或 infobox 明载）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | F. Albert Cotton | 师→生（博士后导师） | 1986–1987 Texas A&M University 博士后 |
| co-honored | Richard Robson | 无向 | 2025 诺贝尔化学奖共同得主 |
| co-honored | Omar M. Yaghi | 无向 | 2025 诺贝尔化学奖共同得主 |

> **禁入库名单**：Makoto Fujita（仅研究脉络提及 1994 年发现，非个人关系）；Shigeru Ishiba（合影，政治人物）；博士导师（页面与 metadata 均无载）。metadata.json 无额外人名。

## 8. 奖项清单

- Chemical Society of Japan (CSJ) Prize for Creative Work（2003）
- Humboldt Research Prize（2008）
- Chemical Society of Japan Award（2009）
- Thomson Reuters Citation Laureates（2010）
- Medal with Purple Ribbon 紫绶褒章（2011）
- De Gennes Prize（2013）
- Japan Academy Prize 日本学士院奖（2016）
- Fred Basolo Medal, Northwestern University（2016）
- Chemistry for the Future Solvay Prize（2017）
- Fujihara Award, The Fujihara Foundation of Science（2017）
- Grand Prix de la Fondation de la Maison de la Chimie（2019）
- Emanuel Merck Lectureship（2019）
- Member of the Japan Academy（2019）
- Fellow of the Royal Society, FRS（2023）
- Nobel Prize in Chemistry（2025，三人共享）
- Person of Cultural Merit 文化功劳者（2025）
- Order of Culture 文化勋章（2025）
- Technical University of Munich 荣誉博士（2018）
- 其他 metadata 提及（Ernest Solvay Prize 即上列 Solvay；Clarivate Citation Laureates 即上列）

## 9. 机构清单

- 教育：京都大学（本科、PhD 1979，hydrocarbon chemistry）
- 任职：Kindai University（1979 助理教授 → 1983 讲师 → 1988 副教授）；Texas A&M University（1986–1987 博士后）；Tokyo Metropolitan University（1992 教授）；City University of New York（1996 客座教授）；京都大学（1998– 无机功能化学教授）；iCeMS（2007 共同创办，2013–2023 所长）；京都大学副学长（2024–）
- 学界服务：日本学术会议成员及协作成员（2011–2023）

## 10. 终审清单

- [ ] 生卒 1951-07-04 / 在世，出生地京都
- [ ] 2025 三人共享表述准确；获奖理由用页面转述口径，无杜撰官方原句
- [ ] 1997 工作定位为「Fujita 1994 / Yaghi 1995 之后的证明」——无首创归属错误
- [ ] 博士导师无载不写；Fujita/Ishiba 未入关系库
- [ ] iCeMS 副所长/所长/副学长三段职务年份准确
- [ ] 文化功劳者与文化勋章 2025 并列表述准确
- [ ] 无引语杜撰；无「第一次/唯一」类无载断言
- [ ] 品牌 OpenMathAI；表格语义化 + 公式框 + 孔洞圆阵背景

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 `pages/Susumu_Kitagawa/page.md` 逐页对照 Beamer tex 全部事实
- [ ] 头像核对（2025-10-08 记者会个人照，非与石破茂合影）
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
