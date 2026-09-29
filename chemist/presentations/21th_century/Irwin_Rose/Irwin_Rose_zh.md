# Irwin Rose（欧文·罗斯）立传提示词

> qid=Q230652 · 1926-07-16（布鲁克林）– 2015-06-02（迪尔菲尔德，享年 88）· 美国生物化学家 · 21 世纪 · 诺贝尔化学奖（2004，与 Aaron Ciechanover / Avram Hershko 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Irwin_Rose/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/`）——身份信息页 + 时间线页 + 表格语义化 tabularx + 金边公式框，是本次执行的版式语言。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注；肖像优先取本地 `images.txt` 所列真实图片下载至 `images/`（250px 改 500px），404 则装饰圆占位，不强求。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 泛素密码的破译者\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（Irwin Allan Rose）、国籍、出生地/去世地、教育、博士、导师、核心领域、荣誉。事实取自本地 infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「泛素标签 → 逐段水解」母题——大圆被小圆逐步蚕食消散，暗示蛋白质被标记后降解。
5. **表格语义化 + 公式框**（★ 每个核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Irwin Allan Rose（中文惯称：欧文·罗斯；组内昵称 Ernie）
- **生卒**：1926-07-16 生于纽约布鲁克林 → 2015-06-02 逝于马萨诸塞州迪尔菲尔德（Deerfield），享年 88
- **国籍**：United States（美国）——metadata 另列 Sweden，系噪声：infobox 与出生、去世地均在美国，不入库
- **身份**：生物化学家（BS 与 PhD 专业均为 biochemistry；Wikipedia 描述行作 biologist；经典酶学家 enzymologist 是其学术底色）
- **家庭**：世俗犹太家庭；父 Harry Royze 开地板店（flooring store），母 Ella（娘家姓 Greenwald）；妻 Zelda Budenstein，育有四子女（页面未具名，勿编名字）
- **教育轨迹**：
  - Lewis and Clark High School（metadata 载）
  - Washington State University 就读一年 → 二战期间参加美国海军
  - 战后入 University of Chicago：1948 BS，1952 生物化学 PhD（论文 *Studies on the Biochemical Synthesis of Nucleic Acids*，1952）
  - 博士后：NYU（纽约大学）
- **导师**：Bernard S. Schweigert（博士导师，infobox Doctoral advisor 明载）
- **研究领域**：经典酶学（乙酸盐激酶、磷酸葡萄糖异构酶、磷酸丙糖异构酶、己糖激酶、腺苷酸激酶、Mg²⁺ 作用、酶催化反应立体化学）；泛素介导的蛋白质降解

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **布鲁克林起家（1926）**：世俗犹太家庭，父亲经营地板店——大萧条前后美国普通人家的科学之路。
2. **战争插曲（1940s）**：Washington State University 读一年后投笔从戎，二战在海军服役；战后重返校园完成学业。
3. **芝加哥博士（1952）**：生物化学博士，论文做核酸的生化合成；此后一生主业是酶学。
4. **耶鲁十年（1954–1963）**：Yale School of Medicine 生化系任教，完成从青年学者到成熟酶学家的过渡。
5. **Fox Chase 三十年（1963–1995）**：1963 加入费城 Fox Chase 癌症中心，直至 1995 退休——泛素故事的全部主舞台。
6. **宾大兼职教授（1970s）**：期间在 University of Pennsylvania 任物理生物化学教授（Professor of Physical Biochemistry）。
7. **经典酶学大家**：与 Marianne Grunberg-Manago、Saul Korey、Severo Ochoa 合作研究乙酸盐激酶催化的乙酰辅酶 A 生成（三羧酸循环的引燃反应），纯化酶并测平衡常数。
8. **酶学纵横**：与 O'Connell 研究磷酸葡萄糖异构酶机理、与 Rieder 研究磷酸丙糖异构酶、与 Warms 发现肉瘤己糖激酶定位于肝肾脑线粒体；对 Mg²⁺ 在细胞中作用的通盘研究（腺苷酸激酶平衡中 Mg²⁺/H⁺/K⁺ 与 ATP/ADP/AMP 的众多复合物）。
9. **立体化学一脉**：从 Ogston 理论出发研究酶催化反应的立体化学，遍及多种酶，晚年与 Kenneth Hanson 合写谷氨酰胺合成酶综述。
10. **泛素登场（1975）**：泛素由 Gideon Goldstein 等人于 1975 年发现；此后 Rose 与 Avram Hershko、Aaron Ciechanover、A. L. Haas、H. Heller 等对泛素展开大量研究。
11. **三驾马车**：与 Hershko/Ciechanover 合作阐明泛素介导的蛋白质降解——细胞如何给「待回收蛋白」打上泛素标签再逐一水解。
12. **2004 诺贝尔化学奖**：与 Ciechanover/Hershko 三人共享，理由 "for the discovery of ubiquitin-mediated protein degradation"；时年 78 岁，是三位得主中年长者。
13. **博士后三杰与演讲**：在 Fox Chase 训练了 Art Haas（第一个看到泛素链）、Keith Wilkinson（第一个鉴定 APF-1 即泛素）、Cecile Pickart；诺奖演讲 2004-12-08 *Ubiquitin at Fox Chase*。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深靛蓝 deepindigo） | `#2A3468` | 蛋白质降解的深沉与秩序（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（泛素 badgeUb） | `#1B7A43` | 绿泛素标签 / APF-1 |
| 分类色 2（蛋白降解 badgeProt） | `#2E5A9E` | 蓝水解循环 / 蛋白酶体时代序幕 |
| 分类色 3（经典酶学 badgeEnz） | `#D97B29` | 琥珀激酶 / 平衡常数 |
| 分类色 4（Fox Chase 岁月 badgeFox） | `#C0395B` | 玫瑰三十年 / 传承 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「标记—降解」的渐次消散。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Tragedy** — Alex-Productions（`/Users/ericksun/workspace/codebuddy/OpenMathAI/music_audio/alex-productions/80-K5f65-22sY4-Tragedy.wav`；**不要复制 wav 文件**，Makefile 按此绝对路径引用）
- **风格**：肃穆 / 低回弦乐 / 迟来的加冕
- **匹配理由**：
  - 78 岁高龄才与两位后辈共享 2004 诺奖——一辈子坐冷板凳的经典酶学家在暮年获得加冕，Tragedy 的低回与庄重正合「大器晚成」的叙事张力
  - 肃穆基调匹配 Fox Chase 癌症中心三十年如一日的安静研究
  - 片尾落在传承：Haas、Wilkinson、Pickart 三位博士后把泛素学发扬光大
- **时长**：以实际文件为准 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 泛素密码的破译者 / Irwin Rose 1926–2015 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/导师/出生地/去世地/领域/荣誉）
03  罗斯的一生 — Sanger 式时间线（10 节点：1926→1944→1948→1952→1954→1963→1975→1995→2004→2015）
04  早年：布鲁克林与二战 (1926–1948) — 表格「时间|事件|结果」
05  芝加哥与耶鲁 (1948–1963) — 表格「时间|事件|结果」
06  Fox Chase 与经典酶学 (1963–1970s) — 表格「酶|合作者|结论」+ 公式框：乙酸盐激酶反应（乙酸盐+ATP→乙酰辅酶 A）
07  Mg²⁺ 与酶催化立体化学 — 表格「问题|方法|结果」+ 公式框：腺苷酸激酶 Mg²⁺ 平衡
08  泛素登场 (1975) — 表格「发现者|对象|意义」
09  三驾马车：泛素介导降解 — 表格「问题|方法|结果」+ 公式框：泛素标记循环（E1–E2–E3 勿展开，页面无载只写"打标签—水解"）
10  博士后三杰与传承 — 表格「人物|贡献|后续」（Haas / Wilkinson / Pickart）
11  荣誉与晚年 — Sanger 式「类别|代表|意义」表格（2004 诺奖 + Guggenheim + 诺奖演讲）
12  Fox Chase 三十年 — Sanger FFT 页式流程图（1963 加入 → 泛素研究 → 1995 退休 → 2004 获奖时 UC Irvine）
13  遗产：蛋白质降解的第二次革命 — 四分类遗产盒 + 公式框：ubiquitin-mediated protein degradation
14  结尾 — 「细胞回收每一件废料之前，都先盖同一枚邮戳。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 共享结构 | 2004 三人共享（Ciechanover、Hershko、Rose），勿写独享 |
| 获奖理由口径 | 页面 intro 口径 "for the discovery of ubiquitin-mediated protein degradation"；"蛋白酶体"三字页面无载，勿写入获奖理由 |
| 国籍 | 仅 United States；metadata 的 Sweden 系噪声，勿写"美瑞双重国籍" |
| 职业称谓 | 页面首句作 biologist，但教育/博士均为 biochemistry、infobox occupation 含 biochemist——立传统一称"生物化学家" |
| 博士后 ≠ 博士生 | infobox 无 doctoral students 一栏；Art Haas/Keith Wilkinson/Cecile Pickart 是正文明载的**博士后研究员**——勿写成博士生 |
| 姓名混写 | Art Haas 与泛素论文署名 A. L. Haas 为同一人（正文两处）；Keith Wilkinson 勿与其他同名学者混淆 |
| 泛素发现者 | 泛素由 Gideon Goldstein 等 1975 年发现——勿写 Rose "发现泛素"，他阐明的是泛素**介导的降解** |
| E1/E2/E3 | 页面无载三酶级联命名，勿展开；只写"打标签—水解"的泛素循环 |
| H. Heller | 仅作为论文合作者署名出现，无具体关系叙述——不入库 |
| 引语 | 正文无带引号的直接引语——人物"台词"一律间接转述，勿编引号 |
| 卒地 | 2015-06-02 逝于 Deerfield, Massachusetts，享年 88——勿与出生地 Brooklyn 混淆 |
| 子女 | 四名子女页面未具名——勿编名字 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q230652 | ✅ |
| name_zh | 欧文·罗斯 | ✅ |
| name_en | Irwin Rose | ✅（新建记录，库内无同名） |
| birth_date | 1926-07-16 | ✅ |
| death_date | 2015-06-02 | ✅ |
| nationality | United States | ✅（Sweden 噪声不入） |
| primary_occupation | biochemist | ✅ |
| field_of_work | biology（metadata 口径）；person_field 细分见下 | ✅ |
| has_biography | false（Beamer 立传后置 1） | ✅ |

person_field 细分（rank 表）：

| rank | field | 说明 |
|---|---|---|
| 0 | enzymology | 经典酶学是看家本领 |
| 1 | ubiquitin-mediated protein degradation | 2004 诺奖工作 |
| 2 | enzyme stereochemistry | Ogston 理论一脉 |
| 3 | biochemistry | 学科归属 |

## 7. 社会关系入库清单

**师长 / 合作者 / 共同得主**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Bernard S. Schweigert | 师→生（博士导师） | 芝加哥大学博士导师 |
| co-honored | Aaron Ciechanover | 无向 | 2004 诺贝尔化学奖共同得主（本 yaml 先建 stub，chem21-batch-02 UPD 回填） |
| co-honored | Avram Hershko | 无向 | 2004 诺贝尔化学奖共同得主（同上） |
| colleague | Severo Ochoa | 无向 | 乙酸盐激酶合作研究 |
| colleague | Marianne Grunberg-Manago | 无向 | 乙酸盐激酶合作研究 |
| colleague | Saul Korey | 无向 | 乙酸盐激酶合作研究 |
| spouse | Zelda Budenstein | 无向 | 妻子，育有四子女 |

**博士后（正文明载，Rose 训练）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Art Haas | Rose → 学生（博士后） | 第一个看到泛素链（论文署名 A. L. Haas） |
| advisor-student | Keith Wilkinson | Rose → 学生（博士后） | 第一个鉴定 APF-1 即泛素 |
| advisor-student | Cecile Pickart | Rose → 学生（博士后） | 泛素链研究者 |

> **禁入库名单**：H. Heller（仅论文署名）、Gideon Goldstein（泛素发现者，无个人关系叙述）、四名子女（页面未具名）。metadata.json 无 doctoral_student/advisor 增补，无 metadata-only 冲突项。

## 8. 奖项清单

- Nobel Prize in Chemistry（2004，与 Ciechanover/Hershko 共享）
- Guggenheim Fellowship（年份页面无载，勿写）
- Nobel Lecture（2004-12-08，*Ubiquitin at Fox Chase*）
- 页面明载奖项仅以上——勿从记忆补别的奖

## 9. 机构清单

- 教育：Lewis and Clark High School；Washington State University（一年）；University of Chicago（BS 1948、PhD 1952）；NYU（博士后）
- 任职：Yale School of Medicine 生化系（1954–1963）；Fox Chase Cancer Center（1963–1995 退休）；University of Pennsylvania（1970s，物理生物化学教授）；UC Irvine 医学院生理学与生物物理学系 distinguished professor-in-residence（2004 获奖时）

## 10. 终审清单

- [x] 2004 三人共享表述准确；获奖理由英文口径照页面 intro
- [x] 国籍仅美国，Sweden 噪声已剔除
- [x] 博士后三人（非博士生）表述准确；Art Haas = A. L. Haas 已注
- [x] 泛素发现者归 Goldstein 等 1975
- [x] 全篇无杜撰引语（正文无直接引语）
- [x] 品牌 OpenMathAI、半角引号、封面国籍行、身份信息页齐备
- [x] `make distclean && make` 0 错误（Beamer 执行时验证）

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Irwin_Rose/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/` 已就位（真实肖像或装饰圆占位，图注如实）
- [ ] **国籍**：封面顶部明示美国
- [ ] **引语核对**：全篇无引号原话；间接转述均可溯源
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 21 世纪批次其他篇格式对齐
