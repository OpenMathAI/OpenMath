# 医学家立传提示词（Susumu Tonegawa）

> OpenMedic 项目 · 20 世纪诺贝尔生理学或医学奖 1987 年得主（独得） · 本文件是该人物的专属立传提示词，
> 按 9 节结构执行 Beamer 立传；数据库入库（fields/relations）已由批次完成，本文件第四/三节与 yaml 一致。

## 一、背景信息 【人物专属】

- **目标医学家**：Susumu Tonegawa（利根川 進，1939-09-05 生于名古屋 ~ 2026-07-11 逝于加州 San Mateo，享年 86 岁）
- **气质关键词**：**V(D)J 重组合成机制的发现者、抗体多样性之谜的独得破解者、两度转场的记忆探索者** —— 1987 年获奖理由（逐字引用 medic/nobel_medicine_citations.json，独享）：
  > "for his discovery of the genetic principle for generation of antibody diversity"
  > （因其发现产生抗体多样性的遗传学原理）
- **设计母题**：**基因的洗牌（the genetic shuffle）**。胚胎与成体 B 细胞 DNA 的对照、抗体基因片段的移动重组删除——"两万基因如何造出百万抗体"。
- **本地 Wikipedia 路径**：medic/presentations/pages/20th_century/Susumu_Tonegawa/page.md
- **参考模板**：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）

## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章）

- 第 0/1/2/3 步按 **medic 路径**执行：事实基准 = `medic/presentations/pages/20th_century/Susumu_Tonegawa/page.md`；目录 `medic/presentations/20th_century/Susumu_Tonegawa/`；Makefile 改 `MAIN=Susumu_Tonegawa_zh`；肖像优先 images.txt 所列 Commons 图（MIT 早期照），失败用装饰圆占位。
- 第 4/4.5 步（入库）**已完成**（第三、四节与 `MySQL/data/Susumu_Tonegawa.yaml` 一致，勿重复入库）。
- 第 5-9 步：配色 → 幻灯片 → Beamer → 布局检查（0 error、vbox≤10pt、hbox≤50pt、逐页目检）→ 史实审查（第七节）。

## 三、研究领域梳理 + 入库（rank 0-4 表）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | immunology | 免疫学 | 抗体多样性遗传原理，诺奖核心 | 核心页 |
| 1 | molecular biology | 分子生物学 | 训练出身 | 求学页 |
| 2 | neuroscience | 神经科学 | 诺奖后转场：记忆印记细胞 | 转场页 |
| 3 | genetics | 遗传学 | 转基因/基因敲除技术先驱 | 技术页 |

## 四、社会关系梳理 + 入库（与 yaml 完全一致，已完成）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Masaki Hayashi | 师→本人 | UCSD 博士导师（1968） |
| influence | Renato Dulbecco | 无向 | Salk 博士后东家，鼓励其转赴巴塞尔（库内 id=6115 复用） |
| influence | François Jacob | 无向 | 京都读书时被其操纵子论文吸引（库内 id=6232 复用） |
| influence | Jacques Monod | 无向 | 同上，与 Jacob 并提（库内 id=4852 复用） |
| spouse | Mayumi Yoshinari Tonegawa | 无向 | 原 NHK 导演/访谈者，现为自由科学作家 |

> 对手方规范名：`Renato Dulbecco`(6115)/`François Jacob`(6232)/`Jacques Monod`(4852) 沿用库内完整记录（他批已入库）；`Masaki Hayashi`/`Mayumi Yoshinari Tonegawa` 新建。**metadata doctoral_advisor 列 Renato Dulbecco，但 page.md 正文明确博士导师是 Masaki Hayashi、Dulbecco 系 Salk 博士后东家——按正文裁定，Dulbecco 入库 influence**。**relations=5 为诚实值**（三子女仅叙事不入库）。1987 系**独得**。

## 五、配色方案

- **气质**：日本战国名著少年 + 巴塞尔孤身转行的勇气的 + 波士顿红袜队的烟火
- **主色**：抗体蓝紫 `#3D3A6B`（免疫球蛋白与深海的复合色）
- **诺奖香槟金**：`#D4AF37`
- **badge 四分类色**：
  - `badgeA` V(D)J 重组 — 重排金 `#C9A227`
  - `badgeB` 增强子发现 — 转录橙 `#C97B2D`
  - `badgeC` 记忆印记细胞（engram） — 神经紫 `#5E4B8B`
  - `badgeD` 疾病转化（FXS/抑郁/阿尔茨海默） — 临床青 `#2E7D8C`
