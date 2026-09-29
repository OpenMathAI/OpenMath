# Robert Burns Woodward（罗伯特·伯恩斯·伍德沃德）立传提示词

> qid=Q232316 · 1917-04-10 – 1979-07-08 · 美国化学家 · 20 世纪 · 诺贝尔化学奖（1965，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Robert_Burns_Woodward/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像按 `images.txt` / REST API 下载；404 则装饰圆占位并注明）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{project-diagram}\enspace 有机合成艺术的大师\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「全合成路线图」母题——圆点连线暗示多步合成路线中中间体的串联。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），分子式/反应式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Robert Burns Woodward（中文惯称：罗伯特·伯恩斯·伍德沃德；ForMemRS HonFRSE）
- **生卒**：1917-04-10 生于美国马萨诸塞州波士顿 → 1979-07-08 逝于马萨诸塞州剑桥，享年 62（睡梦中心脏病发作）
- **国籍**：United States（美国）
- **身份**：有机化学家——被普遍视为 20 世纪最杰出的合成有机化学家
- **家庭**：母 Margaret Burns（苏格兰移民，自称诗人 Robert Burns 后裔），父 Arthur Chester Woodward（1918 年大流感罹难者之一）；1938 年娶 Irja Pullman（两女 Siiri Anna 1939、Jean Kirsten 1944）；1946 年娶 Eudoxia Muller（艺术家/技术员，Polaroid 相识；育 Crystal Elisabeth 1947、Eric Richard Arthur 1953；婚姻持续至 1972）
- **教育轨迹**：
  - Quincy 公立小学与 Quincy High School（入学前已做完 Gattermann 有机化学教科书的大部分实验）
  - 1928 年（11 岁）通过德国驻波士顿总领事获取德文期刊原始论文——初遇 Diels–Alder 反应原始通讯
  - MIT：1933 入学、1934 秋季学期末因荒废正式课业被开除、1935 秋复学、1936 获 BS、1937 获 PhD（论文《A Synthetic Attack on the Oestrone Problem》，雌酮合成）——同学还在读本科时他已是博士
