# 物理学家立传提示词（21 世纪批次：John M. Martinis）

> **本文件是 OpenPhysicist「物理学家立传提示词」的 John M. Martinis 专属实例**，按标杆 Kenneth_G_Wilson_zh.md 的 0–11 节结构撰写。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。
> 事实基准唯一来源：本地 page.md（Wikipedia 全文），**page.md 无载的内容一律禁写**。

---

## 一、模板定位 【模板通用】

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：John M. Martinis（约翰·马蒂尼斯），美国实验物理学家，2025 诺贝尔物理学奖得主（三人共享），从宏观量子隧穿到 Sycamore 量子霸权的超导量子计算工程旗手。
- **设计哲学**：物理学家立传必须有「身份信息页」与结构化「研究领域」表达；Martinis 的主线是**一个博士论文实验长成一台处理器**——用「从势垒到芯片（from barrier to chip）」作为贯穿视觉母题。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：John Matthew Martinis（1958 生于美国，在世）
- **气质关键词**：**量子霸权的实现者、超导量子比特的工程师、克羅地亚移民之子** —— 2025 诺贝尔物理学奖获奖理由（官方原文，禁改写）：
  > "For the discovery of macroscopic quantum mechanical tunnelling and energy quantisation in an electric circuit."（因发现电路中的宏观量子力学隧穿与能量量子化）
- **设计母题**：**从势垒到芯片（from barrier to chip）**。视觉上用隧穿势垒曲线渐变为芯片电路走线：1985 年博士论文里的一个势垒，40 年后长成 53 量子比特的 Sycamore。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/physicist/presentations/21th_century/21st_century/John_M._Martinis/page.md`
- **第 0 步标注**：page.md 已有本地；**html 与 images/ 待下载**。Wikipedia URL：`https://en.wikipedia.org/wiki/John_M._Martinis`。
- **参考模板**：
  - 标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步**：本提示词的第 4 步（研究领域表）与第 4.5 步（社会关系表）已由本批次完成入库（greatminds 库），立传时**只读勿改**，核对即可。

### 第 0 步：事实基准（page.md 已核对） 【人物专属】

- **生卒**：1958 年生（page.md 无月日），在世。
- **国籍**：美国（United States）。
- **家庭**：在洛杉矶圣佩德罗（San Pedro）长大；父亲是克罗地亚 Komiža（Vis 岛）人，为逃离南斯拉夫政权移民美国；母亲生于圣佩德罗、父母同为克罗地亚移民。
- **教育**：UC Berkeley 物理学 B.S. 1980 → PhD 1987；博士论文 *Macroscopic Quantum Tunneling and Energy-Level Quantization in the Zero Voltage State of the Current-Biased Josephson Junction*（1985）；博士导师 John Clarke。
- **博士后**：第一站 CEA Paris-Saclay（法国）→ NIST Boulder 电磁技术部（SQUID 放大器）。
- **任职机构**：2004 起 UCSB 教职（多年担任 Susan and Bruce Worster Chair in Experimental Physics）；2014 被 Google Quantum AI Lab（UCSB 与 Google 合作项目）连同团队整体聘用；2020-04 在被改任顾问角色后从 Google 辞职；2020 加入澳大利亚 Michelle Simmons 创办的 Silicon Quantum Computing；2022 与 CEO Alan Ho 创立 Qolab（半导体芯片工艺路线的量子计算公司）；2026 年获奖（克罗地亚 Grand Order）。
- **关键荣誉**：Samuel Wesley Stratton Award 1996；APS Fellow；Fritz London Memorial Prize 2014（与 Devoret、Schoelkopf 共享）；*Nature*'s 10（2019）；John Stewart Bell Prize 2021；Nobel Prize in Physics 2025（与 Clarke、Devoret 共享）；Grand Order of King Dmitar Zvonimir 2026（克罗地亚，表彰对量子物理与技术的全球贡献）。
- **知名学生**：page.md 未列 Doctoral students，**禁写**。
- **核心贡献清单**：
  1. 博士期间（与 Clarke、Devoret）研究约瑟夫森隧道结宏观变量的量子行为——1985 三人发表微波脉冲分析、演示量子化能级，成为超导量子计算的基础（2025 诺奖核心）；
  2. NIST 时期 SQUID 放大器；
  3. UCSB 时期：与同事发展的量子器件被 *Science* 评为 2010 年度突破（Breakthrough of the Year）；
  4. Google 时期：领导团队研制超导量子计算机，2019 年以 53 量子比特 Sycamore 处理器在 *Nature* 发表论文，宣称首次实现量子霸权（quantum supremacy）；
  5. 创业时期：Qolab（2022，与 Alan Ho）；Qolab 与 HPE 共同领导 DARPA 量子基准测试倡议（QBI）硬件构建；Quantum Scaling Alliance 联合负责人。
- **关键时间线（15–20 节点）**：1958 生 → 圣佩德罗长大 → 1980 Berkeley B.S. → 博士期间（Clarke 门下，与 Devoret 合作）研究约瑟夫森结宏观量子行为 → 1985 博士论文/三人微波脉冲实验演示量子化能级 → 1987 Berkeley PhD → CEA Paris-Saclay 博后 → NIST Boulder（SQUID 放大器）→ 1996 Stratton Award → 2004 任教 UCSB（Worster 讲席）→ 2010 *Science* 年度突破 → 2014 团队入驻 Google Quantum AI Lab → 2019 Sycamore 53 量子比特 *Nature* 量子霸权论文、*Nature*'s 10 → 2020-04 辞去 Google 职务 → 2020 加入 Silicon Quantum Computing（澳大利亚）→ 2021 Bell Prize → 2022 创立 Qolab → 2014 Fritz London Prize（注意年份在前，勿与 Bell 混）→ 2025 诺贝尔物理学奖 → 2025-12 Qolab Start 平台发布 → 2026 Grand Order of King Dmitar Zvonimir、Qolab 与 HPE 共同领导 DARPA QBI、与新加坡 NQFF 合作。

### 第 4 步：研究领域表（已入库，只读） 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | quantum computing | 量子计算 | page.md field_of_work 首列；Sycamore 与 Qolab 的主线 | 核心页 |
| 1 | superconducting qubits | 超导量子比特 | 相位量子比特到 Sycamore 的工程化 | 量子比特页 |
| 2 | macroscopic quantum phenomena | 宏观量子现象 | 2025 诺奖核心：1985 博士论文实验 | 1985 实验页 |
| 3 | Josephson junction | 约瑟夫森结 | 实验与器件的物理载体 | 1985 实验页 |
| 4 | precision measurement | 精密测量 | NIST SQUID 放大器时期 | NIST 页 |

### 第 4.5 步：社会关系表（与 yaml 完全一致，已入库） 【人物专属】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | John Clarke | 对方是导师 | UC Berkeley 博士导师（PhD 1987），1985 宏观量子实验 PI |
| colleague | Michel H. Devoret | 无向 | 1985 年合作演示约瑟夫森结能级量子化（其时为 Clarke 组博士后） |
| co-honored | John Clarke | 无向 | 2025 诺贝尔物理学奖共享（与其博士导师同台获奖） |
| co-honored | Michel H. Devoret | 无向 | 2025 诺贝尔物理学奖共享 |
| co-honored | Robert J. Schoelkopf | 无向 | 2014 Fritz London Memorial Prize 共享 |

### 第 5 步：配色方案 【人物专属】

- **气质**：攻坚、工程、从低温势垒到芯片的炽热
- **配色**：深红（主色）+ 诺奖香槟金 `C9A227` + 四分类色
  - 主色 `mainclr` — 深红 `#8C1515`（批内唯一）
  - `badgeA` 超导量子比特 — 铜橙 `#B3541E`
  - `badgeB` 宏观量子现象 — 靛蓝 `#4C5FD5`
  - `badgeC` 约瑟夫森结 — 琥珀 `#E07B30`
  - `badgeD` 精密测量 — 青瓷 `#2E8B8B`
- **背景母题**：柔和气泡 + 势垒曲线渐变为电路走线的连续图样。

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注（肖像待下载，2025 年照片优先）。
2. **封面有国籍**：底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素（机构 = UC Santa Barbara）。
3. **必须有身份信息页**：含至少：生年（1958，无月日）、国籍、成长地（San Pedro）、克罗地亚裔背景、教育（Berkeley B.S. 1980/PhD 1987）、博士导师（Clarke）、任职（NIST → UCSB → Google → UCSB/Qolab）、主要荣誉（Nobel 2025/Bell 2021/Fritz London 2014）、核心领域。
4. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，12 帧 + 共享首页】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 从宏观量子到量子霸权 / John M. Martinis 1958– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — 1985 实验组员 / SQUID 放大器 / Sycamore 量子霸权 / Qolab
04  圣佩德罗与伯克利 (1958–1987) — 克罗地亚移民家庭、Berkeley B.S./PhD、Clarke 门下
05  1985：博士论文的核心实验 — 与 Clarke/Devoret 演示宏观量子隧穿与能级量子化；公式框放隧穿势能 U(φ) 概念图式（page.md 无公式推导，注明示意）
06  CEA 与 NIST (1987–2004) — Paris-Saclay 首站博后、Boulder SQUID 放大器、Stratton Award 1996
07  UCSB：量子比特的工坊 (2004–2014) — Worster 讲席、*Science* 2010 年度突破
08  Google Quantum AI (2014–2020) — 团队入驻、Sycamore 处理器、2019 *Nature* 量子霸权论文、*Nature*'s 10
09  2020 之后：Qolab 与量子工程 — Silicon Quantum Computing、Qolab 2022、DARPA QBI 联盟
10  荣誉与认可 — Nobel 2025 · Bell 2021 · Fritz London 2014 · Stratton 1996 · Nature's 10
11  遗产：一个实验到一台处理器 — 师生三代同获诺奖的传承
12  结尾
```

### 第 7–8 步：版式要点 + 陷阱表 【人物专属】

**版式要点**：工程类人物多用「里程碑年份轴 + 器件照片位」；公式框建议放电流偏置约瑟夫森结的抛物线-余弦势能概念图式 `U(φ) = -EJ·cos(φ) + (1/2)EC·(φ−φx)²`（page.md 无公式推导，需注明为示意）。

**Martinis 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 出生年 | 仅 1958（page.md 无月日），禁写具体日期；正文有 "age 67–68" 表述，立传只写年份 |
| 姓名形式 | 全名 John Matthew Martinis；条目与目录名 John_M._Martinis；克罗地亚裔（父 Komiža/Vis 岛），2026 获克罗地亚大勋章 |
| 1985 三人分工 | Martinis 是博士生（博士论文即此实验）、Devoret 是博士后、Clarke 是 PI；勿写成三人同等资历 |
| 量子霸权口径 | 2019 *Nature* 论文是 "claimed the first evidence of quantum supremacy"（宣称首个证据），禁写成「证明了量子霸权」；处理器名 Sycamore、53 量子比特 |
| Google 离职 | 2020-04 在被重新分配为顾问角色后辞职——一句话客观带过，禁展开公司内幕叙事 |
| Fritz London 年份 | 2014（与 Devoret、Schoelkopf 共享），勿与 Bell Prize 2021 混淆；Devoret 获 Bell 是 2013 |
| 两个三人组勿混 | 2025 Nobel = Clarke + Martinis + Devoret；2021 Micius = Clarke + Devoret + Yasunobu Nakamura（**不含** Martinis，Martinis 篇不收 Micius） |
| 无学生名单 | page.md 未载 Doctoral students，学生关系禁写 |
| PCAST 任命 | page.md 载 2026 年获任总统科技顾问委员会（PCAST），涉及政治人物，**立传省略不写** |
| 在世 | 1958 年生、在世，生卒页留白卒年 |
| 荣誉年份轴 | 1996 Stratton → 2014 Fritz London → 2019 Nature's 10 → 2021 Bell → 2025 Nobel → 2026 Grand Order，勿乱序 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| macroscopic quantum tunnelling | 宏观量子隧穿 | 诺奖理由核心词 |
| energy-level quantization | 能级量子化 | 论文标题美式 quantization，诺奖理由为英式 quantisation，两处各按原文 |
| Josephson junction | 约瑟夫森结 | 隧道结 |
| phase qubit | 相位量子比特 | 1985 实验电路形态 |
| Sycamore processor | 悬铃木处理器 | 53 量子比特，2019 |
| quantum supremacy | 量子霸权/量子优越性 | 用 claimed the first evidence 口径 |
| SQUID amplifier | SQUID 放大器 | NIST 时期工作 |
| superconducting quantum computer | 超导量子计算机 | Google 时期目标 |
| Breakthrough of the Year | 年度突破 | *Science* 2010 |
| qubit | 量子比特 | 勿写「量子位元」与「量子比特」混用 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Savage** — Alex-Productions（强推进 / 紧张 / 攻坚）
- **风格**: 强推进 / 紧张 / 难题攻克
- **匹配理由**: 「攻坚」气质匹配 Martinis 的工程底色——从 1985 年一个博士论文实验，到 NIST 的放大器打磨，再到 53 量子比特的量子霸权冲刺，是持续三十年的硬仗；强推进节奏贴合 Sycamore 里程碑的紧张感。
- **备选** (未采用): Cinematic Experience（高潮感强但已多批使用）；Through the Darkness（突破前夕氛围，已多批使用）。
- **本地路径**: `music_audio/alex-productions/34-pILVwyuW3jw-Savage.wav`
- **时长**: 约 2–3 分钟 > 13 页 × 7 秒 ≈ 91 秒 → ffmpeg `-shortest` 自动对齐。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/John_M._Martinis/page.md` | 本地 Wikipedia 正文（事实唯一来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架/源码标杆 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/John_M._Martinis.yaml` | 研究领域 + 社会关系（已入库，只读） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
