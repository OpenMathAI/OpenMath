# 医学家立传提示词（Gertrude B. Elion）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1988 年得主 Gertrude B. Elion（格特鲁德·贝勒·埃利恩）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Gertrude_B._Elion/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Gertrude "Trudy" Belle Elion（1918-01-23 生于纽约 ~ 1999-02-21 逝于北卡罗来纳州教堂山，享年 81 岁），美国生物化学家与药理学家，ForMemRS，史上第五位医学诺奖女性
- **气质关键词**：**理性药物设计的先驱、嘌呤之路的开拓者、从被拒到诺奖的女性科学家**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1988 条目，Black/Elion/Hitchings 三人共享）：
  > "for their discoveries of important principles for drug treatment"（因其关于药物治疗重要原理的发现）
- **设计母题**：**以假乱真的嘌呤（antimetabolite）**——设计与天然化合物相似的人工分子，"欺骗"癌细胞将其纳入生长通路；用「真假嘌呤分子并列」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Gertrude_B._Elion/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；第 0/1/2/3 步按 medic 路径执行：页面已在 `medic/presentations/pages/20th_century/Gertrude_B._Elion/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Gertrude_B._Elion_zh`、`VIDEO_NAME=Gertrude_B._Elion_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Elion 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | pharmacology | 药理学 | metadata field_of_work 明载 | 全篇 |
| 1 | rational drug design | 理性药物设计 | 与 Hitchings 共同开创，1988 诺奖核心 | 核心页 |
| 2 | biochemistry | 生物化学（嘌呤抗代谢物） | 6-MP/硫鸟嘌呤的合成路线 | 核心页 |
| 3 | chemotherapy | 化学治疗（抗白血病/抗病毒） | AZT、阿昔洛韦等 | 药物页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | George H. Hitchings | 对方 → 导师 | 1944 年起为其研究助理，理性药物设计路线的合作开创者（无正式博士项目） |
| co-honored | George H. Hitchings | 无向 | 1988 诺贝尔生理学或医学奖三人共享 |
| co-honored | James W. Black | 无向 | 1988 同届诺奖三人共享（Black 的β受体阻滞剂/西咪替丁路线） |

**诚实值说明**：Elion 终生未婚、page.md 无其他具名私人/科研关系，relations=3 为诚实值；杜克大学指导的医学生与研究生（25+ 篇合著论文）未具名，不入库。

**不入库但提示词可叙述**：未婚夫 Leonard Canter（CCNY 统计学学生，1941-06-25 死于细菌性心内膜炎——其诺奖访谈自述此举坚定了从研决心，非 spouse 边）；父母 Robert Elion（立陶宛犹太移民牙医）与 Bertha Cohen（波兰犹太移民）。

## 五、配色方案 【人物专属】

- **气质**：被拒十五次仍前行的韧性、嘌呤分子的简洁、教堂山晚年的澄澈
- **主色**：`#52307C`（药紫——合成分子与女性科学家的锋芒）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgePurine` 嘌呤抗代谢物 — 药紫 `#52307C`
  - `badgeRational` 理性设计 — 深蓝 `#1E4E79`
  - `badgeAZT` AZT 与抗病毒 — 暗红 `#8C2F1B`
  - `badgeWomen` 女性科学家 — 赭金 `#B07D2B`
- **背景母题**：真假嘌呤分子并列与培养皿剪影，稀疏排布。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 理性药物设计的先驱 / Gertrude B. Elion 1918–1999 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、纽约出身、Hunter College/NYU 硕士、
    Burroughs-Wellcome/杜克任职、诺奖 1988、核心领域；"无博士学位的诺奖得主"注脚）
03  核心贡献概览 — 6-MP 与硫鸟嘌呤 1950 / 硫唑嘌呤 / 阿昔洛韦 / AZT
04  大萧条中的神童 (1918–1937) — 15 岁中学毕业、祖父胃癌离世立志医学、Hunter 免费+summa cum laude
05  性别之墙 (1937–1944) — 15 份助学金申请因性别被拒、秘书/中学教师/腌菜酸度与蛋黄酱蛋黄测色、
    J&J 缝线强度测试、夜校 NYU 硕士 1941
06  1944：加入 Hitchings 实验室 — Wellcome 研究实验室、以天然化合物为蓝本的设计哲学、
    核酸衍生物拮抗剂
07  1950：6-巯基嘌呤与硫鸟嘌呤（核心贡献页）— 首个白血病有效治疗药物
08  药物谱系 — 硫唑嘌呤（首个免疫抑制药，器官移植）/ 别嘌醇（痛风）/ 乙胺嘧啶（疟疾）/
    甲氧苄啶（脑膜炎败血症）/ 阿昔洛韦（首个选择性抗病毒药，疱疹）
09  AZT 与 nelarabine — 首个广泛用于艾滋病的药物 AZT、逝世前仍在推进的 nelarabine
10  1988 诺奖：三人共享 — 与 Hitchings（44 年搭档）、Black（β阻滞剂路线）共享，获奖理由逐字呈现；
    第五位医学诺奖女性、当年唯一女性得主、少数无博士学位得主
11  杜克岁月 (1971–1999) — 兼职教授→研究教授、指导医学生与研究生发表 25+ 篇论文、
    鼓励女性投身科学
12  荣誉与认可 — Garvan-Olin 1968、NMS 1991、Lemelson-MIT 1997、首个入选发明家名人堂的女性（1991）、
    NAS 1990/IOM 1991/AAAS 1991、ForMemRS 1995
13  个人的代价与选择 — 未婚夫 Canter 1941 病逝坚定从研决心（诺奖访谈自述）、终生未婚、
    摄影旅行歌剧芭蕾
14  遗产与结尾 — 理性设计取代试错、现代药物研发的范式转移 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 姓名口径 | **yaml/入库用 manifest 形式 "Gertrude B. Elion"**；昵称 Trudy、全名 Gertrude Belle Elion |
| 1988 三人结构 | Black（β受体阻滞剂 propranolol 与抗溃疡药 cimetidine 的路线）/ Elion+Hitchings（理性设计）——同一句获奖理由，三人贡献各述；Elion 与 Hitchings 是 44 年搭档，Black 是同届另一路线 |
| "导师"边性质 | Hitchings 是其 1944 年起的实验室领导与研究导师（frontmatter doctoral_advisor 明载），但**两人之间没有正式博士项目**（她为保工作放弃博士）——advisor-student 边 note 已注明，勿写成"博士导师" |
| 无 PhD 口径 | 放弃博士（兼职读博被要求转全职时选择工作）；1989 Tandon 荣誉 PhD、1998 哈佛荣誉 S.D.——"荣誉学位"勿写成正式学位 |
| AZT 表述 | AZT 是"她发挥重要作用 developed"（page.md 口径 played a significant role），团队成果，勿写成独力发明；其用于艾滋病的时间在她退休后 |
| 性别歧视细节 | 15 份申请被拒、Hunter 免费教育（诺奖访谈自述归因）、腌菜/蛋黄/缝线的打工清单——反差叙事主线，均可写 |
| 感情线 | 未婚夫 Leonard Canter 1941 年病逝——诺奖访谈自述坚定其科研决心；终生未婚未育——**不建 spouse 边**（未成婚），只叙述 |
| 引语红线 | 诺奖访谈两句（Hunter 免费教育、未婚夫之死与从研决心）为访谈转述，page.md 未载英文原文——**用忠实转述，勿加引号直引** |
| 荣誉年份链 | Garvan-Olin 1968、Judd 1983、ACS 杰出化学家+Cain 1985、Golden Plate 1989、ACS 荣誉勋章 1990、NAS 1990、NMS+发明家名人堂+IOM+AAAS 1991、女性名人堂 1991、工程科学名人堂 1992、Lemelson-MIT 1997、ForMemRS 1995——1991 年四项勿漏勿串 |
| 职年链 | 1967-1983 实验治疗部主任、1983 退休、杜克兼职教授 1971-83→研究教授 1983-99——退休后仍"几乎全职"工作，勿写成完全退休 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| important principles for drug treatment | 药物治疗的重要原理 | 获奖理由逐字对应 |
| rational drug design | 理性药物设计 | 相对于 trial-and-error |
| antimetabolite | 抗代谢物 | 以假乱真的核苷酸类似物 |
| purine derivatives | 嘌呤衍生物 | 早期工作的化学基础 |
| mercaptopurine (6-MP) | 6-巯基嘌呤 | 1950，首个白血病治疗 |
| azathioprine (Imuran) | 硫唑嘌呤 | 首个免疫抑制药 |
| acyclovir (Zovirax) | 阿昔洛韦 | 首个选择性有效抗病毒药 |
| zidovudine (AZT) | 齐多夫定（AZT） | 首个广泛抗艾滋病药物 |
| allopurinol | 别嘌醇 | 痛风用药 |
| nelarabine | 奈拉滨 | 逝世前仍在推进的抗癌药 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Pathfinder**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：在"女人做不了科学"的年代，Elion 自己凿出一条路——15 次被拒后走进 Wellcome 实验室，再用"理性设计"为整个制药业开路；Pathfinder 的开拓感对应她从被拒者到开宗立派者的一生，也对应每一颗"先理解靶点再设计分子"的新药背后那条她踩出的路径。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Gertrude_B._Elion/Pathfinder.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
