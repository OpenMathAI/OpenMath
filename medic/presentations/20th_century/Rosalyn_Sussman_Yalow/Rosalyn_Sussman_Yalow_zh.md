# 医学家立传提示词（Rosalyn Sussman Yalow）

> **OpenMedic** 项目 · 20 世纪诺贝尔生理学或医学奖 **1977 年**得主（独享一半，Guillemin/Schally 共享另一半）。
> 本文件是 Yalow 的「人物专属立传提示词」，供后续 Beamer 立传 agent 直接使用；配套数据已按第三、四节入库 greatminds 库。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Rosalyn Sussman Yalow（1921-07-19 ~ 2011-05-30，享年 89 岁），美国医学物理学家
- **气质关键词**：**放射免疫测定法（RIA）的发明者、第二位医学诺奖女性、拒绝专利的测量革命者** —— 1977 诺贝尔生理学或医学奖获奖理由（官方原文，逐字引用）：
  > "for the development of radioimmunoassays of peptide hormones"（因其开发肽类激素的放射免疫测定法）
- **设计母题**：**看不见的量尺（a ruler for the invisible）**。RIA 让此前不可测的痕量物质变得可测——以「放射衰变刻度尺量出血液中的微量圆点」作为视觉隐喻。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Rosalyn_Sussman_Yalow/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `Physicist_Bio_Prompt_Template.md` 第三章八步流程：下载核对 → 建目录 → 复制 Makefile → 收集图片 → 研究领域入库 → 社会关系入库 → 编写 Beamer → 布局检查 + 史实审查。
> **第 0/1/2/3 步按 medic 路径执行**：页面用 `medic/presentations/pages/20th_century/Rosalyn_Sussman_Yalow/`；Makefile 复制后设 `MAIN=Rosalyn_Sussman_Yalow_zh`；BGM 复制到本目录（见第九节）。
> 数据库两步（第 4/4.5 步）**已完成**，见第三、四节；执行 agent 只需做 Beamer 与目检。

## 三、研究领域梳理 + 入库 【已入库，与 yaml 完全一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | medical physics | 医学物理学 | 1977 诺奖核心：RIA 放射同位素示踪 | 核心页 |
| 1 | endocrinology | 内分泌学 | 胰岛素测量起点、内分泌诊断革命 | 研究页 |
| 2 | nuclear medicine | 核医学 | 布朗克斯 VA 医院放射性同位素实验室 | 任职页 |

## 四、社会关系梳理 + 入库 【已入库，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Roger Guillemin | 无向 | 1977 诺奖同届共享（其一半为肽类激素脑内生产研究） |
| co-honored | Andrew V. Schally | 无向 | 1977 诺奖同届共享（其一半为肽类激素脑内生产研究） |
| colleague | Solomon Berson | 无向 | VA 医院搭档，共同发明 RIA；Berson 1972 早逝未及诺奖 |
| influence | Mildred Dresselhaus | 无向 | 亨特学院执教时引其放弃小学教职转向科研 |
| spouse | A. Aaron Yalow | 无向 | 1943-06 结婚，二子；1992 卒 |

**方向约定**：无向关系 from<to 自动归一。

## 五、配色方案 【人物专属】

