# 医学家立传提示词（César Milstein）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1984 年得主 César Milstein（塞萨尔·米尔斯坦）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/César_Milstein/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：César Milstein（1927-10-08 生于阿根廷 Bahía Blanca ~ 2002-03-24 逝于英国剑桥，享年 74 岁）
- **气质关键词**：**单克隆抗体之父、抗体亲和力成熟的阐释者、科学的普惠信念者**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1984 条目，与 Köhler 共享一半、Jerne 独享另一半）：
  > "for theories concerning the specificity in development and control of the immune system and the discovery of the principle for production of monoclonal antibodies"（因免疫系统发育与控制特异性的理论及单克隆抗体生产原理的发现）
  - Milstein 侧对应"单克隆抗体生产原理"（1975 杂交瘤技术）。
- **设计母题**：**亲和力的成熟（affinity maturation）**——体细胞超突变不断打磨抗体精度的意象：以渐次逼近靶心的突变箭簇图案作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/César_Milstein/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；第 0/1/2/3 步按 medic 路径执行：页面已在 `medic/presentations/pages/20th_century/César_Milstein/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=César_Milstein_zh`、`VIDEO_NAME=César_Milstein_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | immunology | 免疫学 | 抗体结构与多样性主线 |
| 1 | monoclonal antibodies | 单克隆抗体 | 1975 杂交瘤技术，1984 诺奖核心 |
| 2 | somatic hypermutation | 体细胞超突变 | 免疫球蛋白 V 基因突变与亲和力成熟 |
| 3 | antibody engineering | 抗体工程 | 重组 DNA 应用于单抗的治疗转化远见 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Andrés O.M. Stoppani | 对方 → 导师 | 布宜诺斯艾利斯大学生物化学教授、博士导师（酶动力学，1956 SAIB 奖） |
| advisor-student | Malcolm Dixon | 对方 → 导师 | 剑桥生化学系第二博士导师（1958 英国文化协会资助；磷酸葡萄糖变位酶金属激活）；库内规范名 id=4657 |
| colleague | Frederick Sanger | 无向 | 博士期间以短期 MRC 聘任加入其组合作；库内规范名 id=1122 |
| advisor-student | Georges J. F. Köhler | Milstein → 学生 | 其实验室博士后研究员（1974–76），杂交瘤共同发明人 |
| colleague | Leonard Herzenberg | 无向 | 1976–77 在其实验室休假期间创造 "hybridoma" 一词 |
| colleague | Claudio Cuello | 无向 | 合作奠基单抗作神经疾病病理通路探针与免疫诊断增强 |
| spouse | Celia Prilleltensky | 无向 | 1953 结婚；抗体氨基酸多样性早期工作部分与妻合作；妻 2020 逝 |
| co-honored | Georges J. F. Köhler | 无向 | 1984 诺贝尔生理学或医学奖共享一半（单克隆抗体生产原理） |
| co-honored | Niels Kaj Jerne | 无向 | 1984 诺贝尔生理学或医学奖（Jerne 独享一半为理论） |

**不入库但提示词可叙述**：父母 Lázaro（乌克兰犹太移民）与 Máxima（家世叙述）；Sociedad Argentina de Investigación en Bioquímica（1956 奖项事件）；UNESCO Finlay 奖等纯奖项；2010 纪录片《Un fueguito》（文化事件）。

## 五、配色方案 【人物专属】

- **气质**：流亡者的热忱、剑桥的严谨、普惠的信念
- **主色**：`#1B5E8C`（拉普拉塔河蓝——从布宜诺斯艾利斯到剑桥的科学航线）+ 香槟金诺奖色
- **badge 四分类色**：`badgeMab` 单克隆抗体 河蓝 `#1B5E8C`；`badgeAID` 亲和力成熟 玫瑰 `#9E2B25`；`badgeSignal` 信号肽发现 深蓝 `#1E4E79`；`badgeSouth` 南南科学 琥珀 `#C07A2A`
- **背景母题**：渐次逼近靶心的突变箭簇图案，呼应「亲和力的成熟」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 单克隆抗体之父 / César Milstein 1927–2002 + 四色 badge + 右上头像 + 国籍行（Argentina / United Kingdom）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1927-10-08 Bahía Blanca ~ 2002-03-24 剑桥、
    布宜诺斯艾利斯大学、剑桥 MRC LMB、FRS 1975、诺奖 1984）
03  核心贡献概览 — 杂交瘤技术 / 信号肽先行证据 / 体细胞超突变 / 抗体工程远见
04  巴伊亚布兰卡少年 (1927–1945) — 乌克兰犹太移民之子、布宜诺斯艾利斯大学
05  双站博士 (1945–1962) — Stoppani 门下酶动力学（醛脱氢酶，1956 SAIB 奖）、
    1958 英国文化协会资助赴剑桥、Dixon 门下磷酸葡萄糖变位酶、短期加入 Sanger 组
06  MRC LMB 与抗体多样性 — 抗体氨基酸层面多样性、二硫键（部分与妻 Celia 合作）、
    mRNA 信号肽的先行证据
07  1975：杂交瘤（核心贡献页）— 与博士后 Köhler 融合淋巴细胞与骨髓瘤细胞、
    Nature 论文；Herzenberg 休假期间命名 hybridoma
08  单抗技术的持续改进 — 细胞型标记单抗、与 Cuello 奠基神经病理探针与
    免疫诊断增强；专利布局（单抗生产等四项专利）
09  体细胞超突变与亲和力成熟（核心贡献页）— V 基因局部突变打磨抗体精度、
    保护性免疫与免疫记忆的贡献；临终前一周仍在投稿
10  抗体工程的远见 — 预见重组 DNA 应用于单抗、更安全强效的治疗性抗体
11  普惠科学的信念 — 页面引语 "Science will only fulfill its promises when the
    benefits are equally shared by the really poor of the world"（可引原文+译文）；
    帮助发展中国家科学家的长期投入
12  荣誉与认可 — FRS 1975、Horwitz 1980、Wolf 1980、Hardy/Krebs 1981、
    Franklin 1982、Finlay 1983、Nobel 1984、Copley 1989、CH 1995、
    Konex 钻石奖 1993
13  家庭与身后 — 1953 与 Celia Prilleltensky 结婚（科研搭档）；2002-03-24 剑桥
    心脏疾患辞世；妻 2020 逝；2010 纪录片 Un fueguito
14  遗产与结尾 — 从诊断试剂到抗体药物：单抗时代的全景
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 1984 两半结构 | Jerne 独享一半（理论）；Milstein+Köhler 共享另一半（杂交瘤单抗原理）——citation 合写一句，Milstein 篇侧重单抗原理与后续改进 |
| 双站博士 | 布宜诺斯艾利斯 PhD（Stoppani，酶动力学）+ 剑桥 PhD（Dixon，磷酸葡萄糖变位酶金属激活）——两站两导师两条边，勿合并 |
| Köhler 定位 | Köhler 是其实验室**博士后研究员**（1974–76）——学生边（postdoc 注记）+ co-honored 边；署名对等勿写成"导师成果" |
| hybridoma 命名 | 术语由 **Herzenberg** 创造（1976–77 休假于其实验室）——命名归 Herzenberg，技术归 Köhler/Milstein |
| 信号肽先行证据 | Milstein 提供分泌多肽前体含信号肽的首批证据——概念表述从简，信号肽假说的完整归属是 Blobel（1999），勿越界 |
| 专利 | Milstein 专利了单抗生产并另有三项专利——与"不图专利收益"的普惠叙事并置时按 page.md 措辞，勿编造专利争议 |
| 引语 | "Science will only fulfill its promises..." 为页面引语块明载，可引原文+译文；全文唯一可用引语 |
| 国籍 | 阿根廷出生、后获英国籍、双国籍（page.md 明载）——yaml 取 Argentina(0)+United Kingdom(1)，封面国籍行两写 |
| 卒因 | 长年心脏疾患，2002-03-24 逝于剑桥（74 岁） |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| hybridoma | 杂交瘤 | 命名者 Herzenberg |
| monoclonal antibody | 单克隆抗体 | 均一特异性抗体 |
| somatic hypermutation | 体细胞超突变 | V 基因局部突变 |
| affinity maturation | 亲和力成熟 | 抗体精度打磨过程 |
| signal sequence / peptide | 信号肽 | Milstein 先行证据；假说归属 Blobel 勿越界 |
| phosphoglucomutase | 磷酸葡萄糖变位酶 | 剑桥博士论文酶 |
| aldehyde dehydrogenase | 醛脱氢酶 | 早期酶动力学对象 |
| antibody engineering | 抗体工程 | 其前瞻方向 |
| Copley Medal | 科普利奖章 | 1989 |
| Konex Diamond Award | 孔内克斯钻石奖 | 阿根廷最高文化荣誉 1993 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Cinematic Experience**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：从潘帕斯草原到剑桥实验室、从流亡学者到改写医学的诺奖得主——Milstein 的人生是一部自带配乐的传记电影；"Cinematic Experience" 匹配其跨越大洲与时代的戏剧弧光，以及 2010 年纪录片《Un fueguito》的致敬。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/César_Milstein/Cinematic_Experience.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
