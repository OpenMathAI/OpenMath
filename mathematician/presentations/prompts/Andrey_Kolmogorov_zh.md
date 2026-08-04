# 柯尔莫哥洛夫 (Andrey Kolmogorov) 立传提示词

> 本提示词严格遵循 [数学家立传工作指南.md](./数学家立传工作指南.md)，以 Grothendieck、Riemann、Hilbert、Serre、Noether 成品为参考模板，为柯尔莫哥洛夫制作 Beamer 演示文稿。
> 直接复制本文件内容到新对话中使用。

---

## 背景信息

- **目标数学家**: Andrey Kolmogorov (1903–1987)
- **气质关键词**: **全才、深邃、概率之父、苏联数学的灯塔、最后的百科全书式数学家之一**
- **Wikipedia 页面已下载**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Andrey_Kolmogorov/`
  - `page.md` — 正文 Markdown (~36K)
  - `metadata.json` — Wikidata 元数据
  - `images.txt` — 图片 URL 清单
- **参考模板**:
  - `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/grothendieck/Alexander_Grothendieck_zh.tex` — Grothendieck 完整源码（教皇气质）
  - `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/riemann/Bernhard_Riemann_zh.tex` — Riemann 完整源码（克制天才气质）
  - `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/hilbert/David_Hilbert_zh.tex` — Hilbert 完整源码（王者气质）
  - `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/serre/Jean_Pierre_Serre_zh.tex` — Serre 完整源码（优雅气质）
  - `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/noether/Emmy_Noether_zh.tex` — Noether 完整源码（开创者气质）
  - `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/grothendieck/Makefile` — 构建脚本（直接复制）
- **操作指南**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/数学家立传工作指南.md`

---

## 你的任务

按照 [数学家立传工作指南.md](./数学家立传工作指南.md) 第十一节「推荐制作流程」的步骤，依次完成。**每完成一步向我汇报进度**，遇到歧义时先征求我的意见再继续。

---

## 第 0 步：确认 Wikipedia 页面已就绪

- 读取 `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Andrey_Kolmogorov/metadata.json` 及 `page.md`
- 输出以下信息供我校验：
  - **生卒日期**：1903-04-25 ~ 1987-10-20，享年 84 岁
  - **国籍**：沙俄 → 苏联
  - **出生地**：Tambov（坦波夫），母亲难产去世，由姨妈抚养长大
  - **博士导师**：Nikolai Luzin（鲁金）
  - **博士论文**：1929，莫斯科大学
  - **主要任职机构**：莫斯科大学终身教授（1931–1987）
  - **关键荣誉**：
    - 1941: 斯大林奖
    - 1962: Balzan 奖
    - 1964: 英国皇家学会外籍院士
    - 1965: 列宁奖
    - 1980: Wolf 数学奖
    - 1986: Lobachevsky 奖
    - 社会主义劳动英雄
     - 多次获得列宁勋章
  - **知名学生**（page.md 列 21 位博士生）：Gelfand, Arnold, Sinai, Dynkin, Levin, Martin-Löf, Nikolsky, Prokhorov, Shiryaev, Gnedenko, Obukhov, Uspensky, Yaglom, Monin, Vitushkin 等
  - **Wikipedia 正文中提取出的关键时间线**（按年份列出 15–20 个关键节点）：
    - 1903: 出生于 Tambov，母亲去世，由姨母抚养
    - 1910: 被姨母收养，移居莫斯科
    - 1920: 高中毕业，同时进入莫斯科大学和门捷列夫化工学院
    - 1922: 年仅 19 岁，构造了几乎处处发散的傅里叶级数——一战成名
    - 1925: 莫斯科大学毕业；发表直觉主义逻辑论文"排中律原理"
    - 1929: 获博士学位；与 Alexandrov 结为终身挚友
    - 1930: 首次出国访问——哥廷根、慕尼黑、巴黎，接触 Courant, Weyl, Landau
    - 1931: 任莫斯科大学教授
    - 1933: 出版《概率论基础》(Grundbegriffe der Wahrscheinlichkeitsrechnung)——概率论公理化的里程碑
    - 1935: 莫斯科大学概率论系首任系主任
    - 1936: "鲁金事件"——Kolmogorov 参与指控导师 Luzin（争议性事件）
    - 1938: 建立平稳随机过程的平滑与预测理论（冷战期间有重大军事应用）
    - 1939: 当选苏联科学院院士
    - 1941: 开始湍流理论研究；二战期间用统计理论优化炮兵射击和阻拦气球部署
    - 1954: 在 ICM 上首次提出 KAM 定理（经典力学的稳定性理论）
    - 1957: 与 Arnold 合作解决了 Hilbert 第十三问题的特定解释
    - 1960s: 开创算法复杂性理论（Kolmogorov 复杂性）
    - 1971: 参与海洋学考察（Dmitri Mendeleev 号）
    - 1987: 在莫斯科逝世，葬于新圣女公墓
  - **人格特质线索**：
    - 博学多才——大学时同时研究数学和历史，第一篇论文是关于 15–16 世纪诺夫哥罗德土地制度的
    - 五岁就"编辑"了校刊的数学栏目；六岁发现了奇数求和的规律
    - 与 Pavel Alexandrov 维持了终身的深厚友谊（多位研究者认为两人有过亲密关系）
    - 热爱教学，不仅教大学生，也积极投身天才儿童教育（文学、音乐、数学）
    - Vladimir Arnold 对他的评价："Kolmogorov – Poincaré – Gauss – Euler – Newton，这五个人将我们与科学的源头连接起来。"
    - 名言："每个数学家都认为自己领先于他人。他们不在公开场合说这句话，只是因为他们都是聪明人。"
    - 在"鲁金事件"中参与指控自己导师的行为一直是争议焦点——苏联时代的道德复杂性

### 与其他已立传数学家的关系网络

- **Hilbert** — Hilbert 第十三问题被 Kolmogorov 和 Arnold 解决（1957）；Kolmogorov 概率论公理化受 Hilbert 第六问题影响
- **Riemann** — Kolmogorov 在湍流理论中使用了与 Riemann 几何完全不同的数学框架（统计与动力系统）
- **Noether** — Kolmogorov 与 Alexandroff 的友谊（Alexandroff 也曾与 Noether 密切合作）
- **Grothendieck** — 不是直接关系，但 Kolmogorov 复杂性的思想影响了算法信息论，后者又与范畴论有交集
- **Luzin** — 博士导师，但关系因"鲁金事件"而蒙上阴影
- **Alexandrov** — 终身挚友，同在 Luzin 门下
- **Arnold** — 最杰出的学生之一，KAM 定理的共同创立者
- **von Neumann** — 同时代的全才型对手，都在概率论和动力系统领域有基础性贡献

---

## 第 1 步：建立目录

- 在 `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/` 下创建 `kolmogorov/` 子目录
- 创建 `kolmogorov/images/` 子目录

---

## 第 2 步：复制 Makefile

- 将 `grothendieck/Makefile` 复制到 `kolmogorov/Makefile`
- 将 `MAIN` 变量改为 `Andrey_Kolmogorov_zh`
- 将 `VIDEO_NAME` 变量改为 `Andrey_Kolmogorov_zh`

---

## 第 3 步：收集图片

- 从 `pages/Andrey_Kolmogorov/images.txt` 中选出 4–6 张高质量图片
- 优先选择：
  1. **经典肖像照** — Kolmogorov 中年或晚年经典肖像
  2. 莫斯科大学主楼（他的学术家园）
  3. 《概率论基础》(Grundbegriffe) 封面
  4. 与 Alexandrov 的合影（如有）
  5. Kolmogorov 演讲场景（Tallinn, 1973）
- 下载到 `kolmogorov/images/`
- ★ **特殊要求**：Kolmogorov 的 Wikipedia 图片数量有限。如有需要，可从其他公共来源补充肖像

---

## 第 4 步：建立时间线和叙事骨架

Kolmogorov 的一生是一个"全才叙事"——他不是某一个领域的专家，而是**概率论、湍流、动力系统、逻辑、复杂性理论**等多个领域的奠基者。他的故事核心是：**一个人如何在一个极权时代，同时成为多个数学分支的奠基人。**

### 生平阶段

1. **早慧天才与莫斯科求学 (1903–1931)**：母亲早逝、姨妈抚养、5 岁编辑校刊数学栏、6 岁发现奇数求和规律、19 岁构造发散的傅里叶级数、师从 Luzin、获博士学位、首次出国访问哥廷根
2. **概率论公理化与战争年代 (1931–1945)**：1933 年出版《概率论基础》——概率论的欧几里得《几何原本》、二战期间用统计学帮助苏联防御莫斯科
3. **动力系统、湍流与 KAM 定理 (1941–1960)**：1941 年开始湍流研究、1954 年提出 KAM 定理、1957 年解决 Hilbert 第十三问题
4. **算法复杂性、教育与国际声望 (1960–1987)**：1960s 开创 Kolmogorov 复杂性理论、天才儿童教育、获得 Wolf 奖等最高荣誉、84 岁逝世

### 核心数学贡献

| 领域 | 贡献 | 年代 |
|------|------|:--:|
| 概率论 | 概率论公理化 (Grundbegriffe) — 现代概率论的《几何原本》 | 1933 |
| 傅里叶分析 | 构造几乎处处发散的傅里叶级数 (19岁!) | 1922 |
| 数理逻辑 | 直觉主义逻辑的排中律原理；Brouwer–Heyting–Kolmogorov 解释 | 1925 |
| 拓扑学 | Kolmogorov 空间 (T₀ 分离性) | 1920s–1930s |
| 随机过程 | Chapman–Kolmogorov 方程；平稳过程的预测理论 | 1931–1938 |
| 湍流 | Kolmogorov 湍流理论 (1941)，Kolmogorov 微尺度 | 1941–1960s |
| 经典力学 | KAM 定理 — 动力系统稳定性的基石 | 1954 |
| 函数论 | Hilbert 第十三问题的解决 (与 Arnold 合作) | 1957 |
| 算法信息论 | Kolmogorov 复杂性 — 算法信息论的奠基 | 1960s |
| 统计学 | Kolmogorov–Smirnov 检验 | 1930s |

### ★ Kolmogorov 独有的叙事线索

1. **概率论的欧几里得** — 在 Kolmogorov 之前，概率论是哲学的附庸。他的 1933 年《概率论基础》用测度论将概率论变成了真正的数学学科。这是 20 世纪数学最重要的公理化成就之一。
2. **全才的广度** — 从概率论到湍流，从逻辑到力学，从信息论到海洋学——Kolmogorov 是 Poincaré、von Neumann 之后少有的百科全书式数学家。
3. **19 岁的天才** — 1922 年，19 岁的 Kolmogorov 构造了几乎处处发散的傅里叶级数，推翻了当时的主流猜想。这个结果让他一夜之间成为国际数学界关注的对象。
4. **鲁金事件的阴影** — 1936 年，Kolmogorov 参与指控自己的导师 Luzin。这是一段道德上灰色的历史。2013 年俄罗斯数学史家 Kutateladze 的结论是：学生们出于个人恩怨主动发起指控。这个事件不需要过度渲染，但也不能回避。
5. **数学教育的热情** — Kolmogorov 培养出数十位博士生（Gelfand, Arnold, Sinai 等），还投入大量精力于中小学天才儿童教育。他不仅教大学生，也积极参与文学、音乐、数学方向的天才儿童实验学校。
6. **苏联时代的科学家** — Kolmogorov 在斯大林时期、二战、冷战、后斯大林解冻中始终保持学术产出。军功（炮兵射击优化、阻拦气球部署）和纯粹数学交织。
7. **Kolmogorov 复杂性** — 1960 年代，他独立于 Solomonoff 和 Chaitin 提出了算法复杂性的概念。今天，Kolmogorov 复杂性是理论计算机科学的基石之一。
8. **湍流的未竟之业** — 湍流是流体力学中最深刻的问题之一。Kolmogorov 于 1941 年开始发表湍流研究，其理论至今仍是该领域的核心框架，但湍流的完整解答仍未出现。

### 人物关系

- **Nikolai Luzin (导师)** — 莫斯科数学学派的创始人之一，但"鲁金事件"使关系复杂化
- **Pavel Alexandrov (终身挚友)** — 同门师兄，维持了一生的深厚友谊
- **Aleksandr Khinchin** — 早期概率论合作者
- **Vladimir Arnold (学生)** — 最杰出的学生之一，KAM 定理和 Hilbert 第十三问题的合作者
- **Israel Gelfand (学生)** — 泛函分析大师
- **Yakov Sinai (学生)** — 动力系统与遍历理论大师，Abel 奖得主
- **Hermann Weyl** — 1930 年哥廷根访问期间的学术交流对象
- **Richard Courant** — 同上的哥廷根访问对象

---

## 第 5 步：设计配色方案

- Kolmogorov 的气质关键词：**深邃、理性、广度、苏联学术的厚重、概率与确定性的张力**
- **建议配色：深松绿 + 古铜金 + 大地灰**（概率论的理性 + 苏联学术的厚重 + 湍流与自然的力量）
- **需要与已有的配色区分**：
  - Hilbert：普鲁士蓝 + 金
  - Grothendieck：深靛 + 金
  - Serre：勃艮第红 + 象牙暖金
  - Noether：深紫罗兰 + 暗玫瑰金
  - Riemann：墨绿 + 银灰（需确保 Kolmogorov 的松绿与 Riemann 的墨绿有足够区分度）
- 请给出完整的 `\definecolor` 方案：
  - **主色 (coverprimary)**：**深松绿** (#1B4D3E 或相近) — 理性、深沉，象征概率论中从随机中寻找确定性的精神
  - **强调色 (coveraccent)**：**古铜金** (#C49A2A 或相近) — 温暖而有历史厚重感，象征莫斯科大学的金色穹顶和苏联时代的学术尊严
  - 四个分类色，对应 Kolmogorov 的四大支柱：
    - **badgeprob** (概率论/随机过程) — 深蓝灰
    - **badgedynam** (动力系统/湍流/KAM) — 暖铜
    - **badgelogic** (逻辑/复杂性/信息论) — 紫罗兰
    - **badgeanaly** (分析/拓扑/函数论) — 深松绿（与主色呼应但略浅）
  - 各面板色 (purplepanel/amberpanel/greenpanel/bluepanel/goldpanel/graypanel)

---

## 第 6 步：规划幻灯片序列

Kolmogorov 的内容广度极大，建议约 19 页：

```
00  OpenMath 项目首页（从 cover 模板 \input，见 §3.4）

=== 人物篇 ===
01  封面 — 《柯尔莫哥洛夫：概率之王》 / Andrey Kolmogorov 1903–1987 + 四色badge
02  为什么他是不可替代的 — 全才广度：概率公理化 + 湍流 + KAM + 复杂性

=== 早年 ===
03  早慧天才 (1903–1925) — 母亲早逝、五岁编辑数学栏目、六岁发现奇数求和、19岁一战成名

=== 概率论革命 ===
04  概率论公理化 (1933) — 《概率论基础》，用测度论为概率建立了严格数学基础
05  随机过程与预测理论 (1931–1938) — Chapman–Kolmogorov 方程，冷战的数学武器

=== 数学物理 ===
06  湍流理论 (1941) — 经典物理最后一个未解问题，Kolmogorov 微尺度
07  KAM 定理 (1954) — 为什么太阳系是稳定的？动力系统的里程碑

=== 广度与深度 ===
08  逻辑与拓扑 (1925–1930s) — 直觉主义逻辑 + Kolmogorov 空间
09  Hilbert 第十三问题 (1957) — 与 Arnold 合作，函数论的突破

=== 计算机科学 ===
10  Kolmogorov 复杂性 (1960s) — 算法信息论的奠基，随机性的数学定义

=== 教育家 ===
11  数学教育家 — 数十位博士生 + 天才儿童学校，数学之美的传递者
=== 历史阴影 ===
12  鲁金事件 (1936) — 一位天才与他的导师之间的道德复杂性

=== 遗产 ===
13  Arnold 的评价 — "Kolmogorov – Poincaré – Gauss – Euler – Newton"
14  荣誉满身 — Wolf 奖 · Lenin 奖 · Balzan 奖 · 多次列宁勋章

=== 结尾 ===
15  升起海水 — Kolmogorov 证明了：即使在最无序的世界里，数学也能找到规律
16  结束页 — 主题句：他用公理驯服了随机。
```

> **可以微调。** 征求我的意见后再开始写代码。

---

## 第 7 步：编写 Beamer 源码

- 文件名：`/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/Andrey_Kolmogorov/Andrey_Kolmogorov_zh.tex`
- 完全参照已有模板的代码结构
- 每页用 `\newcommand{\xxxslide}{% ... }` 定义

### 关键要求

- **每写完一页立即编译 (`make clean && make`)，不等待全部写完**
- 编译失败立即修复，不要跳过
- 中文正文，英文术语和公式保留原文

---

## 第 8 步：布局检查 ★★★

同已有模板，每写完一页检查溢出。

---

## 第 9 步：史实审查 + 术语审查

### Kolmogorov 特有的史实陷阱（★ 必须逐页扫描）

| 陷阱类型 | Kolmogorov 特有的高危点 |
|---------|---------------------|
| **概率论公理化的"唯一性"** | ★ Kolmogorov 的概率公理化是最有影响力的，但不是唯一的。在他之前，Bernstein、von Mises 等人也有公理化尝试。不要写"第一个人"。正确表述："给出了被广泛接受的概率论公理化体系。" |
| **"概率论之父"** | 这个称号历史上常用于 Pierre-Simon Laplace。Kolmogorov 更适合称为"现代概率论的奠基人"或"概率论公理化的完成者"。 |
| **KAM 定理的归属** | Kolmogorov 1954 年首次提出核心思想，Arnold 和 Moser 分别独立发展和完善。不要说"Kolmogorov 证明了 KAM 定理"——他提出了框架，完整证明由三人共同完成。 |
| **Hilbert 第十三问题的"解决"** | Kolmogorov 和 Arnold 解决的是 Hilbert 第十三问题的**一种解释**。该问题是否"完全解决"在数学史上仍有讨论。用"给出了重要进展"或"在特定解释下解决"更准确。 |
| **鲁金事件** | 这是一个道德上灰色的事件。不要用"背叛"或"被迫"等确定性的道德判断。客观描述："Kolmogorov 参与了对导师 Luzin 的指控。2013 年 Kutateladze 的研究结论认为指控出于个人恩怨。" |
| **Kolmogorov 复杂性** | 1960 年代，Solomonoff (1960)，Kolmogorov (1965)，Chaitin (1966) 几乎同时独立提出算法复杂性概念。不要写"Kolmogorov 是第一个"。用"独立于 Solomonoff 和 Chaitin"更为公允。 |
| **湍流"解决"** | 湍流仍然是未完全解决的问题。Kolmogorov 的 1941 年理论是最重要的框架之一，但不是"解答"。 |
| **湍流"最后边疆"论** | ★ page.md 中无 Feynman 引语。页面上仅说 "Later, Kolmogorov focused his research on turbulence, beginning his publications in 1941"。不要添加外部引语。 |
| **"最后的百科全书式数学家"** | 这个称号也常用于 Poincaré 和 von Neumann。避免排他性断言。用"20 世纪最具广度的数学家之一"更稳。 |
| **★ 博士生数量** | ★ page.md 仅列 21 位博士生 + Tony Hoare。不要说"60+ 位"。用"数十位"或列具体名单。 |
| **★ 列宁勋章数量** | ★ metadata 中 "Order of Lenin" 出现 12 次（非 7 枚）。不要给出精确数字，用"多次获得列宁勋章"。 |
| **★ 引语来源** | ★ page.md 中仅有的引语是 Arnold 评价和 Kolmogorov 自述。不要添加任何无法在 page.md 中逐字验证的引语。 |
| **★ "几何原本"类比** | ★ page.md 中不存在此类比。不要将《概率论基础》比作概率论的《几何原本》——这是润色而非事实。 |

### 术语清单

| 英文 | 正确中文译法 | 风险点 |
|------|-------------|--------|
| Foundations of the Theory of Probability | 《概率论基础》 | 德文原著名：Grundbegriffe der Wahrscheinlichkeitsrechnung |
| Kolmogorov complexity | Kolmogorov 复杂性 | 也译为"柯尔莫哥洛夫复杂度" |
| KAM theorem | KAM 定理 | Kolmogorov–Arnold–Moser，三人并列，不分先后 |
| Chapman–Kolmogorov equation | Chapman–Kolmogorov 方程 | Chapman 是英国数学家 Sydney Chapman |
| turbulence | 湍流 | 注意与"紊流"的区分（中文学术界一般用"湍流"） |
| Grundbegriffe | 基本概念 | 德文，不要翻译成"基础"（那是 Grundlage） |
| intuitionistic logic | 直觉主义逻辑 | 不要与"直观逻辑"混淆 |
| Luzin Affair | 鲁金事件 | 保留专有名词 |
| Kolmogorov microscales | Kolmogorov 微尺度 | 流体力学专有名词 |
| Kolmogorov–Smirnov test | Kolmogorov–Smirnov 检验 | Smirnov 是 Nikolai Smirnov |

### 通用陷阱

| 陷阱类型 | 检查点 |
|---------|--------|
| "第一次/第一个"断言 | 避免"第一个公理化概率论"→"给出了被广泛接受的概率论公理化体系" |
| 学科归属 | Kolmogorov 复杂性常见于计算机科学，但 Kolmogorov 本人是数学家。这是一个跨领域贡献，不要只说"计算机科学" |
| 苏联意识形态 | 不要过度渲染冷战意识形态对立。聚焦数学本身，政治背景客观描述 |

---

## 第 10–13 步：同已有模板

（布局微调、OpenMath首页、最终编译、音乐选择）

### 音乐选择

> **音乐库**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/` — 详见 `curated_tracks.md`

Kolmogorov 的气质：**深邃、理性、广度、力量与秩序** — 宏大而理性的交响乐，有力但不张扬。

**推荐曲目（精选自 music_audio/curated_tracks.md）：**

| 优先级 | 曲目 | 来源 | 本地路径 | 理由 |
|:--:|------|------|------|------|
| ★★★ | Symphony No. 5 | beethoven-karajan | `music_audio/beethoven-karajan/05-OV6Lp7cnX7s-Beethoven "Symphony No 5" Karajan.wav` | 力量与秩序的厚重，苏联学术的庄严 |
| ★★★ | New Lands | alex-productions | `music_audio/alex-productions/74-oK8HN0FsZmc-New-Lands.wav` | 史诗开阔，百科全书式数学家 |
| ★★ | Eternals | alex-productions | `music_audio/alex-productions/76-V5T_kW2PH_s-Eternals.wav` | 宏大深远，概率论公理化的永恒影响 |
| ★ | Timeless | alex-productions | `music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav` | 纪录片风，匹配理性与深度 |

**操作**：复制选定的 `.wav` 到 `Andrey_Kolmogorov/` 目录，`make video` 自动混入。

---

## 关键参考文件清单

| 文件 | 用途 |
|------|------|
| `mathematician/presentations/数学家立传工作指南.md` | 完整操作手册 |
| `mathematician/pages/Andrey_Kolmogorov/page.md` | Kolmogorov Wikipedia 正文 |
| `mathematician/pages/Andrey_Kolmogorov/metadata.json` | Kolmogorov Wikidata 元数据 |
| `mathematician/pages/Andrey_Kolmogorov/images.txt` | 图片 URL 清单 |
| `mathematician/presentations/grothendieck/Alexander_Grothendieck_zh.tex` | Grothendieck 完整源码 |
| `mathematician/presentations/riemann/Bernhard_Riemann_zh.tex` | Riemann 完整源码 |
| `mathematician/presentations/hilbert/David_Hilbert_zh.tex` | Hilbert 完整源码 |
| `mathematician/presentations/serre/Jean_Pierre_Serre_zh.tex` | Serre 完整源码 |
| `mathematician/presentations/noether/Emmy_Noether_zh.tex` | Noether 完整源码 |

---

## 第 13 步：Wikipedia 本地文档终审（★ 提交前必做）

### 终审执行流程

```
1. 打开 pages/Andrey_Kolmogorov/page.md，从头到尾逐段阅读全文
2. 同时打开 Andrey_Kolmogorov_zh.tex 源码，逐页对照
3. 发现不一致 → 标注优先级（P0/P1/P2）
4. 全部扫描完毕 → 先修复所有 P0，再评估 P1，P2 可选
5. 修复后重新编译 → 确认零错误
```

### ⚠️ Kolmogorov 特有的终审高危点

| 高危点 | 为什么高危 | 终审时如何检查 |
|--------|---------|--------------|
| **博士生数量** | page.md 仅列 21 位，非 "60+" | page.md 统计 Doctoral students 列表行数 |
| **Feynman 湍流引语** | 不在 Kolmogorov 页面中 | page.md 全文搜索 "Feynman" → 无结果 |
| **Kolmogorov 教学引语** | "数学家不应该只做研究…"不在 page.md | page.md 搜索 "传递" → 无此引语 |
| **列宁勋章数量** | metadata 显示 12 次，非 "7 枚" | metadata.json 统计 "Order of Lenin" 出现次数 |
| **"唯一的苏联人"** | 不在 page.md 中 | Arnold 引语后无此评论 |
| **"几何原本"类比** | 不在 page.md 中 | 属创意润色，非事实 |
| **"神经网络"引用** | 不在 Kolmogorov page.md 中 | 属当代解读，非历史事实 |

### 优先级定义

| 优先级 | 定义 | Kolmogorov 实际案例（本轮） |
|:--:|------|------|
| 🔴 P0 | **事实存疑**（数字/引语/归属与page.md矛盾的硬错误） | "60+ 位博士生"、Feynman引语不在页面、教学引语捏造 |
| 🟡 P1 | **来源存疑/润色过度**（在page.md中无法逐字验证的修饰性表述） | "7枚列宁勋章"、"唯一的苏联人"、"几何原本"类比、"神经网络"引用 |
| 🟢 P2 | **重要遗漏** | Kolmogorov 与 Alexandrov 的同性关系（page.md提到但Beamer未涉及）、Kolmogorov–Smirnov检验未提及 |
| ⚪ P3 | **可选补充** | Kolmogorov 的名言 "Every mathematician believes he is ahead of the others..." |

---

> **开始执行。每完成一步向我汇报。**
>
> **特别提醒：**
> 1. Kolmogorov 的广度是最大亮点，也是最大挑战——需要精选几个最核心的贡献，而非面面俱到
> 2. 概率论公理化 (1933) 是必须浓墨重彩的页面——这是他的欧几里得时刻
> 3. "鲁金事件"要处理得客观、克制，不回避但也不渲染
> 4. KAM 定理的命名（K-A-M 三人并列）本身就体现了他的学术传承
> 5. Kolmogorov 复杂性和湍流分别展示了他的前瞻性——这些思想在他去世几十年后仍在引领前沿
> 6. Arnold 的评价"Kolmogorov – Poincaré – Gauss – Euler – Newton"可以作为最高级的引语使用
> 7. **所有引语必须来自 page.md** —— 不要使用任何无法在 page.md 中逐字验证的引语
> 8. **数字必须精确** —— page.md 仅列 21 位博士生，不说 "60+"；metadata 中列宁勋章 12 次，不说 "7 枚"
> 9. **不要添加外部来源的引语**（如 Feynman 的湍流评论）—— 仅使用 Kolmogorov 页面内的内容