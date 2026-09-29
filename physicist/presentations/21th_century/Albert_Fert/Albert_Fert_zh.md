# 物理学家立传提示词（Albert Fert）

> 本文件是 OpenPhysicist 21 世纪批次人物专属立传提示词，目标人物：Albert Fert（2007 诺贝尔物理学奖，巨磁电阻 GMR / 自旋电子学）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Albert Fert（阿尔贝·费尔）。
- **设计哲学**：物理学家立传必须有「身份信息页」+「研究领域」结构化表达，此骨架务必保留。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Albert Fert（1938-03-07 生于法国卡尔卡松，在世）
- **气质关键词**：**巨磁电阻的共同发现者、自旋电子学之父、斯格米子的开拓者** —— 2007 诺贝尔物理学奖获奖理由（与 Peter Grünberg 共享）：
  > "for the discovery of Giant Magnetoresistance"（因发现巨磁电阻效应）
- **设计母题**：**自旋的双通道（two spin channels）**。GMR 的本质是电子自旋相对磁化方向取向不同导致散射率迥异——自旋向上/向下两条并联电阻通道随磁层排列在「高阻/低阻」间切换；这正是硬盘读取头与 MRAM 存储的物理根基。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Albert_Fert/page.md`（已有本地）
- **第 0 步素材状态**：`Albert_Fert.html` 与 `images/` **待下载**；Wikipedia URL：`https://en.wikipedia.org/wiki/Albert_Fert`
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ✅ page.md 已有本地（frontmatter + infobox + 正文已核对，事实基准如下）
- 🔲 待下载：`https://en.wikipedia.org/wiki/Albert_Fert` → `Albert_Fert.html`；肖像（infobox 照片，Fert in 2008）→ `images/`
- **事实基准**（全部取自 page.md）：
  - 生卒：1938-03-07 生于法国卡尔卡松；在世（death_date 留白）
  - 国籍：法国
  - 教育：1962 巴黎高等师范学院（ENS）毕业，求学时听过 Alfred Kastler 与 Jacques Friedel 的课程（本科嗜好摄影与电影，崇拜 Ingmar Bergman）；Grenoble 大学深造；1963 巴黎大学博士（doctorat de troisième cycle，论文在 Orsay 理学部基础电子学与 Grenoble 物理光谱实验室完成）；1970 国家博士（doctorat des sciences）
  - 博士导师：两阶段两说——infobox 作 Ian Campbell；frontmatter 作 Pierre Averbuch（详见陷阱表）
  - 任职：1965 服完兵役回 Orsay 任巴黎十一大助理教授；1976 正教授；1970–1995 凝聚态物理实验室研究主任；后转 CNRS/Thales 联合实验室（Unité Mixte de Physique）任科学主任；Paris-Saclay 荣休教授；Michigan State University 兼职教授
  - 关键荣誉（含年份）：APS International Prize for New Materials 1994；Jean Ricard Prize 1994；IUPAP Magnetism Award 1994；Hewlett-Packard Europhysics Prize 1997；法国科学院院士 2004；CNRS Gold Medal 2003；Gutenberg Lecture Award 2006；Wolf Prize 2006；Japan Prize 2007（与 Grünberg 共享，30 万欧元）；**Nobel 2007**；Gay-Lussac Humboldt Award 2014；荣誉军团统帅勋章（Commander）；另有多校荣誉博士（Kaiserslautern 2006、Zagreb、Zaragoza、巴塞罗那自治、蒙特利尔、亚琛、巴斯克、鲁汶、Bar-Ilan、都柏林三一）
  - 知名学生：page.md 无载（勿写）
  - 核心贡献清单（4–6 条）：①1988 与 Grünberg 各自独立发现磁性多层膜的巨磁电阻（GMR）——自旋电子学诞生的标志；②GMR 读取头使硬盘存储密度大幅提升；③铁磁/金属输运理论：镍、铁的电阻各向异性与自旋相关散射（1970 国家博士）；④诺奖后开拓表面/界面拓扑自旋电子学；⑤斯格米子（skyrmions）与拓扑绝缘体的电荷流-自旋流转换
  - 关键时间线（15–20 节点）：1938 生于卡尔卡松 → 1962 ENS 毕业 → 1963 巴黎大学第三周期博士 → 1962–1965 Grenoble + Orsay → 1965 兵役归来任 Orsay 助理教授 → 1970 国家博士（Campbell 指导，镍铁输运）→ 1970–1995 凝聚态实验室研究主任 → 1976 正教授 → 1988 发现 GMR（与 Jülich 的 Grünberg 同期独立）→ 1994 三奖连获（APS 新材料/Jean Ricard/IUPAP）→ 1997 Europhysics Prize → 2003 CNRS 金质奖章 → 2004 法国科学院院士 → 2006 Wolf Prize → 2007 Japan Prize + Nobel（与 Grünberg）→ 后诺奖时代拓扑自旋电子学 → 转入 CNRS/Thales 联合实验室科学主任 → Paris-Saclay 荣休 + Michigan State 兼职

