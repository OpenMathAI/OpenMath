# 医学家立传提示词（Günter Blobel）

> 本文件是 OpenMedic 项目「20 世纪诺贝尔生理学或医学奖得主人物专属立传提示词」。
> 目标人物：Günter Blobel（1999 年诺贝尔生理学或医学奖得主，美国）。
> 用途：指导后续 Beamer 立传（15 页）与配套视频制作；事实基准为本地 Wikipedia 页面
> `medic/presentations/pages/20th_century/Günter_Blobel/page.md`（下称 page.md）。
> 社会关系与研究领域已按本文件第三、四节入库 greatminds 库（yaml 与本文件完全一致）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Günter Blobel（京特·布洛贝尔，1936-05-21 西里西亚瓦尔特斯多夫（今波兰） ~ 2018-02-18 纽约曼哈顿，享年 81 岁）
- **气质关键词**：**蛋白质「地址标签」（信号肽）的发现者、把细胞生物学带入分子时代的人、倾尽诺奖奖金重建德累斯顿的赤子** —— 1999 年诺贝尔生理学或医学奖获奖理由（逐字引自 medic/nobel_medicine_citations.json，独享）：
  > "for the discovery that proteins have intrinsic signals that govern their transport and localization in the cell"
  > （因其发现蛋白质具有内在信号，调控其在细胞内的运输与定位）
- **设计母题**：**「地址标签」**。每条新合成的蛋白质都带着一串信号肽邮编寄往细胞内的正确地址——视觉隐喻：细胞剖面里贴着条码标签的蛋白质包裹流向各器室。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Günter_Blobel/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 **medic 路径**执行：页面用 `medic/presentations/pages/20th_century/Günter_Blobel/`，成目录 `medic/presentations/20th_century/Günter_Blobel/`，Makefile 复制后设 `MAIN=Günter_Blobel_zh`、`VIDEO_NAME=Günter_Blobel_zh`，BGM 见第九节。
> 第 4 步（研究领域）与第 4.5 步（社会关系）**已完成入库**，见第三、四节。
> 数据库：本人记录复用库内既有 stub（id=6104）UPD 回填 QID Q60108，`has_social_data=1`；`has_biography` 待 Beamer 立传完成后置 1。

## 三、研究领域梳理 + 入库（已完成）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | cell biology | 细胞生物学 | 蛋白质靶向运输与定位，1999 诺奖核心 | 总览页 |
| 1 | protein targeting | 蛋白质靶向运输 | 信号肽假说、信号识别颗粒（SRP） | 信号肽页 |
| 2 | molecular biology | 分子生物学 | 分级分离与体外重建的功能复合体方法学 | 方法页 |

## 四、社会关系梳理 + 入库（已完成，与 MySQL/data/Günter_Blobel.yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Van R. Potter | 师 | 威斯康星麦迪逊其实验室博士训练，1967 年获 PhD |
| advisor-student | George Emil Palade | 师 | 洛克菲勒博士后导师（他批已建同边） |
| advisor-student | Peter Walter | 生 | 博士生（infobox 明载） |
| advisor-student | David J. Anderson | 生 | 其他知名学生（infobox 明载） |
| advisor-student | André Hoelz | 生 | 其他知名学生（infobox 明载） |
| spouse | Laura Maioglio | — | 妻，纽约老牌餐馆 Barbetta 所有者 |

> 说明：博士训练（Potter 实验室，body 明载）与博士后导师（Palade，frontmatter doctoral_advisor+infobox academic advisor+body「postdoctoral fellow with Palade」三载一致）分建两条师生边；Palade 边已由其本人批次先建（11836）幂等去重。三个学生仅 infobox 明载（沿 Eccles 篇 Rall/Kuffler/Llinás 先例入库并标注）。姐姐 1945 年死于列车轰炸、兄长未具名——不入库。

## 五、配色方案 【人物专属】

- **气质**：西里西亚流亡者的乡愁、分子时代的开创者、古典主义的重建者
- **主色**：信号肽靛蓝 `#2B4A8C`（分子邮编的深蓝）
- **诺奖色**：香槟金（奖章/年份徽章专用）
- **四分类色（badgeA-D）**：
  - `badgeA` 细胞生物学 — 器室青 `#1F7A6D`
  - `badgeB` 蛋白质靶向 — 邮签橙 `#C08A2E`
  - `badgeC` 信号肽 — 序列紫 `#5B4E8E`
  - `badgeD` 德累斯顿重建 — 石灰岩金 `#B8A26A`
- **背景母题**：细胞器室剖面与贴标签的蛋白质包裹流、圣母教堂穹顶线稿遥相呼应，低透明度铺底

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input medic/presentations/cover/）
01  封面 — 蛋白质地址标签的发现者 / Günter Blobel 1936–2018 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像（2008 照）+ 右信息网格（生卒、教育、任职、家庭、荣誉、核心领域）
03  核心贡献概览 — 信号肽 / 蛋白质靶向 / SRP / 基因门控假说
04  西里西亚与逃亡 (1936–1945) — 普鲁士下西里西亚出生、1945 年 1 月举家逃往德累斯顿、姐姐死于列车轰炸
05  战后与医学 (1945–1960) — 弗赖贝格中学、图宾根大学 1960 医学毕业、两年实习
06  威斯康星：Potter 实验室 (1962–1967)（核心页）— 随兄赴麦迪逊、1967 PhD
07  洛克菲勒：Palade 门下 (1968–)（核心页）— 博士后、即获教职、分级分离与体外重建方法学
08  信号肽假说与 SRP（核心页）— 「地址标签」模型、信号识别颗粒、蛋白质靶向机制
09  1999 诺贝尔奖（核心页）— citation 原文（独享）、「把细胞生物学带入分子时代」的评价
10  基因门控假说 — 晚年理论贡献（gene gating hypothesis）
11  德累斯顿的赤子 — Friends of Dresden 创立（1994）、诺奖奖金全数捐赠、圣母教堂重建 (2005) 与新犹太会堂
12  莱比锡的呼吁 — Paulinerkirche 重建之倡、「德国文化史的圣殿」引语（原文+译文）
13  荣誉链（上） — NAS 分子生物学奖 1978 · Gairdner 1982 · Warburg 1983 · Wilson Medal 1986 · Horwitz 1987
14  荣誉链（下）与遗产 — Lasker 1993 · King Faisal 1996 · Nobel 1999 · Pour le Mérite 2001；细胞生物学的分子时代
15  结尾
```

## 七、特殊陷阱表（★ 执行 Beamer 前必读）

| # | 陷阱 | 裁定 |
|---|------|------|
| 1 | 获奖理由表述 | 逐字用 citation 原文 "for the discovery that proteins have intrinsic signals that govern their transport and localization in the cell"——**独享**，无 co-honored 边 |
| 2 | 两位导师分层 | Potter（威斯康星 PhD 实验室）与 Palade（洛克菲勒博士后；frontmatter/infobox 亦列为 advisor）——两条师生边分别建、note 分清 PhD 与 postdoc 属性；勿写成同一站 |
| 3 | 双重国籍 | 出生地为时属德国的西里西亚（今波兰 Niegosławice）；frontmatter nationality 含 Nazi Germany 噪声——yaml 按 Nobel 口径 United States，正文叙述「德裔美国人、西里西亚出生」 |
| 4 | 德累斯顿叙事 | 1945 逃亡与德累斯顿大轰炸的童年记忆、姐姐之死、战后诺奖奖金全捐重建——page.md 明载，克制叙述其个人史与公益，不评价战争责任议题 |
| 5 | 姐姐之死 | 死于 1945 年列车空袭——page 明载可写一句，勿渲染细节 |
| 6 | 引语红线 | Paulinerkirche「this is a shrine of German cultural history...」有英文原文可引；「ushered cell biology into the molecular age」为转述评价，注明出处 |
| 7 | 学生 | Peter Walter/Anderson/Hoelz 仅 infobox 明载——沿 Eccles 篇先例入库并标注；若 Review 认为证据不足可降级文字 |
| 8 | 家庭 | 妻 Laura Maioglio（Barbetta 餐厅所有者）建 spouse 边；兄姐未具名不入库 |
| 9 | 引语红线 2 | 本人无其他直接引语；歌剧与建筑的热爱为叙述性侧写 |
| 10 | metadata 冲突 | frontmatter doctoral_advisor=Palade 与 body 的 PhD 语境（Potter）有张力——按 body+infobox 双证分别建边并注明分层，Review 复核 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| signal peptide | 信号肽 | 「地址标签」隐喻的本体 |
| protein targeting | 蛋白质靶向运输 | 诺奖理由核心 |
| signal recognition particle (SRP) | 信号识别颗粒 | 靶向机制的组分 |
| gene gating hypothesis | 基因门控假说 | 晚年理论 |
| translocation | 转位 | 蛋白过膜运输 |
| in vitro reconstitution | 体外重建 | 其方法学标志 |
| Frauenkirche | 德累斯顿圣母教堂 | 2005 年重建完成 |
| Friends of Dresden | 德累斯顿之友 | 1994 创立 |
| Pour le Mérite | 功勋勋章 | 2001（科学艺术类） |
| E.B. Wilson Medal | 威尔逊奖章 | 美国细胞生物学最高奖 1986 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Winds Of Freedom** — Alex-Productions（manifest 预分配）
- **匹配理由**：
  - 「自由之风」匹配其人生底色——从东线逃亡的难民少年到自由女神下的科学家，再到倾囊重建自由之城的赤子
  - 辽阔而带乡愁的旋律贴合「地址标签」母题：每个蛋白质都要找到归属，每个人亦然
- **备选**（未采用）：Last Hope（本批 Carlsson 已用）、Winds 类已避开重复
- **本地路径**：按 music_audio/ 内 Alex-Productions Winds Of Freedom 曲目复制至 `medic/presentations/20th_century/Günter_Blobel/Winds_Of_Freedom.wav`，ffmpeg `-shortest` 对齐
