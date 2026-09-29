# 医学家立传提示词（Ivan Pavlov）

> OpenMedic 项目 · 20 世纪诺贝尔生理学或医学奖 1904 年得主 · 本文件是该人物的专属立传提示词，
> 按 9 节结构执行 Beamer 立传；数据库入库（fields/relations）已由批次完成，本文件第四/三节与 yaml 一致。

## 一、背景信息 【人物专属】

- **目标医学家**：Ivan Petrovich Pavlov（1849-09-14 生于梁赞 ~ 1936-02-27 逝于列宁格勒，享年 86 岁）
- **气质关键词**：**消化生理的改造者、条件反射的发现者、首位俄罗斯诺贝尔奖得主** —— 1904 年获奖理由（逐字引用 medic/nobel_medicine_citations.json）：
  > "in recognition of his work on the physiology of digestion , through which knowledge on vital aspects of the subject has been transformed and enlarged"
  > （表彰其在消化生理学上的工作——使该学科的重要知识得到变革与扩充）
- **设计母题**：**铃与反射弧（bell & reflex arc）**。条件刺激→信号→反应的弧线、狗与唾液滴——用"信号传递"的弧线贯穿全篇视觉。
- **本地 Wikipedia 路径**：medic/presentations/pages/20th_century/Ivan_Pavlov/page.md
- **参考模板**：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）

## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章）

- 第 0/1/2/3 步按 **medic 路径**执行：事实基准 = `medic/presentations/pages/20th_century/Ivan_Pavlov/page.md`；目录 `medic/presentations/20th_century/Ivan_Pavlov/`；Makefile 改 `MAIN=Ivan_Pavlov_zh`；肖像优先 images.txt 所列 Commons 图（晚年照、Nesterov 1935 肖像油画等），失败用装饰圆占位。
- 第 4/4.5 步（入库）**已完成**（第三、四节与 `MySQL/data/Ivan_Pavlov.yaml` 一致，勿重复入库）。
- 第 5-9 步：配色 → 幻灯片 → Beamer → 布局检查（0 error、vbox≤10pt、hbox≤50pt、逐页目检）→ 史实审查（第七节）。

## 三、研究领域梳理 + 入库（rank 0-4 表）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | physiology | 生理学 | 消化生理（诺奖理由）/高级神经活动 | 消化页、诺奖页 |
| 1 | psychology | 心理学 | 条件反射对心理学的影响；2002 排名 24 位最有影响心理学家 | 条件反射页 |
| 2 | behavioral science | 行为科学 | 现代行为疗法奠基（behavior therapy） | 遗产页 |

## 四、社会关系梳理 + 入库（与 yaml 完全一致，已完成）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Elias von Cyon | 师→本人 | 军医学院 former teacher，曾任其助手 |
| advisor-student | Carl Ludwig | 师→本人 | 1884-1886 莱比锡留学师从 |
| influence | Sergey Botkin | — | 1878 邀其主持诊所生理实验室，职业引路人 |
| influence | Ivan Sechenov | — | 俄国生理学之父，立志科学的思想源头 |
| collaborator | Ivan Tolochinov | — | 1901 共同提出条件反射（reflex at a distance） |
| advisor-student | Pyotr Anokhin | 本人→学生 | infobox Doctoral students 明载 |
| advisor-student | Boris Babkin | 本人→学生 | infobox Doctoral students 明载 |
| advisor-student | Leon Orbeli | 本人→学生 | infobox Doctoral students 明载 |
| spouse | Seraphima Vasilievna Karchevskaya | — | 1881-05-01 结婚，育五子 |

> 对手方规范名：均无库内记录，按 page.md 形式新建 stub（`Sergey Botkin` 用正文形式，勿用 metadata 的 Sergey Petrovich Botkin；`Elias von Cyon` 用 page.md 形式）。

## 五、配色方案

- **气质**：实验生理学的严密 + 圣彼得堡的冬夜 + 老科学家的执拗天真
- **主色**：实验室深棕 `#5B3A29`（木质实验台与皮革笔记本）
- **诺奖香槟金**：`#D4AF37`
- **badge 四分类色**：
  - `badgeA` 消化生理 — 腺体橙 `#C97B2D`
  - `badgeB` 条件反射 — 信号蓝 `#2E6E9E`
  - `badgeC` 高级神经活动/气质类型 — 神经紫 `#5E4B8B`
  - `badgeD` 实验犬与慢性实验 — 暖灰 `#7A6A5B`
