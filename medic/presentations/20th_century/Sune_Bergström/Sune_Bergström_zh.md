# 医学家立传提示词（Sune Bergström）

> 本文件是 OpenMedic 项目「20 世纪诺贝尔生理学或医学奖得主人物专属立传提示词」。
> 目标人物：Sune Bergström（1982 年诺贝尔生理学或医学奖得主，瑞典）。
> 用途：指导后续 Beamer 立传（15 页）与配套视频制作；事实基准为本地 Wikipedia 页面
> `medic/presentations/pages/20th_century/Sune_Bergström/page.md`（下称 page.md）。
> 社会关系与研究领域已按本文件第三、四节入库 greatminds 库（yaml 与本文件完全一致）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Karl Sune Detlof Bergström（苏内·贝里斯特伦，1916-01-10 斯德哥尔摩 ~ 2004-08-15，享年 88 岁）
- **气质关键词**：**前列腺素的分离与结构测定先驱、皇家科学院院长、2022 诺奖得主 Svante Pääbo 的父亲** —— 1982 年诺贝尔生理学或医学奖获奖理由（逐字引自 medic/nobel_medicine_citations.json，与 Samuelsson、Vane 三人共享）：
  > "for their discoveries concerning prostaglandins and related biologically active substances"
  > （因其关于前列腺素及相关生物活性物质的发现）
- **设计母题**：**「二十碳酸的信使」**。从羊精囊中提纯出的前列腺素信使分子——视觉隐喻：二十碳脂肪酸链上一个个官能团徽记，化作体内信使网络。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Sune_Bergström/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 **medic 路径**执行：页面用 `medic/presentations/pages/20th_century/Sune_Bergström/`，成目录 `medic/presentations/20th_century/Sune_Bergström/`，Makefile 复制后设 `MAIN=Sune_Bergström_zh`、`VIDEO_NAME=Sune_Bergström_zh`，BGM 见第九节。
> 第 4 步（研究领域）与第 4.5 步（社会关系）**已完成入库**，见第三、四节。
> 数据库：本人记录复用库内既有 stub（id=5696）UPD 回填 QID Q295696，`has_social_data=1`；`has_biography` 待 Beamer 立传完成后置 1。

## 三、研究领域梳理 + 入库（已完成）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biochemistry | 生物化学 | 前列腺素分离纯化与结构测定，1982 诺奖核心 | 总览页 |
| 1 | prostaglandins | 前列腺素 | 与 Samuelsson 的结构工作、体内信使系统 | 前列腺素页 |
| 2 | lipid chemistry | 脂质化学 | 脂肪酸衍生活性物质 | 化学页 |

## 四、社会关系梳理 + 入库（已完成，与 MySQL/data/Sune_Bergström.yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Bengt I. Samuelsson | — | 1982 诺贝尔生理学或医学奖三人共享（前列腺素等） |
| co-honored | John Vane | — | 1982 诺贝尔生理学或医学奖三人共享（前列腺素等） |
| collaborator | Bengt I. Samuelsson | — | 前列腺素结构研究长期搭档，1975 年同获 Horwitz 奖 |
| spouse | Maj Gernandt | — | 1943 年成婚 |
| parent-child | Rurik Reenstierna | 子 | 企业家，约 2004 年才知有异母弟 |
| parent-child | Svante Pääbo | 子 | 进化遗传学家，2022 诺贝尔生理学或医学奖得主 |

> 说明：本篇 page.md 极简（全文不足 50 行），按「禁编造」纪律边数从简。Svante Pääbo 复用库内既有记录（id 5694, Q170342）；非婚生子事实 page.md 明载、以一句克制陈述呈现（两子同年 1955 年出生、Rurik 约 2004 年才知有异母弟），不作道德评述。无博士导师明载（斯德哥尔摩大学出身）；父辈未具名不入库。

## 五、配色方案 【人物专属】

- **气质**：瑞典学统的沉静、结构化学的秩序、家族科学传承的余韵
- **主色**：信使琥珀 `#9A6B2E`（前列腺素脂质分子的暖调）
- **诺奖色**：香槟金（奖章/年份徽章专用）
- **四分类色（badgeA-D）**：
  - `badgeA` 生物化学 — 提纯青 `#1F7A6D`
  - `badgeB` 前列腺素 — 信使橙 `#C08A2E`
  - `badgeC` 脂质化学 — 链条灰金 `#8A7A4E`
  - `badgeD` 学术行政 — 皇家蓝 `#33637D`
- **背景母题**：二十碳脂肪酸链的锯齿线稿与信使分子徽记，低透明度铺底

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input medic/presentations/cover/）
01  封面 — 前列腺素的提纯者 / Sune Bergström 1916–2004 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像（1980 照）+ 右信息网格（生卒、教育、任职、家庭、荣誉、核心领域）
03  核心贡献概览 — 前列腺素分离 / 结构测定 / 相关活性物质 / 学术行政
04  斯德哥尔摩 (1916–1943) — 全名 Karl Sune Detlof、斯德哥尔摩大学出身、1943 年成婚
05  脂质化学与前列腺素起步 — 羊精囊来源的提纯难题、与 Samuelsson 的结构接力
06  与 Samuelsson 的搭档岁月（核心页）— 结构工作、1975 同获 Horwitz 奖、师徒搭档的接力棒
07  1982 诺贝尔奖（核心页）— citation 原文、三人共享、诺奖演讲 The Prostaglandins: From the Laboratory to the Clinic
08  前列腺素：体内的信使系统 — 相关生物活性物质家族（对照 Samuelsson 的下游发现）
09  皇家科学院院长 (1983) — 1965 两院院士、1975 诺贝尔基金会董事会、1985 教皇科学院
10  家庭的两个平行故事 — 1943 年与 Maj 成婚；两个儿子同生于 1955 年；Pääbo 的 2022 诺奖让父子同列诺奖名录
11  荣誉链 — Gairdner 1972 · Horwitz 1975 · Cameron 1977 · Welch 1980 · Nobel 1982 · Illis quorum 1985
12  与 Vane 的交汇 — 瑞典结构化学与英国药理学的三奖拼图（Bergström/Samuelsson 结构+Vane 机理）
13  晚年 (1985–2004) — 名誉职务、2004 年辞世（与 Vane 同年离世）
14  遗产 — 前列腺素家族药物（抗炎/心血管/生殖）的结构化学基石；父子双诺奖的科学世家
15  结尾
```

## 七、特殊陷阱表（★ 执行 Beamer 前必读）

| # | 陷阱 | 裁定 |
|---|------|------|
| 1 | 获奖理由表述 | 逐字用 citation 原文 "for their discoveries concerning prostaglandins and related biologically active substances"（their 三人共享同一理由）——与 1981 半奖结构不同 |
| 2 | 三人分工 | Bergström/Samuelsson 是结构化学（瑞典系，师徒搭档）、Vane 是阿司匹林机理（英国系）——同一 citation 下两支脉络，分工帧必须写清 |
| 3 | 页面极简 | 本篇 page.md 全文不足 50 行——禁为凑页数编造生平细节；结构用「诺奖三人拼图+荣誉链+家庭」三个真实骨架展开 |
| 4 | 家庭结构 | 两个儿子（Rurik Reenstierna/Svante Pääbo）均为 1955 年生、其中 Svante 系与 Estonian 化学家 Karin Pääbo 的非婚生子、Rurik 约 2004 年才知情——page.md 明载，一句克制陈述、不作道德评述、不渲染 |
| 5 | Pääbo 边 | Svante Pääbo 复用库内记录（id 5694, Q170342）；「父子双诺奖」（1982/2022 生理学或医学奖）是本篇独有亮点 |
| 6 | 无师承 | 斯德哥尔摩大学出身、page.md 无博士导师明载——禁编造；与 Samuelsson 的关系是「搭档/导师」（后者 frontmatter 有载），本篇以 collaborator 建边 |
| 7 | 职务年代链 | RSAS 院士 1965、院长 1983；皇家工学院院士 1965；AAAS 荣誉院士 1966；诺奖基金会董事 1975；教皇科学院 1985——勿错置 |
| 8 | 名字 | 全名 Karl Sune Detlof Bergström 仅身份页用；库内规范名 Sune Bergström（与 manifest 一致）；勿与儿子 Svante 混写 |
| 9 | 死亡地 | page.md 只载日期（2004-08-15）无地点——身份页卒地留白，勿杜撰 |
| 10 | metadata 冲突 | frontmatter workplaces 只列 Columbia University——正文无其他任职叙事，立传不添加卡罗林斯卡等未载机构 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| prostaglandin | 前列腺素 | 得名于前列腺但实为全身组织产物 |
| related biologically active substances | 相关生物活性物质 | citation 措辞，涵盖下游家族 |
| arachidonic acid | 花生四烯酸 | 前列腺素前体（Samuelsson 主线） |
| structural work | 结构测定 | Bergström-Samuelsson 接力的核心 |
| Horwitz Prize | 霍维茨奖 | 1975 两人同获 |
| Royal Swedish Academy of Sciences | 瑞典皇家科学院 | 1983 年院长 |
| Illis quorum | 伊利斯夸伦奖章 | 瑞典王室勋章 1985 |
| Nobel Foundation Board | 诺贝尔基金会董事会 | 1975 年起任职 |
| Pontifical Academy of Sciences | 教皇科学院 | 1985 年入选 |
| Welch Award in Chemistry | 韦尔奇化学奖 | 1980 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**The Flow of Time** — Alex-Productions（manifest 预分配）
- **匹配理由**：
  - 「时间之流」匹配其分子信使的主题——前列腺素正是体内随时间流转的调控信使
  - 也匹配两代科学的时间接力：1982 父亲、2022 儿子，同一奖项四十年两岸
- **备选**（未采用）：Daylight（本批 Samuelsson 已用，师徒组曲目须区分）、Timeless（结构感贴切但高频占用）
- **本地路径**：按 music_audio/ 内 Alex-Productions The Flow of Time 曲目复制至 `medic/presentations/20th_century/Sune_Bergström/The_Flow_of_Time.wav`，ffmpeg `-shortest` 对齐
