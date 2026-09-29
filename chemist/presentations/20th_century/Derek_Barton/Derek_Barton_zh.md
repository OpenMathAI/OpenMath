# Derek Barton（德里克·巴顿）立传提示词

> qid=Q102419 · 1918-09-08 – 1998-03-16 · 英国有机化学家 · 20 世纪 · 诺贝尔化学奖（1969，与 Odd Hassel 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Derek_Barton/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页 + 气泡背景，是本次重写的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像从 `images.txt` / Commons 下载；404 则用装饰圆占位并在 Review 记录）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 构象分析的奠基人\enspace·\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士导师、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「构象 / 环己烷椅式翻转」母题——离散圆点暗示分子在空间中的三维排布。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Sir Derek Harold Richard Barton（中文惯称：德里克·哈罗德·理查德·巴顿；头衔 FRS FRSE，1972 年受封 Knight Bachelor）
- **生卒**：1918-09-08 生于英格兰肯特郡 Gravesend → 1998-03-16 逝于美国得州 College Station，享年 79；安葬于得州 La Grange Cemetery
- **国籍**：United Kingdom（英国）；1986 年移居美国得克萨斯
- **身份**：有机化学家（organic chemist）、1969 年诺贝尔化学奖得主
- **家庭**：父 William Thomas Barton、母 Maude Henrietta Barton（娘家姓 Lukes）；婚姻三次——Jeanne Kate Wilkins（1944-12-20 结婚，育一子）、Christiane Cognet（1969 结婚，1992 去世）、Judith Von-Leuenberger Cobb（1993 结婚；1939–2012）
- **教育轨迹**：
  - Gravesend Grammar School（1926–29）
  - The King's School, Rochester（1929–32）
  - Tonbridge School（1932–35）
  - Medway Technical College（1937–39）
  - 1938 入 Imperial College London，1940 毕业，1942 获有机化学 PhD
- **博士导师**：Ian Heilbron（infobox 明载）
- **研究领域**：有机化学、立体化学——构象分析、天然产物几何结构、自由基化学命名反应

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **格雷夫森德少年（1918）**：肯特郡 Gravesend 出生，辗转四所学校完成中学教育—— Gravesend / Rochester / Tonbridge / Medway Technical College。
2. **帝国学院（1938–1942）**：1938 入 Imperial College London，1940 毕业，1942 获有机化学博士——战时伦敦完成科班训练。
3. **战时工业化学（1942–1945）**：政府研究化学家（1942–44）→ 伯明翰 Albright and Wilson（1944–45）；1946–49 任 ICI Research Fellow。
4. **哈佛访学（1949–1950）**：任哈佛大学天然产物化学访问讲师——把英国学派与美国前沿接通。
5. **构象分析（1950）**：★ 核心贡献——综合化学物理学家（特别是 Odd Hassel）积累的实验结果，证明有机分子存在**优先构象**（preferred conformation），创立构象分析方法。
6. **Birkbeck 与格拉斯哥（1953–1955）**：1953 任 Birkbeck College 教授；1955 任格拉斯哥大学 Regius Professor of Chemistry。
7. **回归帝国学院（1957）**：任 Imperial College 有机化学教授；1958 MIT Arthur D. Little 访问教授、1959 伊利诺伊/威斯康星 Karl Folkers 访问教授。
8. **1969 诺贝尔化学奖**：与 Odd Hassel 共享，理由 "contributions to the development of the concept of conformation and its application in chemistry"——用构象分析确定众多天然产物分子的几何结构。
9. **以他命名的反应**：Barton reaction、Barton decarboxylation、Barton–McCombie deoxygenation、Barton–Kellogg reaction、Barton–Zard synthesis、Barton vinyl iodine procedure、Barton's base——有机化学史上罕见的「一人多名」。
10. **法国岁月（1978）**：出任法国 Gif-sur-Yvette 的 Institut de Chimie des Substances Naturelles（ICSN）所长。
11. **得州晚年（1986–1998）**：移居美国，任 Texas A&M University distinguished professor 12 年直至去世；1996 出版文集 *Reason and Imagination: Reflections on Research in Organic Chemistry*。
12. **荣誉满载**：Corday-Morgan 奖首位得主（1949）、FRS（1954）、Davy Medal（1961）、Royal Medal（1972）、Knight Bachelor（1972）、Copley Medal（1980）、Priestley Medal（1995）；1977 年英国皇家化学学会百年，英国邮政为其在内的 6 位英国诺奖化学家发行邮票。
13. **传承**：博士生 Jack Baldwin、Anthony Barrett、David Crich；母校 Tonbridge School 2019 年落成的 Barton Science Centre 以他命名。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深松绿 pinegreen） | `#2F5D50` | 天然产物与环系结构的沉稳底色（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（构象分析 badgeConf） | `#1E5A8A` | 蓝优先构象 / Hassel 数据 |
| 分类色 2（命名反应 badgeRxns） | `#8A3A1E` | 琥珀棕 Barton 反应家族 |
| 分类色 3（天然产物 badgeNatProd） | `#4A6B1E` | 橄榄绿萜类 / 生物碱几何结构 |
| 分类色 4（荣誉与传承 badgeHonor） | `#5B2A6E` | 紫 FRS / Copley / Knight |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「构象 / 三维分子几何」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Cinematic Experience** — Alex-Productions（文件：`music_audio/alex-productions/48-QL3O8MUFAm4-Cinematic-Experience.wav`；不要复制 wav 到人物目录，video 阶段按路径引用）
- **风格**：电影感 / 大气 / 叙事推进
- **匹配理由**：
  - "电影感" 匹配巴顿一生的三段式迁徙叙事——英国 → 法国 ICSN → 得州 A&M，横跨大西洋两岸
  - "大气" 匹配构象分析的开创气魄——把二维纸面分子式立起来看
  - "叙事推进" 匹配从战时工业化学到诺奖到命名反应家族的持续产出
- **时长核对**：video 阶段用 ffmpeg `-shortest` 自动对齐 15 页 × 7 秒 ≈ 105 秒

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 构象分析的奠基人 / Derek Barton 1918–1998 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士导师/出生地/去世地/领域/荣誉）
03  巴顿的一生 — Sanger 式时间线（10 节点：1918→1942→1949→1950→1955→1957→1969→1978→1986→1998）
04  早年与教育 (1918–1942) — 表格「时间|学校|结果」
05  战时与学术起步 (1942–1949) — 表格「时间|岗位|结果」
06  构象分析 (1950) — 表格「问题|方法|结果」+ 公式框：优先构象概念（Hassel 数据 → 巴顿综合）
07  教席与访学 (1953–1959) — 表格「年份|机构|职位」
08  1969 诺贝尔化学奖 — 表格「人物|贡献|理由」+ 公式框：获奖理由原文
09  命名反应家族 — 表格「反应|类型|用途」（Barton reaction / 脱羧 / McCombie 脱氧 / Kellogg / Zard）
10  ICSN 与得州岁月 (1978–1998) — 表格「时间|机构|结果」
11  荣誉与骑士 — Sanger 式「类别|代表|意义」表格（FRS 1954 / Davy 1961 / Copley 1980 / Priestley 1995 + Knight Bachelor 1972）
12  门生与传承 — 表格「人物|方向|结果」（Jack Baldwin / Anthony Barrett / David Crich + Tonbridge Barton Science Centre）
13  遗产：把分子立起来看 — 四分类遗产盒 + 公式框：构象分析纲领
14  结尾 — 「分子不是平面图形，而是有自己偏爱姿态的立体存在。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1969 获奖口径 | 与 Odd Hassel **共享**（非独享）；理由 "contributions to the development of the concept of conformation and its application in chemistry"（page.md 实载英文原句） |
| 构象分析归属 | 巴顿 1950 年是基于**化学物理学家（特别是 Odd Hassel）**积累的结果做综合与应用——勿写成巴顿一人独立发明构象概念 |
| 博士年份 | 1942 年获 PhD（Imperial College）；1940 年是本科毕业——勿混淆 |
| 教职顺序 | Birkbeck 教授（1953）→ 格拉斯哥 Regius Professor（1955）→ Imperial College 教授（1957）——勿倒序 |
| 骑士封号 | 1972 年受封 Knight Bachelor（同时获 Royal Medal 与法国荣誉军团勋章）——注意与 1980 Copley Medal、1995 Priestley Medal 年份区分 |
| 三次婚姻 | Jeanne Kate Wilkins（1944）、Christiane Cognet（1969，卒 1992）、Judith Von-Leuenberger Cobb（1993，1939–2012）——首次婚姻育**一子**；年份勿写错 |
| 去世地 | 1998-03-16 逝于得州 College Station，享年 79，葬 La Grange Cemetery——勿写回英国 |
| 同名区分 | Barton reaction 与 Thomas Barton 等无关；Barton–McCombie 的 McCombie 是合作者；Barton's base 是 2-tert-丁基-1,1,3,3-四甲基胍 |
| 博士生名单 | infobox 仅载 Jack Baldwin、Anthony Barrett、David Crich 三人——其余 WikiData 条目不入库 |
| 邮票细节 | 1977 年皇家化学学会百年，英国邮政为巴顿**与其他 5 位**诺奖英国化学家发行四枚一套邮票——勿写"单独发行" |
| 引语红线 | page.md 正文无巴顿直接引语——全篇不得杜撰"巴顿说过"，改间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q102419 | ✅ |
| name_zh | 德里克·巴顿 | ✅ |
| name_en | Derek Barton | ✅ |
| birth_date | 1918-09-08 | ✅ |
| death_date | 1998-03-16 | ✅ |
| nationality | United Kingdom | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | organic chemistry（person_field 细分：organic chemistry / stereochemistry / conformational analysis / natural products chemistry，带 rank） | ✅ |
| has_biography | 0（Beamer 立传完成后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 学生 / 共同得主 / 婚姻**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Ian Heilbron | 师→生（博士导师） | Imperial College，1942 年 PhD |
| advisor-student | Jack Baldwin | Barton → 学生 | infobox doctoral students 明载 |
| advisor-student | Anthony Barrett | Barton → 学生 | infobox doctoral students 明载 |
| advisor-student | David Crich | Barton → 学生 | infobox doctoral students 明载 |
| co-honored | Odd Hassel | 无向 | 1969 诺贝尔化学奖共同得主 |
| influence | Odd Hassel | Hassel → Barton | 1950 构象分析基于 Hassel 等化学物理学家的实验结果（page.md 明载，仅此一人点名） |
| spouse | Jeanne Kate Wilkins | 无向 | 1944-12-20 结婚，育一子 |
| spouse | Christiane Cognet | 无向 | 1969 结婚，1992 去世 |
| spouse | Judith Von-Leuenberger Cobb | 无向 | 1993 结婚（1939–2012） |

> metadata.json-only 的关系一律不入库；本页正文与 infobox 之外无新增名单。

## 8. 奖项清单

- Corday-Morgan Medal and Prize（1949，首位得主）
- Tilden Prize（1952）
- Fellow of the Royal Society，FRS（1954）
- Ernest Guenther Award（1957）
- Davy Medal（1961）
- Nobel Prize in Chemistry（1969，与 Odd Hassel 共享）
- Knight Bachelor（1972）；Royal Medal（1972）；Légion d'honneur（1972）
- Copley Medal（1980）
- Priestley Medal（1995）
- 院士类：Leopoldina（1966）、美国 NAS（1970）、American Philosophical Society（1978）、FRSE（1956）、美国艺术与科学院外籍荣誉成员（1959）
- 荣誉博士：Montpellier、Valencia、Metz、Claude Bernard Lyon 1、Paris-XI、Salamanca、香港大学、中国科学院荣誉博士、Paul Cézanne 大学等

## 9. 机构清单

- 教育：Gravesend Grammar School（1926–29）、King's School Rochester（1929–32）、Tonbridge School（1932–35）、Medway Technical College（1937–39）、Imperial College London（1938–1942，PhD）
- 任职：政府研究化学家（1942–44）→ Albright and Wilson（1944–45）→ Imperial College 助教 / ICI Fellow（1946–49）→ 哈佛访问讲师（1949–50）→ Birkbeck College 教授（1953）→ 格拉斯哥 Regius Professor（1955）→ Imperial College 教授（1957）→ ICSN 所长（1978）→ Texas A&M distinguished professor（1986–1998）
- 命名机构：Tonbridge School 的 Barton Science Centre（2019 落成）

## 10. 终审清单

- [x] 生卒 1918-09-08 / 1998-03-16，享年 79，出生地 Gravesend（Kent）、去世地 College Station（Texas）
- [x] 1969 与 Hassel 共享；获奖理由用 page.md 英文原句
- [x] 构象分析表述为"综合 Hassel 等人的结果"——不写独立发明
- [x] 三次婚姻年份与首次婚姻一子表述准确
- [x] 教职顺序 Birkbeck→Glasgow→Imperial 准确
- [x] 博士生仅 Baldwin/Barrett/Crich 三人；正文无直接引语、全篇不杜撰
- [x] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Derek_Barton/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：从 images.txt / Commons 下载；404 用装饰圆占位并记录
- [ ] **国籍**：封面顶部明示英国
- [ ] **引语核对**：全篇不得出现无法在 page.md 溯源的"原话"
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 骨架）对齐

---

> **名单状态**：本文件由 chem-batch-14 生成；`chemist/generate_20th_century_list.py` 由主控统一更新。
> **最重要的事：每写一页就 make，看到溢出就修。**
