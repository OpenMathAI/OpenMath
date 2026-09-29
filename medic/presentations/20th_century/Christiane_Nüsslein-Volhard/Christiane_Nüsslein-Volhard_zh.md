# 医学家立传提示词（Christiane Nüsslein-Volhard）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1995 年得主 Christiane Nüsslein-Volhard（克里斯蒂安娜·尼斯莱因-福尔哈德）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Christiane_Nüsslein-Volhard/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Christiane (Janni) Nüsslein-Volhard（1942-10-20 生于德国马格德堡，在世）
- **气质关键词**：**海德堡筛选的统帅、果蝇胚胎发育基因的测绘者、德国唯一科学诺奖女性**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1995 条目，与 Edward B. Lewis、Eric F. Wieschaus 三人共享同一理由）：
  > "for their discoveries concerning the genetic control of early embryonic development"（因他们发现早期胚胎发育的遗传控制）
- **设计母题**：**果蝇胚胎的分节图案（segmentation）**——幼虫体节与小齿带在突变下缺失/成隙的意象：以分节条纹的缺失图谱作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Christiane_Nüsslein-Volhard/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；第 0/1/2/3 步按 medic 路径执行：页面已在 `medic/presentations/pages/20th_century/Christiane_Nüsslein-Volhard/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Christiane_Nüsslein-Volhard_zh`、`VIDEO_NAME=Christiane_Nüsslein-Volhard_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | developmental biology | 发育生物学 | 果蝇胚胎发育的遗传控制，1995 诺奖核心 |
| 1 | genetics | 遗传学 | infobox Fields；EMS 诱变大筛选 |
| 2 | embryology | 胚胎学 | infobox Fields；体节与齿带表型分析 |
| 3 | biochemistry | 生物化学 | 博士阶段蛋白质-DNA 相互作用 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Heinz Schaller | 对方 → 导师 | 图宾根大学博士导师（1974，大肠杆菌 RNA 聚合酶与噬菌体 fd 复制型 DNA 的结合） |
| advisor-student | Walter Gehring | 对方 → 导师 | 巴塞尔 Biozentrum 博士后导师（1975，EMBO 长期奖学金） |
| colleague | Klaus Sander | 无向 | 1977 转赴弗莱堡大学其实验室（胚胎图式专家） |
| colleague | Eric F. Wieschaus | 无向 | 1978 EMBL 海德堡共建实验室，三年筛约两万突变家系（海德堡筛选） |
| co-honored | Eric F. Wieschaus | 无向 | 1995 诺贝尔生理学或医学奖三人共享（早期胚胎发育的遗传控制） |
| co-honored | Edward B. Lewis | 无向 | 1995 诺贝尔生理学或医学奖三人共享（早期胚胎发育的遗传控制） |

**在世者关系少为诚实值**（6 条）。**不入库但提示词可叙述**：祖父 Franz Volhard（内科名家）与曾祖父 Jacob Volhard（化学家，家世叙述）；侄子 Benjamin List（2021 诺贝尔化学奖，亲戚叙述不建边）；父母与四兄妹（家世叙述）；Toll 基因的关联（其发现引出 TLR，正文叙述；Hoffmann/Beutler 的 TLR 工作不建边）。

## 五、配色方案 【人物专属】

- **气质**：德式的严谨、果蝇翅影的轻盈、筛选的宏大耐心
- **主色**：`#4A2A6A`（图宾根深紫——马普发育生物学研究所的沉静）+ 香槟金诺奖色
- **badge 四分类色**：`badgeScreen` 海德堡筛选 深紫 `#4A2A6A`；`badgeSegment` 分节图案 青绿 `#0E7C7B`；`badgeToll` Toll 基因 琥珀 `#C07A2A`；`badgeZebra` 斑马鱼 苔绿 `#175E54`
- **背景母题**：分节条纹的缺失图谱，呼应「果蝇胚胎的分节图案」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 果蝇胚胎基因的测绘者 / Christiane Nüsslein-Volhard 1942– + 四色 badge + 右上头像 + 国籍行（Germany）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1942-10-20 马格德堡、法兰克福/图宾根、
    PhD 1974、马普发育生物学研究所所长 1984–2014、诺奖 1995、德国唯一科学诺奖女性）
03  核心贡献概览 — 海德堡筛选 / 分节基因分类 / gap/pair-rule/segment-polarity / Toll
04  马格德堡与艺术少年 (1942–1962) — 五子女之二、"被训练去看与认出事物"、
    弃医从生物（一个月护理实习后）、法兰克福生物系
05  图宾根生化与博士 (1964–1974) — 1969 生化文凭、Schaller 门下 PhD 1974
    （大肠杆菌 RNA 聚合酶与 fd 噬菌体 DNA 结合）
