# Richard Kuhn（里夏德·库恩）立传提示词

> qid=Q78483 · 1900-12-03 – 1967-07-31 · 奥地利-德国生物化学家 · 20 世纪 · 诺贝尔化学奖（1938，独享；战后才受领）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Richard_Kuhn/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传的 Beamer 格式与提示词结构**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 表格语义化 tabularx + 公式展示框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。本地 images.txt 仅有墓碑照（Rkuhn_grab.JPG），**不可用作肖像**；先尝试 Wikipedia REST API `page/summary` 取 infobox 原图（Commons `Special:FilePath` 回退，250px 改 500px）；404 则用**装饰圆占位**（主色渐变圆 + 首字母 RK），并在 Review 时记录。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 类胡萝卜素与维生素\enspace·\enspace 奥地利/德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名 Richard Johann Kuhn、国籍（奥匈帝国维也纳出生 → 西德海德堡去世）、教育（Vienna → LMU Munich）、博士导师、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「多烯长链 / 共轭体系」母题——圆点暗示类胡萝卜素共轭链上重复的异戊二烯单元。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如核黄素全合成 / 维生素 B6。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Richard Johann Kuhn（中文惯称：里夏德·约翰·库恩，通称 Richard Kuhn）
- **生卒**：1900-12-03 生于奥匈帝国维也纳 → 1967-07-31 逝于西德海德堡，享年 66
- **国籍**：奥地利-德国（Austrian-German；出生奥匈帝国，主要学术生涯在德国，晚年属西德）
- **身份**：生物化学家（carotenoids 与 vitamins；海德堡大学化学系主任 / 威廉皇帝医学研究所所长）
- **家庭**：1928 年娶 Daisy Hartmann，育二子四女
- **教育轨迹**：
  - 维也纳读文理中学与高中；1910–1918 与后来的物理学诺奖得主 **Wolfgang Pauli** 同校
  - 1918 起在 University of Vienna 听化学课；在 **LMU Munich** 完成学业
  - 1922 年在 **Richard Willstätter** 指导下以酶学研究获博士学位
- **导师**：Richard Willstätter（博士导师，1915 诺贝尔化学奖得主）
- **研究领域**：生物化学——类胡萝卜素、黄素类、维生素（B2/B6）、酶；理论有机化学（脂肪族/芳香族立体化学、多烯与联烯合成、烃的酸性）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **维也纳少年与 Pauli 同窗（1910–1918）**：与后来的物理学诺奖得主 Wolfgang Pauli 是中学同校同学——两颗未来的诺贝尔星同框。
2. **晚定的化学志向**：早年兴趣广泛，较晚才决定学化学；1918 起在维也纳大学听化学课。
3. **慕尼黑与 Willstätter（至 1922）**：在 LMU Munich 完成学业，以酶学研究获博士学位——师承叶绿素化学大家。
4. **三站履历**：毕业后先留慕尼黑，再赴 ETH Zurich，1929 起落脚海德堡大学。
5. **执掌威廉皇帝医学研究所（1929）**：出任新成立的威廉皇帝医学研究所化学研究所所长（Kaiser Wilhelm Institute for Medical Research；1950 年后改称海德堡 Max Planck Institute for Medical Research），1937 年起兼管全所。
6. **海德堡教授（1937）**：任海德堡大学化学系负责人，兼生物化学教授；并曾以访问研究教授身份在宾夕法尼亚大学（费城）任生理化学客座一年。
7. **理论有机化学**：脂肪族与芳香族化合物的立体化学、多烯与联烯（cumulenes）合成、构型与颜色、烃的酸性。
8. **类胡萝卜素与维生素**：对维生素 B2（核黄素）与抗皮炎的维生素 B6 有重要工作；**核黄素与维生素 B6 全合成**是其标志性成果。
9. **Kuhn–Winterstein 反应**：以二磷化四碘的有机化学反应命名传世。
10. **1938 诺贝尔化学奖（拒领）**：官方理由 "for his work on carotenoids and vitamins"；因希特勒禁止德国公民接受诺贝尔奖而**被迫拒领**——他在一封亲笔信中甚至称把奖颁给德国人是对元首禁令的公然冒犯；**战后**才正式受领。
11. **Soman（1944）**：被归于 1944 年发现致命神经毒剂 Soman——科学被战争扭曲的沉重一页。
12. **纳粹时期的污点**：与纳粹高层合作，1936 年告发三位犹太同事；2005 年德国化学家学会（GDCh）宣布停发以其命名的 Richard Kuhn Medal——"尽管有科学成就，库恩不适合作为楷模与重要奖项的命名者"。
13. **编者与身后**：1948 年起任 *Justus Liebigs Annalen der Chemie* 主编；1967 年逝于海德堡。奖项：Goethe Prize（1942）、Wilhelm Exner Medal（1952）、Paul Ehrlich and Ludwig Darmstaedter Prize（1958）、Centenary Prize（1962）、维也纳大学荣誉博士（1960）、奥地利科学与艺术勋章（1961）等。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（钢蓝 steel-navy） | `#123C5B` | 多烯共轭的深邃（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（类胡萝卜素 badgeCaro） | `#C9702A` | 橙 carotenoids / 维生素 A 前体 |
| 分类色 2（黄素类 badgeFlavin） | `#D9A400` | 黄核黄素 / 异咯嗪环 |
| 分类色 3（维生素 B6 badgeB6） | `#1B7A43` | 绿抗皮炎维生素 / 全合成 |
| 分类色 4（历史之重 badgeShadow） | `#7A2430` | 暗红拒领诺奖 / Soman / 纳粹污点 |
| 背景 | `#F7F6F9` | 浅灰白（与高斯一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「共轭多烯链的重复单元」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Timeless** — Alex-Productions（文件 `music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav`；不要复制 wav 文件，Makefile 直接引用该路径）
- **风格**：沉稳 / 纪录片 / 有厚重感
- **匹配理由**：
  - "厚重" 匹配库恩的双重遗产——维生素化学的巅峰成就与纳粹时期的沉重污点并存，叙事需要克制的纪录片质感
  - "沉稳" 匹配拒领-战后受领诺奖这段横跨十余年的历史弧线
  - 无欢快色彩的曲目避免对 Soman/告发同事等沉重史实的轻慢
