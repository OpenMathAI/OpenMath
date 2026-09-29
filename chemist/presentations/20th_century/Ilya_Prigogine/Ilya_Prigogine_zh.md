# Ilya Prigogine（伊利亚·普里高津）立传提示词

> qid=Q183509 · 1917-01-25 – 2003-05-28 · 比利时物理化学家（俄裔） · 20 世纪 · 诺贝尔化学奖（1977，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Ilya_Prigogine/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 高斯式时间线 + 表格语义化 tabularx + 公式展示框 + 气泡背景。

---

## 0. 正文形式说明（参考 Sanger 桑格模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像下载后放 `images/`；Commons 404 则按 Wikipedia REST API 回退，再失败用装饰圆占位并在 Review 记录）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{project-diagram}\enspace 耗散结构之父\enspace·\enspace 比利时`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒（含俄历注记）、国籍变迁、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「耗散结构 / 自组织」母题——由混沌圆点自发聚成的有序斑图。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Viscount Ilya Romanovich Prigogine（俄文：Илья Романович Пригожин；中文惯称：伊利亚·罗曼诺维奇·普里高津；1989 年获比利时子爵衔）
- **生卒**：1917-01-25（俄历 1 月 12 日）生于莫斯科，十月革命前数月 → 2003-05-28 逝于布鲁塞尔，享年 86
- **国籍变迁**：生于俄罗斯帝国 → 1921 举家离俄（立陶宛短暂逗留→柏林）→ 1929 迁布鲁塞尔 → 1949 入比利时籍
- **身份**：比利时物理化学家（俄裔犹太家庭）；以耗散结构、复杂系统与不可逆性闻名
- **家庭**：父 Ruvim Abramovich Prigogine（1884–1974）为化学家（帝国莫斯科技术学校出身）、油漆厂厂主；母 Yulia Leivikovna Vikhman（1892–?）为钢琴家（莫斯科音乐学院）；弟 Alexandre（1913–1991）后成鸟类学家
- **教育轨迹**：
  - 少年时代兴趣在音乐、历史与考古；1935 毕业于 Athenée d'Ixelles（主修希腊文拉丁文）
  - 父母劝其学法律——布鲁塞尔自由大学法律系注册后，经由心理学→化学→物理的兴趣链最终弃法
  - 同时注册化学与物理两专业且"uncommon success"：1939 双科硕士同等学历；1941 化学博士（师从 Théophile de Donder）
- **导师**：Théophile de Donder（博士导师）
- **婚姻**：首娶比利时诗人 Hélène Jofé（1945 婚，后离异；1945 得子 Yves）；1961 娶波兰裔化学家 Maria Prokopowicz（1970 得子 Pascal）
- **研究领域**：非平衡态热力学、耗散结构、统计力学、复杂系统、时间的不可逆性

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **革命前夜的莫斯科（1917）**：十月革命前数月生于莫斯科犹太家庭；父辈的油漆厂 1921 年被苏维埃政权国有化，内战动荡中举家西迁（立陶宛→柏林）。
2. **从柏林到布鲁塞尔（1921–1929）**：德国经济凋敝与纳粹渐起，再度西迁布鲁塞尔——他的童年是一部欧洲动荡史。
3. **从希腊拉丁文到热力学（1935–1941）**：古典文科生先入法律系，经心理学兴趣链转向化学与物理；双专业同修；1941 师从 de Donder 获化学博士。
4. **占领下的地下课堂（1940–1944）**：德占比利时期间自 1940 年起为学生开设秘密讲座；1941 大学为抗议占领当局强纳亲纳粹的弗拉芒 New Order 教授而正式关闭，他坚持地下授课至 1944 解放；同期发表 21 篇论文。
5. **被捕与营救（1943）**：与未婚妻 Hélène Jofé 被德方逮捕，经多方干预（含王后 Elisabeth）数周后获释。
6. **最年轻正教授（1951）**：34 岁任母校科学系正教授——布鲁塞尔科学系史上最年轻。
7. **索尔维与国际舞台（1959–）**：1959 出任布鲁塞尔国际索尔维研究所所长；同年起在德克萨斯大学奥斯汀分校执教，后任 Regental Professor 与 Ashbel Smith 教授；1961–1966 挂靠芝加哥大学 Enrico Fermi 研究所、任西北大学访问教授。
8. **奥斯汀双中心（1967）**：在奥斯汀 co-found 热力学与统计力学中心（今 Center for Complex Quantum Systems）；同年回到比利时任统计力学与热力学中心主任。
9. **耗散结构（诺奖核心）**：发现向化学系统输入并耗散能量可因内部自重组而涌现新结构——"耗散结构"；1955 年专著中已把它与 Rayleigh-Bénard 失稳及 Turing 机制相连。
10. **从十字路口到交通流**：与 Robert Herman 合作发展城市路网的双流体交通模型——热力学思维越出化学的例证。
11. **1977 诺贝尔化学奖（独享）**："for his contributions to non-equilibrium thermodynamics, particularly the theory of dissipative structures"；此前 1955 Francqui Prize（精确科学）、1975 Cothenius Medal、1976 Rumford Medal。
12. **确定性的终结**：与 Isabelle Stengers 合著 *La Nouvelle Alliance*（Order out of Chaos，1977/1984）与 *The End of Certainty*（1996/1997）——"The more we know about our universe, the more difficult it becomes to believe in determinism."（page.md 明载可引）；主张牛顿物理已被三次"扩展"（时空/波函数/不稳定性）。
13. **晚年与身后**：晚期专注非线性系统的非决定论，与同事提出量子力学的 Liouville 空间扩展（指向时间之矢与测量问题）；53 个荣誉学位；1989 年受封子爵；2003 年为签署《人文主义宣言》的 22 位诺奖得主之一；2001 年起以其名设 Ilya Prigogine Prize for Thermodynamics（两年一届，JETC 颁发），其生前亲任监理至 2003。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（紫罗兰深紫 deeppurple） | `#283593` | 远离平衡态的深邃与秩序涌现（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（耗散结构 badgeDiss） | `#2E6E8E` | 青蓝自组织 / 有序从混沌涌现 |
| 分类色 2（非平衡热力学 badgeNoneq） | `#1B7A43` | 绿不可逆过程 / 熵产生 |
| 分类色 3（复杂系统 badgeCx） | `#D97B29` | 琥珀交通流双流体模型 / Liouville 扩展 |
| 分类色 4（时间之矢 badgeTime） | `#C0395B` | 玫瑰确定性的终结 / 时间的创造性 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「耗散结构」自组织斑图。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**New Lands** — Alex-Productions（`music_audio/alex-productions/74-oK8HN0FsZmc-New-Lands.wav`；不要复制 wav 文件，Makefile 引用即可）
- **风格**：开阔 / 求索 / 新天地感
- **匹配理由**：
  - "New Lands" 直扣其学术纲领——把热力学从平衡态带进非平衡态的"新大陆"
  - "求索" 匹配其三度流亡、两次转系、从古典文科走向物理化学的人生轨迹
  - "开阔" 匹配《确定性的终结》对决定论物理版图的重画
