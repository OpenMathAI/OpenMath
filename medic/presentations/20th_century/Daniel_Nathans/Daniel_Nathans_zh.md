# 医学家立传提示词（Daniel Nathans）

> **OpenMedic** 项目 · 20 世纪诺贝尔生理学或医学奖 **1978 年**得主（与 Werner Arber、Hamilton O. Smith 三人共享）。
> 本文件是 Nathans 的「人物专属立传提示词」，供后续 Beamer 立传 agent 直接使用；配套数据已按第三、四节入库 greatminds 库。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Daniel Nathans（1928-10-30 ~ 1999-11-16，享年 71 岁），美国微生物学家
- **气质关键词**：**DNA 切割作图的第一人、约翰霍普金斯的中流砥柱、九个孩子中最小的移民之子** —— 1978 诺贝尔生理学或医学奖获奖理由（官方原文，逐字引用）：
  > "for the discovery of restriction enzymes and their application to problems of molecular genetics"（因其发现限制性内切酶及其在分子遗传学问题上的应用）
- **设计母题**：**酶切地图（the restriction map）**。用限制酶把 DNA 切成片段再拼出物理图谱——以「被剪成数段再连线复原的双链地图」作为视觉隐喻。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Daniel_Nathans/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `Physicist_Bio_Prompt_Template.md` 第三章八步流程：下载核对 → 建目录 → 复制 Makefile → 收集图片 → 研究领域入库 → 社会关系入库 → 编写 Beamer → 布局检查 + 史实审查。
> **第 0/1/2/3 步按 medic 路径执行**：页面用 `medic/presentations/pages/20th_century/Daniel_Nathans/`；Makefile 复制后设 `MAIN=Daniel_Nathans_zh`；BGM 复制到本目录（见第九节）。
> 数据库两步（第 4/4.5 步）**已完成**，见第三、四节；执行 agent 只需做 Beamer 与目检。

## 三、研究领域梳理 + 入库 【已入库，与 yaml 完全一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | microbiology | 微生物学 | 1978 诺奖核心、约翰霍普金斯微生物系主任 | 核心页 |
| 1 | molecular biology | 分子生物学 | 限制酶作图应用 | 核心页 |
| 2 | physiology | 生理学 | 页面职业口径 | 早年页 |
| 3 | medicine | 医学 | 华盛顿大学 MD（1954）、肿瘤化疗临床起点 | 早年页 |

## 四、社会关系梳理 + 入库 【已入库，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Werner Arber | 无向 | 1978 诺贝尔生理学或医学奖三人共享（限制酶） |
| co-honored | Hamilton O. Smith | 无向 | 1978 诺贝尔生理学或医学奖三人共享（限制酶） |
| colleague | Fritz Albert Lipmann | 无向 | 1959 入其洛克菲勒研究所实验室任研究助理 |
| spouse | Joanne Gomberg | 无向 | 正文图载 |

**方向约定**：无向关系 from<to 自动归一。

## 五、配色方案 【人物专属】

- **气质**：大萧条移民家庭的坚韧、临床医生转型的沉稳、作图者的条理
- **主色**：`#5C4A21`（作图土金，酶切图谱与纸张）
- **香槟金**：`#D4B26A`（诺奖色）
- **badgeA-D 四分类色**：`badgeMap` 酶切作图 — 图谱金 `#8C6A1E`；`badgeRestr` 限制酶 — 剪刀红 `#A33A2E`；`badgeJHU` 约翰霍普金斯 — 学院蓝 `#2E5E7E`；`badgeMyeloma` 骨髓瘤蛋白研究 — 肿瘤紫 `#4A3560`
- **背景母题**：米白底上被剪成片段的双链与虚线复原连线，错落铺陈成图。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — DNA 的制图师 / Daniel Nathans 1928–1999 + 四色 badge + 右上肖像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Wilmington、特拉华/华盛顿大学、约翰霍普金斯、荣誉）
03  核心贡献概览 — 限制酶作图 / 约翰霍普金斯微生物系 / McKusick-Nathans 研究所 / 分子生物学新时代
04  九个孩子的最小一个 (1928–1954) — 俄国犹太移民家庭、大萧条家道中落、特拉华化学 BS 1950、华盛顿大学 MD 1954
05  临床起点与 NC I (1954–1959) — Robert Loeb 病房实习、NCI 临床联合员、浆细胞瘤与蛋白合成
06  洛克菲勒 Lipmann 实验室 (1959–1962) — 全职研究转折点
07  约翰霍普金斯 (1962–1999) — 微生物学助理教授→教授 1967→系主任 1972、1982 改名分子生物学与遗传学系
08  Smith 的 HindII 与作图构想 — 1970 Smith 分离首个 II 型酶；Nathans 立即将其变成作图工具
09  限制酶作图（核心贡献页）— 将 HindII 变作图工具、restriction mapping、分子遗传学通用方法
10  1976-1978 连捷 — NAS 分子生物学奖 1976、1978 三人诺奖
11  大学教授与 HHMI (1982–) — 霍普金斯大学教授、HHMI 高级研究员
12  临危受命 (1995–1996) — 约翰霍普金斯大学代理校长
13  1993 国家科学奖章 — 与 1999 McKusick-Nathans 遗传医学研究所命名
14  遗产与身后 — 作图法成基因组时代前置技术、1999-11-16 卒于巴尔的摩
15  结尾
```

## 七、特殊陷阱表 【★ 核心，从 page.md 提炼】

| 陷阱 | 说明 |
|------|------|
| 生卒日 | 1928-10-30 生于 Wilmington, Delaware；1999-11-16 卒于 Baltimore, Maryland，享年 71 |
| 获奖理由 | "for the discovery of restriction enzymes and their application to problems of molecular genetics"——**their**；本页亦提及其应用方向为 **restriction mapping**（限制酶作图） |
| 三人分工 | Arber 理论化、Smith 分离 HindII、Nathans 作图应用——本篇强调「作图应用」一侧 |
| 页面口径注意 | 本页未载具体作图对象（如病毒名）——幻灯片不得写 page.md 之外的实验细节，一律用「限制酶作图」口径 |
| Loeb 关系 | 实习/住院医均在 Robert Loeb 病房——临床意味但信息单薄，不建边，此处注明 |
| Lipmann 关系 | 1959 入其洛克菲勒研究所实验室任 research associate——用 colleague（非学位师承）；沿用库内 id=6028 |
| 家庭 | 九个孩子中最小、俄裔犹太移民家庭、大萧条中父亲失业——早年叙事可用；妻 Joanne Gomberg（图载）；子 Benjamin Nathans——不建 parent-child 边 |
| 荣誉链 | 1967 Selman Waksman 微生物学奖（与本批 Waksman 遥相呼应）→ 1976 NAS 分子生物学奖 → 1978 诺奖 → 1993 国家科学奖章 |
| 无引语 | 本页正文无直接引语——引号内不得出现「原话」 |
| 机构遗产 | 1999 年霍普金斯设 McKusick-Nathans 遗传医学研究所（以其与 McKusick 命名）——McKusick 不建边（命名并列非直接关系），此处注明 |

## 八、术语清单 【6-10 条】

| 英文 | 中文 | 风险点 |
|------|------|------|
| restriction enzyme | 限制性内切酶 | 诺奖理由核心词 |
| restriction mapping | 限制酶作图 | 其应用方向 |
| HindII | HindII 限制酶 | Smith 1970 分离的首个 II 型酶 |
| plasma-cell tumor | 浆细胞瘤 | NCI 时期研究对象 |
| multiple myeloma | 多发性骨髓瘤 | 类比人类疾病 |
| Howard Hughes Medical Institute | 霍华德·休斯医学研究所 | 1982 起高级研究员 |
| McKusick-Nathans Institute | McKusick-Nathans 遗传医学研究所 | 1999 年设立 |
| interim president | 代理校长 | 1995-96 霍普金斯 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Falling Apart** — Alex-Productions（manifest 预分配）
- **风格**：解构 / 深沉 / 张力
- **匹配理由**：把完整基因组「切开再看清」——Falling Apart 的解构意象正是限制酶作图的音乐化：先落刀分段，再拼出真相（第二次使用该曲，首用 Joliot-Curie 夫妇，同为切分与重组的叙事）。
- **本地路径**：`music_audio/` 下 Falling Apart 曲目 → 复制为 `presentations/20th_century/Daniel_Nathans/Falling_Apart.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐 15 页时长。

