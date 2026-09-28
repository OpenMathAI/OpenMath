# 物理学家立传提示词（Paul Adrien Maurice Dirac）

> 本文件是 OpenPhysicist 20 世纪诺贝尔物理学奖得主的「人物专属立传提示词」，以 Kenneth G. Wilson 篇为结构母本（0–11 节骨架一致）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Paul Adrien Maurice Dirac（保罗·狄拉克，1933 诺贝尔物理学奖，与 Schrödinger 共享；狄拉克方程、反物质预言、QED 奠基）。
- **设计哲学**：物理学家立传必须有「身份信息页」与结构化「研究领域」表达；Dirac 篇的设计重心是**数学美（mathematical beauty）**——"Physical laws should have mathematical beauty" 是他一生的纲领，立传以极简、精确、留白为视觉语言，呼应其寡言性格。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Paul Adrien Maurice Dirac（1902-08-08 ~ 1984-10-20，享年 82 岁）
- **气质关键词**：**量子力学的第二位立法者、沉默的预言家、数学美的信徒** —— 1933 诺贝尔物理学奖获奖理由（与 Erwin Schrödinger 共享）：
  > "for the discovery of new productive forms of atomic theory"（因发现原子理论的新型富有成果的形式）
- **设计母题**：**对称与对易（symmetry / commutation）**。不满足对易关系的算符、预言反粒子的负解、bra–ket 的左右互文——「成对出现而次序有别」是比单纯「方程」更贴合他思想的视觉语言。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/physicist/presentations/20th_century/20th_century/Paul_Adrien_Maurice_Dirac/page.md`（Wikipedia 全文已抓取）
- **待下载**：本目录尚无 `Paul_Adrien_Maurice_Dirac.html` 与 `images/`，第 0 步需从 `https://en.wikipedia.org/wiki/Paul_Adrien_Maurice_Dirac` 下载页面与肖像（infobox 1933 年照片或 Clara Ewald 1939 肖像画）。
- **参考模板**：
  - 结构母本：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- page.md 已在本地（见上），**事实基准如下**（以 page.md 为唯一依据）：
  - 生卒（1902-08-08 生于英格兰布里斯托尔 ~ 1984-10-20 逝于美国佛罗里达州塔拉哈西，享年 82 岁）
  - 国籍（英国；1919-10-22 入籍前持瑞士国籍，父 Charles Adrien Ladislas Dirac 为瑞士 Saint-Maurice 移民、布里斯托尔法语教师；母 Florence Hannah Holten 出自康沃尔卫理公会家庭）
  - 兄弟姐妹（兄 Reginald Charles Félix 1925 年 3 月自杀，妹 Béatrice）；父严苛，强迫只用法语交谈——"I feel much freer now" 原句可引
  - 教育（Bishop Road Primary School（同学 Archibald Leach 即 Cary Grant）→ Merchant Venturers' Technical College → 1921 布里斯托尔大学电机工程 BSc 一等荣誉 → 1923 布里斯托尔大学数学 B.A.（免第一年，受 Peter Fraser 射影几何影响）→ 剑桥 St John's College，导师 Ralph Fowler → 1926-06 博士（史上第一篇量子力学博士论文《Quantum Mechanics》）→ 哥本哈根/哥廷根博士后）
  - 任职机构（1932-1969 剑桥 Lucasian 数学教授；1970-1984 佛罗里达州立大学物理学教授）
  - 关键荣誉（FRS、Nobel 1933、Royal Medal 1939、Copley Medal 1952、Max Planck Medal 1952、Oppenheimer Memorial Prize 1969、Order of Merit）
  - 家庭（1937 娶 Margit Wigner（Manci），Eugene Wigner 之妹；抚养继子 Judith 与 Gabriel Andrew Dirac（后成图论学家），与 Manci 生两女 Mary Elizabeth、Florence Monica）
  - 知名学生（博士生：Harish-Chandra、Richard J. Eden、C. J. Eliezer、Behram Kurşunoğlu、John Polkinghorne、Dennis Sciama；其他 notable：Homi J. Bhabha、Freeman Dyson、Fred Hoyle、Herbert Jehle、Victor Weisskopf）
  - 核心贡献清单（见第 4 步）
  - 关键时间线（15–20 节点）：1902 布里斯托尔生 → 1921 电机工程毕业、剑桥奖学金不足 → 1923 数学二学位 + 入剑桥 → 1925-09 Fowler 转来海森堡论文、认出泊松括号结构 → 1926 博士（首篇 QM 论文）→ 1926 费米–狄拉克统计 → 1928 狄拉克方程 → 1930《The Principles of Quantum Mechanics》→ 1931 磁单极子论文 → 1932 正电子由 Anderson 观测、同年就任 Lucasian → 1933 诺贝尔奖 + 拉格朗日量论文（路径积分之源）→ 1937 与 Manci 结婚 + 大数假说 → 1939 bra–ket 记号 + Royal Medal → 1941 引入分离功单位 SWU（Tube Alloys 气体离心法）→ 1950 约束系统哈密顿理论 → 1956 莫斯科黑板题词 → 1959 重提 graviton → 1962 Dirac membrane（弦论先声）→ 1969 退休 + Oppenheimer 奖 → 1970 FSU → 1984-10-20 塔拉哈西逝世

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/20th_century/` 下使用本目录 `Paul_Adrien_Maurice_Dirac/` 并创建 `images/`。

### 第 2 步：复制 Makefile 【模板通用】

- 复制参照成品 `Makefile`，设置 `MAIN=Paul_Adrien_Maurice_Dirac_zh`、`VIDEO_NAME=Paul_Adrien_Maurice_Dirac_zh`。

### 第 3 步：收集图片 【人物专属】

- 下载 infobox 肖像到 `images/`；404 用 Commons `Special:FilePath`（候选：`Clara Ewald - Paul Dirac.jpg`、`Dirac,Paul 1963 Kopenhagen.jpg`）。可补插图：1927 索尔维会议合影、1962 Jabłonna 与费曼合影。

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

**Dirac 的研究领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | quantum mechanics | 量子力学 | 泊松括号→对易量的一般形式、第一篇 QM 博士论文 | 核心页 |
| 1 | quantum field theory | 量子场论 | 被视为 QFT 创建者、首创该术语 | 场论页 |
| 2 | quantum electrodynamics | 量子电动力学 | 奠基人之一；晚年拒斥重整化 | QED 页 |
| 3 | mathematical physics | 数学物理 | δ 函数、狄拉克代数、算子、bra–ket 记号 | 方法页 |
| 4 | quantum gravity | 量子引力 | 引力场量子化、正则量子引力奠基 | 引力页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Ralph H. Fowler | 导师→本人 | 剑桥博士导师，转来海森堡论文者 |
| advisor-student | Harish-Chandra | 本人→学生 | 博士生，表示论数学家 |
| advisor-student | Dennis Sciama | 本人→学生 | 博士生，现代宇宙学学派宗师 |
| advisor-student | Freeman Dyson | 本人→学生 | infobox 其他 notable 学生，QED 重整化 |
| advisor-student | Homi J. Bhabha | 本人→学生 | infobox 其他 notable 学生，印度核科学之父 |
| spouse | Margit Wigner | 无向 | 1937 年结婚，Eugene Wigner 之妹 |
| co-honored | Erwin Schrödinger | 无向 | 1933 诺贝尔物理学奖共享 |
| colleague | Werner Heisenberg | 无向 | 1929 同乘 Graf Zeppelin 环球讲学 |
| colleague | Enrico Fermi | 无向 | 费米–狄拉克统计（各自独立提出） |
| colleague | Eugene Wigner | 无向 | 内兄，亦是物理同行（Weisskopf–Wigner） |
| colleague | Richard Feynman | 无向 | 1933 拉格朗日量论文为路径积分奠基，1962 Jabłonna 同框 |

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：极简、精确、深不可测
- **配色**：墨蓝（主色 `#1A2E4F`）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeQM` 量子力学 — 墨蓝 `#1A2E4F`
  - `badgeQFT` 量子场论 — 靛蓝 `#4C5FD5`
  - `badgeQED` 量子电动力学 — 玫瑰 `#C4204F`
  - `badgeGrav` 量子引力 — 青绿 `#0E7C7B`
- **背景母题**：大面留白 + 极细几何线（对易关系的双圈箭头图形），呼应其寡言与数学美的信条。

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + 细边框 + 姓名小字注）与国籍行。
2. 必须有身份信息页：左侧头像 + 右侧信息网格（生卒、本名、国籍、出生地、师承、任职、主要荣誉、核心领域），事实取自 page.md infobox，不得杜撰。
3. 结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 量子力学的立法者 / P. A. M. Dirac 1902–1984 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（含教育、师承、任职、荣誉、家庭）
03  核心贡献概览 — 狄拉克方程 / QED / 数学物理 / 量子引力
04  布里斯托尔的沉默少年（1902–1923）— 法语家教、电机工程、误打误撞的数学二学位
05  剑桥与泊松括号（1925–1926）— 海森堡论文、史上首篇 QM 博士论文
06  狄拉克方程（核心贡献页）— 相对论与量子力学的联姻、自旋、负能解
07  公式框页 — 狄拉克方程 (iγ^μ∂_μ − m)ψ = 0（page.md 未给显式形式，此为标准形式并注明）
08  预言反物质 — 正电子 1932 由 Anderson 观测、Dirac sea
09  费米–狄拉克统计与记号革命 — "Fermi statistics" 的对称理由、bra–ket
10  数学美信条 — 1956 莫斯科黑板题词、拒绝重整化（1975 原句可引）
11  个性轶事页 — "dirac" 单位、Wigner's sister、与 Feynman 的方程对话（均 page.md 明载）
12  门生与传承 — Harish-Chandra、Sciama、Dyson、Bhabha
13  战时与晚年 — Tube Alloys 离心法、SWU、剑桥→FSU
14  荣誉与认可 — Nobel 1933 · Copley 1952 · OM
15  遗产：现代物理的"真实种子"
16  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；头部宏定义整体复用结构母本骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make distclean && make pdf`，用 `pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Dirac 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方原句 "for the discovery of new productive forms of atomic theory"，与 Schrödinger 共享；勿写成"因狄拉克方程获奖" |
| 正电子 | 方程**预测**，1932 由 Carl Anderson **观测**；勿写"狄拉克发现正电子" |
| 费米–狄拉克统计 | 费米与狄拉克各自独立提出；狄拉克本人坚持称 "Fermi statistics"（出于对称 reasons），勿写"狄拉克命名" |
| 2×2 自旋矩阵 | Dirac 自述可能独立于 Pauli 得到（对 Pais 原话），两说并存须加注 |
| 瑞士国籍 | 1919-10-22 前持瑞士籍（随父），勿漏 |
| 家庭 | Margit 即 Manci；Gabriel Andrew Dirac 是**继子**（图论学家），勿写成亲生；内兄 Eugene Wigner |
| 兄长之死 | 兄 Felix 1925-03 自杀为 page.md 明载，可写事实，勿演绎为"性格成因的唯一定论" |
| 引语 | "dirac 单位""That was not a question, it was a comment""I have an equation. Do you have one too?" 等均为 page.md 转载轶事，可引用但须保持轶事口吻，勿当名言引句处理 |
| 拒斥重整化 | "Sensible mathematics involves neglecting a quantity when it is small" 为 1975 原话，可引；勿写成他"否定 QED 全部成果" |
| 战时工作 | Tube Alloys 铀浓缩气体离心法 + 1941 引入 SWU，被评 "probably the most important theoretical result in centrifuge technology"，勿漏也勿夸大为"主持曼哈顿计划" |
| 同名区分 | 继女 Judith；亲生女儿 Mary Elizabeth / Florence Monica；Gabriel Andrew Dirac 是图论学家——注意与物理学家区分 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Dirac equation | 狄拉克方程 | 相对论性电子方程 |
| Dirac sea | 狄拉克之海 | 负能态填充图像 |
| positron | 正电子 | Anderson 1932 观测 |
| antimatter | 反物质 | 方程的推论 |
| bra–ket notation | 狄拉克记号（左右矢记号） | 1939 引入教材第三版 |
| Dirac delta function | 狄拉克 δ 函数 | 《Principles》引入 |
| Fermi–Dirac statistics | 费米–狄拉克统计 | 两人各自独立 |
| magnetic monopole | 磁单极子 | 1931 提议，至今未观测到 |
| large numbers hypothesis | 大数假说 | 1937 宇宙学推测 |
| Hamiltonian constraints | 约束哈密顿理论 | 正则量子引力奠基 |
| mathematical beauty | 数学美 | 其方法论核心信条 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **The Invisible Light** — Infraction（2:34）
- **风格**: 纪录片 / 电影 / 稳重
- **匹配理由**: 狄拉克的工作是"看不见的光"——方程先于观测、反物质先于发现；纪录片的稳重质感匹配其沉默寡言、以数学美为唯一信条的立法者气质。
- **备选**（未采用）: Timeless（沉稳/纲领，但已是母本 Wilson 篇用曲）；Eternals（宏大/深远，匹配遗产但戏剧感弱于本篇的"预言成真"张力）。
- **本地路径**: `music_audio/inspiring-electronic/19-tGxXsgSKPiQ-Documentary Cinematic by Infraction [No Copyright Music] ⧸ The Invisible Light.wav` → `presentations/20th_century/Paul_Adrien_Maurice_Dirac/TheInvisibleLight.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/20th_century/20th_century/Paul_Adrien_Maurice_Dirac/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | 成品 Beamer 骨架/源码 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/seed_person.py` | 人物 + 领域 + 关系入库引擎 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修；所有事实以 page.md 为准，无载禁写。**
