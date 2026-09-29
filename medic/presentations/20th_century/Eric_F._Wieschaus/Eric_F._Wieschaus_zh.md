# 医学家立传提示词（Eric F. Wieschaus）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1995 年得主 Eric F. Wieschaus（埃里克·弗朗西斯·威绍斯）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Eric_F._Wieschaus/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Eric Francis Wieschaus（1947-06-08 生于美国印第安纳州南本德，在世）
- **气质关键词**：**海德堡筛选的另一位执灯人、合子基因转录的破译者、普林斯顿的果蝇学家**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1995 条目，与 Lewis、Nüsslein-Volhard 三人共享同一理由）：
  > "for their discoveries concerning the genetic control of early embryonic development"（因他们发现早期胚胎发育的遗传控制）
- **设计母题**：**合子基因的开关（zygotic transcription）**——母源产物铺好底图、合子基因接管发育时序的意象：以母源底图上渐次亮起的合子基因开关作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Eric_F._Wieschaus/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；第 0/1/2/3 步按 medic 路径执行：页面已在 `medic/presentations/pages/20th_century/Eric_F._Wieschaus/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Eric_F._Wieschaus_zh`、`VIDEO_NAME=Eric_F._Wieschaus_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | developmental biology | 发育生物学 | infobox Fields；果蝇胚胎发生 |
| 1 | genetics | 遗传学 | 饱和突变筛选（海德堡筛选） |
| 2 | embryogenesis | 胚胎发生 | 早期果蝇胚胎图式发生 |
| 3 | evolutionary developmental biology | 演化发育生物学 | 正文对其身份的表述 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Gertrud Schüpbach | 无向 | 分子生物学家，普林斯顿分子生物学教授（果蝇卵子发生方向） |
| colleague | Christiane Nüsslein-Volhard | 无向 | 1978 EMBL 海德堡共建实验室（海德堡筛选双人组） |
| co-honored | Christiane Nüsslein-Volhard | 无向 | 1995 诺贝尔生理学或医学奖三人共享（早期胚胎发育的遗传控制） |
| co-honored | Edward B. Lewis | 无向 | 1995 诺贝尔生理学或医学奖三人共享（早期胚胎发育的遗传控制） |

**在世者关系少为诚实值**（4 条）：page.md 未载 Wieschaus 的博士导师（圣母大学 BS、耶鲁 PhD 均无导师姓名）——Review 勿补造边。**不入库但提示词可叙述**：三位女儿（家庭叙述）；2007 年 77 位诺奖得主联名请愿废除路易斯安那科学教育法（公共事件，无神论者身份一并客观一句）。

## 五、配色方案 【人物专属】

- **气质**：印第安纳的朴素、显微镜前的专注、普林斯顿的沉静
- **主色**：`#14647E`（青蓝——果蝇胚胎透视的冷光）+ 香槟金诺奖色
- **badge 四分类色**：`badgeZygotic` 合子基因 青蓝 `#14647E`；`badgeHeidelberg` 海德堡筛选 深紫 `#4A2A6A`；`badgeMaternal` 母源产物 琥珀 `#C07A2A`；`badgePrinceton` 普林斯顿 深蓝 `#1E4E79`
- **背景母题**：母源底图上渐次亮起的合子基因开关图案，呼应「合子基因的开关」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 果蝇胚胎基因的破译者 / Eric F. Wieschaus 1947– + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1947-06-08 南本德、
    圣母大学 BS、耶鲁 PhD、EMBL 海德堡 1978、普林斯顿 Squibb 讲席、诺奖 1995）
03  核心贡献概览 — 海德堡筛选 / 合子基因 / 母源 vs 合子转录 / 饱和突变
04  印第安纳与阿拉巴马少年 (1947–1965) — 南本德出生、John Carroll Catholic 高中（伯明翰）
05  圣母大学与耶鲁 (1965–) — 生物学 BS；耶鲁 PhD（生物学，导师未载）
06  1978：EMBL 海德堡（核心贡献页）— 首个独立职位、与 Nüsslein-Volhard 共建实验室
07  海德堡筛选（核心贡献页）— 染色体致死性突变的饱和测试、EMS 诱变、
    体节与小齿带表型逐一看片、1980 发表 15 个分节基因
08  母源与合子的分工 — 早期胚胎多靠未受精卵中的母源转录产物、
    少数基因由胚胎自身"合子"转录——时空模式或为发育触发器
09  从分节到形态发生 — 突变互作研究推进对体节逐步发育机制的理解；
    1981 迁普林斯顿
10  普林斯顿岁月 (1981–) — Squibb 分子生物学讲席；RWJ 医学院兼职生化教授（曾任）
11  1995 诺奖 — 与 Lewis、Nüsslein-Volhard 共享；Nobel 讲演
    "From Molecular Patterns to Morphogenesis: The Lessons from Drosophila"（1995-12-08）
12  荣誉与认可 — AAAS 1993、NAS 1994、GSA Medal 1995、Nobel 1995、
    Mendel Medal 1999（英国遗传学会）、SDB 终身成就奖 2018、Pour le Mérite
13  家庭 — 与分子生物学家 Gertrud Schüpbach 结婚（普林斯顿教授、果蝇卵子发生方向）、
    三女；无神论者与 2007 科学教育请愿（客观一句）
14  遗产与结尾 — 发育基因学的今日面貌：从海德堡筛选到 evo-devo
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 页面极短 | Wieschaus page.md 仅 ~76 行——事实基准逐句对应，勿从诺奖官网或其他来源补写细节 |
| 师承为零 | 圣母大学 BS、耶鲁 PhD 均无导师姓名（page.md 未载）——师承边为零是诚实值，勿补造 |
| 海德堡筛选分工 | 与 Nüsslein-Volhard 共建共享（两人 1978 EMBL 建组）——"saturation ... was done by Eric Wieschaus" 的表述体现其执行角色，双人叙述对等 |
| 合子基因定位 | Wieschaus 的研究重心是"合子活性基因"（zygotically active genes）——与 N-V 的母源效应因子研究呼应但有分工侧重，叙述勿互串 |
| 配偶 | Gertrud Schüpbach 是普林斯顿分子生物学教授（果蝇卵子发生）——spouse 边；同校同领域可一句叙述，勿另建 colleague 边 |
| 身份表述 | page.md 称 "evolutionary developmental biologist"、Fields 却是 Developmental biology——yaml 用 developmental biology，正文可用演化发育生物学表述 |
| 2007 请愿 | 77 位诺奖得主联名废除 Louisiana Science Education Act——公共事件客观一句，不展开政见 |
| 在世者生卒 | 仅生年 1947-06-08，无卒年——封面 1947– 开放区间 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| embryogenesis | 胚胎发生 | 研究对象 |
| zygotically active genes | 合子活性基因 | Wieschaus 的侧重 |
| maternal transcription | 母源转录 | 卵子发生期产物 |
| oogenesis | 卵子发生 | 其妻 Schüpbach 的方向 |
| saturation screen | 饱和筛选 | 染色体致死突变全覆盖 |
| segmentation | 分节 | 果蝇幼虫体节 |
| Heidelberg screen | 海德堡筛选 | 1978–1980 |
| Squibb Professor | Squibb 讲席教授 | 普林斯顿头衔 |
| denticles | 小齿带 | 幼虫表皮表型标记 |
| evo-devo | 演化发育生物学 | 其身份表述之一 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**With Me**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：海德堡筛选是两个人的长征——Wieschaus 与 Nüsslein-Volhard 在 EMBL 并肩三年看片十万计；"With Me" 的同行感正对应这段双人组歌，也呼应与妻子同在普林斯顿果蝇学界的家庭图景。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Eric_F._Wieschaus/With_Me.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
