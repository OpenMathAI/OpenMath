# 医学家立传提示词（Stanley Cohen）

> OpenMedic 项目 · 20 世纪诺贝尔生理学或医学奖 1986 年得主（与 Levi-Montalcini 共享） · 本文件是该人物的专属立传提示词，
> 按 9 节结构执行 Beamer 立传；数据库入库（fields/relations）已由批次完成，本文件第四/三节与 yaml 一致。

## 一、背景信息 【人物专属】

- **目标医学家**：Stanley Cohen（1922-11-17 生于布鲁克林 ~ 2020-02-05 逝于纳什维尔，享年 97 岁）
- **气质关键词**：**神经生长因子的共同分离者、表皮生长因子的发现者、生长因子生物学的开创者** —— 1986 年获奖理由（逐字引用 medic/nobel_medicine_citations.json，与 Levi-Montalcini 共享同一句）：
  > "for their discoveries of growth factors"
  > （因他们关于生长因子的发现）
- **设计母题**：**生长因子之窗（the growth factor window）**。新生小鼠提前睁眼与长牙的惊人现象、培养皿中的因子活性——"一针下去，窗口提前打开"。
- **本地 Wikipedia 路径**：medic/presentations/pages/20th_century/Stanley_Cohen_biochemist/page.md
- **参考模板**：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）

## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章）

- 第 0/1/2/3 步按 **medic 路径**执行：事实基准 = `medic/presentations/pages/20th_century/Stanley_Cohen_biochemist/page.md`；目录 `medic/presentations/20th_century/Stanley_Cohen_biochemist/`；Makefile 改 `MAIN=Stanley_Cohen_biochemist_zh`；肖像优先 images.txt 所列 Commons 图（Cohen in 2007 等），失败用装饰圆占位。
- 第 4/4.5 步（入库）**已完成**（第三、四节与 `MySQL/data/Stanley_Cohen_biochemist.yaml` 一致，勿重复入库）。
- 第 5-9 步：配色 → 幻灯片 → Beamer → 布局检查（0 error、vbox≤10pt、hbox≤50pt、逐页目检）→ 史实审查（第七节）。

## 三、研究领域梳理 + 入库（rank 0-4 表）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biochemistry | 生物化学 | 职业主领域（infobox Fields） | 封面 |
| 1 | growth factor biology | 生长因子生物学 | NGF/EGF，诺奖核心 | 核心页 |
| 2 | endocrinology | 内分泌学 | 职业构成之一 | 封面注记 |
| 3 | cancer biology | 癌症生物学 | 生长因子与抗癌药物设计 | 遗产页 |

## 四、社会关系梳理 + 入库（与 yaml 完全一致，已完成）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Howard B. Lewis | 师→本人 | 密歇根大学博士导师（1948，蚯蚓氮代谢） |
| colleague | Rita Levi-Montalcini | 无向 | 圣路易斯华盛顿大学合作者，共同分离 NGF |
| co-honored | Rita Levi-Montalcini | 无向 | 1986 诺贝尔生理学或医学奖共享（生长因子） |

> 对手方规范名：`Rita Levi-Montalcini` 沿用库内裸 stub id=6125（Dulbecco 批次所建，UPD 由其本批处理）；`Howard B. Lewis` 新建。**库内规范名带消歧后缀 'Stanley Cohen (biochemist)'（manifest 逐字一致），Levi-Montalcini 篇镜像边同键。** page.md 极薄（无家庭/学生记载）——**relations=3 为诚实值**，立传勿虚构补边。

## 五、配色方案

- **气质**：布鲁克林裁缝之子的朴素 + "总在正常反应之外再做一步"的实验嗅觉 + 纳什维尔的沉静晚年
- **主色**：生长因子绿 `#4E7A3A`（培养皿与新生小鼠的生机色）
- **诺奖香槟金**：`#D4AF37`
- **badge 四分类色**：
  - `badgeA` NGF 分离 — 神经金橙 `#C97B2D`
  - `badgeB` EGF 发现 — 生长绿 `#3E6B4F`
  - `badgeC` 同位素与代谢方法学 — 方法青 `#2E7D8C`
  - `badgeD` 癌症药物设计 — 转化蓝 `#2E6E9E`
- **背景母题**：低透明度新生小鼠窗台意象（早开的眼睑）+ 因子梯度扩散弧线。

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 生长因子的共同发现者 / Stanley Cohen 1922–2020 + badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、布鲁克林、Brooklyn College 1943、Oberlin MA 1945、密歇根博士 1948、WashU/Vanderbilt、诺奖 1986）
03  核心贡献概览 — NGF 共同分离 / EGF 发现 / 生长因子与癌症 / h-index 82 的沉静产出
04  裁缝之子与牛奶厂 (1922–1943) — 犹太移民家庭、父亲 Louis 是裁缝、Brooklyn College 化学兼生物双主修、牛奶厂细菌学家打工
05  蚯蚓的氮代谢 (1943–1949) — Oberlin 动物学硕士 1945、密歇根大学 Lewis 门下博士（蚯蚓氮代谢）1948、科罗拉多做早产儿代谢
06  圣路易斯与同位素 (1952–1959) — 放射学系学同位素方法、转动物学系；与 Levi-Montalcini 携手
07  NGF 的分离（核心页一）— Levi-Montalcini 观察到肿瘤促神经生长之谜→Cohen 以生化手段分离活性因子；双人分工：生物学现象×化学纯化
08  意外的窗口：EGF（核心页二）— 注射 NGF 提取物的对照发现新生小鼠提前睁眼长牙→分离出促上皮生长蛋白→更名表皮生长因子
09  Vanderbilt 岁月 (1959–1999) — 医学院教席四十年、持续研究细胞生长因子
10  1986 诺贝尔奖 — 与 Levi-Montalcini 共享；官方理由全句（NGF 分离 + EGF 发现双成就）；Horwitz 1983/Lasker 1986/国家科学奖章 1986 预演
11  荣誉长廊 — Rosenstiel 1981、Horwitz 1983、Lasker 1986、Franklin 奖章 1987、Gairdner、Fred Conrad Koch 奖
12  遗产：从生长因子到抗癌药 — 生长因子研究奠定癌症发生理解与靶向药物设计基础（EGFR 通路一线）
13  沉静的产出 — h-index 82（2022 口径）；1999 从 Vanderbilt 退休
14  家庭与身后 — page.md 无婚姻子女记载（诚实值注记）；2020-02-05 逝于纳什维尔，享年 97
15  结尾（OpenMathAI 品牌口径）
```

## 七、特殊陷阱表（★ 核心）

| 陷阱 | 说明 |
|------|------|
| 共享结构 | 1986 两人共享同一句理由；分工：Levi-Montalcini=生物学现象（肿瘤促神经生长观察）、Cohen=化学分离与 EGF 发现——互补勿混写 |
| 消歧后缀 | 库内/manifest 规范名 **Stanley Cohen (biochemist)**（勿与遗传学家 Stanley Cohen 混）——Levi-Montalcini 篇镜像边同键；正文行文写"斯坦利·科恩"即可 |
| EGF 意外发现 | EGF 系 NGF 实验的**对照观察**（早睁眼早长牙）——科学史经典"意外之喜"，保留叙事；勿写成有计划发现 |
| 页面极薄 | page.md 仅 67 行、无家庭/门生/引语——**relations=3 诚实值**；生平细节（如 EGF 具体年份、蛇毒来源等）page.md 未载者禁外部知识补充 |
| NGF 分工 | NGF 分离系"Working with Rita Levi-Montalcini"——双人合作完成，勿写成 Cohen 独立分离 |
| 后期荣誉 | Franklin Medal 1987 等；1999 退休；2020 逝于纳什维尔——时间线简单勿错置 |
| 引语红线 | page.md 无整句直接引语——全部转述 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| nerve growth factor (NGF) | 神经生长因子 | 1986 诺奖核心之一 |
| epidermal growth factor (EGF) | 表皮生长因子 | Cohen 独立发现 |
| growth factor | 生长因子 | 本届诺奖共同领域 |
| incisor eruption | 切牙萌出 | EGF 发现的意外表型 |
| eyelid opening | 睁眼 | 同上 |
| isotope methodology | 同位素方法 | WashU 放射学系训练 |
| EGFR pathway | EGFR 通路 | 遗产页应用方向 |
| h-index | h 指数 | 82（2022 口径） |

## 九、背景音乐选择

- **选定曲目**：**Shine Like The Sun** — Alex-Productions（manifest 预分配）
- **匹配理由**："如日生辉"贴合新生小鼠提前睁开眼睛的经典意象——一针因子让生命的窗口提前打开；明快温暖的曲式匹配其"沉静而高产"的一生。
- **本地路径**：music_audio/ 下 Alex-Productions Shine Like The Sun 曲目（执行时按 curated_tracks.md 对应文件复制到本目录）。