- **时长**：以实际曲目时长为准 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 耗散结构之父 / Ilya Prigogine 1917–2003 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒含俄历/国籍变迁/出生地/去世地/教育/博士/师承/领域/荣誉）
03  普里高津的一生 — 高斯式时间线（10 节点：1917→1921→1929→1941→1951→1959→1967→1977→1989→2003）
04  革命前夜的莫斯科与三度流亡 (1917–1929) — 表格「时间|事件|结果」
05  从法律到化学（布鲁塞尔自由大学）(1935–1941) — 表格「时间|事件|结果」+ de Donder
06  占领下的地下课堂 (1940–1944) — 表格「背景|行动|结果」（秘密讲座 / 1943 被捕营救 / 21 篇论文）
07  耗散结构 (1955–1977) — 表格「问题|方法|结果」+ 公式框：能量输入+耗散 → 内部自重组涌现新结构
08  1977 诺贝尔化学奖 — 表格「人物|方向|结果」（独享 · "non-equilibrium thermodynamics, particularly the theory of dissipative structures"）
09  索尔维与奥斯汀双中心 (1959–) — 表格「机构|角色|结果」
10  越界：交通流与量子力学扩展 — 表格「领域|合作者|结果」（Robert Herman 双流体模型 / Liouville 空间扩展）
11  确定性的终结 — 表格「著作|合作者|论点」+ 公式框：牛顿物理三次扩展；引语 "The more we know..."
12  荣誉与子爵 — 高斯式「类别|代表|意义」表格（Francqui 1955 / Rumford 1976 / 诺奖 1977 / 53 荣誉学位 / 1989 子爵）
13  遗产：时间重新进入物理学 — 四分类遗产盒 + 公式框：Ilya Prigogine Prize for Thermodynamics（2001–）
14  结尾 — 「时间不是幻觉，而是创造。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1977 获奖理由 | 官方原文 "for his contributions to non-equilibrium thermodynamics, particularly the theory of dissipative structures"——勿写成"证明耗散结构存在"或泛化为复杂系统 |
| 独享 | 1977 **独享**——勿与他人共享 |
| 生年双值 | frontmatter 双值 1917-01-12 / 1917-01-25——正文 infobox 作 25 January 1917（俄历 1 月 12 日），**取 1917-01-25** 并保留俄历注记 |
| 国籍 | 生于俄罗斯帝国、**1949 年入比利时籍**；Citizenship 行只写 Belgian (1949–2003)——勿写"生来比利时人"；封面写"比利时" |
| 耗散结构表述 | "importation and dissipation of energy into chemical systems could result in the emergence of new structures due to internal self reorganization"——能量输入与耗散→内部自重组→新结构，勿写成"负熵"或脑补术语 |
| Brusselator | Known for 明载 Brusselator——但 page.md 正文未展开；如展示只列名不编故事 |
| 战时被捕 | 1943 与 **未来妻子** Hélène Jofé 被捕，经含王后 Elisabeth 在内的多方干预获释——勿写"被送集中营" |
| 博士导师 | Théophile **de Donder**（1941 化学博士）——勿写成 de Donder 的"合作者" |
| 最年轻教授 | 34 岁、**布鲁塞尔科学系**史上最年轻正教授（1951）——勿写"比利时最年轻" |
| 合著者 | 正文明载合著 **Isabelle Stengers**（Order out of Chaos / The End of Certainty）；Defay/Glansdorff/Nicolis/Kondepudi 仅书目出现——正文中不展开为个人叙事 |
| 兄弟 | Alexandre Prigogine 是**弟弟**（鸟类学家）——关系白名单无 sibling 类型，不入库；正文可一句提及 |
| 引语红线 | 可引：诺贝尔理由整句、The End of Certainty 的 "The more we know about our universe, the more difficult it becomes to believe in determinism."；其余（Wikiquote 相关内容、访谈）一律不得作"原话" |
| 人文主义宣言 | 2003 年 22 位诺奖得主签署《人文主义宣言》(Humanism and Its Aspirations)——一句客观带过 |
| 政治敏感 | 十月革命/苏联国有化按 page.md 原文口径一句带过（工厂国有化→举家西迁），不展开政治叙事 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q183509 | ✅ |
| name_zh | 伊利亚·普里高津 | ✅ |
| name_en | Ilya Prigogine | ✅ |
| birth_date | 1917-01-25（俄历 1917-01-12，取公历正文口径） | ✅ |
| death_date | 2003-05-28 | ✅ |
| nationality | Russian Empire（rank 0）→ Belgium（rank 1） | ✅ |
| primary_occupation | chemist（physical chemist） | ✅ |
| field_of_work | chemistry（person_field 细分见下表，带 rank） | ✅ |

**person_field rank 表**：

| field | rank | 语义 |
|---|---|---|
| non-equilibrium thermodynamics | 0 | 非平衡态热力学（诺奖方向） |
| dissipative structures | 1 | 耗散结构理论 |
| statistical mechanics | 2 | 非平衡统计力学 |
| complex systems | 3 | 复杂系统 / 自组织 |

## 7. 社会关系入库清单

**★ 红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**

