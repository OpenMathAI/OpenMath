# 医学家立传提示词（Baruj Benacerraf）

> OpenMedic 项目、20 世纪诺贝尔生理学或医学奖 1980 年得主（巴鲁赫·贝纳塞拉夫，免疫应答基因 Ir 的发现者之一）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Baruj Benacerraf Lasry（1920-10-29 生于委内瑞拉加拉加斯 ~ 2011-08-02 卒于马萨诸塞州牙买加平原，享年 90 岁）
- **气质关键词**：**免疫应答基因 Ir 的发现者、MHC 与自身免疫之门的开启者、因犹太身份被医学院拒之门外的坚韧者** —— 1980 获奖理由（与 Jean Dausset、George Davis Snell 三人共享）：
  > "for their discoveries concerning genetically determined structures on the cell surface that regulate immunological reactions"（因发现细胞表面调控免疫反应的遗传决定结构）
- **设计母题**：**细胞表面的门牌**。MHC 基因编码的细胞表面分子，是免疫系统的"自我/非我"识别牌。视觉隐喻：细胞膜上一排发光的门牌号， responder 与 non-responder 两组小鼠的对照。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Baruj_Benacerraf/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/20th_century/Baruj_Benacerraf/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准，裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/20th_century/Baruj_Benacerraf/`（含 `images/`）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=Baruj_Benacerraf_zh`、`VIDEO_NAME=Baruj_Benacerraf_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/20th_century/Baruj_Benacerraf/images.txt`（1969 照）；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/Baruj_Benacerraf.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | immunology | 免疫学 | Ir 基因发现，1980 诺奖核心 | 核心页 |
| 1 | major histocompatibility complex | 主要组织相容性复合体 | 30+ 基因的 MHC 基因群 | 核心页 |
| 2 | immunogenetics | 免疫遗传学 | 显性常染色体免疫应答基因 | 核心页 |
| 3 | pathology | 比较病理学 | 哈佛 Fabyan 讲席（1970-91） | 身份页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Jean Dausset | 无向 | 1980 诺贝尔生理学或医学奖三人共享（细胞表面遗传决定结构调控免疫反应的发现） |
| co-honored | George D. Snell | 无向 | 1980 诺贝尔生理学或医学奖三人共享（细胞表面遗传决定结构调控免疫反应的发现） |
| advisor-student | Elvin A. Kabat | 导师 | 1948 哥伦比亚大学在其实验室入门免疫学（实验性超敏反应机制，两年） |
| advisor-student | Bernard Halpern | 导师 | 巴黎 Broussais 医院其实验室（1950-56，网状内皮系统与免疫） |
| colleague | Guido Biozzi | 无向 | 巴黎时期密友，合作研究颗粒物清除与免疫 |
| spouse | Annette Dreyfus | 无向 | 1943 结婚，2011 年先其两月去世 |
| parent-child | Beryl Benacerraf | 女儿 | 女儿，哈佛医学院毕业，Brigham 妇女医院与 MGH 主任级医师（2022 逝） |

> relations=7 为诚实值，Review 勿误判虚增。
> 不入库：兄 Paul Benacerraf（普林斯顿哲学家——同胞手足无对应关系类型，仅在身份页提及）；父 Abraham（纺织商）母 Henrietta Lasry（阿尔及利亚犹太裔，背景叙事）；George W. Bakeman（弗吉尼亚医学院录取恩人——事件性，引用其诺奖自传段落叙事而非入库）。
> 库内当时无上述对手方记录，均由本 yaml 新建 stub；Dausset/Snell 由本批各自 yaml 幂等覆盖。

## 五、配色方案 【人物专属】

- **气质**：加拉加斯的暖橙 + 巴黎实验室的灰 + 哈佛的深红
- **主色**：免疫红 `#9E2B25`（免疫应答的活性色，亦呼应哈佛深红传统）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` Ir 基因与 MHC — 免疫红 `#9E2B25`
  - `badgeB` 巴黎岁月（Halpern/Biozzi） — 灰蓝 `#4A5A6A`
  - `badgeC` 被拒与坚韧 — 灰紫 `#5C5470`
  - `badgeD` 自身免疫的启示 — 深青 `#0E7C7B`
- **背景母题**：细胞膜弧线上一排发光"门牌"方格（MHC 分子），responder/non-responder 双列对照元素。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — 免疫应答基因的发现者 / Baruj Benacerraf 1920–2011 + 四色 badge + 右上头像 + 国籍行 Venezuela/USA
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生加拉加斯、摩洛哥-委内瑞拉塞法迪犹太裔/
    阿尔及利亚犹太裔母亲、教育 Columbia BS 1942/弗吉尼亚医学院 MD、
    任职 NYU/NIH/哈佛（1970-91）/Dana-Farber、荣誉 Nobel 1980/National Medal of Science 1990、核心领域）
03  核心贡献概览 — responder/non-responder / Ir 免疫应答基因 / MHC 基因群 / 自身免疫疾病
04  加拉加斯到巴黎到纽约 (1920–1942) — 委内瑞拉出生、1925 迁巴黎、返委内瑞拉后
    1940 移美、Lycée Français de New York 会考、哥伦比亚 BS 1942
