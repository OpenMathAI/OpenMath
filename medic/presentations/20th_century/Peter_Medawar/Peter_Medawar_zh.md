# 医学家立传提示词（Peter Medawar）

> OpenMedic 项目 · 20 世纪诺贝尔生理学或医学奖 1960 年得主（与 Burnet 共享） · 本文件是该人物的专属立传提示词，
> 按 9 节结构执行 Beamer 立传；数据库入库（fields/relations）已由批次完成，本文件第四/三节与 yaml 一致。

## 一、背景信息 【人物专属】

- **目标医学家**：Sir Peter Brian Medawar（1915-02-28 生于巴西 Petrópolis ~ 1987-10-02 逝于伦敦，享年 72 岁）
- **气质关键词**：**"移植之父"、获得性免疫耐受的实验证明者、最机智的科学作家** —— 1960 年获奖理由（逐字引用 medic/nobel_medicine_citations.json，与 Burnet 共享同一句）：
  > "for discovery of acquired immunological tolerance"
  > （因发现获得性免疫耐受）
- **设计母题**：**接纳的皮肤（the accepted graft）**。皮肤移植片在异体宿主上成活、免疫系统放下武器的瞬间——"教会身体说不拒绝"。
- **本地 Wikipedia 路径**：medic/presentations/pages/20th_century/Peter_Medawar/page.md
- **参考模板**：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）

## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章）

- 第 0/1/2/3 步按 **medic 路径**执行：事实基准 = `medic/presentations/pages/20th_century/Peter_Medawar/page.md`；目录 `medic/presentations/20th_century/Peter_Medawar/`；Makefile 改 `MAIN=Peter_Medawar_zh`；肖像优先 images.txt 所列 Commons 图（Medawar in 1960、蓝牌等），失败用装饰圆占位。
- 第 4/4.5 步（入库）**已完成**（第三、四节与 `MySQL/data/Peter_Medawar.yaml` 一致，勿重复入库；库内既有 stub id=5868 已 UPD 回填）。
- 第 5-9 步：配色 → 幻灯片 → Beamer → 布局检查（0 error、vbox≤10pt、hbox≤50pt、逐页目检）→ 史实审查（第七节）。

## 三、研究领域梳理 + 入库（rank 0-4 表）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | immunology | 免疫学 | 免疫耐受与移植排斥 | 核心页 |
| 1 | zoology | 动物学 | 职业出身（Oxford 动物学） | 求学页 |
| 2 | organ transplantation | 器官移植 | 耐受发现的应用根基 | 诺奖页 |
| 3 | biology of ageing | 衰老生物学 | 1951 演化衰老理论 | 衰老页 |

## 四、社会关系梳理 + 入库（与 yaml 完全一致，已完成）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | John Zachary Young | 无向 | Oxford 动物学训练导师，共同研究神经再生 |
| influence | Ashley Gordon Lowndes | 无向 | Marlborough 生物学老师，点燃其科学热情 |
| advisor-student | Leslie Brent | 本人→学生 | 博士生，1953 耐受实验三人组之一 |
| advisor-student | Avrion Mitchison | 本人→学生 | infobox Doctoral students 明载 |
| advisor-student | Rupert E. Billingham | 本人→学生 | 博士后（infobox Other notable students），1953 三人组之一 |
| co-honored | Frank Macfarlane Burnet | 无向 | 1960 诺贝尔生理学或医学奖共享（获得性免疫耐受） |
| influence | Karl Popper | 无向 | 科学哲学上被视为 Popper 最知名的信徒 |
| spouse | Jean Medawar | 无向 | 1937 结婚（Oxford 研究生时相识），合著《Aristotle to Zoos》 |

> 对手方规范名：`Howard Florey` 沿用库内记录 id=5328——**Florey→Medawar advisor-student 边已由 Florey 批次入库（edge 11439），本篇不重复建**；`Frank Macfarlane Burnet` 与本批 Burnet 篇同形式镜像；其余按 page.md 形式新建 stub。

## 五、配色方案

- **气质**：黎巴嫩-巴西-英国的三重流浪 + 机锋百出的写作 + 移植医学的人道温度
- **主色**：移植紫红 `#6B4E7A`（新生皮肤与紫水晶般的智性）
- **诺奖香槟金**：`#D4AF37`
- **badge 四分类色**：
  - `badgeA` 免疫耐受/移植 — 移植红 `#A63A2B`
  - `badgeB` 动物学与神经再生 — 动物学青 `#2E7D8C`
  - `badgeC` 衰老的演化理论 — 衰老橙 `#C97B2D`
  - `badgeD` 科学写作与人文 — 人文紫 `#5E4B8B`
- **背景母题**：低透明度移植皮片几何拼图 + 一条逐渐淡出的排斥反应曲线。

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 移植之父 / Peter Medawar 1915–1987 + badge + 右上头像 + 国籍行（United Kingdom，生于巴西）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Petrópolis、Marlborough、Oxford Magdalen 动物学、Birmingham/UCL/NIMR、诺奖 1960）
03  核心贡献概览 — 获得性免疫耐受 / 移植排斥机制 / 衰老演化理论 / 科普写作
04  巴西出生的黎巴嫩之子 (1915–1928) — 黎巴嫩马龙派父亲（"在南美卖假牙"）与英国母亲、出生即登记英国籍、后放弃巴西籍免征兵；生地 Rio/Petrópolis 两说注记
05  Marlborough 与 Lowndes (1928–1932) — "从头到尾都不快乐"的公学（对解剖课的抱怨可引原文）+生物老师 Lowndes 点燃热情（"He fired me with enthusiasm"可引）
06  Oxford 师门 (1932–1941) — Magdalen 动物学一等荣誉、J. Z. Young 门下神经再生、Florey 的 Dunn School 监督并受其启发转向免疫学、博士论文 1941（付不起 25 镑未领学位的趣闻可引原话）
07  二战与皮肤移植起点 (1939–1947) — 烧伤士兵植皮研究、1941 Nature 纯表皮片论文、神经胶（nerve glue）发明
08  Birmingham 三人组 (1947–1951) — Mason 动物学教授、带博士生 Brent 与博士后 Billingham、1951 移植技术论文
09  1949-1956：证明 Burnet 假说（核心页）— Burnet 胚胎期耐受假说→胚胎细胞注入→成年后接受供者皮片；1953 Nature 简报→1956 Phil Trans 正式命名 actively acquired tolerance
10  1960 诺贝尔奖 — 与 Burnet 共享；官方理由全句；"移植之父"——直接奠基 Murray 1990 诺奖的肾移植
11  衰老与内分泌演化理论 — 1951《生物学一个未解问题》：自然选择随年龄减弱；内分泌演化格言（可引英文原句）
12  NIMR 所长与科学写作 — 1962 接任 Mill Hill（"滑进劳斯莱斯驾驶座"可引）、1969 卒中致残仍坚持写作、Dawkins/Gould 的评价可引；Reith 讲座 1959
13  荣誉矩阵 — FRS 1949、Royal Medal 1959、Copley 1969、OM 1981、Kalinga 1985、Faraday 1987；1970 皇家学会会长因卒中未就任
14  家庭与身后 — 妻 Jean（1937 结婚，合著《Aristotle to Zoos》，岳家反对的婚事）；两子两女（外孙 Alex Garland）；1987-10-02 逝于伦敦；2024 诺奖章捐牛津
15  结尾（OpenMathAI 品牌口径）
```

## 七、特殊陷阱表（★ 核心）

| 陷阱 | 说明 |
|------|------|
| 共享结构 | 1960 两人共享同一句理由；分工：Burnet=假说预言、Medawar=实验证明（1953 三人组）——本篇以实验线为主叙事 |
| Florey 边 | 库内已有 Florey 批次写的 Florey→Medawar advisor-student 边（11439）；本篇 page.md 口径为"supervised + inspired"——**不重复建边**，正文可写"受 Florey 监督与启发" |
| 生地两说 | Rio de Janeiro 与 Petrópolis 两说并存——**以 infobox/正文首选 Petrópolis 为准**，陷阱表注记 |
| PhD 趣闻 | 1941 论文通过但因付不起 25 镑未领学位（1947 才获 DSc）——"Morally I'm a PhD"原话可引；勿写成"1941 获 PhD" |
| 1970 皇家学会会长 | 当选 1970-1975 任期但 1969 卒中未就任——"当选"与"就任"勿混 |
| Marlborough 比喻 | 其将公学比作纳粹党卫队训练校系激烈言辞——page.md 有载，立传建议省略或中性化，禁渲染 |
| 政治敏感 | 无；宗教观（理性主义/不可知论）有大量英文原文，可节选一句客观呈现 |
| 移民细节 | 离巴西赴英时间有三说（1918/1928-29/1929-30）——页面已并列，行文用"一战末随家人返英"模糊化或注记 |
| 引语红线 | 富含原话（Lowndes/PhD 趣闻/单调 Endocrine 格言/Dawkins"Gould 评语等），引原文+译文；其余转述 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| acquired/actively acquired tolerance | 获得性免疫耐受 | 1956 正式命名 |
| graft rejection | 移植排斥 | 二战烧伤植皮起点 |
| skin grafting | 皮肤移植 | 临床起点 |
| senescence | 衰老 | 与 ageing 区分（其 1951 定义） |
| reproductive value | 繁殖价值 | 衰老演化理论概念 |
| viviparity | 胎生 | 内分泌演化演讲主题 |
| nerve glue | 神经胶 | 二战手术发明 |
| Kalinga Prize | 卡林加科普奖 | 1985 UNESCO |

## 九、背景音乐选择

- **选定曲目**：**New Lands** — Alex-Productions（manifest 预分配）
- **匹配理由**："新大陆"贴合其"让身体接受新器官"的开拓——耐受的发现为器官移植这片医学新大陆奠基；三重文化出身的漂泊者最终在新科学大陆登陆，曲意相合。
- **本地路径**：music_audio/ 下 Alex-Productions New Lands 曲目（执行时按 curated_tracks.md 对应文件复制到本目录）。
