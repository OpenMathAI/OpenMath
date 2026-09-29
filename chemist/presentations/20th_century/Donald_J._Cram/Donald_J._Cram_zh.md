# Donald J. Cram（唐纳德·克拉姆）立传提示词

> qid=Q135151 · 1919-04-22 – 2001-06-17 · 美国化学家 · 20 世纪 · 诺贝尔化学奖（1987，与 Jean-Marie Lehn、Charles J. Pedersen 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Donald_J._Cram/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：参考 `chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`（表格语义化 tabularx + 公式展示框 + 时间线页）。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面头像**：page.md 与 images.txt **无真实人物肖像**（唯一图片为 hemicarcerand 包结硝基苯的晶体结构图）——右上角用**装饰圆占位**（主色渐变 + 姓名/主-客体示意题字）；可尝试 Wikipedia REST API `page/summary` 查 infobox 原图，404 则维持装饰圆。晶体结构图（`images/Nitrobenzene_bound_within_hemicarcerand...jpg`）留作 §4 正文第 12 页"主-客体化学"插图，不得充当肖像。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{cube}\enspace 为分子造屋者\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像（或装饰圆）+ 右侧 2×2 信息网格，至少含：生卒、出生地/去世地、国籍、教育（Rollins/Nebraska/Harvard）、博士导师、核心领域（Cram's rule、主-客体化学）、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆），母题呼应「主体分子包裹客体分子」——大圆环内嵌小圆点的图形语义。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化（主-客体互补示意 / Cram's rule 的羰基亲核进攻模型）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Donald James Cram（中文惯称：唐纳德·詹姆斯·克拉姆）
- **生卒**：1919-04-22 生于佛蒙特州 Chester → 2001-06-17 逝于加利福尼亚州 Palm Desert（癌症），享年 82
- **国籍**：United States（美国）
- **身份**：化学家（UCLA 有机化学教授；Saul Winstein 有机化学讲席教授）
- **家庭**：苏格兰移民之父（Cram 未满四岁时去世，家中五个孩子唯一的男性）、德国移民之母；靠 Aid to Dependent Children 长大，自幼打工——摘果、送报、刷房，以物易物换钢琴课；18 岁前已做过至少 18 份工。第一任妻子 Jean Turner（Rollins 同级 1941 届，后获哥伦比亚大学社会工作硕士）；第二任妻子 Jane（Mount Holyoke 化学教授，后为合著者）；**主动选择不要孩子**——"because I would either be a bad father or a bad scientist."（page.md 明载）
- **教育轨迹**：
  - Winwood High School（纽约长岛）
  - Rollins College（Winter Park, Florida，1938–1941，全国荣誉奖学金；化学系助理；戏剧、教堂唱诗班、Lambda Chi Alpha；以自建化学装置闻名）——1941 化学 BS
  - University of Nebraska——1942 有机化学 MS（论文 "Amino ketones, mechanism studies of the reactions of heterocyclic secondary amines with -bromo-, -unsaturated ketones."）
  - Harvard University——1947 有机化学 PhD（论文 "Syntheses and reactions of 2-(ketoalkyl)-3-hydroxy-1,4-naphthoquinones"）
- **导师**：Louis Fieser（哈佛博士导师）；硕士导师 Norman O. Cromwell（内布拉斯加）；Merck 时期导师 Max Tishler（青霉素研究）
- **研究领域**：化学——有机化学、立体化学（Cram's rule）、主-客体化学（host–guest chemistry）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **寒门少年（1919–1937）**：父亲早逝、救助金长大、18 份工与钢琴课——佛蒙特 Chester 出身的自力少年。
2. **Rollins 岁月（1938–1941）**：以自建化学装置闻名；奖学金 + 勤工 + 社团俱全，1941 化学 BS。
3. **内布拉斯加硕士（1942）**：Norman O. Cromwell 指导有机化学 MS。
4. **Merck 青霉素（1942–1945）**：在 Merck & Co 实验室做青霉素研究，导师 Max Tishler——战时工业化学的历练。
5. **哈佛博士与 MIT 博士后（1945–1947+）**：Fieser 门下萘醌合成获 PhD（1947）；后为 ACS 博士后研究员在 MIT 与 John D. Roberts 共事。
6. **UCLA 五十年（1947–1987）**：1947 助理教授、1955 教授，至 1987 退休；一生教过约 8,000 名本科生、指导 200 名研究生、学生来自 21 国；课堂上弹吉他唱民谣。
7. **Cram's rule（1952 前后提出，page.md 未载年份——不得标注年份）**：预测羰基化合物亲核进攻产物的立体化学模型——不对称诱导领域的经典规则。
8. **从平面到立体（1970s–）**：在 Charles Pedersen 开创性的**冠醚**（二维有机化合物，可识别并选择性结合特定金属离子）基础上，把这类化学推进到**三维**——合成形状各异的分子，以互补三维结构选择性结合其他化学物种。
9. **主-客体化学（host–guest chemistry）**：与 Lehn（超分子）、Pedersen（冠醚）共同奠基的领域；Cram 的工作是迈向"人工合成酶功能模拟物"的一大步——酶的特殊行为源于其特征结构。
10. **hemicarcerand（1997）**：与同事报道硝基苯被包结于 hemicarcerand 内的晶体结构（Chemical Communications, 1997）——"分子容器"意象的实证（page.md 唯一图片）。
11. **1987 诺贝尔化学奖**：与 Jean-Marie Lehn、Charles J. Pedersen 三人共享，理由 "for their development and use of molecules with structure-specific interactions of high selectivity"（page.md 口径）；三人被 page.md 称为 host–guest chemistry 的奠基者。
12. **多产学者**：发表逾 350 篇论文、8 部有机化学专著（含与 Hammond 的经典教科书《Organic Chemistry》三个版次、与 Jane M. Cram 合著《The Essence of Organic Chemistry》《Container Molecules and their Guests》）；1973 年与爱尔兰化学家 Francis Leslie Scott 合作研究。
13. **自白与落幕**：研究方法论自白——"An investigator starts research in a new field with faith, a foggy idea, and a few wild experiments. Eventually the interplay of negative and positive results guides the work."（page.md 明载可引）；2001-06-17 因癌症逝于 Palm Desert，享年 82。

## 3. 配色方案（主色 + 强调 + 分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深绛 dark maroon） | `#7E1E23` | 冠醚环抱客体的深邃（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（主-客体化学 badgeHost） | `#2E5A9E` | 蓝主体包裹客体 / 分子容器 |
| 分类色 2（立体化学 badgeCram） | `#1B7A43` | 绿 Cram's rule / 不对称诱导 |
| 分类色 3（冠醚谱系 badgeCrown） | `#D97B29` | 琥珀 Pedersen 冠醚 / 三维化 |
| 分类色 4（教育与传承 badgeTeach） | `#6B4E16` | 棕 8000 本科生 / 教科书 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 篇一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），母题「大环之中嵌套小点」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Through the Darkness** — Audiomachine（清单预置 `music_audio/inspiring-electronic/14-Trn1cSsY2t8-Audiomachine - Through the Darkness.wav`；执行时按项目惯例软链至本目录，不复制 wav 文件）
- **风格**：史诗 / 穿越 / 破晓感
- **匹配理由**：
  - "穿越黑暗"匹配其寒门早年（丧父、救助金、18 份工）走向诺贝尔的自我锻造
  - 破晓感匹配"从二维冠醚到三维主-客体"的范式跃迁——前路无人处点亮结构选择性的化学
  - 史诗感匹配其为分子"造屋"的宏大愿景（人工酶模拟物）
  - ★ 备查：本曲在化学家 20 世纪系列已分配给 Moissan（1906）篇——若执行时判定撞曲不可接受，可向主控申请改曲；本提示词暂按清单指定执行
- **时长核对**：执行时确认音轨时长 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，00–14）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 为分子造屋者 / Donald J. Cram 1919–2001 + 四色 badge + 右上（肖像或装饰圆）+ 国籍行
02  身份信息页（★ 必做）— 左头像/装饰圆 + 右 2×2 信息网格（生卒/出生地 Chester/去世地 Palm Desert/教育三校/博士导师 Fieser/领域/荣誉）
03  克拉姆之路 — 时间线（10 节点：1919→1941→1942→1945→1947→1947→1955→1987→1997→2001）
04  寒门少年 (1919–1938) — 表格「时间|事件|结果」（丧父/ADC/18 份工/钢琴课）
05  Rollins 与内布拉斯加 (1938–1942) — 表格「时间|事件|结果」（自建装置/BS 1941/MS 1942）
06  Merck、哈佛与 MIT (1942–1947) — 表格「人物|工作|收获」（Tishler 青霉素/Fieser 萘醌/Roberts）
07  UCLA 五十年 (1947–1987) — 表格「时间|事件|结果」+ 自白引语框（faith, a foggy idea...）
08  Cram's rule — 表格「问题|方法|结果」+ 公式框：羰基亲核进攻立体模型（★ 不得标注提出年份）
09  从冠醚到三维 (Pedersen → Cram) — 表格「前驱|拓展|意义」+ hemicarcerand 晶体结构插图
10  1987 诺奖 — 表格「三人|方向|贡献」（与 Lehn、Pedersen 共享；主-客体/超分子/冠醚）+ 公式框：structure-specific interactions of high selectivity
11  讲台与书桌 — 双栏页：8,000 本科生/200 博士生/21 国 / 吉他民谣 / 教科书与专著（8 部）
12  荣誉清单 — 「类别|代表|意义」表格（含 itemize：诺奖/National Medal of Science 1993/NAS 1961/Cope 1974/Willard Gibbs 1985）
13  遗产：主-客体化学 — 四分类遗产盒 + 公式框：Cram → Lehn 超分子谱系
14  结尾 — 「给分子造一间恰好合身的屋子。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 获奖理由口径 | page.md 措辞 "for their development and use of molecules with structure-specific interactions of high selectivity"；三人被 page.md 称为 host–guest chemistry 奠基者——勿另编官方全句 |
| 三人分工方向 | Pedersen=冠醚（二维、开创）、Cram=三维化/主-客体、Lehn=超分子化学方向（page.md 只对 Cram 与 Pedersen 有明确表述；Lehn 的具体方向 page.md 无载，勿替 Lehn 篇代言） |
| Cram's rule 年份 | page.md **未载**提出年份——Slide 与正文一律不标年份；勿写"1952" |
| 肖像红线 | images.txt 仅 hemicarcerand 晶体结构图——**禁用晶体结构图冒充肖像**；装饰圆占位或 REST API 回退 |
| 博士论文年份 | 哈佛论文标注 1947；内布拉斯加硕士论文 1942——两条论文勿混、年份勿换位 |
| 导师三线 | 哈佛博士导师 Louis Fieser / 内布拉斯加硕士导师 Norman O. Cromwell / Merck 导师 Max Tishler——三条线并列，勿合并、勿漏 |
| 子女 | 主动不要孩子（引语 page.md 明载）——勿写"无子女"以外演绎；**绝不与 parent-child 关系入库** |
| 博士生名单 | infobox 明载 **M. Frederick Hawthorne、Norman L. Allinger** 两人；metadata.json 另有 **Fred Wudl**——Wudl 属 metadata-only，**禁入库** |
| 第一块 IC 语境 | 本篇无涉；勿因 "Cram" 与其他领域同名人物混淆（如编程语言作家等） |
| 逝世地 | 2001-06-17 逝于 Palm Desert, California（享年 82）——与出生地 Chester, Vermont 勿混 |
| 引语 | 可引两处：研究方法论自白（faith, a foggy idea...）与不要孩子的自白（because I would either...）；其余不得编造 |
| 公司名 | Merck & Co（药企实验室）勿与"Bayer 无关"类错误交叉（那是 Baeyer 篇教训）——本篇按 page.md 写 Merck & Co 即可 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q135151 | ✅ |
| name_zh | 唐纳德·克拉姆 | ✅ |
| name_en | Donald J. Cram | ✅ |
| birth_date | 1919-04-22 | ✅ |
| death_date | 2001-06-17 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | chemistry（person_field 细分：organic chemistry / stereochemistry / host–guest chemistry / supramolecular chemistry，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Louis Fieser | 师→生（博士导师） | 哈佛博士导师（1947，萘醌合成） |
| advisor-student | Norman O. Cromwell | 师→生（硕士导师） | 内布拉斯加有机化学硕士导师（1942） |
| advisor-student | Max Tishler | 师→生（企业导师） | Merck 时期导师（1942–1945 青霉素研究） |
| advisor-student | M. Frederick Hawthorne | 师→生（学生） | infobox 博士生 |
| advisor-student | Norman L. Allinger | 师→生（学生） | infobox 博士生 |
| colleague | John D. Roberts | 无向 | MIT 博士后（ACS postdoctoral fellow）共事 |
| colleague | Francis Leslie Scott | 无向 | 1973 年合作研究（爱尔兰化学家） |
| spouse | Jean Turner | 无向 | 第一任妻子，Rollins 同级（1941 届），哥伦比亚大学社会工作硕士 |
| spouse | Jane M. Cram | 无向 | 第二任妻子，前 Mount Holyoke 化学教授，多部著作合著者 |
| co-honored | Jean-Marie Lehn | 无向 | 1987 诺贝尔化学奖共同得主 |
| co-honored | Charles J. Pedersen | 无向 | 1987 诺贝尔化学奖共同得主 |

> **禁入库名单**：Fred Wudl（metadata.json-only 博士生，page.md infobox 无——禁入库）；子女（主动不育，无子女可入库）； textbook 合著者 George S. Hammond / James B. Hendrickson（著作署名非人际语义）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1987，与 Lehn、Pedersen 共享）
- National Medal of Science（1993）
- NAS Award in Chemical Sciences
- Arthur C. Cope Award, ACS（1974）
- ACS Award for Creative Work in Synthetic Organic Chemistry（1965）
- Willard Gibbs Award, ACS Chicago Section（1985）
- Tolman Award, ACS Southern California（1984）
- Glenn T. Seaborg Medal（1989）
- Golden Plate Award of the American Academy of Achievement（1988）
- Roger Adams Award in Organic Chemistry（frontmatter 有载）；Centenary Prize（frontmatter 有载）
- Guggenheim Fellowship（1955）
- 院士：美国国家科学院（1961）；美国艺术与科学院（1967）；International Academy of Science, Munich
- Saul Winstein Endowed Chair in Organic Chemistry（UCLA 讲席）

## 9. 机构清单

- 教育：Winwood High School（长岛）；Rollins College（BS 1941）；University of Nebraska（MS 1942）；Harvard University（PhD 1947）
- 任职：Merck & Co（1942–1945，青霉素研究）；MIT（ACS 博士后，John D. Roberts）；University of California, Los Angeles（1947 助理教授 → 1955 教授 → 1987 退休；Saul Winstein 讲席）
- 著作：与 Hammond《Organic Chemistry》1959/1964/1970 三版；《Fundamentals of Carbanion Chemistry》1965；《The Essence of Organic Chemistry》1978；《From Design to Discovery》1990；《Container Molecules and their Guests》1994

## 10. 终审清单

- [ ] 生卒 1919-04-22 / 2001-06-17，享年 82；出生地 Chester, Vermont、去世地 Palm Desert
- [ ] 三人共享方向准确；获奖理由按 page.md 口径；Lehn 方向不代言
- [ ] Cram's rule 不标年份；博士/硕士/企业导师三线准确
- [ ] 博士生只入 Hawthorne、Allinger 两人；Wudl 禁入库
- [ ] 肖像处理合规（装饰圆或 REST API 实图；晶体结构图仅作插图）
- [ ] 两处引语按原文；无编造引语；无子女表述准确
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 `pages/Donald_J._Cram/page.md` 逐页对照 Beamer tex 全部事实
- [ ] 头像：装饰圆或 REST API 实图，晶体结构图仅插图（★ 重点核查）
- [ ] 国籍：封面明示美国
- [ ] 编译验证：`make distclean && make`
- [ ] Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox≤10pt、hbox≤50pt）
- [ ] 身份信息页布局与 Sanger 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐

---

> **名单状态**：由 chem-batch-19 批次产出提示词与数据入库；立传与 Review 列由主控统一收尾。
