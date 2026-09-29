# Koichi Tanaka（田中耕一）立传提示词

> qid=Q110963 · 1959-08-03 –（在世）· 日本化学家（电气工程师出身） · 21 世纪 · 诺贝尔化学奖（2002，与 Fenn 共享半奖·质谱电离；另一半 Wüthrich·NMR）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Koichi_Tanaka/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框。本地 images.txt **无单人肖像**：第 1 张为与 Koshiba、小泉纯一郎的合影（2002-10-11 首相官邸）——**非单人肖像禁作头像**（可作诺奖轰动页插图）；第 2 张 Shimadzu LCMS-IT-TOF 仪器照片作诊断技术页插图。封面用**装饰圆占位**（主色渐变 + 汉字「田中」）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{cog}\enspace\ 车间里的诺奖工程师\enspace·\enspace 日本`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧装饰圆头像 + 右侧 2×2 信息网格，至少含：生卒、本名（田中 耕一 / Tanaka Kōichi）、国籍、出生地、教育（东北大学电气工程学士 1983）、任职（岛津制作所，无博士学位）、核心领域（软激光解吸 SLD / 质谱 / 血液早期诊断）、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「激光打在基质上」母题——一个亮点射入圆群激发离子（圆点高亮渐变）。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）——如 SLD 原理框（超微金属粉+甘油基质 → 激光解吸 → 大分子完整电离）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Koichi Tanaka（田中 耕一，*Tanaka Kōichi*；中文惯称：田中耕一）
- **生卒**：1959-08-03 生于日本富山县富山市（infobox 口径 3 August 1959；metadata.json 含 1959-10-03 噪声值——**以正文/infobox 08-03 为准**）——在世
- **国籍**：Japan（日本）
- **身份**：电气工程师出身的化学家（infobox Fields：Electrical Engineering、chemistry）；终身以岛津制作所（Shimadzu Corporation）工程师/研究员身份工作——**无博士学位的「草根」诺奖得主**
- **家庭**：生母在其出生一个月后去世（由养亲抚养——页面仅一句实载，勿展开）；页面无婚姻子女实载，禁写
- **教育轨迹**：富山市下新村中 → 富山中部高中 → 东北大学工学部电气工程学科，1983 年学士毕业（无更高学位）
- **导师**：无（企业工程师路线，页面无导师实载——禁写）
- **研究领域**：质谱分析（软激光解吸 SLD）、生物大分子检测、血液早期疾病诊断

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **富山之子（1959）**：生于富山；出生一个月痛失生母——人生起点的沉默一页。
2. **电气工程师的起点（1983）**：东北大学电气工程学士毕业，入职岛津制作所，投身质谱仪研发——非化学科班、非学术机构。
3. **1985 年 2 月的发现**：发现以**甘油混合超微金属粉**为基质，激光照射可让分析物**不碎裂地电离**——质谱分析蛋白质等大分子的大门被推开。
4. **专利先行（1985）**：成果先以专利申请固定（1985），公开后于 1987 年 5 月在日本质谱学会年会（京都）报告——后称**软激光解吸（SLD）**。
5. **与 MALDI 的平行竞赛**：德国的 Franz Hillenkamp 与 Michael Karas 1985 年先报告了灵敏度更高、以小分子有机物为基质的 **MALDI**——引来「二人也应获奖」的批评；但 MALDI 在田中报告之前**从未用于电离蛋白质**。
6. **MALDI 与 SLD 的现实**：如今 SLD 已不用于生物分子分析、MALDI 则广泛使用——评审争议与实际影响并存的复杂遗产（按页面实载两点写）。
7. **「第二低职级」的诺奖得主（2002）**：获奖时在岛津仅处倒数第二职级——公司尴尬之余立刻晋升其为 research fellow 并以其名命名实验室。
8. **2002 诺贝尔化学奖**：与 John Bennett Fenn 共享半奖（质谱分析生物大分子的新方法）、另一半 Kurt Wüthrich（NMR）；官方理由 "for the development of methods for identification and structure analyses of biological macromolecules."
9. **举国轰动（2002-10-11）**：与诺奖物理得主小柴昌俊、首相小泉纯一郎在首相官邸会面（合影插图）——「公司里的普通工程师拿了诺贝尔奖」成为全民话题。
10. **从诺奖到临床的野心**：SLD 初代方法灵敏度不足以医用；团队把目标转向**血液早期疾病检测**。
11. **PEG 弹簧抗体**：用聚乙二醇在抗体基部修饰使其「如弹簧般摆动」，同时结合抗原——阿尔茨海默病相关蛋白片段实验中结合力超常规抗体百倍以上。
12. **FIRST 计划（2009–）**：入选「下一代质谱系统与创药·诊断贡献」计划，5 年约 40 亿日元、约 60 人团队，一年内实现灵敏度最高万倍提升；2011 年日本学士院英文志电子版报告、2012-08-23 与东京大学医科研 Motoharu Seiki 合作在 PLOS ONE 发表；2014 年起实现 1 mL 血液检出阿尔茨海默病相关物质并鉴定 8 种未知相关物质。
13. **IEEE Milestone（2024）**：LAMS-50K 质谱仪（五人开发团队之一）获 IEEE 历史里程碑认定——工程师身份的最终盖章。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（青碧蓝 tealblue） | `#0F4C5C` | 工程师的务实与坚韧（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（软激光解吸 badgeSLD） | `#2E5A9E` | 蓝超微金属粉+甘油 / 1985 发现 |
| 分类色 2（质谱革命 badgeMS） | `#1B7A43` | 绿大分子电离 / 2002 诺奖 |
| 分类色 3（血液诊断 badgeBlood） | `#D97B29` | 琥珀 PEG 抗体 / 早期检测 |
| 分类色 4（争议与荣誉 badgeHonor） | `#C0395B` | 玫瑰 MALDI 争议 / 文化勋章 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），其中一个亮点圆嵌入圆群——「激光打在基质上激发离子」的图形隐喻。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Awaken** — Alex-Productions（`music_audio/alex-productions/36-aqLUvpAdLNQ-Awaken.wav`；**不要复制 wav 文件，Makefile 直接引用该路径**）
- **风格**：苏醒 / 渐强 / 平凡人的高光
- **匹配理由**：
  - "觉醒" 匹配其叙事内核——公司底层工程师一夜间震惊世界，「草根诺奖」的戏剧性转折
  - "渐强" 匹配其事业曲线——1985 发现 → 1987 报告 → 2002 诺奖 → 2010s 血液诊断，层层递进
  - "平凡人高光" 匹配品牌气质——没有博士学位与名校头衔，靠车间里的一次实验改写历史
- **时长核对**：以实际曲目时长为准，> 15 页 × 7 秒即可由 ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 车间里的诺奖工程师 / Koichi Tanaka 1959– + 四色 badge + 右上装饰圆 + 国籍行
02  身份信息页（★ 必做）— 左装饰圆 + 右 2×2 信息网格（生卒/本名田中耕一/国籍/教育东北大电气工程/无博士/任职岛津/领域/荣誉）
03  Tanaka 的一生 — 时间线（10 节点：1959→1983 东北大入职岛津→1985.02 发现→1985 专利→1987.05 京都报告→SLD→2002 诺奖→2006 学士院会员→2009 FIRST→2024 IEEE Milestone）
04  早年与东北大学 (1959–1983) — 表格「时间|事件|结果」（生母早逝按页面一句实载；电气工程学位）
05  岛津制作所：质谱仪研发 — 表格「阶段|工作|意义」（1983 入职，工程师路线）
06  1985 年 2 月：甘油+超微金属粉 — 表格「问题|方法|结果」+ 公式框：基质辅助激光解吸不碎裂电离
07  SLD：专利与 1987 京都报告 — 表格「节点|形式|意义」（1985 专利 / 1987 学会报告）
08  2002 诺贝尔化学奖 — 表格「得主|份额|理由」+ 公式框：官方英文获奖理由
09  MALDI 争议 — 表格「人物|方法|争议」（Hillenkamp/Karas 1985 先报告·灵敏度更高；但先于田中报告未用于蛋白电离；SLD 现已不用而 MALDI 广用——两点实载）
10  职级第二低与举国轰动 — 表格「事实|反应|意义」（岛津晋升+命名实验室；与 Koshiba/小泉会面插图）
11  血液早期疾病检测 (2009–2014) — 表格「目标|方法|结果」+ 公式框：PEG 弹簧抗体 / 1 mL 血液检出
12  荣誉清单 — 「类别|代表|意义」表格 + itemize（2002 三连：诺奖/文化勋章/文化功劳者；学士院会员等）
13  遗产：草根诺奖的启示 — 四分类遗产盒 + IEEE Milestone（LAMS-50K 五人团队）
14  结尾 — 「没有博士学位的车间工程师，同样可以把诺贝尔奖领回家。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 获奖理由口径 | 官方英文 "for the development of methods for identification and structure analyses of biological macromolecules."（三人共享整体表述）；Fenn 与 Tanaka 共享**半奖**（质谱电离），Wüthrich 另一半（NMR）——勿写三人平分 |
| 生卒噪声 | metadata.json 双值 1959-08-03 / 1959-10-03——**以 infobox 与正文 3 August 1959 为准** |
| MALDI 争议表述 | 按页面两点实载：①Hillenkamp/Karas 1985 先报告 MALDI、灵敏度更高，「贡献大到不应被无视」的批评存在；②MALDI 虽先开发、**在田中报告之后才用于电离蛋白质**；且如今 SLD 已不用于生物分子分析、MALDI 广泛使用——不得省略对其不利的后半句 |
| MALDI 竞赛者定位 | Hillenkamp 与 Karas 是**落选争议方**（competitor/controversy 语境）——勿写成合作关系；姓名全称 Franz Hillenkamp / Michael Karas |
| 引语 | 田中本人**页面无直接引语**——全文不得出现中文引号内的"原话"，一律间接转述；「obscure」「second-lowest rank」等是页面叙述词 |
| 政治人物 | 与小泉纯一郎/小柴昌俊合影仅作**事件插图**——不作关系入库、不作政治评价；文化勋章/文化功劳者仅写授衔事实 |
| 家庭 | 生母在本人出生一个月后去世——页面仅一句，勿展开养亲细节；**无婚姻子女实载禁写** |
| 无博士 | 田中无博士学位（东北大学学士 1983）——身份信息页如实标注，勿写「博士」；亦无博士导师实载禁编 |
| FIRST 计划 | 2009 入选、5 年约 40 亿日元、约 60 人、灵敏度最高 1 万倍、2011 学士院志 / 2012-08-23 PLOS ONE（合作者 Motoharu Seiki·东京大学医科研）/ 2014 年 1 mL 血液——数字与日期逐一对照 |
| IEEE Milestone | 2024 年授予 "LAMS-50K"，田中是**五人开发团队之一**——勿写成个人独得 |
| 入库名规范 | 本人入库名 Koichi Tanaka；对手方 John Fenn（勿写 John B. Fenn）、Kurt Wüthrich、Franz Hillenkamp、Michael Karas、Motoharu Seiki |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q110963 | ✅ |
| name_zh | 田中耕一 | ✅ |
| name_en | Koichi Tanaka | ✅（新建记录） |
| birth_date | 1959-08-03 | ✅（弃 1959-10-03 噪声） |
| death_date | （在世，留空） | ✅ |
| nationality | Japan | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | chemistry（person_field 细分见下表） | ✅ |

**person_field 细分 rank 表**：

| rank | name_en | name_zh |
|---|---|---|
| 0 | mass spectrometry | 质谱法 |
| 1 | soft laser desorption | 软激光解吸 |
| 2 | biomolecule analysis | 生物大分子分析 |
| 3 | disease diagnostics | 疾病早期诊断 |

## 7. 社会关系入库清单

**★ 红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | John Fenn | 无向 | 2002 诺贝尔化学奖共同得主（共享半奖·质谱电离方法） |
| co-honored | Kurt Wüthrich | 无向 | 2002 诺贝尔化学奖共同得主（另一半·NMR 溶液结构分析） |
| competitor | Franz Hillenkamp | 无向 | MALDI 开发者（1985 先报告、灵敏度更高）；2002 诺奖落选争议的当事人之一 |
| competitor | Michael Karas | 无向 | MALDI 开发者（同上）；与 Hillenkamp 并行 |
| colleague | Motoharu Seiki | 无向 | 东京大学医科学研究所教授；2012 年 PLOS ONE 血液诊断论文合作者 |

> **禁入库名单**：小泉纯一郎（政治人物，仅官邸会面合影）；小柴昌俊（合影出席，非学术关系）；岛津制作所（机构非人物）；生母与养亲（页面仅一句实载，无学术关系）；FIRST 计划团队约 60 人（未具名）。

## 8. 奖项清单

- Nobel Prize in Chemistry（2002，与 Fenn 共享半奖；另一半 Wüthrich）
- Order of Culture 文化勋章（2002）
- Person of Cultural Merit 文化功劳者（2002）
- Honorary doctorate, Tohoku University（2002）
- Award of the Mass Spectrometry Society of Japan（1989）
- Special Award of the Mass Spectrometry Society of Japan（2003）
- Honorary citizenship of Toyama Prefecture 富山县荣誉县民（2003）
- Member of the Japan Academy 日本学士院会员（2006）
- IEEE Milestone（2024，"LAMS-50K"，五人开发团队之一）
- （metadata 注记：Keio Medical Science Prize、Montpellier 荣誉博士见 frontmatter——正文未展开，不单独成页）

## 9. 机构清单

- 教育：富山市下新村中 → 富山中部高中 → 东北大学工学部电气工程学科（学士 1983）
- 任职：岛津制作所（1983–至今；质谱仪研发 → 2002 获奖后晋升 research fellow、以其名命名实验室；分析开发第二部部长级职衔页面未载禁写）
- 公共研发：FIRST 计划「下一代质谱系统」项目组（2009–，约 60 人团队）
- 纪念：Shimadzu LCMS-IT-TOF（插图用）

## 10. 终审清单

- [ ] 生卒 1959-08-03（弃 10-03 噪声）/ 在世；出生地富山
- [ ] 2002 表述：Fenn 与 Tanaka 共享半奖（质谱电离）、Wüthrich 另一半（NMR）；官方英文获奖理由逐字
- [ ] 1985.02 发现 / 1985 专利 / 1987.05 京都报告时间线准确；SLD 名称正确
- [ ] MALDI 争议两点实载齐全（含对田中不利的「SLD 已不用」句）
- [ ] 全文无中文引号内"原话"（页面无田中直接引语）
- [ ] 无博士学位如实标注；无导师/婚姻子女实载禁写
- [ ] 入库对手方名：John Fenn / Kurt Wüthrich / Franz Hillenkamp / Michael Karas / Motoharu Seiki（规范名，与 Fenn 篇一致）
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Koichi_Tanaka/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：装饰圆占位；合影（Koshiba/小泉）与 LCMS-IT-TOF 仅作插图、图注准确
- [ ] **国籍**：封面顶部明示日本
- [ ] **引语核对**：确认全文无引号内"原话"
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 2002 批次（Fenn / Wüthrich 篇）的份额与理由表述交叉一致

---

> **开始执行。每完成一步向主控汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
