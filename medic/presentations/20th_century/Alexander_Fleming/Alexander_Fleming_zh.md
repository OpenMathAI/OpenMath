# 医学家立传提示词（Alexander Fleming）

> 本文件是 OpenMedic 项目（OpenMathAI 诺贝尔生理学或医学奖人物史）20 世纪 1945 年得主 Alexander Fleming 的人物专属立传提示词。
> 事实基准：`medic/presentations/pages/20th_century/Alexander_Fleming/page.md`（唯一事实来源，metadata.json 仅作参考）。
> 结构对齐标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（11 节合并为 9 节）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Sir Alexander Fleming（1881-08-06 生于苏格兰艾尔郡达尔维尔 ~ 1955-03-11 逝于伦敦，享年 73 岁，骨灰葬圣保罗大教堂）
- **气质关键词**：**青霉素的发现者、溶菌酶的发现者、抗生素时代的开启人** —— 1945 年诺贝尔生理学或医学奖（与 Florey、Chain 共享）获奖理由（逐字引用 `medic/nobel_medicine_citations.json`）：
  > "for the discovery of penicillin and its curative effect in various infectious diseases"（因其发现青霉素及其对多种传染病的疗效）
- **设计母题**：**培养皿上的抑菌圈（the killing zone）**。一枚霉菌孢子落进金黄色葡萄球菌的培养皿，周围现出透明的环——"那是怎么回事（That's funny）"。视觉语言：培养皿中透明的抑菌环、霉菌与菌落的对峙。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Alexander_Fleming/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）
- **关键时间线（身份信息页与时间轴素材，均出自 page.md）**：
  - 1881-08-06 生于达尔维尔附近 Lochfield 农场（父 Hugh 为农夫，再婚时 59 岁，Alexander 7 岁时丧父）
  - Loudoun Moor School、Darvel School、Kilmarnock Academy 奖学金；迁伦敦入 Royal Polytechnic Institution
  - 航运公司做工四年；1901 入圣玛丽医院医学院
  - 1900-1914 伦敦苏格兰志愿军团士兵（步枪队）
  - 1906 以优等获 MBBS；任 Almroth Wright 的助理细菌学家
  - 1908 获细菌学 BSc（金质奖章），任圣玛丽讲师至 1914
  - 一战任皇家陆军军医队军官（1914 中尉/1917 上尉），西线战场医院；1917《柳叶刀》发文论消毒剂之害
  - 1915-12-24 娶护士 Sarah Marion McElroy；1924 独子 Robert 出生
  - 1918 回圣玛丽；1928 当选伦敦大学细菌学教授
  - 1921-11 发现溶菌酶（1922-05-01 发表）；1932-10-18 皇家医学会主席演讲为其正名
  - 1928-09-03 返实验室发现青霉菌污染培养皿的抑菌现象；1929-03-07 命名 penicillin；1929 发表于《英国实验病理学杂志》
  - 1930-11-25 前学生 Paine 在谢菲尔德完成首例青霉素成功治疗
  - 1940 牛津团队（Florey/Chain）实现提纯；1941-08 Fleming 用牛津样品治愈 Harry Lambert 脑膜炎
  - 1943 FRS；1944 受封 Knight Bachelor（George VI）
  - 1945 与 Florey、Chain 共享诺贝尔奖；1945 与 Florey 共享爱丁堡 Cameron 奖
  - 1949 首妻去世；1953-04-09 娶希腊同事 Amalia Koutsouri-Vourekas
  - 1955-03-11 心脏病逝于伦敦

---

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章执行 Beamer 立传，**第 0/1/2/3 步按 medic 路径执行**：
> - 页面与元数据：`medic/presentations/pages/20th_century/Alexander_Fleming/`（page.md / metadata.json / images.txt）
> - 目录创建：`medic/presentations/20th_century/Alexander_Fleming/` 与 `images/`
> - Makefile：复制 medic 侧同结构模板，设 `MAIN=Alexander_Fleming_zh`
> - 肖像：正文含 1943 实验室照与 1945 领奖照缩略 URL（250px 改 500px，curl 加 `-A "Mozilla/5.0"`，file 验证）；404 用 Commons `Special:FilePath` 回退；均失败用装饰圆占位
> 每完成一步汇报，溢出即修（make → pdftoppm 逐页目检）。

---

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | bacteriology | 细菌学 | 诺奖核心：青霉素的发现与抑菌作用 | 核心页 |
| 1 | immunology | 免疫学 | 溶菌酶——首个天然免疫抗菌蛋白（infobox Fields 双列之一） | 溶菌酶页 |
| 2 | pharmacology | 药理学 | 抗生素治疗与耐药性警告 | 耐药页 |

---

## 四、社会关系梳理 + 入库 【人物专属】

> 与 `MySQL/data/Alexander_Fleming.yaml` 完全一致；只收 page.md 明载的关系。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Howard Florey | 无向 | 1945 诺贝尔生理学或医学奖共享（青霉素的发现及其疗效） |
| co-honored | Ernst Chain | 无向 | 1945 诺贝尔生理学或医学奖共享（青霉素的发现及其疗效） |
| colleague | Almroth Wright | 无向 | 圣玛丽医院预防接种科上司，疫苗疗法与免疫学先驱 |
| colleague | Leonard Colebrook | 无向 | 一战随其同赴布洛涅英军医院 |
| collaborator | V. D. Allison | 无向 | 研究学者，合作发表溶菌酶后续研究 |
| collaborator | Harold Raistrick | 无向 | 与其团队尝试青霉素化学提纯（未果） |
| advisor-student | Cecil George Paine | 生→ | 前学生，1930-11-25 完成首例青霉素成功治疗 |
| spouse | Sarah Marion McElroy | — | 1915 结婚，1949 去世 |
| spouse | Amalia Koutsouri-Vourekas | — | 1953 结婚，圣玛丽希腊裔同事 |
| parent-child | Robert Fleming | — | 独子（1924-2015），全科医生 |
| parent-child | Hugh Fleming | — | 父，农夫，Alexander 七岁时去世 |
| parent-child | Grace Stirling Morton | — | 母，邻家农夫之女 |

**不入库裁定**：兄 Tom（建议学医的医生）属 sibling 不入库；Merlin Pryce、Charles J. La Touche、Stuart Craddock、Keith Bernard Rogers、Harry Lambert 均系轶事人物不入库；Edward Abraham/Heatley 系牛津团队，与 Fleming 无直接个人关系行，归 Florey/Chain 篇。

## 五、配色方案 【人物专属】

- **气质**：邋遢的天才、培养皿边缘的偶然之光
- **主色**：霉菌深绿 `#33691E`（与人物气质呼应——青霉菌落、平板上的生命对峙）
- **诺奖色**：香槟金 `#D4AF37`
- **四分类色（badgeA-D）**：
  - `badgeA` 细菌学（青霉素）——抑菌圈透明金 `#C89B3C`
  - `badgeB` 免疫学（溶菌酶）——泪滴青 `#2E7D6B`
  - `badgeC` 药理学（耐药警告）——警示橙 `#B4632A`
  - `badgeD` 战地医学——军装褐 `#5C3A21`
