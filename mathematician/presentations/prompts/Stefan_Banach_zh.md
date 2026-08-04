# 巴拿赫 (Stefan Banach) 立传提示词

> 本提示词严格遵循 [数学家立传工作指南.md](../数学家立传工作指南.md)，以 Kolmogorov、Hilbert、Riemann 等成品为参考模板，为巴拿赫制作 Beamer 演示文稿。
> 直接复制本文件内容到新对话中使用。

---

## 背景信息

- **目标数学家**: Stefan Banach (1892–1945)
- **气质关键词**: **自学成才的天才、Lwów 学派灵魂、苏格兰咖啡馆数学、波兰数学的荣耀、被战争吞噬的分析巨人**
- **Wikipedia 页面**: ⚠️ **尚未下载。** 第一步需要运行下载脚本：
  - 页面路径: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Stefan_Banach/`
- **参考模板**: `kolmogorov/`, `hilbert/`, `riemann/`, `neumann/` 等完整源码
- **操作指南**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/数学家立传工作指南.md`

---

## 你的任务

按照 [数学家立传工作指南.md](../数学家立传工作指南.md) 第十一节「推荐制作流程」的步骤，依次完成。**每完成一步向我汇报进度**，遇到歧义时先征求我的意见再继续。

---

## 第 0 步：下载 Wikipedia 页面并校验

下载到 `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Stefan_Banach/`

输出以下信息供校验：

- **生卒日期**：1892-03-30 ~ 1945-08-31，享年 53 岁
- **国籍**：波兰（奥匈帝国出生 → 波兰第二共和国）
- **出生地**：Kraków (克拉科夫)，当时属奥匈帝国加利西亚
- **死亡地**：Lwów (利沃夫/伦贝格)，当时被纳粹德国占领（今乌克兰）
- **博士导师**：Hugo Steinhaus（非正式指导，实际上 Banach 没有正式意义上的博士培养过程）
- **博士论文**：1920，《Sur les opérations dans les ensembles abstraits et leur application aux équations intégrales》（论抽象集合中的运算及其在积分方程中的应用）— 博士论文包含 Banach 空间和 Hahn–Banach 定理的核心思想
- **主要任职机构**：
  - 1920–1922: 克拉科夫理工大学（Lwów Polytechnic 的助理）
  - 1922–1941: 利沃夫大学（Jan Kazimierz 大学，Lwów）
  - 1941–1944: 纳粹占领期间被剥夺教职，在 Weigl 研究所靠喂养虱子为生
  - 1944–1945: 利沃夫大学复职（短暂）
- **关键荣誉**：
  - 1924: 波兰科学院成员
  - 1930: 波兰数学学会主席
  - 1936: 奥斯陆 ICM 全体大会报告
  - 1939: 波兰数学学会大奖
  - ★ 1939: 原本将获得斯大林颁发的苏联国家奖（因二战爆发未颁发）
  - ★ 多次被提名但从未获得 Fields 奖（Fields 奖 1936 年才设立，Banach 当时已 44 岁）
- **重要合作者/同事/学生**：
  - 发现者与合作者: Hugo Steinhaus（在公园长椅上"发现"了 Banach）
  - Lwów 学派核心成员: Stanisław Mazur, Stanisław Ulam, Juliusz Schauder, Władysław Orlicz, Józef Schreier
  - 苏格兰咖啡馆常客: Mazur, Ulam, Schauder, Steinhaus, Mark Kac
  - 苏联数学家: Sergei Sobolev, Andrey Kolmogorov（两人曾访问 Lwów）
  - 学生: Stanisław Mazur（最重要的合作者，苏格兰咖啡馆问题集的联合提出者）