- **背景母题**：稀疏弧线（反射弧）与小圆点信号（低透明度），从刺激端到反应端渐次出现。

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 条件反射的发现者 / Ivan Pavlov 1849–1936 + 四色 badge + 右上头像 + 国籍行（Russia）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、梁赞、圣彼得堡大学、军事医学 academy、实验医学研究所 45 年、诺奖 1904）
03  核心贡献概览 — 消化生理 / 巴氏小胃 / 条件反射 / 气质类型
04  梁赞神学生 (1849–1870) — 神父之家十兄妹、11 岁才入学（摔伤）、神学校辍学转向科学（Pisarev/Sechenov 影响）
05  圣彼得堡与军医研究院 (1870–1879) — 胰腺神经研究获奖、Cyon 助手、Ustimovich 实验室、Botkin 诊所生理实验室主任、金质奖章
06  博士与留学 (1883–1886) —《心脏的离心神经》博士论文、神经营养功能、莱比锡 Carl Ludwig、布雷斯劳 Heidenhain
07  实验医学研究所 (1891–) — 生理部 45 年、1890 军事医学院药理学教授、1895 生理学讲席 30 年
08  消化生理：慢性实验革命 — 全规模犬舍、"chronic experiments"、食管造瘘与巴氏小胃（Heidenhain/Pavlov pouch）、1897《消化腺工作》
09  1904 诺贝尔奖 — 首位俄罗斯诺奖得主；连续四年提名才因"消化生理"具体成果获奖；官方理由全句
10  条件反射：意外的伟大 — 与助手 Tolochinov 1901 共同提出、"reflex at a distance"、1903 赫尔辛基/马德里报告；Twitmyer 1902 平行研究注记
11  高级神经活动与气质 — 强/平衡/灵活三属性、四种气质类型、越限抑制（TMI）
12  门生与传承 — Anokhin（功能系统理论）、Babkin、Orbeli；星期三座谈会 (1921–1936)
13  荣誉 — ForMemRS 1907、NAS 1908、Copley Medal 1915、美国哲学会 1932；Pawlowia 小行星与月球环形山
14  遗产：从狗铃到行为疗法 — 行为主义（Watson/Skinner）、系统脱敏、 Brave New World 中的巴甫洛夫母题；1994 铃声之争一句带过（Catania vs Littman）
15  结尾（OpenMathAI 品牌口径）
```

## 七、特殊陷阱表（★ 核心）

| 陷阱 | 说明 |
|------|------|
| 获奖理由口径 | 官方理由是**消化生理**；条件反射**不在获奖理由内**——勿写成"因条件反射获诺奖" |
| 生日历法 | 正文 26 September 1849 为儒略历(O.S.)，公历(N.S.) 14 September；infobox 用 1849-09-14；metadata 另有 09-26/09-27 噪声——yaml 与封面统一用 **1849-09-14**，页面可注"俄历 26 日" |
| 无博士学位导师行 | Botkin 非其博士导师（博士论文 1883 完成于军医体系）；page.md 只载其邀入诊所实验室——入库用 influence，勿写 advisor-student |
| Carl Ludwig 关系 | 1884-86 莱比锡留学（博士之后），page.md 明载 "studied in Leipzig with Carl Ludwig"；按留学师从入库，勿写"博士导师" |
| Heidenhain 小胃 | Heidenhain 首创外置胃瓣，Pavlov 改进保留神经支配（Pavlov pouch）；归属勿写反 |
| 条件反射合作者 | 条件反射概念系**与助手 Ivan Tolochinov 1901 年共同提出**（Tolochinov 名其 "reflex at a distance"，1903 赫尔辛基先行报告）——勿写成 Pavlov 独创 |
| 铃铛神话 | "铃铛"是大众误传：实验用多种刺激（电击/哨/节拍器/音叉等），1994 Catania 质疑用铃；页面表述须存疑化 |
| 政治敏感 | 与苏联政府关系节（批评政权/致信斯大林等）**一律禁写**；苏联政府的支持与荣誉仅可在"荣誉/建制"语境客观一句，不展开 |
| 妻子名 | Sara = Seraphima Vasilievna Karchevskaya，1855 生、1947 逝；1881-05-01 结婚；子 Vsevolod 1935 先逝——年份勿混 |
| 引语红线 | 无神论答 Kreps 问句有英文原文（page.md 实载），可引原文+译文；其余"名言"（如"不要后悔"类）page.md 无载禁写 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| classical conditioning | 经典条件反射 | Pavlov 原称 "conditional reflex" |
| conditioned/conditional reflex | 条件反射 | 与口语"条件作用"区分 |
| chronic experiments | 慢性实验 | 犬存活的长期生理实验（对比 acute/vivisection） |
| Heidenhain pouch / Pavlov pouch | 海登海因小胃/巴氏小胃 | 神经支配差异，归属勿混 |
| esophageal fistula | 食管造瘘 | 假饲实验 |
| transmarginal inhibition (TMI) | 越限抑制 | 应激关断反应 |
| Wednesday meetings | 星期三座谈会 | 1921-1936 实验室例会 |
| behaviorism | 行为主义 | Watson/Skinner 引申，非 Pavlov 本人标签 |
| trophic function | 神经营养功能 | 1883 博士论文核心概念 |

## 九、背景音乐选择

- **选定曲目**：**Nostalgia** — Alex-Productions（manifest 预分配）
- **匹配理由**："怀旧/悠长"贴合 86 岁横跨沙俄与苏联的漫长科学生涯——从梁赞神学校到列宁格勒实验室，是时间纵深感最强的一位；略带旧俄色调的旋律呼应 19 世纪生理学传统。
- **本地路径**：music_audio/ 下 Alex-Productions Nostalgia 曲目（执行时按 curated_tracks.md 对应文件复制到本目录）。
