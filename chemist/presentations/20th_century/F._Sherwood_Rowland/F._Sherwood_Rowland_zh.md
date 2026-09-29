# F. Sherwood Rowland（F. 舍伍德·罗兰）立传提示词

> qid=Q111190 · 1927-06-28 – 2012-03-10 · 美国化学家 · 20 世纪 · 诺贝尔化学奖（1995，三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/F._Sherwood_Rowland/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。本地 images.txt 无 infobox 原图 URL：可尝试经 Wikipedia REST API `page/summary` 查 infobox 实际文件名下载（2008 年 World Science Summit 照片），404 则改用 images.txt 中 1975 年 RIT 颁奖合影裁左侧的 Rowland，再不行用装饰圆占位（图注须如实）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{cloud}\enspace 平流层的预警者\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「大气 / 臭氧层」母题——弥散圆点暗示平流层中稀薄而关键的臭氧分子。
5. **表格语义化 + 公式框**（★ Sanger 版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 证据 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如 CFC 光解链式反应 `CFCl3 + hν → CFCl2· + Cl·`、`Cl· + O3 → ClO· + O2`（示意式须忠实页面叙述：氯原子与臭氧反应生成一氧化氯，单个氯原子可破坏大量臭氧分子）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Frank Sherwood "Sherry" Rowland（中文惯称：F. 舍伍德·罗兰；昵称 Sherry）
- **生卒**：1927-06-28 生于俄亥俄州 Delaware（美国）→ 2012-03-10 逝于加州 Newport Beach（帕金森病并发症，短暂身体不适之后），享年 84
- **国籍**：United States（美国）
- **身份**：化学家（加州大学欧文分校化学教授；1995 诺贝尔化学奖得主）
- **家庭**：艺术史学家 Ingrid Rowland 之父，另有一子 Jeff Rowland；两名孙女。页面未载配偶信息——勿编造
- **教育轨迹**：
  - 公立学校体系；因加速跳级，16 岁生日前数周即高中毕业
  - 高中暑假受托管理当地气象站——第一次系统性实验与数据采集经历
  - Ohio Wesleyan University（BA，1948）
  - 入芝加哥大学前曾入海军训练雷达操作员 14 个月，以上士军衔退伍
  - University of Chicago（M.S. 1951、Ph.D. 1952）
- **导师**：Willard Libby（博士导师，芝加哥大学指派导师）
- **博士**：1952，《The epithermal reactions of recoil atoms》（回旋加速器产生的放射性溴原子的化学状态研究）
- **研究领域**：大气化学（atmospheric chemistry）、化学动力学（chemical kinetics）；最著名工作是发现氯氟烃（CFC）导致臭氧损耗

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **俄亥俄神童（1927–1945）**：跳级少年、高中暑假管气象站——系统实验兴趣的起点；未满 16 岁高中毕业。
2. **海军雷达教官（约 1945）**：大学期间应征入伍训练雷达操作员，14 个月以上士退伍——战时服务与无线电技术初遇。
3. **芝加哥放射化学（1948–1952）**：师从 Willard Libby 研究放射化学，博士课题为回旋加速器放射性溴原子的化学状态。
4. **东岸到中西部的学术漂流（1952–1964）**：Princeton（1952–1956）→ University of Kansas（1956–1964）——反应化学与化学动力学的积累期。
5. **扎根 UC Irvine（1964）**：出任加州大学欧文分校化学教授，此后一生在此；1978 当选美国国家科学院院士，1993 任美国科学促进会（AAAS）主席。
6. **与 Molina 的合作（1970 年代初）**：在欧文分校开始与 Mario J. Molina 合作——师徒式搭档由此起步（页面口径为 "began working with"，勿写"招收博士后/博士生"）。
7. **CFC–臭氧理论（1974）**：理论预言人造有机卤代气体将在平流层被太阳辐射分解、释放氯原子，氯与臭氧反应生成一氧化氯，且单个氯原子可破坏大量臭氧分子；论文首刊 *Nature*（1974）。
8. **预警者的自觉（可引语）**：页面实载原句 "...I knew that such a molecule could not remain inert in the atmosphere forever, if only because solar photochemistry at high altitudes would break it down"——用于封面或核心页引语。
9. **全球实测（1970s–80s）**：全球多城市采样测 CCl3F 南北混合——不同纬度浓度对比证明其跨半球快速混合；8 年后复测显示 CCl3F 浓度稳定上升；臭氧层季节起伏（11 月升高、持续下降至 4 月趋平）之下逐年整体下降。
10. **从禁令到议定书（1978–1980s）**：1978 美国首批禁用喷雾罐 CFC，但实际产量很快回升至原有水平；全球管制直到 1980 年代 Vienna Agreement 与 Montreal Protocol 才实现——科学预警与政策落地的漫长接力。
11. **1995 诺贝尔化学奖**：与 Paul J. Crutzen、Mario J. Molina 三人共享（页面口径：CFC 臭氧损耗之发现；官方 citation 原句本地页面无载，见 §5）。
12. **命名遗产**：UC Irvine 理学楼 1998 年命名为 Rowland Hall（门厅立其半身像）；南极 Mount Rowland 2007 年以其命名；母校 Rutherford B. Hayes High School 的 STEM 楼亦以其命名。
13. **落幕（2012）**：帕金森病并发症辞世；挚友 Molina 哀悼原句 "Sherry was a prime influence throughout my career and had inspired me and many others to walk in the shadow of his greatness"（页面实载，Molina 说 Rowland——引用方向勿反）。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（臭氧深绿 ozonedeep） | `#146B3A` | 平流层臭氧与地球生命的守护之色（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（CFC 理论 badgeCFC） | `#1E4E79` | 蓝氯氟烃光解 / 氯催化链 |
| 分类色 2（全球实测 badgeMeasure） | `#B07A2A` | 琥珀 CCl3F 跨半球混合 / 季节与长期趋势 |
| 分类色 3（政策接力 badgePolicy） | `#5B2A86` | 紫 1978 禁令 → Vienna → Montreal |
| 分类色 4（环境预警 badgeWarn） | `#8A1E2D` | 猩红科学预警 / 公众与政治互动 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「大气 / 臭氧层」的弥散分布。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Expedition** — Alex-Productions（清单指定，文件 `music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav`；不要复制 wav 文件）
- **风格**：恢弘 / 探索 / 远征感
- **匹配理由**：
  - "远征" 匹配其科学征程——从放射化学到大气化学，用一生的实测把一行理论推到全球政策
  - "恢弘" 匹配主题尺度——平流层、半球输运、南极以他命名的山峰
  - "探索" 匹配预警者气质——在无人相信的年代坚持测量
