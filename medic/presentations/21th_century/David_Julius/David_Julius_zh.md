# 医学家立传提示词（David Julius）

> OpenMedic 项目、21 世纪诺贝尔生理学或医学奖 2021 年得主（戴维·朱利叶斯，辣椒素受体 TRPV1 的克隆者）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：David Jay Julius（1955-11-04 生于纽约市，在世）
- **气质关键词**：**痛觉分子机制的解密者、TRPV1 辣椒素受体的克隆者、从"为什么辣会疼"到温度与触觉受体全景图的开拓者** —— 2021 获奖理由（与 Ardem Patapoutian 两人共享）：
  > "for the discovery of receptors for temperature and touch"（因发现温度与触觉的受体）
- **设计母题**：**一只辣椒点燃的受体**。1997 年 TRPV1 被克隆——辣椒的"热"与烫伤的"热"共用同一枚分子开关。视觉隐喻：一颗辣椒剖面化作离子通道 pore，热浪从通道涌出。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/David_Julius/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/21th_century/David_Julius/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准，裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/21th_century/David_Julius/`（含 `images/`）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=David_Julius_zh`、`VIDEO_NAME=David_Julius_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/21th_century/David_Julius/images.txt`（2022 照）；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。插图可用 2021 诺奖 TRPV1/Piezo2 机制图（22_Hegasy_EN_Nobel_Prize_2021_TRPV1_Piezo2.png）。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/David_Julius.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | neuroscience | 神经科学 | 痛觉与温度的分子机制，2021 诺奖核心 | 核心页 |
| 1 | TRP channels | TRP 离子通道 | TRPV1/TRPM8/TRPA1 的克隆与表征 | 核心页 |
| 2 | nociception | 伤害感受 | 毒素探针、物种适应、冷冻电镜结构 | 研究页 |
| 3 | biochemistry | 生物化学 | 嘌呤能受体与 5HT3 的克隆 | 研究页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Randy W. Schekman | 导师 | Berkeley 博士联合导师（1984，酵母 α 因子加工分泌，Kex2 发现） |
| advisor-student | Jeremy Thorner | 导师 | Berkeley 博士联合导师 |
| advisor-student | Richard Axel | 导师 | 哥伦比亚大学博士后导师（1989 完成，克隆 5-羟色胺 1c 受体） |
| co-honored | Ardem Patapoutian | 无向 | 2021 诺贝尔生理学或医学奖两人共享（发现温度与触觉受体） |
| spouse | Holly Ingraham | 无向 | 同在 UCSF 的神经科学家 |

> 在世者，relations=5 为诚实值，Review 勿误判缺漏。
> 不入库：infobox "Other academic advisors"（Alexander Rich / Alexander Rich 之外的语境人物——Rich 无正文语境不入库）；父母（Brighton Beach 阿什肯纳兹犹太家庭背景叙事）。
> 库内既有 Randy Schekman（#4427）与 Richard Axel（#4833, Q211940）规范记录直接引用；Jeremy Thorner / Ardem Patapoutian / Holly Ingraham 由本 yaml 新建 stub（Patapoutian 用 manifest 全名，其本人 yaml 回填）。本人记录 UPD 复用库内 stub #4837 回填 Q1174906。

## 五、配色方案 【人物专属】

- **气质**：辣椒的炽红 + 布鲁克林海风的率直 + 受体通道的精密
- **主色**：辣椒红 `#B03030`（capsaicin 之热，TRPV1 的视觉化身）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` TRPV1/热 — 辣椒红 `#B03030`
  - `badgeB` TRPM8/冷 — 冰蓝 `#2E7C9C`
  - `badgeC` 嘌呤能受体与药物 — 深青 `#0E7C7B`
  - `badgeD` 师门传承 — 钢蓝 `#2E4A66`
- **背景母题**：横向温度色带（冷→热渐变）+ 通道 pore 圆点，badge 沿温标分布。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — 辣椒素受体的克隆者 / David Julius 1955– + 四色 badge + 右上头像 + 国籍行 USA
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生纽约 Brighton Beach、教育 MIT BS 1977/
    Berkeley MS/PhD 1984/Columbia 博后、双导师 Thorner & Schekman、博后 Axel、
    任职 UCSF 1989 起、荣誉 Nobel 2021/Shaw 2010/Kavli 2020/Breakthrough 2020、核心领域）
03  核心贡献概览 — TRPV1 / TRP 超家族全景 / 嘌呤能受体与药物靶点 / 痛觉研究的结构时代
04  布鲁克林少年 (1955–1977) — Brighton Beach 阿什肯纳兹犹太家庭（俄国移民背景）、
    Abraham Lincoln High School、MIT 本科 1977
05  Berkeley 双导师岁月 (1977–1984) — Thorner 与 Schekman 联合指导、
    酵母 α 交配信息素加工分泌、鉴定 Kex2 为 furin 样前蛋白转化酶创始成员
