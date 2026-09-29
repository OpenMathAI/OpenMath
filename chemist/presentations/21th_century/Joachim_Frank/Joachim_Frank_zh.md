# Joachim Frank（约阿希姆·弗兰克）立传提示词

> qid=Q28833112 · 1940-09-12 –（在世）· 德裔美国生物物理学家 · 21 世纪 · 诺贝尔化学奖（2017，与 Jacques Dubochet、Richard Henderson 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Joachim_Frank/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/` 取 page.md 首图 2017 年斯德哥尔摩诺奖记者会照片；下载失败用装饰圆占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{project-diagram}\enspace 单颗粒重建之父\enspace·\enspace 美国 / 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「单颗粒」母题——离散圆点暗示溶液中亿万个随机取向的单个分子被逐帧捡起、对齐、平均。
5. **表格语义化 + 公式框**（★ 核心版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Joachim Frank（中文惯称：约阿希姆·弗兰克；头衔缩写 HonFRMS）
- **生卒**：1940-09-12 生于德国锡根（Siegen）魏德瑙区 → 在世（2026-09 无卒日，年龄留白处理）
- **国籍**：United States + Germany（双重国籍，infobox Citizenship 口径）
- **身份**：德裔美国生物物理学家（German-American biophysicist）；哥伦比亚大学生物化学与分子生物物理学系及生物科学系教授；**单颗粒冷冻电镜的创始人**（regarded as the founder of single-particle cryo-EM）
- **家庭**：两段婚姻——1968 年娶 Gerda Cathy Frank；1983 年娶 Carol Saginaw；两子：Ze Frank 与 Mariel Frank（页面具名，但非学术关系，不入库）
- **教育轨迹**：
  - University of Freiburg 物理学 Vordiplom（B.S.，1963）
  - LMU Munich 物理学 Diplom（1967，Walter Rollwagen 指导；论文：金熔点二次电子发射研究）
  - Technical University of Munich 博士（1970），在 Walter Hoppe 于马克斯·普朗克蛋白质与皮革研究所（今马克斯·普朗克生物化学研究所）实验室完成研究生学业
- **导师**：Walter Hoppe（博士导师）；other academic advisors：Robert Glaeser、Robert Nathan（infobox 明载）
- **博士**：1970，《Untersuchungen von elektronenmikroskopischen Aufnahmen hoher Auflösung mit Bilddifferenz- und Rekonstruktionsverfahren》（用图像差分与重建方法研究高分辨率电子显微图像）——探索数字图像处理、光学衍射与互相关函数对齐
- **研究领域**：生物物理学——单颗粒冷冻电镜、核糖体结构与动力学、电子断层扫描

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **锡根少年（1940）**：生于战时德国锡根的魏德瑙区；物理学的严谨与图像的兴趣贯穿一生。
2. **弗莱堡到慕尼黑（1963–1967）**：物理学本科 → LMU Diplom 论文研究金熔点的二次电子发射——从第一天起就在与"电子与物质"打交道。
3. **博士：图像差分与重建（1970）**：在 Hoppe 实验室完成电子显微图像的数字处理、光学衍射与互相关对齐——单颗粒重建的全部数学根基在此埋下。
4. **哈克尼斯博士后环美之旅（1970–1972）**：Harkness Fellowship 资助两年美国行——JPL 的 Robert Nathan（图像处理）、伯克利 Donner Lab 的 Robert M. Glaeser（生物物理电镜）、康奈尔的 Benjamin M. Siegel——横跨图像科学与生物电镜两大阵营。
5. **重返马丁斯里德与剑桥（1972–1975）**：1972 回马普生物化学研究所任研究助理（电镜部分相干理论）；1973 加入剑桥卡文迪什实验室任高级研究助理（Vernon Ellis Cosslett 之下）。
6. **Wadsworth 中心：单颗粒方法起步（1975）**：受聘纽约州卫生部实验室与研究处（今 Wadsworth Center）高级研究科学家，正式开始电子显微镜单颗粒方法研究。
7. **互相关对齐 + 多变量统计平均**：把溶液中成千上万个随机取向的单个分子图像对齐、分类、平均——信噪比从噪声海洋中被打捞出来，不需要晶体。
8. **奥尔巴尼教授（1985/1986）**：1985 任新成立的 SUNY 奥尔巴尼生物医学科学系副教授，1986 升正教授。
9. **两次学术休假（1987/1994）**：1987 赴剑桥 MRC LMB 与 Richard Henderson 合作；1994 以洪堡研究奖得主身份赴海德堡马普医学研究所与 Kenneth C. Holmes 合作。
10. **HHMI 研究员（1998）**：获任霍华德·休斯医学研究所研究员。
11. **核糖体的结构与动力学**：对细菌与真核生物核糖体结构和功能的重大贡献——把单颗粒方法转向"细胞中最繁忙的分子机器"。
12. **2017 诺贝尔化学奖**：与 Jacques Dubochet、Richard Henderson 共享，官方理由 "for developing cryo-electron microscopy for the high-resolution structure determination of biomolecules in solution"——他贡献的是**算法环节**：单颗粒重建（Nobel Lecture 题目 "Single-Particle Reconstruction – Story in a Sample"）。
13. **荣誉与著述**：洪堡研究奖（1994）、美国艺术与科学院院士 + 美国国家科学院院士（2006）、富兰克林生命科学奖章（2014）、Wiley Prize（2017）、锡根大学荣誉博士 + 皇家显微学会荣誉会士（2018）；著有《Electron Tomography》《Three-Dimensional Electron Microscopy of Macromolecular Assemblies》等。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深苔绿 deepmoss） | `#2F5D50` | 图像对齐的沉稳与算法的克制（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（单颗粒重建 badgeSPR） | `#2E7FA8` | 蓝互相关对齐 / 多变量统计 |
| 分类色 2（核糖体 badgeRibosome） | `#1B7A43` | 绿分子机器 / 翻译动力学 |
| 分类色 3（电子断层扫描 badgeET） | `#D97B29` | 琥珀三维重建 |
| 分类色 4（方法学传承 badgeMethod） | `#C0395B` | 玫瑰算法开花 / 冷冻电镜革命 |
| 背景 | `#F5F7F6` | 冷调浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「从噪声中浮现的单颗粒」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Nostalgy** — AShamaluevMusic（inspiring-electronic 系列，文件 `music_audio/inspiring-electronic/17-_DA0mdtL-jI-Nostalgy - by AShamaluevMusic ｜ Sad Cinematic Music For Videos, Documentaries & Films.wav`；不复制 wav 文件）
- **风格**：怀旧 / 忧伤电影感纪录片配乐
- **匹配理由**：
  - "怀旧" 匹配其半个世纪的 method 学史——1970 年的互相关论文到 2017 年诺奖，四十七年长跑
  - "纪录片" 匹配其 Nobel Lecture 自述式的 "Story in a Sample"——一个样品里的故事，正是传记视角
  - 忧伤底色呼应大西洋两岸的迁徙人生（德国 → 美国 → 剑桥 → 海德堡 → 纽约）
- **时长**：以实际曲目时长为准，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 单颗粒重建之父 / Joachim Frank 1940– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/领域/荣誉）
03  弗兰克的一生 — 时间线（10 节点：1940→1963→1967→1970→1973→1975→1986→1998→2008→2017）
04  早年：锡根到慕尼黑 (1940–1967) — 表格「时间|事件|结果」
05  博士：Hoppe 实验室 (1967–1970) — 表格「问题|方法|结果」+ 公式框：互相关函数对齐
06  哈克尼斯环美博士后 (1970–1972) — 表格「站点|导师|收获」（Nathan/Glaeser/Siegel）
07  剑桥与 Wadsworth (1973–1986) — 表格「时间|事件|结果」
08  单颗粒重建：原理 — 表格「问题|方法|结果」+ 公式框：多帧平均提升信噪比
09  核糖体机器 (1990s–2010s) — 表格「对象|方法|意义」
10  2017 诺贝尔化学奖 — 表格「三人|分工|理由」+ 公式框：官方获奖理由英文原句（三人共享同一理由）
11  学术谱系与合作网络 — 表格「人物|关系|时期」（Hoppe/Glaeser/Nathan/Henderson/Holmes/Cosslett）
12  荣誉与院士 — 高斯式「类别|代表|意义」表格 + itemize 荣誉清单
13  遗产：不用晶体的结构生物学 — 四分类遗产盒
14  结尾 — 「样品里的故事，终被逐帧读出。」（自撰收束句，非引语）
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2017 三人分工 | Frank＝单颗粒重建算法、Dubochet＝玻璃化冷冻制样、Henderson＝首张膜蛋白电子密度图/推动技术极限——勿混淆；三人共享**同一句**官方理由 |
| 获奖理由 | "for developing cryo-electron microscopy for the high-resolution structure determination of biomolecules in solution"——develop 非 invent |
| founder 口径 | 页面原文 "regarded as the founder of single-particle cryo-EM"——"被视为创始人"的表述须保留限定语，勿写成"发明了冷冻电镜" |
| 国籍顺序 | Citizenship: United States, Germany（双籍）；描述 "German-born American"——叙述顺序德国出生、美国国籍 |
| 博士机构 | 博士学位授予 **Technical University of Munich**，实验在 Hoppe 的马普蛋白质与皮革研究所（今马普生物化学研究所）——勿只写其一 |
| 两位 other advisors | infobox 明载 Robert Glaeser、Robert Nathan；Benjamin M. Siegel 仅正文提及（同为 Harkness 站点）——Siegel 不入关系库 |
| 1985 vs 1986 | 1985 受聘副教授、1986 升正教授——两个年份勿混 |
| 同名区分 | 与 1958 年物理诺奖得主 **Ilja Frank**（伊利亚·弗兰克，Cherenkov 辐射）无任何关系；本篇是 Joachim Frank——DB 与叙述中两人严禁合并 |
| 子女 | Ze Frank（知名网络视频人）与 Mariel Frank 页面具名，但非学术关系——不入关系库 |
| 妻子 | 两段婚姻（1968 Gerda Cathy Frank；1983 Carol Saginaw）均 infobox 明载可入库 |
| 页面局限 | 本地页面无 ACM 式 citation 整句之外的额外引语，无原话引语可引——引语一律间接转述 |
| sabbatical 口径 | 1987 剑桥（Henderson/LMB）、1994 洪堡奖（Holmes/海德堡马普医学研究所）——两站勿混 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q28833112 | ✅ |
| name_zh | 约阿希姆·弗兰克 | ✅ |
| name_en | Joachim Frank | ✅ |
| birth_date | 1940-09-12 | ✅ |
| death_date | （在世，留空） | ✅ |
| nationality | United States（rank 0）+ Germany（rank 1） | ✅ |
| primary_occupation | biophysicist | ✅ |
| field_of_work | structural biology（person_field 细分见下表） | ✅ |

**person_field 细分（rank 表）**：

| rank | name_en | name_zh |
|---|---|---|
| 0 | cryo-electron microscopy | 冷冻电子显微镜 |
| 1 | single-particle reconstruction | 单颗粒重建 |
| 2 | ribosome structure | 核糖体结构 |
| 3 | structural biology | 结构生物学 |

## 7. 社会关系入库清单

**师长 / 同事 / 共同得主 / 家庭**（★红线：只收 page.md 正文或 infobox 明载；metadata-only 一律不入库）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Walter Hoppe | 师→生（博士导师） | 慕尼黑工大博士（1970），马普蛋白质与皮革研究所 |
| advisor-student | Robert M. Glaeser | 师→生（other academic advisor / 博士后） | Harkness 博士后，伯克利 Donner Lab |
| advisor-student | Robert Nathan | 师→生（other academic advisor / 博士后） | Harkness 博士后，JPL 图像处理 |
| colleague | Vernon Ellis Cosslett | 无向 | 1973 入剑桥卡文迪什实验室任高级研究助理在其下 |
| colleague | Kenneth C. Holmes | 无向 | 1994 洪堡研究奖学术休假，海德堡马普医学研究所 |
| co-honored | Jacques Dubochet | 无向 | 2017 诺贝尔化学奖共同得主 |
| co-honored | Richard Henderson | 无向 | 2017 诺贝尔化学奖共同得主（1987 亦曾赴其 LMB 实验室合作） |
| spouse | Gerda Cathy Frank | 无向 | 1968 结婚（infobox 明载） |
| spouse | Carol Saginaw | 无向 | 1983 结婚（infobox 明载） |

> **禁入库名单**（页面无具名学术关系或仅正文提及）：Benjamin M. Siegel（Harkness 博士后站点接收人，不在 infobox other advisors 名单）、Ze Frank / Mariel Frank（子女，非学术关系）、Walter Rollwagen（Diplom 导师，硕士层级不建 advisor-student）。metadata.json properties 无额外关系字段。

## 8. 奖项清单

- Nobel Prize in Chemistry（2017，与 Dubochet/Henderson 共享）
- Humboldt Research Award，Alexander von Humboldt Foundation（1994）
- Fellow of the American Academy of Arts and Sciences（2006）
- Member of the National Academy of Sciences（2006）
- Benjamin Franklin Medal in Life Science，Franklin Institute（2014）
- Wiley Prize in Biomedical Sciences（2017）
- Honorary Doctorate, University of Siegen（2018）
- Honorary Fellow of the Royal Microscopical Society（2018）
- Knight Commander's Cross of the Order of Merit of the Federal Republic of Germany（frontmatter 载）

## 9. 机构清单

- 教育：University of Freiburg（BS 1963）、LMU Munich（Diplom 1967）、Technical University of Munich（PhD 1970，Hoppe 实验室）、Max Planck Institute of Biochemistry（Martinsried）
- 任职：JPL/伯克利/康奈尔 Harkness 博士后（1970–1972）；马普生物化学研究所研究助理（1972–1973）；剑桥卡文迪什实验室高级研究助理（1973–1975）；Wadsworth Center 高级研究科学家（1975–）；SUNY Albany 副教授（1985）→ 正教授（1986）；HHMI 研究员（1998–）；Columbia University 讲师（2003）→ 教授（2008–）

## 10. 终审清单

- [ ] 生卒 1940-09-12 / 在世留白；出生地 Siegen（Weidenau）
- [ ] 2017 三人共享同一句官方理由；三人分工表述准确
- [ ] "regarded as the founder of single-particle cryo-EM" 限定语保留
- [ ] 博士机构慕尼黑工大 + 马普实验室双表述；1985/1986 两年份准确
- [ ] 与 Ilja Frank（1958 物理诺奖）无任何关联，禁止混淆
- [ ] 引语全部间接转述（本地页面无原话引语）
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Joachim_Frank/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/` 肖像就位（2017 斯德哥尔摩记者会照片；失败用装饰圆）
- [ ] **国籍**：封面顶部明示美国 / 德国双籍
- [ ] **引语核对**：官方获奖理由为唯一可直接引用整句；其余一律间接转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 黄金参照）对齐
