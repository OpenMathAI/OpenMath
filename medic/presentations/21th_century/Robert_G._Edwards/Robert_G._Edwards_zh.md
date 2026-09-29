# 医学家立传提示词（Robert G. Edwards）

> OpenMedic 项目、21 世纪诺贝尔生理学或医学奖 2010 年得主（罗伯特·爱德华兹，体外受精 IVF 之父）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Sir Robert Geoffrey Edwards（1925-09-27 生于约克郡 Batley ~ 2013-04-10 卒于剑桥附近家中，享年 87 岁）
- **气质关键词**：**体外受精的开拓者、四百万家庭的送子者、在争议中坚持三十年的生理学家** —— 2010 获奖理由（独享）：
  > "for the development of in vitro fertilization"（因发展体外受精技术）
- **设计母题**：**第一个细胞团**。1978-07-25 23:47，Louise Brown 在 Oldham General Hospital 诞生——护士 Jean Purdy 是第一个看到胚胎分裂的人。视觉隐喻：显微镜下的受精卵从单细胞到桑葚胚的四次分裂，裂而复始，生生不息。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Robert_G._Edwards/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/21th_century/Robert_G._Edwards/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准，裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/21th_century/Robert_G._Edwards/`（含 `images/`）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=Robert_G._Edwards_zh`、`VIDEO_NAME=Robert_G._Edwards_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/21th_century/Robert_G._Edwards/images.txt`；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。插图可用 Bourn Hall Clinic 照。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/Robert_G._Edwards.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | reproductive medicine | 生殖医学 | IVF 开创，2010 诺奖核心 | 核心页 |
| 1 | in vitro fertilization | 体外受精 | 1968 体外受精成功 → 1978 首例试管婴儿 | 核心页 |
| 2 | embryology | 胚胎学 | 爱丁堡胚胎学博士起点、配子与早期胚胎培养 | 早年页 |
| 3 | physiology | 生理学 | 剑桥生理系 Reader（1969） | 身份页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | R. A. Beatty | 导师 | 爱丁堡大学博士导师之一（1955 PhD，小鼠异倍体诱导） |
| advisor-student | C. H. Waddington | 导师 | 爱丁堡动物遗传学与胚胎学研究所博士导师之一 |
| advisor-student | Richard Gardner (embryologist) | 学生 | infobox 明载博士生 |
| advisor-student | Martin Hume Johnson | 学生 | infobox 明载博士生 |
| advisor-student | Roger Gosden | 学生 | 最早的博士生之一（正文与 infobox 均载） |
| advisor-student | Azim Surani | 学生 | infobox 明载博士生 |
| collaborator | Patrick Steptoe | 无向 | IVF 共同开创者（腹腔镜取卵），1978-07-25 Louise Brown 诞生 |
| collaborator | Jean Purdy | 无向 | 护士兼胚胎学家，首个看到 Brown 胚胎分裂，共创 Bourn Hall |
| spouse | Ruth Fowler Edwards | 无向 | 1956 结婚（infobox 作 1959），育五女；Rutherford 外孙女 |

> relations=9 为诚实值（infobox Doctoral students 四人全收）。Review 勿误判虚增。
> 不入库：Louise Brown（首例试管婴儿，医患成果对象非关系）；Simon Fishel（颁奖礼转述者）；Alastair MacDonald（首例 IVF 男婴，铭牌揭幕者）；Göran K. Hansson（诺奖宣布人）；Ralph Fowler（岳父，物理学家，非本人关系；库内 #2039 为同名物理学家记录，注意勿误连）。
> 库内当时无上述对手方记录，均由本 yaml 新建 stub（R. A. Beatty / C. H. Waddington / Richard Gardner (embryologist) / Martin Hume Johnson / Roger Gosden / Azim Surani / Patrick Steptoe / Jean Purdy / Ruth Fowler Edwards）。

## 五、配色方案 【人物专属】

- **气质**：晨曦般的暖 + 实验室玻璃器皿的透亮 + 三十年争议中的坚韧
- **主色**：晨光橙棕 `#B4632C`（生命的起点、暖箱与第一缕晨光）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` IVF 开创 — 晨光橙棕 `#B4632C`
  - `badgeB` 胚胎学根基 — 深青 `#0E7C7B`
  - `badgeC` 争议与坚持 — 灰紫 `#5C5470`
  - `badgeD` Bourn Hall 与传承 — 钢蓝 `#2E4A66`
- **背景母题**：圆形细胞分裂序列（1→2→4→8 细胞）作为版面装饰元素，呼应"第一个细胞团"。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — IVF 之父 / Robert G. Edwards 1925–2013 + 四色 badge + 右上头像 + 国籍行 United Kingdom
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 Batley/Cambridge、教育 Bangor BSc/Edinburgh
    PhD 1955、导师 Beatty & Waddington、任职 NIMH/Glasgow/Cambridge/Bourn Hall、
    荣誉 Nobel 2010/Lasker 2001/Knight Bachelor 2011、核心领域）
03  核心贡献概览 — 人类体外受精 / 首例试管婴儿 / Bourn Hall 与行业建立 / 生殖医学的科学化
04  约克郡少年与军旅 (1925–1951) — Batley 出生、Manchester Central High School、
    英国陆军服役、Bangor 大学普通学位毕业
05  爱丁堡：胚胎学起点 (1951–1955) — 动物遗传学与胚胎学研究所（Roslin 前身）、
    Beatty 与 Waddington 双导师、1955 博士论文《小鼠异倍体的实验诱导》