### 第 0.5 步：事实核对清单（执行立传前逐项打勾，page.md ↔ 本提示词）【人物专属】

- [ ] 1938-03-07 生于法国卡尔卡松；在世（death_date 留白）
- [ ] 1962 ENS（巴黎高师）毕业；求学时听过 Kastler 与 Friedel 的课程（仅听课，不入关系库）
- [ ] 本科嗜好摄影与电影，崇拜 Ingmar Bergman
- [ ] Grenoble 大学深造；1963 巴黎大学博士（doctorat de troisième cycle；frontmatter 导师 Pierre Averbuch）
- [ ] 1965 兵役归来任 Orsay（巴黎十一大）助理教授
- [ ] 1970 国家博士（doctorat des sciences；infobox+正文导师 Ian Campbell，固体物理实验室，镍铁电输运）
- [ ] 1976 正教授；1970–1995 凝聚态物理实验室研究主任
- [ ] 后转 CNRS/Thales 联合实验室（Unité Mixte de Physique）科学主任
- [ ] Paris-Saclay 荣休教授；Michigan State University 兼职教授
- [ ] 1988 与 Jülich 的 Grünberg 同期独立发现 GMR——自旋电子学诞生标志
- [ ] GMR 读取头→硬盘存储密度跃升；MRAM 为另一应用
- [ ] 1994 三奖：APS International Prize for New Materials（frontmatter 名 McGroddy Prize）/ Jean Ricard / IUPAP Magnetism Award
- [ ] 1997 Hewlett-Packard Europhysics Prize（frontmatter 名 EPS Europhysics Prize，同一奖）
- [ ] 2003 CNRS Gold Medal；2004 法国科学院院士
- [ ] 2006 Gutenberg Lecture Award + Wolf Prize
- [ ] 2007 Japan Prize（与 Grünberg 共享，30 万欧元）+ 诺贝尔物理学奖
- [ ] 2014 Gay-Lussac Humboldt Award
- [ ] 晚近：skyrmions、拓扑绝缘体的电荷流-自旋流转换
- [ ] 荣誉博士多校：Kaiserslautern 2006 / Zagreb / Zaragoza / 巴塞罗那自治 / 蒙特利尔 / 亚琛 / 巴斯克 / 鲁汶 / Bar-Ilan / 都柏林三一
- [ ] 军团勋章：Commander（统帅级）+ Grand Officer（大军官级）
- [ ] 数字口径：Japan Prize 奖金 30 万欧元（page.md 欧式千分位写法 300.000 Euro，中译勿写成 30 万欧元以上或 3 万欧元）

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/21th_century/` 下创建 `Albert_Fert/` 与 `images/`（第 0 步已建则复用）

### 第 2 步：复制 Makefile 【模板通用】

- 复制标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设置 `MAIN=Albert_Fert_zh`、`VIDEO_NAME=Albert_Fert_zh`

### 第 3 步：收集图片 【人物专属，待下载】

- 肖像：Wikipedia infobox「Fert in 2008」照片 → `images/portrait.jpg`；下载后 `file` 验证为真实图片（JFIF density 1x1 异常时用 sips 改 72dpi，防 xelatex Dimension too large）
- Commons 直链 404 时回退：Wikipedia REST API `page/summary` 查 infobox 原图名，或 `Special:FilePath/<文件名>?width=600`
- 可选插图：Fe/Cr 多层膜剖面示意 / 双电流模型并联电阻图 / 硬盘 GMR 读取头示意

### 第 3.5 步：示意图规划 【人物专属】

- 核心页 07 的双电流模型：自绘 tikz（两通道电阻 R↑ 与 R↓ 并联，磁层箭头平行/反平行两态并置），勿抓网上版权图
- GMR 示意：Fe/Cr/Fe 三明治 + 磁化箭头方向切换；色带用本篇 badgeGMR 钢蓝与 badgeSpin 琥珀
- 若版面紧张：示意图与公式框二选一，保留公式框

### 第 9.5 步：交付前自查清单 【模板通用，第 9 步完成后逐项核对】

- [ ] 编译 0 error；vbox ≤ 10pt、hbox ≤ 50pt（取真实 xelatex 日志核对，勿被 latexmk -c 误判）
- [ ] 页数与第 6 步规划一致（pdfinfo 数页数，页数不符 = 可能有帧未渲染或被合并）
- [ ] 逐页 pdftoppm 目检溢出/重叠；修复优先级：删 \plainbar → 缩 inner sep → 缩字号 → 减行距
- [ ] 引语逐条对照白名单；陷阱表「无载禁写」逐条核对
- [ ] 批内主色互查不重复；BGM 曲名批内唯一
- [ ] 术语清单中译逐条核对；结尾页品牌口径 OpenMathAI

### 第 4 步：研究领域梳理 + 入库 【人物专属内容】

**Fert 的研究领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | condensed matter physics | 凝聚态物理 | 职业主线（Orsay 固体物理实验室） | 身份页 |
| 1 | spintronics | 自旋电子学 | GMR 开创的新子领域，应用硬盘/MRAM | 核心页 |
| 2 | magnetism | 磁学 | 磁性多层膜、铁磁输运 | 核心贡献页 |
| 3 | magnetic multilayers | 磁性多层膜 | GMR 发现的物质载体 | 核心贡献页 |
| 4 | topological materials | 拓扑材料 | 拓扑绝缘体、斯格米子（晚期工作） | 晚近页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属内容，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Ian Campbell | 师→生（博士导师） | 巴黎十一大固体物理实验室国家博士导师（1970，镍铁电输运） |
| advisor-student | Pierre Averbuch | 师→生（博士导师） | 1963 第三周期博士导师（frontmatter 记载） |
| co-honored | Peter Grünberg | 无向 | 2007 诺贝尔物理学奖共享（GMR 各自独立发现）与 2007 Japan Prize 共享 |

- 仅收 page.md 明载关系；ENS 听课的 Kastler / Friedel 仅是授课教师（无师承/合作明载），一律不做关系入库。

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：冷峻、精密、金属质感
- **配色**：深松绿（主色）+ 香槟金（诺奖 `C9A227`）+ 四分类色
  - 主色 `mainclr` 深松绿 `#1B4D3E`
  - `badgeGMR` 巨磁电阻 — 钢蓝 `#2E5E8C`
  - `badgeSpin` 自旋电子学 — 琥珀 `#D08A2E`
  - `badgeSkyrmion` 斯格米子 — 玫瑰 `#C2466B`
  - `badgeTransport` 输运理论 — 紫灰 `#5C4A72`
- **批内主色查重**：#1B4D3E 仅本篇使用（Mather #0F3057 / Smoot #8C2F39 / Grünberg #2F4F4F / Nambu #4E3D6E）
- **背景母题**：深底上两组交替取向的平行磁条带（红蓝双色箭头层），呼应「平行 vs 反平行磁化 → 低阻 vs 高阻」的 GMR 物理图像

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 自旋电子学之父 / Albert Fert 1938– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地、教育、师承、任职、荣誉、核心领域）
03  核心贡献概览 — GMR / 自旋电子学 / 磁性多层膜 / 斯格米子
04  早年：卡尔卡松到 ENS (1938–1962) — 摄影与电影、Kastler/Friedel 的课堂
05  两段博士：Grenoble-Orsay (1963) 与国家博士 (1970) — Campbell 指导、镍铁输运
06  Orsay 固体物理实验室 (1965–1995) — 助理教授到正教授、研究主任
07  1988：巨磁电阻的诞生（核心贡献页一，公式框放双电流模型并联电阻 R = R↑R↓/(R↑+R↓) 概念式）
08  从 GMR 到硬盘革命 — 读取头、存储密度、spintronics 子领域
09  2007 诺贝尔奖 — 与 Grünberg 各自独立发现、Japan Prize 同年共享
10  CNRS/Thales 时代 — Unité Mixte de Physique 科学主任
11  拓扑自旋电子学 — 斯格米子、拓扑绝缘体电荷-自旋转换
12  荣誉与认可 — CNRS 金质奖章 2003 · Wolf 2006 · Nobel 2007 · 荣誉军团勋章
13  遗产：自旋电子学的开枝散叶
14  结尾
```

### 第 7–8 步：版式要点 + 该人专属陷阱表 【人物专属】

- 版式复用标杆骨架（`\plainbar` / `\deckbackground` / `\profileslide`）；每写一页 make 并截图查溢出。
- **Fert 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 双博士两导师 | 1963 第三周期博士（frontmatter 作 Pierre Averbuch）与 1970 国家博士（infobox+正文作 Ian Campbell）是两个学位、两条记录；入库各建一行并注明对应学位，勿混成一人或互相覆盖 |
| GMR 归属 | 1988 Fert（Orsay）与 Grünberg（Jülich）**同期独立**发现，勿写「Fert 最早/Grünberg 最早」或任何师承/主从关系 |
| 获奖理由 | 官方 "for the discovery of Giant Magnetoresistance"；「开创自旋电子学」是影响表述，不在 citation 原文内 |
| 1994 三奖 | APS 新材料奖（frontmatter 名 James C. McGroddy Prize）、Jean Ricard、IUPAP Magnetism Award 同年三获，勿漏或混并 |
| Europhysics Prize | 正文作 Hewlett-Packard Europhysics Prize (1997)，frontmatter 作 EPS Europhysics Prize，同一奖的两称 |
| Japan Prize | 2007 与 Grünberg 共享（30 万欧元），infobox 措辞 Japan Award，同一奖 |
| 名字写法 | 正文另作 Gruenberg 拼写一次，规范用 Peter Grünberg |
| 在世口径 | 1938 生、在世，death_date 留白 |
| 亲属/师承 | page.md 无子女、无博士生记载，门生/家庭页禁写 |
| 法国学制 | doctorat de troisième cycle ≠ doctorat d'État（国家博士），勿统一译作「博士」而不加区分 |

---

## 四、背景音乐建议 【人物专属】

- **选定曲目**: **Through the Darkness** — Audiomachine（史诗 / 推进）
- **匹配理由**: 从铁磁输运的长期沉默积累到 1988 年多层膜里的关键一测，是「突破前夕」的暗夜叙事；「推进」标签贴合 GMR 从实验室到硬盘产业的势能释放。
- **批内查重**: Through the Darkness 仅本篇使用（Mather=Expedition / Smoot=The Invisible Light / Grünberg=New Lands / Nambu=Eternals）
- **本地路径**: `music_audio/inspiring-electronic/14-Trn1cSsY2t8-Audiomachine - Through the Darkness.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Albert_Fert/page.md` | 本地事实基准 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `MySQL/data/Albert_Fert.yaml` | 社会关系入库源 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