- **时长对齐**：以实际曲目时长与 15 页 × 7 秒 ≈ 105 秒比较，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 类胡萝卜素与维生素 / Richard Kuhn 1900–1967 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/出生地/去世地/教育/博士导师/领域/荣誉）
03  库恩的一生 — 高斯式时间线（10 节点：1900→1918→1922→1928→1929→1937→1938→1944→1948→1967）
04  维也纳少年：与 Pauli 同窗 (1910–1918) — 表格「时间|事件|结果」
05  慕尼黑：Willstätter 门下 (1918–1922) — 表格「阶段|导师|收获」+ 公式框：酶学博士课题
06  三站履历：慕尼黑—苏黎世—海德堡 (1922–1929) — 表格「站点|机构|方向」
07  威廉皇帝医学研究所 (1929–1937) — 所长履职 / 海德堡教授 / 宾大客座
08  类胡萝卜素与维生素 B2/B6 — 表格「对象|贡献|意义」+ 公式框：核黄素全合成
09  理论有机化学 — 多烯/联烯合成、立体化学、烃酸性（表格「问题|方法|结果」）
10  1938 诺贝尔化学奖：拒领与受领 — 官方获奖理由 + 希特勒禁令 + 战后受领（暗红分类色）
11  战争的阴影 — Soman（1944）/ 告发同事（1936）/ 2005 GDCh 停发 Kuhn 奖章（克制客观一页）
12  编者与荣誉 — Annalen 主编（1948）/ Goethe Prize / Exner Medal / 奖项表格
13  遗产：复杂的一生 — 四分类遗产盒 + 公式框：维生素化学贡献与历史教训并置
14  结尾 — 「科学的光环之下，历史要求诚实的注视。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1938 独享 | 1938 诺贝尔化学奖为**独享**（无共同得主）；官方理由 "for his work on carotenoids and vitamins" |
| 拒领表述 | 因**希特勒禁止德国公民接受诺贝尔奖**而拒领；亲笔信称颁奖是对元首禁令的冒犯（page.md 明载可转述）；**战后**才受领——勿写"主动拒绝" |
| 国籍口径 | "Austrian-German biochemist"；出生奥匈帝国维也纳，metadata 国籍链为 Cisleithania/Nazi Germany/West Germany——行文写"奥地利-德国"，入库写 Austria + Germany 两条（见 §6），勿写"纳粹籍" |
| 同窗 Pauli | 1910–1918 **schoolmate**（同校同学），非同事非合作者——入库用 other 类型 |
| Soman | page.md 用 "is credited with the discovery"（被归于）措辞——转述保持 "credited with"，勿改写成"发明" |
| 纳粹时期 | 告发三位犹太同事（1936）、与纳粹高层合作、GDCh 2005 年停发奖章及其声明——**page.md 明载，必须如实呈现**，语气克制客观；GDCh 声明中的 "career-oriented camp follower" 等定性句只作转述不加渲染 |
| 荣誉年份 | Goethe Prize 1942（infobox 表格载）、Wilhelm Exner Medal 1952、维也纳荣誉博士 1960、奥地利勋章 1961、Paul Ehrlich and Ludwig Darmstaedter Prize 1958、Centenary Prize 1962——勿混淆；infobox award_received 另列 Pour le Mérite、Emil-von-Behring-Prize、Adolf-von-Baeyer Gold Medal、Cothenius Medal 等无年份项 |
| 姓名 | Richard Johann Kuhn——与核物理学家（如 Kuhn 其他同名者）无涉；德语发音注记可省 |
| 家庭 | 1928 娶 Daisy Hartmann，二子四女——数字勿错 |
| 无引语 | page.md 除亲笔信定性句（建议间接转述）外无直接引语——禁造引号"原话" |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q78483 | ✅（metadata.json） |
| name_zh | 里夏德·库恩 | ✅ |
| name_en | Richard Kuhn | ✅（page.md 规范名，db_id 空） |
| birth_date | 1900-12-03 | ✅ |
| death_date | 1967-07-31 | ✅ |
| nationality | Austria, Germany（两条带 rank） | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry（person_field 细分：carotenoids / vitamins / flavins / stereochemistry，带 rank） | ✅ |
| has_biography | false（立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 同窗**（仅收 page.md 正文或 infobox 明载）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Richard Willstätter | 师→生（博士导师） | LMU Munich，1922 年以酶学研究获博士学位 |
| spouse | Daisy Hartmann | 无向 | 1928 年结婚，育二子四女 |
| other | Wolfgang Pauli | 无向 | 1910–1918 维也纳同校同学 |

