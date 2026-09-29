# 医学家立传提示词（Paul Hermann Müller）

> 本文件是 OpenMedic 项目「20 世纪诺贝尔生理学或医学奖得主人物专属立传提示词」。
> 目标人物：Paul Hermann Müller（1948 年诺贝尔生理学或医学奖得主，瑞士）。
> 用途：指导后续 Beamer 立传（15 页）与配套视频制作；事实基准为本地 Wikipedia 页面
> `medic/presentations/pages/20th_century/Paul_Hermann_Müller/page.md`（下称 page.md）。
> 社会关系与研究领域已按本文件第三、四节入库 greatminds 库（yaml 与本文件完全一致）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Paul Hermann Müller（保罗·赫尔曼·米勒，1899-01-12 瑞士奥尔滕 ~ 1965-10-13 巴塞尔，享年 66 岁）
- **气质关键词**：**DDT 杀虫力的发现者、349 次失败后的第 350 号化合物、独自在实验室里较劲的「独行客」** —— 1948 年诺贝尔生理学或医学奖获奖理由（逐字引自 medic/nobel_medicine_citations.json）：
  > "for his discovery of the high efficiency of DDT as a contact poison against several arthropods"
  > （因其发现 DDT 作为接触性毒剂对若干节肢动物的高效杀灭力）
- **设计母题**：**「第 350 号笼子」**。四年搜索、349 次失败，1939 年 9 月关着苍蝇的那只药笼——视觉隐喻：一排编号笼子中一只亮起，飞虫倒下。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Paul_Hermann_Müller/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 **medic 路径**执行：页面用 `medic/presentations/pages/20th_century/Paul_Hermann_Müller/`，成目录 `medic/presentations/20th_century/Paul_Hermann_Müller/`，Makefile 复制后设 `MAIN=Paul_Hermann_Müller_zh`、`VIDEO_NAME=Paul_Hermann_Müller_zh`，BGM 见第九节。
> 第 4 步（研究领域）与第 4.5 步（社会关系）**已完成入库**，见第三、四节。
> 数据库已置 `has_social_data=1`；`has_biography` 待 Beamer 立传完成后置 1。

## 三、研究领域梳理 + 入库（已完成）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | chemistry | 化学 | Geigy 染料部研究化学家出身，诺奖得主的非医生身份 | 总览页 |
| 1 | insecticide research | 杀虫剂研究 | DDT 接触毒效的发现（1939）与结构-活性研究 | DDT 页 |
| 2 | plant protection | 植物保护 | 鞣剂 Irgatan 系列、种子消毒剂 Graminone、杀虫专利 | 前期工作页 |

## 四、社会关系梳理 + 入库（已完成，与 MySQL/data/Paul_Hermann_Müller.yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| parent-child | Gottlieb Müller | 父 | 瑞士联邦铁路职员 |
| parent-child | Fanny Leypoldt | 母 | — |
| advisor-student | Hans Rupe | 师 | 巴塞尔有机化学实验室导师，1925 年最优等获博士 |
| influence | Friedrich Fichter | — | 大学无机化学启蒙导师，受益终身 |
| spouse | Friedel Rüegsegger | — | 1927 年成婚，操持家务使其专注化学 |
| parent-child | Margaretha | 女 | 戏称父亲为独行者 |

> 说明：Othmar Zeidler（1874 年首合成 DDT 而未察其效）是历史前驱非个人交往，不建边（见陷阱 4）；两个儿子未具名不入库；女儿 Margaretha 无姓氏叙事（独名提及），stub 仅用 Margaretha 防造名；「The Ghost」「Eigenbrötler」等绰号系家人同学语，作叙事细节。

## 五、配色方案 【人物专属】

- **气质**：瑞士式的缄默与固执、工业实验室的秩序、孤勇者的耐心
- **主色**：DDT 粉末灰白 `#7A8290`（结晶粉末的冷灰）
- **诺奖色**：香槟金（奖章/年份徽章专用）
- **四分类色（badgeA-D）**：
  - `badgeA` 化学 — 烧瓶蓝灰 `#41607E`
  - `badgeB` 杀虫剂研究 — 毒效黄绿 `#8FA82E`
  - `badgeC` 植物保护 — 鞣剂棕 `#8E5A2E`
  - `badgeD` 疟疾防治 — 救疫青 `#2E7A6E`
