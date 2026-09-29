# 医学家立传提示词（Otto Fritz Meyerhof）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1922 年得主 Otto Fritz Meyerhof（奥托·弗里茨·迈尔霍夫）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Otto_Fritz_Meyerhof/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Otto Fritz Meyerhof（1884-04-12 生于汉诺威，普鲁士王国 ~ 1951-10-06 逝于美国费城，享年 67 岁）
- **气质关键词**：**氧与乳酸的定量者、糖酵解的命名者、被驱逐的流亡生物化学家**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1922 条目，Meyerhof 半边口径）：
  > "for his discovery of the fixed relationship between the consumption of oxygen and the metabolism of lactic acid in the muscle"（因其发现肌肉中氧的消耗与乳酸代谢之间的固定关系）
- **设计母题**：**氧与乳酸的定量天平（oxygen–lactate balance）**——肌肉中氧耗与乳酸代谢存在固定关系；用「双向转化的天平/循环箭头」作背景母题：乳酸与氧化的闭环线条。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Otto_Fritz_Meyerhof/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/20th_century/Otto_Fritz_Meyerhof/`。Makefile 复制后设 `MAIN=Otto_Fritz_Meyerhof_zh`、`VIDEO_NAME=Otto_Fritz_Meyerhof_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Meyerhof 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biochemistry | 生物化学 | 肌肉代谢化学，1922 诺奖核心 | 封面、核心页 |
| 1 | glycolysis | 糖酵解 | Embden–Meyerhof–Parnas 途径以其命名 | 核心页 |
| 2 | muscle metabolism | 肌肉代谢 | 氧耗与乳酸代谢的固定关系（诺奖理由） | 核心页 |
| 3 | physiology | 生理学 | infobox 职业兼载；基尔大学教授 | 职业页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md/frontmatter 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Otto Heinrich Warburg | 对方 → 导师 | page.md frontmatter doctoral_advisor 明载（正文未展开，note 注明来源） |
| co-honored | Archibald Hill | 无向 | 1922 诺贝尔生理学或医学奖共享（Meyerhof 氧耗—乳酸代谢 / Hill 肌肉产热，工作平行独立） |
| spouse | Hedwig Schallenberg | 无向 | 1914 结婚，育三子女 |

**不入库但提示词可叙述**：子女 Bettina / Gottfried（移民后用名 Geoffrey）/ Walter（page.md 仅具名，无实质描述）；Embden 与 Parnas（糖酵解途径共列命名者，page.md 无任何人物关系记载，只在术语层出现）；Emergency Rescue Committee（救援组织，非个人）。

## 五、配色方案 【人物专属】

- **气质**：德式严谨、流亡的暗色与费城晚霞
- **主色**：`#6E2B2B`（暗砖红——肌肉组织与流亡岁月的沉郁）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeOxy` 氧耗—乳酸定量 — 暗砖红 `#6E2B2B`
  - `badgeGly` 糖酵解途径 — 深金 `#B8860B`
  - `badgeKiel` 基尔与海德堡 — 深蓝 `#1E3A5F`
  - `badgeExile` 流亡与宾大 — 灰紫 `#46356B`
- **背景母题**：氧分子与乳酸分子间的定量循环箭头，秤杆两端平衡的抽象线条。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 氧与乳酸的定量者 / Otto Fritz Meyerhof 1884–1951 + 四色 badge + 右上头像 + 国籍行（Germany）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、汉诺威出身、斯特拉斯堡/海德堡求学 1909 毕业、
    基尔大学教授 1918、KWI 医学研究所所长 1929–1938、诺奖 1922、核心领域）
03  核心贡献概览 — 氧耗—乳酸固定关系 / 糖酵解 / 肌肉能量转换 / 流亡岁月
04  汉诺威与柏林童年 (1884–1900s) — 犹太富商家庭，1888 迁柏林；医学起步
05  斯特拉斯堡与海德堡 (1909) — 毕业论文《精神疾病心理学理论贡献》——精神医学起点的冷知识
06  基尔岁月与教授就任 (1912–1918) — 1912 迁基尔，1918 获教授职
07  氧耗与乳酸的固定关系（核心贡献页）— 肌肉中氧的消耗与乳酸代谢的定量耦合，1922 诺奖理由
08  1922 诺奖：与 Hill 平行而共享 — Meyerhof 化学计量 / Hill 产热测量；两条平行线交汇于斯德哥尔摩
09  糖酵解与 EMP 途径 — 真核生物糖酵解共同反应序列以 Embden–Meyerhof–Parnas 命名
10  KWI 医学研究所 (1929–1938) — 海德堡所长之一；1938 犹太人被逐出大学教职
11  流亡之路 (1938–1940) — 巴黎 → 法国陷落 → 马赛；Emergency Rescue Committee 援助下乘船赴美
12  费城宾大岁月 (1940–1951) — 客座教授，1951-10-06 逝于费城
13  诺奖演讲与著作 — 1923-12-12 诺贝尔演讲《Energy Conversions in Muscle》
14  遗产与结尾 — EMP 途径 / 现代生物能量学 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 1922 共享的结构 | 与 Hill 共享但**工作平行独立**；获奖理由各有一句，Meyerhof 半边是 "for his discovery of the fixed relationship between the consumption of oxygen and the metabolism of lactic acid in the muscle"，勿与 Hill 的"肌肉产热"句混用 |
| 博士导师来源 | **Otto Heinrich Warburg** 仅载于 page.md frontmatter（doctoral_advisor），正文未展开——入库成立但 note 注明来源；勿与库内 Emil Warburg（id=2148，物理学家）混淆，亦勿简写 "Otto Warburg" |
| 国籍口径 | frontmatter 国籍 Germany+United States；yaml/总表按 **Nobel 官方口径 Germany**；正文可叙述其流亡美国、逝于费城 |
| 纳粹叙事分寸 | 1938 被逐出教职、流亡巴黎/马赛/美国——史实陈述保持克制，聚焦个人轨迹不展开政治渲染 |
| 出生地点细节 | 生于汉诺威 Theaterplatz 16A（今 Rathenaustrasse 16A）；出生国为普鲁士王国/德意志帝国（1884），国籍行写 Germany 即可 |
| 子女命名 | 次子 Gottfried 移民后用英化名 **Geoffrey**——叙述时注明年份语境，勿混用 |
| EMP 途径的三人 | 途径命名含 Embden 与 Parnas，但 page.md 对二人**无任何关系记载**——只在术语页出现，禁建任何人物关系边 |
| 婚龄锚点 | 1914 与 Hedwig Schallenberg 结婚（海德堡相识）——1914 既是结婚年也是一战爆发年，叙述分开写 |
| KWI → Max Planck | 1929 任 Kaiser Wilhelm Institute for Medical Research（今 Max Planck Institute for Medical Research）所长之一，1938 离任——"今名"仅作括注 |
| 教育序列 | 斯特拉斯堡→海德堡→柏林三校；1909 海德堡毕业（论文为精神医学方向）——勿写"海德堡博士"单一口径之外的杜撰细节 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| fixed relationship | 固定关系 | 获奖理由核心词：氧耗与乳酸代谢间的定量关系 |
| lactic acid | 乳酸 | 肌肉代谢核心分子 |
| glycolysis | 糖酵解 | EMP 途径主体 |
| Embden–Meyerhof–Parnas pathway | EMP 途径（糖酵解共同序列） | 三人共列命名，Meyerhof 居中 |
| muscle metabolism | 肌肉代谢 | 诺奖理由域 |
| energy conversions in muscle | 肌肉中的能量转换 | 1923 诺贝尔演讲题 |
| Kaiser Wilhelm Institute | 威廉皇帝研究所 | 今马克斯·普朗克医学研究所 |
| guest professorship | 客座教授 | 1940 宾大职位口径 |
| Emergency Rescue Committee | 紧急救援委员会 | 1940 援助其赴美的组织 |
| biochemist | 生物化学家 | page.md description 主口径 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Last Hope**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：1940 年法国陷落、马赛港的最后一班船——"最后的希望"正是 Emergency Rescue Committee 援助下的流亡航程；曲名的悲怆与救赎感对应其从 KWI 海德堡到费城宾大的命运转折，也呼应科学在乱世中的存续。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Otto_Fritz_Meyerhof/LastHope.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
