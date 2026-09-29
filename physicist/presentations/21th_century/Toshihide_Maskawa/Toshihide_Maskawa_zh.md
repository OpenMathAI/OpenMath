# 物理学家立传提示词（Toshihide Maskawa 益川敏英）

> **OpenPhysicist 21 世纪批次**人物专属立传提示词。以 Kenneth_G_Wilson_zh.md 为结构母本（0–11 节），
> 本文件为 Toshihide Maskawa（2008 诺贝尔物理学奖，CKM 矩阵与 CP 破缺）定制。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位 【模板通用】

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Toshihide Maskawa（益川 敏英，1940-02-07 ~ 2021-07-23，享年 81 岁）。
- **设计哲学**：物理学家立传必须有「身份信息页」（Identity / Bio 速览页），且强调「研究领域」的结构化表达——这两点构成模板骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Toshihide Maskawa（益川 敏英，1940-02-07 生于名古屋 ~ 2021-07-23 逝于京都）
- **气质关键词**：**相位角的破译者、汤川研究所掌门、日语诺奖演讲第一人** —— 2008 诺贝尔物理学奖获奖理由（官方原文，禁止改写）：
  > "for the discovery of the origin of the broken symmetry which predicts the existence of at least three families of quarks in nature"（发现对称性破缺的起源，预言了自然界至少存在三代夸克；与小林诚共享 1/2 奖金，即个人得 1/4）
- **设计母题**：**复相位角（complex phase）**。CP 破缺的唯一来源是 CKM 矩阵中的复相位 δ——可用「旋转的复平面 + 相位差扇形」的视觉语言，与一般线段/圆环区分。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Toshihide_Maskawa/page.md`（已有本地）
- **待下载**：`Toshihide_Maskawa.html` 与 `images/` 待下载；Wikipedia URL：`https://en.wikipedia.org/wiki/Toshihide_Maskawa`
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

### 第 0 步：事实基准 【人物专属，page.md 已核对】

- 生卒：1940-02-07 生于名古屋（当时属大日本帝国）~ 2021-07-23 逝于京都家中（口腔癌，享年 81 岁；恰逢东京奥运开幕式同日，与三重灾难及新冠无关；2021-10 私人葬礼后火化）。
- 国籍：日本（frontmatter 含 Empire of Japan 出生口径）。
- 家庭：二战后家中经营砂糖批发业。1967 年与高桥明子（Akiko Takahashi）结婚，育有 Kazuki 与 Tokifuji 二子女。
- 教育：1962 名古屋大学毕业；1967 名古屋大学粒子物理 PhD，博士论文《粒子と共鳴準位の混合効果について》（1967）。
- 博士导师：Shoichi Sakata（page.md 明载 "His doctoral advisor was the physicist Shoichi Sakata"）。
- 博士后：page.md 无载。
- 幕间侧写：自幼喜欢杂学（trivia），自学数学、化学、语言学；高中爱读小说，尤其侦探推理与芥川龙之介。计算不用计算机——计算尺现藏斯德哥尔摩诺贝尔博物馆。
- 任职机构（Professional record 全表）：
  - 1967-07 名古屋大学理学部助手
  - 1970-05 京都大学理学部助手
  - 1976-04 东京大学原子核研究所副教授
  - 1980-04 京都大学基础物理学研究所（现汤川研究所 YITP）教授
  - 1990-11 京都大学理学部教授
  - 1995 京都大学评议员
  - 1997-01 汤川研究所教授；1997-04 ~ 2003 汤川研究所所长
  - 2003-04 京都大学名誉教授；京都产业大学教授（至 2009-05）
  - 2004-10 京都产业大学研究所所长
  - 2007-10 名古屋大学特聘教授（Distinguished Invited University Professor）
  - 2009-02 京都产业大学理事；2009-03 名古屋大学大学教授；2009-06 益川塾塾长兼教授（至 2019-03）
  - 2010-04 小林·益川研究所（KMI）所长；2010-12 日本学士院会员
  - 2018-04 KMI 名誉所长；2019-04 京都产业大学名誉教授
- 关键荣誉：仁科纪念奖 1979；樱井奖 1985；日本学士院奖 1985；中日文化奖 1995；朝日奖 1995；欧洲物理学会高能与粒子物理奖 2007；诺贝尔物理学奖 2008（1/4）；文化勋章 2008；日本学士院会员 2010-12；上海交通大学荣誉博士（frontmatter）。
- 知名学生：page.md 无载（禁写）。
- 核心贡献清单：
  1. 与小林诚 1973 年论文《CP Violation in the Renormalizable Theory of Weak Interaction》——CP 破缺在小林·益川矩阵（CKM 矩阵）框架下的解释；
  2. 预言自然界至少存在三代夸克（六味夸克），四年后由底夸克发现实验证实；
  3. 该论文截至 2010 年为高能物理史上被引第四高的论文；
  4. 1997–2003 任汤川理论物理研究所所长；
  5. KMI 首任所长、益川塾塾长——跨学科与人才培养。
