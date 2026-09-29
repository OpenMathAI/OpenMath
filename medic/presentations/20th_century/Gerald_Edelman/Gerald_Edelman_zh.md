# 医学家立传提示词（Gerald Edelman）

> OpenMedic 项目 · 20 世纪诺贝尔生理学或医学奖 1972 年得主（与 Porter 共享） · 本文件是该人物的专属立传提示词，
> 按 9 节结构执行 Beamer 立传；数据库入库（fields/relations）已由批次完成，本文件第四/三节与 yaml 一致。

## 一、背景信息 【人物专属】

- **目标医学家**：Gerald Maurice Edelman（1929-07-01 生于纽约 ~ 2014-05-17 逝于加州 La Jolla，享年 84 岁）
- **气质关键词**：**抗体分子结构的破译者、神经达尔文主义的创立者、从免疫学到意识的跨越者** —— 1972 年获奖理由（逐字引用 medic/nobel_medicine_citations.json，与 Porter 共享同一句）：
  > "for their discoveries concerning the chemical structure of antibodies"
  > （因他们关于抗体化学结构的发现）
- **设计母题**：**选择的同构（selection across scales）**。抗体 Y 形分子、神经元群的竞争修剪——"免疫系统与大脑都在做达尔文式选择"。
- **本地 Wikipedia 路径**：medic/presentations/pages/20th_century/Gerald_Edelman/page.md
- **参考模板**：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）

## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章）

- 第 0/1/2/3 步按 **medic 路径**执行：事实基准 = `medic/presentations/pages/20th_century/Gerald_Edelman/page.md`；目录 `medic/presentations/20th_century/Gerald_Edelman/`；Makefile 改 `MAIN=Gerald_Edelman_zh`；肖像优先 images.txt 所列 Commons 图（Edelman in 2010），失败用装饰圆占位。
- 第 4/4.5 步（入库）**已完成**（第三、四节与 `MySQL/data/Gerald_Edelman.yaml` 一致，勿重复入库）。
- 第 5-9 步：配色 → 幻灯片 → Beamer → 布局检查（0 error、vbox≤10pt、hbox≤50pt、逐页目检）→ 史实审查（第七节）。

## 三、研究领域梳理 + 入库（rank 0-4 表）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | immunology | 免疫学 | 抗体结构，诺奖核心 | 诺奖页 |
| 1 | neuroscience | 神经科学 | 神经群选择理论 | 意识页 |
| 2 | philosophy of mind | 心灵哲学 | 意识的生物学理论 | 理论页 |
| 3 | developmental biology | 发育生物学 | CAM 细胞黏附分子与 Topobiology | 后期页 |

## 四、社会关系梳理 + 入库（与 yaml 完全一致，已完成）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | Henry Kunkel | 无向 | Rockefeller 博士阶段实验室主持人（1960 博士） |
| co-honored | Rodney Robert Porter | 无向 | 1972 诺贝尔生理学或医学奖共享（抗体化学结构） |
| collaborator | Giulio Tononi | 无向 | 《A Universe of Consciousness》合著者 |
| advisor-student | Paul David Gottlieb | 本人→学生 | infobox Doctoral students 明载 |
| advisor-student | Olaf Sporns | 本人→学生 | infobox Doctoral students 明载 |
| spouse | Maxine M. Morrison | 无向 | 1950 结婚，二子一女 |

> 对手方规范名：均无库内记录按 page.md 形式新建 stub；`Rodney Robert Porter` 与本批 Porter 篇同形式镜像。**metadata 的 doctoral_advisor 列 Frederick Sanger，但 page.md 全文无 Sanger 记载——裁定不入库**（其博士阶段实验室主持人是 Kunkel）；Porter 批次另行处理 Sanger 边（Porter 页明载 Sanger 系其博士导师）。

## 五、配色方案

- **气质**：皇后区少年提琴手的转向 + 洛克菲勒的精密 + 圣地亚哥的思辨狂想
- **主色**：抗体蓝 `#1E5A8A`（IgG 分子图的经典蓝）
- **诺奖香槟金**：`#D4AF37`
- **badge 四分类色**：
  - `badgeA` 抗体结构 — 免疫金 `#C9A227`
  - `badgeB` 神经达尔文主义 — 选择绿 `#3E6B4F`
  - `badgeC` 意识理论 — 意识紫 `#5E4B8B`
  - `badgeD` CAM 与 Topobiology — 形态青 `#2E7D8C`
- **背景母题**：低透明度 Y 形抗体 + 神经元群竞争的扇形修剪。

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 抗体结构之谜的破译者 / Gerald Edelman 1929–2014 + badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Ozone Park、Ursinus 1950、宾大 MD 1954、洛克菲勒 PhD 1960、Scripps 1992 起、诺奖 1972）
03  核心贡献概览 — 抗体结构 / 抗体测序 / CAM 细胞黏附分子 / 神经达尔文主义
04  小提琴手的转身 (1929–1954) — 犹太医师之家、多年小提琴训练自认"缺乏内在驱动力"转向医学研究、Ursinus magna cum laude、宾大 MD 1954
05  巴黎的抗体之书 (1955–1957) — 驻法军医时读一本少谈抗体的书立志研究、Mass General 住院医、1957 入洛克菲勒 Kunkel 实验室
06  1960：二硫键与轻重链 — 抗体由二硫键连接的重链/轻链构成（2+2）；Fab 抗原结合域由两链共同贡献
07  抗体测序（核心页）— 溴化氰+蛋白酶片段化测序；1969 首个完整抗体序列=当时最长的完整蛋白序列；恒定区/可变区的发现
08  Porter 的平行线与 1972 诺奖 — Porter=木瓜蛋白酶切分抗体（Fab/Fc）、Edelman=还原断链；两人路径互补；Karolinska 新闻稿评价（英文原文可引节选）
09  诺奖之后：CAM 的发现 — 细胞黏附分子引导胚胎发育与神经系统构建；神经 CAM 前基因演化出整个适应性免疫系统
10  Topobiology (1988) — 形态发生由异质细胞群的差异黏附驱动
11  神经达尔文主义（核心页二）— 三支柱：发育选择/经验选择/再入（reentry）；指纹式突触多样性；"宇宙中再无他物如此被再入回路标记"（可引）
12  意识的生物学理论 — 拒绝二元论与计算主义；意识定义（Second Nature 原文可引节选）；与 Tononi 合著 A Universe of Consciousness
13  神经科学研究所 (1993–2012) — 圣地亚哥非营利研究中心创始人兼所长
14  家庭与身后 — 妻 Maxine（1950 起，子 Eric 视觉艺术家/David 神经科学教授、女 Judith 蓝草音乐家）；前列腺癌+帕金森；2014-05-17 逝于 La Jolla
15  结尾（OpenMathAI 品牌口径）
```

## 七、特殊陷阱表（★ 核心）

| 陷阱 | 说明 |
|------|------|
| 共享结构 | 1972 两人共享同一句理由；分工：Edelman=化学断链与完整测序、Porter=酶切分段——路径互补勿混写 |
| Sanger 裁定 | metadata doctoral_advisor 列 Frederick Sanger，但 **page.md 全文无载**——不入库；其博士阶段实验室主持人是 Henry Kunkel（influence）；勿写成"Sanger 门下" |
| 抗体测序年份 | 1969 首个完整抗体序列，且是当时最长完整蛋白序列——勿与诺奖 1972 混淆 |
| Porter 分工 | Porter 用木瓜蛋白酶把免疫球蛋白切成片段便于研究——写 Porter 篇主线，本篇仅对照 |
| CAM/免疫系统演化 | "神经 CAM 前基因演化出适应性免疫系统分子系统"系其研究结论，页面以研究叙事呈现——勿拔高为定律 |
| 意识理论定位 | Neural Darwinism 是其个人理论体系（有争议），行文用"他提出/他主张"，勿写成学界共识；拒绝计算主义系其立场 |
| 引言红线 | Karolinska 新闻稿、Second Nature 意识定义、reentry 两句均有英文原文可引节选；其余转述 |
| 家庭 | 三子女职业各异（艺术家/神经科学教授/蓝草音乐家）可一句；Richard Powers 小说影射系评论者说法，可省 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| disulfide bond | 二硫键 | 连接轻重链 |
| heavy / light chain | 重链/轻链 | 抗体亚基 |
| Fab / variable region | 抗原结合片段/可变区 | 多样性来源 |
| cyanogen bromide | 溴化氰 | 测序片段化试剂 |
| cell adhesion molecule (CAM) | 细胞黏附分子 | 后期核心发现 |
| neural group selection | 神经群选择 | 即 Neural Darwinism |
| reentry | 再入信号 | 脑区图间递归交互 |
| degeneracy | 简并性 | 与 Gally 首次系统指出 |
| topobiology | 拓扑生物学 | 1988 形态发生理论 |

## 九、背景音乐选择

- **选定曲目**：**SEA** — Alex-Productions（manifest 预分配）
- **匹配理由**："海洋/深广"贴合其思想版图的两次下潜——从抗体分子的深海到意识的海面之光；La Jolla 海边的晚年与"Bright Air, Brilliant Fire"的书名意象相映。
- **本地路径**：music_audio/ 下 Alex-Productions SEA 曲目（执行时按 curated_tracks.md 对应文件复制到本目录）。
