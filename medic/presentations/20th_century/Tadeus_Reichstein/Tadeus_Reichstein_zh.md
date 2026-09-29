# 医学家立传提示词（Tadeus Reichstein）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1950 年得主 Tadeus Reichstein（塔德乌什·赖希施泰因）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Tadeus_Reichstein/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Tadeusz Reichstein，亦作 **Tadeus Reichstein**（1897-07-20 生于波兰弗沃茨瓦韦克（时属俄国 partition） ~ 1996-08-01 逝于瑞士巴塞尔，享年 99 岁）
- **气质关键词**：**维生素 C 的独立合成者、可的松的分离者、最长寿的诺奖得主（时年纪录）**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1950 条目，三人共享同句）：
  > "for their discoveries relating to the hormones of the adrenal cortex , their structure and biological effects"（因其关于肾上腺皮质激素的结构与生物学效应的发现）
- **设计母题**：**合成的双峰（two syntheses）**——1933 维生素 C 的 Reichstein process 与 1950 前后的可的松分离；用「两条化学合成路线从同一烧瓶分岔」的抽象图形作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Tadeus_Reichstein/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/20th_century/Tadeus_Reichstein/`（弗沃茨瓦韦克纪念牌/巴塞尔故居纪念牌，见 images.txt）。Makefile 复制后设 `MAIN=Tadeus_Reichstein_zh`、`VIDEO_NAME=Tadeus_Reichstein_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Reichstein 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | organic chemistry | 有机化学 | 巴塞尔大学有机化学教授（1946–1967）；1950 诺奖核心 | 封面、核心页 |
| 1 | carbohydrate chemistry | 糖类化学 | 维生素 C（抗坏血酸）独立合成，Reichstein process | 核心页 |
| 2 | steroid chemistry | 甾体化学 | 肾上腺皮质激素分离，可的松 | 核心页 |
| 3 | phytochemistry | 植物化学 | 晚年蕨类植物化学与细胞学 80+ 论文 | 后期页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 正文/infobox 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Hermann Staudinger | 对方 → 导师 | 卡尔斯鲁厄理工学院随 Staudinger 学习（其短暂执教期；库内既有 id=3329，1953 诺贝尔化学奖得主） |
| colleague | Leopold Ružička | 无向 | 卡尔斯鲁厄同期博士生，后其在苏黎世 ETHZ 实验室促成维生素 C 合成（库内规范名带变音符，id=3327） |
| colleague | Norman Haworth | 无向 | 1933 各自独立合成维生素 C（英国团队；库内既有 id=3308） |
| co-honored | Edward Calvin Kendall | 无向 | 1950 诺贝尔生理学或医学奖共享（官方理由句同一）；1951 又共享 Cameron Prize |
| co-honored | Philip Showalter Hench | 无向 | 1950 诺贝尔生理学或医学奖共享（官方理由句同一） |
| spouse | Henriette Louise Quarles van Ufford | 无向 | 1927 结婚，育一子 |

**不入库但提示词可叙述**：父母 Gastawa（Brockmann）与 Izydor Reichstein（仅具名）；Tadeusz Kościuszko（命名渊源，18 世纪波兰民族英雄）；Rita Levi-Montalcini（2008 超越其长寿纪录，仅比较句）。

## 五、配色方案 【人物专属】

- **气质**：瑞士的精确、波兰的乡愁、双峰合成的化学之美
- **主色**：`#0F4C81`（巴塞尔湖蓝——莱茵河畔实验室的冷静精确）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeVC` 维生素 C 合成 — 湖蓝 `#0F4C81`
  - `badgeCort` 皮质激素与可的松 — 深金 `#B8860B`
  - `badgeFern` 蕨类植物化学 — 苔绿 `#175E54`
  - `badgeExile` 波兰-瑞士流徙 — 深紫 `#46356B`
- **背景母题**：同一烧瓶分岔出的两条合成路线（糖链→维生素 C；甾体→可的松）。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 双峰合成的大师 / Tadeus Reichstein 1897–1996 + 四色 badge + 右上头像 + 国籍行（Switzerland）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、弗沃茨瓦韦克出身、ETHZ、巴塞尔大学药物化学/
    有机化学教授 1937–1967、诺奖 1950、享年 99、核心领域）
03  核心贡献概览 — 维生素 C 合成 / 可的松分离 / 蕨类植物化学 / 长寿纪录
04  弗沃茨瓦韦克与流徙童年 (1897–1907) — 波兰犹太富商家庭；基辅童年；1905 pogroms 后经耶拿赴苏黎世；
    以民族英雄 Kościuszko 命名
05  卡尔斯鲁厄：Staudinger 门下 (1910s–1920s) — 师承起点；同窗 Ruzicka
06  ETHZ 与维生素 C (1933)（核心贡献页一）— 在 Ruzicka 实验室独立合成抗坏血酸；Reichstein process 命名
07  独立的三重奏 — 与英国 Haworth 团队各自独立；工业合成法沿用至今
08  巴塞尔教授席 (1937–1967) — 药物化学教授 1937；有机化学教授 1946–1967
09  肾上腺皮质激素与可的松 (1940s)（核心贡献页二）— 皮质激素分离工作以可的松分离告成
10  1950 三人共享诺奖 — 与 Kendall、Hench；官方理由句；1950-12-11 演讲《Chemistry of the Adrenal Cortex Hormones》
11  1951 Cameron Prize — 与 Kendall 联合再获爱丁堡奖
12  晚年转向：蕨类 — 植物化学与细胞学；染色体数目与杂交史解读；80+ 论文
13  99 岁与纪录 — 时为最长寿诺奖得主（2008 被 Levi-Montalcini 超越）；Marcel Benoist 1947 / Copley 1968 / 皇家学会外籍会员
14  遗产与结尾 — Reichstein process 的现代工业地位 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 姓名两种拼写 | page.md 标题/正文 **Tadeusz Reichstein**、"also known as **Tadeus Reichstein**"；yaml/manifest 用 **Tadeus Reichstein**（★库内另有 bare stub "Tadeusz Reichstein" #3843 待主控合并，勿引用该记录） |
| 生年双值 | frontmatter 1897-07-**08** vs 正文/infobox **1897-07-20**——以正文 07-20 为准，yaml 填 1897-07-20，陷阱表注明 |
| 1950 共享同句理由 | 与 Kendall、Hench 共享且官方理由同句（"for their discoveries relating to the hormones of the adrenal cortex, their structure and biological effects"）——引用以 citations json 逐字为准 |
| 维生素 C 的「独立」 | 1933 合成是 **independently of** Norman Haworth 及其英国团队——两条独立路线，勿写成合作或先后师承；colleague 边 note 注明独立 |
| Reichstein process | 人工合成维生素 C 的主要工业流程至今以其命名——遗产亮点，与诺奖理由（皮质激素）区分 |
| Ruzicka 的拼写 | 库内规范名 **Leopold Ružička**（带变音符，id=3327，1939 化学诺奖得主）——yaml 用此形式，正文两可 |
| Staudinger 的教职 | 师承发生在 Staudinger 于卡尔斯鲁厄理工的**短暂执教期**——note 点明；Staudinger 后以高分子化学获 1953 化学诺奖 |
| 国籍口径 | yaml/总表按 Nobel 官方口径 **Switzerland**（Swiss chemist）；frontmatter Switzerland+Poland、infobox Citizenship 双列——正文可叙述波兰出生与波兰-瑞士双重身份 |
| 童年叙事分寸 | 1905 年俄国全境 pogroms 促使全家考虑移民——史实克制陈述；波裔犹太家庭与爱国传统一句带过 |
| 长寿纪录 | 99 岁辞世（1996-08-01），**当时**最长寿诺奖得主，2008 被 Rita Levi-Montalcini 超越——「当时」限定词必须保留 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| Reichstein process | 赖希施泰因法 | 维生素 C 工业合成流程 |
| ascorbic acid | 抗坏血酸（维生素 C） | 1933 合成对象 |
| cortisone | 可的松 | 1950 诺奖理由域的分离成果 |
| hormones of the adrenal cortex | 肾上腺皮质激素 | 获奖理由核心词 |
| carbohydrate chemistry | 糖类化学 | 维生素 C 合成的学科归属 |
| steroid chemistry | 甾体化学 | 皮质激素的学科归属 |
| phytochemistry | 植物化学 | 晚年蕨类方向 |
| polyploidy | 多倍性 | 蕨类细胞学研究关键词 |
| Marcel Benoist Prize | 马塞尔·伯努瓦奖 | 瑞士科学奖，1947 |
| Cameron Prize | 卡梅伦奖 | 1951 与 Kendall 共享 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Daylight**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Reichstein 的一生横跨整个 20 世纪（1897–1996）——从俄国 partition 的暗夜童年到苏黎世的晨光实验室，再到 99 岁的世纪暮年；「天光」对应其穿越黑暗时代、在瑞士安放一生的明亮终章。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Tadeus_Reichstein/Daylight.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