05  被拒的医学院 — 优秀成绩却因犹太与外来背景被众多医学院拒绝、
    诺奖自传引语（"kindness and support of George W. Bakeman..."可引原文）、
    弗吉尼亚医学院 MD（唯一录取者）、入学后即入籍
06  军旅与哥大入门 (1945–1950) — 1945-48 陆军（南锡军医院）、
    1948 在哥大 Kabat 实验室两年入门免疫学（实验性超敏反应）
07  巴黎六年 (1950–1956) — 因家事返法、Broussais 医院 Halpern 实验室、
    与 Biozzi 密友合作、网状内皮系统清除颗粒物研究并建立方程、
    因无法在法国建立独立实验室而返美
08  NYU 与重大发现 (1956–1968) — 建立自己的实验室、重返超敏反应研究、
    同遗传动物注入抗原出现 responder/non-responder 两组、
    显性常染色体免疫应答（Ir）基因的决定作用
09  MHC 基因群 — 30+ 基因的主要组织相容性复合体、
    自身免疫疾病（多发性硬化/类风湿关节炎）的阐明路径
10  1980 诺贝尔奖 — 三人共享官方理由逐字引用、
    同届：Dausset（HLA 人系统）与 Snell（H-2 小鼠系统）——三角互补
11  荣誉序列 — AAAS Fellow 1971、Rous-Whipple 1985、National Medal of Science 1990、
    Gold-Headed Cane 1996、Charles A. Dana 1996、十校荣誉博士（1981-1995）
12  个人生活与身后 — 妻 Annette Dreyfus（1943 结婚、2011 先其两月逝）、
    女儿 Beryl（哈佛医学院毕业、Brigham/MGH 主任级医师，2022 逝）、
    2011-08-02 卒于 Jamaica Plain（肺炎，90 岁）、自传 1998 年出版
13  教育者的另一面 — 转向培养新科学家、 devoted 实验室育人（page.md 口径）
14  遗产 — 从移植排斥到自身免疫的 MHC 时代、
    "犹太背景被拒"与科学界多元化的历史注脚、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方逐字 "for their discoveries concerning genetically determined structures on the cell surface that regulate immunological reactions"（三人共享、their）；page.md 另引 Nobel 表述 "discovery of the major histocompatibility complex genes..."——两种口径各自照抄勿混 |
| 国籍裁定 ★ | manifest 仅 United States；citation json 官方 **"Venezuela United States"**；page.md citizenship Venezuela+US(1943 起)——yaml 取 Venezuela(0)+United States(1)（官方顺序），供主控统一口径 |
| 医学院拒录 | 诺奖自传引语完整（page.md 英文原文在）："refused admission by the numerous medical schools...kindness and support of George W. Bakeman"——可引原文+译文；Bakeman 系事件恩人不入库 |
| 双导师 | Kabat（哥大入门免疫学，1948 两年）+ Halpern（巴黎 Broussais，1950-56）——两条 advisor-student 边 note 区分；Biozzi 是"密友同事"用 colleague |
| 返美原因 | "无法在法国建立自己的独立实验室"（page.md 口径）——1956 返美的动因，如实 |
| 哥哥 | Paul Benacerraf 系著名哲学家（普林斯顿）——身份页一句；无 sibling 类型不入库 |
| 女儿 | Beryl Benacerraf（放射科医师，Brigham/MGH 主任级，2022 逝）——parent-child 入库（page.md 明载其履历） |
| 妻子去世 | Annette 先其**两月**去世（2011）——时间细节勿错 |
| 300+ 论著 | "including a variety of different editions, over 300 books and articles"——口径含不同版本，勿简化为"300 篇论文" |
| 1948 双起点 | 1948 既开始研究过敏、又入 Kabat 实验室——两个 1948 事件并存 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| Ir genes (immune response genes) | 免疫应答基因 | 其诺奖核心发现 |
| MHC | 主要组织相容性复合体 | 30+ 基因群 |
| responder / non-responder | 应答者/无应答者 | 动物实验的两组划分 |
| hypersensitivity | 超敏反应 | 早年研究方向 |
| reticuloendothelial system | 网状内皮系统 | 巴黎时期研究对象 |
| transplant rejection | 移植排斥 | Ir 基因调控对象 |
| Sephardic Jewish | 塞法迪犹太裔 | 父系摩洛哥-委内瑞拉背景 |
| Fabyan Professor | Fabyan 讲席教授 | 哈佛比较病理学讲席 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**PAST**（manifest 预分配）
- **风格**：历史感 / 深沉 / 回望
- **匹配理由**：塞法迪犹太家庭的三国迁徙、被医学院拒之门外的屈辱、巴黎六年的蛰伏——PAST 的历史回望感匹配"过去的每次拒绝都在为未来的发现蓄力"的叙事；MHC 研究本身也是对免疫"过去记忆"（自我/非我识别）的科学解读。
- **本地路径**：`music_audio/alex-productions/89-geyy8_WXDK0-PAST.wav` → 复制为 `presentations/20th_century/Baruj_Benacerraf/PAST.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；拒录自传引语与国籍裁定务必精确。**