- **导师**：James Flack Norris 与 Avery Adrian Morton（MIT 规定的名义博士导师；page.md 明载"他是否实际听取过建议并不清楚"）
- **研究领域**：有机化学——复杂天然产物全合成、分子结构测定、Woodward 规则、Woodward–Hoffmann 规则
- **性格侧写**：讲座常三四个小时（最长者定义了时间单位 "Woodward"，其余讲座以 "milli-Woodwards" 计）；不用幻灯片、彩色粉笔在白手帕上排开；蓝癖（西装、汽车、车位皆蓝）；烟不离手、讨厌运动

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **波士顿之子（1917）**：父死于 1918 大流感——由母亲独自抚养；少年时代已完成 Gattermann 教科书大部分实验。
2. **德文原始文献（1928）**：经德国总领事获取期刊论文初遇 Diels–Alder 反应——此后一生反复且有力地使用与研究这一反应。
3. **MIT 传奇（1933–1937）**：被开除→复学→一年 BS→一年 PhD；雌酮合成起步——四年拿完学位的奇迹。
4. **哈佛终身（1937–1979）**：伊利诺伊短暂博士后 → 1937–38 Junior Fellow → 此后终生哈佛；1960 年代任 Donner Professor of Science（免教正式课程，全时研究）。
5. **Woodward 规则（1940 年代初）**：系统收集紫外光谱经验数据，建立推断天然产物结构的经验规则——仪器方法取代繁琐化学降解的革命性开端。
6. **奎宁全合成（1944）**：与博士后 William von Eggers Doering 报道奎宁合成——关键洞见是 Rabe 1905 年已证明 quinotoxine 可转化为奎宁，故合成 quinotoxine 即打通路线；实际工艺太冗长不实用，但宣示了合成可以成为理性科学。
7. **青霉素之争（二战）**：任战时生产委员会青霉素项目顾问；最初为 Peoria 小组错误的三环结构背书、后转向 β-内酰胺立场——与当时权威 Robert Robinson 的 thiazolidine–oxazolone 结构对峙；β-内酰胺最终由 **Dorothy Hodgkin 1945 年用 X 射线晶体学证明正确**。
8. **Woodwardian era（1940 年代末）**：奎宁、胆固醇、可的松、士的宁（strychnine）、麦角酸、利血平、叶绿素、头孢菌素、秋水仙碱——物理有机原理+缜密规划的开创性全合成系列；立体化学与立体选择性合成的先驱（利血平与士的宁合成是里程碑）。
9. **二茂铁结构（1950 年代初）**：与哈佛的 Geoffrey Wilkinson 共同提出二茂铁夹心结构——开启过渡金属有机化学领域；Wilkinson 1973 年与 Ernst Otto Fischer 因此获诺奖；一些历史学家认为伍德沃德本应分享该奖——伍德沃德本人也这么认为，并曾致信诺奖委员会直陈此意。
10. **1965 诺贝尔化学奖（独享）**：官方理由 "for his outstanding achievements in the art of organic synthesis"；1946–1965 间共获提名 111 次；诺奖演讲讲述头孢菌素全合成（刻意把进度赶在授奖仪式前后完成）。
11. **维生素 B12（1960 年代–1973）**：与苏黎世同事 Albert Eschenmoser 合作，近 100 名学生与博士后奋战多年；1973 年发表，约 100 步——当时最复杂的天然产物全合成，至今（截至 2019）无第二例 B12 全合成发表。
12. **Woodward–Hoffmann 规则（1965）**：基于 B12 合成中的观察，请 Hoffmann 用扩展 Hückel 方法做理论验证，共同提出周环反应立体化学规则；Hoffmann 与 Fukui 分享 1981 诺奖——伍德沃德 1979 年去世，诺贝尔奖不追授逝者。
13. **木桶与传承**：Woodward Research Institute（巴塞尔，1963 任所长）；MIT Trustee（1966–1971）、Weizmann 研究所 Trustee；约 200 篇论著（85 篇全文）；培养 200+ 博士生与博士后；1979-07-08 在剑桥睡梦中心脏病离世时正在攻关红霉素（erythromycin）合成。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（钢蓝 steelblue） | `#37548D` | 合成路线图的理性与蓝癖气质（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（全合成 badgeSynth） | `#4A5FA0` | 蓝 B12 / 奎宁 / 士的宁 |
| 分类色 2（结构测定 badgeStruct） | `#1B7A43` | 绿 Woodward 规则 / 紫外与红外光谱 |
| 分类色 3（理论规则 badgeWH） | `#B0432A` | 砖红 Woodward–Hoffmann 规则 / 轨道对称性 |
| 分类色 4（哈佛传承 badgeHarvard） | `#2E6B4F` | 绿哈佛学派 / 200 弟子 |
| 背景 | `#F7F6F9` | 浅灰白（与高斯一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应合成路线图上中间体节点与连线的排布。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**The Flow of Time** — Alex-Productions（`music_audio/alex-productions/35-jqIDnltiDRI-The-Flow-of-Time.wav`，不要复制 wav 文件，Makefile 直接引用该路径）
- **风格**：时间流动 / 宏大 / 深情
- **匹配理由**：
  - "时间流动" 匹配其生涯密度——从 11 岁读德文原始文献到 62 岁猝然离世的紧凑一生
  - "宏大" 匹配 Woodwardian era 的史诗感——一己之力定义了整个合成化学时代
  - "深情" 匹配结尾页——红霉素未竟之作与学生的悼词
