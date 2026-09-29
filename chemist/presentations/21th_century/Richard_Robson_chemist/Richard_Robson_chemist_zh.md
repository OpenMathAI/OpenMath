# Richard Robson（理查德·罗布森）立传提示词

> qid=Q23073819 · 1937-06-04 生于英格兰 Glusburn · 在世 · 英国-澳大利亚化学家 · 诺贝尔化学奖（2025，与 Susumu Kitagawa、Omar M. Yaghi 三人共享）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Richard_Robson_chemist/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：对齐 `chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}` 黄金骨架（表格语义化 tabularx + 公式展示框 + 时间线页 + 身份信息页）。

---

## 0. 正文形式说明（★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。页面无独立个人肖像（images.txt 仅 2025 三人斯德哥尔摩大学合影）：用合影裁剪或装饰圆占位，图注写「Robson with Susumu Kitagawa and Omar Yaghi, Stockholm University 2025」。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{project-diagram}\enspace 配位聚合物的前驱者\enspace·\enspace 英国 / 澳大利亚`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍（英/澳）、出生地、教育、博士导师、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和节点-连线圆阵（稀疏圆点以细线相连），呼应「金刚石骨架 / 节点-连接体」母题。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如 Cu(I) 四面体节点 + 四腈连接体 → 类金刚石骨架。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`；中文名「理查德·罗布森」。

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Richard Robson（中文惯称：理查德·罗布森），FAA FRS
- **生卒**：1937-06-04 生于英格兰约克郡 Glusburn（West Yorkshire，今 North Yorkshire；在世）
- **国籍**：United Kingdom + Australia（英国-澳大利亚；页面首句 "English and Australian chemist"）
- **身份**：化学家，University of Melbourne 化学教授（终身效力）
- **家庭**：女儿 Naomi Robson，前电视主持人（page.md Personal life 明载）
- **教育轨迹**：Brasenose College, Oxford 读化学——1959 BA、1962 DPhil；博士在 Dyson Perrins Laboratory 完成有机分子光化学研究
- **导师**：博士导师 John A. Barltrop（metadata 全名形式 John Alfred Barltrop）；博士后导师 Henry Taube（Stanford，1964–1965）
- **职业轨迹**：Caltech 博士后（1962–1964）→ Stanford 博士后（1964–1965，Henry Taube 组）→ 1966 年起 Melbourne 讲师，直至整个职业生涯
- **研究领域**：无机化学——配位聚合物、金属有机框架（MOFs）；被誉为「过渡金属晶体工程的先驱」

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **1937 年生于 Glusburn**：英格兰约克郡乡村走出的化学家。
2. **牛津 Brassensoe 岁月（1959/1962）**：Brasenose College BA（1959）→ DPhil（1962），Dyson Perrins Laboratory 有机光化学。
3. **跨越大西洋（1962–1965）**：Caltech 博士后两年 → Stanford 一年，在 Henry Taube（1983 诺贝尔化学奖得主）组做博士后。
4. **定居墨尔本（1966）**：接受 University of Melbourne 化学讲师职位，此后一生未离。
5. **1974 灵感时刻**：为一年级化学讲座搭建大型木质晶体结构模型时，萌生「用分子做同样的事」的念头——MOF 领域的起点。
6. **1989 奠基论文**：与 Bernard F. Hoskins 发表 JACS 论文，提出三维连接的无限聚合物骨架（infinite polymeric frameworks）。
7. **1990 类金刚石骨架**：用倾向四面体构型的 Cu(I) 与定制四腈有机连接体，构筑出带显著工程化空腔的类金刚石晶体骨架——本批三人中「前驱性概念论文」的代表。
8. **开创全新化学领域**：1990 年代创造的这类配位聚合物，成为整个现代 MOF 化学领域的地基。
9. **1998 互穿网络综述**：与 Stuart R. Batten 发表 Interpenetrating Nets 长篇综述（Angew. Chem.），系统化有序周期纠缠网络。
10. **Burrows Award（1998）**：皇家澳大利亚化学学会无机化学分部奖。
11. **双院会士**：Australian Academy of Science 会士（2000）→ Royal Society 会士（2022）。
12. **2025 诺贝尔化学奖**：与 Kitagawa、Yaghi 共享，表彰其对 MOF 领域的早期奠基贡献（页面口径 "for his early contribution to the field of MOFs"）。
13. **迟来的加冕**：88 岁获奖、在墨尔本坚守近六十年——「先坐冷板凳，后开新大陆」的前驱者叙事。

## 3. 配色方案（主色 + 强调 + 分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（框架绿 framegreen） | `#146B3A` | 类金刚石骨架的秩序与生长（表头 / 公式文本） |
| 强调色（香槟金，coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（配位聚合物 badgeCP） | `#2E5A9E` | 蓝节点-连接体 / Cu(I) 四面体 |
| 分类色 2（骨架设计 badgeNet） | `#1B7A43` | 绿类金刚石网络 / 空腔工程 |
| 分类色 3（晶体工程 badgeCE） | `#D97B29` | 琥珀 crystal engineering / 互穿网络 |
| 分类色 4（学术轨迹 badgePath） | `#C0395B` | 玫瑰牛津→加州→墨尔本 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和节点-连线圆阵（稀疏实心圆点以细线相连，四档大小错落），暗示四面体节点与连接体构成的开放骨架。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Tragedy** — Alex-Productions（文件 `music_audio/alex-productions/80-K5f65-22sY4-Tragedy.wav`；不要复制 wav 到本目录）
- **风格**：深沉 / 悲壮叙事 / 迟来的认可
- **匹配理由**：
  - "深沉" 匹配前驱者的孤独——1974 年的灵感等待了半个世纪才等来诺奖加冕
  - "悲壮叙事" 匹配其坚守——1966 年起在墨尔本近六十年深耕冷门方向
  - 迟来的认可不是悲剧，而是向坚守者致以的厚重配乐；结尾页可落「前人栽树」的暖色收束
- **时长**：以实际曲目时长为准，ffmpeg `-shortest` 自动对齐 15 页 × 7 秒

## 4. Slide 规划（15 页，00–14）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 配位聚合物的前驱者 / Richard Robson 1937– + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士导师/领域/现职/荣誉）
03  罗布森的一生 — 时间线（10 节点：1937→1959→1962→1964→1966→1974→1989→1990→1998→2025）
04  约克郡与牛津 (1937–1962) — 表格「时间|事件|结果」
05  加州博士后与墨尔本扎根 (1962–1966) — 表格「阶段|导师|结果」
06  木质模型与灵感 (1974) — 表格「场景|念头|意义」+ 公式框：晶体模型 → 分子骨架
07  1989 奠基论文 — 表格「问题|方法|结果」+ 公式框：无限聚合物骨架
08  1990 类金刚石骨架 — 表格「节点|连接体|结果」+ 公式框：Cu(I) 四面体 + 四腈连接体
09  2025 诺贝尔化学奖 — 表格「三人|方向|分工」（Robson 概念 / Kitagawa 柔性 / Yaghi 系统化）
10  互穿网络与合作者 (1998) — 表格「合作者|主题|结果」（Hoskins / Batten）
11  荣誉年表 — 高斯式「类别|代表|意义」表格（Burrows Award / FAA 2000 / FRS 2022 / 诺奖 2025）
12  传承与意义 — 四分类遗产盒（MOF 地基 / 晶体工程 / 墨尔本学派 / 后续 MOF 化学）
13  遗产：先坐冷板凳 — 公式框 + 总结
14  结尾 — 「用分子搭出晶体，再用晶体装下世界。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 消歧义目录 | 本页是化学家 Richard Robson（`Richard_Robson_chemist`），与库内既有记录 #3755「Richard Robson」为同一人（复用回填 QID）——yaml name_en 必须用 **Richard Robson** 精确形式 |
| 前驱性论文 | 概念奠基有两篇：**1989**（无限聚合物骨架）与 **1990**（类金刚石 Cu(I) 四腈骨架）；任务口径「1990 前驱性概念论文」指后者——勿把 MOF-5（Yaghi 1999）归给 Robson |
| 首创归属 | Robson 是配位聚合物/MOF 概念前驱；MOF 的系统化与命名普及属 Yaghi、气体吸附证明属 Kitagawa——三人分工勿混 |
| 2025 获奖理由 | 页面口径 "for his early contribution to the field of MOFs" / 三人 "for the development of metal-organic frameworks"；官方完整英文原句页面无载，**禁止杜撰整句** |
| 博士后导师 | Henry Taube 是 Stanford 博士后导师（1964–1965，infobox Other academic advisors）——是合作关系，**勿写成博士导师**（博士导师是 Oxford 的 Barltrop） |
| 获奖时机构 | University of Melbourne（1966 至今）——勿写 Oxford/Caltech |
| 国籍 | 英国 + 澳大利亚（metadata：United Kingdom, Australia；正文 "English and Australian chemist"）——勿只写其一 |
| 家庭 | 仅女儿 Naomi Robson 明载（前电视主持人）；妻子等信息页面无载**禁写** |
| "先驱" 引语 | 页面原文是间接引语 "He has been described as 'a pioneer in crystal engineering involving transition metals'"——引用时保留 "described as" 归属，勿写成直接自述 |
| 木模型年份 | 灵感年份是 **1974**（"sparked in 1974 while constructing large wooden models"）——勿写其他年份 |
| 同名区分 | 对手方规范名 **Susumu Kitagawa**、**Omar M. Yaghi**——yaml/关系表必须用这两形式，防分裂 stub |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q23073819（回填库内 #3755） | ✅ |
| name_zh | 理查德·罗布森 | ✅ |
| name_en | Richard Robson（库内精确形式） | ✅ |
| birth_date | 1937-06-04 | ✅ |
| death_date | （在世，留空） | ✅ |
| nationality | United Kingdom（rank 0）+ Australia（rank 1） | ✅ |
| primary_occupation | chemist（UPD 时由 stub 的 mathematician 更正） | ✅ |
| field_of_work | coordination polymers / metal-organic frameworks / inorganic chemistry / crystal engineering（person_field 带 rank） | ✅ |
| has_biography | false（立传完成后再置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 合作者 / 家庭 / 共同得主**（全部为 page.md 正文或 infobox 明载）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | John Alfred Barltrop | 师→生（博士导师） | Oxford Dyson Perrins Laboratory，有机光化学博士（1962） |
| advisor-student | Henry Taube | 师→生（博士后导师） | 1964–1965 Stanford 博士后；库内既有记录 Henry Taube #3750 |
| colleague | Bernard F. Hoskins | 无向 | 1989/1990 JACS 奠基论文共同作者 |
| colleague | Stuart R. Batten | 无向 | 1998 Interpenetrating Nets 综述共同作者 |
| parent-child | Naomi Robson | 父→女 | 女儿，前电视主持人 |
| co-honored | Susumu Kitagawa | 无向 | 2025 诺贝尔化学奖共同得主 |
| co-honored | Omar M. Yaghi | 无向 | 2025 诺贝尔化学奖共同得主 |

> **禁入库名单**：metadata.json 与正文一致，无额外 metadata-only 人名。Henry Taube 走库内既有记录（#3750，勿新建 stub）。

## 8. 奖项清单

- Burrows Award, Royal Australian Chemical Institute 无机化学分部（1998）
- Fellow of the Australian Academy of Science, FAA（2000）
- Fellow of the Royal Society, FRS（2022）
- Nobel Prize in Chemistry（2025，三人共享）

## 9. 机构清单

- 教育：Brasenose College, University of Oxford（BA 1959、DPhil 1962；Dyson Perrins Laboratory）
- 博士后：California Institute of Technology（1962–1964）；Stanford University（1964–1965，Henry Taube 组）
- 任职：University of Melbourne（1966 年起讲师，终身效力）
- 代表论文：Hoskins & Robson, JACS 1989；Hoskins & Robson, JACS 1990；Batten & Robson, Angew. Chem. 1998

## 10. 终审清单

- [ ] 生卒 1937-06-04 / 在世，出生地 Glusburn
- [ ] 2025 三人共享表述准确；三人分工（概念/柔性/系统化）无张冠李戴
- [ ] 博士导师 Barltrop（Oxford）与博士后导师 Taube（Stanford）区分准确
- [ ] 1974 木模型灵感；1989 与 1990 两篇论文年份准确
- [ ] 国籍英/澳双值；女儿 Naomi Robson 按页面口径
- [ ] yaml name_en=Richard Robson 走 UPD #3755 回填 QID
- [ ] 无引语杜撰；"pioneer" 保留 described as 归属
- [ ] 品牌 OpenMathAI；表格语义化 + 公式框 + 节点连线背景

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 `pages/Richard_Robson_chemist/page.md` 逐页对照 Beamer tex 全部事实
- [ ] 头像核对（三人合影图注或装饰圆占位）
- [ ] 引语核对：仅 "described as 'a pioneer...'" 一处，其余不得出现引号原话
- [ ] 编译验证：`make distclean && make` 0 错误
- [ ] Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] Overfull/Underfull 检查（vbox ≤10pt、hbox ≤50pt）
- [ ] 身份信息页布局与 Sanger 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐

---

> **名单状态**：`chemist/generate_21th_century_list.py` 由主控统一收尾，本文件不改动清单脚本。
