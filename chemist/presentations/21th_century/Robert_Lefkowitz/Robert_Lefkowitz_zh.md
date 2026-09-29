# Robert Lefkowitz（罗伯特·莱夫科维茨）立传提示词

> qid=Q80910 · 1943-04-15 生于纽约布朗克斯 · 在世 · 美国内科/心脏科医生、生物化学家 · 诺贝尔化学奖（2012，与 Brian Kobilka 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Robert_Lefkowitz/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 表格语义化 tabularx + 金色公式框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像从本地 `images.txt` 列表下载，如 2012 斯德哥尔摩照；下载失败用装饰圆占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{heartbeat}\enspace 细胞信号之门\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地、教育、研究领域、任职、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「受体-配体」母题——大圆为受体、小圆为配体/药物，散布如钥匙寻找锁孔。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），七次跨膜结构示意或受体家族数即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Robert Joseph Lefkowitz（中文惯称：罗伯特·莱夫科维茨）
- **生卒**：1943-04-15 生于纽约州纽约市布朗克斯（The Bronx）→ 在世（卒日留白）
- **国籍**：United States（美国）
- **身份**：内科医生（internist / cardiologist）与生物化学家——杜克大学 James B. Duke 医学教授、生物化学与化学教授；Howard Hughes Medical Institute（HHMI）研究员（1976–）
- **家庭**：犹太家庭，父母 Max 与 Rose Lefkowitz，两家均于 19 世纪末自波兰移民美国；前妻 Arna Brandel（离异）；1991 年娶 Lynn（娘家姓 Tilley）；五个子女、六个孙辈（子女未具名，页面无载勿展开）
- **教育轨迹**：
  - 1959 毕业于 Bronx High School of Science（布朗克斯科学高中）
  - 1962 Columbia College 化学学士（BA in chemistry；在 Columbia 师从 Ronald Breslow）
  - 1966 Columbia University College of Physicians and Surgeons 医学博士（M.D.）
  - 内科实习与一年普通内科住院医；1968–1970 NIH 临床与研究 associate
- **研究领域**：受体生物学与信号转导——β 肾上腺素受体、G 蛋白偶联受体（GPCR）、GPCR 激酶、β-arrestins
- **无 PhD**：以 M.D. 走通研究之路（"accidental scientist" 自况），勿写博士导师/博士论文（页面无载）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **布朗克斯科学高中（1959）**：纽约精英公立学校的科学启蒙，1959 届毕业。
2. **哥伦比亚化学少年（1959–1962）**：Columbia College 化学本科，师从 Ronald Breslow；1962 年毕业即入医学院。
3. **M.D. 与 "黄贝雷帽"（1966–1970）**：P&S 1966 届；因越战兵役义务加入美国公共卫生服务（USPHS，"Yellow Berets"），1968–1970 在 NIH 做临床与研究 associate——兵役义务意外点燃终生研究热情（回忆录叙事，页面明载）。
4. **扎根杜克（1973–）**：1973 受聘杜克医学中心医学副教授兼生物化学助理教授；1977 升医学教授；1982 任 James B. Duke Professor。
5. **受体放射配基时代**：以放射配基技术详细刻画 β 肾上腺素及相关受体的序列、结构与功能。
6. **1980s 克隆基因**：与同事先克隆 β 肾上腺素受体基因，随后共克隆 8 个肾上腺素受体——打开分子时代。
7. **七次跨膜的家族规律**：发现所有 GPCR（含 β 肾上腺素受体）结构高度相似——氨基酸序列来回穿越质膜七次；人体约 1,000 个受体同属此家族，使用相同的基本机制。
8. **调节蛋白双发现**：发现并刻画调节 GPCR 的两大家族蛋白——GPCR 激酶（GRK）与 β-arrestins。
9. **药物半壁江山**：今天 30–50% 的处方药设计为 "fit" 进 Lefkowitz 式受体的同构锁孔——从抗组胺、胃药到缓解高血压/心绞痛/冠心病的 β 阻断剂。
10. **高被引与师门**：Thomson-ISI 口径下生物学、生物化学、药理学、毒理学与临床医学领域最高被引研究者之一；2006 获 AHA Eugene Braunwald 学术导师奖，门下学生遍布 GPCR 领域（infobox 列 12 人，见 §7）。
11. **2012 诺贝尔化学奖**：与学生 Brian Kobilka 共享，表彰 "discoveries that reveal the inner workings of an important family of G protein-coupled receptors"（页面表述）——师生同台是本篇最大戏剧点。
12. **2021 回忆录**：《A Funny Thing Happened on the Way to Stockholm: The Adrenaline-Fueled Adventures of an Accidental Scientist》（与 1990 年代实验室博士后 Randy Hall 合著）；《纽约时报》"New & Noteworthy"、Nature "one of the week's best science picks"。
13. **荣誉满载**：2007 National Medal of Science + Shaw Prize + Albany Medical Center Prize；2009 BBVA Frontiers of Knowledge Award（生物医学类）；1988 Gairdner 国际奖；1978 John Jacob Abel 药理学奖。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深孔雀蓝 deeppeacock） | `#0E4D64` | 受体生物学的深沉与杜克蓝的底色（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（GPCR badgeGPCR） | `#2E5A9E` | 蓝七次跨膜 / 受体家族 |
| 分类色 2（信号转导 badgeSignal） | `#1B7A43` | 绿 GRK / β-arrestins |
| 分类色 3（临床转化 badgeClinic） | `#D97B29` | 琥珀处方药 30–50% / β 阻断剂 |
| 分类色 4（师门传承 badgeMentor） | `#C0395B` | 玫瑰 12 门生 / 导师奖 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落）——受体与配体：大圆锁孔、小圆钥匙，如药物分子在膜面寻找契合位点。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**New Lands** — Alex-Productions（文件 `74-oK8HN0FsZmc-New-Lands.wav`，**勿复制 wav 文件**）
- **风格**：开阔 / 上行 / 发现新大陆般的推进感
- **匹配理由**：
  - "New Lands（新大陆）" 对应 GPCR 家族的"地理大发现"——从单一受体到约 1,000 个同族受体的版图展开
  - "上行" 匹配其职业弧线——兵役义务的意外起点 → 杜克四十年 → 师生共享诺奖
  - "开阔" 匹配临床转化视野——30–50% 处方药指向的受体的确是制药业的"新大陆"
- **时长核对**：以 ffmpeg `-shortest` 自动对齐 15 页 × 7 秒 ≈ 105 秒的幻灯时长

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 细胞信号之门 / Robert Lefkowitz 1943– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/领域/任职/家庭/荣誉）
03  莱夫科维茨的一生 — Sanger 式时间线（10 节点：1943→1959→1962→1966→1968→1973→1982→1980s→2007→2012）
04  早年：布朗克斯与哥伦比亚 (1943–1966) — 表格「时间|事件|结果」
05  NIH 的 "黄贝雷帽" 岁月 (1966–1973) — 表格「阶段|任务|转折」
06  扎根杜克：受体生物学 (1973–1982) — 表格「问题|方法|结果」（放射配基刻画 β 受体）
07  克隆基因与七次跨膜 (1980s) — 表格「挑战|方法|结果」+ 公式框：GPCR 七次跨膜示意 / 约 1,000 受体家族
08  GRK 与 β-arrestins — 表格「对象|机制|意义」+ 公式框：脱敏/内吞通路示意
09  2012 诺贝尔化学奖 — 表格「奖项|年份|理由」+ 公式框：师生共享（Lefkowitz + Kobilka）
10  师门与传承 — 表格「人物|方向|结果」（infobox 12 门生选列 + Braunwald 导师奖）
11  荣誉与奖项 — Sanger 式「类别|代表|意义」表格（含 itemize 荣誉清单）
12  从布朗克斯到斯德哥尔摩 — 机构流程图（Bronx Science → Columbia → NIH → Duke/HHMI）
13  遗产：药物半壁江山 — 四分类遗产盒 + 公式框：30–50% 处方药与 GPCR
14  结尾 — 「偶然闯入科学的医生，为半数药物画出了锁孔。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2012 获奖口径 | 与 Brian Kobilka **两人共享**；官方完整 citation 英文全句页面无载——只可用页面实载表述 "discoveries that reveal the inner workings of an important family of GPCRs"（intro）/ "discoveries that reveal the workings of GPCRs"（Kobilka 篇），**勿杜撰 nobelprize.org 全句** |
| 学位口径 | 只有 M.D.（1966 Columbia P&S），**无 PhD、无博士导师**——勿写"博士论文"或虚构导师 |
| 师生方向 | Kobilka 是在杜克 **postdoctoral fellow under Lefkowitz**（Kobilka 页面口径）；Lefkowitz infobox 将 Kobilka 列入 Notable students——两篇统一记 "博士后导师"，勿写"博士导师" |
| 家庭口径 | 前妻 Arna Brandel（离异）、1991 年娶 Lynn Tilley；五个子女、六个孙辈——子女未具名，勿编造姓名 |
| 宗教与移民背景 | 波兰犹太移民家庭可写（页面明载）；相关政治语境勿展开 |
| 回忆录书名 | 2021《A Funny Thing Happened on the Way to Stockholm》——书名照抄，合著者 Randy Hall 是 1990 年代博士后 |
| 同名区分 | Ronald Breslow（哥伦比亚本科师承）≠ 他人在杜克的导师；Randy Hall（回忆录合著博士后）≠ Marc Caron 等门生 |
| 奖项年份 | Gairdner 1988、National Medal of Science 2007、Shaw Prize 2007、BBVA 2009、Nobel 2012——勿混淆 |
| 高被引口径 | "among the most highly cited researchers" 限定在 biology/biochemistry/pharmacology/toxicology/clinical medicine，出自 Thomson-ISI——勿泛化为"全球最高被引" |
| 在世口径 | 无卒日，封面与身份页一律 "1943–" 留白，勿虚构 |
| 中文译名 | 惯称「罗伯特·莱夫科维茨」，勿用「莱弗科维茨」等其他形式 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q80910 | ✅ |
| name_zh | 罗伯特·莱夫科维茨 | ✅ |
| name_en | Robert Lefkowitz | ✅ |
| birth_date | 1943-04-15 | ✅ |
| death_date | NULL（在世留白） | ✅ |
| nationality | United States | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry（person_field 细分：G protein-coupled receptors / receptor biology / signal transduction / biochemistry，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**家人 / 导师 / 门生 / 共同得主**（★红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Arna Brandel | 无向 | 前妻（离异） |
| spouse | Lynn Tilley | 无向 | 1991 年结婚 |
| advisor-student | Ronald Breslow | 师→生 | 哥伦比亚本科期间师从（studied under） |
| advisor-student | Brian Kobilka | 师→生 | 杜克博士后导师；克隆 β2 肾上腺素受体起点 |
| co-honored | Brian Kobilka | 无向 | 2012 诺贝尔化学奖共同得主 |
| advisor-student | Jeffrey Benovic | 师→生 | infobox Notable students |
| advisor-student | Michel Bouvier | 师→生 | infobox Notable students |
| advisor-student | Marc G. Caron | 师→生 | infobox Notable students |
| advisor-student | Richard A. Cerione | 师→生 | infobox Notable students |
| advisor-student | Henrik Dohlman | 师→生 | infobox Notable students |
| advisor-student | Walter J. Koch | 师→生 | infobox Notable students |
| advisor-student | Lee Limbird | 师→生 | infobox Notable students |
| advisor-student | Martin J. Lohse | 师→生 | infobox Notable students |
| advisor-student | Gang Pei | 师→生 | infobox Notable students |
| advisor-student | Lewis Williams | 师→生 | infobox 记 "Lewis \"Rusty\" Williams" |
| advisor-student | R. Sanders Williams | 师→生 | infobox Notable students |
| colleague | Randy Hall | 无向 | 1990 年代实验室博士后、2021 回忆录合著者 |

