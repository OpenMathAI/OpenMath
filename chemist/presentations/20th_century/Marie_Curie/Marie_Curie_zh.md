# Marie Curie（玛丽·居里）立传提示词

> qid=Q7186 · 1867-11-07 – 1934-07-04 · 波兰裔法国物理学家、化学家 · 20 世纪 · 诺贝尔化学奖（1911，独享；另获 1903 诺贝尔物理学奖，三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Marie_Curie/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 表格语义化 tabularx + 公式展示框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像取自本地 images/ 目录 Wikipedia 1903 年诺奖照 `Marie_Curie_1903.jpg`，下载后使用；404 则用装饰圆占位并注明）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{atom}\enspace 放射性之母\enspace·\enspace 波兰裔 · 法国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（Maria Salomea Skłodowska）、国籍（Russian Empire 至 1895 / France 自 1895）、出生地（华沙）/去世地（Passy, Haute-Savoie）、教育（Flying University / University of Paris）、博士导师（Gabriel Lippmann）、核心领域（放射性 / 放射化学）、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「放射性衰变 / 粒子径迹」母题——离散圆点与辐射路径暗示原子内部的能量释放。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Maria Salomea Skłodowska Curie（中文惯称：玛丽·居里 / 居里夫人；昵称 Mania）
- **生卒**：1867-11-07 生于华沙（Russian Empire 治下的 Congress Poland，Freta 街 16 号）→ 1934-07-04 逝于法国 Passy, Haute-Savoie 的 Sancellemoz 疗养院，享年 66，死因为 aplastic anaemia（再生障碍性贫血）
- **国籍**：Russian Empire（至 1895）→ France（自 1895）；终身保持波兰认同，教女儿波兰语、命名钋以志故国
- **身份**：物理学家、化学家（第一位诺奖女性得主、第一位两度诺奖得主、唯一在两个不同科学领域获奖者）
- **家庭**：五子女中最幼；父 Władysław Skłodowski 教数学物理、任华沙两所男子中学 director，因亲波立场被俄方解职；母 Bronisława（娘家姓 Boguska）办华沙著名女子寄宿学校，1878 年 5 月死于肺结核（Maria 时年 10 岁）；姐 Zofia 更早死于斑疹伤寒——两场死亡使她放弃天主教成为不可知论者；兄 Józef、姐 Bronisława（医生，巴黎求学之约）与 Helena。1895-07-26 在 Sceaux 嫁 Pierre Curie（无宗教仪式）；长女 Irène（1897）、次女 Ève（1904）；1906-04-19 Pierre 死于巴黎街头车祸
- **教育轨迹**：J. Sikorska 寄宿学校 → 女子中学（1883-06-12 金奖毕业）→ 因性别无法入正规高校，参加地下 Flying University → 任家庭教师（含 Szczuki 的 Żorawski 家两年）→ 1890-1891 在表兄 Józef Boguski 主持的工农业博物馆实验室受实验训练 → 1891 底赴巴黎入 University of Paris → 1893 物理学位、1894 第二学位（数学抑或化学，来源有分歧，Tadeusz Estreicher 考证为化学）
- **导师**：Gabriel Lippmann（博士导师；1893 起在其工业实验室工作）
- **博士**：1903，《Recherches sur les substances radioactives》（University of Paris）
- **研究领域**：放射性（术语 radioactivity 由她创造）、放射化学、物理学、化学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **教师之家与地下大学（1867–1891）**：父辈因波兰起义失产、父亲被俄方解职——逆境中的家教与 Flying University 是她的科学起点。
2. **巴黎阁楼（1891–1894）**：独居拉丁区阁楼，冬天穿全部衣服御寒、专注到忘记吃饭；1893 物理学位 + 1894 第二学位。
3. **磁钢课题与相识（1894）**：受全国工业促进学会委托研究各类钢的磁性；经波兰物理学家 Józef Wierusz-Kowalski 介绍认识 Pierre Curie。
4. **1895 成婚**：Pierre 愿为她迁居波兰；她坚持返巴黎读博；深蓝衣裙兼作多年实验服；共同爱好是长途自行车旅行。
5. **铀射线课题（1895–1896）**：受 Röntgen X 射线与 Becquerel 铀盐射线启发，选定铀射线作博士课题——用 Pierre 与其兄发明的静电计测电离。
6. **关键假设（1898 前）**：铀化合物活性只与铀含量有关 → 放射性来自原子本身——原子不可分观念被动摇的重要一步。
7. **钋与镭（1898）**：系统测量沥青铀矿活性为铀的 4 倍，推断含更强放射性新元素；1898-07-14 公布钋（纪念波兰），1898-12-26 公布镭；radioactivity 一词亦由居里夫妇创造；钋公布论文由 Lippmann 代呈科学院（1898-04-12）；钍的放射性发现上她被 Gerhard Carl Schmidt 抢先报道。
8. **分离镭（1898–1902/1910）**：分步结晶法，从 1 吨沥青铀矿得 0.1 g 氯化镭（1902）；1910 分离出纯镭金属；钋（半衰期 138 天）始终未能分离；1898-1902 两人共发表 32 篇论文（含镭毁伤肿瘤细胞快于健康细胞一篇）。
9. **1903 诺贝尔物理学奖**：与 Pierre、Becquerel 三人共享，"in recognition of the extraordinary services they have rendered by their joint researches on the radiation phenomena discovered by Professor Henri Becquerel"；委员会原只打算授 Pierre 与 Becquerel，经 Mittag-Leffler 提醒、Pierre 抗议后补入 Marie——第一位女性诺奖得主；1905 才赴斯德哥尔摩演讲；未申请专利。
10. **1906 接任索邦教席**：Pierre 车祸去世后，1906-05-13 索邦决定保留为其设的讲席并授予 Marie——大学第一位女教授。
11. **1911 诺贝尔化学奖（独享）**："in recognition of her services to the advancement of chemistry by the discovery of the elements radium and polonium, by the isolation of radium and the study of the nature and compounds of this remarkable element"；同年法国科学院落选（Édouard Branly 当选）；Langevin 丑闻下 Arrhenius 曾试图劝阻其出席典礼，她回答 "the prize has been given to her for her discovery of polonium and radium"、"there is no relation between her scientific work and the facts of her private life"；她是与 Pauling 并列的仅有的两位两领域诺奖得主之一（且是唯一横跨两门科学者）。
12. **一战 petites Curies（1914–1918）**：速学放射学、解剖学与汽车机械，组建 20 辆移动 X 光车 + 200 个野战放射单元，任红十字会放射服务主任，约百万伤员受检；镭气空心针消毒；捐出诺奖金奖（央行拒收）改购战争公债；战后著《Radiology in War》（1919）——法国政府未给过任何正式表彰。
13. **镭研究所与身后**：1920 创巴黎 Curie Institute、1932 创华沙镭研究所（姐 Bronisława 任所长）；1921/1929 两度访美（Harding 总统赠 1 g 镭）；1922 起任国联文化合作委员会委员（与 Einstein、Lorentz、Bergson 同僚）；1934 逝世，1995 迁葬先贤祠——第二位入葬先贤祠的女性、第一位凭自身成就入葬的女性；居里家族共五座诺奖；合成元素锔（curium）以她命名。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深藏青 deepnavy） | `#1E3A5F` | 实验记录般的严谨与放射科学的深邃（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（钋与镭 badgeElem） | `#2E5A9E` | 蓝 1898 双元素发现 |
| 分类色 2（分离提纯 badgeIso） | `#1B7A43` | 绿分步结晶 / 纯镭金属 |
| 分类色 3（放射性 badgeRad） | `#D97B29` | 琥珀 radioactivity 概念 / 电离测量 |
| 分类色 4（医学应用 badgeMed） | `#C0395B` | 玫瑰 petites Curies / 肿瘤治疗 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「放射性衰变 / 粒子径迹」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**New Lands** — Alex-Productions（清单指定 `music_audio/alex-productions/74-oK8HN0FsZmc-New-Lands.wav`）
- **风格**：开阔 / 探索 / 新天地感的史诗叙事
- **匹配理由**：
  - "New Lands" 匹配其贡献本质——发现两种新元素、开辟放射性化学这一全新疆域
  - "开阔" 匹配其人生轨迹——从华沙地下大学到巴黎索邦，再到镭研究所，一路向未知进发
  - "史诗" 匹配传记叙事——第一位诺奖女性、第一位两度得主、唯一两科学领域得主的历史重量
