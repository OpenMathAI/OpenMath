# 医学家立传提示词（Jacques Monod）

> 本文件是 OpenMedic 项目（OpenMathAI 诺贝尔生理学或医学奖人物史）20 世纪 1965 年得主 Jacques Monod 的人物专属立传提示词。
> 事实基准：`medic/presentations/pages/20th_century/Jacques_Monod/page.md`（唯一事实来源，metadata.json 仅作参考）。
> 结构对齐标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（11 节合并为 9 节）。
> ★ 库内已有同名 stub 'Jacques Monod'（id=4852，无 qid），yaml 走 UPD 回填 Q231402。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Jacques Lucien Monod（1910-02-09 生于巴黎 ~ 1976-05-31 逝于戛纳，享年 66 岁）
- **气质关键词**：**lac 操纵子的共同发现者、分子生物学奠基人之一、《偶然与必然》的作者、抵抗运动参谋长** —— 1965 年诺贝尔生理学或医学奖（与 Jacob、Lwoff 共享）获奖理由（逐字引用 `medic/nobel_medicine_citations.json`）：
  > "for their discoveries concerning genetic control of enzyme and virus synthesis"（因其关于酶合成与病毒合成的遗传控制的发现）
- **设计母题**：**偶然与必然（chance and necessity）**。细菌"选择"是否合成消化乳糖的酶——必然的生化约束之下涌现出看似自由的选择；正如他所言，生命的全部复杂性源于偶然变异与必然约束的长舞。视觉语言：酶的刚性口袋（必然）与掷出的骰子（偶然）同框。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Jacques_Monod/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）
- **关键时间线（身份信息页与时间轴素材，均出自 page.md）**：
  - 1910-02-09 生于巴黎（母 Charlotte "Sharlie" MacGregor Todd 来自密尔沃基；父 Lucien Monod 为雨格诺派画家，启迪其艺术与思想）
  - 戛纳读中学至 18 岁；1928-10 入巴黎大学生物学
  - 求学四大引路人（正文原句）：George Teissier（定量描述偏好）、André Lwoff（微生物学的潜能）、Boris Ephrussi（生理遗传学）、Louis Rapkine（唯有化学与分子描述才能完满解释生命）
  - 博士前在加州理工 Thomas Hunt Morgan 实验室一年，做果蝇遗传学（"真正的启示"）
  - 博士论文研究细菌在混合糖上的生长，创造术语 diauxie（双峰生长）；发展 Monod equation 与恒化器（chemostat）理论
  - 1938 娶 Odette Bruhl（1972 卒）
  - 二战参加抵抗运动，任法国内地军（FFI）行动参谋长：策划伞降武器、铁路爆破、邮件截查
  - 1943 加入巴斯德研究所（Jacob 1949 入所）
  - 1945 获军团骑士勋章、战争十字、美国青铜星章
  - 战后短暂加入法国共产党，李森科事件后疏远
  - 与 Jacob 提出乳糖操纵子负调控模型；预言信使 RNA 的存在
  - 与 Changeux、Jacob 提出别构转换理论；与 Wyman、Changeux 扩展为协同性的 MWC 模型
  - 1960 当选美国艺术与科学院；1965 共享诺贝尔奖；1968 当选皇家学会外籍会员
  - NAS 与美国哲学学会院士；Institut Jacques Monod（CNRS 与巴黎大学共建）以他命名
  - 1970 出版《偶然与必然》（英译 1971；基于 1969 Pomona 学院讲座；题词引 Camus《西西弗神话》）
  - 1973 联署《人道主义宣言 II》
  - 1968 五月风暴中支持学生，与多位诺奖得主联名上书戴高乐
  - 与加缪为挚友（同出抵抗运动、同样批评苏联体制）
  - 爱好航海与大提琴
  - 1976-05-31 因白血病卒于戛纳，葬 Cimetière du Grand Jas

---

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章执行 Beamer 立传，**第 0/1/2/3 步按 medic 路径执行**：
> - 页面与元数据：`medic/presentations/pages/20th_century/Jacques_Monod/`（page.md / metadata.json / images.txt）
> - 目录创建：`medic/presentations/20th_century/Jacques_Monod/` 与 `images/`
> - Makefile：复制 medic 侧同结构模板，设 `MAIN=Jacques_Monod_zh`
> - 肖像：优先 images.txt 缩略 URL（250px 改 500px，curl 加 `-A "Mozilla/5.0"`，file 验证）；404 用 Commons `Special:FilePath` 回退；均失败用装饰圆占位
> 每完成一步汇报，溢出即修（make → pdftoppm 逐页目检）。

---

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | molecular biology | 分子生物学 | 诺奖核心：遗传控制酶合成；mRNA 概念的提出 | 核心页 |
| 1 | biochemistry | 生物化学 | infobox Fields；diauxie、Monod equation、恒化器 | 研究页 |
| 2 | genetics | 遗传学 | 乳糖操纵子与调节基因（infobox Fields） | 核心页 |
| 3 | allostery | 别构调节 | 别构转换理论与 MWC 协同模型 | 研究页 |

---

## 四、社会关系梳理 + 入库 【人物专属】

> 与 `MySQL/data/Jacques_Monod.yaml` 完全一致；只收 page.md 明载的关系。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | François Jacob | 无向 | 1965 诺贝尔生理学或医学奖共享（酶与病毒合成的遗传控制） |
| co-honored | André Michel Lwoff | 无向 | 1965 诺贝尔生理学或医学奖共享（酶与病毒合成的遗传控制） |
| advisor-student | André Michel Lwoff | 师→生 | "Lwoff 引他领略微生物学的潜能"（正文四大引路人句） |
| influence | Georges Teissier | 无向 | 引路人之一：定量描述的偏好 |
| influence | Boris Ephrussi | 无向 | 引路人之一：生理遗传学的发现（库内 id=5760） |
| influence | Louis Rapkine | 无向 | 引路人之一：化学与分子描述的生命观 |
| colleague | Thomas Hunt Morgan | 无向 | 博士前在加州理工其实验室访学一年做果蝇遗传（库内 id=5339） |
| collaborator | Jean-Pierre Changeux | 无向 | 共同提出别构转换理论 |
| collaborator | Jeffries Wyman | 无向 | 与 Changeux 共同扩展出协同性 MWC 模型 |
| colleague | Albert Camus | 无向 | 挚友：同出抵抗运动、同样批评苏联体制（库内 id=4897） |
| spouse | Odette Bruhl | — | 1938 结婚，1972 去世 |
| parent-child | Lucien Monod | — | 父，雨格诺派画家 |
| parent-child | Charlotte MacGregor Todd | — | 母，来自密尔沃基的美国人 |

**不入库裁定**：Daniel Dennett/Douglas Hofstadter/Marvin Minsky/Richard Dawkins 系"受其影响的学人"罗列句（Minsky 有库内图灵记录），非个人关系叙事，不入库；Charles de Gaulle（请愿对象）、Howard L. Kaye（批评者）、Michel Werner（Institut 现任主任）不入库；Lysenko Affair 系政治事件，未与 Lysenko 本人建立关系边（与 Muller-Lysenko 边区分）。

## 五、配色方案 【人物专属】

- **气质**：骑士般的多面手——实验室、抵抗运动指挥部、大提琴与哲学讲台
- **主色**：必然深红 `#7E1E23`（与人物气质呼应——酶的刚性约束与抵抗运动的旗帜）
- **诺奖色**：香槟金 `#D4AF37`
- **四分类色（badgeA-D）**：
  - `badgeA` 分子生物学——mRNA 金 `#C89B3C`
  - `badgeB` 生物化学——恒化器青 `#2E7D6B`
  - `badgeC` 遗传学（操纵子）——操纵基因蓝 `#3A6FA8`
  - `badgeD` 别构调节——构象紫 `#6B4E9E`
- **背景母题**：骰子与酶的刚性口袋同框（对应"偶然与必然"），badge 四色错落

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
01  封面 — 偶然与必然的解读者 / Jacques Monod 1910–1976 + 四色 badge + 右上头像 + 国籍行（France）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、巴黎、巴黎大学、巴斯德研究所、FFI 参谋长、荣誉、核心领域）
03  核心贡献概览 — lac 操纵子 / mRNA 概念 / 别构与 MWC 模型 / 《偶然与必然》
04  巴黎与四大引路人（1910–1938）— 画家之父与美裔之母、Teissier/Lwoff/Ephrussi/Rapkine
05  摩根实验室的一年 — 加州理工的果蝇启示；diauxie 与 Monod equation
06  抵抗运动参谋长（1939–1945）— 伞降武器、铁路爆破、邮件截查；军团勋章/战争十字/青铜星章
07  巴斯德岁月（1943–1961）— 与 Jacob 相遇（1949 入所）、1958 Monod 的灵感之夜
08  lac 操纵子（核心贡献页一）— 阻遏物-操纵基因-诱导物的负调控回路
09  mRNA 与分子生物学（核心贡献页二）— "信使"概念的提出；奠基人地位
10  别构与协同 — 与 Changeux/Jacob 的别构理论；与 Wyman/Changeux 的 MWC 模型
11  1965 诺贝尔奖 — 三人共享同一句理由；Monod 侧=酶合成的遗传控制
12  《偶然与必然》 — 1970；Camus 题词与"知识伦理学"；结尾引语（有英文原文可引）
13  公共与哲思 — 人道主义宣言 II（1973）、May 68 上书戴高乐、与加缪的友谊
14  结尾 — 1976-05-31 卒于戛纳；"想象西西弗是幸福的"
```

---

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方逐字为 "for their discoveries concerning genetic control of enzyme and virus synthesis"——三人共享同一句 |
| 引语红线 | 结尾引语 "man at last knows he is alone..." 与 "One must imagine Sisyphus happy." 均为 page.md 载英文原文（后者系 Camus 语，Monod 选题词）——可引，须各自署名 |
| 四大引路人 | 正文是一句排比（Teissier/Lwoff/Ephrussi/Rapkine）——Lwoff 用 advisor-student（"initiated"），其余三人用 influence，类型勿混 |
| 摩根关系 | "spent a year in the laboratory" 系访学非师承——用 colleague，勿建 advisor-student（Morgan 的博士生名单属 Muller 篇口径） |
| 政治叙事 | 战后加入法共→李森科事件后疏远；May 68 支持学生并上书戴高乐；抵抗运动细节——均按正文客观一句，不引申政治评价 |
| Camus 关系 | "became a close friend" + 共同批评苏联体制——colleague 类型承载友谊，note 写"挚友"；勿写成师承或合作 |
| Lysenko 区分 | Monod 是"李森科事件后疏离法共"——与 Muller 篇的 Muller-Lysenko controversy 边不同人不同事，两篇勿混 |
| 双荣誉句 | Légion d'honneur 军官级（metadata）/骑士级 1945（正文）双口径——页面取正文 1945 Chevalier，metadata 军官级注存疑 |
| mRNA 表述 | "Monod also suggested the existence of messenger RNA"——是概念提出（suggested），勿写成"发现 mRNA" |
| 生卒一致 | 1910-02-09 / 1976-05-31（白血病，戛纳）两处一致，无双值问题 |

---

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| lac operon | 乳糖操纵子 | 核心词 |
| repressor / operator | 阻遏物 / 操纵基因 | 负调控三件套之一 |
| messenger RNA (mRNA) | 信使 RNA | "suggested the existence" 口径 |
| diauxie | 双峰生长（二度生长） | 其创造的术语 |
| Monod equation | Monod 方程 | 细菌生长定量 |
| chemostat | 恒化器 | 连续培养系统 |
| allosteric transition | 别构转换 | 与 Changeux/Jacob |
| MWC model | MWC 模型（Monod-Wyman-Changeux） | 协同性最广为接受的解释 |
| Chance and Necessity | 《偶然与必然》 | 1970，哲学著作 |
| Forces Françaises de l'Interieur | 法国内地军（FFI） | 抵抗运动建制 |

---

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Lonesome**（manifest 预分配）
- **匹配理由**：抵抗运动参谋长与分子生物学奠基人的双重孤独——"人是宇宙中孤独的存在"恰是其哲学结论；Lonesome 的低回气质贴合《偶然与必然》的冷峻收束
- **本地路径**：`music_audio/` 下检索曲名（参照 `curated_tracks.md`），复制到 `medic/presentations/20th_century/Jacques_Monod/Lonesome.wav`
- **时长**：曲长须 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐
