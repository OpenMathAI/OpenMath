# 经济学家立传提示词（Edward C. Prescott）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2004 年得主 Edward C. Prescott（爱德华·普雷斯科特）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Edward_C._Prescott/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Edward Christian Prescott（1940-12-26 生于纽约州格伦斯福尔斯 ~ 2022-11-06 逝于亚利桑那州天堂谷，享年 81 岁）
- **气质关键词**：**真实经济周期的旗手、时间一致性的揭示者、宏观经济的微观基础工程师**
- **诺奖获奖理由**（2004 为共享理由年份，全句逐字引用，manifest `citation_en`/`citation_zh` 已给出）：
  > "for their contributions to dynamic macroeconomics: the time consistency of economic policy and the driving forces behind business cycles"（表彰他们对动态宏观经济学的贡献：经济政策的时间一致性与经济周期背后的驱动力量）
- **设计母题**：**时间与冲击（time & shock）**——一只沙漏旁伸出一道脉冲响应曲线：政策规则随时间可信，技术冲击在周期中扩散，是「规则胜于相机抉择、波动源于真实力量」的视觉隐喻，构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Edward_C._Prescott/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Edward_C._Prescott/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Edward_C._Prescott_zh`、`VIDEO_NAME=Edward_C._Prescott_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至十二节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Prescott 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | macroeconomics | 宏观经济学 | infobox 所属学派新古典宏观；诺奖核心 | 封面、核心页 |
| 1 | business cycles | 经济周期 | RBC 理论：技术冲击驱动 | 核心页 |
| 2 | general equilibrium | 一般均衡 | 递归竞争均衡与宏观建模方式 | 方法页 |
| 3 | macroeconomic policy | 宏观经济政策 | 时间一致性：规则 vs 相机抉择 | 核心页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Michael C. Lovell | 师→生（博士导师） | 卡内基梅隆博士导师（1967），论文适应性决策规则 |
| influence | Morris H. DeGroot | 无向 | infobox Influences 明载（frontmatter 亦列其博士导师，infobox 只载 Lovell，按 influence 入） |
| influence | Robert Lucas Jr. | 无向 | infobox Influences 明载；1971《Investment Under Uncertainty》合著 |
| influence | John Muth | 无向 | infobox Influences 明载（复用库内 id=1405 stub） |
| co-honored | Finn E. Kydland | 无向 | 2004 诺贝尔经济学奖共享（动态宏观经济学：时间一致性与经济周期驱动力量） |
| colleague | Finn E. Kydland | 无向 | 卡内基梅隆 GSIA 同事，1977 与 1982 两篇论文合著 |
| advisor-student | Finn E. Kydland | Prescott → 学生 | 博士生（infobox 明载；对方页面正文明载受其指导） |
| advisor-student | Costas Azariadis | Prescott → 学生 | infobox Doctoral students 明载 |
| advisor-student | Gary Hansen | Prescott → 学生 | infobox Doctoral students 明载 |
| advisor-student | V. V. Chari | Prescott → 学生 | infobox Doctoral students 明载 |
| advisor-student | Fernando Alvarez | Prescott → 学生 | infobox Doctoral students 明载 |
| advisor-student | Richard Rogerson | Prescott → 学生 | infobox Doctoral students 明载 |
| parent-child | William Clyde Prescott | 父 → 子 | 父（正文 Biography 明载全名） |
| parent-child | Mathilde Helwig Prescott | 父 → 子 | 母（正文 Biography 明载全名） |

**不入库但提示词可叙述**：配偶（page.md 全篇无载，禁写婚姻）；Rajnish Mehra（1985 股权溢价论文合著者，仅出版物列表）；Timothy Kehoe（合编者）；Barack Obama 与 Cato Institute 公开信（一次性行文，客观一句即可）；Delta Upsilon 兄弟会、福特基金会讲席等职务性信息。

## 五、配色方案 【人物专属】

