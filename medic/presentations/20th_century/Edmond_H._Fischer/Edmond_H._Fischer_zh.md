# 医学家立传提示词（Edmond H. Fischer）

> **OpenMedic** 项目 · 20 世纪诺贝尔生理学或医学奖 **1992 年**得主（与 Edwin G. Krebs 共享）。
> 本文件是 Fischer 的「人物专属立传提示词」，供后续 Beamer 立传 agent 直接使用；配套数据已按第三、四节入库 greatminds 库。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Edmond Henri Fischer（1920-04-06 ~ 2021-08-27，享年 101 岁），瑞士裔美国生物化学家
- **气质关键词**：**可逆蛋白磷酸化的共同发现者、生于上海的日内瓦钢琴家、最年长的在世诺奖得主（至 2021）** —— 1992 诺贝尔生理学或医学奖获奖理由（官方原文，逐字引用）：
  > "for their discoveries concerning reversible protein phosphorylation as a biological regulatory mechanism"（因其关于可逆蛋白磷酸化作为生物调控机制的发现）
- **设计母题**：**生命的开关（the phosphorylation switch）**。激酶装上磷酸、磷酸酶卸下磷酸——以「蛋白分子上一开一关的磷酸小锁」作为视觉隐喻。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Edmond_H._Fischer/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `Physicist_Bio_Prompt_Template.md` 第三章八步流程：下载核对 → 建目录 → 复制 Makefile → 收集图片 → 研究领域入库 → 社会关系入库 → 编写 Beamer → 布局检查 + 史实审查。
> **第 0/1/2/3 步按 medic 路径执行**：页面用 `medic/presentations/pages/20th_century/Edmond_H._Fischer/`；Makefile 复制后设 `MAIN=Edmond_H_Fischer_zh`（宏名禁句点，文件名保持 manifest 原名）；BGM 复制到本目录（见第九节）。
> 数据库两步（第 4/4.5 步）**已完成**，见第三、四节；执行 agent 只需做 Beamer 与目检。

## 三、研究领域梳理 + 入库 【已入库，与 yaml 完全一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biochemistry | 生物化学 | 1992 诺奖核心：可逆蛋白磷酸化 | 核心页 |
| 1 | cell signaling | 细胞信号 | 磷酸化开关与细胞通讯 | 核心页 |
| 2 | enzymology | 酶学 | 糖原磷酸化酶、α-淀粉酶博士论文 | 研究页 |

## 四、社会关系梳理 + 入库 【已入库，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Edwin G. Krebs | 无向 | 1992 诺贝尔生理学或医学奖共享（可逆蛋白磷酸化） |
| advisor-student | Kurt Heinrich Meyer | 师→生（博士导师） | 日内瓦大学多糖结构门下作 α-淀粉酶论文（1947） |
| spouse | Nelly Gagnaux | 无向 | 1948 结婚，1961 卒 |
| spouse | Beverly Bullock | 无向 | 1963 结婚，2006 卒 |

**方向约定**：`advisor-student` + `direction: advisor` = 对方是导师；其余无向（from<to 自动归一）。

## 五、配色方案 【人物专属】

