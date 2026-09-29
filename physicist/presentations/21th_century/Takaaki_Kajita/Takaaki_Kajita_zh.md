# 物理学家立传提示词（Takaaki Kajita 梶田隆章）

> **OpenPhysicist 21 世纪批次 · 人物专属立传提示词**。
> 目标人物：Takaaki Kajita（梶田 隆章，1959-03-09 ~ 在世），2015 诺贝尔物理学奖得主（大气中微子振荡发现者）。
> 执行方式：复制本文件到新对话中，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Takaaki Kajita（梶田 隆章），日本物理学家，神冈观测所 Kamiokande/Super-Kamiokande 中微子实验核心人物，大气中微子振荡的发现者之一。
- **设计哲学**：物理学家立传必须有「身份信息页」，且强调「研究领域」的结构化表达。梶田篇的叙事核心是「地下的沉默守望者」——在神冈矿山地下的大型水切伦科夫探测器中，从数据残缺的异常里读出中微子在两种味之间的振荡，证明中微子有质量、标准模型有缺口。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Takaaki Kajita（梶田 隆章，1959-03-09 生于日本埼玉县东松山市，在世）
- **气质关键词**：**大气中微子的读数人、神冈地下的守望者、中微子质量的证明者** —— 2015 诺贝尔物理学奖获奖理由（官方英文原文，禁止改写）：
  > "for the discovery of neutrino oscillations, which shows that neutrinos have mass"（发现中微子振荡，表明中微子具有质量）
- **设计母题**：**不可见之光（invisible light）**。中微子无法直接看见、只能在巨型探测器的微光中显形——视觉语言可用深紫底色上一枚贯穿地球的粒子轨迹与一环淡蓝切伦科夫光圈。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/physicist/presentations/21th_century/21st_century/Takaaki_Kajita/page.md`
- **第 0 步状态**：page.md 已有本地；`Takaaki_Kajita.html` 与 `images/` 待下载，Wikipedia URL：`https://en.wikipedia.org/wiki/Takaaki_Kajita`
- **参考模板**：
  - 物理学家成品骨架：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页）
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准（已核对 page.md，建 Beamer 前须再对照原文）

- 生卒：1959-03-09 生于埼玉县东松山市，在世
- 国籍：日本
- 教育：埼玉大学物理学学士 1981；东京大学硕士、博士 1986；高中：埼玉县立川越高中
- 博士导师：Masatoshi Koshiba（小柴昌俊）；infobox 另载 other academic advisor：Yoji Totsuka（户塚洋二）
- 加入小柴研究组的理由（page.md 原话转述）：中微子「seemed like they might be interesting」
- 任职：1988 起任职东京大学宇宙线研究所（Institute for Cosmic Ray Research, ICRR）；1992 助教授；1999 教授 + 宇宙中微子中心主任；2017 时任东京大学国际宇宙物理数学研究所（Kavli IPMU）PI + ICRR 所长；KAGRA 引力波探测器 PI；2020-10-01 就任日本学术会议会长；2021–2024 任 IUPAP 天体粒子物理委员会（C4）主席
- 关键荣誉：朝日奖 1987（Kamiokande 集体，代表小柴昌俊）/ 1998（Super-K 集体，代表户塚洋二）；Bruno Rossi Prize 1989（Kamiokande 合作组）；Nishina Memorial Prize 1999；Panofsky Prize 2002（大气中微子振荡的令人信服的实验证据）；Yoji Totsuka Award 2010；日本学士院奖 2012；Julius Wess Award 2013；Nobel 2015；Breakthrough Prize in Fundamental Physics 2016；Asian Scientist 100 2016；Homi Bhabha Medal 2019；文化勋章・文化功勋者 2015
- 荣誉学位：2016 阿里加尔穆斯林大学/帕多瓦大学/圣安德烈斯大学；2017 那不勒斯费德里科二世大学/伯尔尼大学/佩鲁贾大学；2024 格拉斯哥大学
- 核心贡献清单：
  1. 1998 年 Super-Kamiokande 团队发现宇宙线在大气中产生的中微子在到达探测器前于两种味之间转换（大气中微子振荡）
  2. 证明中微子有质量——标准模型（要求中微子无质量）存在缺口
  3. 与 McDonald 的 SNO 工作共同解决长期悬而未决的太阳中微子问题
  4. KAGRA 引力波探测器项目 PI
- 关键时间线（15–20 节点）：1959 出生东松山市 → 川越高中 → 1981 埼玉大学学士 → 东京大学硕士/博士、加入小柴组 → 1986 博士 → 1987 朝日奖（Kamiokande 集体）→ 1988 入职宇宙线研究所 → 1989 Rossi Prize → 1992 助教授 → 1998 Super-K 发现大气中微子振荡 + 朝日奖 → 1999 教授 + 宇宙中微子中心主任 + Nishina 奖 → 2002 Panofsky Prize → 2010 Totsuka Award → 2012 日本学士院奖 → 2013 Julius Wess 奖 → 2015 诺贝尔物理学奖 + 文化勋章 → 2016 Breakthrough Prize → 2019 Homi Bhabha Medal → 2020 日本学术会议会长 → 2021–2024 IUPAP C4 主席
- 诺奖记者会引语（page.md 英文原话，可引用）："I want to thank the neutrinos, of course. And since neutrinos are created by cosmic rays, I want to thank them, too."
- 获诺奖后第一个电话打给恩师小柴昌俊（2002 诺奖得主）

### 第 4 步：研究领域表（与 yaml fields 一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | neutrino physics | 中微子物理 | Kamiokande/Super-K 毕生主战场 | 核心页 |
| 1 | neutrino oscillations | 中微子振荡 | 1998 大气中微子发现，2015 诺奖核心 | 核心页 |
| 2 | astroparticle physics | 粒子天体物理 | IUPAP C4 委员会主席领域 | 荣誉页 |
| 3 | cosmic ray physics | 宇宙线物理 | 宇宙线研究所 ICRR 任职主线 | 机构页 |
| 4 | gravitational wave detection | 引力波探测 | KAGRA 项目 PI | 遗产页 |

### 第 4.5 步：社会关系表（与 yaml relations 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Masatoshi Koshiba | 导师 | 东京大学博士导师，2002 诺贝尔物理学奖得主，神冈探测器创始人 |
| advisor-student | Yoji Totsuka | 导师 | infobox 明载 other academic advisor，Super-K 时期指导者（非博士导师） |
| co-honored | Arthur B. McDonald | 无向 | 2015 诺贝尔物理学奖共同得主，SNO 发现同类结果 |
| spouse | Michiko | 无向 | 妻子 |

> 注：与 Koshiba 兼有师生与同事双属性，仅建 advisor-student 一条；1987/1998 朝日奖与 1989 Rossi Prize 为合作组集体获奖（代表分别为 Koshiba/Totsuka），以 advisor/co-honored 关系覆盖，不再另建组级 co-honored。

### 第 5 步：配色方案 【人物专属】

- **气质**：深邃、沉静、地下实验室的微光
- **配色**：中微子紫（主色）+ 诺奖香槟金 `C9A227` + 四分类色
  - `mainclr` 主色 — 中微子紫 `#3A2E6E`（批内不重复）
  - `badgeOsc` 中微子振荡 — 靛蓝 `#2B4C9B`
  - `badgeSK` Super-K — 青蓝 `#1E88C7`
  - `badgeAtm` 大气中微子 — 青绿 `#0E7C7B`
  - `badgeKAGRA` KAGRA — 玫瑰 `#C4204F`
- **背景母题**：深紫底色上一枚粒子轨迹斜贯而过，尾部拖出一环淡蓝切伦科夫光圈

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 大气中微子的读数人 / Takaaki Kajita 1959– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、国籍、教育、师承、任职、荣誉、核心领域）
03  核心贡献概览 — 大气中微子振荡 / 中微子有质量 / 太阳中微子问题 / KAGRA
04  埼玉少年与东京大学 (1959–1986) — 川越高中、埼玉大学、入小柴组「似乎有趣」
05  神冈岁月：Kamiokande (1986–1996) — 宇宙线研究所、集体奖项、助教授
06  Super-Kamiokande 时代 (1996–1998) — 大型水切伦科夫探测器
07  突破：大气中微子振荡 (1998)（核心贡献页）— 两种味之间转换、中微子有质量（公式框：振荡概率概念式或概念图式，page.md 无具体公式须注明）
08  太阳中微子问题的终解 — 与 McDonald 的 SNO 互证、标准模型的缺口
09  荣誉与认可 — Nobel 2015 · Panofsky 2002 · 日本学士院奖 2012 · Breakthrough 2016
10  「感谢中微子」— 诺奖记者会原话、第一个电话打给小柴
11  科学组织与传承 — 日本学术会议会长、IUPAP C4 主席
12  新边界：KAGRA 引力波探测
13  遗产：中微子天文学的黄金时代
14  结尾
```

### 第 7–8 步：版式要点 + 梶田隆章专属陷阱表

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方原文 "for the discovery of neutrino oscillations, which shows that neutrinos have mass"；与 McDonald 共享，勿写成独立获奖 |
| 双导师区分 | 博士导师是 Koshiba（frontmatter doctoral_advisor）；Totsuka 是 infobox 的 other academic advisors，勿写成博士导师 |
| 朝日奖两次 | 1987 属 Kamiokande（代表 Koshiba）、1998 属 Super-K（代表 Totsuka），均为集体获奖，勿写成个人奖 |
| 机构名称 | page.md 行文作 Institute for Cosmic Radiation Research（正文）与 Institute for Cosmic Ray Research（infobox 链接，即 ICRR），统一用 ICRR/宇宙线研究所口径 |
| 1998 发现表述 | 是 Super-K 团队发现大气中微子的味缺失（振荡）；「中微子有质量」是推论，勿写成直接测得质量 |
| 诺贝尔份额 | 2015 奖 Kajita 与 McDonald 各半（两人共享），SNO 三人组中仅 McDonald 获奖，勿写错 |
| 同名区分 | Koshiba 是 2002 诺奖得主；Yoji Totsuka 未获诺奖（2010 年以 Totsuka Award 纪念），两人身份勿混 |
| 无载禁写 | 家庭细节（仅载妻子名 Michiko）、生平轶事超出 page.md 者禁写；「有趣」引语为英文原话可引 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| neutrino oscillation | 中微子振荡 | 味之间的转换 |
| atmospheric neutrino | 大气中微子 | 宇宙线产生 |
| flavour | 味 | μ 子型/电子型 |
| Super-Kamiokande | 超级神冈探测器 | 神冈矿山水切伦科夫 |
| Cherenkov light | 切伦科夫光 | 探测原理 |
| neutrino mass | 中微子质量 | 振荡的推论 |
| solar neutrino problem | 太阳中微子问题 | 与 SNO 共同解决 |
| KAGRA | KAGRA 引力波探测器 | 神冈地下低温干涉仪 |
| cosmic ray | 宇宙线 | 中微子的产生源 |
| Standard Model | 标准模型 | 要求中微子无质量 |

---

## 四、BGM 建议 【人物专属】

- **选定曲目**：**The Invisible Light** — Infraction（2:34，纪录片/电影/稳重）
- **匹配理由**：
  - 「The Invisible Light」曲名即中微子意象——不可见之光在地下深处显形
  - 「传记主线叙事、稳重」匹配神冈三十年的沉默守望
- **备选**（未采用）：Expedition（留给同批 McDonald）、Eternals（留给同批 Thouless）
- **本地路径**：`music_audio/inspiring-electronic/19-tGxXsgSKPiQ-Documentary Cinematic by Infraction [No Copyright Music] ⧸ The Invisible Light.wav`
- **时长**：154 秒 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐
