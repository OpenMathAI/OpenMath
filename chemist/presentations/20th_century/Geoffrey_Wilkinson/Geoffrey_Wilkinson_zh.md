# Geoffrey Wilkinson（杰弗里·威尔金森）立传提示词

> qid=Q274128 · 1921-07-14 – 1996-09-26 · 英国化学家 · 诺贝尔化学奖（1973，与 Ernst Otto Fischer 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Geoffrey_Wilkinson/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 时间线页 + 表格语义化 tabularx + 公式展示框。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像按 `images.txt` 就位；page.md 页首有 "Wilkinson c. 1976" 照片，如已下载则用真实肖像；否则装饰圆占位并如实标注）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{atom}\enspace 均相催化的开路人\enspace·\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、国籍、出生地/去世地、教育（Imperial College）、博士（导师/论文）、博士后导师（Seaborg）、家庭（妻 Lise Schou）、核心领域、机构、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「夹心结构 / 催化循环」母题。
5. **表格语义化 + 公式框**（★ Sanger 版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如「Wilkinson 催化剂 $\mathrm{RhCl(PPh_3)_3}$」。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Sir Geoffrey Wilkinson（中文惯称：杰弗里·威尔金森；FRS；1976 年受封 Knight Bachelor）
- **生卒**：1921-07-14 生于英格兰约克郡西瑞丁 Todmorden 的 Springside → 1996-09-26 逝于伦敦，享年 75
- **国籍**：United Kingdom（英国）
- **身份**：化学家（chemist；无机化学与均相过渡金属催化的开拓者；1973 诺贝尔化学奖共同得主）
- **家庭**：父 Henry Wilkinson 为房屋油漆与装修工匠；母 Ruth 在当地棉纺厂做工；一位舅舅（管风琴师兼唱诗班指挥）娶了经营小型化工公司（为制药业生产泻盐 Epsom salts 与芒硝 Glauber's salts）之家——化学兴趣由此萌芽。娶 Lise Schou（丹麦植物生理学家，UC Berkeley 结识），二女 Anne 与 Pernille
- **教育轨迹**：
  - Todmorden 当地市立小学；1932 获 County Scholarship 入 Todmorden Grammar School（物理老师 Luke Sutcliffe 也教过"劈开原子"的诺奖得主 John Cockcroft）
  - 1939 获 Royal Scholarship 入 Imperial College London，1941 毕业
- **导师**：Henry Vincent Aird Briscoe（博士导师，infobox 明载）；Glenn T. Seaborg（博士后导师，infobox "Other academic advisors" 明载）
- **博士**：1946，《Some physico-chemical observations on hydrolysis in the homogeneous vapour phase》
- **研究领域**：无机化学——过渡金属配合物、均相催化、二茂铁结构、Wilkinson 催化剂

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **约克郡工匠之家（1921）**：油漆匠之子、棉纺厂母亲——化学启蒙来自舅舅姻亲的小化工厂（泻盐与芒硝）。
2. **考克饶夫的母校（1932–1939）**：County Scholarship 入 Todmorden Grammar School；物理老师 Sutcliffe 曾教过 John Cockcroft——小镇学校的诺奖传统。
3. **帝国理工与博士（1939–1946）**：Royal Scholarship 入 Imperial College；1941 毕业，1946 获 PhD（均相气相水解的物理化学观察）。
4. **核能项目（1942–1946）**：1942 年 Paneth 教授为核能项目招募青年化学家，Wilkinson 应征赴加拿大，先蒙特利尔后 Chalk River Laboratories，至 1946 年离开。
5. **Berkeley 四年（1946–1950）**：在 UC Berkeley 与 Glenn T. Seaborg 合作四年，主要做核分类学（nuclear taxonomy）——博士后阶段。
6. **MIT 回归本行**：任研究助理，回到学生时代的初心——CO 与烯烃等配体的过渡金属配合物。
7. **哈佛岁月（1951–1955）**：1951 年 9 月至 1955 年 12 月在哈佛（含 9 个月哥本哈根学术假）；仍做钴质子激发函数的核工作，但已转向烯烃配合物。
8. **帝国理工讲席（1955）**：1955 年 6 月出任 Imperial College 无机化学讲席教授，此后几乎全力研究过渡金属配合物。
9. **二茂铁结构**：与 Fischer（各自独立）给出二茂铁 Fe(C₅H₅)₂ 的夹心结构——本篇 page.md 口径 "the discovery of the structure of ferrocene"。
10. **Wilkinson 催化剂**：RhCl(PPh₃)₃ 在催化加氢中的推广使用；工业上用于烯烃加氢成烷烃——均相催化的命名性地标。
11. **名师与教科书**：指导博士生与博后 F. Albert Cotton、Richard A. Andersen、John A. Osborn、Alan Davison、Malcolm Green 等；与 Cotton 合著《Advanced Inorganic Chemistry》——人称 "Cotton and Wilkinson" 的标准教材。
12. **1973 诺贝尔化学奖**：与 Ernst Otto Fischer 共享，表彰其在有机金属化合物方面的工作（page.md 口径 "organometallic compounds"）。
13. **爵士与真话（1976–1996）**：1976 生日授勋受封 Knight Bachelor；虽为爵士却不自认"建制派"，公开批评历届首相、教育大臣与大学校长对科学的投入不足。1996-09-26 逝于伦敦；身后 RSC 设 Sir Geoffrey Wilkinson Prize（1999 起）、Imperial 设年度讲座（2022 起），由其女 Anne Hardy 经营的慈善基金会资助。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（普鲁士蓝 prussian） | `#16324F` | 过渡金属配合物的深蓝——无机化学的厚重（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（夹心结构 badgeSandwich） | `#1B7A43` | 绿二茂铁 Fe(C5H5)2 |
| 分类色 2（均相催化 badgeCatalysis） | `#D97B29` | 琥珀 Wilkinson 催化剂 / 加氢 |
| 分类色 3（学派与教材 badgeSchool） | `#C0395B` | 玫瑰 Cotton & Wilkinson 教科书 |
| 分类色 4（核能岁月 badgeNuclear） | `#7A3E9D` | 紫 Chalk River / Seaborg |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「两片环夹金属」的夹心几何与催化循环的闭环意象。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Winds Of Freedom** — Really Slow Motion & Giant Apes（文件 `25-l3Fsk4R6eys-Really Slow Motion & Giant Apes - Winds Of Freedom (Epic Heroic Orchestral).wav`）
- **风格**：英雄式管弦 / 开阔上行 / 长气息
- **匹配理由**：
  - "Winds Of Freedom" 的开阔管弦匹配从约克郡小镇经核能项目到帝国理工讲席的地理与学术跨越
  - 英雄式上行匹配 1973 诺奖与 Wilkinson 催化剂的产业落地
  - 长气息乐句匹配其"批判建制、直言不讳"的独立人格
- **时长**：以实际文件为准 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 均相催化的开路人 / Geoffrey Wilkinson 1921–1996 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/国籍/教育/博士/博士后导师/家庭/领域/荣誉）
03  威尔金森的一生 — Sanger 式时间线（10 节点：1921→1932→1939→1942→1946→1951→1955→1965→1973→1996）
04  约克郡少年 (1921–1939) — 表格「时间|事件|结果」（泻盐工厂启蒙 / Sutcliffe / Royal Scholarship）
05  帝国理工与核能项目 (1939–1946) — 表格「阶段|导师|成果」（PhD Briscoe / Chalk River）
06  Berkeley：Seaborg 门下 (1946–1950) — 表格「地点|合作|课题」+ 公式框：核分类学四年
07  MIT 与哈佛：回归配合物 (1950–1955) — 表格「机构|转向|成果」（CO 与烯烃配合物）
08  二茂铁的夹心结构 (1952–) — 表格「旧说|挑战|新解」+ 公式框：Fe(C5H5)2 夹心结构
09  Wilkinson 催化剂 — 表格「问题|方法|结果」+ 公式框：RhCl(PPh3)3 催化加氢，工业烯烃→烷烃
10  帝国理工讲席与学派 (1955–) — 表格「人物|方向|成果」（Cotton/Barron/Bennett/Davison/Green/Osborn）
11  1973 诺贝尔化学奖 — 与 Fischer 共享（co-honored）+ 授奖理由口径框
12  爵士与真话 — 1976 Knight Bachelor + 批评政府/大学投入（Sanger 式荣誉对照表）
13  荣誉与身后 — Royal Medal 1981 / Ludwig Mond 1981 / Davy Medal 1996 / RSC 奖与蓝色牌匾
14  结尾 — 「一勺铑配合物，让加氢在试管里温柔地进行。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 同名区分（最重要） | Geoffrey Wilkinson（1921–1996，无机化学，1973 化学诺奖）≠ James H. Wilkinson（1930–1986，数值分析家、1970 图灵奖）——立传与入库全程带教名 Geoffrey |
| 1973 诺奖口径 | 与 Ernst Otto Fischer 共享，page.md 仅载 "organometallic compounds"；官方完整 citation（含 "performed independently"、"sandwich compounds"）**本页无载**——引用以 page.md 为限 |
| 二茂铁归属 | 本篇 page.md 口径 "the discovery of the structure of ferrocene"；Fischer 篇口径为"质疑 Pauson/Kealy 并发表结构数据"——两篇各忠于本人页面，Review 勿强行统一为同一句式 |
| 二战服役 | 1942 由 Paneth 招募入**核能项目**赴加拿大（蒙特利尔/Chalk River）——是战时科研而非从军服役，勿写"参军" |
| 博士后导师 | Seaborg 是 "Other academic advisors (post doctoral advisor)"——为 Berkeley 四年博士后导师，勿写成博士导师（博士导师是 Briscoe） |
| 博士论文题目 | 《Some physico-chemical observations on hydrolysis in the homogeneous vapour phase》(1946)——infobox 正文一处作 "of"，论文题按 infobox 照录 |
| 爵位与批评并存 | 1976 受封 Knight Bachelor 与"公开批评首相/教育大臣/校长"并存——两者都写，勿只写荣衔 |
| 奖项年份 | Royal Medal 1981、Ludwig Mond Award 1981、Davy Medal 1996、Lavoisier Medal 1968（正文）——infobox Awards 列与正文年份一致处照录，勿提前或推后 |
| 配偶 | Lise Schou 丹麦植物生理学家、Berkeley 结识、二女 Anne 与 Pernille——实载可写；Anne Hardy 是其女（页载 "run by Professor Anne Hardy, one of Wilkinson's daughters"） |
| 学生名单 | infobox Doctoral students 六人（Cotton、Barron、Bennett、Davison、Green、Osborn）+ Other notable students Andersen（postdoc）——按 infobox 全收；正文另提 Andersen 为 postdoc 与 Osborn/Davison/Green/Cotton，与 infobox 一致 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q274128 | ✅ |
| name_zh | 杰弗里·威尔金森 | ✅ |
| name_en | Geoffrey Wilkinson | ✅ |
| birth_date | 1921-07-14 | ✅ |
| death_date | 1996-09-26 | ✅ |
| nationality | United Kingdom | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | inorganic chemistry（person_field 细分见下表，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

**person_field 细分 rank 表**：

| rank | name_en | name_zh |
|---|---|---|
| 0 | inorganic chemistry | 无机化学 |
| 1 | homogeneous catalysis | 均相催化 |
| 2 | organometallic chemistry | 金属有机化学 |
| 3 | ferrocene | 二茂铁 |

## 7. 社会关系入库清单

**红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Henry Vincent Aird Briscoe | 师→生（direction=advisor） | Imperial College 博士导师，1946 PhD |
| advisor-student | Glenn T. Seaborg | 师→生（direction=advisor） | UC Berkeley 博士后导师（1946–1950，核分类学） |
| advisor-student | F. Albert Cotton | 生→师（direction=student） | 博士生；后合著《Advanced Inorganic Chemistry》 |
| advisor-student | Andrew R. Barron | 生→师（direction=student） | 博士生（infobox Doctoral students） |
| advisor-student | Martin A. Bennett | 生→师（direction=student） | 博士生（infobox Doctoral students） |
| advisor-student | Alan Davison | 生→师（direction=student） | 博士生（infobox Doctoral students） |
| advisor-student | Malcolm Green | 生→师（direction=student） | 博士生；1999 首届 Sir Geoffrey Wilkinson Prize 得主 |
| advisor-student | John A. Osborn | 生→师（direction=student） | 博士生（infobox Doctoral students） |
| advisor-student | Richard A. Andersen | 生→师（direction=student） | 博士后（infobox Other notable students） |
| colleague | Friedrich Paneth | 无向 | 1942 为核能项目招募 Wilkinson 赴加拿大 |
| spouse | Lise Schou | 无向 | 丹麦植物生理学家，UC Berkeley 结识，二女 |
| co-honored | Ernst Otto Fischer | 无向 | 1973 诺贝尔化学奖共同得主 |

> 禁入库名单：Luke Sutcliffe（中学物理老师，仅"也教过 Cockcroft"轶事，非关系类型白名单内、非研究生导师）、John Cockcroft（同校轶事，不入库）、Henry Wilkinson / Ruth Wilkinson（父母——infobox 与正文实载，如需可按 parent-child 入库；本表默认不收以控制噪声，若立传需要可补 parent-child 两行）——除明示外均不入库。

## 8. 奖项清单

- Nobel Prize in Chemistry（1973，与 Ernst Otto Fischer 共享）
- Fellow of the Royal Society，FRS（1965 当选）
- Lavoisier Medal，法国化学会（1968）
- Royal Medal，皇家学会（1981）
- Ludwig Mond Award，皇家化学会（1981）
- Davy Medal（1996）
- American Chemical Society Award in Inorganic Chemistry；Longstaff Prize；Guggenheim Fellowship（metadata.json 明载）
- Knight Bachelor（1976 Birthday Honours，女王伊丽莎白二世册封）
- 荣誉博士/院士：Columbia University DSc（1978）、University of Bath DSc（1980）、University of Essex（1989）、Imperial College Honorary Fellowship（1993）、University of Granada（metadata.json 明载）
- 身后纪念：RSC Sir Geoffrey Wilkinson Prize（1999 起）、Imperial 年度讲座（2022 起）、蓝色牌匾（Todmorden 1990 / Imperial 2007）、Wilkinson Hall（2009）

## 9. 机构清单

- 教育：Todmorden 市立小学、Todmorden Grammar School（1932–1939）、Imperial College London（1939–1946，BSc 1941、PhD 1946）
- 任职：Montreal 与 Chalk River Laboratories（1942–1946，核能项目）→ UC Berkeley（1946–1950，Seaborg 组）→ MIT（研究助理）→ Harvard University（1951-09–1955-12，含 9 个月哥本哈根学术假）→ Imperial College London 无机化学讲席教授（1955-06 起）

## 10. 终审清单

- [ ] 生卒 1921-07-14 / 1996-09-26，享年 75；出生地 Todmorden、去世地伦敦
- [ ] 1973 与 Fischer 共享表述准确；诺奖理由以 page.md 口径为准
- [ ] 与 James H. Wilkinson（图灵奖）同名区分明确
- [ ] 博士导师 Briscoe / 博士后导师 Seaborg 方向不混
- [ ] 二战经历写"核能项目"非"服役"
- [ ] 学生名单按 infobox 六人 + postdoc Andersen，不多收
- [ ] 引语全部可在本地 Wikipedia 原文找到；无直接引语时不出现引号原话
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Geoffrey_Wilkinson/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：按 `images.txt` 核对肖像（页首 c. 1976 照片）；无真实肖像用装饰圆占位并如实标注
- [ ] **国籍**：封面顶部明示英国
- [ ] **引语核对**：本页无直接引语，一律间接转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批 Fischer 篇互查：1973 共享口径、二茂铁归属表述两篇一致
