# Alexey Ekimov（阿列克谢·叶基莫夫）立传提示词

> qid=Q1547368 · 1945 生于列宁格勒（苏联，在世；frontmatter 具体日 1945-02-28，正文仅记 1945 年） · 俄罗斯固态物理学家 · 21 世纪 · 诺贝尔化学奖（2023，与 Brus、Bawendi 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Alexey_Ekimov/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**对齐 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。`images.txt` 为空；infobox 有 "Ekimov in 2023" 实照——执行时经 Wikipedia REST API `page/summary` 查 infobox 原图名回退下载（250px 改 500px，`curl -A "Mozilla/5.0"` + `file` 验证），失败则用主色装饰圆占位。
2. **封面有国籍**：顶部副标题明示（`\faIcon{eye}\enspace` 玻璃里看见量子尺寸的人`\enspace·\enspace` 俄罗斯），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。国籍口径：封面写"俄罗斯"；苏联出身背景放身份信息页（生于列宁格勒/苏联）。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生年、本名俄文（Алексей Екимов）、国籍变迁、出生地、教育（列宁格勒大学/Ioffe 研究所）、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「玻璃中的纳米晶」母题——大小错落的圆点即 CuCl 微晶，越小越蓝。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）——核心页必须呈现「晶粒越小 → 玻璃越蓝」的量子尺寸效应链。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Alexey Ekimov / Aleksey Yekimov（俄文：Алексей Екимов；中文惯称：阿列克谢·叶基莫夫）
- **生年**：1945 生于列宁格勒（苏联；正文仅记年份，metadata.json 记 1945-02-28——正文为准取 1945 年，具体日期可在身份页加注）
- **国籍变迁**：Soviet Union（苏联）→ Russia（俄罗斯）→ United States（1999 起旅居美国工作）
- **身份**：固态物理学家（solid state physicist）、纳米材料研究先驱；2023 诺贝尔化学奖三人共享得主之一（以物理学家身份获化学奖）
- **教育轨迹**：
  - 列宁格勒国立大学物理系（1967 毕业，BS）
  - Ioffe 研究所（俄罗斯科学院）：物理学 PhD（1974），论文 Quantum Dimensional Phenomena in Semiconductor Microcrystals（1989，俄文 Квантовые размерные явления в полупроводниковых микрокристаллах）
- **师承**：页面与 infobox **均无载博士导师**——严禁编造
- **研究领域**：固态物理 / chemical physics、纳米材料、半导体激活玻璃

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **战后世代的列宁格勒（1945）**：生于围城解除当年的列宁格勒，苏联物理学传统中成长。
2. **列宁格勒大学物理系（1967）**：本科毕业，进入苏联科学院体系。
3. **Ioffe 研究所 PhD（1974）**：俄罗斯科学院 Ioffe 研究所物理学博士。
4. **电子自旋取向研究（1970s）**：因半导体中电子自旋取向（spintronics 方向）工作获 1975 苏联国家科学与工程奖。
5. **转入 Vavilov 国家光学研究所**：毕业后移步 Vavilov State Optical Institute，开始研究半导体激活玻璃（Schott glasses）并发展解释其颜色的理论。
6. **玻璃变色的物理（1970s–80s）**：玻璃加热再冷却后析出 CuCl 晶体（X 射线证实），产生蓝色——**晶粒越小，玻璃越蓝**。
7. **1981 首发量子尺寸效应（★核心）**：与 Alexei A. Onushchenko 在 JETP Letters 报道 CuCl 纳米晶中的量子尺寸效应——即今天所称 quantum dots 的发现。
8. **量子限域理论（1980s）**：与 Alexander Efros 共同发展量子限域（quantum confinement）理论。
9. **1985 理论深化**：与 Efros、Onushchenko 发表 Solid State Communications 论文，系统阐述半导体微晶中的量子尺寸效应。
10. **冷战之墙**：其研究在西方难以获得——直到 1990 年 Brus 才终于与 Ekimov、Efros 见面（此为 Brus 页面交叉叙事，本篇从 Ekimov 视角写"先行者与缺席的掌声"）。
11. **1993 CdSe 精密谱学**：与 Hache、Flytzanis、Efros 等发表 CdSe 量子点吸收与强度依赖光致发光测量（JOSA B）——玻璃体系与胶体体系合流。
12. **旅美（1999–）**：1999 起在美国纽约州的 Nanocrystals Technology 公司任科学家，居住工作至今。
13. **2023 诺贝尔化学奖**：与 Louis E. Brus、Moungi Bawendi 共享，官方理由 "for the discovery and synthesis of quantum dots"——以物理学家身份获化学奖，实至名归的"第一个看见的人"。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（靛紫 indigoviolet） | `#52307C` | 玻璃深处 CuCl 微晶折射的靛紫（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（玻璃光学 badgeGlass） | `#1E5E8C` | 青蓝 Schott 玻璃 / CuCl 析晶 |
| 分类色 2（量子尺寸效应 badgeSize） | `#B3462E` | 橙红晶粒越小越蓝的尺寸谱 |
| 分类色 3（量子限域理论 badgeConfine） | `#2E7D4F` | 绿 Efros 共同理论 |
| 分类色 4（冷战与迟到 badgeWall） | `#8C6A2F` | 暗金铁幕延迟的承认 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「玻璃中的纳米晶」——粒径决定蓝色的深浅。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**SEA** — Alex-Productions（源文件 `music_audio/alex-productions/92-WEqfdRXU3IU-SEA.wav`，执行时软链/复制至本目录，不复制 wav 入库）
- **风格**：辽阔 / 深沉 / 长距离叙事
- **匹配理由**：
  - "辽阔深沉" 匹配先行者的孤独——1981 年在玻璃里看见量子尺寸效应，掌声却迟到了四十年
  - "长距离" 匹配地理与体制的跨越——列宁格勒 → 莫斯科体系 → 1999 旅美，冷战东西两侧的科学接力
  - 海的意象呼应"颜色随尺寸漂移"的光谱——从红到蓝的漫长位移
- **时长**：执行时用 ffprobe 核对 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 玻璃里看见量子尺寸的人 / Alexey Ekimov 1945– + 四色 badge + 右上头像 + 国籍行（俄罗斯）
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生年/俄文本名/国籍变迁/出生地/教育/领域/荣誉）
03  叶基莫夫的一生 — 时间线（10 节点：1945→1967→1974→1975→1981→1985→1990→1993→1999→2023）
04  列宁格勒与 Ioffe (1945–1974) — 表格「时间|事件|结果」
05  自旋取向与苏联国家奖 (1975) — 表格「方向|内容|结果」+ 公式框：半导体电子自旋取向
06  Vavilov：玻璃之谜 (1970s–80s) — 表格「问题|方法|结果」（Schott 玻璃/X 射线/CuCl）
07  1981 首发 (★核心) — 表格「观察|解释|结果」+ 公式框：晶粒越小 → 玻璃越蓝（量子尺寸效应）
08  量子限域理论 (1985) — 表格「问题|合作者|结果」+ Efros/Onushchenko
09  冷战之墙与 1990 会合 — 表格「人物|事件|结果」（Brus 视角交叉叙事）
10  1993 CdSe 谱学与合流 — 表格「体系|测量|结果」（玻璃 vs 胶体）
11  旅美与产业 (1999–) — 表格「时间|事件|结果」（Nanocrystals Technology）
12  荣誉清单 — 「类别|代表|意义」表格 + itemize（USSR State Prize 1975 / Wood 2006 / Nobel 2023）
13  三人接力 — 流程图：Ekimov 1981 玻璃 → Brus 1982 溶液 → Bawendi 1993 合成
14  结尾 — 「第一个在玻璃里看见量子的人。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2023 诺奖共享口径 | 与 **Brus、Bawendi 三人共享**，官方理由 "for the discovery and synthesis of quantum dots"——勿写"独享" |
| 三人分工 | Ekimov（**1981 玻璃中首发**）→ Brus（1982 溶液/胶体 + 理论）→ Bawendi（1993 合成法）——本篇"发现"锚定 1981 CuCl 玻璃体系 |
| USSR State Prize 年份 | 正文记 **1975**（"1975 USSR State Prize in Science and Engineering"，自旋取向工作）；infobox 奖项列作 (1976)——**以正文 1975 为准**，可加注 infobox 差异 |
| 奖项获奖理由 | 国家奖理由是**电子自旋取向（spintronics 方向）**，勿写成"因量子点获苏联国家奖" |
| 博士导师 | 页面与 infobox **均无载**——严禁编造导师；PhD 单位是 Ioffe 研究所（1974） |
| 博士论文年份 | 论文条目标 1989（ProQuest 记录），PhD 学位 1974——两处年份并存须分开表述，勿混 |
| 姓名拼写 | Alexey Ekimov / Aleksey Yekimov / Алексей Екимов 三种形式并列（页面第一段明载）；Nobelprize.org 用 Aleksey Yekimov——正文用 Alexey Ekimov，封面可加俄文 |
| Onushchenko 名字 | 1981 论文合作者 **Alexei A. Onushchenko**——勿写成 Efros；Efros 是理论合作者（1985） |
| 化学奖给物理学家 | Ekimov 是固态物理学家获化学奖——叙事口径照实写，勿拔高为化学家 |
| 页面无载禁写 | 页面无家庭/配偶/子女、无直接引语、无 2023 后近况细节——一律不写；全文不编引语，改间接转述 |
| 页面无载禁写（国籍日） | 出生仅记 1945 年（列宁格勒）；metadata 的 1945-02-28 只作脚注，正文用"1945 年" |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q1547368 | ✅ |
| name_zh | 阿列克谢·叶基莫夫 | ✅ |
| name_en | Alexey Ekimov | ✅ |
| birth_date | 1945-02-28（metadata；正文仅 1945 年——库取 frontmatter 全日期，提示词正文口径"1945 年"） | ✅ |
| death_date | （在世，留空） | ✅ |
| nationality | Soviet Union / Russia / United States（rank 0/1/2） | ✅ |
| primary_occupation | physicist | ✅ |
| field_of_work | solid-state physics（person_field 细分：solid-state physics / quantum dots / nanomaterials / chemical physics，带 rank） | ✅ |
| has_biography | false（Beamer 立传完成后再置 1） | ✅ |

