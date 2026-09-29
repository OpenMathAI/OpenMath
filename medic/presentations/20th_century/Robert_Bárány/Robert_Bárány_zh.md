# 医学家立传提示词（Robert Bárány）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1914 年得主 Robert Bárány（罗伯特·巴拉尼）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Robert_Bárány/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Robert Bárány（1876-04-22 生于维也纳，奥匈帝国 ~ 1936-04-08 逝于瑞典乌普萨拉，享年 59 岁）
- **气质关键词**：**前庭器官的探路者、温度试验的发明人、战俘营里的诺奖得主**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1914 条目）：
  > "for his work on the physiology and pathology of the vestibular apparatus"（因其关于前庭器官的生理学与病理学的研究）
- **设计母题**：**平衡与水流（equilibrium & caloric flow）**——冷热液体注入外耳道引起内淋巴沉浮、眼震方向翻转，是「温度驱动内流、前庭感知平衡」的视觉隐喻：错落的同心圆与流向箭头构成背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Robert_Bárány/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`（OpenMedic 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/20th_century/Robert_Bárány/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Robert_Bárány_zh`、`VIDEO_NAME=Robert_Bárány_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Bárány 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | otolaryngology | 耳鼻喉科学 | infobox Fields；临床身份核心 | 封面、核心页 |
| 1 | vestibular physiology | 前庭生理学 | 温度试验（caloric reaction），诺奖核心 | 核心页 |
| 2 | neurophysiology | 神经生理学 | 平衡控制与小脑功能研究 | 核心页 |
| 3 | otology | 耳科学 | 前庭器官疾病外科治疗由此成为可能 | 应用页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Gösta Dohlman | Bárány → 学生 | infobox Doctoral students 明载 |
| controversy | Sigmund Freud | 无向 | 1917 巴拉尼提名弗洛伊德获奖；弗洛伊德自述多年前拒收其为弟子并对巴拉尼获奖不快 |
| spouse | Ida Felicitas Berger | 无向 | 1909-03-09 结婚，妻 1881-12-12 生 |
| parent-child | Ernst Bárány | Bárány → 子 | 医生、瑞典皇家科学院成员（1910–1991） |

**不入库但提示词可叙述**：孙子 Anders Bárány（物理学家、诺贝尔物理学委员会前秘书，隔代不入 parent-child）；Nils Gunnar Holmgren 教授与瑞典卡尔王子主导 1916 获释外交斡旋（一次性事件，非持续关系）；祖父同名 Ignác Bárány。

## 五、配色方案 【人物专属】

- **气质**：冷静、临床、内耳深处的暗流
- **主色**：`#0E7490`（前庭青——耳蜗迷路冷水的临床感）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeVest` 前庭生理 — 青蓝 `#0E7490`
  - `badgeClin` 临床耳科 — 深蓝 `#16324F`
  - `badgeWar` 战俘与获释 — 灰紫 `#52307C`
  - `badgeFam` 家学传承 — 琥珀 `#C07A2A`
- **背景母题**：同心圆与流向箭头（眼震方向随冷热翻转的抽象），呼应「温度驱动内淋巴流动」的核心发现。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 前庭器官的探路者 / Robert Bárány 1876–1936 + 四色 badge + 右上头像 + 国籍行（Austria-Hungary）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地维也纳、教育维也纳大学 MD 1900、
    任职乌普萨拉大学 1917–1936、诺奖 1914、核心领域）
03  核心贡献概览 — 温度试验 / 前庭器官生理与病理 / 小脑与平衡 / BPPV 首述
04  早年与家庭教育 (1876–1900) — 维也纳，六子女之长，父匈牙利裔银行职员
05  维也纳医学院与临床转机 (1900s) — 洗耳水过冷引发眩晕与眼震的临床观察
06  温度试验：内淋巴的冷降热升（核心贡献页）— caloric reaction 与本体感受信号
07  前庭疾病外科治疗的开启 — 手术可能性的确立
08  小脑与平衡控制 — 平衡研究的另一翼
09  一战军医与战俘岁月 (1914–1916) — 奥匈军文职外科医生，被俄军俘获
10  战俘营里的诺贝尔奖 — 1914 授奖身陷囹圄；瑞典丹挪荷+红十字会斡旋 1916 获释、赴典领奖
11  提名弗洛伊德的插曲 (1917) — 得奖后自动提名资格；Freud 的回应（引语原文）
12  乌普萨拉岁月 (1917–1936) — 医学院教授直至去世，逝于六十岁生日前
13  以 Bárány 命名 — Bárány chair（旋转椅试验）、Robert Bárány Award
14  遗产与结尾 — 前庭功能检查的现代临床格局 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 授奖年份 vs 领奖年份 | 1914 授奖时 Bárány 是俄国战俘，**1916 年**才经瑞典/丹麦/挪威/荷兰+红十字会联合外交斡旋获释并出席授奖典礼；勿写"1914 亲自领奖" |
| 国籍口径 | yaml 按 Nobel 官方口径填 **Austria-Hungary**；frontmatter 国籍列 Cisleithania/Sweden/Austria 系 Wikidata 噪声，page.md 正文只说生于维也纳（奥匈）、逝于瑞典乌普萨拉 |
| Freud 关系表述 | page.md 明载两件事：Bárány 1917-01 利用得主提名权提名 Freud；Freud 恼火并自述多年前"因其过于反常"拒收其为弟子。写 controversy 时弗洛伊德引语必须用 page.md 原文（"The granting of the Nobel Prize to Bárány, whom I refused to take as a pupil..."），不可改写为中文"原话" |
| BPPV 首述 | "is **said to have been** first described in medical texts by Bárány"——用"据称/被认为首次描述"，勿写成断言 |
| 温度试验原理 | 内淋巴遇冷下沉、遇热上升，流动方向提供本体感受信号——这是 Bárány 当年的理论解释，按 page.md 口径转述 |
| 儿孙两代 | 子 Ernst Bárány（医生、瑞典皇家科学院成员，入库 parent-child）；孙 Anders Bárány（物理学家，不入库）；勿混淆 |
| 获释斡旋 | 主导者是耳鼻喉科教授 Nils Gunnar Holmgren + 瑞典卡尔王子（外交），红-link 人物，不建库边 |
| metadata 噪声 | metadata.json description 拼作 "Austri-Hungarian"；以正文为准 |
| 乌普萨拉任期 | 1917 年起任乌普萨拉大学医学院教授直至 1936 去世，"去世前约 60 岁生日不久"，享年 59 |
| 诺奖演讲 | 1916-09-11 题为 *Some New Methods for Functional Testing of the Vestibular Apparatus and the Cerebellum*，勿与获奖理由混淆 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| vestibular apparatus | 前庭器官 | 获奖理由核心词，勿写成"耳蜗" |
| caloric reaction / caloric test | 温度试验 | 冷热水注入外耳道诱发眼震 |
| nystagmus | 眼球震颤 | 冷热方向相反、翻转出现 |
| endolymph | 内淋巴 | 冷降热升的解释模型 |
| vertigo | 眩晕 | 症状名，勿译"头晕"泛化 |
| BPPV (benign paroxysmal positional vertigo) | 良性阵发性位置性眩晕 | "said to be first described"措辞 |
| cerebellum | 小脑 | Bárány 平衡研究的另一对象 |
| Bárány chair | 巴拉尼旋转椅 | 试验器械命名 |
| otology | 耳科学 | 与 otolaryngology（耳鼻喉科）层次不同 |
| prisoner of war | 战俘 | 1914–1916 经历，叙事主线之一 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**The Invisible Light**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：内耳前庭深藏于颞骨之中、功能无形却主宰平衡——"不可见之光"的隐喻恰好对应「看不见的平衡器官」；曲名的深邃感也贴合战俘营黑暗中获批诺奖的戏剧弧线。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Robert_Bárány/TheInvisibleLight.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