- 关键时间线（15 节点）：
  1. 1940-02-07 生于名古屋
  2. 二战后家中经营砂糖批发
  3. 高中沉迷推理小说与芥川龙之介
  4. 1962 名古屋大学毕业
  5. 1967 名古屋大学 PhD（导师坂田昌一）
  6. 1967 与高桥明子结婚
  7. 1967-07 名古屋大学助手；1970-05 转京都大学助手
  8. 1973 与小林诚发表 CP 破缺论文，预言三代夸克
  9. 1977 底夸克发现，预言四年内获证实
  10. 1976-04 东大原子核研究所副教授；1979 仁科纪念奖
  11. 1980-04 京都大学基研教授
  12. 1985 樱井奖 + 日本学士院奖
  13. 1997-04 ~ 2003 汤川研究所所长
  14. 2007 EPS 高能与粒子物理奖；2008 诺贝尔奖（1/4）+ 文化勋章
  15. 2008-12-08 斯德哥尔摩大学以日语发表诺奖演讲 "What Did CP Violation Tell Us?"
  16. 2010-04 KMI 首任所长；2010-12 日本学士院会员
  17. 2018-04 KMI 名誉所长；2019-04 京产大名誉教授
  18. 2021-07-23 逝于京都，享年 81 岁

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 在 `physicist/presentations/21th_century/` 下建 `Toshihide_Maskawa/` 与 `images/`；Makefile 设 `MAIN=Toshihide_Maskawa_zh`、`VIDEO_NAME=Toshihide_Maskawa_zh`。
- 肖像：2008 年 2008 诺贝尔记者会同框照（Commons，Krugman-Tsien-Chalfie-Shimomura-Kobayashi-Masukawa）可裁右端；404 则用装饰圆占位。

### 第 4 步：研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | particle physics | 粒子物理 | 主业：高能物理理论 | 封面、核心页 |
| 1 | CP violation | CP 破缺 | 1973 论文核心问题 | 核心页 |
| 2 | weak interaction | 弱相互作用 | 论文题目限定 renormalizable theory | 理论页 |
| 3 | quark mixing | 夸克混合 | CKM 矩阵的物理内涵 | 矩阵页 |
| 4 | standard model | 标准模型 | CKM 为其组成部分 | 脉络页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Shoichi Sakata | 师→生（博士导师） | 名古屋大学博士导师（1967），坂田模型提出者 |
| colleague | Makoto Kobayashi | 无向 | 京都大学同事，1973 年 CP 破缺论文合作者 |
| co-honored | Makoto Kobayashi | 无向 | 2008 诺贝尔物理学奖共享 1/2 |
| co-honored | Yoichiro Nambu | 无向 | 2008 诺贝尔物理学奖另一半得主 |
| spouse | Akiko Takahashi | 无向 | 1967 年结婚，育 Kazuki/Tokifuji 二子女 |

> 无载禁写：与小林诚之间无师生关系（二人同出坂田门下但是同辈合作者）；Nicola Cabibbo（仅矩阵命名）；日意合作者/学生均未载。

### 第 5 步：配色方案 【人物专属】

- **气质**：桀骜、复相位、和风文人
- **主色**：深紫 `#5B2A86`（复相位的神秘感）+ 诺奖香槟金 `C9A227`
  - `badgeCP` CP 破缺 — 玫瑰 `#C4204F`
  - `badgeYITP` 汤川研究所 — 靛蓝 `#3B5998`
  - `badgeKMI` 小林·益川研究所 — 青绿 `#0E7C7B`
  - `badgeJuku` 益川塾 — 琥珀 `#C87F2F`
- **背景母题**：复平面上缓慢旋转的相位扇形与单位圆刻度，象征 CKM 相位 δ——CP 破缺的唯一来源。

### 第 6 步：幻灯片序列（10–16 页规划）【人物专属】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 相位角的破译者 / Toshihide Maskawa 1940–2021 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒/国籍/出生地/师承/任职/荣誉/核心领域）
03  核心贡献概览 — CP 破缺 / CKM 矩阵 / 三代预言 / 汤川研究所
04  早年：名古屋与杂学少年 (1940–1962) — 砂糖批发、芥川龙之介
05  名古屋大学：坂田门下 (1962–1967) — PhD 论文、混合效应
06  京都协作：与小林诚 (1970–1976) — 1973 论文诞生
07  CKM 矩阵：复相位的力量（核心贡献页，公式框放 3×3 CKM 矩阵与相位因子 e^{iδ}）
08  三代预言与证实 — 1977 底夸克、史上第四高引
09  东大与基研 (1976–1997) — 副教授→基研教授→汤川所长
10  诺奖之年 2008 — 记者会同框 · "Sorry, I cannot speak English" 日语演讲
11  KMI 与益川塾 (2007–2019) — 首任所长、塾长、计算尺藏于诺贝尔博物馆
12  荣誉与晚年 — 学士院 2010 · 京都家中 2021
13  结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 得奖份额 | Maskawa 与 Kobayashi **共享 1/2**（个人 1/4），另一半归南部阳一郎；勿写成「三人平分」 |
| 名字拼写 | 正文用 Maskawa（本人自称/罗马字 Masukawa），照片说明作 Masukawa；立传统一用 Maskawa，首段可注明 (or Masukawa) |
| 得奖理由 | 官方措辞强调 "origin of the broken symmetry…at least three families of quarks"；勿改写 |
| 与小林关系 | 二人同为坂田昌一门下但是**同辈合作者**（colleague），禁写成师生 |
| 政治主张 | page.md 有 Political proposition 一节（与白川英树 2013 年反对特定秘密保护法声明、宪法第九条、靖国神社、夫妇别姓等）——**Beamer 立传与提示词正文一律回避不展开**，仅在陷阱表记录「禁写」裁定 |
| 诺奖演讲 | 2008-12-08 于斯德哥尔摩大学以**日语**演讲 "What Did CP Violation Tell Us?"，开场自嘲 "Sorry, I cannot speak English"；年份日期勿写错 |
| 计算尺 | 其计算尺藏于诺贝尔博物馆；勿写成「拒绝计算机」的杜撰细节 |
| 卒因 | 2021-07-23 口腔癌逝于京都家中，享年 81；与东京奥运开幕式同日——可客观并记，勿渲染 |
| 师承 | 博士导师 Shoichi Sakata（1967，名古屋），论文题为日文《粒子と共鳴準位の混合効果について》 |
| 机构沿革 | 基础物理学研究所（基研）现名汤川理论物理研究所（YITP），1997 起任所长至 2003；勿与 KEK 混淆 |

### 第 9 步：术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| CKM matrix | 小林·益川矩阵（CKM 矩阵） | 全称 Cabibbo–Kobayashi–Maskawa matrix |
| CP violation | CP 破缺 | 非「CP 不守恒」的口语化 |
| broken symmetry | 对称性破缺 | 获奖理由原词 |
| complex phase | 复相位 | CP 破缺唯一来源 |
| quark generation | 夸克代 | 三代=六味夸克 |
| bottom quark | 底夸克 | 1977 发现 |
| Yukawa Institute | 汤川理论物理研究所 | 基研改名，京都大学 |
| KMI | 小林·益川研究所 | 名古屋大学，2010 设立 |
| Maskawa Juku | 益川塾 | 京都产业大学，跨学科 |
| slide rule | 计算尺 | 藏于诺贝尔博物馆 |

---

## 四、BGM 建议 【人物专属】

- **选定曲目**：**Cinematic Experience** — Alex-Productions（电影感/高张力）
- **匹配理由**：电影感匹配其「相位角改写标准模型」的戏剧性——1973 论文沉寂三十年后在 B 介子工厂被证实时张力拉满；高张力基调也贴合益川桀骜的文人气质与日语演讲的著名瞬间。
- **备选**：Through the Darkness（攻克难题）、Tragedy（晚年）。
- 批内不重复：本批 Kobayashi=The Invisible Light、Kao=Shine Like The Sun、Boyle=Daylight、Smith=Ascension。

---

## 五、执行红线 【模板通用】

- 只收 page.md 明载的关系；yaml note 含 ": " 或以引号开头时整体单引号包裹。
- 对手方入库用规范名：Shoichi Sakata（库内 id=2094 复用）、Makoto Kobayashi（库内 id=2972 复用）、Yoichiro Nambu、Akiko Takahashi；不给对手方编造 qid。
- 政治主张节（特定秘密保护法/宪法第九条/靖国神社/夫妇别姓）禁入 Beamer 与关系库。
- 禁止修改 generate_21st_century_list.py、名录 md、模板文件。
