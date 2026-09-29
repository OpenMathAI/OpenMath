# Melvin Calvin（梅尔文·卡尔文）立传提示词

> qid=Q49347 · 1911-04-08 – 1997-01-08 · 美国生物化学家 · 20 世纪 · 诺贝尔化学奖（1961，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Melvin_Calvin/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/` 取 c. 1960s 照，若 images.txt 缺失则装饰圆占位并注明）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{leaf}\enspace 光合作用碳之路的绘制者\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育（Michigan College of Mining and Technology/Minnesota）、博士（1935，George Glocker 门下）、博士后导师（Michael Polanyi）、核心领域（Calvin cycle）、荣誉（1961 诺奖）。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「碳原子在循环中的逐站流转」母题——圆点首尾相连暗示循环路径。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化（CO₂ 固定第一产物 PGA（3-碳磷酸甘油酸）、受体分子核酮糖二磷酸——均为 page.md 实载，循环图以语义框呈现）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Melvin Ellis Calvin（中文惯称：梅尔文·卡尔文；别称 "Mr. Photosynthesis"）
- **生卒**：1911-04-08 生于明尼苏达州 St. Paul → 1997-01-08 逝于加州 Berkeley，享年 85
- **国籍**：United States（美国）
- **身份**：生物化学家（biochemist；Calvin cycle 发现者）
- **家庭**：犹太移民之子——父 Elias Calvin、母 Rose Herwitz 来自俄罗斯帝国（今立陶宛与格鲁吉亚一带）；幼年随家迁底特律，父母经营杂货店。1942 年娶 Genevieve Jemtegaard（infobox 全名 Genevieve Elle Jemtegaard，正文作 Marie Genevieve Jemtegaard；1987 卒），育两女 Elin、Karole 与一子 Noel
- **教育轨迹**：
  - Central High School, Detroit（1928 毕业）
  - Michigan College of Mining and Technology（今 Michigan Technological University）——获该校第一个化学理学士
  - University of Minnesota，1935 年 PhD（卤素的电子亲和性，George Glocker 指导）
  - 博士后两年：University of Manchester，Michael Polanyi 实验室（有机分子结构与行为）
- **导师**：博士导师 George Glocker（明尼苏达）；博士后导师 Michael Polanyi（曼彻斯特）——frontmatter `doctoral_advisor` 只列 Polanyi 属噪声，以正文为准
- **博士**：1935，University of Minnesota
- **研究领域**：生物化学——光合作用固碳路径（Calvin–Benson–Bassham cycle）、化学演化、放射性碳示踪

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **杂货店里的好奇心（1911）**：俄罗斯帝国犹太移民之子，底特律杂货店的货架是他的第一座实验室。
2. **两个"第一"（1931/1935）**：Michigan College of Mining and Technology 第一个化学理学士；明尼苏达 PhD 研究卤素电子亲和性。
3. **曼彻斯特两年（1935–1937）**：Polanyi 实验室博士后——有机分子结构与行为，奠定其"物理化学家的生物学"底色。
4. **伯克利入职**：UC Radiation Laboratory 主任 Joel Hildebrand 访问曼彻斯特时邀其加入伯克利教职——化学系 25 年来第一个非伯克利毕业生。
5. **站在 Kamen/Ruben 肩上（1940）**：Calvin 在伯克利最初的研究建立在 Martin Kamen 与 Sam Ruben 1940 年发现长寿命放射性碳-14 的基础上。
6. **1945 年 recruits**：Lawrence（Radiation Lab 主任）与化学化工学院长 Wendell Latimer 于 1945 年招募 Calvin 推进放射性碳研究。
7. **Bio-Organic 组（1947）**：升化学教授并执掌 Lawrence Radiation Laboratory 生物有机化学组；组建 Andrew Benson、James A. Bassham 等团队，Benson 负责搭建光合作用实验室。
8. **碳之路（1950s）**：以碳-14 为示踪剂，与 Benson、Bassham 绘出碳在植物中从大气 CO₂ 吸收到转化为碳水化合物的完整路径——发现非光化学的 CO₂ 还原，颠覆"糖生成是光反应"的旧理论。
9. **第一产物与受体（1950s）**：纸层析（W.A. Stepka 开创的技术）确定 CO₂ 固定第一产物为 3-碳磷酸甘油酸（PGA）；Benson 认出两种未知糖为酮糖；Bassham 借高碘酸降解锁定七碳糖；限制 CO₂ 摄取使核酮糖二磷酸积累——确认其为 CO₂ 受体分子；Calvin 提出"新型羧化机制"，1958 年补全整个序列。
10. **芝加哥挑战与 AAAS 公断**：芝加哥大学的竞争实验室无法复现而对 Calvin 组文献发起强攻；AAAS 赞助的研讨会上 Calvin 与 Benson 说服了听众，攻击被驳回。
11. **1961 诺贝尔化学奖**：官方理由 "for his research on the carbon dioxide assimilation in plants"；1961-12-11 诺奖演讲 "The Path of Carbon in Photosynthesis"。
12. **Roundhouse（1963）**：加聘分子生物学教授；创建并主持"Roundhouse"化学生物动力学实验室（圆形建筑专为跨界协作设计），兼任 Berkeley Radiation Lab 副主任直至 1980 退休；晚年研究产油植物与生命化学演化（1969 年出书）。
13. **公共服务**：美国化学会、美国植物生理学会、AAAS 太平洋分会主席；NAS 科技公共政策委员会主席；总统科学顾问委员会成员（1963–1966）；能源研究咨询委员会；与 NASA 合作制定阿波罗任务地月相互生物污染防护方案；"Mr. Photosynthesis" 之名；2011 年美国科学家邮票（与 Asa Gray、Maria Goeppert-Mayer、Severo Ochoa 同版）。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（墨蓝 navyblue） | `#14324F` | 深植物暗部的光合之蓝（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（Calvin 循环 badgeCyc） | `#1B7A43` | 叶绿固碳循环 |
| 分类色 2（碳-14 示踪 badgeC14） | `#2E5A9E` | 蓝放射性示踪技术 |
| 分类色 3（Roundhouse badgeRound） | `#D97B29` | 琥珀跨界实验室 |
| 分类色 4（化学演化 badgeEvo） | `#8E44AD` | 紫生命起源 / 产油植物 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），圆点以淡线首尾相连，呼应「碳的循环之路」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Timeless** — Alex-Productions（文件路径见 manifest `music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav`；**不要复制 wav 文件**）
- **风格**：沉稳 / 纪录片 / 长期主义
- **匹配理由**：
  - "长期纲领" 匹配其五十年坚守伯克利的单一大问题——把光合作用碳之路一寸寸画完
  - "沉稳" 匹配示踪科学的气质——耐心、重复、不动声色的严谨
  - "纪录片" 匹配从杂货店到 Roundhouse 的完整传记弧线
- **时长**：以实际文件为准 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 光合作用碳之路的绘制者 / Melvin Calvin 1911–1997 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/博士后导师/出生地/去世地/领域/荣誉）
03  卡尔文的一生 — Sanger 式时间线（10 节点：1911→1928→1935→1937→1945→1947→1958→1961→1963→1997）
04  底特律杂货店之子（1911–1935）— 表格「时间|事件|结果」（Central High → 采矿学院第一个化学 BS → Minnesota PhD）
05  曼彻斯特与 Polanyi（1935–1937）— 表格「实验室|课题|收获」
06  伯克利与碳-14（1937–1947）— 表格「事件|人物|意义」（Hildebrand 邀聘、Kamen/Ruben 1940、Lawrence/Latimer 1945 招募）
07  碳之路：从 CO₂ 到糖（1950s）— 表格「问题|方法|结果」+ 公式框：第一产物 PGA / 受体核酮糖二磷酸
08  1958：循环补全 — 表格「证据|推理|结论」+ AAAS 公断事件
09  1961 诺贝尔化学奖 — 表格「领域|贡献|认可」+ 公式框：官方获奖理由原文
10  Roundhouse（1963–1980）— 表格「设计|理念|成果」+ 圆形实验室流程示意
11  公共服务 — Sanger 式「机构|职务|意义」表格（学会主席/PSAC/NASA/邮票）
12  Benson 争议 — 表格「主张|来源|口径」（2011 BBC 批评、Benson 自述被解雇与自传未提及其角色——客观呈现）
13  遗产：给地球绿色引擎画电路图 — 四分类遗产盒 + 公式框：Calvin–Benson–Bassham 循环
14  结尾 — 「他追着放射性碳原子跑了一圈，把阳光变成粮食的路画在了纸上。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1961 诺奖 | **独享**，官方理由 "for his research on the carbon dioxide assimilation in plants"；Benson/Bassham 未分享诺奖——循环命名却是 Calvin–Benson–Bassham Cycle，三方口径分列勿混 |
| 博士导师 | PhD 导师是 **George Glocker**（明尼苏达，卤素电子亲和性）；Polanyi 是**博士后**导师——frontmatter `doctoral_advisor` 只列 Polanyi 属噪声，以正文为准 |
| 妻子姓名 | infobox 作 Genevieve Elle Jemtegaard、正文作 Marie Genevieve Jemtegaard——yaml 取 Genevieve Jemtegaard 并注两说；勿凭空展开 |
| 循环归属 | 发现是 Calvin **与** Andrew Benson、James Bassham 共同完成——正文处处三名字并列，勿写成 Calvin 一人之功 |
| Benson 争议 | 2011 年 BBC（Timothy Walker）批评 + Benson 本人抱怨被解雇、自传未提其角色——为 page.md 实载；呈现须客观标注"Calvin 侧回应页面无载"；禁写"剽窃"定性词 |
| 芝加哥论战 | 竞争实验室"无法确认"并发起强攻，AAAS 研讨会 Calvin/Benson 胜出——对手实验室名页面无载，禁写具体校名人名（芝加哥大学本身可提） |
| Kamen/Ruben | 碳-14 是他们 1940 年的发现，Calvin 是应用者——勿写 Calvin 发现 C-14 |
| Ruben 之死 | Ruben 实验室意外身亡、Kamen 因安全问题陷入麻烦——背景一笔带过即可，细节禁渲染 |
| PGA 名称 | 3-碳磷酸甘油酸（PGA）为 CO₂ 固定第一产物——勿写成丙酮酸或甘油醛 |
| 受体分子 | 核酮糖二磷酸（ribulose bisphosphate）经限制 CO₂ 实验确认——勿写"Calvin 发明了它" |
| 邮票年份 | 2011 年 American Scientists 系列第三卷（前两卷 2005、2008）——同版四人为 Asa Gray、Goeppert-Mayer、Ochoa、Calvin |
| 荣誉学位 | "13 个其他荣誉学位"（含 1971 Whittier College LL.D.）——勿凑具体名单 |
| 引语 | page.md 正文无 Calvin 直接引语——全文禁用引号"原话"（仅诺奖理由英文原文一处） |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q49347 | ✅ |
| name_zh | 梅尔文·卡尔文 | ✅ |
| name_en | Melvin Calvin | ✅ |
| birth_date | 1911-04-08 | ✅ |
| death_date | 1997-01-08 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry（person_field 细分见下表，带 rank） | ✅ |
| has_biography | 0（立传 Beamer 完成后置 1） | ✅ |

**person_field 细分 rank 表**：

| name_en | rank | name_zh | 依据 |
|---|---|---|---|
| photosynthesis | 0 | 光合作用（Calvin 循环） | 1961 诺奖理由 |
| biochemistry | 1 | 生物化学 | infobox 描述 |
| carbon-14 tracing | 2 | 碳-14 示踪 | 方法论核心 |
| chemical evolution | 3 | 化学演化 | 晚年研究 + 1969 专著 |

## 7. 社会关系入库清单

**★ 红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | George Glocker | 师→生（博士导师） | 1935 Minnesota PhD（卤素电子亲和性） |
| advisor-student | Michael Polanyi | 师→生（博士后导师） | 曼彻斯特两年，有机分子结构与行为 |
| advisor-student | Cyril Ponnamperuma | Calvin → 学生 | infobox Doctoral students |
| advisor-student | Dean H. Kenyon | Calvin → 学生 | infobox Other notable students |
| colleague | Andrew Benson | 无向 | Calvin 循环共同发现者（负责搭建光合作用实验室）；后因署名与解雇问题公开批评 Calvin |
| colleague | James Bassham | 无向 | Calvin 循环共同发现者（高碘酸降解锁定七碳糖） |
| colleague | Joel Hildebrand | 无向 | UC Radiation Lab 主任，访曼彻斯特时邀 Calvin 加入伯克利教职 |
| colleague | Ernest Lawrence | 无向 | Radiation Lab 主任，与 Latimer 一起于 1945 年招募 Calvin |
| colleague | Wendell Latimer | 无向 | 化学化工学院长，与 Lawrence 一起于 1945 年招募 Calvin |
| influence | Martin Kamen | 无向 | Kamen/Ruben 1940 发现碳-14——Calvin 伯克利研究的思想与工具源头 |
| influence | Sam Ruben | 无向 | 同上（1940 碳-14 发现者之一） |
| controversy | Andrew Benson | 无向 | Benson 指控被 Calvin 解雇且自传未提及其贡献（2011 BBC 批评转述 + Benson 自述）；Calvin 侧回应页面无载 |
| spouse | Genevieve Jemtegaard | 无向 | 1942 结婚（infobox 全名 Genevieve Elle Jemtegaard，正文作 Marie Genevieve Jemtegaard）；1987 卒 |

