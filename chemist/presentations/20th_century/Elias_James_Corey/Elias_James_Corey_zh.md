# Elias James Corey（伊利亚斯·詹姆斯·科里）立传提示词

> qid=Q135171 · 1928-07-12 –（在世）· 美国有机化学家 · 20 世纪 · 诺贝尔化学奖（1990，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Elias_James_Corey/`（page.md + metadata.json）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。肖像用 Wikipedia "Corey in 2007"；下载失败用装饰圆占位并如实标注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace合成的逻辑\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（Elias James Corey，姓氏源自黎凡特阿拉伯语 Khoury）、国籍、出生地、教育、博士导师、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「逆合成分析 / 键的拆解」母题——分子骨架被逐层拆解成合成子。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如 目标分子 ⇒（逆合成）⇒ 合成子 ⇒（正向合成）⇒ 目标分子。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Elias James Corey（惯称 E.J. Corey；中文惯称：伊利亚斯·詹姆斯·科里；姓氏由黎凡特阿拉伯语 *Khoury*（意为"祭司"）英语化而来）
- **生卒**：1928-07-12 生于美国马萨诸塞州 Methuen（波士顿以北 50 km）→ 在世（页面无卒日）
- **国籍**：United States（美国）
- **身份**：有机化学家；哈佛大学有机化学荣休教授（实验室仍保持活跃研究）
- **家庭**：黎巴嫩希腊东正教移民之子——父 Elias Corey、母 Fatima（娘家姓 Hasham）；父亲在其出生 18 个月后去世，母亲将其本名 William 改为 "Elias" 以纪念亡父；寡母与兄弟、两个姐妹、姑婶与叔伯同住一栋大屋，挣扎度过大萧条；少年时代独立、爱棒球、橄榄球与远足
- **配偶与子女**：页面无载（禁写）
- **教育轨迹**：天主教小学 → Lawrence High School（Lawrence, Massachusetts）→ 16 岁入 MIT（原读工程，大二第一堂化学课后改志）→ MIT 化学 BS（1948）→ 留校读博
- **博士**：1951 年 MIT；导师 John C. Sheehan；论文《The synthesis of N,N-diacylamino acids and analogs of penicillin》
- **研究领域**：有机化学——逆合成分析、合成方法学、全合成、试剂设计、计算机辅助合成（LHASA）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **大萧条里的黎巴嫩移民遗孤（1928）**：父亲早逝，母亲改其名为 Elias 以承父名；一屋寡母孤幼在萧条中挣扎——独立性格的起点。
2. **16 岁的 MIT 少年（1944）**：入学时唯一的科学经验是数学，本读工程；大二一堂化学课改写人生方向。
3. **Sheehan 门下（1948–1951）**：受 John C. Sheehan 之邀留校读博，1951 年获博士——青霉素类似物与 N,N-二酰基氨基酸的全合成训练。
4. **27 岁的正教授（1951–1956）**：博士毕业后受聘伊利诺伊大学厄巴纳-香槟分校，1956 年 27 岁升正教授；1952 年入 Alpha Chi Sigma 荣誉化学兄弟会。
5. **转战哈佛（1959）**：移师剑桥；1967 年任 Sheldon Emory 讲席教授，1968–69 年 Guggenheim Fellow。
6. **约 100 个天然分子**：在哈佛合成约 100 个此前仅存在于自然界的分子；至今其课题组已完成**至少 265 个天然化合物的全合成**（1950 年以来）。
7. **逆合成分析（retrosynthetic analysis）**：把目标分子**倒着拆**——逐键切断成简单合成子，再正向组装；这套"合成的逻辑"成为有机合成的通用方法论，1990 年独享诺贝尔化学奖，官方理由 "for his development of the theory and methodology of organic synthesis"。
8. **试剂帝国**：PCC（Corey–Suggs 试剂，醇的氧化）、TBS/TIPS/MEM 保护基（1972 起 TBS 成最常用硅保护基）、1,3-二噻烷与 *umpolung*（极性反转）化学。
9. **命名反应群**：CBS 还原（Corey–Bakshi–Shibata，脯氨酸+硼烷的手性噁唑硼烷催化剂）、Corey–Fuchs 炔合成、Corey–Kim 氧化、Corey–Winter 烯化、Corey–Nicolaou 大环内酯化（7–44 元环）、Johnson–Corey–Chaykovsky 环氧化；1950 年以来课题组发展**至少 302 种方法**。
10. **前列腺素经典（1969）**：多种前列腺素的全合成被视为经典——PGF2α 含顺/反双烯与 5 个手性碳；后又以手性 CBS 还原与不对称 Diels–Alder 大幅简化路线。其他代表作：Longifolene、银杏内酯 A/B、Lactacystin、Miroestrol、Ecteinascidin 743、Salinosporamide A。
11. **LHASA：合成的早期 AI**：与课题组创建 LHASA 程序——用人工智能发现通向全合成的反应序列，且是最早用图形界面输入与显示化学结构的程序之一。
12. **论文与引用**：1100+ 篇论文；2002 年 ACS 授予 "Most Cited Author in Chemistry"；2007 年获首届 ACS "Cycle of Excellence High Impact Contributor Award"，并以 h 指数居化学家研究影响力第一。
13. **门墙之盛**：截至 2010 年约 700 人先后属于 Corey 组；2008 年 80 岁生日时建成 580 位前组员数据库；学生与博后中包括 K. C. Nicolaou、野依良治（Ryōji Noyori，2001 诺奖）、Bengt Samuelsson（1982 诺奖）、David R. Liu、Phil Baran 等。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（靛蓝 indigo） | `#283593` | 合成逻辑的严谨与深邃（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（逆合成 badgeRetro） | `#1B7A43` | 绿逆合成分析 / 合成子 |
| 分类色 2（试剂与方法 badgeReagent） | `#B0413E` | 绯红PCC / CBS / 命名反应 |
| 分类色 3（全合成 badgeSynth） | `#D97B29` | 琥珀前列腺素 / 银杏内酯 |
| 分类色 4（LHASA badgeLhasa） | `#2E5A9E` | 蓝计算机辅助合成 / AI |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「分子骨架被逐层拆解」的逆合成树。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Shine Like The Sun** — Really Slow Motion（文件：`music_audio/inspiring-electronic/15-w6kT1BfvETI-Really Slow Motion - Shine Like The Sun (Epic Beautiful Uplifting).wav`；不要复制 wav 文件）
- **风格**：宏大上行 / 史诗而优美 / 帝国气象
- **匹配理由**：
  - "宏大" 匹配合成的逻辑帝国——302 种方法、265 个全合成、1100+ 论文，一个方法论统治整个学科
  - "优美上行" 匹配逆合成分析的思维之美——从复杂倒推简单的层层展开
  - "史诗" 匹配其身位——从大萧条遗孤到哈佛讲席再到斯德哥尔摩，一生上行曲线
- **时长**：以曲文件实际时长为准，ffmpeg `-shortest` 自动对齐 15 页

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 合成的逻辑 / Elias James Corey 1928– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士导师/出生地/领域/荣誉/机构/门生规模）
03  科里的一生 — Sanger 式时间线（10 节点：1928→1944→1951→1956→1959→1967→1969→1990→2004→在世）
04  早年：大萧条中的黎巴嫩移民之子 (1928–1944) — 表格「时间|事件|结果」
05  MIT：从工程到化学 (1944–1951) — 表格「时间|事件|结果」
06  伊利诺伊与哈佛 (1951–1967) — 表格「站点|事件|结果」（27 岁正教授 / 1959 转哈佛 / Sheldon Emory 教授）
07  逆合成分析 — 表格「问题|方法|结果」+ 公式框：目标分子 ⇒ 合成子 ⇒ 正向组装
08  试剂帝国 — 表格「试剂|功能|地位」（PCC / TBS-TIPS-MEM / 二噻烷 umpolung）
09  命名反应群与 CBS — 表格「反应|变换|意义」+ 公式框：CBS 手性还原（脯氨酸→噁唑硼烷→对映选择性）
10  前列腺素与其他全合成 — 表格「分子|挑战|路线」+ 公式框：PGF2α = 顺/反双烯 + 5 手性碳
11  1990 诺贝尔化学奖 — 独享；官方理由 "for his development of the theory and methodology of organic synthesis"
12  LHASA 与数字合成 — 表格「目标|手段|地位」+ 公式框：LHASA 反应序列搜索
13  门墙与荣誉 — Sanger 式「类别|代表|意义」表格（Wolf 1986 / NMS 1988 / Nobel 1990 / Priestley 2004 / ForMemRS 1998 / 19 个荣誉博士）
14  结尾 — 「先想清楚分子从哪里来，再动手把它造出来。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1990 诺奖口径 | **独享**，官方理由 "for his development of the theory and methodology of organic synthesis"，页面特别注明 "specifically retrosynthetic analysis"——勿写成共享、勿泛化成"发明有机合成" |
| 姓名 | 本名 William，母亲改为 "Elias" 纪念早逝父亲；姓氏 Khoury 英语化为 Corey——勿写成"以色列裔"（页面作 Lebanese Greek Orthodox Christian） |
| 学位年份 | MIT BS **1948**、PhD **1951**（导师 John C. Sheehan）；16 岁入学 MIT——勿写 1949/1952 |
| 27 岁正教授 | 1956 年在 **Illinois**（UIUC）27 岁升正教授；1959 年才转 Harvard——勿把 UIUC 经历挂到哈佛名下 |
| 合成统计 | "至少 302 种方法"与"至少 265 个天然化合物全合成"均为 1950 年以来课题组累计（页面明载 since 1950）；"约 100 个天然分子"指其个人在哈佛合成——三个数字勿混 |
| TBS 年份 | "Since 1972 the TBS group has become the most popular silicon protecting group"——1972 是"成为最常用"的起点表述，勿写成"1972 年发明" |
| CBS 命名 | Corey–Bakshi–Shibata；页面亦作 Corey–Itsuno reduction——两个名字均为页面实载，注明即可 |
| Altom 事件（敏感） | 学生 Jason Altom 1998 年自杀，遗书呼吁保护学生免受"abusive research advisors"之害；Corey 回应 "My conscience is clear..." 等——如需提及必须**双方视角并置、仅用页面原文**，且建议 Beamer 正文一笔带过或置于敏感点注释页，不作叙事主线 |
| Woodward–Hoffmann 争议（敏感） | 2004 年 Priestley 演讲中 Corey 声称 1964-05-04 曾向 Woodward 提出对称性解释；Hoffmann 在 Angewandte Chemie 公开反驳——如需提及必须**双方立场并置**、标注"争议"字样，勿替任何一方下结论 |
| 门生入库 | 页面 infobox "Notable students" 24 人 + 正文组员名单（含 Alice Ting）；metadata doctoral_student 仅 4 人（Dale L. Boger、William L. Jorgensen、Hisashi Yamamoto、Andrew G. Myers）。**择要入库**（见 §7），其余防噪声不入库；Andrew G. Myers 为 metadata-only **禁入**；infobox 的 "Albert Meyers" 与 metadata 的 "Andrew G. Myers" 是**两个不同的人**，勿混 |
| 荣誉年份 | Wolf 1986 / NMS 1988 / Japan Prize 1989 / Nobel 1990 / ForMemRS 1998 / Priestley 2004；ACS Award in Pure Chemistry 1960 是其早年奖——勿与晚年奖并串 |
| CIBR | 2013 年 E.J. Corey Institute of Biomedical Research 在中国江苏江阴启用——页面明载可写；勿加任何页面外评论 |
| Pfizer 顾问 | "an advisor to Pfizer for more than 50 years"——照写，勿具体化 |
| 引语红线 | 直接引语仅两处：①选择有机化学之因 "its intrinsic beauty and its great relevance to human health" ②2004 Priestley 声明原文（如引用）；"That letter doesn't make sense..." 等仅限 Altom 事件注释页；其余一律间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q135171 | ✅ |
| name_zh | 伊利亚斯·詹姆斯·科里 | ✅ |
| name_en | Elias James Corey | ✅ |
| birth_date | 1928-07-12 | ✅ |
| death_date | （页面无载，在世，留空） | ✅ |
| nationality | United States | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | organic chemistry（person_field 细分见下表） | ✅ |
| has_biography | false（立传 Beamer 完成后置 1） | ✅ |

person_field 细分（rank 表）：

| field | rank | 说明 |
|---|---|---|
| organic chemistry | 0 | 页面 Fields 主字段 |
| retrosynthetic analysis | 1 | 诺奖核心方法论 |
| synthetic methodology | 2 | 302 种方法 / 命名反应群 |
| total synthesis | 2 | 265 个天然产物 |
| computer-assisted synthesis | 3 | LHASA |

## 7. 社会关系入库清单

**红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | John C. Sheehan | 师→生（博士导师） | MIT，1951 博士 |
| advisor-student | K. C. Nicolaou | Corey→学生 | infobox Notable students |
| advisor-student | Ryōji Noyori | Corey→学生 | infobox Notable students；2001 诺贝尔化学奖 |
| advisor-student | Bengt I. Samuelsson | Corey→学生 | infobox Notable students；1982 诺贝尔生理学或医学奖 |
| advisor-student | David R. Liu | Corey→学生 | 正文组员名单明载 |
| advisor-student | Phil Baran | Corey→学生 | infobox Notable students |
| advisor-student | Dale L. Boger | Corey→学生 | infobox Notable students（metadata doctoral_student 亦载） |
| advisor-student | William L. Jorgensen | Corey→学生 | infobox Notable students（metadata doctoral_student 亦载） |
| advisor-student | Hisashi Yamamoto | Corey→学生 | infobox Notable students（metadata doctoral_student 亦载） |
| advisor-student | Dieter Seebach | Corey→学生 | infobox Notable students；Corey–Seebach 反应以两人命名 |
| advisor-student | Eric Block | Corey→学生 | 正文组员名单明载（组员名单首位） |
| colleague | Robert Burns Woodward | 无向 | 1964-05-04 Corey 自述曾向 Woodward 提出对称性解释（Woodward–Hoffmann 规则归属之争的源头；页面原文并置双方立场） |
| controversy | Roald Hoffmann | 无向 | 2004 年 Hoffmann 在 Angewandte Chemie 公开反驳 Corey 对 Woodward–Hoffmann 规则的贡献主张 |

