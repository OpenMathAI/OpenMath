# 医学家立传提示词（Rolf M. Zinkernagel）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1996 年得主 Rolf M. Zinkernagel（罗尔夫·马丁·青克纳格尔）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Rolf_M._Zinkernagel/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Rolf Martin Zinkernagel（1944-01-06 生于瑞士 Riehen（巴塞尔州），在世）
- **气质关键词**：**MHC 限制性识别的发现者、瑞士第 24 位诺奖得主、抗病毒免疫原则的确立者**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1996 条目，与 Peter C. Doherty 共享同一理由）：
  > "for their discoveries concerning the specificity of the cell mediated immune defence"（因他们发现细胞介导免疫防御的特异性）
- **设计母题**：**MHC I 限制性识别**——杀伤性 T 细胞只认"自体旗帜 + 病毒战利品"的组合：以旗帜与战利品并列出示的图案作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Rolf_M._Zinkernagel/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；第 0/1/2/3 步按 medic 路径执行：页面已在 `medic/presentations/pages/20th_century/Rolf_M._Zinkernagel/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Rolf_M._Zinkernagel_zh`、`VIDEO_NAME=Rolf_M._Zinkernagel_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | immunology | 免疫学 | infobox Fields；细胞免疫识别 |
| 1 | cytotoxic T cells | 杀伤性 T 细胞 | Known for 明载 |
| 2 | virology | 病毒学 | LCMV 等病毒免疫控制 |
| 3 | major histocompatibility complex | 主要组织相容性复合体 | MHC I 限制性识别 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Peter C. Doherty | 无向 | John Curtin 医学研究院（ANU）同事，LCMV 双重识别合作 |
| co-honored | Peter C. Doherty | 无向 | 1996 诺贝尔生理学或医学奖共享（细胞介导免疫防御的特异性） |

**在世者关系极少为诚实值**（2 条）：page.md 未载博士导师（巴塞尔 MD 1970、ANU PhD 1975 论文 H-2 基因复合体但导师未载）、未载配偶——Review 勿补造边；提示词注明防 Review 误判。**不入库但提示词可叙述**：Cancer Research Institute 科学顾问委员会等院士/会员（机构角色）；Coley 奖 1987 等纯奖项。

## 五、配色方案 【人物专属】

- **气质**：瑞士的精确、临床医生的克制、免疫前线的锋利
- **主色**：`#123C5B`（莱茵深蓝——巴塞尔与苏黎世的学术底色）+ 香槟金诺奖色
- **badge 四分类色**：`badgeMHCI` MHC I 限制 深蓝 `#123C5B`；`badgeCTL` 杀伤性 T 细胞 青绿 `#0E7C7B`；`badgeLCMV` 病毒免疫 琥珀 `#C07A2A`；`badgeUZH` 苏黎世大学 玫瑰 `#A63A2B`
- **背景母题**：旗帜与战利品并列出示的图案，呼应「MHC I 限制性识别」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — MHC 限制性识别的发现者 / Rolf M. Zinkernagel 1944– + 四色 badge + 右上头像 + 国籍行（Switzerland）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1944-01-06 Riehen、巴塞尔大学 MD 1970、
    ANU PhD 1975、苏黎世大学实验免疫学教授、诺奖 1996）
03  核心贡献概览 — 双重识别 / MHC I 限制 / 抗病毒免疫原则 / 免疫记忆
04  巴塞尔与医学 (1944–1970) — Riehen 少年、巴塞尔大学 MD 1970
05  澳洲深造 (1970–1975) — ANU John Curtin 医学研究院、博士论文：
    H-2 基因复合体在病毒与细菌感染细胞免疫中的作用（1975）
06  堪培拉与 Doherty 相遇（核心贡献页）— 与 Doherty 在 John Curtin 合作；
    LCMV 感染小鼠的杀伤性 T 细胞研究
07  双重识别的发现（核心贡献页）— 杀伤性 T 细胞须同时识别病毒抗原与
    自体 MHC I——T 细胞受体介导
08  MHC 的身份翻转 — 从移植排斥分子到抗病毒免疫中枢；
    MHC I 限制性识别确立抗病毒免疫关键原则
09  苏黎世大学 — 实验免疫学教授；免疫记忆与病毒免疫的长期研究
10  1996 诺奖 — 与 Doherty 共享；Nobel 讲演 "Cellular Immune Recognition and the
    Biological Role of Major Transplantation Antigens"（1996-12）；第 24 位瑞士诺奖得主
11  荣誉与认可 — Cloëtta 1981、Ernst Jung 1982、Erlich-Darmstaedter 1983、
    Mack-Forster 1985、Coley 1987、Naegeli 1988、Gairdner 1986、Louis-Jeantet 1988、
    Lasker 1995、Nobel 1996、荣誉 AC 1999、ForMemRS
12  学术身份 — 澳科院通讯院士 1996、Leopoldina 1994、AAAS/NAS/美国哲学会/
    癌症免疫学院成员；CRI 科学顾问委员会
13  双重荣誉 — 澳大利亚荣誉 AC（1999，因其与 Doherty 的科学工作）——
    瑞士人获澳洲最高平民荣誉的佳话
14  遗产与结尾 — MHC 限制：从移植排斥到抗病毒免疫到肿瘤免疫的统一语言
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 师承为零 | 巴塞尔 MD 1970 与 ANU PhD 1975 均未载导师姓名（博士论文题目载但导师无）——师承边为零是诚实值，勿补造 |
| 关系极少 | 仅 2 条（Doherty colleague+co-honored）——page.md 极简（59 行），在世者诚实值；勿从诺奖官网/他处补边 |
| 双重识别 | 与 Doherty 篇同一发现的两面：杀伤性 T 细胞须同时识别病毒抗原+自体 MHC I——表述一致 |
| 论文题目 | ANU 博士论文 "The role of the H-2 gene complex in cell-mediated immunity to viral and bacterial infections in mice"（1975）——H-2 即小鼠 MHC，诺奖工作伏笔 |
| 第 24 位瑞士诺奖得主 | page.md 明载口径，可写 |
| 荣誉 AC | 1999 获澳大利亚荣誉 Companion of the Order of Australia（非公民获荣誉）——瑞士人获澳洲最高平民荣誉，注意"荣誉（honorary）"性质 |
| 在世者生卒 | frontmatter 双值取正文 1944-01-06；无卒年——封面 1944– 开放区间 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| MHC I restriction | MHC I 限制性识别 | 获奖核心原则 |
| cytotoxic T cell | 杀伤性 T 细胞 | Known for 主体 |
| dual recognition | 双重识别 | 病毒肽 + 自体 MHC I |
| H-2 complex | H-2 基因复合体 | 小鼠 MHC（博士论文主题） |
| LCMV | 淋巴细胞性脉络丛脑膜炎病毒 | 研究模型 |
| transplantation antigens | 移植抗原 | MHC 的旧身份 |
| University of Zurich | 苏黎世大学 | 长期教职 |
| immunological memory | 免疫记忆 | 其长期研究方向 |
| Riehen | 里亨 | 出生镇（巴塞尔州） |
| honorary AC | 荣誉澳大利亚勋衔 | 1999 非公民荣誉 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Cinematic Experience**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：瑞士青年医师远赴堪培拉、与澳洲搭档在 LCMV 模型上共同改写免疫学教科书——"Cinematic Experience" 匹配这场跨国合作的戏剧弧光与 MHC 身份翻转的史诗感。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Rolf_M._Zinkernagel/Cinematic_Experience.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
