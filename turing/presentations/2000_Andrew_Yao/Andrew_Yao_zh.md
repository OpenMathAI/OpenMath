# 图灵奖得主立传提示词（人物实例：Andrew Yao / 姚期智）

> **本文件是 OpenTuring 的「图灵奖得主立传提示词」人物实例**，以 Andrew Chi-Chih Yao（姚期智，2000 图灵奖，计算复杂性、密码学、通信复杂性）为目标人物。
> 格式对标图灵奖侧人物实例 Donald E. Knuth、Leslie Lamport，并融合通用模板 `Turing_Bio_Prompt_Template.md`。
> 凡标注 `【模板通用】` 的部分可原样复用；标注 `【人物专属】` 的部分需按姚期智替换。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenTuring —— 开放图灵奖得主人物史（与 OpenMath 数学家侧、OpenChemist、OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：图灵奖通用模板 `Turing_Bio_Prompt_Template.md` 与标杆实例 Donald E. Knuth、Leslie Lamport。
- **本实例**：Andrew Chi-Chih Yao（姚期智，1946-12-24 生于上海，在世）。
- **设计哲学**：图灵奖得主必须有「身份信息页」（Identity / Bio 速览页），且强调「研究领域」的结构化表达；姚期智的「贡献」主要表现为**理论、模型、协议与复杂性下界**——立传应突出他**用数学的严格性为计算、密码与信息交流建立边界**这一主线。

---

## 二、背景信息 【人物专属】

- **目标得主**：Andrew Chi-Chih Yao（姚期智；1946-12-24 ~ ，截至资料基准日在世）
- **气质关键词**：**理论计算机科学奠基人、Yao's principle 提出者、通信复杂性开创者、安全多方计算与混淆电路先驱、伪随机性理论的复杂性奠基人、首位华人图灵奖得主、物理博士转计算机科学家** —— 2000 图灵奖获奖理由（ACM 官方措辞，已核实）：
  > "in recognition of his fundamental contributions to the theory of computation, including the complexity-based theory of pseudorandom number generation, cryptography, and communication complexity"（表彰他对计算理论的根本性贡献，包括基于复杂性的伪随机数生成理论、密码学与通信复杂性）
- **设计母题**：**用复杂性丈量信息与计算的边界（Measuring Information by Complexity）**。姚期智毕生主题是：把模糊的「安全」「高效交流」「随机性」变成可由最坏情形与概率刻画的数学对象。视觉语言：minimax 博弈、混淆电路、通信矩阵、比特/概率、随机数生成器、安全多方计算（百万富翁问题）、从物理到计算机的跨越。
- **本地 Wikipedia**：
  - 原始 HTML：`turing/pages/2000/Andrew Yao/index.html`（含 infobox + 完整正文）
  - 元数据：`turing/pages/2000/Andrew Yao/metadata.json`（title/url/year/image_count）
  - 头像：`turing/pages/2000/Andrew Yao/images/500px-Andrew_Yao_P1130016_cropped_.jpg`（infobox 肖像，2015 年拍摄，可直接复制）
- **参考模板**：
  - 图灵奖通用模板：`turing/presentations/Turing_Bio_Prompt_Template.md`
  - 图灵奖标杆成品：`turing/presentations/Donald_Knuth/Donald_Knuth_zh.tex`、`turing/presentations/Leslie_Lamport/Leslie_Lamport_zh.tex`
  - 项目首页模板：`turing/presentations/cover/openturing_page.tex`

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「研究领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步）两个数据库步骤，写入 `greatminds` 库（MySQL），与 Beamer 立传并行。

### 第 0 步：核对本地 Wikipedia 页面 【人物专属】

