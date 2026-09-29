# 医学家立传提示词（Martin Rodbell）

> 本文件是 OpenMedic 项目（OpenMathAI 诺贝尔生理学或医学奖人物史）20 世纪 1994 年得主 Martin Rodbell 的人物专属立传提示词。
> 事实基准：`medic/presentations/pages/20th_century/Martin_Rodbell/page.md`（唯一事实来源，metadata.json 仅作参考）。
> ★ 本篇 page.md 正文较短（约 25 行实质内容），15 页规划按正文信息密度压缩，禁止脑补未载事实填版。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Martin Rodbell（1925-12-01 生于美国马里兰州巴尔的摩 ~ 1998-12-07 逝于北卡罗来纳州教堂山，享年 73 岁）
- **气质关键词**：**G 蛋白的发现者、细胞信号转导"鉴别器-换能器-放大器"模型的提出者、分子内分泌学家** —— 1994 年诺贝尔生理学或医学奖（与 Alfred G. Gilman 共享）获奖理由（逐字引用 `medic/nobel_medicine_citations.json`）：
  > "for their discovery of G-proteins and the role of these proteins in signal transduction in cells"（因其发现 G 蛋白及其在细胞信号转导中的作用）
- **设计母题**：**细胞的赛博装置（the cybernetic cell）**。受 1960 年代计算机与生物学类比启发，他把细胞表述为三件套的信息处理系统：鉴别器（受体）、换能器（G 蛋白）、放大器（效应器）。视觉语言：三级信号回路、GTP 火花点燃的换能器。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Martin_Rodbell/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）
- **关键时间线（身份信息页与时间轴素材，均出自 page.md）**：
  - 1925-12-01 生于巴尔的摩（父 Milton 为杂货商；母 Shirley，原姓 Abrams；犹太家庭）
  - Baltimore City College 高中毕业后 1943 入约翰斯·霍普金斯大学（兴趣：生物学与法国存在主义文学）
  - 1944-1946 二战服役：美国海军无线电操作员
  - 1946 回霍普金斯，1949 获生物学 B.S.
  - 1950 娶 Barbara Charlotte Ledermann（其密友即《安妮日记》作者 Anne Frank 的姐姐 Margot Frank）
  - 1954 华盛顿大学生物化学博士；1954-1956 伊利诺伊大学厄巴纳-香槟分校博士后
  - 1956 入国立卫生研究院（NIH）国家心脏研究所任研究生物化学家（贝塞斯达）
  - 1985 任 NIH 国家环境健康科学研究所（NIEHS，北卡三角研究园）科学主任，至 1994 退休
  - 1991-1998 兼杜克大学细胞生物学 adjunct 教授；兼 UNC 教堂山分校药理学 adjunct 教授
  - 细胞三件套模型：鉴别器（受体）接收胞外信息、换能器跨膜处理、放大器（效应器）放大信号
  - 1969-12 至 1970-01：胰高血糖素-大鼠肝细胞膜受体实验；发现 ATP 可反转结合、GTP 快近千倍→GTP 是解离胰高血糖素的活性因子、激活鸟苷酸核苷酸蛋白（后称 G 蛋白）
  - 该活化即 Sutherland 所理论化的"第二信使"过程；G 蛋白=鉴别器与放大器之间的关键换能器
  - 后又提出并证实受体处存在多种可同时抑制/激活转导的 G 蛋白
  - 荣誉：Gairdner 国际奖 1984、Richard Lounsbery 奖 1987、诺贝尔奖 1994、Golden Plate 1995、蒙彼利埃第一大学荣誉博士
  - 1998-12-07 久病后因多器官衰竭卒于教堂山

---

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章执行 Beamer 立传，**第 0/1/2/3 步按 medic 路径执行**：
> - 页面与元数据：`medic/presentations/pages/20th_century/Martin_Rodbell/`（page.md / metadata.json / images.txt）
> - 目录创建：`medic/presentations/20th_century/Martin_Rodbell/` 与 `images/`
> - Makefile：复制 medic 侧同结构模板，设 `MAIN=Martin_Rodbell_zh`
> - 肖像：正文含 1994 年肖像缩略 URL（250px 改 500px，curl 加 `-A "Mozilla/5.0"`，file 验证）；404 用 Commons `Special:FilePath` 回退；均失败用装饰圆占位
> 每完成一步汇报，溢出即修（make → pdftoppm 逐页目检）。

---

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biochemistry | 生物化学 | infobox Fields/occupation；本职学科 | 身份页 |
| 1 | signal transduction | 信号转导 | 诺奖核心：G 蛋白与三件套模型 | 核心页 |
| 2 | molecular endocrinology | 分子内分泌学 | 导语称谓；胰高血糖素-肝细胞膜受体体系 | 核心页 |
| 3 | G-protein biology | G 蛋白生物学 | GTP 活化的鸟苷酸核苷酸蛋白 | 核心页 |

---

## 四、社会关系梳理 + 入库 【人物专属】

> 与 `MySQL/data/Martin_Rodbell.yaml` 完全一致；只收 page.md 明载的关系。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Alfred G. Gilman | 无向 | 1994 诺贝尔生理学或医学奖共享（G 蛋白的发现及其在信号转导中的作用） |
| spouse | Barbara Charlotte Ledermann | — | 1950 结婚；其密友为《安妮日记》作者之姐 Margot Frank |
| parent-child | Shirley Abrams | — | 母 |
| parent-child | Milton Rodbell | — | 父，杂货商 |

