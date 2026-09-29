# 医学家立传提示词（Karl Landsteiner）

> 本文件是 OpenMedic 项目（OpenMathAI 诺贝尔生理学或医学奖人物史）20 世纪 1930 年得主 Karl Landsteiner 的人物专属立传提示词。
> 事实基准：`medic/presentations/pages/20th_century/Karl_Landsteiner/page.md`（唯一事实来源，metadata.json 仅作参考）。
> 结构对齐标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（11 节合并为 9 节）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Karl Landsteiner（1868-06-14 生于奥地利巴登（维也纳附近）~ 1943-06-26 逝于美国纽约，享年 75 岁）
- **气质关键词**：**血型的发现者、输血医学之父、脊髓灰质炎病毒的共同发现者** —— 1930 诺贝尔生理学或医学奖获奖理由（逐字引用 `medic/nobel_medicine_citations.json`）：
  > "for his discovery of human blood groups"（因其发现人类血型）
- **设计母题**：**凝集之网（agglutination）**。一滴血遇上另一滴血清，红细胞凝聚成肉眼可见的网格——1900/1901 年的观察把"输血为什么会死人"变成了可分型的问题。视觉语言：血滴相遇处的凝集颗粒网格、A/B/O 三色分型棋盘，比通用"显微镜"更贴合其核心发现。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Karl_Landsteiner/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）
- **关键时间线（身份信息页与时间轴素材，均出自 page.md）**：
  - 1868-06-14 生于巴登 bei Wien；1875（6 岁）丧父 Leopold（《新闻报》主编），与母亲 Fanny 相依
  - 1890 由犹太教改宗天主教
  - 1891 获维也纳大学 MD（在校期间发表饮食对血液组成影响的论文）
  - 1891-1893 游学：符兹堡（Hermann Emil Fischer）、慕尼黑（Bamberger）、苏黎世（Hantzsch）
  - 1897-11 至 1908 任维也纳大学病理解剖研究所助手（Weichselbaum 门下，75 篇论文、约 3600 例解剖）
  - 1900 发现两人血液接触发生凝集；1901 确定系血清所致并分出 A、B、O 三型
  - 1903 讲师资格（Habilitation，Weichselbaum 指导）
  - 1907 Ottenberg 于纽约 Mount Sinai 完成首例成功输血（基于其发现）
  - 1908-1920 任 Wilhelminenspital prosector；1911 任病理解剖副教授
  - 1908-1909 与 Popper 证实脊髓灰质炎传染性并分离病毒
  - 1916 娶 Leopoldine Helene Wlasto
  - 1920-1922 战后流离：海牙 St. Joannes de Deo 医院、结核素工厂
  - 1923 春 应 Simon Flexner 之邀移居纽约洛克菲勒研究所
  - 1926 获 Aronson 奖；1927 与 Levine 发现 M、N、P 血型（同年用于亲权鉴定）
  - 1929 入籍美国；1930 获诺贝尔生理学或医学奖
  - 1932 当选 NAS；1935 当选美国哲学学会；1937 与 Wiener 鉴定 Rh 因子、获 Cameron Prize
  - 1941 当选 ForMemRS；1943-06-26 卒于纽约
  - 1946 Lasker-DeBakey 追授；1958 追入 Polio Hall of Fame；2005 起 World Blood Donor Day 定于其生日 6-14

---

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章执行 Beamer 立传，**第 0/1/2/3 步按 medic 路径执行**：
> - 页面与元数据：`medic/presentations/pages/20th_century/Karl_Landsteiner/`（page.md / metadata.json / images.txt）
> - 目录创建：`medic/presentations/20th_century/Karl_Landsteiner/` 与 `images/`
> - Makefile：复制 medic 侧同结构模板，设 `MAIN=Karl_Landsteiner_zh`
> - 肖像：images.txt 含童年照/实验室照缩略 URL（250px 改 500px）；正式肖像可经 Wikipedia REST API 查 infobox 原图名；404 用 Commons `Special:FilePath` 回退；均失败用装饰圆占位
> 每完成一步汇报，溢出即修（make → pdftoppm 逐页目检）。

---

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | immunology | 免疫学 | 诺奖核心：凝集素与血型分类（1901） | 核心页 |
| 1 | hematology | 血液学 | ABO 血型系统、MNP 血型（1927）、Rh 因子（1937） | 血型页 |
| 2 | virology | 病毒学 | 与 Popper/Levaditi 发现脊髓灰质炎病毒（1909） | 维也纳页 |
| 3 | serology | 血清学 | 免疫机制与抗体本质研究（维也纳 75 篇论文主线） | 病理页 |

---

## 四、社会关系梳理 + 入库 【人物专属】

> 与 `MySQL/data/Karl_Landsteiner.yaml` 完全一致；只收 page.md 明载的关系。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Hermann Emil Fischer | 师→生 | 1891-1893 符兹堡随其学化学（进修非博士导师；MD 为维也纳 1891） |
| advisor-student | Anton Weichselbaum | 师→生 | 维也纳病理解剖研究所共事十年，1903 讲师资格（Habilitation）导师 |
| colleague | Max von Gruber | 无向 | 卫生研究所助手，免疫机制与抗体研究的起点 |
| collaborator | Erwin Popper | 无向 | 1908-1909 共同证实脊髓灰质炎传染性并分离病毒 |
| collaborator | Constantin Levaditi | 无向 | 1909 共同发现脊髓灰质炎病毒 |
| collaborator | Alexander S. Wiener | 无向 | 1937 共同鉴定恒河猴因子（Rh factor） |
| collaborator | Philip Levine | 无向 | 1927 共同发现 M、N、P 血型，同年用于亲权鉴定 |
| spouse | Leopoldine Helene Wlasto | — | 1916 结婚，希腊正教背景后随夫入天主教 |
| parent-child | Leopold Landsteiner | — | 父，《新闻报》（Die Presse）主编，逝于其 6 岁时 |
| parent-child | Fanny Hess | — | 母（1837-1908），与其感情至笃 |

**不入库裁定**：Simon Flexner 系洛克菲勒研究所邀请发起者，无实质个人关系实载，不入库；Reuben Ottenberg 1907 年首例成功输血系"基于其发现"的他人成就，不入库；Eugen Bamberger、Arthur Rudolf Hantzsch 为游学教授（一笔带过），不入库；Jan Janský 仅 See also 提及，不入库。

---

## 五、配色方案 【人物专属】

- **气质**：冷峻、精确、血清管里的生死分界
- **主色**：血液深红 `#9E2B25`（与人物气质呼应——血型、输血、生命线）
- **诺奖色**：香槟金 `#D4AF37`
- **四分类色（badgeA-D）**：
  - `badgeA` 免疫学——凝集深红 `#B03A2E`
  - `badgeB` 血液学——血浆玫红 `#C25B4E`
  - `badgeC` 病毒学——灰质青 `#2E7D6B`
  - `badgeD` 血清学——血清淡金 `#C89B3C`
- **背景母题**：稀疏凝集颗粒网格与三色分型圆（对应"凝集之网"），badge 四色错落

### 5.1 医学家格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + 细边框 + 姓名小字注；无真实肖像用装饰圆占位并注明。
2. **封面有国籍**：底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（02 页）：左头像 + 右信息网格，含生卒、出生地、教育、师承、任职、荣誉、核心领域；事实取自 page.md infobox，不得杜撰。
4. **品牌口径统一**：结尾页底部品牌标注写 `OpenMathAI`；引号用半角 `" "`。
5. **获奖理由逐字引用** `medic/nobel_medicine_citations.json` 原文 + 中译，不得改写或扩写。

---

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input medic 封面模板）
01  封面 — 输血医学之父 / Karl Landsteiner 1868–1943 + 四色 badge + 右上头像 + 国籍行（Austria / United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、巴登、维也纳 MD 1891、洛克菲勒研究所、荣誉、核心领域）
03  核心贡献概览 — ABO 血型（1901）/ 脊灰病毒（1909）/ MNP 血型（1927）/ Rh 因子（1937）
04  维也纳早年（1868–1891）— 记者 Leopold 之子、六岁丧父、与母亲相依、维也纳大学 MD 1891
05  化学游学（1891–1893）— 符兹堡 Fischer、慕尼黑 Bamberger、苏黎世 Hantzsch
06  维也纳病理学年月（1897–1908）— Weichselbaum 门下 75 篇论文、约 3600 例解剖、1903 讲师资格
07  1900/1901 凝集反应（核心贡献页）— 两人血液相遇凝集、A/B/O 三型、同型输血安全
08  脊髓灰质炎病毒（1908–1909）— 与 Popper 证实传染性并分离病毒、1958 追入 Polio Hall of Fame
09  战后流离（1920–1922）— 海牙小医院、结核素工厂、五篇荷文论文
10  洛克菲勒岁月（1923–1943）— Flexner 邀请、免疫与过敏研究、1927 MNP 血型与 Levine
11  Rh 因子与晚年（1937）— 与 Wiener 鉴定恒河猴因子、1943 纽约逝世
12  荣誉与认可 — Nobel 1930、Aronson 1926、Cameron 1937、ForMemRS 1941、Lasker 1946 追授
13  遗产 — 输血医学之父、World Blood Donor Day（6-14 其生日）、万能供血者/受血者概念
14  结尾 — 一滴血的分型改变外科与急救
```

---

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方逐字为 "for his discovery of human blood groups"（人类血型的发现） |
| 独享年份 | 1930 年为独享，无共享得主 |
| 血型范围 | page.md 明载他鉴定的是 A、B、O 三组（当时他标注为 C）——勿自行补写"发现 AB 型"及其年份 |
| 年份双锚 | 1900 发现两人血液接触凝集，1901 确定系血清所致并分型——两句话术勿混 |
| 输血首例 | 首例成功输血是 Reuben Ottenberg 1907 年于纽约 Mount Sinai Hospital 基于其发现完成——勿写成 Landsteiner 本人实施 |
| 三组合作年份 | Rh 因子=1937 与 Wiener；脊灰病毒=1909 与 Levaditi+Popper；MNP=1927 与 Levine——搭档与年份勿串 |
| Cameron 奖年份 | 正文作 1937，infobox 作 1938——取正文 1937，陷阱表注明双值 |
| 国籍口径 | Nobel 官方口径两写 Austria + United States（1929 入籍，infobox Citizenship from 1929）；yaml 按总表 Austria 为主、United States 为辅；页面国籍行可双写 |
| 学位口径 | 博士为维也纳大学 MD 1891；符兹堡 1891-93 系化学进修（Emil Fischer 门下）非博士——Fischer 关系 note 已注明"非博士导师" |
| 宗教与诉讼 | 1890 年由犹太教改宗天主教；1937 年因被列入 Who's Who in American Jewry 提起诉讼（败）——页面上若提及须按正文一句客观处理，不展开 |
| 职业年表 | 1897-1908 病理解剖研究所（75 篇论文、约 3600 例解剖）；1908-1920 Wilhelminenspital prosector；1911 副教授；1923 春抵纽约洛克菲勒研究所 |
| 追授荣誉 | Lasker-DeBakey 1946 追授；Polio Hall of Fame 1958 追入；World Blood Donor Day 自 2005 年定在其生日 6-14 |
| metadata 噪声 | metadata 无导师/配偶/父母载；Fischer/Weichselbaum/父母/妻子均以 page.md 为准 |

---

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| agglutination | 凝集（反应） | 血型判定的现象基础 |
| agglutinin | 凝集素 | 血中的抗体成分 |
| ABO blood group system | ABO 血型系统 | 1901 建立分类 |
| Rhesus factor / Rh factor | 恒河猴因子 | 1937 与 Wiener 共同鉴定 |
| poliovirus | 脊髓灰质炎病毒 | 1909 共同发现 |
| transfusion medicine | 输血医学 | 其"父亲"称号领域 |
| serum | 血清 | 凝集反应的介质 |
| universal donor / recipient | 万能供血者/受血者 | O 阴性 / AB 的通俗说法 |
| prosector | 病理解剖员 | 维也纳与海牙职务名 |
| Habilitation | 讲师资格 | 1903 由 Weichselbaum 指导 |
| tuberculinum pristinum | 旧结核菌素 | 海牙工厂产品 |

---

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Nostalgia**（manifest 预分配）
- **匹配理由**：维也纳黄金年代的病理学走廊、战后流离与纽约新岸——"怀旧"气质匹配这条从奥匈帝国到洛克菲勒的世纪漂移线；旋律克制，贴合凝集反应背后冷静的分类学天才
- **本地路径**：`music_audio/` 下检索曲名（参照 `curated_tracks.md`），复制到 `medic/presentations/20th_century/Karl_Landsteiner/Nostalgia.wav`
- **时长**：曲长须 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐

