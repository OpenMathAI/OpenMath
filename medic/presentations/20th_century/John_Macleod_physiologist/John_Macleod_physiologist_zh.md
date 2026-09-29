# 医学家立传提示词（John Macleod）

> OpenMedic 项目、20 世纪诺贝尔生理学或医学奖 1923 年得主（约翰·麦克劳德，胰岛素发现的关键组织者）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：John James Rickard Macleod（1876-09-06 生于苏格兰 Perthshire Clunie ~ 1935-03-16 卒于苏格兰 Aberdeen，享年 58 岁）
- **气质关键词**：**碳水化合物代谢的毕生研究者、胰岛素发现的实验室组织者、争议中沉默的学者** —— 1923 获奖理由（与 Frederick Banting 共享）：
  > "for the discovery of insulin"（因发现胰岛素）
- **设计母题**：**实验室的钥匙**。1921 年夏，Macleod 把实验室钥匙、实验动物与学生 Best 留给 Banting 外出度假——"钥匙"作为视觉隐喻贯穿：打开胰岛素之门的人，自己却被挡在荣誉门外半个世纪。辅以鱼胰腺切片与阿伯丁海风。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/John_Macleod_physiologist/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/20th_century/John_Macleod_physiologist/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准，裁定见第七节——注意国籍裁定）。
2. **第 1 步 建目录**：`medic/presentations/20th_century/John_Macleod_physiologist/`（含 `images/`）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=John_Macleod_physiologist_zh`、`VIDEO_NAME=John_Macleod_physiologist_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/20th_century/John_Macleod_physiologist/images.txt`（c. 1928 照）；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。插图可用 Duthie Park 的 Macleod 雕像照与阿伯丁墓园照。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/John_Macleod_physiologist.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | carbohydrate metabolism | 碳水化合物代谢 | 1905 年起的毕生核心方向 | 晚年页 |
| 1 | diabetes | 糖尿病与胰岛素 | 1923 诺奖核心；《Diabetes: its Pathological Physiology》1913 | 胰岛素页 |
| 2 | physiology | 生理学 | Western Reserve/Toronto/Aberdeen 任教 | 身份页 |
| 3 | biochemistry | 生物化学 | 莱比锡进修；磷酸肌酸等早期论文 | 早年页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Frederick Banting | 无向 | 1923 诺贝尔生理学或医学奖共享（for the discovery of insulin） |
| controversy | Frederick Banting | 无向 | 胰岛素发现功劳之争（Banting 指其贡献微薄，两人此后再未交谈） |
| advisor-student | John Alexander MacWilliam | 导师 | 阿伯丁大学就读时的主要教师之一 |
| advisor-student | Charles Best | 学生 | 自己的学生，1921 派予 Banting 任实验助手 |
| colleague | James Collip | 无向 | 引入的生化学家，负责酒精法纯化提取物 |
| spouse | Mary Watson McWalter | 无向 | 1903 结婚，无子女 |

> 不入库：August Krogh（1923 提名人，来访取经属事件非个人关系，可在幻灯片叙事中提及）；Nicolae Paulescu（优先权争议对象，非个人交往）；Thorburn Brailsford Robertson（任职上下文）；Leonard E. Hill / R. G. Pearce / W. R. Campbell（合著者，page.md 仅书目列举）。
> 库内当时无上述对手方记录，均由本 yaml 新建 stub；本人在 Banting yaml 中以 manifest 全名 `John Macleod (physiologist)` 被引用，本 yaml 即规范记录（回填 QID Q232024）。

## 五、配色方案 【人物专属】

- **气质**：苏格兰高地的冷峻 + 实验室的秩序 + 争议的暗影
- **主色**：苏格兰深蓝 `#1F3A5F`（学术沉静，亦含"迟到公论"的阴翳）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` 碳水代谢 — 深青 `#0E7C7B`
  - `badgeB` 胰岛素发现 — 朱红 `#B02A30`
  - `badgeC` 教学与机构 — 钢蓝 `#2E4A66`
  - `badgeD` 争议与平反 — 灰紫 `#5C5470`
- **背景母题**：低饱和大圆 + 钥匙形细线元素，呼应"实验室的钥匙"母题。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — 胰岛素发现的关键组织者 / John J. R. Macleod 1876–1935 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 Clunie/Aberdeen、教育 Aberdeen/Leipzig、
    任职 Western Reserve/Toronto/Aberdeen、荣誉 Nobel 1923/Cameron 1923、核心领域）
03  核心贡献概览 — 碳水化合物代谢 / 胰岛素发现的组织与阐释 / 鱼胰腺定位实验 / 200+ 论文 11 部专著
04  苏格兰早年 (1876–1898) — Clunie 牧师之家、Aberdeen Grammar School、医学院、
    MacWilliam 是主要教师之一、1898 荣誉医学学位
05  莱比锡与伦敦 (1898–1903) — 旅行奖学金赴莱比锡学生物化学、London Hospital 医学院讲师（1902）、
    剑桥公共卫生博士（DPH）、首篇论文肌肉含磷量
06  克利夫兰十五年 (1903–1918) — Western Reserve 生理学讲师、1905 起转向碳水代谢与糖尿病、
    1910 AMA 实验性糖尿病讲演、1913《Diabetes: its Pathological Physiology》
