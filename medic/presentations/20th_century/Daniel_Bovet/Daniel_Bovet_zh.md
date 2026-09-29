# 医学家立传提示词（Daniel Bovet）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1957 年得主 Daniel Bovet（达尼埃尔·博韦）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Daniel_Bovet/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Daniel Bovet（1907-03-23 生于瑞士 Fleurier ~ 1992-04-08 逝于罗马，享年 85 岁），瑞士出生的意大利药理学家，ForMemRS，母语世界语者
- **气质关键词**：**抗组胺之父、神经递质阻断剂的开拓者、世界语科学家**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1957 条目，独得）：
  > "for his discoveries relating to synthetic compounds that inhibit the action of certain body substances , and especially their action on the vascular system and the skeletal muscles"（因其发现能抑制某些体内物质作用的合成化合物，尤其是它们对血管系统与骨骼肌的作用）
- **设计母题**：**一把锁住组胺的合成钥匙（synthetic compound blocking histamine）**——1937 年首个抗组胺药阻断"身体自身的物质"；用「分子钥匙锁住受体」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Daniel_Bovet/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；第 0/1/2/3 步按 medic 路径执行：页面已在 `medic/presentations/pages/20th_century/Daniel_Bovet/`（肖像见 images.txt；若无真实肖像用装饰圆占位）。Makefile 复制后设 `MAIN=Daniel_Bovet_zh`、`VIDEO_NAME=Daniel_Bovet_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Bovet 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | pharmacology | 药理学 | infobox Fields 明载，1957 诺奖学科 | 全篇 |
| 1 | neuropharmacology | 神经药理学 | 阻断神经递质作用；交感神经系统研究 | 核心页 |
| 2 | medicinal chemistry | 药物化学（合成化合物） | 获奖理由核心词；磺胺、抗组胺合成 | 核心页 |
| 3 | chemotherapy | 化学治疗 | 早期化疗方向研究 | 核心页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Filomena Nitti | 无向 | 妻子 |

**在库诚实值说明（★ 本批次最简）**：Bovet 的 page.md 叙事极简（无导师/学生/合作者具名），relations=1 为诚实值，Review 勿以"关系太少"为由补边；其意大利药理学界人脉（含妻族 Nitti 家背景）page.md 无载，一律不入库。

**不入库但提示词可叙述**：日内瓦大学 1927 毕业/1929 博士（导师无载，勿杜撰）；巴斯德研究所 1929-1947 与罗马高等卫生研究所 1947 起（机构履历非个人关系）。

## 五、配色方案 【人物专属】

- **气质**：合成化学的冷峻、过敏季的清朗、罗马的暖色晚年
- **主色**：`#5E3A87`（药紫——合成分子与实验室玻璃）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeAnti` 抗组胺 — 药紫 `#5E3A87`
  - `badgeNeuro` 神经药理 — 深蓝 `#1E4E79`
  - `badgeSynth` 合成化合物 — 青灰 `#0E7490`
  - `badgeHonor` 荣誉传承 — 暗红 `#7A2430`
- **背景母题**：分子锁钥图案与受体表面，稀疏排布。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 抗组胺之父 / Daniel Bovet 1907–1992 + 四色 badge + 右上头像/装饰圆 + 国籍行（Switzerland→Italy）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Fleurier 出身、日内瓦大学、巴斯德研究所/罗马高等卫生
    研究所/萨萨里大学/罗马一大任职、诺奖 1957、核心领域；世界语母语者注脚）
03  核心贡献概览 — 抗组胺 1937 / 磺胺与化疗 / 箭毒药理 / 交感神经系统
04  瑞士湖畔与世界语童年 (1907–1929) — Fleurier 出生、世界语母语、日内瓦大学 1927/1929
05  巴黎巴斯德研究所 (1929–1947) — 十八年法国岁月
06  1937：第一个抗组胺药（核心贡献页）— 阻断组胺这一"体内物质"、过敏症治疗的起点
07  磺胺与化学治疗 — 早期化疗与磺胺药物研究
08  交感神经系统与箭毒 — 箭毒（curare）药理研究、骨骼肌阻断（获奖理由的另一半）
09  1947 迁罗马：意大利岁月 — 高等卫生研究所、1949 Cameron Prize
10  1957 诺奖：独得 — 获奖理由逐字呈现（合成化合物抑制体内物质：血管系统与骨骼肌）
11  萨萨里与罗马一大 (1964–1982) — 1964 萨萨里教授、1969-71 CNR 心理生物学与心理药理学实验室主任、1982 退休
12  1965 年的吸烟研究 — 团队结论与其对纽约时报的表述（见陷阱表：建议回避或客观一句）
13  荣誉与认可 — Cameron Prize 1949、ForMemRS、蒙彼利埃/巴黎/南锡/斯特拉斯堡荣誉博士
14  遗产与结尾 — 抗组胺药的日常化、神经药理学的奠基 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 姓名口径 | **yaml/入库用 manifest 形式 "Daniel Bovet"**；封面写 Daniel Bovet 1907–1992 即可 |
| 国籍口径 | 瑞士出生、瑞士-意大利双籍（citation json "Switzerland Italy"；metadata 含 Kingdom of Italy 历史噪声不入库）——yaml 已双入 Switzerland(0)+Italy(1)；封面国籍行写 Switzerland → Italy 迁移叙事 |
| 独得诺奖 | 1957 为单元奖，获奖理由 "for **his** discoveries..."——勿写共享，无 co-honored 边 |
| 无导师/学生边 | page.md 全程未载博士导师与任何学生姓名——**不建 advisor-student 边**；配偶 Filomena Nitti 是唯一明载关系（relations=1 诚实值） |
| 获奖理由逐字 | json 原文 "synthetic compounds that inhibit the action of certain body substances"——获奖对象是"抑制体内物质（组胺、神经递质等）的合成化合物"整体工作，勿窄化为"发明抗组胺药"单一表述（1937 抗组胺只是最著名一项） |
| 1937 年归属 | 抗组胺发现于 1937（page.md 明文），在巴斯德研究所时期——勿系到罗马时期 |
| 1965 吸烟研究 | page.md 载其团队结论"吸烟提高智力"及对 NYT 的引语——**与现代科学共识相悖的争议结论，建议整体回避**；如需提及仅客观一句"1965 年曾领导一项备受争议的吸烟与智力关系研究"，勿引用其原话渲染 |
| 职年链 | 日内瓦 1927 毕业/1929 博士 → 巴斯德 1929-1947 → 罗马高等卫生研究所 1947 → 萨萨里教授 1964 → CNR 实验室主任 1969-71 → 罗马一大教授 → 1982 退休——勿串 |
| 荣誉年份 | Cameron Prize 1949（爱丁堡）、ForMemRS、蒙彼利埃/巴黎/南锡/斯特拉斯堡荣誉博士——年份 page.md 多未载，荣誉页按名单呈现勿编年份 |
| 世界语元素 | 母语世界语者（native Esperanto speaker）——身份页特色注脚，可提 Esperantist 身份 |
| 生卒地 | 生于瑞士 Fleurier（纳沙泰尔州湖区小镇）、逝于罗马——勿互换 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| antihistamine | 抗组胺（药） | 1937 年发现，获奖理由的代表性成果 |
| histamine | 组胺 | 被阻断的"体内物质" |
| neurotransmitter | 神经递质 | 获奖理由的另一表述层 |
| synthetic compounds | 合成化合物 | 获奖理由核心词 |
| vascular system | 血管系统 | 获奖理由明载的作用对象 |
| skeletal muscles | 骨骼肌 | 箭毒作用的靶点 |
| curare | 箭毒 | 其药理研究对象 |
| sulfonamide (sulfa drugs) | 磺胺类药物 | 研究方向之一 |
| chemotherapy | 化学治疗 | 此处指广义药物化疗，非肿瘤化疗专义 |
| sympathetic nervous system | 交感神经系统 | 研究方向之一 |
| Esperanto | 世界语 | 其母语，人物特色 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Pathfinder**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：从瑞士湖畔到巴斯德研究所再到罗马，Bovet 一生都在"合成分子"的无人区里探路——抗组胺、箭毒药理、神经递质阻断，每一步都是开辟新航道的先遣者；Pathfinder 的开拓感正对应他"用合成化合物驯服体内物质"的先导地位。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Daniel_Bovet/Pathfinder.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
