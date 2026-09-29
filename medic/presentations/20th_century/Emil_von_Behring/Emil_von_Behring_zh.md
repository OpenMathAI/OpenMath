# 医学家立传提示词（Emil von Behring）

> OpenMedic 项目 · 20 世纪诺贝尔生理学或医学奖 1901 年（首届）得主 · 本文件是该人物的专属立传提示词，
> 按 9 节结构执行 Beamer 立传；数据库入库（fields/relations）已由批次完成，本文件第四/三节与 yaml 一致。

## 一、背景信息 【人物专属】

- **目标医学家**：Emil von Behring（1854-03-15 生于普鲁士 Hansdorf（今波兰 Ławice） ~ 1917-03-31 逝于马堡，享年 63 岁）
- **气质关键词**：**首届诺奖得主、血清疗法的开创者、儿童的救星（"saviour of children"）** —— 1901 年获奖理由（逐字引用 medic/nobel_medicine_citations.json）：
  > "for his work on serum therapy, especially its application against diphtheria , by which he has opened a new road in the domain of medical science and thereby placed in the hands of the physician a victorious weapon against illness and deaths"
  > （因其对血清疗法的研究，特别是其用于对抗白喉——由此在医学科学领域开辟了一条新路，把战胜疾病与死亡的胜利武器交到医生手中）
- **设计母题**：**盾与血清滴（shield & serum droplet）**。抗毒素血清 = 注入体内的"武器"：一滴血清在血液中化作抵御毒素的屏障——用盾牌轮廓 + 液滴 + 免疫网络的视觉隐喻贯穿全篇。
- **本地 Wikipedia 路径**：medic/presentations/pages/20th_century/Emil_von_Behring/page.md
- **参考模板**：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）

## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章）

- 第 0/1/2/3 步按 **medic 路径**执行：页面事实基准 = `medic/presentations/pages/20th_century/Emil_von_Behring/page.md`；目录建在 `medic/presentations/20th_century/Emil_von_Behring/`；Makefile 复制自 Kenneth 模板改 `MAIN=Emil_von_Behring_zh`；肖像从同目录 images.txt 所列 Commons 图下载（失败则 Wikipedia REST API page/summary 查 infobox 原图名，再失败用装饰圆占位）。
- 第 4/4.5 步（fields/relations 入库）**已完成**（本文件第三、四节与 `MySQL/data/Emil_von_Behring.yaml` 一致，执行时勿重复入库）。
- 第 5-9 步：配色 → 幻灯片序列 → Beamer 源码 → 布局检查（0 error、vbox≤10pt、hbox≤50pt、pdftoppm 逐页目检）→ 史实/术语审查（对照第七节陷阱表）。

## 三、研究领域梳理 + 入库（rank 0-4 表）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | immunology | 免疫学 | 抗毒素/抗体血清疗法开创 | 抗毒素页、诺奖页 |
| 1 | bacteriology | 细菌学 | Koch 学派出身，感染与免疫 | 早年页 |
| 2 | serum therapy | 血清疗法 | 白喉/破伤风抗毒素，1890 联名论文 | 核心页 |
| 3 | physiology | 生理学 | page.md 介绍身份 "German physiologist" | 封面 |

## 四、社会关系梳理 + 入库（与 yaml 完全一致，已完成）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Robert Koch | Koch→本人 | 转入 Koch 领导的帝国卫生局实验室，师承关系 |
| collaborator | Shibasaburo Kitasato | 无向 | 1890 白喉/破伤风抗毒素联名论文 |
| advisor-student | Hans Schlossberger | 本人→学生 | infobox Notable students 明载 |
| colleague | Paul Ehrlich | 无向 | 合作研制白喉马血清 |
| controversy | Paul Ehrlich | 无向 | 白喉血清商业化独占利益，挤占 Ehrlich 荣誉 |
| spouse | Else Spinola | 无向 | 1896 结婚，Charité 院长之女，育六子 |
| colleague | Hans Horst Meyer | 无向 | 马堡同楼实验室，激发其破伤风毒素研究 |

> 对手方规范名说明：库内已有 `Paul Ehrlich`(id=766) 直接复用；`Robert Koch`/`Shibasaburo Kitasato` 由本批次统一形式新建（Kitasato 全篇用 ASCII 形式 Shibasaburo Kitasato，勿用 Kitasato Shibasaburō 产生分裂）。

## 五、配色方案

- **气质**：普鲁士军医的严谨 + 首届诺奖的历史分量 + 拯救儿童的温度
- **主色**：普鲁士深蓝 `#16324F`（军医学院与德意志帝国的庄重）
- **诺奖香槟金**：`#D4AF37`
- **badge 四分类色**：
  - `badgeA` 血清疗法 — 医疗青 `#2E86AB`
  - `badgeB` 白喉 / 破伤风 — 警示红 `#B23A48`
  - `badgeC` 细菌学 Koch 学派 — 深靛 `#3A4A6B`
  - `badgeD` Behringwerke 产业 — 琥珀 `#C97B2D`
- **背景母题**：稀疏的血清滴与细线免疫网络（低透明度大圆 + 连线），呼应"一滴血清化作屏障"。

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 首届诺贝尔生理学或医学奖得主 / Emil von Behring 1854–1917 + 四色 badge + 右上头像 + 国籍行（Germany）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地 Hansdorf、Kaiser Wilhelm Academy、师承 Koch、马堡教授、诺奖 1901）
03  核心贡献概览 — 抗毒素 / 血清疗法 / 白喉 / Behringwerke
04  早年：军医之路 (1854–1889) — 13 子之家、Kaiser Wilhelm Academy 1874-78（因家境从军入学）、眼科研究（Poznań、Schweigger/Uhthoff、眼肿瘤论文）
05  帝国卫生局：Koch 门下 (1880s) — 与 Kitasato 相遇、细菌学派训练
06  1890：抗毒素的诞生 — 豚鼠/山羊/马免疫实验、"to stimulate the body's internal disinfection"（page.md 英文原文可引）
07  白喉血清走向临床 (1892–1894) — 1892 首次人体试验失败、1894 优化后成功 + Cameron Prize
08  马堡岁月 (1895–1901) — 卫生学教授（终身职）、与 Hans Horst Meyer 同楼
09  首届诺贝尔奖 (1901) — 官方理由全句、Kitasato 同获提名未获奖（当年只授一人）
10  荣誉与贵族 — 1901 普鲁士贵族封号 "von"、1902 AAAS 外籍荣誉会员
11  Behringwerke 与结核 (1904–1917) — 创办血清疫苗公司、"T C" 物质与牛结核 bovivaccine（人体防治未成功）
12  争功公案：与 Ehrlich — 合作与决裂（客观呈现，仅 page.md 实载两点）
13  家庭与身后 — Else Spinola、六子、Capri 别墅（Gorky 曾居）、Behring 陵墓；名字存于 CSL Behring/Dade Behring；诺奖章藏于日内瓦红十字博物馆
14  遗产：儿童的救星 — 白喉从儿童头号杀手变为可防可治
15  结尾（OpenMathAI 品牌口径）
```

## 七、特殊陷阱表（★ 核心）

| 陷阱 | 说明 |
|------|------|
| 获奖理由表述 | 官方全句以 citation json 为准（serum therapy 尤其针对 diphtheria）；勿缩写成"发现白喉抗毒素"单点 |
| Kitasato 名字形式 | Behring 篇与 Koch 篇统一用 **Shibasaburo Kitasato**（ASCII）；勿用 Kitasato Shibasaburō 长音符形式造成库内分裂 |
| Kitasato 未获奖 | page.md 明载其获提名但未获奖（"only given to a single awardee at the time"），可写；勿写"被抢功" |
| 与 Koch 关系 | page.md 载"work under Robert Koch"于帝国卫生局（metadata 列为 doctoral_advisor）；勿写成 Koch 指导其博士论文（其医学博士学位论文实为视神经切断术方向，完成于军医体系） |
| Ehrlich 公案 | 仅写 page.md 实载两点：合作研制马血清 + 独占商业合同利益；措辞用 "is believed to have cheated"（转述），勿定性为"欺诈" |
| 1892 vs 1894 | 首次人体试验 1892 **失败**；成功治疗始于 1894（抗毒素生产与定量优化后），勿混淆 |
| 贵族封号 | 1901 年因获奖获普鲁士贵族身份，此后姓 "von Behring"；出生名 Emil Adolf Behring |
| 眼科阶段 | 早年有正式眼科研究（Wicherkiewicz 医院、Schweigger/Uhthoff 指导、眼肿瘤临床论文），勿省略 |
| 1905 结核声明 | 国际结核大会上宣布发现 "T C" 物质用于牛结核疫苗（bovivaccine）；人体防治**未成功**，勿写成成功 |
| 死亡地点 | 1917-03-31 逝于马堡（Marburg, Hesse-Nassau），勿与出生地混淆 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| serum therapy | 血清疗法 | 当时称谓，即抗毒素血清治疗 |
| antitoxin | 抗毒素 | 今知含抗体；勿与"抗生素"混淆 |
| diphtheria | 白喉 | 儿童头号死因之一 |
| tetanus | 破伤风 | 与白喉同期 1890 论文对象 |
| Behringwerke | 贝林工厂（贝林制品厂） | 1904 年马堡创办的血清疫苗公司 |
| bovivaccine | 牛结核疫苗 | "T C" 物质制备 |
| Cameron Prize | 爱丁堡卡梅伦奖 | 1894 年获奖 |
| Prussian nobility | 普鲁士贵族封号 | 1901 年授予 |

## 九、背景音乐选择

- **选定曲目**：**Timeless** — Alex-Productions（manifest 预分配）
- **匹配理由**："长期纲领/沉稳/纪录片"气质贴合首届诺奖得主的历史分量——血清疗法不是单一突破而是现代免疫学的奠基；从军医少年到"儿童的救星"，是思想与制度演进的纪录。
- **本地路径**：music_audio/ 下 Alex-Productions Timeless 曲目（执行时按 curated_tracks.md 对应文件复制到本目录）。
