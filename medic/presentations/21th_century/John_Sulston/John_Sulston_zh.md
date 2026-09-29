# 医学家立传提示词（John Sulston）

> 本文件是 OpenMedic 项目 21 世纪诺贝尔生理学或医学奖 **2002 年得主 John Sulston（约翰·爱德华·苏尔斯顿）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/21th_century/John_Sulston/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Sir John Edward Sulston（1942-03-27 生于英格兰白金汉郡 Fulmer ~ 2018-03-06，享年 75 岁），CH FRS MAE，2001 年受封 Knight Bachelor
- **气质关键词**：**细胞谱系的绘制者、线虫基因组的开拓者、人类基因组的公共捍卫者**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 2002 条目，Brenner/Horvitz/Sulston 三人共享）：
  > "for their discoveries concerning 'genetic regulation of organ development and programmed cell death '"（因其关于器官发育与细胞程序性死亡的遗传调控的发现）
- **设计母题**：**一张画到每一个细胞的谱系图（complete cell lineage）**——线虫 *C. elegans* 从受精卵到成体 959 个体细胞的每一次分裂都被记录在案，用「分叉的细胞树」作背景母题：纤细的分叉线从单点生长为完整有机体。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/John_Sulston/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/21th_century/John_Sulston/`（世纪目录一律 `21th_century`，肖像见 images.txt）。Makefile 复制后设 `MAIN=John_Sulston_zh`、`VIDEO_NAME=John_Sulston_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Sulston 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | developmental genetics | 发育遗传学 | *C. elegans* 全细胞谱系与发育突变研究，2002 诺奖核心 | 核心页 |
| 1 | programmed cell death | 细胞程序性死亡（凋亡） | 诺奖获奖理由核心词（与 Horvitz/Brenner 共享） | 核心页 |
| 2 | genomics | 基因组学 | *C. elegans* 基因组（1998，首个全测序动物）与人类基因组 | 测序页 |
| 3 | molecular biology | 分子生物学 | 博士为核苷酸化学，后转入分子发育生物学 | 早年页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Colin Reese | 对方 → 导师 | 剑桥大学博士导师（1966，核苷酸化学），亦安排其赴 Salk 博士后 |
| advisor-student | Leslie Orgel | 对方 → 博士后合作者 | Salk 研究所博士后（1966-1969），经其引见结识 Crick 与 Brenner |
| colleague | Sydney Brenner | 无向 | Brenner 招其回剑桥 MRC LMB 研究 *C. elegans* 神经生物学（库内 id=3873） |
| co-honored | Sydney Brenner | 无向 | 2002 诺贝尔生理学或医学奖三人共享 |
| colleague | H. Robert Horvitz | 无向 | MRC LMB 合作同事，2002 同届共享诺奖 |
| co-honored | H. Robert Horvitz | 无向 | 2002 诺贝尔生理学或医学奖三人共享 |
| spouse | Daphne Edith Bate | 无向 | 剑桥研究助理，1966 结婚后同赴美国，育一女 Ingrid 与一子 Adrian |

**不入库但提示词可叙述**：Francis Crick（仅"经 Orgel 引见结识"，一面之缘非持续关系）；父亲 Arthur Edward Aubrey Sulston（圣公会牧师）与母亲 Josephine Muriel Frearson； sister Madeleine；Alexander Todd（面试其入剑桥化学系）。

## 五、配色方案 【人物专属】

- **气质**：线虫的透亮、谱系图的秩序、公共数据的开放
- **主色**：`#145C4E`（深松绿——显微镜下线虫与基因组测序图谱）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeCell` 细胞谱系 — 深松绿 `#145C4E`
  - `badgeGenome` 基因组测序 — 深蓝 `#1E4E79`
  - `badgeOpen` 开放科学 — 赭金 `#B07D2B`
  - `badgeHon` 荣誉传承 — 暗红 `#7A2430`
- **背景母题**：从单一受精卵分叉生长的细胞树（细线分叉图），四种透明度错落。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 细胞谱系的绘制者 / John Sulston 1942–2018 + 四色 badge + 右上头像 + 国籍行（United Kingdom）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Fulmer 出身、剑桥 Pembroke 学院、MRC LMB/
    Sanger Centre/曼彻斯特任职、诺奖 2002、核心领域）
03  核心贡献概览 — 细胞谱系 / 凋亡与器官发育 / 线虫基因组 / 人类基因组
04  Fulmer 神童 (1942–1963) — 牧师家庭、解剖动植物的兴趣、Merchant Taylors' 奖学金、Pembroke 化学学位
05  剑桥博士：核苷酸化学 (1963–1966) — Colin Reese 门下，Todd 面试，寡核糖核苷酸合成
06  Salk 博士后与转折 (1966–1969) — Orgel 引见 Crick 与 Brenner，从化学转向生物学
07  回到剑桥 LMB：线虫神经元图谱 (1969–1974) — Brenner 招募、*C. elegans* 神经系统完整图谱（核心页）
08  全细胞谱系 (1974–1983) — 追踪每一个胚胎细胞的分裂命运，1983 年论文，首个细胞起源全部已知的生物
09  凋亡与器官发育的遗传调控（核心贡献页）— 与 Brenner/Horvitz 共享的 2002 诺奖理由
10  线虫基因组 (1989–1998) — 物理图谱、与华盛顿大学圣路易斯合作，首个全基因组测序的动物
11  Sanger Centre 与人类基因组 (1992–2000) — 以 Fred Sanger 命名中心主任、工作草图完成、反对基因专利
12  2002 诺奖：三人共享 — 与 Brenner/Horvitz 同出 MRC LMB，获奖理由逐字呈现
13  荣誉与认可 — FRS 1986、Darwin Medal 1996、爵士 2001、Companion of Honour 2017 等
14  遗产与结尾 — The Common Thread、开放科学信念、Sulston 实验室命名 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 姓名形式 | 全名 Sir John Edward Sulston，**yaml/入库用 manifest 形式 "John Sulston"**；封面可写 John Sulston 1942–2018 |
| 2002 三人共享 | 与 Sydney Brenner、H. Robert Horvitz 共享；获奖理由是三人共同一句（"genetic regulation of organ development and programmed cell death"），勿拆成各半 |
| 三人同源 | 三人皆出自剑桥 MRC 分子生物学实验室（LMB）；Sulston 与 Brenner/Horvitz 均"在 LMB 合作过"（page.md 明载），colleague 边有据 |
| 博士导师 | Colin Reese（infobox/正文一致，1966 年核苷酸化学博士）；**勿与面试其入系的 Alexander Todd 混淆**——Todd 只是面试者非导师 |
| 博士后关系 | Salk 研究所 1966-1969 与 Leslie Orgel 合作（Reese 安排）；Orgel 是博士后合作者，advisor-student 边以"博士后合作者"note 表述，勿写成博士导师 |
| Crick 边界 | Orgel 把 Sulston 引见给 Crick 与 Brenner——仅"结识"，勿写 Crick 指导或合作 |
| 首个全测序动物 | 1998 年 *C. elegans* 基因组发表（与华盛顿大学圣路易斯合作），是**首个完成全基因组测序的动物**；人类基因组 2000 年是"工作草图"完成，Sulston 同年从 Sanger Centre 主任卸任 |
| 死因与年龄 | 2018-03-06 死于胃癌（stomach cancer），享年 75 岁 |
| 反基因专利立场 | 称从基因组研究牟利"totally immoral and disgusting"（page.md 英文原文明载，可引原文+译文）；主张药品（Tamiflu/Roche）专利限制妨碍患者 |
| 政治敏感禁写 | 2010-2012 为 Julian Assange 担保一事虽为 page.md 实载，属政治敏感，**立传中整体回避**；Humanists UK 与 2003 人文主义宣言可一句客观带过 |
| 荣誉年份 | FRS 1986、EMBO 1989、Beadle 2000、爵士+Edinburgh Medal 2001、Dan David+Robert Burns 人道奖+Gairdner 2002、Golden Plate 2004、CH 2017（Birthday Honours）、剑桥化学校友奖章 2017-10-23——年份勿串 |
| 在库对手方 | Brenner（id=3873）已在库；Horvitz 由 med21-batch-01 以 "H. Robert Horvitz" 入库——对手方名一律用此形式 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| cell lineage | 细胞谱系 | *C. elegans* 每个细胞的分裂与命运图谱 |
| programmed cell death | 细胞程序性死亡 | 获奖理由核心词，即凋亡（apoptosis） |
| Caenorhabditis elegans | 秀丽隐杆线虫 | 模式生物，斜体书写 |
| genome sequencing | 基因组测序 | 线虫（1998）与人类（草图 2000） |
| Sulston score | Sulston 分数 | 测序数据质量评估指标 |
| MRC Laboratory of Molecular Biology | MRC 分子生物学实验室 | 剑桥 LMB，三人共同工作地 |
| Sanger Centre | 桑格中心 | 今 Wellcome Trust Sanger Institute，以 Fred Sanger 命名 |
| oligoribonucleotide | 寡核糖核苷酸 | 博士研究方向 |
| Companion of Honour | 功绩勋章同伴（CH） | 2017 年获授 |
| open access | 开放获取 | 公共资助数据应免费公开的立场 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**SEA**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Sulston 的一生如海岸般开阔而克制——从线虫一个细胞的分裂追踪到人类基因组草图，SEA 的沉静与绵延对应他把微观谱系铺展成公共财富的事业；其晚年为开放科学与反对基因私有化的奔走，也如潮汐般持之以恒。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/21th_century/John_Sulston/SEA.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
