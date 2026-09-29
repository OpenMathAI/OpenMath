# 医学家立传提示词（Selman Waksman）

> **OpenMedic** 项目 · 20 世纪诺贝尔生理学或医学奖 **1952 年**得主（独享）。
> 本文件是 Waksman 的「人物专属立传提示词」，供后续 Beamer 立传 agent 直接使用；配套数据已按第三、四节入库 greatminds 库。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Selman Abraham Waksman（1888-07-22 [俄历 7-10] ~ 1973-08-16，享年 85 岁），乌克兰裔美国生物化学家、微生物学家
- **气质关键词**：**抗生素一词的命名者、链霉素的发现者、土壤微生物学的宗师** —— 1952 诺贝尔生理学或医学奖获奖理由（官方原文，逐字引用）：
  > "for his discovery of streptomycin , the first antibiotic effective against tuberculosis"（因其发现链霉素——首个对结核病有效的抗生素）
- **设计母题**：**土壤中的药房（the pharmacy in the soil）**。一捧黑土里放线菌的菌丝网络——Waksman 从泥土里挖出链霉素，以「土层剖面中发光的菌丝」作为视觉隐喻。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Selman_Waksman/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `Physicist_Bio_Prompt_Template.md` 第三章八步流程：下载核对 → 建目录 → 复制 Makefile → 收集图片 → 研究领域入库 → 社会关系入库 → 编写 Beamer → 布局检查 + 史实审查。
> **第 0/1/2/3 步按 medic 路径执行**：页面用 `medic/presentations/pages/20th_century/Selman_Waksman/`；Makefile 复制后设 `MAIN=Selman_Waksman_zh`；BGM 复制到本目录（见第九节）。
> 数据库两步（第 4/4.5 步）**已完成**，见第三、四节；执行 agent 只需做 Beamer 与目检。

## 三、研究领域梳理 + 入库 【已入库，与 yaml 完全一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | microbiology | 微生物学 | 1952 诺奖核心：土壤放线菌与抗生素筛选矩阵 | 核心页 |
| 1 | biochemistry | 生物化学 | 伯克利博士（1918）、酶与腐殖质研究 | 早年页 |
| 2 | soil microbiology | 土壤微生物学 | 一生主业：土壤中有机体分解研究 | 研究页 |
| 3 | antibiotics | 抗生素 | 链霉素/新霉素等 15+ 种、命名 antibiotic 一词 | 药物页 |

## 四、社会关系梳理 + 入库 【已入库，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | J. G. Lipman | 师→生（硕士导师） | 罗格斯新泽西农试站土壤细菌学导师 |
| advisor-student | Albert Schatz | 生（Waksman→学生） | 博士生，1943 实际分离链霉素并验其对结核效力 |
| advisor-student | Hubert A. Lechevalier | 生（Waksman→学生） | 博士生，合作发现新霉素（Science 刊载） |
| controversy | Albert Schatz | 无向 | 1950 诉讼：获 12 万美元与 3% 版税、共同发现者身份获庭外确认 |
| colleague | Elizabeth Bugie Gregory | 无向 | 确证链霉素结果、首篇论文署名但未获应得荣誉 |
| colleague | Charles Thom | 无向 | 1915-16 其农业部处习土壤真菌 |
| spouse | Deborah B. Mitnik | 无向 | 1974 卒 |

**方向约定**：`advisor-student` + `direction: advisor` = 对方是导师；`direction: student` = 对方是学生；其余无向（from<to 自动归一）。

## 五、配色方案 【人物专属】

- **气质**：泥土的厚重、俄裔移民的坚韧、诉讼岁月的暗涌
- **主色**：`#5C3A1E`（沃土棕，土壤与放线菌）
- **香槟金**：`#D4B26A`（诺奖色）
- **badgeA-D 四分类色**：`badgeSoil` 土壤微生物 — 沃土棕 `#5C3A1E`；`badgeStrep` 链霉素 — 药青 `#1E7A6B`；`badgeDispute` 学讼 — 争议灰紫 `#5C4A6E`；`badgeMarine` 海洋细菌 — 海蓝 `#2E5E7E`
- **背景母题**：土层剖面横带（深浅棕）之上散布发光菌丝网络与孢子小圆。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 土壤里的药房 / Selman Waksman 1888–1973 + 四色 badge + 右上肖像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Novaya Priluka、罗格斯/伯克利、罗格斯四十年、荣誉）
03  核心贡献概览 — 链霉素 / 抗生素命名 / 筛选矩阵 / 海洋细菌
04  从乌克兰到新泽西 (1888–1916) — 基辅犹太家庭、1910 移美、罗格斯农学 1915/1916、Lipman 门下
05  伯克利博士与土壤岁月 (1916–1930) — Thom 处农业部、1918 伯克利博士、《土壤微生物学原理》1927
06  Woods Hole 兼职 (1931–1942) — 组建海洋细菌部、海洋氮循环研究
07  筛选矩阵方法论（核心贡献页）— 抗生素×病原全矩阵系统筛选、15+ 抗生素清单（放线菌素/链丝菌素/新霉素…）
08  1943 链霉素 — Schatz 自实验室外农田分离灰色链霉菌、对结核杆菌首效、Bugie 确证
09  antibiotic 一词 — 现代含义由其引入（1871 Hallopeau 旧义之辨析）
10  专利与基金会 — 专利版税、1951 捐半数设微生物学基金会、Waksman 研究所
11  1952 诺贝尔奖 — 独享、「人类最伟大的恩人之一」颁奖辞；Schatz 抗议致信瑞典国王被驳回
12  Schatz 之讼 (1950) — 庭外和解：12 万美元 + 3% 版税 + 共同发现者身份；The Lancet 之评
13  学术制度遗产 — 此讼推动大学专利与署名制度变革——正文明载的制度影响
14  遗产与身后 — NAS Waksman 奖、2005 ACS 国家历史化学地标、1973 卒于 Woods Hole
15  结尾
```

## 七、特殊陷阱表 【★ 核心，从 page.md 提炼】

| 陷阱 | 说明 |
|------|------|
| 生卒日 | 1888-07-22（俄历 7-10）生于基辅省 Novaya Priluka（今乌克兰文尼察州）；1973-08-16 卒于 Woods Hole（Hyannis 医院），葬 Woods Hole Village Cemetery |
| 获奖理由 | "for his discovery of streptomycin , the first antibiotic effective against tuberculosis"——**his**（独享）；citation 原文逗号前有空格，逐字引用保留 |
| Schatz 双边 | Schatz 既是博士生（实际分离者）又是 1950 诉讼对手——**advisor-student 与 controversy 两边并存**，叙事两段都讲：功劳与争议各自成立 |
| Bugie 削名 | Elizabeth Bugie Gregory 首篇论文署名、第二篇未署且未列专利（签免责宣誓书）——正文明载的荣誉不公案例，客观呈现 |
| antibiotic 词源 | Waksman 引入其**现代含义**；1871 年 Hallopeau 已用旧义——「引入现代含义」勿写成「发明单词」 |
| frontmatter 导师不入库 | infobox 博士导师 T. Brailsford Robertson 正文无载——**不建边**（新纪律执行例），提示词此处注明 |
| 子女 | 子 Byron H. Waksman（1919-2012，哈佛/耶鲁教授、基金会继任者 1970-2000）——正文有载但本批不建 parent-child 边，留主控口径 |
| 引语 | 正文引语：诺奖颁奖辞「one of the greatest benefactors to mankind」、The Lancet 对诺委会之评——引语仅用这些 |
| 争议表述 | Waksman「最终声称独得发现功」与 Schatz 自述三个月在实验室——两说并陈，不裁决 |
| 国籍口径 | manifest/Nobel 官方为 United States（1916 归化）；生地今属乌克兰——表述「俄属乌克兰出身的美籍科学家」 |

## 八、术语清单 【6-10 条】

| 英文 | 中文 | 风险点 |
|------|------|------|
| streptomycin | 链霉素 | 自 S. griseus 分离；首个抗结核抗生素 |
| antibiotic | 抗生素 | 现代含义由 Waksman 引入 |
| actinomycetes | 放线菌 | 新霉素等来源菌群 |
| Streptomyces griseus | 灰色链霉菌 | 链霉素产生菌 |
| neomycin | 新霉素 | 与 Lechevalier 合作发现 |
| screening matrix | 筛选矩阵 | 抗生素×病原系统化试验法 |
| soil microbiology | 土壤微生物学 | 其一生主业 |
| tuberculosis | 结核病 | 链霉素首效适应症 |
| Waksman Institute | 瓦克斯曼微生物研究所 | 罗格斯 Busch 校区 |
| marine bacteriology | 海洋细菌学 | Woods Hole 兼职领域 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Tragedy** — Alex-Productions（manifest 预分配）
- **风格**：悲怆 / 深沉 / 命运感
- **匹配理由**：链霉素救回无数结核病人，而发现者之一 Schatz 却被荣誉除名、对簿公堂——Tragedy 的命运感匹配这段「拯救与亏欠并存」的复杂叙事（第二次使用该曲，首用 Koch/Buchner，同为辛酸底色）。
- **本地路径**：`music_audio/` 下 Tragedy 曲目 → 复制为 `presentations/20th_century/Selman_Waksman/Tragedy.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐 15 页时长。
