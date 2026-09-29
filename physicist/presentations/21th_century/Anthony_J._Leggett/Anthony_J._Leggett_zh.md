# 物理学家立传提示词（21 世纪批次：Anthony J. Leggett）

> **本文件是 OpenPhysicist「物理学家立传提示词」**，对象：Anthony J. Leggett（2003 诺贝尔物理学奖，超流氦-3 理论与量子力学基础）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节）。
> 凡标注 `【模板通用】` 的部分可复用；标注 `【人物专属】` 的部分为本人物定制。

---

## 一、模板定位 【人物专属】

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Sir Anthony James Leggett（安东尼·詹姆斯·莱格特爵士），2003 诺贝尔物理学奖得主（三人共享之一）。
- **设计哲学**：保留物理学家模板「身份信息页 + 结构化研究领域」骨架；Leggett 是「低温物理世界领袖 + 量子力学基础的拷问者」双线人物，叙事主线取「古典学出身 → 物理学 DPhil → 超流 3He 定音之论 → 量子测量的宏观检验」。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Sir Anthony James Leggett（1938-03-26 ~ 2026-03-08，享年 87 岁）
- **获奖理由（官方英文原文 + 中译，page.md 明载，禁止改写）**：
  > "for pioneering contributions to the theory of superconductors and superfluids"（因对超导体和超流体理论的先驱性贡献）
- **共享格局**：2003 奖由 Leggett（超流体理论）与 Vitaly Ginzburg、Alexei Abrikosov（超导体理论）三人共享。
- **气质关键词**：**超流氦-3 的理论定音者、宏观量子 dissipative 系统的开路人、量子力学基础的拷问者**
- **设计母题**：**超流（frictionless flow）**。氦-3 超流相无摩擦流动、量子相干在宏观尺度显现——以「无漩涡损耗的层流线 + 与宏观世界的量子纠缠丝带」为核心视觉概念。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/physicist/presentations/21th_century/21st_century/Anthony_J._Leggett/page.md`
- **第 0 步状态**：page.md 已有本地；**html 与 images/ 待下载**；Wikipedia URL：`https://en.wikipedia.org/wiki/Anthony_J._Leggett`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`、`physicist/presentations/cover/openphysicist_page.tex`

---

## 三、任务流程 【模板通用，逐步执行】

