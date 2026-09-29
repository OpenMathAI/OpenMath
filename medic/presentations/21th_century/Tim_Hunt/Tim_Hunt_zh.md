# 医学家立传提示词（Tim Hunt）

> 本文件是 OpenMedic 项目 21 世纪诺贝尔生理学或医学奖 **2001 年得主 Tim Hunt（蒂姆·亨特）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/21th_century/Tim_Hunt/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Sir Richard Timothy "Tim" Hunt（1943-02-19 生于英格兰柴郡 Neston，在世）
- **气质关键词**：**细胞周期蛋白的发现者、海胆卵边的观察者、乐与好运的信徒**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 2001 条目，三人共享同一理由）：
  > "for their discoveries of key regulators of the cell cycle"（因他们发现细胞周期的关键调节因子）
  - 其个人专属部分（Nobel 官网口径，page.md 明载转引）：Hunt "is awarded for his discovery of cyclins, proteins that regulate the CDK function. He showed that cyclins are degraded periodically at each cell division, a mechanism proved to be of general importance for cell cycle control."——立传时先引共享理由，再引此段。
- **设计母题**：**周期涨落的蛋白（cyclin 的周期消长）**——凝胶上蛋白条带随分裂周期亮起又消隐的意象：以波浪式升降的条带/曲线作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Tim_Hunt/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/21th_century/Tim_Hunt/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Tim_Hunt_zh`、`VIDEO_NAME=Tim_Hunt_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Hunt 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | cell cycle regulation | 细胞周期调控 | cyclin 发现者，2001 诺奖核心 | 封面、核心页 |
| 1 | cyclin | 细胞周期蛋白 | 周期性合成并在分裂期被特异性降解 | 核心页 |
| 2 | protein synthesis | 蛋白质合成控制 | 兔网织红细胞血红蛋白合成、起始复合物 | 早年页 |
| 3 | biochemistry | 生物化学 | infobox Fields 明载 | 全篇 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Asher Korner | 对方 → 导师 | 剑桥生物化学系博士导师（1964 入其门下，兔网织红细胞血红蛋白合成论文，1968 获博士学位） |
| advisor-student | Hugh Pelham | Hunt → 学生 | infobox Doctoral students 与正文均明载 |
| advisor-student | Jonathon Pines | Hunt → 学生 | infobox Doctoral students 与正文均明载 |
| spouse | Mary Collins | 无向 | 1995 结婚，免疫学家（OIST 前教务长、QMUL Blizard Institute 院长），育二女 |
| co-honored | Leland H. Hartwell | 无向 | 2001 诺贝尔生理学或医学奖三人共享（发现细胞周期关键调节因子） |
| co-honored | Paul Nurse | 无向 | 2001 诺贝尔生理学或医学奖三人共享（发现细胞周期关键调节因子） |

**不入库但提示词可叙述**：Tony Hunter（长期同门/合作者，Korner 门下同事与 Cambridge 回剑桥后再合作）、Richard Jackson、Irving London（纽约实验室东家）、Nechama/Edward Kosower、Ellie Ehrenfeld（纽约合作者）、Andrew Murray（教科书合著者）、Vernon Ingram（一次讲演激发兴趣）——均为 page.md 明载人物但关系属短期合作/同门，不设独立边，由正文叙述承载。

## 五、配色方案 【人物专属】

- **气质**：明快、潮汐感、海边的偶然与必然
- **主色**：`#0E4D64`（海胆深青——Woods Hole 夏日的海）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeCyclin` 细胞周期蛋白 — 深青 `#0E4D64`
  - `badgeCycle` 细胞周期调控 — 青绿 `#0E7C7B`
  - `badgeSynth` 蛋白质合成 — 苔绿 `#175E54`
  - `badgeSea` 海洋模式生物 — 琥珀 `#C07A2A`
- **背景母题**：凝胶条带随周期升降的波浪曲线，呼应「cyclin 的周期消长」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 细胞周期蛋白的发现者 / Tim Hunt 1943– + 四色 badge + 右上头像 + 国籍行（United Kingdom）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1943-02-19 Neston、Clare College 剑桥、
    博士导师 Asher Korner、ICRF/London Research Institute、Francis Crick Institute 荣休组长、诺奖 2001）
03  核心贡献概览 — cyclin / MPF / 蛋白质合成控制 / 短线性基序
04  牛津少年 (1943–1961) — Dragon School 的 Gerd Sommerhoff 启蒙、Magdalen College School
05  剑桥与 Korner 门下 (1961–1966) — Clare College 自然科学、生物化学系、Tony Hunter 同门
06  纽约一年与血红蛋白 (1966–1968) — Albert Einstein College of Medicine、Irving London、
    谷胱甘肽与 RNA 对合成的抑制；1968 博士
07  Woods Hole 的夏天 — Marine Biological Laboratory、Spisula 浪蛤与 Arbacia 海胆、透明胚胎
08  发现 cyclin (1982)（核心贡献页）— 海胆卵、放射性甲硫氨酸标记、10 分钟取样、
    有丝分裂前升高随后消失、命名 "cyclin"、Cell 1983 发表
09  cyclin 与 CDK：MPF 的拼图 — cyclin+CDK 组成 MPF；Masui & Markert 1971 先行鉴定 MPF；Xenopus 验证
10  蛋白质合成的控制 — 40S 亚基先结合起始 tRNA、eIF-2 磷酸化、thioredoxin 意外角色（FRS 证书口径）
11  ICRF 岁月与短线性基序 (1990–) — ICRF/London Research Institute、1990 提出 short linear motifs、
    Clare Hall 实验室至 2010、Francis Crick Institute 荣休组长
12  荣誉与认可 — EMBO 1978、FRS 1991（证书引语可引）、NAS 外籍院士 1999、Nobel 2001、
    Royal Medal 2006、封爵 2006、HonFRSE 2003
13  2015 年风波 — 首尔世界科学记者大会即兴祝酒引发的争议与辞职（须按陷阱表口径客观三段式）
14  乐与好运 — "having fun and being lucky" 的科学观、把权力交给年轻人；遗产与结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 博士年份 | infobox 论文标注 (1969)、正文 "awarded in 1968"——**以正文 1968 为准**，陷阱表记录双值 |
| cyclin 时间线 | 发现于 1982 年 7 月（Woods Hole），发表于 1983 年 *Cell*——两年份勿混写 |
| MPF 归属 | MPF 1971 年由 **Yoshio Masui 与 Clement Markert** 先行鉴定；Hunt 的工作是 cyclin 与 cyclin 降解，cyclin+CDK 组成 MPF 是后续整合——勿写"Hunt 发现 MPF" |
| cyclin 命名 | "cyclin" 由 Hunt 根据其周期性消长命名；后续发现 cyclin 持续合成、于有丝分裂被特异性蛋白水解 |
| 模式生物 | 发现用的是 *Arbacia punctulata* 海胆（后亦在 *Lytechinus pictus* 海胆与 *Spisula* 浪蛤证实）；勿误写海星/青蛙为主发现体系（Xenopus 是后续验证） |
| 共享理由 | 官方理由三人同一句 "for their discoveries of key regulators of the cell cycle"；其个人段（cyclin 发现与周期性降解）为 Nobel 官网个人 citation，两者分层引用 |
| 2015 风波 | 首尔即兴祝酒言论、社交媒体反弹、辞去 UCL 名誉教授及其他职位、本人道歉并称"in jest/被断章取义"——如立传处理，必须客观三段式（言论/反弹/道歉与辩护，含"反弹是否过当"的既有争议描述），不得渲染或站队 |
| 父亲之谜 | 父 Richard William Hunt 在 BBC Bush House 工作而实职不明（"most likely in intelligence"是维基措辞）——照页面措辞，勿坐实 |
| 在世者生卒 | 仅生年 1943-02-19，无卒年——封面用 1943– 开放区间 |
| FRS 证书引语 | 1991 FRS 当选证书长段为 page.md 明载可引原文；引语红线：仅此段与 Nobel 个人 citation 可作原文引用 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| cyclin | 细胞周期蛋白 | Hunt 命名；周期性合成、分裂期被特异性降解 |
| cyclin-dependent kinase (CDK) | 周期蛋白依赖激酶 | 与 cyclin 结合成 MPF |
| maturation-promoting factor (MPF) | 促成熟因子 | 1971 Masui & Markert 先行鉴定 |
| reticulocyte | 网织红细胞 | 血红蛋白合成研究体系 |
| sea urchin | 海胆 | *Arbacia punctulata*，发现 cyclin 的体系 |
| short linear motif | 短线性基序 | 1990 年 Hunt 提出概念 |
| proteolysis | 蛋白水解 | cyclin 分裂期降解机制 |
| eIF-2 | 起始因子 eIF-2 | 磷酸化调控蛋白质合成 |
| Royal Medal | 皇家奖章 | 2006，"discovering a key aspect of cell cycle control" |
| Knight Bachelor | 下级勋位爵士 | 2006 生日授勋 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**PAST**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Hunt 的叙事带着旧日实验台的温度——海胆卵、夏季课程、凝胶上的放射性条带；"PAST" 的怀旧质感匹配其"乐与好运"的回望式科学人生，也呼应他从 1960 年代蛋白质合成一路走到 cyclin 的研究脉络。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/21th_century/Tim_Hunt/PAST.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