**师长**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Théophile de Donder | 师→生（博士导师） | 1941 布鲁塞尔自由大学化学博士 |

**门生（infobox Doctoral students，Prigogine → 学生，6 人全数明载）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Radu Bălescu | Prigogine → 学生 | infobox 明载 |
| advisor-student | Adi Bulsara | Prigogine → 学生 | infobox 明载 |
| advisor-student | Paul Clavin | Prigogine → 学生 | infobox 明载 |
| advisor-student | Harry Friedmann | Prigogine → 学生 | infobox 明载 |
| advisor-student | Linda Reichl | Prigogine → 学生 | infobox 明载 |
| advisor-student | Isabelle Stengers | Prigogine → 学生 | infobox 明载；亦为《Order out of Chaos》《The End of Certainty》合著者 |

**同事 / 其他明载**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Robert Herman | 无向 | 合作发展城市路网双流体交通模型 |
| spouse | Hélène Jofé | 无向 | 1945 结婚（诗人），后离异；1945 得子 Yves |
| spouse | Maria Prokopowicz | 无向 | 1961 结婚（波兰裔化学家）；1970 得子 Pascal |

> **禁入库名单（书目-only 或白名单外类型）**：R. Defay / Paul Glansdorff / G. Nicolis / Dilip Kondepudi（仅书目合著者，Defay/Nicolis 连全名都无载，防分裂 stub 不入库）；Alexandre Prigogine（兄弟，白名单无 sibling 类型）；Robert M. May 类无关人物不涉及。

## 8. 奖项清单

- Francqui Prize for Exact Sciences（1955）
- Cothenius Medal（1975）
- Rumford Medal（1976）
- Nobel Prize in Chemistry（1977，独享；诺奖演讲 1977-12-08 "Time, Structure and Fluctuations"）
- Viscount（Belgian nobility，1989，由比利时国王授予）
- Commander of the Legion of Honour；Order of Friendship；Bogolyubov Prize；Honda Prize；Kampé de Fériet Award（frontmatter 明载，正文未给年份——展示慎写）
- 荣誉学位 53 个（含 Heriot-Watt 1985、UNAM 1998 及 frontmatter 所列诸校）
- 国际科学院（慕尼黑）主席（至去世）；CODE 世界远程教育认证机构共同创始人（1997）

## 9. 机构清单

- 教育：Athenée d'Ixelles（1935 毕业）；Université libre de Bruxelles（双科硕士同等学历 1939；PhD 1941）
- 任职：Université libre de Bruxelles（1951 正教授；1967 起任统计力学与热力学中心主任）；International Solvay Institute 所长（1959–）；University of Texas at Austin（1959 起执教，Regental Professor / Ashbel Smith Professor；1967 co-found 热力学与统计力学中心，今 Center for Complex Quantum Systems）；Enrico Fermi Institute, University of Chicago（1961–1966）；Northwestern University 访问教授
- 纪念：Ilya Prigogine Prize for Thermodynamics（2001 创设，JETC 两年一届）

## 10. 终审清单

- [ ] 生卒 1917-01-25（俄历 01-12 注记）/ 2003-05-28，享年 86，出生地 Moscow、去世地 Brussels
- [ ] 1977 **独享**；获奖理由"非平衡态热力学、特别是耗散结构理论"口径准确
- [ ] 国籍三段式（俄→柏林→布鲁塞尔；1949 入籍）；封面写"比利时"
- [ ] 地下课堂 / 1943 被捕营救 / 34 岁最年轻正教授 表述准确
- [ ] Stengers=学生+合著者一人一行；Defay/Glansdorff/Nicolis/Kondepudi 不入库
- [ ] 引语仅诺贝尔理由与 determinism 一句，其余不得出现引号"原话"
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Ilya_Prigogine/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：确认肖像就位（Commons/Wikipedia REST API；失败则装饰圆占位并记录）
- [ ] **国籍**：封面顶部明示"比利时"
- [ ] **引语核对**：仅两段明载引语，其余不得出现引号"原话"
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Frederick_Sanger_zh.tex）对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾，本提示词不改动该文件。