> 数据库同步含「研究领域 + 入库」（第 4 步）与「社会关系 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL）。

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- ☐ 待下载 `https://en.wikipedia.org/wiki/Anthony_J._Leggett` 到 `{Dir}.html` 与 `images/` 肖像（Commons `Anthony_Leggett_at_GYSS_19Jan2016_2.jpg` 2016 新加坡照，250px 改 500px）
- 事实基准（以本地 page.md 为准，第一轮已核对）：
  - 生卒：1938-03-26 生于伦敦坎伯威尔 ~ 2026-03-08 逝于美国伊利诺伊州厄巴纳家中，享年 87 岁
  - 国籍/公民权：英国 + 美国（British-American）
  - 家庭：父母均为家族第一代大学生（伦敦大学教育研究院结识），父为中学物理/化学/数学教师，母亦教过中学数学；兄妹五人（妹 Clare、Judith，弟 Terence、Paul），罗马天主教家庭抚养，二十岁出头停止实践信仰；1973-06 与 Haruko Kinase 结婚（在 Sussex 相识，后于 UIUC 获文化人类学博士），1978 年生女 Asako（UIUC 地理与化学联合专业毕业）
  - 教育：Wimbledon College（11-plus 提前录取）→ Beaumont College（耶稣会学校，主修古典学）→ 1954-12 获 Balliol College 奖学金，1955 入牛津读古典学（Literae Humaniores/Greats）→ 第二个本科：Merton College 物理 → DPhil 1964（导师 Dirk ter Haar，论文《Some Problems in the Theory of Many-Body Systems》，液体氦两个课题：超流 4He 高阶声子相互作用 + 4He 在正常液 3He 中稀溶液性质）；Magdalen College Prize Fellowship 1963–1967；牛津荣誉 DLitt 2005
  - 任职轨迹：UIUC 博士后 1964-08–1965-08（David Pines 及 Bardeen/Baym/Kadanoff 等的环境）→ 京都大学 Takeo Matsubara 组一年 → 「漫游式」博士后一年（Oxford/Harvard/Illinois）→ 1967 秋 Sussex 大学讲师（此后十五年主场）→ 1970s 中期多次访东京大学 + 加纳库马西 Kwame Nkrumah 大学 → 1982 接受 UIUC MacArthur 讲席教授（1983 初 Cornell 访问八个月后，当年秋抵 Urbana，终其职业生涯）→ 2006–2016 加拿大 Waterloo 量子计算研究所（IQC）→ 2013 上海复杂物理中心创始主任 → 截至 2023-04 任 UIUC 凝聚态理论研究所（ICMT）首席科学家
  - 关键荣誉：Maxwell Medal and Prize 1975；FRS 1980；APS Fellow 1985；HonFInstP 1998；Eugene Feenberg Memorial Medal 1999；IOP Dirac Medal 2002（infobox 载 1992，见陷阱表）；Wolf 物理学奖 2002/2003（与 B. I. Halperin 共享，凝聚态物质研究）；Nobel 2003；KBE 2004（"for services to physics"）；院士身份：NAS、美国哲学学会、美国艺术与科学院、俄罗斯科学院（外籍）、印度国家科学院外籍 Fellow 2011
  - 知名学生（infobox 明载）：Amir Caldeira、Matthew P. A. Fisher、Mohit Randeria
  - 核心贡献清单（4–6 条）：①正常与超流氦液体、强耦合超流体的理论理解（超流 3He 相理论，诺奖核心）；②Caldeira–Leggett 量子耗散模型；③Leggett–Garg 不等式与 Leggett 不等式（量子力学基础检验）；④宏观耗散系统量子物理方向设定；⑤玻璃低温性质、高温超导、BEC 原子气体、拓扑量子计算
  - 关键时间线（15–20 节点）：1938-03-26 生于坎伯威尔 → 战时疏散至 Surrey Englefield Green → Wimbledon College → Beaumont College（古典学）→ 1954-12 Balliol 奖学金 → 1955 入牛津（古典学 Greats）→ Merton 第二本科（物理）→ 1963–1967 Magdalen Prize Fellowship → 1964 DPhil（ter Haar 门下）→ 1964-65 UIUC 博士后 → 1965-66 京都大学 Matsubara 组 → 1967 Sussex 讲师 → 1970s 中期东京/库马西 → 1973-06 与 Haruko Kinase 结婚 → 1975 Maxwell 奖 → 1978 女儿 Asako 出生 → 1980 FRS + 研究兴趣转离 3He → 1982 UIUC MacArthur 讲席（1983 秋到任）→ 1999 Feenberg 奖章 → 2002/03 Wolf 奖（与 Halperin）→ 2003 诺贝尔物理学奖 → 2004 KBE → 2005 牛津荣誉 DLitt + Berkeley 与 Ramsey 论战 → 2006–2016 Waterloo IQC → 2013 上海复杂物理中心创始主任 → 2023 ICMT 首席科学家 → 2026-03-08 逝于 Urbana

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/21th_century/` 下创建 `Anthony_J._Leggett/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制 20 世纪成品目录 Makefile，设 `MAIN=Anthony_J._Leggett_zh`、`VIDEO_NAME=Anthony_J._Leggett_zh`

### 第 3 步：收集图片 【人物专属】

