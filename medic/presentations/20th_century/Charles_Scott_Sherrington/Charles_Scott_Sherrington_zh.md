# 医学家立传提示词（Charles Scott Sherrington）

> **OpenMedic** 项目 · 20 世纪诺贝尔生理学或医学奖 **1932 年**得主（与 Edgar Adrian 共享）。
> 本文件是 Sherrington 的「人物专属立传提示词」，供后续 Beamer 立传 agent 直接使用；配套数据已按第三、四节入库 greatminds 库。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Charles Scott Sherrington（1857-11-27 ~ 1952-03-04，享年 94 岁），英国神经生理学家
- **气质关键词**：**synapse 一词的缔造者、神经整合之父、三位诺奖弟子的宗师** —— 1932 诺贝尔生理学或医学奖获奖理由（官方原文，逐字引用）：
  > "for their discoveries regarding the functions of neurons"（因其关于神经元功能的发现）
- **设计母题**：**突触之隙（the synaptic gap）**。两枚神经元之间那一道极窄的间隙——「相邻而不相连」的信号传递点，正是 Sherrington 命名 synapse 的地方，也是本篇的视觉隐喻。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Charles_Scott_Sherrington/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `Physicist_Bio_Prompt_Template.md` 第三章八步流程：下载核对 → 建目录 → 复制 Makefile → 收集图片 → 研究领域入库 → 社会关系入库 → 编写 Beamer → 布局检查 + 史实审查。
> **第 0/1/2/3 步按 medic 路径执行**：页面用 `medic/presentations/pages/20th_century/Charles_Scott_Sherrington/`；Makefile 复制后设 `MAIN=Charles_Scott_Sherrington_zh`；BGM 复制到本目录（见第九节）。
> 数据库两步（第 4/4.5 步）**已完成**，见第三、四节；执行 agent 只需做 Beamer 与目检。

## 三、研究领域梳理 + 入库 【已入库，与 yaml 完全一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | neurophysiology | 神经生理学 | 1932 诺奖核心：神经元功能、脊髓反射 | 核心页 |
| 1 | physiology | 生理学 | 剑桥生理学出身、「英国生理学之父」Foster 门下 | 早年页 |
| 2 | histology | 组织学 | 1881 医学大会狗脑半球组织学检查（首篇论文） | 早年页 |
| 3 | pathology | 病理学 | 布朗研究所/利物浦时期病理工作 | 任职页 |

## 四、社会关系梳理 + 入库 【已入库，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Michael Foster | 师→生（生理学导师） | 剑桥「英国生理学之父」，生理学导师 |
| advisor-student | John Newport Langley | 师→生（另一导师） | 剑桥另一导师，1884 合发其首篇论文 |
| advisor-student | John Farquhar Fulton | 生（Sherrington→学生） | 博士生（infobox 明载） |
| advisor-student | John Carew Eccles | 生（Sherrington→学生） | 学生，后获 1963 诺贝尔生理学奖 |
| advisor-student | Howard Florey | 生（Sherrington→学生） | 学生，后获 1945 诺贝尔生理学奖 |
| advisor-student | Ragnar Granit | 生（Sherrington→学生） | 学生，后获 1967 诺贝尔生理学奖 |
| advisor-student | Wilder Penfield | 生（Sherrington→学生） | 牛津弟子，引其入脑研究 |
| influence | David Ferrier | 无向 | 其英雄，大脑功能定位先驱，1906 书题献 |
| influence | Harvey Cushing | 无向 | 影响的美国脑外科先驱 |
| spouse | Ethel Mary Wright | 无向 | 1891-08-27 结婚，子 Carr；1933 卒 |
| co-honored | Edgar Adrian | 无向 | 1932 诺贝尔生理学或医学奖共享（神经元功能发现） |
| colleague | Charles Smart Roy | 无向 | 挚友，剑桥病理学教授，1885 同赴西班牙调查霍乱 |
| colleague | Friedrich Goltz | 无向 | 斯特拉斯堡共事，名言「凡事唯最优者足矣」 |
| colleague | Rudolf Virchow | 无向 | 1885 柏林验霍乱标本，荐其赴 Koch 处 |
| colleague | Robert Koch | 无向 | 随其习细菌学技术一年 |
| colleague | Derek Denny-Brown | 无向 | 牛津同事（1924-1928） |

**方向约定**：`advisor-student` + `direction: advisor` = 对方是导师；`direction: student` = 对方是学生；其余无向（from<to 自动归一）。

## 五、配色方案 【人物专属】

- **气质**：英伦的克制与深邃、皇家学会的庄重、94 岁一生的沉稳
- **主色**：`#16324F`（皇家深蓝，牛津与皇家学会）
- **香槟金**：`#D4B26A`（诺奖色）
- **badgeA-D 四分类色**：
  - `badgeSyn` 突触与反射 — 突触青 `#1B6B6B`
  - `badgeInteg` 整合作用 — 靛蓝 `#3B4E8C`
  - `badgeOx` 牛津岁月 — 深酒红 `#6E1E2B`
  - `badgeArt` 艺术与诗 — 暖赭 `#A8752F`
