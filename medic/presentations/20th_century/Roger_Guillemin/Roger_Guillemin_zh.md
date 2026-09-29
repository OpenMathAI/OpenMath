# 医学家立传提示词（Roger Guillemin）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1977 年得主 Roger Guillemin（罗歇·夏尔·吉耶曼）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Roger_Guillemin/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Roger Charles Louis Guillemin（1924-01-11 生于法国第戎 ~ 2024-02-21 逝于加州圣地亚哥，享年 100 岁）
- **气质关键词**：**神经激素的开拓者、两百多万个羊下丘脑的解剖者、Salk 神经内分泌学的掌门**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1977 条目，Guillemin/Schally 共享同句）：
  > "for their discoveries concerning the peptide hormone production of the brain"（因其关于脑内肽类激素生成的发现）
- **设计母题**：**下丘脑-垂体的信使（hypothalamic messengers）**——下丘脑经释放因子（releasing factors）指挥垂体；用「脑与腺体之间的信使分子链路渐次点亮」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Roger_Guillemin/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/20th_century/Roger_Guillemin/`。Makefile 复制后设 `MAIN=Roger_Guillemin_zh`、`VIDEO_NAME=Roger_Guillemin_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Guillemin 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | neuroendocrinology | 神经内分泌学 | 释放因子与下丘脑控制垂体，1977 诺奖核心 | 封面、核心页 |
| 1 | endocrinology | 内分泌学 | TRH/GnRH/生长抑素结构鉴定 | 核心页 |
| 2 | neuroscience | 神经科学 | infobox Fields；Salk 神经内分泌实验室主任 | 职业页 |
| 3 | peptide chemistry | 肽类化学 | 脑肽激素的结构测定（理由句关键词） | 核心页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 正文/infobox 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Andrew Schally | 无向 | 1957 加入贝勒共事五年后决裂（进展停滞与个人冲突），其后独立竞赛：羊下丘脑对猪脑、TRH/GnRH 结构分立鉴定 |
| co-honored | Andrew Schally | 无向 | 1977 诺贝尔生理学或医学奖共享（脑肽激素生成，官方理由句同一） |
| co-honored | Rosalyn Sussman Yalow | 无向 | 1977 诺贝尔生理学或医学奖共享（Yalow 半边理由为放射免疫测定法研发，跨批次 batch-25，用 manifest 形式名） |
| advisor-student | Hans Selye | 对方 → 导师 | 蒙特利尔大学实验医学与外科学院 Selye 门下获博士（1953） |
| advisor-student | Wylie Vale | Guillemin → 学生 | infobox Doctoral students 明载；后于 Salk 自立实验室成「又一场激烈竞争」（CRF 之赛） |
| colleague | Roger Burgus | 无向 | 团队成员：1969 鉴定促甲状腺释放因子（TRF）取得突破、保住经费 |
| spouse | Lucienne Jeanne Billard | 无向 | 婚姻 69 年，妻 2021 以百岁去世；育五女一子 |

**不入库但提示词可叙述**：《The Nobel Duel》（Wade 1981）与《Laboratory Life》（Latour & Woolgar 1986）两本以其之争为题材的书（仅书讯）；六名子女（仅具数量）。

## 五、配色方案 【人物专属】

- **气质**：法兰西的起点、得克萨斯的竞赛、拉霍亚的海光
- **主色**：`#8C2F1B`（释放因子赭红——两百万羊下丘脑的漫长氧化与晨光）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeRF` 释放因子 — 赭红 `#8C2F1B`
  - `badgeTrh` TRH/GnRH 结构 — 深金 `#B8860B`
  - `badgeSalk` Salk 建制 — 深蓝 `#16324F`
  - `badgeDuel` 诺奖对决 — 灰紫 `#52307C`
- **背景母题**：脑与垂体之间的信使链路，节点随发现渐次点亮。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 神经激素的开拓者 / Roger Guillemin 1924–2024 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、第戎出身、里昂 MD 1949、蒙特利尔博士 1953（Selye 门下）、
    贝勒医学院→Salk 神经内分泌实验室主任 1970–1989、诺奖 1977、享年 100、核心领域）