- **气质**：克制、规则感、长周期的时间纵深
- **主色**：`#2A3468`（规则蓝——政策规则的冷静与纵深；manifest 预分配，与同届共享得主 Kydland 同色，同批撞色为 manifest 口径）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeTC` 时间一致性 — 规则蓝 `#2A3468`
  - `badgeRBC` 真实经济周期 — 普鲁士蓝 `#1E4E79`
  - `badgeHP` HP 滤波 — 琥珀 `#C07A2A`
  - `badgeEP` 股权溢价之谜 — 铁锈红 `#A63A2B`
- **背景母题**：沙漏与一道金色脉冲响应曲线：沙漏象征时间一致性，脉冲象征技术冲击在周期中的扩散。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 真实经济周期的旗手 / Edward C. Prescott 1940–2022 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生地格伦斯福尔斯、Swarthmore 数学学士 1962、
    Case Western 运筹学硕士 1963、卡内基梅隆经济博士 1967、Minnesota/ASU、诺奖 2004、核心领域）
03  核心贡献概览 — 时间一致性 / 真实经济周期 / HP 滤波 / 股权溢价之谜
04  格伦斯福尔斯与数学少年 (1940–1962) — 父母、Swarthmore 数学学士、Delta Upsilon
05  从运筹学到经济学 (1962–1967) — Case Western 硕士、卡内基梅隆博士、Lovell 门下、Henderson 奖
06  执教版图 (1966–2003) — 宾大 → 卡内基梅隆 → 明尼苏达；芝加哥/西北访问
07  时间一致性：规则为何被背弃（核心贡献页）— 1977 与 Kydland 合著、洪水平原例、可信性
08  真实经济周期 (1982)（核心贡献页）— Time to Build、技术冲击解释约 70% 产出波动、微观基础
09  明尼苏达与美联储 (1980–2003) — 明尼阿波利斯联储顾问（1981 起）、宏观前沿阵地
10  HP 滤波与股权溢价之谜 — Hodrick–Prescott 滤波、Mehra–Prescott 1985
11  ASU 与晚年 (2003–2022) — W. P. Carey 商学院、UCSB 讲席 2004、NYU 2006、ANU 2014
12  2004 诺贝尔经济学奖 — 与 Kydland 共享（同句理由）；核心研究完成于卡内基梅隆 GSIA 时期
13  荣誉与认可 — NAS 2008、Nemmers 2002、AAAS 会士 1992、计量学会会士 1980、Henderson 奖 1967
14  遗产与结尾 — DSGE/RBC 范式与宏观经济学微观基础 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 共享理由口径 | 2004 为共享理由年份（非拆分），manifest 全句用 "their"；两人同句理由，co-honored note 与 Kydland 篇文案一致 |
| 双博士导师噪声 | frontmatter `doctoral_advisor` 载 Lovell+DeGroot 两人，但 infobox Doctoral advisor 只载 Lovell、DeGroot 列于 Influences；入库裁定 advisor=Lovell、influence=DeGroot，禁写双导师 |
| Lucas 关系 | influence（infobox Influences 明载）而非导师；1971 合著《Investment Under Uncertainty》载于出版物列表，note 可提，勿写成师承 |
| Kydland 三行并存 | co-honored（2004 共享）+ colleague（GSIA 同事+两篇合著）+ advisor-student（infobox 博士生，对方页面正文明载）三行并存，note 各表其意 |
| 六位博士生 | infobox Doctoral students 六人全部入库（含 Kydland）；metadata 无更宽名单，防噪声不外扩 |
| 引用排名双口径 | 正文两处："19th most widely cited economist in the world **in 2013**" 与 "as of **August 2012**"；幻灯片取一处并注另一处，勿混写 |
| 政治内容红线 | 2009 年 250+ 经济学家联署公开信反对《美国复苏与再投资法》（Cato Institute 赞助、NYT/Arizona Republic 刊广告）：**客观一句**即可，禁评价、禁展开政策立场 |
| 妻子无载 | page.md 全篇无配偶信息，禁写婚姻；父母 William Clyde Prescott / Mathilde Helwig Prescott 具名入库 parent-child |
| 死因口径 | 2022-11-06 癌症病逝于天堂谷，享年 81，客观陈述 |
| 诺奖演讲 | 2004-12-08 *The Transformation of Macroeconomic Policy and Research*，与获奖理由分开，勿混写 |
| 机构年代 | Penn 1966–1971 → CMU 至 1980 → Minnesota 1980–2003 → ASU 2003 起；芝加哥访问 1978、西北 1979–1982；Minneapolis 联储顾问 1981 起；勿互换 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| time consistency | 时间一致性 | 获奖理由核心词，勿译「时间连贯性」 |
| dynamic inconsistency | 动态不一致 | 同一现象的另一称呼 |
| rules rather than discretion | 规则胜于相机抉择 | 1977 论文标题核心对举 |
| real business cycle (RBC) | 真实经济周期 | 1982 论文开创的范式 |
| technology shock | 技术冲击 | RBC 的波动来源 |
| Hodrick–Prescott filter | HP 滤波 | 时间序列平滑工具 |
| equity premium puzzle | 股权溢价之谜 | 1985 与 Mehra 合著 |
| microfoundations | 微观基础 | page.md 明载「主要贡献」表述 |
| recursive competitive equilibrium | 递归竞争均衡 | 1980 与 Mehra 合著论文 |
| social objective function | 社会目标函数 | 1977 论文论证中的概念 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Daylight**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：RBC 把周期归于「日光下的真实力量」——技术、生产率与劳动供给，而非货币幻影；「日光」的明亮感贴合新古典学派清晰冷峻的均衡世界观，也呼应从规则中解放政策信用的主旨。
- **本地路径**：复制 `music_audio/alex-productions/44-JoyIRE5k2Yo-Daylight.wav` 到 `economics/presentations/21th_century/Edward_C._Prescott/Daylight.wav`
- **撞曲注记**：同届共享得主 Finn E. Kydland 同曲（manifest 同批预分配）；若出片阶段需去重，由主控统一裁定。
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 十、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `economics/presentations/pages/21th_century/Edward_C._Prescott/page.md` | 事实基准（唯一事实来源） |
| `economics/presentations/pages/21th_century/Edward_C._Prescott/metadata.json` | 结构化参考（冲突以 page.md 为准） |
| `economics/presentations/pages/21th_century/Edward_C._Prescott/images.txt` | 肖像候选 URL |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `economics/presentations/cover/` | OpenEcon 统一封面 |
| `economics/prompt_manifest_21th.json` | 批次条目（citation_en/zh、BGM、主色） |

