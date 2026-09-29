# Paul Karrer（保罗·卡雷）立传提示词

> qid=Q73093 · 1889-04-21 – 1971-06-18 · 瑞士化学家 · 20 世纪 · 诺贝尔化学奖（1937，与 Norman Haworth 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Paul_Karrer/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传的 Beamer 格式与提示词结构**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 表格语义化 tabularx + 公式展示框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。本地 images.txt **为空**（无任何图片线索），先尝试 Wikipedia REST API `page/summary` 取 infobox 原图（Commons `Special:FilePath` 回退，250px 改 500px）；404 则用**装饰圆占位**（主色渐变圆 + 首字母 PK），并在 Review 时记录。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 维生素的化学家\enspace·\enspace 瑞士`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名 Paul Karrer（FRS FRSE FCS）、国籍、出生地 Moscow / 去世地 Zürich、教育（Old Cantonal School Aarau → University of Zurich PhD）、博士导师、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「类胡萝卜素 / 色素分子」母题——圆点暗示共轭链上依次排列的发色团。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如 β-胡萝卜素结构式 / 维生素 A 转化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Paul Karrer（中文惯称：保罗·卡雷；FRS、FRSE、FCS）
- **生卒**：1889-04-21 生于俄国莫斯科 → 1971-06-18 逝于瑞士苏黎世，享年 82
- **国籍**：Switzerland（瑞士）——父母 Paul Karrer 与 Julie Lerch 均为瑞士侨民；1892 年（3 岁）随家返瑞士
- **身份**：有机化学家（维生素化学；University of Zurich 教授兼化学研究所所长）
- **家庭**：1914 年娶 Helena Froelich，育三子（其中一子夭折于婴儿期）；1971 年卡雷去世，妻子 1972 年去世
- **教育轨迹**：
  - Wildegg 就读；Old Cantonal School Aarau，1908 年毕业（Matura）
  - University of Zurich 师从 **Alfred Werner** 学化学，1911 年获 PhD，后再留化学研究所任助理一年
- **导师**：Alfred Werner（博士导师，1913 诺贝尔化学奖得主）
- **研究领域**：有机化学——植物色素（类胡萝卜素）、维生素 A/B2/C/E、黄素类（flavins）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **莫斯科出生的瑞士人（1889）**：生于俄国莫斯科的瑞士侨民家庭，3 岁随家回国——跨文化生活起点。
2. **阿尔高州的少年（1892–1908）**：Wildegg 与 Old Cantonal School Aarau 受教育，1908 Matura 毕业。
3. **维尔纳门下（1908–1911）**：苏黎世大学师从配位化学奠基人 Alfred Werner，1911 年获 PhD——从金属配合物入门。
4. **欧利希研究所（1911 后）**：博士毕业后赴法兰克福 Georg Speyer Haus，任 Paul Ehrlich（1908 诺贝尔生理学或医学奖得主）麾下化学师——药物化学的历练。
5. **执掌苏黎世化学研究所（1919）**：任 University of Zurich 化学教授兼化学研究所所长——此后一生扎根苏黎世。
6. **从金属配合物到植物色素**：早期研究复杂金属配合物；最重要的工作转向植物色素，特别是黄色**类胡萝卜素**。
7. **类胡萝卜素结构解析**：阐明类胡萝卜素化学结构，并证明其中某些物质在体内转化为**维生素 A**。
8. **β-胡萝卜素结构式（里程碑）**：确立维生素 A 主要前体 β-胡萝卜素的正确结构式——**维生素或维生素原结构被首次确立**（page.md 原文 "the first time that the structure of a vitamin or provitamin had been established"）。
9. **维生素 C 结构确认**：后与霍沃思的工作相互印证——确认抗坏血酸（维生素 C）的结构。
10. **维生素 B2 与 E**：将研究扩展到维生素 B2 与 E；对**黄素类**化学的重要贡献促成 lactoflavin 被鉴定为原以为的"维生素 B2"复合物的一部分。
11. **George Wald 的访客岁月**：后来获 1967 诺贝尔生理学或医学奖的 George Wald 曾短期在卡雷实验室工作，研究维生素 A 在视网膜中的作用。
12. **1937 诺贝尔化学奖**：与英国化学家 Norman Haworth **共享**；诺贝尔演讲 1937-12-11《Carotenoids, Flavins and Vitamin A and B2》。
13. **教科书与身后荣光**：《Lehrbuch der Organischen Chemie》（1927 初版）出至十三版、译成七种语言；1959 年 CIBA、Geigy、Roche、Sandoz、Nestlé、Wander 等公司共同设立 **Paul Karrer Gold Medal** 及讲座（每年或两年一次在苏黎世大学颁发）——以他命名的大奖延续至今。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深青蓝 teal-deep） | `#0E4D64` | 色素分子的深邃（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（类胡萝卜素 badgeCaro） | `#C9702A` | 橙 β-胡萝卜素 / 维生素 A 前体 |
| 分类色 2（黄素类 badgeFlavin） | `#D9A400` | 黄 lactoflavin / 维生素 B2 |
| 分类色 3（维生素 A/C/E badgeVitamin） | `#1B7A43` | 绿脂溶性维生素家族 |
| 分类色 4（学院与传承 badgeLegacy） | `#8C3A5B` | 玫瑰苏黎世 / Karrer 金奖 |
| 背景 | `#F7F6F9` | 浅灰白（与高斯一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「共轭多烯链上依次排列的色素单元」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**New Lands** — Alex-Productions（文件 `music_audio/alex-productions/74-oK8HN0FsZmc-New-Lands.wav`；不要复制 wav 文件，Makefile 直接引用该路径）
- **风格**：开拓 / 明亮 / 发现之旅
- **匹配理由**：
  - "新大陆" 匹配卡雷的学术版图——从金属配合物到植物色素再到维生素结构的未知疆域（维生素/维生素原结构首次确立）
  - "明亮" 匹配类胡萝卜素与黄素的色彩母题——他的化学本身就是关于颜色的化学
  - 上扬叙事匹配「莫斯科出生 → 维尔纳门下 → 欧利希研究所 → 苏黎世掌门 → 1937 诺贝尔」
