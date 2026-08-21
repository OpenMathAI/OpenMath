# Wolfgang Pauli（沃尔夫冈·泡利）立传提示词

> 榜单：1945 诺贝尔物理学奖 · qid=Q65989 · 1900-04-25 – 1958-12-15 · 奥地利理论物理学家、量子力学先驱
> 本地 Wikipedia 数据源：`physicist/presentations/pages/20th_century/Wolfgang_Pauli/`（page.md + metadata.json，已下载）

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **标杆实例**：`20th_century/Kenneth_G_Wilson/`（完整成品，可对照）。
- **本实例**：Wolfgang Pauli（沃尔夫冈·泡利，全名 Wolfgang Ernst Pauli）。
- **设计哲学**：物理学家立传必须保留「身份信息页」（Identity / Bio 速览页）与「研究领域」的结构化表达——这是物理学家模板的骨架，务必保留。

## 二、背景信息【人物专属】

- **全名**：Wolfgang Ernst Pauli（沃尔夫冈·恩斯特·泡利）
- **生卒**：1900-04-25 生于维也纳（奥匈帝国）→ 1958-12-15 逝于苏黎世，享年 58
- **国籍（变迁）**：奥地利 → 美国（1946 入籍）→ 瑞士（1949 入籍）
- **身份**：奥地利理论物理学家、量子力学先驱、"物理学的良心"
- **气质关键词**：**量子力学的良心、不相容原理的发现者、中微子的预言者、爱因斯坦的精神继承者** —— 1945 诺贝尔物理学奖获奖理由：
  > "for the discovery of the Exclusion Principle, also called the Pauli Principle."（因发现不相容原理，也称泡利原理）
- **设计母题**：**不相容性 / 排他性（exclusion）**。泡利不相容原理是"没有两个电子能处于完全相同的量子态"——「排他 / 唯一 / 区分」是其物理思想的灵魂，比"粒子"更贴合泡利的视觉语言；辅以"自旋"的二元性（±1/2）与"泡利效应"的神秘气质。
- **本地 Wikipedia**：`physicist/presentations/pages/20th_century/Wolfgang_Pauli/page.md`（第 0 步已下载）
- **参考模板**：
  - 物理学家标杆：`20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

## 三、任务流程【模板通用，逐步执行】

> 每完成一步汇报进度，遇到歧义先征求用户意见再继续。
> **数据库同步要求**：第 4 步（研究领域入库）与第 4.5 步（社会关系入库）写入 `greatminds` 库（MySQL），与 Beamer 立传并行。

### 第 0 步：下载并核对 Wikipedia 页面【人物专属】

- ✅ 已下载到 `pages/20th_century/Wolfgang_Pauli/`（page.md 41.1KB / metadata.json / images.txt）
- 事实基准（已从本地 page.md + metadata.json 提取核对）：
  - 生卒：1900-04-25 生于维也纳 → 1958-12-15 逝于苏黎世，享年 58（胰腺癌，病逝于苏黎世 Rotkreuz 医院 137 号病房）
  - 国籍：奥地利 → 美国（1946 入籍）→ 瑞士（1949 入籍）
  - 父母：父 Wolfgang Josef Pauli（né Pascheles）；母 Bertha Camilla Schütz
  - 教父：物理学家 Ernst Mach（中间名 Ernst 即为纪念教父）
  - 妹妹：Hertha Pauli（作家、演员）
  - 教育：维也纳 Döblinger-Gymnasium（1918 以优等毕业）→ LMU 慕尼黑（1921 博士，Sommerfeld 门下）
  - 博士论文：《Über das Modell des Wasserstoffmolekülions》（关于氢分子离子模型，1921）
  - 博士导师：Arnold Sommerfeld；哥廷根任 Max Born 助手一年，后赴哥本哈根（Bohr）一年
  - 任职：汉堡大学讲师(1923–1928) → ETH Zurich 理论物理教授(1928) → 1935 普林斯顿 IAS 访问教授 → 1940 移居美国任 IAS 教授 → 1946 回苏黎世
  - 关键荣誉：Lorentz Medal 1931、Nobel 1945（爱因斯坦提名）、Franklin Medal 1952、Matteucci Medal 1956、Max Planck Medal 1958；1953 皇家学会外籍会员
  - 婚姻：Käthe Deppner（1929，一年内离异）、Franziska "Franca" Bertram（1934）
  - 核心贡献清单（见第 4 步）
  - 关键时间线（15–20 个节点）

### 第 1 步：建立目录【模板通用】

- 在 `physicist/presentations/20th_century/` 下创建 `Wolfgang_Pauli/` 与 `images/`。

### 第 2 步：复制 Makefile【模板通用】

- 复制 `Kenneth_G_Wilson/Makefile`，设置 `MAIN=Wolfgang_Pauli_zh`、`VIDEO_NAME=Wolfgang_Pauli_zh`。

### 第 3 步：收集图片【人物专属】

- 下载 Wikipedia 肖像：`images/Pauli.jpg`（infobox 用 "Pauli in 1945" 照片；`images.txt` 中备选：1924 年 `Wolfgang_Pauli.jpg`、1929 年讲课照 `Wolfgang_Pauli_young.jpg`、1953 年 `Wolfgang_Pauli_1953.png`）。

### 第 4 步：研究领域梳理 + 入库【模板通用，人物专属内容】

**泡利的研究领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | quantum mechanics / Pauli exclusion principle | 量子力学 / 不相容原理 | 泡利不相容原理(1925)、泡利矩阵、泡利方程 | 封面、核心页 |
| 1 | spin theory | 自旋理论 | 1924 两值量子数、非相对论自旋、泡利顺磁性 | 核心页 |
| 2 | neutrino physics | 中微子物理 | 1930 预言中微子、1956 证实 | 专属页 |
| 3 | quantum field theory | 量子场论 | 自旋统计定理(1940)、Pauli–Villars 正则化(1949) | 专属页 |

### 第 4.5 步：社会关系梳理 + 入库【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Arnold Sommerfeld | 师→生（博士导师） | 慕尼黑博士导师，原子模型先驱 |
| advisor-student | Max Born | 师→生（学术导师） | 哥廷根任其助手一年 |
| colleague | Niels Bohr | 无向 | 哥本哈根一年，Aufbau 原理合作 |
| colleague | Werner Heisenberg | 无向 | 挚友，晚年因统一场论决裂 |
| colleague | Albert Einstein | 无向 | 爱因斯坦称其为"精神继承者"，提名诺奖 |
| colleague | Carl Gustav Jung | 无向 | 心理治疗师兼合作者，共探共时性 |
| co-honored | （无共同得主，1945 独享诺奖） | — | — |
| spouse | Käthe Deppner | 无向 | 1929，一年内离异 |
| spouse | Franziska Bertram | 无向 | 1934–1958 |

**门生**（metadata `doctoral_student`）：Charles Enz、Max Robert Schafroth、Felix Villars（"other notable students"）等 17 人。

### 第 5 步：设计配色方案【人物专属】

- **气质**：严谨、深刻、批判、带神秘色彩（量子力学深度 + 荣格对话）。
- **配色**：深紫罗兰（量子力学深度 + 心理神秘气质）+ 香槟金（诺奖）+ 四分类色
  - `badgeExclusion` 不相容原理 — 靛蓝 `#4C5FD5`
  - `badgeSpin` 自旋理论 — 青绿 `#0E7C7B`
  - `badgeNeutrino` 中微子物理 — 琥珀 `#E07B30`
  - `badgeQFT` 量子场论 — 玫瑰 `#C4204F`
- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「排他性 / 自旋二元性 / 不相容」的视觉语言。

### 5.1 物理学家格式硬要求【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍，底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、去世地、教育、师承、任职、主要荣誉、核心领域。事实取自本地 Wikipedia infobox，不得杜撰。
4. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；GitHub 链接由首页模板 `\input` 继承；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 量子力学的良心 / 泡利 1900–1958 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格
03  核心贡献概览 — 不相容原理 / 自旋理论 / 中微子 / 量子场论
04  早年与教育 (1900–1921) — 维也纳出生、神童、Sommerfeld 门下、237 页相对论综述
05  泡利不相容原理 (1925) — 四个量子数、电子壳层结构
06  自旋理论 (1924–1927) — 两值量子数、泡利矩阵、泡利方程
07  中微子预言 (1930) — "亲爱的放射性女士们先生们"、β 衰变、1956 证实
08  量子场论贡献 (1940–1949) — 自旋统计定理、Pauli–Villars 正则化
09  物理学的良心 — "not even wrong"、Pauli effect、与 Heisenberg 决裂
10  与荣格的对话 — 共时性、Pauli–Jung 猜想、137 执念
11  荣誉与晚年 — 诺贝尔奖、Max Planck 奖章、137 病房
12  结尾
```

### 第 7 步：编写 Beamer 源码【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照标杆 `\profileslide`。
- 头部宏定义（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle` / `\lab` / `\infob`）整体复用 `Physicist_Bio_Prompt_Template.md` 第四章骨架。

### 第 8 步：布局检查【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查【人物专属】

**泡利特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 不相容原理归属 | 1924 泡利提出"两值量子数"，1925 才系统表述为不相容原理；**自旋思想源于 Ralph Kronig**，Uhlenbeck & Goudsmit 一年后才认定为电子自旋，泡利一度拒绝相信，勿写"泡利发明自旋" |
| 诺奖理由 | 1945 获奖，官方措辞针对"发现不相容原理"，**不是**因中微子预言获奖，勿混淆 |
| 中微子命名 | 泡利 1930 提议粒子，**"neutrino"一词由 Fermi 1934 命名**（意大利语"小中性粒子"），勿写"泡利命名中微子" |
| 博士导师 | metadata `doctoral_advisor` 为 Arnold Sommerfeld；Max Born 是哥廷根助手期间的导师，Fermi 无师徒关系，勿混淆 |
| 国籍变迁 | 奥地利 → 美国(1946) → 瑞士(1949)，时间线精确 |
| 与 Wolfgang Paul 混淆 | 泡利(Pauli)与 Wolfgang Paul（离子阱、1989 诺奖得主）不是同一人，Paul 戏称 Pauli 是自己的"虚部" |
| 自旋统计定理 | 1940 泡利"重新推导"，初证源于 Markus Fierz 1939，勿写"泡利独自首次证明" |
| 与 Heisenberg 决裂 | 因 1958 统一场论新闻稿称泡利为"Heisenberg 的助手"而决裂，非因学术分歧本身 |
| 137 病房 | 泡利毕生执念精细结构常数 ≈ 1/137，逝世病房号恰为 137——可作结尾素材，勿写"泡利预言了 137" |
| 独享诺奖 | 1945 泡利**独享**诺奖（非共同得主），勿写"与他人共同获奖" |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Pauli exclusion principle | 泡利不相容原理 | 又称泡利原理，勿译"排除原理" |
| spin | 自旋 | 内禀角动量，勿与宏观旋转混淆 |
| Pauli matrices | 泡利矩阵 | 2×2 自旋算符基，勿译"泡利母体" |
| Pauli equation | 泡利方程 | 非相对论含自旋的薛定谔方程 |
| neutrino | 中微子 | Fermi 命名，泡利预言 |
| spin-statistics theorem | 自旋统计定理 | 费米子/玻色子分类 |
| Pauli–Villars regularization | 泡利-维拉斯正则化 | 与 Felix Villars 合作 |
| Pauli paramagnetism | 泡利顺磁性 | 金属自由电子 |
| Pauli effect | 泡利效应 | 轶事性"仪器破坏"能力 |
| not even wrong | 并非甚至错误 | 泡利名言，指不可证伪的理论 |
| synchronicity | 共时性 | 与荣格合作的概念 |

## 四、背景音乐选择【人物专属】

- **气质**：深刻、批判、神秘（量子力学良心 + 荣格对话 + 58 岁早逝的悲剧底色）。
- **首选曲目**：**Timeless** — Alex-Productions（沉稳/纪录片/长期纲领）
  - 理由：泡利是量子力学奠基人之一，不相容原理与自旋贯穿整个现代物理——与 Timeless 的"永恒/纲领"气质匹配；泡利气质深沉内敛、批判犀利，非宏大征服。
- **备选**：
  - PAST — "历史感/深沉"，匹配从维也纳到苏黎世、跨越两次世界大战的物理史
  - Eternals — "宏大/深远"，匹配量子力学奠基、中微子预言等基础理论贡献
- **本地路径**：`music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav` → `20th_century/Wolfgang_Pauli/Timeless.wav`
- **时长**：128 秒 > 12 页 × 7 秒 ≈ 84 秒 → ffmpeg `-shortest` 自动对齐

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `physicist/presentations/pages/20th_century/Wolfgang_Pauli/page.md` | 本地 Wikipedia 正文 |
| `physicist/presentations/pages/20th_century/Wolfgang_Pauli/metadata.json` | Wikidata 结构化元数据 |
| `20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | 标杆实例 Beamer 源码 |
| `20th_century/Physicist_Bio_Prompt_Template.md` | 通用提示词模板 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
