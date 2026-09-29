# 教育家立传提示词（OpenPeace 批次 6 实例：Ferdinand Buisson）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Ferdinand Buisson（1927 诺贝尔和平奖，法国世俗教育之父、"laïcité" 一词的铸造者）为实例。
> 凡标注 `【模板通用】` 的部分可原样复用；标注 `【人物专属】` 的部分需按本人物替换。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 共享体系，与 OpenPhysicist / OpenMedic 平级）。
- **本实例**：Ferdinand Édouard Buisson（费迪南·爱德华·比松）。
- **设计哲学**：和平奖得主（教育家/和平活动家类）立传保留「身份信息页 + 事业领域结构化」骨架；本例的叙事重心是**世俗教育与法德和解的双线**——用学校与词典缔造共和国良心，又以对德和解赢得 1927 年和平奖。

---

## 二、背景信息 【人物专属】

- **目标人物**：Ferdinand Édouard Buisson（1841-12-20 生于巴黎 ~ 1932-02-16 卒于 Thieuloy-Saint-Antoine，享年 90 岁）
- **气质关键词**：**世俗教育之父、良心的自由派新教徒、九旬和平老人**
- **诺奖**：1927 诺贝尔和平奖（与德国教授 Ludwig Quidde 共享），获奖理由（Nobel 官方英文原文照抄，their 为共享口径）：
  > "for their contribution to the emergence in France and Germany of a public opinion which favours peaceful international cooperation"（表彰他们为法德两国形成支持和平国际合作的社会舆论做出的贡献）
- **设计母题**：**世俗的晨光（secular dawn）**。把课堂从教会的钟声下解放出来，用黑板、词典与《人权宣言》意象构建视觉语言；一个"自由派新教徒"为无神论共和国立法，这种张力本身就是设计母题。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Ferdinand_Buisson/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页骨架）；`peace/presentations/cover/`（项目首页）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准（第一轮已核对，勿改） 【人物专属】

- 生卒：1841-12-20 生于巴黎 ~ 1932-02-16 卒于 Thieuloy-Saint-Antoine（90 岁）
- 国籍：法国；激进社会党（Radical-Socialist，左翼自由派）政治家；全国自由思想者协会主席
- 教育：Lycée Condorcet → 巴黎文学院哲学 agrégation（大中学教师资格）；博士论文研究对象 Sebastian Castellio（视其为"自由派新教徒"同类）
- 流亡与信仰：因拒向第二帝国宣誓效忠，1866–1870 自愿流亡瑞士（纳沙泰尔大学教授）；自由派新教史上的标志性人物；曾尝试建立自由派新教教会（延请 Jules Steeg、Félix Pécaut 两位牧师）
- 任职（含年份）：国际和平与自由联盟三届大会 1867–1869（1869 洛桑大会宣读演讲）；1870-12 任巴黎 17 区孤儿院负责人（首座世俗孤儿院，后成塞纳孤儿院）；巴黎学校主管（Jules Simon 友谊引荐）；初等教育局局长 1879–1896（Jules Ferry 延揽）；索邦教育学教授 1890；人权联盟（LDH）共同创建者 1898、主席 1913/1914–1926（正文两说，见陷阱表）；教育联盟主席 1902–1906；众议员（塞纳选区）1902–1914、1919–1924
- 关键荣誉：Prix Marcelin Guérin（法兰西学术院，1892）；荣誉军团大军官（Grand Officer，1924）；1927 诺贝尔和平奖
- 核心事业清单：①铸造 "laïcité"（世俗主义）一词并 superviser 世俗主义法律起草②1905 政教分离法议会委员会主席③《教育学与初等教育词典》（Hachette 1882–1887，1911 新版，350+ 合作者、James Guillaume 主编，本人亲撰 laïcité/Intuition/Prayer 等条目，"世俗共和学校的圣经"）④1909-07-16 妇女选举权委员会报告人（支持 Dussaussoy 提案）⑤一战后法德和解（1923 鲁尔占领后邀德国和平主义者访法、本人赴柏林）⑥国联早期支持者
- 关键时间线（15 节点）：1841 巴黎生 / 1866 流亡瑞士 / 1867–1869 和平自由联盟大会 / 1870 归国办世俗孤儿院 / 1879 初等教育局局长 / 1882–1887 教育学词典 / 1890 索邦教授 / 1898 共创人权联盟（德雷福斯派） / 1902–1906 教育联盟主席·入众议院 / 1905 政教分离法委员会主席 / 1909 妇女选举权报告 / 1914 一战神圣同盟 / 1919–1924 复任议员·法德和解 / 1924 荣誉军团大军官 / 1927 诺奖 / 1932 卒

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 目录 `peace/presentations/20th_century/Ferdinand_Buisson/images/`；Makefile 设 `MAIN=Ferdinand_Buisson_zh`
- 肖像：正文有 Ferdinand_Buisson_(1841-1932).jpg（1920s 直链，unscaled）——优先直接下载；404 则装饰圆占位并核对图注

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | pedagogy | 教育学 | 索邦教育学教授、教育学词典 | 词典页 |
| 1 | secular education | 世俗教育 | 初等教育局局长 1879–1896 | 教育页 |
| 2 | secularism (laïcité) | 世俗主义 | 铸词者、1905 政教分离法 | 立法页 |
| 3 | human rights | 人权 | 人权联盟共同创建者与主席 | LDH 页 |
| 4 | peace activism | 和平运动 | 和平自由联盟、法德和解、国联 | 诺奖页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致） 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Ludwig Quidde | 无向 | 1927 诺贝尔和平奖共同得主 |
| colleague | Jules Ferry | 无向 | 1879 延揽其出任初等教育局局长 |
| colleague | Jules Simon | 无向 | 公共教育部长挚友，引荐任巴黎学校主管 |
| colleague | James Guillaume | 无向 | 教育学词典主编，350 人编辑部核心 |
| colleague | Paul Robin | 无向 | 1880 任命其为 Cempuis 孤儿院院长 |
| advisor-student | Vincent Peillon | Buisson→学生 | 正文明载的当代弟子（教育部长） |

- 方向约定：advisor-student 有向（Peillon=学生），其余无向（seed 幂等归一 from<to）
- 不入库：Félix Pécaut / Jules Steeg（延请的牧师，无稳定类型）、Sebastian Castellio（论文研究对象，跨四百年非关系）、Dussaussoy（提案原提出者，非合作）、配偶与子女 page.md 无载禁写

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：黑板与晨光、九旬的安详、良心自由的暖色
- **配色**：主色深红 `#8C1515`（manifest 预分配，勿改）+ 诺奖香槟金 `C9A227` + 四分类色：
  - `badgeLaicite` 世俗主义 — 金 `#C9A227`
  - `badgeEdu` 教育 — 靛 `#4C5FD5`
  - `badgeLDH` 人权 — 玫瑰 `#C4204F`
  - `badgePeace` 和平 — 群青 `#3B6FB6`
- **背景母题**：柔和圆点 + 黑板粉笔质感的细线格

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像；2. 封面明示国籍与 `国籍 | 机构 | 主要奖项` 状态栏；3. **必须有身份信息页**；4. 品牌口径统一 `OpenMathAI`，引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，13 页规划】

```
00  OpenPeace 项目首页（\input cover 封面）
01  封面 — 世俗教育之父 / Ferdinand Buisson 1841–1932 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  事业概览 — 世俗教育 / 词典 / 立法 / 人权 / 和平
04  早年：良心的流亡 (1841–1870) — Condorcet、哲学 agrégation、拒宣誓流亡瑞士
05  和平运动的起点 (1867–1869) — 和平与自由联盟三届大会
06  世俗孤儿院与巴黎学校 (1870–1879) — 17 区孤儿院、Cempuis、Paul Robin
07  初等教育局：共和国的学校 (1879–1896) — Ferry 延揽、世俗学校体系
08  索邦讲坛与教育学词典 (1890–1911) — 350 合作者、"世俗共和学校的圣经"
09  1905 政教分离法 — 委员会主席、laïcité 的铸造（核心贡献页）
10  人权联盟与德雷福斯 (1898–1926) — LDH 共创与主席
11  议席与社会事业 — 妇女选举权报告、职业教育
12  法德和解与 1927 诺贝尔和平奖 — 与 Quidde 共享、赴柏林邀客
13  遗产：世俗共和学校的圣经 + 结尾
```

### 第 7–8 步：编写 Beamer 源码 + 布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}` 定义；每写完一页 `make`，`pdftoppm` 目检溢出/重叠。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Buisson 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| LDH 主席起始年 | 导语作 1914、正文作 1913——**两说并存须加注**，勿取单一值冒充定论 |
| 教育联盟主席年份 | 1902–1906（导语），勿与人权联盟主席任期混淆 |
| 与 Briand 的政教分离法 | 1905 法委员会主席是 Buisson；Briand 是报告人/主要作者——**同一部法律两个角色**，两篇立传勿互相抢功 |
| laïcité | 他"铸造"（coined）该词——"铸造词语"勿写成"发明制度" |
| 信仰张力 | 自由派新教徒 + 全国自由思想者协会主席 + 无神论色彩——三者并存照实写，勿简化成"无神论者"或"新教徒"任一单标签 |
| Vincent Peillon | 当代（2012 年代）教育部长、"his disciples" 之一——只作事实性一句，勿展开当代政治 |
| 流亡原因 | 拒绝向第二帝国（拿破仑三世政权）宣誓效忠——客观记录，勿展开帝国史评价 |
| Castellio | 是其博士论文研究对象与他自我认同的镜像（"liberal Protestant in his image"），非真实关系，禁建关系 |
| 死亡地 | Thieuloy-Saint-Antoine（瓦兹省小镇），勿与出生地巴黎混淆 |
| 引语 | page.md 无 Buisson 本人英文原话，全篇禁直接引语；"liberal Protestant in his image" 是叙述性转述非原话引用 |
| 政治红线 | 政教分离、教会史、当代政治人物均只作 page.md 明载客观事实记录，禁评价 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| laïcité | 世俗主义 | 法语借词，保留原文 |
| separation of church and state | 政教分离 | 1905 法国法律 |
| Ligue de l'enseignement | 教育联盟 | 1902–1906 任主席 |
| Ligue des droits de l'Homme (LDH) | 人权联盟 | 1898 共创 |
| Dictionnaire de pédagogie | 教育学词典 | Hachette 1882–1887 / 1911 |
| agrégation | 大中学教师资格会考 | 哲学科 |
| League of Peace and Freedom | 和平与自由联盟 | 1867–1869 大会 |
| Sacred Union | 神圣同盟 | 一战国内和解口径 |
| Sebastian Castellio | 塞巴斯蒂安·卡斯特利奥 | 论文对象 |
| Radical-Socialist | 激进社会党 | 左翼自由派，非"社会主义" |
| freethinker | 自由思想者 | 全国协会主席 |
| Sorbonne | 索邦 | 1890 教育学教授 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **SEA** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 开阔 / 深远 / 潮汐
- **匹配理由**: "开阔/潮汐"匹配其事业的长时段性——从 1867 和平自由联盟到 1927 诺奖整整六十年的涨落；九旬老人见证第二帝国、第三共和国与一战三个时代，如海般缓慢而不可逆地把世俗学校的地平线推向全国。
- **本地路径**: `music_audio/alex-productions/92-WEqfdRXU3IU-SEA.wav` → 复制为 `presentations/20th_century/Ferdinand_Buisson/SEA.wav`
- **时长**: 128 秒 > 13 页 × 7 秒 ≈ 91 秒 → ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Ferdinand_Buisson/page.md` | 本地 Wikipedia 正文（事实唯一来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 获奖理由中译口径 |
| `MySQL/data/Ferdinand_Buisson.yaml` | 入库 yaml（第 4 / 4.5 步落地） |
| `MySQL/seed_person.py` | 幂等入库引擎 |

> **开始执行。每完成一步汇报。**
> **最重要的事：无载禁写；每写一页就 make，看到溢出就修。**
