# 经济学家立传提示词（James A. Robinson）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2024 年得主 James A. Robinson（詹姆斯·罗宾逊）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/James_A._Robinson/page.md`，与其冲突时以 page.md 为准（metadata.json 仅作结构化参考）。

## 一、背景信息 【人物专属】

- **目标经济学家**：James Alan Robinson（1960-02-27 生于英格兰切姆斯福德，英国/美国双重公民，**在世**，卒年留白）
- **气质关键词**：**殖民地田野的行走者、制度持续性的史家、政治学家出身的经济诺奖得主** —— 2024 年诺贝尔经济学奖获奖理由（与 Daron Acemoglu、Simon Johnson 共享，逐字引自 `economics/nobel_economics_citations.json` 2024 年 James A. Robinson 条目）：
  > "for studies of how institutions are formed and affect prosperity"（表彰他们关于制度如何形成并影响繁荣的研究）
- **设计母题**：**田野地图与制度地层（fieldwork map & institutional strata）**——Robinson 的研究足迹遍布博茨瓦纳、智利、刚果（金）、海地、菲律宾、塞拉利昂、南非、哥伦比亚；他看繁荣差异像看地质剖面：殖民时代沉积的制度层至今决定地表收成。视觉隐喻：一幅手绘风世界地图上散布田野调查标记点，地层剖面从地图剖面展开，标注「1750s—今日」的制度延续。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/James_A._Robinson/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/James_A._Robinson/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=James_A._Robinson_zh`、`VIDEO_NAME=James_A._Robinson_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Robinson 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | political economy | 政治经济学 | 正文 Career 节明载的主领域首位 | 封面、核心页 |
| 1 | comparative politics | 比较政治学 | 正文 Career 节明载（政治科学家身份） | 核心页 |
| 2 | development economics | 发展经济学 | 经济与政治发展研究；Pearson 全球冲突研究所 | 应用页 |
| 3 | economic history | 经济史 | 殖民地起源与长期制度延续研究 | 核心页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致，共 5 条）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Truman Bewley | 师→生（博士导师） | Yale 博士导师（1993），论文隐性劳动契约的动态执行 |
| co-honored | Daron Acemoglu | 无向 | 2024 诺贝尔经济学奖三人共享（制度如何形成并影响繁荣） |
| co-honored | Simon Johnson | 无向 | 2024 诺贝尔经济学奖三人共享（制度如何形成并影响繁荣） |
| collaborator | Daron Acemoglu | 无向 | LSE 结识后长期合著三书（2006/2012/2019） |
| collaborator | Simon Johnson | 无向 | 2001 合著殖民地起源论文（迄今被引最高） |

**不入库但提示词可叙述**：合编文集的编辑群（Akyeampong/Bates/Nunn、Diamond、Amsden 等——仅出版物列表合编者，防噪声不入）；Pierre Yared（Income and Democracy 等论文合著者，仅书目列表出现，不入）；乌兹别克斯坦塔什干交流（一次性事件，客观一句）； 全球田野调查各国（叙事素材非关系）。

## 五、配色方案 【人物专属】

- **气质**：田野感、历史纵深、冷静的全球视野
- **主色**：`#14324F`（manifest 预分配藏蓝——与 Acemoglu 篇同色，2024 三人组统一色系）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeField` 全球田野 — 青绿 `#175E54`
  - `badgeInst` 制度与繁荣 — 藏蓝 `#14324F`
  - `badgeBook` 制度三部曲 — 琥珀 `#C07A2A`
  - `badgeNobel` 诺奖荣誉 — 金 `#C9A227`
- **背景母题**：田野地图标记点 + 制度地层剖面，呼应「制度沉积决定今日繁荣」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 殖民地田野的行走者 / James A. Robinson 1960– + 四色 badge + 右上头像 + 国籍行（United Kingdom / United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地切姆斯福德、教育 LSE BSc 1982 /
    Warwick MA 1986 / Yale PhD 1993、任职 UChicago Harris、诺奖 2024、核心领域）
03  核心贡献概览 — 殖民地起源 / 制度三部曲 / 现代化理论批判 / 全球田野
04  英格兰青年 (1960–1982) — 切姆斯福德出身、LSE 本科
05  Warwick 与 Yale (1986–1993) — Truman Bewley 门下，隐性劳动契约论文
06  哈佛岁月 (2004–2015) — Government 系副教授→David Florence/Cowett 讲席教授
07  芝加哥与 Pearson 研究所 (2015–) — 九位 University Professor 之一；全球冲突研究
08  殖民地起源（核心贡献页）— 2001 三人合著：制度差异解释前殖民地约四分之三人均收入差
09  制度三部曲 — Economic Origins（2006）/ Why Nations Fail（2012）/ The Narrow Corridor（2019）
10  现代化理论批判 — Income and Democracy（2008）：收入与民主无因果；Non-Modernization（2022）
11  全球田野地图 — 博茨瓦纳/智利/刚果（金）/海地/菲律宾/塞拉利昂/南非/哥伦比亚（每年夏赴波哥大执教）
12  2024 诺贝尔经济学奖 — 三人共享；政治学家出身的经济诺奖得主
13  学术谱系与方法 — 与 Acemoglu 的 LSE 相遇、长期 productive relationship
14  遗产与结尾 — 比较发展研究的制度转向 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由表述 | 2024 三人共享**同一句** "for studies of how institutions are formed and affect prosperity"；勿拆分改写；中译统一「表彰他们关于制度如何形成并影响繁荣的研究」 |
| 身份双轨 | 政治科学家 + 经济学家（description 与 infobox 双载）；fields 政治学与经济学并置，勿只写经济一侧；诺奖是经济学奖、本人是 UChicago Harris 公共政策学院教授，三条线勿混 |
| 国籍口径 | infobox Citizenship United Kingdom + American；yaml 双国籍；「英裔美国人 British-American」可写 |
| 学位序列 | LSE BSc 1982 → Warwick MA 1986 → Yale PhD 1993（注意博士在 Yale 而非 LSE）；博士导师 Truman Bewley 仅 infobox 明载 |
| 合著边界 | 与 Acemoglu 是 co-honored + collaborator 双边；Johnson 是 co-honored + collaborator 双边；仅书目列表出现的合编者/Yared 不入库（防噪声） |
| 书名与年份 | Economic Origins of Dictatorship and Democracy 2006 / Why Nations Fail 2012 / The Narrow Corridor 2019，勿串年；书名致敬 Barrington Moore Jr. 1966 一事归 Acemoglu 篇 influence 注记，Robinson 篇可一句带过 |
| 乌兹别克斯坦 | 2023 塔什干行程与《国家的失败》「棉花之王」章节问答，客观一句即可，不涉政治评价 |
| 为什么国家的失败 | 书中 Soviet Russia 例证、英国 1689 例证可写；Bill Gates/Jeffrey Sachs 书评争议属书评非本人观点，Robinson 篇不展开（如需引用以 page.md 为准） |
| 在世口径 | 1960 年生、在世，卒年留白，三处口径一致 |
| 蒙古名誉博士 | 2016-05-09 蒙古国立大学名誉博士（首次访蒙），可作荣誉页条目 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| extractive institutions | 汲取型制度 | 三人组共享核心词 |
| inclusive institutions | 包容型制度 | 获奖研究核心词 |
| institutional persistence | 制度持续性 | 殖民地起源论文的因果链 |
| comparative politics | 比较政治学 | Robinson 的政治学主领域 |
| University Professor | 校级教授 | 芝加哥大学最高教席之一（九人） |
| Pearson Institute | Pearson 全球冲突研究所 | Robinson 曾主持 |
| critical juncture | 关键节点 | 制度分岔时刻 |
| Why Nations Fail | 国家的失败 | 2012 合著书名，勿误译 |
| The Narrow Corridor | 窄廊 | 2019 合著书名 |
| Harris School | Harris 公共政策学院 | 现职所在院系 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Timeless**（manifest 预分配，`music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav`；2024 三人组同曲，出片阶段若撞曲需主控协调可换备选）
- **匹配理由**：与 Acemoglu 篇同曲——制度研究的长时段气质一致；Robinson 侧的田野行走与地质剖面隐喻同样需要「超越单代人的时间感」。
- **备选**：★ **The Flow of Time**（时间感更直白）；★ **Pathfinder**（田野开拓感）。
- **本地路径**：复制 wav 到 `economics/presentations/21th_century/James_A._Robinson/Timeless.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 十、执行清单 【模板通用】

1. 读本提示词 + `Kenneth_G_Wilson_zh.tex` 骨架，建目录 `economics/presentations/21th_century/James_A._Robinson/`；
2. 从 images.txt / Commons 下载肖像（250px→500px），404 则装饰圆占位；
3. 复制 Makefile 设 `MAIN=James_A._Robinson_zh`、`VIDEO_NAME=James_A._Robinson_zh`；
4. 写 tex（配色按第五节、Slide 序列按第六节），每写一页 `make` 查溢出（0 error、vbox≤10pt、hbox≤50pt）；
5. `make pdf` → `pdftoppm` 逐页目检 → `make images` → `make video` 出 mp4；
6. 全程遵守第七节陷阱表；引语仅限 page.md 载有英文原文者（引原文+译文），无原文不得造「原话」；政治内容零评价。
