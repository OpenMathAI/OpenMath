# 物理学家立传提示词（J. Michael Kosterlitz）

> 本文件是 OpenPhysicist 21 世纪批次「物理学家立传提示词」，目标人物：J. Michael Kosterlitz（2016 诺贝尔物理学奖，拓扑相变 BKT 理论）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：John Michael Kosterlitz（约翰·迈克尔·科斯特利茨）。
- **设计哲学**：物理学家立传必须有「身份信息页」与结构化「研究领域」表达；Kosterlitz 篇的视觉主线是**涡旋与解离（vortex & unbinding）**——二维世界里正反涡旋对在临界温度下的挣脱，是拓扑相变最直观的图像。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：John Michael Kosterlitz（1943-06-22 生于苏格兰阿伯丁，在世）
- **气质关键词**：**拓扑相变的命名者、二维世界的探索者、阿尔卑斯的攀登者** —— 2016 诺贝尔物理学奖获奖理由（与 Thouless / Haldane 共享）：
  > "for theoretical discoveries of topological phase transitions and topological phases of matter"（因其拓扑相变与拓扑物态的理论发现）
- **设计母题**：**涡旋对解离（vortex-antivortex unbinding）**。低温下正反涡旋束缚成对、高温下解离 proliferation——「束缚与挣脱」贯穿 BKT 相变、KTHNY 二维熔化与他的人生轨迹（攀登、与多发性硬化共处）。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/physicist/presentations/21th_century/21st_century/J._Michael_Kosterlitz/page.md`
- **第 0 步状态**：page.md 已有本地；`{Dir}.html` 与 `images/` **待下载**。Wikipedia URL：`https://en.wikipedia.org/wiki/J._Michael_Kosterlitz`
- **参考模板**：
  - 物理学家首例成品：`physicist/presentations/20th_century/Eugene_Wigner/Eugene_Wigner_zh.tex`（16 页）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

> 数据库同步：含「研究领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL）。

### 第 0 步：事实基准 【人物专属，已核对 page.md】

- 生卒：1943-06-22 生于苏格兰阿伯丁；在世（享年留白）
- 国籍：英国出生；**美国公民**（infobox Citizenship United States；口径 "British-American physicist"）
- 家庭：德裔犹太移民之子；父亲 Hans Walter Kosterlitz 为开创性生物化学家（脑啡肽/内啡肽专门研究者，1934 年为躲避纳粹迫害移居英国，阿伯丁大学 Kosterlitz Centre 以其命名）；母亲 Hannah Gresshöner
- 教育：Robert Gordon's College → Edinburgh Academy（大学入学备考）；剑桥 Gonville and Caius College（BA，后转 MA）；牛津 Brasenose College（DPhil 1969）
- 博士论文：《Problems in strong interaction physics》（1969）；牛津博士导师 page.md 无载
- 学术导师：David Thouless（**infobox 明确标注 postdoc——博士后导师**，Birmingham 合作）
- 任职机构：博士后（University of Birmingham，与 Thouless 合作；Cornell University）→ University of Birmingham 教员（1974，lecturer 后 reader）→ Brown University 物理教授（1982 至今）；Aalto University（芬兰）visiting research fellow；Korea Institute for Advanced Study 特聘教授（2016 起）
- 关键荣誉：Nobel Prize in Physics（2016，与 Thouless / Haldane 共享）；Maxwell Medal and Prize（英国物理学会，1981）；Lars Onsager Prize（APS，2000，尤其表彰 BKT 相变工作）；APS Fellow（1992 起）；FRS（2026 当选，按本地页面原文）
- 核心贡献清单：
  1. Berezinskii–Kosterlitz–Thouless（BKT）相变理论（二维拓扑相变）
  2. KTHNY 理论（二维熔化的拓扑理论）
  3. 一维与二维物理
  4. 相变：随机系统、电子局域化、自旋玻璃
  5. 临界动力学：熔化与冻结
- 关键时间线（15 节点）：1943 生于阿伯丁 → Robert Gordon's College → Edinburgh Academy → 剑桥 Caius BA/MA → 1969 牛津 DPhil → 博士后 Birmingham（Thouless 合作）/ Cornell → 1974 Birmingham 教员（lecturer→reader）→ 1960s 阿尔卑斯攀登先驱 → 1978 确诊多发性硬化 → 1981 Maxwell Medal → 1982 Brown 教授 → 1992 APS Fellow → 2000 Lars Onsager Prize → 2016 诺贝尔奖 / KIAS 特聘教授 → 2026 FRS

### 第 4 步：研究领域表 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | condensed matter physics | 凝聚态物理 | 主领域（infobox Fields） | 全篇 |
| 1 | topological phase transitions | 拓扑相变 | BKT 相变，2016 诺奖核心 | 核心页 |
| 2 | phase transitions | 相变 | 随机系统 / 电子局域化 / 自旋玻璃 | 研究版图页 |
| 3 | critical dynamics | 临界动力学 | 熔化与冻结 | KTHNY 页 |
| 4 | spin glasses | 自旋玻璃 | 相变研究方向之一 | 研究版图页 |

### 第 4.5 步：社会关系表 【与 yaml 完全一致，仅收 page.md 明载】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | David J. Thouless | 对方是导师 | 博士后导师（infobox 标注 postdoc），Birmingham 期间合作 |
| co-honored | David J. Thouless | 无向 | 2016 诺贝尔物理学奖共同得主（拓扑相变与拓扑物态） |
| co-honored | Duncan Haldane | 无向 | 2016 诺贝尔物理学奖共同得主（拓扑相变与拓扑物态） |
| parent-child | Hans Kosterlitz | 对方是父亲 | 生物化学家（内啡肽先驱），阿伯丁 Kosterlitz Centre 以其命名 |

> 无载不入库：KTHNY 中其余贡献者（Halperin、Nelson 等）page.md 仅以理论缩写出现，未载个人关系；牛津 DPhil 博士导师无载禁写；与 Berezinskii 无直接关系记载（仅理论命名）禁写。

### 第 5 步：配色方案 【人物专属】

- **气质**：涡旋、临界、冷峻的拓扑
- **配色**：涡旋紫（主色）+ 诺奖香槟金 `C9A227` + 四分类色
  - 主色 `mainclr` — 涡旋紫 `#4A3B8C`（本批专属，勿与他篇重复）
  - `badgeA` BKT 相变 — 青 `#0E7C7B`
  - `badgeB` KTHNY 熔化 — 琥珀 `#E07B30`
  - `badgeC` 自旋玻璃 — 靛蓝 `#4C5FD5`
  - `badgeD` 临界动力学 — 玫瑰 `#C4204F`
- **背景母题**：成对与解离的螺旋涡旋（小圆环对低温束缚、大圆环对高温散开，温度梯度排布），呼应涡旋-反涡旋对的束缚与解离

### 第 6 步：幻灯片序列 【人物专属，12 页】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 拓扑相变命名者 / J. Michael Kosterlitz 1943– + 四色 badge + 右上头像 + 国籍行（United Kingdom → United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、国籍、教育、导师、任职、荣誉、核心领域）
03  核心贡献概览 — BKT 相变 / KTHNY 理论 / 相变与自旋玻璃 / 临界动力学
04  早年阿伯丁 (1943–1969) — 德裔犹太移民家庭、Robert Gordon's、Edinburgh Academy、剑桥 Caius、牛津 DPhil
05  博士后与伯明翰 (1969–1982) — Thouless 合作、Cornell、Birmingham 教员
06  BKT 相变（核心贡献页）— 二维世界正反涡旋对的束缚与解离；page.md 无公式 → 用涡旋对解离概念图式并注明
07  KTHNY 理论 — 二维熔化的拓扑机制（位错→位错环两步解束缚）
08  研究版图 — 随机系统 / 电子局域化 / 自旋玻璃 / 临界动力学
09  攀登者的一面 — 1960s 阿尔卑斯攀登先驱、Fessura Kosterlitz 首登、Nuovo Mattino 自由攀登运动
10  荣誉与认可 — Nobel 2016 · Onsager 2000 · Maxwell 1981 · FRS 2026
11  结尾 — 底部品牌 OpenMathAI
```

### 第 7–8 步：版式要点 + 陷阱表

版式照标杆（身份信息页左头像右网格、每页 make 后 pdftoppm 目检）。**Kosterlitz 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| Thouless 导师身份 | infobox 明确标注 **postdoc（博士后导师）**；frontmatter 虽列 doctoral_advisor，但以 infobox 精确口径为准，写「博士后导师」勿写「博士导师」★ 本篇 P0 裁定 |
| 牛津博士导师 | DPhil 1969 导师 page.md 无载，禁写（勿从强相互作用方向反推） |
| FRS 年份 | 本地页面原文 "elected a Fellow of the Royal Society in **2026**"，照实写，勿按惯例改成早年 |
| 国籍口径 | infobox Citizenship=United States，出生地 Aberdeen；口径 "British-American physicist"，勿写「美国人（生于英）」之外引申，勿写「苏格兰籍」 |
| 父亲身份 | Hans Walter Kosterlitz 是**生物化学家**（内啡肽先驱、Kosterlitz Centre 冠名者），勿写成物理学家；母亲 Hannah Gresshöner 仅姓名可写 |
| BKT 全称 | Berezinskii–Kosterlitz–Thouless transition，勿漏 Berezinskii；Berezinskii 与本人无直接合作记载 |
| KTHNY | 仅以理论缩写出现，Halperin / Nelson 等其余贡献者无载禁写 |
| 多发性硬化 | 1978 确诊为 Personal life 明载，立传可一句客观带过或不写，勿渲染成「逆境叙事」主线 |
| 诺奖三人分工 | Thouless / Kosterlitz 主攻**拓扑相变**，Haldane 主攻**拓扑物态**；BKT 勿归到 Haldane 名下 |
| 登山 | Fessura Kosterlitz 首登（Orco Valley）、American Direct 首次重登（Petit Dru）、Nuovo Mattino 运动均明载可写；其余攀登履历禁写 |

### 第 9 步：术语清单 【8–12 条】

| 英文 | 中文 | 风险 |
|------|------|------|
| Berezinskii–Kosterlitz–Thouless transition | BKT 相变 | 勿漏 Berezinskii；拓扑相变首个实例 |
| vortex-antivortex pair | 涡旋-反涡旋对 | 束缚态解离是 BKT 机制 |
| topological phase transition | 拓扑相变 | 2016 诺奖理由前半句 |
| KTHNY theory | KTHNY 理论 | 二维熔化的位错解束缚理论 |
| two-dimensional physics | 二维物理 | 本人主战场，勿写成「低维物理」泛称之外引申 |
| spin glass | 自旋玻璃 | 相变方向之一 |
| electron localization | 电子局域化 | 相变方向之一 |
| critical dynamics | 临界动力学 | 含熔化与冻结 |
| random systems | 随机系统 | 无序系统研究 |
| Lars Onsager Prize | 昂萨格奖 | APS 2000，表彰 BKT |
| Maxwell Medal and Prize | 麦克斯韦奖章 | 英国物理学会 1981，勿与数学 Maxwell 混淆 |

---

## 四、背景音乐建议 【人物专属】

- **选定曲目**: **Through the Darkness** — Audiomachine（标签：史诗 / 黑暗 / 推进）
- **匹配理由**: 「突破前夕」正是 BKT 理论的叙事底色——二维相变长期被正统理论判为不可能，Kosterlitz 与 Thouless 在伯明翰的博士后岁月里从涡旋图像中凿出全新范式；穿越黑暗之后是 2016 年斯德哥尔摩。
- **本地路径**: `music_audio/inspiring-electronic/14-Trn1cSsY2t8-Audiomachine - Through the Darkness.wav`
- **备选**: Mirage（抽象思维）；The Flow of Time（时间线叙事）。

---

## 五、关键参考文件

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/J._Michael_Kosterlitz/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `MySQL/data/J._Michael_Kosterlitz.yaml` | 社会关系入库 yaml |
| `MySQL/seed_person.py` | 入库引擎（幂等，QID → name_en 匹配） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
