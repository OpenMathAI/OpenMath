# 医学家立传提示词（Earl Wilbur Sutherland Jr.）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1971 年得主 Earl Wilbur Sutherland Jr.（厄尔·萨瑟兰）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Earl_Wilbur_Sutherland_Jr./page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Earl Wilbur Sutherland Jr.（1915-11-19 生于美国堪萨斯州伯林盖姆 ~ 1974-03-09 逝于佛罗里达州迈阿密，享年 58 岁）
- **气质关键词**：**第二信使 cAMP 的发现者、激素作用机制的破译者、被时代过早带走的大师**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1971 条目，独得）：
  > "for his discoveries concerning the mechanisms of the action of hormones"（因他发现激素的作用机制）
- **设计母题**：**第二信使（cAMP）**——激素在细胞膜外敲门、cAMP 作为信使在胞内传令的意象：以膜外钥匙+胞内涟漪传令的图案作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Earl_Wilbur_Sutherland_Jr./page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；第 0/1/2/3 步按 medic 路径执行：页面已在 `medic/presentations/pages/20th_century/Earl_Wilbur_Sutherland_Jr./`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Earl_Wilbur_Sutherland_Jr._zh`、`VIDEO_NAME=Earl_Wilbur_Sutherland_Jr._zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | signal transduction | 信号转导 | cAMP 第二信使，1971 诺奖核心 |
| 1 | biochemistry | infobox Fields | 糖原磷酸化酶系列研究 |
| 2 | pharmacology | 药理学 | 药理系主任（Case Western 1953、专业本行） |
| 3 | endocrinology | 内分泌学 | 肾上腺素与胰高血糖素作用机制 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Carl Ferdinand Cori | 对方 → 导师 | 华盛顿大学圣路易斯药理学实验室研究导师（1940 起；引其走上科研路）；库内规范名 id=3460 |
| colleague | Theodore W. Rall | 无向 | Case Western 药理学同事、终身研究伙伴（cAMP 共同发现线） |
| advisor-student | Ferid Murad | Sutherland → 学生 | infobox Doctoral students 明载（1998 诺奖得主） |
| spouse | Mildred Rice | 无向 | 1937 结婚，1962 离异；二子一女 |
| spouse | Claudia Sebeste Smith | 无向 | 1963 结婚（范德堡助理院长），相伴终生 |

**在世者关系少为诚实值**（独得诺奖、无 co-honored，5 条）：**不入库但提示词可叙述**：Walter D. Wosilait、Jacques Berthet（JBC 四部曲论文合作者，一次性论文合作）；George S. Patton（二战巴顿麾下营军医，军旅经历非关系）；Edith M. Hartshorn 与 Earl W. Sutherland（父母，家世叙述）；Heidi E. Hamm（Sutherland 讲席首任持有者，纪念性提及）。

## 五、配色方案 【人物专属】

- **气质**：堪萨斯草原的朴素、实验的反复试错、信使的灵光
- **主色**：`#8A1E2D`（深砖红——糖原磷酸化酶系列论文的红字标题）+ 香槟金诺奖色
- **badge 四分类色**：`badgeCAMP` cAMP 第二信使 深砖红 `#8A1E2D`；`badgeLP` 磷酸化酶 青绿 `#0E7C7B`；`badgeHormone` 激素机制 深蓝 `#1E4E79`；`badgeTrial` 试错之路 琥珀 `#C07A2A`
- **背景母题**：膜外钥匙+胞内涟漪传令图案，呼应「第二信使」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 第二信使的发现者 / Earl W. Sutherland Jr. 1915–1974 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1915-11-19 伯林盖姆 ~ 1974-03-09 迈阿密、
    Washburn BS 1937、华盛顿大学圣路易斯 MD 1942、Case Western/Vanderbilt/迈阿密、诺奖 1971）
03  核心贡献概览 — 肝磷酸化酶限速 / 匀浆化突破 / cAMP 鉴定 / 第二信使概念
04  堪萨斯少年 (1915–1937) — 杂货店主之家、体育多面手、Washburn 学院半工半读 BS 1937
05  圣路易斯与 Cori 门下 (1937–1942) — 华盛顿大学医学院、与 Carl Cori 的师承、
    肾上腺素/胰高血糖素与糖原分解；1942 MD
06  二战军医 (1942–1945) — 巴顿麾下营军医、德国战地医院
07  回到 Cori 实验室 (1945–1953) — 肝磷酸化酶（LP）为糖原分解限速酶、
    磷酸化/脱磷酸化开关、LP 激酶与磷酸酶；教职阶梯
08  Case Western 与 Rall (1953–1963) — 药理学教授兼系主任、与 Ted Rall 终身搭档、
    匀浆化实验的抉择（蔗糖之谜、完整细胞迷信、Berthet 的规范操作之争）
09  1956：热稳定因子（核心贡献页）— JBC 四部曲 "The Relationship of Epinephrine and
    Glucagon to Liver Phosphorylase"；颗粒组分+激素 → 未知热稳定因子 → 激活上清组分 LP
10  cAMP 与第二信使（核心贡献页）— 未知因子即环磷酸腺苷；激素作用于膜、
    cAMP 作为胞内第二信使——激素作用机制的统一图景
11  Vanderbilt 与迈阿密 (1963–1974) — 1963 解剖学教授、AHA 职业研究员 1967、
    1973 迈阿密杰出教授（AMP/GMP 新研究，1973 一年四篇）
12  荣誉与认可 — Banting 讲席 1952、Sollman 奖/Gairdner 1969、Lasker 1970、
    Dickson 1971、Nobel 1971、Golden Plate 1971、国家科学奖章 1973（尼克松颁发）、NAS 1973
13  英年早逝与纪念 — 1974-03-09 食管大出血术后内出血逝世（58 岁）；
    Sutherland 纪念讲座/范德堡 Sutherland 奖与讲席
14  遗产与结尾 — 第二信使学说开启的信号转导时代；学生 Murad 1998 再获诺奖的师门线
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 独得诺奖 | 1971 为**独得**（"for his discoveries"），无 co-honored——与 1969/1970 三人共享对照 |
| Cori 师承性质 | Sutherland 是 MD（1942），Cori 是其**研究导师**（mentorship 明载、实验室 1940–1953）——非正式 PhD 导师，边注记写"研究导师" |
| cAMP 发现年份 | 关键第四篇 JBC 论文 1956 年发表（匀浆化+热稳定因子）；"cAMP"命名与第二信使概念在其后确立——1956 论文/后续命名两层勿混 |
| 伙伴 Rall | Ted Rall 是"lifelong research partner"——cAMP 发现的核心搭档，colleague 边承载；Wosilait/Berthet 仅论文合作不入库 |
| 试错叙事 | 蔗糖匀浆的误信、完整细胞迷信被 Rall 说服打破、Berthet 要求规范倾析被拒——三条试错细节 page.md 明载，是科学过程教育的亮点，如实呈现 |
| 军旅 | 二战营军医（巴顿麾下、赴德至 1945）——经历叙述，勿写成科研中断的挫折叙事 |
| 学生 Murad | infobox 仅 Ferid Murad 一位博士生——1998 诺奖（NO 信号）可作师门线预告，细节由其本人篇展开 |
| 国籍 | citations json=United States，frontmatter 同——无冲突 |
| 卒因 | 1974-03-09 食管大出血术后内出血，享年 58——英年早逝，勿误写其他病因 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| cyclic AMP (cAMP) | 环磷酸腺苷 | 第二信使本体 |
| second messenger | 第二信使 | 激素胞内传令概念 |
| liver phosphorylase (LP) | 肝磷酸化酶 | 限速酶研究对象 |
| glycogenolysis | 糖原分解 | Cori 实验室框架 |
| phosphorylation / phosphatase | 磷酸化 / 磷酸酶 | LP 开关机制 |
| phosphorylase kinase | 磷酸化酶激酶 | LP 激活酶 |
| epinephrine / glucagon | 肾上腺素 / 胰高血糖素 | 触发激素 |
| homogenate | 匀浆 | 方法论突破点 |
| JBC four-part series | JBC 四部曲 | "Relationship of Epinephrine and Glucagon to Liver Phosphorylase" |
| Sutherland Prize / Chair | 萨瑟兰奖/讲席 | 范德堡纪念机制 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Awaken**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：激素在膜外敲门、cAMP 在胞内"唤醒"级联——"Awaken" 直译第二信使的传令意象，也呼应 Sutherland 把激素作用从黑箱带回分子光亮的觉醒式贡献。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Earl_Wilbur_Sutherland_Jr./Awaken.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
