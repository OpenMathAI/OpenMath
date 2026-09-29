# 医学家立传提示词（Michael Stuart Brown）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1985 年得主 Michael Stuart Brown（迈克尔·斯图尔特·布朗）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Michael_Stuart_Brown/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Michael Stuart Brown（1941-04-13 生于美国纽约布鲁克林，在世）
- **气质关键词**：**LDL 受体的发现者、受体介导胞饮的阐明者、他汀时代的奠基人**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1985 条目，与 Goldstein 共享同一理由）：
  > "for their discoveries concerning the regulation of cholesterol metabolism"（因他们发现胆固醇代谢的调节机制）
- **设计母题**：**细胞门口的 LDL 受体**——LDL 颗粒停靠有被小窝、受体介导内吞的意象：以颗粒入港的图案作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Michael_Stuart_Brown/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；第 0/1/2/3 步按 medic 路径执行：页面已在 `medic/presentations/pages/20th_century/Michael_Stuart_Brown/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Michael_Stuart_Brown_zh`、`VIDEO_NAME=Michael_Stuart_Brown_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | cholesterol metabolism | 胆固醇代谢调节 | LDL 受体与家族性高胆固醇血症，1985 诺奖核心 |
| 1 | cell biology | 细胞生物学 | 受体介导内吞、有被小窝与小泡 |
| 2 | genetics | 遗传学 | infobox field_of_work；FH 基因突变谱 |
| 3 | biochemistry | infobox field_of_work | SREBP 通路与蛋白异戊二烯化 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Joseph L. Goldstein | 无向 | UT 达拉斯同事、终身研究搭档（LDL 受体共同发现者；库内 stub id=5736，batch-29 回填其 QID Q271424） |
| advisor-student | Xiaodong Wang | Brown/Goldstein → 受训者 | 1993 与 Michael Briggs 纯化 SREBP 的 trainee（page.md 明载） |
| spouse | Alice Lapin | 无向 | 1964 结婚，育二子女 |

**在世者关系少为诚实值**（5 条）：page.md 未载 Brown 的博士导师与多数受训者姓名（Michael Briggs 未链接不入库）——Review 勿补造边。**不入库但提示词可叙述**：父母 Evelyn 与 Harvey（纺织推销员，家世叙述）；Anderson/Basu/Südhof 等 JBC/Cell 论文合作者（论文合作不建边；Südhof 后获 2013 诺奖可一句带过）；statins 他汀药（成果应用非人物）。

## 五、配色方案 【人物专属】

- **气质**：达拉斯的沉稳、代谢通路的全景、临床转化的踏实
- **主色**：`#7E2A1E`（深赭红——动脉与血脂的警醒之色）+ 香槟金诺奖色
- **badge 四分类色**：`badgeLDL` LDL 受体 深赭红 `#7E2A1E`；`badgeEndo` 受体介导胞饮 深蓝 `#1E4E79`；`badgeSREBP` SREBP 通路 青绿 `#0E7C7B`；`badgeStatin` 他汀时代 琥珀 `#C07A2A`
- **背景母题**：LDL 颗粒停靠有被小窝的入港图案，呼应「细胞门口的受体」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — LDL 受体的发现者 / Michael Stuart Brown 1941– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1941-04-13 布鲁克林、宾大 1962/MD 1966、
    UT Southwestern Moncrief 讲席/Regental 教授、诺奖 1985）
03  核心贡献概览 — LDL 受体 / 家族性高胆固醇血症 / 受体介导胞饮 / SREBP 通路
04  布鲁克林与费城 (1941–1966) — 犹太家庭、Cheltenham 高中、宾大 1962、
    宾大医学院 MD 1966
05  达拉斯会师 — UT 健康科学中心（今 UT Southwestern）、与 Goldstein 的终生搭档
06  1974：家族性高胆固醇血症 — 杂合子显性遗传机制（Science 1974）；FH 病理之谜
07  LDL 受体的发现（核心贡献页）— 人体细胞表面的 LDL 受体从血流提取胆固醇；
    受体不足即 FH 的病理根基
08  受体介导胞饮（核心贡献页）— 有被小窝/有被小泡的内吞机器——细胞生物学
    的基本原理之一；受体循环往返
09  他汀时代 — 发现直接催生 statins：全美 1600 万使用者的最常用处方药；
    新联邦指南三倍扩容（page.md 口径）
10  SREBP 通路 (1993–) — 受训者 Xiaodong Wang 与 Michael Briggs 纯化 SREBP；
    膜结合转录因子的固醇调控蛋白酶解、SCAP/Insig——胆固醇稳态的复杂机器
11  蛋白质异戊二烯化 — 脂质修饰（prenylation）与癌症的关联线
12  荣誉与认可 — Wieland 1974、Pfizer 1976、Passano 1978、Lounsbery 1979、
    NAS 1980、Gairdner 1981、AAAS 1981、Horwitz 1984、Lasker/Allan/Nobel 1985、
    国家科学奖章 1988、ForMemRS 1991、Kober 2002、Albany 2003 等
13  职务与荣誉讲席 — Moncrief 胆固醇与动脉硬化研究杰出讲席、
    Regental Professor、Paul J. Thomas 医学讲席
14  遗产与结尾 — 从受体到他汀到 SREBP：胆固醇生物学的完整闭环；在世持续研究
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 双人组结构 | Brown 与 Goldstein 自 1970s 起在 UT 达拉斯搭档、论文几乎全部合署——1985 共享诺奖；两人侧重不分工叙述（ LDL 受体/内吞/SREBP 均共同成果），勿生造侧重差异 |
| Goldstein 归属 | Goldstein 是 batch-29 成员——本 yaml 用库内 stub id=5736（其本人 yaml 将回填 QID Q271424）；建 colleague+co-honored 双边 |
| 受训者边界 | 1993 SREBP 纯化的 trainees 是 **Xiaodong Wang 与 Michael Briggs**——Wang 有 wiki 链接入库（学生边），Briggs 无链接不入库；合称时注意两人 |
| Südhof 提及 | 论文合作者列表多次出现 Südhof（2013 诺奖）——仅论文合作叙述，不建边 |
| 他汀数据 | "1600 万美国人使用/全美最常用处方药/新指南三倍扩容"为 page.md 撰写时点口径——立传照引并注明为页面时点数据，勿更新为当代数字 |
| 页面瑕疵 | 正文第 44 行有残断行 "B"（维基源文瑕疵）；引用时勿带入 |
| 在世者生卒 | 仅生年 1941-04-13，无卒年——封面用 1941– 开放区间 |
| 姓名 | 全名 Michael Stuart Brown；Nobel 官网口径 Michael S. Brown；yaml/manifest 用 Michael Stuart Brown |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| LDL receptor | 低密度脂蛋白受体 | 获奖核心发现 |
| familial hypercholesterolemia | 家族性高胆固醇血症 | FH；受体不足病理 |
| receptor-mediated endocytosis | 受体介导胞饮 | 细胞生物学基本原理 |
| coated pit / coated vesicle | 有被小窝 / 有被小泡 | 内吞的结构基础 |
| statin | 他汀类药物 | LDL 发现的转化成果 |
| SREBP | 固醇调节元件结合蛋白 | 1993 起的通路主角 |
| SCAP / Insig | SREBP 切割激活蛋白 / Insig | 胆固醇稳态机器组件 |
| prenylation | 蛋白质异戊二烯化 | 脂质修饰与癌症 |
| HMG CoA reductase | HMG-CoA 还原酶 | 他汀靶酶 |
| UT Southwestern | 德州大学西南医学中心 | 终身研究根据地 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Lonesome**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**： Brown 的叙事是一部沉稳的长跑——从布鲁克林到宾大到达拉斯，与 Goldstein 双人组数十年如一日的并肩；"Lonesome" 的悠远对应基础科学长路上的寂寞与专注，以及成果最终惠及亿万患者的辽阔回响。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Michael_Stuart_Brown/Lonesome.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