- **时长对齐**：以曲目实际时长 > 15 页 × 7 秒为宜，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 放射性之母 / Marie Curie 1867–1934 + 四色 badge + 右上头像 + 国籍行（波兰裔 · 法国）
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  居里夫人的一生 — 高斯式时间线（10 节点：1867→1891→1895→1898→1903→1906→1910→1911→1914→1934）
04  华沙：教师之家与飞行大学 (1867–1891) — 表格「时间|事件|结果」
05  巴黎：阁楼里的学生 (1891–1895) — 表格「时间|事件|结果」
06  钋与镭 (1898) — 表格「问题|方法|结果」+ 公式框：radioactivity 一词的创造与钋/镭命名
07  分离镭 (1898–1910) — 表格「挑战|方法|结果」+ 公式框：1 吨沥青铀矿 → 0.1 g RaCl₂
08  1903 诺贝尔物理学奖 — 表格「得主|理由|史实」+ 公式框：三人共享官方理由原文
09  1906 索邦教席 · 1911 诺贝尔化学奖 — 表格「事件|细节|意义」+ 公式框：1911 独享官方理由原文
10  一战与 petites Curies (1914–1918) — 表格「需求|行动|结果」
11  门生与传承 — 表格「人物|方向|结果」（infobox 博士生 8 人 + 镭研究所四诺奖）
12  荣誉与谦逊 — 高斯式「类别|代表|意义」表格（含 itemize 荣誉清单）+ 拒专利、拒荣誉勋章
13  遗产：先贤祠与居里家族 — 四分类遗产盒 + 公式框：五座诺奖家族 + curium
14  结尾 — 「人生中没有什么可怕的东西，只有需要理解的东西。」※此句仅作意境收束——页面无载，禁作引语标注
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1903 诺奖份额 | 页面只载「Pierre、Marie、Becquerel 三人共享」；**未载份额比例**——禁写"Becquerel 一半、夫妇一半" |
| 1911 诺奖口径 | **独享**；官方理由 "in recognition of her services to the advancement of chemistry by the discovery of the elements radium and polonium, by the isolation of radium and the study of the nature and compounds of this remarkable element"——勿与 1903 物理奖理由混淆 |
| 两领域得主 | "remains alone with Linus Pauling as Nobel laureates in two fields each"——她与 Pauling 是仅有的两位两领域得主；她是**唯一在两门不同科学领域**获奖者（Pauling 是化学 + 和平）；勿写成"唯一两领域" |
| "第一" 断言 | 页面明载可写：第一位女性诺奖得主、第一位两度诺奖得主、索邦第一位女教授、第一位凭自身成就入葬先贤祠的女性；其余"第一次/唯一"禁写 |
| 国籍口径 | Russian Empire（至 1895）→ France（自 1895）；frontmatter 的 "Second Polish Republic" 是 Wikidata 现代政区回溯口径，立传正文用「波兰裔 · 法国籍」 |
| 第二学位 | 1894 第二学位数学/化学两说并存——页脚注 Estreicher 考证为化学；立传取化学并加注 |
| 钍的发现 | 钍的放射性她独立发现但**被 Gerhard Carl Schmidt 抢先报道**——勿写"她第一个发现钍的放射性" |
| 钋命名 | 纪念故国波兰（时被俄普奥瓜分）；脚注提示"可能是第一个因政治问题而命名的元素"——表述需谨慎带注 |
| Langevin 事件 | 1911 媒体风波 page 明载，**中性记载**、一笔带过；Arrhenius 劝阻出席与其两句回击可写（引语白名单内） |
| 死因口径 | aplastic anaemia（再生障碍性贫血），归因于长期辐射暴露；但 1995 挖掘后 OPRI 结论"生前未达致死镭剂量"、推测更多源于一战战地 X 射线——两条并存，勿下单一结论 |
| 引语白名单 | 仅可用页面原文：1911 回应两句、"The fact is very remarkable..."、"a passionate desire to verify this hypothesis as rapidly as possible"、战时捐金购国债段落、"probably the only person who could not be corrupted by fame"（Einstein，reportedly 须带 reportedly） |
| 结尾"人生中没有什么可怕…" | **页面无载**，禁作带引号引语使用，只作无出处意境句或删除 |
| 博士生口径 | 正文 infobox 载 8 人：Debierne、Failla、Ladislas Goldstein、Émile Henriot、Irène、Óscar Moreno、Perey、Francis Perrin；metadata 另有 Branca Edmée Marques、郑大章、施士元、Ștefania Mărăcineanu——**metadata-only 不入库**；Goldstein/Moreno 库内既有数据未收，维持现状 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q7186 | ✅ |
| name_zh | 玛丽·居里 | ✅ |
| name_en | Marie Curie | ✅（清单 db_id=1064，复用库内记录） |
| birth_date | 1867-11-07 | ✅ |
| death_date | 1934-07-04 | ✅ |
| nationality | Poland / France | ✅ |
| primary_occupation | physicist | ✅ |
| field_of_work | radioactivity（person_field 细分：radioactivity / radiochemistry / physics / chemistry，带 rank） | ✅ |
| has_social_data | 1（既有入库，与 §7 一致） | ✅ |

