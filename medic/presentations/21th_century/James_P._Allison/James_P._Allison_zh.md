# 医学家立传提示词（James P. Allison）

> OpenMedic 项目 · 21 世纪诺贝尔生理学或医学奖 2018 年得主（与 Honjo 共享） · 本文件是该人物的专属立传提示词，
> 按 9 节结构执行 Beamer 立传；数据库入库（fields/relations）已由批次完成，本文件第四/三节与 yaml 一致。

## 一、背景信息 【人物专属】

- **目标医学家**：James Patrick Allison（1948-08-07 生于得州 Alice，在世）
- **气质关键词**：**CTLA-4"免疫刹车"的松开者、癌症免疫检查点疗法的开创者、蓝口琴手** —— 2018 年获奖理由（逐字引用 medic/nobel_medicine_citations.json，与 Honjo 共享同一句）：
  > "for their discovery of cancer therapy by inhibition of negative immune regulation"
  > （因他们发现通过抑制负向免疫调控来治疗癌症）
- **设计母题**：**松开的刹车（releasing the brakes）**。T 细胞油门（共刺激）与 CTLA-4 刹车的拔销动作、 unleashing 的箭头——"免疫系统的油门一直在，只是刹车焊死了"。
- **本地 Wikipedia 路径**：medic/presentations/pages/21th_century/James_P._Allison/page.md
- **参考模板**：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）

## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章）

- 第 0/1/2/3 步按 **medic 路径**执行：事实基准 = `medic/presentations/pages/21th_century/James_P._Allison/page.md`；目录 `medic/presentations/21th_century/James_P._Allison/`；Makefile 改 `MAIN=James_P._Allison_zh`；肖像优先 images.txt 所列 Commons 图（Allison in 2018），失败用装饰圆占位。
- 第 4/4.5 步（入库）**已完成**（第三、四节与 `MySQL/data/James_P._Allison.yaml` 一致，勿重复入库）。
- 第 5-9 步：配色 → 幻灯片 → Beamer → 布局检查（0 error、vbox≤10pt、hbox≤50pt、逐页目检）→ 史实审查（第七节）。

## 三、研究领域梳理 + 入库（rank 0-4 表）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | immunology | 免疫学 | 职业主领域（infobox Fields） | 封面 |
| 1 | tumor immunotherapy | 肿瘤免疫治疗 | 检查点阻断疗法，诺奖核心 | 核心页 |
| 2 | T-cell biology | T 细胞生物学 | TCR 复合体、共刺激/抑制信号 | 研究页 |

## 四、社会关系梳理 + 入库（与 yaml 完全一致，已完成）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | G. Barrie Kitto | 师→本人 | UT Austin 博士导师（1973，天冬酰胺酶） |
| influence | Ralph Reisfeld | 无向 | Scripps 博士后导师（HLA 与 T 细胞） |
| colleague | G. N. Callahan | 无向 | 1977 Nature 通讯合著：抗原关联蛋白抑制免疫攻击 |
| co-honored | Robert D. Schreiber | 无向 | 2017 Balzan 奖共享（肿瘤免疫治疗免疫学途径） |
| co-honored | Tasuku Honjo | 无向 | 2018 诺贝尔生理学或医学奖共享（负向免疫调控抑制） |
| spouse | Malinda Bell | 无向 | 1969 结婚，2012 离异，育一子 |
| spouse | Padmanee Sharma | 无向 | 2014 结婚，合作者与朋友成婚 |
| collaborator | Padmanee Sharma | 无向 | 2004 相识后长期科研合作 |

> 对手方规范名：均无库内记录按 page.md 形式新建 stub；`Tasuku Honjo` 与本批 Honjo 篇同形式镜像 co-honored 边幂等合并。

## 五、配色方案

- **气质**：得州的执拗 + 基础科学通往临床的长跑 + 蓝调口琴的自由
- **主色**：免疫红 `#A63A2B`（T 细胞与红丝带式的战斗色）
- **诺奖香槟金**：`#D4AF37`
- **badge 四分类色**：
  - `badgeA` CTLA-4 刹车 — 检查点红 `#B23A48`
  - `badgeB` TCR 与共刺激 — 受体蓝 `#2E6E9E`
  - `badgeC` ipilimumab 临床 — 药物绿 `#3E6B4F`
  - `badgeD` MD Anderson 建制 — 得州橙 `#C97B2D`
- **背景母题**：低透明度 T 细胞球体 + 一条松开的束缚带（刹车线）。

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 癌症免疫检查点疗法的开创者 / James P. Allison 1948– + badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生年 Alice TX、UT Austin 1969/1973、Berkeley/MSKCC/MD Anderson、诺奖 2018）
03  核心贡献概览 — TCR 首次分离 / CTLA-4 抑制分子 / 1996 抗体阻断 / ipilimumab
04  得州少年与初中数学老师 (1948–1969) — 三子之幼、八年级数学老师点燃科学志向、NSF 暑期项目、函授修完高中生物、UT 微生物学士（DKE 兄弟会）
05  越南阴影下的科学选择 — 页面直接引语（英文原文可引）："I felt that I had to do medically related research in order to avoid going to Vietnam..."；asparaginase 研究、1973 博士（Kitto 门下）
06  Scripps 与 T 细胞训练 (1974–1977) — Reisfeld 门下研究 HLA 与 T 细胞、自我/非我识别
07  1977 Nature 通讯 — 与 Callahan：抗原与额外蛋白关联使免疫系统无法攻击癌细胞——检查点思想的种子
08  1982：首次发现 T 细胞受体 — Berkeley 1990s：CTLA-4 是抑制性分子
09  1996：松开刹车（核心页）— 首次证明抗体阻断 CTLA-4 可增强抗肿瘤免疫与肿瘤排斥——"immune checkpoint therapies" 的奠基
10  ipilimumab 上市 — 临床转化为 Yervoy，2011 FDA 批准用于转移性黑色素瘤
11  2018 诺贝尔奖 — 与 Honjo 共享；官方理由全句（CTLA-4 与 PD-1 两条刹车线）；2010-2019 顶级奖数第一（13/40，page.md 明载可写）
12  荣誉矩阵 — Breakthrough 2014、Tang 2014（与 Honjo）、Gairdner/Horwitz/Massry/Harvey 2014、Lasker+Ehrlich 2015、Wolf/Alpert/Balzan（与 Schreiber）2017、Sjöberg、Balzan 等
13  家庭与音乐 — 母亲因淋巴瘤去世（他 10 岁）、兄 2005 前列腺癌病逝（私人动机注记）；两任妻子；蓝调口琴手（The Checkpoints/The Checkmates 乐队）
14  遗产：把免疫变成抗癌武器 — 检查点抑制剂时代、2019 纪录片 Jim Allison: Breakthrough
15  结尾（OpenMathAI 品牌口径）
```

## 七、特殊陷阱表（★ 核心）

| 陷阱 | 说明 |
|------|------|
| 共享结构 | 2018 两人共享同一句理由（Allison=CTLA-4 线，Honjo=PD-1 线）——机制互补而非同一分子 |
| "首次发现 TCR" | page.md 称 "one of the first people to isolate the T-cell antigen receptor complex protein"（1982 首次发现）；正文亦有 1982 "first discovered"——措辞保持页面口径，勿写成"唯一发现者" |
| Vietnam 引语 | 直接引语系 page.md 英文原文，可引原文+译文（涉及越战征兵背景，属个人经历非政治立场，客观呈现） |
| 1996 实验 | "first to show antibody blockade of CTLA-4 → anti-tumor response"；1990s 证明 CTLA-4 抑制功能——两个"第一"年份勿混（1990s 机制 / 1996 阻断） |
| Balzan 共享 | 2017 Balzan（免疫学途径治癌）与 Robert D. Schreiber 共享——勿混入 Wolf（2017 Wolf 为个人获奖） |
| 两任妻子 | Malinda Bell（1969-2012，离异，一子）；Padmanee Sharma（2004 相识→合作者→2014 结婚，继三子）——spouse+collaborator 双行；时间线勿倒置 |
| 家族癌症 | 母（淋巴瘤，他 10 岁时）与兄（前列腺癌 2005）病逝系 page.md 明载，可作动机注记，勿煽情化 |
| 在世留白 | 在世者：无卒日；relations=8 诚实值（实验室成员/学生 page.md 无具名记载，勿虚构补边） |
| 引语红线 | 仅 Vietnam 段有英文原话可引；其余全部转述 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| CTLA-4 | 细胞毒性 T 淋巴细胞抗原 4 | 抑制性共刺激分子（刹车） |
| PD-1 | 程序性细胞死亡蛋白 1 | Honjo 线（本篇仅对照提及） |
| immune checkpoint | 免疫检查点 | 治疗概念统称 |
| ipilimumab / Yervoy | 伊匹木单抗 | 2011 FDA 批准抗 CTLA-4 抗体 |
| T-cell receptor (TCR) | T 细胞抗原受体 | 1982 首批分离者之一 |
| metastatic melanoma | 转移性黑色素瘤 | ipilimumab 首个适应症 |
| HLA | 人类白细胞抗原 | Scripps 时期研究对象 |
| asparaginase | 天冬酰胺酶 | 博士论文对象 |

## 九、背景音乐选择

- **选定曲目**：**Ascension** — Alex-Productions（manifest 预分配）
- **匹配理由**："攀升/升华"贴合其从基础免疫学一路攀升到临床革命的弧线——1996 小鼠实验到 2011 FDA 批准再到 2018 诺奖，层层登高；曲式的推进感匹配"把刹车松开"的力量感。
- **本地路径**：music_audio/ 下 Alex-Productions Ascension 曲目（执行时按 curated_tracks.md 对应文件复制到本目录）。
