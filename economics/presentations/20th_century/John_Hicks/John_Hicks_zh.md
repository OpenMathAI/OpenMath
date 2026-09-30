# 经济学家立传提示词（John Hicks）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1972 年得主 John Hicks（约翰·希克斯）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/John_Hicks/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Sir John Richard Hicks（1904-04-08 生于英格兰沃里克 ~ 1989-05-20 逝于英格兰 Blockley，享年 85 岁）
- **气质关键词**：**IS-LM 模型的构建者、《价值与资本》的作者、一般均衡与福利理论的开路人**
- **诺奖获奖理由**（1972 与 Kenneth Arrow 共享，逐字引用 manifest）：
  > "for their pioneering contributions to general economic equilibrium theory and welfare theory"（表彰他们在一般经济均衡理论与福利理论方面的开创性贡献）
- **设计母题**：**两条曲线的交点（the crossing of two curves）**——IS 与 LM 两条曲线的交点同时定住利率与产出；视觉上以「交叉曲线 + 均衡点」的意象构成背景母题，延伸至替代效应与收入效应的分解图。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/John_Hicks/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/John_Hicks/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=John_Hicks_zh`、`VIDEO_NAME=John_Hicks_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Hicks 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | general equilibrium theory | 一般均衡理论 | Value and Capital 向英语世界引入并精炼动态化 | 封面、核心页 |
| 1 | welfare economics | 福利经济学 | Kaldor–Hicks 效率标准；社会核算应用 | 核心页 |
| 2 | consumer theory | 消费者理论 | 替代效应/收入效应区分；Hicksian 需求函数 | 微观页 |
| 3 | macroeconomics | 宏观经济学 | IS–LM 模型（1937），凯恩斯理论的经典解释 | 宏观页 |
| 4 | capital theory | 资本理论 | Value and Capital 与 Capital and Growth | 资本页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Kenneth Arrow | 无向 | 1972 诺贝尔经济学奖共享（一般经济均衡理论与福利理论的开创性贡献） |
| spouse | Ursula Webb | 无向 | LSE 同事，1935 年成婚（Lady Ursula Hicks） |
| influence | Léon Walras | 单向 | infobox Influences 明载 |
| influence | Vilfredo Pareto | 单向 | infobox Influences 明载 |
| influence | Lionel Robbins | 单向 | 正文明载 influences included（LSE 时期） |
| influence | Erik Lindahl | 单向 | infobox Influences 明载 |
| influence | John Maynard Keynes | 单向 | infobox Influences 明载 |
| colleague | Friedrich Hayek | 无向 | LSE 时期的交往同事（正文 associates 明载） |
| colleague | R. G. D. Allen | 无向 | 1934 两篇价值理论开山论文的合作者 |
| colleague | Nicholas Kaldor | 无向 | LSE 时期同事；Kaldor–Hicks 效率标准双方命名 |
| colleague | Abba Lerner | 无向 | LSE 时期同事 |
| advisor-student | Harald Malmgren | Hicks→学生 | infobox Doctoral students 明载 |
| advisor-student | Lorie Tarshis | Hicks→学生 | infobox Notable students 明载 |
| advisor-student | Robert W. Clower | Hicks→学生 | infobox Notable students 明载 |

**不入库但提示词可叙述**：Hicks–Hansen IS–LM 模型的 Hansen 命名（Alvin Hansen 是模型传播推广者，page.md 仅载模型双名，无两人合作记载，不建边）；父亲 Edward Hicks（沃里克报业主笔兼合伙人，仅具名）；捐赠诺奖奖金给 LSE 图书馆募捐（事件非关系）；Hayek 同时出现在 infobox Influences——按正文 associates 取 colleague 类型。

## 五、配色方案 【人物专属】

- **气质**：牛津的克制均衡、数理与人文的双重修养
- **主色**：`#123C5B`（牛津深蓝——Clifton 数学奖学金少年的冷静与一般均衡的秩序感）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeGE` 一般均衡 — 深蓝 `#123C5B`
  - `badgeWelf` 福利理论 — 青绿 `#146B5A`
  - `badgeISLM` IS–LM 宏观 — 琥珀 `#C07A2A`
  - `badgeValue` 价值与资本 — 深红 `#7E1E23`
- **背景母题**：交叉曲线与均衡点——IS/LM 之交、替代/收入效应之分解，一切归于"两条线的交点"。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — IS-LM 的缔造者 / Sir John Hicks 1904–1989 + 四色 badge + 右上头像 + 国籍行（United Kingdom）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、教育 Clifton/Balliol 数学奖学金→PPE 二等学位、
    LSE→剑桥冈维尔与凯斯学院→曼彻斯特→Nuffield/All Souls 任职线、诺奖 1972、核心领域）
