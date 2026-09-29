# 医学家立传提示词（Michael Houghton）

> OpenMedic 项目、21 世纪诺贝尔生理学或医学奖 2020 年得主（迈克尔·霍顿，丙型肝炎病毒的鉴定者）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Sir Michael Houghton（1949 生于伦敦，在世；page.md 未载月日）
- **气质关键词**：**丙肝病毒的鉴定者、丁肝基因组的共同发现者、为同事拒领大奖的谦逊者、HCV 疫苗的现行攻坚者** —— 2020 获奖理由（与 Harvey J. Alter、Charles M. Rice 三人共享）：
  > "for the discovery of Hepatitis C virus"（因发现丙型肝炎病毒）
- **设计母题**：**百万分之一的猎获**。在数百万克隆中筛选出 HCV 的核酸片段——从输血感染率"三分之一"到"二百万分之一"，一条向下的风险曲线就是其成就的坐标轴。视觉隐喻：文库筛出的那一枚发光克隆。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Michael_Houghton_virologist/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/21th_century/Michael_Houghton_virologist/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准，裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/21th_century/Michael_Houghton_virologist/`（含 `images/`）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=Michael_Houghton_virologist_zh`、`VIDEO_NAME=Michael_Houghton_virologist_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/21th_century/Michael_Houghton_virologist/images.txt`（2017 照）；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/Michael_Houghton_virologist.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | virology | 病毒学 | HCV 鉴定者，2020 诺奖核心 | 核心页 |
| 1 | microbiology | 微生物学 | infobox Fields | 身份页 |
| 2 | biochemistry | 生物化学 | KCL 博士专业（RNA 聚合酶与转录） | 早年页 |
| 3 | vaccinology | 疫苗学 | Alberta 的 HCV 单株疫苗（2013） | 研究页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Norman Carey | 导师 | 伦敦国王学院博士导师之一（1977，鸡输卵管 RNA 聚合酶与转录） |
| advisor-student | James Chesterton | 导师 | 伦敦国王学院博士导师之一 |
| co-honored | Harvey J. Alter | 无向 | 2020 诺贝尔生理学或医学奖三人共享（发现丙型肝炎病毒） |
| co-honored | Charles M. Rice | 无向 | 2020 诺贝尔生理学或医学奖三人共享（发现丙型肝炎病毒） |
| collaborator | Qui-Lim Choo | 无向 | Chiron 同事，1989 共同发现丙型肝炎病毒 |
| collaborator | George Kuo | 无向 | Chiron 同事，1989 共同发现丙型肝炎病毒 |
| collaborator | Daniel W. Bradley | 无向 | CDC 研究员，提供 NANBH 样本共同发现丙型肝炎病毒 |

> 在世者，relations=7 为诚实值，Review 勿误判虚增或缺漏。
> ★ Choo/Kuo 不获诺奖而 Houghton 获奖是公认讨论点——二人以 collaborator 入库（page.md 明载共同发现），陷阱表要求客观呈现。
> 不入库：兄 Graham、父母（工人家庭背景叙事）；G. D. Searle 时期同事未具名。
> 库内当时无 Norman Carey / James Chesterton / Qui-Lim Choo / George Kuo / Daniel W. Bradley 记录，均由本 yaml 新建 stub；Alter/Rice 由本批各自 yaml 规范化。

## 五、配色方案 【人物专属】

- **气质**：伦敦工人街区的朴实 + 分子克隆的精密 + 拒领大奖的风骨
- **主色**：皇家蓝 `#274690`（英伦底色与文库筛选的深潜）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` HCV 鉴定 — 皇家蓝 `#274690`
  - `badgeB` 丁肝基因组 — 暗红 `#8C2F1B`
  - `badgeC` 血液筛查革命 — 深青 `#0E7C7B`
  - `badgeD` 疫苗攻坚 — 琥珀 `#B4632C`
- **背景母题**：密集点阵文库中一枚高亮圆点（筛出的克隆），配下行的风险曲线细线。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — 丙肝病毒的鉴定者 / Michael Houghton 1949– + 四色 badge + 右上头像 + 国籍行 United Kingdom
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生于伦敦 1949、教育 UEA BSc 1972/KCL PhD 1977、
    导师 Carey & Chesterton、任职 Chiron/Alberta、荣誉 Nobel 2020/Lasker 2000/Knight 2021、
    核心领域；出生月日 page.md 未载，写 1949）
03  核心贡献概览 — HCV 的鉴定 / 丁肝基因组 / 血液筛查 / 疫苗攻坚
04  伦敦工人家庭 (1949–1972) — 父为卡车司机与工会干部、Lyndhurst Grove 小学、
    获奖学金入 Alleyn's School 专修理化数、UEA 奖学金、1972 生物学二等乙荣誉学位
05  国王学院博士 (1972–1977) — 生物化学 PhD 1977、鸡输卵管 RNA 聚合酶与转录研究、
    双导师 Norman Carey 与 James Chesterton
06  工业界：Searle 与 Chiron (1977–1982) — 先入 G. D. Searle、1982 转投 Chiron 公司——
    工业实验室成为病毒猎场
07  1986：丁肝基因组 — 与同事共同发现丁型肝炎病毒基因组
08  1989：HCV 的鉴定 — 与 Choo/Kuo（Chiron）及 Bradley（CDC，提供 NANBH 样本）
    首次获得丙肝病毒证据、 cDNA 文库筛选的攻坚叙事
09  从鉴定到筛查 (1989–1992) — 1989-1990 系列里程碑研究：血中 HCV 抗体检测、
    1990 首代筛查测试、1992 更敏感测试普及——加拿大血源 HCV 污染基本消除
10  风险曲线的沉降 — 输血感染 HCV 风险从 1/3 降至约 1/200 万、
    仅美国每年至少避免 4 万新感染、并关联肝癌研究
11  2013：拒领 Gairdner ★ — 首位拒领 10 万加元 Gairdner 奖的人、
    引语原文（page.md 载）："没有两位同事 Choo 与 Kuo 在列，我受之有愧"——风骨页
12  2020 诺贝尔奖 — 与 Alter/Rice 三人共享、Choo/Kuo/Bradley 不在获奖名单的公认讨论点——
    客观呈现分工与局限（诺奖规则框架内的事实陈述）
13  Alberta 岁月与疫苗 — Canada Excellence Research Chair、李嘉诚病毒学讲席教授、
    应用病毒研究所所长、2013 单株疫苗抗全株（2020 临床前）
14  荣誉与遗产 — Karl Landsteiner 1992、Robert Koch Prize 1993、William Beaumont 1994、
    Lasker 2000、Gairdner 2013（拒领）、爵位 2021、UEA 与香港浸会大学荣誉博士、
    血液安全的全球坐标、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方逐字 "for the discovery of Hepatitis C virus"（三人共享） |
| 出生信息 ★ | page.md 仅载 1949 年（metadata date_of_birth '1949-00-00'）——yaml 存 '1949-00-00'，幻灯片与正文一律写 "1949 年生"，**勿杜撰月日** |
| 四人组与诺奖 | HCV 鉴定是 Houghton+Choo+Kuo（Chiron）+Bradley（CDC）四人工作，诺奖仅授 Houghton——Choo/Kuo/Bradley 以 collaborator 入库；第 12 页客观陈述"分工与诺奖规则框架"，勿替委员会辩护或攻击 |
| 拒领 Gairdner ★ | 2013 首例拒领 10 万加元奖；引语逐字引自 page.md（英文原文在）："I felt that would be unfair of me to accept this award without the inclusion of two colleagues, Dr. Qui-Lim Choo and Dr. George Kuo."——本篇人格高光，务必引原文+译文 |
| 学位口径 | UEA 为 lower second class honours（二等乙）——page.md 明载，诚实呈现勿美化 |
| 丁肝在前 | 丁肝基因组共同发现是 **1986**，早于 HCV 的 1989——时间线勿倒置 |
| 数字锚点 | 输血 HCV 风险 1/3 → 约 1/200 万；美国年防 4 万+ 新感染；1990 首代筛查、1992 敏感版普及——数字勿错 |
| 规范名 | manifest/库内用 **Michael Houghton (virologist)**（消歧义括号是规范名一部分）；正文首现写全名 Sir Michael Houghton |
| 双导师 | Norman Carey + James Chesterton 并列——两条 advisor 边 |
| 爵位年份 | 2021 Birthday Honours 封爵士（Knight Bachelor）——勿写 2020 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| hepatitis C virus (HCV) | 丙型肝炎病毒 | 2020 诺奖对象 |
| hepatitis D genome | 丁型肝炎基因组 | 1986 共同发现 |
| cDNA library screening | cDNA 文库筛选 | HCV 鉴定的方法学 |
| NANBH specimen panel | 非甲非乙肝炎样本组 | CDC Bradley 提供的材料 |
| antibody testing | 抗体检测 | 血液筛查的原理 |
| single-strain vaccine | 单株疫苗 | 2013 Alberta 成果 |
| lower second class honours | 二等乙荣誉学位 | 诚实呈现的学历细节 |
| Chiron Corporation | 奇龙公司 | 工业界实验室 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Through the Darkness**（manifest 预分配）
- **风格**：黑暗中前行 / 悲怆转光明 / 史诗
- **匹配理由**：在未知病毒的黑暗中筛查百万克隆，那枚发光的克隆就是隧道尽头的光；Through the Darkness 匹配其"工业实验室里的漫长攻坚"，也呼应他宁愿拒领大奖也不让同事隐入黑暗的风骨。
- **本地路径**：`music_audio/inspiring-electronic/14-Trn1cSsY2t8-Audiomachine - Through the Darkness.wav` → 复制为 `presentations/21th_century/Michael_Houghton_virologist/Through_the_Darkness.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；拒领引语与四人分工务必忠实 page.md。**
