# 医学家立传提示词（Katalin Karikó）

> OpenMedic 项目、21 世纪诺贝尔生理学或医学奖 2023 年得主（卡塔琳·考里科，核苷修饰 mRNA 技术的奠基人）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Katalin "Kati" Karikó（1955-01-17 生于匈牙利索尔诺克，在世）
- **气质关键词**：**mRNA 疗法的科学地基、被降职仍不放弃的坚韧者、拯救数百万生命的假尿苷修饰发明人** —— 2023 获奖理由（与 Drew Weissman 两人共享）：
  > "for their discoveries concerning nucleoside base modifications that enabled the development of effective mRNA vaccines against COVID-19"（因发现核苷碱基修饰，从而使针对新冠的有效 mRNA 疫苗得以开发）
- **设计母题**：**一枚被"静音"的尿苷**。把 mRNA 中的尿苷换成假尿苷，免疫系统便不再攻击它——"修改一个字母，改写一场大流行"。视觉隐喻：RNA 链上一个发光的替换碱基，向外辐射成疫苗瓶轮廓。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Katalin_Karikó/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/21th_century/Katalin_Karikó/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准，裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/21th_century/Katalin_Karikó/`（含 `images/`；目录名含 ó，Makefile/shell 注意 UTF-8）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=Katalin_Karikó_zh`、`VIDEO_NAME=Katalin_Karikó_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/21th_century/Katalin_Karikó/images.txt`（2024 肖像/与 Szent-Györgyi 雕像合照）；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/Katalin_Karikó.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biochemistry | 生物化学 | 核苷修饰 mRNA，2023 诺奖核心 | 核心页 |
| 1 | messenger RNA | 信使 RNA 治疗 | 体外转录 mRNA 用于蛋白替代疗法 | 核心页 |
| 2 | RNA immunology | RNA 免疫学 | 假尿苷抑制免疫原性 | 核心页 |
| 3 | vaccine technology | 疫苗技术 | mRNA 疫苗与脂质纳米颗粒递送 | 研究页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Drew Weissman | 无向 | 2023 诺贝尔生理学或医学奖两人共享（核苷碱基修饰使有效 mRNA 疫苗成为可能） |
| collaborator | Drew Weissman | 无向 | 1997 相识于宾大复印机旁，2005 起系列里程碑研究，RNARx 共同创立与专利共同持有人 |
| colleague | Jenő Tomasz | 无向 | 塞格德大学与匈牙利科学院 BRC 时期合作者 |
| advisor-student | Robert J. Suhadolnik | 导师 | Temple University 博士后东家（1985-88，dsRNA 临床试验） |
| colleague | Elliot Barnathan | 无向 | 宾大心脏病学家，1989 引其进入 mRNA 研究 |
| collaborator | Uğur Şahin | 无向 | BioNTech 合作（2014 mRNA 治疗综述与 2020 BNT162b1 论文合著者） |
| spouse | Béla Francia | 无向 | 结婚，1985 携全家赴美 |
| parent-child | Susan Francia | 女儿 | 女儿，两届奥运会赛艇金牌得主 |

> 在世者，relations=8 为诚实值，Review 勿误判虚增。
> 不入库：Ian MacLachlan（Tekmira 时期的合作尝试，曾被拒——事件叙事不入关系边）；David Langer（聘用她的神经外科医生，事件性）；Özlem Türeci（2014 综述共同作者，仅 Şahin 入库代表性足够）；Gary Dahl（专利受让方商人）；Moderna/Flagship/Pfizer（企业非个人）；父母（屠夫与簿记员，背景叙事）。
> 库内当时无上述对手方记录，均由本 yaml 新建 stub；Weissman 由本批其本人 yaml 规范化。

## 五、配色方案 【人物专属】

- **气质**：匈牙利平原的麦金 + 实验台深夜的灯光 + mRNA 链的柔韧
- **主色**：麦金绿 `#2F6B4F`（塞格德的学术绿与生命科技的生机）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` 核苷修饰 — 麦金绿 `#2F6B4F`
  - `badgeB` mRNA 疗法 — 深青 `#0E7C7B`
  - `badgeC` 冷遇与坚持 — 灰紫 `#5C5470`
  - `badgeD` 疫苗的全球之战 — 暗红 `#8C2F1B`
- **背景母题**：一条 RNA 链细线上一个高亮碱基（假尿苷），自其向外放射疫苗瓶轮廓线。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — mRNA 技术的奠基人 / Katalin Karikó 1955– + 四色 badge + 右上头像 + 国籍行 Hungary/USA
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生 Szolnok、成长 Kisújszállás、
    教育 Szeged BSc 1978/PhD 1982、任职 BRC/Temple/Uniformed Services/宾大/BioNTech/Szeged、
    荣誉 Nobel 2023/Lasker 2021/Time Hero of the Year 2021、核心领域）
03  核心贡献概览 — 核苷修饰 / mRNA 治疗平台 / 脂质纳米颗粒递送 / 新冠疫苗的科学地基
04  无自来水的小屋 (1955–1978) — Szolnok 出生、Kisújszállás 长大、无自来水/冰箱/电视、
    父为屠夫（因参加 1956 革命受罚）、母为簿记员、匈牙利生物竞赛第三名
05  塞格德岁月 (1978–1985) — BSc 1978/PhD 1982、与 Jenő Tomasz 合作、BRC 博后、
    1985 BRC 经费断供；1985-88 被列为由匈牙利秘密警察的情报档案——
    她称系受要挟、未提供过信息也未做过情报活动（自述口径，客观呈现）
06  一只塞满 900 英镑的泰迪熊 (1985) — 卖车换汇（黑市）、一家三口赴美、
    泰迪熊腹中缝入 900 英镑——Temple University Suhadolnik 供给职位
07  Temple 与 dsRNA 临床试验 (1985–1988) — AIDS/血液病/慢性疲劳患者的 dsRNA 治疗、
    干扰素诱导机制未明时代的开创性研究
08  宾大与三十年冷遇 (1989–2013) — 1989 入宾大（Barnathan 团队）、1990 首份 mRNA 基因治疗
    基金申请、1990s mRNA 被学界与产业抛弃、 repeated 拒资助、1995 降职、
    从未获终身教职、Barnathan 引语 "Kate was really just unbelievable..."（可引原文）
09  1997：复印机旁的相遇 — 与免疫学家 Weissman 相识、抱怨 RNA 研究缺经费、
    他的免疫学 × 她的生物化学、Weissman 引语 "We had to fight the entire way."
10  2005：假尿苷的胜利 — tRNA 对照不引起炎症的洞察、用假尿苷替换尿苷、
    关键论文先遭 Nature/Science 拒稿、终被 Immunity 接受——2005 起系列里程碑
11  LNP 递送与专利波折 — 脂质纳米颗粒包裹 mRNA 的递送系统、动物实验验证、
    RNARx（2006 创立）、2006/2013 专利、宾大售 IP 予 Cellscript（Gary Dahl）、
    Moderna 来授权时已不可得、MacLachlan/Tekmira 合作未成
12  BioNTech 与新冠之战 (2013–2022) — 2013 见 Moderna-AstraZeneca 2.4 亿美元交易后
    转任 BioNTech VP（2019 SVP）、2022 离开回归研究；2020 BNT162b1（与 Şahin 等合著）、
    Pfizer/BioNTech 与 Moderna 疫苗 >90% 保护率、史无前例的速度
13  2023 诺贝尔奖与回赠 — 10-02 宣布、两人共享；诺奖周引语
    "I dreamt about doing research, not getting an award."（可引原文）；
    2024-04-16 将逾 50 万美元奖金捐给母校塞格德大学
14  遗产 — 自传《Breaking Through》（2023，匈牙利年度非虚构畅销、9+ 语言译本）、
    130+ 国际奖项、Time 100/BBC 100 Women、国家发明家名人堂 2023、
    NAS 院士 2025、mRNA 从边缘到"一类新药"的范式转移、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方逐字 "for their discoveries concerning nucleoside base modifications that enabled the development of effective mRNA vaccines against COVID-19"（长句完整引用，their） |
| 特工档案呈现 ★ | 1985-88 列为匈牙利秘密警察情报资产系 page.md 明载——**以她的自述口径转述**（受要挟、未提供信息、未做过情报活动），标注"她称/她自述"，不判定真伪、不展开冷战叙述 |
| Suhadolnik 事件 | 赴 Johns Hopkins 事件出自 Zuckerman 2021 书（二手转述）+ Karikó 确认；须标注"据 Zuckerman 书转述"+她后来"感谢 Suhadolnik 给我 IAP66 与实验室机会"的回应引语——**两面呈现，不站队** |
| 降职与冷遇 | 1995 降职、从未获终身教职、宾大"主动劝阻/欠资/deprioritize mRNA"——page.md 明载，客观呈现学术体制的迟钝，不情绪化 |
| 拒稿史 | 关键论文先遭 Nature 与 Science 拒稿、终被 Immunity 接受——科学传播史的经典桥段，如实写 |
| 专利链顺序 | RNARx 专利 → 宾大售 IP 给 Gary Dahl（Cellscript）→ 数周后 Flagship/Moderna 来谈已不可得 → 授权 Moderna/BioNTech——顺序勿倒 |
| 女儿 | Susan Francia 系两届奥运赛艇金牌得主（parent-child 边，note 注明）——体坛成就如实标注 |
| 姓名变体 | 匈牙利语姓前名后 "Karikó Katalin"、英语序 "Katalin Karikó"、昵称 Kati、infobox Other name "Kati Kariko"（无重音）——正文统一 Katalin Karikó |
| 目录名含 ó | {Dir}=Katalin_Karikó——Makefile/shell 引用注意 UTF-8；tex 用 ó 字符（XeLaTeX 原生） |
| 2026 口径 | 匈牙利卫生部长顾问委员会成员（2026 起）与 Forbes Hungary 50 人名单照 page.md 写（当前 2026 年） |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| nucleoside modification | 核苷修饰 | 获奖理由核心词 |
| pseudouridine | 假尿苷 | 替换尿苷的"静音"碱基 |
| in vitro-transcribed mRNA | 体外转录 mRNA | 其技术平台基础 |
| immunogenicity | 免疫原性 | 修饰所抑制的对象 |
| lipid nanoparticle (LNP) | 脂质纳米颗粒 | 递送系统 |
| protein replacement therapy | 蛋白替代疗法 | mRNA 治疗的最初愿景 |
| RNARx | RNARx 公司 | 2006-2013 其任 CEO |
| BNT162b1 | BNT162b1 | 2020 BioNTech 疫苗论文代号 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Nostalgia**（manifest 预分配）
- **风格**：回望 / 温情 / 坚韧
- **匹配理由**：从无自来水的小屋到斯德哥尔摩音乐厅——Nostalgia 的回望感匹配"被降职、被拒稿、被时代冷落三十年仍不回头"的漫长坚守；那个塞满 900 英镑的泰迪熊，正是这首曲子最温柔的记忆锚点。
- **本地路径**：`music_audio/alex-productions/86-5ETNuoDcBg4-Nostalgia.wav` → 复制为 `presentations/21th_century/Katalin_Karikó/Nostalgia.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；特工档案与 Suhadolnik 事件务必按自述/转述口径两面呈现。**