- **时长**：对齐 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 有机合成艺术的大师 / Robert Burns Woodward 1917–1979 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  伍德沃德的一生 — 高斯式时间线（10 节点：1917→1933→1937→1944→1950→1953→1965→1963→1973→1979）
04  早年：神童与大流感 (1917–1933) — 表格「时间|事件|结果」
05  MIT 奇迹 (1933–1937) — 表格「年份|事件|结果」
06  Woodward 规则与奎宁 (1940–1944) — 表格「问题|方法|结果」+ 公式框：quinotoxine → quinine 路线
07  青霉素之争与 Hodgkin 交叉 (1943–1945) — 表格「人物|立场|结果」（β-内酰胺最终由 Hodgkin 证明）
08  Woodwardian era (1940s–1960s) — 表格「分子|难点|意义」+ 公式框：利血平/士的宁里程碑
09  1965 诺贝尔化学奖（独享） — 表格「奖项|口径|意义」+ 公式框：官方获奖理由英文原文 · 111 次提名
10  B12 与 Eschenmoser (1960s–1973) — 表格「问题|方法|结果」+ 公式框：约 100 步 · 截至 2019 无第二例
11  Woodward–Hoffmann 规则 (1965/1981) — 表格「人物|贡献|结果」+ 公式框：轨道对称性 · 1981 Hoffmann/Fukui（不追授）
12  荣誉与纪念 — 高斯式「类别|代表|意义」表格（Davy 1959 / National Medal of Science 1964 / Cope 1973 与 Hoffmann 共享 / Copley 1978）
13  遗产：合成的理性与艺术 — 四分类遗产盒 + 公式框：学生悼词句
14  结尾 — 「他证明了：复杂分子的诞生，可以被规划。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 诺奖官方获奖理由 | page.md 明载英文原文：`"for his outstanding achievements in the art of organic synthesis."`——**可整句引用**；中文统一译"表彰其在有机合成艺术中的杰出成就" |
| 独享 | 1965 为**独享**，无共同得主 |
| 与 1973 诺奖 | 二茂铁结构是 Woodward 与 **Wilkinson** 共同提出；1973 诺奖给 Wilkinson 与 Ernst Otto Fischer——"一些历史学家认为伍德沃德本应分享，他本人曾致信诺奖委员会"（page.md 明载可写，但注明是"一些历史学家"口径，勿写成定论） |
| 与 1981 诺奖 | Woodward–Hoffmann 规则 1981 年诺奖给 **Hoffmann 与 Fukui**；伍德沃德 1979 年去世——"诺奖不追授逝者"按 page.md 口径一句带过，勿写成"诺奖委员会欠他一个奖" |
| β-内酰胺 | β-内酰胺结构**最早由 Merck 化学家与 Edward Abraham 提出**；伍德沃德起初背书的是 Peoria 小组的错误三环结构，随后才支持 β-内酰胺——**勿写"伍德沃德提出 β-内酰胺"**；最终由 Dorothy Hodgkin 1945 年晶体学证明（与本批霍奇金篇交叉互认） |
| 奎宁合成 | 1944 年为 **formal total synthesis**（经 quinotoxine；Rabe 1905 转化是关键前提）；page.md 明载"实际太冗长不适合实用规模"——勿写成"解决了疟疾药物短缺" |
| MIT 开除 | 1934 秋季学期末被开除、1935 秋复学——勿美化成跳级；BS 1936、PhD 1937 |
| 博士导师 | Norris 与 Morton 是 MIT 规定的名义导师，page.md 明载"不清楚他是否实际听取建议"——师承关系 note 必须如实注明 |
| 婚姻 | 两段婚姻：Irja Pullman（1938–）、Eudoxia Muller（1946–1972）——第一段离婚 page.md 未明写、只写 1946 再娶，note 措辞"1938 年第一段婚姻"即可，勿写"1946 离婚" |
| 吸烟与性格 | 连锁吸烟、蓝色癖、"Woodward" 时间单位——人物侧写页可用（page.md 明载），但"死于吸烟相关疾病"**页面无载禁写** |
| 死因 | 1979-07-08 剑桥睡梦中心脏病发作，时在攻关红霉素——勿写"实验室事故"或猜测诱因 |
| 学生口径 | infobox Doctoral students 仅 **Foote/Houk/Breslow/Schreiber/Roush/Lemal 六人**；正文 best-known students 叙述名单（Kishi、Dolphin 等）不入师承关系（防噪声），可作正文提及 |
| 同名区分 | Robert Burns Woodward ≠ 诗人 Robert Burns（母系自称后裔）；≠ Robert Robinson（青霉素结构之争的对手方） |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q232316 | ✅ |
| name_zh | 罗伯特·伯恩斯·伍德沃德 | ✅ |
| name_en | Robert Burns Woodward（page.md 规范名；库内无既有记录） | ✅ |
| birth_date | 1917-04-10 | ✅ |
| death_date | 1979-07-08 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | organic chemistry（person_field 细分：organic chemistry / total synthesis / physical organic chemistry / stereochemistry，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 学生 / 合作者 / 配偶**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | James Flack Norris | 师→生（名义博士导师） | MIT 规定导师；page.md 明载"是否实际听取建议不详" |
| advisor-student | Avery Adrian Morton | 师→生（名义博士导师） | MIT 规定导师；同上 |
| advisor-student | Christopher Foote | 伍德沃德→学生 | infobox 博士生 |
| advisor-student | Ken Houk | 伍德沃德→学生 | infobox 博士生 |
| advisor-student | Ronald Breslow | 伍德沃德→学生 | infobox 博士生 |
| advisor-student | Stuart Schreiber | 伍德沃德→学生 | infobox 博士生 |
| advisor-student | William R. Roush | 伍德沃德→学生 | infobox 博士生 |
| advisor-student | David M. Lemal | 伍德沃德→学生 | infobox 博士生 |
| colleague | William von Eggers Doering | 无向 | 博士后合作者，1944 年奎宁全合成 |
| colleague | Geoffrey Wilkinson | 无向 | 1950 年代初共同提出二茂铁夹心结构 |
| colleague | Albert Eschenmoser | 无向 | 苏黎世合作者，B12 全合成（1973 发表） |
| colleague | Roald Hoffmann | 无向 | Woodward–Hoffmann 规则；1973 年 Cope Award 共享 |
| spouse | Irja Pullman | 无向 | 1938 年第一段婚姻，两女 |
| spouse | Eudoxia Muller | 无向 | 1946–1972，Polaroid 相识，一子一女 |

