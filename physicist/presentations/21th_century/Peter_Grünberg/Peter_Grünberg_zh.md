# 物理学家立传提示词（Peter Grünberg）

> 本文件是 OpenPhysicist 21 世纪批次人物专属立传提示词，目标人物：Peter Andreas Grünberg（2007 诺贝尔物理学奖，巨磁电阻 GMR）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Peter Andreas Grünberg（彼得·安德烈亚斯·格林贝格）。
- **设计哲学**：物理学家立传必须有「身份信息页」+「研究领域」结构化表达，此骨架务必保留。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Peter Andreas Grünberg（1939-05-18 生于比尔森 ~ 2018-04-07 逝于德国于利希，享年 78 岁）
- **气质关键词**：**巨磁电阻的共同发现者、层间耦合的先行者、应用物理的发明家** —— 2007 诺贝尔物理学奖获奖理由（与 Albert Fert 共享）：
  > "for the discovery of Giant Magnetoresistance"（因发现巨磁电阻效应）
- **设计母题**：**夹层中的自旋阀（the spin valve）**。Fe/Cr 交替多层膜中，非磁间隔层两侧铁磁层的「平行/反平行」排列像阀门一样开关电子通道——1986 年他先发现反平行交换耦合，1988 年才水到渠成测得 GMR。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Peter_Grünberg/page.md`（已有本地）
- **第 0 步素材状态**：`Peter_Grünberg.html` 与 `images/` **待下载**；Wikipedia URL：`https://en.wikipedia.org/wiki/Peter_Gr%C3%BCnberg`
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ page.md 已有本地（frontmatter + infobox + 正文已核对，事实基准如下）
- 🔲 待下载：`https://en.wikipedia.org/wiki/Peter_Gr%C3%BCnberg` → `Peter_Grünberg.html`；肖像（infobox 照片，Grünberg in 2009；另有拉吉他照片可用）→ `images/`
- **事实基准**（全部取自 page.md）：
  - 生卒：1939-05-18 生于比尔森（Plzeň，时属波希米亚和摩拉维亚保护国，今捷克）~ 2018-04-07 逝于德国于利希（北莱茵-威斯特法伦），享年 78 岁
  - 国籍：德国
  - 家庭：苏台德德裔家庭，父母 Anna 与 Feodor A. Grünberg（父为俄国出生的工程师，1928 起任职 Škoda，1945-11-27 死于捷克拘押、葬于比尔森万人坑）；母亲 2002 年去世（享年 100）；姐姐生于 1937；1946 全家被逐出捷克斯洛伐克，7 岁的 Peter 落脚黑森州 Lauterbach；天主教徒；在 Darmstadt 结识并娶 Helma Prauser（后任中学教师）
  - 教育：1962 法兰克福歌德大学中期文凭；1966 TU Darmstadt 物理学 BSc 文凭；1969 TU Darmstadt PhD
  - 博士导师：Stefan Hüfner（frontmatter + infobox 明载）
  - 博士后：1969–1972 Carleton University（渥太华）
  - 任职：1972 起于利希研究中心固体物理研究所（薄膜与多层磁学领军研究者，至 2004 退休）；1984–85 Argonne 国家实验室访问学者；1984–92 科隆大学 Habilitation 讲师（Junior Professor）；1992–2004 科隆大学编外正教授（ausserplanmässiger Professor）；1998–2004 东北大学（仙台）访问教授
  - 关键荣誉（含年份）：APS International Prize for New Materials 1994（共享）；IUPAP Magnetism Award 1994（共享）；Hewlett-Packard Europhysics Prize 1997（与 Albert Fert、Stuart Parkin 三人共享）；德国未来奖 1998；马普学会会员 2003；Stern-Gerlach Medal 2006；European Inventor of the Year 2006（「高校与科研机构」类别）；Wolf Prize 2006；Japan Prize 2007；**Nobel 2007**；中国友谊奖 2016；荣誉博士：RWTH Aachen 2007、萨尔大学 2008、Gebze 理工、雅典大学 2009；另获北威州功绩勋章、联邦德国功绩勋章骑士指挥官十字、德国研究名人堂、比尔森市徽章等
  - 知名学生：page.md 无载（勿写）
  - 核心贡献清单（4–6 条）：①1986 发现被非磁薄层隔开的铁磁层间的反平行交换耦合（Fe/Cr 多层膜，PRL）；②1988 发现巨磁电阻效应（GMR），与 Fert 同期独立；③GMR 专利（DE 3820475，1988-06-16 申报「含铁磁薄层的磁场传感器」）；④GMR 读取头推动硬盘容量突破至 GB 量级，MRAM 为另一应用；⑤层间交换耦合振荡（Fe/Al、Fe/Au 隔层，1992）等薄膜磁学系统工作
  - 关键时间线（15–20 节点）：1939 生于比尔森 → 1945 父亲死于拘押 → 1946 被逐出捷克、落脚 Lauterbach → 1962 法兰克福中期文凭 → 1966 Darmstadt 物理文凭 → 1969 Darmstadt PhD（Hüfner）→ 与 Helma Prauser 成婚 → 1969–1972 Carleton 博士后 → 1972 入于利希 → 1984–85 Argonne 访问 → 1984–92 科隆 Habilitation 讲师 → 1986 反平行交换耦合（PRL 57, 2442）→ 1988-06-16 申报 GMR 专利 → 1988 GMR（与 Fert 独立同期）→ 1989 Binasch 等 PRL 39, 4828 → 1992 科隆编外教授 → 1994 双奖 → 1997 Europhysics Prize（Fert/Parkin）→ 1998 德国未来奖 → 1998–2004 东北大学访问教授 → 2003 马普学会会员 → 2004 退休 → 2006 Stern-Gerlach + 发明家年奖 + Wolf → 2007 Japan Prize + Nobel → 2016 中国友谊奖 → 2018-04-07 卒于于利希

