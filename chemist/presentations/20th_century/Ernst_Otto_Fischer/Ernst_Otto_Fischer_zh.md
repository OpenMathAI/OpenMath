# Ernst Otto Fischer（恩斯特·奥托·菲舍尔）立传提示词

> qid=Q44594 · 1918-11-10 – 2007-07-23 · 德国化学家 · 诺贝尔化学奖（1973，与 Geoffrey Wilkinson 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Ernst_Otto_Fischer/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 时间线页 + 表格语义化 tabularx + 公式展示框。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像按 `images.txt` 就位；本页 page.md 页首图为 2018 年 Deutsche Post 纪念邮票像，若仅此图可用邮票像并如实标注图注；否则装饰圆占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{atom}\enspace 夹心化合物的建筑师\enspace·\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、国籍、出生地/去世地、教育（TUM）、博士（导师/论文）、家庭（父 Karl T. Fischer）、核心领域、机构、荣誉。事实取自本地 Wikipedia infobox，不得杜撰；页面无载字段（如配偶/子女）如实标「页面无载」。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「夹心结构 / 金属-环」母题——上下两片圆环夹住金属原子。
5. **表格语义化 + 公式框**（★ Sanger 版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如「二茂铁 $\mathrm{Fe(C_5H_5)_2}$ 夹心结构」。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Ernst Otto Fischer（中文惯称：恩斯特·奥托·菲舍尔）
- **生卒**：1918-11-10 生于慕尼黑近郊 Solln（时属 People's State of Bavaria）→ 2007-07-23 逝于慕尼黑，享年 88
- **国籍**：Germany（德国）
- **身份**：化学家（chemist；金属有机化学先驱；1973 诺贝尔化学奖共同得主）
- **家庭**：父 Karl T. Fischer 为慕尼黑工业大学（TUM）物理学教授；母 Valentine（娘家姓 Danzer）——**配偶/子女页面无载**，立传如实留白
- **教育轨迹**：
  - 1937 年通过 Abitur（中学毕业考试）
  - 义务兵役未满两年二战爆发，先后在波兰、法国、俄国服役
  - 1941 年底趁学习假进入 TUM 开始学化学
  - 1945 年秋被美军释放后复学，1949 年 TUM 毕业
- **导师**：Walter Hieber（TUM 无机化学研究所，以其助理身份开展博士论文）
- **博士**：1952 获博士学位；论文《The Mechanisms of Carbon Monoxide Reactions of Nickel(II) Salts in the Presence of Dithionites and Sulfoxylates》
- **研究领域**：金属有机化学（organometallic chemistry）——二茂铁/夹心化合物、Fischer 卡宾与卡拜、过渡金属配合物

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **慕尼黑教授之家（1918）**：生于 Solln，父亲是 TUM 物理学教授——学术家庭的科学启蒙。
2. **战争中断学业（1937–1945）**：Abitur 后义务兵役未满二战爆发，转战波兰、法国、俄国；1941 年底趁学习假入 TUM 学化学——战火中的化学种子。
3. **战后复学（1945–1949）**：被美军释放后复学，1949 年 TUM 毕业。
4. **Hieber 门下（1949–1952）**：在无机化学研究所任 Hieber 助理，完成镍盐 CO 反应机理博士论文，1952 年获博士学位。
5. **挑战二茂铁结构（1952–）**：获博士学位后留任 TUM，几乎立即质疑 Pauson 与 Kealy 提出的二茂铁结构——科学怀疑精神的经典一课。
6. **二茂铁与新型配合物结构数据**：随后发表二茂铁以及新配合物镍茂（nickelocene）、钴茂（cobaltocene）的结构数据——金属茂家族成形。
7. **Hein 反应之谜（双苯铬）**：聚焦 Hein 的三氯化铬 + 苯基溴化镁反应化学，分离出**双(苯)铬 bis(benzene)chromium**——预示全新一类夹心配合物。
8. **TUM 讲席阶梯（1955–1964）**：1955 讲师、1957 教授、1959 C4 教授、1964 出任 TUM 无机化学讲席教授。
9. **学术院会（1964/1969）**：1964 当选巴伐利亚科学院数学自然科学部成员；1969 当选德国自然科学家科学院 Leopoldina 成员。
10. **Fischer 卡宾与卡拜（1960s）**：其团队发现金属亚烷基（alkylidene）与次烷基（alkylidyne）配合物——后世称 **Fischer carbenes** 与 Fischer-carbynes；至今是有机金属化学的命名性地标。
11. **多产与远播**：约 450 篇期刊论文，培养大量博士与博士后；Firestone Lecturer（威斯康星麦迪逊，1969）、佛罗里达大学访问教授（1971）、MIT Arthur D. Little 访问教授（1973）。
12. **1973 诺贝尔化学奖**：与 Geoffrey Wilkinson 共享，表彰其在有机金属化合物方面的工作（page.md 口径 "for his work on organometallic compounds"）；诺奖演讲 1973-12-11《On the Road to Carbene and Carbyne Complexes》。
13. **最年长的在世德国诺奖得主（2007）**：2007-07-23 逝于慕尼黑；逝世时为最年长的在世德国诺贝尔奖得主，此衔由小他九岁的 Manfred Eigen（1967 化学奖）接续——两位德国化学诺奖得主的世纪接力。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（藏青 deepnavy） | `#1E3A5F` | 金属-配体键的深蓝——无机化学的冷峻（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（夹心化合物 badgeSandwich） | `#1B7A43` | 绿二茂铁 / 双(苯)铬 |
| 分类色 2（金属茂 badgeMetallocene） | `#D97B29` | 琥珀镍茂 / 钴茂 |
| 分类色 3（卡宾卡拜 badgeCarbene） | `#C0395B` | 玫瑰 Fischer carbene / carbyne |
| 分类色 4（讲席与学会 badgeChair） | `#7A3E9D` | 紫 TUM 讲席 / Leopoldina |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「夹心结构：上下两片环戊二烯环夹住金属」的几何意象。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**The Invisible Light** — Infraction（文件 `19-tGxXsgSKPiQ-Documentary Cinematic by Infraction [No Copyright Music] ⧸ The Invisible Light.wav`）
- **风格**：纪录片 / 冷峻电子 / 悬浮感铺底
- **匹配理由**：
  - "Invisible Light"（不可见之光）匹配金属有机化学的本质——肉眼不可见却照亮结构化学新大陆的夹心配合物
  - 纪录片式铺底匹配「战火中起步 → TUM 一生 → 450 篇论文」的沉静学术人生
  - 悬浮电子音色呼应夹心化合物的几何对称美