- **时长**：以实际曲目时长为准，不足/超出由 ffmpeg `-shortest` 对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 平流层的预警者 / F. Sherwood Rowland 1927–2012 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  罗兰的一生 — Sanger 式时间线（10 节点：1927→1948→1952→1964→1974→1978→1989→1995→2004→2012）
04  早年：跳级少年与气象站 (1927–1948) — 表格「时间|事件|结果」
05  芝加哥：Libby 与放射化学 (1948–1952) — 表格「时间|事件|结果」
06  CFC–臭氧理论 (1974) — 表格「问题|推理|结果」+ 公式框：Cl· + O3 → ClO· + O2 链式损耗示意
07  全球实测 (1970s–80s) — 表格「对象|方法|结果」（CCl3F 混合 / 8 年复测 / 季节与长期趋势）
08  从禁令到议定书 (1978–1987) — 表格「阶段|措施|局限」（1978 禁令→产量回升→Vienna→Montreal）
09  1995 诺贝尔化学奖 — 三人共享页（Crutzen / Molina / Rowland 分工勿混）+ 公式框：获奖口径
10  同事与搭档：Molina — 表格「阶段|合作|结果」+ Molina 哀悼引语
11  荣誉清单 — Sanger 式「类别|代表|意义」表格（Tolman 1976 → ForMemRS 2004）
12  命名遗产 — Rowland Hall（1998）/ Mount Rowland（2007）/ 母校 STEM 楼 流程图页
13  遗产：预警者的世纪 — 四分类遗产盒 + 公式框：科学预警→全球治理的范式
14  结尾 — 「他让看不见的臭氧层，成为全人类看得见的责任。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1995 共享口径 | 与 **Paul J. Crutzen、Mario J. Molina** 三人共享；页面只载罗兰本人的 CFC–臭氧工作，勿替 Crutzen 编造获奖细节 |
| 官方 citation | 1995 官方获奖理由英文原句**本地页面无载**——正文只用页面实载口径（"the discovery that chlorofluorocarbons contribute to ozone depletion"），Review 时经 nobelprize.org 核对原句后再补 |
| Molina 身份 | 页面口径为 "began working with Mario J. Molina"——**勿写"罗兰的博士生/博士后"**，入库用 colleague（见 §7） |
| 引语方向 | "Sherry was a prime influence..." 是 **Molina 悼念 Rowland** 的话，勿写成罗兰自述；"I knew that such a molecule..." 是罗兰本人的话 |
| 本名 | 本名即 **Frank Sherwood "Sherry" Rowland**——"F. Sherwood Rowland" 是惯用署名，勿写"原名 Frank 后改名" |
| 出生地 | 生于俄亥俄州 **Delaware 市**（Delaware, Ohio）——勿与特拉华州混淆；逝于 **Newport Beach, California**，勿写 Irvine |
| 海军经历 | 是**应征训练雷达操作员 14 个月**、上士退伍——勿渲染为"参战" |
| 1978 禁令 | 1978 美国首批禁用喷雾罐 CFC，**但实际产量未停、很快回升至原有水平**；全球管制到 1980 年代——勿写成"禁令一举解决问题" |
| Rowland Hall | 1998 年命名的是 **UC Irvine physical sciences 大楼**（门厅有半身像）；勿与 2004 ForMemRS 混淆年份 |
| 学院会员 | 页面载 "Elected to the American Academy of Arts and Sciences"（未标年份）与 American Philosophical Society（1995）、NAS（1978）——年份口径照实，未载者不标 |
| 政策文件名 | 页面作 **Vienna Agreement** 与 **Montreal Protocol**——照页面用词，勿改写为中文习惯全称 |
| 同名区分 | Willard Libby（1960 诺奖化学得主）是博士导师；勿与放射化学界其他 Libby 混淆 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q111190 | ✅ |
| name_zh | F. 舍伍德·罗兰 | ✅ |
| name_en | F. Sherwood Rowland | ✅ |
| birth_date | 1927-06-28 | ✅ |
| death_date | 2012-03-10 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | atmospheric chemistry（person_field 细分：atmospheric chemistry / chemical kinetics / environmental chemistry / radiochemistry，带 rank） | ✅ |
| has_biography | false（立传完成后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 同事 / 共同得主**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Willard Libby | 师→生（博士导师） | 芝加哥大学指派导师，放射化学方向 |
| colleague | Mario J. Molina | 无向 | 1970 年代初于 UC Irvine 合作提出 CFC 臭氧损耗理论 |
| co-honored | Paul J. Crutzen | 无向 | 1995 诺贝尔化学奖共同得主 |
| co-honored | Mario J. Molina | 无向 | 1995 诺贝尔化学奖共同得主 |