### 第 0.5 步：事实核对清单（执行立传前逐项打勾，page.md ↔ 本提示词）【人物专属】

- [ ] 1939-05-18 生于比尔森（Plzeň，时属波希米亚和摩拉维亚保护国，今捷克）；2018-04-07 卒于于利希（78 岁）
- [ ] 苏台德德裔；父 Feodor A. Grünberg（俄 born 工程师，1928 起任职 Škoda）1945-11-27 死于捷克拘押、葬比尔森万人坑
- [ ] 母 Anna（2002 年去世，享年 100）；姐姐 1937 年生；1946 全家被逐出捷克斯洛伐克，落脚黑森州 Lauterbach；天主教徒
- [ ] 1962 法兰克福歌德大学中期文凭；1966 TU Darmstadt 物理学 BSc 文凭；1969 TU Darmstadt PhD
- [ ] 博士导师 Stefan Hüfner；在 Darmstadt 结识并娶 Helma Prauser（后任中学教师）
- [ ] 1969–1972 Carleton University（渥太华）博士后
- [ ] 1972 起于利希研究中心固体物理研究所（薄膜与多层磁学领军研究者，至 2004 退休）
- [ ] 1984–85 Argonne 国家实验室访问学者；1984–92 科隆 Habilitation 讲师；1992–2004 科隆编外正教授；1998–2004 东北大学（仙台）访问教授
- [ ] 1986 反平行交换耦合（Fe/Cr 多层膜，PRL 57, 2442）——先于 GMR 的独立发现
- [ ] 1988-06-16 申报 GMR 专利（DE 3820475）；1988 发现 GMR（与 Fert 同期独立）
- [ ] 1994 双奖共享（APS 新材料 + IUPAP）；1997 Europhysics Prize（Fert/Grünberg/Parkin 三人）；1998 德国未来奖；2003 马普学会会员
- [ ] 2006 Stern-Gerlach Medal + European Inventor of the Year + Wolf；2007 Japan Prize + Nobel；2016 中国友谊奖
- [ ] 荣誉博士：RWTH Aachen 2007 / 萨尔大学 2008 + Gebze / 雅典大学 2009；另获北威州功绩勋章、联邦功绩勋章骑士指挥官十字等

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/21th_century/` 下创建 `Peter_Grünberg/` 与 `images/`（第 0 步已建则复用）

### 第 2 步：复制 Makefile 【模板通用】

- 复制标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设置 `MAIN=Peter_Grünberg_zh`、`VIDEO_NAME=Peter_Grünberg_zh`

### 第 3 步：收集图片 【人物专属，待下载】

- 肖像：Wikipedia infobox「Grünberg in 2009」照片 → `images/portrait.jpg`；下载后 `file` 验证（JFIF density 异常时 sips 改 72dpi）
- 备选历史照：演讲中拉吉他照片（page.md 内嵌 commons 图）
- Commons 直链 404 时回退：Wikipedia REST API `page/summary` 查 infobox 原图名，或 `Special:FilePath/<文件名>?width=600`
- 可选自绘插图：Fe/Cr/Fe 三明治剖面 + 磁化箭头两态（tikz）；GMR 专利首页可作史料插图

### 第 9.5 步：交付前自查清单 【模板通用，第 9 步完成后逐项核对】

- [ ] 编译 0 error；vbox ≤ 10pt、hbox ≤ 50pt（取真实 xelatex 日志核对，勿被 latexmk -c 误判）
- [ ] 页数与第 6 步规划一致（pdfinfo 数页数，页数不符 = 可能有帧未渲染或被合并）
- [ ] 逐页 pdftoppm 目检溢出/重叠；修复优先级：删 \plainbar → 缩 inner sep → 缩字号 → 减行距
- [ ] 引语逐条对照白名单；陷阱表「无载禁写」逐条核对
- [ ] 批内主色互查不重复；BGM 曲名批内唯一
- [ ] 术语清单中译逐条核对；结尾页品牌口径 OpenMathAI

### 第 4 步：研究领域梳理 + 入库 【人物专属内容】

**Grünberg 的研究领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | condensed matter physics | 凝聚态物理 | 职业主线（于利希固体物理研究所） | 身份页 |
| 1 | magnetism | 磁学 | 薄膜与多层磁学领军研究者 | 核心页 |
| 2 | spintronics | 自旋电子学 | GMR 读取头 / MRAM 应用根基 | 核心贡献页 |
| 3 | thin film magnetism | 薄膜磁学 | 于利希研究所方向 | 职业页 |
| 4 | magnetic multilayers | 磁性多层膜 | Fe/Cr 反平行耦合与 GMR 载体 | 核心贡献页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Stefan Hüfner | 师→生（博士导师） | TU Darmstadt 博士导师（1969） |
| spouse | Helma Prauser | 无向 | Darmstadt 结识成婚，中学教师 |
| co-honored | Albert Fert | 无向 | 2007 诺贝尔物理学奖共享（GMR 各自独立发现）；1997 Europhysics Prize、2007 Japan Prize 亦共享 |
| colleague | Stuart Parkin | 无向 | 1997 Hewlett-Packard Europhysics Prize 三人共享（与 Fert） |

- 仅收 page.md 明载关系；Zinn 等仅出现在论文作者列表，不做关系入库。

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：冷峻、克制、工程感
- **配色**：深灰绿（主色）+ 香槟金（诺奖 `C9A227`）+ 四分类色
  - 主色 `mainclr` 深灰绿 `#2F4F4F`
  - `badgeCoupling` 层间耦合 — 钢蓝 `#2E5E8C`
  - `badgeGMR` 巨磁电阻 — 琥珀 `#D08A2E`
  - `badgeValve` 自旋阀 — 玫瑰 `#C2466B`
  - `badgeInvent` 发明与专利 — 紫灰 `#5C4A72`