- **时长**：以实际文件为准 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 夹心化合物的建筑师 / Ernst Otto Fischer 1918–2007 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/国籍/教育/博士/导师/家庭/领域/荣誉）
03  菲舍尔的一生 — Sanger 式时间线（10 节点：1918→1937→1941→1945→1949→1952→1955→1964→1973→2007）
04  战火中的求学 (1918–1949) — 表格「时间|事件|结果」（Abitur/服役/学习假入学/复学）
05  Hieber 门下 (1949–1952) — 表格「导师|论文|结果」+ 公式框：镍盐 CO 反应机理题目
06  质疑二茂铁 (1952–) — 表格「旧说|挑战|新解」+ 公式框：二茂铁 Fe(C5H5)2 夹心结构
07  镍茂、钴茂与双(苯)铬 — 表格「对象|方法|意义」（结构数据 / Hein 反应 / bis(benzene)chromium）
08  TUM 讲席阶梯 (1955–1964) — 表格「年份|职位|结果」（讲师→教授→C4→无机化学讲席）
09  Fischer 卡宾与卡拜 (1960s) — 表格「发现|命名|影响」+ 公式框：金属亚烷基/次烷基配合物
10  多产的学派 — 表格「维度|数字|意义」（约 450 论文 / 学生 / 三大访问教职）
11  1973 诺贝尔化学奖 — 与 Wilkinson 共享（co-honored）+ 诺奖演讲《On the Road to Carbene and Carbyne Complexes》
12  荣誉清单 — Sanger 式「类别|代表|意义」表格（Alfred Stock / Centenary / 巴伐利亚勋章等，从 metadata award_received）
13  最年长的德国诺奖得主（2007）— 与 Manfred Eigen 的接续 + 墓碑页（Grabstaette 照片可用）
14  结尾 — 「两片环夹住一个金属原子，夹出了化学的新纪元。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 同名区分（最重要） | Ernst Otto Fischer（1918–2007，金属有机、1973 诺奖）≠ Hermann Emil Fischer（1902 诺奖、糖化学/嘌呤）≠ Fischer 投影式（Hermann E. Fischer）——立传中凡称"菲舍尔"须带全名 |
| Fischer 卡宾 ≠ Fischer 酯化 | Fischer carbene（1960s 金属亚烷基配合物）与 Emil Fischer 命名的经典有机反应（酯化/投影式/锁钥学说）毫无关系——勿混写 |
| 诺奖理由口径 | page.md 仅载 "for his work on organometallic compounds"（Wilkinson 篇同口径）；官方完整 citation（含 "performed independently" 与 "sandwich compounds"）**本页无载**——引用以 page.md 为限，独立发现的双语表述勿加引号原话 |
| 二茂铁结构归属 | Fischer 是"质疑 Pauson 与 Kealy 所提结构"并发表结构数据者； Wilkinson 篇作 "discovery of the structure of ferrocene"——两篇各忠于本人页面，勿在 Fischer 篇写"发现二茂铁结构"一家独揽 |
| 卡宾年份 | "In the 1960s his group discovered..."——勿精确到单一年份 |
| 家庭 | 仅父母（父 Karl T. Fischer、母 Valentine née Danzer）实载；**配偶/子女页面无载**——身份信息页留白，禁止编造婚姻 |
| 死后衔称 | "At the time of his death, Fischer was the oldest living German Nobel laureate"——是"最年长的在世德国诺奖得主"，勿写"最后一位"或"唯一" |
| Eigen 接续 | Manfred Eigen（1967 化学奖共享得主）接续"最年长在世德国诺奖得主"，且小 Fischer 九岁——年份与年龄差如实 |
| 军役表述 | 二战在波兰/法国/俄国服役、1945 秋被美军释放——如实简述，勿渲染战争细节 |
| 论文题目 | 英文题目照录《The Mechanisms of Carbon Monoxide Reactions of Nickel(II) Salts in the Presence of Dithionites and Sulfoxylates》——勿缩写或意译走样 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q44594 | ✅ |
| name_zh | 恩斯特·奥托·菲舍尔 | ✅ |
| name_en | Ernst Otto Fischer | ✅ |
| birth_date | 1918-11-10 | ✅ |
| death_date | 2007-07-23 | ✅ |
| nationality | Germany | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | chemistry（person_field 细分见下表，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

