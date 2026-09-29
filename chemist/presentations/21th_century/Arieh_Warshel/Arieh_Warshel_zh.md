# Arieh Warshel（阿里耶·瓦谢尔）立传提示词

> qid=Q4790366 · 1940-11-20 生于英属巴勒斯坦托管地 Sde Nahum 基布兹（今以色列）· 在世 · 以色列/美国双籍 · 诺贝尔化学奖（2013，与 Karplus/Levitt 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Arieh_Warshel/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：参考 `chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.md` §0-§11 结构标杆（高斯式：身份信息页 + 时间线 + 表格语义化 + 公式框）。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像取 `pages/Arieh_Warshel/images.txt` 中 2013 年斯德哥尔摩记者会照 `Arieh_Warshel_6_2013.jpg`；下载失败用装饰圆占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 计算酶学的开山者\enspace·\enspace 以色列 / 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（אריה ורשל）、国籍、出生地、教育、博士导师、兵役、核心领域、任职、荣誉。事实取自本地 page.md infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「多尺度模拟」母题——大小错落的圆点暗示从量子到连续介质的尺度层级。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化（QM/MM 划分、EVB 势能面等）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Arieh Warshel（希伯来文 אריה ורשל；中文惯称：阿里耶·瓦谢尔）
- **生卒**：1940-11-20 生于基布兹 Sde Nahum（时属英属巴勒斯坦托管地，今以色列）· 在世
- **国籍**：以色列、美国（ Israeli-American；正文口径）
- **身份**：生物化学家、生物物理学家；USC 化学与生物化学杰出教授（Distinguished Professor），持 Dana and David Dornsife 化学讲席
- **家庭**：生于犹太家庭（page.md 未载配偶子女——留白，勿编造）
- **兵役**：以色列国防军装甲兵（Israeli Armored Corps），最终军衔上尉（Captain）；作为士兵参加 1967 六日战争与 1973 赎罪日战争
- **教育轨迹**：
  - 退伍后入海法 Technion（以色列理工学院），1966 获化学 BSc，summa cum laude
  - Weizmann 科学研究院：1967 MSc、1969 化学物理 PhD（导师 Shneior Lifson）
- **博士后**：哈佛大学博士后至 1972（page.md 正文未点名博士后合作者——Karplus 导师关系仅 metadata 有载，见 §5）
- **任职轨迹**：1972–1976 回 Weizmann，同时为剑桥 MRC 工作；1976 被 Weizmann 拒绝 tenure → 加入 USC 化学系任教至今
- **研究领域**：计算生物化学与生物物理——计算机模拟、计算酶学（Computational Enzymology）、静电相互作用、酶催化

## 2. 核心叙事亮点（约 13 条）

1. **基布兹之子（1940）**：生于 Sde Nahum 基布兹的犹太家庭——从「基布兹鱼塘到诺贝尔奖」（其 2021 回忆录书名自况）。
2. **军旅与转折**：装甲兵服役至过上尉；参加 1967、1973 两场战争后进入 Technion 读化学。
3. **Technion 一等荣誉（1966）**：化学 BSc summa cum laude 毕业。
4. **Weizmann 师从 Lifson（1967–1969）**：化学物理 MSc/PhD；Lifson 是其博士导师（infobox 明载唯一博士导师）。
5. **哈佛博士后（至 1972）**：完成博士后训练后回 Weizmann。
6. **Weizmann–剑桥 MRC 双线（1972–1976）**：在 Weizmann 任职同时为剑桥医学研究理事会（LMB）工作。
7. **被迫出走（1976）**：被 Weizmann 拒绝 tenure，转赴南加州大学（USC）化学系——此后在此完成全部获奖工作。
8. **力场程序与首个生物过程分子动力学模拟**：开创并共同开创基于笛卡尔坐标的力场程序；完成**第一个生物过程的分子动力学模拟**。
9. **QM/MM 方法**：发展量子化学/分子力学（QM/MM）组合方法模拟酶促反应——多尺度模型的支柱。
10. **蛋白质微观静电模型与自由能微扰**：建立蛋白质微观静电模型、蛋白质中自由能微扰方法等关键进展——计算酶学的概念骨架。
11. **2013 诺贝尔化学奖**：与 Martin Karplus、Michael Levitt 共享，官方理由 "for the development of multiscale models for complex chemical systems"（复杂化学体系的多尺度模型之发展）。
12. **深圳诺奖实验室（2017）**：2017-04 在香港中文大学（深圳） campus 创办 Warshel Institute for Computational Biology（深圳市「十三五」诺奖实验室计划的一部分）。
13. **持续荣誉（2009–2025）**：2009 当选美国国家科学院院士；2025 当选塞尔维亚国家科学院（SASA）外籍成员；著有《Computer Modeling of Chemical Reactions in Enzymes and Solutions》（1997）、《Electrostatic Basis of Biological Actions》（2026）等。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（靛蓝 indigoblue） | `#283593` | 计算化学的严谨与纵深（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（力场与 MD badgeForce） | `#3F51B5` | 蓝力场程序 / 首个生物过程 MD |
| 分类色 2（QM/MM badgeQMMM） | `#00838F` | 青量子-经典耦合 / 多尺度 |
| 分类色 3（静电与自由能 badgeEle） | `#E07B39` | 琥珀静电模型 / 微扰 |
| 分类色 4（计算酶学 badgeEnz） | `#B23A5B` | 玫瑰酶催化 / 计算酶学 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「多尺度」的层级圆融。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Awaken** — Alex-Productions（`music_audio/alex-productions/36-aqLUvpAdLNQ-Awaken.wav`，勿复制 wav，Makefile 直接引用路径）
- **风格**：觉醒感 / 上行推进 / 纪录片
- **匹配理由**：
  - "Awaken" 匹配其学科叙事——把酶催化从试管「唤醒」进计算机，开创计算酶学
  - 上行推进感匹配「基布兹 → Technion → Weizmann → USC → 诺贝尔」的人生爬坡
  - 纪录片质感匹配 1967/1973 战争与科研双线交织的传记叙事
