# 物理学家立传提示词（人物专属：Johannes Diderik van der Waals）

> 本文件是 OpenPhysicist 20 世纪诺贝尔物理学奖批量立传的**人物专属提示词**，结构对齐标杆 `Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节母本）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Johannes Diderik van der Waals（约翰内斯·迪德里克·范德瓦耳斯），1910 年诺贝尔物理学奖得主，气体液体状态方程之父。
- **设计哲学**：保留物理学家模板两大骨架——「身份信息页」与「研究领域结构化表达」；本人物是"大器晚成 + 理论勇气"的典范：在分子尚被否认的年代（Mach/Ostwald 唯能论），坚持分子的实在性并算出它们的大小。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Johannes Diderik van der Waals（1837-11-23 ~ 1923-03-08，享年 85 岁）
- **气质关键词**：**分子实在性的辩护者、气液连续性的统一者、大器晚成的莱顿学徒**
- **官方获奖理由（禁止改写）**：
  > "for his work on the equation of state for gases and liquids"（因其关于气体与液体状态方程的工作）
- **设计母题**：**气液的连续统一（continuity of gas and liquid）**——临界点两侧的同一物质；视觉语言用 P-V 相图等温线与临界点标记。
- **本地数据源**：`physicist/presentations/20th_century/20th_century/Johannes_Diderik_van_der_Waals/page.md`（Wikipedia 全文 + frontmatter）
- **参考模板**：标杆 `Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`；首页 `cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ⏳ **待下载** `https://en.wikipedia.org/wiki/Johannes_Diderik_van_der_Waals` 到 `{Dir}/Johannes_Diderik_van_der_Waals.html`（本地暂只有 `page.md`）
- **事实基准**：
  - 生卒（1837-11-23 生于莱顿 ~ 1923-03-08 卒于阿姆斯特丹，享年 85；女诗人 Jacqueline 一年后先逝）
  - 家庭（木匠 Jacobus van der Waals 十孩之长；1865-09 娶 Anna Magdalena Smit（18 岁），三女一子；妻 1881 年 34 岁因肺结核去世，此后**约十年未发表论著且终身未再娶**；子 Johannes Diderik van der Waals Jr. 同为理论物理学家并继任其教席）
  - 教育（工人阶层无缘文法中学 → 高等初等学校 → 小学教师学徒 → 1856-1861 考取教师与校长资格 → 1862 起在莱顿大学旁听数学/物理/天文（不受注册资格限制） → 部长豁免古典语言要求 → 通过博士资格考试）
  - 博士（1873-06-14 莱顿大学答辩 *Over de Continuïteit van den Gas- en Vloeistoftoestand*《论气液状态的连续性》，导师 Pieter Rijke；Maxwell 在 Nature 撰文盛赞）
  - 任职（1865 Deventer HBS 物理教师 → 1866 海牙 → 1877-09 新建阿姆斯特丹市立大学**首任**物理学教授，至 70 岁退休）
  - 核心贡献清单：
    1. 范德瓦耳斯状态方程（1873，分子体积 b 与吸引参数 a）
    2. 气液连续性学说（临界点统一气液两相）
    3. 对应态定律（1880，约化变量普适）
    4. 二元溶液理论（1890，承 Gibbs Ψ 面）
    5. 毛细现象热力学理论（1893）
    6. 分子尺寸与引力的定量估计（为分子科学定基调）
  - 诺奖演讲（注记）：1910-12-12 *The Equation of State for Gases and Liquids*（分子实在性长段可引）
  - 核心时间线（1837 生 → 1856-61 教师资格 → 1862 旁听莱顿 → 1865 Deventer+成婚 → 1866 海牙 → 1873 博士论文 → 1875 荷兰皇家艺术与科学院院士 → 1877 阿姆斯特丹教授 → 1880 对应态定律 → 1890 二元溶液理论/Ψ 面 → 1893 毛细理论 → 1896-1912 科学院秘书 → 1910 诺贝尔奖（72 岁） → 1913 美国 NAS 外籍院士 → 1916 美国哲学学会荣誉会员 → 1923 卒）

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/20th_century/` 下已有 `Johannes_Diderik_van_der_Waals/`（本提示词所在），需新建 `images/` 子目录存放肖像与插图

### 第 2 步：复制 Makefile 【模板通用】

- 复制标杆目录 `Kenneth_G_Wilson/Makefile`，设置 `MAIN=Johannes_Diderik_van_der_Waals_zh`、`VIDEO_NAME=Johannes_Diderik_van_der_Waals_zh`

### 第 3 步：收集图片 【人物专属】

- 肖像：page.md 内嵌 "Van der Waals in 1910" infobox 像；优先 Commons `Special:FilePath/Johannes Diderik van der Waals.jpg?width=500`
- 404/HTML 则经 Wikipedia REST API `page/summary` 查 infobox 原图名再抓；再失败用装饰圆占位（主色边框圆 + 姓名缩写）
- 插图建议：P-V 相图等温线（可 TikZ 绘制，勿用网图冒充史料照片）

### 第 4 步：研究领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | thermodynamics | 热力学 | 状态方程/对应态/二元溶液 | 主线页 |
| 1 | molecular physics | 分子物理 | 分子体积与引力的实在性 | 核心页 |
| 2 | capillarity | 毛细现象理论 | 1893 热力学进路（对 Laplace 力学进路） | 毛细页 |
| 3 | physical chemistry | 物理化学 | 二元溶液与 Gibbs Ψ 面 | 溶液页 |

入库：`MySQL/data/Johannes_Diderik_van_der_Waals.yaml`（已备好；**注意 name_en 沿用库内形式 `Johannes van der Waals`**，`cd MySQL && python3 seed_person.py data/Johannes_Diderik_van_der_Waals.yaml`）。

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Pieter Rijke | 师→生 | 莱顿大学博士导师，1873 答辩 |
| advisor-student | Willem Hendrik Keesom | vdW→学生 | 博士生，低温物理学家 |
| advisor-student | Diederik Korteweg | vdW→学生 | 博士生 |
| spouse | Anna Magdalena Smit | 无向 | 1865 结婚，1881 早逝，终身未再娶 |
| parent-child | Johannes Diderik van der Waals Jr. | vdW→孩子 | 之子，继任其阿姆斯特丹教席 |
| colleague | Jacobus Henricus van 't Hoff | 无向 | 阿姆斯特丹同事，1901 首届化学诺奖 |
| colleague | Hugo de Vries | 无向 | 阿姆斯特丹同事，生物学家 |
| influence | Rudolf Clausius | 思想来源 | 1857 年论热的运动论著引其入气体理论 |
| influence | James Clerk Maxwell | 思想影响 | 1873 年 Nature 盛赞其博士论文 |
| influence | Heike Kamerlingh Onnes | 思想影响 | 受其工作影响，1908 液化氦 |

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：相图、连续、深沉晚成
- **配色**：流体青绿（主色）+ 诺奖香槟金 `C9A227` + 四分类色
  - 主色 — 流体青绿 `#0E5A50`
  - `badgeEOS` 状态方程 — `#B0752B`
  - `badgeMol` 分子实在性 — `#7A3B69`
  - `badgeCorr` 对应态定律 — `#2F6690`
  - `badgeCapil` 毛细/二元溶液 — `#8A3033`
