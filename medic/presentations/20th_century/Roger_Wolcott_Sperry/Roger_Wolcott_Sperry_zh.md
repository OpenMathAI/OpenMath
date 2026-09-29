# 医学家立传提示词（Roger Wolcott Sperry）

> OpenMedic 项目、20 世纪诺贝尔生理学或医学奖 1981 年得主（罗杰·斯佩里，裂脑研究与大脑半球功能特化的开创者）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Roger Wolcott Sperry（1913-08-20 生于康涅狄格州哈特福德 ~ 1994-04-17 卒于加州帕萨迪纳，享年 80 岁）
- **气质关键词**：**裂脑研究的开创者、化学亲和假说的提出者、从英语专业转行神经科学的"左边画右手说"实验大师** —— 1981 获奖理由（独享一半；Hubel/Wiesel 共享另一半）：
  > "for his discoveries concerning the functional specialization of the cerebral hemispheres"（因发现大脑半球的功能特化）
- **设计母题**：**_split brain_的两个世界**。切断胼胝体后，左脑看不见右脑看见的东西——"左手解扣子右手扣回去"的病人观察是神经科学最诗意的实验。视觉隐喻：一条中缝把大脑分成两半，两侧各点亮一盏意识之灯。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Roger_Wolcott_Sperry/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/20th_century/Roger_Wolcott_Sperry/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准——生卒日 metadata 噪声裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/20th_century/Roger_Wolcott_Sperry/`（含 `images/`）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=Roger_Wolcott_Sperry_zh`、`VIDEO_NAME=Roger_Wolcott_Sperry_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/20th_century/Roger_Wolcott_Sperry/images.txt`；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/Roger_Wolcott_Sperry.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | neuropsychology | 神经心理学 | 裂脑研究，1981 诺奖核心 | 核心页 |
| 1 | neurobiology | 神经生物学 | 神经特异性与脑回路 | 核心页 |
| 2 | split-brain research | 裂脑研究 | 半球分离与功能特化 | 核心页 |
| 3 | chemoaffinity hypothesis | 化学亲和假说 | 神经接线化学标识（1951 提出、1963 发表） | 研究页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Paul A. Weiss | 导师 | 芝加哥大学动物学博士导师（1941，大鼠神经交叉与肌肉移位实验） |
| advisor-student | Karl Lashley | 导师 | 哈佛/Yerkes 灵长类中心博士后导师（蝾螈视神经旋转实验） |
| influence | R. H. Stetson | 无向 | Oberlin 心理学导论教师（曾师从 William James），引其转向心理学 |
| co-honored | David H. Hubel | 无向 | 1981 诺贝尔生理学或医学奖（Sperry 独得一半；Hubel/Wiesel 共享另一半——视觉系统信息处理） |
| co-honored | Torsten Wiesel | 无向 | 1981 诺贝尔生理学或医学奖（Sperry 独得一半；Hubel/Wiesel 共享另一半——视觉系统信息处理） |
| collaborator | Joseph Bogen | 无向 | MD，裂脑手术的临床合作者（裂脑病人研究的医学来源） |
| advisor-student | Michael Gazzaniga | 学生 | 博士生，裂脑病人语言/视觉/运动测试的共同设计者 |
| spouse | Norma Gay Deupree | 无向 | 1949 结婚，一子 Glenn Michael 一女 Janeth Hope |

> relations=8 为诚实值，Review 勿误判虚增。
> 不入库：R. H. Stetson 之外 Oberlin 咖啡馆同事；Victor Hepburn（邀其讲座的友人——间接引出 Caltech 教职，事件性）；William James（Stetson 的老师，思想谱系语境）；Epilepsy 病人们（研究合作对象未具名）。
> 库内当时无上述对手方记录，均由本 yaml 新建 stub；Hubel/Wiesel（1981 另一半得主）若由其他批次规范化将按名幂等回填。

## 五、配色方案 【人物专属】