07  麦吉尔与多伦多 (1916–1920) — 1916 McGill 生理学教授、战后多伦多生理实验室主任、
    六年制医学课程建设者、结核杆菌化学/肌酸代谢等并行研究
08  1920 年冬：Banting 来访 — 怀疑其设想（深知前人失败）、相信神经系统调节血糖、
    1921 夏苏格兰度假前出借实验室、提供动物与学生 Best、协助第一例犬手术
09  突破与争执 (1921–1922) — B&B 犬血糖下降、Macleod 归来质疑、复验成功、
    1921-12 Yale 美国生理学会报告风波、1922-02 论文拒署名（"declined co-authorship"）
10  临床试验与工业化 — 引入 Collip 酒精纯化、1922-01 Leonard Thompson 首例成功、
    1922-05 华盛顿报告全场起立（Banting/Best 拒席抗议）、Eli Lilly 规模生产、专利转予 MRC
11  诺贝尔奖与争议 (1923) — Krogh 提名、委员会裁定（数据阐释/临床试验统筹/公开发表关键）、
    Macleod 分半奖给 Collip、1972 诺贝尔基金会承认漏 Best 是错误、Paulescu 优先权风波（Best 晚年致歉）
12  鱼胰腺与晚年研究 (1923–1935) — St. Andrews 海洋站硬骨鱼胰岛/腺泡分离实验证明胰岛素来源、
    1928 回阿伯丁任 Regius Professor（继其师 MacWilliam）、医学院长、MRC 成员 1929-33、
    中枢神经调节碳水代谢假说最终获证
13  荣誉与认可 — Nobel 1923、Cameron Prize 1923、皇家学会会员、爱丁堡皇家学会会员、
    利奥波第娜通讯会员、美国生理学会主席（1921）、加拿大皇家学会（1919）
14  遗产与平反 — 1950 独立复核还四人公道、1988《Glory Enough for All》客观呈现、
    2012 入选 Canadian Medical Hall of Fame、多伦多医学研究中心讲堂以其命名、
    Diabetes UK 70 年生存奖、Duthie Park 雕像、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 与 Banting 共享，官方逐字 "for the discovery of insulin"；勿写成"领导发现"或"独自发现" |
| 国籍裁定 ★ | 总表/manifest 作 Canada（1923 共享行 rowspan 串行所致）；citation json 与 page.md 均为 **United Kingdom（苏格兰人）**——以 page.md 为准，yaml 填 United Kingdom，幻灯片国籍行写 Scotland/United Kingdom |
| 争议呈现 | 诺奖当年即有争议；1950 独立复核确认四人各有贡献；1972 诺贝尔基金会官方承认漏 Best 是错误——**中立呈现，不站队** |
| 冲突烈度 | page.md 明载"Banting hated him passionately, and the two never spoke again"、1928 拒出席欢送晚宴；引用 Banting 观点时须标注是其单方叙述 |
| 1922 论文 | Macleod **拒绝署名**（认为属 B&B 的工作）——勿写成"抢署名" |
| Yale 报告 | 1921-12 美国生理学会：Banting 紧张失手、Macleod 接手收尾——Banting 视之为"夺功"，页面以 Banting 视角叙述，须带视角注记 |
| 全名 | John James Rickard Macleod；yaml/库内用 manifest 形式 `John Macleod (physiologist)`（消歧义括号是规范名一部分） |
| 鱼胰腺实验 | 1923 夏 St. Andrews（新不伦瑞克）海洋生物站，硬骨鱼胰岛与腺泡组织分离——证明胰岛素源于胰岛组织，勿写"鳕鱼"以外臆测物种 |
| Regius 教席 | 1928 继**其老师** MacWilliam 出任阿伯丁 Regius Professor of Physiology——"继任自己的老师"这一点常被漏写 |
| 提名人 | 丹麦诺奖得主 August Krogh（妻子患糖尿病、来访取法回丹麦）是 1923 提名人——可叙事，不入库关系 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| carbohydrate metabolism | 碳水化合物代谢 | 其毕生主线，勿窄化为"糖尿病" |
| insulin | 胰岛素 | 组织者/阐释者角色与其争议核心 |
| alcohol extraction | 酒精提取法 | 三人共同发展的高效提取路线 |
| teleost islet-acinar separation | 硬骨鱼胰岛-腺泡分离 | 定位胰岛素来源的关键实验 |
| gluconeogenesis | 糖异生 | 1932 论文主题；脂肪转化碳水假说终未获证 |
| Regius Professor of Physiology | 王家生理学讲席教授 | 阿伯丁 1928 |
| Medical Research Council (MRC) | 医学研究委员会 | 专利受让方 + 其 1929-33 成员，两处勿混 |
| Cameron Prize | 卡梅伦奖 | 爱丁堡大学治疗学奖，1923 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Mirage**（manifest 预分配）
- **风格**：迷离 / 反思 / 冷峻氛围
- **匹配理由**：海市蜃楼——荣誉与功劳的错位镜像：贡献半个世纪被遮蔽、又被独立复核还原的学者一生；冷色调氛围匹配苏格兰与阿伯丁的叙事底色。
- **本地路径**：`music_audio/inspiring-electronic/04-5gcb94jhG1I-Notan Nigres - Mirage (Audio).wav` → 复制为 `presentations/20th_century/John_Macleod_physiologist/Mirage.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；争议内容务必中立、忠实 page.md 叙述视角。**
