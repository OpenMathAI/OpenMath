# 经济学家立传提示词（Peter Diamond）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2010 年得主 Peter Diamond（彼得·戴蒙德）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Peter_Diamond/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Peter Arthur Diamond（1940-04-29 生于纽约市，在世）
- **气质关键词**：**搜寻摩擦的刻度师、世代交叠模型的奠基人、社会保障政策的顶梁柱**
- **诺奖获奖理由**（2010，与 Dale T. Mortensen、Christopher A. Pissarides 共享；逐字引自 manifest）：
  > "for their analysis of markets with search frictions"（表彰他们对存在搜寻摩擦的市场的分析）
- **设计母题**：**匹配与摩擦（search & match）**——工人与岗位、买者与卖者在摩擦市场中彼此寻找：错落的圆点与连接虚线构成「待匹配」视觉隐喻，呼应搜寻理论的核心。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Peter_Diamond/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Peter_Diamond/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Peter_Diamond_zh`、`VIDEO_NAME=Peter_Diamond_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Diamond 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | search and matching | 搜寻与匹配 | 劳动力市场搜寻摩擦，2010 诺奖核心（Diamond 1982） | 核心页 |
| 1 | overlapping generations model | 世代交叠模型 | Diamond 1965 扩展 Ramsey–Cass–Koopmans | OLG 页 |
| 2 | macroeconomics | 宏观经济学 | 政府债务、资本积累、动态无效率 | 理论页 |
| 3 | optimal taxation | 最优税收 | Diamond–Mirrlees 生产效率结果 | 税收页 |
| 4 | social insurance | 社会保险 | 美国社会保障政策分析（职业生涯重心） | 政策页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致；共 13 条）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Robert Solow | Diamond → 学生 | MIT 博士导师（1963），论文 Essays on optimal economic growth |
| advisor-student | Martin Hellwig | Diamond → 学生 | 博士生（infobox Doctoral students 明载） |
| advisor-student | David K. Levine | Diamond → 学生 | 博士生（infobox 明载） |
| advisor-student | Andrei Shleifer | Diamond → 学生 | 博士生，John Bates Clark Medal 得主 |
| advisor-student | Emmanuel Saez | Diamond → 学生 | 博士生，John Bates Clark Medal 得主 |
| advisor-student | Botond Kőszegi | Diamond → 学生 | 博士生（infobox 明载） |
| advisor-student | Ben Bernanke | Diamond → 学生 | 正文明载曾是 Diamond 学生（2022 诺奖得主） |
| co-honored | Dale T. Mortensen | 无向 | 2010 诺贝尔经济学奖共享（搜寻摩擦市场分析） |
| co-honored | Christopher A. Pissarides | 无向 | 2010 诺贝尔经济学奖共享（搜寻摩擦市场分析） |
| spouse | Kate Myrick | 无向 | Kate Priscilla Myrick，1966 结婚，育二子 |
| influence | Paul Samuelson | 无向 | OLG 框架源自其 exact consumption-loan model |
| collaborator | James Mirrlees | 无向 | Diamond–Mirrlees 生产效率结果 |
| collaborator | Peter R. Orszag | 无向 | 合著 Saving Social Security（Brookings 2005） |

**不入库但提示词可叙述**：兄弟 Richard（1934 生）；2010 诺贝尔得主合影同框者（Geim/Novoselov 等属物理化学侧）；Shelby 参议员仅为提名冲突转述方，禁建关系。

## 五、配色方案 【人物专属】

- **气质**：沉稳、务实、理论为政策服务
- **主色**：`#1E6B52`（搜寻青绿——匹配达成前市场摩擦的深色调）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeSearch` 搜寻匹配 — 青绿 `#1E6B52`
  - `badgeOLG` 世代交叠 — 靛蓝 `#2A3468`
  - `badgeTax` 最优税收 — 琥珀 `#C07A2A`
  - `badgeSSI` 社会保障 — 灰紫 `#52307C`
- **背景母题**：错落圆点与连接虚线（待匹配的工人与空缺岗位），呼应搜寻摩擦母题。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 搜寻摩擦的刻度师 / Peter Diamond 1940– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、纽约出身、Yale 数学 1960 / MIT 博士 1963、
    导师 Solow、MIT Institute Professor 1997、诺奖 2010、核心领域）