- **背景母题**：深蓝底上两枚神经元轮廓隔一细隙相对，隙间以微小亮点串联成弧——「突触之隙」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 突触之父 / Charles Scott Sherrington 1857–1952 + 四色 badge + 右上肖像 + 国籍行（United Kingdom）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Islington/Ipswich、剑桥/圣托马斯医院、任职、荣誉）
03  核心贡献概览 — 脊髓反射 / 交互神经支配 / 突触 / 本体感受
04  出身之谜 (1857–1876) — 官方传记与史学考证的分歧（Caleb Rose 之家、缪勒《生理学要素》启蒙）
05  剑桥岁月 (1876–1885) — Foster/Langley 门下、1881 Natural Sciences Tripos 双一等、Ipswich Town 足球
06  第七届国际医学大会 (1881) — Goltz vs Ferrier 之争、狗脑半球组织学检查、1884 首篇论文
07  欧陆游学 (1884–1886) — Goltz 处斯特拉斯堡、西班牙霍乱调查（未遇 Cajal）、Virchow 引荐 Koch 处一年
08  布朗研究所 (1891–1895) — 皮节图谱、1892 肌梭与牵张反射发现
09  利物浦岁月 (1895–1913) — Holt 讲席、交互神经支配、1897 Croonian 讲座与 synapse 命名
10  《神经系统的整合作用》(1906)（核心贡献页）— 耶鲁 Silliman 讲座合成、神经元学说定谳、题献 Ferrier
11  牛津 Waynflete 讲席 (1913–1936) — 全票当选、弟子群像（Eccles/Granit/Florey 三诺奖）、一战兵工厂疲劳研究
12  1932 诺贝尔奖 — 与 Adrian 共享、Copley 1927 / OM 1924 / 皇家学会会长 1920-25
13  诗人与哲人 — 1925 诗集、Gifford 讲座《人论其本性》(1940)、「百万倍的民主」神经元群像
14  遗产：以 Sherrington 命名的传统 — 突触/交互神经支配/本体感受进入教科书、Caius 学院彩窗、伊普斯维奇博物馆
15  结尾
```

## 七、特殊陷阱表 【★ 核心，从 page.md 提炼】

| 陷阱 | 说明 |
|------|------|
| 出身之谜 | 官方传记称父为乡村医生 James Norton Sherrington；正文考证 James 实为五金商/画材商且卒于 1848（其出生前 9 年），多位学者（Norrby 2016、Gardiner、Swazey）指其为 Ipswich 外科医师 Caleb Rose 之私生子——**不下定论**，表述用「官方传记与史学考证存在分歧」 |
| 获奖理由 | "for their discoveries regarding the functions of neurons"——**their**（与 Adrian 共享）；Sherrington 侧重点是中枢反射与整合，Adrian 是单纤维电记录 |
| synapse 命名 | 1897 年提出该词；词本身由古典学家 **A. W. Verrall** 建议——归属勿全归 Sherrington |
| proprioceptive | 「本体感受」一词亦为其所造（正文明载） |
| 三位诺奖弟子 | Eccles 1963 / Granit 1967 / Florey 1945——正文明载，师生传承页亮点 |
| 1885 未遇 Cajal | 正文明确 "did **not** meet Santiago Ramón y Cajal on this trip"——趣味事实，勿写成相见 |
| 皇家学会 | 第 43 任会长（1920-25），前任 J.J. Thomson、后任 Rutherford；FRS 1893 |
| 引语 | 正文有原话：Goltz 转述句、Oxford 教学论（1937-38 Gifford 讲座语境）、excitation-inhibition「不行动亦可如行动般主动」、晚年「old age isn't pleasant」——引原话须用这些，勿自造 |
| 兴奋-抑制 | 「不作为亦可如作为一样主动」（desistence from action...），1913 年「极性对立」表述——两条引语年份不同勿混 |
| 晚年 | 1951 入养老院（关节炎），1952-03-04 心脏衰竭猝逝于 Eastbourne，享年 94 |
| 学生边口径 | Fulton/Eccles/Florey 出自 infobox，Granit/Penfield 出自正文——均 page.md 明载；Denny-Brown 是同事非学生 |

## 八、术语清单 【6-10 条】

| 英文 | 中文 | 风险点 |
|------|------|------|
| synapse | 突触 | 1897 命名；词源建议者 Verrall |
| neuron doctrine | 神经元学说 | 其反射工作为哺乳类定谳 |
| reciprocal innervation | 交互神经支配 | 拮抗肌群兴奋-抑制 |
| stretch reflex | 牵张反射 | 1892 肌梭发现 |
| proprioceptive | 本体感受 | 其自造词 |
| dermatome | 皮节 | 布朗研究所时期图谱 |
| The Integrative Action of the Nervous System | 《神经系统的整合作用》 | 1906，Silliman 讲座 |
| Man on His Nature | 《人论其本性》 | 1940 Gifford 讲座，Jean Fernel 研究 |
| Waynflete Professor | 温弗利特讲席教授 | 牛津 1913 全票 |
| Copley Medal | 科普利奖章 | 1927 皇家学会 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**SEA** — Alex-Productions（manifest 预分配）
- **风格**：辽阔 / 沉静 / 探索感
- **匹配理由**：Sherrington 用半个世纪把脊髓反射写成一部「神经系统的整合史诗」——SEA 的辽阔沉静匹配其 94 岁一生的学术纵深，也匹配「百万倍的民主」中亿万神经元协作的图景；第二次使用该曲（首用 Golgi），同为神经结构主题遥相呼应。
- **本地路径**：`music_audio/` 下 SEA 曲目 → 复制为 `presentations/20th_century/Charles_Scott_Sherrington/SEA.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐 15 页时长。
