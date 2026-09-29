# 物理学家立传提示词（Gérard Mourou）

> 本文件是 OpenPhysicist 21 世纪诺贝尔物理学奖得主的「人物专属立传提示词」。
> 目标人物：Gérard Mourou（2018 诺贝尔物理学奖，啁啾脉冲放大 CPA 共同发明人，「极端光」先驱）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节）。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Gérard Albert Mourou（热拉尔·阿尔贝·穆鲁），2018 年诺贝尔物理学奖（与 Strickland 共享一半），超快光学与强激光的开创者。
- **设计哲学**：保留「身份信息页 + 结构化研究领域」骨架；Mourou 篇叙事主线是「把激光变强再变短」—— CPA 让最短、最强的激光束成为可能。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Gérard Albert Mourou（1944-06-22 生于法国阿尔贝维尔，Occupied France；在世）
- **气质关键词**：**极端光的布道者、超快光学奠基人、跨洋四十年的激光远征者**
- **官方获奖理由（2018，与 Strickland 共享一半）**：
  > "for their method of generating high-intensity, ultra-short optical pulses"（因产生高强度超短光脉冲的方法）
  - 另一半授予 Arthur Ashkin（光镊）；本篇提及但重心在 CPA。
- **设计母题**：**脉冲的拉伸与压缩（stretch–amplify–compress）**。CPA 三步节奏是天然的视觉语言——先展宽、再放大、后压缩成阿秒级尖峰。
- **本地数据源**：`physicist/presentations/21th_century/21st_century/Gérard_Mourou/page.md`（**已有本地**）
- **待下载**：`{Dir}.html` 与 `images/` 肖像待下载；Wikipedia URL：`https://en.wikipedia.org/wiki/Gérard_Mourou`
- **参考模板**：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属，已按 page.md 核对】

- **生卒**：1944-06-22 生于法国阿尔贝维尔（被占领法国）；在世（death_date 留白）
- **国籍**：法国（后长期在美任教，2024 年回北京大学任讲席教授；国籍口径写 France）
- **教育**：格勒诺布尔大学（Grenoble Alpes）BSc、MSc → 皮埃尔与玛丽·居里大学（巴黎六大）PhD 1973
- **博士导师**：page.md 无载（infobox 无 doctoral_advisor 字段），**禁写**
- **博士后**：加州大学圣迭戈分校（UC San Diego）一年
- **任职机构**：罗切斯特大学教授 1977（Laboratory for Laser Energetics，1980s 与学生 Strickland 完成 CPA）→ 密歇根大学 1988（1990 或 1991 年创建超快光学科学中心 CUOS 任创始主任）→ 回法国任 École polytechnique 教授、ENSTA 应用光学实验室（LOA）主任 2005–2009 → 2007 起推动 Extreme Light Infrastructure（ELI）→ 2024-10 受聘北京大学讲席教授；密歇根大学 A. D. Moore 杰出荣休教授；机构名单另含下诺夫哥罗德罗巴切夫斯基国立大学
- **关键荣誉**：Nobel 2018；R. W. Wood Prize 1995；SPIE Harold E. Edgerton Award 1997；NAE 院士 2002；IEEE Quantum Electronics Award 2004；Willis E. Lamb Award 2005；Charles Hard Townes Award 2009；Frederic Ives Medal 2016；Berthold Leibinger Zukunftspreis 2016；Arthur L. Schawlow Prize 2018；荣誉博士：维尔纽斯大学 2020、保加利亚科学院 2020-02-25、拉瓦尔大学（frontmatter）；法兰西荣誉军团骑士勋章（frontmatter）；Lazare-Carnot Prize、IEEE David Sarnoff Award（frontmatter，正文无年份）
- **知名学生**：Donna Strickland（infobox Doctoral students 明载；博士论文 *Development of an ultra-bright laser and an application to multi-photon ionization*）
- **核心贡献清单**：
  1. 啁啾脉冲放大（CPA，与 Strickland 共同发明）——「产生高强度、超短光脉冲的方法」，Strickland 首篇论文即此
  2. 拍瓦（petawatt）级超短脉冲激光——最短、最强激光束之路
  3. 1994 密歇根团队发现太瓦级激光在大气中的「丝化」（filament）：Kerr 自聚焦与电离/稀疏化自衰减衍射的平衡形成波导，阻止发散
  4. 阿秒脉冲可行性——CPA 原则上可产生仅持续一阿秒的脉冲，可研究化学反应乃至原子内部
  5. ELI（Extreme Light Infrastructure）项目的推动者
- **关键时间线（16 节点）**：1944 生于阿尔贝维尔 → 格勒诺布尔本科/硕士 → 1973 巴黎六大博士 → 1973-74 UCSD 博士后 → 1977 罗切斯特教授 → 1980s 与 Strickland 发明 CPA → 1985 CPA 论文（Strickland 首篇论文）→ 1988 密歇根大学 → 1990/91 CUOS 创始主任 → 1994 丝化发现 → 2002 NAE 院士 → 2005–2009 ENSTA LOA 主任 → 2007 ELI 启动 → 2018-10-02 获诺奖 → 2018-12-08 诺奖演讲 *Passion for Extreme Light: for the greatest benefit to human kind* → 2024-10 北京大学讲席教授

### 第 4 步：研究领域表 【人物专属，与 yaml fields 一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | ultrafast optics | 超快光学 | 阿秒/飞秒脉冲，CUOS 主任 | 核心贡献页 |
| 1 | chirped pulse amplification | 啁啾脉冲放大 | 2018 诺奖核心技术，Strickland 首篇论文 | 核心贡献页 |
| 2 | nonlinear optics | 非线性光学 | Kerr 自聚焦、丝化 | 丝化页 |
| 3 | laser physics | 激光物理 | 高强度拍瓦脉冲 | 极端光页 |
| 4 | applied optics | 应用光学 | 激光加工、激光视力矫正、癌症治疗前景 | 应用页 |

### 第 4.5 步：社会关系表 【人物专属，与 yaml relations 一致；只收 page.md 明载】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Donna Strickland | 师→生 | 罗切斯特时期博士生，CPA 共同发明人，2018 诺奖共享 |
| co-honored | Donna Strickland | 无向 | 2018 诺贝尔物理学奖共享（两人共享一半，Ashkin 得另一半） |
| co-honored | Arthur Ashkin | 无向 | 2018 诺贝尔物理学奖共享（同上） |

> 博士导师 page.md 无载，禁编造；团队其他成员未具名，不入库。

### 第 5 步：配色方案 【人物专属】

- **气质**：炽烈、极快、穿透
- **主色**：深绛红 `#7A1E28`（极端光的能量与强度）+ 诺奖香槟金 `C9A227`
  - `badgeCPA` 啁啾脉冲放大 — 琥珀 `#E07B30`
  - `badgeUltra` 超快光学 — 电光青 `#0E7C9B`
  - `badgeFilament` 丝化/强场 — 玫瑰 `#C4204F`
  - `badgeApp` 应用 — 苔绿 `#3E7C4F`
