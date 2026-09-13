# Jim Gray（吉姆·格雷）立传提示词

> qid=Q92606 · 1944-01-12 – 2007-01-28 海上失踪（2012-01-28 缺席宣告死亡） · 美国计算机科学家 · 20 世纪 · 1998 图灵奖
> 本地 Wikipedia 数据源：`turing/pages/1998/Jim Gray (computer scientist)/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（两阶段提交协议 / 五分钟法则的技术化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：James Nicholas Gray（中文惯称：吉姆·格雷）
- **生卒**：1944-01-12 生于 San Francisco, California（美国）→ **2007-01-28 驾帆船出海失踪**（旧金山近海，63 岁）→ 2012-01-28 被法院缺席宣告死亡（declared dead in absentia，68 岁）——**措辞必须谨慎，写"失踪/宣告死亡"，勿写"遇难"等推定性死因**
- **国籍**：美国（American）
- **身份**：计算机科学家（数据库与事务处理）
- **家庭**：父 James Able Gray（美国陆军出身、业余发明家，打字机色带匣专利获利颇丰）、母 Ann Emma Sanbrailo（教师）；幼年随家迁罗马（先学会意大利语后学英语）；父母离异后随母回旧金山。首婚 Loretta（后离异，育一女）、第二任妻子 Donna Carnes
- **教育轨迹**：
  - 报考 Air Force Academy 被拒后，**1961 年**入 UC Berkeley（曾因化学成绩离开半年，转做工业界后称那段经历 "dreadful"）
  - 1966 年 UC Berkeley **工程数学**学士（BS, Math and Statistics）
  - Bell Labs 工作期间于 NYU Courant Institute 读硕士（MS）
  - 1969 年 UC Berkeley **程序设计语言**博士（PhD），导师 Michael A. Harrison
- **研究领域**：数据库（database）与事务处理（transaction processing）系统

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **图灵奖理由整句**：1998 年图灵奖 "for seminal contributions to database and transaction processing research and technical leadership in system implementation"（数据库与事务处理研究的开创性贡献 + 系统实现的技术领导力）。
2. **System R**：在 IBM San Jose Research Laboratory 参与研发 System R——引入 SQL 的原型关系数据库系统，成为后来商业关系数据库产品的基础。
3. **两阶段提交协议（two-phase commit protocol）**：分布式事务处理的基石，其最著名成就之一。
4. **粒度数据库锁（granular database locking）**：数据库并发控制的关键贡献。
5. **五分钟法则（five-minute rule）**：存储页在内存与磁盘间分配的经典经验法则。
6. **OLAP cube 算子**：数据仓库（data warehousing）的 OLAP cube 算子。
7. **软件缺陷类型刻画**：对 software bug types 的系统刻画；另著 *"Why do computers stop and what can be done about it?"*（1986，参考文献实载）。
8. **工业界巨擘的轨迹**：IBM（博士毕业后两年博士后）→ Tandem Computers → DEC → **Microsoft（1995 年入职，Technical Fellow，直至 2007 年海上失踪）**。
9. **Microsoft 时代：科学与 Earth 之窗**：TerraServer-USA 与 Skyserver；参与 Virtual Earth 开发——把数据库技术用于科学数据与地图服务。
10. **中立的裁判者**：Roger Sippl 称其为业界 "technical gods in this industry" 之一、标准委员会中受敬重的中立仲裁者（带归属的转述，页面实载）。
11. **学术组织贡献**：CIDR（Conference on Innovative Data Systems Research）共同创始人。
12. **海上失踪与全球搜索（2007）**：2007-01-28 独驾 40 英尺帆船 Tenacious 前往 Farallon Islands 撒母亲骨灰未归；天气晴好、无求救信号、EPIRB 无反应；海岸警卫队四日搜索无果；DigitalGlobe 卫星影像上传 Amazon Mechanical Turk，全球志愿者组成 "Jim Gray Group" 逐图搜寻——计算机史上最著名的众包搜救。
13. **身后遗产**：Microsoft WorldWide Telescope 题献给他；2008 年 Microsoft Research 设立 Gray Systems Lab（Madison, Wisconsin）；SIGMOD 每年颁发 Jim Gray Doctoral Dissertation Award；Microsoft Research 每年颁发 Jim Gray eScience Award。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（数据库系统 — 蓝） | `#2E5A9E` | System R / SQL |
| 分类色 2（事务处理 — 青绿） | `#1E8E8E` | 两阶段提交 / 锁 |
| 分类色 3（数据仓库与存储 — 琥珀） | `#D9A441` | OLAP cube / 五分钟法则 |
| 分类色 4（eScience 与地球之窗 — 玫瑰） | `#C0395B` | TerraServer / Skyserver / eScience |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆），呼应「数据之海与帆船 Tenacious」的视觉语言。

### 3.5 背景音乐选择 ✅【人物专属】

- **气质定位**：辽阔 / 苍茫（数据库之海、帆船远航与未归的传奇）
- **选定曲目**：Alex-Productions **SEA**（manifest 预分配，直接沿用；化学 Arrhenius 篇同曲，属正常复用），匹配"事务处理的秩序与大海的苍茫"双重意象。
- **落地文件**：`turing/presentations/Jim_Gray/SEA.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「事务处理巨擘 · 美国」+ 格雷 1944–2007（失踪）+ 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育路线 / 导师 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1944–2012（宣告死亡）生平纵览
4. **早年：罗马学语的少年**（1944–1961）：陆军父亲、意大利语第一语言、父母离异、空军学院落榜
5. **Berkeley 本科与 Bell Labs**（1961–1966）：工程数学、General Dynamics co-op、Monroe 计算器、Multics 数字仿真
6. **Berkeley 博士**（1966–1969）：程序设计语言方向、导师 Michael A. Harrison、IBM 博士后两年
7. **System R 与 SQL**：IBM San Jose、原型关系数据库
8. **两阶段提交协议**（公式框：2PC 提交/回滚的语义化表达）
9. **粒度锁与五分钟法则**：并发控制与存储分配
10. **OLAP cube 与缺陷刻画**：数据仓库算子、bug types
11. **Tandem → DEC → Microsoft**（1995）：Technical Fellow、TerraServer-USA / Skyserver / Virtual Earth
12. **2007：海上失踪**：Tenacious、Farallon Islands、众包搜救、2012 宣告死亡（措辞谨慎页）
13. **荣誉**：Turing 1998、Charles Babbage Award 1998
14. **遗产**：Gray Systems Lab、SIGMOD 博士论文奖、eScience Award、WorldWide Telescope
15. **结尾**："technical gods" 的评价与未归的航程

## 5. 史实陷阱与敏感点（终审必须检查）

- **失踪/宣告死亡措辞（P0 红线）**：页面口径为"2007-01-28 失踪（disappeared）→ 2012-01-28 缺席宣告死亡（declared dead in absentia）"——**勿写"溺亡/遇难/去世"等推定死因**；年份勿混（失踪 2007、宣告 2012）。
- **失踪细节按实载**：撒母亲骨灰、Farallon Islands、天气晴好、无求救信号、无 EPIRB 信号、C&C 40 船型船体脆弱 30 秒内可沉没——只写页面实载，勿加推理（如"可能遇到大浪"）。
- **众包搜救按实载**：DigitalGlobe 影像 → Amazon Mechanical Turk → "Jim Gray Group" → 2/16 暂停 → 5/31 水下搜索结束——数字与日期勿混。
- **图灵奖理由整句**："for seminal contributions to database and transaction processing research and technical leadership in system implementation"——勿改写。
- **奖项**：图灵奖 1998 与 IEEE Computer Society Charles Babbage Award **同为 1998**——勿错开年份。
- **学位**：BS 1966（工程数学 Math and Statistics）、PhD 1969（programming languages，Berkeley，导师 Michael A. Harrison）；硕士在 **NYU Courant**（Bell Labs 工作期间）——勿把硕士写成 Berkeley。
- **System R 定位**："原型关系数据库系统、引入 SQL、成为后来商业关系产品的基础"——勿写 Gray 是 SQL 唯一发明人。
- **"first"类表述禁写**：页面未载任何"首位/第一"类断言（CIDR 是 co-founder，可写）；勿编造。
- **家庭**：Loretta（离异）、Donna Carnes（第二任、 petition 宣告死亡者）、一女——按实载，勿渲染 2014 CNN 采访等背景细节。
- **引语**：页面实载两条——Sippl 的 "technical gods in this industry"（转述带归属）与 Gray 自述工业经历 "dreadful"；除此之外全文无本人直接引语，勿编造。
- **生卒字段**：出生 1944-01-12；死亡日期数据库如需填写，用 2012-01-28（宣告死亡日）并注记"2007-01-28 失踪"，或按 DB 约定留白——执行时二选一并保持前后一致。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | manifest 为 null，待补 |
| name_zh | 格雷（或 吉姆·格雷） | 待写入 |
| name_en | Jim Gray | 待写入 |
| birth_date | 1944-01-12 | 待写入 |
| death_date | 2007-01-28 失踪 / 2012-01-28 宣告死亡（按 DB 约定二选一） | 待写入 |
| nationality | United States | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | database / transaction processing | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Michael A. Harrison（UC Berkeley）
- **合作者参照**：Andreas Reuter（*Transaction Processing: Concepts and Techniques* 1993 合著者，参考文献实载）；Eswaran/Lorie/Traiger（1976 consistency & predicate locks 论文合著者）——按"合作者"入库
- **纪念者**：Gordon Bell、Leslie Lamport、Butler W. Lampson（NAS 传记回忆作者）——不入关系表，仅限文本
- **无载禁写**：页面未列其博士生名单——勿编造学生关系

## 8. 奖项清单

- Turing Award（1998，理由见 §5 红线）
- IEEE Computer Society Charles Babbage Award（1998）
- 身后纪念（非个人获奖，可列"遗产"页）：SIGMOD Jim Gray Doctoral Dissertation Award（年度）、Microsoft Research Jim Gray eScience Award（年度）、Gray Systems Lab（2008, Madison）、WorldWide Telescope 题献（2008-05-31 Berkeley 追思会前后）

## 9. 机构清单

- 教育：UC Berkeley（BS 1966 工程数学；PhD 1969 程序设计语言）、NYU Courant Institute（硕士，Bell Labs 工作期间）
- 任职：Bell Labs（Multics 数字仿真）、IBM（博士后两年 → San Jose Research Laboratory，System R）、Tandem Computers（事务处理）、DEC（事务处理）、Microsoft（1995–2007，Technical Fellow；TerraServer-USA、Skyserver、Virtual Earth）

## 10. 终审清单

- [ ] 失踪/宣告死亡措辞全程合规（2007 失踪、2012 宣告，无推定死因）
- [ ] 图灵奖获奖理由整句引用无误
- [ ] 鼠标——不适用本篇；两阶段提交/粒度锁/五分钟法则/OLAP cube 四大成就页齐全
- [ ] System R "原型、引入 SQL、商业基础"定位准确
- [ ] 学位路线 Berkeley 1966 / NYU Courant 硕士 / Berkeley PhD 1969（导师 Harrison）
- [ ] 任职链 IBM → Tandem → DEC → Microsoft 1995 完整
- [ ] 众包搜救日期数字全部对齐页面
- [ ] 引语仅两条实载（Sippl 转述、"dreadful"），带归属
- [ ] 国籍用「美国」，封面底部状态栏 `美国 | IBM · Tandem · DEC · Microsoft | Turing 1998`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/1998/Jim Gray (computer scientist)/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 `images/500px-Jim_Gray_Computing_in_the_21st_Century_2006.jpg`（2006 年真肖像，最大版）；帆船照 `500px-Jim_Gray_on_Tenacious_2006.jpg` 可作失踪页插图
- [ ] **国籍**：封面顶部徽章明示美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Minsky/McCarthy 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同代图灵奖得主（1996 Pnueli / 1997 Engelbart）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
