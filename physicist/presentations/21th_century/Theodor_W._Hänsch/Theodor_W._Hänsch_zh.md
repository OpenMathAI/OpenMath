# 物理学家立传提示词（21 世纪批次：Theodor W. Hänsch）

> **本文件是 OpenPhysicist 21 世纪诺奖物理学家立传的人物专属提示词**，以 Theodor W. Hänsch（2005 诺贝尔物理学奖，激光精密光谱与光频梳）为对象。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Theodor Wolfgang Hänsch（特奥多尔·亨施），2005 年诺贝尔物理学奖四分之一得主（与 John L. Hall 共享一半，另一半归 Glauber），光频梳之父、马普量子光学研究所所长。
- **设计哲学**：保留「身份信息页」+ 研究领域结构化骨架；Hänsch 篇的设计母题围绕「用最简单的原子追问最深的常数」——氢原子谱线精测 + 基本常数是否随时间漂移，视觉语言可用「氢原子谱线与光尺」。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Theodor Wolfgang Hänsch（1941-10-30 生于德国海德堡，在世）
- **气质关键词**：**光频梳之父、氢原子谱线的守望者、门下诺奖连片的导师**
- **诺奖理由（官方原文，禁止改写）**：
  > "for contributions to the development of laser-based precision spectroscopy, including the optical frequency comb technique"（因对激光精密光谱学的发展（包括光频梳技术）的贡献）
- **设计母题**：**氢之尺**——从 1970 年窄线宽可调谐激光测 Balmer 线，到光频梳把 Lyman 线测到百万亿分之一，再到检验基本常数漂移。
- **本地数据源**：
  - ✅ `physicist/presentations/21th_century/21st_century/Theodor_W._Hänsch/page.md`（已有本地）
  - ⬜ `{Dir}.html` 与 `images/` **待下载**：Wikipedia URL `https://en.wikipedia.org/wiki/Theodor_W._H%C3%A4nsch`
- **参考模板**：`physicist/presentations/cover/openphysicist_page.tex`；骨架复用 20 世纪成品（如 `Kenneth_G_Wilson_zh.tex`）。

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属】

- 生卒：1941-10-30 生于德国海德堡；在世。国籍：德国（frontmatter 另列 United States）。
- 教育：Helmholtz-Gymnasium Heidelberg → 海德堡大学 Diplom 与博士学位（1960 年代）。
- 博士导师：Peter E. Toschek；infobox 另列其他学术导师 Arthur L. Schawlow 与 Christoph Schmelzer。
- 博士后：NATO 博士后研究员，Stanford，与 Arthur L. Schawlow 合作（1970–1972）。
- 任职：Stanford 助理教授（1975–1986）；1986 年回德国执掌马普量子光学研究所（MPQ，Garching）；LMU Munich 实验物理与激光光谱学教授。
- 关键荣誉（节选，均 page.md 明载）：Klung Wilhelmy Science Award（1980）；Herbert P. Broida Award（1983）；Comstock Prize in Physics（1983）；William F. Meggers Award（1985）；Albert A. Michelson Medal（1986）；King Faisal International Prize（1989）；Gottfried Wilhelm Leibniz Prize（1989，德国研究最高荣誉）；Arthur L. Schawlow Prize（1996）；Stern–Gerlach Medal（2000）；Matteucci Medal（2001）；Otto Hahn Prize（2005）；Frederic Ives Medal（2005）；I. I. Rabi Award（2005）；Nobel（2005，四分之一）；Carl Friedrich von Siemens Prize（2006）；Rudolf-Diesel-Medaille（2006）；OSA 荣誉会员（2008）等。
- 知名博士生：Immanuel Bloch、Tilman Esslinger、Markus Greiner、Carl E. Wieman（Wieman 获 2001 诺贝尔物理学奖）。
- 核心贡献清单：
  1. 1970 年发明**窄线宽可调谐激光**（腔内望远镜光束扩束 + 光栅调谐），精测氢原子 Balmer 线
  2. 1990 年代末与团队发明**光学频率梳合成器**（诺奖核心）
  3. 氢 1S–2S 双光子跃迁频率测至 15 位小数；Lyman 线测至百万亿分之一
  4. 据此可搜寻**基本物理常数**是否随时间变化
  5. 激光冷却、灰黏胶（gray molasses）、Vernier 光谱、GBAR 实验
- 关键时间线（15–20 节点）：1941 生海德堡 → Helmholtz-Gymnasium → 1960 年代海德堡大学 Diplom/博士（Toschek 门下）→ 1970 窄线宽可调谐激光 + Balmer 线精测 → 1970–72 Stanford NATO 博士后（Schawlow）→ 1975 Stanford 助理教授 → 1983 Comstock Prize → 1986 Michelson Medal → 1986 回德执掌 MPQ → 1989 Leibniz Prize + King Faisal → 1990 年代末光频梳 → 1998 Philip Morris Research Prize（"测量装置"）→ 2002 起 Menlo Systems 商业化光频梳 → 2005 Otto Hahn Prize + Ives Medal + Rabi Award + 诺贝尔奖（四分之一）→ 2006 Siemens Prize / Rudolf-Diesel → 2008 OSA 荣誉会员 → 晚年推进 GBAR（反氢重力实验）等。

### 第 4 步：研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | laser spectroscopy | 激光光谱学 | 2005 诺奖核心、氢谱精测 | 核心页 |
| 1 | optical frequency metrology | 光学频率计量 | 光频梳合成器 | 频率梳页 |
| 2 | laser cooling | 激光冷却 | 灰黏胶等冷却方案 | 冷却页 |
| 3 | quantum optics | 量子光学 | MPQ 所长、量子光学重镇 | 身份页 |
| 4 | atomic physics | 原子物理 | 氢 1S–2S、基本常数检验 | 氢原子页 |

### 第 4.5 步：社会关系梳理 + 入库 【与 yaml 完全一致，只收 page.md 明载】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Peter E. Toschek | 师→生（博士导师） | 海德堡大学博士导师 |
| advisor-student | Arthur Schawlow | 师→博士后 | Stanford NATO 博士后导师（1970–1972），infobox 列为 other academic advisors |
| advisor-student | Carl E. Wieman | Hänsch→学生 | 博士生，2001 诺贝尔物理学奖得主 |
| advisor-student | Immanuel Bloch | Hänsch→学生 | 博士生，冷原子量子模拟名家 |
| advisor-student | Tilman Esslinger | Hänsch→学生 | 博士生，冷原子名家 |
| advisor-student | Markus Greiner | Hänsch→学生 | 博士生，冷原子名家 |
| co-honored | John L. Hall | 无向 | 2005 诺贝尔物理学奖共同得主（两人共享一半） |
| co-honored | Roy Glauber | 无向 | 2005 诺贝尔物理学奖共同得主（Glauber 得另一半） |

> 入库注意：Schawlow 沿用库内规范名 **`Arthur Schawlow`**（id=2488）；Glauber 用库内 `Roy Glauber`（id=2566）；Hall 已入库（id=3016）；Wieman 由 batch 1 负责（json 名 Carl E. Wieman，frontmatter 同名一致）。

### 第 5 步：设计配色方案 【人物专属】

- **气质**：精密、德国工艺、光尺之美
- **配色**：主色 **光谱金橙 `#8C5A10`**（谱线之光）+ 诺奖香槟金 `C9A227` + 四分类色：
  - `badgeComb` 光频梳 — 靛蓝 `#4C5FD5`
  - `badgeH` 氢原子谱线 — 青绿 `#0E7C7B`
  - `badgeCool` 激光冷却 — 玫瑰 `#C4204F`
  - `badgeMPQ` MPQ 时代 — 琥珀 `#E07B30`
- **背景母题**：等距梳齿与氢原子 Balmer 谱线（红蓝紫三线）。

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + 细边框 + 姓名小字注）；封面有国籍。
2. **必须有身份信息页**：左头像 + 右信息网格（生卒、国籍、出生地、教育、师承、任职、荣誉、核心领域），事实取自 infobox 不得杜撰。
3. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 光频梳之父 / Theodor W. Hänsch 1941– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — 可调谐激光 / 光频梳 / 氢谱精测 / 激光冷却
04  海德堡 (1941–1970) — Toschek 门下、Diplom 与博士
05  Stanford：Schawlow 门下 (1970–1986) — NATO 博士后、1970 窄线宽激光、Balmer 线
06  光频梳（核心贡献页）— 公式框放梳齿频率 f_n = n·f_rep + f_CEO 概念式（page.md 未给显式公式，注明为概念图式）
07  丈量氢原子 — 1S–2S 十五位小数、Lyman 线、基本常数检验
08  MPQ 时代 (1986– ) — Garching、LMU 教授、Menlo Systems
09  门生与传承 — Wieman（2001 诺奖）、Bloch、Esslinger、Greiner
10  荣誉与认可 — Nobel 2005（四分之一）· Leibniz 1989 · Ives 2005 · Comstock 1983
11  遗产：每个实验室都有他的光尺
12  结尾
```

### 第 7–8 步：版式要点 + 陷阱表

- 每写完一页 make，用 pdftoppm 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

**Hänsch 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖份额 | Hänsch 得**四分之一**（与 Hall 共享一半），Glauber 得另一半；勿写"两人平分全奖"或三人平分 |
| 获奖工作地点 | 诺奖表彰的是 1990 年代末在 **MPQ（Garching）** 的工作，非 Stanford 时期 |
| 博士导师 | **Peter E. Toschek**（海德堡）；Schawlow 是**博士后导师**（infobox 列 other academic advisors），两者勿混 |
| Schawlow 类型 | 入库按 advisor-student + note「博士后导师」，勿直接写成博士导师 |
| 学生 | infobox 博士生四人：Bloch / Esslinger / Greiner / Wieman；Wieman 2001 诺奖是"学生获奖"，勿写成"共同获奖" |
| 名字拼写 | 德语 Hänsch（ä）；文献中常见 Hansch 无变音，tex 中注意 ä 渲染 |
| 1970 激光 | 是**窄线宽可调谐激光**（内腔望远镜扩束+光栅调谐），勿写成"发明激光" |
| 光频梳精度 | Lyman 线百万亿分之一（1 part in a hundred trillion）、1S–2S 十五位小数——两个数字勿互换 |
| Philip Morris Prize | 1998 与 2000 两届（frontmatter），正文 1998 与"测量装置"绑定 |
| 奖项取舍 | 荣誉极多（30+），幻灯片只挑代表性 6–8 项，年份必须对表 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| optical frequency comb | 光频梳 | 等距谱线"光尺" |
| frequency comb synthesizer | 光频梳合成器 | MPQ 发明 |
| precision spectroscopy | 精密光谱学 | 诺奖理由核心词 |
| narrow-linewidth tunable laser | 窄线宽可调谐激光 | 1970 年发明 |
| Balmer line | 巴耳末谱线 | 氢原子可见光谱线 |
| Lyman series | 莱曼系 | 紫外谱线 |
| gray molasses | 灰黏胶冷却 | 亚多普勒冷却 |
| laser cooling | 激光冷却 | 勿与 Doppler cooling 混同 |
| fundamental physical constants | 基本物理常数 | 检验其随时间漂移 |
| GBAR experiment | GBAR 实验 | 反氢重力测量 |
| Max-Planck-Institut für Quantenoptik | 马普量子光学研究所 | 缩写 MPQ，Garching |
| Gottfried Wilhelm Leibniz Prize | 莱布尼茨奖 | 德国研究最高荣誉（1989） |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Shine Like The Sun** — Really Slow Motion（史诗 / 美丽 / 振奋）
- **匹配理由**: 「光明、振奋」贴合光频梳把光变成最精密量尺的意象——谱线如阳光色散般铺开。
- **本地路径**: `music_audio/inspiring-electronic/15-w6kT1BfvETI-Really Slow Motion - Shine Like The Sun (Epic Beautiful Uplifting).wav`
- **备注**: 批内曲不重复（前四人用 Savage/Expedition/The Invisible Light/SEA）。

---

## 五、关键参考文件 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Theodor_W._Hänsch/page.md` | 本地 Wikipedia 事实基准 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Theodor_W._Hänsch.yaml` | 社会关系入库 yaml |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
