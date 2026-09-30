# 经济学家立传提示词（Ragnar Frisch）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1969 年得主 Ragnar Frisch（拉格纳·弗里施）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Ragnar_Frisch/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Ragnar Anton Kittil Frisch（1895-03-03 生于克里斯蒂安尼亚（今奥斯陆） ~ 1973-01-31 逝于奥斯陆，享年 77 岁）
- **气质关键词**：**"计量经济学"与"宏观/微观"的命名者、经济学定量化的总设计师、银匠世家出身的诺奖首帧**
- **诺奖获奖理由**（1969 与 Jan Tinbergen 共享首届奖，逐字引用 manifest）：
  > "for having developed and applied dynamic models for the analysis of economic processes"（表彰他们为经济过程分析开发并应用了动态模型）
- **设计母题**：**命名与量化（naming & quantification）**——一个人为一门学科定名（econometrics 1926）、把经济世界一分为二（micro/macro 1933）；视觉上以「镌刻字模 + 坐标网格」的意象构成背景母题，呼应银匠家世的镌刻手艺与统计定量的精确。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Ragnar_Frisch/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/Ragnar_Frisch/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位；正文配有父亲 Anton Frisch 照片可作早年页插图）；Makefile 复制后设 `MAIN=Ragnar_Frisch_zh`、`VIDEO_NAME=Ragnar_Frisch_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Frisch 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | econometrics | 计量经济学 | 1926 年创造该术语；Econometric Society 创始人、Econometrica 首任主编 21 年 | 封面、核心页 |
| 1 | production theory | 生产理论 | 数学化生产理论，不可分投入与联合性 | 核心页 |
| 2 | macroeconomics | 宏观经济学 | 1933 年提出 micro/macro 二分术语 | 核心页 |
| 3 | business cycle theory | 经济周期理论 | 1933 冲击-传播模型，新古典周期理论源头之一 | 周期页 |
| 4 | utility theory | 效用理论 | 1926 论文对序数/基数效用的公理化 | 方法页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Jan Tinbergen | 无向 | 1969 首届诺贝尔经济学奖共享（发展并应用动态模型分析经济过程） |
| advisor-student | Olav Reiersøl | Frisch→学生 | infobox Doctoral students 明载 |
| advisor-student | Trygve Haavelmo | Frisch→学生 | infobox Doctoral students 明载；1989 经济学诺奖得主 |
| colleague | Irving Fisher | 无向 | 1927 洛克菲勒访美期间交往的计量先驱 |
| colleague | Wesley Clair Mitchell | 无向 | 1927 访美交往；Mitchell 推广了 Frisch 的投资-波动论文 |
| colleague | Allyn Young | 无向 | 1927 访美交往的数理经济学者 |
| colleague | Henry Schultz | 无向 | 1927 访美交往的数理经济学者 |
| spouse | Marie Smedal | 无向 | 1920 年结婚，1952 年去世 |
| spouse | Astrid Johannessen | 无向 | 1953 年再婚，童年好友，1980 年去世 |
| parent-child | Anton Frisch | 父→子 | 奥斯陆金银匠，Frisch 家族世代为 Kongsberg 银矿工匠 |

**不入库但提示词可叙述**：女儿 Ragna（1938 年生，page.md 仅名无全名）；孙女 Nadia Hasnaoui（电视主持人，隔代）；Paul Samuelson 归功 Frisch 在 1930 耶鲁讲义上首创现代意义的"model"一词（术语归属叙述，非关系）；Kenneth Arrow 曾撰《The Work of Ragnar Frisch, Econometrician》书评式综述（文献关系）。

## 五、配色方案 【人物专属】

- **气质**：北欧的清冽精确、手艺人与科学家的双重自律
- **主色**：`#1E3A5F`（峡湾深蓝——计量定量的冷峻与挪威底色）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeEcm` 计量经济 — 靛蓝 `#1E3A5F`
  - `badgeProd` 生产理论 — 青绿 `#145C54`
  - `badgeCycle` 周期理论 — 琥珀 `#C07A2A`
  - `badgeCraft` 银匠家世 — 玫瑰灰 `#8A5A5A`
- **背景母题**：镌刻字模与坐标网格——银匠錾刻的字母与统计坐标系叠加，呼应"为一门学科定名"的设计主题。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 计量经济学命名者 / Ragnar Frisch 1895–1973 + 四色 badge + 右上头像 + 国籍行（Norway）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒奥斯陆、教育奥斯陆大学 dr.philos. 1926、
    任职奥斯陆大学 1931 正教授/经济研究所所长、诺奖 1969 首届、核心领域）
03  核心贡献概览 — 命名 econometrics/micro/macro / 生产理论 / 冲击-传播周期模型 / 效用公理化
04  银匠学徒 (1895–1919) — 家族三百年金银手艺；母亲建议下边学艺边读皇家弗雷德里克大学
05  转向科学：1919 学位与 1921 游学 — 法英三年研读经济学与数学
06  1926：双论文之年（核心贡献页）— 铸造 "econometrics" 一词；《Sur un problème d'économie pure》
    效用公理化；数学统计 dr.philos. 学位
07  访美岁月 (1927) — 洛克菲勒奖学金；与 Fisher/Mitchell/Young/Schultz 交往；Mitchell 推广其论文
08  1931/1932：教授与研究所 — 正教授；创建洛克菲勒资助的经济研究所并任研究主任
09  1933：micro/macro 与冲击-传播模型（核心贡献页）— 术语二分；周期理论成新古典源头
10  Econometrica 与计量学会 — 1930 创始人之一；主编 21 年；Frisch Medal 以其命名
11  战时囚禁 (1943–1944) — 与 13 位同事百余名学生被捕；Bredtveit/Berg/Grini 三营流转
12  1969 首届诺贝尔经济学奖 — 与 Tinbergen 共享；官方理由逐字
13  荣誉与身后 — Feltrinelli 奖 1961；奥斯陆大学经济研究所大讲堂与其名；Frisch Centre
14  遗产与结尾 — 养蜂与遗传学爱好的人性一笔 + 经济学定量化的总设计师 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 首届奖共享 | 1969 首届奖与 Tinbergen **共享**，理由用"他们"；Frisch 篇与 Tinbergen 篇各自忠于本人页面叙事，共享事实两边都要醒目标注 |
| 三个术语的年份 | econometrics=1926 创造；microeconomics/macroeconomics=1933 提出；勿混写年份。"model"一词现代经济含义由 Samuelson 归功于 Frisch 1930 耶鲁讲义（归属句式：Samuelson 认为系 Frisch 首创） |
| 学位名称 | 1926 年获 **dr.philos.** 学位（数学统计方向）——挪威体系学位，勿写成 PhD 导师-学生关系（page.md 无导师记载，frontmatter 也无 doctoral_advisor） |
| 拒绝耶鲁 | 1930-31 在耶鲁短暂任教后获正教授席位，因同事力劝回国而**婉拒**；1931 由国王枢密院任命为奥斯陆经济学与统计学教授——勿写成"耶鲁教授多年" |
| 战时经历 | 1943-10 与 13 位奥斯陆大学同事及百余学生被捕；Bredtveit（1943-10-17 起）→Berg（1943-11-22 起）→Grini（1943-12-09~1944-10-08）三营时序勿颠倒 |
| Frisch–Waugh 定理 | 与 Frederick V. Waugh 提出（Econometrica 1933），后称 Frisch–Waugh–Lovell 定理；Waugh 未入库（合著定理，非持续关系），提示词可叙述 |
| 经济学"最短最易" | 选经济学只因它看似"大学里最短最容易的科目"（page.md 原话转述）——人生转折的真实细节，勿美化为"志向远大" |
| 养蜂 | 最重要的爱好是养蜂并做遗传学研究——可作结尾页人性细节 |
| 生卒无冲突 | frontmatter 与正文一致（1895-03-03 / 1973-01-31），直接使用 |
| 国籍口径 | yaml 按 Nobel 口径仅 Norway；正文明载生于 Kristiania（今奥斯陆） |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| econometrics | 计量经济学 | 1926 年 Frisch 造词；全篇统一译名 |
| microeconomics / macroeconomics | 微观/宏观经济学 | 1933 年二分术语，勿写成其"发明了两个学科" |
| impulse-propagation | 冲击-传播机制 | 1933 周期模型核心 |
| Frisch–Waugh–Lovell theorem | FWL 定理 | 回归分解定理，1933 Econometrica |
| Frisch elasticity | 弗里施弹性 | 劳动供给弹性概念，infobox Known for 明载 |
| ordinal / cardinal utility | 序数/基数效用 | 1926 公理化对象 |
| conjectural variation | 推测变差 | 寡头理论方法 |
| dr.philos. | 挪威博士学位 | 1926，数学统计方向 |
| Econometrica | 《经济计量学》期刊 | 学会会刊，Frisch 主编 21 年 |
| Grini detention camp | 格里尼拘留营 | 战时关押终点站 1943-12~1944-10 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**New Lands**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**："新大陆"对应首届诺奖与经济定量化新疆域的双重开拓——Frisch 为一门古老学科铸新名、立新法，是从零到一的拓荒者；与 Tinbergen 同配一首也暗合 1969 共享奖的"同一乐章两人奏"。
- **本地路径**：复制 `music_audio/alex-productions/74-oK8HN0FsZmc-New-Lands.wav` 到 `economics/presentations/20th_century/Ragnar_Frisch/NewLands.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
- **撞曲说明**：与 Tinbergen 篇同曲（manifest 预分配如此）；出片阶段如需去重由主控统一裁定。
