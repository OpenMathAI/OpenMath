# 医学家立传提示词（Albrecht Kossel）

> 本文件是 OpenMedic 项目「20 世纪诺贝尔生理学或医学奖得主人物专属立传提示词」。
> 目标人物：Albrecht Kossel（1910 年诺贝尔生理学或医学奖得主，德国）。
> 用途：指导后续 Beamer 立传（15 页）与配套视频制作；事实基准为本地 Wikipedia 页面
> `medic/presentations/pages/20th_century/Albrecht_Kossel/page.md`（下称 page.md）。
> 社会关系与研究领域已按本文件第三、四节入库 greatminds 库（yaml 与本文件完全一致）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Albrecht Kossel（阿尔布雷希特·科塞尔，全名 Ludwig Karl Martin Leonhard Albrecht Kossel，1853-09-16 罗斯托克 ~ 1927-07-05 海德堡，享年 73 岁）
- **气质关键词**：**细胞化学的奠基人、核酸五碱基的发现者、遗传物质化学的先驱** —— 1910 年诺贝尔生理学或医学奖获奖理由（逐字引自 medic/nobel_medicine_citations.json）：
  > "in recognition of the contributions to our knowledge of cell chemistry made through his work on proteins , including the nucleic substances"
  > （以表彰其对细胞化学知识的贡献，包括通过对蛋白质及含核物质的研究所做的工作）
- **设计母题**：**「生命的演员表」**。Kossel 名言把生命过程比作戏剧、自己研究「演员而非剧情」——腺嘌呤、胞嘧啶、鸟嘌呤、胸腺嘧啶、尿嘧啶五种碱基正是他点名的五位演员。视觉隐喻：五枚分子「角色牌」排成一行，指向 43 年后的双螺旋。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Albrecht_Kossel/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 **medic 路径**执行：页面用 `medic/presentations/pages/20th_century/Albrecht_Kossel/`，成目录 `medic/presentations/20th_century/Albrecht_Kossel/`，Makefile 复制后设 `MAIN=Albrecht_Kossel_zh`、`VIDEO_NAME=Albrecht_Kossel_zh`，BGM 见第九节。
> 第 4 步（研究领域）与第 4.5 步（社会关系）**已完成入库**，见第三、四节。
> 数据库已置 `has_social_data=1`；`has_biography` 待 Beamer 立传完成后置 1。

## 三、研究领域梳理 + 入库（已完成）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biochemistry | 生物化学 | 细胞化学奠基人，1910 诺奖核心 | 总览/核心页 |
| 1 | nucleic acids | 核酸化学 | 分离命名五种核碱基（1885–1901），DNA/RNA 的前奏 | 核酸页 |
| 2 | protein chemistry | 蛋白质化学 | 组蛋白/精蛋白、六碱基定量分离、预示多肽本质 | 蛋白质页 |
| 3 | physiological chemistry | 生理化学 | 执编 Zeitschrift für Physiologische Chemie 三十余年 | 期刊页 |

## 四、社会关系梳理 + 入库（已完成，与 MySQL/data/Albrecht_Kossel.yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Felix Hoppe-Seyler | 师 | 斯特拉斯堡导师，1877 年起任其研究助手 |
| advisor-student | Emil du Bois-Reymond | 师 | 1883 年柏林生理学研究所任职期间受其督导 |
| colleague | Friedrich Miescher | — | 承接并推进米歇尔 1869 年发现的核素研究 |
| advisor-student | Henry Drysdale Dakin | 生 | 英国门生，合作研究精氨酸酶 |
| advisor-student | Edwin B. Hart | 生 | 美国门生，后主持单粒实验 |
| advisor-student | Otto Folin | 生 | 美国门生，后发现磷酸肌酸 |
| spouse | Luise Holtzman | — | 1886 年成婚，1913 年病逝于急性胰腺炎 |
| parent-child | Albrecht Karl Ludwig Enoch Kossel | 父 | 商人兼普鲁士领事 |
| parent-child | Clara Jeppe Kossel | 母 | — |
| parent-child | Walther Kossel | 子 | 理论物理学家，化学键理论与位移律（库内既有记录） |
| parent-child | Gertrude Kossel | 女 | 1889 年生 |

> 说明：与 Dakin 的合作（arginase）并入师生边 note，不另建 collaborator 边；1911 年访美同行的妻子与女儿不入关系表；妻子亲戚 Hilgard/Villard/Garrison 仅姻亲提及，不入库。

## 五、配色方案 【人物专属】

- **气质**：严谨、化学家的冷静与德意志学统的厚重
- **主色**：细胞核深蓝 `#16324F`（显微镜下的核质与 Baltic 学统）
- **诺奖色**：香槟金（奖章/年份徽章专用）
- **四分类色（badgeA-D）**：
  - `badgeA` 生物化学 — 分子青 `#1F7A6D`
  - `badgeB` 核酸化学 — 碱基紫 `#5B3E8E`
  - `badgeC` 蛋白质化学 — 肽键橙 `#C26A2E`
  - `badgeD` 生理化学 — 期刊灰蓝 `#41607E`