- **背景母题**：培养皿同心环与散落菌落点（对应"抑菌圈"），badge 四色错落

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
01  封面 — 抗生素时代的开启人 / Alexander Fleming 1881–1955 + 四色 badge + 右上头像 + 国籍行（United Kingdom）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、达尔维尔、圣玛丽医院医学院、伦敦大学细菌学教授、荣誉、核心领域）
03  核心贡献概览 — 青霉素（1928）/ 溶菌酶（1921）/ 消毒剂之辩（1917）/ 耐药性警告
04  农场少年与圣玛丽（1881–1906）— 七岁丧父、叔叔遗产、兄长建议学医、1906 优等 MBBS
05  Wright 门下与一战（1906–1918）— 助理细菌学家、西线战场医院、1917《柳叶刀》论消毒剂之害
06  溶菌酶（1921–1922）— 鼻涕与眼泪的杀菌圈、"父亲般的爱"（1932 演讲引语）
07  1928-09 的培养皿（核心贡献页）— 度假归来、霉菌污染、"That's funny"
08  命名与冷遇（1929–1936）— 1929-03-07 命名 penicillin、两次报告无人问津、提纯屡败
09  牛津接棒与 Lambert 病例（1940–1942）— Florey/Chain 提纯、1941-08 脑膜炎治愈、The Times 与"Fleming myth"
10  大生产与 D-Day（1942–1944）— 青霉素委员会、盟军充足供应；专利风波引语
11  耐药性警告 — 1945-06-26 引语与诺奖演讲引语（少用、短用会催生耐药）
12  荣誉与认可 — Nobel 1945、FRS 1943、Knight Bachelor 1944、Cameron 1945、 Medal for Merit 等
13  神话与真相 — "Fleming myth" 自我命名、丘吉尔故事为假（"A wondrous fable"）、Henry Harris 链条句
14  结尾 — "single greatest victory ever achieved over disease"
```

---

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方逐字为 "for the discovery of penicillin and its curative effect in various infectious diseases"——三人共享同一句 |
| 日期双值 | 正文作 1928-09-03 度假返回后发现污染培养皿；其自述引语作 "September 28, 1928"——页面取正文 09-03，引语页须注明为本人回忆口径 |
| 霉菌学名沿革 | 疑为 P. chrysogenum→La Touche 定 P. rubrum→后改正 P. notatum→再定 P. chrysogenum→2011 定为 **P. rubens**——勿写死单一学名 |
| 发现链定位 | Fleming 发现并命名（1929-03-07），提纯与成药归牛津团队（Florey/Chain/Heatley）；Henry Harris 链条句 "Without Fleming, no Chain; without Chain, no Florey; without Florey, no Heatley; without Heatley, no penicillin." 是最安全的分工表述 |
| 首例治疗 | 首例成功治疗是前学生 Cecil George Paine（1930-11-25，结膜炎）；Fleming 本人 1929 对 Craddock 的试验无效（流感杆菌不敏感）——勿写成 Fleming 治好第一人 |
| "Fleming myth" | The Times 报道 Lambert 病例只提 Fleming（Florey 禁止牛津团队曝光）——Fleming 自称此为 "the Fleming myth"；叙事页须点破 |
| 丘吉尔故事 | "父亲救丘吉尔→丘吉尔父资助学费"与"青霉素救丘吉尔"（实为磺胺 M&B 693）均为假，Fleming 称 "A wondrous fable"——**禁写** |
| 引语可用 | "That's funny"、"One sometimes finds what one is not looking for..."、耐药警告 1945-06-26 与诺奖演讲引语、"I found penicillin and have given it free..."（专利风波）——均为 page.md 载英文原文，可引 |
| 溶菌酶 | 1921-11 发现、notebook "Staphyloid coccus from A.F.'s nose"；诺奖演讲自认 "Penicillin was not the first antibiotic I happened to discover"——溶菌酶须有独立页 |
| metadata 噪声 | metadata 死亡日期双值 ["1955-03-11","1955-03-00"]——取 1955-03-11（正文与 infobox 一致） |
| Cameron 双奖 | 1945 Cameron 奖系与 Florey 共享——与诺奖 co-honored 同人不同奖，不加第二行（uq_rel 按 type 去重），陷阱表注明即可 |
| 荣誉年份 | FRS 1943、Knight Bachelor 1944（George VI）、Cameron 1945、Actonian 1949、Alfonso X 大十字 1948、爱丁堡大学 Rector 1951——勿串 |

---

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| penicillin | 青霉素 | 1929-03-07 命名 |
| lysozyme | 溶菌酶 | 1921 发现，天然免疫首批抗菌蛋白 |
| benzylpenicillin / penicillin G | 苄青霉素 | 后来的正式名 |
| killing zone | 抑菌（杀菌）圈 | 培养皿透明环 |
| Gram-positive / Gram-negative | 革兰阳性/阴性 | 敏感谱差异 |
| antibiotic resistance | 抗生素耐药性 | 其早期警告 |
| antiseptic | 消毒剂/防腐剂 | 1917 论战对象 |
| Micrococcus lysodeikticus | 溶壁微球菌 | 1972 改名 M. luteus |
| Inoculation Department | 预防接种科 | 圣玛丽 Wright 部门 |
| mould juice | "霉菌汁" | penicillin 命名前的俗称 |

---

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Mirage**（manifest 预分配）
- **匹配理由**：一个"海市蜃楼"般的偶然——培养皿上的透明圈差点被整个学界视而不见；"幻影"气质贴合发现被冷落十年、又以"Fleming myth"折射出的名利镜像；音乐宜带悬疑与释然的双重层次
- **本地路径**：`music_audio/` 下检索曲名（参照 `curated_tracks.md`），复制到 `medic/presentations/20th_century/Alexander_Fleming/Mirage.wav`
- **时长**：曲长须 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐

