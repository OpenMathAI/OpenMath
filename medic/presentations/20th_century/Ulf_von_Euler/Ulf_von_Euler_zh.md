# 医学家立传提示词（Ulf von Euler）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1970 年得主 Ulf von Euler（乌尔夫·冯·奥伊勒）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Ulf_von_Euler/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Ulf Svante von Euler-Chelpin（1905-02-07 生于瑞典斯德哥尔摩 ~ 1983-03-09 逝于斯德哥尔摩，享年 78 岁）
- **气质关键词**：**去甲肾上腺素的鉴定者、前列腺素的发现者、科学世家的诺奖二代**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1970 条目，与 Katz、Axelrod 三人共享同一理由）：
  > "for their discoveries concerning the humoral transmitters in the nerve terminals and the mechanism for their storage, release and inactivation"（因他们发现神经末梢中的体液递质及其贮存、释放与失活机制）
- **设计母题**：**突触小泡里的递质（vesicular storage）**——去甲肾上腺素贮存于神经末梢胞内小泡的意象：以小泡点亮的突触末梢图案作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Ulf_von_Euler/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；第 0/1/2/3 步按 medic 路径执行：页面已在 `medic/presentations/pages/20th_century/Ulf_von_Euler/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Ulf_von_Euler_zh`、`VIDEO_NAME=Ulf_von_Euler_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | physiology | 生理学 | infobox 首要领域；卡罗林斯卡讲席 1939–1971 |
| 1 | pharmacology | 药理学 | 1930 药理学助理教授起步 |
| 2 | neurochemistry | 神经化学 | substance P/前列腺素/去甲肾上腺素等内源活性物质 |
| 3 | biochemistry | 生物化学 | 递质分布与代谢的组织化学分析 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| parent-child | Hans von Euler-Chelpin | 对方 → 父 | 化学教授，1929 诺贝尔化学奖得主；库内规范名 id=3226 |
| parent-child | Astrid Cleve | 对方 → 母 | 植物学与地质学教授；库内规范名 id=3233 |
| advisor-student | Robin Fåhraeus | 对方 → 导师 | 卡罗林斯卡血沉与流变学导师（博士论文 1930） |
| advisor-student | Henry Dale | 对方 → 导师 | 1930–31 Rochester 奖学金伦敦博士后导师（Dale 实验室） |
| colleague | John H. Gaddum | 无向 | 1931 共同发现 autopharmacological 原理 substance P |
| colleague | G. Liljestrand | 无向 | 早年合作，Euler–Liljestrand 机制（肺局部缺氧动脉分流） |
| spouse | Jane Sodenstierna | 无向 | 1930 结婚 1957 离异，育四子女 |
| spouse | Dagmar Cronstedt | 无向 | 1958 结婚（伯爵夫人、电台主播） |
| co-honored | Bernard Katz | 无向 | 1970 诺贝尔生理学或医学奖三人共享（神经末梢体液递质及贮存释放失活机制） |
| co-honored | Julius Axelrod | 无向 | 1970 诺贝尔生理学或医学奖三人共享（神经末梢体液递质及贮存释放失活机制） |

**不入库但提示词可叙述**：外祖父 Per Teodor Cleve（铥与钬的发现者，家世叙述）；Daly/Heymans/Embden/Hill/Braun-Menéndez（留学游历各站导师，一次性访问关系；其中 Dale/Heymans/Hill/Houssay 后获诺奖——page.md 明载趣闻可写）；Houssay（布宜诺斯艾利斯研究所创办人，机构叙述）。

## 五、配色方案 【人物专属】

- **气质**：北欧的清冽、科学世家的从容、突触末梢的微光
- **主色**：`#1E4E79`（波罗的海蓝——卡罗林斯卡的沉静）+ 香槟金诺奖色
- **badge 四分类色**：`badgeNA` 去甲肾上腺素 深蓝 `#1E4E79`；`badgeSP` substance P 青绿 `#0E7C7B`；`badgePG` 前列腺素 琥珀 `#C07A2A`；`badgeFamily` 科学世家 玫瑰 `#A63A2B`
- **背景母题**：小泡点亮的突触末梢图案，呼应「突触小泡里的递质」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 去甲肾上腺素的鉴定者 / Ulf von Euler 1905–1983 + 四色 badge + 右上头像 + 国籍行（Sweden）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1905-02-07 ~ 1983-03-09 斯德哥尔摩、
    卡罗林斯卡 MD、生理学教授 1939–1971、诺奖 1970、父亲 1929 化学诺奖）
03  核心贡献概览 — substance P / 前列腺素 / 去甲肾上腺素 / 囊泡贮存
04  科学世家 (1905–1922) — 父 Hans（1929 化学诺奖）、母 Astrid（教授）、
    外祖父 Cleve（发现铥与钬）
