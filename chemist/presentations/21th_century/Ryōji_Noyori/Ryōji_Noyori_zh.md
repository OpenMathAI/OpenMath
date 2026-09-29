# Ryōji Noyori（野依良治）立传提示词

> qid=Q157210 · 1938-09-03 –（在世）· 日本化学家 · 21 世纪 · 诺贝尔化学奖（2001，与 Knowles 共享半奖；另一半 Sharpless）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Ryōji_Noyori/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框。images.txt 第 3 张 `Study with a fresh and straightforward mind! Ryoji Noyori.jpg` 是**本人工作照（真照片）**，可裁剪作肖像；第 4 张与 Yamanaka 的橄榄球开球仪式合影**非单人肖像禁作头像**（可作趣闻插图）；第 1/2 张为名古屋大学野依纪念建筑照片（作 RIKEN/名大页插图）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace\ 实用优雅的合成化学家\enspace·\enspace 日本`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（野依 良治 / Noyori Ryōji）、国籍、出生地、教育（京都大学 DEng）、博士导师（Hitoshi Nozaki）、博士后导师（Elias J. Corey）、任职（名古屋大学 / RIKEN）、核心领域（不对称催化 / BINAP / 绿色化学）、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「催化 / 旋向」母题——圆点带方向性渐变，暗示手性分子的螺旋旋向。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）——如 (S)-BINAP-Ru(OAc)2 催化体系框、薄荷醇异构化流程框。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Ryōji Noyori（野依 良治，*Noyori Ryōji*；中文惯称：野依良治）
- **生卒**：1938-09-03 生于日本神户（infobox 正文口径 Kobe；metadata place_of_birth 作 Ashiya——**以 page.md 正文 Kobe 为准**）
- **国籍**：Japan（日本）
- **身份**：化学家（chemist / professor；名古屋大学教授、RIKEN 理化学研究所理事长 2003–2015）
- **教育轨迹**：
  - Nada Junior and Senior High School（灘中学·高中）
  - 京都大学工学部工业化学科，1961 年毕业
  - 京都大学大学院工学研究科，工业化学硕士（1963）
  - 1963–1967 京都大学工学部助手（Hitoshi Nozaki 研究室）
  - 1967 京都大学工学博士（Doctor of Engineering, DEng）
  - 1968 京都大学副教授
  - Harvard 博士后（Elias J. Corey 组）→ 1972 名古屋大学教授，此后扎根名古屋
- **导师**：Hitoshi Nozaki（博士导师·野依组）；Elias J. Corey（博士后导师，Harvard）
- **研究领域**：不对称催化（铑/钌配合物·BINAP 配体）、不对称氢化、绿色化学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **神户之子（1938）**：生于神户；少年时代因父亲挚友、1949 年诺贝尔物理学奖得主**汤川秀树**的影响而迷上物理。
2. **尼龙讲演的转折**：在工业博览会上听尼龙（nylon）报告后转向化学——他看到化学的力量是「从几乎一无所有中制造高价值」（间接转述其原话 "produce high value from almost nothing"）。
3. **京都大学（1961–1967）**：工学部工业化学科 → 硕士 → Nozaki 组助手 → 1967 年工学博士（DEng）。
4. **Nozaki 组的起点（1963–1967）**：在 Hitoshi Nozaki 研究室任助手——日后获奖的手性催化萌芽期在此度过。
5. **Corey 门下（博士后）**：Harvard 博士后师从 Elias J. Corey，1968 年回京都任副教授，1972 年升名古屋大学教授。
6. **BINAP 不对称氢化**：以**铑与钌的 BINAP 配合物**为催化剂做不对称氢化——他最著名的贡献。
7. **萘普生（naproxen）工业生产**：(S)-BINAP-Ru(OAc)2 催化烯烃不对称氢化，商业化生产对映纯度 **97% ee** 的消炎药萘普生。
8. **左氧氟沙星（levofloxacin）**：Ru(II)-BINAP 卤素配合物催化酮不对称氢化制造抗菌药。
9. **薄荷醇（menthol）**：Takasago International Corporation 用其**烯丙胺异构化法**年产 3000 吨（扩产后）94% ee 薄荷醇。
10. **绿色化学与 DMF 新工艺**：与 Philip G. Jessop 以 RuCl2(P(CH3)3)4 催化，用氢气、二甲胺与**超临界二氧化碳**制 N,N-二甲基甲酰胺。
11. **「实用的优雅」(2005)**：2005 年撰文主张追求 "practical elegance in synthesis"；名言（页面原文）："our ability to devise straightforward and practical chemical syntheses is indispensable to the survival of our species." 另有 "Research is for nations and mankind, not for researchers themselves."
12. **2001 双奖年**：诺贝尔化学奖（与 Knowles 共享氢化半奖；Sharpless 得另一半·氧化）+ Wolf 奖同年到手。
13. **科学的管理者（2003–2015）**：执掌年度预算 8 亿美元的 RIKEN 十二年；2006 年后出任首相安倍晋三设立的教育再生会议主席；主张科研人员参与公共政策（"Researchers must spur public opinions and government policies toward constructing the sustainable society in the 21st century."）；以其命名的 The Ryoji Noyori Prize 成为本领域奖项。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深靛蓝 deepindigo） | `#16324F` | 名古屋学派的沉稳与体系性（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（BINAP 氢化 badgeBinap） | `#2E5A9E` | 蓝 BINAP-Ru / 不对称氢化 |
| 分类色 2（工业合成 badgeIndus） | `#1B7A43` | 绿萘普生 / 薄荷醇 / 左氧氟沙星 |
| 分类色 3（绿色化学 badgeGreen） | `#D97B29` | 琥珀超临界 CO2 / 实用的优雅 |
| 分类色 4（科学管理 badgeRiken） | `#C0395B` | 玫瑰 RIKEN / 教育再生会议 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「催化 / 旋向」的方向性。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Timeless** — Alex-Productions（`music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav`；**不要复制 wav 文件，Makefile 直接引用该路径**）
- **风格**：沉稳 / 纪录片 / 长期主义
- **匹配理由**：
  - "跨越时代" 匹配其贡献本质——BINAP 体系从 1960s Nozaki 组萌芽到 2001 诺奖再到持续的绿色化学纲领，是一以贯之的长期主义
  - "沉稳" 匹配名古屋学派气质——扎根一地（名古屋）半个世纪，实用优雅胜过戏剧性突破
  - "纪录片" 匹配传记叙事——神户 → 京都 → Harvard → 名古屋 → RIKEN → 教育再生会议
- **时长核对**：以实际曲目时长为准，> 15 页 × 7 秒即可由 ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 实用优雅的合成化学家 / Ryōji Noyori 1938– + 四色 badge + 右上工作照肖像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名野依良治/国籍/教育/双导师/机构/领域/荣誉）
03  Noyori 的一生 — 时间线（10 节点：1938→1961 京大→1963 Nozaki 组→1967 DEng→1968 副教授→Harvard Corey→1972 名大教授→BINAP/萘普生→2001 诺奖→2003 RIKEN）
04  早年：从汤川到尼龙 (1938–1961) — 表格「时间|事件|结果」
05  京都：Nozaki 组与工学博士 (1963–1968) — 表格「时间|事件|结果」
06  Corey 门下与名古屋岁月 (1969–1972) — 表格「阶段|工作|意义」
07  BINAP 不对称氢化 — 表格「问题|方法|结果」+ 公式框：(S)-BINAP-Ru(OAc)2 催化体系
08  工业：萘普生·左氧氟沙星·薄荷醇 — 表格「产品|方法|规模」+ 公式框：97% ee 萘普生 / 3000 吨薄荷醇
09  绿色化学与「实用的优雅」— 表格「理念|实践|意义」+ 公式框：超临界 CO2 制 DMF + 引语
10  2001 诺贝尔化学奖 — 表格「得主|份额|理由」+ 公式框：官方英文获奖理由
11  RIKEN 与教育再生会议 (2003–2015) — 表格「职务|作为|意义」
12  荣誉清单 — 「类别|代表|意义」表格 + itemize（Wolf/Asahi/Cope/Tetrahedron/Lomonosov/ForMemRS 等）
13  遗产：Noyori Prize 与不对称催化的黄金时代 — 四分类遗产盒
14  结尾 — 「从几乎一无所有中制造高价值——化学的力量，被他做成了工业与现实。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 获奖理由口径 | 官方英文 "for their work on chirally catalysed hydrogenation reactions"（他与 Knowles 共享的半奖）；Sharpless 另一半为氧化反应——勿混 |
| 奖项分配 | 页面口径：Knowles 与 Noyori **平分一半**，另一半 Sharpless——勿写「三人平分」 |
| 出生地 | page.md 正文与 infobox 作 **Kobe**；metadata.json place_of_birth 作 Ashiya——**以正文 Kobe 为准**，Review 勿被 metadata 带偏 |
| 学位口径 | 京都大学 **Doctor of Engineering（DEng，工学博士）**——勿写成 PhD in Chemistry |
| 双导师区分 | 博士导师 **Hitoshi Nozaki**（入库 advisor）；**Elias J. Corey** 是博士后导师（Harvard，入库 advisor-student 注明博士后；**入库名用库内规范形式 Elias James Corey #3508**，勿新建 Elias J. Corey stub）——勿混为同一层 |
| 汤川秀树 | 页面明载是**父亲的挚友**、激发其对物理的兴趣——用 **influence** 类型，勿写成师承 |
| Shinya Yamanaka | 仅出现于橄榄球开球仪式**合影图注**——非学术关系，**禁入库禁写为同事** |
| 引语 | 三条引语均须忠于 page.md 原文（"produce high value..." / "...survival of our species." / "Research is for nations and mankind..." / "Researchers must spur..."）——不得改写后仍加引号 |
| 政治人物 | 教育再生会议系安倍晋三内阁设立——**只写机构事实，不作政治评价** |
| metadata 奖项噪声 | frontmatter award_received 含 Order of Culture / Person of Cultural Merit 等正文未逐项列出的奖项——§8 以正文奖项清单为准，metadata-only 项仅注记 |
| 入库名规范 | 本人入库名用 **Ryōji Noyori**（库内 #3511 既有形式，UPD 回填）；Knowles 入库名 William Standish Knowles、Sharpless 入库名 Karl Barry Sharpless |
| 薄荷醇产量 | 3000 吨/年是「扩产后（after new expansion）」数字——勿写成发现当时产量 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q157210 | ✅（UPD 回填 #3511） |
| name_zh | 野依良治 | ✅ |
| name_en | Ryōji Noyori | ✅（必须用库内 #3511 精确形式） |
| birth_date | 1938-09-03 | ✅ |
| death_date | （在世，留空） | ✅ |
| nationality | Japan | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | chemistry（person_field 细分见下表） | ✅ |

**person_field 细分 rank 表**：

| rank | name_en | name_zh |
|---|---|---|
| 0 | asymmetric catalysis | 不对称催化 |
| 1 | asymmetric hydrogenation | 不对称氢化 |
| 2 | green chemistry | 绿色化学 |
| 3 | organic chemistry | 有机化学 |

## 7. 社会关系入库清单

**★ 红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Hitoshi Nozaki | 师→生（博士导师） | 京都大学 Nozaki 组助手出身，1967 工学博士 |
| advisor-student | Elias James Corey | 师→生（博士后导师） | Harvard 博士后（1969–70 前后），后回日本任名大教授（入库名用库内规范形式 Elias James Corey #3508） |
| influence | Hideki Yukawa | 无向 | 父亲挚友、1949 诺贝尔物理学奖得主，少年时代激发其对科学的兴趣 |
| colleague | Philip G. Jessop | 无向 | 共同开发超临界 CO2 制 DMF 的绿色化学工业工艺 |
| co-honored | William Standish Knowles | 无向 | 2001 诺贝尔化学奖共同得主（共享手性催化氢化半奖） |
| co-honored | Karl Barry Sharpless | 无向 | 2001 诺贝尔化学奖（Sharpless 得另一半·不对称氧化） |

> **禁入库名单**：Shinya Yamanaka（仅橄榄球仪式合影图注）；安倍晋三（政治人物，仅机构设立事实）；Takasago International Corporation 等企业为机构非人物；Wolf Prize 2001 共同得主 Henri B. Kagan 在**本人页面未点名**（仅 Sharpless 页面明载）——Noyori 篇不入 Kagan，由 Sharpless 篇入库。

## 8. 奖项清单

- Nobel Prize in Chemistry（2001，与 Knowles 共享半奖；另一半 Sharpless）
- Wolf Prize in Chemistry（2001）
- Matsunaga Prize（1978）
- Chuniichi Culture Award（1982）
- The Chemical Society of Japan Award（1985）
- John G. Kirkwood Award（1991，ACS 与 Yale 联合）
- Asahi Prize（1992）
- Tetrahedron Prize（1993）
- Japan Academy Prize（1995）
- Arthur C. Cope Award（1997）
- Chirality Medal（1997）
- King Faisal International Prize（1999）
- Lomonosov Gold Medal（2009）
- Foreign Member of the Royal Society，ForMemRS（2005）
- 荣誉博士：University of Rennes 1（2000，1995 年曾在此授课）、Technical University of Munich 与 RWTH Aachen University（2005）、Institute of Chemical Technology Mumbai（2018-02-23）等
- The Ryoji Noyori Prize：以其命名的奖项（对称性致敬）
- （metadata 注记：Order of Culture / Person of Cultural Merit 等见 frontmatter，正文未逐项展开——不单独成页）

## 9. 机构清单

- 教育：Nada Junior and Senior High School → 京都大学工学部工业化学科（1961 学士；1963 硕士）→ 京都大学 DEng（1967）
- 任职：京都大学工学部助手（1963–1967）→ 副教授（1968）→ Harvard 博士后（Corey 组）→ 名古屋大学教授（1972–，终身基地）→ RIKEN 理事长（2003–2015，年度预算 8 亿美元）
- 公职：教育再生会议主席（2006 年后，安倍内阁设立）
- 纪念：名古屋大学野依纪念物质科学研究馆 / 野依纪念学术交流馆（插图用）

## 10. 终审清单

- [ ] 生卒 1938-09-03 / 在世；出生地 Kobe（不采 metadata 的 Ashiya）
- [ ] 2001 表述：与 Knowles 平分一半（氢化）、Sharpless 另一半（氧化）；获奖理由英文原文准确
- [ ] DEng（工学博士）口径正确；Nozaki=博士导师 / Corey=博士后导师 不混
- [ ] 萘普生 97% ee / 薄荷醇 3000 吨（扩产后）94% ee / 左氧氟沙星 Ru-BINAP 数字准确
- [ ] 四条引语逐字对照 page.md 原文；无无溯源"原话"
- [ ] Yamanaka / 安倍 晋三不作关系入库、不作政治评价
- [ ] 入库对手方名：William Standish Knowles / Karl Barry Sharpless / Hitoshi Nozaki / Elias James Corey / Hideki Yukawa / Philip G. Jessop（规范全名）
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Ryōji_Noyori/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`Study with a fresh and straightforward mind!` 工作照裁剪就位；确认未误用与 Yamanaka 的合影作头像
- [ ] **国籍**：封面顶部明示日本
- [ ] **引语核对**：全部引语在 page.md 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一；日文长音符（ō）渲染正常
- [ ] 与 2001 批次（Knowles / Sharpless 篇）的获奖格局表述交叉一致

---

> **开始执行。每完成一步向主控汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