03  核心贡献概览 — IS-LM / 价值与资本 / 消费者理论 / Kaldor-Hicks 效率
04  沃里克少年与牛津转轨 (1904–1926) — 数学专长转 PPE；毕业自评"没有任何学科的合格资格"
05  LSE 劳动经济学家 (1926–1935) — 从劳资描述转向分析；Robbins 与一群 associates
06  1934 与 Allen：价值理论双论（核心贡献页）— 序数效用；替代效应/收入效应的标准化区分
07  1937 IS-LM：给凯恩斯一个框架（核心贡献页）— 《Mr. Keynes and the "Classics"》；Hicks-Hansen 之名
08  IS-LM 的自我否定 (1980) — 晚年自斥为"教室玩具"（a classroom gadget）
09  1939 Value and Capital — 一般均衡进入英语世界；动态精炼；稳定性条件首次严格陈述
10  Kaldor-Hicks 效率与福利经济学 — 补偿标准；曼彻斯特时期的社会核算应用
11  收入的三种度量 — Hicks 收入定义与会计学基础
12  1972 共享诺奖 — 与 Arrow 同享；1973 捐奖金予 LSE 图书馆募捐
13  荣誉与晚年 — 1964 爵士；All Souls 研究员（1965-1971）退休后笔耕不辍；1989 绝笔 A Market Theory of Money
14  遗产与结尾 — Hicksian 需求函数/Hicks 中性技术进步/希克斯最优 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 共享奖对手方 | 1972 与 **Kenneth Arrow** 共享（理由用"他们"）；Arrow 用库内记录 id=2639 name_en 'Kenneth Arrow'（勿写 Kenneth J. Arrow 造成分裂） |
| IS-LM 的归属 | 模型出自 1937 论文《Mr. Keynes and the "Classics"; a suggested interpretation》；"Hicks–Hansen IS–LM"是双名——Hansen 的推广工作 page.md **无载**，勿编造 Hansen 修改模型的细节，只写模型双名事实 |
| IS-LM 自我评价 | 1980 年论文自斥为 "a classroom gadget"——引语 page.md 明载可逐字引用；展示"作者本人摇摆"的诚实叙事 |
| 毕业荣誉 | 牛津 PPE 二等学位，且自述"在所学科目中没有任何合格资格"——反差细节 page.md 明载，勿美化 |
| 无博士导师 | Hicks 教育背景无 doctoral advisor（Clifton→Balliol）；正文 influences 不等于师承——Robbins 用 influence、Hayek/Allen/Kaldor/Lerner 用 colleague，类型勿混 |
| Ursula Webb 双重身份 | 先是 LSE 同事（associates 名单中），1935 成妻——取 spouse 单一类型，note 注明 LSE 同事出身 |
| Kaldor-Hicks 命名 | 1939 同年 Hicks 提出"补偿准则"，与 Kaldor 并名——是各自独立提出的标准并名，非两人合著（page.md 无合著记载，禁写共同论文） |
| 收入定义 | 三种收入度量引语出自 Hicks 1946 (Value and Capital 2nd ed.) 页码 p.173/174——引语逐字带出处 |
| 任职节点 | LSE 1926-35 讲师；剑桥 1935-38（冈维尔与凯斯学院 fellow）；曼彻斯特教授 1938-46；牛津 Nuffield 1946-52、Drummond 教授 1952-65、All Souls 1965-71——勿混淆年序 |
| 爵士年份 | 1964 受封 Knight Bachelor（infobox 明载），勿与诺奖 1972 混写 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| IS–LM model | IS-LM 模型 | 1937；投资储蓄-流动性偏好货币供给曲线 |
| Hicksian demand function | 希克斯需求函数 | 补偿需求函数的别名 |
| substitution / income effect | 替代效应/收入效应 | 1934 与 Allen 的标准化区分 |
| Kaldor–Hicks efficiency | 卡尔多-希克斯效率 | 潜在帕累托改进的补偿标准 |
| Value and Capital | 《价值与资本》 | 1939 magnum opus，2nd ed. 1946 |
| ordinal utility | 序数效用 | 无差异分析的基础 |
| comparative statics | 比较静态学 | Value and Capital 中被形式化 |
| general equilibrium | 一般均衡 | 向英语读者引入并动态化 |
| Hicks-neutral technical change | 希克斯中性技术进步 | 技术变化分类命名 |
| compensation criterion | 补偿准则 | 福利比较判据，1939 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Nostalgia**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**："怀旧"对应 Hicks 晚年对自身框架的回望与否定——IS-LM 的缔造者亲手称之为"教室玩具"，1989 年还在写《货币的市场理论》；曲目的回望气质贴合这位终生活在自我修订中的均衡大师。
- **本地路径**：复制 `music_audio/alex-productions/86-5ETNuoDcBg4-Nostalgia.wav` 到 `economics/presentations/20th_century/John_Hicks/Nostalgia.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
- **撞曲说明**：Nostalgia 同时预分配给 1972 Arrow（batch-02）；共享年两人同曲合理，如需去重由主控统一裁定。
