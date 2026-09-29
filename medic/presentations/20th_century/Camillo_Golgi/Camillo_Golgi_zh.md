# 医学家立传提示词（Camillo Golgi）

> **OpenMedic** 项目 · 20 世纪诺贝尔生理学或医学奖 **1906 年**得主（与 Santiago Ramón y Cajal 共享）。
> 本文件是 Golgi 的「人物专属立传提示词」，供后续 Beamer 立传 agent 直接使用；配套数据已按第三、四节入库 greatminds 库。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Camillo Golgi（1843-07-07 ~ 1926-01-21，享年 82 岁），意大利生物学家、病理学家
- **气质关键词**：**黑色反应的发明者、高尔基体的发现者、网状学说的坚守者** —— 1906 诺贝尔生理学或医学奖获奖理由（官方原文，逐字引用）：
  > "in recognition of their work on the structure of the nervous system"（因其对神经系统结构的研究）
- **设计母题**：**银染的星丛（silver-stained constellation）**。黑色反应让极少数神经细胞在黄色背景上被银铬沉淀染成完整的黑色剪影——「随机少数、整体呈现」正是 Golgi 染色法的精髓，也是本篇的视觉隐喻：稀疏黑枝网络铺陈于暖黄底色之上。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Camillo_Golgi/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `Physicist_Bio_Prompt_Template.md` 第三章八步流程：下载核对 → 建目录 → 复制 Makefile → 收集图片 → 研究领域入库 → 社会关系入库 → 编写 Beamer → 布局检查 + 史实审查。
> **第 0/1/2/3 步按 medic 路径执行**：页面用 `medic/presentations/pages/20th_century/Camillo_Golgi/`（page.md 已就位）；Makefile 复制后设 `MAIN=Camillo_Golgi_zh`；BGM 复制到本目录（见第九节）。
> 数据库两步（第 4/4.5 步）**已完成**，见第三、四节；执行 agent 只需做 Beamer 与目检。

## 三、研究领域梳理 + 入库 【已入库，与 yaml 完全一致】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | neuroscience | 神经科学 | 1906 诺奖核心：神经系统结构 | 核心页 |
| 1 | histology | 组织学 | 黑色反应/高尔基染色法（1873） | 染色法页 |
| 2 | pathology | 病理学 | 帕维亚病理解剖学教授、曾任帕维亚医学院病理所负责人 | 任职页 |
| 3 | malaria | 疟疾 | 三日疟/间日疟分型、高尔基周期（Golgi cycle） | 疟疾页 |
| 4 | cell biology | 细胞生物学 | 1898 发现高尔基体（apparato reticolare interno） | 细胞器页 |

## 四、社会关系梳理 + 入库 【已入库，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Cesare Lombroso | 师→生（博士导师） | 帕维亚大学医学博士导师（1868 精神病病因学论文） |
| advisor-student | Antonio Pensa | 生（Golgi→学生） | 博士生（infobox 明载） |
| influence | Giulio Bizzozero | 无向 | 启发其神经研究；后娶其侄女 Lina Aletti |
| spouse | Lina Aletti | 无向 | Bizzozero 之侄女，无子女，领养侄女 Carolina |
| co-honored | Santiago Ramón y Cajal | 无向 | 1906 诺贝尔生理学或医学奖共享（神经系统结构研究） |
| controversy | Santiago Ramón y Cajal | 无向 | 网状说与神经元学说对立，斯德哥尔摩互不交谈 |
| colleague | Charles Louis Alphonse Laveran | 无向 | 用更优显微镜与染色证实其疟原虫发现 |
| colleague | Ettore Marchiafava | 无向 | 1889-1890 共同描述良性/恶性间日疟差异 |

**方向约定**：`advisor-student` + `direction: advisor` = 对方是导师；`direction: student` = 对方是学生；其余无向（from<to 自动归一）。

## 五、配色方案 【人物专属】

- **气质**：严谨、内敛、银黑与暖黄对比
- **主色**：`#2A4B7C`（深钴蓝，帕维亚学院气质）
- **香槟金**：`#D4B26A`（诺奖色，用于奖项徽章与年份）
- **badgeA-D 四分类色**：
  - `badgeStain` 染色法 — 银灰蓝 `#5B7EA6`
  - `badgeNeuro` 神经结构 — 墨黑 `#2B2B2B`
  - `badgeMalaria` 疟疾 — 疟原虫酒红 `#7A2E2E`
  - `badgeCell` 细胞器 — 琥珀 `#C98A2D`
- **背景母题**：暖黄底（`#E8DAB2!20`）上稀疏的黑色枝状网络（细线 + 端点小圆），呼应黑色反应下神经元在黄背景上的黑色剪影。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 神经结构之光 / Camillo Golgi 1843–1926 + 四色 badge + 右上肖像 + 国籍行（Italy）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地 Corteno、帕维亚、师承 Lombroso/Bizzozero、任职、荣誉）
03  核心贡献概览 — 黑色反应 / 网状学说 / 高尔基体 / 疟疾研究
04  早年与帕维亚求学 (1843–1872) — Corteno 出生、帕维亚医学博士 1868、Lombroso 门下
05  阿比亚泰格拉索的厨房实验室 (1872–1875) — 慢性病院首席医官、废旧厨房改建实验室、1873 黑色反应
06  黑色反应：la reazione nera（核心贡献页）— 重铬酸钾硬化 + 硝酸银染色、随机整体呈现单个神经元
07  网状学说 vs 神经元学说 — Gerlach 原初网络、Golgi 弥散神经网、Cajal 用同法反证
08  神经结构诸发现 — 小脑/海马/脊髓首述、1878 高尔基腱器官、Golgi-Mazzoni 小体
09  高尔基体 (1898) — 鸮小脑浦肯野细胞、锇-重铬酸盐染色、被斥为染色伪影、50 年后电镜证实
10  疟疾研究 — 证实 Laveran 疟原虫、三日疟/间日疟分型、1886 高尔基周期、1898 按蚊传播确认
11  帕维亚的治校岁月 — 1875 组织学教席、两任校长 (1893-96, 1901-09)、1900 参议员
12  1906 诺贝尔奖 — 与 Cajal 共享、斯德哥尔摩获奖致辞（仍坚守网状说）
13  荣誉与身后 — Pour le Mérite (1914)、多校荣誉博士、帕维亚雕像/故居/博物馆、小行星 6875
14  遗产：以 Golgi 命名的世界 — 高尔基体/腱器官/染色法/高尔基 I·II 型细胞
15  结尾
```

## 七、特殊陷阱表 【★ 核心，从 page.md 提炼】

| 陷阱 | 说明 |
|------|------|
| 生卒日 | 1843-07-07 生于 Corteno（当时属奥属伦巴第-威尼西亚），1926-01-21 卒于帕维亚；出生村庄今名 Corteno Golgi |
| 获奖理由 | 官方口径 "in recognition of their work on the structure of the nervous system"，用 **their**（共享）；勿写 Golgi 单独获奖 |
| 网状学说立场 | Golgi 1906 诺奖演讲仍在为网状学说辩护——获奖者本人的学说是错的（Cajal 对），表述时勿回避也勿嘲弄 |
| 博士导师 | page.md 正文与 infobox 双处明载 **Cesare Lombroso**（犯罪心理学名家）；勿与启发者 Giulio Bizzozero 混淆 |
| Bizzozero 身份 | 是启发者 + 同楼居住的挚友 + 岳叔（娶其侄女 Lina），非博士导师 |
| 妻子 | Lina Aletti，无子女，领养 Golgi 的侄女 Carolina；有载可写 |
| 高尔基体的曲折 | 1898 发现后长期被斥为染色伪影、1930s 几乎被弃，电镜时代才被确证——「50 年的冤案」是叙事亮点 |
| 疟疾贡献归属 | Laveran 1880 首先发现疟原虫；Golgi 的贡献是**确证 + 分型 + 高尔基周期**，勿写成 Golgi 发现疟原虫 |
| 学生 Pensa | Antonio Pensa 仅 infobox 明载，正文无展开；metadata 无其他学生信息一律不入库 |
| 与 Cajal 关系 | "came to hate each other and would not speak"——page.md 明载；斯德哥尔摩 Cajal 致意而 Golgi 未回礼，可写 |

## 八、术语清单 【6-10 条】

| 英文 | 中文 | 风险点 |
|------|------|------|
| black reaction / Golgi's method | 黑色反应 / 高尔基染色法 | la reazione nera；1873 年发明 |
| Golgi apparatus | 高尔基体 | 原名 apparato reticolare interno（内网器） |
| Golgi tendon organ | 高尔基腱器官 | 1878 发现的肌张力感受器 |
| reticular theory | 网状学说 | 脑为连续神经纤维网；后被神经元学说取代 |
| neuron doctrine | 神经元学说 | Cajal 立场；两者对立勿混 |
| Golgi cycle | 高尔基周期 | 疟原虫红细胞内无性生殖周期（1886） |
| tertian / quartan fever | 间日疟 / 三日疟 | 分别由 P. vivax / P. malariae 引起 |
| silver chromate | 铬酸银 | 黑色沉淀的化学本质 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**SEA** — Alex-Productions（manifest 预分配）
- **风格**：辽阔 / 沉静 / 探索感
- **匹配理由**：黑色反应让人类第一次「看见」大脑深处的神经网络——如同展开一片从未涉足的内海；SEA 的辽阔沉静匹配 Golgi 在废弃厨房里独自铺开神经星丛的孤独探索，也匹配其网状说「连续之网」的意象。
- **本地路径**：`music_audio/` 下 SEA 曲目 → 复制为 `presentations/20th_century/Camillo_Golgi/SEA.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐 15 页时长。
