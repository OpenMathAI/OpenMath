# 医学家立传提示词（Philip Showalter Hench）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1950 年得主 Philip Showalter Hench（菲利普·肖瓦尔特·亨奇）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Philip_Showalter_Hench/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Philip Showalter Hench（1896-02-28 生于宾夕法尼亚州匹兹堡 ~ 1965-03-30 逝于牙买加奥乔里奥斯，享年 69 岁）
- **气质关键词**：**可的松的临床验证者、风湿病学的掌门、Mayo Clinic 双诺奖之一**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1950 条目，三人共享同句）：
  > "for their discoveries relating to the hormones of the adrenal cortex , their structure and biological effects"（因其关于肾上腺皮质激素的结构与生物学效应的发现）
- **设计母题**：**类风湿的可逆时刻（the reversible moment）**——可的松让被认定不可逆的风湿性关节炎患者重新起身；用「僵直的关节轮廓在金色药光中舒展」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Philip_Showalter_Hench/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/20th_century/Philip_Showalter_Hench/`（1950 年像，见 images.txt）。Makefile 复制后设 `MAIN=Philip_Showalter_Hench_zh`、`VIDEO_NAME=Philip_Showalter_Hench_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Hench 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | rheumatology | 风湿病学 | Mayo 风湿病科主任 1926 起；可的松治疗类风湿的临床验证 | 封面、核心页 |
| 1 | endocrinology | 内分泌学 | 肾上腺皮质激素的临床应用，1950 诺奖核心 | 核心页 |
| 2 | clinical medicine | 临床医学 | 医师身份；可的松治疗试验 1948–1949 | 核心页 |
| 3 | history of medicine | 医学史 | 黄热病发现史终身兴趣与文献收藏 | 后期页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 正文/infobox 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Edward Calvin Kendall | 无向 | Mayo Clinic 同事：生物化学家分离肾上腺皮质类固醇（Compound E），与 Hench 临床试验互补 |
| co-honored | Edward Calvin Kendall | 无向 | 1950 诺贝尔生理学或医学奖共享（官方理由句同一） |
| co-honored | Tadeus Reichstein | 无向 | 1950 诺贝尔生理学或医学奖共享（瑞士化学家；官方理由句同一） |
| spouse | Mary Kahler | 无向 | 1927 结婚（1905–1982），育二女二子 |
| parent-child | Philip Kahler Hench | Hench → 子 | 亦习风湿病学 |

**不入库但提示词可叙述**：岳父 John Henry Kahler（Mayo 创始人 William J. Mayo 之友，姻亲）；William J. Mayo（岳父之友，非本人关系）；获奖晚宴致辞中「一医二化」妙语所指的两位化学家即 Kendall 与 Reichstein。

## 五、配色方案 【人物专属】

- **气质**：美国中西部的临床坚实、可的松带来的金色缓解
- **主色**：`#0B5351`（临床青——Mayo 白墙下的沉静观察）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeCort` 可的松临床 — 临床青 `#0B5351`
  - `badgeRheum` 风湿病学 — 深蓝 `#16324F`
  - `badgeMayo` Mayo 双诺奖 — 深金 `#B8860B`
  - `badgeYellow` 黄热病史 — 暗红 `#8B1A1A`
- **背景母题**：僵直关节轮廓在金色光晕中舒展的渐变。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 可的松的临床验证者 / Philip S. Hench 1896–1965 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、匹兹堡出身、拉法耶特学院 BA 1916、
    匹兹堡大学 MD 1920、Mayo Clinic 1923 起、风湿病科主任 1926、诺奖 1950、核心领域）
03  核心贡献概览 — 可的松临床试验 / 风湿病科建制 / 黄热病史研究 / Mayo 双诺奖
04  匹兹堡与从军学医 (1896–1920) — 拉法耶特 BA 1916；美军医疗队；匹兹堡 MD 1920
05  Mayo 起步 (1923–1926) — Mayo Foundation Fellow；风湿病科 1926 主任
06  临床观察与假说 — 关节炎疼痛缓解的临床观察→类固醇缓解假说
07  Kendall 的 Compound E — 生化侧的分离；一医一化的双线会合
08  延误与转机 (1940s) — Compound E 合成昂贵耗时+二战服役；1948–1949 试验成功（核心贡献页）
09  可的松命名与疗效 — Compound E → cortisone；类风湿患者的可逆缓解
10  1950 三人共享 — 与 Kendall（Mayo 同事）、Reichstein（瑞士化学家）；官方理由句
11  「一医二化」的致辞 — 晚宴引语：medicine 与 chemistry 以双键相连（page.md 明载）
12  诺奖演讲与荣誉 — 1950-12-11 演讲；Heberdeen 1942 / Lasker 1949 / Passano 1950；美国风湿病学会创始成员（1940-41 主席）
13  黄热病的史学家 — 1937 起整理发现史；Philip S. Hench Walter Reed Yellow Fever Collection（弗吉尼亚大学）
14  家与结尾 — 妻 Mary Kahler（1927）；子 Philip Kahler Hench 继习风湿病学；1965 牙买加度假中肺炎辞世 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 1950 三人共享同句理由 | 与 Kendall、Reichstein 共享且**官方理由同句**（"for their discoveries relating to the hormones of the adrenal cortex, their structure and biological effects"）——引用以 citations json 逐字为准，本批三人 yaml note 措辞统一 |
| 与 Kendall 的双线 | Mayo **同事** + **共同得主**两重关系，yaml 分建 colleague 与 co-honored 两行（同 Penrose–Hawking 先例），勿合并为一行 |
| Compound E → cortisone | Kendall 分离的类固醇当时代号 Compound E，治疗后命名 cortisone——命名沿革要点明；试验 1948–1949 成功 |
| 延误的两因 | Compound E 合成昂贵耗时 + Hench 二战服役——试验推迟的并列原因，勿归单因 |
| 「一医二化」引语 | 晚宴致辞 "Perhaps the ratio of one physician to two chemists is symbolic, since medicine is so firmly linked to chemistry by a double bond."——page.md 明载可引原文+译文，双键（double bond）双关勿意译丢失 |
| 黄热病史线 | 1937 起文献收藏，逝后由妻子捐赠弗吉尼亚大学（Philip S. Hench Walter Reed Yellow Fever Collection）——他**研究黄热病史**而非黄热病病毒学，勿与 Theiler 的黄热病疫苗混淆 |
| Mayo 双诺奖口径 | 截至 2010 年，Hench 与 Kendall 是 Mayo Clinic 仅有（only two）的诺奖得主——按页面口径表述 |
| 家庭 | 妻 Mary Kahler（1927 结婚）；岳父 John Henry Kahler 与 Mayo 创始人 William J. Mayo 为友——姻亲不入库；子 Philip Kahler Hench 习风湿病学（入库 parent-child）；四子女中仅此子具名 |
| 死亡地 | 1965-03-30 卒于牙买加奥乔里奥斯（度假中肺炎）——勿写成美国某地 |
| 荣誉年份 | Heberdeen Medal 1942 / Lasker 1949 / Passano 1950；美国风湿病学会创始成员、1940 与 1941 两度主席——年份勿混 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| cortisone | 可的松 | Compound E 的后来命名 |
| hormones of the adrenal cortex | 肾上腺皮质激素 | 获奖理由核心词 |
| rheumatoid arthritis | 类风湿关节炎 | 临床适应症 |
| Compound E | E 化合物 | 可的松前身代号 |
| reversibility | 可逆性 | 诺奖演讲题关键词（The Reversibility of Certain Rheumatic...） |
| ACTH (pituitary adrenocorticotropic hormone) | 促肾上腺皮质激素 | 演讲题中与可的松并列 |
| double bond | 双键 | 致辞双关：化学键+医学化学的紧密联结 |
| yellow fever | 黄热病 | 其史学研究主题（非病毒学） |
| American Rheumatism Association | 美国风湿病学会 | 创始成员、1940-41 主席 |
| Mayo Clinic | 梅奥诊所 | 终身任职机构 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Expedition**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：从风湿病科的临床观察到促成可的松问世的二十年长跑，再到对黄热病发现史的远征式整理——「远征」对应其横跨临床、生化与医史的求索半径；乐曲的行进感也贴合 1948 年试验成功的破晓时刻。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Philip_Showalter_Hench/Expedition.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