> **禁入库名单**（页面未具名或非直接个人关系）：Max 与 Rose Lefkowitz（父母仅姓名）、五个子女与六个孙辈（未具名）、Ronald Breslow 之外的 NIH/USPHS 期间人物、AHA/HHMI 等机构（机构不入 person_relation）。

## 8. 奖项清单

- Nobel Prize in Chemistry（2012，与 Brian Kobilka 共享）
- National Medal of Science（2007）
- Shaw Prize in Life Science and Medicine（2007）
- Albany Medical Center Prize（2007）
- BBVA Foundation Frontiers of Knowledge Award（2009，生物医学类）
- Gairdner Foundation International Award（1988）
- John Jacob Abel Award in Pharmacology（1978）
- Jessie Stevenson Kovalenko Medal（2001，美国国家科学院）
- Bristol-Myers Squibb Award for Distinguished Achievement in Cardiovascular Research（1992）
- Fondation Lefoulon–Delalande Grand Prix（2003，法兰西学会）
- AHA Eugene Braunwald Academic Mentorship Award（2006）；AHA Research Achievement Award（2009）
- Golden Plate Award（2014，American Academy of Achievement）
- 另载（frontmatter/infobox）：Endocrine Regulation Prize、Louis and Artur Lucian Award、Pasarow Award、North Carolina Award、Kober Medal 等

## 9. 机构清单

- 教育：Bronx High School of Science（–1959）；Columbia College（BA chemistry 1962）；Columbia University College of Physicians and Surgeons（M.D. 1966）
- 任职：NIH 临床与研究 associate（1968–1970，USPHS）；Duke University Medical Center（1973 医学副教授兼生物化学助理教授 → 1977 医学教授 → 1982 James B. Duke Professor）；Howard Hughes Medical Institute 研究员（1976–）；American Heart Association established investigator（1973–1976）
- 现职：James B. Duke Professor of Medicine；Professor of Biochemistry and Chemistry（杜克）

## 10. 终审清单

- [ ] 生卒 1943-04-15 / 在世留白；出生地布朗克斯表述准确
- [ ] 2012 与 Kobilka **两人共享**；获奖理由只用页面实载表述，未杜撰官方全句
- [ ] M.D. 口径（无 PhD、无博士导师）准确；Kobilka 关系统一为"博士后导师"
- [ ] 七次跨膜 / 约 1,000 受体 / 30–50% 处方药三个数字均出自页面明载
- [ ] 12 门生入库与 infobox 一一对应，无杜撰
- [ ] 回忆录书名与合著者准确；"New & Noteworthy"/"best science picks" 表述有出处
- [ ] 引语核对——页面正文几无直接引语，全篇以间接转述为主
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Robert_Lefkowitz/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：从 `images.txt` 列表下载（2012 斯德哥尔摩照优先），失败用装饰圆占位
- [ ] **国籍**：封面顶部明示美国
- [ ] **引语核对**：本篇几乎无直接引语——凡引号内容须在原文找到，否则改间接转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 黄金骨架）对齐

---

> **名单状态**：`chemist/generate_21th_century_list.py` 由主控统一收尾，本提示词不直接改动总名单。
> **最重要的事：每写一页就 make，看到溢出就修。**
