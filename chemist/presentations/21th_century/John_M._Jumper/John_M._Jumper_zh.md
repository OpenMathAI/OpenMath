# John M. Jumper（约翰·江珀）立传提示词

> qid=Q89620738 · 1985-01-01 生于美国阿肯色州小石城 · 在世 · 美国化学家/计算机科学家 · 诺贝尔化学奖（2024，与 Demis Hassabis 共享一半；David Baker 独得另一半）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/John_M._Jumper/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：对齐 `chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}` 黄金骨架（表格语义化 tabularx + 公式展示框 + 时间线页 + 身份信息页）。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。页面无独立个人肖像：用 `images.txt` 中 2024 Nobel Prize Conference 三人合影（Jumper 居右）或装饰圆占位，图注写「David Baker, Demis Hassabis, and John Jumper at 2024 Nobel Prize Conference」。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{dna}\enspace AlphaFold 与蛋白质折叠的破晓\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地、教育、博士（双导师）、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和点阵气泡（稀疏圆点网格），呼应「氨基酸残基序列 → 三维折叠坐标」的母题。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如 CASP GDT 得分、AlphaFold 预测流程。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

## 1. 背景信息（用于 Slide 1–3）

- **全名**：John Michael Jumper（中文惯称：约翰·江珀）
- **生卒**：1985-01-01 生于美国阿肯色州 Little Rock（在世；metadata 中 "1985-00-00" 为噪声，以 infobox 1985-01-01 为准）
- **国籍**：United States（美国）
- **身份**：化学家与计算机科学家（American chemist and computer scientist）、AI for Science 研究者
- **家庭**：页面无载，禁写
- **教育轨迹**：
  - 2003 毕业于 Pulaski Academy（阿肯色州）
  - 2007 Vanderbilt University BS，物理与数学双专业
  - 2008 University of Cambridge MPhil，理论凝聚态物理（St Edmund's College；2007 Marshall Scholarship）
  - 2012 University of Chicago MS，理论化学
  - 2017 University of Chicago PhD，理论化学；论文《New Methods Using Rigorous Machine Learning for Coarse-Grained Protein Folding and Dynamics》
- **导师**：博士双导师 Tobin R. Sosnick 与 Karl Freed（University of Chicago）
- **职业轨迹**：Google DeepMind 任 director 近九年；2026-06 宣布休整后离开公司加入 Anthropic
- **研究领域**：蛋白质结构预测、深度学习、人工智能、机器学习（infobox Fields: Artificial intelligence, Machine learning）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **1985 年生于小石城**：比 20 世纪多数化学奖得主年轻近半个世纪的新生代得主。
2. **Pulaski Academy（2003）**：家乡中学毕业，走向物理与数学。
3. **Vanderbilt 双专业（2007）**：物理学 + 数学 BS——日后机器学习建模的数理底盘。
4. **Marshall Scholarship 剑桥（2007–2008）**：St Edmund's College，MPhil 理论凝聚态物理。
5. **芝加哥转向（2012–2017）**：从凝聚态物理转入理论化学，师从 Sosnick 与 Freed 双导师，直面蛋白质折叠。
6. **博士论文（2017）**：用严格的机器学习方法处理粗粒化蛋白质折叠与动力学——AlphaFold 思路的学术原点。
7. **加入 DeepMind**：此后近九年任 director，带队做 AI 蛋白质结构预测。
8. **AlphaFold 诞生**：深度学习模型，从氨基酸序列高精度预测蛋白质三维结构（Known for: AlphaFold）。
9. **CASP14 夺冠（2020-11）**：第 14 届国际结构预测评比中，约三分之二蛋白的 GDT 得分超过 90（100 为完全吻合），远超所有对手算法。
10. **Nature's 10（2021）**：入选《自然》年度十大科学人物。
11. **AlphaFold 数据库（截至 2024-01）**：已释放 2.14 亿个蛋白质结构预测。
12. **2024 诺贝尔化学奖**：与 Demis Hassabis 共享一半 "for protein structure prediction"；另一半归 David Baker（computational protein design）。
13. **荣誉接续与转身（2025–2026）**：2025 Golden Plate Award、Marshall Medal、当选 FRS；2026 当选美国国家工程院院士；2026-06 宣布离开 DeepMind、加入 Anthropic。

## 3. 配色方案（主色 + 强调 + 分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深青 deepteal） | `#0B5351` | 蛋白质折叠的深海与 AI 计算的冷静（表头 / 公式文本） |
| 强调色（香槟金，coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（AlphaFold badgeAF） | `#2E5A9E` | 蓝 AlphaFold 模型 / 结构预测 |
| 分类色 2（CASP badgeCASP） | `#1B7A43` | 绿 CASP14 竞赛 / GDT 得分 |
| 分类色 3（深度学习 badgeDL） | `#D97B29` | 琥珀神经网络 / 机器学习 |
| 分类色 4（学术轨迹 badgePath） | `#C0395B` | 玫瑰物理→化学→AI 的转向 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和点阵气泡（稀疏圆点网格，四档大小错落），暗示氨基酸残基点位与折叠坐标。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Daylight** — Alex-Productions（文件 `music_audio/alex-productions/44-JoyIRE5k2Yo-Daylight.wav`；不要复制 wav 到本目录）
- **风格**：明亮 / 希望 / 新生代破晓感
- **匹配理由**：
  - "Daylight" 呼应 AlphaFold 破晓时刻——五十年蛋白质折叠难题在 2020 年 CASP14 被点亮
  - "希望" 匹配其科学意义——2.14 亿结构预测向全球研究者开放，加速药物与生命科学研究
  - "新生代" 匹配 1985 年生、获奖时 39 岁的年轻得主气质
- **时长**：以实际曲目时长为准，ffmpeg `-shortest` 自动对齐 15 页 × 7 秒

## 4. Slide 规划（15 页，00–14）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — AlphaFold 与蛋白质折叠的破晓 / John M. Jumper 1985– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士双导师/领域/荣誉）
03  江珀的一生 — 时间线（10 节点：1985→2003→2007→2008→2012→2017→2020→2021→2024→2026）
04  早年与数理底盘 (1985–2007) — 表格「时间|事件|结果」
05  剑桥与芝加哥：转向理论化学 (2007–2017) — 表格「阶段|研究|结果」+ 公式框：粗粒化折叠与机器学习
06  AlphaFold：模型与思路 — 表格「问题|方法|结果」+ 公式框：序列 → 3D 结构预测
07  CASP14 破晓 (2020-11) — 表格「对手|得分|含义」+ 公式框：GDT > 90（约三分之二蛋白）
08  AlphaFold 的规模 (2021–2024) — 表格「时间|进展|结果」+ 公式框：2.14 亿结构
09  2024 诺贝尔化学奖 — 表格「得主|份额|获奖方向」（Hassabis 共享一半 / Baker 另一半）
10  荣誉年表 — 高斯式「类别|代表|意义」表格（Nature's 10 / Breakthrough / Lasker / Gairdner / FRS）
11  从 DeepMind 到 Anthropic (2026) — 流程图页
12  传承与意义 — 四分类遗产盒（结构生物学 / 药物发现 / AI for Science / 开放数据）
13  遗产：预测即理解 — 公式框 + 总结
14  结尾 — 「氨基酸的序列里，折叠着生命的形状。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 出生日期 | infobox 明载 **1985-01-01**（Little Rock, Arkansas）；metadata 的 "1985-00-00" 是噪声，勿采用 |
| 2024 获奖结构 | Jumper 与 Hassabis **共享一半**（protein structure prediction），Baker 独得另一半（computational protein design）——勿写三人平分 |
| 2024 获奖理由 | 页面口径 "for protein structure prediction"（蛋白结构预测）；官方完整 citation 英文原句页面无载，**禁止杜撰整句**，用页面转述口径 |
| Baker 的方向 | Baker 获奖方向是 computational protein design（蛋白质设计），与 Jumper/Hassabis 的预测方向不同——勿混 |
| DeepMind 年限 | 正文 "served as a director at Google DeepMind for nearly nine years"——写「近九年」，勿写具体入职年份（页面无载） |
| 离职时间线 | 2026-06 宣布将离开、休整后加入 Anthropic；正文另有 "In 2026, Jumper left DeepMind and joined Anthropic"——两处口径以「2026 年」笼统表述最稳 |
| BBVA 年份冲突 | infobox 作 2022、正文作 "In 2021, Jumper was awarded the BBVA..."——以**正文 2021** 为准并加注口径冲突 |
| Wiley Prize | 正文 "In 2022 Jumper received the Wiley Prize in Biomedical Sciences"——勿并入 2021 |
| "最年轻" 断言 | 页面未载「最年轻化学奖得主」，**禁写**；只可写 1985 年生的事实 |
| AlphaFold 规模 | 2.14 亿结构是 "as of January 2024" 的口径——勿写成当前总数 |
| CASP 得分 | "above 90 for around two-thirds of the proteins"（GDT，100 为完全吻合）——勿写成"全部蛋白" |
| 职业身份 | infobox 职业 computational biologist / AI researcher / chemist；页面首句 "American chemist and computer scientist"——口径统一用后者 |
| 同名区分 | 对手方规范名 **Demis Hassabis**、**David Baker**——yaml/关系表必须用这两形式，防分裂 stub |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q89620738 | ✅ |
| name_zh | 约翰·江珀 | ✅ |
| name_en | John M. Jumper | ✅ |
| birth_date | 1985-01-01 | ✅ |
| death_date | （在世，留空） | ✅ |
| nationality | United States | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | protein structure prediction / artificial intelligence / machine learning / computational biology（person_field 带 rank） | ✅ |
| has_biography | false（立传完成后再置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 共同得主**（全部为 page.md 正文或 infobox 明载）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Tobin R. Sosnick | 师→生（博士导师） | University of Chicago 博士双导师之一 |
| advisor-student | Karl Freed | 师→生（博士导师） | University of Chicago 博士双导师之一 |
| co-honored | Demis Hassabis | 无向 | 2024 诺贝尔化学奖共享一半（AlphaFold 蛋白质结构预测） |
| co-honored | David Baker | 无向 | 2024 诺贝尔化学奖共同得主（Baker 独得另一半，蛋白质设计） |

> **禁入库名单**：页面无配偶/子女/合作者个人关系记载；metadata.json 与正文 infobox 一致，无 metadata-only 人名。AlphaFold 团队成员页面未具名，一律不入库。

## 8. 奖项清单

- Marshall Scholarship（2007）
- Nature's 10（2021）
- BBVA Foundation Frontiers of Knowledge Award, Biology and Biomedicine（正文 2021 / infobox 2022，以正文为准加注）
- Wiley Prize in Biomedical Sciences（2022）
- Breakthrough Prize in Life Sciences（2023）
- Canada Gairdner International Award（2023）
- Albert Lasker Award for Basic Medical Research（2023）
- Nobel Prize in Chemistry（2024，与 Hassabis 共享一半）
- Golden Plate Award of the American Academy of Achievement（2025）
- Marshall Medal, Marshall Aid Commemoration Commission（2025）
- Fellow of the Royal Society, FRS（2025）
- Member of the National Academy of Engineering（2026）
- 其他 metadata 提及（Clarivate Citation Laureates、VinFuture Prize）：页面正文无年份细节，仅列名不展开

## 9. 机构清单

- 教育：Pulaski Academy（–2003）、Vanderbilt University（BS 2007）、University of Cambridge, St Edmund's College（MPhil 2008）、University of Chicago（MS 2012、PhD 2017）
- 任职：Google DeepMind（director，近九年，–2026）；2026 年加入 Anthropic（先休整）
- 相关：AlphaFold 项目与数据库（DeepMind / Alphabet）

## 10. 终审清单

- [ ] 生卒 1985-01-01 / 在世，出生地 Little Rock, Arkansas
- [ ] 2024 获奖结构「与 Hassabis 共享一半 + Baker 另一半」表述准确；获奖理由用页面口径 "for protein structure prediction"
- [ ] 博士双导师 Sosnick + Freed 并列；剑桥 MPhil 凝聚态物理（非化学）
- [ ] CASP14 2020-11 夺冠、GDT >90 约三分之二蛋白；2.14 亿结构注明 "as of January 2024"
- [ ] BBVA 2021（正文口径加注）；Wiley 2022；2025 Golden Plate/Marshall Medal/FRS；2026 NAE
- [ ] 2026 离开 DeepMind 加入 Anthropic 只写事实
- [ ] 无「最年轻」「第一次」类页面无载断言；引语零杜撰（本篇页面无直接引语）
- [ ] 品牌 OpenMathAI；表格语义化 + 公式框 + 点阵气泡背景

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 `pages/John_M._Jumper/page.md` 逐页对照 Beamer tex 全部事实
- [ ] 头像/合影图注核对（三人合影须注明三人身份）
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