- **批内主色查重**：#2F4F4F 仅本篇使用（Mather #0F3057 / Smoot #8C2F39 / Fert #1B4D3E / Nambu #4E3D6E）
- **背景母题**：深底上 Fe/Cr/Fe 三明治剖面示意——两条铁磁层夹一条间隔层，箭头平行/反平行两态并置

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 巨磁电阻的共同发现者 / Peter Grünberg 1939–2018 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地、教育、师承、任职、荣誉、核心领域）
03  核心贡献概览 — 反平行耦合 / GMR / 专利与硬盘 / MRAM
04  乱世童年：比尔森到 Lauterbach (1939–1946) — 苏台德德裔、父亲之死、被逐
05  求学：法兰克福与 Darmstadt (1962–1969) — Hüfner 门下、与 Helma 成婚
06  博士后与于利希 (1969–) — Carleton、固体物理研究所、薄膜磁学
07  1986：反平行交换耦合（核心贡献页一，概念图式：Fe/Cr/Fe 三明治与磁化箭头）
08  1988：巨磁电阻的诞生（核心贡献页二，公式框放双电流模型并联电阻概念式；专利 DE 3820475）
09  与 Fert：同期独立的诺贝尔奖 — 2007 共享、Japan Prize、Europhysics 三人奖
10  从实验室到硬盘革命 — GMR 读取头、存储密度、MRAM
11  科隆与东北大学 — Habilitation、编外教授、仙台访问教授
12  荣誉与认可 — Stern-Gerlach 2006 · Wolf 2006 · Nobel 2007 · 中国友谊奖 2016
13  遗产：自旋电子学的工程化一翼
14  结尾
```

### 第 7–8 步：版式要点 + 该人专属陷阱表 【人物专属】

- 版式复用标杆骨架（`\plainbar` / `\deckbackground` / `\profileslide`）；每写一页 make 并截图查溢出。
- **Grünberg 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| GMR 归属 | 1988 与 Fert **同期独立**发现（于利希 vs Orsay），勿写先后或主从；两人亦共享 Europhysics 1997 / Japan Prize 2007 |
| 1986 先行工作 | 反平行交换耦合（1986 PRL）先于 GMR（1988），是独立发现节点，勿合并叙述 |
| 出生国表述 | 生于比尔森，时称 Pilsen，属波希米亚和摩拉维亚保护国（今捷克）；正文另提 Czechoslovakia——建议口径「生于今捷克比尔森（时属德占波希米亚和摩拉维亚保护国）」，勿写「生于德国」 |
| 家庭悲剧 | 父亲 Feodor 1945-11-27 死于捷克拘押、葬比尔森万人坑；1946 全家被逐——须客观史述，勿渲染 |
| 妻子 | Helma Prauser，Darmstadt 结识，中学教师；仅此明载，婚后生平勿展开 |
| 获奖理由 | 官方 "for the discovery of Giant Magnetoresistance"；「硬盘读取头」是影响表述，不在 citation 原文内 |
| Europhysics Prize | 1997 为 Fert/Grünberg/Parkin **三人**共享，勿写成双人 |
| Habilitation 与职称 | 科隆 1984–92 是 Habilitation 讲师（Junior Professor），1992 起才是编外正教授（ausserplanmässiger Professor），两阶段勿混 |
| 同奖项年份 |APS 新材料奖与 IUPAP 磁学奖均 1994 共享；德国未来奖 1998 独得（技术与创新类） |
| 学生 | page.md 无博士生记载，门生页禁写 |

### 第 9 步：术语审查 【人物专属】

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| giant magnetoresistance (GMR) | 巨磁电阻 | 获奖理由核心词，勿译「巨磁阻效应」与「巨磁电阻效应」混用 |
| antiparallel exchange coupling | 反平行交换耦合 | 1986 发现，GMR 前置 |
| interlayer exchange coupling | 层间交换耦合 | 振荡周期 Fe/Al、Fe/Au |
| magnetic multilayers | 磁性多层膜 | Fe/Cr 交替结构 |
| spin valve | 自旋阀 | 概念比喻，page.md 未用此词，须注明为通称 |
| read head | 读取头 | 硬盘应用 |
| MRAM | 磁阻式随机存取存储器 | GMR/自旋电子学应用 |
| Habilitation | 特许任教资格 | 德国教授资格制度 |
| ausserplanmässiger Professor | 编外正教授 | 科隆 1992–2004 |
| Forschungszentrum Jülich | 于利希研究中心 | 机构规范译名 |

---

## 四、背景音乐建议 【人物专属】

- **选定曲目**: **New Lands** — Alex-Productions（史诗 / 开阔）
- **匹配理由**: 从战乱流离到于利希的薄膜实验室再到「新大陆」般的 GMR 产业革命，开阔史诗感匹配其跌宕而坚韧的一生；与 Fert 篇（Through the Darkness）形成「暗夜突破 vs 新陆开阔」的呼应。
- **批内查重**: New Lands 仅本篇使用（Mather=Expedition / Smoot=The Invisible Light / Fert=Through the Darkness / Nambu=Eternals）
- **本地路径**: `music_audio/alex-productions/74-oK8HN0FsZmc-New-Lands.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Peter_Grünberg/page.md` | 本地事实基准 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `MySQL/data/Peter_Grünberg.yaml` | 社会关系入库源 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
