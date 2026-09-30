# 经济学家立传提示词（Esther Duflo）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2019 年得主 Esther Duflo（埃丝特·迪弗洛）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Esther_Duflo/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Esther Caroline Duflo（1972-10-25 生于法国巴黎，在世）
- **气质关键词**：**最年轻的经济学诺奖得主、第二位女性得主、贫困世界的实验设计师**
- **诺奖获奖理由**（逐字引用，2019 三人共享）：
  > "for their experimental approach to alleviating global poverty"（表彰他们以实验性方法减轻全球贫困）
- **设计母题**：**天平上的村庄（balancing villages）**——对照组与处理组如天平两端，4 亿人的政策效果在微观尺度上被一克一克称量；视觉隐喻为左右分列的对比色块与微妙的杠杆线，呼应「微观干预、宏观称重」。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Esther_Duflo/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Esther_Duflo/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Esther_Duflo_zh`、`VIDEO_NAME=Esther_Duflo_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Duflo 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | development economics | 发展经济学 | infobox Discipline；诺奖核心 | 封面、核心页 |
| 1 | randomized controlled trials | 随机对照试验 | infobox Notable ideas 明载 | 方法页 |
| 2 | education economics | 教育经济学 | 印尼建校自然实验/印度补习项目 | 研究页 |
| 3 | microfinance | 小额信贷 | 海得拉巴 RCT，最具引用度工作之一 | 研究页 |
| 4 | gender economics | 性别经济学 | 南非养老金祖母/孙女 BMI 研究 | 研究页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Abhijit Banerjee | Duflo ← 导师 | MIT 博士联合导师（1999 博士论文） |
| advisor-student | Joshua Angrist | Duflo ← 导师 | MIT 博士联合导师（1999 博士论文） |
| advisor-student | Emily Breza | Duflo → 学生 | infobox Doctoral students 明载 |
| advisor-student | Dean Karlan | Duflo → 学生 | infobox Doctoral students 明载 |
| advisor-student | Vincent Pons | Duflo → 学生 | infobox Doctoral students 明载 |
| co-honored | Abhijit Banerjee | 无向 | 2019 三人共享（实验性方法减轻全球贫困） |
| co-honored | Michael Kremer | 无向 | 2019 三人共享（实验性方法减轻全球贫困） |
| spouse | Abhijit Banerjee | 无向 | 2015 结婚，育二子（2012/2014） |
| parent-child | Michel Duflo | Duflo ← 父 | 父·数学教授（infobox Father 明载） |

**不入库但提示词可叙述**：母亲 Violaine（仅名无姓，防歧义不入库）；Thomas Piketty（莫斯科期间鼓励其申请 MIT，个人建议非思想影响）；Daniel Cohen（招其入经济学，一次性引路人）；Emmanuel Saez（当时男友/同届入学者）；第一堂发展经济学课由 Banerjee 与 Kremer 共同执教（事件非关系）。

## 五、配色方案 【人物专属】

- **气质**：精确、柔韧、微光中的大规模证据
- **主色**：`#1E3A5F`（manifest 预分配·证据深蓝，与 Banerjee 同色系——2019 三人共享属视觉家族）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeRCT` 随机对照试验 — 深蓝 `#1E3A5F`
  - `badgeEdu` 教育与人力资本 — 青绿 `#146B5A`
  - `badgeGender` 性别与发展 — 玫瑰 `#A3455A`
  - `badgeInst` 机构与政策 — 琥珀 `#B07A2A`
- **背景母题**：天平与对比色块（处理组/对照组的左右分列），呼应 RCT 的因果称重母题。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 贫困的实验设计师 / Esther Duflo 1972– + 四色 badge + 右上头像 + 国籍行（France / United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒巴黎、ENS 历史与经济、DELTA 硕士 1995、
    MIT PhD 1999、MIT 贫困缓解与发展经济学讲席教授、诺奖 2019、核心领域）
03  核心贡献概览 — RCT 方法论 / 教育回报 / 小额信贷 / 性别与家庭资源配置
04  早年：阿涅尔与亨利四世中学 (1972–1990) — 母亲的 NGO 人道之旅
05  ENS 与莫斯科转折 (1990–1995) — 历史转经济学、俄央行助理、Piketty 建议申请 MIT
06  MIT 博士：双重导师 (1995–1999) — Banerjee/Angrist 联合指导，印尼建校自然实验
07  教育的因果回报（核心贡献页）— AER 论文 0.12–0.19 年教育增量与工资提升
08  田野的扩展：补习教育与 TaRL — QJE 2007 与教学适配层级项目
09  小额信贷的冷水 — 海得拉巴 RCT，低消费效应与行业反弹
10  性别与资源分配 — 南非养老金研究：祖母养老金与孙女 BMI
11  J-PAL 与机构领导 — 共创/共掌 J-PAL、2010 克拉克奖章、2024 巴黎经济学院院长
12  2019 诺贝尔奖 — 最年轻得主（46 岁）、继 Ostrom 后第二位女性、"megaphone" 电话回应
13  荣誉与影响 — 法国荣誉军团勋章 2020、阿斯图里亚斯亲王奖 2015、苏黎世大学 2026 赴任
14  遗产与结尾 — 循证扶贫的科学化 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 双重身份关系 | Banerjee 对 Duflo 同时是博士导师、丈夫、共同得主——三条关系 note 各自写清，勿混；Banerjee 当时尚与前妻婚姻中（page.md 明载 met in 1995 / married 2015，叙述时间线须准确） |
| "第二位女性"表述 | page.md 明载 "the youngest person (at age 46) and the second woman to win this award (after Elinor Ostrom in 2009)"——可写，勿加"第三位/首位"等发挥 |
| 获奖理由归属 | citation 是 "their"（三人共享）；个人电话回应引语（"at an extremely opportune and important time"/"megaphone"）page.md 载英文原文可引 |
| BJP 争议段 | page.md 末载 BJP 因其夫获奖而发表的贬损言论——**政治敏感内容，全部禁写** |
|母亲名字 | 母亲仅名 Violaine 无姓，页首信息网格可写"母亲是小儿科医生"，**不入库**（防歧义） |
| J-PAL 首任主管 | Rachel Glennerster 是 J-PAL 首任主管且是 Kremer 之妻（page.md 明载）——本篇可叙述，关系边归属 Kremer yaml |
| Clark Medal 年份 | 2010 年约翰·贝茨·克拉克奖章（40 岁以下），infobox Awards 列 2010，勿与 2002 Elaine Bennett 奖混淆 |
| Calvó-Armengol 年份 | page.md 正文一处写 (2019)、获奖列表写 (2009)（首届）——以 2009 为准，陷阱表存疑注 |
| 巴黎经济学院 | 2024 起任院长（president）；2023 起 Collège de France 讲席——两个机构头衔勿混 |
| 苏黎世时间线 | 2025-10 宣布、2026-07 赴任 UZH（与 Banerjee 共同），MIT 保留——同 Banerjee 篇口径一致 |
| 诺奖演讲 | 2019-12-08 *Field experiments and the practice of policy*（注意与 Banerjee 的 ...practice of **economics** 一字之差） |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| randomized controlled trial (RCT) | 随机对照试验 | 获奖理由核心词 |
| development economics | 发展经济学 | 学科主领域 |
| natural experiment | 自然实验 | 印尼建校研究的设计类型 |
| microfinance / microcredit | 小额信贷/微贷款 | 研究对象，结论为"证据不足" |
| teaching at the right level (TaRL) | 适配层级教学 | 印度补习研究衍生的教育项目 |
| John Bates Clark Medal | 约翰·贝茨·克拉克奖章 | 2010，40 岁以下经济学家奖 |
| École Normale Supérieure | 巴黎高等师范学院 | 本科（历史与经济） |
| Paris School of Economics | 巴黎经济学院 | DELTA 硕士与 2024 院长职 |
| J-PAL | 贫困行动实验室 | 共同创立与共同执掌 |
| Collège de France | 法兰西公学院 | 2023 起贫困与公共政策讲席 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Mirage**（manifest 预分配，音乐库 `music_audio/inspiring-electronic/04-5gcb94jhG1I-Notan Nigres - Mirage (Audio).wav`，选曲参考 `curated_tracks.md`）
- **匹配理由**：与 Banerjee 篇同曲（同届共享得主的视觉/听觉家族）；Mirage 的电子冷光质感贴合"把 4 亿人的政策效果称量到小数点后"的精密与克制，也暗合从幻象（直觉教条）到实证的学科转向。
- **本地路径**：复制 `music_audio/inspiring-electronic/04-5gcb94jhG1I-Notan Nigres - Mirage (Audio).wav` 到 `economics/presentations/21th_century/Esther_Duflo/Mirage.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
