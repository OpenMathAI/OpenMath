# 医学家立传提示词（David Baltimore）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1975 年得主 David Baltimore（戴维·巴尔的摩）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/David_Baltimore/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：David Baltimore（1938-03-07 生于纽约 ~ 2025-09-06 逝于 Woods Hole，享年 87 岁），美国生物学家，Caltech 第六任校长、洛克菲勒大学第六任校长、Whitehead 研究所创始所长
- **气质关键词**：**逆转录酶的共同发现者、病毒分类法的缔造者、DNA→RNA 中心法则的改写者**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1975 条目，Baltimore/Temin/Dulbecco 三人共享）：
  > "for their discoveries concerning the interaction between tumour viruses and the genetic material of the cell"（因其关于肿瘤病毒与细胞遗传物质相互作用的发现）
- **设计母题**：**逆向的转录箭头（RNA → DNA）**——逆转录酶让遗传信息可以反向流动；用「双向箭头贯穿双螺旋与 RNA 链」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/David_Baltimore/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；第 0/1/2/3 步按 medic 路径执行：页面已在 `medic/presentations/pages/20th_century/David_Baltimore/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=David_Baltimore_zh`、`VIDEO_NAME=David_Baltimore_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。**注意**：2025 年 9 月逝世——本篇是"刚逝世"得主，生卒口径 1938–2025。

## 三、研究领域梳理 + 入库 【人物专属】

**Baltimore 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | virology | 病毒学 | 逆转录酶、Baltimore 病毒分类、VSV | 全篇 |
| 1 | molecular biology | 分子生物学 | 中心法则修正、感染性 cDNA 克隆 | 核心页 |
| 2 | immunology | 免疫学 | NF-κB、RAG-1/2、抗体基因重排 | 免疫页 |
| 3 | biochemistry | 生物化学 | 酶学训练与病毒酶学 | 早年页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | George Streisinger | 对方 → 本科暑期导师 | 冷泉港 1959 首届 URP，引其入分子生物学 |
| advisor-student | Richard Franklin | 对方 → 博士导师 | 洛克菲勒大学（1964，mengovirus 与首个 RNA 复制酶描述） |
| advisor-student | James E. Darnell | 对方 → 博士后合作者 | MIT（1963）；1975 休假再赴洛克菲勒合作 |
| advisor-student | Jerard Hurwitz | 对方 → 酶学训练导师 | 1964 阿尔伯特·爱因斯坦医学院 |
| colleague | Salvador Luria | 无向 | 1968 招其回 MIT，MIT 癌症研究中心主任 |
| colleague | Renato Dulbecco | 无向 | 1965 招其加入新建索尔克研究所 |
| co-honored | Renato Dulbecco | 无向 | 1975 诺贝尔生理学或医学奖三人共享 |
| co-honored | Howard Martin Temin | 无向 | 1975 三人共享；两人同时独立发现逆转录酶，Nature 背靠背论文 |
| colleague | Paul Berg | 无向 | 协助组织 1975 年 Asilomar 重组 DNA 会议（库内 id=1128） |
| spouse | Alice S. Huang | 无向 | 1967 索尔克相识，1968 结婚，VSV 研究伙伴，育一女 |
| advisor-student | Sara Cherry | Baltimore → 博士生 | infobox Doctoral students 明载 |
| advisor-student | Howard Y. Chang | Baltimore → 博士生 | infobox Doctoral students 明载 |
| advisor-student | Vincent Racaniello | Baltimore → 博士后 | 1981 构建脊髓灰质炎病毒感染性 cDNA 克隆 |
| advisor-student | Ranjan Sen | Baltimore → 博士后 | 1986 共同发现转录因子 NF-κB |
| advisor-student | David G. Schatz | Baltimore → 学生 | 1988-89 发现 RAG-1/RAG-2 |
| advisor-student | Marjorie Oettinger | Baltimore → 学生 | 1988-89 与 Schatz 共同发现 RAG-1/RAG-2 |

**不入库但提示词可叙述**：Marc Girard/Michael Jacobson（索尔克门生）、Martha Stampfer（VSV 合作研究生）、Grosschedl/Weaver（转基因小鼠博士后）、George Q. Daley（bcr-abl→Gleevec 奠基）、Matthew Porteus（2003 首次人类细胞精准基因编辑）、Lili Yang（lentivirus 载体）——门生群按择要口径未逐一建边；Tony Hunter（酪氨酸激酶平行发现）；Maxine Singer（Asilomar 共同组织者）；Imanishi-Kari（合作与争议，见陷阱表禁写口径）。

## 五、配色方案 【人物专属】

- **气质**：冷泉港的初夏、逆转录的反叛、董事会会议室的沉稳
- **主色**：`#16324F`（深海蓝——Woods Hole 与大科学机构的重量）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeRT` 逆转录酶 — 深海蓝 `#16324F`
  - `badgeClass` Baltimore 分类 — 青灰 `#0E7490`
  - `badgeImm` 免疫学 NF-κB/RAG — 深紫 `#4A2A6A`
  - `badgePolicy` 公共科学政策 — 赭金 `#B07D2B`
