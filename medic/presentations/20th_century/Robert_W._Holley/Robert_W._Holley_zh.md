# 医学家立传提示词（Robert W. Holley）

> OpenMedic 项目、20 世纪诺贝尔生理学或医学奖 1968 年得主（罗伯特·霍利，tRNA 序列与三叶草模型的开创者）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Robert William Holley（1922-01-28 生于伊利诺伊州厄巴纳 ~ 1993-02-11 卒于加州 Los Gatos，享年 71 岁）
- **气质关键词**：**史上第一条核酸序列的测定者、tRNA 三叶草模型的奠基者、连接 DNA 与蛋白质合成的摆渡人** —— 1968 获奖理由（与 Har Gobind Khorana、Marshall Warren Nirenberg 三人共享）：
  > "for their interpretation of the genetic code and its function in protein synthesis"（因解析遗传密码及其在蛋白质合成中的功能）
- **设计母题**：**三叶草**。丙氨酸 tRNA 的三叶草形二级结构——核苷酸的"拼图"拼出生命翻译的第一张地图。视觉隐喻：三片叶瓣的 RNA 链，每片缀着序列字母。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Robert_W._Holley/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/20th_century/Robert_W._Holley/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准，裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/20th_century/Robert_W._Holley/`（含 `images/`）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=Robert_W._Holley_zh`、`VIDEO_NAME=Robert_W._Holley_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/20th_century/Robert_W._Holley/images.txt`（R_Holley.jpg，三人合影裁左——图注说明）；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/Robert_W._Holley.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biochemistry | 生物化学 | tRNA 结构测定，1968 诺奖核心 | 核心页 |
| 1 | transfer RNA | 转运 RNA | 丙氨酸 tRNA 全序列（史上首条核酸序列） | 核心页 |
| 2 | organic chemistry | 有机化学 | 博士专业；青霉素首次化学合成参与 | 早年页 |
| 3 | molecular biology | 分子生物学 | mRNA 翻译机制的解释 | 核心页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Vincent du Vigneaud | 导师 | 二战期间康奈尔医学院在其门下两年，参与青霉素首次化学合成 |
| advisor-student | James F. Bonner | 导师 | 1955-56 Caltech 学术休假随其研究，由此转向 RNA |
| collaborator | Elizabeth Beach Keller | 无向 | 团队成员，提出 tRNA 三叶草模型 |
| co-honored | Har Gobind Khorana | 无向 | 1968 诺贝尔生理学或医学奖三人共享（遗传密码的解析及其在蛋白质合成中的功能） |
| co-honored | Marshall Warren Nirenberg | 无向 | 1968 诺贝尔生理学或医学奖三人共享（遗传密码的解析及其在蛋白质合成中的功能） |
| spouse | Ann | 无向 | 妻，1996 年去世 |

> relations=6 为诚实值，Review 勿误判缺漏。
> 不入库： du Vigneaud 之外战时同事；Holley 团队其他成员（page.md 仅具名 Keller）；Salk 研究所同事；NYT 讣告作者。
> 库内既有 Vincent du Vigneaud（#3863, Q33128，1955 诺奖化学得主）规范记录直接引用；James F. Bonner / Elizabeth Beach Keller / Khorana / Nirenberg / Ann 由本 yaml 新建 stub（Khorana/Nirenberg 用 manifest 全名，其本人 yaml 将回填）。

## 五、配色方案 【人物专属】

- **气质**：伊利诺伊平原的麦色 + RNA 序列的排列美 + 三叶草的生命绿
- **主色**：三叶草绿 `#2F6B4F`（tRNA 三叶草模型的生命意象）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` tRNA 序列 — 三叶草绿 `#2F6B4F`
  - `badgeB` 序列"拼图"方法 — 琥珀 `#A0722D`
  - `badgeC` 有机化学起点 — 灰蓝 `#4A5A6A`
  - `badgeD` Salk 岁月 — 深青 `#0E7C7B`
- **背景母题**：三叶草形 RNA 轮廓线 + 沿链排布的小字母方块，四色叶瓣。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — 史上第一条核酸序列 / Robert W. Holley 1922–1993 + 四色 badge + 右上头像 + 国籍行 USA
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生 Urbana、教育 Illinois BS 1942/
    Cornell PhD 1947、战时 du Vigneaud 门下、任职 Cornell 1948-64/Salk 1968 起、
    荣誉 Nobel 1968/Lasker 1965/NAS 分子生物学奖 1967、核心领域）
03  核心贡献概览 — 丙氨酸 tRNA 全序列 / 三叶草模型 / 序列"拼图"方法 / 翻译机制的解释
04  厄巴纳少年 (1922–1942) — Urbana High School 1938、伊利诺伊大学化学 1942
05  康奈尔与青霉素 (1942–1947) — 有机化学博士、二战期间在 du Vigneaud（1955 诺奖化学）
    门下两年、参与青霉素的首次化学合成、1947 PhD
06  Cornell 教职与转向 RNA — 1948 有机化学助理教授、1962 生物化学教授、
    1955-56 Caltech 学术休假随 James F. Bonner——人生的 RNA 转向
07  tRNA 的分离 — 从分离转运 RNA 起步：把氨基酸带入蛋白质的"适配器"分子
08  双酶切"拼图"法 — 两种核糖核酸酶在特定位点切开 tRNA、
    比对两套片段"拼出"完整结构——序列测定的方法论
09  1964：史上第一条核酸序列 — 丙氨酸 tRNA 全序列完成、
    解释 mRNA 指导蛋白质合成的翻译机制
10  三叶草模型 — 团队成员 Elizabeth Beach Keller 提出 tRNA 三叶草模型、
    他人用 Holley 方法测定其余 tRNA、方法被改造用于细菌/植物/人类病毒序列追踪
11  1965 Lasker → 1968 Nobel — Lasker 基础医学研究奖 1965、NAS 分子生物学奖 1967、
    1968 与 Khorana/Nirenberg 三人共享诺奖
12  Salk 岁月与身后 — 1968 起 Salk 研究所常驻研究员、
    业余青铜雕塑家与户外运动者（NYT 讣告口径，可转述）、1993-02-11 卒于 Los Gatos
13  个人生活 — 妻 Ann（1996 年去世）
14  遗产 — 从 tRNA 到基因组时代的测序源头、RNA 生物学的开山谱系、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方逐字 "for their interpretation of the genetic code and its function in protein synthesis"（三人共享、their）；Holley 的个人贡献是**tRNA 结构**（page.md 口径），Khorana/Nirenberg 贡献密码子解码——分工勿混 |
| 首条序列口径 | "第一个被测定的核糖核酸（核酸）序列"——史上第一，勿弱化为"之一" |
| 三叶草模型归属 | 模型由团队成员 **Elizabeth Beach Keller** 提出（page.md 明载 "during the course of the research"）——勿写成 Holley 本人提出 |
| 肖像图注 | images 中 R_Holley.jpg 为三人合影且 Holley 在最左——裁剪时注意，图注勿张冠李戴 |
| du Vigneaud 定位 | 战时两年在其门下（Cornell Medical College）——advisor-student；du Vigneaud 1955 诺奖化学得主可点一句 |
| Bonner 定位 | 1955-56 学术休假（sabbatical）研究一年——人生的 RNA 转折点，advisor-student 边 note 写"学术休假" |
| 青霉素细节 | "参与青霉素的首次化学合成"（involved in）——参与者口径，勿写"主持合成" |
| 妻子姓名 | page.md 仅载 "His widow Ann"（无姓）——yaml 存 'Ann'，勿杜撰全名 |
| 页面极简 | page.md 短、无争议内容——宁少勿造；死亡日期 "He died in 1993" 与 infobox 02-11 一致，取 1993-02-11 |
| Salk 任职 | 1968 年起 resident fellow——与诺奖同年，勿写成诺奖后"退休" |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| transfer RNA (tRNA) | 转运 RNA | 氨基酸的"适配器" |
| alanine tRNA | 丙氨酸 tRNA | 被测定的具体分子 |
| cloverleaf model | 三叶草模型 | tRNA 二级结构（Keller 提出） |
| ribonuclease | 核糖核酸酶 | 双酶切"拼图"的工具 |
| messenger RNA (mRNA) | 信使 RNA | 翻译机制的另一主角 |
| penicillin synthesis | 青霉素合成 | 战时参与项目 |
| sabbatical | 学术休假 | 1955-56 Caltech |
| Salk Institute | 索尔克研究所 | 1968 起常驻 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Pathfinder**（manifest 预分配）
- **风格**：开拓 / 前行 / 沉稳史诗
- **匹配理由**：在无人测过核酸序列的年代，用两把"酶刀"和耐心拼出生命翻译的第一张地图——Pathfinder 的行进感匹配"从青霉素到 tRNA 再到 Salk"的开拓者一生。
- **本地路径**：`music_audio/inspiring-electronic/23-GiwYLGgJw7w-Ghostwriter Music - Pathfinder (Composed by Daniel Beijbom - Recorded in Budapest).wav` → 复制为 `presentations/20th_century/Robert_W._Holley/Pathfinder.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；三叶草模型归属与"首条序列"口径务必精确。**