03  核心贡献概览 — 搜寻匹配 / OLG / Diamond–Mirrlees / 社会保障政策
04  早年与教育 (1940–1963) — 纽约犹太家庭、Woodmere 长岛、Yale 数学 summa cum laude、MIT 博士
05  加州与回麻省 (1963–1970) — Berkeley 助理教授 1963–65，1966 入 MIT，1970 正教授
06  世代交叠模型（核心贡献页一）— 1965 扩展 Ramsey–Cass–Koopmans、动态无效率、政府债务可增进福利
07  Diamond–Mirrlees 生产效率（核心贡献页二）— DM 世界的七假设、中间品免税结论
08  搜寻与匹配（核心贡献页三）— Diamond 1982 椰子模型、均衡失业的内生性
09  社会保障政策研究 — 职业生涯重心、与 Orszag 合著、精算微调建议
10  门生与传承 — Hellwig / Levine / Shleifer / Saez / Kőszegi / Bernanke
11  荣誉与学会 — 计量学会会长、AEA 会长 2003、NAS 1984、NASI 创始会员
12  美联储提名风波 (2010–2011) — 客观记录：三度提名、2011-06 撤回、历时 14 个月未获确认
13  2010 斯德哥尔摩 — 与 Mortensen、Pissarides 共享、诺奖演讲 Unemployment, Vacancies, Wages
14  遗产与结尾 — 搜寻理论进入宏观主流 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由归属 | 2010 三人共享同一句 "for their analysis of markets with search frictions"，勿单写 Diamond 专属措辞 |
| OLG 归属 | Diamond 1965 是把 Samuelson 的 exact consumption-loan model 扩展为新个体不断出生/死亡的框架，勿写成「独自发明 OLG」 |
| 政治红线 | 美联储提名风波（2010-2011）只客观记录「三度提名—参议院未确认—2011-06 主动撤回—历时 14 个月」；Shelby 发言与党派对立表述禁入引语框，禁任何评价性措辞 |
| 学生名单 | infobox Doctoral students 五人（Hellwig/Levine/Shleifer/Saez/Kőszegi）+ 正文明载的 Bernanke 共 6 人；勿漏 Bernanke，也勿把正文未载者加入 |
| 两枚 Clark Medal | Shleifer 与 Saez 是「其博士生中获约翰·贝茨·克拉克奖者」，勿写成别人 |
| 出生日期 | 1940-04-29，frontmatter 与正文一致，无噪声；在世，卒年留白 |
| 合著书 | 与 Orszag 合著 Saving Social Security（2004/-5 Brookings），年份页内作 "(2004,-5)"，幻灯片写 2005 并注 |
| 诺奖演讲 | 2010-12-08 题为 Unemployment, Vacancies, Wages，勿与获奖理由混淆 |
| 职务口径 | MIT Institute Professor（1997 授予）是 MIT 最高教职，勿写成「讲座教授」泛称；1985-86 曾任经济系主任 |
| metadata 噪声 | metadata.json field_of_work 含 behavioral economics（infobox Discipline 亦列），可作叙述但 fields 入库以获奖核心排序 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| search frictions | 搜寻摩擦 | 获奖理由核心词，勿译「搜索」 |
| matching | 匹配 | 与 matching theory（匹配理论）语境一致 |
| overlapping generations model | 世代交叠模型 | OLG，Diamond 1965 |
| dynamic inefficiency | 动态无效率 | 竞争均衡可能非帕累托最优 |
| Golden Rule | 黄金律（储蓄率） | Phelps 提出，Diamond 引用 |
| Diamond–Mirrlees production efficiency | Diamond–Mirrlees 生产效率 | 最优税收基准结果 |
| Diamond coconut model | 椰子模型 | Diamond 1982 搜寻模型别称 |
| Social Security | （美国）社会保障 | 勿与一般「社会保险」泛称混用 |
| crowding out | 挤出（资本） | 政府债务对资本存量的作用 |
| Institute Professor | 学院教授 | MIT 最高教职头衔 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Lonesome**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：搜寻摩擦市场的本质是「未完成的相遇」——失业者与空缺岗位在摩擦中彼此等待，「孤独/等待」的曲意恰好对应搜寻理论的情绪底色；克制的抒情也贴合 Diamond 以理论服务公共政策的沉稳气质。
- **本地路径**：复制 `music_audio/inspiring-electronic/16-xBLYHNv7C4Q-Lonesome - by AShamaluevMusic ｜ Sad and Emotional Cinematic Music.wav` 到 `economics/presentations/21th_century/Peter_Diamond/Lonesome.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
