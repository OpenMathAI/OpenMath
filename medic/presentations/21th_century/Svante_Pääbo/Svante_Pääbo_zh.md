# 医学家立传提示词（Svante Pääbo）

> OpenMedic 项目、21 世纪诺贝尔生理学或医学奖 2022 年得主（斯万特·帕博，古基因组学奠基人、尼安德特基因组测序者）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Svante Pääbo（1955-04-20 生于斯德哥尔摩，在世）
- **气质关键词**：**古基因组学的奠基人、尼安德特基因组的测序者、丹尼索瓦人的命名者、从木乃伊到人类自我认知的摆渡人** —— 2022 获奖理由（独享）：
  > "for his discoveries concerning the genomes of extinct hominins and human evolution"（因发现已灭绝古人类的基因组与人类演化）
- **设计母题**：**从骨头里读出 LETTER**。万年骨粉中的碎片化 DNA 被拼回基因组——" extinct hominins 借他的测序仪重新开口"。视觉隐喻：一根股骨在扫描线中渐次显影为双螺旋。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Svante_Pääbo/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/21th_century/Svante_Pääbo/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准——生日双值裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/21th_century/Svante_Pääbo/`（含 `images/`；目录名含 ä，Makefile 变量照抄，注意 shell 引用）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=Svante_Pääbo_zh`、`VIDEO_NAME=Svante_Pääbo_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/21th_century/Svante_Pääbo/images.txt`（2016 照）；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/Svante_Pääbo.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | paleogenetics | 古基因组学 | 奠基人之一，2022 诺奖核心 | 核心页 |
| 1 | evolutionary genetics | 进化遗传学 | 尼安德特与现代人基因流 | 核心页 |
| 2 | evolutionary anthropology | 进化人类学 | 马普进化人类学研究所遗传系创始所长 | 身份页 |
| 3 | ancient DNA | 古 DNA | 自 1984 年 2400 年木乃伊起步 | 研究页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Allan Wilson | 导师 | Berkeley 博士后（EMBO Fellow），灭绝哺乳动物基因组研究 |
| parent-child | Sune Bergström | 父 | 生父，1982 诺贝尔生理学或医学奖得主（前列腺素研究），非婚生 |
| spouse | Linda Vigilant | 无向 | 灵长类学家兼遗传学家，2008 结婚，莱比锡育一子一女，多篇合著 |
| colleague | Hugo Zeberg | 无向 | 合作者（Karolinska），2020 新冠重症风险与尼安德特遗传关联研究 |

> 在世者，relations=4 为诚实值，Review 勿误判缺漏。
> 不入库：母亲 Karin Pääbo（爱沙尼亚难民化学家，page.md 明载但以其为背景叙事、非学界关系网络；如 Review 追问可议，本批保守不入库）；异母弟 Rurik Reenstierna（2004 才知情的手足，非学界）；福米 Kishida（合影政治人物）。
> 库内当时无 Allan Wilson（生物学家）/ Sune Bergström / Linda Vigilant / Hugo Zeberg 记录，均由本 yaml 新建 stub。**注意**：Allan Wilson 系已故群体遗传学家（Berkeley），与物理学家 Kenneth G. Wilson、数学家 Wilson 等无关，note 已注明领域防混淆。

## 五、配色方案 【人物专属】

- **气质**：冻土的青灰 + 骨骼的米白 + 测序仪扫描线的冷光
- **主色**：冻土青灰 `#4A6670`（尼安德特谷的石灰岩与万年沉积）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` 尼安德特基因组 — 冻土青灰 `#4A6670`
  - `badgeB` 丹尼索瓦人 — 深紫 `#52307C`
  - `badgeC` 古 DNA 方法学 — 琥珀 `#A0722D`
  - `badgeD` 基因流与今日医学 — 暗红 `#8C2F1B`
- **背景母题**：由碎片方块渐次拼合的双螺旋（古 DNA 拼装），四色碎片错落。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — 古基因组学的摆渡人 / Svante Pääbo 1955– + 四色 badge + 右上头像 + 国籍行 Sweden
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生斯德哥尔摩、教育 Uppsala PhD 1986、
    博后 Zurich/Berkeley（Allan Wilson 实验室）、任职 LMU/马普进化人类学研究所/冲绳科大、
    荣誉 Nobel 2022/Breakthrough 2016/Leibniz 1992、核心领域）
03  核心贡献概览 — 尼安德特基因组 / 丹尼索瓦人 / 基因流与今日人类 / 古 DNA 方法学
04  斯德哥尔摩的单亲童年 (1955–1975) — 母 Karin Pääbo 为爱沙尼亚难民化学家（1944 逃离苏联入侵）、
    生父 Sune Bergström 系非婚生关系、父亲仅在周六探访数小时、
    童年引语：卢恩石刻的周末巡游（page.md 英文原文可引）
05  家庭的诺奖回声 — 生父 Sune Bergström 1982 获同一奖项（前列腺素研究）、
    异母弟 Rurik Reenstierna 同年生、2004 年才知晓兄弟关系——家庭线克制呈现
06  Uppsala 与军旅 (1975–1986) — 乌普萨拉求学、瑞典国防军翻译学校服役一年、
    1986 PhD：腺病毒 E19 蛋白如何调节免疫系统
07  博后岁月：苏黎世与伯克利 (1986–1990) — 苏黎世分子生物学研究所 II、
    EMBO Fellow 赴 Berkeley 加入 Allan Wilson 实验室、灭绝哺乳动物基因组——古 DNA 转向
08  木乃伊起步与莱比锡建所 — 1984 年 2400 年木乃伊 DNA 起步（Kistler Prize 授奖口径）、
    1990 LMU Munich 普通生物学教授、1997 马普进化人类学研究所遗传系创始所长
09  1997：尼安德特线粒体 DNA — Feldhofer 洞穴标本 mtDNA 测序成功、
    2002-08 FOXP2"语言基因"发现公布
10  2009-2010：基因组草图与基因流 — 2009-02 AAAS 年会宣布尼安德特基因组草图
    （逾 30 亿碱基对，与 454 Life Sciences 合作）、2010-05 Science 草图发表、
    尼安德特与欧亚（非撒哈拉以南）现代人杂交、5-6 万年前中东基因混合
11  2010：丹尼索瓦人 — 丹尼索瓦洞穴指骨 DNA 分析、未被认知的 Homo 属灭绝成员、
    曾拟独立成种经同行评议后改判；TKTL1 单氨基酸替换与脑发育差异
12  2020：古基因组的当代回响 — 与 Zeberg（Karolinska）确定 3 号染色体区域遗传变异
    （欧洲尼安德特遗产相关）与新冠重症风险关联——Nature 论文
13  2022 诺贝尔奖 — 独享 "for his discoveries concerning the genomes of extinct hominins
    and human evolution"、诺奖授奖口径 "sequencing the first Neanderthal genome"
14  遗产与个人 — 自传《Neanderthal Man》（2014，回忆录+科普混体）、
    自述双性恋（其自传内容，客观一句）、妻 Linda Vigilant（灵长类学家，合著者）、
    h-index 167、皇家极星勋章一等司令（2024）、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方逐字 "for his discoveries concerning the genomes of extinct hominins and human evolution"（**独享**，his）；page.md 另有授奖口径 "for sequencing the first Neanderthal genome"——两者分开使用勿混 |
| 生日双值 ★ | metadata 双值 1955-04-20 / 1955-01-01；infobox 与正文均 **20 April 1955**——取 04-20 |
| 家庭结构呈现 | 非婚生、生父 Sune Bergström（1982 诺奖得主）、母为爱沙尼亚难民、异母弟 2004 年才相认——page.md 明载，**克制、客观呈现**，不猎奇不渲染；引语（童年卢恩石刻）有英文原文可引 |
| Bergström 入库 | 生父系诺奖级生物化学家——parent-child（direction: parent）入库，note 注明"非婚生" |
| Allan Wilson 防混淆 | 博后导师 Allan Wilson 为 Berkeley 群体遗传学家（1991 逝世），与 Kenneth G. Wilson 等无关——stub note 注明领域 |
| Denisova 分类 | Pääbo 曾拟将丹尼索瓦人独立成种、经同行评议后改变主意——细节可写；TKTL1 的单氨基酸替换系 Johannes F. Coy 发现的基因——归属勿错 |
| 基因流表述 | 杂交对象为**欧亚（非撒哈拉以南非洲）**现代人；估计发生在约 5-6 万年前中东——限定词勿省 |
| COVID 关联 | 2020 Zeberg-Pääbo：3 号染色体区域变异（欧洲尼安德特遗产相关）与重症风险——"associated"口径，勿写成决定论 |
| 性倾向自述 | 其 2014 自传自述双性恋——page.md 明载，客观一句带过（自传出处），不展开；妻 Linda Vigilant 引语 "boyish charms" 若引用需克制 |
| 目录名含 ä | {Dir}=Svante_Pääbo——Makefile/shell 引用注意 UTF-8 引号；tex 内 Pääbo 用 ä 字符（XeLaTeX 原生支持） |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| paleogenetics | 古基因组学 | 其奠基领域 |
| Neanderthal genome | 尼安德特基因组 | 2009 草图/2010 Science 发表 |
| Denisova hominin | 丹尼索瓦人 | 2010 指骨 DNA |
| mtDNA | 线粒体 DNA | 1997 起点序列 |
| FOXP2 | FOXP2 基因 | "语言基因"（带引号使用） |
| gene flow / admixture | 基因流/基因混合 | 5-6 万年前中东 |
| TKTL1 | TKTL1 基因 | 单氨基酸替换（Coy 发现） |
| ancient DNA (aDNA) | 古 DNA | 片段化、污染防控是方法学核心 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**New Lands**（manifest 预分配）
- **风格**：史诗 / 开阔 / 新大陆
- **匹配理由**：他在基因组学中开辟了一块"新大陆"——灭绝人类的基因组成为可读之书；New Lands 的开阔史诗感匹配"从尼安德特谷到丹尼索瓦洞，为人类自我认知绘制新地图"的叙事。
- **本地路径**：`music_audio/alex-productions/74-oK8HN0FsZmc-New-Lands.wav` → 复制为 `presentations/21th_century/Svante_Pääbo/New-Lands.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；家庭线克制呈现，时间线数字务必精确。**