- **时长**：以实际文件为准，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，00–14）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 计算酶学的开山者 / Arieh Warshel 1940– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士导师/兵役/领域/任职/荣誉）
03  瓦谢尔的一生 — 高斯式时间线（10 节点：1940→1966→1969→1972→1976→1970s-80s→2009→2013→2017→2025）
04  早年：基布兹与军旅 (1940–1966) — 表格「时间|事件|结果」
05  Weizmann：师从 Lifson (1967–1972) — 表格「时间|事件|结果」
06  双线岁月与出走 (1972–1976) — 表格「阶段|处境|结果」（Weizmann+MRC 双线；拒 tenure→USC）
07  力场与首个生物过程 MD — 表格「问题|方法|结果」+ 公式框：分子动力学积分基本式
08  QM/MM：多尺度模型的支柱 — 表格「挑战|方法|结果」+ 公式框：QM/MM 划分示意 E=E_QM+E_MM+E_coupling
09  静电与自由能微扰 — 表格「问题|方法|结果」+ 公式框：自由能微扰 ΔG
10  2013 诺贝尔化学奖 — 三人共享页（Karplus / Levitt / Warshel）+ citation 原句公式框
11  计算酶学的诞生 — 表格「人物|方向|结果」（对酶催化的计算理解谱系，仅 page.md 实载内容）
12  荣誉与院士 — 高斯式「类别|代表|意义」表格 + itemize 荣誉清单（NAS 2009 等）
13  遗产：深圳诺奖实验室与著作 — 四分类遗产盒（Warshel Institute 2017 / 专著三部 / 回忆录）
14  结尾 — 「把酶装进计算机。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2013 获奖理由 | 官方原句 "for the development of multiscale models for complex chemical systems"；三人**共享**（Karplus / Levitt / Warshel），勿写独享 |
| 博士导师 | 正文 infobox 博士导师**仅 Shneior Lifson**；frontmatter 另列 Martin Karplus，但正文只载「哈佛博士后至 1972」未点名 Karplus——**Karplus 导师关系不入库**（metadata-only 禁写） |
| 出生地 | Kibbutz Sde Nahum, **British Mandate of Palestine (now Israel)**——勿直接写「生于以色列」（1940 年尚无以色列国） |
| 兵役表述 | 装甲兵、最终军衔上尉；参加 1967 六日战争与 1973 赎罪日战争——事实陈述即可，不做政治引申 |
| Weizmann 出走 | 1976 被 Weizmann **拒绝 tenure** 后加入 USC——按 page.md 口径如实写，勿美化或渲染 |
| MRC 表述 | 1972–1976 是「回 Weizmann 任职**同时**为剑桥 LMB 工作」——勿写成全职移居剑桥 |
| 中文译名 | 阿里耶·瓦谢尔；勿与「Michael Levitt（迈克尔·莱维特）」「Martin Karplus（马丁·卡普拉斯）」译名混淆 |
| 军衔两说 | 正文两处均作 Captain（上尉），infobox 与 Biography 节一致——勿写更高军衔 |
| 荣誉年份 | NAS 院士 2009；RSC Fellow 2008 / Honorary Fellow 2014；以色列化学会金奖 page.md 作「The 2013 Israel Chemical Society Gold Medal (2014)」——按 page.md 双年份口径写 |
| 引语红线 | page.md 无 Warshel 直接引语——全部改间接转述，不得编造「原话」 |
| 著作年份 | 1997 Wiley / 2021《From Kibbutz Fishponds to The Nobel Prize》/ 2026《Electrostatic Basis of Biological Actions》——三本勿混 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q4790366 | ✅ |
| name_zh | 阿里耶·瓦谢尔 | ✅ |
| name_en | Arieh Warshel | ✅ |
| birth_date | 1940-11-20 | ✅ |
| death_date | null（在世） | ✅ |
| nationality | Israel / United States（双籍，rank 0/1） | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | computational biology（person_field 细分见下表） | ✅ |
| has_biography | false（Beamer 立传后置 1） | ✅ |

