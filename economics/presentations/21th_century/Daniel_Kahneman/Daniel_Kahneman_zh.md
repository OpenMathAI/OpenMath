# 经济学家立传提示词（Daniel Kahneman）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2002 年得主 Daniel Kahneman（丹尼尔·卡尼曼）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Daniel_Kahneman/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标人物**：Daniel Kahneman（1934-03-05 生于英属巴勒斯坦托管地特拉维夫 ~ 2024-03-27 逝于瑞士宁宁根，享年 90 岁）
- **气质关键词**：**行为经济学之父（自称"祖父"）、不确定条件下人类判断的测绘者、拿诺贝尔经济学奖的心理学家**
- **诺奖获奖理由**（2002 拆分年份，本人那条逐字取自 `economics/nobel_economics_citations.json`；中译对照 `economics/economics_list_data.py` 2002 年 "||" 前段）：
  > "for having integrated insights from psychological research into economic science, especially concerning human judgment and decision-making under uncertainty"
  > （表彰他将心理学研究的洞见融入经济科学，特别是关于不确定条件下的人类判断与决策）
- **设计母题**：**双系统与峰值（two systems & the peak）**——快思考与慢思考双轨并行、体验自我与记忆自我分离、峰值-终值法则支配回忆；视觉隐喻用「双轨道光带/心电图式峰谷曲线」。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Daniel_Kahneman/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Daniel_Kahneman/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Daniel_Kahneman_zh`、`VIDEO_NAME=Daniel_Kahneman_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库（yaml 在 `MySQL/data/Daniel_Kahneman.yaml`），无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Kahneman 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | behavioral economics | 行为经济学 | 诺奖核心，被称为该领域奠基人 | 核心页 |
| 1 | cognitive psychology | 认知心理学 | 本行：注意与努力（Attention and Effort） | 心理学页 |
| 2 | judgment and decision-making | 判断与决策 | 启发法与偏差、前景理论 | 核心页 |
| 3 | hedonic psychology | 享乐心理学 | 体验效用、峰值-终值法则、幸福感测量 | 幸福页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Susan M. Ervin-Tripp | Kahneman → 学生 | UC Berkeley 博士导师（1961 语义微分论文） |
| co-honored | Vernon L. Smith | 无向 | 2002 诺贝尔经济学奖同届拆分共享（理由句各一） |
| collaborator | Amos Tversky | 无向 | 1969 起终身合作者，启发法与偏差、前景理论 |
| collaborator | Paul Slovic | 无向 | 1982 Judgment Under Uncertainty 合编者 |
| collaborator | Jack Knetsch | 无向 | 公平与禀赋效应论文合著者 |
| collaborator | Cass Sunstein | 无向 | Noise 2021 合著者 |
| collaborator | Olivier Sibony | 无向 | Noise 2021 合著者 |
| colleague | Richard Thaler | 无向 | 行为经济学相互影响，1984-85 UBC 共事 |
| spouse | Irah Kahn | 无向 | 第一任妻子，学生时代结婚后离异 |
| spouse | Anne Treisman | 无向 | 1978 结婚，认知心理学家，2018 去世 |
| influence | Yeshayahu Leibowitz | 无向 | 中学化学与大学生理学教授，自述智识发展所受影响 |

**不入库但提示词可叙述**：子女 Lenore（协助准备诺贝尔演讲）与 Michael（未载姓氏，仅有名无姓不入库）；Barbara Tversky（2020 起伴侣，Amos Tversky 遗孀，恋情无对应类型不入库，沿用 lit-batch Galina Kuznetsova 先例）；父母 Efrayim 与 Rachel（大屠杀岁月叙述可写，入边从简不建）。

## 五、配色方案 【人物专属】

- **气质**：理性的怀疑者、明暗双轨、90 年岁月的沉思
- **主色**：`#46356B`（manifest 预分配的暗紫——双系统交界处的暮色）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeProspect` 前景理论 — 暗紫 `#46356B`
  - `badgeBias` 启发法与偏差 — 玫瑰 `#C4204F`
  - `badgeHedon` 享乐心理学 — 琥珀 `#C07A2A`
  - `badgeCog` 认知心理学 — 靛蓝 `#16324F`
- **背景母题**：双轨光带与峰谷曲线（快慢两轨平行延伸、心电图式峰值标注），呼应「体验自我与记忆自我」的分离。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 行为经济学之父 / Daniel Kahneman 1934–2024 + 四色 badge + 右上头像 + 国籍行（Israel / United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地特拉维夫、教育 Hebrew U BS 1954/
    UC Berkeley PhD 1961、任职 Hebrew U→UBC→Berkeley→Princeton 1993–、诺奖 2002、核心领域）
03  核心贡献概览 — 前景理论 / 启发法与偏差 / 峰值-终值法则 / 思考快与慢
04  巴黎童年与逃亡岁月 (1934–1948) — 立陶宛犹太家庭、占领期经历（Nobel bio 引语原文可入）、
    1948 迁巴勒斯坦（客观简述）
05  耶路撒冷与军旅 (1954–1958) — Hebrew U 心理学+数学、IDF 心理部门面试量表
06  Berkeley 博士：Ervin-Tripp 门下 (1958–1961) — 语义微分分析模型、Fortran
07  与 Tversky 的相遇 (1969) — 希伯来大学讲座、掷硬币定署名、"inseparable"
08  前景理论 (1979)（核心贡献页）— Econometrica 发表、损失厌恶、参照点、经济学最高引
09  启发法与偏差 — 小数定律、锚定、可得性、1982 合编
10  从以色列到普林斯顿 (1978–1993) — UBC、Berkeley、与 Thaler/Knetsch 的公平与禀赋效应研究
11  享乐心理学与幸福感测量 — 体验自我 vs 记忆自我、峰值-终值法则、Day-Reconstruction Method
12  诺奖时刻 (2002) — 心理学家得经济学奖、Tversky 1996 早逝未能共享（Thinking Fast and Slow
    引言原文可入）、Presidential Medal of Freedom 2013
13  思考，快与慢与 Noise — 2011 畅销书、2021 与 Sibony/Sunstein 合著、聚焦错觉名言
14  遗产与结尾 — 行为经济学的世纪回响 + 结尾页（品牌 OpenMathAI）
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由拆分 | 2002 为拆分年份：Kahneman 理由="...integrated insights from psychological research..."（心理学洞见融入经济科学），与 Vernon Smith 的实验室实验理由**各一条**，勿写同一句 |
| 共享奖不是同题 | Kahneman（心理学洞见）与 Smith（实验室实验）工作互不相关，仅同届获奖；co-honored note 须写「同届拆分共享、理由句各一」 |
| primary_occupation | 按 page.md 首句取 **psychologist**（非 economist）——他是"拿经济学奖的心理学家"，此定位是本篇灵魂，yaml 已照此入库 |
| Tversky 未能共享 | Tversky 1996 去世（59 岁），诺奖不追授；Thinking, Fast and Slow 引言明载 "would have shared had he not died"——原文可引，勿写成"Tversky 被排除" |
| 国籍与出生地 | 生于特拉维夫（英属巴勒斯坦托管地）、童年在巴黎、公民身份 American/Israeli；yaml nationalities 按 manifest 填 United States + Israel 两条 |
| 死因表述 | 2024-03-27 逝于瑞士宁宁根，协助死亡（Pegasos），2025-03 才公开——按 page.md 客观一句陈述，位置在 Death 节，勿渲染 |
| 伴侣不入库 | Barbara Tversky（2020-2024 伴侣）无婚姻关系，infobox 列 Partner 非 spouse，不入库；Amos Tversky 遗孀身份仅叙述 |
| 子女不入库 | Lenore 与 Michael 仅有名无姓，沿用 Domagk 女儿先例不入库 |
| 政治内容红线 | 以色列/巴勒斯坦相关背景只作出生地与家庭迁徙客观陈述；本书其余政治议题一律不展开 |
| 引语红线 | Nobel bio 的德国士兵记忆、Thinking Fast and Slow 的聚焦错觉句 "Nothing in life is as important as you think it is when you are thinking about it." 均有英文原文，可引原文+译文；其余中文转述禁加引号 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| prospect theory | 前景理论 | 1979 Econometrica，勿写成"展望理论"之外的随意译名 |
| loss aversion | 损失厌恶 | 前景理论核心，损失痛感大于收益快感 |
| heuristics and biases | 启发法与偏差 | 与 Tversky 的纲领性概念 |
| anchoring | 锚定效应 | Judgment Under Uncertainty 引入 |
| peak–end rule | 峰值-终值法则 | 记忆效用的评判规则 |
| experienced vs remembered utility | 体验效用与记忆效用 | 两个自我，勿混用 |
| focusing illusion | 聚焦错觉 | 与 Schkade 提出，最著名格言载体 |
| affective forecasting | 情感预测 | 预测未来体验效用的偏差 |
| Thinking, Fast and Slow | 《思考，快与慢》 | 2011，系统 1/系统 2 大众化表述 |
| Noise | 《噪声》 | 2021 与 Sibony/Sunstein 合著，勿与其前作混淆 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Expedition**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：「远征」贴合其跨越心理学与经济学两大洲的探索——从特拉维夫到巴黎到耶路撒冷到伯克利到普林斯顿，每一步都是对人类判断迷宫的勘测；曲名的行进感也匹配 60 年学术生涯的长途跋涉。
- **本地路径**：复制 `music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav` 到 `economics/presentations/21th_century/Daniel_Kahneman/Expedition.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
