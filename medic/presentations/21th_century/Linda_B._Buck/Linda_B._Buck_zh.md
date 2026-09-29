# 医学家立传提示词（Linda B. Buck）

> 本文件是 OpenMedic 项目 21 世纪诺贝尔生理学或医学奖 **2004 年得主 Linda B. Buck（琳达·巴克）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/21th_century/Linda_B._Buck/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Linda Brown Buck（1947-01-29 生于西雅图，**在世**），美国生物学家，Fred Hutchinson 癌症研究中心 Basic Sciences Division 正式成员
- **气质关键词**：**千种气味受体基因的发现者、西雅图首位诺奖女性校友、嗅觉地图的测绘者**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 2004 条目，Axel/Buck 两人共享）：
  > "for their discoveries of odorant receptors and the organization of the olfactory system"（因其发现气味受体并阐明嗅觉系统的组织方式）
- **设计母题**：**鼻腔里的气味地图（the organization of odor receptor inputs）**——不同气味受体的输入在鼻腔中有序排布；用「鼻形轮廓内渐次点亮的受体位点」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Linda_B._Buck/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/21th_century/Linda_B._Buck/`（世纪目录一律 `21th_century`，肖像见 images.txt；目录名含点号 `Linda_B._Buck`，Makefile/tex 文件名保持一致即可）。Makefile 复制后设 `MAIN=Linda_B._Buck_zh`、`VIDEO_NAME=Linda_B._Buck_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。**在世者注意**：只写出生年；relations 数量为诚实值。

## 三、研究领域梳理 + 入库 【人物专属】

**Buck 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | olfaction | 嗅觉 | 气味受体基因家族与嗅觉输入组织，2004 诺奖核心 | 核心页 |
| 1 | neuroscience | 神经科学 | 气味与信息素如何被鼻子检测、被大脑解读 | 核心页 |
| 2 | molecular biology | 分子生物学 | 基因克隆与受体编码基因分析 | 核心页 |
| 3 | immunology | 免疫学（博士方向） | PhD 为免疫学（IgD/Lyb-2，B 淋巴细胞） | 教育页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Ellen Vitetta | 对方 → 导师 | 得克萨斯大学西南医学中心博士导师（1980，免疫学） |
| advisor-student | Benvenuto Pernis | 对方 → 博士后导师 | 哥伦比亚大学博士后（1980-1982） |
| advisor-student | Richard Axel | 对方 → 博士后导师 | 哥伦比亚大学 Axel 实验室博士后（1982 起），1991 年合作克隆气味受体 |
| co-honored | Richard Axel | 无向 | 2004 诺贝尔生理学或医学奖共享（气味受体与嗅觉系统的组织） |
| spouse | Roger Brent | 无向 | 生物学家，1994 相识，2006 结婚 |
| controversy | Zhihua Zou | 无向 | 合作者造假致三篇论文撤稿（Nature 2008、Science 2010、PNAS 2010） |

**在世者诚实值说明**：Buck 在世且 page.md 叙事精简，relations=6 为诚实值，勿在 Review 时"补足"。

**不入库但提示词可叙述**：Sol Snyder 团队（约翰斯·霍普金斯，其论文触发 Buck 转向嗅觉——是文献启发非个人关系）；父母（父亲电机工程师，爱尔兰裔；母亲瑞典裔主妇）；两个姐妹；Richard Axel 亦是 infobox Other academic advisors 之一（已由 advisor-student 边承载）。

## 五、配色方案 【人物专属】

- **气质**：西雅图的清冽、嗅觉地图的细腻、首位女性诺奖校友的沉静突破
- **主色**：`#6E2B4E`（酒红紫——嗅觉的感性与西北雨林的沉静）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeRecep` 气味受体基因 — 酒红紫 `#6E2B4E`
  - `badgeMap` 嗅觉地图 — 深青 `#14647E`
  - `badgeImmune` 免疫学起点 — 青灰 `#0E7490`
  - `badgeHonor` 荣誉传承 — 琥珀 `#B07D2B`
- **背景母题**：鼻形轮廓内渐次点亮的受体位点与信号回路。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 千种气味受体的发现者 / Linda B. Buck b.1947 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生、西雅图出身、华盛顿大学/UT 西南医学中心、
    Fred Hutchinson/HHMI/哈佛任职轨迹、诺奖 2004、核心领域）
