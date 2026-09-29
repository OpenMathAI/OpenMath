# 医学家立传提示词（Robert Koch）

> OpenMedic 项目 · 20 世纪诺贝尔生理学或医学奖 1905 年得主 · 本文件是该人物的专属立传提示词，
> 按 9 节结构执行 Beamer 立传；数据库入库（fields/relations）已由批次完成，本文件第四/三节与 yaml 一致。

## 一、背景信息 【人物专属】

- **目标医学家**：Heinrich Hermann Robert Koch（1843-12-11 生于 Clausthal ~ 1910-05-27 逝于 Baden-Baden，享年 66 岁）
- **气质关键词**：**现代细菌学之父（与 Pasteur 并称）、科赫法则、结核杆菌的发现者** —— 1905 年获奖理由（逐字引用 medic/nobel_medicine_citations.json）：
  > "for his investigations and discoveries in relation to tuberculosis"
  > （因其关于结核病的研究与发现）
- **设计母题**：**显微镜下的蓝色杆菌（methylene blue bacilli）**。亚甲蓝染色涂片上"beautiful blue"的细长杆菌——以染色涂片的微观视觉贯穿全篇。
- **本地 Wikipedia 路径**：medic/presentations/pages/20th_century/Robert_Koch/page.md
- **参考模板**：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）

## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章）

- 第 0/1/2/3 步按 **medic 路径**执行：事实基准 = `medic/presentations/pages/20th_century/Robert_Koch/page.md`；目录 `medic/presentations/20th_century/Robert_Koch/`；Makefile 改 `MAIN=Robert_Koch_zh`；肖像优先 images.txt 所列 Commons 图（Koch c.1900 等），失败用装饰圆占位。
- 第 4/4.5 步（入库）**已完成**（第三、四节与 `MySQL/data/Robert_Koch.yaml` 一致，勿重复入库）。
- 第 5-9 步：配色 → 幻灯片 → Beamer → 布局检查（0 error、vbox≤10pt、hbox≤50pt、逐页目检）→ 史实审查（第七节）。

## 三、研究领域梳理 + 入库（rank 0-4 表）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | microbiology | 微生物学 | 细菌学奠基、纯培养技术 | 技术页 |
| 1 | bacteriology | 细菌学 | 炭疽/结核/霍乱杆菌发现 | 发现页 |
| 2 | infectious diseases | 传染病学 | Koch 法则、病原-疾病因果链 | 法则页 |
| 3 | tuberculosis | 结核病 | 结核杆菌 1882、结核素 | 结核页 |

## 四、社会关系梳理 + 入库（与 yaml 完全一致，已完成）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Georg Meissner | 师→本人 | Göttingen 博士导师（infobox 明载） |
| advisor-student | Jacob Henle | 师→本人 | 子宫神经结构研究项目导师，传染病学说先驱 |
| advisor-student | Karl Ewald Hasse | 师→本人 | infobox Other academic advisors 明载 |
| advisor-student | Rudolf Virchow | 师→本人 | 短期师从；后对细菌学说持怀疑并公开质疑 |
| advisor-student | Emil von Behring | 本人→学生 | 帝国卫生局门生，1901 首届医学诺奖 |
| advisor-student | Shibasaburo Kitasato | 本人→学生 | infobox Notable students 明载 |
| advisor-student | Richard Pfeiffer | 本人→学生 | 霍乱委员会同事，infobox 明载学生 |
| advisor-student | Friedrich Loeffler | 本人→学生 | 助手，1883 提出三准则（Koch 法则雏形） |
| advisor-student | August von Wasserman | 本人→学生 | infobox Notable students 明载 |
| advisor-student | George Gaffky | 本人→学生 | 1884 发现伤寒杆菌，infobox 明载学生 |
| controversy | Louis Pasteur | 无向 | 炭疽疫苗与细菌学方法公开论战（1882 日内瓦） |
| colleague | Julius Richard Petri | 无向 | 助手，1887 改良培养皿 |
| colleague | Walther Hesse | 无向 | 博士后助手，建议用琼脂培养基 |
| colleague | Ferdinand Julius Cohn | 无向 | 帮其发表炭疽杆菌研究（1876），布雷斯劳邀请 |
| spouse | Emma Fraatz | 无向 | 1867 结婚，1893 离异，育女 Gertrude |
| spouse | Hedwig Freiberg | 无向 | 1893 结婚，演员 |

> 对手方规范名：库内已有 `Paul Ehrlich`(id=766) 复用；`Emil von Behring`/`Shibasaburo Kitasato` 与本批次 Behring 篇 yaml 同形式（Kitasato 统一 ASCII 形式），镜像 advisor-student 边幂等合并；其余按 page.md 形式新建 stub。

## 五、配色方案

- **气质**：德意志实验室的冷峻精确 + 病原学的肃杀 + 治国卫生的宏阔
- **主色**：杆菌红 `#7E1E23`（亚甲蓝背景上的结核杆菌 / WHO 结核日警示色）
- **诺奖香槟金**：`#D4AF37`
- **badge 四分类色**：
  - `badgeA` 细菌学技术 — 亚甲蓝 `#2E5E9E`
  - `badgeB` 结核研究 — 病灶深红 `#8C1F28`
  - `badgeC` 霍乱与热带考察 — 尼罗青 `#1B6B5A`
  - `badgeD` Koch 法则与建制 — 石墨灰蓝 `#3A4A6B`
- **背景母题**：低透明度显微视野圆 + 散在短杆菌线条，色调用亚甲蓝渐变。

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 现代细菌学之父 / Robert Koch 1843–1910 + 四色 badge + 右上头像 + 国籍行（Germany）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Clausthal、Göttingen 1866 maxima cum laude、帝国卫生局、柏林大学、RKI、诺奖 1905）
03  核心贡献概览 — 炭疽杆菌 / 纯培养技术 / 结核杆菌 / 霍乱弧菌 / Koch 法则
04  早年与哥廷根 (1843–1866) — 矿工之子十三弟妹、自学会读写、Henle 研究项目获奖、短期师从 Virchow、1866 最高荣誉毕业
05  沃尔施泰因的私人实验室 (1872–1880) — 区医、妻子赠显微镜生日礼、民间实验室里的细菌学革命
06  1876 炭疽：第一个被证明的病原 — 炭疽杆菌生活史与芽孢、Cohn 帮助发表、"birth of modern bacteriology"；1877 首张细菌显微照片
07  技术革命： oil immersion/聚光器/显微摄影 — 亚甲蓝与 Bismarck brown 染色、马铃薯→明胶→琼脂（Walther Hesse 建议自其妻 Fanny）、Petri 1887 改良培养皿（"本可叫 Koch dish"，page.md 明载可引一句）
08  1882-03-24 结核杆菌 — 染色描述英文原文可引（"remained a beautiful blue"）、Virchow 质疑、Loeffler 1883 三准则；今为 World Tuberculosis Day
09  结核素风波 (1890–1891) — 伦敦大会模糊宣布、保密动机、1891 临床失败"最大的失败"、Koch's phenomenon、声誉重挫与皇家研究所转任
10  霍乱远征 (1883–1884) — 埃及亚历山大→加尔各答、恒河水源、1884-01-07 纯培养、"a little bent, like a comma"；Pacini 先发现注记、Pfeiffer 1896 命名 Vibrio cholerae
11  获得性免疫与新几内亚 (1900) — 巴布亚人疟疾亚临床、移民渐获耐受
12  1905 诺贝尔奖与荣誉 — 官方理由全句、Pour le Mérite 1906、ForMemRS 1897、Robert Koch Medal 1908；身后研究所更名 RKI
13  论战三案（客观呈现）— Pasteur 论战（1882 日内瓦"unreliable/false conclusions"英文原句可引）/ 人牛结核之争（Theobald Smith 1898、1901 伦敦 Lister 训斥）/ 1902 诺奖仲裁倾斜 Ross（本批 Ross 篇互见）
14  家庭与身后 — Emmy Fraatz（1867，女 Gertrude）/ Hedwig Freiberg（1893）；1910-04-09 心梗、05-27 演讲三日后逝于 Baden-Baden；Google Doodle 2017
15  结尾（OpenMathAI 品牌口径）
```

## 七、特殊陷阱表（★ 核心）

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 仅"tuberculosis 相关研究与发现"——勿泛化为"细菌学全部成就"或混入霍乱 |
| Koch 法则归属 | Koch 提出**原理与实验证明**，法则条文由助手 **Loeffler 1883** 成文（三准则），第四条 1905 年由 Erwin Frink Smith 增补——归属勿写反 |
| Petri dish | Petri 只是把玻璃板改为圆皿的直接培养容器（1887 论文改良），并非"发明全新培养皿"；page.md 明载"本可叫 Koch dish" |
| 结核素 | 1890 治疗宣告失败（"greatest failure"）；后世用于结核皮试（诊断）——治疗/诊断两用勿混 |
| tuberculin 命名 | 名称 1844 年已由 Josephs Pohl-Pincus 用于结核培养基，Koch 沿用为 "tuberkulin"——勿写"Koch 命名" |
| 霍乱杆菌 | Pacini 1854 已描述、Balcells 同期观察，但未确证病原；Koch 纯培养确证；命名 Vibrio cholerae 是 Pfeiffer 1896——链条勿简化为"Koch 发现命名" |
| 人牛结核 | Koch 1882 主张两型不同→1884 改口同一→Theobald Smith 1898 证明不同→Koch 1901 仍称牛型无害被 Lister 训斥；立场反复须按年代呈现 |
| 1902 仲裁 | Koch 作诺奖"中立仲裁人"倾斜 Ross（与 Ross 有私谊、与 Grassi 有旧怨）——与 Ross 篇交叉注记，客观陈述 |
| 学生名单 | 七人以 infobox Notable students 为准（Wasserman/Ehrlich/Pfeiffer/Behring/Kitasato/Loeffler/Gaffky）；Hasse 为 infobox Other academic advisors（正文零载，裁定仍入库因属 page.md） |
| 妻子次序 | Emmy Fraatz 1867 结婚 1893 离异（育 Gertrude）；同年娶演员 Hedwig Freiberg——两段婚姻勿混 |
| 死亡地点 | 1910-05-27 逝于 Baden-Baden（心梗 04-09 后），勿写柏林 |
| 引语红线 | 仅引 page.md 有英文原文的句子（1882 染色描述、1881 炭疽论断、对 Pasteur 的批评、1881 伦敦 Pasteur 惊叹 "C'est un grand progrès, Monsieur!"）；其余禁杜撰 |
| Ehrlich 师承 | infobox 列其为门生，但博士学位系莱比锡 Cohnheim 门下（1878），Koch 仅是事业影响者（自述受结核菌发现震动最深），库内按 colleague 入库、不建 advisor-student 边 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| Koch's postulates | 科赫法则 | Loeffler 成文/Smith 增第四条 |
| Bacillus anthracis | 炭疽杆菌 | 1876 证明病原 |
| Mycobacterium tuberculosis | 结核杆菌 | 1882-03-24 宣布 |
| Mycobacterium bovis | 牛结核杆菌 | 与人型之别，Theobald Smith 1898 |
| Vibrio cholerae | 霍乱弧菌 | Pfeiffer 1896 命名 |
| tuberculin | 结核素 | 治疗失败/皮试沿用 |
| agar plate | 琼脂平板 | Hesse 夫妇建议（1881） |
| Petri dish | 培养皿 | Petri 改良非首创 |
| pure culture | 纯培养 | 细菌学方法基石 |
| microphotography | 显微摄影 | Koch 首次有效用于细菌 |

## 九、背景音乐选择

- **选定曲目**：**Awaken** — Alex-Productions（manifest 预分配）
- **匹配理由**："觉醒/揭开"气质贴合病原微生物世界的揭示——1876 炭疽到 1882 结核杆菌，人类第一次看清瘟疫的真身；带推进感的曲式呼应帝国卫生局时代的高强度攻坚。
- **本地路径**：music_audio/ 下 Alex-Productions Awaken 曲目（执行时按 curated_tracks.md 对应文件复制到本目录）。
