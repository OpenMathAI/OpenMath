# 医学家立传提示词（Joseph L. Goldstein）

> OpenMedic 项目 · 20 世纪诺贝尔生理学或医学奖 1985 年得主（与 Brown 共享） · 本文件是该人物的专属立传提示词，
> 按 9 节结构执行 Beamer 立传；数据库入库（fields/relations）已由批次完成，本文件第四/三节与 yaml 一致。

## 一、背景信息 【人物专属】

- **目标医学家**：Joseph Leonard Goldstein（1940-04-18 生于南卡罗来纳州 Kingstree，在世）
- **气质关键词**：**LDL 受体的共同发现者、胆固醇代谢调控的破译者、他汀时代的科学奠基人** —— 1985 年获奖理由（逐字引用 medic/nobel_medicine_citations.json，与 Brown 共享同一句）：
  > "for their discoveries concerning the regulation of cholesterol metabolism"
  > （因他们关于胆固醇代谢调控的发现）
- **设计母题**：**受体循环（the receptor cycle）**。LDL 颗粒被受体捕获入胞、网格蛋白小窝的内吞视图——"给血液里的胆固醇装上门铃"。
- **本地 Wikipedia 路径**：medic/presentations/pages/20th_century/Joseph_L._Goldstein/page.md
- **参考模板**：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）

## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章）

- 第 0/1/2/3 步按 **medic 路径**执行：事实基准 = `medic/presentations/pages/20th_century/Joseph_L._Goldstein/page.md`；目录 `medic/presentations/20th_century/Joseph_L._Goldstein/`；Makefile 改 `MAIN=Joseph_L._Goldstein_zh`；肖像优先 images.txt 所列 Commons 图，失败用装饰圆占位。
- 第 4/4.5 步（入库）**已完成**（第三、四节与 `MySQL/data/Joseph_L._Goldstein.yaml` 一致，勿重复入库；库内裸 stub id=5736 已 UPD 回填）。
- 第 5-9 步：配色 → 幻灯片 → Beamer → 布局检查（0 error、vbox≤10pt、hbox≤50pt、逐页目检）→ 史实审查（第七节）。

## 三、研究领域梳理 + 入库（rank 0-4 表）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biochemistry | 生物化学 | 职业主领域（infobox Fields） | 封面 |
| 1 | genetics | 遗传学 | 家族性高胆固醇血症的遗传分析 | 研究页 |
| 2 | lipid metabolism | 脂质代谢 | 胆固醇调控与 SREBP 通路 | 诺奖页 |
| 3 | cardiovascular medicine | 心血管医学 | 他汀药物的科学基础 | 遗产页 |

## 四、社会关系梳理 + 入库（与 yaml 完全一致，已完成）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Michael Stuart Brown | 无向 | UT Southwestern 长期合作者，1973-1985 合发逾百篇论文 |
| co-honored | Michael Stuart Brown | 无向 | 1985 诺贝尔生理学或医学奖共享（胆固醇代谢调控） |
| advisor-student | Thomas C. Südhof | 本人→学生 | 前博士后，2013 诺贝尔生理学或医学奖得主（库内既有边幂等合并） |
| advisor-student | Xiaodong Wang | 本人→学生 | 前博士后，1993 与 Briggs 共同纯化 SREBP |
| advisor-student | Helen H. Hobbs | 本人→学生 | 前博士后，2015 生命科学突破奖得主 |

> 对手方规范名：`Michael Stuart Brown` 沿用库内裸 stub id=5735（Südhof 批次所建，UPD 由其本批处理）；`Thomas C. Südhof` 沿用 id=5458（Südhof 批次已写 Goldstein→Südhof advisor-student 边 11258，本篇幂等合并）；`Xiaodong Wang`/`Helen H. Hobbs` 新建。**citation json 名形式 Michael S. Brown 不得直接作对手方键**（batch-22 教训）。**relations=5 为在世诚实值**：Russell/Krieger/DeBose-Boyd 等 NAS 博士后仅列表提及不入库（陷阱表留痕）。

## 五、配色方案

- **气质**：南卡小镇服装店之子的踏实 + 达拉斯双星三十年的并肩 + 艺术与科学的跨界随笔
- **主色**：胆固醇深青 `#0F5257`（血脂与显微镜的冷色）
- **诺奖香槟金**：`#D4AF37`
- **badge 四分类色**：
  - `badgeA` LDL 受体 — 受体蓝 `#2E6E9E`
  - `badgeB` 家族性高胆固醇血症 — 遗传紫 `#5E4B8B`
  - `badgeC` SREBP 转录因子机器 — 转录橙 `#C97B2D`
  - `badgeD` 艺术与科学随笔 — 人文金 `#C9A227`
- **背景母题**：低透明度 Y 形受体捕获 LDL 颗粒的内吞循环。

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 胆固醇代谢调控的共同破译者 / Joseph L. Goldstein 1940– + badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生年 Kingstree、Washington & Lee 1962、UT Southwestern MD 1966、NIH、1972 回达拉斯、诺奖 1985）
03  核心贡献概览 — LDL 受体 / 家族性高胆固醇血症 / 受体介导内吞 / SREBP 机器
04  服装店之家 (1940–1962) — 犹太家庭、父亲 Isadore 经营服装店、Washington and Lee 学士 1962
05  医学与 NIH (1962–1972) — UT Southwestern MD 1966、住院医后赴 NIH 从事生化遗传学
06  回达拉斯与 Brown 相遇 (1972–1973) — 出任医学遗传学部主任；与同出 NIH 的 Brown 展开长达三十余年的双人组
07  1973-1974：家族性高胆固醇血症 — FH 纯合子细胞实验：HMG-CoA 还原酶调控缺陷、LDL 结合缺陷——遗传学切入代谢的典范
08  LDL 受体与受体介导内吞（核心页）— 细胞经 LDL 受体清除血胆固醇；受体不足→高胆固醇血症→冠心病；1986 Science 里程碑综述
09  1985 诺贝尔奖 — 与 Brown 共享；官方理由全句；Lasker 1985/William Allan 1985/Horwitz 1984/Gairdner 1981 预演；他汀药物的科学基础（Endo 的"胆固醇青霉素"致敬注记）
10  1988 之后：SREBP 机器 — 1993 博士后 Wang/Briggs 纯化 SREBP 膜结合转录因子家族；蛋白酶水解释放入核的复杂机器与负反馈
11  桃李满门 — 与 Brown 合训 145+ 研究生与博士后；六人入选 NAS；Südhof 2013 诺奖、Hobbs 2015 突破奖
12  荣誉长廊 — 国家科学奖章 1988、ForMemRS 1991、Kober 奖章 2002、Alpert 奖 1999、Albany 奖 2003、Stadtman 奖 2011
13  建制与随笔 — HHMI/洛克菲勒董事、Broad 顾问委员会主席、Regeneron 董事；Lasker 评审团主席 1995 起；2000 起《Nature Medicine》"科学与艺术"系列随笔（The Art of Science 2023 结集）
14  在世的坚守 — 多次被提名国家科学管理要职仍坚持一线研究（与 Brown 同）；现居达拉斯继续执教
15  结尾（OpenMathAI 品牌口径）
```

## 七、特殊陷阱表（★ 核心）

| 陷阱 | 说明 |
|------|------|
| 共享结构 | 1985 两人共享同一句理由；Brown/Goldstein 双人组无明确分工（合作体）——叙事以"双人组"呈现，勿虚构各自主导项 |
| Brown 规范名 | 库内规范名 **Michael Stuart Brown**(5735)——citation json 作 Michael S. Brown，勿以其作对手方键（batch-22 教训） |
| 无博士导师 | page.md 无具名博士导师（MD 临床学位）——不建 advisor 边；NIH 期从事生化遗传学但无具名导师 |
| Südhof 边 | 库内已有 Südhof 批次写的 Goldstein→Südhof advisor-student 边（11258，note「UT Southwestern 博士后导师」）——本篇幂等合并不重复 |
| 博士后群像 | 六位 NAS 博士后仅入库 Südhof/Wang/Hobbs 三位（page.md 给出具体成就者）；Russell/Krieger/DeBose-Boyd 列表性提及不入库；Michael Briggs（与 Wang 共同纯化 SREBP）不入库、正文一句 |
| SREBP 归属 | SREBP 纯化系博士后 Wang/Briggs 完成（1993），机器描述系 Goldstein/Brown 团队集体——归属勿全归 Goldstein |
| 在世者 | 在世：无卒日；无配偶记载（page.md 无家庭婚姻信息，家庭页从略勿虚构）；relations=5 诚实值 |
| 艺术随笔 | 《The Art of Science》系列系 page.md 明载特色（马格利特/修拉/培根等）——可作 badgeD 一页亮点 |
| 引语红线 | page.md 无整句直接引语——全部转述 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| LDL receptor | 低密度脂蛋白受体 | 诺奖核心发现 |
| familial hypercholesterolemia | 家族性高胆固醇血症 | 遗传切入点 |
| HMG-CoA reductase | HMG-CoA 还原酶 | 胆固醇合成限速酶 |
| receptor-mediated endocytosis | 受体介导的内吞 | 受体循环机制 |
| SREBP | 固醇调节元件结合蛋白 | 1993 后期主线 |
| statin | 他汀类药物 | 诺奖工作的临床果实 |
| proteolytic release | 蛋白水解释放 | SREBP 激活机制 |
| negative feedback | 负反馈 | 胆固醇稳态核心 |

## 九、背景音乐选择

- **选定曲目**：**The Invisible Light** — Alex-Productions（manifest 预分配）
- **匹配理由**："不可见之光"贴合 LDL 受体——肉眼不可见的分子机器，却是心血管医学四十年革命的源头；沉静中带推进的曲式匹配达拉斯双人组数十年如一日的长跑。
- **本地路径**：music_audio/ 下 Alex-Productions The Invisible Light 曲目（执行时按 curated_tracks.md 对应文件复制到本目录）。
