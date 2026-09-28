# 物理学家立传提示词（Erwin Schrödinger）

> 本文件是 OpenPhysicist 20 世纪诺贝尔物理学奖得主的「人物专属立传提示词」，以 Kenneth G. Wilson 篇为结构母本（0–11 节骨架一致）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPhysicist —— 开放物理学家人物史（与 OpenMath 数学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Erwin Schrödinger（埃尔温·薛定谔，1933 诺贝尔物理学奖，波动力学，与 Dirac 共享）。
- **设计哲学**：物理学家立传必须有「身份信息页」与结构化「研究领域」表达；Schrödinger 篇的设计重心是**波动与猫的暧昧**——波动力学的优雅形式与他终生对哥本哈根诠释的抗拒，构成「创造者与反叛者一体」的传记张力。

---

## 二、背景信息 【人物专属】

- **目标物理学家**：Erwin Rudolf Josef Alexander Schrödinger（1887-08-12 ~ 1961-01-04，享年 73 岁）
- **气质关键词**：**波动力学的缔造者、薛定谔之猫的饲养者、跨界的哲人科学家** —— 1933 诺贝尔物理学奖获奖理由（与 Paul Dirac 共享）：
  > "for the discovery of new productive forms of atomic theory"（因发现原子理论的新型富有成果的形式）
- **设计母题**：**叠加态（superposition）**。既是波又是粒子、既是创造者又是质疑者、既在维也纳又在都柏林——「两种状态同时为真」是比单纯「波动」更贴合他一生的视觉语言。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/physicist/presentations/20th_century/20th_century/Erwin_Schrödinger/page.md`（Wikipedia 全文已抓取）
- **待下载**：本目录尚无 `Erwin_Schrödinger.html` 与 `images/`，第 0 步需从 `https://en.wikipedia.org/wiki/Erwin_Schr%C3%B6dinger` 下载页面与肖像（infobox 1933 年照片或 c.1914 年轻照）。
- **参考模板**：
  - 结构母本：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：下载并核对 Wikipedia 页面 【人物专属】

- page.md 已在本地（见上），**事实基准如下**（以 page.md 为唯一依据）：
  - 生卒（1887-08-12 生于奥匈帝国维也纳 ~ 1961-01-04 逝于奥地利维也纳，死于肺结核，享年 73 岁）
  - 国籍/公民身份（奥地利；爱尔兰入籍 1948，保留奥地利籍；frontmatter nationality 含 Cisleithania/Germany/Nazi Germany 为历史政权口径）
  - 父母（父 Rudolf Schrödinger 为植物学家；母 Georgine Emilia Brenda Bauer，维也纳工业大学化学教授之女，半奥地利半英国血统）
  - 教育（Akademisches Gymnasium；1906-1910 维也纳大学，师从 Franz S. Exner 与 Friedrich Hasenöhrl；1910 博士（导师 Hasenöhrl）；1914 在 Exner 指导下完成 habilitation）
  - 任职机构（1920 Jena 助教 → Stuttgart 副教授 → 1921 Breslau 正教授 → 1921 苏黎世大学 → 1927 接替 Planck 柏林大学 → 1933 辞德赴牛津 Magdalen College → 1936 Graz → 1938 流亡意大利/牛津/根特 → 1940-1955 都柏林高等研究院（DIAS）理论物理学院院长 → 1956 维也纳大学荣休教授）
  - 关键荣誉（Matteucci 1927、Haitinger 1920、Nobel 1933、Max Planck Medal 1937、Erwin Schrödinger Prize 1956、Pour le Mérite 1956；教廷科学院 1936、皇家学会外籍会士 1949）
  - 知名学生（infobox：Nándor Balázs、Bruno Bertotti、Cécile DeWitt-Morette、James Hamilton、Walter Heitler、Frank C. Hoyt、Fritz London、Francis W. Loomis、Harry Messel、Linus Pauling、彭桓武（Huanwu Peng）、Brendan Scaife、Walter Thirring）
  - 家庭（1920 娶 Annemarie Bertel，婚姻无子女；1934 与 Hildegunde March 生一女；孙辈 Terry Rudolph 为帝国理工量子物理学家）
  - 核心贡献清单（见第 4 步）
  - 关键时间线（15–20 节点）：1887 维也纳生 → 1906 入维也纳大学 → 1910 博士 → 1914 habilitation → 1914-18 奥匈要塞炮兵军官 → 1920 Jena/Stuttgart → 1921 Breslau → 1921 苏黎世 → 1920 Haitinger 奖（大气放射性，验证 Victor Hess 观测）→ 1926-01 起四周一篇的波动力学四部曲 → 1927 接掌柏林 Planck 讲席 → 1933 辞德赴牛津 + 诺贝尔奖 → 1935 纠缠论文与薛定谔猫 → 1936 Graz → 1938 Anschluss 后流亡 → 1939 de Valera 邀请 → 1940 DIAS 院长 → 1943 三一学院讲座 → 1944《What Is Life?》→ 1948 爱尔兰入籍 → 1947 仿射场论宣布失败 → 1955 退休 → 1956 回维也纳 → 1961-01-04 逝世，葬于 Alpbach（墓碑刻 iℏΨ̇=HΨ）

