# 医学家立传提示词（Alfred G. Gilman）

> 本文件是 OpenMedic 项目（OpenMathAI 诺贝尔生理学或医学奖人物史）20 世纪 1994 年得主 Alfred G. Gilman 的人物专属立传提示词。
> 事实基准：`medic/presentations/pages/20th_century/Alfred_G._Gilman/page.md`（唯一事实来源，metadata.json 仅作参考）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Alfred Goodman Gilman（1941-07-01 生于美国康涅狄格州纽黑文 ~ 2015-12-23 逝于得克萨斯州达拉斯，享年 74 岁）
- **气质关键词**：**G 蛋白的发现者与命名者、信号转导的钥匙人、药理学教科书世家的传人** —— 1994 年诺贝尔生理学或医学奖（与 Martin Rodbell 共享）获奖理由（逐字引用 `medic/nobel_medicine_citations.json`）：
  > "for their discovery of G-proteins and the role of these proteins in signal transduction in cells"（因其发现 G 蛋白及其在细胞信号转导中的作用）
- **设计母题**：**膜上的分子开关（the molecular switch）**。激素在膜外叩门，G 蛋白在膜内扳动开关、点燃级联——细胞第一次被表述为可被"接通"的电路。视觉语言：GPCR 门铃、G 蛋白开关、cAMP 信号灯的三级回路。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Alfred_G._Gilman/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）
- **关键时间线（身份信息页与时间轴素材，均出自 page.md）**：
  - 1941-07-01 生于纽黑文（父 Alfred Gilman Sr. 为耶鲁医学院药理学教授、《Goodman & Gilman 药理学治疗基础》合著者；母 Mabel，原姓 Schmidt；犹太家庭）
  - 中间名 Goodman 取自教科书合著者 Louis S. Goodman——Michael Stuart Brown 笑称他"大概是唯一以教科书命名的人"（教科书 1941 年出版，与同年出生；后称药理学"蓝圣经"）
  - 自嘲生来"含着科学/学术银汤匙——或者是一根杵（但没有研钵）"
  - 白原市长大；1955 入康涅狄格州沃特伯里 The Taft School（"学术新兵营"）
  - 耶鲁大学生物学 BA（生物化学主修，1962）；首个课题验证 Crick 的接头假说（Melvin Simpson 实验室，结识未来妻子 Kathryn Hedlund，1963 结婚）
  - 1962 夏在 Burroughs Wellcome 与 Allan Conney 合作，1963 发表头两篇论文
  - 受 Earl Wilbur Sutherland 劝说入 Case Western Reserve MD-PhD 项目（1969 毕业）；Sutherland 转赴 Vanderbilt 后随其合作者 Theodore Rall 完成学业
  - NIH 博后（1969-1971）在 Marshall Nirenberg 麾下；违背其建议自选蛋白结合新方法，六周出成果（cAMP 结合测定，1970 发表）
  - 1971 弗吉尼亚大学药理学助理教授；1977 正教授
  - 1981 起任德州大学西南医学中心（达拉斯）药理学系主任；2004 院长；2006-2009 常务副校长兼教务长
  - 2009 退休出任德州癌症预防与研究研究所首席科学官，2012 因行政与政治压力辞职（七名资深科学家随其离职）
  - Regeneron 制药联合创始人；Alliance for Cellular Signaling 创始人兼主席（1990 起任所长）；2005 起任礼来（Eli Lilly）董事
  - G 蛋白发现链：Rodbell 证明 GTP 参与→Gilman 用淋巴瘤细胞缺失蛋白实验追凶→1977-1979 系列论文→1980 分离命名 G protein
  - 荣誉：John J. Abel 奖 1975、Gairdner 国际奖 1984、Lasker 基础医学研究奖与 Horwitz 奖 1989（后者与 Edwin Krebs 共享）、NAS 1986、诺贝尔奖 1994、Golden Plate 1995、AACR 学院会士 2013
  - 科学教育捍卫者：2003 年反对德州教委把演化移出课程（率 NAS 科学家在《达拉斯晨报》公开批评）、反对创世研究所认证申请、联署反对路易斯安那 2008 科学教育法；引语 "How can Texas simultaneously launch a war on cancer and approve educational platforms that submit that the universe is 10,000 years old?"
  - 2015-12-23 因胰腺癌卒于达拉斯；遗孀 Kathryn 与三名子女 Amy Ariagno、Anne Sincovec、Edward Gilman

---

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章执行 Beamer 立传，**第 0/1/2/3 步按 medic 路径执行**：
> - 页面与元数据：`medic/presentations/pages/20th_century/Alfred_G._Gilman/`（page.md / metadata.json / images.txt）
> - 目录创建：`medic/presentations/20th_century/Alfred_G._Gilman/` 与 `images/`
> - Makefile：复制 medic 侧同结构模板，设 `MAIN=Alfred_G._Gilman_zh`
> - 肖像：优先 images.txt 缩略 URL（250px 改 500px，curl 加 `-A "Mozilla/5.0"`，file 验证）；404 用 Commons `Special:FilePath` 回退；均失败用装饰圆占位
> 每完成一步汇报，溢出即修（make → pdftoppm 逐页目检）。

---

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | pharmacology | 药理学 | infobox field_of_work；本职学科（药理学系主任） | 身份页 |
| 1 | signal transduction | 信号转导 | 诺奖核心：G 蛋白与 cAMP 级联 | 核心页 |
| 2 | biochemistry | 生物化学 | infobox Fields；蛋白纯化与结合测定 | 核心页 |
| 3 | G-protein biology | G 蛋白生物学 | 1980 分离命名；Gs/Gi 家族与结构 | 贡献页 |

---

## 四、社会关系梳理 + 入库 【人物专属】

> 与 `MySQL/data/Alfred_G._Gilman.yaml` 完全一致；只收 page.md 明载的关系。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Martin Rodbell | 无向 | 1994 诺贝尔生理学或医学奖共享（G 蛋白的发现及其在信号转导中的作用） |
| advisor-student | Theodore Rall | 师→生 | Case Western MD-PhD 实际指导者（Sutherland 转赴 Vanderbilt 后随其合作者完成） |
| colleague | Earl Wilbur Sutherland Jr. | 无向 | 劝其入 MD-PhD 项目（其父挚友，第二信使理论提出者） |
| advisor-student | Marshall Warren Nirenberg | 师→生 | NIH 博士后（1969-1971，库内 id=6199） |
| collaborator | Allan Conney | 无向 | Burroughs Wellcome 时期合作，发表头两篇论文（1963） |
| colleague | Michael Stuart Brown | 无向 | 挚友（"以教科书命名"笑谈出处，库内 id=5735） |
| spouse | Kathryn Hedlund | — | 1963 结婚，耶鲁 Melvin Simpson 实验室结识 |
| parent-child | Alfred Gilman Sr. | — | 父，耶鲁药理学教授、Goodman & Gilman 教科书合著者 |
| parent-child | Mabel Schmidt | — | 母 |
| parent-child | Amy Ariagno | — | 女（达拉斯） |
| parent-child | Anne Sincovec | — | 女（达拉斯） |
| parent-child | Edward Gilman | — | 子（奥斯汀） |

**不入库裁定**：Louis S. Goodman（中间名来源、父之合著者）系命名渊源非个人关系；Edwin Krebs（1989 Horwitz 共享）不另建第二行；Robert Millikan/孟德尔学派人物无涉；Melvin Simpson（耶鲁实验室房东级导师，一笔带过）不入库；1971 年后博士生未载不入库。

---

## 五、配色方案 【人物专属】

- **气质**：教科书世家出身的实验杀手——把"第三信使"的悬案办成铁案
- **主色**：信号深灰蓝 `#37474F`（与人物气质呼应——"蓝圣经"的封面、细胞膜的磷脂双层）
- **诺奖色**：香槟金 `#D4AF37`
- **四分类色（badgeA-D）**：
  - `badgeA` 药理学——处方蓝 `#3A6FA8`
  - `badgeB` 信号转导——级联橙 `#B4632A`
  - `badgeC` 生物化学——cAMP 青 `#2E7D6B`
  - `badgeD` G 蛋白生物学——开关金 `#C89B3C`
