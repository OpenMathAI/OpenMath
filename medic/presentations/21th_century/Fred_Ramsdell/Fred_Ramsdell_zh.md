# 医学家立传提示词（Fred Ramsdell）

> 本文件是 OpenMedic 项目 21 世纪诺贝尔生理学或医学奖 **2025 年得主 Fred Ramsdell（弗雷德·拉姆斯德尔）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/21th_century/Fred_Ramsdell/page.md`，与其冲突时以 page.md 为准。（本名 Frederick Jay Ramsdell，yaml/manifest 用 Fred Ramsdell）

## 一、背景信息 【人物专属】

- **目标医学家**：Frederick Jay Ramsdell（1960-12-04 生于美国伊利诺伊州埃尔姆赫斯特，在世）
- **气质关键词**：**产业界的基因猎人、FOXP3 的共同命名者、错过诺贝尔电话的徒步者**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 2025 条目，与 Brunkow、Sakaguchi 三人共享同一理由）：
  > "for their discoveries concerning peripheral immune tolerance"（因他们发现外周免疫耐受机制）
- **设计母题**：**两碱基的插入（two base pairs）**——在 X 染色体约 20 个候选基因里锁定两碱基插入突变的意象：以长序列上一点高亮的图案作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Fred_Ramsdell/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/21th_century/Fred_Ramsdell/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Fred_Ramsdell_zh`、`VIDEO_NAME=Fred_Ramsdell_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | peripheral immune tolerance | 外周免疫耐受 | FOXP3 鉴定与 IPEX，2025 诺奖核心 |
| 1 | immunology | 免疫学 | frontmatter field_of_work |
| 2 | regulatory T cells | 调节性 T 细胞 | T 细胞活化与耐受主线；2017 Crafoord |
| 3 | autoimmunity | 自身免疫 | scurfy/IPEX/关节炎的疾病轴 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Sidney Golub | 对方 → 导师 | UCLA 博士导师（微生物学与免疫学，1987） |
| colleague | Mary E. Brunkow | 无向 | Darwin Molecular/Celltech 时期 scurfy 基因合作鉴定者，诺奖搭档 |
| colleague | Jeffrey Bluestone | 无向 | 2019 共同创立 Sonoma Biotherapeutics |
| colleague | Alexander Rudensky | 无向 | Sonoma 共同创始人 |
| collaborator | Hans D. Ochs | 无向 | 2001 合作证明人 FOXP3 突变致 IPEX |
| collaborator | Robert Wildin | 无向 | 2001 人 FOXP3/IPEX 合作者 |
| co-honored | Mary E. Brunkow | 无向 | 2025 诺贝尔生理学或医学奖三人共享（外周免疫耐受） |
| co-honored | Shimon Sakaguchi | 无向 | 2025 诺贝尔生理学或医学奖三人共享（外周免疫耐受） |
| co-honored | Alexander Rudensky | 无向 | 2017 Crafoord 奖共享（Treg 与多关节炎研究） |

**不入库但提示词可叙述**：Qizhi Tang（Sonoma 四位共同创始人之一，其余三人已有更强关系承载而裁剪，正文可列名）；Rudensky 一人两条边（colleague + co-honored）。

## 五、配色方案 【人物专属】

- **气质**：旷野、求实、产业实验室的行军感
- **主色**：`#175E54`（内华达山脉深松绿——爱达荷徒步线与西雅图产业岁月）+ 香槟金诺奖色
- **badge 四分类色**：`badgeFoxp3` FOXP3 深松绿 `#175E54`；`badgeIndustry` 产业研发 深蓝 `#16324F`；`badgeTreg` Treg 医学 青绿 `#0E7C7B`；`badgeTrail` 徒步与诺奖 琥珀 `#C07A2A`
- **背景母题**：长序列上一点高亮的图案，呼应「两碱基的插入」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 产业界的基因猎人 / Fred Ramsdell 1960– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1960-12-04 Elmhurst、UCSD BS 1983、
    UCLA PhD 1987、Sonoma Biotherapeutics 联合创始人、诺奖 2025）
03  核心贡献概览 — scurfy 基因定位 / FOXP3 命名 / 人源 IPEX / Treg 医学转化
04  加州求学路 (1960–1983) — Homestead High 1979、Foothill 学院转 UCSD
    （付不起四年 UC 而曲线入学）、生物化学与细胞生物学 BS 1983
05  UCLA 博士与 NIH 岁月 (1983–) — Sidney Golub 门下微生物与免疫学 1987、
    NIH 博士后期间领食品券的清苦（page.md 明载可叙述）
06  Immunex 与 Darwin Molecular — T 细胞活化与耐受、基因发现；
    1994 与 Brunkow 同赴 Bothell 的 Darwin Molecular 建免疫学项目
07  并购长廊 (1996–2004) — Darwin→Chiroscience 1996→Celltech 合并；
    1990s 在 Celltech 锁定 scurfy 突变
08  2001：两碱基插入与 FOXP3 命名（核心贡献页）— X 染色体候选区约 20 基因、
    未知基因两碱基插入、命名 Foxp3
09  2001：从鼠到人（核心贡献页）— 与 Ochs、Wildin 团队合作证明人 FOXP3
    突变致 IPEX 综合征
10  产业漂泊与回归 — 2004 ZymoGenetics、2008 Novo Nordisk 西雅图炎症研究中心、
    aTyr Pharma 副总裁、Parker 癌症免疫治疗研究所 CSO
11  Sonoma Biotherapeutics (2019–) — 与 Bluestone/Tang/Rudensky 共同创立、
    CSO、2025 起任科学顾问委员会主席
12  荣誉与认可 — Crafoord 2017（与 Sakaguchi、Rudensky，多关节炎）、Nobel 2025
13  错过的电话 — 公布日正在爱达荷 off-the-grid 徒步；"I did not!" 与 200 条短信；
    登机靴捐赠诺贝尔博物馆（page.md 明载轶事可叙述）
14  遗产与结尾 — Treg/FOXP3 轴的医学转化：从自身免疫到移植耐受
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 2001 两步成果 | 同年两条线：scurfy/FOXP3 基因鉴定（与 Brunkow）+ 人 FOXP3/IPEX 证明（与 Ochs、Wildin 团队）——勿并成一步 |
| FOXP3 命名 | 基因由 Ramsdell/Brunkow 团队命名 *Foxp3*（小鼠）；Brunkow 侧论文产物初名 scurfin——两篇叙述命名链条时保持一致（初名 scurfin、后定 FOXP3） |
| 产业身份 | 获奖时为产业界科学家（Sonoma 顾问）——与学界得主不同的职业路径是本篇特色，勿写成"某大学教授" |
| 并购链 | Darwin Molecular（1994 加入）→ Chiroscience（1996 收购）→ Celltech 合并（1999，曾名 Celltech Chiroscience）→ 2004 两人离开——时间线勿乱 |
| Crafoord 与 Nobel 双线 | 2017 Crafoord（与 Sakaguchi、Rudensky，多关节炎方向）与 2025 Nobel（与 Sakaguchi、Brunkow）两条奖项线，Sakaguchi 两条都在——同奖人勿串 |
| 徒步轶事 | 公布日 off-the-grid 徒步、由妻子转达、"I did not!"（BBC 采访原话可引）、200 条短信、登机靴捐诺贝尔博物馆——page.md 明载可叙述，勿添油加醋 |
| 食品券细节 | NIH 博士后时期符合食品券领取资格（page.md 明载）——可作清苦岁月叙述，尊重语气 |
| 在世者生卒 | 仅生年 1960-12-04，无卒年——封面用 1960– 开放区间 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| peripheral immune tolerance | 外周免疫耐受 | 获奖理由核心词 |
| Foxp3 / FOXP3 | Foxp3（鼠）/FOXP3（人） | 命名由 Ramsdell/Brunkow 团队 |
| scurfy | scurfy 小鼠 | X 连锁自身免疫表型 |
| insertion | 插入突变 | 两碱基插入致病 |
| IPEX syndrome | IPEX 综合征 | 人 FOXP3 突变免疫失调 |
| T cell tolerance | T 细胞耐受 | Immunex 时期研究主线 |
| Crafoord Prize | 克拉福德奖 | 2017 多关节炎方向 |
| polyarthritis | 多关节炎 | Crafoord 授奖领域 |
| Sonoma Biotherapeutics | 索诺玛生物治疗 | 2019 共同创立 |
| Parker Institute | 帕克癌症免疫治疗研究所 | 曾任 CSO |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Daylight**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：公布诺奖时他正在爱达荷的山野徒步——从信号盲区走向 daylight 的瞬间，恰是他三十年产业科研长跑被照亮的一刻；"Daylight" 匹配这份旷野与揭晓交织的叙事。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/21th_century/Fred_Ramsdell/Daylight.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。