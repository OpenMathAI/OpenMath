# 医学家立传提示词（Harold E. Varmus）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1989 年得主 Harold E. Varmus（哈罗德·埃利奥特·瓦慕斯）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Harold_E._Varmus/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Harold Eliot Varmus（1939-12-18 生于纽约州 Oceanside，**在世**），美国病毒学家，NIH 第 14 任院长（1993-1999）、NCI 第 14 任院长（2010-2015）、MSKCC 院长（2000-2010）、PLOS 联合创始人
- **气质关键词**：**原癌基因的发现者、开放获取出版的旗手、三大科学机构的掌舵人**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1989 条目，Varmus/Bishop 两人共享）：
  > "for their discovery of the cellular origin of retroviral oncogenes"（因其发现逆转录病毒癌基因的细胞起源）
- **设计母题**：**从文学到基因的转向（English lit → c-Src）**——文学硕士转身拿起移液枪；用「书页与双螺旋的叠化」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Harold_E._Varmus/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；第 0/1/2/3 步按 medic 路径执行：页面已在 `medic/presentations/pages/20th_century/Harold_E._Varmus/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Harold_E._Varmus_zh`、`VIDEO_NAME=Harold_E._Varmus_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。**在世者注意**：封面写 b.1939。

## 三、研究领域梳理 + 入库 【人物专属】

**Varmus 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | virology | 病毒学（逆转录病毒复制） | infobox Fields；1989 诺奖核心 | 全篇 |
| 1 | cancer biology | 癌症生物学 | infobox Fields（Cancer biology） | 核心页 |
| 2 | molecular biology | 分子生物学 | Wnt-1/乙肝病毒/核糖体移码 | 研究页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Ira Pastan | 对方 → 导师 | NIH 公共卫生服务临床研究员（1968-1970，cAMP 与 lac 操纵子调控） |
| advisor-student | J. Michael Bishop | 对方 → 博士后导师 | 1970 年起 UCSF 其实实验室博士后（美国癌症学会资助） |
| colleague | J. Michael Bishop | 无向 | 长期科学伙伴，c-Src/v-Src 发现搭档 |
| co-honored | J. Michael Bishop | 无向 | 1989 诺贝尔生理学或医学奖共享 |
| colleague | Roel Nusse | 无向 | 共同发现原癌基因 Wnt-1 |
| colleague | Donald Ganem | 无向 | 共同阐明乙型肝炎病毒复制周期 |
| advisor-student | Tyler Jacks | Varmus → 博士生 | infobox Doctoral students 明载，合作发现核糖体移码 |
| advisor-student | Kirsten Bibbins-Domingo | Varmus → 博士生 | infobox Doctoral students 明载 |
| spouse | Constance Louise Casey | 无向 | 记者/科学作家，1969 结婚，二子 Jacob 与 Christopher |

**不入库但提示词可叙述**：Peyton Rous（文献渊源不建边）；John Young 与 Paul Bates（禽逆转录病毒受体合作）、William Pao（肺癌 EGFR 突变合作）——择要口径未建边；Patrick Brown 与 Michael Eisen（PLOS 联合创始人）、David Lipman（PubMed Central）——机构共创非个人师承；Bruce Alberts 与 Marc Kirschner（科学政策战友）。

## 五、配色方案 【人物专属】

- **气质**：文学青年的转身、大科学机构的担当、开放获取的理想主义
- **主色**：`#16324F`（深海蓝——从曼哈顿上西区到日内瓦议程的辽阔）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeOncogene` 原癌基因 — 深海蓝 `#16324F`
  - `badgeNCI` NIH/NCI 院长 — 深青 `#0E7490`
  - `badgePLOS` 开放获取 — 赭金 `#B07D2B`
  - `badgeWnt` Wnt-1 与乙肝 — 深紫 `#4A2A6A`
- **背景母题**：书页与双螺旋叠化、开放期刊的open锁形符号，稀疏排布。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 原癌基因的发现者 / Harold E. Varmus b.1939 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Oceanside 出身、Amherst 英文 BA/哈佛英文 MA/
    哥伦比亚 MD、UCSF/NIH/MSKCC/NCI/Weill Cornell 任职、诺奖 1989、核心领域）
03  核心贡献概览 — c-Src 细胞起源 / Wnt-1 / 乙肝病毒复制 / PLOS 与科学出版革命
04  英文系青年 (1939–1965) — Freeport 高中、Amherst 英文 BA、哈佛英文 MA、两次被哈佛医学院拒收
05  哥伦比亚 MD 与印度 (1965–1968) — P&S 医学博士、Bareilly 传教士医院、哥伦比亚长老会医院
06  NIH 与 Pastan (1968–1970) — 越战期间以公共卫生服务替代服役、cAMP 调控 lac 操纵子
07  1970：投奔 Bishop（核心贡献页）— UCSF 博士后、逆转录病毒致癌机制的长期搭档
08  c-Src 的鉴定（核心页）— 细胞基因 c-src 是 v-src 的源头、原癌基因家族发现潮
09  1989 诺奖：与 Bishop 共享 — 获奖理由逐字呈现、文学硕士的科学转身
10  更多的病毒与基因 — Wnt-1（与 Nusse）、乙肝病毒复制（与 Ganem）、核糖体移码（与 Jacks）、
    肺癌 EGFR 突变（与 Pao）
11  NIH 院长 (1993–1999) — 克林顿提名、预算近翻倍、临床中心与疫苗研究中心、干细胞/克隆/基因治疗
    政策声明
12  MSKCC 与 NCI (2000–2015) — 纪念斯隆-凯特林院长十年半、2010 奥巴马任命 NCI 第 14 任院长
    （史上首位先任 NIH 院长再任下属研究所长）、2015 辞任回纽约
13  PLOS 与开放获取 — PubMed Central 创立（与 Lipman）、PLOS 联合创始（与 Brown/Eisen）、
    癌症药价批评
14  遗产与结尾 — The Art and Politics of Science、Weill Cornell Lewis Thomas 讲席教授 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 姓名与在世口径 | **yaml/入库用 manifest 形式 "Harold E. Varmus"**；1939-12-18 生于 Oceanside，**在世**——封面写 b.1939 |
| 1989 两人共享 | 仅与 Bishop 两人共享（各半）；获奖理由 "for their discovery of the cellular origin of retroviral oncogenes" |
| Bishop 双边 | advisor-student（1970 博士后导师）+ colleague（长期伙伴）+ co-honored 三边并行；c-Src 鉴定是两人共同成果 |
| 英文文学出身 | Amherst 英文 BA + 哈佛英文 MA、两次被哈佛医学院拒收——转行叙事主线；MD 来自哥伦比亚 P&S |
| 越战替代服役 | 以公共卫生服务（PHS）军官身份在 NIH 服役替代参军——客观一句，不展开战争评判 |
| 政治敏感禁写（★） | ①2025 年联署反对 RFK Jr. 出任 HSHS 部长——**涉现任美国政治任命之争，禁写**；②支持戈尔/克里/奥巴马竞选、批评小布什科学政策——**竞选站队与党派批评一律回避**；③克林顿提名 NIH 院长、奥巴马任命 NCI 院长——仅客观列出任职，不评价总统 |
| 职年链 | NIH 临床 associate 1968-70 → UCSF 博士后 1970/助理教授 1972/教授 1979/ACS 研究教授 1984 → NIH 院长 1993-11-23 至 1999-12-31 → MSKCC 院长 2000-01-01 至 2010-06-30 → NCI 院长 2010-07-12 至 2015-03-31 → Weill Cornell——六段勿串 |
| NCI 首例 | 先任 NIH 院长再任其下属 NCI 院长为史上首例（page.md 明载）；任内更名 Frederick 国家实验室、启动 RAS 癌基因计划 |
| PLOS 口径 | 与 Patrick Brown（斯坦福）、Michael Eisen（伯克利）共同创办理科学公共图书馆；PubMed Central 与 NCBI 的 David Lipman 共建——机构共创叙述，个人边不入库 |
| 引语清单 | 诺奖相关与书名 The Art and Politics of Science 可叙述；page.md 无成段直接引语——禁编引语 |
| 家庭线 | 妻 Constance 为记者/科学作家；长子 Jacob 爵士小号手、"Genes and Jazz" 讲奏会（古根海姆/史密森/肯尼迪中心）——身份页调剂素材 |
| 荣誉年份链 | AAAS 院士 1975、Lasker 1982、Sloan 1984、Nobel 1989、Golden Plate 1990、APS 1994、Novartis-Drew 2002、ForMemRS 2005、Friesen 2008、Double Helix 2011、Seaborg 2012、Vannevar Bush 2001——勿串 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| cellular origin of retroviral oncogenes | 逆转录病毒癌基因的细胞起源 | 获奖理由逐字对应 |
| c-Src / v-Src | 细胞/病毒 Src | 细胞基因是病毒癌基因的源头 |
| proto-oncogene | 原癌基因 | 继 Bishop 篇术语 |
| Wnt-1 | Wnt-1 原癌基因 | 与 Nusse 共同发现 |
| ribosomal frameshifting | 核糖体移码 | 与 Jacks 合作的逆转录病毒机制 |
| PLOS | 科学公共图书馆 | 开放获取出版商，三联合创始人 |
| PubMed Central | PubMed Central | 与 Lipman 共建的公共全文库 |
| PCAST | 总统科学技术顾问委员会 | 2009 联合主席（客观职衔） |
| lac operon | lac 操纵子 | NIH 时期 cAMP 调控研究对象 |
| Lewis Thomas University Professor | Lewis Thomas 大学讲席教授 | Weill Cornell 现职 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Through the Darkness**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Varmus 一生穿越了太多"黑暗"——从两次被拒的医学院申请，到癌症病因的未知地带，再到科研经费与论文垄断的制度性迷雾；Through the Darkness 的行进感对应他"发现者+体制改革者"的双重身份，也对应开放获取运动想为整个科学界点亮的灯。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Harold_E._Varmus/ThroughTheDarkness.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