- **背景母题**：膜上的三级回路（门铃—开关—信号灯）与 GTP 水解火花（对应"分子开关"），badge 四色错落

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
01  封面 — G 蛋白的发现者 / Alfred G. Gilman 1941–2015 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、纽黑文、耶鲁/Case Western、UT Southwestern、荣誉、核心领域）
03  核心贡献概览 — G 蛋白的发现与命名 / cAMP 测定方法 / Gs/Gi 家族与结构 / 科学教育捍卫
04  蓝圣经之家（1941–1962）— 药理学教授之子、"以教科书命名"的笑谈、Taft 学校、耶鲁 BA
05  Conney 与头两篇论文（1962–1963）— Burroughs Wellcome 之夏
06  Case Western 与两位导师（1962–1969）— Sutherland 劝入 MD-PhD、Rall 实际指导、"药理学只是有目的的生物化学"
07  NIH 与 Nirenberg（1969–1971）— "无聊的轴突项目"之外自选课题、cAMP 结合测定
08  淋巴瘤细胞的悬案（核心贡献页一）— 癌细胞丢失的膜蛋白=激素信号的缺失环节
09  G 蛋白的诞生（核心贡献页二）— 1977-1979 系列论文、1980 分离并命名 G protein
10  与 Rodbell 的接力 — Rodbell 证 GTP 参与→Gilman 找到蛋白质本体；分工勿混
11  1994 诺贝尔奖 — 共享理由句；演讲《G Proteins and Regulation of Adenylyl Cyclase》（1994-12-08）
12  达拉斯与产业 — UT Southwestern 药理系主任/院长/provost、Regeneron 联合创始人、Alliance for Cellular Signaling、礼来董事
13  科学教育的哨兵 — 2003 德州教委之争（引语可引）、路易斯安那 2008 请愿（正文客观呈现）
14  结尾 — 2015-12-23 卒于达拉斯（胰腺癌）；"药理学只是有目的的生物化学"
```

---

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方逐字为 "for their discovery of G-proteins and the role of these proteins in signal transduction in cells"——注意 their（与 Rodbell 共享）、单数 discovery |
| 分工表述 | Rodbell=1960s 证明 GTP 参与信号（"第三信使"）；Gilman=找到与 GTP 相互作用的蛋白质本体并命名 G protein——接力勿混；Rodbell 页的 Sutherland 是理论被证实，非个人关系 |
| 教科书世家 | 父 Alfred Gilman Sr. 与 Louis S. Goodman 合著《Goodman & Gilman's The Pharmacological Basis of Therapeutics》（1941 年出版，与其同年）；中间名 Goodman 取自合著者；他 1980-2000 继任该书编辑——五件事勿串年份 |
| 双导师口径 | MD-PhD 名义想跟 Sutherland，实际导师是 Theodore Rall（Sutherland 转赴 Vanderbilt）——Rall 建 advisor-student，Sutherland 建 colleague，勿混 |
| Nirenberg 关系 | NIH 博后；"违背 Nirenberg 的建议"自选课题且成果被 Nirenberg 立即送发（1970）——advisor-student（博士后）+叙事张力并存 |
| 辞职叙事 | 2012 辞任 Texas 癌症预防研究所 CSO 系"行政与政治压力"，七名资深科学家随其离职——正文客观呈现，勿引申 |
| Horwitz 双奖 | 1989 Horwitz 奖与 Edwin Krebs 共享——不另建第二行（uq_rel 按 type 去重），陷阱表注明 |
| 引语红线 | "silver spoon...pestle"、"named after a textbook"（Brown 语）、"an eternity in purgatory"、"pharmacology was just biochemistry with a purpose"（Sutherland 语）、"How can Texas simultaneously launch a war on cancer..."——均为 page.md 英文原文，可引但须各自署名 |
| 创造论之争 | 反创造论/捍卫演化教育正文多句明载——按正文客观呈现，属公共立场非私人争议 |
| metadata 噪声 | metadata 无父母/子女载；父母、妻子、三名子女（含婚后姓 Ariagno/Sincovec）以 page.md 为准 |

---

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| G protein | G 蛋白 | 其发现并命名 |
| GPCR | G 蛋白偶联受体 | 膜外激活端 |
| signal transduction | 信号转导 | citation 原文用语 |
| cyclic AMP (cAMP) | 环腺苷酸 | 第二信使 |
| adenylyl cyclase | 腺苷酸环化酶 | cAMP 生成酶 |
| GTP / ATP | 鸟苷三磷酸 / 腺苷三磷酸 | GTP 快千倍的关键 |
| second messenger | 第二信使 | Sutherland 理论 |
| lymphoma | 淋巴瘤 | 缺失蛋白实验的癌细胞 |
| MD-PhD | 医学博士-哲学博士双学位 | Case Western 项目 |
| Goodman & Gilman | 《古德曼-吉尔曼药理学治疗基础》 | 家族教科书（"蓝圣经"） |

---

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**The Flow of Time**（manifest 预分配）
- **匹配理由**：从 1941 年那本"与他同年出版"的教科书，到 2015 年谢幕——两代药理学的时间之流；G 蛋白开关的开合亦如时间之闸。音乐宜沉稳而有流动感
- **本地路径**：`music_audio/` 下检索曲名（参照 `curated_tracks.md`），复制到 `medic/presentations/20th_century/Alfred_G._Gilman/The Flow of Time.wav`
- **时长**：曲长须 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐
