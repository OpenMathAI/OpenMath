# 医学家立传提示词（Richard Axel）

> 本文件是 OpenMedic 项目 21 世纪诺贝尔生理学或医学奖 **2004 年得主 Richard Axel（理查德·阿克塞尔）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/21th_century/Richard_Axel/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Richard Axel（1946-07-02 生于纽约市，**在世**），美国分子生物学家，哥伦比亚大学 University Professor、HHMI 研究员
- **气质关键词**：**基因转移的工程师、千种气味受体的破译者、诺奖门生的园丁**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 2004 条目，Axel/Buck 两人共享）：
  > "for their discoveries of odorant receptors and the organization of the olfactory system"（因其发现气味受体并阐明嗅觉系统的组织方式）
- **设计母题**：**一条受体基因对应一种气味的对应律（one receptor, one neuron）**——约 1000 种受体基因、每个嗅觉神经元只表达其中一种、同种受体的信号汇聚于一个嗅小球；用「一千条发光的通道汇入单一节点」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Richard_Axel/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/21th_century/Richard_Axel/`（世纪目录一律 `21th_century`，肖像见 images.txt）。Makefile 复制后设 `MAIN=Richard_Axel_zh`、`VIDEO_NAME=Richard_Axel_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。**在世者注意**：生卒页只写出生年，无"享年"。

## 三、研究领域梳理 + 入库 【人物专属】

**Axel 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | neuroscience | 神经科学 | 嗅觉系统如何映射气味，2004 诺奖核心 | 核心页 |
| 1 | olfaction | 嗅觉 | 气味受体克隆与嗅觉系统组织 | 核心页 |
| 2 | molecular biology | 分子生物学 | 共转化/转染技术与基因转移 | 技术页 |
| 3 | genetics | 遗传学（基因转移） | "Axel patents" 共转化专利族 | 技术页 |
| 4 | immunology | 免疫学 | CD4 与 HIV 感染关联的最早发现之一 | 免疫页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Linda B. Buck | 无向 | 2004 诺贝尔生理学或医学奖共享（气味受体与嗅觉系统的组织） |
| advisor-student | Linda B. Buck | Axel → 博士后合作者 | 哥伦比亚大学博士后，1991 年合作克隆气味受体 |
| advisor-student | David J. Anderson | Axel → 学生 | infobox Notable students 明载 |
| advisor-student | Catherine Dulac | Axel → 学生 | infobox Notable students 明载 |
| advisor-student | David Julius | Axel → 学生 | infobox Notable students 明载，2021 诺奖得主 |
| advisor-student | Richard Scheller | Axel → 学生 | infobox Notable students 明载 |
| advisor-student | Leslie B. Vosshall | Axel → 学生 | infobox Notable students 明载 |
| advisor-student | Vanessa Ruta | Axel → 学生 | infobox Notable students 明载 |
| advisor-student | Bianca Jones Marlin | Axel → 学生 | infobox Notable students 明载 |
| advisor-student | Fan Wang | Axel → 学生 | infobox Notable students 明载（神经科学家） |
| spouse | Cornelia Bargmann | 无向 | 现任妻子，嗅觉研究先驱科学家 |
| spouse | Ann Axel | 无向 | 前妻，哥伦比亚大学医学中心社工 |

**门生佐证（正文明载）**："mentored many leading scientists"，7 位受训者当选 NAS 院士、6 位关联 HHMI——9 位学生边有 infobox+正文双重支撑，**非噪声，勿删**。**不入库但提示词可叙述**：Saul J. Silverstein 与 Michael H. Wigler（共转化的共同发现者，技术合作者，本批保守口径未入库）；父母为波兰犹太移民。

## 五、配色方案 【人物专属】

- **气质**：纽约的冷峻、基因工程的前卫、嗅觉地图的神秘
- **主色**：`#4A235A`（深紫——嗅觉神经与大脑映射的神秘感）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeOdor` 气味受体 — 深紫 `#4A235A`
  - `badgeGene` 基因转移 — 深蓝 `#1E4E79`
  - `badgeImmune` 免疫学 — 青灰 `#0E7490`
  - `badgeMentor` 门生传承 — 琥珀 `#B07D2B`
- **背景母题**：一千条细发光通道汇入单一节点的辐射状图案。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 千种气味受体的破译者 / Richard Axel b.1946 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生、布鲁克林成长、Stuyvesant/哥伦比亚/约翰斯·霍普金斯、
    哥伦比亚 University Professor + HHMI、诺奖 2004、核心领域）
03  核心贡献概览 — 共转化技术 / 气味受体克隆 / 一受体一神经元 / 门生谱系
04  布鲁克林与 Stuyvesant (1946–1967) — 波兰犹太移民之子、1963 届同窗、哥伦比亚 BA
05  霍普金斯 MD 与"不做临床"的承诺 (1967–1971) — 自认不适合行医、向系主任承诺不执业
06  回到哥伦比亚 (1971–1978) — 从起步到 1978 正教授
07  共转化技术与 Axel patents（技术贡献页）— 与 Silverstein/Wigler 合作、1980 申报/1983 授权、
    曾为哥伦比亚年创近亿美元、2000 到期
08  CD4 与 HIV — 实验室最早把 CD4 与 HIV 感染关联起来的实验室之一
09  1991：克隆气味受体（核心贡献页）— 与 Buck 用大鼠 DNA、约 1000 个受体基因、G 蛋白偶联受体家族
10  一受体一神经元（核心页）— 每个嗅觉神经元只表达一种受体蛋白、信号汇聚于单一嗅小球
11  2004 诺奖：与 Buck 共享 — 获奖理由逐字呈现、Buck 是其实验室前博士后
12  门生与传承 — David Julius（2021 诺奖）、Catherine Dulac、Leslie Vosshall 等；7 位 NAS 院士
13  荣誉与认可 — NAS 1983、Lounsbery 1989、Perl-UNC 2002、Gairdner 2003、Double Helix 2007、ForMemRS 2014
14  遗产与结尾 — 嗅觉研究的现代版图 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 姓名与在世口径 | **yaml/入库用 manifest 形式 "Richard Axel"**；1946-07-02 生于纽约，**在世**——封面写 b.1946，不得写卒年或享年 |
| 2004 共享 | 与 Linda B. Buck 共享；Buck 是其实验室前博士后（page.md 明载）——axel→buck 的 advisor-student（博士后）+co-honored 双边并行，勿合并 |
| 9 位学生边 | infobox Notable students 9 人 + 正文"mentored many leading scientists / 七位 NAS"双重明载——全部入库，Review 勿当噪声删减 |
| Epstein 事件禁写 | 与 Jeffrey Epstein 的交往及 2026-02 辞去 Zuckerman 研究所联席主任、退出 HHMI 事件虽为 page.md 实载，属敏感负面事件，**立传中整体回避**，不展开细节、不引用相关评价 |
| infobox 噪声 | infobox "Known for" 行含 "friend of Jeffrey Epstein"——**该短语禁入封面/正文**，Known for 只写 olfaction |
| 国籍裁定 | metadata nationalities 为 United States+Sweden 双值，page.md 通篇 "American"——**以 page.md 为准，仅入库 United States**（yaml 已如此，Review 勿按 metadata 补 Sweden） |
| 两条婚姻 | 现任妻 Cornelia Bargmann（科学家，嗅觉先驱）；前妻 Ann Axel（社工）——两条 spouse 边并行，note 已区分，勿混 |
| 学位链 | BA 哥伦比亚 1967 → MD 约翰斯·霍普金斯 1971——**MD 之后无 PhD**，勿写"博士"；1978 哥伦比亚正教授 |
| 共转化合作者 | 共转化技术是 Axel 与 Saul J. Silverstein、Michael H. Wigler 共同发现——三人并列，勿独归 Axel；专利 1980 年 2 月申报、1983 年 8 月授权、2000 年 8 月到期 |
| 数量表述 | 约 1000 个气味受体基因（大鼠 DNA 估算）；专利曾为哥伦比亚"（一度）年创近 1 亿美元"许可收入——两数字勿混淆 |
| 学历轶事 | 高中因身高打篮球、1963 届 Stuyvesant 同窗含 Ron Silver 等——可用作身份页调剂，勿喧宾夺主 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| odorant receptor | 气味受体 | 获奖理由核心词 |
| olfactory system | 嗅觉系统 | 获奖理由另一半 |
| G protein-coupled receptor | G 蛋白偶联受体 | 气味受体所属家族 |
| olfactory receptor neuron | 嗅觉受体神经元 | 每个只表达一种受体蛋白 |
| glomerulus | 嗅小球 | 同种受体信号汇聚处 |
| cotransformation | 共转化 | 与 Silverstein/Wigler 共同发现 |
| transfection | 转染 | 外源 DNA 导入宿主细胞 |
| Axel patents | Axel 专利族 | 1983-2000 有效，共转化基础专利 |
| CD4 | CD4 受体 | HIV 的细胞受体 |
| University Professor | （哥伦比亚）大学教授 | 哥伦比亚最高教职 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Daylight**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Axel 的贡献是把"看不见的气味"变成"看得见的地图"——千种受体基因被逐一照亮，如同破晓时分天光渐亮；Daylight 的明快对应其研究从基因转移到嗅觉版图的豁然开朗，也对应其门生群星闪耀的传承气象。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/21th_century/Richard_Axel/Daylight.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
