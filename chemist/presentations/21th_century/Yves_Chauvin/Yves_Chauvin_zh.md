# Yves Chauvin（伊夫·肖万）立传提示词

> qid=Q202146 · 1930-10-10（Menen，比利时）– 2015-01-27（Tours，法国，享年 84）· 法国化学家 · 21 世纪 · 诺贝尔化学奖（2005，与 Robert H. Grubbs / Richard R. Schrock 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Yves_Chauvin/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/`）——身份信息页 + 时间线页 + 表格语义化 tabularx + 金边公式框，是本次执行的版式语言。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注；肖像优先取本地 `images.txt`（本篇 infobox 图为「2005 三位得主同框照」——若裁剪困难可装饰圆占位，图注如实）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 烯烃复分解的解码人\enspace·\enspace 法国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（Yves Chauvin）、国籍、出生地/去世地、教育、核心领域、荣誉；本篇**无博士/无导师字段**（页面无载，网格对应格留白或写工程师学校学历，勿编）。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡呼应「交换舞伴」母题——成对圆点彼此交换后重新结对，暗示双键断开重连。
5. **表格语义化 + 公式框**（★ 每个核心贡献页必须使用）：`tabularx` 三列表格（表头主色白字、第一列强调色加粗、三列语义化如 问题 | 机理 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式框画金属卡宾 + 烯烃 → 金属杂环丁烷 → 新烯烃示意。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Yves Chauvin（中文惯称：伊夫·肖万；法语读音 [iv ʃovɛ̃]）
- **生卒**：1930-10-10 生于比利时 Menen（法国父母）→ 2015-01-27 逝于法国 Tours，享年 84
- **国籍**：France（法国）——生于比利时但国籍为法（infobox/metadata 均 France）；父为电气工程师
- **身份**：化学家、研究者；法国石油研究所（Institut français du pétrole）荣誉研究主任；法国科学院院士（2005 当选）
- **教育轨迹**：
  - École supérieure de chimie physique électronique de Lyon（里昂高等化学物理电子学院，ESCPE Lyon）1954 年毕业——**工程师学校出身，无博士学位**
  - 毕业后进入化学工业界，深感沮丧（frustrated）
- **导师**：页面无载（infobox 无 Doctoral advisor 一栏）——**禁编导师**
- **研究领域**：烯烃复分解（olefin metathesis）机理；均相催化；离子液体中的镍催化二聚

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **生于比利时门宁（1930）**：法国父母之子，父亲是电气工程师——战后欧洲工业世代的一分子。
2. **里昂工程师学校（1954）**：ESCPE Lyon 毕业；学历止步于此，却做出了令全世界博士仰望的机理突破。
3. **工业界的沮丧**：毕业后进入化工行业，自觉处处受限——"如果你要找新东西，就去找新东西……这种态度有风险，最小的失败也会闹得沸沸扬扬，但成功的喜悦值得冒险。"（页面明载引语，可引）
4. **加入法国石油研究所（1960）**：1960 年起任职于 Rueil-Malmaison 的 Institut français du pétrole——一生唯一的东家。
5. **1960s 均相催化练手**：丙烯聚合"调整期"动力学（1964，Martinato/Chauvin/Lefebvre，Comptes Rendus）；镍配合物二聚丙烯（1967，Uchino/Chauvin/Lefebvre）。
6. **1971 机理突破**：与 J. L. Hérisson 发表 *Makromol. Chem.* 141:161–176——烯烃复分解 = 金属卡宾双键 + 底物双键，经金属杂环丁烷（metallacyclobutane）环状中间体结合再裂分，两组分交换"片段"后各带新双键离去。
7. **舞伴比喻**：学者把这个反应比作两对舞伴拉手成环、再拆开重组为两对新舞伴——机理因此一目了然。
8. **五十年代的黑箱**：化学家 1950 年代就在做复分解，却不知反应如何发生；机理不清拖累了高效催化剂的寻找——Chauvin 的工作正是点亮黑箱。
9. **理论点亮灯塔**：Chauvin 的机理描述直接引导 Grubbs（钌）与 Schrock（钼/钨）开发出高效催化剂——Chauvin 是机理奠基人，两位实验者是催化剂实现者（分工勿混）。
10. **绿色红利**：三人的工作让制造商以更低的反应压力与温度、更少有害昂贵试剂、更少副产物与危废制造有机化合物（部分塑料与药品）——能耗更低。
11. **1990 离子液体先驱论文**：Chauvin/Gilbert/Guibard 在氯铝酸盐熔盐（离子液体）中实现镍催化烯烃二聚（*Chem. Comm.* 1990）。
12. **荣誉研究主任（1995）**：1995 年从石油研究所退休，获荣誉研究主任；另任里昂化学物理电子学院（CPE Lyon）荣休研究主任。
13. **2005 诺奖的尴尬与加冕**：因获奖感到窘迫、最初表示可能拒领；最终仍从瑞典国王手中受奖并发表诺奖演讲 *Olefin Metathesis: The Early Days*（2005-12-08）；同年当选法国科学院院士。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（钢蓝 steelblue） | `#37548D` | 石油化工与金属卡宾的冷峻（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（复分解机理 badgeMeta） | `#1B7A43` | 绿金属杂环丁烷 / 交换舞伴 |
| 分类色 2（均相催化 badgeCat） | `#2E5A9E` | 蓝镍配合物 / 二聚 |
| 分类色 3（离子液体 badgeIon） | `#D97B29` | 琥珀熔盐 / 1990 先驱论文 |
| 分类色 4（石油研究所 badgeIFP） | `#C0395B` | 玫瑰 IFP 三十五年 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（成对圆点互换位置），呼应「双键断开—重新结对」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**With Me** — Alex-Productions（`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/alex-productions/83-DXAblXgCK-k-With-Me.wav`；**不要复制 wav 文件**，Makefile 按此绝对路径引用）
- **风格**：温润 / 陪伴感 / 理性叙事
- **匹配理由**：
  - "With Me" 的陪伴感匹配「交换舞伴」母题——复分解的本质就是两对分子互换舞伴
  - 温润理性匹配工业研究所里安静做机理的学者气质（非学院派、非英雄史诗）
  - 片名亦呼应 2005 年他从"想拒领"到最终赴斯德哥尔摩受奖的释然
