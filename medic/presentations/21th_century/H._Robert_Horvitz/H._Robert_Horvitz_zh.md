# 医学家立传提示词（H. Robert Horvitz）

> 本文件是 OpenMedic 项目 21 世纪诺贝尔生理学或医学奖 **2002 年得主 H. Robert Horvitz（霍华德·罗伯特·霍维茨）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/21th_century/H._Robert_Horvitz/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Howard Robert Horvitz（1947-05-08 生于美国芝加哥，在世）
- **气质关键词**：**细胞死亡基因的猎手、线虫谱系的绘制者、凋亡通路的破译者**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 2002 条目，三人共享同一理由）：
  > "for their discoveries concerning 'genetic regulation of organ development and programmed cell death '"（因他们发现器官发育和细胞程序性死亡的遗传调控）
  - page.md 正文另有 Nobel 措辞转述（"seminal discoveries … important for medical research and have shed new light on the pathogenesis of many diseases"）——引用时以 citation json 为准。
- **设计母题**：**生与死的基因开关（ced-3/ced-4/ced-9）**——促死与护命基因对抗的意象：以双色分叉回路作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/H._Robert_Horvitz/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/21th_century/H._Robert_Horvitz/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=H._Robert_Horvitz_zh`、`VIDEO_NAME=H._Robert_Horvitz_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Horvitz 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | apoptosis | 细胞程序性死亡 | ced-3/ced-4/ced-9 死亡基因，2002 诺奖核心 | 封面、核心页 |
| 1 | developmental biology | 发育生物学 | C. elegans 细胞谱系与异时性突变 | 核心页 |
| 2 | genetics | 遗传学 | 线虫遗传筛选，lin-4 异时性基因 | 核心页 |
| 3 | cell biology | 细胞生物学 | 死亡细胞清除通路、信号转导 | 全篇 |
| 4 | molecular biology | 分子生物学 | ced-3 类似人基因、microRNA 项目合作 | 后期页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Walter Gilbert | 对方 → 导师 | 哈佛博士导师（与 Watson 共同指导，T4 诱导的 RNA 聚合酶修饰，1974）；库内规范名 id=1127 |
| advisor-student | James D. Watson | 对方 → 导师 | 哈佛博士导师（与 Gilbert 共同指导，1974）；库内规范名 id=3610 |
| advisor-student | Michael Hengartner | Horvitz → 学生 | infobox Notable students 明载；ced-9 与 bcl-2 同源论文一作 |
| advisor-student | Gary Ruvkun | Horvitz → 学生 | infobox Notable students 明载；2024 诺奖得主（med21-batch-12 将回填其 QID Q504021） |
| advisor-student | Yishi Jin | Horvitz → 学生 | infobox Notable students 明载 |
| advisor-student | Junying Yuan | Horvitz → 学生 | infobox Notable students 明载 |
| spouse | Martha Constantine-Paton | 无向 | infobox Spouse 明载 |
| colleague | Sydney Brenner | 无向 | 1974 起 LMB 博士后共事（C. elegans 遗传学与细胞谱系） |
| colleague | John Sulston | 无向 | LMB 合作追踪幼虫发育全部非生殖系细胞分裂，1977 合著谱系论文；库内 stub id=4265 |
| colleague | Martin Chalfie | 无向 | 与 Sulston、Chalfie 合作表征细胞谱系突变体与 lin-4（1981）；库内规范名 id=4259 |
| collaborator | Victor Ambros | 无向 | 合作表征 C. elegans 基因组 100+ microRNA 全集 |
| collaborator | David Bartel | 无向 | 合作表征 C. elegans 基因组 100+ microRNA 全集 |
| co-honored | Sydney Brenner | 无向 | 2002 诺贝尔生理学或医学奖三人共享（器官发育与程序性细胞死亡的遗传调控） |
| co-honored | John Sulston | 无向 | 2002 诺贝尔生理学或医学奖三人共享（器官发育与程序性细胞死亡的遗传调控） |

**在世者关系说明**：Horvitz 在世，relations=14 为本批次最富——因 infobox 明列两位博士导师与四位学生，仍为诚实值。**不入库但提示词可叙述**：Hilary Ellis（1986 论文一作，仅论文合作者）、父 Oscar/母 Mary（仅家世叙述）、Society for Science & the Public 职务（机构角色非关系）。

## 五、配色方案 【人物专属】

- **气质**：冷峻、精确、生死边界的克制
- **主色**：`#14574B`（深松绿——线虫生命的静默底色）+ 香槟金诺奖色
- **badge 四分类色**：`badgeDeath` 程序性细胞死亡 玫瑰 `#9E2B25`；`badgeLineage` 细胞谱系 深松绿 `#14574B`；`badgeWorm` 发育遗传学 青绿 `#0E7C7B`；`badgeHuman` 通往人类疾病 琥珀 `#C07A2A`
- **背景母题**：双色分叉回路（ced-3/ced-4 促死支 vs ced-9 护命支），呼应「生死基因开关」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 细胞死亡基因的猎手 / H. Robert Horvitz 1947– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1947-05-08 芝加哥、MIT 数学本科 1968、
    哈佛 PhD 1974、MIT 教授/McGovern 研究所、HHMI 研究员、诺奖 2002）
03  核心贡献概览 — 细胞谱系 / 死亡基因 ced-3/ced-4 / 保护基因 ced-9 / 通往人类疾病
04  芝加哥少年与数学 (1947–1968) — 犹太家庭、MIT 数学专业、IBM 夏季打工（会计机接线与
    Conversational Programming System）
05  转向生物学与哈佛博士 (1968–1974) — 高年级首门生物课、Gilbert 与 Watson 双导师、
    T4 诱导的 E. coli RNA 聚合酶修饰
06  LMB 岁月 (1974–1977)（核心贡献页）— 与 Brenner、Sulston 共事；追踪幼虫全部非生殖系
    细胞分裂；1977 合著完整谱系描述
07  谱系突变体与 lin-4 (1981) — 与 Sulston、Chalfie 合作；lin-4 异时性突变改变细胞命运时间表
08  死亡基因 (1986)（核心贡献页）— ced-3 与 ced-4：执行死亡的前提；Ellis & Horvitz 1986 Cell 论文
09  ced-9 与生死平衡（核心贡献页）— ced-9 与 ced-4/ced-3 互作抗死；Hengartner 1994 bcl-2 同源；
    死细胞清除基因
10  通往人类 — 人类基因组含 ced-3 类似基因；ced-3 编码物似哺乳类 ICE（1993 论文）；
    癌症与 ALS 等神经退行疾病的病理新光
11  MIT 与学术版图 (1978–) — MIT 教授、McGovern 脑研究所、HHMI 研究员；microRNA 全集
    项目（与 Ambros、Bartel）
12  荣誉与认可 — NAS 分子生物学奖 1988、NAS 院士 1991、Gairdner 1999、Horwitz Prize 2000、
    Nobel/Wiley/Gruber 2002、英国皇家学会外籍院士 2009
13  学术服务与传承 — Society for Science & the Public 董事会主席；学生 Hengartner/Ruvkun/
    Jin/Yuan 各自开枝（Ruvkun 2024 再获诺奖的师门佳话）
14  遗产与结尾 — 131 个注定死亡的细胞：程序性细胞死亡从线虫到医学
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 双博士导师 | infobox Doctoral advisors 载 **Walter Gilbert 与 James D. Watson 两位**（1974 共同指导）——师承边两条并列；frontmatter metadata 的 doctoral_advisor 另列 Sydney Brenner，但 infobox 不载——**以 page.md infobox 为准**，Brenner 只建 colleague 边，勿建师生边 |
| 姓名 | 全名 Howard Robert Horvitz；yaml/manifest 用 **H. Robert Horvitz**，正文可交代全名 |
| 死亡基因年份 | 1986 鉴定首批"死亡基因" ced-3/ced-4（Ellis & Horvitz Cell 论文）；ced-9 保护基因与 bcl-2 同源为 1994（Hengartner & Horvitz）——两阶段勿混 |
| ced-3 与 ICE | 1993 Yuan 等 ced-3 编码物类似哺乳类白细胞介素-1β 转换酶——Yuan Junying 是学生（已入边），论文合作叙述即可 |
| lin-4 时间 | 1981 年"鉴定并表征 lin-4"（与 Sulston、Chalfie 合作）；lin-4 的 microRNA 本质是后来 Ambros 侧的进展——勿把 miRNA 归属写进 1981 |
| 谱系论文分工 | 1977 非生殖系谱系（Sulston & Horvitz）；生殖系谱系为 Sulston 另作——叙述时勿并成一篇 |
| 共享理由 | 官方理由三人同一句；Horvitz 的个人侧重是程序性细胞死亡的遗传调控（ced 基因）——Brenner 建体系、Sulston 谱系，三人侧重分层 |
| 在世者生卒 | 仅生年 1947-05-08，无卒年——封面用 1947– 开放区间 |
| Ruvkun 伏笔 | 学生 Gary Ruvkun 为 2024 诺奖得主——本 yaml 先建 stub，med21-batch-12 批次将回填其 QID Q504021；立传正文可预告这句师门佳话，但 Ruvkun 本人成就细节由其本人篇展开 |
| IBM 细节 | 夏季 IBM 工作先是接线会计机面板、最后一年参与开发 Conversational Programming System——两阶段勿混 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| programmed cell death / apoptosis | 程序性细胞死亡 / 凋亡 | 诺奖理由核心词；apoptosis 希腊语"落叶" |
| ced-3 / ced-4 | 死亡基因 ced-3/ced-4 | 执行细胞死亡的必要前提（1986） |
| ced-9 | 保护基因 ced-9 | 与 ced-4/ced-3 互作抗死；哺乳类 bcl-2 同源 |
| cell lineage | 细胞谱系 | 1977 Sulston & Horvitz 完整描述 |
| heterochronic mutant | 异时性突变体 | lin-4 改变细胞命运时间表 |
| lin-4 | lin-4 基因 | 后知为 microRNA 前体，1981 先以异时性突变鉴定 |
| Caenorhabditis elegans | 秀丽隐杆线虫 | 模式生物 |
| ICE | 白细胞介素-1β 转换酶 | ced-3 编码物的哺乳类类似物（1993） |
| microRNA | 微 RNA | 与 Ambros/Bartel 合作的全集表征项目 |
| ALS | 肌萎缩侧索硬化 | 后期把线虫发现联系人类疾病的方向之一 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Awaken**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：程序性细胞死亡不是终结而是生命秩序的觉醒——从线虫 131 个注定的死亡到人类凋亡通路的照亮，"Awaken" 匹配"为医学研究 Shed new light"的诺奖评语与其研究从黑暗走向光明的叙事弧。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/21th_century/H._Robert_Horvitz/Awaken.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
