# 医学家立传提示词（Rita Levi-Montalcini）

> OpenMedic 项目 · 20 世纪诺贝尔生理学或医学奖 1986 年得主（与 Cohen 共享） · 本文件是该人物的专属立传提示词，
> 按 9 节结构执行 Beamer 立传；数据库入库（fields/relations）已由批次完成，本文件第四/三节与 yaml 一致。

## 一、背景信息 【人物专属】

- **目标医学家**：Rita Levi-Montalcini（1909-04-22 生于都灵 ~ 2012-12-30 逝于罗马，享年 103 岁）
- **气质关键词**：**种族法下卧室实验室的坚守者、神经生长因子的发现者、世纪长者与终身参议员** —— 1986 年获奖理由（逐字引用 medic/nobel_medicine_citations.json，与 Cohen 共享同一句）：
  > "for their discoveries of growth factors"
  > （因他们关于生长因子的发现）
- **设计母题**：**石床上溪流（rivulets over stones）**。肿瘤周围神经纤维如水过卵石般生长的光环——她在自传里写下的比喻，也是她一生的隐喻。
- **本地 Wikipedia 路径**：medic/presentations/pages/20th_century/Rita_Levi-Montalcini/page.md
- **参考模板**：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）

## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章）

- 第 0/1/2/3 步按 **medic 路径**执行：事实基准 = `medic/presentations/pages/20th_century/Rita_Levi-Montalcini/page.md`；目录 `medic/presentations/20th_century/Rita_Levi-Montalcini/`；Makefile 改 `MAIN=Rita_Levi-Montalcini_zh`；肖像优先 images.txt 所列 Commons 图（1986 Lund 照、2009 照），失败用装饰圆占位。
- 第 4/4.5 步（入库）**已完成**（第三、四节与 `MySQL/data/Rita_Levi-Montalcini.yaml` 一致，勿重复入库；库内裸 stub id=6125 已 UPD 回填）。
- 第 5-9 步：配色 → 幻灯片 → Beamer → 布局检查（0 error、vbox≤10pt、hbox≤50pt、逐页目检）→ 史实审查（第七节）。

## 三、研究领域梳理 + 入库（rank 0-4 表）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | neurobiology | 神经生物学 | 职业主领域（infobox Fields） | 封面 |
| 1 | growth factor biology | 生长因子生物学 | NGF 发现，诺奖核心 | 核心页 |
| 2 | embryology | 胚胎学 | 鸡胚神经纤维生长研究 | 早年页 |
| 3 | endocannabinoid research | 内源性大麻素研究 | 棕榈酰胺乙醇胺（PEA）调节肥大细胞 | 晚年页 |

## 四、社会关系梳理 + 入库（与 yaml 完全一致，已完成）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | Giuseppe Levi | 无向 | 都灵神经组织学家，点燃其神经系统发育兴趣（库内既有记录 id=6124 复用） |
| influence | Viktor Hamburger | 无向 | 圣路易斯华盛顿大学实验室东家（1946 一学期访问改 30 年任职） |
| collaborator | Hertha Meyer | 无向 | 1952 里约联邦大学关键实验合作者（1954 发表首份确证） |
| colleague | Stanley Cohen (biochemist) | 无向 | WashU 合作分离 NGF |
| co-honored | Stanley Cohen (biochemist) | 无向 | 1986 诺贝尔生理学或医学奖共享（生长因子） |

> 对手方规范名：`Giuseppe Levi` 沿用库内 id=6124；`Stanley Cohen (biochemist)` 与本批 Cohen 篇同键（含消歧后缀，manifest 逐字一致）；`Viktor Hamburger`/`Hertha Meyer` 新建。**在世关系裁剪**：终身未婚未育（page.md 明载，2006 访谈原话可引）；兄妹 Paola（艺术家）/Gino（建筑师）不入库。**relations=5 为诚实值**。Dulbecco/Luria 的 colleague 边系 Dulbecco 批次既有（同门友），本篇不重复。

## 五、配色方案

- **气质**：都灵犹太世家的韧性 + 种族法阴影下的卧室实验室 + 103 年的世纪见证
- **主色**：都灵深红 `#7A1E3C`（石榴与家族纹章）
- **诺奖香槟金**：`#D4AF37`
- **badge 四分类色**：
  - `badgeA` NGF 发现 — 神经金橙 `#C97B2D`
  - `badgeB` 卧室实验室岁月 — 烛光紫 `#5E4B8B`
  - `badgeC` 双城双实验室（圣路易斯×罗马） — 双城蓝 `#2E6E9E`
  - `badgeD` 终身参议员与公益 — 公职青 `#2E7D8C`
- **背景母题**：低透明度神经纤维光环（卵石上溪流）+ 鸡胚轮廓。

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 神经生长因子的发现者 / Rita Levi-Montalcini 1909–2012 + badge + 右上头像 + 国籍行（Italy，后入美国籍）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、都灵、都灵大学 MD 1936 summa cum laude、WashU 30 年、诺奖 1986、终身参议员 2001）
03  核心贡献概览 — NGF 发现 / 鸡胚神经死亡与靶标 / 双实验室建制 / PEA 与肥大细胞
04  都灵四兄妹 (1909–1936) — 犹太世家（母画家父工程师）、孪生妹妹 Paola、父亲起初反对女儿上大学、挚友死于胃癌立志学医、Giuseppe Levi 门下 summa cum laude MD 1936
05  1938：种族法斩断学术路 — 墨索里尼《种族宣言》剥夺犹太人教职、助手职务终止
06  卧室实验室 (1940–1943) — 都灵家中卧室搭实验台研究鸡胚神经纤维生长：神经细胞缺乏靶标即死亡——日后全部研究的基石
07  流亡与救护 (1943–1945) — 德占后全家南逃佛罗伦萨、假身份幸存于大屠杀、与行动党游击队联系、光复后志愿盟军医护
08  Hamburger 实验室 (1946–) — 一学期 fellowship 因复现自家结果改 30 年 research associate； tumor 移植鸡胚：神经如"石床上溪流"疯长（原文可引）——肿瘤释放促生长物质假说
09  1952 里约关键实验与 NGF 分离（核心页一）— 与 Hertha Meyer 合作（1954 发表首份确证）；Cohen 以生化手段携手分离 NGF
10  Cohen 与 EGF（对照注记）— Cohen 从 NGF 实验对照发现 EGF（本篇一句带过，详见其传）
11  1986 诺贝尔奖 — 与 Cohen 共享；官方理由全句；Horwitz 1983/Gerard 1985/Lasker 1986/国家科学奖章 1987；首位百岁诺奖得主（2009 罗马市政厅庆生）
12  双城双实验室 — 1962 罗马建第二实验室、1961-78 领导 CNR 神经生物学研究中心与细胞生物学实验室、2002 创立欧洲脑研究所（EBRI）任主席
13  争议与担当（客观一页）— Fidia 药企合作与 Cronassial 风波（调查揭示公司行贿、她受公开批评——page.md 明载客观一句）；EBRI 管理受部分学界批评；1993 PEA/肥大细胞研究开新篇
14  终身参议员与身后 — 2001 Ciampi 总统任命终身参议员；百岁参政；2012-12-30 逝于罗马寓所；Rita Levi-Montalcini 基金会资助非洲与意大利女童教育；Google Doodle 纪念
15  结尾（OpenMathAI 品牌口径）
```

## 七、特殊陷阱表（★ 核心）

| 陷阱 | 说明 |
|------|------|
| 共享结构 | 1986 两人共享同一句理由；分工：Levi-Montalcini=生物学现象与假说（肿瘤促神经生长）、Cohen=化学分离与 EGF——互补勿混写 |
| Giuseppe Levi | 影响其志向的神经组织学家、MD 后任其助手——influence（无博士导师明文）；库内 id=6124 复用 |
| 政治争议（克制）| 2006 参议院表态遭右翼议员嘲弄、Grillo 诽谤诉讼、意大利共济会往来——涉政党政治/私域争议，**立传一律不展开**；共济会段仅陷阱表留存 |
| Fidia/Cronassial | 系科学伦理争议（药企合作、药品不良反应、公司行贿调查牵出其关系）——page.md 明载，客观一句放"争议与担当"页，勿渲染成丑闻主角 |
| EBRI 批评 | 2010 部分学界对其研究所管理批评——一句客观 |
| 国籍 | metadata 三值 [US, Kingdom of Italy, Italy]——yaml 按 Italy(0)+United States(1)（citizenship Italy/US，出生王国意大利作历史背景不入国籍行） |
| 终身未婚 | "never married, no children"+2006 原话（"My life has been enriched by excellent human relations..."）——如实呈现，可引原文 |
| 2009 百岁 | 首位活到 100 岁的诺奖得主——诺奖史注记亮点 |
| 引语红线 | 可引：石床溪流比喻、2006 不婚访谈、Alemanno/Hack/Monti 悼词节选；其余转述 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| nerve growth factor (NGF) | 神经生长因子 | 1986 诺奖核心 |
| Manifesto of Race | （意）《种族宣言》 | 1938 种族法背景（客观一句） |
| chicken embryo | 鸡胚 | 卧室实验室研究对象 |
| sarcoma 180/37 | 小鼠肉瘤 180/37 | 1954 奠基论文对象 |
| gangliosides | 神经节苷脂 | Fidia 时期研究 |
| palmitoylethanolamide (PEA) | 棕榈酰胺乙醇胺 | 1993 内源性调节物 |
| mast cell | 肥大细胞 | 晚年研究焦点 |
| senator for life | 终身参议员 | 2001 意大利 |

## 九、背景音乐选择

- **选定曲目**：**Ascension** — Alex-Productions（manifest 预分配）
- **匹配理由**："攀升/升华"贴合其从种族法下的卧室实验台一路攀升到斯德哥尔摩与终身参议员席位的百年弧线——层层登高、百岁不息；推进感曲式承载 103 年的坚韧。
- **本地路径**：music_audio/ 下 Alex-Productions Ascension 曲目（执行时按 curated_tracks.md 对应文件复制到本目录）。