- **时长对齐**：以实际曲目时长与 15 页 × 7 秒 ≈ 105 秒比较，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 维生素的化学家 / Paul Karrer 1889–1971 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/出生地/去世地/教育/博士导师/领域/荣誉）
03  卡雷的一生 — 高斯式时间线（10 节点：1889→1892→1908→1911→1914→1919→1927→1931→1937→1971）
04  早年：从莫斯科到阿尔高 (1889–1908) — 表格「时间|事件|结果」
05  维尔纳门下 (1908–1911) — 表格「阶段|导师|收获」+ 公式框：金属配合物入门
06  法兰克福：欧利希研究所 (1911–1919) — 表格「人物|角色|收获」（Paul Ehrlich / Georg Speyer Haus）
07  苏黎世掌门 (1919) — 教授兼化学研究所所长
08  类胡萝卜素与维生素 A — 表格「问题|方法|结果」+ 公式框：β-胡萝卜素 → 维生素 A
09  黄素与维生素 B2 — lactoflavin 鉴定（表格「对象|贡献|意义」）
10  维生素 C 与 B/E — 确认抗坏血酸结构、扩展 B2/E（与 Haworth 工作互证）
11  1937 诺贝尔化学奖 — 官方获奖理由 + 与 Norman Haworth 共享（表格「得主|领域|理由」）+ 诺贝尔演讲标题
12  教科书与 Karrer 金奖 — 《Lehrbuch der Organischen Chemie》13 版 7 语言；1959 Karrer Gold Medal（资助公司清单）
13  遗产：维生素化学的奠基者 — 四分类遗产盒 + 公式框：维生素/维生素原结构首次确立
14  结尾 — 「他为看不见的营养素画出了结构式。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1937 共享 | 与 Norman Haworth **共享** 1937 诺贝尔化学奖（Haworth 因碳水化合物与维生素 C）；勿写 Karrer 独享 |
| 获奖理由口径 | page.md 未载 Nobel 官方英文理由整句——**禁杜撰**；只写 "his research on vitamins"（intro 原句）与诺贝尔演讲标题《Carotenoids, Flavins and Vitamin A and B2》（External links 明载） |
| "首次确立" | "the first time that the structure of a vitamin or provitamin had been established" 是 page.md 明载——可用且仅限于此句语境（β-胡萝卜素），勿扩大到"所有维生素" |
| 出生地 | 生于**莫斯科**（俄国），非瑞士本土；父母为瑞士国民；1892 随家返瑞士 |
| 博士导师 | **Alfred Werner**（苏黎世大学，1911 PhD）——勿与他人混淆；页内无第二导师记载 |
| Ehrlich 关系 | 卡雷在 Ehrlich 的 Georg Speyer Haus 任化学师（雇用/同事）——勿写成师承 |
| George Wald | "worked briefly in Karrer's lab"——访客/短暂合作，勿写成博士生；其 1967 诺奖是后来的事 |
| 维生素 B2 | lactoflavin 是"原以为维生素 B2 的复合物的一部分"被鉴定——勿写成"发现维生素 B2" |
| 家庭 | 三子一夭折；妻 Helena Froelich 1914 年结婚、1972 年去世（卡雷 1971 去世后一年）——勿写"妻子先逝" |
| Karrer 金奖设立者 | CIBA AG、J.R. Geigy、F. Hoffmann-La Roche、Sandoz AG、Nestlé、Dr. A. Wander——公司名单列举须完整，颁奖地苏黎世大学 |
| 无引语 | page.md 无任何直接引语——全文禁造引号"原话"，一律间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q73093 | ✅（metadata.json） |
| name_zh | 保罗·卡雷 | ✅ |
| name_en | Paul Karrer | ✅（page.md 规范名，db_id 空） |
| birth_date | 1889-04-21 | ✅ |
| death_date | 1971-06-18 | ✅ |
| nationality | Switzerland | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | organic chemistry（person_field 细分：vitamins / carotenoids / flavins / natural products，带 rank） | ✅ |
| has_biography | false（立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 合作者 / 共同得主**（仅收 page.md 正文或 infobox 明载）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Alfred Werner | 师→生（博士导师） | 苏黎世大学，1911 年 PhD |
| spouse | Helena Froelich | 无向 | 1914 年结婚，育三子 |
| colleague | Paul Ehrlich | 无向 | 法兰克福 Georg Speyer Haus 麾下化学师 |
| colleague | George Wald | 无向 | 曾短期在卡雷实验室研究维生素 A 与视网膜 |
| co-honored | Norman Haworth | 无向 | 1937 诺贝尔化学奖共同得主 |

