# 物理学家立传提示词（OpenPhysicist 21 世纪批次：Anne L'Huillier）

> 本文件是 OpenPhysicist 21 世纪诺贝尔物理学奖得主「人物专属立传提示词」，结构对齐标杆
> `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Anne Geneviève L'Huillier（安妮·吕利耶，2023 诺贝尔物理学奖三位得主之一，高次谐波产生的先驱观察者，本批唯一女性得主）。
- **设计哲学**：物理学家立传必须有「身份信息页」（Identity / Bio 速览页）与结构化「研究领域」表达，此两点为骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Anne Geneviève L'Huillier（1958-08-16 生于巴黎；在世，法国/瑞典双归属）
- **气质关键词**：**氩气中谐波的第一个聆听者、170 阿秒世界纪录保持者、阿秒化学的奠基人** —— 2023 诺贝尔物理学奖获奖理由（与 Pierre Agostini、Ferenc Krausz 共享）：
  > "for experimental methods that generate attosecond pulses of light for the study of electron dynamics in matter"（因产生阿秒光脉冲以研究物质中电子动力学的实验方法）
- **设计母题**：**泛音阶梯（overtone ladder）**。1987 年氩气在激光下发射激光频率整数倍的"泛音"——视觉上可用一列等比升高的谐波峰（阶梯状谱线）表达，正如她 1987 年首次观测的高次谐波谱。
- **本地数据源（已有）**：`physicist/presentations/21th_century/21st_century/Anne_L_Huillier/page.md`
- **待下载（第 0 步执行）**：`Anne_L_Huillier.html` 与 `images/` 肖像尚未下载；Wikipedia URL：`https://en.wikipedia.org/wiki/Anne_L%27Huillier`
- **参考模板**：
  - 物理学家首例成品：`physicist/presentations/20th_century/Eugene_Wigner/Eugene_Wigner_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：核对事实基准 【人物专属】

- page.md 已有本地，事实基准如下：
  - 生卒（1958-08-16 生于巴黎；在世）
  - 国籍（法国 → 瑞典，1994 年移居瑞典；frontmatter France + Sweden）
  - 家庭（丈夫 Claes-Göran Wahlström 为隆德大学教授；两个子女）
  - 教育（丰特奈欧罗斯高等师范 BA；皮埃尔与玛丽·居里大学理论物理与数学**双硕士**，后转实验物理，1986 博士，论文《Ionisation Multiphotonique et Multielectronique》（多光子与多电子电离），研究在 CEA 完成）
  - 博士导师（Bernard Cagnac，frontmatter + infobox 明载）
  - 博士后（哥德堡 Chalmers 技术学院 + 洛杉矶南加州大学）
  - 任职机构（1986 CEA Saclay 永久研究员职位；1992 参加隆德钛宝石飞秒激光实验；1994 移居瑞典；1995 隆德大学讲师；1997 隆德大学教授（原子物理）；另任法国光学研究所理事）
  - 关键荣誉（Julius Springer 奖 2003；瑞典皇家科学院院士 2004；诺贝尔物理学委员会委员 2007–2015；UNESCO L'Oréal 女科学家奖 2011；Carl-Zeiss 研究奖 2013；Blaise Pascal 奖章 2013；UPMC 荣誉博士 2013；美国科学院外籍院士 2018；EPS 量子电子学与光学基础成就奖 2019；Max Born 奖 2021；Wolf 物理学奖 2022 与 Krausz、Corkum；BBVA 前沿知识奖 2022 三人；军团勋章骑士级 2022；Berthold Leibinger 未来奖 2023；2023 诺贝尔物理学奖；北极星勋章司令大十字 2024；另有波尔多/波尔图/巴黎-萨克雷荣誉博士等）
  - 知名学生（page.md 无载，禁写）
  - 核心贡献清单：
    1. 1987 年首次观测氩等气体对强激光发射激光频率整数倍泛音（高次谐波产生 HHG 的实验起点）
    2. 1991 年与 Kenneth Schafer、Kenneth Kulander 用含时薛定谔方程数值模拟解释高次谐波谱形与相位匹配条件
    3. 1994 年与 Maciej Lewenstein、Paul Corkum 提出高次谐波产生的完整量子理论
    4. 2003 年研究组以 170 阿秒刷新最短激光脉冲世界纪录
    5. 开创阿秒化学（attochemistry）：用阿秒光源研究化学反应中的电子过程
    6. 2017 年实验揭示 shake-up 电子贡献，解决 2010 年 Krausz 组氖原子光电发射延迟偏差
  - 关键时间线（20 节点）：1958 生于巴黎 → 双硕士（理论物理+数学） → 1986 博士（CEA 完成） → 博士后 Chalmers + USC → 1986 CEA Saclay 永久职位 → 1987 首测氩气高次谐波 → 1991 与 Schafer/Kulander 数值模拟 → 1992 隆德钛宝石实验 → 1994 移居瑞典 → 1994 与 Lewenstein/Corkum 量子理论 → 1995 隆德讲师 → 1997 隆德教授 → 2003 170 as 世界纪录 → 2003 Springer 奖 → 2004 皇科院院士 → 2007–2015 诺奖委员会委员 → 2011 L'Oréal 奖 → 2021 Max Born 奖 → 2022 Wolf + BBVA + 军团骑士 → 2023 诺贝尔奖

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/21th_century/` 下创建 `Anne_L_Huillier/` 与 `images/`（目录名用 L_Huillier，撇号不入目录名）

### 第 2 步：复制 Makefile 【模板通用】

- 复制同目录既有成品（如 `Serge_Haroche/Makefile`），设置 `MAIN=Anne_L_Huillier_zh`、`VIDEO_NAME=Anne_L_Huillier_zh`

### 第 3 步：收集图片 【人物专属】

- 下载 L'Huillier 2012 年 infobox 肖像（Commons `Special:FilePath` 或 Wikipedia REST API，250px 改 500px，curl 加 `-A "Mozilla/5.0"`，`file` 验证）；404 则装饰圆占位并注明

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | high harmonic generation | 高次谐波产生 | 1987 年首次观测，诺奖工作起点 | 核心页 |
| 1 | attosecond physics | 阿秒物理 | 2023 诺奖核心领域 | 封面、核心页 |
| 2 | multiphoton ionization | 多光子电离 | 博士论文主题 | 博士页 |
| 3 | atomic physics | 原子物理 | 隆德大学教授职位 | 任职页 |
| 4 | attochemistry | 阿秒化学 | 开创领域：化学反应电子过程 | 遗产页 |

- 入库：`cd MySQL && python3 seed_person.py data/Anne_L_Huillier.yaml`

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> 只收 page.md 明载关系；对手方无 qid 不编造。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Bernard Cagnac | 师→生（博士导师） | 皮埃尔与玛丽·居里大学博士导师 |
| spouse | Claes-Göran Wahlström | 无向 | 丈夫，同为隆德大学教授 |
| co-honored | Ferenc Krausz | 无向 | 2022 Wolf + 2022 BBVA + 2023 诺贝尔共同得主 |
| co-honored | Paul Corkum | 无向 | 2022 Wolf + 2022 BBVA 共同得主 |
| co-honored | Pierre Agostini | 无向 | 2023 诺贝尔物理学奖共同得主 |
| colleague | Paul Corkum | 无向 | 1994 年 HHG 完整量子理论合作者 |
| colleague | Maciej Lewenstein | 无向 | 1994 年 HHG 完整量子理论合作者 |

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：阶梯、泛音、北欧清冽
- **主色**：深青绿 `#175E54` + 诺奖香槟金 `C9A227`
- badgeA–D 四分类色：badgeHHG 高次谐波 — 靛蓝 `#4C5FD5`；badgeAtto 阿秒物理 — 琥珀 `#E07B30`；badgeAttochem 阿秒化学 — 玫瑰 `#C4204F`；badgeCareer 机构岁月 — 青绿 `#0E7C7B`
- **背景母题**：谐波阶梯（一组等比升高、亮度递减的竖条），呼应 1987 年氩气泛音谱与 170 as 纪录的"越切越短"

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注）。
2. 封面有国籍：底部状态栏 `国籍 | 机构 | 主要奖项` 三要素（国籍写 France / Sweden）。
3. 必须有身份信息页：封面之后、核心贡献之前，左头像 + 右信息网格，事实取自 page.md infobox。
4. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 高次谐波先驱 / Anne L'Huillier 1958– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — HHG 首测 / 理论与模拟 / 170 as 纪录 / 阿秒化学
04  巴黎求学 (1958–1986) — 双硕士、CEA 博士、Cagnac 门下
05  博士后与大洋两岸 — Chalmers、USC、1986 CEA Saclay 永久职位
06  1987：氩气中的泛音（核心贡献页一）— 高次谐波首次观测
07  从观察到理论 (1991–1994) — Schafer/Kulander 模拟、Lewenstein/Corkum 量子理论
08  移居北欧 (1992–1997) — 隆德钛宝石实验、1995 讲师、1997 教授
09  2003：170 阿秒世界纪录（核心贡献页二）— "世界最快的相机"
10  阿秒化学与 shake-up 之争 — 化学反应电子过程、2017 解决 2010 氖原子延迟偏差
11  荣誉矩阵（高斯表格版式）— 皇科院 2004 / 诺奖委员 2007–2015 / L'Oréal 2011 / Max Born 2021
12  2022 双奖 — Wolf 奖 + BBVA 奖（与 Krausz、Corkum）
13  2023 诺贝尔物理学奖 — 三人共享、citation 原句
14  遗产：attochemistry 的地基
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照成品 `\profileslide`。
- 头部宏定义（配色 / `\plainbar` / `\deckbackground` / `\sectiontitle`）整体复用同目录成品骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**L'Huillier 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 姓名撇号 | L'Huillier 的撇号（U+0027）在 LaTeX 中可直书，但目录名/宏名禁撇号（目录 Anne_L_Huillier） |
| 双硕士 | 理论物理与数学**双**硕士后转实验物理博士，勿写"理论物理博士" |
| HHG 年份 | 1987 年首次观测泛音发射；1991 数值模拟；1994 完整量子理论——三步勿混 |
| 170 as | 2003 年本组刷新世界纪录 170 阿秒；与 Agostini 2001 年 250 as 脉冲串是不同成果 |
| Wolf 三人 | 2022 Wolf 与 Krausz、Corkum 共享；2023 Nobel 是与 Krausz、Agostini 共享——Corkum 无诺奖、Agostini 无 Wolf，勿混 |
| 诺奖委员会委员 | 2007–2015 年任诺贝尔物理学委员会委员；她 2004 年已入皇家科学院，两事实勿合并 |
| Alain Aspect | 2023 巴黎-萨克雷荣誉博士典礼上 Aspect 是嘉宾——仅可在荣誉页作注，勿写成合作关系 |
| 军团勋章 | page.md 明载 2022 骑士级（29 Dec 2022）与 2024 北极星司令大十字；frontmatter 还有 Officer/Commander 级但正文无年份，勿标 |
| 子女 | infobox 载 two children，身份页可写"两个子女"，勿展开 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| high harmonic generation (HHG) | 高次谐波产生 | 强场气体中激光频率整数倍辐射 |
| overtone | 泛音 | page.md 用 overtone 描述 1987 现象 |
| attosecond | 阿秒 | 10⁻¹⁸ 秒 |
| attochemistry | 阿秒化学 | page.md 明载她奠定该领域 |
| phase-matching | 相位匹配 | 1991 模拟预测的条件之一 |
| shake-up electron | shake-up 电子 | 2017 年解决延迟偏差的关键，保留英文 |
| titanium-sapphire laser | 钛宝石激光器 | 1992 隆德欧洲首批飞秒系统 |
| argon | 氩 | 1987 实验气体 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Shine Like The Sun** — Really Slow Motion（inspiring-electronic 合辑）
- **风格**：史诗 / 美丽 / 振奋
- **匹配理由**："光明结尾"匹配她的主题——从 1987 年氩气中"多余的亮光"（泛音）到 2023 诺奖；谐波阶梯本身就是光的升华。
- **本地路径**：`music_audio/inspiring-electronic/15-w6kT1BfvETI-Really Slow Motion - Shine Like The Sun (Epic Beautiful Uplifting).wav`
- **备选** (未采用):
  - ★★ Awaken — "明亮/鼓舞"匹配 1987 年氩气泛音的"第一次亮起"，但开场曲气质与传记中段更配
  - ★ Daylight — "轻快/明亮"匹配北欧气质，但史诗感不足以收 2023 诺奖
- **批内去重**：本曲在本批（batch 13）内不与 Agostini / Krausz / Hopfield / Hinton 重复。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/21th_century/21st_century/Anne_L_Huillier/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构标杆 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/data/Anne_L_Huillier.yaml` | 社会关系 + 领域入库 yaml |
| `MySQL/seed_person.py` | 幂等入库引擎 |

> **开始执行。每完成一步向我汇报。**