06  Columbia：Axel 门下 (1984–1989) — 克隆并表征 5-羟色胺 1c 受体、
    裸盖菇素与 LSD 的好奇心——"自然之物如何与人类受体对话"的问题意识起点
07  1997：TRPV1 的克隆 — 辣椒素受体即有害热受体（thermoception）、
    TRPV1 敲除动物失去对有害热与辣椒素的敏感——因果闭环
08  TRP 超家族全景 — TRPM8（CMR1）检测薄荷醇与冷、TRPA1 检测芥子油（异硫氰酸烯丙酯）、
    TRP 通道检测一系列温度与化学刺激
09  结构时代 — 毒素调制通道的发现、跨物种通道的独特适应、多个通道冷冻电镜结构的解析
10  嘌呤能受体与药物转化 — P2Y（GPCR）与 P2X（配体门控）双类 pioneering 贡献、
    P2Y12 = 氯吡格雷等抗血小板药物的受体（心血管/卒中预防）、
    5HT3 受体克隆 = 昂丹司琼止吐靶点
11  2010 Shaw → 2020 Kavli → 2021 Nobel — Shaw Prize（离子通道与伤害感受）、
    2020 Kavli 神经科学奖与 Patapoutian 共享（诺奖前奏）、2021 两人共享诺奖
12  荣誉序列 — Perl-UNC 首奖 2000、Alden Spencer 2007、Axelrod Prize 2007、
    Gairdner 2017、Prince/Princess of Asturias 2010、Breakthrough 2020、
    UCSF Medal 2022、Bonica Award 2023、SOT 荣誉会员 2025
13  Annual Review of Physiology 主编 (2007–2020) — 学术服务与 UCSF 讲席教授
14  遗产 — 从"辣为什么疼"到疼痛医学的分子坐标、
    慢性疼痛治疗的受体靶点版图、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方逐字 "for the discovery of receptors for temperature and touch"（与 Patapoutian 两人共享） |
| 双导师 | 博士系 **Thorner 与 Schekman 联合指导**（"under joint supervision"）——两条 advisor 边都要；Schekman 2013 诺奖、Axel 2004 诺奖——"诺奖师门"可点一句但不喧宾 |
| TRPV1 双重身份 | 检测辣椒素 **且** 检测有害热（thermoception）——两层都要写；敲除动物证据勿漏 |
| TRPM8/TRPA1 分工 | TRPM8=薄荷醇+冷；TRPA1=芥子油（allyl isothiocyanate）——勿互换 |
| 药物转化 | P2Y12→氯吡格雷（抗血小板）；5HT3→昂丹司琼（止吐）——两例都 page.md 明载，是"基础到药物"亮点；注意拼写 page.md 作 "ondansentron"（正文拼写），规范药名 ondanse**t**ron 可在术语表注明 |
| Kavli 前奏 | 2020 Kavli 神经科学奖系**与 Patapoutian 共享**——先于诺奖的合作者交集，勿写成单独获奖 |
| 兴趣起源 | psilocybin/LSD 兴趣引向受体研究（page.md 明载）——作为问题意识叙事，客观一句、勿渲染药物细节 |
| 出生地点 | 纽约布鲁克林 Brighton Beach（俄裔犹太社区）——精确到街区 |
| 在世者关系 | relations=5 为诚实值；与 Patapoutian 无合作论文记载，仅 co-honored 边 |
| editor 职务 | Annual Review of Physiology 主编 2007-2020——年份勿错 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| TRPV1 | 辣椒素受体/瞬态受体电位香草酸亚型 1 | 1997 克隆 |
| capsaicin | 辣椒素 | "热"的化学载体 |
| thermoception | 温度感觉 | TRPV1 的第二重身份 |
| TRPM8 (CMR1) | 薄荷醇受体 | 冷与薄荷醇 |
| TRPA1 | 芥子油受体 | 异硫氰酸烯丙酯 |
| nociception | 伤害感受 | 痛觉的科学术语 |
| P2Y12 | 嘌呤能受体 P2Y12 | 氯吡格雷靶点 |
| cryo-EM | 冷冻电镜 | 通道结构解析手段 |
| Kex2 | Kex2 蛋白酶 | 博士阶段发现 |
| proprotein convertase | 前蛋白转化酶 | Kex2 所属家族 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Timeless**（manifest 预分配）
- **风格**：沉稳 / 纪录片 / 长期纲领
- **匹配理由**：从酵母分泌通路到痛觉受体版图，Julius 的三十余年是"一个问题问到底"的长程纲领；Timeless 的沉稳纪录片感匹配"好奇心驱动的长期主义"——从 Kex2 到 TRP 家族再到冷冻电镜结构，一以贯之。
- **本地路径**：`music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav` → 复制为 `presentations/21th_century/David_Julius/Timeless.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；双导师与药物转化两例务必精确。**
