# 经济学家立传提示词（Michael Spence）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2001 年得主 Michael Spence（迈克尔·斯宾塞）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Michael_Spence/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Andrew Michael Spence（1943-11-07 生于新泽西州蒙特克莱尔，在世）
- **气质关键词**：**信号传递之父、教育筛选模型的开创者、从学院到商学院的管理者**
- **诺奖获奖理由**（三人共享，逐字取自 manifest）：
  > "for their analyses of markets with information asymmetry"（表彰他们对信息不对称市场的分析）
- **设计母题**：**信号与成本（costly signals）**——Spence 的核心洞见是「有成本的信号才可信」：高能力者以更低成本取得教育信号；视觉隐喻用「灯塔与旗语/双通道光束」：同一光源向两端发出强度不同的信号，接收端按强度分辨。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Michael_Spence/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Michael_Spence/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Michael_Spence_zh`、`VIDEO_NAME=Michael_Spence_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库（yaml 在 `MySQL/data/Michael_Spence.yaml`），无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Spence 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | microeconomics | 微观经济学 | infobox Discipline 首项 | 封面、核心页 |
| 1 | information economics | 信息经济学 | 信号传递模型，诺奖核心 | 核心页 |
| 2 | signaling (economics) | 信号传递 | 教育作为可信信号，Notable ideas | 核心页 |
| 3 | labor economics | 劳动经济学 | 就业市场信号模型的应用场域 | 应用页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Kenneth Arrow | Spence → 学生 | 哈佛博士导师（1972，Market Signalling），库内 id=2639 |
| advisor-student | Thomas Schelling | Spence → 学生 | 哈佛博士导师（联合指导） |
| co-honored | George Akerlof | 无向 | 2001 诺贝尔经济学奖三人共享 |
| co-honored | Joseph Stiglitz | 无向 | 2001 诺贝尔经济学奖三人共享 |
| influence | Richard Zeckhauser | 无向 | infobox Influences 明载 |

**不入库但提示词可叙述**：妻子与子女（page.md 仅 "lives in Milan with his wife and children"，无姓名）；Bill Gates 与 Steve Ballmer（哈佛课上学生轶事，非学术关系）；Danforth Graduate Fellowship 资助方。

## 五、配色方案 【人物专属】

- **气质**：信号的清晰与克制、跨大西洋的学院气质、管理学者的干练
- **主色**：`#372A75`（manifest 预分配的深紫罗兰——与同届三人组统一底色）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeSignal` 信号传递 — 深紫 `#372A75`
  - `badgeMicro` 微观经济学 — 靛蓝 `#16324F`
  - `badgeInfo` 信息经济学 — 青绿 `#0E7C7B`
  - `badgeGrowth` 增长与发展 — 琥珀 `#C07A2A`
- **背景母题**：双通道光束与同心扩散弧（强信号穿透雾层、弱信号被吸收），呼应「信号成本分离类型」的核心模型。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 信号传递之父 / Michael Spence 1943– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地蒙特克莱尔、教育 Princeton 1966/
    Oxford Rhodes Scholar 1968/Harvard PhD 1972、任职 Stanford GSB 院长→NYU Stern 2010–、
    诺奖 2001、核心领域）
03  核心贡献概览 — 信号传递 / 教育筛选 / 增长委员会 / 管理实践
04  多伦多到普林斯顿 (1943–1966) — UTS 中学、Princeton 哲学本科 summa cum laude 1966
05  牛津罗德学者 (1966–1968) — Magdalen College 数学 BA/MA
06  哈佛博士：Arrow 与 Schelling 双导师 (1968–1972) — Market Signalling、Wells 奖
07  信号传递：有成本的信号才可信（核心贡献页）— Job Market Signaling 1973 QJE、
    教育作为分离装置、与 Akerlof/Stiglitz 的拼图关系
08  Clark 奖与学界承认 (1976–1981) — Econometric Society Fellow 1976、Clark Medal 1981、
    AAAS 1983
09  斯坦福商学院院长 (1990–1999) — Knight 讲席教授、1999 卸任转投 Oak Hill
10  从学院到市场 — Oak Hill Capital Partners、哈佛课上 Gates/Ballmer 轶事（一句带过）
11  增长与发展委员会 (2008) — Commission on Growth and Development 主席、
    The Next Convergence 2011
12  纽约岁月 (2010–) — NYU Stern Berkley 讲席、SDA Bocconi 2011、Hoover 高级研究员
13  2001 三人组 — 与 Akerlof/Stiglitz 各答信息不对称一环（逆向选择/信号/筛选）
14  遗产与结尾 — 信号模型进入契约理论 + 结尾页（品牌 OpenMathAI）
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | manifest/官方句 "for their analyses of markets with information asymmetry"；展示勿混入 Stiglitz 篇的引申句 |
| 三人分工 | Spence=信号传递（有信息方主动发信号）、Akerlof=逆向选择、Stiglitz=筛选；Spence 模型里是「雇员向雇主」发信号，方向勿写反 |
| 国籍口径 | yaml 按 manifest/维基表格口径填 United States；page.md 正文首句称 "Canadian-American economist"（多伦多中学+Rotman 任职背景），国籍展示仍以 United States 为准，§一可注一句背景 |
| 姓名全称 | 本人全名 Andrew Michael Spence，但学籍与 manifest 规范名用 Michael Spence；Stiglitz page.md 引用处作 "A. Michael Spence"，引用时保持原样 |
| 博士导师双列 | Kenneth Arrow + Thomas C. Schelling 联合指导 1972 论文，两行入库；Schelling 名用 manifest 形式 Thomas Schelling |
| Rhodes Scholarship | 是牛津 Magdalen College 的奖学金，勿写成"牛津大学本科"泛称；学位为数学 BA/MA 1968 |
| 妻子无名禁编 | Personal life 仅 "with his wife and children"，无姓名无子女数，禁写任何具体信息 |
| Gates/Ballmer 轶事 | 1999 Fortune 访谈：两人自认翘课、考前四天突击通过——可作一句趣味注，但须注明出自 Fortune 访谈转述 |
| 职业混淆 | Clark Medal 1981（美国经济学会）勿与诺奖 2001 混年；院长卸任 1999、入职 NYU 是 2010-09-01，勿写"2001 后即赴 NYU" |
| frontmatter 噪声 | metadata.json educated_at 含 University of Toronto Schools（中学），展示教育履历时区分中学/本科/研究生 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| signaling | 信号传递 | Spence 诺奖核心，与 screening（筛选，Stiglitz）方向相反 |
| costly signal | 有成本的信号 | 信号可信的条件：高能力者成本更低 |
| job-market signaling | 就业市场信号 | 1973 QJE 论文 Job Market Signaling |
| Market Signaling | 市场信号 | 1972 博士论文及 1974 专著标题 |
| information asymmetry | 信息不对称 | 获奖理由核心词 |
| screening | 筛选 | 雇主侧机制，勿与 signaling 混用 |
| contract theory | 契约理论 | 信号模型启发的分支 |
| Commission on Growth and Development | 增长与发展委员会 | 2008 起任主席 |
| The Next Convergence | 《下一轮趋同》 | 2011 著作 |
| Rhodes Scholarship | 罗德奖学金 | 牛津 Magdalen College |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**SEA**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：灯塔与雾笛是海上信号的原型——「用光与声在看不见的距离上传信」恰好对应信号传递模型；曲名的辽阔感也匹配其跨大西洋（多伦多/牛津/普林斯顿/斯坦福/米兰/纽约）的生涯轨迹（2001 三人共享奖同曲，属批次内撞曲，出片阶段由主控统一协调）。
- **本地路径**：复制 `music_audio/alex-productions/92-WEqfdRXU3IU-SEA.wav` 到 `economics/presentations/21th_century/Michael_Spence/SEA.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
