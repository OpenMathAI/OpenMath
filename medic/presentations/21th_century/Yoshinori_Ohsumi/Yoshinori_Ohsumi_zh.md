# 医学家立传提示词（Yoshinori Ohsumi 大隅良典）

> 本文件是 OpenMedic 项目 21 世纪诺贝尔生理学或医学奖 **2016 年得主 Yoshinori Ohsumi（大隅良典）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/21th_century/Yoshinori_Ohsumi/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Yoshinori Ohsumi（大隅 良典，1945-02-09 生于日本福冈，**在世**），细胞生物学家，东京工业大学（现东京科学大学）创机研究所教授，单元诺奖得主
- **气质关键词**：**酵母里看见自噬的人、冷门领域的孤独坚守、把基础研究做成一片学科的耐性**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 2016 条目，**独得，无共享**）：
  > "for his discoveries of mechanisms for autophagy"（因其发现细胞自噬的机制）
- **设计母题**：**液泡里的自噬体（yeast vacuole → autophagosome → recycling）**——饥饿状态下细胞"吃掉自己"并循环再利用；用「酵母细胞内同心圆的双层膜自噬体」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Yoshinori_Ohsumi/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/21th_century/Yoshinori_Ohsumi/`（世纪目录一律 `21th_century`，肖像见 images.txt）。Makefile 复制后设 `MAIN=Yoshinori_Ohsumi_zh`、`VIDEO_NAME=Yoshinori_Ohsumi_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。**在世者注意**：封面写 b.1945。

## 三、研究领域梳理 + 入库 【人物专属】

**大隅良典的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | autophagy | 细胞自噬 | 2016 诺奖核心，1988 年起开拓 | 核心页 |
| 1 | cell biology | 细胞生物学 | infobox Fields（Cell biologist） | 身份页 |
| 2 | molecular biology | 分子生物学 | metadata field_of_work 明载；ATG 基因体系 | 核心页 |
| 3 | yeast genetics | 酵母遗传学 | 突变筛选找出自噬必需基因 | 核心页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Mariko Ohsumi | 无向 | 妻子，帝京科学大学教授，多项论文合著者、研究合作者 |

**在世者诚实值说明（★ 本批次最简）**：2016 诺奖为大隅**独得**——**无 co-honored 边**；page.md 叙事极简、无具名导师/学生/合作者，relations=1 为诚实值，Review 勿以"关系太少"为由补边。

**不入库但提示词可叙述**：Kazutomo Imahori（frontmatter doctoral_advisor 有载，**page.md 正文无载——按纪律不入库**，本表留注防 Review 误补）；Christian de Duve（1963 年自噬术语命名者，文献渊源非个人关系，不建边）；Takeshige K / Baba M / Noda T / Mizushima N 等合著者（未展开人物叙事）；John Dirks、D. Lorne Tyrrell（颁奖礼合影人物）。

## 五、配色方案 【人物专属】

- **气质**：显微镜下酵母的微光、基础研究的素朴、诺奖奖章捐赠的慷慨
- **主色**：`#1B4D6B`（细胞深蓝——液泡与显微镜视野）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeAutophagy` 细胞自噬 — 深蓝 `#1B4D6B`
  - `badgeYeast` 酵母遗传学 — 青灰 `#0E7490`
  - `badgeBasic` 基础研究 — 赭金 `#B07D2B`
  - `badgeHonor` 荣誉传承 — 暗红 `#7A2430`
- **背景母题**：双层膜自噬体同心圆与酵母细胞轮廓，稀疏排布。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 细胞自噬机制的发现者 / Yoshinori Ohsumi b.1945 + 四色 badge + 右上头像 + 国籍行（Japan）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生、福冈出身、东京大学 BSc/DSci、洛克菲勒博士后、
    东工大/NIBB/综合研究大学院任职、诺奖 2016、核心领域）
03  核心贡献概览 — 酵母自噬形态学 / ATG 基因突变筛选 / 自噬体双层膜 / 哺乳动物同源化（LC3）
04  福冈少年与东大 (1945–1974) — 1967 BSci、1974 DSci，东京大学
05  洛克菲勒博士后 (1974–1977) — 纽约三年，回国任 research associate
06  东京大学讲师岁月 (1977–1988) — 1986 讲师、1988 副教授——"迟迟不到的教授职位"是耐心叙事
07  自噬之前的世界 — de Duve 1963 命名 autophagy、每年论文不足 20 篇的冷门、1988 年大隅起步
08  酵母中的自噬（核心贡献页）— 液泡观察、1992 Takeshige 等蛋白酶缺陷突变体论文
09  突变筛选与 ATG 基因（核心页）— 自噬缺陷突变体、必需基因鉴定、自噬体超微结构（1994）
10  分子机制的两套泛素样系统 — 1998 Nature 蛋白偶联系统、2000 LC3（哺乳动物 Apg8p 同源）、2001 综述
11  2016 诺奖：独得 — "for his discoveries of mechanisms for autophagy" 逐字呈现、第 25 位日本诺奖得主
12  荣誉与认可 — 富士产 2005、日本学士院奖 2006、朝日奖 2008、京都奖 2012、Gairdner 2015、
    Breakthrough 2017、文化勋章
13  妻子与实验室 — Mariko（帝京科学大学教授）合著者、Cell Biology Research Unit
14  遗产与结尾 — 2024 捐出诺奖奖章与证书给东京科学大学（"激励青年研究者"引语）+ 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 姓名与在世口径 | **yaml/入库用 manifest 形式 "Yoshinori Ohsumi"**；1945-02-09 生于福冈，**在世**——封面写 b.1945；日文名汉字"大隅 良典"，**勿与"大村智"（2015）混淆**——两位日本得主名字相近，封面副标题务必写清 |
| 独得诺奖 | 2016 为**单元奖**，获奖理由 "for **his** discoveries..."——勿画蛇添足写共享，无 co-honored 边 |
| Imahori 裁定 | frontmatter doctoral_advisor=Kazutomo Imahori，但 **page.md 正文全程无载**——按纪律不入库；本表留注防 Review 误补 |
| de Duve 不建边 | Christian de Duve 1963 年命名 autophagy，与 1988 年起步的大隅是文献传承非个人关系——不建 influence 边，只作背景叙述 |
| 引语红线 | page.md 仅一处引语：2024 年捐赠奖章时的 "serve as a strong stimulus for young researchers who seek to create the future"（明载可引原文+译文）；其余全篇无引语，禁编造 |
| 履历年份链 | 1967 BSci →1974 DSci →1974-77 洛克菲勒博士后 →1977 东大 research associate →1986 讲师 →1988 副教授 →1996 NIBB（冈崎）教授 →2004-09 兼综合研究大学院教授 →2009 三栖（NIBB/综合研究大学院名誉教授+东工大教授）→2014 退休后续任东工大创机研究所教授——勿串 |
| 机构更名 | 东京工业大学 2024 年后与东京医科齿科大学合并为 Institute of Science Tokyo（东京科学大学）——page.md 现行口径；叙述以"东京工业大学（现东京科学大学）"处理 |
| 1992 奠基论文 | Takeshige K 等 "Autophagy in yeast demonstrated with proteinase-deficient mutants..."（J Cell Biology 1992）为自噬形态学奠基——是大隅实验室代表作，作者非大隅本人第一作者，表述为"其团队论文" |
| LC3 归属 | LC3（哺乳动物 Apg8p 同源物）2000 年论文作者群含 Kabeya/Mizushima 等——表述"大隅团队/合作"口径，勿单归大隅一人 |
| 捐赠叙事 | 2024 年向东京科学大学捐赠诺贝尔奖章与证书，引语见上——作为结尾页素材 |
| 妻子关系 | Mariko 为帝京科学大学教授、"collaborated on his research，co-author of many academic papers"——spouse 边已承载，叙述中提"亦为科研合作者" |
| 荣誉年份 | 富士产 2005、学士院奖 2006、朝日 2008、京都奖 2012、Citation Laureate 2013、Gairdner/国际生物学奖/庆应医学奖/文化功臣/Rosenstiel 2015（五奖同年）、Wiley+Janssen+Nobel 2016、Breakthrough 2017、京都大学名誉博士 2017——2015 年五奖勿漏勿串 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| autophagy | 细胞自噬 | 获奖理由核心词，de Duve 1963 命名 |
| autophagosome | 自噬体 | 双层膜结构 |
| vacuole | （酵母）液泡 | 自噬物质降解场所 |
| ATG genes | 自噬相关基因（ATG） | 突变筛选鉴定的必需基因家族 |
| ubiquitin-like system | 泛素样系统 | Atg12/Atg8 两套偶联系统 |
| LC3 (Apg8p homologue) | LC3 蛋白 | 哺乳动物自噬标志物 |
| protease-deficient mutant | 蛋白酶缺陷突变体 | 1992 奠基论文的酵母株 |
| Saccharomyces cerevisiae | 酿酒酵母 | 模式生物，斜体 |
| starvation response | 饥饿响应 | 自噬的生理诱导条件 |
| selective autophagy | 选择性自噬 | 后期拓展方向（如过氧化物酶体自噬） |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Cinematic Experience**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：从每年不足 20 篇论文的冷门角落到独享一座诺奖，大隅的故事本身就是一部慢镜头的纪录片——显微镜下静默的酵母、三十年如一日的突变筛选、2024 年把奖章交回年轻研究者手中的收束；Cinematic Experience 的电影质感贴合这种"孤独坚守终成史诗"的叙事。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/21th_century/Yoshinori_Ohsumi/CinematicExperience.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