> **禁入库名单（防噪声择要裁定的不入库部分）**：infobox Notable students 其余 13 人（Weston T. Borden、David E. Cane、Rick L. Danheiser、John Katzenellenbogen、Alan P. Kozikowski、Bruce H. Lipshutz、Gojko Lalic、Gary H. Posner、Martin F. Semmelhack、Vinod K. Singh、Brian Stoltz、Ramakanth Sarabu、Jin-Quan Yu）与正文组员 Alice Ting、Albert Meyers——页面虽明载但按批次防噪声裁定不入库，全名单存档于本节；**Andrew G. Myers 仅 metadata 载，禁入**；Pfizer（顾问机构）、Alpha Chi Sigma（兄弟会）非人际不入库。

## 8. 奖项清单

- Nobel Prize in Chemistry（1990，独享）
- ACS Award in Pure Chemistry（1960）
- Ernest Guenther Award（1968）
- Centenary Medal（1971）
- Linus Pauling Award（1973）；George Ledlie Prize（1973）
- Arthur C. Cope Award（1976）；William H. Nichols Medal（1977）
- Franklin Medal（1978）
- Chemical Pioneer Award（1981）；Lewis S. Rosenstiel Award（1981）
- Paul Karrer Gold Medal（1982）
- Tetrahedron Prize（1983）
- Willard Gibbs Award（1984）
- Wolf Prize in Chemistry（1986）
- National Medal of Science（1988）
- Japan Prize（1989）
- Golden Plate Award（1991）；Roger Adams Award（1993）
- Foreign Member of the Royal Society, ForMemRS（1998）
- Priestley Medal（2004，ACS 最高荣誉）
- 累计 40+ 项大奖；19 个荣誉博士（截至 2008；含牛津、剑桥等）；Alpha Chi Sigma Hall of Fame（1998）；Paracelsus Prize、Dickson Prize、Remsen Award、Robert Robinson Award、Sir Derek Barton Gold Medal、NAS Award in Chemical Sciences 等（infobox 明载）

## 9. 机构清单

- 教育：Lawrence High School、Massachusetts Institute of Technology（16 岁入学；BS 1948、PhD 1951）
- 任职：University of Illinois at Urbana–Champaign（1951–1959，1956 年 27 岁正教授）、Harvard University（1959–，1967 Sheldon Emory 教授，现有机化学荣休教授）
- 其他：Alpha Chi Sigma（1952 入会，1998 入 Hall of Fame）；Pfizer 顾问（50+ 年）；E.J. Corey Institute of Biomedical Research（CIBR，2013 年启用，中国江苏江阴）

## 10. 终审清单

- [ ] 生卒 1928-07-12 / 在世留白；出生地 Methuen, Massachusetts
- [ ] 1990 独享；获奖理由原文口径准确
- [ ] MIT BS 1948 / PhD 1951（Sheehan）；1956 UIUC 27 岁正教授；1959 转哈佛
- [ ] 302 方法 / 265 全合成 / 约 100 天然分子三个数字语境勿混
- [ ] Altom 事件与 Woodward–Hoffmann 争议如提及必双方并置、仅用页面原文
- [ ] 关系入库 13 行（Sheehan 导师 + 10 位明载学生 + Woodward colleague + Hoffmann controversy）与禁入库名单一致
- [ ] 荣誉年份逐项对照 infobox 与正文两处清单
- [ ] 引语仅页面原文两三处，均可回溯
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Elias_James_Corey/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：Wikipedia "Corey in 2007" 肖像或装饰圆占位（如实标注）
- [ ] 国籍：封面顶部明示 美国
- [ ] 引语核对：直接引语须在 page.md 原文找到
- [ ] 敏感点复核：Altom 与 Woodward–Hoffmann 两处表述立场平衡
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger）对齐

---

> **名单状态**：本文件由 chem-batch-21 执行生成；`chemist/generate_20th_century_list.py` 状态列由主控统一收尾，本批次不改动。