- **背景母题**：双向转录箭头与病毒颗粒剪影，稀疏排布。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 逆转录酶的共同发现者 / David Baltimore 1938–2025 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、皇后区/Great Neck 出身、Swarthmore BA 1960/
    洛克菲勒 PhD 1964、MIT/索尔克/Whitehead/洛克菲勒/Caltech 任职、诺奖 1975、核心领域）
03  核心贡献概览 — 逆转录酶 1970 / Baltimore 病毒分类 / NF-κB 与 RAG / Asilomar 与科学政策
04  大颈镇少年与 Jackson 实验室 (1938–1960) — 高中暑期缅因 Bar Harbor 初遇 Temin、
    Swarthmore 化学 BA 高荣誉
05  冷泉港与洛克菲勒 (1959–1964) — Streisinger 门下入分子生物学、MIT 博士项目、
    转投 Franklin 实验室两年速成 PhD、首个 RNA 复制酶描述
06  博士后漂流与索尔克 (1963–1968) — Darnell、Hurwitz 酶学、1965 被 Dulbecco 招入索尔克、
    病毒多聚蛋白水解加工、遇 Alice Huang
07  回 MIT 与 VSV (1968–1970) — Luria 招募、与 Huang/Stampfer 发现 VSV 粒内 RNA 依赖的 RNA 聚合酶
08  1970：逆转录酶（核心贡献页）— 与 Temin（及 Mizutani）同时独立发现、Nature 背靠背论文、
    逆转病毒类群、中心法则修正
09  1975 诺奖：三人共享 — 获奖理由逐字呈现、37 岁、与 Temin/Dulbecco 的分工口径
10  Asilomar 与科学政策 (1975) — 与 Berg/Singer 组织重组 DNA 会议、安全准则与自愿暂停、
    AIDS 时代 Confronting AIDS 报告与 NIH 疫苗委员会
11  Whitehead 研究所 (1982–1990) — 创始所长、35M 建楼/135M 总捐、Fink/Jaenisch/Lodish/Weinberg
    创始成员、全球分子生物学第一
12  免疫学的丰收 — NF-κB（Sen 1986）、RAG-1/2（Schatz/Oettinger）、bcr-abl（Daley→Gleevec 铺路）
13  两段校长岁月 — 洛克菲勒第六任校长（1990-91 辞任）、Caltech 第六任校长（1997-2005）、
    2021 Millikan 除名后头衔改 Distinguished Professor
14  遗产与结尾 — 700+ 论文、百项专利、2021 Lasker-Koshland 终身成就奖、
    "60 年研究，该把领域交给年轻人" + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 生卒口径 | 1938-03-07 纽约 ~ **2025-09-06** 逝于 Woods Hole 家中（癌症），87 岁——刚逝世得主，生卒双写 |