05  卡罗林斯卡求学 (1922–1930) — Fåhraeus 门下血沉与流变学、血管收缩病理生理、
    1930 博士论文与药理学助理教授
06  环球游学 (1930–1938) — 伦敦 Dale 实验室（1931 与 Gaddum 发现 substance P）、
    Birmingham/根特 Heymans/法兰克福 Embden、1934 Hill 门下学生物物理、1938 G. L. Brown
    神经肌肉传递
07  Euler–Liljestrand 机制 — 与 Liljestrand 早年的肺局部缺氧动脉分流发现
08  五种内源活性物质 (1931–1946)（核心贡献页）— substance P、前列腺素、vesiglandin (1935)、
    piperidine (1942)、noradrenaline (1946)
09  1946 之后：去甲肾上腺素专攻（核心贡献页）— 分布与命运、生理与病理条件、
    发现 NA 贮存于神经末梢胞内小泡——改变领域进程
10  1970 诺奖 — 与 Katz（量子式释放）、Axelrod（再摄取）共享；Nobel 讲演
    "Adrenergic Neurotransmitter Functions"（1970-12-12）
11  诺贝尔委员会与科学组织 — 1953 起活跃于诺贝尔基金会、卡罗林斯卡医学生理或医学
    委员会成员、1965 起董事会主席；IUPS 副主席 1965–71；世界文化理事会创始成员 1981
12  荣誉与认可 — Gairdner 1961、Jahre 1965、Stouffer 1967、Carl Ludwig 奖章 1953、
    Schmiedeberg 纪念章 1969、美国哲学会 1970、AAAS/NAS 1972、ForMemRS 1973
13  家庭 — 父母与外祖父的科学谱系；两段婚姻（Jane 1930–57 四子女、
    Dagmar 1958–）；长子 Hans Leo 任 US NIH 科学管理
14  遗产与结尾 — 从 substance P 到 NA 囊泡贮存：自主神经药理学的骨架
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 诺奖二代 | 父 Hans von Euler-Chelpin 获 **1929 诺贝尔化学奖**（非生理学医学）——两代诺奖是本篇亮点，学科勿写错 |
| 三人分工 | von Euler：去甲肾上腺素的递质身份、分布与囊泡贮存；Katz：突触量子式释放；Axelrod：再摄取与失活——citation 同一句，侧重分层 |
| substance P 发现 | 1931 年在 **Dale 实验室**与 **John H. Gaddum** 共同发现——勿写成独发现 |
| 五种物质清单 | substance P / prostaglandin / vesiglandin (1935) / piperidine (1942) / noradrenaline (1946)——年份与清单对应勿串 |
| 前列腺素 | von Euler 是前列腺素的**发现者**（1935 上下文），但前列腺素结构解析与命名发展是后人工作——表述从简 |
| 游学名单 | Daly/Heymans/Embden/Hill/Braun-Menéndez 为各站访问导师——不建边；"Dale、Heymans、Hill、Houssay 后获诺奖"是 page.md 明载趣闻可写 |
| 两段婚姻 | Jane Sodenstierna（1930–1957，四子女）与 Dagmar Cronstedt（1958–）——两条 spouse 边；Dagmar 战时 Radio Königsberg 经历 page.md 明载但与科学无关，正文一笔带过或略去 |
| 卡罗林斯卡职务 | 1939–1971 生理学正教授；诺贝尔委员会成员/1965 起董事会主席——与其获奖的独立性无涉，可作机构叙述 |
| 卒地 | 逝于斯德哥尔摩（1983-03-09），与生地同城 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| noradrenaline / norepinephrine | 去甲肾上腺素 | 1946 鉴定；NA/NAd 缩写 |
| substance P | P 物质 | 1931 与 Gaddum 共同发现 |
| prostaglandin | 前列腺素 | von Euler 发现命名 |
| vesicular monoamine transporter | 囊波单胺转运体 | NA 贮存于突触末梢胞内小泡 |
| Euler–Liljestrand mechanism | 奥伊勒–利耶斯特兰德机制 | 肺局部缺氧性动脉分流 |
| autopharmacological principle | 自体药理学原理 | substance P 的早期定性 |
| neuromuscular transmission | 神经肌肉传递 | 1938 与 G. L. Brown 研究 |
| World Cultural Council | 世界文化理事会 | 1981 创始成员 |
| Nobel Committee for Physiology or Medicine | 卡罗林斯卡诺贝尔委员会 | 成员/董事会主席 |
| ForMemRS | 英国皇家学会外籍院士 | 1973 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**New Lands**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：从 substance P 到前列腺素再到去甲肾上腺素——von Euler 一生接连抵达内源活性物质的"新大陆"；"New Lands" 匹配其五次开疆式发现与环球游学的科学人生。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Ulf_von_Euler/New_Lands.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