- **背景母题**：柔和气泡 + 一条由宽到窄再尖峰化的光线（对应 stretch–amplify–compress）

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + 细边框 + 姓名小字注）；无真实肖像则用装饰圆占位。
2. 封面有国籍；底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. 必须有身份信息页（封面之后、核心贡献之前）。
4. 结尾页品牌标注统一 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 极端光先驱 / Gérard Mourou 1944– + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像/装饰圆 + 右信息网格（生卒、出生地、教育、任职、荣誉、核心领域）
03  核心贡献概览 — CPA / 拍瓦脉冲 / 丝化 / ELI
04  阿尔贝维尔到巴黎 (1944–1973) — 格勒诺布尔、巴黎六大博士
05  跨越大西洋 (1973–1977) — UCSD 博士后、罗切斯特上任
06  罗切斯特岁月：CPA 诞生 (1977–1988) — LLE、与 Strickland 的合作（核心贡献页，公式框放脉冲展宽-放大-压缩三段概念图式或功率放大示意）
07  密歇根：超快光学中心 (1988–2005) — CUOS 创始主任、1994 丝化发现
08  CPA 之后的世界 — 拍瓦激光、阿秒脉冲、原子内部
09  回到法国：LOA 与 ELI (2005–) — École polytechnique、ENSTA、极端光基础设施
10  2018 诺贝尔奖 — 与 Strickland 共享一半、Ashkin 另一半
11  荣誉与认可 — Wood 1995 · Townes 2009 · Ives 2016 · Schawlow 2018 · NAE
12  遗产与应用 — 激光加工、视力矫正、癌症治疗前景
13  东方新章 — 北京大学讲席教授 (2024)
14  结尾
```

### 第 7–8 步：版式要点 + 陷阱表 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 获奖份额 | Mourou 与 Strickland **共享一半**，Ashkin 得另一半；勿写成三人平分 |
| 获奖理由 | 官方措辞 "for their method of generating high-intensity, ultra-short optical pulses"；勿写「因发明激光」 |
| CPA 论文年份 | CPA 是 Strickland 的**首篇科学论文**（1985）；正文未给年份，如需写年份须另行核实，否则写「1980s 于罗切斯特 LLE」 |
| CUOS 年份 | page.md 原文作 "in 1990 or 1991"——两说并存，写「1990 或 1991」或择一加注，勿断言单一年份 |
| 博士导师 | page.md 无载，**禁写**；教育履历只写到格勒诺布尔 + 巴黎六大 |
| Strickland 关系 | 既是 Mourou 的博士生（infobox + 正文 "his then student"），又是共同获奖者——两行关系并列，勿合并 |
| 丝化机制 | 1994 年发现：Kerr 自聚焦折射 vs 电离/稀疏化自衰减衍射的平衡形成丝状波导；勿简化为「激光自聚焦」 |
| 争议视频 | 2018 获奖时 2010 年 ELI 宣传片引发批评（诺奖委员会亦批评其对女性科学家的呈现）；Mourou 回应 "I am not very proud of this video"——如写须客观一句带过，勿展开渲染 |
| 荣誉年份 | R.W. Wood 1995、Edgerton 1997、NAE 2002、Quantum Electronics 2004、Lamb 2005、Townes 2009、Ives 2016、Leibinger 2016、Schawlow 2018——Ives/Leibinger 同为 2016 勿漏一个 |
| Sarnoff/Lazare-Carnot/军团骑士 | 仅 frontmatter 有载、正文无年份；幻灯片如列须写「年份不详」或省略 |
| 下诺夫哥罗德 | 机构名单含下诺夫哥罗德罗巴切夫斯基国立大学，正文无展开；可列机构不展开叙事 |

### 第 9 步：术语审查 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| chirped pulse amplification (CPA) | 啁啾脉冲放大 | 勿译「啁啾放大」丢 pulse |
| ultrashort optical pulses | 超短光脉冲 | 获奖理由原词 |
| petawatt | 拍瓦 | 10^15 瓦 |
| attosecond | 阿秒 | 10^-18 秒 |
| Kerr effect | 克尔效应 | 自聚焦折射的来源 |
| filamentation | 丝化 | 自聚焦与衍射的平衡 |
| waveguide | 波导 | 丝的角色 |
| stretch–amplify–compress | 展宽–放大–压缩 | CPA 三步 |
| Extreme Light Infrastructure (ELI) | 极端光基础设施 | 欧洲大科学装置 |
| laser machining | 激光加工 | CPA 应用 |
| multi-photon ionization | 多光子电离 | Strickland 博士论文应用 |

---

## 四、背景音乐建议 【人物专属】

- **选定曲目**：**Last Hope** — Victor Cooper（戏剧性/力量/史诗）
- **匹配理由**：「革命性突破」匹配 CPA 从罗切斯特实验室走向拍瓦/阿秒极端光的爆发力；2:51 时长适合 15 页节奏。
- **备选**（未采用）：Cinematic Experience（电影感强，但更匹配定理证明类高潮）；Ascension（上升感，弱于「突破」叙事）。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Gérard_Mourou/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Gérard_Mourou.yaml` | 社会关系/领域入库数据 |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
