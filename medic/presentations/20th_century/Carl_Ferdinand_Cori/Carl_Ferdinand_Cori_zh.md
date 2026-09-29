# 医学家立传提示词（Carl Ferdinand Cori）

> 本文件是 OpenMedic 项目「20 世纪诺贝尔生理学或医学奖得主人物专属立传提示词」。
> 目标人物：Carl Ferdinand Cori（1947 年诺贝尔生理学或医学奖得主，美国）。
> 用途：指导后续 Beamer 立传（15 页）与配套视频制作；事实基准为本地 Wikipedia 页面
> `medic/presentations/pages/20th_century/Carl_Ferdinand_Cori/page.md`（下称 page.md）。
> 社会关系与研究领域已按本文件第三、四节入库 greatminds 库（yaml 与本文件完全一致）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Carl Ferdinand Cori（卡尔·费迪南德·科里，1896-12-05 布拉格 ~ 1984-10-20，享年 87 岁，晚年定居波士顿）
- **气质关键词**：**科里循环的命名者、糖原磷酸化酶的鉴定人、科学史上第三对诺奖夫妻的另一半** —— 1947 年诺贝尔生理学或医学奖获奖理由（逐字引自 medic/nobel_medicine_citations.json，与 Gerty Cori 共享，Houssay 得同年另一半）：
  > "for their discovery of the course of the catalytic conversion of glycogen"
  > （因其关于糖原催化转化途径的发现）
- **设计母题**：**「循环」**。肌肉里的糖原→乳酸→肝脏再合成→回到肌肉——视觉隐喻：闭环回路箭头连接肌肉与肝脏双轮廓，Cori ester（葡萄糖-1-磷酸）位于环路中央。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Carl_Ferdinand_Cori/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 **medic 路径**执行：页面用 `medic/presentations/pages/20th_century/Carl_Ferdinand_Cori/`，成目录 `medic/presentations/20th_century/Carl_Ferdinand_Cori/`，Makefile 复制后设 `MAIN=Carl_Ferdinand_Cori_zh`、`VIDEO_NAME=Carl_Ferdinand_Cori_zh`，BGM 见第九节。
> 第 4 步（研究领域）与第 4.5 步（社会关系）**已完成入库**，见第三、四节。
> 数据库：本人记录复用他批已建 stub（库内 3460，原名为裸形式 Carl Cori，本批已改名归并为 manifest 形式后 UPD 回填 QID Q78501），`has_social_data=1`；`has_biography` 待 Beamer 立传完成后置 1。

## 三、研究领域梳理 + 入库（已完成）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biochemistry | 生物化学 | 糖代谢主线，1947 诺奖核心 | 总览页 |
| 1 | carbohydrate metabolism | 糖代谢 | Cori 循环（1929）、糖原磷酸化酶鉴定与合成 | 循环页 |
| 2 | pharmacology | 药理学 | 圣路易斯华盛顿大学药理学教授（1931） | 生涯页 |

## 四、社会关系梳理 + 入库（已完成，与 MySQL/data/Carl_Ferdinand_Cori.yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Gerty Cori | — | 1947 诺贝尔生理学或医学奖夫妻共享糖代谢一半 |
| co-honored | Bernardo Houssay | — | 1947 同年共享，Houssay 得垂体激素另一半 |
| spouse | Gerty Cori | — | 1920 年布拉格成婚，同窗同实验室终身合作 |
| spouse | Anne Fitzgerald-Jones | — | 1960 年续弦 |
| parent-child | Tom Cori | 子 | 独子，2016 年捐出父母诺奖奖章 |
| parent-child | Carl Isidor Cori | 父 | 动物学家，的里雅斯特海洋生物站站长 |
| parent-child | Maria Lippich | 母 | 奥地利医生之女 |
| colleague | Otto Loewi | — | 1921-22 年受邀赴格拉茨研究迷走神经对心脏的作用 |
| collaborator | Salomé Glüecksohn-Waelsch | — | 1968-1983 年哈佛时期遗传学合作者 |

> 说明：与 Gerty 同时建 spouse + co-honored 双边（夫妻共同得主惯例）。Loewi 是 frontmatter doctoral_advisor，但正文只载「受邀赴格拉茨合作研究」（其医学博士在布拉格）——按合作建 colleague 不建师生边（Loewi 库内 id 5081，本批 batch-08 所建）。妹妹 Margarete、外祖父 Ferdinand Lippich、祖父辈、儿子姻亲 Phyllis Schlafly 等均不入库；与 Glüecksohn-Waelsch 的合作建 collaborator。

## 五、配色方案 【人物专属】

- **气质**：中欧学统的严谨、新大陆实验室的双人协奏
- **主色**：糖原琥珀 `#8A6A2E`（糖原颗粒的暖棕）
- **诺奖色**：香槟金（奖章/年份徽章专用）
- **四分类色（badgeA-D）**：
  - `badgeA` 生物化学 — 代谢青 `#1F7A6D`
  - `badgeB` 糖代谢 — 循环紫 `#5B4E8E`
  - `badgeC` 药理学 — 圣路易斯蓝 `#33637D`
  - `badgeD` 科里酯 — 磷酸橙 `#C07A2E`
