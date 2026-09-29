# 医学家立传提示词（Edward B. Lewis）

> 本文件是 OpenMedic 项目（OpenMathAI 诺贝尔生理学或医学奖人物史）20 世纪 1995 年得主 Edward B. Lewis 的人物专属立传提示词。
> 事实基准：`medic/presentations/pages/20th_century/Edward_B._Lewis/page.md`（唯一事实来源，metadata.json 仅作参考）。
> ★ 1995 年为三人共享，另两位 Christiane Nüsslein-Volhard 与 Eric F. Wieschaus 属 med-batch-33，co-honored 边两侧各自落地。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Edward Butts Lewis（1918-05-20 生于美国宾夕法尼亚州威尔克斯-巴里 ~ 2004-07-21 逝于加州帕萨迪纳，享年 86 岁）
- **气质关键词**：**双胸复合群（Bithorax complex）的发现者、同源异形基因研究的奠基人、演化发育生物学（evo-devo）的开创者之一** —— 1995 年诺贝尔生理学或医学奖（与 Nüsslein-Volhard、Wieschaus 共享）获奖理由（逐字引用 `medic/nobel_medicine_citations.json`）：
  > "for their discoveries concerning the genetic control of early embryonic development"（因其关于早期胚胎发育的遗传控制的发现）
- **设计母题**：**长出第二对翅膀的果蝇（the four-winged fly）**。Bithorax 突变让后胸长成本该属于前胸的结构——一组基因像一串沿染色体排布的"身体坐标"。视觉语言：双翅果蝇的剪影、染色体上按体节排开的基因珠链。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Edward_B._Lewis/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）
- **关键时间线（身份信息页与时间轴素材，均出自 page.md）**：
  - 1918-05-20 生于威尔克斯-巴里（父 Edward Butts Lewis 为钟表匠珠宝商，与本人同名；母 Laura Mary，原姓 Histed；★出生证误把 Jr. 写成 "B."——本应为小爱德华）
  - E. L. Meyers 高中毕业
  - 1939 明尼苏达大学生物统计学 BA（在 C. P. Oliver 实验室做果蝇）
  - 1939 入加州理工；1942 博士（导师 Alfred Sturtevant；论文：果蝇串联重复的遗传与细胞学分析）
  - 1942 入美国陆军航空队气象训练项目，1943 获气象学 MS；赴夏威夷与冲绳做了四年天气预报
  - 校长 Robert A. Millikan 承诺战后保留加州理工教职；1946 回任（承担遗传学导论课实验助教）
  - 1956 升教授；1966 任 Thomas Hunt Morgan 生物学讲席教授
  - 1946 结识 Pamela Harrah（1925-2018；斯坦福出身、发现 Polycomb 突变体的艺术家），结缡；三子 Glenn、Hugh、Keith；Pam 后因感染致局部偏瘫
  - 1940s-50s 拟等位基因（pseudoallelism）奠基研究（white/apricot 座位可重组分离）——挑战"基因不可分"的经典观
  - 发现果蝇 Bithorax complex（同源异形基因群）并阐明其功能；发展互补测验（complementation test）
  - 奠基演化发育生物学（evo-devo）；为动物发育保守机制的现代理解铺路
  - 1950s 辐射致癌研究：审阅广岛/长崎幸存者、放射科医生与 X 光暴露患者的病历，结论"辐射的健康风险被低估"；主张线性无阈值（LNT）模型；1957 向国会原子能委员会作证（《Science》等刊文）
  - 荣誉：NAS 1968、Umeå 大学荣誉博士 1981、Thomas Hunt Morgan 奖章 1983、Gairdner 国际奖 1987、Wolf 医学奖 1989、Rosenstiel 奖 1990、国家科学奖章 1990、Lasker 基础医学研究奖 1991、Louisa Gross Horwitz 奖 1992、明尼苏达荣誉博士 1993、诺贝尔奖 1995、ForMemRS
  - 1995-12-08 诺贝尔演讲《The Bithorax Complex: The First Fifty Years》
  - 生活：晨练、安纳森餐膳俱乐部午餐、午休、夜间工作；吹长笛、室内乐、歌剧、慢跑游泳
  - 2004-07-21 卒于帕萨迪纳

---

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章执行 Beamer 立传，**第 0/1/2/3 步按 medic 路径执行**：
> - 页面与元数据：`medic/presentations/pages/20th_century/Edward_B._Lewis/`（page.md / metadata.json / images.txt）
> - 目录创建：`medic/presentations/20th_century/Edward_B._Lewis/` 与 `images/`
> - Makefile：复制 medic 侧同结构模板，设 `MAIN=Edward_B._Lewis_zh`
> - 肖像：正文含 1986 年肖像缩略 URL（250px 改 500px，curl 加 `-A "Mozilla/5.0"`，file 验证）；404 用 Commons `Special:FilePath` 回退；均失败用装饰圆占位
> 每完成一步汇报，溢出即修（make → pdftoppm 逐页目检）。

---

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | genetics | 遗传学 | infobox Fields；诺奖核心：同源异形基因与 Bithorax complex | 核心页 |
| 1 | developmental biology | 发育生物学 | infobox Fields；早期胚胎发育的遗传控制 | 核心页 |
| 2 | embryology | 胚胎学 | infobox Fields；体节坐标与同源异形转化 | 核心页 |
| 3 | radiation genetics | 辐射遗传学 | 1950s 辐射致癌与 LNT 模型（与 Muller 篇呼应勿混写） | 辐射页 |

---

## 四、社会关系梳理 + 入库 【人物专属】

> 与 `MySQL/data/Edward_B._Lewis.yaml` 完全一致；只收 page.md 明载的关系。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Christiane Nüsslein-Volhard | 无向 | 1995 诺贝尔生理学或医学奖共享（早期胚胎发育的遗传控制） |
| co-honored | Eric F. Wieschaus | 无向 | 1995 诺贝尔生理学或医学奖共享（早期胚胎发育的遗传控制） |
| advisor-student | Alfred Sturtevant | 师→生 | 加州理工博士导师（1942，摩尔根学派传人，库内 id=5342） |
| advisor-student | Mark M. Davis | 生→ | 博士生（infobox 明载） |
| colleague | Clarence Paul Oliver | 无向 | 明尼苏达大学本科在其实验室做果蝇（库内 id=5880；本人后为 Muller 博士生，勿混两条边） |
| spouse | Pamela Harrah | — | 艺术家兼遗传学者，Polycomb 突变体的发现者（1925-2018） |
| parent-child | Glenn Lewis | — | 子 |
| parent-child | Hugh Lewis | — | 子 |
| parent-child | Keith Lewis | — | 子 |
| parent-child | Laura Mary Lewis | — | 母（原姓 Histed） |

**不入库裁定**：★父与本人同名（均 Edward Butts Lewis，钟表匠珠宝商）——同名人建 parent-child 会自环，不入库、页面仅文字提及（循 Eijkman 父子同名先例）；Robert A. Millikan（承诺教职的校长，库内有物理学家记录）系职务承诺不入库；Elliot Meyerowitz（2001 口述史采访者）、Ernest Sternglass/Alice Stewart/John Gofman（辐射论战人物）不入库。

---

## 五、配色方案 【人物专属】

- **气质**：半个世纪只盯着一种小虫的安静天才——从拟等位基因到体节坐标
- **主色**：双胸绛红 `#6E2B2B`（与人物气质呼应——果蝇复眼的石榴色与 Bithorax 突变体的奇观）
- **诺奖色**：香槟金 `#D4AF37`
- **四分类色（badgeA-D）**：
  - `badgeA` 遗传学——拟等位金 `#C89B3C`
  - `badgeB` 发育生物学——体节青 `#2E7D6B`
  - `badgeC` 胚胎学——胚胎蓝 `#3A6FA8`
  - `badgeD` 辐射遗传学——警示橙 `#B4632A`
- **背景母题**：染色体珠链与双翅果蝇剪影（对应"体节坐标"），badge 四色错落

### 5.1 医学家格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + 细边框 + 姓名小字注；无真实肖像用装饰圆占位并注明。
2. **封面有国籍**：底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（02 页）：左头像 + 右信息网格，含生卒、出生地、教育、师承、任职、荣誉、核心领域；事实取自 page.md infobox，不得杜撰。
4. **品牌口径统一**：结尾页底部品牌标注写 `OpenMedic`；引号用半角 `" "`。
5. **获奖理由逐字引用** `medic/nobel_medicine_citations.json` 原文 + 中译，不得改写或扩写。

