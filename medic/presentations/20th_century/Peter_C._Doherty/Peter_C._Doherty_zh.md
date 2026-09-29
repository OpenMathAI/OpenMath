# 医学家立传提示词（Peter C. Doherty）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1996 年得主 Peter C. Doherty（彼得·查尔斯·多尔蒂）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Peter_C._Doherty/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Peter Charles Doherty（1940-10-15 生于澳大利亚布里斯班，在世）
- **气质关键词**：**MHC 双重识别的发现者、兽医出身的免疫学家、科学的公共写作者**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1996 条目，与 Rolf M. Zinkernagel 共享同一理由）：
  > "for their discoveries concerning the specificity of the cell mediated immune defence"（因他们发现细胞介导免疫防御的特异性）
- **设计母题**：**双重钥匙孔（MHC I + 病毒肽）**——杀伤性 T 细胞须同时认出病毒肽与自体 MHC I 的意象：以双钥匙孔对应锁芯的图案作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Peter_C._Doherty/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；第 0/1/2/3 步按 medic 路径执行：页面已在 `medic/presentations/pages/20th_century/Peter_C._Doherty/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Peter_C._Doherty_zh`、`VIDEO_NAME=Peter_C._Doherty_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | immunology | 免疫学 | infobox Fields；T 细胞与 MHC |
| 1 | medicine | 医学 | infobox Fields；兽医起步 |
| 2 | virology | 病毒学 | LCMV 小鼠模型、病毒免疫 |
| 3 | major histocompatibility complex | 主要组织相容性复合体 | MHC I 限制性识别 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | G. L. Montgomery | 对方 → 导师 | 爱丁堡大学博士导师之一（1970 病理学博士，louping-ill 脑炎实验病理） |
| advisor-student | J. T. Stamp | 对方 → 导师 | 爱丁堡大学博士导师之二（infobox Doctoral advisor 并列） |
| spouse | Penelope Stephens | 无向 | 微生物学研究生，1965 结婚；二子 Michael（神经科医师）与 James（律师） |
| colleague | Rolf M. Zinkernagel | 无向 | John Curtin 医学研究院同事（LCMV 双重识别合作） |
| co-honored | Rolf M. Zinkernagel | 无向 | 1996 诺贝尔生理学或医学奖共享（细胞介导免疫防御的特异性） |

**在世者关系少为诚实值**（5 条）。**不入库但提示词可叙述**：Sharon Lewin（Doherty 研究所所长，机构叙述）；父母 Eric 与 Linda（家世叙述）；2020 COVID 期间"Dan Murphy opening hours"误发推特的走红轶事（page.md 明载，轻松一笔）。

## 五、配色方案 【人物专属】

- **气质**：澳洲阳光的坦率、兽医的临床触感、免疫战线的机敏
- **主色**：`#2A4B7C`（昆士兰海蓝——布里斯班到孟菲斯的免疫战场）+ 香槟金诺奖色
- **badge 四分类色**：`badgeMHC` MHC 双重识别 海蓝 `#2A4B7C`；`badgeTcell` 杀伤性 T 细胞 青绿 `#0E7C7B`；`badgeLCMV` LCMV 模型 琥珀 `#C07A2A`；`badgeVet` 兽医出身 玫瑰 `#A63A2B`
- **背景母题**：双钥匙孔对应锁芯的图案，呼应「双重钥匙孔」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — MHC 双重识别的发现者 / Peter C. Doherty 1940– + 四色 badge + 右上头像 + 国籍行（Australia）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1940-10-15 布里斯班、昆士兰大学兽医
    1962/硕士 1966、爱丁堡 PhD 1970、John Curtin/St. Jude、诺奖 1996）
03  核心贡献概览 — 双重识别 / MHC I 限制 / LCMV 模型 / 免疫防御的特异性
04  昆士兰少年 (1940–1962) — Sherwood 长大、Indooroopilly 高中（今有以其名命名的讲堂）、
    昆士兰大学兽医学士 1962
05  乡村兽医与转轨 (1962–1966) — 昆州农业与畜牧部乡村兽医官、动物研究所实验室工作、
    遇微生物学研究生 Penelope Stephens（1965 结婚）、硕士 1966
06  爱丁堡博士 (1966–1970) — Montgomery 与 Stamp 双导师、louping-ill 脑炎实验病理
07  堪培拉 John Curtin (1970–) — 回澳加入 ANU John Curtin 医学研究院；Zinkernagel 到来
08  LCMV 双重识别（核心贡献页）— 杀伤性 T 细胞须同时识别(i)病毒肽抗原与
    (ii)自体 MHC I 分子——T 细胞受体介导的双重识别
09  MHC 的身份翻转（核心贡献页）— MHC 从"移植排斥元凶"到"抗病毒免疫中枢"——
    脑膜炎病毒免疫控制的关键原则
10  St. Jude 岁月 (1988–2001) — 孟菲斯圣犹大儿童研究医院免疫学系主任
11  双城生活与 Doherty 研究所 — 每年 3 个月 St. Jude/9 个月墨尔本大学；
    2014 运营的 Peter Doherty Institute（墨大+墨尔本健康联合体，所长 Sharon Lewin）
12  荣誉与认可 — FAA 1983、FRS 1987、Erlich-Darmstaedter 1983、Lasker 1995、
    Nobel 1996、Australian of the Year 1997、AC 勋衔 1997、国家活宝库、
    Leeuwenhoek 讲座 1999、Q150 Icons 2009
13  科普写作八部 — The Beginner's Guide to Winning the Nobel Prize (2006)、
    Sentinel Chickens、The Knowledge Wars、Pandemics、An Insider's Plague Year (2021) 等
14  遗产与结尾 — T 细胞免疫的双钥匙原则：从基础免疫到疫苗与肿瘤免疫的时代
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 双博士导师 | infobox Doctoral advisor 并列 **G. L. Montgomery 与 J. T. Stamp**（爱丁堡）——两条师承边 |
| 兽医出身 | 昆士兰大学兽医科学学士 1962 + 兽医科学硕士 1966；PhD 是**病理学**（爱丁堡 1970）——三个学位学科勿混 |
| 双重识别表述 | T 细胞须同时识别(i)病毒肽抗原与(ii)自体 MHC I；由 T 细胞受体介导——"dual recognition" 逻辑勿写反 |
| MHC 身份翻转 | MHC 先前已知与移植排斥相关，Doherty/Zinkernagel 发现其与抗病毒免疫（脑膜炎病毒）相关——"身份翻转"是叙事亮点 |
| LCMV | 淋巴细胞性脉络丛脑膜炎病毒小鼠研究是"landmark studies"——体系名与物种勿错 |
| 推特轶事 | 2020 误发 "Dan Murphy opening hours"（本想搜索酒类商店营业时间）意外走红——page.md 明载可用轻松一笔，勿引申 |
| 在世者生卒 | 仅生年 1940-10-15（page.md 显示 age 85），无卒年——封面 1940– 开放区间 |
| 妻子姓名 | 婚前 Penelope Stephens、婚后称 Penny——yaml 用 Penelope Stephens |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| cell mediated immune defence | 细胞介导免疫防御 | 获奖理由核心词 |
| MHC class I | MHC I 类分子 | 双重识别的自体分子 |
| cytotoxic T cell | 杀伤性 T 细胞 | 识别感染靶细胞 |
| T-cell receptor | T 细胞受体 | 双重识别的介导者 |
| LCMV | 淋巴细胞性脉络丛脑膜炎病毒 | 标志性小鼠模型 |
| viral peptide antigen | 病毒肽抗原 | 双重识别的外来分子 |
| John Curtin School of Medical Research | 约翰·柯廷医学研究院 | ANU；诺奖工作地 |
| St. Jude Children's Research Hospital | 圣犹大儿童研究医院 | 孟菲斯 1988–2001 |
| Doherty Institute | 多尔蒂研究所 | 2014 运营 |
| Australian of the Year | 年度澳大利亚人 | 1997 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Eternals**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：从兽医到诺奖得主再到全球公卫的公共写作者——Doherty 的工作定义了免疫识别的恒久原则；"Eternals" 的宏大感对应 T 细胞双重识别这一跨越时代的免疫学基石。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Peter_C._Doherty/Eternals.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
