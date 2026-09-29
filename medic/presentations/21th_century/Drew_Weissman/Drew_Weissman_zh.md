# 医学家立传提示词（Drew Weissman）

> OpenMedic 项目、21 世纪诺贝尔生理学或医学奖 2023 年得主（德鲁·韦斯曼，核苷修饰 mRNA 疫苗的共同发明人）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Drew Weissman（1959-09-07 生于马萨诸塞州列克星敦，在世）
- **气质关键词**：**mRNA 疫苗的免疫学之眼、"我们一路都在战斗"的长期主义者、从复印机旁的抱怨到全球疫苗平台的另一半** —— 2023 获奖理由（与 Katalin Karikó 两人共享）：
  > "for their discoveries concerning nucleoside base modifications that enabled the development of effective mRNA vaccines against COVID-19"（因发现核苷碱基修饰，从而使针对新冠的有效 mRNA 疫苗得以开发）
- **设计母题**：**免疫之眼看穿 RNA**。他带来的免疫学视角与她的生物化学互补——"免疫系统为什么攻击合成 RNA"这一问，问出了假尿苷的答案。视觉隐喻：免疫之眼注视 RNA 链，被修饰的碱基悄然隐身。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Drew_Weissman/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/21th_century/Drew_Weissman/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准，裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/21th_century/Drew_Weissman/`（含 `images/`）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=Drew_Weissman_zh`、`VIDEO_NAME=Drew_Weissman_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/21th_century/Drew_Weissman/images.txt`（2024 诺奖周照）；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。插图可用 2022 与 Karikó 合影照。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/Drew_Weissman.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | immunology | 免疫学 | RNA 与先天免疫，2023 诺奖核心 | 核心页 |
| 1 | messenger RNA | 信使 RNA | 修饰 mRNA 疗法平台 | 核心页 |
| 2 | RNA vaccine | RNA 疫苗 | 新冠 mRNA 疫苗的科学基础 | 核心页 |
| 3 | innate immunity | 先天免疫 | Toll 样受体对 RNA 的识别 | 研究页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Ann Marshak-Rothstein | 导师 | 波士顿大学免疫学博士导师（1987，B 淋巴细胞调控） |
| advisor-student | Anthony Fauci | 导师 | NIH 博士后导师（时任 NIAID 所长） |
| co-honored | Katalin Karikó | 无向 | 2023 诺贝尔生理学或医学奖两人共享（核苷碱基修饰使有效 mRNA 疫苗成为可能） |
| collaborator | Katalin Karikó | 无向 | 1997 宾大相识合作，免疫学+生物化学互补，RNARx 共同创立与专利共同持有人 |
| colleague | Robert S. Langer | 无向 | BBVA 基础知识前沿奖共同得主 |

> 在世者，relations=5 为诚实值，Review 勿误判缺漏。
> 不入库：Gerald Fasman（Brandeis 本科实验室）；父母 Hal/Adele Weissman（背景叙事）；Chulalongkorn University（机构合作，泰国及中低收入国家疫苗供应）；粉丝信作者。
> 库内当时无 Ann Marshak-Rothstein / Anthony Fauci / Robert S. Langer 记录，均由本 yaml 新建 stub；Karikó 已由本批其本人 yaml 规范化。

## 五、配色方案 【人物专属】

- **气质**：新英格兰的沉稳蓝 + 免疫应答的电流感 + 医者温度
- **主色**：疫苗蓝 `#20558A`（公共卫生的冷静与全球协作的广度）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` 先天免疫/TLR — 疫苗蓝 `#20558A`
  - `badgeB` 核苷修饰共研 — 麦金绿 `#2F6B4F`
  - `badgeC` 全球疫苗公平 — 暗红 `#8C2F1B`
  - `badgeD` 下一代平台 — 琥珀 `#B4632C`
- **背景母题**：一只"免疫之眼"轮廓 + 自眼内射出的 RNA 链细线，四色 badge 如抗体般环绕。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — mRNA 疫苗的免疫学之眼 / Drew Weissman 1959– + 四色 badge + 右上头像 + 国籍行 USA
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生 Lexington、教育 Brandeis BA/MA 1981/
    波士顿大学 MD-PhD 1987、导师 Marshak-Rothstein、NIH 博后 Fauci、
    任职宾大 Roberts 家庭疫苗研究讲席/RNA 创新研究所所长、
    荣誉 Nobel 2023/Lasker 2021/Breakthrough 2022、核心领域）
03  核心贡献概览 — RNA 的先天免疫识别 / 核苷修饰共研 / LNP 递送 / 下一代 RNA 平台
04  列克星敦少年 (1959–1981) — 父犹太裔、母意大利裔、随家庆祝犹太节日、
    Lexington High School 1977、Brandeis 生物化学与酶学 BA/MA 1981（Fasman 实验室）
05  波士顿大学 MD-PhD (1981–1987) — 免疫学与微生物学、1987 论文
    （交联表面免疫球蛋白调控 B 淋巴细胞）、导师 Ann Marshak-Rothstein、
    Beth Israel Deaconess 住院医训练
