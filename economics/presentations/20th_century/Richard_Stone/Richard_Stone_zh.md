# 经济学家立传提示词（Richard Stone）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1984 年得主 Richard Stone（理查德·斯通）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Richard_Stone/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Sir John Richard Nicholas Stone（1913-08-30 生于伦敦 ~ 1991-12-06 逝于剑桥，享年 78 岁），CBE、FBA
- **气质关键词**：**国民核算之父、复式记账的诗人、把一国经济写成资产负债表的统计学家**
- **诺奖获奖理由**（逐字引用）：
  > "for having made fundamental contributions to the development of systems of national accounts and hence greatly improved the basis for empirical economic analysis"（表彰他对国民经济核算体系发展的奠基性贡献，从而极大改善了实证经济分析的基础）
- **设计母题**：**复式记账的平衡（double-entry balance）**——借贷两侧必须相抵、一国收支在表格里两两对齐，是「国民经济整体可核算」的视觉隐喻：左右呼应的账目栏与一枚金色天平构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Richard_Stone/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/Richard_Stone/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Richard_Stone_zh`、`VIDEO_NAME=Richard_Stone_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Stone 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | national accounts | 国民核算 | 诺奖核心：SNA 雏形与复式记账引入 | 核心页 |
| 1 | economic statistics | 经济统计 | 战时政府统计与中央统计局工作 | 早期页 |
| 2 | input-output analysis | 投入产出分析 | infobox Notable ideas 明载 | 贡献页 |
| 3 | consumer demand analysis | 消费者需求分析 | DAE 时期需求分析项目 | DAE 页 |
| 4 | socio-demographic accounting | 社会人口核算 | DAE 三大项目之一 | DAE 页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| collaborator | James Meade | 无向 | 战时为英政府共同构建早期国民核算，1941 英国第一份国民核算 |
| influence | Colin Clark | 无向 | 剑桥统计学老师，引入国民收入测算项目（infobox Influences 明载） |
| advisor-student | Richard Kahn | Stone ← 导师 | 剑桥转经济学的指导教师（正文明载 supervision） |
| advisor-student | Gerald Shove | Stone ← 导师 | 剑桥转经济学的指导教师（正文明载 supervision） |
| colleague | John Maynard Keynes | 无向 | 战时中央统计局任 Keynes 助手 |
| advisor-student | James Mirrlees | Stone → 学生 | infobox Doctoral students 明载 |
| advisor-student | Angus Deaton | Stone → 学生 | infobox Doctoral students 明载 |
| spouse | Winifred Mary Jenkins | 无向 | 1936 结婚，合办月刊 Trends，1940 离异 |
| spouse | Feodora Leontinoff | 无向 | 1941 结婚，1956 去世 |
| spouse | Giovanna Saffi | 无向 | 1960 结婚，多项著作合作者（1959/1961 两书合著） |

**不入库但提示词可叙述**：女儿 Caroline（仅具名不入 parent-child）；J.A.C. Brown（剑桥增长项目共事，红链同事防噪声）；Terry Barker（增长项目继任者）；Agatha Chapman（DAE 研究助手）；Durbin & Watson（DAE 旗下成果）；第三任妻曾祖父 Aurelio Saffi（意大利爱国者，隔代姻缘禁建边）。

## 五、配色方案 【人物专属】

- **气质**：账目的秩序、战时统计的冷静、英式的严谨
- **主色**：`#1E5631`（核算绿——复式记账的平衡与账本深色封皮）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeNA` 国民核算 — 深绿 `#1E5631`
  - `badgeStat` 经济统计 — 靛蓝 `#16324F`
  - `badgeIO` 投入产出 — 琥珀 `#C07A2A`
  - `badgeDem` 社会人口核算 — 灰紫 `#52307C`
- **背景母题**：左右呼应的账目栏与一枚金色天平（复式记账两侧必须相抵的抽象化），呼应「一国经济可以像账本一样被平衡记录」的核心思想。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 国民核算之父 / Richard Stone 1913–1991 + 四色 badge + 右上头像 + 国籍行（United Kingdom）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地伦敦、教育 Caius/King's Cambridge、
    任职剑桥 DAE 主任与 P.D. Leake 讲席教授、诺奖 1984、核心领域）