### 关键时间线（15–20 个节点）：
- 1892: 3 月 30 日出生于克拉科夫，父亲是奥匈帝国军官，母亲未嫁——由洗衣女工抚养长大
- 1910–1914: 在 Lwów 理工大学学习工程（未正式毕业——不按学位要求走过场，只上感兴趣的课）
- 1914–1918: 一战爆发，返回克拉科夫——自学数学，这个时期完成了他最重要的基础工作
- 1916: 在克拉科夫公园长椅上，Hugo Steinhaus 偶然听到 Banach 和朋友讨论 Lebesgue 积分——这是数学史上最著名的"偶遇"
- 1919: 与 Steinhaus 合作发表第一篇论文
- 1920: 以博士论文获 Lwów 理工大学博士学位（★ 无常规博士培养——他的论文基于已发表的工作，口试委员会不得不适应他的"非标准"知识结构）
- 1922: 在 Lwów 大学取得任教资格 (habilitation) 并成为教授
- 1922: 发表博士论文，正式定义 Banach 空间——现代泛函分析的基础
- 1927: 发表 Hahn–Banach 定理的 Banach 版本（Hahn 独立发现于 1927，Banach 更早）
- 1929: 与 Steinhaus 合作创办《Studia Mathematica》— 世界上第一本泛函分析专业期刊
- 1931: 出版《Théorie des opérations linéaires》（线性算子理论）— 泛函分析的"圣经"
- 1932: 发表 Banach–Tarski 悖论（与 Alfred Tarski 合作）
- 1935: 苏格兰咖啡馆传统正式化——Mazur 购买了一本专用笔记本记录问题
- 1936: 在奥斯陆 ICM 做全体大会报告
- 1939: 二战爆发——Lwów 先被苏联占领、后被纳粹占领
- 1939–1941: 苏联占领期——Banach 受到相对优待（苏联数学家 Sobolev 和 Kolmogorov 访问了他）
- 1941–1944: 纳粹占领期——大学关闭，Banach 被剥夺教职，被迫在 Weigl 研究所工作（喂养虱子用于斑疹伤寒疫苗生产）
- 1944: 苏军解放 Lwów，Banach 与苏联数学家 Sobolev 重建联系
- 1945: 计划去克拉科夫担任雅盖隆大学数学系主任——但因肺癌于 8 月 31 日去世，享年 53 岁

### 人格特质线索：
- 自学成才，几乎没有接受过正式的数学教育——他的数学基础完全来自自学和朋友讨论
- 在咖啡馆中完成了他最重要的工作——苏格兰咖啡馆 (Kawiarnia Szkocka) 是历史上最著名的数学聚集地之一
- 苏格兰咖啡馆问题集：一本专用笔记本记录未解决问题，Mazur 承诺给解决某些问题的人提供活鹅奖励
- 性格开朗、热爱社交、热爱饮酒——与 Steinhaus 形成鲜明对比（Steinhaus 严肃保守）
- 极度不重视正式学位和程序——他的博士培养是"逆向"的：先做出一流成果，再补走程序
- 在纳粹占领期间，他被迫在一家生产斑疹伤寒疫苗的研究所工作——喂养虱子以换取生存和工作许可
- 尽管身处极端恶劣环境，他仍在战争期间继续数学研究和教学
- 经常靠波兰咖啡（他称之为"café turk"）提神，在咖啡馆讨论数学到深夜

---

## 核心贡献

| 领域 | 贡献 | 年代 |
|------|------|:--:|
| 泛函分析 | Banach 空间的公理化定义 — 现代泛函分析的基石 | 1920–1922 |
| 线性算子理论 | Banach–Steinhaus 定理（一致有界原理） | 1927 |
| 泛函分析 | Hahn–Banach 定理（线性泛函延拓定理）— 泛函分析三大基本定理之一 | 1927 |
| 泛函分析 | 开映射定理与闭图像定理 | 1929–1930 |
| 测度论 | Banach–Tarski 悖论 — 一个球可以分成有限块重新组合成两个相同的球 | 1924（1932 发表） |
| 逼近论 | Banach 空间中的逼近问题 | 1930s |
| 专著 | 《Théorie des opérations linéaires》— 泛函分析的开山经典 | 1931 |
| 期刊创建 | 《Studia Mathematica》— 世界上第一本泛函分析专业期刊 | 1929 |

### ★ 巴拿赫独有的叙事线索

