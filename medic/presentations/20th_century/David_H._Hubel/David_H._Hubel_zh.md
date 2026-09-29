# 医学家立传提示词（David H. Hubel）

> 本文件是 OpenMedic 项目「20 世纪诺贝尔生理学或医学奖得主人物专属立传提示词」。
> 目标人物：David H. Hubel（1981 年诺贝尔生理学或医学奖得主，美国）。
> 用途：指导后续 Beamer 立传（15 页）与配套视频制作；事实基准为本地 Wikipedia 页面
> `medic/presentations/pages/20th_century/David_H._Hubel/page.md`（下称 page.md）。
> 社会关系与研究领域已按本文件第三、四节入库 greatminds 库（yaml 与本文件完全一致）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：David Hunter Hubel（戴维·亨特·休伯尔，1926-02-27 加拿大温莎 ~ 2013-09-22 马萨诸塞州林肯镇，享年 87 岁）
- **气质关键词**：**视觉皮层的制图师、简单细胞与复杂细胞的命名者、自制钨丝微电极的巧手** —— 1981 年诺贝尔生理学或医学奖获奖理由（逐字引自 medic/nobel_medicine_citations.json，与 Torsten Wiesel 共享，Sperry 得同年另一半）：
  > "for their discoveries concerning information processing in the visual system"
  > （因其关于视觉系统信息处理的发现）
- **设计母题**：**「朝向选择性」**。猫视皮层的神经元只对特定角度的光条放电——视觉隐喻：一束旋转的光条扫过网格，不同角度点亮不同的神经元单元。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/David_H._Hubel/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 **medic 路径**执行：页面用 `medic/presentations/pages/20th_century/David_H._Hubel/`，成目录 `medic/presentations/20th_century/David_H._Hubel/`，Makefile 复制后设 `MAIN=David_H._Hubel_zh`、`VIDEO_NAME=David_H._Hubel_zh`，BGM 见第九节。
> 第 4 步（研究领域）与第 4.5 步（社会关系）**已完成入库**，见第三、四节。
> 数据库已置 `has_social_data=1`；`has_biography` 待 Beamer 立传完成后置 1。

## 三、研究领域梳理 + 入库（已完成）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | neurophysiology | 神经生理学 | 视皮层结构与功能研究，1981 诺奖核心 | 总览页 |
| 1 | visual system | 视觉系统 | 朝向选择性、简单/复杂细胞、眼优势柱 | 视皮层页 |
| 2 | cortical plasticity | 皮层可塑性 | 单眼剥夺实验与关键期、弱视机理 | 发育页 |

## 四、社会关系梳理 + 入库（已完成，与 MySQL/data/David_H._Hubel.yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Torsten Wiesel | — | 1981 诺贝尔生理学或医学奖两人共享视觉系统一半 |
| co-honored | Roger Wolcott Sperry | — | 1981 同年共享，Sperry 得大脑半球功能特化另一半 |
| collaborator | Torsten Wiesel | — | 1958 年约翰霍普金斯相遇，二十余年研究搭档 |
| spouse | Ruth Izzard | — | 1953 年成婚，2013 年卒 |

> 说明：本篇 page.md 极简（科学史名篇但传记叙事短），按「禁编造」纪律只建 4 条边。Wiesel 与 Hubel 同时建 co-honored + collaborator 双边（1981 半奖+二十年搭档）。Sperry 用 manifest 规范名 Roger Wolcott Sperry（med-batch-26）。无博士导师明载（麦吉尔医学博士）；父亲（化学工程师）与祖父未具名不入库；三个儿子未具名不入库；Kuffler 在 Hubel 页无载（Wiesel 页才出现），Hubel 篇不建边。

## 五、配色方案 【人物专属】

- **气质**：工程巧手与制图耐心、北美实验室的清爽
- **主色**：皮层深青 `#1E5A72`（视皮层方位柱的冷调）
- **诺奖色**：香槟金（奖章/年份徽章专用）
- **四分类色（badgeA-D）**：
  - `badgeA` 神经生理学 — 微电极银灰 `#8A98A8`
  - `badgeB` 视觉系统 — 光条金 `#C8A02E`
  - `badgeC` 皮层可塑性 — 关键期橙 `#C0622E`
  - `badgeD` 计算机视觉 — SIFT 蓝 `#33637D`
- **背景母题**：旋转光条与方位柱网格、稀疏放电尖峰波形，低透明度铺底

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input medic/presentations/cover/）
01  封面 — 视觉皮层的制图师 / David H. Hubel 1926–2013 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像（1992 照）+ 右信息网格（生卒、教育、任职、家庭、荣誉、核心领域）
03  核心贡献概览 — 朝向选择性 / 简单与复杂细胞 / 眼优势柱 / 关键期可塑性
04  温莎-蒙特利尔 (1926–1954) — 美裔家庭、化学与电子少年实验、麦吉尔数学物理转医学
05  麦吉尔与住院医 (1951–1954) — 1951 医学博士、蒙特利尔总医院神经科住院医
06  沃尔特里德：微电极 (1954–1958)（核心页）— 被征入伍、漆包钨丝金属微电极与液压微驱动的发明
07  1958：与 Wiesel 会师（核心页）— 约翰霍普金斯、1959 年猫视皮层实验、朝向选择性的发现
08  简单细胞与复杂细胞 — 光/暗条形反应、感受野、运动方向检测
09  哈佛岁月 (1959–) — 神经生物学系新建、1968 教授、神经生物学教授
10  眼优势柱与单眼剥夺 — 缝合小猫单眼、皮层柱被另一眼接管、双眼视觉丧失
11  关键期与临床意义 — 剥夺性弱视机理、儿童白内障/斜视治疗的科学基础
12  1981 诺贝尔奖（核心页）— citation 原文、与 Wiesel 共享一半、Sperry 另一半、1981-12 领奖
13  荣誉与认可 — Horwitz 1978 · Dickson 1980 · ForMemRS 1982 · Gerard 1993 · 神经科学学会主席 1988-89
14  遗产 — 视觉神经生理学的奠基；SIFT 特征描述符的思想源头（计算机视觉回响）
15  结尾
```

## 七、特殊陷阱表（★ 执行 Beamer 前必读）

| # | 陷阱 | 裁定 |
|---|------|------|
| 1 | 获奖理由表述 | 逐字用 citation 原文 "for their discoveries concerning information processing in the visual system"（their 两人共享）；Sperry 的另一半理由（大脑半球功能特化）不同，勿混写 |
| 2 | 国籍口径 | frontmatter 双值 Canada/United States；Nobel/manifest 口径 United States——yaml 已按 US，正文叙述「加拿大出生、美裔家庭」 |
| 3 | 无师承 | 麦吉尔医学博士（1951）后无正式博士导师明载——禁编造导师；Wiesel 是搭档非学生，Kuffler 在本篇 page.md 无载不建边 |
| 4 | 1959 实验细节 | 微电极插入麻醉猫的初级视皮层、明暗图形投射——「简单细胞」「复杂细胞」命名是两人共同提出，勿归单人 |
| 5 | 两条诺奖理由 | 诺奖归于两大贡献：视觉系统发育（眼优势柱/关键期）+ 视觉神经生理学基础（边缘/运动/立体深度/颜色探测器）——page 明载可作结构帧 |
| 6 | 发明家侧面 | WRAIR 期间发明现代金属微电极（Stoner-Mudge 漆+钨）与液压微驱动——自学习机工技能，工程巧手是本篇人设亮点 |
| 7 | SIFT 回响 | 视觉处理研究启发计算机视觉 SIFT 特征（Lowe 1999）——遗产页可提，注明是灵感渊源而非直接参与 |
| 8 | 家庭 | 妻 Ruth Izzard 2013-02-17 先逝、同年 9 月 Hubel 病逝（肾衰竭）——同年度的双别离，时间线勿错 |
| 9 | 引语红线 | 中学教师 Julia Bradshaw 的英文引语（学写作）有原文可引；其余无直接引语，禁编造 |
| 10 | metadata 冲突 | frontmatter field_of_work 仅 neurophysiology；yaml fields 另两项（visual system/cortical plasticity）均为正文明载主题 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| visual cortex | 视觉皮层 | 初级视皮层 V1 语境 |
| simple cell / complex cell | 简单细胞 / 复杂细胞 | Hubel-Wiesel 命名 |
| orientation selectivity | 朝向选择性 | 特定角度光条反应 |
| ocular dominance column | 眼优势柱 | 左右眼输入交替的皮层柱 |
| critical period | 关键期 | 发育可塑性的时间窗 |
| deprivation amblyopia | 剥夺性弱视 | 单眼剥夺后果 |
| strabismus | 斜视 | 临床意义语境 |
| microelectrode | 微电极 | 其 WRAIR 发明 |
| hydraulic microdrive | 液压微驱动 | 其发明 |
| monocular deprivation | 单眼剥夺 | 缝合眼睑实验 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**SEA** — Alex-Productions（manifest 预分配）
- **匹配理由**：
  - 「海」的纵深匹配视觉信息处理的层级之海——从光点到边缘到运动到立体深度，一层层潜入皮层
  - 宽广克制的编曲契合其二十五年如一日的制图耐心
- **备选**（未采用）：Expedition（本批 Wiesel 已用，双人组曲目须区分）、Ascension（上升意象偏探险叙事）
- **本地路径**：按 music_audio/ 内 Alex-Productions SEA 曲目复制至 `medic/presentations/20th_century/David_H._Hubel/SEA.wav`，ffmpeg `-shortest` 对齐
