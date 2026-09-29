# 医学家立传提示词（Archibald Hill）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1922 年得主 Archibald Hill（阿奇博尔德·希尔）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Archibald_Hill/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Archibald Vivian Hill（1886-09-26 生于布里斯托 ~ 1977-06-03 逝于剑桥，享年 90 岁），通称 **A. V. Hill**
- **气质关键词**：**肌肉热学的测量者、生物物理学奠基人、营救学者的议员**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1922 条目，Hill 半边口径）：
  > "for his discovery relating to the production of heat in the muscle"（因其关于肌肉产热的发现）
- **设计母题**：**收缩中的热与功（heat & work in contracting muscle）**——肌肉收缩时产热（需耗化学能）、舒张时不产热（被动过程），用「0.003 °C 的温度攀升曲线」作背景母题：极细的量热曲线与力—速度双曲线交织。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Archibald_Hill/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/20th_century/Archibald_Hill/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Archibald_Hill_zh`、`VIDEO_NAME=Archibald_Hill_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Hill 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | physiology | 生理学 | 肌肉产热测量，1922 诺奖核心 | 封面、核心页 |
| 1 | biophysics | 生物物理学 | 与 Helmholtz 并列的奠基人之一 | 核心页 |
| 2 | muscle physiology | 肌肉生理学 | Hill equation / Hill's model / 力—速度关系 | 核心页 |
| 3 | operations research | 运筹学 | 一战反飞机实验组 "Hill's Brigands"，学科奠基人之一 | 战时页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Walter Morley Fletcher | 对方 → 导师 | frontmatter/infobox Academic advisors 明载 |
| advisor-student | John Newport Langley | 对方 → 指导教师 | 本科阶段首篇论文（1909 受体理论/Langmuir 方程）在其指导下完成 |
| co-honored | Otto Fritz Meyerhof | 无向 | 1922 诺贝尔生理学或医学奖共享（Hill 肌肉产热 / Meyerhof 氧耗—乳酸代谢，工作平行独立） |
| spouse | Margaret Neville Keynes | 无向 | 1913 结婚（1885–1974），经济学家 John Neville Keynes 之女 |
| advisor-student | Te-Pei Feng | Hill → 学生 | infobox Notable students 明载（冯德培） |
| advisor-student | Ralph H. Fowler | Hill → 学生 | infobox Notable students 明载；亦为一战 "Hill's Brigands" 成员（库内 id=2039） |
| advisor-student | Bernard Katz | Hill → 学生 | infobox Notable students 明载 |
| parent-child | David Keynes Hill | Hill → 子 | 1915–2002，生理学家 |
| parent-child | Maurice Hill | Hill → 子 | 1919–1966，海洋学家/地球物理学家 |
| colleague | Ernest Rutherford | 无向 | 1933 与其共同创立 Academic Assistance Council（救援受迫害学者；库内 id=2030） |
| colleague | William Beveridge | 无向 | 1933 共同创立 Academic Assistance Council，Hill 任副主席（新建 stub） |

**不入库但提示词可叙述**：John Maynard Keynes / Geoffrey Keynes（妻之兄弟，姻亲不入 spouse/parent-child 白名单类型）；女儿 Polly Hill（经济学家）/ Janet Hill；孙 Nicholas Humphrey；一战实验组成员 Douglas Hartree / Arthur Milne / James Crowther（团队事件，Fowler 已以学生边承载）；Magnus Blix（留下设备的瑞典生理学家，仅物件渊源）；Hermann Helmholtz（"并列为生物物理奠基人"的比较，非关系）；William Stirling / Ernest Starling（教席前后任）；Horace Darwin（军需部委托人）；Patrick Blackett / Henry Tizard（雷达委员会）。

## 五、配色方案 【人物专属】

- **气质**：英式克制、量热计的毫度精进、剑桥的三一蓝
- **主色**：`#37474F`（蓝灰——量热计金属与三一学院石墙）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeHeat` 肌肉产热 — 蓝灰 `#37474F`
  - `badgeBio` 生物物理 — 深青 `#0F4C5C`
  - `badgeWar` 战时科学 — 军绿 `#37543C`
  - `badgeRef` 营救学者 — 暗红 `#8B1A1A`
- **背景母题**：极小温升（0.003 °C）的量热曲线与肌肉力—速度双曲线，两种细线交织。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 肌肉热学的测量者 / A. V. Hill 1886–1977 + 四色 badge + 右上头像 + 国籍行（United Kingdom）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、布里斯托出身、剑桥三一学院数学 Tripos 第三名、
    曼彻斯特/剑桥/UCL 任职、诺奖 1922、核心领域）
03  核心贡献概览 — 肌肉产热 / Hill equation / 生物物理奠基 / 运筹学先声
04  布里斯托与三一学院 (1886–1909) — Blundell's School；数学 Tripos 第三 wrangler；1909 Langmuir 方程
05  Langley 与受体理论 — 首篇论文：烟碱与箭毒结合「受物质」，受体理论里程碑
06  Hill equation (1910)（核心贡献页）— 氧与血红蛋白结合的量化方程；h 系数与正/负协同
07  肌肉产热的测量 — 继承 Blix 的设备；0.003 °C 温升；热电偶持续改良
08  收缩产热、舒张不产热 — 化学能投入在收缩相；与德国同行的互访
09  一战与 "Hill's Brigands" — 反飞机实验组：双镜测高、射程表；Fowler/Hartree/Milne；OBE
10  曼彻斯特与自身实验 (1920–1922) — 每晨 7:15–10:30 自我测试；VO2 max 与氧债概念 1922 提出
11  1922 诺奖：与 Meyerhof 各自平行 — Hill 产热 / Meyerhof 氧耗—乳酸；共享而工作互不隶属
12  UCL 岁月与营救学者 (1923–1951) — 继 Starling 教席；1933 AAC 与 Beveridge/Rutherford；救下 900 学者
13  二战与议员 — 雷达委员会；1940–45 剑桥大学选区独立 MP；驻华盛顿促科学共享
14  遗产与结尾 — 生物物理系 1951 / Hill equation / 运动医学 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 姓名形式 | 全名 Archibald Vivian Hill，通称 A. V. Hill；**yaml/入库用 manifest 形式 "Archibald Hill"**，封面与正文可写 A. V. Hill |
| 1922 共享的结构 | 与 Meyerhof 共享，但**两人工作平行独立**（Hill 产热/热量学，Meyerhof 氧耗与乳酸代谢），勿写师承或合作；获奖理由也各有一句，Hill 半边是 "for his discovery relating to the production of heat in the muscle" |
| 两条师承并存 | 博士/学术导师 **Fletcher**（frontmatter+infobox）；首篇论文（1909 受体理论）由 **Langley** 指导——两条 advisor-student 边并行，勿合并成一人 |
| Hill equation 的 h | h 表达偏离 Michaelis–Menten 动力学的程度；**Hill 本人反对把 h 解读为结合位点数目**——page.md 明载，Review 勿"补充"位点数解读 |
| Langmuir 方程归属 | 1909 他推得的是"后来被称为 Langmuir 方程"的形式——写"Hill 1909 年导出，后以 Langmuir 命名"，勿写成 Hill 方程的前身混淆 |
| Keynes 姻亲 | 妻 Margaret Neville Keynes 是经济学家 John Neville Keynes 之女、John Maynard Keynes 与外科医生 Geoffrey Keynes 之妹——姻亲不入库（无对应白名单类型），只叙述 |
| 玩具摆件轶事 | UCL 实验室陈列挥手玩具希特勒以"感谢德国驱逐的科学家"——史实敏感，建议弱化，或以引语 "Laughter is the best detergent for nonsense"（page.md 明载）替代 |
| 两段战时 | 一战 "Hill's Brigands"（反飞机射击法/射程表，OBE）与二战（雷达诞生委员会、驻华盛顿、救犹太学者、1940-45 独立议员、印度之行影响 IIT 创立）——两段勿混 |
| Rutherford 称谓 | page.md 作 "Lord Rutherford"；库内规范名 **Ernest Rutherford**（id=2030），yaml 用库内名 |
| 死亡地 | 1977-06-03 逝于剑桥；Highgate 蓝牌故居（1923–1967 住）勿写成死亡地 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| production of heat in the muscle | 肌肉产热 | 获奖理由核心词，逐字对应 |
| Hill equation | Hill 方程 | 生化结合/协同量化，h 系数 |
| Hill plot | Hill 图 | ln 变换直线图 |
| maximal oxygen uptake (VO2 max) | 最大摄氧量 | 1922 提出 |
| oxygen debt | 氧债 | 1922 提出，与运动后过量氧耗关联 |
| myothermic | 肌热量法的 | 其装置命名 |
| thermocouple | 热电偶 | 测 0.003 °C 温升的关键器件 |
| wrangler | Tripos 榜次 | 数学荣誉学位考试名次（第三名） |
| operations research | 运筹学 | 战时反飞机问题孕育的学科 |
| Academic Assistance Council | 学术援助理事会 | 1933 创立，后更名 SPSL，救 900 学者 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Winds Of Freedom**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Hill 的一生两度以科学服务自由——一战造射程表、二战救出 900 名受纳粹迫害的学者并促成盟国科学共享，"自由之风"正是 Academic Assistance Council 与驻华盛顿使命的注脚；开阔的旋律也对应其从量热计毫度到国会议席的宽广人生。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Archibald_Hill/WindsOfFreedom.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