03  核心贡献概览 — 气味受体基因家族 / GPCR 归属 / 嗅觉输入的组织 / 信息素与气味检测
04  西雅图少女 (1947–1975) — 三姐妹中的老二、父修电机的家庭、华盛顿大学心理+微生物双学位
05  免疫学博士 (1975–1980) — UT 西南医学中心、Ellen Vitetta 门下、IgD 与 Lyb-2 论文
06  哥伦比亚博士后 (1980–1982) — Pernis 实验室起步
07  转向嗅觉 (1982) — 读到 Sol Snyder 组论文后决意从分子层面绘制嗅觉通路；加入 Axel 实验室
08  1991：克隆气味受体基因家族（核心贡献页）— 大鼠 DNA、>1000 个基因、G 蛋白偶联受体
09  哈佛与嗅觉地图 (1991–1993) — 神经生物学助理教授、1993 年发表嗅觉输入在鼻内的组织方式
10  2004 诺奖：与 Axel 共享 — 获奖理由逐字呈现、从博士后到共享诺奖的十七年
11  Fred Hutchinson 岁月 — 西雅图回响、UW 兼职教授、HHMI 研究员
12  荣誉与认可 — Takasago 1992、Rosenstiel 1996、Perl-UNC 2002、Gairdner 2003、NAS 2003、ForMemRS 2015、
    哈佛荣誉博士 2015、UW 首位女性诺奖校友
13  科学诚实的代价 — 三篇撤稿事件（合作者 Zou 造假）、Buck 主动撤稿的处置
14  遗产与结尾 — 嗅觉分子时代的开启 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 姓名与在世口径 | **yaml/入库用 manifest 形式 "Linda B. Buck"**；1947-01-29 生于西雅图，**在世**——封面写 b.1947，不得写卒年 |
| 2004 共享双边 | 与 Axel 有 advisor-student（对方是博士后导师）+co-honored 两条边并行，勿合并；叙事重点是 **Buck 在 Axel 实验室做出关键发现**，1991 论文署名 Buck and Axel |
| 诺奖功劳口径 | 1991 年克隆气味受体是 Buck（在 Axel 实验室）完成的 landmark 工作——勿写成 Axel 指导下的次要贡献，也勿写成 Buck 单独完成（共享奖） |
| 荣誉细节防混淆 | 1996 年一年内获 Unilever Science Award、R.H. Wright Award、Lewis S. Rosenstiel Award 三奖（page.md 列于 Awards 段，infobox 只载 Rosenstiel）——以正文为准可写三项；Takasago 1992 |
| 学位与导师 | BS 华盛顿大学 1975（心理+微生物）；PhD UT Southwestern 1980，导师 Ellen Vitetta；infobox Other academic advisors 含 Benvenuto Pernis 与 Richard Axel——三条指导关系各有其位 |
| 撤稿事件口径 | 三篇论文（Nature 2001/Science 2006/PNAS 2005）因**第一作者兼合作者 Zhihua Zou 造假**被撤（2008/2010/2010）——责任在 Zou，Buck 主动撤稿；第 13 页可客观呈现，勿渲染、勿归责 Buck |
| Fields 防错 | page.md infobox Fields 栏错写 "Rhinologist"（鼻科医生）——**以正文为准**（biology/neuroscience），勿照抄 infobox |
| UW 首位 | "第一位获诺奖的华盛顿大学（校友）女性"（first female University of Washington alumnus to win the Nobel Prize）——page.md 明载可写；勿扩写成"华盛顿州首位" |
| spouse 细节 | Roger Brent 亦为生物学家，1994 相识、2006 结婚——两个年份勿混 |
| 国籍 | metadata 仅 United States，无冲突 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| odorant receptor | 气味受体 | 获奖理由核心词 |
| olfactory system | 嗅觉系统 | 获奖理由另一半 |
| olfactory receptor gene family | 气味受体基因家族 | >1000 个成员 |
| G protein-coupled receptor (GPCR) | G 蛋白偶联受体 | 气味受体归属家族 |
| organization of odor receptor inputs | 气味受体输入的组织方式 | 1993 年论文主题 |
| pheromone | 信息素 | Buck 研究兴趣之一 |
| IgD / Lyb-2 | 免疫球蛋白 D / Lyb-2 抗原 | 博士论文对象（B 淋巴细胞） |
| retraction | 撤稿 | 三篇论文因合作者造假撤回 |
| Fred Hutchinson Cancer Research Center | 弗雷德·哈金森癌症研究中心 | 现职机构 |
| ForMemRS | 皇家学会外籍院士 | 2015 当选 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Savage**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：气味是动物世界最原始的感官——从信息素到恐惧的气味信号，Buck 破译的正是这套古老而野性的化学语言；Savage 的原始张力对应嗅觉系统亿万年演化的本能力量，也对应她在男性主导的领域里一锤定音的锋锐。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/21th_century/Linda_B._Buck/Savage.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
