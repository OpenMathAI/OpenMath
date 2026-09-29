# 医学家立传提示词（Karl von Frisch）

> OpenMedic 项目 · 20 世纪诺贝尔生理学或医学奖 1973 年得主（三人共享之一） · 本文件是该人物的专属立传提示词，
> 按 9 节结构执行 Beamer 立传；数据库入库（fields/relations）已由批次完成，本文件第四/三节与 yaml 一致。

## 一、背景信息 【人物专属】

- **目标医学家**：Karl Ritter von Frisch（1886-11-20 生于维也纳 ~ 1982-06-12 逝于慕尼黑，享年 95 岁）
- **气质关键词**：**蜜蜂语言的翻译者、摇摆舞的解码人、在怀疑声中坚守六十年的感觉生理学家** —— 1973 年获奖理由（逐字引用 medic/nobel_medicine_citations.json，三人共享同一句）：
  > "for their discoveries concerning organization and elicitation of individual and social behaviour patterns"
  > （因他们关于个体与社会行为模式的组织与引发机制的发现）
- **设计母题**：**八字舞与太阳罗盘（waggle dance & sun compass）**。巢脾上的 8 字轨迹、偏振天光下的角度密码——"一秒钟一公里"的蜂群电报。
- **本地 Wikipedia 路径**：medic/presentations/pages/20th_century/Karl_von_Frisch/page.md
- **参考模板**：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）

## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章）

- 第 0/1/2/3 步按 **medic 路径**执行：事实基准 = `medic/presentations/pages/20th_century/Karl_von_Frisch/page.md`；目录 `medic/presentations/20th_century/Karl_von_Frisch/`；Makefile 改 `MAIN=Karl_von_Frisch_zh`；肖像优先 images.txt 所列 Commons 图（传统装束与蜜蜂合影），失败用装饰圆占位。
- 第 4/4.5 步（入库）**已完成**（第三、四节与 `MySQL/data/Karl_von_Frisch.yaml` 一致，勿重复入库）。
- 第 5-9 步：配色 → 幻灯片 → Beamer → 布局检查（0 error、vbox≤10pt、hbox≤50pt、逐页目检）→ 史实审查（第七节）。

## 三、研究领域梳理 + 入库（rank 0-4 表）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | ethology | 动物行为学 | 职业主领域（infobox Fields） | 封面 |
| 1 | sensory physiology | 感觉生理学 | 蜜蜂色觉/嗅觉/本体感觉 | 感觉页 |
| 2 | animal navigation | 动物导航 | 太阳罗盘/偏振光/地磁三罗盘 | 导航页 |
| 3 | chemical ecology | 化学生态学 | 蜂王信息素与巢群秩序 | 信息素页 |

## 四、社会关系梳理 + 入库（与 yaml 完全一致，已完成）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Hans Leo Przibram | 师→本人 | 维也纳大学博士导师（1910） |
| influence | Richard von Hertwig | 无向 | 慕尼黑阶段师从 |
| advisor-student | Ingeborg Beling | 本人→学生 | infobox Notable students 明载，延续蜜蜂研究 |
| advisor-student | Maximilian Renner | 本人→学生 | infobox Notable students 明载 |
| controversy | Carl von Hess | 无向 | 1913 抢发论文并质疑其色觉结论与专业性 |
| co-honored | Konrad Lorenz | 无向 | 1973 诺贝尔生理学或医学奖三人共享（行为模式） |
| co-honored | Nikolaas Tinbergen | 无向 | 1973 诺贝尔生理学或医学奖三人共享（行为模式） |
| parent-child | Anton von Frisch | 父→本人 | 父，外科与泌尿科医生 |
| spouse | Margarete Mohr | 无向 | 结婚，1964 先逝，子 Otto 任不伦瑞克自然史博物馆馆长 |

> 对手方规范名：均无库内记录按 page.md 形式新建 stub；`Konrad Lorenz`/`Nikolaas Tinbergen` 与本批两篇同形式镜像。

## 五、配色方案

- **气质**：维也纳旧都的优雅 + 六十年蜂场旁的耐心 + 95 岁的世纪长者
- **主色**：蜂蜡金 `#A67B1E`（巢脾、蜂蜜与金色阳光）
- **诺奖香槟金**：`#D4AF37`（双金呼应"太阳罗盘"）
- **badge 四分类色**：
  - `badgeA` 摇摆舞语言 — 舞蹈金橙 `#C97B2D`
  - `badgeB` 色觉与偏振罗盘 — 紫外紫 `#5E4B8B`
  - `badgeC` 三重导航罗盘 — 天空蓝 `#2E6E9E`
  - `badgeD` 信息素与社会秩序 — 巢脾棕 `#7A5230`
- **背景母题**：低透明度 8 字舞轨迹 + 放射状太阳角度刻度。

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 蜜蜂语言的翻译者 / Karl von Frisch 1886–1982 + badge + 右上头像 + 国籍行（Austria）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、维也纳、Przibram/Hertwig 师承、慕尼黑研究所所长、诺奖 1973）
03  核心贡献概览 — 蜜蜂色觉 / 三重导航罗盘 / 圆舞与摇摆舞 / 信息素
04  医生之家的幼子 (1886–1910) — 外科泌尿医生之父、四子皆成教授、部分犹太血统、维也纳 Przibram 门下博士 1910、慕尼黑 Hertwig 处进修
05  花香与花恒（早期感觉研究）— 蜜蜂凭气味辨花、"flower constant"、甜味觉仅略强于人类
06  蜜蜂看得见颜色（与 Hess 之争）— 条件反射训练实验证明色觉（光谱偏向紫外、红即黑）；Hess 1913 抢发论文并质疑其专业性——Fisch 指出其实验缺陷（客观呈现）
07  三重罗盘（核心页一）— 太阳主罗盘 + 偏振蓝天模式 + 地磁备份；内部时钟三套计时机制；巢脾磁性对齐与头部摆锤垂直感
08  圆舞与摇摆舞（核心页二）— 圆舞=近距食物无方向；摇摆舞=角度对垂直线=相对太阳方位、直线时长编码距离（约 1 秒 1 公里）；气味补充食源信息；绕山迂回仍可达
09  "方言"与听觉悬案 — 不同品种舞蹈要素有异；听觉未能确证、后由 Würzburg Tautz 证实振动感知
10  蜂王信息素 — 蜂王与工蜂信息素维系巢群复杂秩序、雄蜂婚飞
11  怀疑的六十年 — 1927《蜜蜂的生活》遭学界广泛质疑、数十年后才被公认准确——科学史上的坚守样本
12  1973 诺贝尔奖 — 与 Lorenz、Tinbergen 三人共享；官方理由全句；Balzan 1962 授奖词（"数以千计的蜜蜂实验"）可引
13  荣誉长廊 — Lieben 1921、Pour le Mérite 1952、Kalinga 1958、Balzan 1962、ForMemRS 1954、德国联邦大十字星绶 1974、巴伐利亚马克西米利安科学艺术勋章 1981；Karl Ritter von Frisch 奖章（德国动物学会最高奖）
14  家庭与身后 — 妻 Margarete（1964 先逝）、子 Otto 任不伦瑞克自然史博物馆馆长；1982-06-12 逝于慕尼黑
15  结尾（OpenMathAI 品牌口径）
```

## 七、特殊陷阱表（★ 核心）

| 陷阱 | 说明 |
|------|------|
| 共享结构 | 1973 三人共享同一句理由；分工：von Frisch=蜜蜂通讯与感觉、Lorenz=印记与本能理论、Tinbergen=实验验证与四问框架——勿混写 |
| 双师承 | 维也纳 Przibram（博士 1910，metadata 亦列）+ 慕尼黑 Hertwig（进修师从）——分别入库 advisor-student / influence，勿混 |
| 色觉优先权 | 蜜蜂色觉**首次证明者是 Charles Henry Turner**（page.md 明载 "first was Charles Henry Turner"），Frisch 系第二人——归属勿写反；Turner 不入库（无互动记载） |
| Hess 之争 | Hess 1913 抢发论文、质疑 Frisch 知识与专业操守、Frisch 指出其实验错误并要求停止——controversy 边与叙事均系 page.md 明载，客观呈现 |
| 纳粹时期 | 遭政权针对（雇犹太助手与女性职员）被迫退休、后因蜜蜂 nosema 研究恢复教职——**受迫害事实可客观一句**；其《Du und das Leben》初版曾支持绝育法一事系 page.md 有载但涉政治敏感，**立传省略不写** |
| 摇摆舞数字 | 直线段约 1 秒≈1 公里（速度与距离反比）；圆舞对应 50-100 米内——两组数字勿混 |
| 蜂种 | 研究对象系卡尼鄂拉蜂（Apis mellifera carnica）亚种——术语页给准 |
| 家族 | 四兄弟皆教授；父 Anton 系外科泌尿医生——parent-child 已入；部分犹太血统一句即可 |
| 引语红线 | 圆舞描述段（"perpetual comet's tail of bees"）有英文原文可引节选；Hess 之争与 Balzan 授奖词可引；其余转述 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| waggle dance | 摇摆舞 | 远距食物通讯 |
| round dance | 圆舞 | 近距食物通讯 |
| flower constancy | 花恒性 | 单花专注采蜜 |
| polarization pattern | 偏振光模式 | 蓝天罗盘 |
| ethology | 动物行为学 | 本届诺奖共同领域 |
| Apis mellifera carnica | 卡尼鄂拉蜂 | 研究蜂种 |
| pheromone | 信息素 | 蜂王物质 |
| nosema | 微孢子虫病（蜂） | 令其复职的研究 |
| Zeitgeber time | 授时时间 |（勿与 Pavlov 篇混——本篇用"太阳时角"表述）|

## 九、背景音乐选择

- **选定曲目**：**The Flow of Time** — Alex-Productions（manifest 预分配）
- **匹配理由**："时间之流"贴合其两大母题——蜜蜂的内部时钟与太阳时角、以及他横跨 1886-1982 的近一个世纪人生；流畅绵延的曲式如摇摆舞在巢脾上的时间编码。
- **本地路径**：music_audio/ 下 Alex-Productions The Flow of Time 曲目（执行时按 curated_tracks.md 对应文件复制到本目录）。