- **气质**：上海童年与瑞士寄宿的流丽、钢琴家的优雅、101 岁一生的从容
- **主色**：`#6B4A8C`（日内瓦紫，音乐与生化）
- **香槟金**：`#D4B26A`（诺奖色）
- **badgeA-D 四分类色**：`badgePhos` 磷酸化开关 — 磷酸橙 `#D07B2A`；`badgeKinase` 激酶/磷酸酶 — 酶青 `#1B7A6B`；`badgeShanghai` 上海童年 — 外滩金 `#A8752F`；`badgeUW` 华盛顿大学岁月 — 常青绿 `#2E5E4E`
- **背景母题**：浅紫底上蛋白分子剪影，其上磷酸小锁一开一关成对出现，错落连缀。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 生命开关的发现者 / Edmond H. Fischer 1920–2021 + 四色 badge + 右上肖像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、上海/瑞士寄宿、日内瓦大学、华盛顿大学、荣誉）
03  核心贡献概览 — 可逆磷酸化 / 激酶-磷酸酶循环 / 糖原磷酸化酶 / 疾病意义
04  上海国际租界的童年 (1920–1927) — 奥地利犹太律师之父、法国母亲、外祖父创《中国法兰西报》
05  瑞士寄宿与钢琴梦 (1927–1940) — La Châtaigneraie 寄宿学校、登山滑雪、日内瓦音乐学院钢琴录取
06  日内瓦与 Meyer 门下 (1940–1950) — 父死于结核转向微生物学又改化学、1947 α-淀粉酶博士
07  西雅图的选择 (1950) — 原定加州理工、意外获华盛顿大学教职、「西雅图像瑞士」
08  与 Krebs 会师（核心贡献页）— 同系同问题：肌肉的能量从何而来、肌型 vs 薯型磷酸化酶之异
09  磷酸化-水解循环 — 激酶自 ATP 取磷酸装上蛋白、磷酸酶卸下还原——激素与钙触发的开关
10  迟到的承认 (1955→) — 1955 年发现未获重视、终成细胞通讯的基本机制（癌/糖尿病/心脏病关键）
11  1992 诺贝尔奖 — 与 Krebs 共享、ForMemRS 2010、1972 美艺科学院/1973 NAS
12  荣誉集 — Werner 奖（瑞士化学会）、Montpellier/巴塞尔荣誉博士、World Cultural Council 荣誉主席 2007-14
13  钢琴与飞行 — 贝多芬/莫扎特奏鸣曲、私人飞行执照——人文侧面
14  遗产：磷酸化药物的世纪 — 现代多类药物以其机制为基础；2021-08-27 卒于西雅图、享年 101
15  结尾
```

## 七、特殊陷阱表 【★ 核心，从 page.md 提炼】

| 陷阱 | 说明 |
|------|------|
| 生卒日 | 1920-04-06 生于上海公共租界（父奥地利犹太律师、母法国人）；2021-08-27 卒于西雅图，享年 101——卒时为最年长在世诺奖得主（正文明载） |
| 获奖理由 | "for their discoveries concerning reversible protein phosphorylation as a biological regulatory mechanism"——**their**（与 Krebs 共享） |
| 国籍口径 | manifest/Nobel 官方为 United States（citation country 作 Switzerland United States）；frontmatter 三值 Switzerland/US/Italy——行文「瑞士裔美国」，yaml 用 United States |
| 钢琴支线 | 日内瓦音乐学院钢琴录取、曾考虑职业演奏、晚年常奏贝多芬/莫扎特——人文亮点，勿挤掉科学主线 |
| 择业之变 | 本想学微生物学（受 Pasteur 感召+父亲死于结核）、被劝学化学——动机链可写 |
| 与 Krebs 会合点 | 到西雅图半年后得知同校 Krebs 研究同类问题：肌肉收缩能量来源；肌型（需额外化学因子）vs 薯型（不需）磷酸化酶之差是突破口 |
| Cori 的位置 | 糖原磷酸化酶系 Cori 夫妇 1947 诺奖发现——本篇作为背景引用，Fischer/Krebs 是**机制**发现者，勿混 |
| 1955 冷遇 | 「importance not fully recognised in 1955」——迟到的承认是叙事张力 |
| 两位配偶 | Nelly Gagnaux（1948-1961 卒）、Beverly Bullock（1963-2006 卒）——各建 spouse 一行 |
| 引语 | 本页正文无直接引语——引号内不得出现「原话」 |

## 八、术语清单 【6-10 条】

| 英文 | 中文 | 风险点 |
|------|------|------|
| reversible protein phosphorylation | 可逆蛋白磷酸化 | 诺奖理由核心词 |
| protein kinase | 蛋白激酶 | 自 ATP 转移磷酸基 |
| phosphatase | 磷酸酶 | 水解除磷还原 |
| glycogen phosphorylase | 糖原磷酸化酶 | 研究对象（Cori 发现） |
| ATP / ADP | 腺苷三/二磷酸 | 磷酸基供体 |
| cell signaling | 细胞信号 | 磷酸化决定生长/分裂/分化 |
| alpha-amylase | α-淀粉酶 | 博士论文对象 |
| World Cultural Council | 世界文化理事会 | 2007-14 荣誉主席 |
| ForMemRS | 皇家学会外籍会士 | 2010 当选 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Nostalgia** — Alex-Productions（manifest 预分配）
- **风格**：怀旧 / 温情 / 回望
- **匹配理由**：上海童年、瑞士寄宿、日内瓦琴键——Fischer 的一生自带怀旧的流丽层次；Nostalgia 的温情回望匹配「西雅图像瑞士」的乡愁选择与 101 岁人生的悠长谢幕（第二次使用该曲，首用 Rabin/Newell，同为怀旧叙事）。
- **本地路径**：`music_audio/` 下 Nostalgia 曲目 → 复制为 `presentations/20th_century/Edmond_H._Fischer/Nostalgia.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐 15 页时长。