- **气质**：裂脑中缝的对称美学 + Caltech 的实验冷调 + 意识之问的深蓝
- **主色**：意识深蓝 `#46647A`（两半球各一盏意识之灯的沉静底色）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` 裂脑研究 — 意识深蓝 `#46647A`
  - `badgeB` 化学亲和假说 — 深青 `#0E7C7B`
  - `badgeC` 神经交叉实验 — 暗红 `#8C2F1B`
  - `badgeD` 意识与心智哲学 — 琥珀 `#A0722D`
- **背景母题**：版面中央一条垂直中缝，两侧对称分布 badge 圆点（左/右半球的镜像构图）。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — 裂脑研究的开创者 / Roger Wolcott Sperry 1913–1994 + 四色 badge + 右上头像 + 国籍行 USA
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生 Hartford、教育 Oberlin BA 1935（英语）/
    MA 1937（心理学）/芝加哥 PhD 1941（Weiss 门下）、博后 Lashley、
    任职 Yerkes/芝加哥/NIH/Caltech（1954 Hixson 讲席）、荣誉 Nobel 1981/Wolf 1979/Lasker 1979、核心领域）
03  核心贡献概览 — 裂脑研究 / 化学亲和假说 / 神经交叉实验 / 意识的心智哲学
04  哈特福德的运动健将 (1913–1935) — 11 岁丧父（银行家）、母任中学助理校长、
    Hall High School 多项运动明星、Oberlin 奖学金、篮球队长兼棒球/橄榄球/田径、
    ★英语专业 1935 BA——Stetson 的心理学导论课改变人生（可写载送 Stetson 听学术闲谈的细节）
05  Oberlin 硕士与芝加哥博士 (1935–1941) — 心理学 MA 1937、
    芝加哥动物学 PhD 1941（Weiss 门下）、大鼠腿部运动神经交叉实验：
    左神经控右腿、电栅测试——大鼠永远学不会抬对侧腿→"神经系统的某些连接是硬连线的"
06  Lashley 门下与蝾螈实验 (1941–1946) — 哈佛/Yerkes（Orange Park, Florida）博后、
    蝶螈视神经切断+眼球旋转 180°——动物永远"看颠倒的世界"且训练无法纠正、
    "遗传控制的精细化学密码"引导神经生长→1951 化学亲和假说、1963 PNAS 发表
07  芝加哥、结核与 NIH (1946–1954) — 芝加哥助理/副教授、1949 胸片查见结核赴
    Saranac Lake 疗养（其间写作心智-脑概念，1952 发表于 American Scientist）、
    1952 NIH 神经疾病与失明组组长、芝加哥未获终身教职
08  1954：Caltech 的偶然 — 友人 Hepburn 邀其讲座、听众中的 Caltech 教授
    当场 offer Hixson 心理生物学讲席——最著名实验的起点
09  眼间传递与猫实验 — interocular transfer 问题："一只眼学会的为何另一只眼也会？"、
    切断猫视神经交叉+胼胝体→左右半球分别学习互不相通——半球独立功能的证据
10  裂脑病人与 Gazzaniga — Bogen 医生的裂脑手术（癫痫治疗：切断胼胝体阻止痫性放电扩散）、
    与博士生 Gazzaniga 设计语言/视觉/运动测试：右视野词→左脑能说、
    左视野词→右脑不能言说但左手能取物、双手"解扣-扣回"的日常观察
11  意识的双声道 — 1974 引语："每个半球都是一个有意识的系统……
    左右半球可以同时以不同甚至冲突的心理经验并行运作"（page.md 英文原文在，可引原文+译文）、
    2002 Review of General Psychology 20 世纪最常引用心理学家第 44 位
12  1981 诺贝尔奖 — Sperry 独得一半（his：大脑半球功能特化）、
    Hubel/Wiesel 共享另一半（their：视觉系统信息处理）——份额结构勿写错、
    1979 Wolf/Lasker 为前奏、1981 世界文化理事会创始成员
13  荣誉序列 — NAS 1960/ Warren Medal 1969/ Lashley Award 1976/ ForMemRS 1976、
    California Scientist of the Year 1972、National Medal of Science 1989、
    APA 终身成就奖 1993、Oberlin Sperry 神经科学楼 1990
14  遗产与身后 — 大脑功能偏侧化研究的奠基、化学亲和假说被轴突导向分子实验证实
    （Science 2009 综述口径；Nirenberg 1970s 鸡视网膜/果蝇验证）、
    业余古生物学家/雕塑家/陶艺家、1994-04-17 卒于 ALS（肌萎缩侧索硬化）、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由与份额 ★ | 官方逐字 "for his discoveries concerning the functional specialization of the cerebral hemispheres"（**Sperry 独得一半，his**）；Hubel/Wiesel 共享另一半 "for their discoveries concerning information processing in the visual system"（their）——1/2+1/4+1/4 结构勿写成"三人平分" |
| 生日/卒日噪声 ★ | metadata birth 含 "(2018-08-21)" 显然为 infobox 解析错误（正文 August 20, 1913）；death 双值 04-17/04-18——取 **1913-08-20 / 1994-04-17**（infobox/正文口径） |
| 英语专业 ★ | Oberlin 本科是**英语专业**（1935），心理学是硕士（1937）——Stetson 的导论课+开车接送听学术闲谈是转轨契机（page.md 明载细节可叙事） |
| 大鼠实验结论 | 交叉神经大鼠"永远学不会抬对侧腿"→"no adaptive functioning of the nervous system took place"（Sperry 引语，page.md 英文原文在）——硬连线结论 |
| 蝾螈实验 | 视神经切断+眼球旋转 180°→世界永远颠倒且训练无效→化学密码引导神经→化学亲和假说（1951 提出/1963 PNAS） |
| Lashley 双重身份 | 博后导师 + 胼胝体功能的玩笑（"只是防止两半球塌在一起？"）——Lashley Award 以 Lashley 命名，双重联系 |
| Caltech 的偶然 | 未获芝加哥终身教职→Bethesda 建设延期→Hepburn 讲座→Caltech 当场邀聘——偶然性叙事照 page.md |
| 1974 引语 | "each hemisphere is indeed a conscious system..."（page.md 英文原文在，可引原文+译文）——意识双声道核心引语 |
| Nirenberg 呼应 | 化学亲和假说 1970s 被 Nirenberg（1968 诺奖得主）鸡视网膜/果蝇工作证实——跨批次人物呼应（Science 2009 综述口径），仅叙事不入库 |
| 死因 | ALS（肌萎缩侧索硬化）——1994-04-17 帕萨迪纳 |
| 页面噪声 | page.md 开头有大型神经心理学 sidebar 表格——事实提取时跳过；infobox 出生行 "(2018-08-21)" 为明显解析错误 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| split-brain | 裂脑 | 胼胝体切断后的状态 |
| corpus callosum | 胼胝体 | 两半球间的连接结构 |
| chemoaffinity hypothesis | 化学亲和假说 | 1951 提出/1963 发表 |
| lateralization | 功能偏侧化 | 获奖理由核心概念 |
| interocular transfer | 眼间传递 | 猫实验的起点问题 |
| neuronal specificity | 神经特异性 | 博士阶段兴趣 |
| Hixson Professor | Hixson 讲席教授 | Caltech 心理生物学讲席 |
| epilepsy | 癫痫 | 裂脑手术的医学适应症 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Awaken**（manifest 预分配）
- **风格**：觉醒 / 上扬 / 黎明感
- **匹配理由**：裂脑病人让"两个意识"在实验中同时觉醒——Awaken 的觉醒感匹配"每个半球都是独立的意识系统"的革命性发现；也呼应其从英语课堂到神经科学圣殿的智识觉醒。
- **本地路径**：`music_audio/alex-productions/36-aqLUvpAdLNQ-Awaken.wav` → 复制为 `presentations/20th_century/Roger_Wolcott_Sperry/Awaken.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；份额结构与引语务必忠实 page.md。**
