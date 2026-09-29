# Louis E. Brus（路易斯·布鲁斯）立传提示词

> qid=Q194646 · 1943-08-10 生于克利夫兰 – 2026-01-11 卒于 Hastings-on-Hudson（纽约州） · 美国化学家 · 21 世纪 · 诺贝尔化学奖（2023，与 Ekimov、Bawendi 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Louis_E._Brus/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**对齐 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。`images.txt` 为空；infobox 有 "Brus in 2008" 实照——执行时经 Wikipedia REST API `page/summary` 查 infobox 原图名回退下载（250px 改 500px，`curl -A "Mozilla/5.0"` + `file` 验证），失败则用主色装饰圆占位。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{atom}\enspace` 在溶液里看见量子的人`\enspace·\enspace` 美国），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（Louis Eugene Brus）、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「量子点 / 胶体」母题——悬浮的圆点即溶液中的纳米晶。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）——核心页必须给 **Brus 方程**（限域能量随粒径蓝移的 1/R² 关系）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Louis Eugene Brus（中文惯称：路易斯·布鲁斯）
- **生卒**：1943-08-10 生于俄亥俄州克利夫兰 → 2026-01-11 卒于纽约州 Hastings-on-Hudson（骨髓增生异常综合征，myelodysplastic syndrome），享年 82
- **国籍**：United States（美国）
- **身份**：化学家、化学物理学家；哥伦比亚大学 Samuel Latham Mitchell 化学教授；胶体半导体纳米晶（量子点）共同发现者
- **教育轨迹**：
  - 堪萨斯州 Roeland Park 读高中，对化学与物理产生兴趣
  - Rice University（1961 入学，NROTC 海军奖学金；1965 化学物理 B.S.）
  - Columbia University：化学物理 PhD（1969），论文 Lifetime Shortening of Na(32p) and T(72S) Quenched by Halogens
- **导师**：Richard Bersohn（博士导师；论文做碘化钠蒸气的光解）
- **军旅与转轨**：博士毕业后以海军中尉身份回海军，在华盛顿 Naval Research Laboratory 与 Lin Ming-chang 合作任科学参谋；经 Bersohn 推荐永久离开海军
- **研究领域**：physical chemistry / chemical physics、量子点、纳米技术

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **克利夫兰 → 堪萨斯（1943–1961）**：俄亥俄出生，堪萨斯高中萌生对化学与物理的兴趣。
2. **NROTC 奖学金入 Rice（1961）**：海军预备役军官团奖学金要求随舰见习——1965 化学物理 B.S. 毕业。
3. **哥伦比亚光解动力学（1965–1969）**：Bersohn 组测碘化钠蒸气光解，1969 化学物理博士。
4. **海军实验室岁月（1969–1973）**：中尉科学参谋，NRL 与 Lin Ming-chang 合作。
5. **入职 Bell Labs（1973）**：经 Bersohn 推荐，离开海军加入 AT&T Bell Laboratories——做出量子点工作的地方。
6. **CdS 表面光化学研究（1982 前后）**：为太阳能应用研究 CdS 颗粒表面的有机光化学（pump–probe 拉曼光谱）。
7. **意外发现（1982）**：晶体放置 24 小时后光学性质改变——归因于晶体长大过程中的 Ostwald ripening（奥斯特瓦尔德熟化）导致的带隙变化——**独立首次在溶液中合成出量子点**。
8. **Brus 方程（1983–1984）**：JCP 两篇论文建立小半导体晶粒的电离能/电子亲和能与电子-空穴相互作用的尺寸依赖简单模型——粒径与发射波长的联系，后世称 Brus equation。
9. **与苏联同行会合（1990）**：多方尝试联系苏联研究者后，终于见到 Ekimov 与 Efros——后者 1981 年已在玻璃中更早做出半导体纳米晶，但研究在美不可得。
10. **缩小尺寸的攻坚（1990 前后）**：在 Bell Labs 与博士后 Paul Alivisatos、Moungi Bawendi 及金属有机合成化学家 Michael L. Steigerwald 合作，攻关把量子点做小。
11. **单量子点荧光闪烁（1996）**：Nirmal/Bawendi/Brus 等 Nature 论文报道单个 CdSe 纳米晶的荧光间歇性（页面 Selected publications 明载）。
12. **晚年多面手**：表面增强拉曼（1999）、MoS2 单层反常晶格振动（2010，ACS Nano 高被引）——从量子点到二维材料。
13. **2023 诺贝尔化学奖与身后**：与 Ekimov、Bawendi 共享，官方理由 "for the discovery and synthesis of quantum dots"；2026-01-11 因骨髓增生异常综合征去世，享年 82——诺奖得主的最后一年。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（暗紫 nightviolet） | `#46356B` | 深夜实验室里量子点荧光的底色（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（胶体合成 badgeColloid） | `#1E6E8C` | 青蓝胶体溶液 / CdS 悬浮液 |
| 分类色 2（Brus 方程 badgeBrus） | `#B3462E` | 橙红限域能量蓝移曲线 |
| 分类色 3（理论框架 badgeTheory） | `#2E7D4F` | 绿尺寸-波长的量子限域理论 |
| 分类色 4（单晶光谱 badgeSingle） | `#8C2F5B` | 玫红单量子点闪烁 / SERS |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「胶体量子点」——溶液中悬浮的纳米晶。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Awaken** — Alex-Productions（源文件 `music_audio/alex-productions/36-aqLUvpAdLNQ-Awaken.wav`，执行时软链/复制至本目录，不复制 wav 入库）
- **风格**：苏醒 / 渐强 / 开辟新域的史诗感
- **匹配理由**：
  - "苏醒" 匹配 1982 年的意外发现——放置 24 小时的 CdS 晶体"醒来"变色的瞬间，一个新领域从熟化副产物中苏醒
  - "开辟新域" 匹配其理论奠基角色——Brus 方程把现象变成可计算的物理
  - 渐强结构匹配其生涯曲线——海军→Bell Labs→哥伦比亚，1990 与苏联同行会合、2023 登顶诺奖
- **时长**：执行时用 ffprobe 核对 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 在溶液里看见量子的人 / Louis E. Brus 1943–2026 + 四色 badge + 右上头像 + 国籍行（美国）
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/出生地/去世地/教育/博士/领域/荣誉）
03  布鲁斯的一生 — 时间线（10 节点：1943→1961→1965→1969→1973→1982→1983→1990→1996→2023/2026）
04  早年：NROTC 与 Rice (1943–1965) — 表格「时间|事件|结果」
05  哥伦比亚与海军 (1965–1973) — 表格「阶段|内容|结果」+ 博士导师 Bersohn
06  Bell Labs：CdS 表面光化学 (1973–1982) — 表格「问题|方法|结果」
07  意外发现 (1982) — 表格「观察|归因|结果」+ 公式框：Ostwald ripening 与带隙
08  Brus 方程 (1983–1984) — 表格「问题|建模|结果」+ 公式框：限域能量 ~ 1/R²（★核心页）
09  与苏联同行会合 (1990) — 表格「人物|事件|结果」（Ekimov/Efros 1981 玻璃先行）
10  缩小量子点：Bell Labs 攻坚 — 表格「人物|角色|结果」（Alivisatos/Bawendi/Steigerwald）
11  单量子点与晚年研究 — 表格「方向|代表作|结果」（1996 闪烁 / 1999 SERS / 2010 MoS2）
12  荣誉清单 — 「类别|代表|意义」表格 + itemize（Kavli 2008 / Gibbs 2009 / Wood 2006 / Nobel 2023）
13  三人接力与遗产 — 流程图：Ekimov 1981 → Brus 1982 → Bawendi 1993；2026-01-11 去世注记
14  结尾 — 「把量子限域写成方程的人。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2023 诺奖共享口径 | 与 **Ekimov、Bawendi 三人共享**，官方理由 "for the discovery and synthesis of quantum dots"——勿写"独享" |
| 三人分工 | Ekimov（1981 玻璃中首发）→ Brus（**1982 溶液/胶体**中独立首次合成 + 理论框架）→ Bawendi（1993 合成法）——Brus 的"第一"限定在"溶液中独立首次" |
| "co-discoverer" | 页面称其为胶体半导体纳米晶的 co-discoverer——与 Ekimov 的玻璃体系并行，勿写"唯一发现者" |
| Brus 方程内容 | 粒径与发射波长的联系（限域能量的尺寸依赖）——勿写成"量子点合成方法"；hot-injection 法是 Bawendi 的贡献 |
| 1982 归因链 | 24 小时后光学性质改变 → Ostwald ripening 晶体长大 → 带隙变化——三步因果链按页面顺序，勿倒置 |
| 博士后关系 | Bawendi 在 Bell Labs 是 **Brus 的博士后**（页面明载）——Bawendi 篇以 advisor 方向建边、本篇以 student 方向建边，镜像一致 |
| Alivisatos 角色 | 页面称 postdoc researchers Paul Alivisatos 与 Moungi Bawendi——Alivisatos 建 colleague（同组博士后）非学生明载学位关系 |
| 与 Ekimov/Efros | 1990 才见面；此前苏联研究在美不可得——勿写"早就知道对方工作" |
| R. W. Wood Prize | 2006 与 **Efros、Ekimov** 共同获奖（"for the discovery of nanocrystal quantum dots..."）——勿漏 Efros |
| Kavli Prize | 2008 首届 Kavli 纳米科学奖与 **Sumio Iijima** 共享（零维/一维纳米结构）——勿写成与 Ekimov 共享 |
| 去世口径 | 2026-01-11，Hastings-on-Hudson，纽约州，骨髓增生异常综合征（myelodysplastic syndrome），享年 82——勿写"卒于纽约市" |
| 学位口径 | Rice B.S. 1965（化学物理）、Columbia PhD 1969（化学物理）——勿写 Rice 博士 |
| 页面无载禁写 | 页面无其妻子/子女、无 Bell Labs 具体职位名、无直接引语——全文不编引语，改间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q194646 | ✅ |
| name_zh | 路易斯·布鲁斯 | ✅ |
| name_en | Louis E. Brus | ✅ |
| birth_date | 1943-08-10 | ✅ |
| death_date | 2026-01-11 | ✅ |
| nationality | United States | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | quantum dot（person_field 细分：quantum dots / physical chemistry / chemical physics / nanotechnology，带 rank） | ✅ |
| has_biography | false（Beamer 立传完成后再置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 门生 / 同事**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Richard Bersohn | 师→生（博士导师） | 哥伦比亚博士导师，光解动力学；库内已有记录（id=2666） |
| advisor-student | Moungi Bawendi | Brus → 学生（博士后） | Bell Labs 博士后，后 1993 热注入法（与 Bawendi 篇 advisor 方向镜像同一有向边） |
| colleague | Paul Alivisatos | 无向 | Bell Labs 同组博士后，合作缩小量子点 |
| colleague | Michael L. Steigerwald | 无向 | 同组金属有机合成化学家 |

**共同得主**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Alexey Ekimov | 无向 | 2023 诺贝尔化学奖共同得主；2006 R. W. Wood Prize 共同得主 |
| co-honored | Moungi Bawendi | 无向 | 2023 诺贝尔化学奖共同得主 |
| co-honored | Alexander Efros | 无向 | 2006 R. W. Wood Prize 共同得主 |
| co-honored | Sumio Iijima | 无向 | 2008 首届 Kavli 纳米科学奖共同得主 |

> Lin Ming-chang（NRL 合作同事）页面正文有载，但仅一段军旅背景提及、无实质学术合作细节——从严**不予入库**（可选：若 Review 认为该合作足够实质，可补 colleague 一行，note 注明 NRL）。
> metadata.json 无 doctoral_students 等额外关系字段；页面无载师承之外的家庭关系，**不予入库**。

## 8. 奖项清单

- Nobel Prize in Chemistry（2023，与 Ekimov/Bawendi 共享，"for the discovery and synthesis of quantum dots"）
- Irving Langmuir Prize in Chemical Physics（2001）
- American Academy of Arts and Sciences Fellow（1998）；NAS 院士（2004）；挪威科学与文学院成员
- R. W. Wood Prize（2006，与 Efros、Ekimov 共享）
- 首届 Kavli Prize in Nanoscience（2008，与 Sumio Iijima 共享）
- Willard Gibbs Award（2009，"for his leading role in the creation of chemical quantum dots"）
- NAS Award in Chemical Sciences（2010）；Rice 杰出校友奖（2010）
- Bower Award and Prize for Achievement in Science（2012，Franklin Institute）
- Clarivate Citation Laureate in Chemistry（"for discovery of colloidal semiconductor nanocrystals (quantum dots)"）
- National Academy of Inventors 2025 Fellow

## 9. 机构清单

- 教育：Rice University（1961–1965，B.S. 化学物理）；Columbia University（PhD 1969，化学物理）
- 任职：United States Naval Research Laboratory（1969–1973，海军中尉科学参谋）；AT&T Bell Laboratories（1973–1996）；Columbia University 化学系（1996–，Samuel Latham Mitchell Professor）
- 去世：2026-01-11，纽约州 Hastings-on-Hudson

## 10. 终审清单

- [ ] 生卒 1943-08-10 / 2026-01-11（享年 82，死因 myelodysplastic syndrome）表述准确
- [ ] 1982 溶液中独立首次合成 / Brus 方程 1983–1984 归属无误
- [ ] 2023 三人共享口径与官方理由英文原文无误；三人接力分工准确
- [ ] Wood Prize（Efros/Ekimov）与 Kavli（Iijima）共享名单不混淆
- [ ] Bawendi 博士后关系双向镜像一致（advisor/student）
- [ ] 全文无编造引语；"第一次/唯一"类断言均有页面明载
- [ ] `make distclean && make` 编译通过，0 错误，vbox≤10pt / hbox≤50pt

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Louis_E._Brus/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：经 REST API 回退下载 infobox 2008 实照；失败则装饰圆占位并注记
- [ ] 国籍：封面明示"美国"
- [ ] 引语核对：Willard Gibbs 授奖词、"for the discovery of nanocrystal quantum dots..."（Wood Prize）等均须在页面原文找到
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox≤10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐；结尾品牌 OpenMathAI

---

> **名单状态**：`chemist/generate_21th_century_list.py` 更新由主控统一收尾，本文件不改动生成器。