03  核心贡献概览 — 释放因子 / TRH 与 GnRH 结构 / 生长抑素与内啡肽 / 双雄竞赛
04  第戎与里昂 (1924–1949) — Lycée Carnot；里昂 MD 1949；勃艮第乡村行医
05  蒙特利尔：Selye 门下 (1949–1953) — 实验医学与外科研究所；博士 1953
06  1954 年的关键观察 — 垂体细胞无下丘脑细胞在场即不产激素→「下丘脑经激素控制垂体」
07  贝勒岁月与 Schally 来投 (1957–1962) — 共事五年；决裂（进展停滞与个人冲突）；Schally 迁新奥尔良 VA
08  两百万羊下丘脑对十万猪脑（竞赛页）— 两线独立处理海量组织；释放因子含量极低的检测难题
09  Burgus 的突破 (1969) — TRF 鉴定保住经费；FRF 随之
10  TRH 与 GnRH 结构的分立鉴定 — 两实验室各自完成；1977 共享诺奖（核心贡献页）
11  Salk 岁月 (1970–1989) — 神经内分泌实验室；生长抑素发现；内啡肽「最早一批」分离者；与 Vale 的 CRF 之赛
12  1977 三人共享的结构 — Guillemin/Schally 同句（脑肽激素生成）+ Yalow 另句（放射免疫测定）
13  荣誉年表 — NAS 1974 / Gairdner 1974 / Lasker 1975 / Dickson+Passano+国家科学勋章 1976 / AAAS 1977 / 诺贝尔 1977
14  百岁与结尾 — 2007 Salk 临时校长；2024-01-11 满百、02-21 辞世圣地亚哥 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 1977 三人共享但理由句不同 | Guillemin/Schally 同句 "for their discoveries concerning the peptide hormone production of the brain"；**Yalow 另句** "for the development of radioimmunoassays of peptide hormones"（放射免疫测定法）——Yalow 的获奖理由与脑肽激素无关，note 与叙述勿混 |
| 决裂与竞赛的表述 | 1957 Schally 来投、五年后决裂（"for lack of progress and personal conflicts"）；其后羊下丘脑（Guillemin，逾 200 万个）对猪脑（Schally，1966 年已处理 10 万猪脑）的独立竞赛——叙事聚焦方法与结果，不作贬抑；《The Nobel Duel》仅书讯 |
| Burgus 的位置 | TRF 鉴定的实验突破出自团队成员 Roger Burgus（1969）——colleague 边已建，叙事勿把结构鉴定全归 Guillemin 亲手 |
| Vale 的双面 | infobox 博士生 + Salk 自立实验室后的「yet another furious rivalry」（其实验室率先纯化测序 CRF）——学生边一行承载，note 点明后竞 |
| 两条理由句的页内呈现 | 诺奖页应并列三人但区分两组理由句——结构化排版避免误读 |
| 国籍口径 | infobox Citizenship **United States**（1965 入籍）；出生法国、法裔——yaml 按 manifest/Nobel 口径 United States，正文可写 French-American |
| 百岁 | 2024-01-11 满百，2024-02-21 辞世圣地亚哥——「享年 100 岁」 |
| 政治内容禁写（★） | page.md 载其联署请求联合国儿童权利委员会探视被软禁的班禅喇嘛转世灵童——**涉及中国政治议题，一律禁写禁提**，15 页规划不含此内容 |
| 妻子姓名 | infobox 作 Lucienne Guillemin，正文全名 **Lucienne Jeanne Billard**（婚姻 69 年，2021 以百岁去世）——yaml 用正文全名 |
| 荣誉年表 | NAS/Gairdner 1974、Lasker 1975、Dickson/Passano/国家科学勋章 1976、AAAS/诺贝尔 1977——七个年份勿混 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| releasing factors | 释放因子 | 早期称谓，后称 hormone |
| peptide hormone production of the brain | 脑内肽类激素生成 | 获奖理由核心词，逐字对应 |
| TRH (thyrotropin-releasing hormone) | 促甲状腺激素释放激素 | 1969 鉴定（TRF→TRH） |
| GnRH (gonadotropin-releasing hormone) | 促性腺激素释放激素 | 控制 FSH/LH |
| somatostatin | 生长抑素 | Salk 时期发现 |
| endorphins | 内啡肽 | 「among the first」分离者口径 |
| CRF (corticotropin-releasing factor) | 促皮质素释放因子 | 与 Vale 竞赛的标的 |
| hypothalamus / pituitary | 下丘脑/垂体 | 控制链两端 |
| neurohormone | 神经激素 | Known for 词条 |
| sheep hypothalami | 羊下丘脑 | 逾 200 万个的采样规模 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Winds Of Freedom**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：从第戎到蒙特利尔再到拉霍亚——横跨三国的自由科学生涯；「自由之风」也呼应其与 Schally 竞赛终以共享诺奖收束的开放格局，以及 Salk 研究所的自由探究精神。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Roger_Guillemin/WindsOfFreedom.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