- **背景母题**：五枚五边形/六边形碱基分子徽记错落排布，低透明度铺底，呼应「五位演员」母题

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input medic/presentations/cover/）
01  封面 — 细胞化学奠基人 / Albrecht Kossel 1853–1927 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、全名、教育、任职、家庭、荣誉、核心领域）
03  核心贡献概览 — 核酸五碱基 / 蛋白质化学 / 核素研究 / 期刊编辑
04  早年：罗斯托克 (1853–1872) — 商人之子、Gymnasium 时代对化学与植物学的兴趣
05  斯特拉斯堡：Hoppe-Seyler 门下 (1872–1883) — 医学训练、1877 助手、核素拆分
06  五种核碱基的分离 (1885–1901) — adenine/cytosine/guanine/thymine/uracil 逐一登场
07  柏林与马尔堡 (1883–1901) — 化学室主任、1895 Marburg 教授、1896 发现组氨酸
08  海德堡岁月 (1901–1924) — 蛋白质研究所、多肽本质的预示
09  1910 诺贝尔奖（核心页）— citation 原文、1910-12-10 授奖、引言演讲摘录
10  「演员而非剧情」— 1910 NYT 访谈引语页（英文原文+译文）
11  期刊与学统 — Zeitschrift für Physiologische Chemie 1895–1927、Hoppe-Seyler 创刊
12  门生与传承 — Dakin/Hart/Folin；1911 Herter 讲座唯一美国行
13  荣誉与认可 — Nobel 1910 · 1923 爱丁堡荣誉学位 · 罗斯托克 Kossel 研究所
14  遗产：从五碱基到双螺旋 — Franklin Photo 51、Watson & Crick 1953 的前置基石
15  结尾
```

## 七、特殊陷阱表（★ 执行 Beamer 前必读）

| # | 陷阱 | 裁定 |
|---|------|------|
| 1 | 获奖理由表述 | 逐字用 citation 原文（含 "cell chemistry / proteins / nucleic substances" 三要素）；勿简写为「因发现核酸而获奖」 |
| 2 | 「发现核酸」的表述 | Kossel 是分离并描述核酸的非蛋白组分与五种碱基；核酸本身 1869 年由 Miescher 首先分离——行文须区分，勿把「发现核酸」整个归给 Kossel |
| 3 | 生卒日期 | 1853-09-16 / 1927-07-05，page.md 正文与 infobox 一致；死因复发性心绞痛 |
| 4 | 全名 | 全名 Ludwig Karl Martin Leonhard Albrecht Kossel 仅身份页使用，通篇以 Albrecht Kossel 行文 |
| 5 | NYT 引语 | "The processes of life are like a drama..." page.md 有英文原文（The New York Times 访谈），可引原文+译文；其余无直接引语 |
| 6 | 诺奖引言演讲 | Nobel introduction speech 大段引文 page.md 有英文原文（1910-12-10），如用需整段忠实翻译 |
| 7 | 子承父名陷阱 | 儿子 Walther Kossel 是理论物理学家（八隅律/位移律），勿与其混淆；父亲 Albrecht Karl Ludwig Enoch Kossel 与本人同首名，行文用全名区分 |
| 8 | 政治细节 | 1914 拒签德国教授宣言、1917 拒绝政府关于配给充足的单方面声明——page.md 明载可写，一句带过，不展开一战政治 |
| 9 | Watson/Crick/Franklin | 只在「遗产」页作下游影响提及（page.md Legacy 节明载），不建任何人物关系 |
| 10 | metadata 冲突 | metadata.json 与 page.md 无实质冲突；doctoral_advisor=Hoppe-Seyler 两处一致 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| nuclein | 核素 | Miescher 1869 年命名，Kossel 拆分出核酸 |
| nucleic acid | 核酸 | 勿与「核蛋白」混淆 |
| nucleobases | 核碱基 | 五种：A/C/G/T/U |
| adenine / cytosine / guanine / thymine / uracil | 腺嘌呤/胞嘧啶/鸟嘌呤/胸腺嘧啶/尿嘧啶 | T 在 DNA、U 在 RNA |
| histidine | 组氨酸 | 1896 年发现 |
| histones / protamines | 组蛋白/精蛋白 | 晚年研究重点 |
| hexone bases | 六碱基类 | 精氨酸/组氨酸/赖氨酸定量分离口径 |
| agmatine | 鲱精胺 | 鲱鱼卵中发现 |
| theophylline | 茶碱 | 首次分离者 |
| polypeptide | 多肽 | 其研究「预示」了蛋白质的多肽本质 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**With Me** — Alex-Productions（manifest 预分配）
- **匹配理由**：
  - 「同行/陪伴」气质匹配 Kossel 的学术人生底色——师承 Hoppe-Seyler、执编其创刊期刊直至去世，是「与师同行一生」的写照
  - 温和而持续的节奏契合「为双螺旋铺路」的长期主义者形象：不喧哗，却奠基
- **备选**（未采用）：The Flow of Time（时间感合适但已高频占用）、Eternals（更宏大，留给有争议/跨域人物更佳）
- **本地路径**：按 music_audio/ 内 Alex-Productions With Me 曲目复制至 `medic/presentations/20th_century/Albrecht_Kossel/With_Me.wav`，ffmpeg `-shortest` 对齐
