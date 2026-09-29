# Thomas Cech（托马斯·切赫）立传提示词

> qid=Q135180 · 1947-12-08 –（在世）· 美国化学家/生物化学家 · 20 世纪 · 诺贝尔化学奖（1989，与 Sidney Altman 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Thomas_Cech/`（page.md + metadata.json）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。肖像用 Wikipedia "Cech in 2005"；下载失败用装饰圆占位并如实标注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{dna}\enspace会剪接自己的 RNA\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（Thomas Robert Cech）、国籍、出生地、教育、博士导师、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「RNA 自剪接 / 内含子飞出」母题。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如 rRNA 前体 − 内含子 → 成熟 rRNA（无蛋白参与）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Thomas Robert Cech（中文惯称：托马斯·切赫；姓氏发音 "check"）
- **生卒**：1947-12-08 生于美国芝加哥 → 在世（页面无卒日）
- **国籍**：United States（美国）；祖辈为捷克移民（祖父捷克人，其余祖父母为第一代美国移民）
- **身份**：化学家 / 生物化学家；科罗拉多大学博尔德分校生物化学系特聘教授；HHMI 前总裁
- **家庭与成长**：在艾奥瓦城（Iowa City）长大；初中就敲开爱荷华大学地质系教授的门，请教晶体结构、陨石与化石
- **配偶**：大学有机化学实验搭档 Carol Lynn Martinson——后成婚（正文明载）
- **教育轨迹**：
  - National Merit Scholar；1966 入 Grinnell College，读过《奥德赛》《神曲·地狱篇》、宪政史与化学
  - Grinnell College B.A.（1970）
  - UC Berkeley 化学博士（1975）；同年赴 MIT 做博士后
- **博士**：1975 年 UC Berkeley；导师 John E. Hearst；论文《Characterization of the most rapidly renaturing sequences in the main band DNA of the mouse (Mus musculus)》（小鼠主带 DNA 快速复性序列的表征）
- **研究领域**：生物化学——RNA 剪接与核酶、端粒与端粒酶（TERT）、转录、癌症生物学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **敲教授门的初中生（约 1960 初）**：在艾奥瓦城挨个敲开爱荷华大学地质学教授的门，要聊晶体结构、陨石和化石——科学好奇心的原点。
2. **文理兼修的 Grinnell 岁月（1966–1970）**：National Merit Scholar 读 Homer、但丁、宪政史与化学；在有机化学实验课上遇到一生的搭档。
3. **从实验搭档到终身伴侣**：娶了有机化学实验搭档 Carol Lynn Martinson——实验室里的相遇。
4. **伯克利博士（1970–1975）**：John E. Hearst 门下研究小鼠主带 DNA 快速复性序列；1975 年获博士学位。
5. **MIT 博士后（1975–1978）**：博士毕业后同年入 MIT 从事博士后研究。
6. **落基山下的独立实验室（1978–）**：1978 年获科罗拉多大学（博尔德）第一个教职，讲本科化学与生物化学；此后一直在此任教，现为生物化学系特聘教授。
7. **四膜虫里的意外（1970s–1982）**：研究嗜热四膜虫（Tetrahymena thermophila）的 RNA 剪接时发现——**未加工的 RNA 分子能剪接它自己**。
8. **RNA 也能当酶（1982）**：成为第一个证明 RNA 分子不只是遗传信息的被动载体——它们有催化功能、能参与细胞反应的人。
9. **核酶（ribozyme）的世界**：RNA 加工反应与核糖体上的蛋白合成尤其由 RNA 催化；核酶成为基因技术新工具，并有望剪切入侵病毒 RNA 成为新疗法。
10. **RNA 世界的想象**：RNA 能自己剪接自己——暗示生命可能以 RNA 起步（RNA 既是信息又是催化剂）。
11. **第二条战线：端粒与端粒酶**：其实验室发现 TERT（端粒酶逆转录酶）——细胞分裂后恢复端粒长度的酶；端粒酶在 90% 的人类癌症中被激活，抑制其活性的药物有望用于治癌。
12. **HHMI 总裁（2000–2008）**：2000 年接替 Purnell Choppin 出任霍华德·休斯医学研究所总裁（马里兰）；同时保留科罗拉多实验室；2008-04-01 宣布卸任，2009 春回归教学科研。
13. **回归讲台与著述**：回博尔德后任 BioFrontiers Institute 首任执行主任（至 2020），亲自给新生讲普通化学；2024 年 6 月出版《The Catalyst: RNA and the Quest to Unlock Life's Deepest Secrets》。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深海藏蓝 deepnavy） | `#14324F` | 分子深处的秩序——端粒到核酶（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（核酶 badgeRibozyme） | `#1B7A43` | 绿自剪接 RNA / RNA 催化 |
| 分类色 2（端粒酶 badgeTelomerase） | `#B0413E` | 绯红 TERT / 端粒与癌症 |
| 分类色 3（求学生涯 badgeEdu） | `#D97B29` | 琥珀Grinnell—Berkeley—MIT |
| 分类色 4（科罗拉多与 HHMI badgeColo） | `#2E5A9E` | 蓝博尔德讲台 / HHMI 治理 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「内含子被剪出、RNA 折叠成催化形状」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Mirage** — Notan Nigres（文件：`music_audio/inspiring-electronic/04-5gcb94jhG1I-Notan Nigres - Mirage (Audio).wav`；不要复制 wav 文件）
- **风格**：明亮探索 / 电子氛围 / 海市蜃楼般的未知感
- **匹配理由**：
  - "未知感" 匹配 1982 年的发现——在所有人都认定酶必是蛋白质时，四膜虫的 RNA 像海市蜃楼中的绿洲般出现
  - "明亮探索" 匹配其双重探索轨迹——从 RNA 催化到端粒酶，再到 RNA 世界与生命起源的想象
  - "电子氛围" 匹配纪录片叙事：芝加哥 → 艾奥瓦城 → Grinnell → 伯克利 → 博尔德 → 斯德哥尔摩
- **时长**：以曲文件实际时长为准，ffmpeg `-shortest` 自动对齐 15 页

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 会剪接自己的 RNA / Thomas Cech 1947– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士导师/配偶/出生地/领域/荣誉/机构）
03  切赫的一生 — Sanger 式时间线（10 节点：1947→1966→1970→1975→1978→1982→1989→2000→2009→2024）
04  早年：敲开教授门的少年 (1947–1966) — 表格「时间|事件|结果」
05  Grinnell 与伯克利 (1966–1975) — 表格「时间|事件|结果」
06  MIT 博士后与博尔德起步 (1975–1981) — 表格「站点|课题|结果」
07  四膜虫的自剪接 RNA (1982) — 表格「问题|方法|结果」+ 公式框：rRNA 前体 − 内含子 → 成熟 rRNA（无蛋白参与）
08  1989 诺贝尔化学奖 — 与 Sidney Altman 共享；官方理由 "for their discovery of catalytic properties of RNA"
09  核酶与 RNA 世界 — 表格「发现|意义|延伸」（核酶工具 / 病毒 RNA 剪切 / RNA world）
10  第二战线：端粒与 TERT — 表格「问题|发现|意义」+ 公式框：端粒缩短 ↔ 端粒酶延长；90% 癌症激活
11  HHMI 总裁岁月 (2000–2009) — 表格「时间|职务|动作」
12  荣誉与学会 — Sanger 式「类别|代表|意义」表格（Lasker 1988 / NMS 1995 / Othmer 2007 / NAS 1987 / AAAS 1988 / APS 2001）
13  遗产：回到讲台 — 四分类遗产盒（教学 / 著作 The Catalyst 2024 / BioFrontiers / 科普）
14  结尾 — 「生命最早的酶，也许是一条会剪自己的 RNA。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1989 诺奖口径 | 与 Sidney Altman **共享**，官方理由 "for their discovery of catalytic properties of RNA"——Cech 发现 **rRNA 前体自剪接**，Altman 发现 **RNase P 的 RNA 亚基单独具催化活性**；两条线勿混 |
| 官方获奖理由引语 | 页面导语原文 "for their discovery of catalytic properties of RNA"（含弯引号，排版时转半角）；勿再"润色" |
| 博士导师 | **John E. Hearst**（UC Berkeley，1975）——勿写成 MIT 博士后站点或 Grinnell |
| 学位年份 | Grinnell B.A. **1970**；Berkeley Ph.D. **1975**；1966 入学 Grinnell——勿改 |
| 出生地 | **芝加哥**出生，**艾奥瓦城**长大——两城勿混 |
| 配偶 | Carol Lynn Martinson（大学有机化学实验搭档成婚）——**infobox 无配偶行**，仅正文一句明载；其余婚姻细节页面无载，勿写 |
| 端粒酶发现者表述 | 页面只说 "his lab discovered TERT"——**不得点名 Carol Greider 等具体合作者**（页面无载）；Greider 在本页面完全未出现 |
| 端粒酶与癌症 | "Telomerase is activated in 90% of human cancers"——比例照写，勿夸大为"所有癌症" |
| HHMI 卸任 | 2008-04-01 **宣布**卸任，2009 春正式回归——勿写成 2008 当年卸任 |
| 接任关系 | 2000 年接替 **Purnell Choppin** 任 HHMI 总裁——仅为职务接替，不构成科研合作关系，**不入库**关系 |
| 荣誉年份 | Pfizer 酶化学奖 1985 / Newcomb Cleveland 1986 / NAS 分子生物学奖 1987 / Rosenstiel 与 Heineken 与 Lasker 均 1988 / NMS 1995 / Othmer 2007；NAS 院士 1987、AAAS 1988、APS 2001——勿并串 |
| Heineken 奖 | 正文作 "Heineken Prize of the Royal Netherlands Academy"（1988）；infobox 全称 Dr H.P. Heineken Prize for Biochemistry and Biophysics——两写法均页面实载 |
| 《The Catalyst》 | 2024 年 6 月出版；书名照抄 "The Catalyst: RNA and the Quest to Unlock Life's Deepest Secrets" |
| "第一次/唯一"类断言 | "第一个证明 RNA 有催化功能"来自页面导语原句 "Cech became the first to show..."——可用但注明出处为页面表述 |
| 引语红线 | 页面正文几乎无直接引语；除获奖理由句与 "became the first..." 句外一律间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q135180 | ✅ |
| name_zh | 托马斯·切赫 | ✅ |
| name_en | Thomas Cech | ✅ |
| birth_date | 1947-12-08 | ✅ |
| death_date | （页面无载，在世，留空） | ✅ |
| nationality | United States | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry（person_field 细分见下表） | ✅ |
| has_biography | false（立传 Beamer 完成后置 1） | ✅ |

person_field 细分（rank 表）：

| field | rank | 说明 |
|---|---|---|
| biochemistry | 0 | metadata field_of_work 首项 |
| RNA catalysis | 1 | 核酶 / 自剪接 |
| telomerase | 1 | 端粒与 TERT |
| cancer biology | 2 | metadata field_of_work 第三项 |
| transcription | 3 | 正文主研究区一 |

## 7. 社会关系入库清单

**红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | John E. Hearst | 师→生（博士导师） | UC Berkeley，1975 博士 |
| spouse | Carol Lynn Martinson | 无向 | 大学有机化学实验搭档成婚（正文一句明载） |
| co-honored | Sidney Altman | 无向 | 1989 诺贝尔化学奖共同得主（对方 yaml name_en 同用 Sidney Altman） |

> **禁入库名单**：Purnell Choppin（仅为 HHMI 职务接替，非科研关系）；Carol Greider 等端粒酶共同发现者（**本页面完全未载**，metadata 亦无）；Cech 的博士生（页面 infobox 与正文均未列出）；Daniel Stach（ČT24 节目主持人）等媒体人物。

## 8. 奖项清单

- Nobel Prize in Chemistry（1989，与 Sidney Altman 共享）
- Pfizer Award in Enzyme Chemistry（1985）
- Newcomb Cleveland Prize（1986）
- NAS Award in Molecular Biology（1987）
- American Cancer Society lifetime professorship（1987）
- Rosenstiel Award（1988）
- Dr H.P. Heineken Prize（荷兰皇家科学院，1988）
- Albert Lasker Basic Medical Research Award（1988）
- Golden Plate Award, American Academy of Achievement（1990）
- National Medal of Science（1995）
- Othmer Gold Medal（2007）
- Guggenheim Fellowship；Canada Gairdner International Award（infobox 明载，页面正文未给年份——如实标注）
- Louisa Gross Horwitz Prize（Columbia，infobox 明载；正文奖项段未列年份——如实标注）
- 学会：NAS 院士（1987）、AAAS Fellow（1988）、American Philosophical Society（2001）、Fellow of the AACR Academy（infobox）
- George Gamow Memorial Lecture（2003）；Distinguished Eagle Scout Award（infobox）；Harvard 荣誉博士（infobox）

## 9. 机构清单

- 教育：Iowa City High School（metadata 明载）、Grinnell College（1966–1970，B.A.）、UC Berkeley（Ph.D. 1975）、MIT（1975– 博士后）
- 任职：University of Colorado Boulder（1978 起教职，现为生物化学系特聘教授）、Howard Hughes Medical Institute（2000–2009 总裁，马里兰）、BioFrontiers Institute（回博尔德后首任执行主任，至 2020）
- 著作：The Catalyst: RNA and the Quest to Unlock Life's Deepest Secrets（Norton，2024-06）

## 10. 终审清单

- [ ] 生卒 1947-12-08 / 在世留白；出生地芝加哥、成长地艾奥瓦城
- [ ] 1989 与 Altman 共享；自剪接 vs RNase P 两条线分工表述准确
- [ ] 博士导师 John E. Hearst（Berkeley 1975）；Grinnell 1970 / Berkeley 1975
- [ ] Carol Lynn Martinson 仅一句正文明载；无其他婚姻细节
- [ ] TERT 表述 "his lab discovered"；不点任何共同发现者姓名
- [ ] HHMI 2000–2008（宣布）/2009（正式）；接替 Choppin 不入库关系
- [ ] 荣誉年份逐项对照 infobox 与正文两处清单
- [ ] 引语仅获奖理由句与 "became the first..." 句，均可回溯 page.md 原文
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Thomas_Cech/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：Wikipedia "Cech in 2005" 肖像或装饰圆占位（如实标注）
- [ ] 国籍：封面顶部明示 美国
- [ ] 引语核对：获奖理由句与 "became the first..." 句须在 page.md 原文找到
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger）对齐

---

> **名单状态**：本文件由 chem-batch-21 执行生成；`chemist/generate_20th_century_list.py` 状态列由主控统一收尾，本批次不改动。
