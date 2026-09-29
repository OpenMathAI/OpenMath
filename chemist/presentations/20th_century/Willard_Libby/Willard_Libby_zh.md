# Willard Libby（威拉德·利比）立传提示词

> qid=Q190486 · 1908-12-17 – 1980-09-08 · 美国物理化学家 · 20 世纪 · 诺贝尔化学奖（1960，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Willard_Libby/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像用 `images/Willard_Libby_in_Lab.jpg`（实验室照，c. 1960s），若 images.txt 缺失则装饰圆占位并注明）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{clock}\enspace 时间的测量者\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育（Berkeley BS 1931/PhD 1933）、博士（Wendell Mitchell Latimer）、核心领域（radiocarbon dating）、荣誉（1960 诺奖）。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「放射性衰变的指数钟」母题——离散圆点渐次稀疏暗示半衰期递减。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化（宇宙线生成 C-14 核反应式 ^1n + ^14N → ^14C + ^1p 为 page.md 实载；C-14 半衰期 5,730±40 年）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Willard Frank Libby（中文惯称：威拉德·利比）
- **生卒**：1908-12-17 生于美国科罗拉多州 Parachute（农场家庭）→ 1980-09-08 逝于洛杉矶 UCLA Medical Center（肺血块并发肺炎），享年 71
- **国籍**：United States（美国）
- **身份**：物理化学家（physical chemist；放射性碳测年发明人、AEC 委员）
- **家庭**：农场主 Ora Edward Libby 与妻 Eva May（娘家姓 Rivers）之子，有两兄 Elmer、Raymond 与两妹 Eva、Evelyn；5 岁随家迁加州 Santa Rosa；身高 6 英尺 2 寸，高中橄榄球队 tackle。1940 年娶体育体育教师 Leonor Hickey（1945 年生双胞胎女 Janet Eva、Susan Charlotte；1966 离婚）；1967 年娶核物理学家 Leona Woods Marshall（Chicago Pile-1 原始建造者之一，1986 卒；通过此婚姻获两名继子）
- **教育轨迹**：
  - 科罗拉多乡村两间校舍小学起步
  - Analy High School（Sebastopol，1926 毕业）
  - 1927 入 University of California, Berkeley；BS 1931、PhD 1933（论文 "Radioactivity of ordinary elements, especially samarium and neodymium: method of detection"）
- **导师**：Wendell Mitchell Latimer（博士导师，infobox + 正文双载）
- **博士**：1933，Berkeley（普通元素放射性，尤其钐与钕的检测方法）
- **研究领域**：物理化学——放射性碳测年、弱放射性测量、核化学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **科罗拉多农场之子（1908）**：Parachute 出生、Santa Rosa 长大——从两间校舍走向 Berkeley。
2. **独立发现钐衰变（1933）**：独立于 George de Hevesy 与 Max Pahl 的工作，发现钐的天然长寿命同位素主要经 α 衰变。
3. **盖革计数器专家（1930s）**：在 Berkeley 逐年晋升（1933 Instructor、1938 助理教授），建造灵敏盖革计数器测量微弱天然与人工放射性——为日后测年技术储备了全部手段。
4. **Guggenheim Fellowship（1941）**：赴 Princeton University 工作。
5. **曼哈顿计划（1941–1945）**：珍珠港次日（1941-12-08）主动请缨于 Harold Urey；赴哥伦比亚大学 SAM 实验室，从事铀浓缩气体扩散法研究——Norris-Adler 镍粉 barriers 评估与 K-25 工厂设计（1945 年 2 月投产）。广岛投弹后他把一摞报纸带回家对妻子说 "This is what I've been doing."（page.md 唯一直接引语）。
6. **芝加哥大学与碳十四（战后）**：出任芝加哥大学核研究所化学教授；基于 Serge Korff 1939 年"宇宙线在高层大气产生中子"的发现（中子与氮-14 反应生成碳-14），意识到生物死亡后停止摄入碳-14——有机物自带"核时钟"。
7. **放射性碳测年理论（1946/1949/1955）**：1946 年发表理论；1949 年发展出放射性碳测年方法；1955 年出版专著 *Radiocarbon Dating*；以已知树轮年代的巨杉验证其可靠准确——革命性改变考古学与古生物学。
8. **氚测年**：发现氚可用于测定水（因此也包括酒）的年龄。
9. **1960 诺贝尔化学奖**：官方理由 "for his method to use carbon-14 for age determination in archaeology, geology, geophysics, and other branches of science"；1960-12-12 诺奖演讲 "Radiocarbon Dating"。
10. **原子能委员会（1950–1959）**：1950 入 GAC；1954 年由艾森豪威尔总统任命为 AEC 委员——五名委员中唯一的科学家；支持 Teller 的氢弹紧急计划、参与"Atoms for Peace"并为此辩护大气核试验（1955/1958 日内瓦和平利用原子能会议美国代表团成员）。
11. **Project Sunshine（1956 公开）**：1953 年发起、1956 年 1 月公开的秘密研究——评估放射性沉降物对全球人口的影响；公开后因涉及未经父母同意采集死者（多为婴幼儿童）遗体做放射性实验而引发巨大争议。
12. **UCLA 岁月（1959–1976）**：辞去 AEC，任 UCLA 化学教授至 1976 退休；1962 年起兼加州大学系统 IGPP 主任（任内跨阿波罗计划与登月）；1972 年创办 UCLA 首个环境工程项目；任加州空气资源委员会成员改进空气污染标准（研究多相催化以减少机动车排放）。
13. **迟来的争议与认可**：1968 年尼克松当选后一度盛传其将出任总统科学顾问，因科学界抗议未成；1947 年测年论文 2016 年获 ACS 化学史分会 Citation for Chemical Breakthrough Award；Analy High School 图书馆有其壁画，Sebastopol 有以其命名的公园与公路。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深海蓝深青 deepocean） | `#0F4C5C` | 深海般的岁月纵深（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（碳十四测年 badgeC14） | `#2E5A9E` | 蓝放射性碳钟 |
| 分类色 2（曼哈顿计划 badgeManh） | `#7A1E28` | 绛红气体扩散 / K-25 |
| 分类色 3（原子能委员会 badgeAEC） | `#1B7A43` | 绿核政策与 Atoms for Peace |
| 分类色 4（环境科学 badgeEnv） | `#D97B29` | 琥珀IGPP / 环境工程 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「半衰期指数衰减」的疏密渐变。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**New Lands** — Alex-Productions（文件路径见 manifest `music_audio/alex-productions/74-oK8HN0FsZmc-New-Lands.wav`；**不要复制 wav 文件**）
- **风格**：辽阔 / 开疆拓土 / 纪实感
- **匹配理由**：
  - "New Lands（新大陆）" 匹配测年技术为考古学打开的时间新边疆——让史前有了绝对年代
  - "辽阔纪实" 匹配其横跨实验室、曼哈顿工程、核政策与地球物理的多面人生
  - 曲名的开拓气质呼应 IGPP 主任任内的阿波罗与登月时代
- **时长**：以实际文件为准 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 时间的测量者 / Willard Libby 1908–1980 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  利比的一生 — Sanger 式时间线（10 节点：1908→1931→1933→1941→1946→1949→1954→1960→1962→1980）
04  农场少年与 Berkeley（1908–1933）— 表格「时间|事件|结果」（两间校舍 → Analy High School → BS/PhD）
05  盖革计数器与钐衰变（1930s）— 表格「问题|方法|结果」+ 公式框：钐 α 衰变独立发现
06  曼哈顿计划（1941–1945）— 表格「任务|方法|意义」（SAM 实验室、气体扩散、K-25）
07  碳十四测年（1946–1955）— 表格「问题|方法|结果」+ 公式框：^1n + ^14N → ^14C + ^1p；半衰期 5,730±40 年
08  1960 诺贝尔化学奖 — 表格「领域|贡献|认可」+ 公式框：官方获奖理由原文
09  原子能委员会（1950–1959）— 表格「职务|立场|事件」（GAC → 委员、氢弹、Atoms for Peace）
10  Project Sunshine 与争议 — 表格「事件|年份|影响」（1953 发起、1956 公开、争议要点客观简述）
11  UCLA 与环境科学（1959–1976）— 表格「领域|工作|结果」（IGPP/环境工程/空气资源委员会）
12  家庭 — 表格「人物|关系|注」（两任妻子：Leonor Hickey、Leona Woods Marshall）
13  遗产：给过去一个年代 — 四分类遗产盒 + 公式框：Citation for Chemical Breakthrough 2016
14  结尾 — 「他让每一块骨头和每一片木屑，都开口报出了自己的年龄。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1960 诺奖 | **独享**，官方理由 "for his method to use carbon-14 for age determination in archaeology, geology, geophysics, and other branches of science"；page.md 亦强调 "his contributions to the team"——勿写"独自发明了考古学" |
| 测年年份 | 1946 发表理论、1949 发展出方法、1955 专著——三个年份勿混写 |
| 半衰期 | C-14 半衰期 **5,730±40 年**（勿用已废弃的 Libby 半衰期 5568 年——页面无载禁写） |
| Korff 分工 | 宇宙线中子发现是 **Serge Korff（1939）**；利比是应用者——勿写利比"发现"宇宙线生成 C-14 |
| 钐衰变 | "独立于 de Hevesy 与 Max Pahl 的工作"——是并列独立发现，勿写成师承或合作 |
| 唯一引语 | 全文仅 "This is what I've been doing." 一处直接引语（对妻子、广岛报纸）——勿再杜撰第二句 |
| Project Sunshine | 页面实载"未经父母同意获取死婴遗体做实验"的争议内容——如写入须一句客观带过，重点放 AEC 科学叙事；细节渲染禁止 |
| 氢弹立场 | 利比**支持 Teller**（与 Oppenheimer 对立阵营）——如实呈现，勿写成"反对氢弹" |
| 妻子姓名 | 第一任 Leonor Hickey（1940 娶、1966 离）；第二任 **Leona Woods Marshall**（1967 娶）——勿与 Chicago Pile-1 事实混淆归属 |
| 学位年份 | BS 1931、PhD 1933——勿颠倒；Guggenheim 1941 赴 Princeton |
| AEC 辞职 | 1959 辞职转 UCLA——勿写"任期结束" |
| 死因 | 肺部血块并发肺炎（UCLA Medical Center）——勿写癌症 |
| 引语红线 | 其余叙述一律间接转述 page.md 原文 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q190486 | ✅ |
| name_zh | 威拉德·利比 | ✅ |
| name_en | Willard Libby | ✅ |
| birth_date | 1908-12-17 | ✅ |
| death_date | 1980-09-08 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | physical chemistry（person_field 细分见下表，带 rank） | ✅ |
| has_biography | 0（立传 Beamer 完成后置 1） | ✅ |

**person_field 细分 rank 表**：

| name_en | rank | name_zh | 依据 |
|---|---|---|---|
| radiocarbon dating | 0 | 放射性碳测年 | 1960 诺奖理由 |
| physical chemistry | 1 | 物理化学 | infobox Fields |
| weak radioactivity measurement | 2 | 微弱放射性测量 | 盖革计数器工作 |
| isotope tracing | 3 | 同位素示踪 | 氚测水龄 |

## 7. 社会关系入库清单

**★ 红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Wendell Mitchell Latimer | 师→生（博士导师） | 1933 PhD（普通元素放射性论文） |
| advisor-student | Maurice Sanford Fox | Libby → 学生 | infobox Doctoral students |
| advisor-student | Frank Sherwood Rowland | Libby → 学生 | infobox Doctoral students；1995 诺贝尔化学奖得主（规范名取 page.md 全名 Frank Sherwood Rowland） |
| colleague | Harold Urey | 无向 | 1941 利比主动请缨，Urey 安排其离开 Berkeley 加入哥伦比亚 SAM 实验室（曼哈顿计划） |
| influence | Serge Korff | 无向 | Korff 1939 发现宇宙线高层大气产生中子——碳-14 生成机制的思想源头 |
| spouse | Leonor Hickey | 无向 | 1940 结婚，1945 双胞胎女，1966 离婚 |
| spouse | Leona Woods Marshall | 无向 | 1967 结婚；核物理学家、Chicago Pile-1 原始建造者之一；1973 随夫任 UCLA 环境工程教授 |

> **禁入库名单（政治立场/非直接合作，page.md 虽提及但不构成学术人际）**：Edward Teller（氢弹立场同侧）、Robert Oppenheimer（对立阵营）、George de Hevesy 与 Max Pahl（平行独立发现非合作）、Richard Nixon / Lewis Strauss / Gordon Dean / Dwight D. Eisenhower（任命与政治人物）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1960，独享；"for his method to use carbon-14 for age determination in archaeology, geology, geophysics, and other branches of science"）
- Guggenheim Fellowship（1941）
- Chandler Medal, Columbia University（1954）
- Remsen Memorial Lecture Award（1955）
- Bicentennial Lecture Award, City College of New York；Nuclear Applications in Chemistry Award（1956）
- Elliott Cresson Medal, Franklin Institute（1957）
- Willard Gibbs Award, American Chemical Society（1958）
- Joseph Priestley Award, Dickinson College（1959）；Albert Einstein Medal（1959）
- Arthur L. Day Medal, Geological Society of America（1961）
- Golden Plate Award, American Academy of Achievement（1961）
- Gold Medal of the American Institute of Chemists（1970）；Lehman Award, New York Academy of Sciences（1971）
- Citation for Chemical Breakthrough Award（2016，ACS 化学史分会，授予芝加哥大学，纪念 1947 测年论文）
- 美国国家科学院院士（1950 当选）；American Academy of Arts and Sciences；American Philosophical Society

## 9. 机构清单

- 教育：Analy High School（Sebastopol，1926）；University of California, Berkeley（BS 1931、PhD 1933）
- 任职：Berkeley 化学系（1933 Instructor、1938 助理教授）；Princeton University（1941–1942，Guggenheim）；SAM Laboratories, Columbia University（1942–1945，曼哈顿计划）；University of Chicago 核研究所（战后教授）；UCLA（1959–1976 化学教授；1962–1976 兼加州大学 IGPP 主任）
- 公职：AEC General Advisory Committee（1950）；AEC 委员（1954–1959，艾森豪威尔任命）；Atoms for Peace；1955/1958 日内瓦和平利用原子能会议美国代表团；California Air Resources Board
- 纪念：Analy High School 图书馆壁画；Sebastopol 利比公园与公路；论文藏 UCLA Charles E. Young Research Library（七卷本文集 1981 年由 Leona 与 Rainer Berger 编辑出版）

## 10. 终审清单

- [ ] 生卒 1908-12-17 / 1980-09-08，享年 71，出生地 Parachute（科罗拉多）、去世地洛杉矶 UCLA Medical Center
- [ ] 1960 **独享**，官方理由原文完整引用（archaeology, geology, geophysics 顺序勿改）
- [ ] Korff（1939 发现）→ Libby（1946 理论/1949 方法/1955 专著）分工勿混
- [ ] 唯一引语 "This is what I've been doing." 出处（广岛报纸、对妻子）准确
- [ ] 氢弹立场（支持 Teller）与 Project Sunshine 争议表述客观、不渲染
- [ ] 两任妻子姓名与年份（1940/1966/1967）准确
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Willard_Libby/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：核对 images/Willard_Libby_in_Lab.jpg（实验室照）
- [ ] **国籍**：封面顶部明示美国
- [ ] **引语核对**：全文仅一处直接引语且可在 page.md 找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 等）对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾，本文件不改动该脚本。