- 肖像：Commons `Anthony_Leggett_at_GYSS_19Jan2016_2.jpg`；404 则装饰圆占位

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | superfluidity | 超流性 | 氦-3 超流相理论，2003 诺奖核心 | 核心页 |
| 1 | low-temperature physics | 低温物理 | 世界公认领袖领域 | 概览页 |
| 2 | condensed matter physics | 凝聚态物理 | 玻璃/高温超导/BEC/拓扑量子计算 | 后期页 |
| 3 | foundations of quantum mechanics | 量子力学基础 | Leggett–Garg / Leggett 不等式、测量问题 | 基础页 |
| 4 | quantum dissipation | 量子耗散 | Caldeira–Leggett 模型 | 耗散页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> **只收 page.md 明载**；对手方 name_en 已查库，沿用库内/将建规范形式。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Dirk ter Haar | 师→生（博士导师） | 牛津 DPhil 导师（1964，多体系统理论），Magdalen 学院 fellow |
| co-honored | Vitaly Ginzburg | 无向 | 2003 诺贝尔物理学奖共享（超导体理论） |
| co-honored | Alexei Abrikosov | 无向 | 2003 诺贝尔物理学奖共享（超导体理论） |
| co-honored | Bertrand I. Halperin | 无向 | 2002/2003 Wolf 物理学奖共享（凝聚态物质研究） |
| colleague | David Pines | 无向 | 1964–65 UIUC 博士后东家，提供丰沃研究环境 |
| colleague | Takeo Matsubara | 无向 | 京都大学其组内访问一年 |
| advisor-student | Amir Caldeira | Leggett → 学生 | 博士生，合作提出 Caldeira–Leggett 量子耗散模型 |
| advisor-student | Matthew P. A. Fisher | Leggett → 学生 | infobox 明载博士生 |
| advisor-student | Mohit Randeria | Leggett → 学生 | infobox 明载博士生 |
| spouse | Haruko Kinase | 无向 | 1973-06 结婚，Sussex 相识，文化人类学博士 |

- 入库注意：Leggett 库内无记录，本 yaml 新建（name_en=`Anthony J. Leggett`，与 Abrikosov/Ginzburg yaml 中对手方写法一致）；Halperin 用库内 `Bertrand I. Halperin`(2637)、Pines 用库内 `David Pines`(2598)；学生 Matthew P. A. Fisher 注意与 20 世纪临界现象名家 Michael Fisher 区分；Ginzburg/Abrikosov 关系与本批前两篇互为镜像，撞 uq_rel 跳过即可。

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：液氦深青、无摩擦流动、古典出身的思想者
- **配色**：液氦深青（主色，批内唯一）+ 香槟金 `C9A227`（诺奖）+ 四分类色
  - `mainclr` 主色 — 液氦深青 `#14647E`
  - `badgeSF` 超流氦-3 — 冰青 `#16A085`
  - `badgeQM` 量子基础 — 深紫 `#5B2C6F`
  - `badgeMacro` 宏观耗散 — 橙 `#CA6F1E`
  - `badgeLife` 古典学与人生 — 石墨灰 `#5D6D7E`
- **背景母题**：柔和气泡——水平无旋层流线贯穿画面，局部一缕丝带状相干线表示宏观量子相干

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注）。
2. 封面有国籍，底部状态栏给 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前，左头像 + 右信息网格，事实取自 page.md。
4. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 超流氦-3 的理论定音者 / Anthony J. Leggett 1938–2026 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — 超流 3He / 量子耗散 / Leggett–Garg / 量子基础检验
04  古典学少年 (1938–1955) — 伦敦南郊、战时疏散、耶稣会学校、Balliol 奖学金
05  从 Greats 到物理 (1955–1964) — 古典学本科转 Merton 物理、ter Haar 门下 DPhil、液氦两课题
06  博士后漫游 (1964–1967) — UIUC（Pines/Bardeen 环境）→ 京都（Matsubara）→ Oxford/Harvard/Illinois
07  Sussex 岁月 (1967–1982) — 十五年主场、东京与库马西、1970s 超流 3He 理论（核心贡献页，公式框放超流 3He 相图概念图式，page.md 无具体公式，注明）
08  1982：MacArthur 讲席与 UIUC — Cornell 访问、1983 秋到任、后半生基地
09  宏观量子世界 — Caldeira–Leggett 模型、玻璃低温性质、BEC 气体、拓扑量子计算
10  量子力学基础拷问 — Leggett–Garg / Leggett 不等式、测量问题、2005 Berkeley 与 Ramsey 论战
11  2003 诺贝尔物理学奖 — 三人共享格局页（Leggett 超流 / Ginzburg+Abrikosov 超导）
12  荣誉与认可 — Maxwell 1975 · FRS 1980 · Wolf 2002/03 · Nobel 2003 · KBE 2004
13  遗产：从超流到量子技术的宏观视野
14  结尾
```

### 第 7–8 步：编写 Beamer 源码 + 布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}`；身份信息页参照成品 `\profileslide` 模式；每写完一页 `make` 并 `pdftoppm` 截图检查。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Leggett 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 享年与卒日 | 2026-03-08 逝于 Urbana 家中，享年 87 岁（3 月 26 日生日前 18 天）；勿写「享年 88」 |
| 国籍口径 | 出生英国、英国+美国双重公民权；frontmatter description 写 British physicist——立传记「英国/美国」两枚国籍 |
| 古典学出身 | 牛津第一学位是古典学（Literae Humaniores/Greats），物理是**第二个本科**——勿写成「物理本科」 |
| IOP Dirac Medal 年份 | infobox Awards 表列 1992，正文 honors 段未给年份、frontmatter 无年份——若名录/官方页无据，页面上写 1992 须以 infobox 口径并加注 |
| Wolf 奖年份 | 2002/2003 Wolf Prize（与 Halperin 共享），正文作 2002/2003、infobox 作 2002——两种口径择一注明 |
| 三人格局 | Leggett=超流体、Ginzburg+Abrikosov=超导体；与其二人是 co-honored，禁写合作 |
| UIUC 到任 | 1982 接受 MacArthur 讲席 offer，因 1983 初 Cornell 八个月访问，**1983 年秋**才抵 Urbana——接受年份与到任年份勿混 |
| Bardeen/Baym/Kadanoff | 仅为 UIUC 博士后环境群体提及（"David Pines and his colleagues"），关系表只入 Pines（直接东家），群体成员不入库 |
| Ramsey 论战 | 2005 Berkeley 与 Norman Ramsey 关于量子理论修改是否值得的公开辩论（Leggett 正方、Ramsey 反方）——是一次事件非长期关系，不入关系表，只在量子基础页叙述 |
| KBE | 2004 年 Queen's Birthday Honours，"for services to physics"；Sir 头衔来自 KBE，勿写成「受封爵士早于获奖」 |
| 上海中心 | 2013 任上海复杂物理中心 founding director——按 page.md 客观叙述即可 |
| 妻女 | Haruko Kinase 1973-06 结婚（Sussex 相识）；女儿 Asako 1978 年生——infobox 作 m. 1972、正文作 1973-06，以**正文 1973-06** 为准 |
| 学生 | 仅收 infobox 三人（Caldeira/Matthew P. A. Fisher/Randeria）；Matthew P. A. Fisher 勿与 Michael Fisher（20 世纪临界现象）混淆 |
| 信仰 | 天主教家庭抚养、二十岁出头停止实践信仰——一句带过，不扩写 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| superfluid helium-3 | 超流氦-3 | 诺奖核心，1970s 理论 |
| Caldeira–Leggett model | 卡尔代拉–莱格特模型 | 量子耗散 |
| Leggett–Garg inequality | 莱格特–加尔格不等式 | 宏观量子检验 |
| Leggett inequality | 莱格特不等式 | 量子力学基础 |
| quantum measurement problem | 量子测量问题 | 量子力学可能不完备 |
| macroscopic dissipative systems | 宏观耗散系统 | 研究方向设定 |
| Bose–Einstein condensate | 玻色–爱因斯坦凝聚 | 原子气体 |
| topological quantum computation | 拓扑量子计算 | 后期方向 |
| Literae Humaniores | 古典人文学科（牛津 Greats） | 第一学位 |
| MacArthur Chair | 麦克阿瑟讲席 | UIUC 教授职 |
| Knight Commander (KBE) | 大英帝国司令勋章 | 2004 |
| Institute for Quantum Computing | 量子计算研究所 | Waterloo，2006–2016 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **SEA** — Alex-Productions（75k views，流动 / 平稳）
- **匹配理由**: 「流动」字面契合超流（superfluidity）——无摩擦的持续流动是其一生科学意象；「平稳」匹配其从古典学到低温物理的从容转型与 58 年的稳定学术生涯。
- **备选**（未采用）: The Flow of Time（时间感，但已被 20 世纪多人占用且受众略低）；Daylight（明亮轻快，气质偏浅）。
- **本地路径**: `music_audio/alex-productions/92-WEqfdRXU3IU-SEA.wav`
- 批内 BGM 不重复备案：Giacconi=The Invisible Light、Abrikosov=PAST、Ginzburg=Through the Darkness、Leggett=SEA、Gross=Savage。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Anthony_J._Leggett/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构标杆 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/seed_person.py` | 人物 + 关系入库引擎（幂等） |
| `MySQL/data/Anthony_J._Leggett.yaml` | yaml 数据文件 |

> **开始执行。每完成一步汇报。**