- **时长**：以实际文件为准 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 烯烃复分解的解码人 / Yves Chauvin 1930–2015 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/出生地/去世地/领域/荣誉；无博士导师字段）
03  肖万的一生 — Sanger 式时间线（10 节点：1930→1954→1960→1964→1967→1971→1990→1995→2005→2015）
04  早年：门宁与里昂 (1930–1954) — 表格「时间|事件|结果」
05  工业界与 IFP (1954–1960) — 表格「时间|事件|结果」+ 引语框："如果你要找新东西……"
06  1960s 均相催化 — 表格「体系|合作者|产物」
07  1971 机理突破 — 表格「黑箱|机理|结果」+ 公式框：金属卡宾 + 烯烃 → 金属杂环丁烷 → 交换产物
08  舞伴比喻 — 表格「步骤|类比|化学」
09  理论→催化剂：三人接力 — 表格「人物|金属|贡献」（Chauvin 机理 / Schrock Mo,W / Grubbs Ru）+ 绿色红利
10  1990 离子液体先驱 — 表格「体系|方法|意义」+ 公式框：氯铝酸盐熔盐镍催化二聚
11  荣誉与院士 — Sanger 式「类别|代表|意义」表格（诺奖 2005 / 法国科学院 2005 / Carl Engler Medal / 国家功勋勋章）
12  IFP 三十五年 — Sanger FFT 页式流程图（1960 加入 → 机理 → 1995 荣誉研究主任 → CPE Lyon 荣休）
13  遗产：更清洁的化学 — 四分类遗产盒 + 公式框：更低温度压力 / 更少危废
14  结尾 — 「看清一支舞的舞步，全世界的舞池都亮了。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 官方获奖理由 | **page.md 未载 2005 官方 citation 整句**——只可写"因 1970 年代初对烯烃复分解机理的工作与 Grubbs/Schrock 共享 2005 诺奖"（页面原句口径），勿杜撰 "for the development of the metathesis method in organic synthesis" 等页面无载的整句 |
| 三人分工 | Chauvin = 机理（1970s 初）；Schrock = 钼/钨催化剂；Grubbs = 钌催化剂——勿把催化剂发明安在 Chauvin 头上 |
| 国籍/出生 | 生于比利时 Menen、法国父母——国籍写法国，勿写"比利时化学家" |
| 卒日双值 | metadata 有 2015-01-28 与 2015-01-27 两值——以正文 27 January 2015 为准 |
| 学位 | 无博士学位（1954 工程师学校毕业）——勿编博士学历与博士导师 |
| 论文年份 | 1971 年 Hérisson–Chauvin 论文因原刊排印错误偶被引作 1970——写 1971 并加注 |
| 拒领风波 | 表述为"感到窘迫、最初表示可能拒领；最终从瑞典国王手中受奖并发表演讲"——勿写成"拒绝领奖" |
| 引语 | 唯一可引语为 "If you want to find something new..."（页面带引号明载）——其余一律间接转述 |
| 院士年份 | 法国科学院院士 2005 当选——勿提前 |
| 卒地 | Tours, France，享年 84——勿与出生地 Menen 混淆 |
| 诺奖演讲标题 | *Olefin Metathesis: The Early Days*（2005-12-08；2006 年刊于 Angew. Chem. Int. Ed. 45:3740–3747）——勿写错副题 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q202146 | ✅ |
| name_zh | 伊夫·肖万 | ✅ |
| name_en | Yves Chauvin | ✅（新建记录，库内无同名） |
| birth_date | 1930-10-10 | ✅ |
| death_date | 2015-01-27 | ✅（正文口径，弃 28 噪声值） |
| nationality | France | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | （metadata 无显式字段）；person_field 细分见下 | ✅ |
| has_biography | false（Beamer 立传后置 1） | ✅ |

person_field 细分（rank 表）：

| rank | field | 说明 |
|---|---|---|
| 0 | olefin metathesis | 一生主业：机理破译 |
| 1 | catalysis | 均相催化大框架 |
| 2 | organometallic chemistry | 金属卡宾 / 镍配合物 |
| 3 | polymer chemistry | 丙烯聚合与二聚论文 |

## 7. 社会关系入库清单

**共同得主（2005 三人两两互指）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Robert H. Grubbs | 无向 | 2005 诺贝尔化学奖共同得主（Grubbs 钌催化剂沿 Chauvin 机理开发） |
| co-honored | Richard R. Schrock | 无向 | 2005 诺贝尔化学奖共同得主（Schrock 钼/钨催化剂沿 Chauvin 机理开发） |

> **禁入库名单**：Martinato / Lefebvre / Uchino / Hérisson / Gilbert / Guibard / Basset / Niccolai / Magna（均为论文署名合作者，页面无个人关系叙述，仅列 publications）；infobox 无导师、无配偶、无子女记载。本篇 relations=2 为诚实值——页面关系叙述极少，勿硬凑。

## 8. 奖项清单

- Nobel Prize in Chemistry（2005，与 Grubbs/Schrock 共享）
- 法国科学院院士（2005 当选）
- Carl Engler Medal（年份页面无载，勿写）
- Grand Officer of the National Order of Merit / Grand Cross of the National Order of Merit（年份页面无载，勿写）
- Nobel Lecture（2005-12-08，*Olefin Metathesis: The Early Days*）

## 9. 机构清单

- 教育：École supérieure de chimie physique électronique de Lyon（1954 毕业）；里昂化学物理电子学院（CPE Lyon）荣休研究主任
- 任职：化学工业界（1954–1960，短暂而沮丧）；Institut français du pétrole（Rueil-Malmaison，1960–1995，退休后任荣誉研究主任）
- 荣誉机构：French Academy of Sciences（2005 当选）

## 10. 终审清单

- [x] 2005 三人共享 + 三人分工（机理/钼/钌）表述准确
- [x] 官方 citation 整句页面无载——间接口径，无杜撰
- [x] 卒日 2015-01-27（弃 metadata 28 噪声值）
- [x] 无博士学位、无导师——身份信息页如实留白
- [x] 1971 论文排印错误注记在位
- [x] 全篇唯一引语 "If you want to find something new..." 可在 page.md 溯源
- [x] 品牌 OpenMathAI、半角引号、封面国籍行、身份信息页齐备
- [x] `make distclean && make` 0 错误（Beamer 执行时验证）

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Yves_Chauvin/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/` 已就位（同框照裁剪或装饰圆占位，图注如实）
- [ ] **国籍**：封面顶部明示法国
- [ ] **引语核对**：仅 "If you want to find something new..." 一句带引号，可在原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一；法语名读音注 [iv ʃovɛ̃] 排版正常
- [ ] 与 21 世纪批次其他篇格式对齐
