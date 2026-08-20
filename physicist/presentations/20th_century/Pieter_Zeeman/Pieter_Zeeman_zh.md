# 彼得·塞曼 (Pieter Zeeman) 立传提示词

> 本提示词严格遵循 `physicist` 项目的人物立传规范（`Physicist_Bio_Prompt_Template.md`），并参照物理学家侧标杆 `Hendrik_Lorentz_zh.md`（1902 诺奖系列首个完整范例）与 `Wilhelm_Rontgen_zh.md` 的全面结构，为塞曼制作 Beamer 演示文稿。
> 直接复制本文件内容到新对话中使用。

---

## 背景信息 【人物专属】

- **目标物理学家**: Pieter Zeeman（彼得·塞曼，1865-05-25 ~ 1943-10-09，享年 78 岁）
- **气质关键词**: **实验精神、敏锐观察、塞曼效应发现者、原子结构的揭示者** — "因他们研究磁对辐射现象的影响所作出的杰出贡献"（1902 诺贝尔物理学奖获奖理由，与 Hendrik Lorentz 共享）
- **本地 Wikipedia**:
  - 权威数据源：`physicist/presentations/pages/20th_century/Pieter_Zeeman/page.md`（已含完整 infobox + 正文）
  - 结构化元数据：`physicist/presentations/pages/20th_century/Pieter_Zeeman/metadata.json`
  - 立传目录 HTML：`physicist/presentations/20th_century/Pieter_Zeeman/Pieter_Zeeman.html`
- **参考模板**:
  - 同系列标杆（1902 诺奖）：`physicist/presentations/20th_century/Hendrik_Lorentz/Hendrik_Lorentz_zh.tex`
  - 首例成品：`physicist/presentations/20th_century/Wilhelm_Rontgen/Wilhelm_Rontgen_zh.tex`
  - 通用模板：`physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md`
- **后续配套数据库脚本**（见第 4 步 / 第 4.5 步）：
  - `MySQL/seed_zeeman_full.py` — 人物主记录 + 研究领域入库（`person_field`）
  - `MySQL/seed_zeeman_relations.py` — 社会关系入库（`person_relation`）

---

## 你的任务

按照本提示词的步骤依次完成。**每完成一步向我汇报进度**，遇到歧义时先征求我的意见再继续。

> **数据库同步要求**：本提示词包含「研究领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步）两个数据库步骤。请严格按步骤操作，将塞曼的**研究领域**与**社会关系**写入 `greatminds` 数据库（MySQL），这是 OpenPhysicist 项目人物关系网络的一部分，与 Beamer 立传并行。

---

## 第 0 步：确认 Wikipedia 页面已就绪

- 读取本地 Wikipedia `page.md`、`metadata.json` 的 infobox 与正文
- 输出供校验的信息（事实基准如下）：

  - **生卒日期**：1865-05-25 生于荷兰宗内迈尔（Zonnemaire）～ 1943-10-09 逝于荷兰阿姆斯特丹（Amsterdam），享年 78 岁
  - **国籍**：荷兰（Kingdom of the Netherlands），荷兰"第二个黄金时代"实验物理的代表人物
  - **父母**：父 Catharinus Forandinus Zeeman，荷兰归正教会（Dutch Reformed Church）牧师；母 Willemina Worst
  - **教育**：泽里茨（Zierikzee）高中；1883 年赴代尔夫特（Delft）补古典语言；1885 年入莱顿大学；1893 年获博士学位
  - **博士导师**：Heike Kamerlingh Onnes（海克·卡末林·昂内斯）；**学术引路人**：Hendrik Lorentz（其他学术顾问）
  - **博士论文**：1893《Metingen over het verschijnsel van Kerr...》（论克尔效应——偏振光在磁化表面的反射）
  - **主要任职机构**：
    - 1890 莱顿大学 Lorentz 助手
    - 1895 莱顿大学 Privatdozent（编外讲师，数学与物理）
    - 1896 秋 阿姆斯特丹大学讲师
    - 1900 阿姆斯特丹大学物理教授
    - 1908 接替 Johannes van der Waals 任正教授兼物理研究所所长
    - 1935 退休
  - **关键荣誉**：诺贝尔物理学奖 1902（与 Lorentz 共享）；Matteucci Medal 1912；Henry Draper Medal 1921；Rumford Medal 1922；Franklin Medal 1925
  - **家庭**：1895 与 Johanna Elisabeth Lebret 结婚，育三女一子
  - **核心贡献**（metadata `notable_work` 仅 1 项，但极具分量）：
    - Zeeman effect（塞曼效应）—— 光谱线在强磁场中分裂
  - **关键时间线**（20 个节点）：
    1. 1865-05-25 生于荷兰宗内迈尔，父亲是归正教会牧师
    2. 1883 极光在荷兰可见，还是高中生的他画图并投稿 Nature 发表
    3. 1883 高中毕业后赴代尔夫特补古典语言（大学入学要求）
    4. 代尔夫特期间首次遇见 Kamerlingh Onnes
    5. 1885 入莱顿大学，师从 Kamerlingh Onnes 与 Lorentz
    6. 1890 成为 Lorentz 助手，参与克尔效应研究
    7. 1893 博士论文（克尔效应）
    8. 博士毕业后赴斯特拉斯堡 Kohlrausch 研究所半年
    9. 1895 回莱顿任 Privatdozent
    10. 1896 发现塞曼效应（搬去阿姆斯特丹前不久）
    11. 1896-10-31 周六，Kamerlingh Onnes 在荷兰皇家科学院会议通报其观测结果
    12. 下周一，Lorentz 召见并给出基于电子论的理论解释
    13. 1896 秋 赴阿姆斯特丹大学任讲师
    14. 1900 升教授
    15. 1902 与 Lorentz 共享诺贝尔物理学奖
    16. 1908 接替 van der Waals 任正教授兼物理研究所所长
    17. 1918 发表等效原理实验验证（引力质量与惯性质量之比）
    18. 1923 阿姆斯特丹新建实验室（1940 更名 Zeeman 实验室）
    19. 1935 退休
    20. 1943-10-09 逝于阿姆斯特丹，葬于哈勒姆（Haarlem）

### 人格特质线索（源自 Wikipedia 原文）

- **少年的科学天赋**：1883 年还是高中生时，泽里茨高中学生 Zeeman 就绘制并描述了可见的极光，投稿给《Nature》并获发表。编辑称赞"来自宗内迈尔天文台的 Zeeman 教授的仔细观测"——误称其为"教授"，实为高中生
- **敏锐的实验观察**：发现光谱线在强磁场中分裂，这一发现后来成为揭示原子结构的钥匙，其重要性远超实验现象本身
- **实验与理论的完美配合**：塞曼效应是"实验发现（Zeeman）+ 理论解释（Lorentz）"的典范，二人共享诺奖

### 与其他已立传物理学家的关系网络

- **Hendrik Lorentz** — 学术引路人（other academic advisors）兼 1902 共享诺奖的理论解释者。塞曼是 Lorentz 的"其他知名学生"（other notable students）；Lorentz 在 1896-10-31 次日（下周一）就给出塞曼效应的理论解释。两人是理论与实验印证关系的典范
- **Heike Kamerlingh Onnes** — 博士导师；1896 年在科学院会议通报塞曼的观测结果（"communicated by Heike Kamerlingh Onnes"）
- **Albert Einstein** — 同事；circa 1920 年 Einstein 到访阿姆斯特丹，与 Ehrenfest 合影
- **Paul Ehrenfest** — 同事；与 Einstein 一同到访
- **Johannes van der Waals** — 1908 年接替其任正教授兼物理研究所所长
- **J. J. Thomson** — 无直接师承，但塞曼效应在 Thomson 1897 年发现电子之前，就揭示了发光粒子带负电、比氢原子轻千倍——塞曼效应是电子发现的前奏

---

## 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/20th_century/` 下创建 `Pieter_Zeeman/` 子目录与 `images/`

---

## 第 2 步：复制 Makefile 【模板通用】

- 复制标杆实例 `Hendrik_Lorentz/Makefile` 或 `Wilhelm_Rontgen/Makefile`，设置 `MAIN=Pieter_Zeeman_zh`、`VIDEO_NAME=Pieter_Zeeman_zh`

---

## 第 3 步：收集图片 【人物专属】

- 从 Wikipedia 下载塞曼肖像照到 `images/Zeeman.jpg`：
  - 首选：Jan Veth 1925 年所作塞曼肖像画（"Portrait of Pieter Zeeman by Jan Veth, 1925"）
  - 备选：1929 年 Georges Chevalier 的 Autochrome 彩色照片
- 可选补充：
  1. 塞曼效应光谱分裂照片（"A photo Zeeman took of the Zeeman effect"）
  2. Einstein 到访阿姆斯特丹合影（"Einstein visiting Pieter Zeeman in Amsterdam, accompanied by Paul Ehrenfest, circa 1920"）
- 优先真实感与学术气质，不做刻意美化

---

## 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

> **目的**：把研究领域变成可检索、可图形化的结构化字段（`fields` + `person_field` 表）。

### 4.1 塞曼的研究领域（按重要性 rank 排序）

| rank | 领域（name_en） | 中文 | 说明 | 对应 Beamer 页 |
|:--:|------|------|------|------|
| 0 | Zeeman effect | 塞曼效应 | 光谱线在磁场中分裂，核心贡献 | 封面、核心页 |
| 1 | magneto-optics | 磁光学 | 磁光克尔效应、光在运动介质中的传播 | 核心页 |
| 2 | spectroscopy | 光谱学 | 光谱线分析、原子结构 | 核心页 |
| 3 | atomic physics | 原子物理 | 塞曼效应揭示原子结构 | 意义页 |

> 领域字典 `fields` 表：`physics`、`magnetism` 等可能已存在，缺失的 `Zeeman effect`/`magneto-optics`/`spectroscopy`/`atomic physics` 由 `seed_zeeman_full.py` 自动补建。

### 4.2 入库操作（见 `MySQL/seed_zeeman_full.py`）

- 新建 `people` 主记录：`name_en='Pieter Zeeman'`、`name_zh='彼得·塞曼'`、`primary_occupation='physicist'`、`has_biography=1`、`has_social_data=1`，qid=`Q79000`
- 关联职业 `physicist`（rank 0），国籍 `Netherlands`（荷兰）
- 将 4 个领域写入 `person_field`（带 rank），缺失领域先在 `fields` 建字典项
- 执行后校验：
  ```sql
  SELECT f.name_en, pf.rank FROM person_field pf
  JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=<id> ORDER BY pf.rank;
  ```

---

## 第 4.5 步：社会关系梳理 + 数据库入库 ★（数据库同步）

> **目的**：将塞曼的师承、合作、门生、家庭与科学影响写入 `person_relation`，形成可查询的人物关系网络。

### 4.5.1 关系清单（从 Wikipedia 提取）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Heike Kamerlingh Onnes | 师→生（博士导师） | 莱顿大学博士导师 |
| advisor-student | Hendrik Lorentz | 师→生（其他学术顾问） | 塞曼是 Lorentz 的"其他知名学生" |
| colleague | Albert Einstein | 无向 | circa 1920 到访阿姆斯特丹 |
| colleague | Paul Ehrenfest | 无向 | 同事，与 Einstein 一同到访 |
| colleague | Johannes van der Waals | 无向 | 1908 接替其任正教授兼所长 |
| co-honored | Hendrik Lorentz | 无向 | 1902 诺贝尔物理学奖共同得主 |
| spouse | Johanna Elisabeth Lebret | 无向（夫妻） | 妻子，1895 结婚 |

> 关系类型键取自 `relation_types`：`advisor-student` / `colleague` / `co-honored` / `spouse`。

### 4.5.2 入库操作（见 `MySQL/seed_zeeman_relations.py`）

- 连接 `greatminds` 库，以 `name_en='Pieter Zeeman'` 为中心
- 库中已存在人物优先复用（如 Lorentz、Einstein、Ehrenfest 可能已在库），不在库的先建占位（`has_biography=0`），关系 note 加 `[材料待展开] ` 前缀
- 有向关系 advisor-student 按师→生；无向（colleague/co-honored/spouse）按 `MIN(id)→MAX(id)` 存储
- 执行后校验并汇报：新建 X 人（占位）、新增 Y 条关系

---

## 第 5 步：设计配色方案 【人物专属】

- **气质**：实验的冷静、光谱的绚烂、敏锐观察、塞曼效应的揭示力
- **建议配色**：深松绿（光谱的冷静实验精神）+ 香槟金（诺奖，与 Lorentz 保持 1902 系列统一）+ 四个分类色
  - `badgeZeeman` 塞曼效应 — 深松绿 `#1B4D3E`
  - `badgeMagneto` 磁光学 — 深靛蓝 `#1A237E`
  - `badgeSpectro` 光谱学 — 琥珀 `#E07B30`
  - `badgeAtom` 原子物理 — 玫瑰 `#C4204F`
- **背景母题**：光谱分裂线条——柔和细线从一点向两侧扩散，呼应"光谱线在磁场中分裂"的核心意象
- **注意与已有立传区分**：Röntgen 用深黑蓝+香槟金、Lorentz 用深普鲁士蓝+荷兰橙，塞曼应选用可辨识的深松绿+香槟金主调

### 5.1 物理学家格式硬要求 ★

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍，底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，含至少：生卒、本名、国籍、出生地、去世地、教育、师承、任职、主要荣誉、核心领域。事实取自本地 Wikipedia，不得杜撰。
4. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`（不是 `OpenPhysicist`）；GitHub 链接由首页模板 `\input` 继承，子 deck 不重复；引号用半角 `" "`。

---

## 第 6 步：规划幻灯片序列 【人物专属，可微调】

塞曼的一生是一条主线：**从牧师之子的极光投稿，到发现光谱线在磁场中分裂，再到揭示原子结构的前奏**。建议 17 页：

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 顶部标签「20 世纪物理学 · 磁光学与原子结构」/ Pieter Zeeman 1865–1943 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 主标题「彼得·塞曼 - 塞曼效应的发现者」+ 左头像 + 右 2×2 信息网格
03  核心贡献概览 — 塞曼效应 / 磁光学 / 光谱学 / 原子物理
04  早年：宗内迈尔的牧师之子 (1865–1883) — 荷兰归正教会牧师家庭、泽里茨高中
05  极光与 Nature：少年的科学天赋 (1883) — 高中生投稿 Nature 发表、被误称"教授"
06  莱顿岁月：Kamerlingh Onnes 与 Lorentz 门下 (1885–1893) — 师从两位巨匠、Lorentz 助手
07  博士论文：克尔效应 (1893) — 偏振光在磁化表面的反射
08  发现塞曼效应 (1896) — 光谱线在强磁场中分裂
09  Lorentz 的理论解释：下周一的故事 — 周六通报、下周一解释，实验与理论印证
10  塞曼效应的意义：电子论的前奏 — 在 Thomson 发现电子之前揭示发光粒子带负电、比氢原子轻千倍
11  1902 诺奖（与 Lorentz 共享） — "因他们研究磁对辐射现象的影响所作出的杰出贡献"
12  Amsterdam 生涯：从讲师到所长 (1896–1935) — 1900 教授、1908 接替 van der Waals
13  等效原理验证 (1918) — 引力质量与惯性质量之比
14  门生与传承 — 博士生 Cornelis Bakker 等
15  荣誉与纪念 — Matteucci、Henry Draper、Rumford、Franklin、Zeeman 实验室
16  遗产 — 从塞曼效应到原子结构的揭示
17  结尾
```

---

## 第 7 步：编写 Beamer 源码 【模板通用】

- 文件名：`physicist/presentations/20th_century/Pieter_Zeeman/Pieter_Zeeman_zh.tex`
- 每页用 `\newcommand{\xxxslide}{...}` 定义，配色与卡片版式复用标杆实例骨架
- **身份信息页实现模式**（参照 `\profileslide`）：
  - 左：`\IfFileExists{images/Zeeman.jpg}{\includegraphics[width=3.0cm,height=3.9cm,keepaspectratio]{Zeeman.jpg}}{...}` 头像 + 姓名注
  - 右：2×2 信息网格，`infob` 圆角卡片（上排两张 `anchor=north`，下排两张 `anchor=south`）
    - 上排：生卒+本名+国籍 / 师承+任职
    - 下排：出生地+去世地+教育 / 主要荣誉+核心领域
  - 任职务必含 `Leiden · Amsterdam`，与封面底部状态栏一致；师承栏区分 `Kamerlingh Onnes（博士导师）` 与 `Lorentz（学术引路人）`

---

## 第 8 步：布局检查 ★★★ 编译即查

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图肉眼检查溢出/重叠
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标

---

## 第 9 步：史实审查 + 术语审查

### 塞曼特殊陷阱（★ 必须逐页扫描）

| 陷阱 | 说明 |
|------|------|
| "Lorentz 发现塞曼效应" | ★ 绝不能说。塞曼效应是 Zeeman 1896 实验发现，Lorentz 提供理论解释。不要写成"Lorentz 发现"或"二人共同发现" |
| 博士导师 | 博士导师是 Heike Kamerlingh Onnes，不是 Lorentz。Lorentz 是"其他学术顾问"（other academic advisors）。两者勿混淆 |
| 塞曼效应的意义 | 在 J.J. Thomson 1897 年发现电子**之前**，塞曼效应就揭示了发光粒子带负电、比氢原子轻千倍——这是电子发现的前奏。勿遗漏这个时间先后 |
| Nature 投稿细节 | 1883 年还是高中生投稿 Nature 获发表，编辑误称其为"Professor Zeeman from his observatory in Zonnemaire"（教授）。这是一个既可爱又有力的细节，可保留"被误称教授"的幽默 |
| 发现日期细节 | 1896-10-31 周六 Kamerlingh Onnes 在科学院会议通报结果；下周一 Lorentz 召见并解释。这个"下周一"的细节体现理论与实验的快速印证 |
| 任职时间 | 1900 升教授，1908 接替 van der Waals 任正教授兼物理研究所所长。勿把 1900 和 1908 混淆 |
| 等效原理验证 | 1918 发表的是"等效原理的实验验证"（引力质量与惯性质量之比），不是"发现等效原理"（那是 Einstein 广义相对论的内容）。勿写成"发现等效原理" |
| 去世地 | 逝于阿姆斯特丹，葬于哈勒姆（Haarlem）。勿把两地混淆 |
| Zeeman 实验室 | 1923 年新建实验室，1940 年才更名 Zeeman 实验室。勿写"1923 年更名" |
| 博士论文主题 | 博士论文是关于克尔效应（Kerr effect），不是塞曼效应。塞曼效应是 1896 年才发现的 |

### 术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| Zeeman effect | 塞曼效应 | 光谱线在磁场中分裂 |
| magneto-optic effect | 磁光效应 | 磁场对光的效应 |
| Kerr effect | 克尔效应（磁光克尔效应） | 偏振光在磁化表面反射 |
| spectral line | 光谱线 | — |
| spectral splitting | 光谱分裂 | 塞曼效应的核心现象 |
| magnetic field | 磁场 | — |
| polarization | 偏振 | 光的偏振 |
| equivalence principle | 等效原理 | 引力质量与惯性质量等价 |
| mass spectrometry | 质谱 | 塞曼后期研究兴趣 |
| Privatdozent | 编外讲师 | 保留德文 |
| polarised light | 偏振光 | — |

### 通用陷阱

| 陷阱类型 | 检查点 |
|---------|--------|
| "第一次/第一个/唯一"断言 | 不说"第一个发现光谱分裂"→"发现光谱线在磁场中分裂" |
| 归属过度 | 不说"塞曼创立电子论"→"塞曼效应为电子论提供实验证据" |
| 现代语言包装历史人物 | 不用"量子化的电子自旋"等现代术语描述 19 世纪末的工作 |

---

## 第 9.5 步：Review 完成后更新名单状态 ★

> **两轮 Review 全部完成后，必须同步更新总名单的「Review」列**，否则名单会一直停留在 🔲。

- 编辑 `physicist/generate_20th_century_list.py`，将塞曼姓名加入 `BIOGRAPHIES_DONE`（立传）与 `REVIEWS_DONE`（Review）集合：
  ```python
  BIOGRAPHIES_DONE = {..., "Pieter Zeeman"}
  REVIEWS_DONE = {..., "Pieter Zeeman"}
  ```
- 重新生成名单：
  ```bash
  cd physicist && python3 generate_20th_century_list.py
  ```
- 校验：名单中塞曼行应为 `| ✅ | ✅ |`，统计区「已立传」「已 Review」计数 +1。

---

## 关键参考文件清单

| 文件 | 用途 |
|------|------|
| `physicist/presentations/pages/20th_century/Pieter_Zeeman/page.md` | 本地 Wikipedia 正文（权威事实基准） |
| `physicist/presentations/pages/20th_century/Pieter_Zeeman/metadata.json` | Wikidata 结构化元数据 |
| `physicist/presentations/20th_century/Pieter_Zeeman/Pieter_Zeeman.html` | 本地 Wikipedia HTML |
| `physicist/presentations/20th_century/Hendrik_Lorentz/Hendrik_Lorentz_zh.tex` | 同系列标杆 Beamer 源码 |
| `physicist/presentations/20th_century/Wilhelm_Rontgen/Wilhelm_Rontgen_zh.tex` | 首例成品参考 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/seed_zeeman_full.py` | 研究领域入库（第 4 步） |
| `MySQL/seed_zeeman_relations.py` | 社会关系入库（第 4.5 步） |

## 背景音乐选择 ✅ 【人物专属】

- **气质**：实验的冷静、光谱的绚烂、敏锐观察、揭示原子结构的庄严
- **建议曲目**（精选自 `music_audio/curated_tracks.md`）：
  - **首选**: The Flow of Time（Alex-Productions，时间感纪录片，契合"光谱线分裂→原子结构揭示"的科学史叙事）
  - **备选**: SEA（Alex-Productions，流动平稳，契合光谱的流动感）
  - **备选**: Daylight（Alex-Productions，明亮轻快，契合"少年投稿 Nature"的朝气）
- **本地路径**: `music_audio/` 下选定曲目 → `presentations/20th_century/Pieter_Zeeman/`
- **时长**: 与 17 页 × 7 秒 ≈ 119 秒对齐，ffmpeg `-shortest` 自动对齐

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
> **特别提醒**：
> 1. 塞曼是实验物理学家，叙事核心是"敏锐的实验观察 → 光谱线分裂 → 原子结构的揭示"，勿把他写成理论家
> 2. 他与 Lorentz 的关系是"实验发现（Zeeman）+ 理论解释（Lorentz）"的典范，1902 共享诺奖，务必体现
> 3. "1883 年高中生投稿 Nature 被误称教授"是一个既可爱又有力的细节，可保留
> 4. 塞曼效应在 Thomson 发现电子之前就揭示了发光粒子带负电、比氢原子轻千倍——这是电子发现的前奏，务必体现这个时间先后
> 5. 引语必须来自 page.md，不要使用任何无法逐字验证的引语