06  巴塞尔与弗莱堡 (1975–1978) — Gehring 实验室博士后（EMBO 奖学金）、
    果蝇发育生物学专长、1977 Sander 实验室（胚胎图式）
07  1978：EMBL 海德堡建组（核心贡献页）— 与 Wieschaus 共建实验室、
    EMS 随机诱变、约两万突变家系、600 突变体、约 5000 必需基因中仅 120 个为早期发育所必需
08  显微镜下的表型分类（核心贡献页）— 体节与齿带表型逐一看片、
    gap/pair-rule/segment-polarity 三类基因的逻辑；hedgehog/gurken/Krüppel 等命名故事
09  1980 发表 — 15 个基因控制果蝇幼虫分节图谱（10 月发表）；规模与工作量的史话
10  意义与回响 — 原口/后口共同祖先的复杂体型的演化推论、转录调控与细胞命运理解；
    Toll 发现 → TLR 家族（Hoffmann/Beutler 的先天免疫延伸，一句带过）
11  图宾根马普与斑马鱼 (1981–2014) — Friedrich Miescher 实验室 1981、
    马普发育生物学研究所所长 1984–2014、1984 后开启斑马鱼脊椎动物发育
12  荣誉与认可 — Leibniz 1986、Rosenstiel 1989、Lasker 1991、Sloan/Louis-Jeantet/
    Horwitz/Warburg/Bayer 1992、Krebs/Schering 1993、Nobel 1995、Pour le Mérite 1997、
    大十字级联邦十字勋章 2005、ForMemRS 1990、NAS 1990；小行星 15811 命名
13  公共事务与基金会 — 德国国家伦理委员会 2001–06、2004 创立
    Christiane Nüsslein-Volhard Stiftung（资助有孩子的年轻女科学家）、
    《Coming to Life》2006 与 2006 食谱
14  遗产与结尾 — 从果蝇到斑马鱼：发育基因学的两翼；音乐与室内乐的一生（客观收尾）
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 三人共享结构 | 1995 三人共享同一句理由；Lewis 的侧重是同源框基因（homeotic），N-V/Wieschaus 的侧重是饱和筛选与分节——个人侧重分层，Lewis 细节由其本人篇展开 |
| 海德堡筛选数字 | 约 20,000 突变家系、约 600 突变体、约 5,000 必需基因中 120 个必需、1980-10 发表仅 15 个分节基因——四个数字勿串 |
| 命名故事 | hedgehog/gurken（德语"黄瓜"）/Krüppel（"残废"）等按突变幼虫外观命名——趣味可写，德语词义准确 |
| 双导师结构 | 博士导师 Schaller（图宾根 1974）+ 博士后导师 Gehring（巴塞尔 1975）——两条 advisor 边阶段注记不同；Sander 1977 用 colleague（转赴其实验室一年） |
| Toll 归属 | N-V "associated with the discovery of Toll"；TLR 家族鉴定与先天免疫是 Hoffmann/Beutler 的诺奖线——一句带过勿越界（本人篇侧重发育） |
| 亲戚 | 侄 Benjamin List 2021 化学诺奖、祖父 Franz Volhard、曾祖父 Jacob Volhard——家世叙述不建边 |
| 在世者生卒 | frontmatter 双值取正文 1942-10-20；无卒年——封面 1942– 开放区间 |
| 婚姻 | 1960s 中期短暂婚姻旋即离异、无子女（page.md 明载）——身份页可客观一句，不展开 |
| 德国唯一 | "德国唯一获科学类诺贝尔奖的女性"（Literature 两位德语女性在 Notes 有说明）——表述照 page.md |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| Heidelberg screen | 海德堡筛选 | 1978–1980 与 Wieschaus 的大筛选 |
| ethyl methanesulfonate (EMS) | 甲基磺酸乙酯 | 化学诱变剂 |
| segmentation genes | 分节基因 | gap/pair-rule/segment-polarity 三类 |
| gap gene | gap 基因 | 体节成隙表型 |
| pair-rule gene | 配对规则基因 | 隔体节表型 |
| Krüppel | Krüppel 基因 | 德语"残废"，gap 基因代表 |
| hedgehog | hedgehog 基因 | 后成著名信号通路 |
| Toll | Toll 基因 | 胚背腹轴+先天免疫源头 |
| zebrafish (Danio rerio) | 斑马鱼 | 1984 后的脊椎动物模型 |
| saturation screen | 饱和筛选 | 染色体致死性全覆盖测试 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Tragedy**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：筛选岁月的漫长与孤独、被质疑多年后才被世界听懂的发现——"Tragedy" 的低回承载"为科学甘坐冷板凳"的重量；诺奖的揭晓是悲剧底色上最亮的一笔。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Christiane_Nüsslein-Volhard/Tragedy.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