- **气质**：纽约布朗克斯的坚韧、放射性测量的精密、女性拓荒者的锋芒
- **主色**：`#6E1E5C`（放射性紫红，盖革计数器与示踪）
- **香槟金**：`#D4B26A`（诺奖色）
- **badgeA-D 四分类色**：`badgeRIA` 放射免疫测定 — 示踪紫 `#6E1E5C`；`badgeTrace` 放射性同位素 — 辐射橙 `#D07B2A`；`badgeHormone` 激素测量 — 内分泌青 `#1B7A6B`；`badgeBronx` 布朗克斯岁月 — 城市灰蓝 `#4E6478`
- **背景母题**：浅紫底上放射衰变刻度线与微量样品小圆，错落连缀成测量曲线。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 测量不可见之人 / Rosalyn Sussman Yalow 1921–2011 + 四色 badge + 右上肖像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、布朗克斯、亨特/伊利诺伊、VA 医院/西奈山、荣誉）
03  核心贡献概览 — RIA / 胰岛素测量 / 拒绝专利 / 内分泌学遗产
04  布朗克斯的女儿 (1921–1941) — 犹太家庭、亨特学院免费女校、母亲期望教师而她选物理
05  秘书桌上的科学梦 — Schoenheimer/Heidelberger 秘书、打字与速记的代价
06  伊利诺伊的 400 分之一 (1941–1945) — 工程学院唯一女性、1917 年来第一人、战时机遇、1945 博士
07  亨特讲台与 VA 起点 (1946–1950) — 回母校执教、影响 Dresselhaus、1947 VA 顾问
08  放射性同位素实验室 (1950) — 布朗克斯 VA 自建实验室、全职科研转折
09  与 Berson 共创 RIA (1950s–1960)（核心贡献页）— 胰岛素抗体结合、痕量测量、1960 论文
10  拒绝专利 — 「商业潜力巨大」仍不申请专利——科学的公共性
11  1972 双重时刻 — Berson 去世、Midleton 奖与 Koch 奖；1975 AMA 奖追及 Berson
12  1977 诺贝尔奖 — 独享一半（RIA）、Guillemin/Schally 共享另一半、第二位医学诺奖女性
13  「首位」的精确表述 — Gerty Cori 之后第二位、美国本土出生第一位
14  遗产：从 exendin-4 到 GLP-1 — 学生 John Eng 的 Gila 毒液发现、Exenatide 2005 获批、内分泌学之母
15  结尾
```

## 七、特殊陷阱表 【★ 核心，从 page.md 提炼】

| 陷阱 | 说明 |
|------|------|
| 生卒日 | 1921-07-19 生于纽约布朗克斯；2011-05-30 卒于布朗克斯，享年 89 |
| 获奖理由 | "for the development of radioimmunoassays of peptide hormones"——**her 独享一半**；Guillemin/Schally 共享另一半且理由不同（肽类激素脑内生产），勿混写 |
| Berson 悲剧 | RIA 与 Solomon Berson 共同开发，但 Berson 1972 早逝（诺奖不追授）——1975 AMA 奖追及其名；叙事核心张力 |
| 拒绝专利 | 正文明载两人拒绝申请专利——科学公共性亮点 |
| 女性议题两面 | 她回避女性科学组织、反对特殊待遇（有原话 "It bothers me..."），又倡导更多女性进入科学——按正文两面呈现，勿标签化 |
| 「首位」表述 | 第二位医学诺奖女性（Gerty Cori 之后）、第一位美国本土出生女性、第六位个体女性诺奖（算居里两度则第七）——三重口径精确使用 |
| 引语 | 正文原话：童年物理志向句、女性组织 "It bothers me..." 句——引语仅用这些 |
| 秘书经历 | 曾任 Schoenheimer/Heidelberger 秘书（打字/速记）——时代壁垒注脚，**不是师承**，不建边 |
| 学生遗产线 | 学生 John Eng 1992 发现 exendin-4 → Exenatide 2005 获批（首个 GLP-1 受体激动剂）——RIA 传承的当代回响 |
| 家庭 | 1943-06 嫁同学 Aaron Yalow（拉比之子），二子 Benjamin/Elanna，持 kosher 家庭；不建 parent-child 边 |

## 八、术语清单 【6-10 条】

| 英文 | 中文 | 风险点 |
|------|------|------|
| radioimmunoassay (RIA) | 放射免疫测定法 | 诺奖理由核心词 |
| peptide hormone | 肽类激素 | RIA 首测对象 |
| radioisotope tracing | 放射性同位素示踪 | 技术原理 |
| insulin antibody binding | 胰岛素抗体结合 | RIA 发现起点 |
| endocrinology | 内分泌学 | 「内分泌学之母」称号 |
| hepatitis screening | 肝炎筛查 | RIA 血液筛查应用 |
| exendin-4 | 艾塞那肽-4 | 学生 Eng 自 Gila 毒液发现 |
| GLP-1 receptor agonist | GLP-1 受体激动剂 | Exenatide 开启的药物类 |
| Veterans Administration | 退伍军人管理局医院 | 其研究主场 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Pathfinder** — Alex-Productions（manifest 预分配）
- **风格**：开拓 / 坚毅 / 先行者气质
- **匹配理由**：从「 respectable 学院不收女性」的自我怀疑到为医学装上测量痕量的标尺——Pathfinder 的开拓者气质正是 Yalow 一生的注脚：400 分之一的女性、第二位医学诺奖女性、RIA 的开路先锋。
- **本地路径**：`music_audio/` 下 Pathfinder 曲目 → 复制为 `presentations/20th_century/Rosalyn_Sussman_Yalow/Pathfinder.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐 15 页时长。