**门生**：page.md 无 doctoral students 明载——**不设学生关系**。

> **禁入库名单（metadata-only / 背景人物）**：Julie Lerch（母亲）、Charles Glen King、Edmund Hirst（Haworth 侧人物，与 Karrer 无直接记载）、Karrer 金奖各资助公司（机构非人物）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1937，与 Norman Haworth 共享）
- Marcel Benoist Prize（1922）
- 荣誉博士：马德里康普鲁滕塞大学、里昂大学（doctor honoris causa）、巴黎大学（doctor honoris causa）、斯特拉斯堡大学
- Honorary Fellow of the Royal Society of Edinburgh（FRSE）
- Foreign Member of the Royal Society（ForMemRS）
- Fellow of the Chemical Society（FCS）
- Paul Karrer Gold Medal（1959 年以其名设立，苏黎世大学颁发）

## 9. 机构清单

- 教育：Old Cantonal School Aarau（Matura 1908）、University of Zurich（PhD 1911）
- 任职：Georg Speyer Haus, Frankfurt-am-Main（Ehrlich 麾下化学师）、University of Zurich（1919 起化学教授兼化学研究所所长；Karrer 讲座基金会设于其化学研究所 Rämistrasse 71）
- 纪念：Paul Karrer Gold Medal and Lecture（1959 设立）

## 10. 终审清单

- [ ] 生卒 1889-04-21 / 1971-06-18，享年 82；出生地莫斯科、去世地苏黎世
- [ ] 1937 与 Norman Haworth 共享表述准确；获奖理由无杜撰引语
- [ ] 博士导师 Alfred Werner 表述准确；Ehrlich 为雇用关系非师承
- [ ] β-胡萝卜素"首次确立维生素/维生素原结构"仅限 page.md 原句语境
- [ ] lactoflavin 与维生素 B2 表述准确（复合物的一部分，非"发现 B2"）
- [ ] 教科书 13 版 / 7 种语言；Karrer 金奖 1959 年设立、资助公司完整
- [ ] 中文引号内无 page.md 无法溯源的"原话"；无"第一次/唯一"类断言（除 §5 明示原句外）
- [ ] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Paul_Karrer/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：images.txt 为空——REST API / Special:FilePath 尝试结果与占位方案记录回写本节
- [ ] **国籍**：封面顶部明示瑞士（生于莫斯科须交代背景）
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到；本篇全文无直接引语，禁造
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与高斯模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 模板）对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾，执行者不改。
> **最重要的事：每写一页就 make，看到溢出就修。**