| 1975 三人分工 | **Temin 与 Baltimore 同时独立发现逆转录酶**（Temin 先提出前病毒假说，Mizutani 与 Temin 共同实验；Nature 背靠背论文）；**Dulbecco 未直接参与实验，但教会了两人所用方法**且证明肿瘤病毒基因整合——三人贡献各述勿混 |
| 与 Temin 的相逢 | 高中暑期 Jackson 实验室即相识（page.md 明载）——命运的伏笔可写一句 |
| 争议事件禁写口径（★） | ①Imanishi-Kari 案：**整体回避**；如必须提及仅一句客观带过且必须含终局（1996 申诉小组驳回全部 19 项指控，OSI/ORI 从未指控 Baltimore 本人有不端）；②Luk van Parijs 案：回避；③**COVID-19 "smoking gun" 实验室泄漏言论（2021）涉地缘政治敏感，一律禁写** |
| MIT 职年细节 | 1960 入 MIT 研究生项目→转洛克菲勒完成 PhD（1964）→1963 年表上"回 MIT 做博士后 with Darnell"（page.md 原文年份如此，照写）→1972 34 岁获终身教职→1997 离开 MIT 教职 |
| Whitehead 数字 | 3500 万美元建楼、每年 500 万保底、遗嘱追加共 1.35 亿美元总赠——三个数字勿混 |
| 校长顺位 | 洛克菲勒第六任（前任 Lederberg、后任 Wiesel）；Caltech 第六任（前任 Everhart、后任 Chameau）——两条校长线勿混 |
| Millikan 除名 | 2021 Caltech 因其优生学参与移除创始人 Millikan 之名，Baltimore 头衔由 emeritus 系列改为 Distinguished Professor of Biology——客观一句可写 |
| 引语清单 | 可引：Asilomar "The whole Asilomar process opened up to the world..."；退休 "I have been involved in research for 60 years..."；RAG "our most significant discovery in immunology"——均 page.md 明载 |
| 荣誉年份链 | Gustav Stern 1971（首得主）、Warren Triennial 1971、Eli Lilly 1971、NAS/AAAS/IOM 1974、NAS 分子生物学奖+Gairdner 1974、Nobel 1975、Pontifical 1978、EMBO 1983、ForMemRS 1987、NMS 1999、Alpert 2000、法科院 2000、APS 1997、Lasker-Koshland 2021——勿串 |
| 免疫学成果归属 | NF-κB=Sen 与 Baltimore（1986）；RAG-1/2=Schatz 与 Oettinger（1988-89）；酪氨酸激酶活性=Tony Hunter 平行发现——各归其位 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| tumour viruses | 肿瘤病毒 | 获奖理由核心词 |
| reverse transcriptase | 逆转录酶 | RNA 依赖的 DNA 聚合酶，1970 |
| retrovirus | 逆转录病毒 | 其发现的新病毒类群 |
| provirus hypothesis | 前病毒假说 | Temin 先行提出 |
| Baltimore classification | Baltimore 病毒分类 | 按核酸类型与转录策略七分类 |
| VSV | 水疱性口炎病毒 | 粒内 RNA 聚合酶发现的对象 |
| defective interfering particles | 缺陷干扰颗粒 | 与 Huang 的合作课题 |
| NF-κB | 核因子 κB | 1986 与 Sen 发现的关键转录因子 |
| RAG-1/RAG-2 | 重组激活基因 | 抗体基因重排机制（1988-89） |
| Asilomar conference | Asilomar 重组 DNA 会议 | 1975，生物安全政策里程碑 |
| infectious clone | 感染性克隆 | 1981 与 Racaniello 的脊髓灰质炎病毒 cDNA |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Cinematic Experience**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Baltimore 的一生是三部曲式的电影剧本——37 岁的诺奖高光、执掌三大科学机构的行政史诗、以及晚年捐出实验室的谢幕独白；Cinematic Experience 的大片质感对应这种多幕人生，也对应逆转录那个改写教科书的"剧情反转"。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/David_Baltimore/CinematicExperience.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