06  NIH：Fauci 门下 (1987–1997) — NIAID 所长 Anthony Fauci 指导的 fellowship、
    艾滋病时代的免疫学训练——疫苗研究的起点
07  1997：复印机旁的相遇 — 新到宾大组建 RNA 与先天免疫实验室、
    与 Karikó 在复印机旁互相抱怨 RNA 研究缺经费、免疫学+生物化学的互补组合、
    引语 "We had to fight the entire way."（可引原文）
08  2005：先天免疫识别的破解 — 合成 RNA 高度致炎而 tRNA 不然的对照洞察、
    核苷修饰抑制免疫应答的系列里程碑（Karikó-Ni-Capodici-Lamphier-Weissman 2004 JBC、
    Karikó 等 2005 Immunity）、发表时几乎无人问津
09  LNP 递送与 RNARx — 脂质纳米颗粒包裹 mRNA、动物实验验证、
    2006 共同创立 RNARx、专利 US8278036B2/US8748089B2、授权链（Cellscript→Moderna/BioNTech）
10  2020：疫苗的全球部署 — 修饰 RNA 技术成为 Pfizer/BioNTech 与 Moderna 新冠疫苗的
    关键基础组件、史无前例的开发速度、全球部署
11  泰国合作与疫苗公平 — 与朱拉隆功大学合作、为泰国及中低收入国家开发并提供新冠疫苗
12  下一代 RNA 平台 — 泛冠状病毒疫苗、体内生产缺失抗体的基因编辑、
    急性炎症治疗；流感/疱疹/HIV 疫苗愿景
13  2023 诺贝尔奖与荣誉序列 — 两人共享诺奖（10-02 宣布）、
    Rosenstiel 2020/Horwitz/Albany/Lasker-DeBakey 2021、BBVA（与 Langer）、
    Princess of Asturias 2021、Breakthrough/Japan Prize/Koch/Tang/Novo Nordisk 2022、
    Harvey 2023、NAS 医学与 AAA&S 院士 2022
14  遗产 — 粉丝信 "You've made hugs and closeness possible again"（华盛顿邮报转述，可引）、
    从边缘技术到全球公卫基石、宾大 Roberts 讲席与 RNA 创新研究所、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方逐字 "for their discoveries concerning nucleoside base modifications that enabled the development of effective mRNA vaccines against COVID-19"（两人共享，their） |
| 合作双叙事 | 复印机相遇与"免疫学+生物化学互补"是两人篇共用的核心叙事——本篇以免疫学视角讲述，与 Karikó 篇区分视角 |
| Fauci 定位 | NIH fellowship **导师**（时任 NIAID 所长）——advisor-student 边；勿写成"共事/合作" |
| Brandeis Fasman | 本科实验室（生物化学与酶学）——不入库（弱关系，裁定记录），正文一句带过 |
| 专利号 | US8278036B2 与 US8748089B2（与 Karikó 共同发明人）——数字勿错 |
| Lasker 届别 | 2021 Lasker-DeBakey 临床奖（与 Karikó）；BBVA 前沿奖则**与 Robert S. Langer 三人共享**——两类共享对象勿混 |
| Weissman 名言 | "We had to fight the entire way."（page.md 英文原文在）——两人篇均可用，注明语境是经费与认可的困境 |
| 粉丝信引语 | 华盛顿邮报转述粉丝来信 "You've made hugs and closeness possible again"——注明系 WaPo 转述的读者来信 |
| Karikó 姓名一致 | 对手方名统一 Katalin Karikó（带重音），勿用 "Kati Kariko" |
| 家庭背景 | 父犹太裔、母意大利裔（未改宗）、随家过犹太节日——page.md 明载背景，一句带过 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| innate immunity | 先天免疫 | 其免疫学主线 |
| Toll-like receptor | Toll 样受体 | RNA 作为内源配体的识别者 |
| nucleoside modification | 核苷修饰 | 获奖理由核心词 |
| lipid nanoparticle (LNP) | 脂质纳米颗粒 | 递送系统 |
| pan coronavirus vaccine | 泛冠状病毒疫苗 | 下一代项目 |
| Roberts Family Professor | Roberts 家庭讲席教授 | 宾大疫苗研究首任 |
| Penn Institute for RNA Innovation | 宾大 RNA 创新研究所 | 其任所长 |
| Chulalongkorn University | 朱拉隆功大学 | 泰国疫苗公平合作 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Awaken**（manifest 预分配）
- **风格**：觉醒 / 上扬 / 黎明感
- **匹配理由**：免疫系统的"觉醒与耐受"恰是其科学主题——让免疫认出该认的、放过该放的；Awaken 的黎明感匹配"无人问津的 2005 论文在十五年后唤醒全球疫苗平台"的弧线。
- **本地路径**：`music_audio/alex-productions/36-aqLUvpAdLNQ-Awaken.wav` → 复制为 `presentations/21th_century/Drew_Weissman/Awaken.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；Fauci 导师定位与专利号务必精确。**
