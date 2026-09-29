# 医学家立传提示词（Johannes Fibiger）

> OpenMedic 项目、20 世纪诺贝尔生理学或医学奖 1926 年得主（约翰内斯·菲比格，科学史上最著名的诺奖误判之一）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Johannes Andreas Grib Fibiger（1867-04-23 生于丹麦 Silkeborg ~ 1928-01-30 卒于哥本哈根，享年 60 岁）
- **气质关键词**：** Spiroptera carcinoma 的"发现者"、哥本哈根病理解剖学教授、对照临床试验的先驱——以及诺奖史上被事后证伪的得主** —— 1926 获奖理由（独享，1927 年补发）：
  > "for his discovery of the Spiroptera carcinoma"（因其发现螺旋体癌）
- **设计母题**：**显微镜下的双面**。同一视野：一侧是线虫与胃乳头状瘤，另一侧是维生素 A 缺乏的假象——"结论的真伪由时间裁决"是本篇的叙事张力。视觉隐喻可用裂开的培养皿/镜像显微视野。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Johannes_Fibiger/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/20th_century/Johannes_Fibiger/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准，裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/20th_century/Johannes_Fibiger/`（含 `images/`）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=Johannes_Fibiger_zh`、`VIDEO_NAME=Johannes_Fibiger_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/20th_century/Johannes_Fibiger/images.txt`；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/Johannes_Fibiger.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | cancer research | 癌症研究 | Spiroptera carcinoma 实验致癌，1926 诺奖核心 | 核心页 |
| 1 | anatomical pathology | 病理解剖学 | 哥本哈根大学教授（1900）兼研究所所长 | 身份页 |
| 2 | bacteriology | 细菌学 | 白喉杆菌两型与血清疗法；1898 对照试验 | 白喉页 |
| 3 | parasitology | 寄生虫学 | Gongylonema neoplasticum（Spiroptera carcinoma） | 核心页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Robert Koch | 导师 | 1890 年代赴柏林随其学习细菌学 |
| advisor-student | Emil Adolf von Behring | 导师 | 赴柏林随其学习（白喉抗毒素发现者） |
| colleague | C. J. Salomonsen | 无向 | 1891-1894 在其哥本哈根大学细菌学系任助手 |
| collaborator | Hjalmar Ditlevsen | 无向 | 1914 共同描述 Spiroptera (Gongylonema) neoplastica |
| spouse | Mathilde Fibiger | 无向 | 表亲，1894-08-04 结婚 |

> 不入库：Katsusaburo Yamagiwa（1926 同获提名但**未共享**、未颁奖当年，非 co-honored，且二人无私人交往）；山极的搭档 Koichi Ichikawa；批评者 Bullock/Rohdenburg、Passey/Léese/Knox、Cramer、Hitchcock/Bell（学术证伪链条，可叙事不入库）；Karolinska 评审 Henschen/Bergstrand/Hammersten（机构评审）。哥本哈根大学的命名者叔父（clergyman/poet）仅称谓未具名。
> 库内当时无 Robert Koch / Emil Adolf von Behring 等记录，均由本 yaml 新建 stub（对手方名用 page.md 正文形式 Robert Koch / Emil Adolf von Behring / C. J. Salomonsen / Hjalmar Ditlevsen / Mathilde Fibiger）。

## 五、配色方案 【人物专属】

- **气质**：丹麦的冷冽 + 病理切片的暗红 + 历史反思的灰
- **主色**：暗酒红 `#7E1E23`（病理组织的暗红，兼作"警示色"——本篇自带科学史警示意味）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` 癌症研究 — 暗酒红 `#7E1E23`
  - `badgeB` 病理解剖 — 灰紫 `#5C5470`
  - `badgeC` 细菌学/白喉 — 钢蓝 `#2E4A66`
  - `badgeD` 寄生虫学 — 琥珀 `#A0722D`
- **背景母题**：圆形"显微视野"框线 + 半明半暗的对分圆（真/伪的双面母题），badge 圆点散布如镜下视野。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — 诺奖误判的主角 / Johannes Fibiger 1867–1928 + 四色 badge + 右上头像 + 国籍行 Denmark
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 Silkeborg/Copenhagen、教育 Copenhagen、
    柏林游学 Koch/Behring、任职 Copenhagen 病理解剖学教授、荣誉 Nobel 1926、author abbrev. Fibiger）
03  核心贡献概览 — 白喉对照试验 / 线虫致癌实验 / 双重身后遗产（方法论为真·致癌结论为伪）
04  西日德兰少年 (1867–1890) — Silkeborg、三岁丧父、母办哥本哈根第一所烹饪学校维生、
    叔父资助求学、1883 入哥本哈根学动物学植物学、1890 医学学位
05  柏林游学与哥本哈根起步 (1890–1897) — 随 Koch 与 von Behring 学习、Salomonsen 细菌学系助手
    (1891-94)、皇家陆军军医 (1894-97)、1895 博士论文《白喉细菌学研究》
06  白喉研究与 1898 对照试验 — 白喉杆菌两型（鼻咽型/皮肤型）、血清疗法、
    484 名患者分组对照——被 BMJ 1998 视为首个强调随机分配的对照临床试验
07  病理解剖学教授 (1897–1907) — 1897 prosector、1900 正教授兼研究所所长、
    军队中央实验室主任与军医顾问（1905）