1. **自学成才的天才** — Banach 从未系统接受过数学教育。他不按课程走——只在 Lwów 理工大学上自己感兴趣的课，从未取得正式工程学位。他的数学完全来自自学和朋友讨论。Steinhaus 称这次发现为"我一生中最重要的数学发现"——他发现的不是定理，而是一个人。
2. **苏格兰咖啡馆** — 这是数学史上传奇性的场景：Lwów 的苏格兰咖啡馆，Banach 和他的同事（Mazur, Ulam, Schauder 等）在烟雾缭绕中讨论数学，用铅笔在笔记本上记录问题和解答。这不是浪漫化——这是 Lwów 学派的实际工作方式。
3. **苏格兰咖啡馆问题集** — Mazur 买的一本专用笔记本，记录了 193 个未解决的问题。问题 153 的奖励是"活鹅"——1972 年当 Per Enflo 解决了该问题时，Mazur 在华沙的一次公开仪式上将一只活鹅交给了他。
4. **Banach 空间** — 这是现代泛函分析的 DNA。Banach 不是第一个使用函数空间的人（Hilbert 空间早在 1900s 就被研究了），但他是第一个给出**公理化定义**的人。Banach 空间 = 完备的赋范向量空间。这个定义简单到可以写在一行里，但它统一了整个分析领域。
5. **Banach–Tarski 悖论** — 不是悖论，而是严格定理。它揭示了选择公理（AC）的惊人后果：在三维空间中，一个球可以分解为有限块，重新组合成两个与原来大小完全相同的球。Banach 本人对这个结果的态度是冷静的——它是 AC 的一个后果，不是物理事实。
6. **战争中的数学** — Banach 在二战中度过了他最艰难的岁月。苏联占领时期受到相对优待（Kolmogorov 和 Sobolev 亲自访问了他），纳粹占领时期却被迫放弃教职，在研究所喂虱子维持生存。但他没有停止数学——战争期间他仍在秘密教学和思考。
7. **《线性算子理论》** — 1931 年出版的这本专著是泛函分析的"圣经"。它不仅是定理的合集，更是为整个泛函分析领域建立了统一语言和框架体系。
8. **53 岁肺癌去世** — Banach 在二战结束后不到一年就去世了。他有机会成为雅盖隆大学数学系主任（波兰最高学术荣誉），但疾病夺走了这个机会。他的早逝是 20 世纪数学最大的损失之一。

### 人物关系

- **Hugo Steinhaus (1887–1972)** — 发现 Banach 的伯乐，终生合作者。一个保守严肃的教授，一个开朗爱社交的天才——绝妙的互补
- **Stanisław Mazur (1905–1981)** — 最重要的合作者和学生，苏格兰咖啡馆问题集的共同提出者
- **Stanisław Ulam (1909–1984)** — Lwów 学派成员，后来在 Los Alamos 与 von Neumann 发明了 Monte Carlo 方法
- **Juliusz Schauder (1899–1943)** — 拓扑度的共同发明者（Schauder 不动点定理），1943 年被纳粹杀害
- **Alfred Tarski (1901–1983)** — Banach–Tarski 悖论的共同提出者，后来成为 20 世纪最重要的逻辑学家之一
- **Andrey Kolmogorov (1903–1987)** — 苏联占领期间访问了 Lwów，与 Banach 建立了专业联系
- **Sergei Sobolev (1908–1989)** — 苏联数学家，占领期间和战后与 Banach 保持联系
- **Władysław Orlicz (1903–1990)** — Lwów 学派核心成员，Orlicz 空间以他命名

---

## 第 1 步：建立目录

- 在 `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/` 下创建 `banach/` 子目录
- 创建 `banach/images/` 子目录

---

## 第 2 步：复制 Makefile

- 将 `grothendieck/Makefile` 复制到 `banach/Makefile`
- 将 `MAIN` 变量改为 `Stefan_Banach_zh`
- 将 `VIDEO_NAME` 变量改为 `Stefan_Banach_zh`

---

## 第 3 步：收集图片

- 从 `pages/Stefan_Banach/images.txt` 中选出 4–6 张高质量图片
- 优先级：
  1. **经典肖像（1930s Lwów 时期）** — 最具代表性的 Banach 形象
  2. 苏格兰咖啡馆（历史照片如有）— ★ 这是最具叙事感染力的场景
  3. Lwów 大学外景 或 Lwów 街景（二战前）
  4. 《Théorie des opérations linéaires》封面
  5. 波兰相关学术场景（Jagellonian 大学等）
- 下载到 `banach/images/`

---

## 第 4 步：建立时间线和叙事骨架

巴拿赫的一生可以用"波兰的三次沦陷"来标记地理与政治的伤痕：

### 生平阶段

1. **自学成才的克拉科夫少年 (1892–1916)**：私生子出身、自学数学、公园长椅上的偶遇
2. **Lwów 的黄金时代 (1916–1939)**：博士论文（Banach 空间的诞生）、苏格兰咖啡馆、《线性算子理论》
3. **战争的吞噬 (1939–1945)**：苏联占领 → 纳粹占领 → 喂虱子为生 → 战后的短暂曙光 → 53 岁肺癌去世

### 核心数学贡献（按领域排列）

| 领域 | 贡献 | 年代 |
|------|------|:--:|
| 泛函分析基础 | Banach 空间的公理化定义 | 1920–1922 |
| 线性算子理论 | Banach–Steinhaus 定理 | 1927 |
| 线性泛函 | Hahn–Banach 定理 | 1927 |
| 泛函分析 | 开映射定理、闭图像定理 | 1929–1930 |
| 测度论 | Banach–Tarski 悖论 | 1924/1932 |
| 逼近论 | Banach 空间中的逼近问题 | 1930s |
| 专著 | 《线性算子理论》 | 1931 |

### ★ 巴拿赫独有的叙事线索

1. **自学成才** — Banach 的数学完全来自自学和朋友讨论。这个事实必须作为叙事主线：他不是体制培养的产物，他是咖啡馆和印刷品中涌现的天才。
2. **苏格兰咖啡馆** — 这是 20 世纪数学最浪漫的场景——不是比喻，是真的浪漫。在烟雾缭绕的咖啡馆里，用伏特加和咖啡作燃料，Lwów 学派创建了现代泛函分析。
3. **Banach 空间的公理化定义** — 这是 Banach 最核心的贡献：将前人（Hilbert, Fréchet, Riesz 等）的工作统一为一个简洁优雅的公理体系。完备赋范向量空间——这个定义改变了分析的面貌。
4. **波兰学派** — Banach 不是一个孤立的数学家，他是整个 Lwów 学派的灵魂。这个学派在两次大战之间（1918–1939）创造了世界级的数学成果，然后被战争摧毁了。Schauder 死于纳粹之手（1943），Ulam 流亡美国，Banach 自己死于战后的肺癌。
5. **Banach–Tarski 悖论** — 作为 AC（选择公理）的惊人后果，这个"悖论"不是 Banach 的主要贡献，但它是向非数学家解释选择公理力量的最佳案例。同时要指出：Banach 本人对此结果保持冷静——它是一个数学定理，不是物理悖论。
6. **纳粹占领下的生存** — 在 Weigl 研究所喂养虱子以换取生存。这个故事不是要诉苦，而是要展现：即使在最黑暗的时期，波兰数学家仍然在秘密教学和研究。
7. **苏格兰咖啡馆问题集** — 193 个问题、活鹅的承诺，这是数学共同体精神的最高象征。

### 人物关系

- **Hugo Steinhaus** — 发现 Banach 的伯乐，终生合作者。两人性格完全相反：Steinhaus 保守严肃，Banach 开朗爱酒
- **Stanisław Mazur** — 合作伙伴，苏格兰咖啡馆问题集联合提出者
- **Stanisław Ulam** — Lwów 学派成员，后来 Monte Carlo 方法的共同发明者
- **Juliusz Schauder** — 拓扑度的发明者，1943 年被纳粹杀害——Lwów 学派悲剧的象征
- **Alfred Tarski** — Banach–Tarski 悖论的共同提出者
- **Andrey Kolmogorov** — 苏联占领期访客，对 Banach 工作有深厚敬意
- **Sergei Sobolev** — 苏联数学家，与 Banach 在占领期间和战后保持联系

---

