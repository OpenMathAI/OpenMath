# 经济学家立传提示词（Trygve Haavelmo）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1989 年得主 Trygve Haavelmo（特里夫·哈维默）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Trygve_Haavelmo/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Trygve Magnus Haavelmo（1911-12-13 生于挪威 Skedsmo ~ 1999-07-28 逝于奥斯陆，享年 87 岁）
- **气质关键词**：**计量经济学的概率论奠基人、联立方程的解读者、因果推断的先声**
- **获奖理由**（1989 独得，逐字引用，中文翻译照抄总名录）：
  > "for his clarification of the probability theory foundations of econometrics and his analyses of simultaneous economic structures"
  > （表彰他阐明了经济计量学的概率论基础，并对联立经济结构进行了分析）
- **设计母题**：**概率云与联立方程（probability cloud & simultaneous equations）**——把经济结构看作一组联立的假想实验方程，观测点如概率云般围绕其散布；散点云 + 方程网格构成背景母题，暗合其获奖理由的两个组成部分。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Trygve_Haavelmo/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**路径按 economics 执行**：页面已在 `economics/presentations/pages/20th_century/Trygve_Haavelmo/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Trygve_Haavelmo_zh`、`VIDEO_NAME=Trygve_Haavelmo_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Haavelmo 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | econometrics | 经济计量学 | 研究核心与诺奖理由主词 | 封面、核心页 |
| 1 | probability theory | 概率论基础 | *The Probability Approach in Econometrics*（1941 完成于哈佛，1946 学位） | 核心页 |
| 2 | macroeconomics | 宏观经济学 | infobox Discipline；均衡预算乘数 | 贡献页 |
| 3 | causal inference | 因果推断 | 经济模型即假想实验、政策模拟思想，do-calculus 思想源头 | 遗产页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | John Maynard Keynes | 无向 | infobox Influences；neo-Keynesian 传统（库内规范名复用 #850） |
| influence | Ragnar Frisch | 无向 | infobox Influences；经其推荐入经济研究所、任其助手 |
| influence | Jan Tinbergen | 无向 | infobox Influences |
| influence | Judea Pearl | 无向 | Pearl 追溯因果推断思想源头至 Haavelmo（库内规范名复用 #269） |
| influence | Robert H. Strotz | 无向 | 1960 首先将 Haavelmo 的政策模拟思想操作化 |
| influence | Herman Wold | 无向 | 1960 与 Strotz 共同操作化，"wiping out" 方程 |

**不入库但提示词可叙述**：Nortraship（战时纽约统计部任职，机构不入库）；Oslo 经济研究所（机构）；Alfred Cowles 无涉。**本篇 relations=6 为 page.md 明载诚实值，在世家人（配偶/子女）page.md 完全无载禁写**——防止 Review 误判为缺漏。

## 五、配色方案 【人物专属】

- **气质**：清冷、数学、北欧的克制
- **主色**：`#A63A2B`（挪威赤陶红——manifest 预分配；对应概率云散点的暖色与奥斯陆学派的厚重）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeProb` 概率方法 — 深蓝 `#1E3A5F`
  - `badgeSim` 联立结构 — 灰紫 `#52307C`
  - `badgeMacro` 宏观与乘数 — 深青 `#0E4D64`
  - `badgeCausal` 因果推断 — 琥珀 `#C07A2A`
- **背景母题**：概率散点云与联立方程网格（观测点围绕假想实验方程散布的抽象），呼应「概率云与联立方程」母题。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 计量经济学的概率论奠基人 / Trygve Haavelmo 1911–1999 + 四色 badge + 右上头像 + 国籍行（Norway）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地 Skedsmo、教育 Oslo 大学/UCL、
    任职 Oslo 大学教授 1948–79、Aarhus/Chicago 讲学与访学、诺奖 1989、核心领域）
03  核心贡献概览 — 概率方法 / 联立经济结构 / 均衡预算乘数 / 因果推断先声
04  早年 Skedsmo 与奥斯陆 (1911–1930s) — Oslo Cathedral School；1930 经济学学位；Frisch 推荐入经济研究所
05  Frisch 门下与游学 — 助手与计算主管；1936 UCL 统计学；柏林/日内瓦/牛津；1938 Aarhus 讲师
06  战时纽约与哈佛论文 (1939–1946) — 奖学金赴美；Nortraship 统计部；
    *The Probability Approach in Econometrics* 1941 哈佛完成
07  概率方法：计量的概率论基础（核心贡献页）— 经济模型即一系列假想实验；1946 奥斯陆 PhD
08  联立经济结构分析 — *The Statistical Implications of a System of Simultaneous Equations*；
    Pearl 称之为"causal counterparts 的转折点"（引语英文原文）
09  均衡预算乘数 — 宏观政策分析的名片贡献
10  奥斯陆教授岁月 (1948–1979) — 经济学与统计学教授；贸易部门主管 1947–48；Østerås, Bærum
11  因果推断的先声 — Strotz–Wold 1960 操作化 → 图形模型 → Pearl 的 do-calculus 链条；
    Pearl 评价（引语英文原文，注明出自 Pearl）
12  1989 诺贝尔奖 — 独得；诺奖演讲 1989-12-07 *Econometrics and the Welfare State*
13  荣誉与传承 — Nansen 奖；Econometric Society / IMS Fellow；计量经济学教科书中的缺位之辩（Pearl 猜测）
14  遗产与结尾 — 从概率方法到现代因果推断 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 卒日双值冲突 | infobox 表格作 **26 July 1999**，正文两处（开头括注与 Biography 末段 "He died on 28 July 1999 in Oslo"）作 **28 July 1999**；metadata frontmatter 双值同——**以正文 07-28 为准**，yaml 已取 07-28 |
| 1989 独得 | 1989 年诺奖由 Haavelmo 独得，无共享者；理由含两个并列部分（概率论基础+联立结构），勿拆成两次奖 |
| Frisch 关系定性 | 本篇按 Haavelmo 页面 infobox Influences 建 influence 边（推荐入所、任助手、计算主管）；PhD 1946 由奥斯陆大学授予（论文在哈佛完成）。**注意**：Frisch 篇（batch-01）依 Frisch 页面 infobox Doctoral students 行（明载 Haavelmo）另建 advisor-student 边——两页口径各有本页依据、双向并存，Review 勿删任一，本篇 Beamer 中导师表述用「影响者/上司」措辞 |
| Tinbergen 关系 | 仅 infobox Influences 明载，无具体交往叙述——influence 一条边即可，勿扩写 |
| Pearl 引语 | Pearl 评价须用 page.md 英文原文（"Haavelmo was the first to recognize the capacity of economic models to guide policies" 等），注明出自 Pearl 2014 年文，不可改写为中文"原话" |
| do-calculus 链条 | 演化链 = Haavelmo 思想 → Strotz/Wold 1960 "wiping out" → 图形模型 → do-calculus；Haavelmo 本人**未提出** do-calculus，禁写"发明 do-calculus" |
| 生年 | 1911-12-13，frontmatter 单值无冲突 |
| 机构任期 | 奥斯陆大学经济学与统计学教授 **1948–1979**；贸易部门主管 1947–1948；Aarhus 讲师 1938 一年——年份勿混 |
| metadata 噪声 | metadata occupation 含 mathematician——primary 取 economist；date_of_death 双值见第一条 |
| 诺奖演讲题目 | 1989-12-07 *Econometrics and the Welfare State*（external links 明载），勿与获奖理由混淆 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| econometrics | 经济计量学 | 获奖理由核心词，勿译"经济测量学" |
| probability approach | 概率方法 | 1944 发表的博士论文核心主张 |
| simultaneous economic structures | 联立经济结构 | 获奖理由第二半句 |
| balanced budget multiplier | 均衡预算乘数 | 宏观名片贡献 |
| hypothetical experiments | 假想实验 | 经济模型的 Pearl 式解读 |
| wiping out | 抹去方程 | Strotz–Wold 1960 的操作化 |
| do-calculus | do-演算 | Pearl 提出，非 Haavelmo |
| counterfactuals | 反事实 | 因果推断遗产链概念 |
| Nortraship | 挪威航运战时机构 | 二战纽约统计部任职背景 |
| neo-Keynesian economics | 新凯恩斯主义 | infobox School or tradition |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**The Invisible Light**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：概率方法给经济结构照进"不可见之光"——把杂乱观测背后的联立结构显影；曲名的纪录片深邃感也贴合其贡献长期"缺席于教科书之争"的沉默地位。
- **本地路径**：复制 `music_audio/inspiring-electronic/19-tGxXsgSKPiQ-...The Invisible Light.wav` 到 `economics/presentations/20th_century/Trygve_Haavelmo/TheInvisibleLight.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
