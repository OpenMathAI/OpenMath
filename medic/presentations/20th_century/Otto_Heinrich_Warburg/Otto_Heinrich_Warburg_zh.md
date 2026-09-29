# 医学家立传提示词（Otto Heinrich Warburg）

> 本文件是 OpenMedic 项目（OpenMathAI 诺贝尔生理学或医学奖人物史）20 世纪 1931 年得主 Otto Heinrich Warburg 的人物专属立传提示词。
> 事实基准：`medic/presentations/pages/20th_century/Otto_Heinrich_Warburg/page.md`（唯一事实来源，metadata.json 仅作参考）。
> 结构对齐标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（11 节合并为 9 节）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Otto Heinrich Warburg（1883-10-08 生于德意志帝国弗赖堡 ~ 1970-08-01 逝于西柏林，享年 86 岁）
- **气质关键词**：**呼吸酶的解密者、肿瘤代谢研究的开创者、瓦博格效应的命名来源** —— 1931 年诺贝尔生理学或医学奖**独享**，获奖理由（逐字引用 `medic/nobel_medicine_citations.json`）：
  > "for his discovery of the nature and mode of action of the respiratory enzyme"（因其发现呼吸酶的性质与作用方式）
- **设计母题**：**呼吸的曲线（the respiratory curve）**。海胆卵受精后呼吸率跃升六倍——一条耗氧曲线把"生命如何燃烧"变成可测量的量。视觉语言：测氧曲线的攀升、线粒体内微弱的火焰，比通用"实验室"更贴合其毕生主题：细胞呼吸。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Otto_Heinrich_Warburg/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）
- **关键时间线（身份信息页与时间轴素材，均出自 page.md）**：
  - 1883-10-08 生于弗赖堡（父 Emil Warburg 为物理学家、帝国物理技术研究院院长）
  - 1906 获柏林化学博士学位（Emil Fischer 门下）
  - 1908-1914 那不勒斯海洋生物站：海胆卵受精后呼吸率增至六倍、铁为幼体发育所必需
  - 1911 获海德堡医学博士学位（Ludolf von Krehl 门下）
  - 1914-1918 一战任骠骑兵（Uhlans）军官，获一级铁十字勋章（1918）
  - 一战末 Albert Einstein 受友人之托致信劝其返学界；后成挚友
  - 约 1918 起 Jacob Heiss 任其私人助理/秘书/行政助理（相伴 50 年）
  - 1918 任威廉皇帝生物学研究所教授（柏林达勒姆）
  - 1931 任威廉皇帝细胞生理学研究所所长（前一年由洛克菲勒基金会捐建）
  - 1931 获诺贝尔生理学或医学奖（独享；1923 起 9 年 46 次提名，当年 13 次）
  - 1932-1933 George Wald 在其实验室访问研究，发现视网膜中的维生素 A
  - 1935 按 Reichsbürgergesetz 被划为半犹太（Mischling）；被禁教学、准许研究
  - 1941 因批评政权言论短暂免职，数周后经总理府个人命令复职；1942-09 同权申请获准
  - 1943 实验室迁至柏林近郊 Liebenburg 躲避空袭
  - 1944 被 Szent-Györgyi 提名第二次诺奖（Nobel Foundation 否认"被政权阻止领奖"传闻）
  - 1952 获 Pour le Mérite；1962 出版《New Methods of Cell Physiology》
  - 1963 Otto Warburg 奖章设立（德国生化与分子生物学会）
  - 1968 股骨骨折并发深静脉血栓；1970-08-01 卒于西柏林（肺栓塞），葬 Dahlem 墓园

---

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章执行 Beamer 立传，**第 0/1/2/3 步按 medic 路径执行**：
> - 页面与元数据：`medic/presentations/pages/20th_century/Otto_Heinrich_Warburg/`（page.md / metadata.json / images.txt）
> - 目录创建：`medic/presentations/20th_century/Otto_Heinrich_Warburg/` 与 `images/`
> - Makefile：复制 medic 侧同结构模板，设 `MAIN=Otto_Heinrich_Warburg_zh`
> - 肖像：正文含 1931 年肖像 `Otto_Heinrich_Warburg_(cropped).jpg` 缩略 URL（250px 改 500px，curl 加 `-A "Mozilla/5.0"`，file 验证）；404 用 Commons `Special:FilePath` 回退；再失败用装饰圆占位
> 每完成一步汇报，溢出即修（make → pdftoppm 逐页目检）。

---

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biochemistry | 生物化学 | 诺奖核心：呼吸酶（细胞呼吸的氧化酶）的性质与作用方式 | 核心页 |
| 1 | cell biology | 细胞生物学 | infobox Fields 口径；细胞呼吸与代谢测量方法 | 研究页 |
| 2 | oncology | 肿瘤学 | 肿瘤代谢、瓦博格效应与瓦博格假说 | 假说页 |
| 3 | physiology | 生理学 | 本职学科；海胆卵受精后呼吸率六倍跃升（1908-14 那不勒斯） | 那不勒斯页 |

---

## 四、社会关系梳理 + 入库 【人物专属】

> 与 `MySQL/data/Otto_Heinrich_Warburg.yaml` 完全一致；只收 page.md 明载的关系。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Hermann Emil Fischer | 师→生 | 柏林化学博士导师（1906），库内规范名 id=3231 |
| advisor-student | Ludolf von Krehl | 师→生 | 海德堡医学博士（MD 1911）导师 |
| parent-child | Emil Warburg | — | 父，物理学家，帝国物理技术研究院院长，库内 id=2148 |
| influence | Albert Einstein | 无向 | 一战末受父友之托致信劝其返学界；后成挚友；爱因斯坦物理学工作对其生化研究影响甚大（库内 id=349） |
| colleague | George Wald | 无向 | 1932-33 在其实验室访问研究，期间发现视网膜中的维生素 A（后获 1967 诺奖），库内 id=3320 |
| colleague | Hans Adolf Krebs | 无向 | 曾在其实验室工作，后鉴定三羧酸循环并获 1953 诺奖 |
| collaborator | Dean Burk | 无向 | 合作研究光合作用的量子产额 |
| colleague | Anton Dohrn | 无向 | 那不勒斯海洋生物站所长，与其家族终身友好 |

**不入库裁定**：Jacob Heiss（约 1918 起的私人助理/秘书/生活伴侣 50 年、继承全部遗产）无白名单对应类型，不入库（叙事页可客观一笔）；Albert Szent-Györgyi 1944 年提名其第二次诺奖系提名事件非个人关系；Birgit Vennesland（转述轶事）、Josef Issels（愿为其作证）不入库；纳粹当局人物系政治背景非个人关系，一律不入库。

---

## 五、配色方案 【人物专属】

- **气质**：深邃、精微、把生命还原成一条耗氧曲线的执着
- **主色**：呼吸深海蓝 `#16324F`（与人物气质呼应——达勒姆研究所的长夜、细胞内的氧化之火）
- **诺奖色**：香槟金 `#D4AF37`
- **四分类色（badgeA-D）**：
  - `badgeA` 生物化学（呼吸酶）——氧化橙 `#B4632A`
  - `badgeB` 细胞生物学——线粒体青 `#2E7D6B`
  - `badgeC` 肿瘤学——病灶紫 `#6B4E9E`
  - `badgeD` 生理学——海水蓝 `#3A6FA8`
- **背景母题**：攀升的耗氧曲线与稀疏气泡（对应"呼吸的曲线"），badge 四色错落

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
01  封面 — 呼吸酶的解密者 / Otto Heinrich Warburg 1883–1970 + 四色 badge + 右上头像 + 国籍行（Germany）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、弗赖堡、双博士、达勒姆研究所、荣誉、核心领域）
03  核心贡献概览 — 呼吸酶（1931 诺奖）/ 肿瘤代谢 / 瓦博格效应 / 光合作用量子产额
04  弗赖堡与书香门第（1883–1906）— 物理学家 Emil Warburg 之子、柏林 Fischer 门下化学博士 1906
05  海德堡与那不勒斯（1906–1914）— Krehl 门下 MD 1911、海胆卵呼吸实验、铁与幼体发育
06  战壕与爱因斯坦来信（1914–1918）— 骠骑兵军官、铁十字勋章（一级）、Einstein 劝归学界
07  达勒姆研究所（1918–1931）— 威廉皇帝生物学研究所教授、1931 任细胞生理学研究所所长（洛克菲勒基金会捐建）
08  呼吸酶与 1931 诺奖（核心贡献页）— 46 次提名、独享
09  肿瘤代谢与瓦博格效应 — 肿瘤产生大量乳酸、瓦博格假说（引语页：有英文原文）
10  纳粹时期的幸存 — 半犹太身份、禁教准研、1941 短暂免职后复职、1942 同权申请获准、拒绝行纳粹礼
11  实验室里的后来诺奖得主 — Krebs 等三人、George Wald 访问（1932-33）、1944 二次提名与传闻澄清
12  荣誉与认可 — Pour le Mérite 1952、Paul Ehrlich 奖 1962、ForMemRS、Otto Warburg 奖章（1963 设立）
13  晚年与遗产 — 《New Methods of Cell Physiology》、1970-08-01 肺栓塞逝世、现代癌症代谢视角的再评估
14  结尾 — 一条耗氧曲线测出的生命之火
```

---

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方逐字为 "for his discovery of the nature and mode of action of the respiratory enzyme"（呼吸酶的性质与作用方式） |
| 独享与提名数 | 1931 为独享（sole recipient）；生涯共获提名 48 次；其中 1923 起 9 年内 46 次、1931 年当年 13 次——两组数字勿混 |
| 双博士 | 柏林化学博士 1906（Emil Fischer）+ 海德堡医学博士 1911（Ludolf von Krehl）——infobox Doctoral advisor 两值并列，两位都要入库 |
| 1944 二次提名 | "因希特勒政权禁令被阻止领奖"是传闻——Nobel Foundation 明确否认（当时未入选）；禁写传闻为事实 |
| Krebs 关系 | Krebs 系"曾在其实验室工作"后获 1953 诺奖（三羧酸循环），非其博士生——关系类型用 colleague |
| 癌症引语 | "Cancer, above all other diseases..." 段落 page.md 有英文原文（署名 Otto H. Warburg），可引用并给译文；同时须写明现代观点：突变是主因、代谢变化（Warburg effect）被认为是结果 |
| 纳粹叙事平衡 | Göring 改划四分之一犹太、1941 短暂免职后经总理府个人命令复职、1942-09 同权（Gleichstellung）获准、拒绝行纳粹礼——均 page.md 明载可写；"Apple 认为他低估了威胁"等系作者推测，引用时须标注为推测 |
| Jacob Heiss | 约 1918 起任私人助理/秘书/行政助理，达勒姆别墅同住 50 年，继承全部遗产——无对应关系类型不入库，叙事页可客观一笔 |
| Einstein 关系 | 两点依据：战末来信劝归学界 + "Einstein's work in physics had a great influence on Warburg's biochemical research"——influence 类型的出处 |
| Planck 名言 | "Science advances one funeral at a time" 系 Warburg 转述并归功 Max Planck——勿写成 Planck 原话考证或 Warburg 原创 |
| 领奖轶事 | 让大学把奖章邮寄给他以避开仪式、离开心爱的实验室——正文明载，可作结尾页点缀 |
| 死因与安葬 | 1968 股骨骨折并发深静脉血栓，1970-08-01 死于肺栓塞；葬柏林 Dahlem 墓园（基督教墓园） |
| metadata 噪声 | metadata.json 无母亲姓名（正文仅"巴登新教银行家家庭之女"）；父亲 Emil Warburg、双博士导师以 page.md 为准 |

---

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| respiratory enzyme | 呼吸酶 | 诺奖核心词，勿写成"呼吸酵素" |
| cellular respiration | 细胞呼吸 | 与"细胞呼吸作用"同义 |
| Warburg effect | 瓦博格效应 | 肿瘤细胞偏好糖酵解的现象 |
| Warburg hypothesis | 瓦博格假说 | 癌症线粒体功能障碍说，注意与现代突变说的主从关系 |
| oncometabolism | 肿瘤代谢 | infobox Known for |
| glycolysis | 糖酵解 | 假说中的无氧产能途径 |
| lactic acid | 乳酸 | 肿瘤大量产生 |
| nicotinamide | 烟酰胺 | 1944 提名理由之一 |
| flavin | 黄素 | 黄素酶（yellow enzymes） |
| quantum yield | 量子产额 | 与 Burk 的光合作用合作 |
| sea urchin | 海胆 | 那不勒斯实验材料 |
| Kaiser Wilhelm Institute | 威廉皇帝研究所 | 后易名马克斯·普朗克学会 |

---

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Awaken**（manifest 预分配）
- **匹配理由**：从海胆卵受精那一刻呼吸率六倍跃升，到把"呼吸酶"从黑箱里解出来——"唤醒"意象贴合受精/氧化的生命点火主题；音乐的开阔感匹配其跨越生化的宏大纲领（呼吸-发酵-光合）
- **本地路径**：`music_audio/alex-productions/36-aqLUvpAdLNQ-Awaken.wav`（以 curated_tracks.md 为准），复制到 `medic/presentations/20th_century/Otto_Heinrich_Warburg/Awaken.wav`
- **时长**：曲长须 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐

