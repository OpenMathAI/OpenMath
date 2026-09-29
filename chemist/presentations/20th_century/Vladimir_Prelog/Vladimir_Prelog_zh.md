# Vladimir Prelog（弗拉迪米尔·普雷洛格）立传提示词

> qid=Q83501 · 1906-07-23 – 1998-01-07 · 克罗地亚–瑞士化学家 · 20 世纪 · 诺贝尔化学奖（1975，与 John Cornforth 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Vladimir_Prelog/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 高斯式时间线 + 表格语义化 tabularx + 公式展示框 + 气泡背景。

---

## 0. 正文形式说明（参考 Sanger 桑格模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像下载后放 `images/`；Commons 404 则按 Wikipedia REST API 回退，再失败用装饰圆占位并在 Review 记录）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace CIP 规则的共同缔造者\enspace·\enspace 克罗地亚 / 瑞士`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、国籍变迁、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「手性 / 优先级」母题——成对镜像圆点暗示对映体与 CIP 序列规则。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Vladimir Prelog（中文惯称：弗拉迪米尔·普雷洛格；ForMemRS）
- **生卒**：1906-07-23 生于萨拉热窝（时属奥匈帝国波斯尼亚黑塞哥维那共管领）→ 1998-01-07 逝于瑞士苏黎世，享年 91
- **国籍变迁**：奥匈帝国（出生）→ 南斯拉夫王国 → 瑞士（1959 年入籍）；克罗地亚裔
- **身份**：克罗地亚–瑞士有机化学家（正文 intro 口径 Croatian-Swiss；frontmatter description 作 Bosnian-Swiss——以正文为准，见 §5）
- **家庭**：父亲 Milan 为萨拉热窝文科中学历史教授、后任教萨格勒布大学；1933 年娶 Kamila Vitek，1949 年得子 Jan
- **教育轨迹**：
  - 萨拉热窝小学起步；1915（9 岁）随父母迁萨格勒布；1919–1921 奥西耶克文科中学（教师 Ivan Kuria 点燃化学兴趣）
  - 1921（15 岁）在德国《Chemiker-Zeitung》发表短文 „Eine Titriervorrichtung"（滴定装置）
  - 1924 萨格勒布完成中学；赴布拉格
  - Czech Technical University in Prague：1928 化学工程文凭；1929 Sc.D.
- **导师**：Emil Votoček（博士教师）；Rudolf Lukeš（Votoček 的助手与导师，领他进入有机化学世界）
- **研究领域**：有机化学、生物化学——立体化学、构象分析、CIP 优先级规则、生物碱与抗生素天然产物

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **萨拉热窝的孩童（1906–1915）**：8 岁时（1914）恰站在斐迪南大公遇刺地点附近——帝国黄昏的亲历者。
2. **奥西耶克的化学火种（1919–1921）**：教师 Ivan Kuria 唤醒其对化学的热情；15 岁即在《Chemiker-Zeitung》发表滴定装置短文；与 Kuria 终生通信。
3. **布拉格求学（1924–1929）**：遵父愿赴布拉格；Votoček 门下获 Sc.D.；Lukeš 引其入门有机化学。
4. **大萧条里的工业化学家（1929–1935）**：学术界职位稀缺，在布拉格 G.J. Dríza 公司负责稀有化学品生产；业余研究可可树皮生物碱；带出第一位博士生（公司雇主）。
5. **萨格勒布讲席（1935–1941）**：任 University of Zagreb 讲师，讲有机化学与化学工程；受药厂 "Kaštel"（今 Pliva）资助研究奎宁类化合物；开发出商业上成功的磺胺药 Streptazol 生产法。
6. **金刚烷首合成（1941）**：在萨格勒布完成金刚烷（adamantane）的首次合成——从摩拉维亚油田分离出的奇异笼状烃。
7. **战火中的出走（1941）**：Richard Kuhn 邀其赴德讲学；Prelog 借机求助 Lavoslav Ružička，以两份邀请为跳板携妻经德国逃往苏黎世；得 CIBA 资助入职 ETH 有机化学实验室。
8. **氮手性中心（1944）**：以色谱法在手性底物上拆分 Tröger's 碱对映体——证明不只碳，氮原子也可作手性中心（多年悬案的实验回答）。
9. **中环与构象理论（1940s）**：以偶姻缩合合成 8–12 元中环化合物，以"非经典张力"解释其异常反应性；对 Bredt 规则作出贡献（环足够大时桥头可有双键）；1949 应邀作化学会伦敦首个 Centenary Lecture。
10. **天然产物与抗生素**：阐明茄碱（solanine）结构；续攻金鸡纳生物碱与士的宁——证明 Robert Robinson 的士的宁结构式不正确（自己的式子也不对，但声望大增）；后与 Barton、Jeger、Woodward 合作芳香 Erythrina 生物碱；转向微生物代谢产物，阐明 nonactin、boromycin、rifamycins 结构。
11. **ETH 登顶（1952/1957）**：1952 正教授；1957 接替 Ružička 出任实验室主任——因厌恶行政而首创轮值主席制。
12. **CIP 规则（1954–）**：与 Robert Sidney Cahn、Christopher Kelk Ingold 共建以"序列规则"定义绝对构型的 CIP 系统，合发两文；Cahn/Ingold 去世后独自发表第三篇。
13. **1975 诺贝尔化学奖**：获奖理由 "for his research into the stereochemistry of organic molecules and reactions"（有机分子与反应的立体化学），与 John Cornforth 共享；1986 年南斯拉夫科学院与艺术学院荣誉成员；骨灰 2001-09-27 安葬萨格勒布 Mirogoj 公墓，2008 布拉格立纪念碑。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深湖青 deepcyan） | `#0F4C5C` | 立体化学镜像世界的冷峻与清晰（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（CIP 规则 badgeCIP） | `#2E6E8E` | 青蓝序列规则 / 绝对构型 |
| 分类色 2（天然产物 badgeNat） | `#1B7A43` | 绿生物碱 / 抗生素结构 |
| 分类色 3（中环与构象 badgeRing） | `#D97B29` | 琥珀 8–12 元环 / 非经典张力 |
| 分类色 4（金刚烷 badgeAdam） | `#C0395B` | 玫瑰笼状烃首合成 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「手性镜像」成对圆点。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Shine Like The Sun** — Really Slow Motion（`music_audio/inspiring-electronic/15-w6kT1BfvETI-Really Slow Motion - Shine Like The Sun (Epic Beautiful Uplifting).wav`；不要复制 wav 文件，Makefile 引用即可）
- **风格**：昂扬 / 明亮 / 史诗抒情
- **匹配理由**：
  - "明亮" 匹配其一生横跨四国、屡绝处逢生（大萧条、战火出逃）终至 ETH 之巅的轨迹
  - "昂扬" 匹配 CIP 规则成为全世界化学家的通用语言的深远成就
  - "史诗抒情" 匹配传记叙事——萨拉热窝 → 奥西耶克 → 布拉格 → 萨格勒布 → 苏黎世 → 1975 诺奖
- **时长**：以实际曲目时长为准 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — CIP 规则的共同缔造者 / Vladimir Prelog 1906–1998 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/国籍变迁/出生地/去世地/教育/博士/师承/领域/荣誉）
03  普雷洛格的一生 — 高斯式时间线（10 节点：1906→1921→1929→1935→1941→1944→1954→1957→1975→1998）
04  早年：萨拉热窝与奥西耶克 (1906–1924) — 表格「时间|事件|结果」（Kuria、15 岁首篇短文）
05  布拉格：Votoček 与 Lukeš (1924–1929) — 表格「时间|事件|结果」
06  大萧条与萨格勒布 (1929–1941) — 表格「挑战|方法|结果」+ 公式框：金刚烷 C10H16 首合成
07  出走苏黎世 (1941) — 表格「背景|路径|结果」（Kuhn 邀请 / Ružička 援手 / CIBA-ETH）
08  氮手性与中环构象 (1944–1949) — 表格「问题|方法|结果」+ 公式框：Tröger's 碱拆分证明氮手性
09  天然产物与抗生素 (1950s–) — 表格「对象|方法|结果」（solanine / 士的宁 / nonactin / boromycin / rifamycins）
10  CIP 序列规则 (1954–) — 表格「问题|方法|结果」+ 公式框：R/S 绝对构型判据 · 三篇论文
11  1975 诺贝尔化学奖 — 表格「人物|方向|结果」（与 Cornforth 共享 · Prelog=有机分子与反应的立体化学）
12  荣誉与晚年 — 高斯式「类别|代表|意义」表格（ForMemRS 1962 / Davy 1967 / Marcel Benoist 1964 / Chirality Medal 1992）
13  遗产：立体化学的通用语言 — 四分类遗产盒 + 公式框：Prelog strain / Prelog's rule / Klyne–Prelog system
14  结尾 — 「分子在手性中写下自己的名字。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1975 获奖理由 | 官方口径 "for his research into the stereochemistry of organic molecules and reactions"——勿写成 CIP 规则本身获奖；勿把 Cornforth 的"酶催化立体化学"安到 Prelog 头上 |
| 共享方向 | 1975 与 **John Cornforth** 共享——勿写成独享 |
| 族裔口径 | 正文 intro 作 **Croatian-Swiss**；frontmatter description 作 Bosnian-Swiss——以正文 intro 为准（生于萨拉热窝、克罗地亚裔）；国籍叙事写变迁（奥匈→南斯拉夫→瑞士 1959） |
| 三中心两电子键式错误 | 士的宁：Prelog 证明 **Robinson 的式子不正确**，但他自己的式子也不对——勿写"Prelog 确定了士的宁正确结构"；Robinson 亦非其"论敌"，系学术竞争关系不作为关系入库 |
| 金刚烷 | 1941 **首次合成**（结构分离自摩拉维亚油田）——勿写"发现金刚烷" |
| 氮手性 | 1944 色谱拆分 Tröger's 碱**证明**氮可为手性中心——系多年悬想的实验证实，勿写"首次提出氮手性" |
| CIP 三人 | 与 Cahn、Ingold 合作发表两篇，第三篇在两人去世后由 Prelog 独自发表——勿写三人各一篇 |
| 博士学位 | 布拉格捷克理工学院 **Sc.D. 1929**（1928 化学工程文凭）——勿写 PhD/苏黎世 |
| 儿子出生年 | 1933 年结婚、1949 年得子 Jan——勿把两个年份混写 |
| 引语红线 | page.md 正文唯一整段引语是 1922-03-16 致 Kuria 信（学钳工/冬季运动/萨格勒布分析化学所）——如引用须整段忠实；其余一律间接转述；"第一次/唯一"类断言禁写 |
|metadata 噪声| frontmatter 奖项含 August Wilhelm von Hofmann Medal、Roger Adams Award、Paracelsus Prize、Robert Robinson Award 等，正文 infobox 未给年份——展示以正文 infobox 年份为准，无年份奖项慎写 |
| 遇刺事件 | 只写"8 岁时站在遇刺地点附近"这一句实载，勿引申叙事 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q83501 | ✅ |
| name_zh | 弗拉迪米尔·普雷洛格 | ✅ |
| name_en | Vladimir Prelog | ✅ |
| birth_date | 1906-07-23 | ✅ |
| death_date | 1998-01-07 | ✅ |
| nationality | Austria-Hungary（rank 0）→ Yugoslavia（rank 1）→ Switzerland（rank 2） | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | organic chemistry（person_field 细分见下表，带 rank） | ✅ |

**person_field rank 表**：

| field | rank | 语义 |
|---|---|---|
| organic chemistry | 0 | 学科大类（frontmatter field_of_work） |
| stereochemistry | 1 | 立体化学 / CIP 规则（诺奖方向） |
| conformational analysis | 2 | 中环构象 / 非经典张力 |
| natural products | 3 | 生物碱与抗生素结构阐明 |

## 7. 社会关系入库清单

**★ 红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Emil Votoček | 师→生（博士教师） | 布拉格捷克理工学院 Sc.D.（1929） |
| influence | Rudolf Lukeš | 无向 | Votoček 的助手与导师，引 Prelog 入有机化学之门 |
| colleague | Leopold Ružička | 无向 | 1941 援手助其赴瑞士；ETH 前任实验室主任（1957 接任）。★规范名用 Leopold Ružička（Wikipedia 条目名/库内 Q122996），勿写 Lavoslav Ružička（page.md 正文用名，防分裂 stub——本批曾因此产生分裂 stub 已合并） |
| colleague | Richard Kuhn | 无向 | 1941 邀请赴德讲学（间接促成出逃瑞士） |
| colleague | Robert Sidney Cahn | 无向 | CIP 序列规则共同提出者（两篇合作论文） |
| colleague | Christopher Kelk Ingold | 无向 | CIP 序列规则共同提出者（两篇合作论文） |
| colleague | Derek Barton | 无向 | 合作阐明芳香 Erythrina 生物碱结构 |
| colleague | Robert Burns Woodward | 无向 | 合作阐明芳香 Erythrina 生物碱结构 |
| colleague | Oskar Jeger | 无向 | 合作阐明芳香 Erythrina 生物碱结构 |
| co-honored | John Cornforth | 无向 | 1975 诺贝尔化学奖共同得主 |
| spouse | Kamila Vitek | 无向 | 1933 结婚；1949 得子 Jan |

> **禁入库名单（非个人关系或不足以成关系）**：Robert Robinson（士的宁结构式纠错系学术事件）、Ivo Andrić（仅同挂纪念牌匾）、Ivan Kuria（中学教师）、G.J. Dríza（雇主）。

## 8. 奖项清单

- Centenary Prize（1949）；化学会伦敦首个 Centenary Lecture（1949）
- Marcel Benoist Prize（1964）
- Fellow of the Royal Society，ForMemRS（1962）
- Davy Medal（1967）
- Paul Karrer Gold Medal（1974）
- Nobel Prize in Chemistry（1975；与 John Cornforth 共享）
- Chirality Medal（1992）
- American Academy of Arts and Sciences（1960）；United States National Academy of Sciences（1961）；American Philosophical Society（1976）
- Yugoslav Academy of Sciences and Arts 荣誉成员（1986）；Serbian Academy of Sciences and Arts 成员
- 荣誉博士：University of Zagreb、Weizmann Institute、University of Paris 等（frontmatter 明载）

## 9. 机构清单

- 教育：III Gymnasium Osijek（1919–1921）；萨格勒布完成中学（1924）；Czech Technical University in Prague（1928 文凭 / 1929 Sc.D.）
- 任职：G.J. Dríza 公司（布拉格，1929–1935）；University of Zagreb（1935–1941，Technical Faculty 讲师）；ETH Zürich 有机化学实验室（1941–；1952 正教授；1957 接替 Ružička 任主任，首创轮值主席制）
- 纪念：萨拉热窝故居纪念牌；Mirogoj 公墓（2001 安葬）与克罗地亚科学院纪念碑；布拉格纪念碑（2008）

## 10. 终审清单

- [ ] 生卒 1906-07-23 / 1998-01-07，享年 91，出生地 Sarajevo、去世地 Zürich
- [ ] 1975 与 Cornforth **共享**；获奖理由为"有机分子与反应的立体化学"口径准确
- [ ] 国籍变迁三段式（奥匈→南斯拉夫→瑞士 1959）；族裔口径 Croatian-Swiss（正文 intro）
- [ ] 士的宁表述：只写"证明 Robinson 式子不正确"，勿写"确定正确结构"
- [ ] 金刚烷 1941 首次合成；氮手性 1944 拆分证明；CIP 三人分工准确
- [ ] 引语仅 1922 致 Kuria 信一段，其余不得出现引号"原话"
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Vladimir_Prelog/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：确认肖像就位（Commons/Wikipedia REST API；失败则装饰圆占位并记录）
- [ ] **国籍**：封面顶部明示"克罗地亚 / 瑞士"
- [ ] **引语核对**：仅 1922 致 Kuria 信一段可引，其余不得出现引号"原话"
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Frederick_Sanger_zh.tex）对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾，本提示词不改动该文件。