- **背景母题**：肌肉-肝脏双轮廓与环形箭头（Cori cycle）、稀疏糖原颗粒点阵，低透明度铺底

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input medic/presentations/cover/）
01  封面 — 科里循环的命名者 / Carl Ferdinand Cori 1896–1984 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像（1947 夫妻合影）+ 右信息网格（生卒、教育、任职、家庭、荣誉、核心领域）
03  核心贡献概览 — Cori 循环 / 糖原磷酸化酶 / Cori ester / 晚年遗传学
04  布拉格-的里雅斯特少年 (1896–1914) — 动物学家之父、的里雅斯特海滨长大
05  布拉格医学院与初遇 Gerty (1914–1920) — 战时滑雪部队与卫生队、1920 同年毕业同年成婚
06  维也纳-格拉茨 (1920–1922) — 维也纳诊所岁月、1921 受邀赴格拉茨与 Loewi 研究迷走神经
07  布法罗： Roswell 岁月 (1922–1931) — 移美、1928 入籍、发表 50 篇合作论文（一作按贡献轮换）
08  Cori 循环 (1929)（核心页）— 糖原→乳酸→肝内再合成的闭环
09  圣路易斯 (1931–1966) — 药理学教授、1942 生化教授、Cori ester 与磷酸化酶
10  1947 诺贝尔奖（核心页）— citation 原文、夫妻共享一半、Houssay 另一半、史上第三对诺奖夫妻
11  Gerty 的战场 — 机构阻挠与同工不同酬（从 Carl 页视角一笔带过，详见其单篇）
12  晚年与续弦 — 1957 Gerty 病逝、1960 续娶 Anne、哈佛与 Mass General 的遗传学研究
13  荣誉与认可 — Lasker 1946 · Nobel 1947 · Willard Gibbs 1948 · NAS 1940 · ForMemRS 1950 · 奥地利科学与艺术勋章 1959
14  遗产 — 2004 National Historic Chemical Landmark、圣路易斯星光大道双子星、2016 奖章入藏 Becker 医学图书馆
15  结尾
```

## 七、特殊陷阱表（★ 执行 Beamer 前必读）

| # | 陷阱 | 裁定 |
|---|------|------|
| 1 | 获奖理由表述 | 逐字用 citation 原文 "for their discovery of the course of the catalytic conversion of glycogen"（their 夫妻共享）；Houssay 是「同年另一半」，两段理由不同勿混写 |
| 2 | 死亡日期双值 | frontmatter 有 1984-10-20 与 1986-10-20 两值，正文/infobox 均为 1984-10-20（享年 87，与 Gerty 页「until his death in 1984」互证）——取 1984 |
| 3 | 国籍口径 | citation json country 为 "Czechoslovakia United States"（rowspan 噪声）；manifest/总表口径 United States——yaml 已按 US，正文叙述「布拉格出生→1928 入籍美国」 |
| 4 | 师承裁定 | frontmatter doctoral_advisor=Otto Loewi，但本人医学博士是布拉格（1920），与 Loewi 是 1921-22 受邀合作——建 colleague 不建师生边，勿写「Loewi 弟子」 |
| 5 | 夫妻分工 | 本篇以 Carl 视角行文，Roswell 50 篇合作论文「一作按贡献轮换」是 Gerty 页明载的制度，可在此提一句呼应，不平摊叙事 |
| 6 | 儿子姻亲 | Tom Cori 之妻是 Phyllis Schlafly 之女——Schlafly 是政治敏感人物，仅可在身份页以「儿媳系美国保守派活动家之女」一句带过或不提，禁展开 |
| 7 | 引语红线 | 本篇 page.md 无直接引语，禁编造；Gerty 页的 Larner 回忆引语归 Gerty 篇使用 |
| 8 | 「第三对夫妻」 | Cori 夫妻是史上第三对诺贝尔奖夫妻（page 明载）；「第三位女性科学诺奖/首位医学诺奖女性」属 Gerty 篇口径，本篇不重复展开 |
| 9 | 奖章去向 | 2016 年儿子 Thomas 将父母奖章捐给华盛顿大学医学院 Becker 图书馆——注意总表/正文别误写为 University of Washington（西雅图），两者不同 |
| 10 | metadata 冲突 | frontmatter nationality 三值（Cisleithania/Czechoslovakia/US），yaml 按 Nobel 官方口径只填 United States |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| Cori cycle | 科里循环 | 肌肉-肝脏乳酸-糖原往返 |
| glycogen | 糖原（动物淀粉） | 勿与淀粉混淆 |
| glycogenolysis | 糖原分解 | 与糖异生区分 |
| glycogen phosphorylase | 糖原磷酸化酶 | 夫妻共同鉴定并合成的酶 |
| Cori ester / glucose 1-phosphate | 科里酯 / 葡萄糖-1-磷酸 | 可逆反应的中间物 |
| lactic acid | 乳酸 | 循环的肌肉端产物 |
| carbohydrate metabolism | 糖代谢 | 诺奖理由核心域 |
| Roswell Park | 罗斯威尔帕克研究所 | 布法罗恶性疾病研究所旧称 |
| Washington University in St. Louis | 圣路易斯华盛顿大学 | 勿与西雅图华盛顿大学混淆 |
| National Historic Chemical Landmark | 国家历史化学地标 | ACS 2004 授予 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Timeless** — Alex-Productions（manifest 预分配）
- **匹配理由**：
  - 「长期纲领」匹配其科学遗产——Cori 循环至今是生化教科书骨架，糖原磷酸化酶开启酶调控研究的长路
  - 沉稳节奏契合双人实验室半个世纪的持久协奏
- **备选**（未采用）：PAST（本批 Gerty 已用）、The Flow of Time（时间意象合适但高频占用）
- **本地路径**：按 music_audio/ 内 Alex-Productions Timeless 曲目复制至 `medic/presentations/20th_century/Carl_Ferdinand_Cori/Timeless.wav`，ffmpeg `-shortest` 对齐