## 7. 社会关系入库清单

> Marie Curie 的社会关系此前已入库（has_social_data=1，person_relation 与既有 yaml `MySQL/data/Marie_Curie.yaml` 一致）；本节作为 Beamer 立传的事实对照表，不再重复入库。

**师长 / 家人 / 合作者**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Gabriel Lippmann | 师→生（博士导师） | 1903 博士；1893 起亦为其实验室雇主 |
| spouse | Pierre Curie | 无向 | 1895-07-26 成婚；1906-04-19 Pierre 车祸去世 |
| co-honored | Pierre Curie | 无向 | 1903 诺贝尔物理学奖三人共享 |
| co-honored | Henri Becquerel | 无向 | 1903 诺贝尔物理学奖三人共享 |
| colleague | Gustave Bémont | 无向 | 1898 镭共同发现署名 |
| colleague | Józef Boguski | 无向 | 表兄，工农业博物馆实验室主持，其早年实验训练之地 |
| colleague | Gösta Mittag-Leffler | 无向 | 促成 Marie 补入 1903 诺奖提名 |
| colleague | Svante Arrhenius | 无向 | 1911 曾试图劝阻其出席诺奖典礼 |
| colleague | Paul Langevin | 无向 | Pierre 的学生、同行；1911 风波涉及对象（中性记载） |
| colleague | Hertha Ayrton | 无向 | 挚友兼同行物理学家，1911 风波中避居其英格兰居所 |
| colleague | Émile Roux | 无向 | 巴斯德研究所所长，1909 倡设其镭研究所 |
| colleague | Albert Einstein | 无向 | 1922 起国联文化合作委员会同僚、索尔维会议同行 |
| colleague | Hendrik Antoon Lorentz | 无向 | 国联文化合作委员会同僚、索尔维会议同行 |
| colleague | Henri Bergson | 无向 | 国联文化合作委员会同僚 |

**家人 / 门生（page.md 正文 infobox）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| parent-child | Władysław Skłodowski | 家长→子女 | 其父，数学物理教师 |
| parent-child | Irène Joliot-Curie | 家长→子女 | 长女兼博士生，1935 化学诺奖 |
| parent-child | Ève Curie | 家长→子女 | 次女，著《Madame Curie》 |
| sibling | Bronisława Dłuska | 无向 | 姐姐，医生，巴黎求学之约 |
| advisor-student | André-Louis Debierne | Marie→学生 | 博士生（infobox） |
| advisor-student | Gioacchino Failla | Marie→学生 | 博士生（infobox） |
| advisor-student | Émile Henriot | Marie→学生 | 博士生（infobox） |
| advisor-student | Irène Joliot-Curie | Marie→学生 | 长女兼博士生（infobox） |
| advisor-student | Marguerite Perey | Marie→学生 | 博士生（infobox）；1962 首位入选法国科学院女性 |
| advisor-student | Francis Perrin | Marie→学生 | 博士生（infobox） |

> 禁入库名单（metadata.json-only）：Branca Edmée Marques、郑大章（Zheng Dazhang）、施士元（Shi Shiyuan）、Ștefania Mărăcineanu；infobox 所载 Ladislas Goldstein、Óscar Moreno 此前入库未收，**维持库内现状不补**（在 Review 时知会主控）。Kazimierz Żorawski（早年在 Żorawski 家的情感纠葛）非学术关系，不入库。

## 8. 奖项清单

- Nobel Prize in Physics（1903，与 Pierre Curie、Henri Becquerel 共享）
- Davy Medal（1903，与 Pierre）
- Matteucci Medal（1904，与 Pierre）
- Actonian Prize（1907）
- Elliott Cresson Medal（1909）
- Legion of Honour（1909，拒绝）
- Nobel Prize in Chemistry（1911，独享）
- Civil Order of Alfonso XII（1919）
- Willard Gibbs Award（1921）；John Scott Medal（1921）；Benjamin Franklin Medal（1921）
- French Academy of Medicine fellow（1922）
- Cameron Prize for Therapeutics of the University of Edinburgh（1931）
- Order of the White Eagle（2018，追授）
- 荣誉博士（Jagiellonian University of Krakow 等）；prix Gegner、Albert Medal（1910）等（见 frontmatter award_received 全表）
- 1995 迁葬巴黎先贤祠（第二位入葬女性、第一位凭自身成就者）

## 9. 机构清单

- 教育：J. Sikorska 寄宿学校、华沙女子中学（1883 金奖）、Flying University（地下大学）、工农业博物馆实验室（1890–1891，Boguski 主持）、University of Paris（1891 入学；1893 物理、1894 第二学位、1903 博士）
- 任职：Lippmann 工业实验室（1893）；ESPCI 旁棚屋实验室（与 Pierre）；École normale supérieure de jeunes filles 首位女教师（1900）；University of Paris 教授（1906 接任 Pierre 讲席）；镭研究所 Curie 实验室主任（1914）
- 创建机构：Curie Institute Paris（1920）、华沙镭研究所（1932，姐 Bronisława 任所长）；一战红十字会放射服务主任；国联 International Committee on Intellectual Cooperation 委员（1922–1934）；International Atomic Weights Committee 委员（1930–1934）

## 10. 终审清单

- [ ] 生卒 1867-11-07 / 1934-07-04，享年 66，出生地华沙、去世地 Passy（Sancellemoz 疗养院）
- [ ] 1903 三人共享（份额比例页面无载禁写）/ 1911 独享表述准确；两份官方理由引文准确
- [ ] "两领域得主仅她与 Pauling、唯一两门科学"表述准确；各"第一"均有页面明载
- [ ] 钍发现被 Schmidt 抢先报道；钋始终未分离；1902 0.1 g RaCl₂、1910 纯镭金属年份准确
- [ ] Langevin 事件中性记载；Arrhenius 劝阻与其回应在引语白名单内
- [ ] 死因双口径（再生障碍性贫血 / OPRI 1995 复核）并存
- [ ] 引语全部可在本地 Wikipedia 原文找到；无页面无载引语
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Marie_Curie/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/` 肖像就位（Wikipedia 1903 诺奖照）；404 用装饰圆占位并注明
- [ ] **国籍**：封面顶部明示「波兰裔 · 法国」
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到（见 §5 白名单）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger）对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾；本文件由 chem-batch-01 agent 维护。
> **最重要的事：每写一页就 make，看到溢出就修。**
