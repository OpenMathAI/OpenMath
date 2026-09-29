# 医学家立传提示词（Paul Nurse）

> 本文件是 OpenMedic 项目 21 世纪诺贝尔生理学或医学奖 **2001 年得主 Paul Nurse（保罗·马斯顿·纳斯）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/21th_century/Paul_Nurse/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Sir Paul Maxime Nurse（1949-01-25 生于英格兰诺里奇，在世；英国遗传学家）
- **气质关键词**：**cdc2 基因的捕获者、人类 CDK1 的破译者、皇家学会与克里克研究所的掌舵人**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 2001 条目，三人共享同一理由）：
  > "for their discoveries of key regulators of the cell cycle"（因他们发现细胞周期的关键调节因子）
  - page.md 正文另有表述 "for their discoveries of protein molecules that control the division of cells"——引用诺奖理由以 citation json 为准。
- **设计母题**：**基因开关的磷酸化循环（CDK 的磷酸化开合）**——磷酸基团的加上/卸下驱动周期闸门的意象：以双向箭头环（激活/失活交替）作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Paul_Nurse/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/21th_century/Paul_Nurse/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Paul_Nurse_zh`、`VIDEO_NAME=Paul_Nurse_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Nurse 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | cell cycle regulation | 细胞周期调控 | cdc2/CDK1，2001 诺奖核心 | 封面、核心页 |
| 1 | genetics | 遗传学 | infobox Fields 明载；裂殖酵母遗传筛选 | 核心页 |
| 2 | cell biology | 细胞生物学 | infobox Fields 明载 | 全篇 |
| 3 | cancer research | 癌症研究 | ICRF/构成 Cancer Research UK 的机构主线 | 机构页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Anthony P. Sims | 对方 → 导师 | infobox Doctoral advisor 明载（东英吉利大学 1973 博士，Candida utilis 氨基酸池研究） |
| advisor-student | Alison Woollard | Nurse → 学生 | infobox Doctoral students 明载 |
| colleague | Murdoch Mitchison | 无向 | 1973–1979 在爱丁堡大学 Mitchison 实验室做博士后六年 |
| colleague | Melanie Lee | 无向 | 其博士后研究员，1987 共同在人类中鉴定 cdc2 同源基因 CDK1 |
| spouse | Anne Teresa Talbott | 无向 | 1971 结婚，育二女 Sarah 与 Emily |
| co-honored | Leland H. Hartwell | 无向 | 2001 诺贝尔生理学或医学奖三人共享（发现细胞周期关键调节因子） |
| co-honored | Tim Hunt | 无向 | 2001 诺贝尔生理学或医学奖三人共享（发现细胞周期关键调节因子） |

**不入库但提示词可叙述**：Turi King（2023 帮其追溯生父，一次性事件）；Arnold Levine / Marc Tessier-Lavigne / Martin Rees / Venki Ramakrishnan（均为职务交接前后任，非实质关系）；Gordon Brown（2020 Nature 联署信共同作者，一次性）。

## 五、配色方案 【人物专属】

- **气质**：缜密、纵贯、学术舵手的开阔
- **主色**：`#175873`（皇家深蓝——皇家学会与克里克研究所的沉稳）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeCdc2` 细胞周期调控 — 深蓝 `#175873`
  - `badgeGen` 遗传学 — 青绿 `#0E7C7B`
  - `badgeCell` 细胞生物学 — 苔绿 `#175E54`
  - `badgeLead` 机构掌舵 — 琥珀 `#C07A2A`
- **背景母题**：磷酸化开合的双向箭头环，呼应「CDK 的激活/失活循环」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — cdc2 的捕获者 / Paul Nurse 1949– + 四色 badge + 右上头像 + 国籍行（United Kingdom）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1949-01-25 诺里奇、伯明翰 BSc 1970、
    东英吉利大学 PhD 1973、皇家学会两任会长、洛克菲勒大学第 9 任校长、诺奖 2001）
03  核心贡献概览 — cdc2 / 人类 CDK1 / CDK 磷酸化调控 / 机构领导
04  身世之谜 (1949–) — 母亲 18 岁北上诺里奇隐匿生育、外祖母假扮母亲、"姐姐"实为生母、
    50 多岁因绿卡申请调出完整出生证明才知情、2023 Turi King 追溯生父（客观陈述，尊重语气）
05  求学 (1968–1973) — 伯明翰大学生物学 BSc 1970、东英吉利大学 PhD 1973（Candida utilis）
06  博士后岁月 (1973–1979) — 伯尔尼/爱丁堡/萨塞克斯；爱丁堡 Mitchison 实验室六年
07  发现 cdc2 (1976–)（核心贡献页）— 裂殖酵母 cdc2 基因、控制 G1→S 与 G2→M 两道转换
08  人类 CDK1 (1987)（核心贡献页）— 与博士后 Melanie Lee 鉴定人类同源基因；CDK 磷酸化开合机制
09  机构掌舵 I：ICRF/Cancer Research UK — 1984 加入、1988–牛津微生物学系主任、
    1993 研究主任、1996 总主任
10  机构掌舵 II：洛克菲勒与克里克 — 洛克菲勒大学校长 2003–2011；2011 UKCMRI（今 Francis Crick
    Institute）首任所长兼 CEO
11  皇家学会 — 2010–2015 第 61 任会长；2025-12-01 就任第 64 任会长（现任）；布里斯托大学校监 2017–
12  荣誉与认可 — EMBO 1987、FRS 1989、Lasker 1998、封爵 1999、Royal Medal 1995、
    Copley Medal 2005、Order of Merit 2022、Companion of Honour 2022（年份勿串）
13  好科学家的标准 — "passion to know the answer"、智识诚实/自我批评/开放/怀疑；
    《What Is Life?》2020/2021 两版
14  遗产与结尾 — 从酵母到人类：细胞周期研究的统一框架
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| cdc2 vs CDK1 | cdc2 是**裂殖酵母基因**（1976 起鉴定），1987 年与博士后 Melanie Lee 在人类中发现同源基因 CDK1——两步两物种勿混写为一次完成 |
| Melanie Lee 定位 | Lee 是 Nurse 的**博士后研究员**（postdoctoral researcher），非博士生——用 colleague 边承载，勿写师生 |
| 博士导师 | infobox 载 Anthony P. Sims；metadata.json 亦同——师承边只此一条；东英吉利大学（非伯明翰）1973 博士 |
| 皇家学会两任 | 第 61 任（2010-12-01 继 Martin Rees，至 2015，继任 Ramakrishnan）；2025-12-01 再就任第 64 任（表格 "61st and 64th"）——"169th President of The Birmingham & Midland Institute"（2024）是另一机构，勿混 |
| 生年双值 | frontmatter date_of_birth 双值 ["1949-01-25","1949-00-00"]——取正文完整日期 1949-01-25 |
| 身世叙述 | illegitimacy/假母真姐的故事 page.md 明载可写，但必须客观、克制、尊重（本人自述口径），禁猎奇化 |
| 政治内容禁写 | 工党党员约 40 年、Scientists for Labour 赞助人、苏格兰公投联名等 Political views 节——**立传一律不写**（项目纪律：政治主张不入正文）；"好科学家标准"引语可用 |
| 绿卡插曲 | 诺贝尔奖得主绿卡被拒（短式出生证明无父母姓名）——可作叙事插曲，注明这是 2003–2011 任洛克菲勒校长期间 |
| 在世者生卒 | 仅生年 1949-01-25，无卒年——封面用 1949– 开放区间 |
| 奖项年份 | Rosenstiel/Louis-Jeantet 1992、Royal Medal 1995、Lasker 1998、封爵 1999、Nobel 2001、Copley 2005、Einstein World Award 2013、OM/CH 2022——年份勿串 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| cdc2 | cdc2 基因 | 裂殖酵母细胞周期基因（Nurse 发现） |
| Cdk1 / CDK1 | 周期蛋白依赖激酶 1 | 人类 cdc2 同源基因（1987，与 Melanie Lee） |
| fission yeast | 裂殖酵母 | *Schizosaccharomyces pombe*，勿与酿酒酵母混 |
| G1/S 与 G2/M transition | G1→S 与 G2→M 转换 | cdc2 控制的两道关卡 |
| phosphorylation | 磷酸化 | CDK 激活/失活的分子开关 |
| cyclin-dependent kinase | 周期蛋白依赖激酶 | 与 Hunt 的 cyclin 呼应 |
| Royal Society | 皇家学会 | 两任会长（61st/64th） |
| Francis Crick Institute | 弗朗西斯·克里克研究所 | 2011 首任所长兼 CEO（时名 UKCMRI） |
| Order of Merit | 功绩勋章 | 2022 授予 |
| Candida utilis | 产朊假丝酵母 | 博士论文对象 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**New Lands**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：从裂殖酵母的一个基因到人类 CDK1，再到横跨大西洋执掌洛克菲勒、回英创建克里克研究所——Nurse 的人生是一条不断抵达"新大陆"的航线；"New Lands" 匹配其拓疆式的事业轨迹。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/21th_century/Paul_Nurse/New_Lands.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