## 十一、执行清单 【模板通用】

1. 通读本提示词与 page.md，建立事实卡（生卒/学位/机构/奖项/关系五组）。
2. 下载肖像（images.txt 或 Commons `Special:FilePath`，500px；404 则装饰圆占位）。
3. 复制 Makefile，设 `MAIN=Edward_C._Prescott_zh`、`VIDEO_NAME=Edward_C._Prescott_zh`；复制 BGM wav。
4. 按 §六逐页写 Beamer tex；每页 `make` 检查溢出（vbox≤10pt、hbox≤50pt）。
5. `make pdf` 0 error → `pdftoppm` 逐页目检 → `make images && make video` 出 mp4。
6. 数据库已由本批次入库（has_social_data=1），立传完成后由主控将 has_biography 置 1。

## 十二、版式补遗 【模板通用】

- 表格页安全负间距：顶部 −0.35cm、`arraystretch 0.78–0.82`；公式框前 −0.35~−0.55cm。
- 文本模式希腊字母需数学模式；带圈数字需 `\xeCJKDeclareCharClass{CJK}{"2460->"2473}`。
- 引号用半角 `" "`；品牌口径统一 `OpenMathAI`；`\foreach` 分隔符用 ASCII 逗号。
- 结尾页底部标注 GitHub 链接由首页模板 `\input` 继承，子 deck 不重复。
