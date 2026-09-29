# 医学家立传提示词（James Black）

> OpenMedic 项目 · 20 世纪诺贝尔生理学或医学奖 1988 年得主（与 Elion/Hitchings 三人共享） · 本文件是该人物的专属立传提示词，
> 按 9 节结构执行 Beamer 立传；数据库入库（fields/relations）已由批次完成，本文件第四/三节与 yaml 一致。

## 一、背景信息 【人物专属】

- **目标医学家**：Sir James Whyte Black（1924-06-14 生于苏格兰 Uddingston ~ 2010-03-22 逝于伦敦，享年 85 岁）
- **气质关键词**：**理性药物设计之父、心得安与甲氰咪胍的发明者、为药厂赚得最多却分文不取的苏格兰医生** —— 1988 年获奖理由（逐字引用 medic/nobel_medicine_citations.json，与 Elion/Hitchings 三人共享同一句）：
  > "for their discoveries of important principles for drug treatment"
  > （因他们关于药物治疗重要原理的发现）
- **设计母题**：**受体拮抗的双翼（the antagonist wings）**。β 阻断剂护心、H2 拮抗剂护胃——"不刺激受体，而是锁上它"。
- **本地 Wikipedia 路径**：medic/presentations/pages/20th_century/James_Black_pharmacologist/page.md
- **参考模板**：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）

## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章）

- 第 0/1/2/3 步按 **medic 路径**执行：事实基准 = `medic/presentations/pages/20th_century/James_Black_pharmacologist/page.md`；目录 `medic/presentations/20th_century/James_Black_pharmacologist/`；Makefile 改 `MAIN=James_Black_pharmacologist_zh`；肖像优先 images.txt 所列 Commons 图，失败用装饰圆占位。
- 第 4/4.5 步（入库）**已完成**（第三、四节与 `MySQL/data/James_Black_pharmacologist.yaml` 一致，勿重复入库）。
- 第 5-9 步：配色 → 幻灯片 → Beamer → 布局检查（0 error、vbox≤10pt、hbox≤50pt、逐页目检）→ 史实审查（第七节）。

## 三、研究领域梳理 + 入库（rank 0-4 表）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | pharmacology | 药理学 | 职业主领域（infobox Fields） | 封面 |
| 1 | rational drug design | 理性药物设计 | 由受体理论反向造药，诺奖核心 | 核心页 |
| 2 | cardiology | 心脏病学 | 肾上腺素/心绞痛/β 阻断剂 | 心得安页 |
| 3 | gastroenterology | 胃肠病学 | 组胺/H2 受体/溃疡治疗 | 甲氰咪胍页 |

## 四、社会关系梳理 + 入库（与 yaml 完全一致，已完成）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Gertrude B. Elion | 无向 | 1988 诺贝尔生理学或医学奖三人共享（药物治疗重要原理） |
| co-honored | George H. Hitchings | 无向 | 1988 诺贝尔生理学或医学奖三人共享（药物治疗重要原理） |
| influence | Robert Campbell Garry | 无向 | 邓迪生理学系前辈，为其安排大学学院原初教职 |
| spouse | Hilary Joan Vaughan | 无向 | 1946 结婚，称其为一生"主发条"，1986 先逝 |
| spouse | Rona MacKie | 无向 | 1994 结婚，公共卫生名誉教授 |

> 对手方规范名：均无库内记录按 page.md 形式新建 stub（Elion/Hitchings 为 1988 另两位得主，其本人批次将写镜像边幂等合并）。**无博士导师边**（MB ChB 临床学位，无具名导师）。**relations=5 为诚实值**：John Vane（Wellcome 上司、与其不合）系职场关系不入库（陷阱表留痕）。

## 五、配色方案

- **气质**：苏格兰矿工之子的节俭 + 药厂实验室里的反骨 + 厌恶 publicity 的羞涩天才
- **主色**：药理深红 `#6B3A2E`（处方与心脏的厚重色）
- **诺奖香槟金**：`#D4AF37`
- **badge 四分类色**：
  - `badgeA` 心得安（β 阻断剂） — 心脏红 `#A63A2B`
  - `badgeB` 甲氰咪胍（H2 拮抗剂） — 胃肠绿 `#3E6B4F`
  - `badgeC` 受体理论与理性设计 — 受体蓝 `#2E6E9E`
  - `badgeD` 邓迪 Chancellor 与建制 — 学院紫 `#5E4B8B`
- **背景母题**：低透明度 Y 形受体被钥匙形分子锁住的示意 + 双药剪影。

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 理性药物设计之父 / James W. Black 1924–2010 + badge + 右上头像 + 国籍行（United Kingdom）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Uddingston、Beath 高中、15 岁获奖学金入圣安德鲁斯、MB ChB 1946、ICI/SKF/UCL/KCL、诺奖 1988）
03  核心贡献概览 — 心得安 / 甲氰咪胍 / 理性药物设计方法 / 胃泌素抑制剂
04  矿工之家与数学老师 (1924–1943) — 浸信会五子之家、父亲 Walter 是矿业工程师、太穷上不起大学、Beath 数学老师劝考、15 岁圣安德鲁斯奖学金
05  邓迪与新加坡 (1943–1950) — University College Dundee（圣安德鲁斯临床部）MB ChB 1946、留校生理系助教、因不满当时医患处理方式弃临床、新加坡三年还债
06  格拉斯哥兽医生理系 (1950–1958) — 创建兽医生理学系、肾上腺素对人心脏的作用、心绞痛、 formulate 拮抗肾上腺素的理论
07  ICI 与心得安（核心页一）— 1958 入 ICI、按受体理论目的性造药（方法学革命）、发明心得安——洋地黄之后心脏病治疗最大突破、一度全球最畅销药
08  SKF 与甲氰咪胍（核心页二）— ICI 不愿跟进溃疡项目愤而辞职、Smith Kline & French 九年、发明 H2 受体拮抗剂甲氰咪胍（Tagamet 1975）——销量反超心得安成全球第一处方药
09  UCL 的挫折与 Wellcome 的龃龉 — 1973 UCL 药理系主任建药物化学课程、经费困窘；1978 Wellcome 治疗研究总监、与顶头上司 John Vane 不合 1984 辞职（一句带过）
10  KCL 与 James Black 基金会 — 1984 分析药理学教授至 1992；1988 获强生资助创立基金会、率 25 人团队研发胃泌素抑制剂（防部分胃癌）
11  1988 诺贝尔奖 — 与 Elion、Hitchings 三人共享；官方理由全句；分工：Black=受体拮抗策略、Elion/Hitchings=类似物代谢通路策略；FRS 证书评价段可引
12  荣誉长廊 — Lasker 1976、FRS 1976、Mullard 1978、Baillet Latour 1979、Cameron 1980、下级勋位爵士 1981、Wolf 1982、Scheele 1983、OM 2000、Royal Medal 2004
13  邓迪 Chancellor (1992–2006) — "coming home"（可引）；£2000 万 Sir James Black 中心（Brenner 2006 揭幕）；Glasgow 西医学楼更名、Ninewells 的 James Black Place
14  家庭与身后 — 两任妻子；极度厌 publicity、"惊闻获奖而恐惧"；1985 心得安/甲氰咪胍的故事、Daily Telegraph"为药厂赚得最多而个人所得甚微"；2010-03-22 逝于伦敦葬于苏格兰 Ardclach
15  结尾（OpenMathAI 品牌口径）
```

## 七、特殊陷阱表（★ 核心）

| 陷阱 | 说明 |
|------|------|
| 共享结构 | 1988 三人共享同一句理由；分工：Black=受体拮抗的理性设计（心得安/甲氰咪胍）、Elion/Hitchings=核苷类似物策略——三线并列勿混写 |
| 无博士导师 | MB ChB 临床学位无博士论文/导师——不建 advisor 边 |
| Garry 边 | "responsible for his original appointment at University College Dundee"——职业引路人 influence；勿升级为师承 |
| John Vane 不入库 | Wellcome 顶头上司、不合辞职——职场关系不入库，正文一句带过；Vane 系诺奖得主（1982）勿借其光环 |
| 双药年份 | 心得安 ICI 期（1958-1964）；甲氰咪胍 SKF 期（1964-1973，Tagamet 1975 上市）——两公司两药时间线勿混 |
| "greatest breakthrough" | 心得安被喻为"洋地黄以来心脏病治疗最大突破"——系 page.md 转述评价，注来源 |
| 死亡日期 | metadata 双值 03-22/03-21——**以正文/infobox 22 March 2010 为准** |
| 销量之最 | 心得安曾为全球最畅销药、后被甲氰咪胍反超——先后关系勿倒 |
| 在世性 | 已故（2010）；无在世留白问题；女 Stephanie 仅家庭页一句不入库 |
| 引语红线 | 可引：FRS 当选证书评价段（受体理论贡献）、邓迪"coming home"；其余转述 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| propranolol | 心得安 | 首个有效 β 阻断剂 |
| cimetidine / Tagamet | 甲氰咪胍/泰胃美 | 首个 H2 拮抗剂 |
| beta blocker | β 受体阻断剂 | 心绞痛/心律失常/高血压 |
| H2-receptor antagonist | H2 受体拮抗剂 | 胃酸分泌抑制 |
| angina pectoris | 心绞痛 | 格拉斯哥期研究起点 |
| rational drug design | 理性药物设计 | 由受体理论造药的方法学 |
| gastrin inhibitor | 胃泌素抑制剂 | 基金会期方向 |
| digitalis | 洋地黄 | 对照评价基准 |
| Order of Merit | 功绩勋章 | 2000，全球限 24 人 |

## 九、背景音乐选择

- **选定曲目**：**Last Hope** — Alex-Productions（manifest 预分配）
- **匹配理由**："最后的希望"贴合亿万心绞痛与溃疡患者在他的两粒药里找到的希望——理性设计让"希望"第一次可以按图索骥；沉稳中带张力的曲式匹配其厌名而利他的沉默巨人形象。
- **本地路径**：music_audio/ 下 Alex-Productions Last Hope 曲目（执行时按 curated_tracks.md 对应文件复制到本目录）。