> **禁入库名单（metadata-only 或非人际）**：Timothy Walker（BBC 制片人，仅转述批评）、W.A. Stepka（纸层析技术开创者，正文无人际互动）、George de Hevesy（无）、美国各学会与 NASA（机构非人）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1961，独享；"for his research on the carbon dioxide assimilation in plants"）
- Guggenheim Fellowship；Centenary Prize（1955）
- William H. Nichols Medal（1958）
- Davy Medal, Royal Society（1964）
- Priestley Medal, American Chemical Society（1978）
- AIC Gold Medal / American Institute of Chemists Gold Medal（1979）
- National Medal of Science（1989）
- A. I. Virtanen Award；Willard Gibbs Award；Remsen Award；Oesper Award；Glenn T. Seaborg Award for Nuclear Chemistry
- 美国国家科学院院士（1954）；Royal Netherlands Academy 外籍院士（1958）；American Academy of Arts and Sciences（1958）；Leopoldina（1959）；American Philosophical Society（1960）；Foreign Member of the Royal Society；美国地球物理联合会 Fellow
- 荣誉学位：Whittier College LL.D.（1971）等 13 个；University of Paris-XII 荣誉博士
- 2011 年美国邮政 American Scientists 邮票（第三卷）

## 9. 机构清单

- 教育：Central High School, Detroit（1928）；Michigan College of Mining and Technology（化学 BS，该校首个）；University of Minnesota（PhD 1935）；University of Manchester（博士后，Polanyi 实验室）
- 任职：University of California, Berkeley（1947 化学教授；1963 加聘分子生物学教授）；Lawrence Radiation Laboratory / Berkeley Radiation Laboratory（Bio-Organic 组组长；副所长）；Laboratory of Chemical Biodynamics "Roundhouse"（创建者兼所长）；Science Advisory Committee
- 公职：美国化学会主席、美国植物生理学会主席、AAAS 太平洋分会主席；NAS 科技公共政策委员会主席；总统科学顾问委员会（1963–1966）；能源研究咨询委员会；NASA 阿波罗生物污染防护顾问；IUPAC 放射性应用联合委员会等国际组织
- 纪念：Roundhouse 圆形实验室；2011 American Scientists 邮票

## 10. 终审清单

- [ ] 生卒 1911-04-08 / 1997-01-08，享年 85，出生地 St. Paul（明尼苏达）、去世地 Berkeley（加州）
- [ ] 1961 **独享**，官方理由原文完整；循环命名 Calvin–Benson–Bassham 三方并列
- [ ] 博士导师 Glocker / 博士后导师 Polanyi 区分清楚（frontmatter 噪声已裁定）
- [ ] PGA 第一产物、核酮糖二磷酸受体、1958 序列补全——科学叙事链条准确
- [ ] Benson 争议客观呈现、无定性词；对手实验室名禁写
- [ ] 全文无杜撰引语（page.md 无 Calvin 直接引语）
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Melvin_Calvin/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：核对 images/（c. 1960s 照）
- [ ] **国籍**：封面顶部明示美国
- [ ] **引语核对**：全文无引号"原话"（仅诺奖理由英文原文一处）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 等）对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾，本文件不改动该脚本。