**person_field 细分 rank 表**：

| rank | name_en | name_zh |
|---|---|---|
| 0 | organometallic chemistry | 金属有机化学 |
| 1 | sandwich compounds | 夹心化合物 |
| 2 | ferrocene | 二茂铁 |
| 3 | Fischer carbene | Fischer 卡宾 |

## 7. 社会关系入库清单

**红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Walter Hieber | 师→生（direction=advisor） | TUM 无机化学研究所博士导师，1952 获博士学位 |
| co-honored | Geoffrey Wilkinson | 无向 | 1973 诺贝尔化学奖共同得主（有机金属化合物） |

> 禁入库名单：Pauson、Kealy（仅"质疑其结构假说"的学术交锋，非白名单关系类型，且无个人交往实载）、Hein（反应命名来源，非个人关系）、Manfred Eigen（仅"接续最年长在世德国诺奖得主"事实，无个人关系实载）——均不入库。本页正文与 infobox 之外，metadata.json 的 award_received 不产生关系。

## 8. 奖项清单

- Nobel Prize in Chemistry（1973，与 Geoffrey Wilkinson 共享）
- Alfred Stock Memorial Prize（metadata.json 明载）
- Centenary Prize（metadata.json 明载）
- Bavarian Order of Merit（metadata.json 明载）
- Great Cross with Star and Sash of the Order of Merit of the Federal Republic of Germany（metadata.json 明载）
- Bavarian Maximilian Order for Science and Art（metadata.json 明载）
- Bayerischer Poetentaler；honorary golden medal of the state capital Munich；Munich "München leuchtet" award（metadata.json 明载）
- LMU Munich 荣誉博士（1969 正文：1972 年由 LMU 化学与药学系授予荣誉博士——以正文 1972 为准）
- 院士：巴伐利亚科学院（1964）、Leopoldina（1969）

## 9. 机构清单

- 教育：Technical University of Munich（TUM；1941 底入学、1949 毕业、1952 博士；infobox 另列 LMU Munich）
- 任职：TUM 一生——Hieber 无机化学研究所助理（1949–1952）→ 讲师（1955）→ 教授（1957）→ C4 教授（1959）→ 无机化学讲席教授（1964）
- 访问教职：University of Wisconsin–Madison Firestone Lecturer（1969）、University of Florida（1971）、MIT Arthur D. Little 访问教授（1973）

## 10. 终审清单

- [ ] 生卒 1918-11-10 / 2007-07-23，享年 88；生卒地均为慕尼黑（出生地 Solln）
- [ ] 1973 与 Wilkinson 共享表述准确；诺奖理由以 page.md 口径为准，不引官方完整 citation
- [ ] 与 Hermann Emil Fischer 同名区分贯穿全篇；Fischer carbene 与 Emil Fischer 命名反应不混
- [ ] 二茂铁归属表述按 Fischer 篇口径（质疑 Pauson/Kealy 并发表结构数据）
- [ ] 配偶/子女留白（页面无载）
- [ ] 引语全部可在本地 Wikipedia 原文找到；无直接引语时不出现引号原话
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Ernst_Otto_Fischer/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：按 `images.txt` 核对肖像；可用 2018 Deutsche Post 纪念邮票像（如实标注图注）或装饰圆占位
- [ ] **国籍**：封面顶部明示德国
- [ ] **引语核对**：本页无直接引语，一律间接转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批 Wilkinson 篇互查：1973 共享口径、二茂铁归属表述两篇一致
