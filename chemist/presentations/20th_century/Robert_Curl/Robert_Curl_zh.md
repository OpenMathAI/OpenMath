# Robert Curl（罗伯特·柯尔）立传提示词

> qid=Q110930 · 1933-08-23 – 2022-07-03 · 美国化学家 · 20 世纪 · 诺贝尔化学奖（1996，三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Robert_Curl/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。本地 images.txt 无可用肖像（仅 Wikiquote 图标）：先经 Wikipedia REST API `page/summary` 查 infobox 实际文件名（页面注明 "Curl in 2009"）下载，404 则用装饰圆占位（图注须如实）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{atom}\enspace C60 的光谱学家\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「碳笼 / 足球烯」母题——圆点暗示笼状碳分子与质谱峰。
5. **表格语义化 + 公式框**（★ Sanger 版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如 `C60`（12 个五边形 + 20 个六边形，足球对称性；质谱单一主峰 → 化学惰性、几何封闭、无悬键）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Robert Floyd Curl Jr.（中文惯称：罗伯特·柯尔；Rice 大学 Pitzer–Schlumberger 自然科学讲席教授）
- **生卒**：1933-08-23 生于得州 Alice（美国）→ 2022-07-03 逝于得州 Houston，享年 88
- **国籍**：United States（美国）
- **身份**：化学家（Rice University 化学教授；1996 诺贝尔化学奖得主）
- **家庭**：卫理公会牧师之子；因父亲传教，全家在南/西南得州多次迁居，其父参与创办圣安东尼奥医学中心的卫理公会医院。1955 年娶 Jonel Whipple，育二子；每周与 Rice Bridge Brigade 打桥牌、骑车通勤
- **教育轨迹**：
  - 9 岁得化学实验箱（硝酸煮溢毁掉母亲瓷炉漆面——化学兴趣的起点）
  - Thomas Jefferson High School（圣安东尼奥；高中只有一年化学课，高年级教师另给专题项目）
  - Rice Institute（今 Rice University）化学 BA（1954；慕其学术与橄榄球队之名，且当时免学费）
  - University of California, Berkeley 化学博士（1957）
- **导师**：Kenneth Pitzer（博士导师，时任伯克利化学学院院长；后成终身合作者）
- **博士**：1957，《Some spectroscopic and thermodynamic properties of molecules》（红外光谱测定 disiloxane 键角）
- **研究领域**：红外与微波光谱、自由基检测与分析、富勒烯发现；晚期转向物理化学、DNA 基因分型/测序仪器与量子级联激光光声痕量气体传感器

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **牧师之子的化学箱（1933–1951）**：得州小城、迁居童年；9 岁的化学实验箱与"毁掉瓷炉"的事故——兴趣原点。
2. **免学费的 Rice（1950–1954）**：为学术声誉、橄榄球队与免学费入 Rice Institute，1954 化学BA。
3. **伯克利岁月（1954–1957）**：师从 Kenneth Pitzer 测 disiloxane 键角；与导师结成终身合作。
4. **哈佛博士后（1957–1958）**：随 E. B. Wilson 用微波谱研究分子内旋转势垒。
5. **回 Rice 执教（1958）**：接手离校去 Polaroid 的 George Bird 的设备与研究生；早期研究二氧化氯微波谱。
6. **自由基光谱纲领（1960s–80s）**：微波谱+可调激光检测分析自由基，发展其精细/超精细结构理论与反应动力学。
7. **引来 Smalley（1976）**：Curl 的研究吸引 Richard Smalley 来 Rice 谋求合作——日后 C60 团队的另一半。
8. **Kroto 来电（1985）**：Harry Kroto 想借 Smalley 的激光装置模拟红巨星碳链形成；两人当时正用该装置研究硅锗半导体，起初不情愿、最终让步。
9. **11 天定结构（1985）**：如愿找到长碳链，意外得 60 碳产物；11 天内确定结构，因与 Buckminster Fuller 网格穹顶相似而命名 buckminsterfullerene；依据仅是质谱上单一主峰——推出化学惰性、几何封闭、无悬键。
10. **Curl 的分工**：负责装置内碳蒸气的最优条件与谱图检查；并指出研究生 James R. Heath 与 Sean C. O'Brien 当得与 Kroto/Smalley 同等荣誉。
11. **1996 诺贝尔化学奖**：与 Richard Smalley（同为 Rice）、Harold Kroto（Sussex）共享——官方口径 "for the discovery of the nanomaterial buckminsterfullerene, and hence the fullerene class of materials"（页面实载）。
12. **诺奖后的低姿态（可引语）**：页面实载原句 "After winning a Nobel, you can either become a scientific pontificator... Or you can say, 'Well, I enjoy what I was doing, and I want to keep doing that.'"——向校长提的唯一要求是办公室附近加一个自行车架。
13. **晚年与谢幕（2008–2022）**：DNA 基因分型仪器与量子级联激光光声传感器；Rice 第一任 Lovett College 院长；2008 年 74 岁退休；2022-07-03 逝于 Houston。1985 年 C60 论文 2015 获 ACS 化学史分会 Citation for Chemical Breakthrough Award，2010 年被 ACS 定为 National Historic Chemical Landmark。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（碳笼深绿 fullerenedeep） | `#1E5631` | 碳的第三种同素异形体与谦逊的大师（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（分子光谱 badgeSpec） | `#1E4E79` | 蓝微波/红外谱 / 自由基 |
| 分类色 2（C60 发现 badgeC60） | `#B07A2A` | 琥珀 11 天定结构 / 质谱单峰 |
| 分类色 3（合作与荣誉 badgeTeam） | `#5B2A86` | 紫 Kroto 来电 / Heath 与 O'Brien |
| 分类色 4（晚年新域 badgeLate） | `#8A1E2D` | 猩红痕量气体传感 / DNA 测序仪器 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「碳笼 / 足球烯」的封闭曲面。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**The Flow of Time** — Alex-Productions（清单指定，文件 `music_audio/alex-productions/35-jqIDnltiDRI-The-Flow-of-Time.wav`；不要复制 wav 文件）
- **风格**：舒缓 / 时间流逝 / 沉静回望
- **匹配理由**：
  - "时间之流" 匹配其学术节奏——从 1954 本科到 2008 退休一甲子坚守 Rice 一校
  - "沉静" 匹配其性格——诺奖后拒绝布道、只求一个自行车架的低调
  - "回望" 匹配传记叙事——牧师之子 → 伯克利 → 自由基光谱 → C60 的 11 天 → 88 岁谢幕
- **时长**：以实际曲目时长为准，不足/超出由 ffmpeg `-shortest` 对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — C60 的光谱学家 / Robert Curl 1933–2022 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  柯尔的一生 — Sanger 式时间线（10 节点：1933→1954→1957→1958→1976→1985→1996→2001→2008→2022）
04  早年：牧师之子与化学箱 (1933–1954) — 表格「时间|事件|结果」
05  伯克利与哈佛：光谱学训练 (1954–1958) — 表格「时间|事件|结果」
06  自由基光谱纲领 (1958–1985) — 表格「对象|方法|结果」
07  C60：11 天的发现 (1985) — 表格「问题|方法|结果」+ 公式框：C60 = 12 五边形 + 20 六边形 · 质谱单峰
08  1996 诺贝尔化学奖 — 三人共享页（Curl/Smalley 同校 + Kroto 异校）+ 公式框：获奖口径
09  诺奖后的低姿态 — 引语页（"After winning a Nobel..." + 自行车架轶事）
10  晚年研究 (1996–2008) — 表格「方向|技术|结果」（DNA 分型 / 光声痕量气体传感器）
11  荣誉清单 — Sanger 式「类别|代表|意义」表格（Clayton 1957 → Citation for Chemical Breakthrough 2015）
12  遗产与纪念 — ACS National Historic Chemical Landmark（2010）/ Citation for Chemical Breakthrough（2015）/ Smalley-Curl Institute 流程图页
13  同事与学生 — 表格「人物|关系|结果」（Pitzer / Wilson / Smalley / Kroto / Kinsey / Wang）
14  结尾 — 「他测了一辈子光谱，只为听见分子最诚实的形状。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1996 共享口径 | 与 **Richard Smalley（Rice）与 Harold Kroto（Sussex）** 三人共享；获奖口径照页面 "discovery of the nanomaterial buckminsterfullerene, and hence the fullerene class of materials" |
| 命名归属 | **三页三口径**：Curl 页作团队命名（named it after geodesic domes）、Kroto 页作 Kroto 命名、Smalley 页作 Smalley 命名——**Curl 篇按 Curl 页写"团队命名"，勿跨页混写** |
| Heath / O'Brien | Curl 明言二人 "deserve equal recognition"；诺奖仅授三人——如实并写，勿升格为"第四位得主" |
| 结构依据 | C60 结构推断**仅基于质谱单一主峰**（惰性、封闭、无悬键），1985 年时团队不知道此前已有理论预言——照页面写 |
| 时间线 | 意外产物出现后 **11 天**确定结构；勿写"数月" |
| 本科校名 | 1954 年时称 **Rice Institute**（今 Rice University）——照页面写法 |
| 博士后导师 | E. B. Wilson（Edgar Bright Wilson，哈佛微波谱大家）——勿与其他 Wilson（如 R. W. Wilson）混淆 |
| 高中毕业年龄 | "16 岁前毕业"是 **Rowland** 的记载，Curl 页面无此说——勿串写 |
| 低姿态口径 | "自行车架"轶事与引语均为页面实载；Smalley（纳米技术布道）与 Kroto（科学教育）的不同选择是对照面，勿写成 Curl 参与其中 |
| Lovett College | Curl 是 Lovett College **第一任院长**（residential college 系统）——勿写"创办者" |
| 去世 | 2022-07-03 逝于 Houston，享年 88——页面未载死因细节，勿编造 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q110930 | ✅ |
| name_zh | 罗伯特·柯尔 | ✅ |
| name_en | Robert Curl | ✅ |
| birth_date | 1933-08-23 | ✅ |
| death_date | 2022-07-03 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | microwave spectroscopy（person_field 细分：microwave spectroscopy / infrared spectroscopy / fullerene / physical chemistry，带 rank） | ✅ |
| has_biography | false（立传完成后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 同事 / 共同得主 / 门生**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Kenneth Pitzer | 师→生（博士导师） | 伯克利，disiloxane 键角；后成终身合作者 |
| advisor-student | Edgar Bright Wilson | 师→生（博士后导师） | 哈佛博士后，微波谱研究内旋转势垒 |
| advisor-student | James L. Kinsey | Curl → 学生 | infobox 博士生 |
| advisor-student | Lihong V. Wang | Curl → 学生 | infobox 博士生 |
| colleague | Richard Smalley | 无向 | Curl 的研究吸引其 1976 年来 Rice 合作 |
| colleague | Harry Kroto | 无向 | 1985 年 Kroto 提出借用激光装置研究红巨星碳链 |
| co-honored | Richard Smalley | 无向 | 1996 诺贝尔化学奖共同得主 |
| co-honored | Harry Kroto | 无向 | 1996 诺贝尔化学奖共同得主 |
| colleague | James R. Heath | 无向 | C60 论文合作研究生，Curl 称其当得同等荣誉，后任 Caltech 教授 |
| spouse | Jonel Whipple | 无向 | 1955 年结婚，育二子 |

> **禁入库名单（metadata.json-only 或防噪声）**：Sean C. O'Brien（红链，仅 C60 论文合作者记载）；Yuan Liu（Curl 页无载）；George Bird（前任教授，仅"继承设备与学生"一句）；Raoul Kopelman 等他人页人物；两名子女（页面未具名细节）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1996，与 Smalley/Kroto 共享）
- Clayton Prize, Institute of Mechanical Engineers（1957）
- Alexander von Humboldt Senior US Scientist Award, University of Bonn（1984）
- APS International Prize for New Materials（1992）
- Fellow of the National Academy of Sciences（1997）
- Golden Plate Award of the American Academy of Achievement（1997）
- Fellow of the American Academy of Arts and Sciences（1998）
- Johannes Marcus Marci Award in Spectroscopy（1998）
- Centenary Medal, Royal Society of Chemistry（1999）
- Honorary Fellow, The Royal Society of New Zealand（2001）
- University of Bochum Research Prize（2004）
- National Historic Chemical Landmark, American Chemical Society（2010）
- Citation for Chemical Breakthrough Award, ACS Division of History of Chemistry（2015）
- Humboldt Research Fellowship；Humboldt Prize；James C. McGroddy Prize for New Materials；Carbon Medal；Fellow of the Optical Society of America（metadata 列出，正文未载年份——照实标注）

## 9. 机构清单

- 教育：Thomas Jefferson High School（圣安东尼奥）→ Rice Institute（BA 1954）→ University of California, Berkeley（PhD 1957）
- 任职：Harvard University（博士后，1957–1958）→ Rice University（1958–，Pitzer–Schlumberger 自然科学讲席教授；2008 年 74 岁退休）
- 服务：Rice Quantum Institute / Lovett College 第一任院长
- 命名遗产：Rice 的 Smalley-Curl Institute（2015 年由 CNST 与 RQI 合并而成）；C60 发现地 2010 年被 ACS 定为 National Historic Chemical Landmark

## 10. 终审清单

- [x] 生卒 1933-08-23 / 2022-07-03，享年 88，出生地 Alice, Texas、去世地 Houston
- [x] 1996 三人共享（Smalley/Kroto）表述准确；命名归属按 Curl 页"团队命名"口径
- [x] Heath/O'Brien "equal recognition" 表述准确且未升格
- [x] 博士导师 Pitzer、博士后导师 E. B. Wilson 表述准确
- [x] "11 天定结构 / 质谱单峰 / 不知此前理论预言" 三处口径准确
- [x] 引语全部可在本地 Wikipedia 原文找到（诺奖后三种选择原句、自行车架轶事）
- [x] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Robert_Curl/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：按 §0.1 回退处理（REST API → 装饰圆），图注如实
- [ ] **国籍**：封面顶部明示美国
- [ ] **引语核对**：诺奖后三种选择的原句必须在 Wikipedia 原文找到
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