## 7. 社会关系入库清单

**合作者 / 共同得主**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Alexei A. Onushchenko | 无向 | 1981 玻璃中量子尺寸效应共同发现者，JETP Letters 共同作者 |
| colleague | Alexander Efros | 无向 | 共同发展量子限域理论；2006 R. W. Wood Prize 共同得主 |
| co-honored | Louis E. Brus | 无向 | 2023 诺贝尔化学奖共同得主；2006 R. W. Wood Prize 共同得主 |
| co-honored | Moungi Bawendi | 无向 | 2023 诺贝尔化学奖共同得主 |

> 页面与 infobox 均无载博士导师、家庭、配偶——**无对应关系可入库，禁写**。
> 注：Onushchenko / Efros 均为库内新建 stub，按本表规范全名建。

## 8. 奖项清单

- USSR State Prize in Science and Engineering（1975，电子自旋取向；infobox 作 1976，以正文为准）
- R. W. Wood Prize（2006，与 Efros、Brus 共享，"discovery of nanocrystal quantum dots and pioneering studies of their electronic and optical properties"）
- Nobel Prize in Chemistry（2023，与 Brus/Bawendi 共享，"for the discovery and synthesis of quantum dots"）

## 9. 机构清单

- 教育：列宁格勒国立大学物理系（–1967，BS）；Ioffe 研究所（俄罗斯科学院，PhD 1974）
- 任职：Vavilov State Optical Institute（–1999，Schott 玻璃 / CuCl 纳米晶研究）；Nanocrystals Technology（1999–，纽约州公司科学家）
- 无其他教职载录——勿编造大学教授身份（页面未载）

## 10. 终审清单

- [ ] 生年 1945（列宁格勒）；metadata 全日期仅作脚注
- [ ] 1981 首发作者序 Ekimov/Onushchenko；量子限域理论合作者 Efros
- [ ] USSR State Prize 1975（正文口径，infobox 1976 加注）；获奖理由是自旋取向
- [ ] 2023 三人共享口径与官方理由英文原文无误；三人接力分工准确
- [ ] 博士导师留空（页面无载）；无任何编造引语
- [ ] `make distclean && make` 编译通过，0 错误，vbox≤10pt / hbox≤50pt

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Alexey_Ekimov/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：经 REST API 回退下载 infobox 2023 实照；失败则装饰圆占位并注记
- [ ] 国籍：封面明示"俄罗斯"；苏联/俄/美三段国籍在身份页呈现
- [ ] 引语核对：全文无直接引语（页面无载）——检查无编造"原话"
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox≤10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一；俄文本名 Алексей Екимов 的字体渲染（xelatex 需西里尔字体族，参考 Adi_Shamir 希伯来名做法）
- [ ] 与化学家侧既有格式对齐；结尾品牌 OpenMathAI

---

> **名单状态**：`chemist/generate_21th_century_list.py` 更新由主控统一收尾，本文件不改动生成器。