**不入库裁定**：Earl W. Sutherland 系"其第二信使理论被本实验证实"的理论渊源，非个人关系，不入库（Gilman 页的 Sutherland 边同理按各篇处理）；四名子女仅记数量；妹夫 Sanne Ledermann（Anne Frank 密友）属姻亲不入库；Gilman 与 Rodbell 两人无共事记载，仅为共享得主。

---

## 五、配色方案 【人物专属】

- **气质**：把细胞想象成计算机的人——冷静的类比者与耐心的滴定者
- **主色**：回路深蓝 `#37548D`（与人物气质呼应——1960 年代计算机机房与细胞膜的叠影）
- **诺奖色**：香槟金 `#D4AF37`
- **四分类色（badgeA-D）**：
  - `badgeA` 生物化学——滴定青 `#2E7D6B`
  - `badgeB` 信号转导——级联橙 `#B4632A`
  - `badgeC` 分子内分泌学——激素紫 `#6B4E9E`
  - `badgeD` G 蛋白生物学——GTP 金 `#C89B3C`
- **背景母题**：鉴别器—换能器—放大器三级回路图（对应"细胞的赛博装置"），badge 四色错落

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
01  封面 — 细胞的换能器 / Martin Rodbell 1925–1998 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、巴尔的摩、霍普金斯/华盛顿大学、NIH/NIEHS、荣誉、核心领域）
03  核心贡献概览 — G 蛋白 / 三件套模型 / GTP 的关键角色 / 多重 G 蛋白
04  巴尔的摩与从军（1925–1949）— 杂货商之家、海军无线电操作员、霍普金斯生物学 BS
05  博士与博后（1949–1956）— 华盛顿大学生化博士、伊利诺伊博后
06  NIH 岁月（1956–1985）— 国家心脏研究所研究生物化学家
07  细胞的赛博装置（核心贡献页一）— 鉴别器/换能器/放大器三件套模型
08  1969-70 胰高血糖素实验（核心贡献页二）— ATP 反转结合、GTP 快近千倍
09  G 蛋白的发现 — GTP 激活鸟苷酸核苷酸蛋白；第二信使假说的证实
10  多重 G 蛋白 — 抑制与激活可以同时进行的受体复杂性
11  1994 诺贝尔奖 — 与 Gilman 共享同一句理由；发现者与命名者的接力
12  NIEHS 与晚年 — 1985 科学主任（三角研究园）、杜克/UNC 兼职教授、1994 退休
13  Barbara — 妻子与 Anne Frank 家族的渊源（正文一句，客观呈现）
14  结尾 — 1998-12-07 卒于教堂山（多器官衰竭）；换能器长存
```

---

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方逐字为 "for their discovery of G-proteins and the role of these proteins in signal transduction in cells"——共享单数 discovery |
| 分工表述 | Rodbell=GTP 角色的发现者（GTP 反转胰高血糖素结合、激活 G 蛋白、三件套模型）；Gilman=分离并命名 G 蛋白本体——接力勿混 |
| Sutherland 定位 | G 蛋白活化即"Sutherland 所理论化的第二信使过程"——理论渊源而非个人关系，**不入库**（与 Gilman 页的 Sutherland 边区分） |
| 页面单薄 | 本篇 page.md 正文短——叙事页按上述时间线密度即可，禁止脑补实验细节、弟子名单等未载内容 |
| 军旅细节 | 1944-1946 美国海军无线电操作员（二战）——勿写成陆军或军官 |
| Anne Frank 渊源 | 妻子 Barbara 是 Margot Frank 的前密友——正文一句客观呈现即可，勿展开二战叙事 |
| 机构口径 | NIH 国家心脏研究所（1956 起）≠ NIEHS（1985 起科学主任）；Duke/UNC 均为 adjunct（兼职）教授——勿写成全职 |
| 日期巧合 | 生卒同为 12 月（12-01 / 12-07）——页面如实呈现 |
| metadata 噪声 | metadata 无父母/子女载；父母、妻子 Barbara Charlotte Ledermann 以 page.md 为准；educated_at 有噪声 QID 项（Q219563）以正文 University of Washington 为准 |

---

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| G-protein | G 蛋白 | 诺奖核心词 |
| signal transduction | 信号转导 | citation 原文用语 |
| discriminator | 鉴别器（受体） | 三件套之一 |
| transducer | 换能器 | 三件套之二；G 蛋白所在 |
| amplifier / effector | 放大器 / 效应器 | 三件套之三 |
| glucagon | 胰高血糖素 | 1969-70 实验激素 |
| GTP / ATP | 鸟苷三磷酸 / 腺苷三磷酸 | GTP 快近千倍 |
| second messenger | 第二信使 | Sutherland 理论 |
| receptor | 受体 | 鉴别器的实体 |
| NIEHS | 国家环境健康科学研究所 | 1985-1994 任职 |

---

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Daylight**（manifest 预分配）
- **匹配理由**：从战时无线电操作员到解码细胞电报的人——"白昼"贴合信号被点亮的一瞬（GTP 火花、级联的灯亮起）；亦呼应其巴尔的摩到北卡的安稳后半生
- **本地路径**：`music_audio/` 下检索曲名（参照 `curated_tracks.md`），复制到 `medic/presentations/20th_century/Martin_Rodbell/Daylight.wav`
- **时长**：曲长须 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐
