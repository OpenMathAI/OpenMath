# 经济学家立传提示词（Vernon L. Smith）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2002 年得主 Vernon L. Smith（弗农·史密斯）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Vernon_L._Smith/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Vernon Lomax Smith（1927-01-01 生于堪萨斯州威奇托，在世）
- **气质关键词**：**实验室经济学的开创者、市场机制的试飞员、自发秩序的见证者**
- **诺奖获奖理由**（2002 拆分年份，本人那条逐字取自 `economics/nobel_economics_citations.json`；中译对照 `economics/economics_list_data.py` 2002 年 "||" 后段）：
  > "for having established laboratory experiments as a tool in empirical economic analysis, especially in the study of alternative market mechanisms"
  > （表彰他将实验室实验确立为实证经济分析的工具，尤其是对各种市场机制的研究）
- **设计母题**：**实验室里的市场（the market in a lab）**——供需曲线第一次被请进实验室：双向口头拍卖、诱导价值、可重复的市场实验；视觉隐喻用「实验台上的供需坐标/玻璃罩内的微型交易所」。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Vernon_L._Smith/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Vernon_L._Smith/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Vernon_L._Smith_zh`、`VIDEO_NAME=Vernon_L._Smith_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库（yaml 在 `MySQL/data/Vernon_L._Smith.yaml`），无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**V. Smith 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | experimental economics | 实验经济学 | infobox Discipline，诺奖核心 | 核心页 |
| 1 | behavioral economics | 行为经济学 | 诺奖介绍语载其贡献 | 核心页 |
| 2 | mechanism design | 机制设计 | 1982 AER 论文将 Hurwicz 框架引入实验 | 方法页 |
| 3 | combinatorial auction | 组合拍卖 | 1982 与 Rassenti/Bulfin 首创 | 应用页 |
| 4 | neuroeconomics | 神经经济学 | 晚年拓展：脑活动与经济决策 | 晚年页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Wassily Leontief | V. Smith → 学生 | 哈佛博士导师（1955 资本设备更新论文），库内 id=1453 |
| co-honored | Daniel Kahneman | 无向 | 2002 诺贝尔经济学奖同届拆分共享（理由句各一） |
| colleague | Sidney Siegel | 无向 | 1961-62 斯坦福访学结识，同攻实验经济学 |
| colleague | Charles Plott | 无向 | 加州理工同事，鼓励其方法论形式化 |
| colleague | Bart Wilson | 无向 | 查普曼大学同事，共同开展市场实验 |
| collaborator | Stephen J. Rassenti | 无向 | 1982 组合拍卖设计共同提出者 |
| collaborator | Robert L. Bulfin | 无向 | 1982 组合拍卖论文合著者 |
| collaborator | Steven Gjerstad | 无向 | Rethinking Housing Bubbles 2014 合著者 |
| influence | Edward Chamberlin | 无向 | 课堂实验先驱，Smith 改进其制度参数 |
| influence | Leonid Hurwicz | 无向 | 机制设计框架为实验方法提供形式基础 |
| influence | Friedrich Hayek | 无向 | infobox Influences 明载，自发秩序思想 |
| influence | Richard S. Howey | 无向 | infobox Influences 明载（红链人物，仅注一句） |

**不入库但提示词可叙述**：妻子与家庭（page.md 仅 "moved with his family"，无姓名）；Arlington W. Williams/John O. Ledyard（2000 合著一次，合作密度低不入库）；IFREEE/Independent Institute/Cato 等机构任职非人际关系。

## 五、配色方案 【人物专属】

- **气质**：工程师的精确、堪萨斯的质朴、自发秩序的谦逊
- **主色**：`#46356B`（manifest 预分配的暗紫——与 Kahneman 同届统一底色）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeExp` 实验经济学 — 暗紫 `#46356B`
  - `badgeAuction` 拍卖与机制 — 琥珀 `#C07A2A`
  - `badgeOrder` 自发秩序 — 青绿 `#0E7C7B`
  - `badgeNeuro` 神经经济学 — 靛蓝 `#16324F`
- **背景母题**：玻璃罩内的微型供需坐标与散落交易点（实验台上的市场），呼应「把市场请进实验室」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 实验室经济学的开创者 / Vernon L. Smith 1927– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地威奇托、教育 Caltech BS 1949/
    Kansas MA 1952/Harvard PhD 1955、任职 Purdue→Arizona→George Mason→Chapman 2008–、
    诺奖 2002、核心领域）
03  核心贡献概览 — 市场实验 / 诱导价值 / 机制设计检验 / 组合拍卖
04  堪萨斯与农场岁月 (1927–1949) — 大萧条中的保险金农场、Friends University、Caltech 电机工程
05  从工程师到经济学家 (1949–1955) — Kansas MA、哈佛 Leontief 门下博士
06  普渡的第一堂市场实验 (1955–1956)（核心贡献页）— 课堂双向拍卖、 Chamberlin 制度的改进、
    1962 JPE 发表
07  诱导价值与实验方法论 — 1976 AER Induced Value Theory、1982 AER 微观系统作为实验科学
08  与 Siegel 和 Plott 的同行者 — 斯坦福访学结识 Siegel、Caltech 时期 Plott 的推动
09  亚利桑那二十年 (1976–2001) — 获奖研究的主场、McLellan/Regent's 讲席
10  组合拍卖 (1982) — 与 Rassenti/Bulfin：机场时刻表分配机制
11  从 George Mason 到 Chapman (2001–2008) — 经济学与法学教授、Economic Science Institute 创立
12  自发秩序与生态理性 — 构建理性 vs 生态理性（2003 诺奖演讲 Constructivist and Ecological
    Rationality in Economics）、Hayek 思想脉络
13  2002 诺奖时刻 — 与 Kahneman 同届拆分共享、Nobel medal 2009 捐赠 Chapman、
    Vernon Smith Center（UFM）以之为名
14  遗产与结尾 — 实验经济学成为标准工具 + 结尾页（品牌 OpenMathAI）
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由拆分 | 2002 为拆分年份：V. Smith 理由="...established laboratory experiments as a tool..."（实验室实验），与 Kahneman 的心理学洞见理由**各一条**，勿混写同一句 |
| 与 Kahneman 无合作 | 两人工作互不相关（实验经济学 vs 心理学决策），仅同届获奖；co-honored note 必须写「同届拆分共享」，勿写成"共同发展行为经济学" |
| Nobel 介绍语措辞 | page.md 引言句 "for his contributions to behavioral economics and his work in experimental economics" 是维基转述；诺奖理由以 citations.json 为准，两处勿互相覆盖 |
| 国籍口径 | yaml 按 manifest/维基表格口径填 United States，无歧义 |
| Leontief 复用 | 博士导师 Wassily Leontief 用库内 id=1453 记录（勿新建分裂 stub） |
| Chamberlin 的位置 | Chamberlin 是课堂实验先驱（Harvard 教授），Smith 改进的是其实验制度参数（多交易期）——influence 关系，勿写成师生或同事 |
| Asperger 综合征 | 2005 年自述经自我诊断归因于阿斯伯格综合征——按 page.md 客观陈述带"自述/自我诊断"限定，勿写成医学确诊 |
| 政治内容红线 | 2009 反 stimulus 公开信、Cato Institute 请愿、"most active petition-signers" 等政治立场内容一律禁写；机构任职（Cato/Mercatus/Independent）仅作履历事实一句 |
| 名字消歧义 | 规范名 Vernon L. Smith（manifest 形式）；同届对手 Daniel Kahneman；勿与 Robert B. Wilson（2020 拍卖诺奖）或巴拉克·奥巴马时代人物混淆——特别是"Wilson" |
| frontmatter 噪声 | metadata.json date_of_birth 1927-01-01 与正文一致无噪声；educated_at 含两所中学与 UMass Amherst（任教履历非学位），展示时区分 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| experimental economics | 实验经济学 | 诺奖核心领域 |
| induced value theory | 诱导价值理论 | 1976 AER，实验方法的原理性表述 |
| double auction | 双向拍卖 | 课堂与实验室的市场机制原型 |
| combinatorial auction | 组合拍卖 | 1982 与 Rassenti/Bulfin 首创 |
| mechanism design | 机制设计 | Hurwicz 框架，实验检验机制的形式基础 |
| constructivist vs ecological rationality | 构建理性与生态理性 | 2003 诺奖演讲核心对偶 |
| spontaneous order | 自发秩序 | Hayek 脉络，Smith 的哲学底色 |
| market mechanisms | 市场机制 | 获奖理由关键词 |
| neuroeconomics | 神经经济学 | 晚年拓展领域 |
| Economic Science Institute | 经济科学研究所 | 2008 于 Chapman 创立 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Expedition**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：「远征」贴合实验经济学的开拓本质——把经济学从黑板带进实验室，是一场方法论的远征；曲名的探索感也匹配其 60 余年从 Purdue 课堂实验到神经经济学的持续前行（与 Kahneman 同届同曲，属批次内撞曲，出片阶段由主控统一协调）。
- **本地路径**：复制 `music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav` 到 `economics/presentations/21th_century/Vernon_L._Smith/Expedition.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
