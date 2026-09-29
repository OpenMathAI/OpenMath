# 医学家立传提示词（Leland H. Hartwell）

> 本文件是 OpenMedic 项目 21 世纪诺贝尔生理学或医学奖 **2001 年得主 Leland H. Hartwell（利兰·哈特韦尔）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/21th_century/Leland_H._Hartwell/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Leland Harrison "Lee" Hartwell（1939-10-30 生于美国加州洛杉矶，在世）
- **气质关键词**：**细胞周期检查点的发现者、酵母遗传学的测绘师、癌症早检的推动者**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 2001 条目，三人共享同一理由）：
  > "for their discoveries of key regulators of the cell cycle"（因他们发现细胞周期的关键调节因子）
  - page.md 正文另有表述 "for their discoveries of protein molecules that control the division (duplication) of cells"——引用诺奖理由时以 citation json 为准，正文叙述可带出蛋白分子表述。
- **设计母题**：**细胞周期检查点（checkpoints）**——细胞在 G1/S 闸门前停驻、检验、放行的「周期闸门」意象：以圆环轨道上的分段弧光（各阶段分段点亮、闸门处停驻）作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Leland_H._Hartwell/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/21th_century/Leland_H._Hartwell/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Leland_H._Hartwell_zh`、`VIDEO_NAME=Leland_H._Hartwell_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Hartwell 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | cell cycle regulation | 细胞周期调控 | CDC 基因与检查点，2001 诺奖核心 | 封面、核心页 |
| 1 | yeast genetics | 酵母遗传学 | 以酿酒酵母温度敏感突变体筛选 CDC 基因 | 核心页 |
| 2 | checkpoint control | 检查点控制 | 细胞损伤时延迟分裂的闸门概念 | 核心页 |
| 3 | cancer early detection | 癌症早期检测 | Canary Foundation 科学顾问委员会主席 | 后期页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Boris Magasanik | 对方 → 导师 | infobox Doctoral advisor 明载（MIT 1964 博士，枯草芽孢杆菌组氨酸酶诱导论文） |
| co-honored | Tim Hunt | 无向 | 2001 诺贝尔生理学或医学奖三人共享（发现细胞周期关键调节因子） |
| co-honored | Paul Nurse | 无向 | 2001 诺贝尔生理学或医学奖三人共享（发现细胞周期关键调节因子） |

**在世者关系偏少为诚实值**：page.md 未明载 Hartwell 的具名学生/合作者（Lee Hartwell Award 得主列表是奖项名录非师承，不入库）；metadata.json 亦无额外师承。Review 勿以「关系太少」为由补造边。

## 五、配色方案 【人物专属】

- **气质**：沉静、秩序、周期往复的实验台节律
- **主色**：`#16324F`（深海靛蓝——酵母遗传图谱的沉静测绘）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeCDC` 细胞周期调控 — 靛蓝 `#16324F`
  - `badgeYeast` 酵母遗传学 — 青绿 `#0E7C7B`
  - `badgeCheck` 检查点控制 — 琥珀 `#C07A2A`
  - `badgeCancer` 癌症早检 — 玫瑰 `#A63A2B`
- **背景母题**：圆环轨道分段弧光（G1–S–G2–M 分段点亮、闸门停驻点高亮），呼应「检查点」母题。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 细胞周期检查点的发现者 / Leland H. Hartwell 1939– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1939-10-30 洛杉矶、Glendale High School、
    Caltech BS 1961、MIT PhD 1964、Fred Hutchinson 主席 1997–2010、诺奖 2001、核心领域）
03  核心贡献概览 — CDC 基因 / CDC28 / 检查点 / 交配信号转导通路
04  洛杉矶少年与 Caltech (1939–1961) — Glendale 高中、加州理工学院本科 1961
05  MIT 博士：Magasanik 门下 (1961–1964) — 枯草芽孢杆菌组氨酸酶诱导
06  UC Irvine 与华盛顿大学 (1965–1968) — 尔湾任教；1968 迁西雅图华盛顿大学
07  CDC 基因的发现 (1970–1971)（核心贡献页）— 面包酵母温度敏感突变体筛选、细胞分裂周期基因
08  CDC28：酵母的 Cdk 激酶 — 控制周期起始、G1 推进；突变与某些癌症相关
09  检查点概念（核心贡献页）— 细胞损伤时延迟分裂、保证忠实复制
10  交配信号转导通路 — 酵母交配通路的鉴定与表征
11  Fred Hutchinson 岁月 (1996–2010) — 1996 入职、1997 主席兼所长、2010 退休；NAS 1987
12  荣誉与认可 — Lasker 1998、Massry 2000、Nobel 2001、Horwitz Prize 1995、Mendel Medal 2001、
    华盛顿州 Medal of Merit 2003、Komen Brinker 1998
13  癌症早期检测事业 — Canary Foundation、Pacific Health Summit、ASU 比奥设计研究院
    （Virginia G. Piper 讲席）、Amrita/长庚顾问
14  遗产与结尾 — Lee Hartwell Award（2002 首位得主即本人）、细胞周期研究与肿瘤学的桥梁
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 三人共享 | 2001 与 Tim Hunt、Paul Nurse 共享；citation json 三人同理由 "for their discoveries of key regulators of the cell cycle"；颁奖表述差异（"protein molecules that control the division of cells"）是 Wikipedia 正文转述，勿当官方理由 |
| CDC vs CDK | CDC28 是**酵母基因**（Hartwell 发现），其编码产物是酵母 Cdk 激酶；CDK（周期蛋白依赖激酶）是后来统一命名的蛋白家族——勿写成"Hartwell 发现了 CDK" |
| 检查点归属 | "checkpoints" 概念由 Hartwell 提出（page.md Research 节明载 "introduction of the concept of cell cycle 'checkpoints'"），勿让渡给他人 |
| 年份口径 | 面包酵母 CDC 基因发现：正文 "a series of experiments from 1970 to 1971"——写 1970–1971，勿单写某一年 |
| UC Irvine 职级 | page.md 仅载 "worked at the University of California, Irvine as a professor (1965–1968)"，照页面措辞写，勿自补"助理教授" |
| 在世者生卒 | 仅生年 1939-10-30（洛杉矶），无卒年——封面与身份页用 1939– 开放区间，勿画错 |
| 机构主线 | 华盛顿大学（1968–）→ Fred Hutchinson（1996 入职、1997–2010 主席兼所长）→ ASU（2009 宣布加入）；Fred Hutchinson 退休年份 2010 勿写 2009 |
| 奖项年份 | Rosenstiel 1992、GSA Medal 1994、Horwitz Prize 1995、Komen Brinker/Lasker 1998、Massry 2000、Nobel/Mendel Medal 2001、华盛顿州 Medal of Merit 2003——年份勿串 |
| NAS | 1987 当选美国国家科学院院士（早于诺奖 14 年），勿写"诺奖后当选" |
| metadata 差异 | metadata.json occupation 含 "university teacher/biochemist"，与 infobox 一致可参考；无冲突裁定 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| cell division cycle (CDC) genes | 细胞分裂周期基因 | 酵母基因命名，非蛋白家族名 |
| CDC28 | CDC28 基因 | 编码酵母 Cdk 激酶，控制周期起始 |
| checkpoint | 检查点 | Hartwell 提出的概念，勿混同 DNA 损伤修复本身 |
| start (G1) | 起始点 | CDC28 控制 G1 推进 |
| temperature sensitive mutant | 温度敏感突变体 | CDC 筛选的核心方法 |
| Saccharomyces cerevisiae | 酿酒酵母（面包酵母） | 模式生物，勿写"面包霉菌" |
| mating signal transduction pathway | 交配信号转导通路 | 另一重要发现 |
| early detection | 早期检测 | Canary Foundation 方向 |
| personalized medicine | 个体化医疗 | ASU Piper 讲席名称 |
| Louisa Gross Horwitz Prize | 路易莎·格罗斯·霍维茨奖 | 哥伦比亚大学颁发，1995 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Timeless**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：从洛杉矶少年到酵母图谱再到检查点概念——Hartwell 的工作不是单一发现而是为整个领域立下"时钟与闸门"的框架；"Timeless" 对应细胞周期这一亘古节律与他跨越半个多世纪仍在推进的癌症早检事业。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/21th_century/Leland_H._Hartwell/Timeless.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