**person_field 细分 rank 表**：

| rank | field_en | field_zh |
|---|---|---|
| 0 | computational biology | 计算生物学 |
| 1 | computational enzymology | 计算酶学 |
| 2 | QM/MM | QM/MM 多尺度模拟 |
| 3 | molecular dynamics | 分子动力学 |

## 7. 社会关系入库清单

**师长 / 共同得主**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Shneior Lifson | 师→生（博士导师） | Weizmann 化学物理博士（1969）导师，infobox 明载 |
| co-honored | Martin Karplus | 无向 | 2013 诺贝尔化学奖共同得主（DB 既有记录 #3851，用规范名互指） |
| co-honored | Michael Levitt | 无向 | 2013 诺贝尔化学奖共同得主 |

> **禁入库名单**（metadata.json-only，正文/infobox 无载）：Martin Karplus（博士导师口径，frontmatter 有载但正文仅载哈佛博士后未点名）、Technion/Weizmann 具体同门、USC 同事。Warshel 页面未载配偶子女。

## 8. 奖项清单

- Nobel Prize in Chemistry（2013，与 Karplus/Levitt 共享）
- Annual Award of the International Society of Quantum Biology and Pharmacology（1993）
- Tolman Medal（2003）
- President's Award for Computational Biology, ISQBP（2006）
- RSC Soft Matter and Biophysical Chemistry Award（2012）
- Golden Plate Award of the American Academy of Achievement（2014）
- The Founders Award of the Biophysical Society（2014）
- The 2013 Israel Chemical Society Gold Medal（2014 授予）
- Fellow of the Royal Society of Chemistry（2008）；Honorary FRSC（2014）
- Member, US National Academy of Sciences（2009）
- Fellow of the Biophysical Society（2000）；Fellow of the AAAS（2012）
- Honorary doctorate: Bar-Ilan University（2014）、Uppsala University（2015）、University of Tromsø、Łódź University of Technology
- Member, Serbian National Academy of Science SASA（2025）

## 9. 机构清单

- 教育：Technion – Israel Institute of Technology（BSc 1966）、Weizmann Institute of Science（MSc 1967 / PhD 1969）
- 任职：哈佛大学博士后（至 1972）→ Weizmann Institute（1972–1976，同时为剑桥 LMB 工作）→ University of Southern California 化学系（1976–，杰出教授、Dana and David Dornsife Chair）
- 命名机构：Warshel Institute for Computational Biology（香港中文大学（深圳），2017-04 创办）

## 10. 终审清单

- [x] 生卒 1940-11-20 / 在世；出生地英属巴勒斯坦托管地 Sde Nahum 基布兹
- [x] 2013 三人共享表述准确；citation 英文原句完整
- [x] 博士导师仅 Lifson；Karplus 导师关系不入库并在 §7 注明
- [x] 军旅（装甲兵上尉、两场战争）事实陈述无政治引申
- [x] 1976 拒 tenure→USC 口径如实
- [x] 引语全部间接转述（page.md 无直接引语）
- [x] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 读取 `pages/Arieh_Warshel/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：优先 `Arieh_Warshel_6_2013.jpg`（Commons），404 则装饰圆占位
- [ ] 国籍：封面明示「以色列 / 美国」
- [ ] 引语核对：无直接引语，全篇间接转述
- [ ] 编译验证：`make distclean && make`
- [ ] Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger/高斯模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 2013 三人共享另两篇（Karplus / Levitt）口径交叉对齐