06  辗转与定型 (1956–1963) — Caltech 博后一年、NIMH Mill Hill、Glasgow 一年、
    1963 剑桥生理系 Ford Foundation Fellow + Churchill College
07  1960s：人卵体外受精 — 约 1960 起研究人类受精、1968 实验室受精人卵成功、
    开发人类培养液支持受精与早期胚胎培养
08  三人组成立：Edwards + Steptoe + Purdy — Oldham 妇科腹腔镜专家 Steptoe 取卵、
    护士兼胚胎学家 Purdy、输卵管性不孕患者、若干次诉讼与 MRC 拒绝资助的逆境
09  1978-07-25 23:47：Louise Brown — 世界首例试管婴儿诞生于 Oldham General Hospital、
    Purdy 首个看到胚胎分裂、不孕治疗新纪元
10  Bourn Hall 与行业建立 — 三人共创世界首个 IVF 诊所、培训各国专家、
    Purdy 1985 与 Steptoe 1988 先后离世、Edwards 创刊《Human Reproduction》（1986）
11  从 400 万到 1200 万 — 2010 年约 400 万 IVF 儿童出生（含约 17 万捐卵/捐胚）；
    技术延伸：ICSI、PGD 胚胎活检、干细胞研究的地基
12  2010 诺贝尔奖 — 10-04 宣布、独享（Steptoe/Purdy 已逝，诺奖不追授）、
    Louise Brown 称 "fantastic news"、梵蒂冈官员斥 "completely out of order"、
    颁奖礼由妻子 Ruth Fowler Edwards 代领（Fishel 转述）；2001 Lasker 临床奖为前奏
13  晚年与身后 — 2011 生日荣誉封爵士、BBC《The New Elizabethans》入选（2012）、
    2013-04-10 卒于剑桥附近家中；2013-07 Bourn Hall 铭牌（Steptoe/Edwards/Purdy 并立）
14  遗产 — 不孕从宿命变为可治之症、约千万家庭的改变、
    生殖医学的伦理框架因他而立、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方逐字 "for the development of in vitro fertilization"；2010 独享——Steptoe（1988 逝）与 Purdy（1985 逝）先逝且诺奖不追授，勿写"共享"或"三人获诺奖" |
| 三人组功劳 | IVF 是三人协作：Edwards（培养液/受精）+ Steptoe（腹腔镜取卵）+ Purdy（胚胎学家、首个看到胚胎分裂）——呈现时三人并立，勿只写 Edwards+Steptoe 双人 |
| 结婚年份双值 ★ | 正文 "married ... in 1956"，infobox "(m. 1959)"——以正文 1956 为准并注记；Ruth 婚前姓 Fowler，系 Rutherford 外孙女、物理学家 Ralph Fowler 之女 |
| 争议呈现 | MRC 拒资助、数起诉讼、梵蒂冈反对（2010 诺奖后官员称 "completely out of order"）——按 page.md 客观转述，不站队 |
| 代领诺奖 | 2010-12 斯德哥尔摩颁奖礼，Edwards 因病缺席，妻子代领——出自 Fishel 转述（page.md 有引文），注明转述来源 |
| 学位口径 | Bangor 是 ordinary degree（普通学位）——勿美化为一等学位；PhD 1955 爱丁堡 |
| 数据年份 | "2010 年约 400 万 IVF 儿童"；Guardian 在其 2013 去世时称"逾 400 万"——两个口径勿混写成一个数 |
| 政治参与 | 支持工党、剑桥市议会议员（Newnham 选区 1973-78 两任）、曾考虑竞选国会议员——page.md 明载可写 |
| 姓名 | Robert Geoffrey Edwards；yaml/manifest 用 "Robert G. Edwards"；库内另有 Sam Edwards（物理学家）为不同人，勿混淆 |
| 与 Rutherford 连接 | 岳祖母家世（Rutherford 外孙女）是姻亲事实——库内 Ernest Rutherford 为chemist侧规范记录，不入 Edwards 关系边 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| in vitro fertilization (IVF) | 体外受精 | 官方获奖理由用 fertilization（美拼），正文 fertilisation（英拼）——引语照原文 |
| laparoscopy | 腹腔镜检查 | Steptoe 的取卵技术 |
| culture media | 培养液 | Edwards 的关键贡献之一 |
| ovocyte / oocyte | 卵母细胞 | 取卵对象 |
| ICSI | 卵胞浆内单精子注射 | IVF 后续技术 |
| PGD | 着床前遗传诊断 | 胚胎活检延伸 |
| Bourn Hall Clinic | 伯恩霍尔诊所 | 世界首个 IVF 诊所 |
| Knight Bachelor | 下级勋位爵士 | 2011 生日荣誉 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Through the Darkness**（manifest 预分配）
- **风格**：黑暗中前行 / 悲怆转光明 / 史诗
- **匹配理由**：三十年孤独求索——MRC 拒资助、诉讼缠身、宗教界反对，直至 1978 年深夜的第一声啼哭；Through the Darkness 的"穿越黑暗终见光明"结构，正是 IVF 从争议到四百万家庭的弧线，亦暗合其晚年失智缺席颁奖的苍凉。
- **本地路径**：`music_audio/inspiring-electronic/14-Trn1cSsY2t8-Audiomachine - Through the Darkness.wav` → 复制为 `presentations/21th_century/Robert_G._Edwards/Through_the_Darkness.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；争议史与三人功劳呈现务必按 page.md 客观完整。**
