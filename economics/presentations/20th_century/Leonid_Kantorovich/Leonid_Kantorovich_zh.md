# 经济学家立传提示词（Leonid Kantorovich）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1975 年得主 Leonid Kantorovich（列昂尼德·康托罗维奇）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Leonid_Kantorovich/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Leonid Vitalyevich Kantorovich（1912-01-19 生于圣彼得堡，俄罗斯帝国 ~ 1986-04-07 逝于莫斯科，享年 74 岁）
- **气质关键词**：**线性规划的奠基者、数学家出身的经济诺奖得主、围城冰路上的计算者**
- **诺奖获奖理由**（1975，与 Tjalling Koopmans 共享，逐字引自 manifest）：
  > "for their contributions to the theory of optimum allocation of resources"（表彰他们对资源最优配置理论的贡献）
- **设计母题**：**最优配置（optimal allocation & linear programming）**——在有限资源约束下寻找最优解，是「冰面上车辆间距的临界计算」的视觉隐喻：等距网格、线性可行域与最优角点构成背景母题。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Leonid_Kantorovich/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/Leonid_Kantorovich/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取——page.md 载有 Petrov-Vodkin 1938 油画肖像与 1976 照片两幅，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Leonid_Kantorovich_zh`、`VIDEO_NAME=Leonid_Kantorovich_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Kantorovich 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | linear programming | 线性规划 | 1939 胶合板厂优化任务中首创，早于 Dantzig 数年 | 核心页 |
| 1 | functional analysis | 泛函分析 | 迭代法收敛的泛函分析处理、Kantorovich 定理与不等式 | 数学页 |
| 2 | mathematical economics | 数理经济学 | 资源最优配置理论、影子价格思想（诺奖理由核心） | 核心页 |
| 3 | approximation theory | 逼近论 | Szász–Mirakjan–Kantorovich 算子 | 数学页 |
| 4 | operator theory | 算子理论 | 赋范向量格（K 空间/Kantorovich 空间） | 数学页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Grigorii Fichtenholz | Fichtenholz → 师 | infobox Doctoral advisor 明载（列宁格勒数学学派） |
| advisor-student | Vladimir Smirnov | Smirnov → 师 | infobox Doctoral advisor 明载（复用库内 id=526，须为数学家 V. I. Smirnov，见陷阱表） |
| advisor-student | Svetlozar Rachev | Kantorovich → 学生 | infobox Doctoral students 明载 |
| advisor-student | Gennadii Rubinstein | Kantorovich → 学生 | infobox Doctoral students 明载 |
| co-honored | Tjalling Koopmans | 无向 | 1975 诺贝尔经济学奖共享（资源最优配置理论；对手方批次 econ20th-batch-03 写反向边） |
| collaborator | Vladimir Ivanovich Krylov | 无向 | 合著《高等分析近似方法》（俄文原著 1936） |

**不入库但提示词可叙述**：George Dantzig 与线性规划系平行独立发展（正文只载"早数年提出"，无直接交往记载）禁建边，仅叙述；父为圣彼得堡执业医生（无具名页与学术类型）；1948 年调入苏联原子项目、围城期间任职 VITU 均为机构经历非人物关系；page.md 图片区含德黑兰美国使馆缴获的 CIA 档案照片——立传仅客观提及可不入正文页。

## 五、配色方案 【人物专属】

- **气质**：精确、冷静、在计划经济的体制内寻找数学的最优解
- **主色**：`#283593`（规划靛蓝——可行域与最优角点的深冷感）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeLP` 线性规划 — 靛蓝 `#283593`
  - `badgeFA` 泛函分析 — 青蓝 `#0E7490`
  - `badgeEcon` 数理经济 — 琥珀 `#C07A2A`
  - `badgeSiege` 围城岁月 — 灰紫 `#52307C`
- **背景母题**：等距网格与线性可行域角点（最优配置抽象），呼应设计母题。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 线性规划的奠基者 / Leonid Kantorovich 1912–1986 + 四色 badge + 右上头像 + 国籍行（Soviet Union）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地圣彼得堡、列宁格勒大学 1926 入学/1930 毕业、
    1934 年 22 岁正教授、师承 Fichtenholz/Smirnov、任职列宁格勒大学/新西伯利亚/苏联科学院、诺奖 1975）
