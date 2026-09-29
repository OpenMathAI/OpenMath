# 医学家立传提示词（Michael W. Young）

> OpenMedic 项目 · 21 世纪诺贝尔生理学或医学奖 2017 年得主（三人共享之一） · 本文件是该人物的专属立传提示词，
> 按 9 节结构执行 Beamer 立传；数据库入库（fields/relations）已由批次完成，本文件第四/三节与 yaml 一致。

## 一、背景信息 【人物专属】

- **目标医学家**：Michael Warren Young（1949-03-28 生于迈阿密，在世）
- **气质关键词**：**timeless 与 doubletime 的发现者、从果蝇钟突变体到人类睡眠病的四十年摆渡人** —— 2017 年获奖理由（逐字引用 medic/nobel_medicine_citations.json，三人共享同一句）：
  > "for their discoveries of molecular mechanisms controlling the circadian rhythm"
  > （因他们发现了控制昼夜节律的分子机制）
- **设计母题**：**活动记录条带与光暗双柱（actogram）**。果蝇在监测仪里昼动夜息的条带图、突变体周期的拉伸与压缩——"把时间画成条纹"。
- **本地 Wikipedia 路径**：medic/presentations/pages/21th_century/Michael_W._Young/page.md
- **参考模板**：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）

## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章）

- 第 0/1/2/3 步按 **medic 路径**执行：事实基准 = `medic/presentations/pages/21th_century/Michael_W._Young/page.md`；目录 `medic/presentations/21th_century/Michael_W._Young/`；Makefile 改 `MAIN=Michael_W._Young_zh`；肖像优先 images.txt 所列 Commons 图（2017 诺奖发布会照），失败用装饰圆占位。
- 第 4/4.5 步（入库）**已完成**（第三、四节与 `MySQL/data/Michael_W._Young.yaml` 一致，勿重复入库）。
- 第 5-9 步：配色 → 幻灯片 → Beamer → 布局检查（0 error、vbox≤10pt、hbox≤50pt、逐页目检）→ 史实审查（第七节）。

## 三、研究领域梳理 + 入库（rank 0-4 表）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | chronobiology | 时间生物学 | 昼夜节律基因调控，诺奖核心 | 核心页 |
| 1 | genetics | 遗传学 | 果蝇钟基因正向遗传筛选 | 发现页 |
| 2 | molecular genetics | 分子遗传学 | 重组 DNA/转座子训练背景 | 求学页 |
| 3 | sleep medicine | 睡眠医学 | FASPS 家族性早睡综合征的基因基础 | 临床页 |

## 四、社会关系梳理 + 入库（与 yaml 完全一致，已完成）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Burke Judd | 师→本人 | UT Austin 博士导师（1975，果蝇基因组） |
| influence | Dave Hogness | 无向 | Stanford 博士后东家，习得重组 DNA 方法 |
| influence | Ron Konopka | 无向 | Konopka/Benzer 的果蝇钟突变体工作引其入行 |
| influence | Seymour Benzer | 无向 | Konopka/Benzer 的果蝇钟突变体工作引其入行 |
| advisor-student | Leslie B. Vosshall | 本人→学生 | infobox Doctoral students；1994 发现 PER 无 TIM 不能入核 |
| colleague | Amita Sehgal | 无向 | Young 实验室 timeless 筛选核心成员 |
| colleague | Jeff Price | 无向 | 实验室发现 doubletime 激酶（1998） |
| spouse | Laurel Eckhardt | 无向 | 研究生时相识，今 Hunter College 生物学教授 |
| co-honored | Michael Rosbash | 无向 | 2017 诺贝尔生理学或医学奖三人共享（昼夜节律分子机制） |
| co-honored | Jeffrey C. Hall | 无向 | 2017 诺贝尔生理学或医学奖三人共享（昼夜节律分子机制） |

> 对手方规范名：`Leslie B. Vosshall` 沿用库内既有记录（id=4839）；其余按 page.md 形式新建 stub；`Jeffrey C. Hall`/`Michael Rosbash` 与 Rosbash 篇同形式。

## 五、配色方案

- **气质**：德州少年的好奇 + 洛克菲勒实验室的精确 + 条带图的秩序美
- **主色**：果蝇绿 `#3E6B4F`（培养瓶与生命节律）
- **诺奖香槟金**：`#D4AF37`
- **badge 四分类色**：
  - `badgeA` timeless/doubletime — 时序蓝 `#2E6E9E`
  - `badgeB` per 功能解析 — 节律青 `#2E7D8C`
  - `badgeC` FASPS 睡眠病 — 病理橙 `#C97B2D`
  - `badgeD` 洛克菲勒建制 — 石墨灰蓝 `#3A4A6B`
- **背景母题**：低透明度活动记录条带（昼明夜暗的竖条纹）+ 正弦相位曲线。

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 昼夜节律分子机制的破译者 / Michael W. Young 1949– + 三人共享 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生年迈阿密、UT Austin 1971/1975、Stanford 博士后、洛克菲勒 1978 起、诺奖 2017）
03  核心贡献概览 — per 功能解析 / timeless / doubletime / FASPS 人类睡眠病
04  迈阿密与一本达尔文 (1949–1971) — 化工公司父亲与律所秘书母亲、私设动物园逃出的动物点燃好奇、达尔文著作中"昼闭夜开的怪花"埋下生物钟之问、L. D. Bell 高中
05  UT Austin 与 Burke Judd (1971–1975) — 果蝇基因组暑期研究→博士（多线染色体条带）；研究生时读到 Konopka/Benzer 的钟突变体工作
06  Stanford 博士后 (1975–1978) — Hogness 实验室、重组 DNA 与转座元件；与妻子 Laurel 同迁斯坦福
07  洛克菲勒建实验室 (1978–) — 助理教授 1978、副教授 1984、教授 1988、2004 学术副校长+Fisher 讲席
08  1980s：功能拯救 per — Bargiello/Jackson 合作，重组 DNA 片段注入 per 突变体、活动监测仪记录节律恢复；无义/长/短周期突变=蛋白失活或氨基酸改变
09  timeless 的发现 — Sehgal/Price/Man 正向遗传筛选（2 号染色体）、tim 与 per 强耦合；Vosshall 1994：PER 防降解仍需 TIM 才能入核；Saez：PER-TIM 互稳
10  doubletime 与磷酸化（核心页）— Price 1998 发现 doubletime（CK1）磷酸化 PER 标记降解；PER-TIM 结合时免于磷酸化——延时机制的分子解释
11  2001：从果蝇到人类 FASPS — hPer2 多态性缺失 CK1 磷酸化位点致家族性 advanced sleep phase syndrome；另型为 CK1 基因突变
12  2017 诺贝尔奖 — 与 Hall、Rosbash 共享；官方理由全句；2009 Gruber/2011 Horwitz/2012 Massry+Gairdner/2013 Shaw+Wiley 六奖预演
13  建制与家庭 — NAS 2007、美国哲学学会 2018、Pittendrigh/Aschoff 奖 2006；妻 Laurel Eckhardt（Hunter College 教授）两女 Natalie/Arissa
14  遗产：把果蝇的钟装进人类医学 — 睡眠相位障碍的基因诊断与时间治疗学
15  结尾（OpenMathAI 品牌口径）
```

## 七、特殊陷阱表（★ 核心）

| 陷阱 | 说明 |
|------|------|
| 共享结构 | 2017 三人共享同一句理由；Young 的独特贡献点=**timeless + doubletime**（以及 per 功能拯救实验）；勿与 Rosbash/Hall 的 TTFL 提出混写 |
| Konopka/Benzer | 二人发现 per 突变体在先，Young 受其启发入行——influence，勿写成 Young 发现 per 突变体本身 |
| 实验室群像 | timeless 筛选=Sehgal/Price/Man；per 拯救=Bargiello/Jackson；PER-TIM 入核=Vosshall/Saez；doubletime=Price——页面集体成果，主笔归 Young lab，具名贡献者仅入库 Vosshall（infobox 学生）+ Sehgal/Price（page.md 点名核心），其余在陷阱表说明不入库 |
| FASPS 年份 | 2001 年发现人类家族性早睡综合征（hPer2）；doubletime 突变 1998——两节点勿混 |
| 博士后 | Stanford 为博士后（Hogness），非博士；博士在 UT Austin（Judd） |
| 在世留白 | 在世者：无卒日；relations=10 已含两名 influence 与两名实验室同事，为 page.md 点名的诚实上限，勿再加边 |
| 妻子 | Laurel Eckhardt 系研究生时相识、同赴 Stanford（她随 Herzenberg 读博）——婚后各自发展，勿写成"合作者"关系 |
| 引语红线 | page.md 无整句直接引语——全部转述；达尔文书情节按页面转述 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| timeless (tim) | timeless 基因 | PER-TIM 二聚体入核 |
| doubletime (dbt) | doubletime 基因 | 即酪蛋白激酶 1（CK1） |
| FASPS | 家族性进展期睡眠相位综合征 | 2001 人类发现 |
| actogram | 活动记录图 | 果蝇昼夜活动条带 |
| locomotor monitor | 活动监测仪 | 行为表型定量 |
| recombinant DNA | 重组 DNA | Hogness 实验室训练 |
| forward genetics | 正向遗传学 | 突变筛选→克隆 |
| polytene chromosome | 多线染色体 | 博士论文对象 |

## 九、背景音乐选择

- **选定曲目**：**Shine Like The Sun** — Alex-Productions（manifest 预分配）
- **匹配理由**："如日生辉"贴合昼夜节律的太阳隐喻——光的明暗即钟的表盘；明快坚定的曲式匹配其"从果蝇突变体一路照亮人类睡眠医学"的摆渡者形象。
- **本地路径**：music_audio/ 下 Alex-Productions Shine Like The Sun 曲目（执行时按 curated_tracks.md 对应文件复制到本目录）。
