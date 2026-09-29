# 医学家立传提示词（Françoise Barré-Sinoussi）

> OpenMedic 项目 · 21 世纪诺贝尔生理学或医学奖 2008 年得主（HIV 半奖之一） · 本文件是该人物的专属立传提示词，
> 按 9 节结构执行 Beamer 立传；数据库入库（fields/relations）已由批次完成，本文件第四/三节与 yaml 一致。

## 一、背景信息 【人物专属】

- **目标医学家**：Françoise Barré-Sinoussi（1947-07-30 生于巴黎，在世）
- **气质关键词**：**HIV 的共同发现者、反转录病毒"侦探"、全球艾滋病防治的科学家活动家** —— 2008 年获奖理由（逐字引用 medic/nobel_medicine_citations.json，与 Montagnier 共享同一句）：
  > "for their discovery of human immunodeficiency virus"
  > （因他们发现人类免疫缺陷病毒）
- **设计母题**：**反转录酶的信号曲线与红丝带（RT signal & red ribbon）**。培养液中逆转录酶活性曲线的陡升、红丝带的全球互助——"在培养皿里抓住瘟疫"的视觉隐喻。
- **本地 Wikipedia 路径**：medic/presentations/pages/21th_century/Françoise_Barré-Sinoussi/page.md
- **参考模板**：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）

## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章）

- 第 0/1/2/3 步按 **medic 路径**执行：事实基准 = `medic/presentations/pages/21th_century/Françoise_Barré-Sinoussi/page.md`；目录 `medic/presentations/21th_century/Françoise_Barré-Sinoussi/`；Makefile 改 `MAIN=Francoise_Barre-Sinoussi_zh`（文件名 ASCII 化，提示词目录名照 manifest）；肖像优先 images.txt 所列 Commons 图（Barré-Sinoussi in 2008），失败用装饰圆占位。
- 第 4/4.5 步（入库）**已完成**（第三、四节与 `MySQL/data/Françoise_Barré-Sinoussi.yaml` 一致，勿重复入库）。
- 第 5-9 步：配色 → 幻灯片 → Beamer → 布局检查（0 error、vbox≤10pt、hbox≤50pt、逐页目检）→ 史实审查（第七节）。

## 三、研究领域梳理 + 入库（rank 0-4 表）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | virology | 病毒学 | 职业主领域（infobox Fields） | 封面 |
| 1 | retrovirology | 反转录病毒学 | HIV/HTLV 与逆转录酶检测 | 发现页 |
| 2 | immunology | 免疫学 | 宿主先天免疫与 HIV 控制 | 研究页 |

## 四、社会关系梳理 + 入库（与 yaml 完全一致，已完成）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | Luc Montagnier | 无向 | Pasteur 单位前导师（former mentor），1983 同组发现 HIV |
| colleague | Jean-Claude Chermann | 无向 | 1983 共同分离 LAV（HIV-1） |
| co-honored | Luc Montagnier | 无向 | 2008 诺贝尔生理学或医学奖共享（发现 HIV） |
| co-honored | Harald zur Hausen | 无向 | 2008 诺奖同届共享（HPV 与 HIV 两半） |

> 对手方规范名：均无库内记录按 page.md 形式新建 stub；Montagnier 的 influence+co-honored 双行、与 zur Hausen 单行，均与 Montagnier 篇镜像幂等合并。**relations=4 为诚实值**（在世者，page.md 无配偶/门生记载）——立传时勿虚构补边。

## 五、配色方案

- **气质**：法兰西的理性 + 培养皿前的坚韧 + 为患者发声的温度
- **主色**：塞纳蓝 `#2A4B7C`（巴斯德研究所的严谨与法兰西底色）
- **诺奖香槟金**：`#D4AF37`
- **badge 四分类色**：
  - `badgeA` HIV 发现 — 艾滋红 `#A63A2B`（红丝带色）
  - `badgeB` 反转录病毒 — 反转录紫 `#5E4B8B`
  - `badgeC` 免疫与"精英控制者" — 免疫青 `#2E7D8C`
  - `badgeD` 全球公卫行动 — 行动橙 `#C97B2D`
- **背景母题**：低透明度逆转录酶活性曲线（上升脉冲）+ 散点红丝带弧线。

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — HIV 的共同发现者 / Françoise Barré-Sinoussi 1947– + badge + 右上头像 + 国籍行（France）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生年巴黎、巴黎大学、Pasteur 研究所 1970s 起、2008 诺奖、IAS 主席 2012-2016）
03  核心贡献概览 — HIV 分离 / 逆转录酶检测 / 精英控制者 / 全球抗艾网络
04  巴黎女孩与昆虫假期 (1947–1970s) — 童年观察昆虫动物、自认更想学医（误以为医学更贵更长）、寻实验室兼职近一年才进巴斯德
05  巴斯德与博士 (1970s–1974) — 兼职变全职、只去考试靠同学笔记反而考得更好（page.md 实载可转述）、1974 博士、NIH 实习后回 Montagnier 单元
06  新瘟疫叩门 (1981–1982) — 法国医生团到巴斯德发问"是否反转录病毒所致"、非 HTLV 的推理、1982-12 重度研究启动
07  1983：淋巴结活检中的逆转录酶 — 淋巴结活检策略（早期病例 CD4 未耗竭）、第二周检测到 RT 活性、加血供淋巴细胞救活培养、LAV 命名
08  Science 1983 与 LAV→HIV — 发现使诊断/治疗/政策成为可能（官方理由回扣）；命名演变 LAV→HIV
09  2008 诺贝尔奖 — 与"前导师" Montagnier 共享 HIV 半；同届 zur Hausen 得 HPV 半；官方理由全句
10  自己的实验室 (1988–2015) — 1992 反转录病毒生物学单元主任（2005 更名调控单元）、逆转录感染调控、HIV 疫苗与免疫治疗研究
11  精英控制者与基础-临床之桥 — 少数 HIV 阳性者无药控制复制、母婴传播、先天免疫；240+ 论文、250+ 国际会议
12  全球行动 — 越南/中非合作网络、WHO/UNAIDS 顾问、IAS 理事会 2006、主席 2012-2016、治愈战略为优先
13  为科学发声 — 2009 致教皇公开信（避孕套无效论抗议，page.md 明载一句带过）；2015 强制退休、2017 全退
14  荣誉 — 荣誉军团骑士→大军官（2006/2009/2013）、King Faisal 奖、Körber 奖、Time 1983 年度封面（2019 追授）
15  结尾（OpenMathAI 品牌口径）
```

## 七、特殊陷阱表（★ 核心）

| 陷阱 | 说明 |
|------|------|
| 两半结构 | 2008 = Barré-Sinoussi 与 Montagnier 共享 HIV 半（"their discovery"）+ zur Hausen 独享 HPV 半——勿写三人平分或她独得 |
| Montagnier 关系 | page.md 称 "her former mentor"（前导师/上级）；非学位导师——入库 influence，勿写博士导师（其 1974 博士导师未具名） |
| Chermann 角色 | 1983 分离工作是 Montagnier 单元团队行为，Chermann 为 page.md 点名合作者——勿略去，也勿写成三人均分诺奖（Chermann 未获奖） |
| 发明权叙事 | 检测到的是**逆转录酶活性**（确认反转录病毒的技术在她手上）——发现链：活检策略→RT 信号→加淋巴细胞救培养→LAV 命名 |
| 在世者留白 | 无配偶/子女/门生的 page.md 记载——relations=4 诚实值，立传勿虚构家庭页 |
| 政治与宗教 | 2009 致教皇公开信仅客观一句（page.md 明载）；超出 page.md 的 HIV 政策争议禁展开 |
| 退休节点 | 2015-08-31 强制退休（mandatory retirement）、2017 全退——两节点勿混 |
| 命名史 | 最初名 LAV（淋巴结病相关病毒）——先于 HIV 术语；"HIV 1983"指分离年份，命名在后 |
| 引语红线 | page.md 无整句直接引语——全部转述；不得杜撰"我们发现了艾滋病病毒"类原话 |
| 女性序数 | 勿写"第 X 位女性诺奖得主"之类序数（page.md 无载） |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| HIV / human immunodeficiency virus | 人类免疫缺陷病毒 | 原名 LAV |
| AIDS | 获得性免疫缺陷综合征 | 病症≠病毒 |
| reverse transcriptase | 逆转录酶 | 反转录病毒确认标志 |
| LAV | 淋巴结病相关病毒 | 1983 初名 |
| HTLV | 人 T 细胞白血病病毒 | 当时唯一已知反转录病毒，被排除 |
| elite suppressors / controllers | 精英控制者 | 无药控复制人群 |
| lymphadenopathy | 淋巴结病 | 早期取材指征 |
| IAS | 国际艾滋病学会 | 2012-2016 任主席 |

## 九、背景音乐选择

- **选定曲目**：**Winds Of Freedom** — Alex-Productions（manifest 预分配）
- **匹配理由**："自由之风"贴合其"从培养皿到全球行动"的公共科学家形象——发现病毒是为了让感染者获得诊断、治疗与尊严；开阔而坚定的曲式匹配她为科学与人道发声的一生。
- **本地路径**：music_audio/ 下 Alex-Productions Winds Of Freedom 曲目（执行时按 curated_tracks.md 对应文件复制到本目录）。
