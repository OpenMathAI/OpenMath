# 物理学家立传提示词（21 世纪批次 · Wolfgang Ketterle）

> **本文件是 OpenPhysicist 21 世纪诺奖物理学家立传提示词**，目标人物：Wolfgang Ketterle（2001 诺贝尔物理学奖，玻色–爱因斯坦凝聚与原子激光）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Wolfgang Ketterle（沃尔夫冈·克特勒），21 世纪（2001）诺奖得主系列。
- **设计哲学**：保留「身份信息页 + 研究领域表」骨架；Ketterle 篇以「原子激光——物质波的相干放大」为叙事主线，与 Cornell/Wieman 篇的"首个 BEC"分工互补（他独立实现钠原子 BEC 并率先做出原子激光）。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Wolfgang Ketterle（1957-10-21 生于德国海德堡，在世）
- **气质关键词**：**钠原子气体的独立 BEC 实现者、第一台原子激光的缔造者、跑完波士顿马拉松的实验物理学家** —— 2001 诺贝尔物理学奖获奖理由（官方原文，禁止改写）：
  > "for the achievement of Bose-Einstein condensation in dilute gases of alkali atoms, and for early fundamental studies of the properties of the condensates"（因实现稀薄碱金属气体中的玻色–爱因斯坦凝聚，以及对凝聚体性质的早期基础研究）
- **设计母题**：**相干物质波（coherent matter wave）**。1997 年两团凝聚体干涉条纹与"原子激光"输出耦合是 Ketterle 的标志性画面——封面视觉用双波纹叠加出干涉条纹，呼应物质波的相干性。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Wolfgang_Ketterle/page.md`（**已有本地**）
- **页面 HTML 与图片**：`Wolfgang_Ketterle.html` 与 `images/` **待下载**，Wikipedia URL：`https://en.wikipedia.org/wiki/Wolfgang_Ketterle`
- **参考模板**：
  - 标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报，遇到歧义先征求意见再继续。
> 数据库写入 `greatminds`（MySQL），yaml 母本 `MySQL/data/Kenneth_G_Wilson.yaml`，入库引擎 `MySQL/seed_person.py`。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ `page.md` 已有本地（21th_century/21st_century/Wolfgang_Ketterle/）
- 🔲 待下载 `Wolfgang_Ketterle.html` 与 infobox 头像 `images/`（404 则装饰圆占位；另有 BEC1.2 实验装置照可用作插图）
- 事实基准（已按 page.md 核对）：
  - 生卒：1957-10-21 生于 Heidelberg, Baden-Württemberg（西德时期；在世）
  - 国籍：德国（page.md infobox；居美多年，frontmatter 仅 Germany）
  - 教育：Eppelheim/Heidelberg 上学；1976 入海德堡大学，两年后转慕尼黑工业大学，1982 获硕士同等学历（Diplom）；1986 于加兴马普量子光学研究所（MPQ）获实验分子光谱 PhD，导师 Herbert Walther 与 Hartmut Figger；此后在 Garching 与海德堡大学做博士后
  - 博士导师：Herbert Walther + Hartmut Figger（正文与 infobox 双导师；frontmatter 仅列 Walther）
  - 任职：1990 加入 MIT 电子学研究实验室（RLE）David E. Pritchard 组；1993 任 MIT 物理系教职；1998 起任 John D. MacArthur 物理学教授；2006 任 RLE 副主任并出任 MIT 超冷原子中心主任
  - 关键荣誉：I. I. Rabi 1997 · Dannie Heineman（哥廷根）1999 · Fritz London 1999 · Benjamin Franklin 2000 · Nobel 2001 · 巴登-符腾堡州功绩勋章 2002 · 联邦大十字勋章（Great Cross with Star and Sash）· Packard Fellowship
  - 核心贡献：①1995 独立实现钠原子气体 BEC（K. B. Davis 等合作，PRL 75, 3969）；②1997 两团凝聚体干涉实验 + 首台"原子激光"（输出耦合器，PRL 78, 582）；③2003 分子玻色凝聚；④2005 费米子凝聚体中"高温"超流证据
  - 学生：Martin Zwierlein、Zoran Hadzibabic（infobox 博士生）
  - 个人生活：1985–2001 与 Gabriele Ketterle 婚姻（育三子）；2011 起与 Michèle Plott 婚姻；共五个孩子；儿子 Jonas 2003 参加 RSI
  - 跑者身份：2009-12 Runner's World "I'm a Runner"；2013 波士顿马拉松 2:49:16；2014 个人最好成绩 2:44:06；领诺奖时携跑鞋在斯德哥尔摩晨跑
  - 公共事务：2008-05 为 20 位美国物理学诺奖得主之一联名致函小布什总统，请求追加 DOE/NSF/NIST 基础科学应急经费；CEE 董事会成员；澳大利亚 ARC FLET 国际科学顾问委员会委员
  - 诺奖演讲：2001-12-08 "When Atoms Behave as Waves: Bose-Einstein Condensation and the Atom Laser"
  - 关键时间线（≥15 节点）：1957 生海德堡 → 1976 海德堡大学 → 1978 转慕尼黑工大 → 1982 Diplom → 1986 MPQ 博士（分子光谱）→ 博后 Garching/海德堡 → 1990 入 MIT Pritchard 组 → 1993 MIT 教职 → 1995-11 钠原子 BEC → 1997 凝聚体干涉 + 原子激光 → 1998 MacArthur 讲席教授 → 2001 诺贝尔奖 → 2002 功绩勋章 → 2003 分子 BEC → 2005 费米子凝聚超流证据 → 2006 RLE 副主任/超冷原子中心主任 → 2008 联名信 → 2013/2014 马拉松 → 2011 再婚

### 第 4 步：研究领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | Bose-Einstein condensate | 玻色–爱因斯坦凝聚 | 1995 钠原子独立实现，2001 诺奖核心 | 核心页 |
| 1 | atom laser | 原子激光 | 1997 首次实现，相干物质波输出 | 核心页 |
| 2 | ultracold atoms | 超冷原子 | MIT 超冷原子中心长期纲领 | 方法页 |
| 3 | molecular spectroscopy | 分子光谱学 | MPQ 博士方向 | 早年页 |
| 4 | superfluidity | 超流 | 2005 费米子凝聚体"高温"超流证据 | 后续页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Herbert Walther | 师→生（博士导师） | MPQ 加兴所长，分子光谱方向 |
| advisor-student | Hartmut Figger | 师→生（博士导师） | MPQ 共同指导 |
| colleague | David E. Pritchard | 无向 | 1990 加入其 MIT RLE 组做博士后 |
| co-honored | Eric A. Cornell | 无向 | 2001 诺贝尔物理学奖共享 |
| co-honored | Carl E. Wieman | 无向 | 2001 诺贝尔物理学奖共享 |
| advisor-student | Martin Zwierlein | Ketterle→学生 | 博士生，费米子分子凝聚合作者 |
| advisor-student | Zoran Hadzibabic | Ketterle→学生 | 博士生 |
| spouse | Michèle Plott | 无向 | 2011 年结婚 |
| spouse | Gabriele Ketterle | 无向 | 1985–2001 婚姻，育三子 |

> 方向约定：导师有向（对方为师）；学生有向（对方为生）；同事/共同荣誉/配偶无向。

### 第 5 步：设计配色方案

- **气质**：相干、精密、德式沉稳中带迸发
- **配色**：深青绿（主色）+ 诺奖香槟金 `C9A227` + 四分类色
  - `mainclr` 深青绿 `#0E5C4F`
  - `badgeBEC` 玻色–爱因斯坦凝聚 `#2E8B6F`
  - `badgeLaser` 原子激光 `#4C5FD5`
  - `badgeUltra` 超冷原子 `#E0A030`
  - `badgeSpec` 分子光谱/超流 `#C4204F`
- **背景母题**：柔和气泡——两组正弦波纹叠加出干涉条纹，呼应"相干物质波"

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面右上肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. 封面明示国籍，底部状态栏 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**：左头像 + 右信息网格，事实取自 page.md，不得杜撰。
4. 品牌口径：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列（14 页）

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 原子激光之父 / Wolfgang Ketterle 1957– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — 钠 BEC / 原子激光 / 分子凝聚 / 费米子超流
04  德国岁月：海德堡与慕尼黑 (1957–1986) — 转学、Diplom、MPQ 双导师
05  MPQ 博士：分子光谱 (1982–1986) — Walther/Figger 指导、博后 Garching/海德堡
06  转战 MIT：Pritchard 组 (1990) — RLE、从博后到教职
07  1995：钠原子的玻色–爱因斯坦凝聚（核心贡献页；公式框放概念图式——双波纹干涉条纹示意，page.md 无公式，注明）
08  1997：凝聚体干涉与第一台原子激光
09  BEC 1 装置页 — Commons 实验装置照插图（BEC1.2）
10  2003–2005：分子凝聚与费米子超流
11  荣誉与认可 — Rabi 1997 · London 1999 · Franklin 2000 · Nobel 2001 · 功绩勋章
12  跑者与公知 — 波士顿马拉松、联名致信总统、CEE/RSI
13  遗产：超冷原子量子模拟的奠基者
14  结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表

- 表格页安全负间距：顶部 −0.35cm、arraystretch 0.78–0.82；公式框前 −0.35~−0.55cm；希腊字母一律数学模式；`\foreach` 分隔符必须 ASCII 逗号。

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 只写官方原句，勿缩写为"因 BEC 获奖" |
| 双导师 | 正文明写 Herbert Walther 与 Hartmut Figger 共同指导（frontmatter 只列 Walther），两人都入库为 advisor，勿漏 Figger |
| BEC 归属 | Cornell/Wieman 1995-06 首次实现铷 BEC；Ketterle 同年独立实现**钠** BEC——两篇互补，勿写 Ketterle"最早实现 BEC" |
| 原子激光 | 1997 首次实现（输出耦合 + 干涉实验），勿与 BEC 本身混为一谈 |
| Pritchard 身份 | 1990 年 Ketterle 加入的是 Pritchard 组做博后（colleague），Pritchard 同时是 Cornell 的博士导师，两处 note 勿混 |
| 两段婚姻 | Gabriele（1985–2001）与 Michèle Plott（2011–）都按 page.md 明载入库，note 写清年份 |
| Heineman 奖 | 是哥廷根 Dannie Heineman Prize，与美国 Heineman（天文）不同源，note 需区分 |
| 在世留白 | 在世人物 death_date 省略 |
| 联名信 | 2008 致函 Bush 属公共事务记录，客观一句，勿政治化引申 |

### 第 9 步：术语审查清单

| 英文 | 中文 | 风险 |
|------|------|------|
| atom laser | 原子激光 | 相干物质波输出，非光学激光 |
| output coupler | 输出耦合器 | 1997 PRL 主题 |
| interference between two condensates | 两凝聚体的干涉 | 相干性直接证据 |
| spinor condensate | 自旋凝聚体 | infobox Known for 之一 |
| fermionic condensate | 费米子凝聚 | 2005 超流证据页注意归属团队 |
| molecular Bose condensate | 分子玻色凝聚 | 2003 |
| RLE | 电子学研究实验室 | MIT 机构，不翻译 |
| Center for Ultracold Atoms | 超冷原子中心 | 2006 起任主任 |
| Dannie Heineman Prize (Göttingen) | 哥廷根海涅曼奖 | 区分美国 Heineman 奖 |
| John D. MacArthur Professor | MacArthur 讲席教授 | 1998 起的 MIT 荣衔 |

---

## 四、背景音乐选择 ✅

- **选定曲目**：**Expedition** — Alex-Productions（66k views，探索/史诗）
- **匹配理由**："远征式叙事"贴合从海德堡到加兴再到 MIT、从分子光谱到原子激光的迁跃轨迹；史诗底色匹配原子激光的开创性。
- **本地路径**：`music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav` → 复制为 `presentations/21th_century/Wolfgang_Ketterle/Expedition.wav`
- **备选**：Ascension（上升/科幻）、Daylight

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Wolfgang_Ketterle/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 幂等入库引擎 |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