03  核心贡献概览 — 线性规划 1939 / K 空间与泛函分析 / 资源最优配置与影子价格 / Monge–Kantorovich 输运
04  列宁格勒神童 (1912–1934) — 14 岁入列宁格勒大学数学力学系、1930 毕业、22 岁正教授、1935 博士学位
05  线性规划的诞生 (1939) — 政府下达胶合板工业优化任务、《生产计划与组织的数学方法》、影子价格思想
06  泛函分析与 K 空间（数学页）— 赋范向量格、Kantorovich 定理与不等式、牛顿法与梯度法收敛率
07  围城冰路上的计算 (1941–1942) — 生命之路卡车间距公式、亲自步行冰面核验、卫国勋章与保卫列宁格勒奖章
08  战后岁月 (1948–1960) — 斯大林奖 1949、列宁奖、苏联科学院
09  新西伯利亚 (1960–) — 创建新西伯利亚大学计算数学教研室并主持
10  1975 诺贝尔奖 — 与 Koopmans 共享"资源最优配置理论"、苏联体制内诺奖得主的特殊处境（客观一句）
11  与 Dantzig 的平行发展 — 1939 vs 1940s、两个阵营独立提出线性规划、禁写成"谁抄谁"
12  输运问题与现代回响 — Monge–Kantorovich 输运问题、Kantorovich–Rubinstein 度量、概率论弱收敛应用
13  荣誉与门生 — Rachev/Rubinstein、Krylov 合著教科书
14  遗产与结尾 — 线性规划与最优化方法的现代格局 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 身份口径 | page.md 开篇称 "Soviet mathematician and economist"、infobox Discipline: Mathematics——本篇 primary_occupation 按 page.md 取 **mathematician**、occupations 首条 mathematician（经济学家身份在 fields 与叙事中体现），Review 勿误判 |
| 生日两说 | frontmatter 双值 1912-01-19 / 1912-01-15；infobox 与正文均作 **1912-01-19**，yaml 取 19 正文值 |
| 双博士导师 | frontmatter 与 infobox 均载 Fichtenholz + Smirnov（正文未展开）——按 infobox 明载入库；**Smirnov 必须复用库内 id=526 'Vladimir Smirnov'（primary_occupation=mathematician）**，Review 须核对该记录确为数学家 Vladimir Ivanovich Smirnov（1887–1974）而非同名者，若有误由主控合并 |
| Dantzig 平行 | 正文只载 Kantorovich 1939 首创、"some years before it was advanced by George Dantzig"——平行独立发展，禁建关系、禁写"被剽窃/谁先谁后"的价值判断 |
| Koopmans 边 | 1975 共享奖 co-honored 对手方 Tjalling Koopmans 属 batch-03；本篇 yaml 用 manifest 名 'Tjalling Koopmans' 建 stub，batch-03 agent UPD 回填——勿改用全名 Tjalling C. Koopmans 防分裂 |
| 围城口径 | 生命之路：计算冰面卡车安全间距并亲自步行核验——按正文客观呈现；"许多运粮车被德机炸毁"如实一句，禁煽情扩写 |
| 原子项目 | 1948 年被调入苏联原子项目——page.md 一句带过，客观记录即可，禁展开军事细节 |
| CIA 档案照片 | page.md 图片区载有德黑兰缴获的 CIA 档案照片——立传可提及其档案价值，禁渲染谍战叙事 |
| 国籍口径 | frontmatter nationality 仅 Soviet Union；出生时为俄罗斯帝国（圣彼得堡）、逝世于苏联莫斯科——yaml 按 manifest 填 Soviet Union 一条，身份页正文注明出生地政权 |
| 引语红线 | 本篇 page.md 无引语节；1939 书名《生产计划与组织的数学方法》等俄文原著名按参考文献转写，禁杜撰其"名言" |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| linear programming | 线性规划 | 1939 首创，勿译"线性规划法"冗余 |
| optimum allocation of resources | 资源最优配置 | 诺奖理由核心词 |
| shadow price | 影子价格 | See also 明载，最优对偶变量思想 |
| K-space (Kantorovich space) | K 空间 | Dedekind 完备向量格，以他命名 |
| Kantorovich theorem | Kantorovich 定理 | 牛顿法收敛的半局部条件，勿与不等式混同 |
| Kantorovich inequality | Kantorovich 不等式 | 梯度法收敛率估计 |
| Kantorovich–Rubinstein metric | K–R 度量 | 即 Wasserstein 度量前身 |
| Monge–Kantorovich problem | 蒙日–康托罗维奇问题 | 最优输运问题 |
| Road of Life | 生命之路 | 列宁格勒围城冰上运输线（本文涉及，与 Leontief 篇勿混） |
| Szász–Mirakjan–Kantorovich operator | 算子 | 逼近论成果，勿漏连字符 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Expedition**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：「远征」对应其一生跨越数学与经济学两个大陆的开拓——从列宁格勒的 K 空间到冰面卡车间距的最优解，再到新西伯利亚的荒原建系，是理性在约束中开路的精神。
- **本地路径**：复制 `music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav` 到 `economics/presentations/20th_century/Leonid_Kantorovich/Expedition.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 十、参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `economics/presentations/pages/20th_century/Leonid_Kantorovich/page.md` | 事实基准（唯一事实来源） |
| `economics/PROMPTS_WORKFLOW.md` | 批量作业手册 |
| `MySQL/data/Leonid_Kantorovich.yaml` | 入库 yaml（与本文第三、四节一致） |
| `economics/economics_list_data.py` / `nobel_economics_citations.json` | 获奖理由中文对照 |

## 十一、执行清单 【模板通用】

1. 读 page.md 建立事实基准（本文件已沉淀，直接核对即可）
2. 下载肖像（page.md 载 Petrov-Vodkin 1938 油画与 1976 照片；images.txt 有 URL 直接用 500px，404 用 Commons `Special:FilePath`，再 404 装饰圆占位）
3. 复制 BGM wav 到人物目录
4. 写 tex（配色按第五节、Slide 序列按第六节）
5. 编译循环：0 error、vbox ≤ 10pt、hbox ≤ 50pt
6. pdftoppm + read_file 逐页目检
7. make images/video；Review-1 修正写回本文件