- **背景母题**：编号药笼网格与结晶粉末散点、稀疏六边形分子骨架，低透明度铺底

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input medic/presentations/cover/）
01  封面 — DDT 杀虫力的发现者 / Paul Hermann Müller 1899–1965 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、教育、Geigy 任职、荣誉、核心领域）
03  核心贡献概览 — DDT 接触毒效 / 鞣剂与消毒剂 / 结构-活性研究
04  奥尔滕-巴塞尔 (1899–1916) — 铁路职员之家、家中小实验室（照相底片与无线电）
05  从学徒到博士 (1916–1925) — 辍学当实验员、1918 复学、Rupe 实验室 1925 summa cum laude 博士
06  Geigy 十年 (1925–1935) — 染料与鞣剂：Irgatan G/FL/FLT
07  转向植物保护 (1935–1937) — 瑞士粮荒与俄国斑疹伤寒两大动因、rhodanide/cyanate 专利、Graminone
08  349 次失败与第 350 号 (1939)（核心页）— 理想接触杀虫剂的五条标准、1939-09 药笼中的苍蝇
09  DDT：前史与确证 — Zeidler 1874 年首合成而未察其效；瑞士政府/美国农业部对马铃薯甲虫的验证
10  从专利到战场 (1940–1945) — 1940 瑞士专利、1943 英军补给清单、意大利按蚊疟疾现场试验
11  1948 诺贝尔奖（核心页）— citation 原文、非医生获奖的反常、诺委会「集中营疏散已挽救数十万生命」评语（英文原文可引）
12  荣誉与认可 — Geigy 副主任 1946 · 1951 首届 Lindau 会议七位诺奖得主之一 · 希腊「国家英雄」礼遇 1963 · 塞萨洛尼基荣誉博士
13  独行客的晚年 — 女儿口中的 Eigenbrötler、阿尔卑斯与汝拉的植物学假日、长笛与钢琴二重奏
14  遗产与身后 (1961–1965) — 1961 退休居家实验室继续研究、1965 病逝；DDT 公共卫生史的争议篇章（仅以 page.md 所载诺委会语境收束）
15  结尾
```

## 七、特殊陷阱表（★ 执行 Beamer 前必读）

| # | 陷阱 | 裁定 |
|---|------|------|
| 1 | 获奖理由表述 | 逐字用 citation 原文 "for his discovery of the high efficiency of DDT as a contact poison against several arthropods"；核心是「接触性毒剂的高效杀灭力」，勿写成「发明 DDT」 |
| 2 | 死亡日期双值 | frontmatter 1965-10-12 vs 正文/infobox 1965-10-13（early morning）——取正文 1965-10-13 |
| 3 | 「非医生」反常 | 诺委会明确其既非医生亦非医学研究者仍授医学奖——page 明载可写，恰是本篇的反差点 |
| 4 | Zeidler 前驱 | DDT 由维也纳药理学家 Othmar Zeidler 于 1874 年首次合成，但未研究其性质未识其价值——「发现杀虫力」归 Müller，「首合成」归 Zeidler，两段功劳勿混；Zeidler 不建人物边 |
| 5 | DDT 环境争议 | 本地 page.md 只载公共卫生功绩（诺委会评语、疟疾防控），无 Silent Spring/环境危害叙事——按事实基准纪律不得添加未载内容，遗产帧以诺委会语境收束（见幻灯片 14 的措辞边界） |
| 6 | 349/350 | 「四年搜索、失败 349 次、1939 年 9 月第 350 号化合物见效」——数字链为叙事骨架，勿改写为「350 次失败」 |
| 7 | 诺委会引语 | "DDT has been used in large quantities in the evacuation of concentration camps..." 有英文原文，可引原文+译文；其余叙述无引语 |
| 8 | 师承双线 | Rupe 是博士实验室导师（师生边）；Fichter 是大学早期无机化学启蒙、「college mentor」——建 influence，勿并成一条 |
| 9 | 名字 | 通名 Paul Müller/Pauly Mueller；库内另有 Paul Rudolf Müller（2791，另一人）与本篇无关，身份页勿混淆 |
| 10 | metadata 冲突 | 死亡日见陷阱 2；occupation 含 physician（he is not a physician，frontmatter 噪声）——yaml 保留 chemist 为主、physician 降序处理，正文明确「既非医生」 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| DDT | 滴滴涕（双对氯苯基三氯乙烷） | 全名 dichlorodiphenyltrichloroethane |
| contact poison / insecticide | 接触性毒剂 / 杀虫剂 | 诺奖理由限定「接触毒效」 |
| arthropods | 节肢动物 | 诺奖理由用词（蚊/虱/蚤/白蛉） |
| disease vector | 病媒 | 疟疾/黄热病传播语境 |
| Anopheles | 按蚊 | 疟疾病媒属 |
| Colorado potato beetle | 马铃薯甲虫 | 首个官方验证对象 |
| tanning agent | 鞣剂 | Irgatan 系列，前期成果 |
| rhodanide / cyanate | 硫氰酸盐 / 氰酸盐 | 1937 专利化合物类 |
| Graminone | 格拉米农种衣消毒剂 | 汞制剂的安全替代 |
| summa cum laude | 最优等 | 1925 博士评语 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Nostalgia** — Alex-Productions（manifest 预分配）
- **匹配理由**：
  - 「怀旧」匹配其近乎 19 世纪式的人生底色——山中植物学假日、长笛钢琴二重奏、居家实验室里做到最后一天的老派化学家
  - 温缓曲式反衬「349 次失败」的漫长等待，也让公共卫生拯救百万的宏大叙事落回个体耐心
- **备选**（未采用）：Lonesome（本批 Szent-Györgyi 批次相邻已用；其「独行」气质本可用，但留给更孤绝的人物）、With Me（陪伴感不合其独行气质）
- **本地路径**：按 music_audio/ 内 Alex-Productions Nostalgia 曲目复制至 `medic/presentations/20th_century/Paul_Hermann_Müller/Nostalgia.wav`，ffmpeg `-shortest` 对齐