### 第 1 步：建立目录 【模板通用】

- 在 `physicist/presentations/20th_century/` 下使用本目录 `Erwin_Schrödinger/` 并创建 `images/`。

### 第 2 步：复制 Makefile 【模板通用】

- 复制参照成品 `Makefile`，设置 `MAIN=Erwin_Schrödinger_zh`、`VIDEO_NAME=Erwin_Schrödinger_zh`（宏名/文件名如含非 ASCII 需先验证 xelatex 兼容，必要时用 `Erwin_Schrodinger_zh` 去 ö）。

### 第 3 步：收集图片 【人物专属】

- 下载 infobox 肖像到 `images/`；404 用 Commons `Special:FilePath/Erwin_Schrodinger2.jpg?width=600` 回退。可补插图：1942 DIAS 合影（与 de Valera）、Alpbach 墓碑照片。

### 第 4 步：研究领域梳理 + 入库 【模板通用，人物专属内容】

**Schrödinger 的研究领域（按 rank 排序）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | quantum mechanics | 量子力学 | 波动力学四部曲（1926）、薛定谔方程 | 核心页 |
| 1 | quantum entanglement | 量子纠缠 | 1935 由他命名并系统化 | 纠缠页 |
| 2 | statistical mechanics | 统计力学 | 与热力学、介电物理同属其早期/旁支工作 | 旁支页 |
| 3 | color theory | 色觉理论 | Farbenmetrik 系列论文（1920） | 色觉页 |
| 4 | unified field theory | 统一场论 | 1947 仿射场论等尝试（与爱因斯坦通信） | 晚年页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Friedrich Hasenöhrl | 导师→本人 | 维也纳大学博士导师（1910） |
| advisor-student | Franz S. Exner | 导师→本人 | habilitation 导师，统计自然观影响其一生 |
| advisor-student | Linus Pauling | 本人→学生 | infobox 学生，后获诺贝尔化学奖 |
| advisor-student | Walter Heitler | 本人→学生 | infobox 学生，价键理论 |
| advisor-student | Fritz London | 本人→学生 | infobox 学生，伦敦力 |
| advisor-student | Peng Huanwu | 本人→学生 | infobox 学生（彭桓武） |
| spouse | Annemarie Bertel | 无向 | 1920 年结婚，婚姻无子女 |
| co-honored | Paul Dirac | 无向 | 1933 诺贝尔物理学奖共享 |
| colleague | Werner Heisenberg | 无向 | 1926 第三篇论文证明波动力学与矩阵力学等价 |
| colleague | Hermann Weyl | 无向 | 挚友，几何方法为其波动力学铺路 |
| influence | Albert Einstein | 无向 | 1935 EPR 通信直接催生薛定谔猫思想实验 |

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：暧昧、优雅、维也纳式忧郁
- **配色**：暗蓝灰（主色 `#2B4162`）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeWave` 波动力学 — 暗蓝灰 `#2B4162`
  - `badgeEnt` 量子纠缠 — 洋红 `#9C27B0`
  - `badgeStat` 统计力学 — 青绿 `#0E7C7B`
  - `badgeColor` 色觉理论 — 琥珀 `#E07B30`
- **背景母题**：柔和气泡中以「实心圆与虚线圆重叠」的叠加态图形呼应设计母题。

### 5.1 物理学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + 细边框 + 姓名小字注）与国籍行。
2. 必须有身份信息页：左侧头像 + 右侧信息网格（生卒、本名、国籍、出生地、师承、任职、主要荣誉、核心领域），事实取自 page.md infobox，不得杜撰。
3. 结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPhysicist 项目首页（\input cover/openphysicist_page.tex）
01  封面 — 波动力学缔造者 / Erwin Schrödinger 1887–1961 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（含师承、任职、荣誉、核心领域）
03  核心贡献概览 — 波动力学 / 量子纠缠 / 统计力学 / 色觉理论
04  维也纳少年（1887–1914）— Exner 与 Hasenöhrl、战时炮兵军官
05  漂泊教席（1920–1921）— Jena、Stuttgart、Breslau 到苏黎世
06  1926：波动力学四部曲（核心贡献页）— Quantisierung als Eigenwertproblem
07  公式框页 — 薛定谔方程 iℏ ∂Ψ/∂t = ĤΨ（墓碑同款 iℏΨ̇=HΨ 可并注）
08  等价与抗拒 — 与矩阵力学等价、"I don't like it…"（page.md 原句可引）
09  1935：纠缠与猫 — EPR 通信、coined quantum entanglement、思想实验本意
10  流亡与都柏林（1933–1955）— 拒纳粹、Anschluss、de Valera、DIAS 院长
11  What Is Life?（1944）— 负熵与遗传密码，启发 Watson/Crick
12  柏拉图式的晚景 — 统一场论失败、1956 回维也纳、"only one mind"
13  荣誉与认可 — Nobel 1933 · Planck Medal 1937 · Pour le Mérite 1956
14  遗产：从波函数到量子信息
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；头部宏定义整体复用结构母本骨架。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make distclean && make pdf`，用 `pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Schrödinger 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方原句 "for the discovery of new productive forms of atomic theory"，与 Dirac 共享；勿写"因提出薛定谔方程获诺奖" |
| 波动方程诞生地 | 在瑞士 Arosa 疗养院（1925 年末）构思 wave equation，勿写成"在苏黎世办公室" |
| entanglement | 一词由薛定谔 1935 创造（coined），勿写成他人 |
| 薛定谔的猫 | 1935 思想实验，目的是讽刺哥本哈根诠释，非支持；勿写成"证明猫既死又活" |
| 统计诠释原话 | "I don't like it, and I'm sorry I ever had anything to do with it." 为 page.md 英文原句，可引 |
| 私生活 | 与妻子及情人的居住安排、Oxford/Graz 因之不快为 page.md 明载，可中性一句；**性侵指控一节高度敏感，Beamer 立传建议完全回避**，如须处理只写"相关争议见 page.md" |
| 两说年份 | 无爱尔兰首席身份——他是 DIAS 理论物理学院**院长（Director of the School of Theoretical Physics）**，勿写成"DIAS 院长"泛称 |
| 波粒二象性 | 晚年转向"纯波动观"引发争议（wave-only view），勿写成他否定自己方程 |
| 导师区分 | 博士导师 Hasenöhrl（PhD 1910），habilitation 导师 Exner（1914）；Exner 亦是 Victor Hess 的导师之一，注意跨篇一致性 |
| 同名区分 | 妻子 Annemarie (Anny) Bertel；情妇 Hildegunde March 是同事 Arthur March 之妻；孙辈 Terry Rudolph 现任帝国理工——三者勿混 |
| 墓地 | 葬于 Alpbach 天主教墓园（本人非天主教徒），墓碑刻 iℏΨ̇=HΨ |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| wave mechanics | 波动力学 | 与 matrix mechanics（海森堡）对照 |
| wave function | 波函数 | 勿译"概率幅"泛化 |
| Schrödinger equation | 薛定谔方程 | 时间相关/定态两式勿混 |
| quantum entanglement | 量子纠缠 | 1935 coined |
| Schrödinger's cat | 薛定谔的猫 | 思想实验 |
| eigenvalue problem | 本征值问题 | Quantisierung als Eigenwertproblem |
| negentropy | 负熵 | What Is Life? 核心概念 |
| quantum steering | 量子导引 | infobox Known for 之一 |
| EPR paradox | EPR 悖论 | Einstein–Podolsky–Rosen |
| Pontifical Academy of Sciences | 教廷科学院 | 1936 院士，葬地依据 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Mirage** — Notan Nigres（3:22）
- **风格**: 电子 / 梦幻 / 抽象
- **匹配理由**: 薛定谔是量子力学史上最"暧昧"的身影——波与粒子、生与死的猫、物理与哲学的边界；Mirage 的梦幻抽象质感正贴合叠加态母题与维也纳式忧郁。
- **备选**（未采用）: Falling Apart（渐进/情感，匹配其与量子主流的疏离，但情绪偏丧）；Nostalgy（怀旧/深沉，受众更高但气质偏"回忆"而非"思辨"）。
- **本地路径**: `music_audio/inspiring-electronic/04-5gcb94jhG1I-Notan Nigres - Mirage (Audio).wav` → `presentations/20th_century/Erwin_Schrödinger/Mirage.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `physicist/presentations/20th_century/20th_century/Erwin_Schrödinger/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | 成品 Beamer 骨架/源码 |
| `physicist/presentations/cover/openphysicist_page.tex` | 项目首页模板 |
| `MySQL/seed_person.py` | 人物 + 领域 + 关系入库引擎 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修；所有事实以 page.md 为准，无载禁写。**