- **背景母题**：低透明度基因片段洗牌箭头 + 海马体轮廓中的光点（engram）。

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 抗体多样性遗传原理的破译者 / Susumu Tonegawa 1939–2026 + badge + 右上头像 + 国籍行（Japan）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、名古屋、日比谷高中、京都大学 1963、UCSD 博士 1968、Salk/Basel/MIT 1981、诺奖 1987）
03  核心贡献概览 — V(D)J 重组合成机制 / 首个细胞增强子 / 记忆印记细胞 / CaMKII-NMDA 通路
04  名古屋与京都 (1939–1963) — 日比谷高中、京都大学读书时读 Jacob/Monod 操纵子论文着迷分子生物学、1963 毕业；日本当时分子生物学选择有限
05  UCSD 与 Hayashi (1963–1968) — 赴加州大学圣迭戈分校师从 Masaki Hayashi 读博士、1968 PhD
06  Salk 与 Dulbecco (1968–1971) — Dulbecco 实验室博士后、得其鼓励转赴免疫学
07  巴塞尔转行 (1971–1981) — 巴塞尔免疫学研究所、从分子生物学转免疫学——诺奖级工作在此完成
08  1976：DNA 重排的发现（核心页一）— 胚胎 vs 成体 B 细胞 DNA 对照：基因移动重组删除造出抗体可变区多样性——百年免疫学中心问题的答案；V(D)J 重组合成机制
09  1983：首个细胞增强子 — 抗体基因复合体相关转录增强子元件（本篇第二贡献）
10  1987 诺贝尔奖（独得）— 官方理由全句；Horwitz 1982/Gairdner 1983/文化勋章 1984/罗伯特·科赫奖 1986/Lasker 1987 预演
11  转场神经科学（核心页二）— MIT 1981 教授、学习记忆中心首任所长 1994→Picower 研究所；CaMKII 1992/NMDA 受体 1996 与记忆形成
12  记忆印记细胞时代 — 光遗传学先驱：2012 激活海马特定神经元群足以唤起恐惧记忆、2013 人工植入虚假记忆；记忆效价/社交记忆/遗忘
13  疾病转化 — 脆性 X 综合征（FRAX586 单剂量改善小鼠症状）、抑郁、失忆、阿尔茨海默的印记细胞机制与治疗概念验证
14  家庭与身后 — 妻 Mayumi（NHK 导演转自由科学作家）三子女（Satto 已故）；红袜队球迷 2004 世界系列开球；RIKEN 脑科学所长 2009-2017；2026-07-11 逝于 San Mateo
15  结尾（OpenMathAI 品牌口径）
```

## 七、特殊陷阱表（★ 核心）

| 陷阱 | 说明 |
|------|------|
| 独享 | 1987 系**独得**（无共享者）——封面勿写"共享" |
| 生年三值 | 正文 lead 作 **September 5, 1939**；infobox 作 November 5（版式讹误）；metadata 双值 09-05/09-06——**以正文 09-05 为准**，陷阱表注记 infobox 讹误 |
| 双导师裁定 | metadata doctoral_advisor 列 Dulbecco，但正文明确博士导师是 **Masaki Hayashi**、Dulbecco 系 Salk 博士后东家——Hayashi 入 advisor-student、Dulbecco 入 influence |
| Jacob/Monod | 仅"读论文受启发"（他自述部分归功二人）——两条 influence，勿升级为师承；二人库内均有完整记录直接复用 |
| 1983 增强子 | 首个细胞增强子元件系其第二贡献——与 V(D)J 诺奖成果分列，勿混并 |
| 印记细胞年份 | 2012 光遗传唤起恐惧记忆、2013 虚假记忆植入——两节点勿混 |
| 转场叙事 | 免疫学→神经科学两度转场（分子生物→免疫→神经）系其传记主线；"虽以免疫学获奖但训练出身分子生物学"表述保留 |
| 子女 | 三子女（Hidde/Hanna/Satto deceased）仅家庭页一句，不入库；Satto 已故一事克制带过 |
| 引语红线 | page.md 无整句直接引语——全部转述；2004 红袜开球系轶闻注记 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| V(D)J recombination | V(D)J 重组 | 抗体多样性遗传机制 |
| operon theory | 操纵子理论 | Jacob/Monod |
| B cells | B 细胞 | 胚胎/成体对照实验对象 |
| transcriptional enhancer | 转录增强子 | 1983 首个细胞增强子 |
| memory engram cells | 记忆印记细胞 | 光遗传时代核心概念 |
| CaMKII / NMDA receptor | CaMKII/NMDA 受体 | 突触可塑性与记忆 |
| Fragile X Syndrome | 脆性 X 综合征 | FRAX586 转化方向 |
| optogenetics | 光遗传学 | 印记细胞操作工具 |
| Order of Culture | 日本文化勋章 | 1984 天皇授 |

## 九、背景音乐选择

- **选定曲目**：**Winds Of Freedom** — Alex-Productions（manifest 预分配）
- **匹配理由**："自由之风"贴合其两度自由转场的学术人生——从免疫学的基因洗牌到神经科学的记忆之光，自由换域而巅峰依旧；开阔沉静的曲式承载横跨太平洋的探索者形象。
- **本地路径**：music_audio/ 下 Alex-Productions Winds Of Freedom 曲目（执行时按 curated_tracks.md 对应文件复制到本目录）。
