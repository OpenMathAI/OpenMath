# 医学家立传提示词（Fritz Albert Lipmann）

> **OpenMedic** 项目 · 20 世纪诺贝尔生理学或医学奖 **1953 年**得主（与 Hans Adolf Krebs 共享，各得一半）。
> 本文件是 Lipmann 的「人物专属立传提示词」，供后续 Beamer 立传 agent 直接使用；配套数据已按第三、四节入库 greatminds 库。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Fritz Albert Lipmann（1899-06-12 ~ 1986-07-24，享年 87 岁），德裔美国生物化学家
- **气质关键词**：**辅酶 A 的共同发现者、高能磷酸键「~」符号的引入者、能量代谢的钥匙匠** —— 1953 诺贝尔生理学或医学奖获奖理由（官方原文，逐字引用）：
  > "for his discovery of co-enzyme A and its importance for intermediary metabolism"（因其发现辅酶 A 及其中间代谢中的重要性）
- **设计母题**：**能量的波浪号（the energy squiggle）**。Lipmann 用「~」标记高能磷酸键——以「分子式上一道跳动的波浪线」作为能量货币的视觉隐喻。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Fritz_Albert_Lipmann/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `Physicist_Bio_Prompt_Template.md` 第三章八步流程：下载核对 → 建目录 → 复制 Makefile → 收集图片 → 研究领域入库 → 社会关系入库 → 编写 Beamer → 布局检查 + 史实审查。
> **第 0/1/2/3 步按 medic 路径执行**：页面用 `medic/presentations/pages/20th_century/Fritz_Albert_Lipmann/`；Makefile 复制后设 `MAIN=Fritz_Albert_Lipmann_zh`；BGM 复制到本目录（见第九节）。
> 数据库两步（第 4/4.5 步）**已完成**，见第三、四节；执行 agent 只需做 Beamer 与目检。

## 三、研究领域梳理 + 入库 【已入库，与 yaml 完全一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biochemistry | 生物化学 | 1953 诺奖核心 | 核心页 |
| 1 | intermediary metabolism | 中间代谢 | 辅酶 A 在其中的枢纽作用 | 核心页 |
| 2 | enzymology | 酶学 | 辅酶与酶促能量转移 | 研究页 |

## 四、社会关系梳理 + 入库 【已入库，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Hans Meerwein | 师→生（化学导师） | 重返柯尼斯堡随其学化学 |
| advisor-student | Otto Fritz Meyerhof | 师→生（博士导师） | 1926 入柏林达勒姆研究所随其作博士论文 |
| co-honored | Hans Adolf Krebs | 无向 | 1953 诺贝尔生理学或医学奖共享（各得一半） |
| spouse | Elfreda M. Hall | 无向 | 1931 结婚，一子；遗孀 2008 卒，享年 101 |

**方向约定**：`advisor-student` + `direction: advisor` = 对方是导师；其余无向（from<to 自动归一）。

## 五、配色方案 【人物专属】

- **气质**：化学家的巧思、能量流动的明快、两位诺奖导师门下的传承
- **主色**：`#4A3560`（辅酶紫，分子与能量）
- **香槟金**：`#D4B26A`（诺奖色）
- **badgeA-D 四分类色**：`badgeCoA` 辅酶 A — 辅酶紫 `#4A3560`；`badgeSquiggle` 高能键 — 能量橙 `#D07B2A`；`badgeMetab` 中间代谢 — 代谢青 `#1B6B6B`；`badgeBerlin` 柏林与流亡 — 灰蓝 `#4E6478`
- **背景母题**：米白底上散布分子式片段，其中高能键处以「~」波浪线与亮点标出，错落连缀。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 能量的钥匙 / Fritz Albert Lipmann 1899–1986 + 四色 badge + 右上肖像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Königsberg、柯尼斯堡/柏林/慕尼黑、哈佛/洛克菲勒、荣誉）
03  核心贡献概览 — 辅酶 A / 高能磷酸键「~」/ 中间代谢枢纽 / Pantethine
04  柯尼斯堡的化学转向 (1899–1926) — 犹太律师之子、三校医学、随 Meerwein 学化学
05  Meyerhof 门下 (1926–1930s) — 达勒姆研究所博士论文、随师迁海德堡 Kaiser Wilhelm 医学研究所
06  流亡美国 (1939–1941) — 康奈尔医学院研究助理
07  麻省总医院岁月 (1941–1949) — 外科系→自领生化研究组、1945/1947 辅酶 A 的鉴定
08  辅酶 A 与中间代谢（核心贡献页）— 酰基转移的公共载体、泛酸组分、能量转移枢纽
09  「~」的发明 — 《代谢中磷酸键能量的产生与利用》、高能磷酸键的波浪号标记法
10  1953 诺贝尔奖 — 与 Krebs 各得一半、各自理由不同（辅酶 A vs 柠檬酸循环）
11  两环相扣 — 乙酰辅酶 A 进入 Krebs 循环：两人工作在代谢图上会师
12  哈佛与洛克菲勒 (1949–1986) — 生物化学教授 1949-57、洛克菲勒大学 1957 起、Pantethine 探索
13  荣誉与身后 — 1966 国家科学奖章、皇家学会外籍会员、Pour le Mérite、FLI 以其命名
14  遗产：能量货币的语法 — 「~」沿用至今、辅酶 A 成生化学通用语
15  结尾
```

## 七、特殊陷阱表 【★ 核心，从 page.md 提炼】

| 陷阱 | 说明 |
|------|------|
| 生卒日 | 1899-06-12 生于 Königsberg（德意志帝国，今加里宁格勒）；1986-07-24 卒于 Poughkeepsie, New York，享年 87 |
| 获奖理由 | "for his discovery of co-enzyme A and its importance for intermediary metabolism"——**his**；与 Krebs 各得一半、各自理由不同，勿混写 |
| 共同发现者 | 辅酶 A 系 **1945 年共同发现**（known for: co-discoverer in 1945）——表述用「共同发现」，勿写成独享 |
| 年份口径 | 正文既作 1945（infobox）又作 1947（Krebs 篇语境）——本篇以 infobox 1945 为准，陷阱表注明 |
| 导师两位 | Meerwein（化学，重返柯尼斯堡后）与 Meyerhof（博士论文，达勒姆研究所）——正文均明载「under/study under」；Meyerhof 用库内规范名 Otto Fritz Meyerhof |
| Stockhom 照片 | 与 Lipmann 合影的女士是 Mary Soames 而非其妻 Elfreda——图注陷阱，勿误标 |
| 引语 | 正文唯一原话："that in the field of biosynthesis we have a rare example of progress leading to simplification"——引语仅此一条 |
| 家庭 | 1931 娶 Elfreda M. Hall、一子；遗孀 2008 卒享年 101——可写 |
| 国籍口径 | manifest/Nobel 官方为 United States（1939 起居美）——表述「德裔美籍」 |
| 无争议条目 | 本篇无诉讼/争议——叙事保持明快，勿硬造波折 |

## 八、术语清单 【6-10 条】

| 英文 | 中文 | 风险点 |
|------|------|------|
| coenzyme A | 辅酶 A | 1945 共同发现 |
| acetyl-CoA | 乙酰辅酶 A | 进入 Krebs 循环的枢纽分子 |
| intermediary metabolism | 中间代谢 | 诺奖理由核心词 |
| energy-rich phosphate | 高能磷酸键 | 以「~」标记 |
| pantethine | 泮托硫胺（泛酰巯基乙胺二硫化物） | 其后期探索的辅酶 A 变体 |
| pantothenic acid | 泛酸 | 辅酶 A 的维生素组分 |
| squiggle notation | 波浪号标记法 | 其引入的能量键记号 |
| Rockefeller University | 洛克菲勒大学 | 1957 起的东家 |
| Fritz Lipmann Institute | 弗里茨·李普曼研究所 | 耶拿 FLI，以其命名 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Eternals** — Alex-Productions（manifest 预分配）
- **风格**：宏大 / 深远 / 长期影响
- **匹配理由**：辅酶 A 与「~」标记法是写进每一本生化学教科书的永恒语言——Eternals 的宏大深远匹配其工作「在代谢图上永续运转」的遗产（第二次使用该曲，首用 Ostwald，同为奠基性语法缔造者）。
- **本地路径**：`music_audio/` 下 Eternals 曲目 → 复制为 `presentations/20th_century/Fritz_Albert_Lipmann/Eternals.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐 15 页时长。

