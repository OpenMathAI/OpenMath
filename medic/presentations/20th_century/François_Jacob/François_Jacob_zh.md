# 医学家立传提示词（François Jacob）

> 本文件是 OpenMedic 项目（OpenMathAI 诺贝尔生理学或医学奖人物史）20 世纪 1965 年得主 François Jacob 的人物专属立传提示词。
> 事实基准：`medic/presentations/pages/20th_century/François_Jacob/page.md`（唯一事实来源，metadata.json 仅作参考）。
> 结构对齐标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（11 节合并为 9 节）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：François Jacob（1920-06-17 生于法国南锡 ~ 2013-04-19 逝于巴黎，享年 92 岁）
- **气质关键词**：**操纵子模型的共同提出者、转录调控思想的奠基人、抵抗运动战士与科学散文家** —— 1965 年诺贝尔生理学或医学奖（与 Monod、Lwoff 共享）获奖理由（逐字引用 `medic/nobel_medicine_citations.json`）：
  > "for their discoveries concerning genetic control of enzyme and virus synthesis"（因其关于酶合成与病毒合成的遗传控制的发现）
- **设计母题**：**基因的开关（the genetic switch）**。阻遏蛋白扣在操纵基因上，乳糖一来便松手——生命第一次被表述为"可开可关的调控系统"。视觉语言：DNA 链上的开关拨杆、allolactose 松开阻遏物的瞬间。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/François_Jacob/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）
- **关键时间线（身份信息页与时间轴素材，均出自 page.md）**：
  - 1920-06-17 生于南锡（父 Simon 为商人；母 Thérèse，原姓 Franck；外祖父 Albert Franck 四星将军是其童年偶像）
  - 7 岁入 Lycée Carnot（自传里称之为"笼子"，就读十年）；1934 前后遭右翼青年敌视
  - 母系为世俗犹太人；行过成人礼后不久成为无神论者
  - 恐惧 Polytechnique 两年预备的严苛，改学医（一次手术观摩坚定选择）
  - 1940 德占法国期间赴英加入自由法国第 2 装甲师医疗连（其时仅完成二年级学业）
  - 1944 德军空袭中负伤；1944-08-01 回到解放的巴黎
  - 获解放十字（法国二战最高英勇勋章）、荣誉军团勋章、1939-1945 战争十字
  - 战后回医学院研究短杆菌酪肽（tyrothricin），1947 获医学博士学位（自评论文是"复制美国工作"）
  - 入 Cabanel 中心（后承接种青霉素生产的兵工厂改造合同，未果）
  - 与音乐会钢琴家 Lise Bloch 相恋结婚，育四子女；Lise 1983 卒；1999 娶 Geneviève Barrier
  - 进入巴斯德研究所；1958 Monod 对妻子说"我想我刚想出了什么重要的东西"
  - 1961 与 Monod 提出酶表达水平由 DNA 转录调控决定
  - lac 阻遏物模型：阻遏蛋白结合操纵基因、allolactose 解除抑制的反馈回路
  - 1960 操纵子论文（与 Perrin、Sánchez、Monod）
  - 1962 获孟德尔奖章、Charles-Leopold Mayer 大奖；1964 当选美国艺术与科学院
  - 1965 与 Monod、Lwoff 共享诺贝尔奖
  - 1969 当选美国 NAS 与美国哲学学会；1973 当选皇家学会外籍会员（ForMemRS）
  - 1996 获首届 Lewis Thomas Prize（科学写作）；同年当选法兰西学术院 38 号席
  - 著作：《细菌的性与遗传》（1961，与 Wollman）、《生命的逻辑》、《内在雕像》（自传）等
  - 2013-04-19 卒于巴黎

---

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章执行 Beamer 立传，**第 0/1/2/3 步按 medic 路径执行**：
> - 页面与元数据：`medic/presentations/pages/20th_century/François_Jacob/`（page.md / metadata.json / images.txt）
> - 目录创建：`medic/presentations/20th_century/François_Jacob/` 与 `images/`
> - Makefile：复制 medic 侧同结构模板，设 `MAIN=François_Jacob_zh`
> - 肖像：优先 images.txt 缩略 URL（250px 改 500px，curl 加 `-A "Mozilla/5.0"`，file 验证）；404 用 Commons `Special:FilePath` 回退；均失败用装饰圆占位
> 每完成一步汇报，溢出即修（make → pdftoppm 逐页目检）。

---

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | molecular biology | 分子生物学 | 诺奖核心：转录调控与操纵子模型（infobox Fields） | 核心页 |
| 1 | genetics | 遗传学 | 细菌遗传学、溶原性、操纵基因 | 研究页 |
| 2 | microbiology | 微生物学 | infobox field_of_work；E. coli 与噬菌体实验系统 | 研究页 |
| 3 | developmental biology | 发育生物学 | 其工作"为新兴的分子发育生物学提供动力"（正文语） | 影响页 |

---

## 四、社会关系梳理 + 入库 【人物专属】

> 与 `MySQL/data/François_Jacob.yaml` 完全一致；只收 page.md 明载的关系。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Jacques Monod | 无向 | 1965 诺贝尔生理学或医学奖共享（酶与病毒合成的遗传控制） |
| co-honored | André Michel Lwoff | 无向 | 1965 诺贝尔生理学或医学奖共享（酶与病毒合成的遗传控制） |
| spouse | Lise Bloch | — | 音乐会钢琴家，育四子女，1983 去世 |
| spouse | Geneviève Barrier | — | 1999 结婚 |
| parent-child | Simon Jacob | — | 父，商人 |
| parent-child | Thérèse Franck | — | 母（世俗犹太家庭） |

**不入库裁定**：★Lise Bloch 姓 Bloch，与同批 Konrad Emil Bloch 无亲属关系——两 yaml 互不引用，防混同；外祖父 Albert Franck（四星将军、童年偶像）系 grandparent 不入白名单；Élie Wollman（合著《细菌的性与遗传》）与 Arthur Pardee（PaJoMo 1958 论文）仅见于文献列表，正文未载个人关系叙事，不入库（Pardee 有库内存量 id=3856，上报主控留意）；子女四人仅记数量。

## 五、配色方案 【人物专属】

- **气质**：战士的果决与思想者的澄澈——从战场伤员到"基因开关"的发现者
- **主色**：抵抗深蓝 `#1F3A5F`（与人物气质呼应——自由法国的蓝、巴斯德研究所的夜）
- **诺奖色**：香槟金 `#D4AF37`
- **四分类色（badgeA-D）**：
  - `badgeA` 分子生物学——开关金 `#C89B3C`
  - `badgeB` 遗传学——基因青 `#2E7D6B`
  - `badgeC` 微生物学——培养皿蓝 `#3A6FA8`
  - `badgeD` 战士与作家——洛林红 `#8C1F28`
- **背景母题**：DNA 双链上的开关拨杆与星光点（对应"基因的开关"），badge 四色错落

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
01  封面 — 基因开关的发现者 / François Jacob 1920–2013 + 四色 badge + 右上头像 + 国籍行（France）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、南锡、巴黎医学院、巴斯德研究所、荣誉、核心领域）
03  核心贡献概览 — 操纵子模型 / 转录调控 / 溶原性与原病毒 / 科学写作
04  南锡与"笼子"（1920–1940）— Lycée Carnot 十年、外祖父偶像、弃理工从医
05  自由法国战士（1940–1944）— 第 2 装甲师医疗连、1944 负伤、解放十字/军团勋章/战争十字
06  从军医到研究者（1945–1950）— tyrothricin、1947 医学博士（"复制美国工作"的自嘲）、Cabanel 中心
07  巴斯德研究所岁月（1950s）— 与 Monod 的相遇、1958 "我刚想出了什么重要的东西"
08  操纵子模型（核心贡献页一）— 1960 论文；结构基因/调节基因/操纵基因
09  阻遏物与反馈（核心贡献页二）— lac repressor、allolactose 解除抑制、转录调控普适化
10  1965 诺贝尔奖 — 三人共享同一句理由；与 Lwoff（原病毒）和 Monod（酶调控）的分工
11  荣誉与认可 — 1962 Mendel/Mayer、1969 NAS/APS、1973 ForMemRS、1996 Lewis Thomas Prize 与法兰西学术院
12  科学散文家 — 《生命的逻辑》《内在雕像》《Of Flies, Mice and Men》；"a cage" 的文学笔触
13  家庭 — Lise Bloch（四子女，1983 卒）、1999 再婚 Geneviève Barrier
14  结尾 — 开关之后：一个可以被"调控"理解的生命世界
```

---

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方逐字为 "for their discoveries concerning genetic control of enzyme and virus synthesis"——注意 **their**（三人共享）；页面链接语境 enzyme→转录、virus synthesis→原病毒，勿直译成"酶与病毒的合成"歧义句 |
| 生卒双值 | metadata 死亡日期双值 ["2013-04-19","2013-04-20"]——取正文/infobox **2013-04-19** |
| 入所年份 | Monod 页正文作 "Monod joined the Pasteur Institute in 1943 and Jacob in 1949"；Jacob 页正文未给年份——页面写"战后加入巴斯德研究所"即可 |
| Lise Bloch 混同 | 首妻姓 Bloch，与同批得主 Konrad Emil Bloch **无亲属关系**——两篇 yaml 互不引用；页面若并列出现需加注 |
| Wollman/Pardee | 合著者仅见于文献列表，正文未载关系叙事——不入库（Pardee 库内存量 id=3856 上报主控）；《细菌的性与遗传》作著作页素材 |
| 战功勋章 | 解放十字（法国二战最高英勇荣誉）与 Légion d'honneur、Croix de guerre 并列——三枚勿混层级 |
| 医学博士论文 | 他自评 "replicating American work"——引用自嘲需注明是其自述 |
| 外祖父 | Albert Franck 四星将军、童年 role model——页面可一句，不入关系 |
| metadata 噪声 | metadata occupations 混入 film producer/editor/director（存疑）——primary 按 biologist/geneticist，页面按正文写"生物学家" |
| bibliography 年份 | 操纵子论文 1960（C.R. Acad. Sci. Paris 250）、综述 1961 JMB——与"1961 提出"表述并存，引用注明论文年份 |

---

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| operon | 操纵子 | 1960 论文核心词 |
| operator | 操纵基因 | 与"操作子"混淆风险 |
| repressor | 阻遏物（蛋白） | lac 阻遏物 |
| allolactose | 别乳糖 | 解除阻遏的诱导物 |
| transcriptional regulation | 转录调控 | 诺奖思想核心 |
| provirus | 原病毒 | Lwoff 侧关键词（链接语境） |
| tyrothricin | 短杆菌酪肽 | 战后研究的抗生素 |
| lysogeny / lysogenic | 溶原性 | Jacob-Sussman-Monod 1962 论文语境 |
| ForMemRS | 皇家学会外籍会员 | 1973 |
| Compagnon de la Libération | 解放战友勋章 | 法国二战最高英勇荣誉 |

---

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Eternals**（manifest 预分配）
- **匹配理由**：操纵子思想贯穿此后全部分子生物学——"永恒"贴合其遗产的时间尺度；也呼应这位战士-科学家跨越战场与实验室的一生；音乐宜深远辽阔
- **本地路径**：`music_audio/` 下检索曲名（参照 `curated_tracks.md`），复制到 `medic/presentations/20th_century/François_Jacob/Eternals.wav`
- **时长**：曲长须 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐

