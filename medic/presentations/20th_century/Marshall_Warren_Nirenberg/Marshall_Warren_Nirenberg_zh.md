# 医学家立传提示词（Marshall Warren Nirenberg）

> OpenMedic 项目、20 世纪诺贝尔生理学或医学奖 1968 年得主（马歇尔·尼伦伯格，破译遗传密码第一人）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Marshall Warren Nirenberg（1927-04-10 生于纽约市 ~ 2010-01-15 卒于纽约市，享年 82 岁）
- **气质关键词**：**破译遗传密码第一人、UUU=苯丙氨酸的揭示者、NIH 的"最辉煌时刻"主角、从蜉蝣分类学到密码表的转轨者** —— 1968 获奖理由（与 Har Gobind Khorana、Robert W. Holley 三人共享）：
  > "for their interpretation of the genetic code and its function in protein synthesis"（因解析遗传密码及其在蛋白质合成中的功能）
- **设计母题**：**一串 U 的独白**。多聚尿嘧啶 RNA 在无细胞提取物中只造出苯丙氨酸——生命密码的第一个词被读出。视觉隐喻：一串重复的 U 字母点亮密码表的第一格。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Marshall_Warren_Nirenberg/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/20th_century/Marshall_Warren_Nirenberg/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准，裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/20th_century/Marshall_Warren_Nirenberg/`（含 `images/`）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=Marshall_Warren_Nirenberg_zh`、`VIDEO_NAME=Marshall_Warren_Nirenberg_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/20th_century/Marshall_Warren_Nirenberg/images.txt`（2002 照 / 1961 与 Matthaei 合影）；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/Marshall_Warren_Nirenberg.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biochemistry | 生物化学 | poly-U 实验，1968 诺奖核心 | 核心页 |
| 1 | genetic code | 遗传密码 | 解码竞赛与密码子指认 | 核心页 |
| 2 | genetics | 遗传学 | NIH 生化遗传组主任（1962 起） | 身份页 |
| 3 | neuroscience | 神经科学 | 晚年转向神经发育与同源框基因 | 研究页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | James F. Hogg | 导师 | 密歇根大学博士导师（1957，肿瘤细胞己糖摄取） |
| collaborator | Heinrich Matthaei | 无向 | 1961 poly-U 无细胞提取物实验共同完成（UUU=苯丙氨酸） |
| advisor-student | Philip Leder | 学生 | 博后，Nirenberg-Leder 实验法大幅加速密码子指认 |
| colleague | Severo Ochoa | 无向 | 1961-62 编码竞赛对手（NYU 实验室，大规模团队） |
| co-honored | Har Gobind Khorana | 无向 | 1968 诺贝尔生理学或医学奖三人共享（遗传密码的解析及其在蛋白质合成中的功能） |
| co-honored | Robert W. Holley | 无向 | 1968 诺贝尔生理学或医学奖三人共享（遗传密码的解析及其在蛋白质合成中的功能） |
| spouse | Perola Zaltzman-Nirenberg | 无向 | 巴西里约化学家，1961 结婚，同在 NIH 工作，2001 年去世 |
| spouse | Myrna M. Weissman | 无向 | 哥大流行病学与精神病学教授，2005 结婚 |

> relations=8 为诚实值，Review 勿误判虚增。
> 不入库：父母（父为衬衫裁缝，背景叙事）；四名继子女（Weissman 前婚，仅具名罗列）；实验室同事 Freese/Gajdusek（同楼实验室主任，无直接合作记载）；政治人物 Dole/Biden（致谢信事件）；Meselson/Crick（莫斯科会议轶事——Crick 邀其重讲为叙事亮点但不入库）；Moscow 会议听众。
> 库内既有 Severo Ochoa（#4291, Q233957，1959 诺奖医学）规范记录直接引用；其余对手方新建 stub（Khorana/Holley 由本批各自 yaml 幂等覆盖）。

## 五、配色方案 【人物专属】

- **气质**：纽约的率直 + NIH 实验室的安静 + 密码表被逐格点亮的秩序感
- **主色**：密码蓝 `#20558A`（解码竞赛的理性与 NIH 的克制）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` poly-U 实验 — 密码蓝 `#20558A`
  - `badgeB` 解码竞赛 — 暗红 `#8C2F1B`
  - `badgeC` NIH 集体协作 — 深青 `#0E7C7B`
  - `badgeD` 神经科学转向 — 琥珀 `#A0722D`
- **背景母题**：密码表网格（4×4 方格），U 字格逐格点亮，badge 圆点嵌于格线。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — 破译遗传密码第一人 / Marshall Warren Nirenberg 1927–2010 + 四色 badge + 右上头像 + 国籍行 USA
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生纽约、教育 Florida BS 1948/MS 1952/
    Michigan PhD 1957、导师 Hogg、任职 NIH 1957 起（生化遗传组主任 1962）、
    荣誉 Nobel 1968/NAS 分子生物学奖 1962/National Medal of Science 1964、核心领域）
03  核心贡献概览 — poly-U 实验 / 解码竞赛 / Nirenberg-Leder 方法 / 晚年神经科学
04  纽约到奥兰多 (1927–1948) — 犹太家庭、父为衬衫裁缝、少年风湿热全家迁奥兰多、
    早期生物学兴趣、Florida 动物学 MS 1952——硕士论文是蜉蝣（毛翅目）的生态与分类研究
05  密歇根与 NIH (1952–1959) — PhD 1957（Hogg 门下，肿瘤细胞己糖摄取）、
    1957 美国癌症学会资助入 NIH、1959 任研究生物化学家、
    开始研究 DNA-RNA-蛋白质的关联步骤
06  1958 年的知识地基 — Avery-MacLeod-McCarty、Hershey-Chase、Watson-Crick、
    Meselson-Stahl 已证 DNA 是遗传信息分子——但 DNA 如何指挥蛋白质表达、
    RNA 扮演什么角色仍未知
07  1961：poly-U 实验 — 与 Matthaei 合成多聚尿嘧啶 RNA、加入大肠杆菌无细胞提取物、
    加 DNase 防止本底表达、20 种氨基酸逐一放射性标记——
    只有标记苯丙氨酸的样品产出放射性蛋白→UUU 编码苯丙氨酸、
    亦是对信使 RNA 的首次证明
08  莫斯科的聚光灯 — 1961-08 国际生物化学大会：先在小场报告、
    Meselson 听后拥抱并告知 Crick、Crick 邀其次日向千余人大场重讲——一举震动学界
09  解码竞赛 (1961–1962) — 与诺奖得主 Ochoa 的 NYU 实验室竞速、
    NIH 同仁放下自己的工作支援 Nirenberg、Stetten 称之为 "NIH's finest hour"
10  AAA 与 CCC——Leder 方法 — 腺苷重复→赖氨酸、胞嘧啶重复→脯氨酸、
    博后 Philip Leder 发明 tRNA 片段密码子指认法、50 个密码子由此确定、
    Khorana 实验证实并完成密码表
11  1968 诺贝尔奖 — 三人共享官方理由逐字引用、同年 Horwitz Prize（与 Khorana）、
    1962 NAS 分子生物学奖/1964 国家科学勋章/1967 Gairdner 为前奏
12  晚年转向 — 神经科学、神经发育与同源框（homeobox）基因、
    NIH 实验室主任至逝世、美国哲学会 2001、1981 世界文化理事会创始成员
13  个人生活 — 妻 Perola Zaltzman（巴西化学家，1961 结婚、2001 逝）、
    二婚 Myrna M. Weissman（哥大教授，2005 结婚）、四继子女
14  遗产 — "被遗忘的破译者"（Sci Am 2007 文题口径：为何人们以为是 Crick 破译了密码）、
    密码表与 NAS/NIH 的机构记忆、2010-01-15 卒于癌症、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方逐字 "for their interpretation of the genetic code and its function in protein synthesis"（三人共享、their）；page.md 转述 "breaking the genetic code"——引用以 citation json 为准 |
| poly-U 实验细节 | 多聚尿嘧啶 RNA + 大肠杆菌无细胞提取物 + **DNase 防本底** + 20 氨基酸逐一标记（1 标记 19 不标记）——方法学四步完整，勿简化 |
| 双重第一 | 既是密码子解码第一步、**也是信使 RNA 的首次证明**（page.md 明载）——两层都要说 |
| 莫斯科轶事 | Meselson 拥抱+告知 Crick→Crick 邀其次日千人大场重讲——叙事亮点，人物不入库 |
| 编码竞赛定性 | 与 Ochoa 的竞争是实验室间竞速（Ochoa 团队庞大）——"race"口径客观呈现，Ochoa 以 colleague 入库、note 用"竞赛对手"，勿写成个人恩怨 |
| "NIH's finest hour" | Stetten 语录（page.md 英文原文在，可引）——集体协作叙事的题眼 |
| Leder 方法 | tRNA 片段法确定 50 个密码子；Khorana 实验证实并补完——分工勿混 |
| 两任妻子 | Perola Zaltzman-Nirenberg（巴西化学家、同在 NIH、2001 逝）+ Myrna M. Weissman（哥大教授、2005 结婚）——两行 spouse 区分 |
| 学位口径 | Florida BS 1948/MS 1952（动物学，蜉蝣分类）+ Michigan PhD 1957（生物化学）——从分类学到生化的大转轨 |
| 遗产口径 | Sci Am 2007 "The Forgotten Code Cracker"——"为何人们以为是 Crick 破译了密码"可作遗产页引子，注明杂志口径 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| poly-U (polyuracil) | 多聚尿嘧啶 RNA | 首个被破译的密码子载体 |
| cell-free extract | 无细胞提取物 | 大肠杆菌体系 |
| phenylalanine | 苯丙氨酸 | UUU 对应氨基酸 |
| codon | 密码子 | 三碱基密码单元 |
| messenger RNA (mRNA) | 信使 RNA | 首次证明（page.md 口径） |
| Nirenberg and Leder experiment | Nirenberg-Leder 实验 | tRNA 片段密码子指认法 |
| homeobox | 同源框基因 | 晚年研究对象 |
| coding race | 解码竞赛 | 1961-62 与 Ochoa 实验室竞速 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Falling Apart**（manifest 预分配）
- **风格**：律动 / 解构 / 电子氛围
- **匹配理由**：破译密码=把生命的"密文"拆解到单字——Falling Apart 的解构律动匹配 poly-U 实验把语言还原为重复单元的方法论美学；密码表被一格格点亮的过程也是乐曲层层推进的过程。
- **本地路径**：`music_audio/inspiring-electronic/03-qtNSLNUd1VE-Michael FK & Andy Leech - Falling Apart.wav` → 复制为 `presentations/20th_century/Marshall_Warren_Nirenberg/Falling_Apart.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；poly-U 四步方法学与竞赛定性务必精确。**
