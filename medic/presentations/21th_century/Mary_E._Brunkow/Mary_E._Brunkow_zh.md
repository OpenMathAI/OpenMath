# 医学家立传提示词（Mary E. Brunkow）

> 本文件是 OpenMedic 项目 21 世纪诺贝尔生理学或医学奖 **2025 年得主 Mary E. Brunkow（玛丽·埃伦·布伦科）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/21th_century/Mary_E._Brunkow/page.md`，与其冲突时以 page.md 为准。（注：本名 Mary Elizabeth Brunkow，提示词按 manifest 简写 Mary E. Brunkow）

## 一、背景信息 【人物专属】

- **目标医学家**：Mary Elizabeth Brunkow（1961-04-13 生于美国俄勒冈州波特兰，在世）
- **气质关键词**：**scurfy 小鼠基因的破译者、FOXP3 的命名者、外周免疫耐受的分子地基奠定者**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 2025 条目，与 Ramsdell、Sakaguchi 三人共享同一理由）：
  > "for their discoveries concerning peripheral immune tolerance"（因他们发现外周免疫耐受机制）
- **设计母题**：**踩住刹车的转录因子（FOXP3）**——失控的 T 细胞活化被 FOXP3 拴住的意象：以脱缰箭头被闸口拴住的图案作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Mary_E._Brunkow/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/21th_century/Mary_E._Brunkow/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Mary_E._Brunkow_zh`、`VIDEO_NAME=Mary_E._Brunkow_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | peripheral immune tolerance | 外周免疫耐受 | FOXP3/scurfy 基因，2025 诺奖核心 |
| 1 | immunology | 免疫学 | infobox Fields 首项 |
| 2 | molecular biology | 分子生物学 | infobox Fields 次项；博士阶段 H19 基因 |
| 3 | genetics | 遗传学 | frontmatter field_of_work；scurfy 突变定位 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Shirley M. Tilghman | 对方 → 导师 | 普林斯顿博士导师（1991，转基因小鼠 H19 基因表达与功能） |
| colleague | Fred Ramsdell | 无向 | Celltech/Darwin Molecular 时期 scurfy 基因合作鉴定者，诺奖工作搭档 |
| collaborator | Hans D. Ochs | 无向 | 2001 与 Ochs、Wildin 团队合作证明人 FOXP3 突变致 IPEX 综合征 |
| collaborator | Robert Wildin | 无向 | 2001 人 FOXP3/IPEX 合作者 |
| co-honored | Fred Ramsdell | 无向 | 2025 诺贝尔生理学或医学奖三人共享（外周免疫耐受） |
| co-honored | Shimon Sakaguchi | 无向 | 2025 诺贝尔生理学或医学奖三人共享（外周免疫耐受） |

**在世者关系偏少为诚实值**（6 条）：Brunkow page.md 极短（2025 最新得主），metadata 亦无额外师承/学生——Review 勿补造边。**不入库但提示词可叙述**：Frances Arnold 与 Lotte Bjerre Knudsen（2026 Golden Plate 颁奖人，事件非关系）。

## 五、配色方案 【人物专属】

- **气质**：沉静、坚韧、产业实验室里的关键一跃
- **主色**：`#46356B`（普吉特湾深紫——西雅图产业研发的沉静）+ 香槟金诺奖色
- **badge 四分类色**：`badgeFOXP3` FOXP3 深紫 `#46356B`；`badgeScurfy` scurfy 小鼠 玫瑰 `#9E2B25`；`badgeTreg` 调节性 T 细胞 青绿 `#0E7C7B`；`badgeIPEX` IPEX 综合征 琥珀 `#C07A2A`
- **背景母题**：脱缰箭头被闸口拴住的图案，呼应「踩住刹车的转录因子」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — FOXP3 的破译者 / Mary E. Brunkow 1961– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1961-04-13 波特兰、华盛顿大学 BS 1983、
    普林斯顿 PhD 1991、Institute for Systems Biology 高级项目经理、诺奖 2025）
03  核心贡献概览 — scurfy 表型 / scurfin=FOXP3 / 外周耐受的分子中心 / 人源 IPEX
04  波特兰少女 (1961–1983) — St. Mary's Academy 1979、华盛顿大学分子与细胞生物学 BS 1983
05  普林斯顿：Tilghman 门下 (1983–1991) — 转基因小鼠 H19 基因的表述与功能（印记基因领域起点）
06  进入产业界 — 西雅图 Bothell 的 Celltech R&D（后经 Darwin Molecular/Chiroscience 并购线）
07  scurfy 之谜 (1990s)（核心贡献页）— 自身免疫致死表型的小鼠品系、
    X 染色体候选区约 20 个基因的排查
08  2001：scurfin=FOXP3（核心贡献页）— Nature Genetics 论文鉴定未知基因两碱基插入突变、
    命名 scurfin 后即 FOXP3；失控 T 细胞活化与致死性淋巴增殖
09  从小鼠到人 (2001) — 与 Ochs、Wildin 团队合作：人 FOXP3 突变致 IPEX 综合征
10  FOXP3 与 Treg 的合流 — 与 Sakaguchi 的 Treg 发现（1995/2003）汇成外周耐受完整图景
11  Institute for Systems Biology — 高级项目经理；从产业到系统生物学的转身
12  荣誉与认可 — 2025-10-06 卡罗林斯卡宣布；2026-06-24 Golden Plate Award
    （Frances Arnold/Lotte Bjerre Knudsen 颁授，华盛顿特区）
13  三人分工 — Brunkow/Ramsdell（FOXP3 基因与 IPEX）、Sakaguchi（Treg 细胞的发现）——
    citation 同一句、侧重分层
14  遗产与结尾 — 自身免疫病与移植耐受的 FOXP3 时代；一个在产业界做出的诺奖级发现
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 生日双值冲突 | frontmatter metadata 作 1961-04-23、infobox 与正文均作 **April 13, 1961**——以 page.md 正文为准取 1961-04-13，陷阱表记录裁定（metadata 噪声） |
| 页面极短 | Brunkow 为 2025 最新得主、page.md 仅 60 余行——事实基准逐句对应，凡 page.md 未载的获奖词/机构细节一律不写 |
| 命名链条 | 2001 论文先命名基因产物 **scurfin**，后通称 **FOXP3**——"co-identifying the gene later named FOXP3"，两段命名勿混为一 |
| 机构并购链 | Celltech R&D（Bothell）→（Ramsdell 侧线索）Darwin Molecular 1994→Chiroscience 1996→Celltech 合并→2004 两人离开——Brunkow 页面只载 Celltech 与 ISB 两站，并购链细节从 Ramsdell 篇叙述 |
| Treg 归属 | 调节性 T 细胞的**发现**属 Sakaguchi（1995）；Brunkow 侧贡献是 FOXP3 分子基础（2001）——三人分工勿互串 |
| IPEX | 人 FOXP3 突变致 IPEX 综合征（罕见自身免疫病）——是 2001 年与 Ochs/Wildin 的合作成果，勿写成 Brunkow 单独完成 |
| 在世者生卒 | 仅生年 1961-04-13，无卒年——封面用 1961– 开放区间 |
| 奖项单一 | page.md 载奖项仅 Nobel 2025 与 2026 Golden Plate——勿从他人页面挪奖项 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| peripheral immune tolerance | 外周免疫耐受 | 获奖理由核心词 |
| FOXP3 | FOXP3 转录因子 | 初名 scurfin；Treg 的主控基因 |
| scurfy mouse | scurfy 小鼠 | X 连锁致死性自身免疫表型 |
| regulatory T cell (Treg) | 调节性 T 细胞 | Sakaguchi 发现的细胞类群 |
| IPEX syndrome | IPEX 综合征 | 人 FOXP3 突变所致免疫失调 |
| lymphoproliferative disorder | 淋巴增殖性疾病 | scurfy 表型的致死后果 |
| thymus | 胸腺 | 中枢耐受场所，外周耐受在其外 |
| self-reactivity | 自身反应性 | FOXP3 约束的对象 |
| H19 | H19 基因 | 博士论文对象（印记基因） |
| Institute for Systems Biology | 系统生物学研究所 | 现职机构（西雅图） |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**The Flow of Time**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：从 1991 年 H19 博士论文到 2001 年 scurfin 论文沉寂产业界二十余年、再到 2025 年诺奖揭晓——Brunkow 的故事是时间之流里耐心等待被认出的一块基石；"The Flow of Time" 匹配这种迟来而必然的回响。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/21th_century/Mary_E._Brunkow/The_Flow_of_Time.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
