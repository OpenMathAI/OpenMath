# 医学家立传提示词（Bengt I. Samuelsson）

> 本文件是 OpenMedic 项目「20 世纪诺贝尔生理学或医学奖得主人物专属立传提示词」。
> 目标人物：Bengt I. Samuelsson（1982 年诺贝尔生理学或医学奖得主，瑞典）。
> 用途：指导后续 Beamer 立传（15 页）与配套视频制作；事实基准为本地 Wikipedia 页面
> `medic/presentations/pages/20th_century/Bengt_I._Samuelsson/page.md`（下称 page.md）。
> 社会关系与研究领域已按本文件第三、四节入库 greatminds 库（yaml 与本文件完全一致）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Bengt Ingemar Samuelsson（本特·英格马·萨穆埃尔松，1934-05-21 哈尔姆斯塔德 ~ 2024-07-05 默勒，享年 90 岁）
- **气质关键词**：**前列腺素下游世界的开拓者、凝血噁烷与白三烯的发现者、卡罗林斯卡医学院院长与诺贝尔基金会主席** —— 1982 年诺贝尔生理学或医学奖获奖理由（逐字引自 medic/nobel_medicine_citations.json，与 Bergström、Vane 三人共享）：
  > "for their discoveries concerning prostaglandins and related biologically active substances"
  > （因其关于前列腺素及相关生物活性物质的发现）
- **设计母题**：**「花生四烯酸的分支河流」**。花生四烯酸经级联酶反应分岔出前列腺素、凝血噁烷、白三烯三条支流——视觉隐喻：一条主干河流分出三条染色支流。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Bengt_I._Samuelsson/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 **medic 路径**执行：页面用 `medic/presentations/pages/20th_century/Bengt_I._Samuelsson/`，成目录 `medic/presentations/20th_century/Bengt_I._Samuelsson/`，Makefile 复制后设 `MAIN=Bengt_I._Samuelsson_zh`、`VIDEO_NAME=Bengt_I._Samuelsson_zh`，BGM 见第九节。
> 第 4 步（研究领域）与第 4.5 步（社会关系）**已完成入库**，见第三、四节。
> 数据库：本人记录复用库内既有 stub（id=3512）UPD 回填 QID Q295768，`has_social_data=1`；`has_biography` 待 Beamer 立传完成后置 1。

## 三、研究领域梳理 + 入库（已完成）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biochemistry | 生物化学 | 花生四烯酸代谢级联，1982 诺奖核心 | 总览页 |
| 1 | prostaglandins | 前列腺素 | 与 Bergström 的结构接力、体内调控系统 | 前列腺素页 |
| 2 | arachidonic acid metabolism | 花生四烯酸代谢 | 内过氧化物/凝血噁烷/白三烯的鉴定 | 下游产物页 |

## 四、社会关系梳理 + 入库（已完成，与 MySQL/data/Bengt_I._Samuelsson.yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Sune Bergström | — | 1982 诺贝尔生理学或医学奖三人共享（前列腺素等） |
| co-honored | John Vane | — | 1982 诺贝尔生理学或医学奖三人共享（前列腺素等） |
| collaborator | Sune Bergström | — | 前列腺素结构研究长期师徒搭档（frontmatter 另载其为博士导师） |

> 说明：本篇 page.md 极简（全文约 60 行），按「禁编造」纪律只建 3 条边。博士导师关系仅 frontmatter 明载、正文只载「与 Bergström 共同的结构工作」——按 metadata-only 纪律建 collaborator 承载合作事实（note 中注明 frontmatter 另载导师身份），不建 advisor-student 边（Richet-Robin 纪律）。无配偶/子女叙事不入库；药企董事（Pharmacia/NicOx/Schering）与 HealthCap 顾问为履历叙事不入库。

## 五、配色方案 【人物专属】

- **气质**：青年接棒者的锐气、级联化学的层次感、卡罗林斯卡的行政担当
- **主色**：级联青碧 `#1E7A5C`（三条支流的汇流色）
- **诺奖色**：香槟金（奖章/年份徽章专用）
- **四分类色（badgeA-D）**：
  - `badgeA` 生物化学 — 代谢青 `#1F7A6D`
  - `badgeB` 前列腺素 — 信使橙 `#C08A2E`
  - `badgeC` 花生四烯酸代谢 — 分支蓝 `#33637D`
  - `badgeD` 临床转化 — 血栓红 `#A83A4A`
- **背景母题**：河流分岔图（主干→三支流）与环氧化合物分子线稿，低透明度铺底

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input medic/presentations/cover/）
01  封面 — 花生四烯酸分支河流的开拓者 / Bengt I. Samuelsson 1934–2024 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、教育、任职、荣誉、核心领域）
03  核心贡献概览 — 内过氧化物 / 凝血噁烷 / 白三烯 / 卡罗林斯卡与诺奖基金会
04  哈尔姆斯塔德-隆德 (1934–1960s) — 西南港城出身、隆德大学起步
05  卡罗林斯卡：Bergström 门下 — 胆固醇代谢起步、转入前列腺素结构接力（与 Bergström 共同的结构工作）
06  前列腺素的结构接力（核心页）— 承 Bergström 的分离纯化、结构测定到功能追问
07  花生四烯酸的分支河流（核心页）— 内过氧化物（endoperoxides）、凝血噁烷（thromboxanes）、白三烯（leukotrienes）三支流的鉴定
08  1982 诺贝尔奖（核心页）— citation 原文、三人共享、诺奖演讲 From Studies of Biochemical Mechanisms to Novel Biological Mediators
09  体内调控系统 — 「细胞的控制系统」访谈引语（英文原文+译文）、药物开发的无穷可能
10  临床影响 — 血栓/炎症/过敏三大方向；1981-95 年每年约 3000 篇文献的领域爆发
11  卡罗林斯卡院长 (1983–1995) — 1973 医学生理化学教授、医学院掌门十二年
12  诺贝尔基金会主席 (1993–2005) — 基金会掌门十二年、学界与产业界桥梁（药企董事经历一句带过）
13  荣誉链 — Horwitz 1975（与 Bergström 同获）· Rosenstiel 1980 · Wieland 1981 · Nobel 1982 · ForMemRS 1990
14  遗产 — 前列腺素家族药物开发的理论基石；2024-07-05 辞世（享年 90）
15  结尾
```

## 七、特殊陷阱表（★ 执行 Beamer 前必读）

| # | 陷阱 | 裁定 |
|---|------|------|
| 1 | 获奖理由表述 | 逐字用 citation 原文 "for their discoveries concerning prostaglandins and related biologically active substances"（their 三人共享同一理由） |
| 2 | 师承裁定 | 博士导师仅 frontmatter 载（Sune Bergström），正文只载「along with」的结构合作——按 metadata-only 纪律建 collaborator 承载（note 注明 frontmatter 另载导师身份），不建 advisor-student 边；若 Review 认可 frontmatter+长期师徒语境可升级 |
| 3 | 页面极简 | 本篇 page.md 全文约 60 行——禁编造生平；骨架用「结构接力→三支流鉴定→行政生涯→荣誉链」四个真实支点 |
| 4 | 三支流归属 | 内过氧化物/凝血噁烷/白三烯的鉴定是 Samuelsson 组的核心贡献（page 明载「his research has led to the identification」）——与 Bergström 的上游分离、Vane 的阿司匹林机理三分工勿混 |
| 5 | 两条时间线 | 「1981-95 年每年约 3000 篇前列腺素相关论文」是领域爆发注脚，可作一帧数据 |
| 6 | 引语红线 | 「It's a control system for the cells...」访谈引语有英文原文可引；其余叙事无直接引语 |
| 7 | 产业关联 | Pharmacia/NicOx/Schering 董事与 HealthCap 顾问——一句带过，不展开商业细节 |
| 8 | 死亡日期 | 1934-05-21 ~ 2024-07-05（默勒，享年 90）——2024 年逝世为 page.md 明载，勿按旧资料写在世 |
| 9 | 与 Bergström 篇的镜像 | 师徒二人同奖（1975 Horwitz、1982 Nobel）——两篇以「接力棒」意象互为呼应但叙事视角不同（Bergström 篇主打上游分离与本篇主打下游鉴定） |
| 10 | metadata 冲突 | education 有 Lund/Stockholm/Karolinska 多值；正文写隆德求学+卡罗林斯卡执教——身份页取隆德（学士语境）与卡罗林斯卡（教授语境）并列 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| prostaglandin endoperoxides | 前列腺素内过氧化物 | PGG2/PGH2 级联中间体 |
| thromboxane | 凝血噁烷（血栓素） | 血小板聚集相关，勿译「血栓烷」 inconsistently |
| leukotriene | 白三烯 | 过敏与炎症介质 |
| arachidonic acid | 花生四烯酸 | 级联起点 |
| cholesterol metabolism | 胆固醇代谢 | 其研究起点 |
| endoperoxide | 内过氧化物 | — |
| Karolinska Institute | 卡罗林斯卡医学院 | 1983-95 院长 |
| Nobel Foundation | 诺贝尔基金会 | 1993-2005 主席 |
| Heinrich Wieland Prize | 海因里希·维兰德奖 | 1981 |
| ForMemRS | 皇家学会外籍会员 | 1990 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Daylight** — Alex-Productions（manifest 预分配）
- **匹配理由**：
  - 「白昼」匹配「分支河流」的清澈意象——把花生四烯酸的暗河分梳为三条清晰支流
  - 明快节奏契合青年接棒者形象：39 岁教授、48 岁诺奖、49 岁院长，一路白昼行军
- **备选**（未采用）：The Flow of Time（本批 Bergström 已用，师徒组区分）、Expedition（batch-11 Wiesel 已用）
- **本地路径**：按 music_audio/ 内 Alex-Productions Daylight 曲目复制至 `medic/presentations/20th_century/Bengt_I._Samuelsson/Daylight.wav`，ffmpeg `-shortest` 对齐
