# 医学家立传提示词（Baruch Samuel Blumberg）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1976 年得主 Baruch Samuel Blumberg（巴鲁克·萨缪尔·布伦伯格）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Baruch_Samuel_Blumberg/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Baruch Samuel Blumberg，通称 **Barry Blumberg**（1925-07-28 生于纽约布鲁克林 ~ 2011-04-05 逝于加州山景城，享年 85 岁）
- **气质关键词**：**乙肝病毒的鉴定者、乙肝疫苗的赠与者、天体生物学的掌门人**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1976 条目，两人共享同句）：
  > "for their discoveries concerning new mechanisms for the origin and dissemination of infectious diseases"（因其关于传染病起源与传播新机制的发现）
- **设计母题**：**澳抗与免费疫苗（the Australian antigen & the free vaccine）**——从澳洲原住民血液中的「澳大利亚抗原」到免费放开的乙肝疫苗；用「血液样本地图与渐次点亮的世界」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Baruch_Samuel_Blumberg/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/20th_century/Baruch_Samuel_Blumberg/`（1999 NASA 发布会像，见 images.txt）。Makefile 复制后设 `MAIN=Baruch_Samuel_Blumberg_zh`、`VIDEO_NAME=Baruch_Samuel_Blumberg_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Blumberg 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | virology | 病毒学 | 乙肝病毒鉴定与疫苗，1976 诺奖核心 | 封面、核心页 |
| 1 | human genetics | 人类遗传学 | 1950s 环球血样与人群遗传变异研究 | 核心页 |
| 2 | biochemistry | 生物化学 | infobox Fields；牛津 DPhil 生化出身 | 职业页 |
| 3 | astrobiology | 天体生物学 | NASA 天体生物学研究所首任所长（1999–2002） | 后期页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 正文/infobox 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Daniel Carleton Gajdusek | 无向 | 1976 诺贝尔生理学或医学奖两人共享（官方理由句同一） |
| colleague | Alton Sutnick | 无向 | 同事：发现澳抗系后天获得并与肝脏炎症疾病相关，首次正式连接抗原与肝炎 |
| colleague | Harvey J. Alter | 无向 | 1965 年「白血病血清中的新抗原」里程碑论文合作者 |
| controversy | Saul Krugman | 无向 | 1977 纽约学童乙肝携带者排除政策之争：Krugman 主持小组将 Blumberg 排除在外，Blumberg 为被排除儿童律师提供咨询 |
| spouse | Jean Liebesman | 无向 | 1954 结婚，育四子女 |

**不入库但提示词可叙述**：同校校友 Eric Kandel（主日学校）、Feynman/Richter（Far Rockaway 高中）——仅轶事；父母 Ida/Meyer；Willowbrook 智障儿童事件与诉讼（事件叙述）；Jonathan Chernoff/Daniel Goldin（悼念引语）；Hepatitis B Foundation/United Therapeutics/Library of Congress 等机构身份。

## 五、配色方案 【人物专属】

- **气质**：环球采样的人类学视野、疫苗金的馈赠、星尘与肝火
- **主色**：`#2F4470`（环球深蓝——五洲血样与海洋行旅）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeHBV` 乙肝病毒与疫苗 — 深金 `#B8860B`
  - `badgeGen` 人群遗传变异 — 深蓝 `#2F4470`
  - `badgeBio` 生物伦理 — 暗红 `#7A1E28`
  - `badgeNasa` 天体生物学 — 深紫 `#46356B`
- **背景母题**：世界地图上散落的采血管光点与渐次亮起的免疫金网。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 乙肝疫苗的赠与者 / Barry Blumberg 1925–2011 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、布鲁克林出身、Union College 1946、
    哥伦比亚 MD 1951、牛津 Balliol DPhil 1957、诺奖 1976、核心领域）
03  核心贡献概览 — 澳大利亚抗原 / 乙肝诊断与疫苗 / 生物伦理 / 天体生物学
04  布鲁克林的犹太教育 (1925–1943) — Yeshivah of Flatbush 希伯来原文训练；塔木德思维终身受益
05  海军与医学转折 (1943–1951) — 二战海军甲板军官；Union College；哥伦比亚数学转医学 MD 1951
06  牛津与人类变异 (1951–1957) — Balliol 生化 DPhil；1950s 环球采血研究「为何有人得病有人不得」
07  澳大利亚抗原 (1964)（核心贡献页一）— 澳洲原住民血中的 HBsAg；Sutnick 连接肝炎
08  诊断、筛查与疫苗 — 献血筛查阻断传播；疫苗研发；专利免费放开；中国儿童感染率 15%→1%（十年）
09  病毒与肝癌 — 证明该病毒可致肝癌
10  1976 共享诺奖 — 与 Gajdusek；官方理由句「传染病起源与传播的新机制」
11  生物伦理的先声 (1976–1977) — 诺奖演讲谈伦理；纽约学童排除政策之争、Willowbrook、为被排除儿童辩护（AIDS 时代先例）
12  机构和荣誉 — Fox Chase / 宾大教授 / Balliol 首位美籍 Master（1989–94）/ NASA 天体生物学研究所首任所长 / 美国哲学会会长 2005–2011
13  身后纪念 — NASA/国会图书馆天体生物学讲席；牛津 Baruch Blumberg 病毒学教授席；「预防最多癌症死亡的人」悼语
14  家与结尾 — 妻 Jean Liebesman（1954）；塔木德课每周坚持至终；2011 NASA 演讲后辞世 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 1976 两人共享同句理由 | 与 Gajdusek 共享且官方理由同句（"for their discoveries concerning new mechanisms for the origin and dissemination of infectious diseases"）——引用以 citations json 逐字为准 |
| 命名沿革 | 最初叫 **'Australian antigen'**（澳大利亚抗原），即 HBsAg——历史名与今名要点明 |
| Sutnick 的贡献 | 「首次正式连接神秘抗原与肝炎」的是同事 Sutnick——colleague 边已建，叙事勿把此步归 Blumberg 独功 |
| 专利馈赠 | Blumberg 免费放开疫苗专利以促进药企生产分发；中国儿童乙肝感染率十年 15%→1%——遗产亮点 |
| 生物伦理红线 | 1976 诺奖演讲即谈伦理：预言携带者会被排斥隔离；1977 纽约教师工会排除携带者、Willowbrook 儿童被非自愿检测、Krugman 小组将 Blumberg 排除在外、诉讼后政策被推翻——呈现以 page.md 事实为准，克制不渲染 |
| 校友轶事 | Kandel（Yeshivah of Flatbush 同学）、Feynman/Richter（Far Rockaway 高中校友）——仅一句带过，勿写成「同门」 |
| infobox 噪声 | 页面 Pennsylvania Historical Marker 栏写 "Baruch S. Blumberg (1925–**2001**)"——**2001 是错误年份**（实卒 2011-04-05），禁引用 |
| 学界评价引语 | Chernoff："prevented more cancer deaths than any person who's ever lived"；Goldin："Our planet is an improved place..."——page.md 明载可引 |
| 引语红线 | NYT 2002 访谈 "if you save a single life, you save the whole world"（犹太思想）——原文+译文可引 |
| 死亡情境 | 2011-04-05 在 NASA Ames 月球研究研讨会**主旨演讲后不久**辞世——当时任 NASA 月球科学研究所 distinguished scientist |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| Australian antigen | 澳大利亚抗原 | HBsAg 旧称，1964 发现 |
| HBsAg | 乙肝表面抗原 | 今名 |
| hepatitis B | 乙型肝炎 | 诺奖理由域 |
| chronic carrier state | 慢性携带状态 | 伦理叙事核心 |
| Hepatitis B vaccine | 乙肝疫苗 | 已知 for 词条 |
| bioethics | 生物伦理 | 1976 诺奖演讲主题 |
| genetic variation | 遗传变异 | 早期研究方向 |
| astrobiology | 天体生物学 | NASA 晚年身份 |
| Willowbrook | 柳溪（州立学校） | 事件地名，克制叙述 |
| Talmud | 塔木德 | 其思维方法自述渊源 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Shine Like The Sun**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：一项免费放开的疫苗专利让亿万儿童免于乙肝与肝癌——「如太阳般照耀众生」正是其馈赠姿态的写照；明亮大调亦呼应悼语「预防了史上最多的癌症死亡」。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Baruch_Samuel_Blumberg/ShineLikeTheSun.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