03  核心贡献概览 — 国民核算体系 / 复式记账引入 / 投入产出 / 需求分析
04  伦敦早年与印度之行 (1913–1931) — Westminster School、17 岁随父赴马德拉斯、亚非游历
05  剑桥转轨：从法律到经济学 (1931–1935) — 大萧条失业的触动、Kahn 与 Shove 指导、Colin Clark 引入国民收入测算
06  战时国民核算的诞生 (1939–1945) — 与 Meade 合作为英政府核算战争资源、1941 英国首份国民核算、
    分署后入中央统计局任 Keynes 助手
07  1941：英国第一份国民核算（核心贡献页）— 早期 SNA 的形成
08  DAE 十年 (1945–1955) — 应用经济学系主任、计量与需求分析群星、三大项目
09  复式记账进入国民核算（核心贡献页）— 收支两侧相抵、全球可核算
10  剑桥增长项目与 MDM (1955–1980) — P.D. Leake 讲席、SAM、MDM 模型、Cambridge Econometrics
11  门生与传承 — James Mirrlees、Angus Deaton（两位诺奖弟子）
12  荣誉与认可 — Nobel 1984、CBE、Knight Bachelor、FBA、皇家经济学会主席 1978–80
13  魁奈的影子 — 受奖演说提及 Tableau économique、部门间相互联系的先驱
14  遗产与结尾 — SNA 成为全球统计语言 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由两套表述 | 官方 citation 为 "for having made fundamental contributions to the development of systems of national accounts..."；page.md 正文另有转述 "for developing an accounting model that could be used to track economic activities..."；**引用一律用官方 citation**，正文转述可叙述但勿混写 |
| '国民收入核算之父' | page.md 写 "He is **sometimes known as** the 'father of national income accounting'"——用「有时被称为」，勿写成公认头衔断言 |
| 首创口径 | page.md 明载 "While he was **not the first** economist to work in this field, he was the first to do so with **double entry accounting**"——勿写「第一个做国民核算的人」，首创点在复式记账引入 |
| 三任妻子 | 三段婚姻全部入库 spouse（Winifred Jenkins 1936–1940 / Feodora Leontinoff 1941–1956 / Giovanna Saffi 1960–）；第三任妻是合著者，勿漏「合著」一层 |
| Kahn/Shove 的身份 | 两人是 Stone 转学经济学时在剑桥的 **supervision** 指导教师（本科层级），非博士学位导师；入库 advisor-student 但 note 注明「剑桥指导教师」 |
| Keynes 关系 | 战时 Stone 在中央统计局 **became Keynes' assistant**——是上下级工作关系，入 colleague 并注明助手关系，勿写师承 |
| Meade 关系 | 战时合作构建国民核算（1941 后分署）；infobox 又将 Meade 列入 Influences；取更强的 **collaborator** 单边，勿重复建 influence 边 |
| 女儿 | 只具名 Caroline（"Children: 1"），无其他信息，不入 parent-child |
| 配偶曾祖 | Giovanna Saffi 是意大利爱国者 Aurelio Saffi 的曾孙女，隔代不建边 |
| 全名与头衔 | 全名 John Richard Nicholas Stone，行文可用 Richard Stone；CBE 与 Knight Bachelor（爵士）勿混授年份（page.md 未给封爵年份，只列头衔） |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| system of national accounts (SNA) | 国民经济核算体系 | 获奖理由核心词 |
| double entry accounting | 复式记账 | Stone 引入国民核算的关键 |
| national income | 国民收入 | Colin Clark 项目起点 |
| input-output model | 投入产出模型 | infobox Notable ideas |
| Central Statistical Office | 中央统计局 | 战时任职机构 |
| Department of Applied Economics (DAE) | 剑桥应用经济学系 | 1945–1955 任主任 |
| Cambridge Growth Project | 剑桥增长项目 | 与 J.A.C. Brown 共同启动 |
| Social Accounting Matrix (SAM) | 社会核算矩阵 | 后发展至世界银行 |
| Cambridge Multisectoral Dynamic Model (MDM) | 剑桥多部门动态模型 | 增长项目产物 |
| Tableau économique | 经济表 | 受奖演说提及魁奈著作 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Nostalgy**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Stone 的一生横跨大萧条、二战与战后重建——账本里记下的不是抽象数字而是一个时代的创伤与复原；「怀旧而深情」的曲风贴合这位把战争创伤写成收支平衡表的统计学家，也呼应其晚年回望 1941 年那份英国首份国民核算的历史感。
- **本地路径**：复制 `music_audio/inspiring-electronic/17-_DA0mdtL-jI-Nostalgy - by AShamaluevMusic ｜ Sad Cinematic Music For Videos, Documentaries & Films.wav` 到 `economics/presentations/20th_century/Richard_Stone/Nostalgy.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