> **禁入库名单**（page.md 提及但按红线/惯例不入库）：best-known students 叙述名单 Robert M. Williams、Harry Wasserman、Yoshito Kishi、Steven A. Benner、James D. Wuest、Kevin M. Smith、Thomas R. Hoye、David Dolphin（正文叙述非 infobox 师承口径，防噪声）；Diels 与 Alder（少年时读其论文，思想渊源无个人交往）；Robert Robinson（青霉素结构之争对手方）；Dorothy Hodgkin（β-内酰胺的晶体学证明者，与本批交叉但 page.md 无直接二人关系）；子女四人（明载但按批次惯例不入库）。metadata-only 无新增。

## 8. 奖项清单

- Nobel Prize in Chemistry（1965，独享；"for his outstanding achievements in the art of organic synthesis"）
- John Scott Medal（1945，Franklin Institute 与费城）
- Centenary Prize（1951）
- Leo Hendrik Baekeland Award（1955）
- Foreign Member of the Royal Society，ForMemRS（1956）；William H. Nichols Medal（1956）
- Davy Medal（1959，皇家学会）
- Roger Adams Award / Roger Adams Medal（1961）
- American Academy of Arts and Sciences（1948）；National Academy of Sciences（1953）；American Philosophical Society（1962）
- National Medal of Science（1964，"for an imaginative new approach to the synthesis of complex organic molecules..."）
- Willard Gibbs Award（1967）
- Pius XI Gold Medal（1969，宗座科学院）
- Order of the Rising Sun, Second Class（1970，日本天皇）；Hanbury Memorial Medal（1970）；Pierre Bruylants Medal（1970）
- Lavoisier Medal（1968，法国化学会）；AMA Scientific Achievement Award（1971）
- Arthur C. Cope Award（1973，与 Roald Hoffmann 共享）
- Copley Medal（1978，皇家学会）
- 荣誉博士 20 余个：Wesleyan（1945）、Harvard（1957）、Cambridge（1964）、Brandeis（1965）、Technion（1966）、Western Ontario（1968）、Louvain（1970）等

## 9. 机构清单

- 教育：Quincy High School；MIT（BS 1936、PhD 1937）
- 任职：University of Illinois（短期博士后）；Harvard University（1937 Junior Fellow 起终生；1960 年代 Donner Professor of Science）
- 其他：Woodward Research Institute（Basel，1963 任所长）；MIT Trustee（1966–1971）；Weizmann Institute of Science Trustee；War Production Board 青霉素项目顾问（二战）；Polaroid、Pfizer、Merck 顾问

## 10. 终审清单

- [x] 生卒 1917-04-10 / 1979-07-08，享年 62，出生地波士顿、去世地剑桥（睡梦中心脏病，时在攻关红霉素）
- [x] 1965 独享；官方获奖理由英文原文整句引用无误；111 次提名（1946–1965）
- [x] β-内酰胺口径：Merck/Abraham 先提出 → Woodward 后支持 → Hodgkin 1945 证明——三人角色不混
- [x] 奎宁 formal total synthesis + "不实用"注记；B12 约 100 步、1973 发表、截至 2019 无第二例
- [x] 1973 诺奖（Wilkinson/Fischer）与 1981 诺奖（Hoffmann/Fukui）口径均注明"不追授逝者"
- [x] 名义博士导师 Norris/Morton note 如实；infobox 六博士生入库、叙述名单禁入
- [x] MIT 开除→复学→1936 BS→1937 PhD 时间线准确
- [x] 引语全部可在本地 Wikipedia 原文找到（诺奖理由句、学生悼词句、"Woodward" 时间单位句、致信诺奖委员会句）
- [x] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 路线图气泡背景 + 品牌 OpenMathAI
- [x] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Robert_Burns_Woodward/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：按 `images.txt` 下载并核验（page.md 内嵌 Robert_Burns_Woodward_in_1965.jpg 为 1965 年照片，可作肖像；404 则装饰圆占位）
- [ ] **国籍**：封面顶部明示美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（诺奖理由句、学生悼词、"Woodward" 单位句、二茂铁诺奖信件句）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与高斯模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 骨架）对齐；与本批 Dorothy_Hodgkin 篇青霉素交叉口径互查

---

> **名单状态**：由主控统一更新 `chemist/generate_20th_century_list.py`，本文件不改总表。