## 第 5 步：设计配色方案

- 巴拿赫的气质关键词：**温暖、醇厚、波兰土地的色调、咖啡馆的暗金光泽、分析的严谨与深度**
- **建议配色：深琥珀（波兰蜂蜜酒）+ 深松绿（波兰森林）+ 象牙纸**— 咖啡馆的温暖 + 波兰自然 + 泛函分析论文的象牙白

> ⚠️ 已有配色回顾（避免撞色）：
> - Hilbert：普鲁士蓝+金 | Grothendieck：深靛+金 | Noether：深紫罗兰+暗玫瑰金
> - Riemann：墨绿+银灰 | von Neumann：深黑+电路绿 | Turing：深黑+暗青+冷银
> - Kolmogorov：深松绿+古铜金 | Serre：勃艮第红+象牙暖金 | Weyl：深琥珀金+星夜紫
> - Weil：勃艮第深红+石板暖灰 | Gödel：深勃艮第+古金+暗灰

- Banach 配色方案（必须区分于 Kolmogorov 和 Weyl）：
  - **主色 (coverprimary)**：**深琥珀棕** — 波兰蜂蜜酒的醇厚、苏格兰咖啡馆的暖木调、旧书的暗金色泽。区别于 Kolmogorov 的松绿（更冷），也不同于 Weyl 的琥珀金（更亮）
  - **强调色 (coveraccent)**：**象牙米白** — 泛函分析论文的象牙纸色、咖啡馆的晨光
  - 四个分类色，对应 Banach 的四大支柱：
    - **badgespace** (Banach 空间/泛函分析) — 深松绿 `#2E5A47`（分析的严谨深度，致敬波兰森林）
    - **badgetheorem** (三大基本定理) — 暗金铜 `#B8860B`（定理的经典光泽）
    - **badgecafe** (Lwów 学派/苏格兰咖啡馆) — 暖琥珀 `#C77A33`（咖啡与伏特加的色调）
    - **badgewarsaw** (波兰/战争) — 暗红陶 `#A52A2A`（波兰国旗中的红色，但不张扬）
  - 各面板色：amberpanel(暖琥珀)/greenpanel(深松绿)/goldpanel(暗金铜)/redpanel(暗红陶)/graypanel(象牙灰)

---

## 第 6 步：规划幻灯片序列

Banach 的故事有三条主线：泛函分析的创立 + Lwów 学派的传奇 + 战争的毁灭，建议 17 页：

```
00  OpenMath 项目首页（从 cover 模板 \input，见 §3.4）

=== 封面与总览 ===
01  封面 — 《巴拿赫：泛函分析的奠基人》 / Stefan Banach 1892–1945 + 四色badge
02  为什么巴拿赫改变了分析的面貌 — Banach 空间 · 三大基本定理 · 苏格兰咖啡馆 · 波兰学派的灵魂

=== 自学成才 ===
03  克拉科夫的私生子 (1892–1916) — 由洗衣女工抚养 · 自学数学 · 一战逃回克拉科夫
04  公园长椅上的偶遇 (1916) — Steinhaus 发现了 Banach — "我一生中最重要的数学发现"

=== 泛函分析的诞生 ===
05  Banach 空间 (1920–1922) — 完备赋范向量空间的公理化定义 — 泛函分析的基石
06  三大基本定理 — Hahn–Banach · Banach–Steinhaus · 开映射定理/闭图像定理

=== 苏格兰咖啡馆 ===
07  苏格兰咖啡馆与 Lwów 学派 — 伏特加、咖啡与数学 — 20 世纪最著名的数学聚集地
08  苏格兰咖啡馆问题集 — 193 个未解决问题 · 活鹅的承诺 · 数学共同体精神

=== 专著与悖论 ===
09  《线性算子理论》(1931) — 泛函分析的"圣经"，统一了整片数学疆域
10  Banach–Tarski 悖论 — 选择公理的惊人后果 — 一个球变成两个

=== 战争岁月 ===
11  1939–1941: 苏联占领 — Sobolev 和 Kolmogorov 的访问 · 在学术真空中的坚持
12  1941–1944: 纳粹占领 — 大学关闭 · 在 Weigl 研究所喂虱子 · 秘密教学
13  被战争摧毁的学派 — Schauder 死于纳粹之手 (1943) · Ulam 流亡 · Lwów 的终结

=== 终章 ===
14  战后的最后一年 (1944–1945) — 雅盖隆大学的召唤 · 53 岁肺癌去世
15  巴拿赫的遗产 — Banach 空间是整个现代泛函分析的 DNA · 从 PDE 到量子力学的每一处

=== 结尾 ===
16  升起海水 — 在咖啡馆里，一群波兰数学家创建了现代分析最基本的语言
17  结束页 — "他说：给我一个完备的赋范向量空间，我把它命名为家。"
```

> **可以微调。** 征求我的意见后再开始写代码。

---

## 第 7 步：编写 Beamer 源码

- 文件名：`/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/Stefan_Banach/Stefan_Banach_zh.tex`
- 完全参照已有模板的代码结构
- 每页用 `\newcommand{\xxxslide}{% ... }` 定义

### 关键要求

- **每写完一页立即编译 (`make clean && make`)，不等待全部写完**
- 编译失败立即修复，不要跳过
- 中文正文，英文术语和公式保留原文
- ★ **泛函分析的三大基本定理必须准确表述**：Hahn–Banach、Banach–Steinhaus（一致有界原理）、开映射定理/闭图像定理

---

## 第 8 步：布局检查 ★★★

> 同已有模板，每写完一页检查溢出。

---

## 第 9 步：史实审查 + 术语审查

### 巴拿赫特有的史实陷阱（★ 必须逐页扫描）

| 陷阱类型 | 巴拿赫特有的高危点 |
|---------|---------------------|
| **私生子出身** | Banach 的父亲是奥匈帝国军官 Stefan Greczek，母亲 Katarzyna Banach 是未婚洗衣女工。Banach 随母姓。不要说他"被父亲抛弃"——父亲提供了抚养费并送他上学。但 Banach 确实由祖母/养母抚养长大。 |
| **自学而非正式教育** | ★ Banach 从未取得 Lwów 理工大学正式工程学位。他不按课程走，只上感兴趣的课。不要说"Banach 毕业于…" |
| **博士学位的非常规路径** | 1920 年获博士学位，但他的"博士论文"基于已发表的成果，他从未进行过常规的博士培养。口试委员会不得不适应他的"非标准"知识结构。不要说他"完成了博士学业"。 |
| **公园长椅偶遇** | Steinhaus 在 Planty 公园听到 Banach 和朋友讨论 Lebesgue 积分，这是数学史上最著名的偶遇。但要注意：当时 Banach 不是"无名之辈"——他已经在自学研究中做出了重要发现。这是"被发现"而非"被创造"。 |
| **Hahn–Banach 定理的命名** | ★ 定理以 Hahn 和 Banach 命名，但两人独立发现。Hahn 的版本 1927 年发表，Banach 的版本更早（在博士论文中就有思想萌芽）。不要写"Banach 发现了 Hahn–Banach 定理"——写"Banach 独立证明了线性泛函延拓定理，后与 Hahn 的工作合称 Hahn–Banach 定理"。 |
| **Banach–Tarski 悖论的时间** | 定理是 1924 年证明的，但直到 1932 年才在 Fundamenta Mathematicae 发表。不要混淆发现年和发表年。 |
| **纳粹占领期间的"虱子喂养"** | ★ Banach 在 Rudolf Weigl 的斑疹伤寒疫苗研究所工作，具体工作是喂养感染斑疹伤寒的虱子（虱子被装在绑在腿上的小盒子里，以人体血液喂养）。这是一种极端艰苦但保护了他不被送往集中营的工作。不要轻描淡写——这确实是极其痛苦的经历。 |
| **Schauder 的死因** | Schauder 是犹太人，1943 年在 Lwów 被纳粹盖世太保杀害。这是 Lwów 学派被战争摧毁的核心悲剧事件。不要在叙事中忽略 Schauder。 |
| **苏联占领的评价** | 苏联占领 Lwów 期间，Banach 受到了相对优待（苏联数学家 Sobolev 和 Kolmogorov 访问了他）。但这不意味着他是"亲苏联"的——这是生存策略。叙事要保持中立。 |
| **Lwów 的地理归属** | 战前 Lwów 属于波兰第二共和国。战后划归苏联（今乌克兰利沃夫）。不要在 Beamer 中说 "Lwów 在乌克兰" 来描述战前时期——当时它在波兰。 |

### 术语清单

| 英文 | 正确中文译法 | 风险点 |
|------|-------------|--------|
| Banach space | Banach 空间 | 完备赋范向量空间 |
| normed vector space | 赋范向量空间 | — |
| Hahn–Banach theorem | Hahn–Banach 定理 | 不称"Banach 延拓定理" |
| Banach–Steinhaus theorem | Banach–Steinhaus 定理 | 也称一致有界原理 (uniform boundedness principle) |
| open mapping theorem | 开映射定理 | Banach 空间版 |
| closed graph theorem | 闭图像定理 | — |
| Banach–Tarski paradox | Banach–Tarski 悖论 | 不是真正的悖论，是严格定理 |
| axiom of choice (AC) | 选择公理 | — |
| Scottish Café | 苏格兰咖啡馆 | 保留英文，Kawiarnia Szkocka (波兰语) |
| Scottish Book | 苏格兰咖啡馆问题集 | — |
| Théorie des opérations linéaires | 《线性算子理论》 | 法文原版书名 + 中文注释 |
| Studia Mathematica | 《数学研究》 | 泛函分析第一本专业期刊 |
| typhus vaccine | 斑疹伤寒疫苗 | Weigl 研究所的产品 |

### 通用陷阱

| 陷阱类型 | 检查点 |
|---------|--------|
| **"第一部"叙事** | "第一部泛函分析专著"——确认是否属实。更准确的表述："泛函分析领域最具奠基性的经典专著" |
| **"发现"的夸大** | Steinhaus "发现"了 Banach，但不要浪漫化过度——Banach 当时已经是自学成才的数学研究者，不是"零基础"的天才 |
| **战争叙事过重** | 战争是 Banach 故事的背景，但不是他的数学贡献。叙事比例：数学60%+学派20%+战争20% |
| **伪引语** | 苏格兰咖啡馆没有录音——大部分故事来自 Ulam 和 Steinhaus 的回忆录。使用间接引语 |
| **地理精确性** | Lwów 的战前/战时/战后归属不同。只说"波兰的 Lwów"或"今乌克兰利沃夫"而不混淆时代 |
| **公理化定义的归属** | ★ 不要把 "Banach 空间"定义为"Hilbert 空间的推广"——虽然都对，但 Banach 的公理化定义是独立于 Hilbert 空间提出的，两者是平行发展的 |

---

## 第 13 步：Wikipedia 本地文档终审（★ 提交前必做）

### 终审执行流程

```
1. 打开 pages/Stefan_Banach/page.md，从头到尾逐段阅读全文
2. 同时打开 Stefan_Banach_zh.tex 源码，逐页对照
3. 发现不一致 → 标注优先级（P0/P1/P2）
4. 全部扫描完毕 → 先修复所有 P0，再评估 P1，P2 可选
5. 修复后重新编译 → 确认零错误
```

### ⚠️ Banach 特有的终审高危点

| 高危点 | 为什么高危 | 终审时如何检查 |
|--------|---------|--------------|
| **博士学位的非常规路径** | 容易写成常规博士叙事 | page.md 搜索 "doctorate" "habilitation" |
| **公园偶遇的时间地点** | Planty 公园、1916 年 | page.md 搜索 "Planty" "Steinhaus overheard" |
| **Hahn–Banach 的优先权** | Hahn 版本命名但 Banach 更早 | page.md 搜索 "Hahn" "Banach" "extension" |
| **纳粹时期的生存细节** | "虱子喂养"的具体描述 | page.md 搜索 "Weigl" "lice" "typhus" |
| **Schauder 的死因** | 1943 年被纳粹杀害 | page.md 搜索 "Schauder" "murdered" |
| **Lwów 战后归属** | 划归苏联 | page.md 搜索 "annexed" "Soviet" |
| **苏格兰咖啡馆问题集** | 193 个问题的确切数量 | page.md 搜索 "Scottish Book" "193" |

### 优先级定义

| 优先级 | 定义 | Banach 实际案例 |
|:--:|------|------|
| 🔴 P0 | **事实错误** | "Banach 毕业于 Lwów 理工大学"（从未正式毕业）；"Banach 发现了 Hahn–Banach 定理"（优先权叙事有误导） |
| 🟡 P1 | **来源存疑/捏造** | 无法验证的咖啡馆引语；公园偶遇的过度渲染 |
| 🟢 P2 | **重要遗漏** | 苏联占领期的 Sobolev 和 Kolmogorov 访问；Orlicz 空间 |
| ⚪ P3 | **可选补充** | 活鹅奖励的完整故事；Banach 的婚姻与家庭细节 |

---

## 音乐选择

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`

巴拿赫的气质：**温暖、醇厚、波兰土地的朴实、咖啡馆的亲密感、战争的伤痕** — 避免过于宏大的交响乐，苏格兰咖啡馆不适合管弦乐队尺度。

**推荐曲目（精选自 music_audio/curated_tracks.md）：**

| 优先级 | 曲目 | 来源 | 本地路径 | 理由 |
|:--:|------|------|------|------|
| ★★★ | Nostalgia | alex-productions | `music_audio/alex-productions/86-5ETNuoDcBg4-Nostalgia.wav` | 怀旧温和，Lwów 咖啡馆的黄金时代 |
| ★★★ | With Me | alex-productions | `music_audio/alex-productions/83-DXAblXgCK-k-With-Me.wav` | 温和稳定，人物传记段落 |
| ★★ | Tragedy | alex-productions | `music_audio/alex-productions/80-K5f65-22sY4-Tragedy.wav` | 深色戏剧性，战争伤痕与 Schauder 之死 |
| ★ | SEA | alex-productions | `music_audio/alex-productions/92-WEqfdRXU3IU-SEA.wav` | 流动平稳，泛函分析的连续叙事 |

**操作**：复制选定的 `.wav` 到 `Stefan_Banach/` 目录，`make video` 自动混入。

---

## 关键参考文件清单

| 文件 | 用途 |
|------|------|
| `mathematician/presentations/数学家立传工作指南.md` | 完整操作手册 |
| `mathematician/pages/Stefan_Banach/page.md` | Banach Wikipedia 正文 |
| `mathematician/pages/Stefan_Banach/metadata.json` | Banach Wikidata 元数据 |
| `mathematician/pages/Stefan_Banach/images.txt` | 图片 URL 清单 |
| `mathematician/presentations/grothendieck/Alexander_Grothendieck_zh.tex` | Grothendieck 完整源码 |
| `mathematician/presentations/riemann/Bernhard_Riemann_zh.tex` | Riemann 完整源码 |
| `mathematician/presentations/kolmogorov/Andrey_Kolmogorov_zh.tex` | Kolmogorov 完整源码 |
| `mathematician/presentations/hilbert/David_Hilbert_zh.tex` | Hilbert 完整源码 |

---

> **开始执行。每完成一步向我汇报。**
>
> **特别提醒：**
> 1. Banach 的独特性不在于"他发现了什么定理"——而在于他**创建了泛函分析的语言本身**
> 2. 苏格兰咖啡馆不是修饰——它是数学史最真实、最浪漫的工作场景
> 3. 不要写成"苦难叙事"——Lwów 黄金时代的欢乐和创造力应该和战争悲剧同等篇幅
> 4. Banach 空间的定义简单到可以写在一页幻灯片里——但它是整个现代分析的基石
> 5. Schauder 的死亡是必要的叙事节点——它让战争的毁灭力具体化
> 6. 活鹅是真实的——这不需要过度渲染，它本身就很有力量
> 7. 三大基本定理每一定理都需要一句话直观解释——不要只列名字
> 8. 结尾主题句：**"在咖啡馆的烟雾中，一群波兰数学家发明了现代分析的语言。"**
