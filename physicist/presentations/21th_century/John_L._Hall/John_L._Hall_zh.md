# 物理学家立传提示词（21 世纪批次：John L. Hall）

> **本文件是 OpenPhysicist 21 世纪诺奖物理学家立传的人物专属提示词**，以 John L. Hall（2005 诺贝尔物理学奖，激光精密光谱与光频梳）为对象。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：John Lewis "Jan" Hall（约翰·霍尔），2005 年诺贝尔物理学奖**一半**得主（与 Theodor W. Hänsch 共享另一半；另一半归 Glauber），激光稳定与光频梳先驱。
- **设计哲学**：保留「身份信息页」+ 研究领域结构化骨架；Hall 篇的设计母题围绕「把光的频率变成尺子」——光频梳与光学钟的精密之美，视觉语言可用「等距齿梳」。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：John Lewis Hall（1934-08-21 生于科罗拉多州丹佛，在世）
- **气质关键词**：**激光稳定之父、NIST 四十年、把诺奖奖章捐给母校的实验家**
- **诺奖理由（官方原文，禁止改写）**：
  > "for their contributions to the development of laser-based precision spectroscopy, including the optical frequency comb technique"（因对激光精密光谱学的发展（包括光频梳技术）的贡献）
- **设计母题**：**频率之尺**——光频梳如同等距刻度的光尺，用于丈量氢原子跃迁频率与光学钟。
- **本地数据源**：
  - ✅ `physicist/presentations/21th_century/21st_century/John_L._Hall/page.md`（已有本地）
  - ⬜ `{Dir}.html` 与 `images/` **待下载**：Wikipedia URL `https://en.wikipedia.org/wiki/John_L._Hall`
- **参考模板**：`physicist/presentations/cover/openphysicist_page.tex`；骨架复用 20 世纪成品（如 `Kenneth_G_Wilson_zh.tex`）。

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属】

- 生卒：1934-08-21 生于美国科罗拉多州丹佛；在世。
- 教育：Carnegie Institute of Technology 三级学位——BS（1956）、MS（1958）、PhD（1961，正文口径；infobox 论文行标注 1962，两处并存以正文为主）；博士论文 *Electron spin resonance of interstitial hydrogen atoms in calcium-fluoride*；1957–1961 National Carbon Company 物理研究员。
- 任职：美国商务部国家标准局（NBS，今 NIST）博士后起服务至 2004 年退休（1962–2004），NIST Senior Fellow emeritus；1967 年起在科罗拉多大学博尔德分校讲课；JILA（CU-Boulder 与 NIST 联合研究所）Fellow；CU-Boulder 物理系 adjoint professor。
- 关键荣誉（page.md 明载年份）：Commerce Gold Medal（1969、1974 团体、2002 团体）；Samuel W. Stratton Award（1971）；IR-100（1975 激光稳定器、1977 激光波长计）；E. U. Condon Award（1979）；Charles Hard Townes Award（1984，与苏联科学院 V. P. Chebotayev 共同获得）；Davisson–Germer Prize（1988）；巴黎北部大学荣誉博士（1989）；Frederic Ives Medal（1991）；Einstein Prize for Laser Science（1992）；Arthur L. Schawlow Prize（1993）；Astin Measurement Science Award（2000）；Max Born Award（2002）；Presidential Rank Award（2002）；IEEE Rabi Award（2004）；荣誉军团勋章（2004）；Nobel（2005）；Golden Plate Award（2006）；Glasgow 荣誉 DSc（2007）；OSA 荣誉会员（2007）。
- 知名博士生：Jun Ye（infobox 唯一列名）。
- 核心贡献清单：
  1. **激光稳频**先驱（Pound–Drever–Hall 技术以其命名）
  2. **光学频率梳**技术的开拓者之一（2005 诺奖核心）
  3. **光学钟**（optical clock）
  4. 激光波长精密计量（Lambdameter）
- 关键时间线（15–20 节点）：1934 生丹佛 → 1956/1958/1961 Carnegie 三级学位 → 1957–61 National Carbon Fellow → 1962 入 NBS → 1967 起 CU-Boulder 讲课 → 1969 Commerce Gold Medal → 1971 Stratton Award → 1975 IR-100 激光稳定器 → 1977 IR-100 Lambdameter → 1984 Townes Award（与 Chebotayev 共同）→ 1988 Davisson–Germer Prize → 1991 Ives Medal → 1992 Einstein Prize for Laser Science → 1993 Schawlow Prize → 2002 Max Born Award → 2004 Rabi Award + 荣誉军团勋章 → 2004 自 NIST 退休 → 2005 诺贝尔物理学奖（与 Hänsch 共享一半，Glauber 另一半）→ 2008 与 20 位物理诺奖得主联名致信布什总统 → 2015 签署林道《梅瑙气候变化宣言》→ 2018 将诺奖奖章捐赠科罗拉多大学博尔德分校。

### 第 4 步：研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | laser spectroscopy | 激光光谱学 | 2005 诺奖核心 | 核心页 |
| 1 | optical frequency metrology | 光学频率计量 | 光频梳、光学钟 | 频率梳页 |
| 2 | laser stabilization | 激光稳频 | PDH 技术、稳定激光先驱 | 稳频页 |
| 3 | optics | 光学 | OSA 多项奖章（Ives/Born/Townes） | 荣誉页 |

### 第 4.5 步：社会关系梳理 + 入库 【与 yaml 完全一致，只收 page.md 明载】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Theodor W. Hänsch | 无向 | 2005 诺贝尔物理学奖共同得主（两人共享一半） |
| co-honored | Roy Glauber | 无向 | 2005 诺贝尔物理学奖共同得主（Glauber 得另一半） |
| advisor-student | Jun Ye | Hall→学生 | 博士生，JILA 光学钟名家 |
| co-honored | V. P. Chebotayev | 无向 | 1984 Charles Hard Townes Award 共同得主 |

> 入库注意：Glauber 用库内规范名 **`Roy Glauber`**（id=2566）；Hall 页未载博士导师，**禁写**。

### 第 5 步：设计配色方案 【人物专属】

- **气质**：精密、稳健、实证
- **配色**：主色 **深海军蓝 `#0F4C81`**（精密测量的沉稳）+ 诺奖香槟金 `C9A227` + 四分类色：
  - `badgeComb` 光频梳 — 靛蓝 `#4C5FD5`
  - `badgeClock` 光学钟 — 青绿 `#0E7C7B`
  - `badgePDH` 激光稳频 — 琥珀 `#E07B30`
  - `badgeMetro` 频率计量 — 玫瑰 `#C4204F`
- **背景母题**：等距齿梳（光频梳谱线）横贯画面。

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + 细边框 + 姓名小字注）；封面有国籍。
2. **必须有身份信息页**：左头像 + 右信息网格（生卒、国籍、出生地、教育、师承、任职、荣誉、核心领域），事实取自 infobox 不得杜撰。
3. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 光的频率之尺 / John L. Hall 1934– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — 激光稳频 / 光频梳 / 光学钟 / 频率计量
04  丹佛与 Carnegie (1934–1961) — 三级学位、国家碳公司研究员
05  NIST 四十年 (1962–2004) — NBS→NIST、Senior Fellow
06  JILA 岁月 — CU-Boulder adjoint professor、与 NIST 联合
07  激光稳频（核心贡献页）— 公式框放 PDH 鉴频示意（page.md 无显式公式，注明为概念图式）
08  光频梳：丈量光 — 与 Hänsch 共享的一半诺奖
09  光学钟 — Jun Ye 与下一代计量
10  荣誉与认可 — Nobel 2005 · Ives 1991 · Born 2002 · Townes 1984 · 荣誉军团勋章
11  公共行动 — 2008 致信布什、2015 梅瑙气候宣言、2018 捐赠奖章
12  遗产：精密计量的地基
13  结尾
```

### 第 7–8 步：版式要点 + 陷阱表

- 每写完一页 make，用 pdftoppm 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

**Hall 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖份额 | Hall 与 Hänsch 共享**一半**（各四分之一），Glauber 得**另一半**；勿写成三人平分 |
| 博士年份 | 正文作 PhD 1961，infobox 论文行标 1962——以**正文 1961** 为主线，注明 infobox 差异 |
| Glasgow | frontmatter educated_at 含 University of Glasgow，但正文仅载其 2007 年**荣誉** DSc——勿写成"求学格拉斯哥" |
| 母校口径 | infobox Alma mater 为 Carnegie Institute of Technology（三级学位）；勿写 Carnegie Mellon 现名当年代用 |
| 博士导师 | page.md **无载**——禁写、禁建 advisor-student 关系 |
| Townes Award | 1984 年与苏联科学院 **V. P. Chebotayev** 共同获得——唯一非诺奖的共同获奖关系 |
| 学生 | infobox 博士生仅 **Jun Ye** 一人，勿扩写 |
| 小名 | "Jan" 是其通行昵称（John Lewis "Jan" Hall），封面可用全名+昵称 |
| 捐赠 | 2018 年捐的是**诺奖奖章**给 CU-Boulder，非其他奖 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| optical frequency comb | 光频梳 | 等距谱线"光尺" |
| optical clock | 光学钟 | 下一代时间基准 |
| Pound–Drever–Hall technique | PDH 稳频技术 | 以三人命名 |
| precision spectroscopy | 精密光谱学 | 诺奖理由核心词 |
| laser stabilization | 激光稳频 | 1975 IR-100 |
| NIST / NBS | 美国国家标准与技术研究院（旧称标准局） | 1962–2004 |
| JILA | JILA 研究所 | CU-Boulder 与 NIST 联合 |
| frequency metrology | 频率计量 | Lambdameter |
| Davisson–Germer Prize | 戴维森–革末奖 | APS 1988 |
| Mainau Declaration | 梅瑙宣言 | 2015 气候版，76 位诺奖得主签署 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **SEA** — Alex-Productions（高受众 / 流动 / 平稳）
- **匹配理由**: 「流动、平稳」贴合 Hall 四十年如一日的稳频与计量工作——不是爆发式突破，而是把测量推到极限的长期静流。
- **本地路径**: `music_audio/alex-productions/92-WEqfdRXU3IU-SEA.wav`
- **备注**: 批内曲不重复（前三人用 Savage/Expedition/The Invisible Light）。

---

## 五、关键参考文件 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/John_L._Hall/page.md` | 本地 Wikipedia 事实基准 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/John_L._Hall.yaml` | 社会关系入库 yaml |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