> **禁入库名单（metadata.json-only 或防噪声）**：子女 Ingrid Rowland、Jeff Rowland（正文虽明载但非学界同行，防噪声）；Stanford/Princeton/Kansas 时期无具名合作者可入库；B. J. Finlayson-Pitts / D. R. Blake / A. R. Ravishankara 仅为 NAS 传记纪念文作者，不入库。

## 8. 奖项清单

- Nobel Prize in Chemistry（1995，与 Crutzen/Molina 共享）
- Tolman Medal（1976）
- Leo Szilard Lectureship Award（1979）
- Tyler Prize for Environmental Achievement（1983）
- Japan Prize（1989）
- Whittier College 荣誉理学博士（1989）
- Peter Debye Award（1993）
- Albert Einstein World Award of Science（1994）
- Roger Revelle Medal（1994）
- Golden Plate Award of the American Academy of Achievement（1996）
- Foreign Member of the Royal Society，ForMemRS（2004）
- 当选：National Academy of Sciences（1978）、American Academy of Arts and Sciences（页面未载年份）、American Philosophical Society（1995）
- Guggenheim Fellowship；Nevada Medal；Dickson Prize in Science（metadata 列出，页面正文无年份——照实标注）

## 9. 机构清单

- 教育：Delaware, Ohio 公立学校（跳级）→ Ohio Wesleyan University（BA 1948）→ University of Chicago（M.S. 1951、Ph.D. 1952）
- 任职：Princeton University（1952–1956）→ University of Kansas（1956–1964）→ University of California, Irvine（1964–，化学教授）
- 服务：美国国家科学院院士（1978）；美国科学促进会（AAAS）主席（1993）
- 命名遗产：UC Irvine Rowland Hall（1998，理学楼）；南极 Mount Rowland（2007）；Rutherford B. Hayes High School STEM Wing

## 10. 终审清单

- [x] 生卒 1927-06-28 / 2012-03-10，享年 84，出生地俄亥俄 Delaware、去世地 Newport Beach
- [x] 1995 三人共享（Crutzen/Molina）表述准确；官方 citation 原句"页面无载"已注明
- [x] Molina 为合作者（勿写师生）；两条引语方向与归属核对无误
- [x] 博士导师 Willard Libby 表述准确；海军雷达教官 14 个月口径准确
- [x] 1978 禁令后产量回升、1980 年代全球管制的时间线准确
- [x] 引语全部可在本地 Wikipedia 原文找到（"I knew that such a molecule..."、Molina 悼语）
- [x] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/F._Sherwood_Rowland/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：按 §0.1 的三级回退处理（REST API → 1975 合影裁切 → 装饰圆），图注如实
- [ ] **国籍**：封面顶部明示美国
- [ ] **引语核对**：两条引语必须在 Wikipedia 原文找到，且说话方向正确
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐（对照 Frederick_Sanger_zh.tex）

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾，本提示词不改总名单。
> **最重要的事：每写一页就 make，看到溢出就修。**