---

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input medic 封面模板）
01  封面 — 体节坐标的绘制者 / Edward B. Lewis 1918–2004 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、威尔克斯-巴里、明尼苏达/加州理工、Sturtevant 门下、Morgan 讲席教授、荣誉、核心领域）
03  核心贡献概览 — Bithorax complex / 同源异形基因 / 拟等位基因与互补测验 / 辐射-LNT 研究
04  威尔克斯-巴里与明尼苏达（1918–1939）— 钟表匠之家、出生证误写 "B."、Oliver 实验室的果蝇
05  Sturtevant 门下（1939–1942）— 三年读完博士；1942 气象训练、夏威夷/冲绳四年预报员
06  Millikan 的承诺与回任（1946–1966）— 助教、1956 教授、1966 Morgan 讲席教授
07  拟等位基因（1940s-50s）— white/apricot 座位可重组：基因并非不可分（与 Muller 诱变互为呼应）
08  Bithorax complex（核心贡献页一）— 同源异形基因群的发现
09  体节的坐标（核心贡献页二）— 基因沿染色体的排序对应身体前后轴
10  互补测验与 evo-devo — complementation test 的发展；演化发育生物学的奠基
11  辐射与 LNT — 广岛/长崎幸存者病历、"辐射的健康风险被低估"、1957 国会作证
12  荣誉与认可 — Morgan 奖章 1983、Gairdner 1987、Wolf 1989、NMS 1990、Lasker 1991、Horwitz 1992、Nobel 1995
13  Pamela — 艺术家妻子与 Polycomb 突变体的发现者
14  结尾 — 1995-12-08 演讲《Bithorax Complex: The First Fifty Years》；2004 卒于帕萨迪纳
```

---

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方逐字为 "for their discoveries concerning the genetic control of early embryonic development"——三人共享（另两位属 med-batch-33，co-honored 边两侧各自落地） |
| 分工表述 | Lewis=Bithorax complex 与同源异形基因（成体体节转化）；Nüsslein-Volhard/Wieschaus=胚胎致死突变筛选——三条线共用一句理由，页面须各表其功 |
| 父子同名 | 父 Edward Butts Lewis 与本人同名——parent-child 会自环，**不入库**（循 Eijkman 先例）；出生证误写 "B."（本应 Jr.）是正文明载的趣味点 |
| 姓名缩写 | "B." 系出生证笔误的非缩写中名——勿杜撰 "Butts" 之外的展开，页面可按正文讲这个故事 |
| 学位顺序 | 明尼苏达 BA 1939（生物统计学）→ Caltech PhD 1942 → 气象学 MS 1943（军队项目）——MS 晚于 PhD 属事实，勿"修正" |
| Morgan 讲席 | 1966 任 Thomas Hunt Morgan 生物学讲席教授；1983 又获 Thomas Hunt Morgan 奖章——两个 Morgan 勿混 |
| C.P. Oliver 关系 | 本科实验室之主（colleague）；Oliver 本人后来是 Muller 的博士生（Muller 篇已建 advisor-student 边）——两条边分属两对关系，勿混 |
| 辐射研究 | Lewis 的 LNT 立场与 Muller 呼应但两人无共事记载——**不得跨篇建边**；1957 国会作证与《Science》发文可写 |
| 引语红线 | "health risks from radiation had been underestimated" 为 page.md 英文原句可引；"linear with no threshold" 系正文链接语；其余议论不杜撰 |
| metadata 噪声 | metadata 无配偶/子女载；妻子与三子（Glenn/Hugh/Keith）、父母以 page.md 为准；生卒 1918-05-20 / 2004-07-21 两处一致 |

---

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| Bithorax complex | 双胸复合群 | 核心词（BX-C） |
| homeotic gene | 同源异形基因 | 身份转换的基因 |
| pseudoallelism | 拟等位基因现象 | 1940s-50s 奠基工作 |
| complementation test | 互补测验 | 其发展的经典方法 |
| Drosophila melanogaster | 黑腹果蝇 | 终身实验材料 |
| intragenic recombination | 基因内重组 | 挑战经典基因观 |
| Polycomb | Polycomb（多梳）突变体 | 妻子 Pamela Harrah 发现 |
| linear no-threshold model | 线性无阈值模型（LNT） | 与 Muller 呼应 |
| evo-devo | 演化发育生物学 | 其奠基领域 |
| Thomas Hunt Morgan Professor | 摩根讲席教授 | 1966 Caltech 讲席 |

---

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Savage**（manifest 预分配）
- **匹配理由**：在一种小虫身上守了五十年的猎手——"野性"贴合果蝇遗传学从突变 wilderness 中驯出秩序的历程；亦呼应辐射论战里独持异议的锋芒
- **本地路径**：`music_audio/` 下检索曲名（参照 `curated_tracks.md`），复制到 `medic/presentations/20th_century/Edward_B._Lewis/Savage.wav`
- **时长**：曲长须 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐
