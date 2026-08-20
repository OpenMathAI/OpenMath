# 亨德里克·安东·洛伦兹 (Hendrik Antoon Lorentz) 立传提示词

> 本提示词严格遵循 `physicist` 项目的人物立传规范（`Physicist_Bio_Prompt_Template.md`），并融合物理学家侧标杆（`Kenneth_G_Wilson_zh.md` / `Wilhelm_Rontgen_zh.md`）与数学家侧范例（`Emmy_Noether_zh.md`）的全面结构（含「研究领域入库」「社会关系入库」「人格特质」「独有叙事线索」等章节），为洛伦兹制作 Beamer 演示文稿。
> 直接复制本文件内容到新对话中使用。

---

## 背景信息 【人物专属】

- **目标物理学家**: Hendrik Antoon Lorentz（亨德里克·安东·洛伦兹，1853-07-18 ~ 1928-02-04，享年 74 岁）
- **气质关键词**: **电子论的奠基人、经典物理的集大成者、相对论的引路人、世界物理学界的领航者** — "因他们研究磁对辐射现象的影响所作出的杰出贡献"（1902 诺贝尔物理学奖获奖理由，与 Pieter Zeeman 共享）
- **本地 Wikipedia**:
  - 权威数据源：`physicist/presentations/pages/20th_century/Hendrik_Antoon_Lorentz/page.md`（已含完整 infobox + 正文）
  - 结构化元数据：`physicist/presentations/pages/20th_century/Hendrik_Antoon_Lorentz/metadata.json`
  - 立传目录 HTML：`physicist/presentations/20th_century/Hendrik_Lorentz/Hendrik_Lorentz.html`
- **参考模板**:
  - 物理学家模板标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 物理学家首例成品：`physicist/presentations/20th_century/Eugene_Wigner/Eugene_Wigner_zh.tex`
  - 物理学家最近成品：`physicist/presentations/20th_century/Wilhelm_Rontgen/Wilhelm_Rontgen_zh.tex`（含 Hohenheim 任职、Ioffe 师承等修正经验）
  - 通用模板：`physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md`
- **后续配套数据库脚本**（见第 4 步 / 第 4.5 步）：
  - `MySQL/seed_lorentz_full.py` — 人物主记录 + 研究领域入库（`person_field`）
  - `MySQL/seed_lorentz_relations.py` — 社会关系入库（`person_relation`）

---

## 你的任务

按照本提示词的步骤依次完成。**每完成一步向我汇报进度**，遇到歧义时先征求我的意见再继续。

> **数据库同步要求**：本提示词包含「研究领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步）两个数据库步骤。请严格按步骤操作，将洛伦兹的**研究领域**与**社会关系**写入 `greatminds` 数据库（MySQL），这是 OpenPhysicist 项目人物关系网络的一部分，与 Beamer 立传并行。

---

## 第 0 步：确认 Wikipedia 页面已就绪

- 读取本地 Wikipedia `page.md`、`metadata.json` 的 infobox 与正文
- 输出供校验的信息（事实基准如下）：

  - **生卒日期**：1853-07-18 生于荷兰阿纳姆（Arnhem）～ 1928-02-04 逝于荷兰哈勒姆（Haarlem），享年 74 岁
  - **国籍**：荷兰（Kingdom of the Netherlands），荷兰"第二个黄金时代"科学繁荣的代表人物
  - **父母**：父 Gerrit Frederik Lorentz（1822–1893）；母 Geertruida van Ginkel（1826–1861）。1862 年母亲去世后父亲续娶 Luberta Hupkes。虽受新教教育，但洛伦兹是宗教上的自由思想者，常参加当地法国教堂的天主教弥撒
  - **教育**：1866–1869 就读阿纳姆 HBS（高等市民学校）；1870 通过古典语言考试入莱顿大学；1871 获数学与物理学士；1875 年获博士学位
  - **博士导师**：Pieter Rijke；**学术引路人**：Frederik Kaiser（莱顿大学天文学教授，引导洛伦兹成为物理学家）
  - **博士论文**：1875《Over de theorie der terugkaatsing en breking van het licht》（论光的反射与折射），在论文中修正了麦克斯韦电磁理论
  - **主要任职机构**：
    - 1878 莱顿大学理论物理教席（25 岁获任，该教席原拟授予 van der Waals）— 就职演说《De moleculaire theoriën in de natuurkunde》（物理学中的分子理论）
    - 1912 辞去教席，任泰勒博物馆（Teylers Museum）物理陈列室 Curator；继续在莱顿任编外教授，主讲著名的"周一晨课"
  - **关键荣誉**：诺贝尔物理学奖 1902（与 Pieter Zeeman 共享）；Rumford Medal 1908；Franklin Medal 1917；Copley Medal 1918；Pour le Mérite 1908
  - **学术地位**：1911 首届索尔维会议主席；1925–1928 国际智力合作委员会主席（UNESCO 前身）
  - **家庭**：1881 与 Aletta Catharina Kaiser 结婚，育两女一子；长女 Geertruida de Haas-Lorentz 是物理学家（其父的博士生），嫁 Wander de Haas（莱顿 Kamerlingh Onnes 实验室主任）
  - **核心贡献**（metadata `notable_work` 13 项）：
    - Lorentz transformation（洛伦兹变换）
    - Lorentz force（洛伦兹力）
    - Lorentz ether theory（洛伦兹以太论）
    - Lorentz factor（洛伦兹因子）
    - Lorentz covariance（洛伦兹协变性）
    - Lorentz group（洛伦兹群）
    - Lorentz oscillator model（洛伦兹振子模型）
    - length contraction / Lorentz–FitzGerald contraction（长度收缩）
    - Lorentz–Lorenz equation、Abraham–Lorentz force、Drude–Lorentz model、Heaviside–Lorentz units 等
  - **关键时间线**（15–20 个节点）：
    1. 1853-07-18 生于荷兰阿纳姆
    2. 1862 母亲去世，父亲续娶
    3. 1866–1869 就读阿纳姆 HBS，成绩优异（数理 + 英法德三语）
    4. 1870 入莱顿大学，受天文学家 Kaiser 影响转向物理
    5. 1871 获数学物理学士
    6. 1872 回阿纳姆任夜校教师，同时继续莱顿学业
    7. 1875 博士毕业（Pieter Rijke 指导），论文论光的反射与折射
    8. 1878 获莱顿大学理论物理教席（25 岁）
    9. 1881 与 Aletta Catharina Kaiser 结婚
    10. 1892 提出长度收缩（解释迈克耳孙-莫雷实验）、引入"局域时间"（local time）
    11. 1895 完善运动参考系电磁现象描述
    12. 1896 Zeeman 发现塞曼效应，Lorentz 提供理论解释
    13. 1899/1904 加入时间膨胀，发表洛伦兹变换（Poincaré 1905 命名）
    14. 1902 获诺贝尔物理学奖（与 Zeeman 共享）
    15. 1904 论文含电动力学协变形式
    16. 1905 Einstein 发表狭义相对论
    17. 1906 哥伦比亚大学 Adams 讲座；1909《The Theory of Electrons》出版
    18. 1911 主持首届索尔维会议
    19. 1912 辞教席，任泰勒博物馆 Curator
    20. 1918–1926 主持须德海（Afsluitdijk）拦海大坝水文计算
    21. 1925–1928 任国际智力合作委员会主席
    22. 1928-02-04 逝于哈勒姆；02-10 葬礼，荷兰电报电话停运三分钟致敬

### 人格特质线索（源自 Wikipedia 引语）

- **世界物理学界的领航者**：诺奖基金会传记称"洛伦兹被所有理论物理学家视为世界公认的领航者，他完成了前人未竟的事业，为量子论新思想的接受铺平了道路"
- **"听听洛伦兹会怎么说"**：M. J. Klein（1967）写道"多年来，每当新理论提出，物理学家们总是渴望'听听洛伦兹会怎么说'，即便七十二岁高龄，他也从不让人失望"
- **Einstein 的至高评价**：1928 年 Einstein 悼词称其工作"构成原子论、广义与狭义相对论的基础"；1953 年又写道"对我个人而言，他比我一生中遇到的任何人都更重要"
- **谦逊与诚实**：Lorentz 坦然承认 Poincaré 的贡献——"Poincaré 获得了电动力学方程的完美不变性，并率先提出了'相对性公设'……纠正我工作中的不完善之处时，他从未责备过我"
- **理论物理做工程的奇才**：主持须德海拦海大坝计算，用"人肉计算机"数值求解流体力学方程，预测惊人准确，一组水闸以他命名

### 与其他已立传物理学家的关系网络

- **Pieter Zeeman** — 同事兼前学生（"其他知名学生"），1896 实验发现塞曼效应，Lorentz 提供理论解释，1902 共享诺奖。两人是理论与实验印证关系的典范
- **Albert Einstein** — 深厚友谊；1910 年 Lorentz 邀其继任莱顿教席被拒（Einstein 刚赴 ETH），最终选 Ehrenfest 继任。Einstein 对 Lorentz 的评价（page.md 原文，须逐字溯源）：
  - 1928 悼词："The enormous significance of his work consisted therein, that it forms the basis for the theory of atoms and for the general and special theories of relativity."（"构成原子论、广义与狭义相对论的基础"）
  - 1953："For me personally he meant more than all the others I have met on my life's journey."（"对我个人而言，他比我人生旅途中遇到的所有其他人都更重要"）
- **Henri Poincaré** — 高度评价 Lorentz 理论，命名"洛伦兹变换"与"相对性公设"，是 Lorentz 理论的重要诠释者
- **Paul Ehrenfest** — 1912 年继任者，Lorentz 的学生辈物理学家
- **Joseph Larmor** — 1897 年独立使用相同变换描述电子（Lorentz 当时不知情），变换的早期并行发现者
- **Wander de Haas** — 女婿，莱顿 Kamerlingh Onnes 实验室主任
- **Geertruida de Haas-Lorentz** — 长女，物理学家，其父的博士生

---

## 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/20th_century/` 下创建 `Hendrik_Lorentz/` 子目录与 `images/`

---

## 第 2 步：复制 Makefile 【模板通用】

- 复制标杆实例 `Kenneth_G_Wilson/Makefile` 或 `Wilhelm_Rontgen/Makefile`，设置 `MAIN=Hendrik_Lorentz_zh`、`VIDEO_NAME=Hendrik_Lorentz_zh`

---

## 第 3 步：收集图片 【人物专属】

- 从 Wikipedia infobox 下载洛伦兹肖像照（"Lorentz in 1902"，1902 年诺奖时期照片）到 `images/Lorentz.jpg`
- 可选补充：
  1. 与 Einstein 的合影（1921 年莱顿，Ehrenfest 拍摄）— 体现二人的深厚关系
  2. 洛伦兹力/麦克斯韦方程的 1892 年手稿公式页
  3. 首届索尔维会议合影（1911，Lorentz 为主席）
  4. 须德海拦海大坝相关图片（体现其工程贡献）
- 优先真实感与学术气质，不做刻意美化

---

## 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

> **目的**：把研究领域变成可检索、可图形化的结构化字段（`fields` + `person_field` 表）。

### 4.1 洛伦兹的研究领域（按重要性 rank 排序）

| rank | 领域（name_en） | 中文 | 说明 | 对应 Beamer 页 |
|:--:|------|------|------|------|
| 0 | electron theory | 电子论 | 原子由带电粒子组成、振荡产生光的核心理论 | 封面、核心页 |
| 1 | electrodynamics | 电动力学 | 麦克斯韦理论的推广、洛伦兹力 | 核心页 |
| 2 | relativity theory | 相对论 | 洛伦兹变换、长度收缩、局域时间 | 核心页 |
| 3 | magneto-optics | 磁光学 | 塞曼效应的理论解释（1902 诺奖） | 诺奖页 |
| 4 | hydrodynamics | 流体力学 | 须德海拦海大坝水文计算 | 工程页 |

> 领域字典 `fields` 表：`physics`、`theoretical physics` 等可能已存在，缺失的 `electron theory`/`electrodynamics`/`relativity theory`/`magneto-optics`/`hydrodynamics` 由 `seed_lorentz_full.py` 自动补建。

### 4.2 入库操作（见 `MySQL/seed_lorentz_full.py`）

- 新建 `people` 主记录：`name_en='Hendrik Antoon Lorentz'`、`name_zh='亨德里克·安东·洛伦兹'`、`primary_occupation='physicist'`、`has_biography=1`、`has_social_data=1`，qid=`Q41688`
- 关联职业 `physicist`（rank 0），国籍 `Netherlands`（荷兰）
- 将 5 个领域写入 `person_field`（带 rank），缺失领域先在 `fields` 建字典项
- 执行后校验：
  ```sql
  SELECT f.name_en, pf.rank FROM person_field pf
  JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=<id> ORDER BY pf.rank;
  ```

---

## 第 4.5 步：社会关系梳理 + 数据库入库 ★（数据库同步）

> **目的**：将洛伦兹的师承、合作、门生、家庭与科学影响写入 `person_relation`，形成可查询的人物关系网络。

### 4.5.1 关系清单（从 Wikipedia 提取）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Pieter Rijke | 师→生（博士导师） | 莱顿大学博士导师 |
| advisor-student | Frederik Kaiser | 师→生（学术引路人） | 莱顿天文学教授，引导其转向物理 |
| advisor-student | Pieter Zeeman | 生→师（洛伦兹为师的"其他知名学生"） | 塞曼效应发现者，1902 共享诺奖 |
| advisor-student | Geertruida de Haas-Lorentz | 生→师（长女亦为其博士生） | 物理学家 |
| advisor-student | Adriaan Fokker | 生→师（博士生） | 物理学家，福克-普朗克方程 |
| advisor-student | Leonard Ornstein | 生→师（博士生） | 物理学家，Ornstein-Uhlenbeck 过程 |
| colleague | Albert Einstein | 无向 | 深厚友谊，Einstein 称其一生最敬重之人 |
| colleague | Henri Poincaré | 无向 | 命名"洛伦兹变换"，高度评价其理论 |
| colleague | Paul Ehrenfest | 无向 | 1912 年继任莱顿教席 |
| colleague | Joseph Larmor | 无向 | 1897 年独立使用相同变换 |
| co-honored | Pieter Zeeman | 无向 | 1902 诺贝尔物理学奖共同得主 |
| spouse | Aletta Catharina Kaiser | 无向（夫妻） | 妻子，1881 结婚 |

> 关系类型键取自 `relation_types`：`advisor-student` / `colleague` / `co-honored` / `spouse`。

### 4.5.2 入库操作（见 `MySQL/seed_lorentz_relations.py`）

- 连接 `greatminds` 库，以 `name_en='Hendrik Antoon Lorentz'` 为中心
- 库中已存在人物优先复用（如 Einstein、Poincaré、Zeeman 可能已在库），不在库的先建占位（`has_biography=0`），关系 note 加 `[材料待展开] ` 前缀
- 有向关系 advisor-student 按师→生；无向（colleague/co-honored/spouse）按 `MIN(id)→MAX(id)` 存储
- 执行后校验并汇报：新建 X 人（占位）、新增 Y 条关系

---

## 第 5 步：设计配色方案 【人物专属】

- **气质**：电子论的深邃理性、相对论的前沿感、荷兰的严谨与谦逊、经典物理的集大成
- **建议配色**：深普鲁士蓝 + 荷兰橙（诺奖香槟金）+ 四个分类色
  - `badgeElectron` 电子论 — 深靛蓝 `#1A237E`
  - `badgeElectro` 电动力学 — 青绿 `#0E7C7B`
  - `badgeRelativity` 相对论 — 琥珀 `#E07B30`
  - `badgeMagneto` 磁光学 — 玫瑰 `#C4204F`
- **背景母题**：柔和气泡（稀疏大块实心圆，四种大小错落），呼应"洛伦兹变换"中不同参考系之间的尺度与相对性——层层透明度如坐标变换的嵌套
- **注意与已有立传区分**：Röntgen 用深黑蓝+香槟金、Wigner/Wilson 各有专属色，洛伦兹应选用可辨识的深普鲁士蓝 + 荷兰橙主调

### 5.1 物理学家格式硬要求 ★

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍，底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，含至少：生卒、本名、国籍、出生地、去世地、教育、师承、任职、主要荣誉、核心领域。事实取自本地 Wikipedia，不得杜撰。
4. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`（不是 `OpenPhysicist`）；GitHub 链接由首页模板 `\input` 继承，子 deck 不重复；引号用半角 `" "`。

---

## 第 6 步：规划幻灯片序列 【人物专属，可微调】

洛伦兹的一生是一条主线：**从电子论到相对论前夜，再到世界物理学界的领航者**。建议 17 页：

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 顶部标签「20 世纪物理学 · 电子论与相对论」/ Hendrik Lorentz 1853–1928 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 主标题「亨德里克·洛伦兹 - 从阿纳姆到世界物理学领航者」+ 左头像 + 右 2×2 信息网格
03  核心贡献概览 — 电子论 / 电动力学 / 相对论 / 磁光学
04  早年：阿纳姆与莱顿 (1853–1875) — 荷兰第二个黄金时代、HBS 优等生、Kaiser 引导、博士论文修正麦克斯韦理论
05  莱顿教席 (1878) — 25 岁获理论物理教席、就职演说、分子理论
06  电子论：原子与光 (1892–1895) — 带电粒子振荡产生光、洛伦兹力、局域时间
07  洛伦兹变换 (1899–1904) — 长度收缩、时间膨胀、洛伦兹-菲茨杰拉德收缩、迈克耳孙-莫雷实验
08  塞曼效应与 1902 诺奖 — Zeeman 实验 + Lorentz 理论解释
09  相对论前夜 (1905) — Einstein 狭义相对论、Lorentz 的以太论立场、Lorentz–Einstein theory 混淆
10  与 Einstein 的关系 — 邀请继任教席被拒、深厚友谊、"我一生最敬重之人"
11  首届索尔维会议 (1911) — 主席、新旧物理交汇
12  泰勒博物馆与周一晨课 (1912–1928) — 辞教席、Curator、讲学不辍
13  理论物理做工程：须德海大坝 (1918–1926) — 人肉计算机数值求解、惊人准确的预测
14  门生与传承 — Zeeman、Fokker、Ornstein、长女 Geertruida
15  荣誉与纪念 — Copley、Franklin、Pour le Mérite、洛伦兹奖章
16  遗产 — 从电子论到相对论，经典物理的集大成者
17  结尾
```

---

## 第 7 步：编写 Beamer 源码 【模板通用】

- 文件名：`physicist/presentations/20th_century/Hendrik_Lorentz/Hendrik_Lorentz_zh.tex`
- 每页用 `\newcommand{\xxxslide}{...}` 定义，配色与卡片版式复用标杆实例骨架
- **身份信息页实现模式**（参照 `\profileslide`）：
  - 左：`\IfFileExists{images/Lorentz.jpg}{\includegraphics[width=3.0cm,height=3.9cm,keepaspectratio]{Lorentz.jpg}}{...}` 头像 + 姓名注
  - 右：2×2 信息网格，`infob` 圆角卡片（上排两张 `anchor=north`，下排两张 `anchor=south`）
    - 上排：生卒+本名+国籍 / 师承+任职
    - 下排：出生地+去世地+教育 / 主要荣誉+核心领域
  - 任职务必含 `Leiden · Teylers Museum`，与封面底部状态栏一致；师承栏区分 `Rijke（博士导师）` 与 `Kaiser（学术引路人）`

---

## 第 8 步：布局检查 ★★★ 编译即查

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图肉眼检查溢出/重叠
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标

---

## 第 9 步：史实审查 + 术语审查

### 洛伦兹特殊陷阱（★ 必须逐页扫描）

| 陷阱 | 说明 |
|------|------|
| "洛伦兹变换唯一发现者" | ★ 绝不能说。Joseph Larmor 1897 年已独立使用相同变换（Lorentz 当时不知情）；Poincaré 1905 才命名"洛伦兹变换"。正确表述："推导出（后被 Poincaré 命名为洛伦兹变换）" |
| 狭义相对论的归属 | ★ Lorentz 推导了变换、1904 论文含电动力学协变形式，但**没有完全接受狭义相对论**——始终坚持以太论和"真实时间"。Einstein 1905 才建立狭义相对论。不要写"洛伦兹创立狭义相对论" |
| 以太论立场 | Lorentz 终生相信存在（不可探测的）以太和"真实时间"，与 Einstein 哲学立场根本分歧。不要把他写成"相对论的坚决拥护者"，应写"相对论的前驱/奠基者，但对以太持保守立场" |
| 塞曼效应的归属 | 塞曼效应是 Zeeman 1896 实验发现，Lorentz 提供理论解释。不要写成"洛伦兹发现塞曼效应" |
| 博士导师 | 博士导师是 Pieter Rijke；Frederik Kaiser 是"学术引路人"（天文学家，引导其成为物理学家）。两者勿混淆 |
| 局域时间（local time） | 1892/1895 提出"局域时间"，Poincaré 称为其"最巧妙的构想"。这是洛伦兹变换的数学前身，但当时 Lorentz 未给出物理解释，勿写成"已理解相对论" |
| 长度收缩 | 1892 提出（与 FitzGerald 独立，合称 Lorentz–FitzGerald contraction），目的是解释迈克耳孙-莫雷实验。勿遗漏 FitzGerald 的并行贡献。注意：page.md 正文仅说 Lorentz 1892 提出、未明确提 FitzGerald，但 metadata `notable_work` 含 "Lorentz–FitzGerald contraction" 佐证，Beamer 写"与 FitzGerald 独立"属准确常识 |
| Einstein 继任 | 1910 年 Lorentz 邀 Einstein 继任莱顿教席，Einstein 拒绝（刚赴 ETH），最终选 Ehrenfest。体现二人关系，勿写成"Einstein 继任" |
| 须德海工程 | 1918–1926 主持 Afsluitdijk 拦海大坝水文计算，预测准确，一组水闸以他命名。这是"理论物理做工程"的独特故事，勿遗漏 |
| 葬礼致敬 | 1928-02-10 葬礼，荷兰电报电话停运三分钟致敬；Einstein、Marie Curie 出席。这是其声望的极致体现 |
| 女儿也是物理学家 | 长女 Geertruida de Haas-Lorentz 是物理学家，也是其博士生，嫁 Wander de Haas。勿遗漏这一家学传承 |
| 索尔维会议主席 | 1911 主持首届索尔维会议，勿与"参会者"混淆——他是主席 |
| 国际智力合作委员会 | 1925–1928 任主席（UNESCO 前身），是其晚年国际声望的体现 |
| 门生方程命名（★ 超 page.md） | 门生页写 Fokker"福克-普朗克方程"、Ornstein"Ornstein-Uhlenbeck 过程"——均为准确物理学史常识，但 page.md 仅列其为博士生、未直接记载方程命名。保留可，但属补充常识，若需极致严谨可改为仅列姓名 |
| 洛伦兹奖章年份（★ 超 page.md） | 荣誉页写"1925 年设立、每四年颁发一次"——准确常识，但 page.md 仅在 See also 出现 Lorentz Medal、无年份。保留可，若需极致严谨可删年份 |

### 术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| Lorentz transformation | 洛伦兹变换 | 狭义相对论核心，勿与"洛伦兹力"混淆 |
| Lorentz force | 洛伦兹力 | 带电粒子在电磁场中的受力 |
| Lorentz factor | 洛伦兹因子 | γ = 1/√(1−v²/c²) |
| Lorentz covariance | 洛伦兹协变性 | 物理定律在洛伦兹变换下形式不变 |
| Lorentz ether theory | 洛伦兹以太论 | 相对论出现前的以太理论 |
| Lorentz oscillator model | 洛伦兹振子模型 | 反常色散的经典模型 |
| length contraction | 长度收缩 | 又称 Lorentz–FitzGerald contraction |
| local time | 局域时间 | 洛伦兹变换的数学前身 |
| Zeeman effect | 塞曼效应 | 磁对辐射现象的影响 |
| luminiferous aether | 光以太 | 相对论前假设的光传播介质 |
| electron theory | 电子论 | 洛伦兹核心理论 |
| Michelson–Morley experiment | 迈克耳孙-莫雷实验 | 以太漂移的否定性实验 |
| Solvay Conference | 索尔维会议 | 1911 首届，Lorentz 为主席 |
| Teylers Museum | 泰勒博物馆 | 洛伦兹晚年任职机构 |

### 通用陷阱

| 陷阱类型 | 检查点 |
|---------|--------|
| "第一次/第一个/唯一"断言 | 不说"第一个推导洛伦兹变换"→"推导出（后被 Poincaré 命名）" |
| 相对论归属过度 | 不说"创立狭义相对论"→"为狭义相对论奠定数学基础/相对论前驱" |
| 现代语言包装历史人物 | 不用"参考系变换的群论结构"等现代术语描述 19 世纪末的工作 |

---

## 第 9.5 步：Review 完成后更新名单状态 ★

> **两轮 Review 全部完成后，必须同步更新总名单的「Review」列**，否则名单会一直停留在 🔲。

- 编辑 `physicist/generate_20th_century_list.py`，将洛伦兹姓名加入 `BIOGRAPHIES_DONE`（立传）与 `REVIEWS_DONE`（Review）集合：
  ```python
  BIOGRAPHIES_DONE = {..., "Hendrik Antoon Lorentz"}
  REVIEWS_DONE = {..., "Hendrik Antoon Lorentz"}
  ```
- 重新生成名单：
  ```bash
  cd physicist && python3 generate_20th_century_list.py
  ```
- 校验：名单中洛伦兹行应为 `| ✅ | ✅ |`，统计区「已立传」「已 Review」计数 +1。

---

## 关键参考文件清单

| 文件 | 用途 |
|------|------|
| `physicist/presentations/pages/20th_century/Hendrik_Antoon_Lorentz/page.md` | 本地 Wikipedia 正文（权威事实基准） |
| `physicist/presentations/pages/20th_century/Hendrik_Antoon_Lorentz/metadata.json` | Wikidata 结构化元数据 |
| `physicist/presentations/20th_century/Hendrik_Lorentz/Hendrik_Lorentz.html` | 本地 Wikipedia HTML |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | 模板标杆 Beamer 源码 |
| `physicist/presentations/20th_century/Wilhelm_Rontgen/Wilhelm_Rontgen_zh.tex` | 最近成品参考 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/seed_lorentz_full.py` | 研究领域入库（第 4 步） |
| `MySQL/seed_lorentz_relations.py` | 社会关系入库（第 4.5 步） |

## 背景音乐选择 ✅ 【人物专属】

- **气质**：经典物理的庄严、相对论前夜的深邃、荷兰的沉稳、领航者的从容
- **建议曲目**（精选自 `music_audio/curated_tracks.md`）：
  - **已选定**: **Eternals**（Alex-Productions，宏大深远，契合"为相对论奠基"的深远影响）
  - 备选: Timeless（Alex-Productions，沉稳纪录片，但 Wigner/Wilson 已复用，缺乏辨识度）
  - 未采用: Beethoven · Karajan — Symphony No. 3 "Eroica"（古典庄严，但 562MB 过重，ffmpeg 截取前 119 秒无法体现英雄主题）
- **本地路径**: `music_audio/alex-productions/76-V5T_kW2PH_s-Eternals.wav` → `presentations/20th_century/Hendrik_Lorentz/Eternals.wav`
- **时长**: 与 17 页 × 7 秒 ≈ 119 秒对齐，ffmpeg `-shortest` 自动对齐

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
> **特别提醒**：
> 1. 洛伦兹是"经典物理的集大成者 + 相对论的前驱"，叙事核心是"从电子论到相对论前夜"，勿把他写成相对论的创立者
> 2. 他与 Einstein 的关系是物理学史上最动人的一段——Einstein 称其"一生最敬重之人"，务必体现
> 3. 须德海大坝工程是"理论物理做工程"的绝佳素材，勿遗漏
> 4. 引语必须来自 page.md，不要使用任何无法逐字验证的引语