08  1907：杜尔伯特大鼠 — 研究大鼠结核时于 Dorpat（今 Tartu）野鼠胃中发现乳头状瘤与线虫及虫卵、
    部分瘤体转移性——提出线虫致癌假说
09  1913：实验致癌"成功" — 健康大鼠实验致癌、三连论文、丹麦皇家科学院与布鲁塞尔第三届国际癌症
    会议报告——时评"实验医学最伟大的贡献"
10  命名之争 — 1907 新种、1914 命名 Spiroptera carcinom(a)、与 Ditlevsen 定名
    Spiroptera (Gongylonema) neoplastica、1918 Ditlevsen 修订为 Gongylonema neoplasticum——
    Fibiger 终生只用旧名
11  诺贝尔奖曲折 (1920–1927) — 1920 起 18 次提名、1926 与 Yamagiwa 同获提名但委员会决定当年
    空缺（Henschen 主分奖 vs Bergstrand 反对）、1927 年七次提名补发 1926 奖、
    Karolinska 否决拟同获的 Warburg（1931 才得奖）——Fibiger 独得
12  身后的证伪 (1935–1952) — 1918 Bullock/Rohdenburg 质疑、Fibiger 辩护引语、
    1935 Passey 组证伪、1937 Cramer 实验证实非癌、1952 Hitchcock/Bell 终局：
    肿瘤实为维生素 A 缺乏、线虫仅为组织刺激——Norrby 2010 称之为 Karolinska 最大乌龙之一
13  个人生活与逝世 — 表亲 Mathilde (1863-1954)、1894-08-04 结婚、二子女、
    患结肠癌、领奖一个月后 1928-01-30 心脏骤停逝世
14  遗产 — 双面遗产：致癌结论被证伪 vs 临床试验方法论为真（并提 Yamagiwa 未得奖的公认遗憾、
    Britannica 只列 Yamagiwa、以及吸虫类致癌寄生虫的确立）、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖年份结构 ★ | 1926 年度奖**当年未颁**（与 Yamagiwa 同获提名、委员会空缺）；**1927 年补发 1926 奖且 Fibiger 独得**；勿写成"1926 与 Yamagiwa 共享"或"1927 年奖" |
| Warburg 变数 | 1927 评审建议 1926 奖由 Fibiger 与 Otto Heinrich Warburg 共享，Karolinska 因未公开理由否决 Warburg——Warburg 1931 才获奖；链条勿简化 |
| 结论被证伪 ★ | G. neoplasticum 不致癌；肿瘤实为**维生素 A 缺乏**所致、线虫仅提供慢性刺激；1935 Passey/Léese/Knox、1937 Cramer、1952 Hitchcock/Bell 三级证伪——必须如实呈现，不可只写获奖光环 |
| Norrby 引语 | 2010 年 Norrby 称之为 "one of the biggest blunders made by the Karolinska Institute"——可引用（page.md 英文原文在），须署名身份（前常务秘书） |
| 名字规范 | 官方获奖理由用 **Spiroptera carcinoma**（Fibiger 终生坚持的旧名）；正式名 Gongylonema neoplasticum（Ditlevsen 1918）——两个名都要出现并说明关系 |
| Fibiger 辩护引语 | "That these tumors are true carcinomata cannot, thus, be doubted..."（回应 Bullock/Rohdenburg 1918）——page.md 有英文原文，可引用 |
| 首个对照试验 | 1898 白喉血清试验（484 人分组）被 BMJ 1998 文章视为首个**强调随机分配**的临床试验——表述带"被视为/regarded"口径 |
| 死因细节 | 结肠癌恶化、1928-01-30 心脏骤停；"领奖一个月后"——1926 奖实际 1927 领取，时间线表述须自洽 |
| 导师口径 | page.md 载"随 Koch 与 Emil Adolf von Behring 学习"（短期游学）——入库 advisor-student 但 note 不宜写"博士导师"（博士论文完成于哥本哈根，1895） |
| metadata 冲突 | metadata nationality "Kingdom of Denmark"、导师列表同上——以 page.md 为准；author abbreviation (zoology) "Fibiger" 可作趣闻 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| Spiroptera carcinoma | 螺旋体癌（旧名） | 获奖理由用名；非正式学名 |
| Gongylonema neoplasticum | 筒线虫（正式名） | Ditlevsen 1918 定名 |
| papilloma | 乳头状瘤 | 非癌性瘤，证伪关键 |
| squamous cell carcinoma | 鳞状细胞癌 | Fibiger 声称诱发的癌型 |
| metastatic | 转移性 | 1907 观察中的误判点 |
| vitamin A deficiency | 维生素 A 缺乏 | 1952 终局归因 |
| controlled clinical trial | 对照临床试验 | 1898 白喉试验的历史地位 |
| diphtheria | 白喉 | 博士论文与血清研究主题 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Through the Darkness**（manifest 预分配）
- **风格**：黑暗中前行 / 悲剧感 / 史诗反思
- **匹配理由**：本篇是科学史的"走入黑暗"——从"实验医学最伟大贡献"的桂冠到身后三级证伪的漫长黑隧道；黑色调曲风匹配"诺奖乌龙"的悲剧叙事，也呼应其临终前一个月领奖的苍凉。
- **本地路径**：`music_audio/inspiring-electronic/14-Trn1cSsY2t8-Audiomachine - Through the Darkness.wav` → 复制为 `presentations/20th_century/Johannes_Fibiger/Through_the_Darkness.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；证伪链条必须完整呈现，不可隐去。**