- ✅ 本地数据已就绪：`turing/pages/2000/Andrew Yao/index.html`（含 infobox + 正文）与 `metadata.json`
- ✅ 头像已就绪：`turing/pages/2000/Andrew Yao/images/500px-Andrew_Yao_P1130016_cropped_.jpg`（Wikipedia infobox 肖像，2015 年拍摄）
- 提取 infobox 与正文，输出供校验（**事实基准如下**）：
  - 出生：1946-12-24，上海（当时属中华民国）；现居北京
  - 国籍变迁：中华民国（1946–2015）→ 美国（入籍，?–2015）→ 中华人民共和国（2015 至今，与杨振宁同批放弃美国国籍）
  - 教育：
    - 台北市立建国高级中学
    - 台湾大学物理学士（BS，1967）
    - 哈佛大学物理硕士（MA，1969）、理论物理博士（PhD，1972）
    - 伊利诺伊大学厄巴纳-香槟分校计算机科学博士（PhD，1975，两年完成，NSF Fellow）
  - 博士导师：Sheldon Glashow（哈佛物理，诺贝尔物理学奖得主）、Chung Laung Liu（伊利诺伊 CS）
  - 博士论文：
    - 哈佛物理：_Internal Symmetries and Positivity_
    - 伊利诺伊 CS：_A Study of Concrete Computational Complexity_
  - 任职：
    - MIT 助理教授 1975–1976
    - Stanford 助理教授 1976–1981
    - UC Berkeley 教授 1981–1982
    - Stanford 正教授 1982–1986
    - Princeton William and Edna Macaleer Professor 1986–2004
    - 清华大学高等研究中心（CASTU）教授、理论计算机科学研究中心（ITCS）主任 2004
    - 清华大学交叉信息研究院（IIIS）院长 2010 至今
    - 香港中文大学 Distinguished Professor-at-Large
  - 荣誉：
    - George Pólya Prize 1987
    - Knuth Prize 1996
    - Turing Award 2000（首位华人得主）
    - Kyoto Prize in Advanced Technology 2021
    - Asian Scientist 100 2022
  - 学术身份：美国国家科学院院士、美国艺术与科学院院士、AAAS Fellow、ACM Fellow、中国科学院外籍院士/院士（2015 转为中科院院士）
  - 配偶：Frances Yao（储枫，亦为理论计算机科学家）
  - 已知学生：William A. Dembski
  - 核心贡献：Yao's principle、communication complexity、Dolev–Yao model、garbled circuit、hybrid argument、Yao's Millionaires' Problem、Yao's test、Yao graph
  - 其他：2024 年与 Bengio、Hinton 等共同发表 AI 极端风险专家共识论文

### 第 1 步：建立目录 【模板通用】

- ✅ 已创建 `turing/presentations/Andrew_Yao/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- ✅ 已复制标杆实例 Makefile，并设置 `MAIN=Andrew_Yao_zh`、`VIDEO_NAME=Andrew_Yao_zh`

### 第 3 步：收集图片 【人物专属】

- ✅ 已复制 `turing/pages/2000/Andrew Yao/images/500px-Andrew_Yao_P1130016_cropped_.jpg` 到 `turing/presentations/Andrew_Yao/images/Andrew_Yao.jpg`

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

**姚期智的研究领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | theory of computation | 计算理论 | Yao's principle、复杂性下界、伪随机性、混合论证 | 封面、核心页 |
| 1 | cryptography | 密码学 | 混淆电路、百万富翁问题、Dolev–Yao 模型 | 密码页 |
| 2 | communication complexity | 通信复杂性 | 通信复杂性开创、Yao's test | 通信页 |
| 3 | pseudorandomness | 伪随机性 | 基于复杂性的伪随机数生成理论 | 伪随机页 |

#### 4.1 入库操作

- 新建/更新 `people` 主记录（`name_en='Andrew Yao'`），设置 `primary_occupation='computer scientist'`、`has_biography=1`、`has_social_data=1`
- 关联职业 `computer scientist`（rank 0）、`theoretical physicist`（rank 1，因姚期智本为物理博士）
- 国籍按资料写 `United States` 与 `China`（如字典已有对应国家项；若 `people` 只保存主国籍，则写 `China`）
- 将 4 个领域写入 `person_field`（带 rank），缺失领域先在 `fields` 建字典项
- 生成入库脚本 `MySQL/seed_yao_full.py` 并执行

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

**师长**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Sheldon Glashow | 师→生（哈佛物理博士导师） | 1972 年哈佛理论物理博士导师，1979 年诺贝尔物理学奖得主 |
| advisor-student | Chung Laung Liu | 师→生（伊利诺伊 CS 博士导师） | 1975 年伊利诺伊 CS 博士导师 |

**学生**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | William A. Dembski | 生→师（姚期智→学生） | Wikipedia infobox 所列学生 |

**合作者 / 共同成果**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| collaborator | Danny Dolev | 双向 | Dolev–Yao 模型（密码协议敌手模型） |
| collaborator | Yoshua Bengio | 双向 | 2024 年 AI 极端风险专家共识论文 |
| collaborator | Geoffrey Hinton | 双向 | 2024 年 AI 极端风险专家共识论文 |

**家人**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Frances Yao | 无向 | 妻子（储枫），理论计算机科学家 |

- 将上述关系写入 `person_relation`（`from_id` / `to_id` / `relation_type` / `note` / `source`），`source` 记 `'立传-Andrew_Yao'`
- `advisor-student` 有向：导师为 `from_id`（Glashow→Yao、Liu→Yao），Yao→Dembski；`collaborator` 双向；`spouse` 无向
- 不在库中的关联人物先建占位记录（`has_biography=0`），关系 `note` 加 `[材料待展开] ` 前缀
- 生成入库脚本 `MySQL/seed_yao_relations.py` 并执行

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：理论、精密、跨越物理与计算机
- **配色**：图灵紫（OpenTuring 品牌主色）+ 强调红 + 四分类色
  - `badgeTheory` 计算理论 — 蓝 `#2E5A9E`
  - `badgeCrypto` 密码学 — 琥珀 `#D9A441`
  - `badgeComm` 通信复杂性 — 青绿 `#1E8E8E`
  - `badgePseudo` 伪随机性 — 玫瑰 `#C0395B`
- **背景母题**：稀疏实心圆与连线意象，呼应概率空间、通信矩阵、电路与博弈

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenTuring 项目首页（\input cover/openturing_page.tex）
01  封面 — 姚期智 / Andrew Yao / 2000 图灵奖 + 四色 badge + 右上头像 + 国籍行
02  早年与教育 — 上海出生、香港/台湾成长、建国中学、台湾大学物理 BS
03  身份信息页（★ 必做）— 左头像 + 右信息网格
04  核心贡献概览 — 计算理论 / 密码学 / 通信复杂性 / 伪随机性
05  从物理到计算 — 哈佛物理博士 → UIUC 计算机博士，Glashow / Liu
06  Yao's principle — minimax 原理与随机算法下界
07  通信复杂性 — 定义通信复杂性，衡量分布式计算的信息代价
08  伪随机性 — 基于复杂性的伪随机数生成理论
09  密码学 — 混淆电路、百万富翁问题、Dolev–Yao 模型
10  更多以 Yao 命名的成果 — Yao's test、Yao graph
11  学术生涯 — MIT → Stanford → Berkeley → Princeton
12  清华交叉信息研究院 — CASTU / ITCS / IIIS
13  荣誉 — Turing 2000 · Knuth 1996 · Kyoto 2021 · Pólya 1987
14  遗产 — 首位华人图灵奖得主、理论计算机科学的一代宗师
15  结尾 — 用数学丈量计算与信息的边界
16  彩蛋 — 姚期智的物理导师 Glashow 是 1979 诺贝尔物理学奖得主；妻子 Frances Yao 也是理论计算机科学家
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照通用模板 `\profileslide`。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**姚期智特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 教育时间线 | 姚期智先读物理（台湾大学 BS 1967、哈佛 MA 1969 / PhD 1972），后读计算机（UIUC PhD 1975）；勿写成"只有一个博士" |
| 两个博士导师 | Glashow 是物理博士导师，Liu 是 CS 博士导师，勿混为一个 |
| 图灵奖理由 | 官方措辞强调 pseudorandom number generation、cryptography、communication complexity；LaTeX 与姚期智无关 |
| "首个华人得主" | 姚期智是首位（也是目前唯一）华人图灵奖得主；表述应尊重资料，且不与他人的"华人"定义混淆 |
| 国籍变迁 | 2015 年与杨振宁同批放弃美国国籍并转为中科院院士，勿写成"从未有美国籍" |
| 配偶姓名 | 妻子 Frances Yao，中文名储枫，亦为理论计算机科学家；本地页面只给英文名，勿杜撰更多细节 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| theory of computation | 计算理论 | 与"计算复杂性"关联 |
| computational complexity | 计算复杂性 | 姚期智的核心领域 |
| Yao's principle | 姚氏原理 / minimax 原理 | 保留英文或给出准确中文 |
| communication complexity | 通信复杂性 | 姚期智开创 |
| pseudorandomness | 伪随机性 | 基于复杂性理论 |
| cryptography | 密码学 | 与安全多方计算关联 |
| garbled circuit | 混淆电路 / 乱码电路 | 安全多方计算基础 |
| secure multi-party computation | 安全多方计算 | 姚期智开创性思想 |
| Yao's Millionaires' Problem | 姚氏百万富翁问题 | 保留英文或中文 |
| Dolev–Yao model | Dolev–Yao 模型 | 与 Danny Dolev 共同 |
| hybrid argument | 混合论证 | 伪随机性/密码证明工具 |
| Yao's test | 姚氏测试 | 伪随机性测试 |
| Yao graph | Yao 图 | 计算几何结构 |

---

## 四、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `turing/pages/2000/Andrew Yao/index.html` | 本地 Wikipedia 正文 |
| `turing/pages/2000/Andrew Yao/metadata.json` | 简化元数据 |
| `turing/presentations/Turing_Bio_Prompt_Template.md` | 图灵奖通用模板 |
| `turing/presentations/Donald_Knuth/Donald_Knuth_zh.tex` | 图灵奖标杆成品参考 |
| `turing/presentations/Leslie_Lamport/Leslie_Lamport_zh.tex` | 图灵奖版式参考 |
| `turing/presentations/cover/openturing_page.tex` | 项目首页模板 |
| `turing/turing_award_winners.md` | 图灵奖得主总名单 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
