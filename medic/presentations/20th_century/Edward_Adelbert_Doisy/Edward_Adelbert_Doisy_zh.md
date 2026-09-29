# 医学家立传提示词（Edward Adelbert Doisy）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1943 年得主 Edward Adelbert Doisy（爱德华·阿德尔伯特·多伊西）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Edward_Adelbert_Doisy/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Edward Adelbert Doisy（1893-11-13 生于伊利诺伊州休姆 ~ 1986-10-23 逝于密苏里州圣路易斯，享年 92 岁）
- **气质关键词**：**维生素 K 化学结构的测定者、雌酮的独立发现者、圣路易斯生化系的缔造者**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1943 条目，Doisy 半边口径）：
  > "for his discovery of the chemical nature of vitamin K"（因其发现维生素 K 的化学性质）
- **设计母题**：**分子的确定（fixing the molecule）**——Dam 发现了功能性因子，Doisy 把它变成确定的化学结构；用「从模糊血影到清晰骨架式」的渐变作背景母题：模糊红点渐次显影为萘醌骨架线条。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Edward_Adelbert_Doisy/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/20th_century/Edward_Adelbert_Doisy/`。Makefile 复制后设 `MAIN=Edward_Adelbert_Doisy_zh`、`VIDEO_NAME=Edward_Adelbert_Doisy_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Doisy 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biochemistry | 生物化学 | 维生素 K 化学性质，1943 诺奖核心 | 封面、核心页 |
| 1 | endocrinology | 内分泌学 | 1930 独立发现雌酮（性激素） | 激素页 |
| 2 | nutrition science | 营养科学 | 维生素类研究方法学 | 核心页 |
| 3 | clinical biochemistry | 临床生物化学 | 圣路易斯大学生化系主任 42 年（1923–1965） | 职业页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 正文/infobox 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Otto Folin | 对方 → 导师 | infobox Doctoral advisor 明载（1920 哈佛博士；库内既有 id=3577） |
| co-honored | Henrik Dam | 无向 | 1943 诺贝尔生理学或医学奖共享（Doisy 确定维生素 K 化学性质 / Dam 发现维生素 K） |
| controversy | Adolf Butenandt | 无向 | 1930 各自独立发现雌酮，仅 Butenandt 获 1939 诺贝尔化学奖（库内既有 id=3324） |

**不入库但提示词可叙述**：妻子 Margaret（仅由「family endowed the Edward A. and Margaret Doisy College」间接出现，page.md 未明写婚姻关系，不建 spouse 边）；Washington University / Saint Louis University / Chicago 的机构同僚；Doisy 家族（研究中⼼捐赠方）。

## 五、配色方案 【人物专属】

- **气质**：美国中西部化学系的严谨、分子显影的精确
- **主色**：`#46356B`（圣路易斯紫——化学结构与学术建制的沉稳）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeVK` 维生素 K 化学 — 深紫 `#46356B`
  - `badgeEstrone` 雌酮发现 — 玫瑰 `#C4204F`
  - `badgeHarvard` 哈佛与 Folin — 深红 `#8B1A1A`
  - `badgeSLU` 圣路易斯建制 — 深蓝 `#16324F`
- **背景母题**：从模糊血影到清晰萘醌骨架式的显影渐变。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 维生素 K 化学性质的测定者 / Edward A. Doisy 1893–1986 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、伊利诺伊休姆出身、UIUC AB 1914/MS 1916、
    哈佛博士 1920、圣路易斯大学生化系主任 1923–1965、诺奖 1943、核心领域）
03  核心贡献概览 — 维生素 K 化学性质 / 雌酮 / 胰岛素结晶时代的生化建制 / 荣誉
04  伊利诺伊与哈佛 (1893–1920) — UIUC 本硕；哈佛博士 1920，师从 Otto Folin
05  华盛顿大学起步 (1919–1923) — 生化系讲师至副教授
06  圣路易斯大学建制 (1923–1965) — 创建并执掌生化系 42 年；后冠名 E.A. Doisy Department
07  雌酮的独立发现 (1930) — 与 Butenandt 各自独立；同年同物
08  诺奖的错位 — 仅 Butenandt 获 1939 化学奖；Doisy 与诺奖擦肩的第一次
09  维生素 K 之谜 — Dam 发现功能性因子，缺的是化学身份
10  化学性质的确定（核心贡献页）— 分离提纯、骨架确定；K 的德文渊源（Koagulations-Vitamin）
11  1943 共享诺奖 — Dam 与 Doisy 两句官方理由的分立呈现
12  荣誉与认可 — Willard Gibbs Award 1941；NAS 1938 / APS 1942 / AAAS 1948
13  身后与冠名 — E.A. Doisy Research Center（2007，家族 3000 万美元捐赠）；健康科学学院冠名
14  遗产与结尾 — 生化结构与临床应用的桥梁 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 1943 共享但理由句不同 | Doisy 半边 "for his discovery of the **chemical nature** of vitamin K"；Dam 半边是 "his discovery of vitamin K"——化学性质 vs 发现，两句不可互换 |
| Butenandt 口径 | 1930 **各自独立**发现雌酮（"They discovered the substance independently"）；仅 Butenandt 获 1939 化学奖——写「独立竞争/诺奖错位」，controversy 边成立，禁写合作或剽窃叙事 |
| Otto Folin | 博士导师（infobox 正文表明载，非 frontmatter-only）；1920 哈佛博士——师承边成立 |
| 妻子 Margaret | 仅出现在「family endowed the Edward A. and Margaret Doisy College」——page.md 未明写婚姻，禁建 spouse 边、禁写结婚年份 |
| 页面极短 | page.md 仅约 60 行——立传从简：不杜撰童年、家庭、学生名单；15 页规划靠结构化展开（制度页/荣誉页/冠名页）撑起 |
| 职位跨度 | 圣路易斯大学生化系教授兼主任 **1923–1965**（42 年），退休后系冠名 E.A. Doisy Department of Biochemistry（今加 Molecular Biology）——两个冠名阶段勿混 |
| 学会年份 | NAS 1938 / 美国哲学会 1942 / 美国艺术与科学院 1948——三个年份勿混 |
| Willard Gibbs Award | 1941 年获奖，先于诺奖——勿写反顺序 |
| 芝加哥讲师 | 1940 年芝加哥大学医学院医学讲师——兼职一站，勿写成任职转变 |
| 生卒 | 1893-11-13 生于 Hume, Illinois；1986-10-23 逝于 St. Louis，享年 92——超高寿得主 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| chemical nature of vitamin K | 维生素 K 的化学性质 | 获奖理由核心词，逐字对应 |
| estrone | 雌酮 | 1930 独立发现物 |
| Koagulations-Vitamin | 凝血维生素（德文） | 字母 K 的来源 |
| biochemistry | 生物化学 | 主领域与系名 |
| chairman of department | 系主任 | 1923–1965 建制角色 |
| Willard Gibbs Award | 吉布斯奖章 | 1941，先于诺奖 |
| National Academy of Sciences | 美国国家科学院 | 1938 当选 |
| E. A. Doisy Research Center | 多伊西研究中心 | 2007 冠名，家族捐赠 |
| insulin crystallization era | 胰岛素结晶时代 | 1920s 生化方法学背景（页面未展开，仅限术语级） |
| sex hormone | 性激素 | 雌酮所属类别 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Winds Of Freedom**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Doisy 的一生是「独立之姿」的注脚——独立发现雌酮、独立测定维生素 K 化学性质，虽与 Butenandt 错过诺奖、却终以 1943 共享得偿；「自由之风」对应其 42 年执掌一系、自由建构生化建制的事业。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Edward_Adelbert_Doisy/WindsOfFreedom.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
