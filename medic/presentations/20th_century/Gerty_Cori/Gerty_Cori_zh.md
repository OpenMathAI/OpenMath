# 医学家立传提示词（Gerty Cori）

> 本文件是 OpenMedic 项目「20 世纪诺贝尔生理学或医学奖得主人物专属立传提示词」。
> 目标人物：Gerty Cori（1947 年诺贝尔生理学或医学奖得主，美国）。
> 用途：指导后续 Beamer 立传（15 页）与配套视频制作；事实基准为本地 Wikipedia 页面
> `medic/presentations/pages/20th_century/Gerty_Cori/page.md`（下称 page.md）。
> 社会关系与研究领域已按本文件第三、四节入库 greatminds 库（yaml 与本文件完全一致）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Gerty Theresa Cori（née Radnitz，格蒂·特蕾莎·科里，1896-08-15 布拉格 ~ 1957-10-26 密苏里州格伦代尔，享年 61 岁）
- **气质关键词**：**首位诺贝尔生理学或医学奖女性得主、糖原磷酸化酶的鉴定人、在性别与体制的双重壁垒下从未停步的实验大师** —— 1947 年诺贝尔生理学或医学奖获奖理由（逐字引自 medic/nobel_medicine_citations.json，与 Carl Cori 共享，Houssay 得同年另一半）：
  > "for their discovery of the course of the catalytic conversion of glycogen"
  > （因其关于糖原催化转化途径的发现）
- **设计母题**：**「白瓷水槽」**。两人亲手刷洗玻璃器皿的二十五平米实验室（2004 年列为国家历史地标）——视觉隐喻：一排洁净烧杯与磷酸化酶分子剪影并置。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Gerty_Cori/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 **medic 路径**执行：页面用 `medic/presentations/pages/20th_century/Gerty_Cori/`，成目录 `medic/presentations/20th_century/Gerty_Cori/`，Makefile 复制后设 `MAIN=Gerty_Cori_zh`、`VIDEO_NAME=Gerty_Cori_zh`，BGM 见第九节。
> 第 4 步（研究领域）与第 4.5 步（社会关系）**已完成入库**，见第三、四节。
> 数据库：本人记录复用他批已建 stub（库内 id=3461）UPD 回填 QID Q204733，`has_social_data=1`；`has_biography` 待 Beamer 立传完成后置 1。

## 三、研究领域梳理 + 入库（已完成）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biochemistry | 生物化学 | 糖代谢与糖原化学，1947 诺奖核心 | 总览页 |
| 1 | carbohydrate metabolism | 糖代谢 | Cori 循环、Cori ester、磷酸化酶可逆反应 | 循环页 |
| 2 | glycogen storage disease | 糖原累积症 | 鉴别至少四型，首证酶缺陷可致人类遗传病 | 临床页 |

## 四、社会关系梳理 + 入库（已完成，与 MySQL/data/Gerty_Cori.yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Carl Ferdinand Cori | — | 1947 诺贝尔生理学或医学奖夫妻共享糖代谢一半 |
| co-honored | Bernardo Houssay | — | 1947 同年共享，Houssay 得垂体激素另一半 |
| spouse | Carl Ferdinand Cori | — | 1920 年成婚，机构阻挠合作而丈夫坚持终身共研 |
| parent-child | Tom Cori | 子 | 独子 |
| parent-child | Otto Radnitz | 父 | 化学家兼糖厂经理 |
| parent-child | Martha Radnitz | 母 | 文化修养深厚，卡夫卡之友 |

> 说明：与 Carl 同时建 spouse + co-honored 双边（夫妻共同得主惯例）。叔父（儿科教授，鼓励其学医）无具名不入库；「与丈夫共同培养出 6 位诺奖得主」page.md 明载但无一具名——只作文字叙事，不建关系边；Arthur Compton（校长特批打破 nepotism 规则）为体制叙事，不建边；Joseph Larner（回忆录作者）不建边。六位诺奖门生列表待其各本人批次入库。

## 五、配色方案 【人物专属】

- **气质**：坚韧、明亮、实验台前六十年如一日的专注
- **主色**：磷酸化酶玫红 `#A63A4E`（血液与肌红蛋白的暖红）
- **诺奖色**：香槟金（奖章/年份徽章专用）
- **四分类色（badgeA-D）**：
  - `badgeA` 生物化学 — 代谢青 `#1F7A6D`
  - `badgeB` 糖代谢 — 循环紫 `#5B4E8E`
  - `badgeC` 糖原累积症 — 临床蓝 `#33637D`
  - `badgeD` Cori ester — 磷酸橙 `#C07A2E`
- **背景母题**：实验台玻璃器皿线稿（烧杯/试管/水槽）与糖原颗粒点阵，低透明度铺底

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input medic/presentations/cover/）
01  封面 — 首位医学诺奖女性 / Gerty Cori 1896–1957 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像（1947 夫妻合影）+ 右信息网格（生卒、教育、任职、家庭、荣誉、核心领域）
03  核心贡献概览 — Cori 循环 / Cori ester 与磷酸化酶 / 糖原累积症分型
04  布拉格犹太家庭 (1896–1914) — 糖厂化学家之父、家庭教师、16 岁立志学医后一年补齐八年课程
05  医学院与初遇 Carl (1914–1920) — 解剖课相识、1914 入学（当年罕见）、1920 同年毕业同年成婚（改宗天主教成婚）
06  维也纳与离别之因 (1920–1922) — 儿童医院儿科与体温调节研究、干眼症与反犹空气促离欧
07  布法罗：被禁止的合作 (1922–1931) — 所长以解雇相胁、她继续合作；50 篇合作论文一作按贡献轮换、11 篇独立一作
08  Cori 循环与 Cori ester (1929–1936)（核心页）— 循环提出、葡萄糖-1-磷酸鉴定、磷酸化酶确立
09  圣路易斯：十分之一的薪水 (1931–1943) — 多所大学拒聘夫妻档、Compton 校长特批、研究助理 1/10 薪、13 年等来同职级
10  1947 诺贝尔奖（核心页）— citation 原文、第三位科学诺奖女性（居里母女之后）、首位医学诺奖女性、诺奖前数月升正教授
11  酶缺陷致病：糖原累积症分型 — 至少四型对应特定酶缺陷、人类医学遗传学的先声
12  十年之疾 (1947–1957) — 登山途中确诊骨髓硬化症、疑与早年 X 射线研究相关、抱病工作至最后数月
13  荣誉与认可 — Garvan-Olin 1948 · St. Louis Award 1948 · Sugar Research 1950 · Borden 1951 · AAAS Fellow 1953 · NAS 第四位女性 · Truman 任命 NSF 委员
14  遗产 — 月球与金星 Cori 陨坑、2008 邮票（公式印错插曲）、NERSC-8 超算命名 Cori、夫妻星、2016 奖章入藏
15  结尾
```

## 七、特殊陷阱表（★ 执行 Beamer 前必读）

| # | 陷阱 | 裁定 |
|---|------|------|
| 1 | 获奖理由表述 | 逐字用 citation 原文 "for their discovery of the course of the catalytic conversion of glycogen"；「夫妻得一半、Houssay 得另一半」的份额表述 page.md 明载，必须呈现 |
| 2 | 「第三位」口径 | 第三位科学诺奖女性（前两位 Marie Curie 两度、Irène Joliot-Curie）+ 首位医学诺奖女性 + 首位美国女性——三个「第一/第三」各有准确指向，勿互换 |
| 3 | 死亡日期双值 | frontmatter 有 1957-10-26 与 1956-10-26 噪声，正文/infobox 均为 1957-10-26——取 1957 |
| 4 | 国籍口径 | citation json country "Czechoslovakia United States" 为 rowspan 噪声；yaml 按 manifest 口径 United States，正文叙述布拉格犹太家庭出身 |
| 5 | 性别歧视叙事 | 薪资 1/10、「un-American」面试语、nepotism 规则、Compton 特批——均 page.md 明载，如实呈现但不煽情；Larner 回忆引语（洗器皿/小床/烟灰）有英文原文可引 |
| 6 | 六位诺奖门生 | page.md 明载「夫妻指导的 6 位科学家后获诺奖，仅次于 J.J. Thomson」——无一具名，只作文字叙事，禁列名单禁建边 |
| 7 | X 射线与病因 | 「may have contributed」是 or 式推测——照抄推测语气，勿写成定论 |
| 8 | 邮票错误 | 2008 年 41 美分邮票 Cori ester 化学式印错仍发行——page 明载趣闻，可作彩蛋帧 |
| 9 | 儿子姻亲 | Tom 之妻系 Phyllis Schlafly 之女——一句带过或不提，禁展开政治背景 |
| 10 | metadata 冲突 | occupation 有 psychologist 噪声；yaml 主职业 biochemist，以正文为准 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| Cori cycle | 科里循环 | 肌肉-肝脏往返 |
| Cori ester | 科里酯 | 即葡萄糖-1-磷酸 |
| glucose 1-phosphate | 葡萄糖-1-磷酸 | 勿写成 6-磷酸葡萄糖 |
| glycogen phosphorylase | 糖原磷酸化酶 | 夫妻共同鉴定 |
| glycogen storage disease | 糖原累积症 | 至少四型分型 |
| myelosclerosis | 骨髓硬化症 | 死因 |
| xerophthalmia | 干眼症 | 维也纳营养不良所致 |
| nepotism rules | 亲属回避规则 | 夫妻同校任教壁垒 |
| Garvan–Olin Medal | 加万-奥林奖章 | 美国化学会女性化学家奖 |
| NERSC-8 Cori | Cori 超级计算机 | 劳伦斯伯克利实验室 2016 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**PAST** — Alex-Productions（manifest 预分配）
- **匹配理由**：
  - 「历史感/回望」匹配其人生弧线——从被规训的女性学徒到改写规则的诺奖得主，一整个时代对女性的偏见与她的突围都值得回望
  - 深沉而克制的曲色压得住「十分之一薪水」帧的沉重，也托得起诺奖帧的荣光
- **备选**（未采用）：Timeless（本批 Carl 已用）、The Flow of Time（时间意象重复且高频占用）
- **本地路径**：按 music_audio/ 内 Alex-Productions PAST 曲目复制至 `medic/presentations/20th_century/Gerty_Cori/PAST.wav`，ffmpeg `-shortest` 对齐