- **背景母题**：稀疏 P-V 等温线族 + 临界点圆点，呼应"气与液本是一物"

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍；底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素（范德瓦耳斯：荷兰 | 阿姆斯特丹大学 | Nobel 1910）。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，含至少：生卒、本名（Johannes Diderik van der Waals）、国籍、出生地（莱顿）、师承（Pieter Rijke）、任职（阿姆斯特丹首任物理教授）、主要荣誉、核心领域。事实取自 page.md infobox，不得杜撰。
4. **品牌口径统一（共享 GitHub）**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenPhysicist`）；GitHub 链接由首页模板 `\input` 继承，子 deck 不重复；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 气液状态方程之父 / Johannes Diderik van der Waals 1837–1923 + badge + 头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — 状态方程 / 分子实在性 / 对应态 / 毛细与溶液
04  莱顿木匠之子：被语言挡在门外的少年 (1837–1861) — 教师学徒之路
05  旁听生 (1862–1872) — 部长豁免、HBS 教师、博士资格考试
06  1873 博士论文 — 《论气液状态的连续性》、Rijke 指导、Maxwell 盛赞
07  范德瓦耳斯方程（核心贡献页，公式框 (p + a/V²)(V − b) = RT）
08  分子的实在性 — Mach/Ostwald 唯能论背景下的坚持（客观描述，见陷阱表）
09  1880 对应态定律 — 普适常数；Dewar 氢液化 1898 / Onnes 氦液化 1908 的路标
10  1890 二元溶液理论 — Gibbs Ψ 面的热力学表述
11  1893 毛细理论 — 对 Laplace 力学进路的热力学替代
12  阿姆斯特丹首任教授与家庭 — van 't Hoff / de Vries 同事；1881 丧妻十年沉寂
13  1910 诺贝尔物理学奖 — 官方理由原句 + 诺奖演讲分子实在性长段
14  遗产 — 范德瓦耳斯力/分子/半径、小行星 32893、低温物理的路标
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照成品 `\profileslide`；头部宏（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle`）可整体复用标杆骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make`，用 `pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**van der Waals 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 忠实英文原句 "for his work on the equation of state for gases and liquids"（1910），勿改写为"发现分子间力" |
| 出身叙事 | 木匠之子、无文法中学资格、古典语言豁免——page 明载可写；禁加"贫寒逆袭"之类演绎 |
| 丧妻沉寂 | 妻 1881 卒后约十年未发表+终身未再娶——page 明载，止于事实，禁心理描写 |
| Maxwell 引语 | "there can no doubt that the name of Van der Waals will soon be among the foremost in molecular science"（Nature 1873）page Related quotes 明载**可引**；诺奖演讲长段英文亦可引；其余禁编造 |
| 唯能论争论 | Mach/Ostwald 否认分子是时代哲学潮流——客观描述背景，禁写 vdW 与二人直接论战 |
| 同名区分 | 儿子 **Jr.** 必带后缀；远房表亲 Joan van der Waals（物理学家）与侄 Peter van der Waals（家具工匠）仅在页注层面区分，禁混写 |
| Onnes 链条 | vdW→对应态→低温液化（Onnes 1908 液氦→1911 超导）page 明载；勿写"vdW 指导 Onnes" |
| 对应态归属 | 对应态定律是 vdW **1880** 第二大发现；禁把低温液化实验成果归到 vdW 名下 |
| 导师唯一 | 博士导师仅 Pieter Rijke；禁从诺奖演讲致谢反推其他师承 |
| 元素名 | "van der Waals" 小写 van 在英文语境按姓氏排序，TeX 中注意大小写 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| van der Waals equation | 范德瓦耳斯方程 | (p+a/V²)(V−b)=RT |
| equation of state | 状态方程 | 1910 诺奖主题 |
| law of corresponding states | 对应态定律 | 1880，约化变量普适性 |
| van der Waals forces | 范德瓦耳斯力 | 分子间吸引 |
| van der Waals radius | 范德瓦耳斯半径 | 分子尺寸 |
| critical temperature | 临界温度 | Andrews 1869 实验引发 |
| continuity of gas and liquid | 气液连续性 | 博士论文标题 |
| binary solutions | 二元溶液 | 1890 论著 |
| Ψ surface | Ψ 面（自由能曲面） | 承 Gibbs |
| capillarity | 毛细现象 | 1893 热力学进路 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Eternals** — Alex-Productions（宏大 / 深远 / 长期影响，49k views）
- **匹配理由**：范德瓦耳斯力写进了每一本化学/物理教科书、出现在每一处分子模拟里——"长期影响"标签与其遗产最贴合；宏大感呼应其分子实在性最终被普遍接受的胜利。
- **本地路径**：`music_audio/alex-productions/76-V5T_kW2PH_s-Eternals.wav`
- **备选**（未采用）：
  - ★★ Timeless — "沉稳/长期纲领"匹配其定律长青，但为标杆 Wilson 已用曲目，本批回避
  - ★ Nostalgia — "怀旧/温和"匹配莱顿学徒的晚成叙事，但"宏大"感弱于分子遗产的分量
- **时长核验**：曲目时长 > 16 页 × 7 秒 ≈ 112 秒 → ffmpeg `-shortest` 自动对齐
- **备注**：批内 BGM 去重——Lippmann=Shine Like The Sun、Marconi=SEA、Braun=The Invisible Light、Wien=The Flow of Time。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/20th_century/20th_century/Johannes_Diderik_van_der_Waals/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Johannes_Diderik_van_der_Waals.yaml` | 入库 yaml（已备好，name_en 沿用库内 `Johannes van der Waals`） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
