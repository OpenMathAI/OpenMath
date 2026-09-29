# Akira Suzuki（铃木章）立传提示词

> qid=Q105949 · 1930-09-12 – 在世 · 日本化学家 · 21 世纪 · 诺贝尔化学奖（2010，与 Richard F. Heck、Ei-ichi Negishi 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Akira_Suzuki_chemist/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次执行的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像取 `images/`；infobox 2010 年照片可用；若无真实肖像则用装饰圆占位，图注注明）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 硼之偶联的 Master\enspace·\enspace 日本`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地、教育、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「硼酸 / 偶联键」母题——离散圆点暗示芳基硼酸与芳基卤在钯配合物牵线下的温和结合。
5. **表格语义化 + 公式框**（★ Sanger 版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），Suzuki 偶联通式（芳基/乙烯基硼酸 + 芳基/乙烯基卤，Pd(0) 催化）即最好的具象化（page.md 附 Suzuki Coupling Full Mechanism 2 机理图可作版式参照）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Akira Suzuki（日文 鈴木 章；中文惯称：铃木章；目录名 `Akira_Suzuki_chemist` 以与同名人物区分）
- **生卒**：1930-09-12 生于日本北海道鵡川（Mukawa）——**在世**（页面无卒日，留白）
- **国籍**：Japan（日本）
- **身份**：化学家；北海道大学名誉教授（荣退后辗转冈山理科大学等）
- **家庭**：高中时父亲去世（page.md 仅一句）；**配偶、子女页面无载，禁写**
- **教育轨迹**：北海道苫小牧东高中 → 北海道大学（化学；本科 → 博士 → 助教授 → 教授）
- **转折之书**：少年最爱算术本欲学数学，因读到 Louis Fieser《Textbook of Organic Chemistry》与 Herbert C. Brown《Hydroboration》两本书转向有机合成
- **导师**：Herbert C. Brown（Purdue 博士后导师，1963–1965；1979 诺贝尔化学奖）；北海道大学博士导师**页面无载**
- **研究领域**：有机化学——有机硼化学、钯催化交叉偶联（Suzuki 反应/Suzuki–Miyaura 偶联）、有机合成方法学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **鵡川少年（1930）**：生于北海道 Mukawa；高中丧父；本志在数学——一本 Fieser 教科书与一本 Brown《Hydroboration》改写了人生。
2. **北海道大学一以贯之**：从本科到博士到助教授到教授——除 Purdue 两年的"留学插叙"外，主阵地从未离开北大（Hokudai）。
3. **Purdue 岁月（1963–1965）**：随 Herbert C. Brown 做博士后——硼化学的真传。
4. **归国与偶联（1965→1979）**：回北大后任教授；与助手 **Norio Miyaura** 研究偶联反应——1979 年发表 Suzuki 反应。
5. **Suzuki 反应的定义**：芳基/乙烯基硼酸与芳基/乙烯基卤在 Pd(0) 配合物催化下的偶联——四大"名字反应"中最温和的一支。
6. **为什么好用**：有机硼酸**耐水耐空气、易处理、条件温和**——诸交叉偶联法中最易用者（page.md 口径）。
7. **机理图谱**：Suzuki Coupling Full Mechanism 2（氧化加成→转移金属化→还原消除）成为教科书画法。
8. **无专利的开放哲学**：以政府经费支持为由不申请专利——偶联技术全球普及，相关论文与专利**逾 6,000 篇**（page.md 口径）。
9. **1994 荣退与晚年教职**：北大退休后，冈山理科大学（1994–95）、仓敷芸術科学大学（1995–2002）；特邀教授：Purdue（2001）、中研院与台大（2002）、成功大学荣誉讲座（2016）。
10. **2010 诺贝尔化学奖**：与 Heck、Negishi 共享（官方口径 "for palladium-catalyzed cross couplings in organic synthesis"）；同年文化勋章、文化功劳者。
11. **化学的辩护（2011）**：国际化学年接受 UNESCO《Courier》访谈——"有人把化学仅仅看作污染产业，但那是个错误……"（page.md 明载可引）。
12. **给年轻化学家的话（2014）**：回答华裔学生提问 "...above all else, you must learn to see through the appearance to perceive the essence."（page.md 明载可引）。
13. **小行星与学会**：小行星 **87312 Akirasuzuki** 以他命名；2003 日本学士院奖、2009 Paul Karrer 金奖、2011 日本学士院会员。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深藏青 deepnavy） | `#1E3A5F` | 有机硼化学的深藏青基调 / 北国学术的沉静（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（Suzuki 反应 badgeSuz） | `#2E5A9E` | 蓝芳基硼酸 × 芳基卤，Pd(0) 催化 |
| 分类色 2（硼化学 badgeBoron） | `#1B7A43` | 绿氢硼化传承 / 有机硼酸性质 |
| 分类色 3（开放哲学 badgeOpen） | `#D97B29` | 琥珀无专利 / 6,000+ 论文与专利 |
| 分类色 4（传承与科普 badgeTeach） | `#C0395B` | 玫瑰 Brown 门下 / Miyaura / UNESCO 访谈 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「硼酸与卤代物温和相接」的偶联意象。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Shine Like The Sun** — Really Slow Motion（文件 `music_audio/inspiring-electronic/15-w6kT1BfvETI-...Shine Like The Sun (Epic Beautiful Uplifting).wav`；不要复制 wav 文件）
- **风格**：明亮上扬 / 壮美管弦 / 温暖的史诗感
- **匹配理由**：
  - "Shine Like The Sun" 匹配三位得主中**唯一在世**者的人生基调——温和、长寿、开放，如阳光普照的普及型方法
  - 明亮上扬匹配 Suzuki 反应"温和好用、全球普及"的品格——不是最激烈的革命，而是最广的日光
  - 壮美而不冷峻，匹配北海道大地与北大学派的气质
- **时长**：以实际曲目时长为准，ffmpeg `-shortest` 自动对齐 15 页 × 7 秒 ≈ 105 秒

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 硼之偶联的 Master / Akira Suzuki 1930– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/出生地/教育/师承/领域/荣誉）
03  铃木章的一生 — Sanger 式时间线（10 节点：1930→1950s→1959→1963→1965→1979→1994→2003→2010→2011）
04  鵡川与两本书 (1930–1950s) — 表格「时间|事件|结果」（丧父 / Fieser 书 / Brown 书）
05  北海道大学 (1950s–1963) — 表格「阶段|方向|结果」（本科→博士→助教授）
06  Purdue：Brown 门下 (1963–1965) — 表格「职位|训练|结果」+ 公式框：氢硼化（Hydroboration）传承
07  归国与偶联的诞生 (1965–1979) — 表格「人物|合作|结果」（Miyaura）+ 公式框：Suzuki 反应通式
08  为什么是硼 — 表格「试剂|性质|优势」+ 公式框：耐水耐空气 / 条件温和
09  无专利的开放哲学 — 表格「选择|理由|影响」+ 公式框：6,000+ 论文与专利
10  2010 诺贝尔化学奖 — 公式框：官方理由 "for palladium-catalyzed cross couplings in organic synthesis"；文化勋章 / 文化功劳者
11  荣誉 — Sanger 式「类别|代表|意义」表格（化学会奖 1989 / 学士院奖 2003 / Karrer 金奖 2009 / Nobel 2010 / 学士院会员 2011 / 小行星 87312）
12  化学的辩护 — 公式框 + 引语页：UNESCO Courier 2011 访谈原句
13  给年轻化学家的话 — 四分类遗产盒 + 2014 "see through the appearance to perceive the essence"
14  结尾 — 「温和，也可以是最大的力量。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2010 诺奖口径 | 与 Heck、Negishi **三人共享**；官方理由原文 "for palladium-catalyzed cross couplings in organic synthesis"（Heck 页面明载；本页仅写 jointly awarded）——三篇统一用此英文原句 |
| 年代分工 | Heck 反应 1960s 末（芳基汞/烯烃）；Negishi 偶联（有机锌）与 **Suzuki 反应 1979 年发表**（有机硼）——试剂路线不同；勿写"Suzuki 1970s 末'发明偶联'"这类越界句 |
| 反应命名 | page.md 用 "Suzuki reaction"；学界亦称 Suzuki–Miyaura coupling（Heck 页面口径）——两称可并列，但共同作者 **Norio Miyaura** 必须出现 |
| Miyaura 身份 | 是铃木的**助手**（assistant），共同研究偶联——colleague 口径；页面未载其生卒，禁写 |
| 在世 | **页面无卒日，在世留白**——封面与时间线终点不写卒年；"享年"类表述禁用 |
| 博士导师 | 北海道大学博士导师**页面无载**——禁写、禁入库；师承只入 Brown（Purdue 博士后导师） |
| 家庭 | 高中丧父一句带过；**配偶子女页面无载禁写**（与 Negishi 篇的 Sumire Suzuki 无任何关联——同名陷阱） |
| 引语红线 | 可引原文仅两处：2011 UNESCO Courier 访谈句与 2014 给学生答句——均须注明出处年份；其余转述 |
| "6,000 篇" | "more than 6,000 papers and patents related to Suzuki reaction"——须保留"论文与专利合计"口径，勿拆成"论文 6,000 篇" |
| 小行星 | 87312 Akirasuzuki——"以他命名"页面明载可写；勿写"发现者是他" |
| 同名区分 | 与根岸英一之妻 Sumire Suzuki、与页面上其他 Suzuki 无关；目录/文件名用 `Akira_Suzuki_chemist` |
| 两校职位 | 1994–95 冈山理科大学、1995–2002 仓敷芸術科学大学（Kurashiki University of Science and the Arts）——勿混并年段 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q105949 | ✅（新建 #NEW） |
| name_zh | 铃木章 | ✅ |
| name_en | Akira Suzuki（page.md 规范名） | ✅ |
| birth_date | 1930-09-12 | ✅ |
| death_date | （空——在世，页面无载） | ✅ |
| nationality | Japan | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | chemistry（person_field 细分：organoboron chemistry / palladium-catalyzed cross-coupling / organic synthesis，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 同事 / 共同得主**（★红线：只收 page.md 正文或 infobox 明载的关系）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Herbert C. Brown | 师→生（博士后导师） | Purdue 1963–1965；1979 诺贝尔化学奖（库内已有记录） |
| colleague | Norio Miyaura | 无向 | 与助手共同研究偶联，1979 发表 Suzuki 反应 |
| co-honored | Richard F. Heck | 无向 | 2010 诺贝尔化学奖共同得主 |
| co-honored | Ei-ichi Negishi | 无向 | 2010 诺贝尔化学奖共同得主 |

> **禁入库名单**（页面无载，一律不建关系）：配偶/子女（无载）；北大博士导师（无载）；Louis Fieser（著作影响，非人际关系，且其"转向化学"叙事已含于正文）；根岸英一之妻 Sumire Suzuki（同姓无关）。Fieser 与 Brown 两书若需在正文表达影响，用文字叙述不入库。

## 8. 奖项清单

- Nobel Prize for Chemistry（2010，与 Heck / Negishi 共享）
- Weissberger-Williams Lectureship Award（1986）
- Korean Chemical Society Award（1987）
- Chemical Society of Japan Award（1989）
- DowElanco Lectureship Award（1995）
- The H. C. Brown Lecture Award（2000）
- Japan Academy Prize 日本学士院奖（2003）
- Paul Karrer Gold Medal（2009）
- Special Member of Royal Society of Chemistry（2009）
- Person of Cultural Merit 文化功劳者（2010）；Order of Culture 文化勋章（2010）
- Member of the Japan Academy（2011）
- 小行星 87312 Akirasuzuki 命名；刚果共和国邮票（2011）；成功大学荣誉讲座（2016）

## 9. 机构清单

- 教育：北海道苫小牧东高中 → 北海道大学（化学，本科—博士）
- 任职：北海道大学（助教授→教授，至 1994 退休）
- 退休后：冈山理科大学（1994–1995）→ 仓敷芸術科学大学（1995–2002）
- 特邀/讲席：Purdue University（2001）、Academia Sinica 与 National Taiwan University（2002）、National Cheng Kung University 荣誉讲座（2016）、University of Wales（infobox Workplaces 载）

## 10. 终审清单

- [x] 生于 1930-09-12 Mukawa（北海道）；**在世留白**，无卒日
- [x] 2010 三人共享（Heck / Negishi）表述准确；三篇诺奖理由英文原句统一
- [x] Suzuki 反应 1979 发表、与 Miyaura 合作——主从与合作者口径正确
- [x] Brown 是 Purdue 博士后导师；北大博士导师无载禁写
- [x] 家庭仅"高中丧父"一句；配偶子女无载禁写
- [x] 引语仅 2011/2014 两处原文并注明出处；"6,000 篇"口径为论文与专利合计
- [x] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Akira_Suzuki_chemist/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/` 内真实肖像已就位，否则装饰圆占位并注明
- [ ] **国籍**：封面顶部明示日本
- [ ] **引语核对**：中文引号内原话必须能在 page.md 找到；无原话一律改间接转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 2010 另两篇（Heck、Negishi）口径互查：共享得主名、诺奖理由、年代分工一致