**门生**：page.md 无 doctoral students 明载——**不设学生关系**。

> **禁入库名单（metadata-only / 背景人物）**：被其告发的三位犹太同事（page.md 未具名）、Daisy Hartmann 之外的家庭成员、GDCh（机构非人物）、Adolf Hitler（仅作为政策背景，非学术关系）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1938，独享；因纳粹禁令拒领，战后受领）
- Goethe Prize of the City of Frankfurt（1942）
- Wilhelm Exner Medal（1952）
- Paul Ehrlich and Ludwig Darmstaedter Prize（1958）
- Centenary Prize（1962）
- Honorary doctorate, University of Vienna（1960）
- Austrian Decoration for Science and Art（1961）
- infobox 另载（无年份）：Pour le Mérite for Sciences and Arts、Emil-von-Behring-Prize、Adolf-von-Baeyer Gold Medal、Cothenius Medal、Prize of the City of Vienna for Natural Sciences
- Richard Kuhn Medal（GDCh 设立；**2005 年宣布停发**）

## 9. 机构清单

- 教育：维也纳文理中学/高中、University of Vienna（1918 起听课）、LMU Munich（PhD 1922，Willstätter 门下）
- 任职：Munich（博士后）、ETH Zurich、University of Heidelberg（1929 起；1937 起化学系负责人，兼生物化学教授）、Kaiser Wilhelm Institute for Medical Research（1929 起化学所所长；1950 后改称 Max Planck Institute for Medical Research；1937 起兼管全所）、University of Pennsylvania（访问研究教授一年）
- 编辑：*Justus Liebigs Annalen der Chemie* 主编（1948 起）

## 10. 终审清单

- [ ] 生卒 1900-12-03 / 1967-07-31，享年 66；出生地维也纳、去世地海德堡
- [ ] 1938 独享表述准确；"希特勒禁令→拒领→战后受领"链条准确
- [ ] 博士导师 Willstätter（LMU Munich，1922）表述准确；Pauli 为同校同学
- [ ] Soman 用 "credited with" 措辞；纳粹时期史实如实且克制（告发 1936 / GDCh 2005 停发奖章）
- [ ] 核黄素/B6 全合成、Kuhn–Winterstein 反应表述准确
- [ ] 国籍两条（Austria/Germany）入库口径与行文一致
- [ ] 中文引号内无 page.md 无法溯源的"原话"；无"第一次/唯一"类断言
- [ ] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Richard_Kuhn/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：images.txt 仅墓照——REST API / Special:FilePath 尝试结果与占位方案记录回写本节
- [ ] **国籍**：封面顶部明示奥地利/德国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到；本篇建议全文无直接引语，亲笔信内容用间接转述
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
