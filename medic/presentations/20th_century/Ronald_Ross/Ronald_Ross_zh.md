# 医学家立传提示词（Ronald Ross）

> OpenMedic 项目 · 20 世纪诺贝尔生理学或医学奖 1902 年得主 · 本文件是该人物的专属立传提示词，
> 按 9 节结构执行 Beamer 立传；数据库入库（fields/relations）已由批次完成，本文件第四/三节与 yaml 一致。

## 一、背景信息 【人物专属】

- **目标医学家**：Sir Ronald Ross（1857-05-13 生于英属印度 Almora ~ 1932-09-16 逝于伦敦，享年 75 岁）
- **气质关键词**：**疟疾蚊传机制的证明者、热带医学巨擘、跨界的诗人数学家（polymath）** —— 1902 年获奖理由（逐字引用 medic/nobel_medicine_citations.json）：
  > "for his work on malaria , by which he has shown how it enters the organism and thereby has laid the foundation for successful research on this disease and methods of combating it"
  > （因其对疟疾的研究——阐明了疟原虫如何进入机体，从而为该病的成功研究与防治方法奠定基础）
- **设计母题**：**蚊翼网纹与血涂片（dappled wings & blood smear）**。显微镜视野中的疟原虫、按蚊翅上的斑纹、笔记本里的诗行——微观与文学的双重质感。
- **本地 Wikipedia 路径**：medic/presentations/pages/20th_century/Ronald_Ross/page.md
- **参考模板**：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）

## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章）

- 第 0/1/2/3 步按 **medic 路径**执行：事实基准 = `medic/presentations/pages/20th_century/Ronald_Ross/page.md`；目录 `medic/presentations/20th_century/Ronald_Ross/`；Makefile 改 `MAIN=Ronald_Ross_zh`；肖像优先 images.txt 所列 Commons 图（Ross, 20.Aug.1897 等），失败用装饰圆占位。
- 第 4/4.5 步（入库）**已完成**（第三、四节与 `MySQL/data/Ronald_Ross.yaml` 一致，勿重复入库）。
- 第 5-9 步：配色 → 幻灯片 → Beamer → 布局检查（0 error、vbox≤10pt、hbox≤50pt、逐页目检）→ 史实审查（第七节）。

## 三、研究领域梳理 + 入库（rank 0-4 表）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | malariology | 疟疾学 | 蚊传疟疾完整生命周期证明 | 发现页 |
| 1 | parasitology | 寄生虫学 | 疟原虫在蚊体内的发育 | 核心页 |
| 2 | epidemiology | 流行病学 | 疟疾数学流行病学模型（1908 毛里求斯起） | 数理页 |
| 3 | tropical medicine | 热带医学 | 利物浦热带医学院教授/主席 | 伦敦页 |

## 四、社会关系梳理 + 入库（与 yaml 完全一致，已完成）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | Patrick Manson | — | 疟疾研究导师（mentor），1894 相识后长期指导 |
| controversy | Giovanni Battista Grassi | — | 疟疾传播优先权之争，互指对方 |
| collaborator | Hilda Phoebe Hudson | — | 疟疾流行病学数学模型合作（1915-1917 论文） |
| spouse | Rosa Bessie Bloxam | — | 1889 结婚，1931 去世 |
| parent-child | Campbell Claye Grant Ross | 父→本人 | 父，英属印度陆军将军 |

> 对手方规范名：本篇对手方均无库内记录，按 page.md 形式新建 stub；`Patrick Manson`/`Giovanni Battista Grassi` 全篇统一此形式。

## 五、配色方案

- **气质**：英属印度的酷热与执拗、显微镜下的孤独坚持、诗人的浪漫
- **主色**：热带丛林绿 `#146B5A`（热带医学与恒河平原）
- **诺奖香槟金**：`#D4AF37`
- **badge 四分类色**：
  - `badgeA` 疟疾蚊传发现 — 疟原虫红 `#A63A2B`
  - `badgeB` 印度医局岁月 — 土黄 `#B07B3F`
  - `badgeC` 数理流行病学 — 石板蓝 `#3D5A80`
  - `badgeD` 文学与诗作 — 暮紫 `#5E4B8B`
- **背景母题**：稀疏蚊翼斑纹（半透明菱形网纹）与圆形视野（显微镜目镜），低透明度铺陈。

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 疟疾蚊传机制的证明者 / Ronald Ross 1857–1932 + 四色 badge + 右上头像 + 国籍行（United Kingdom）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地 Almora、St Bartholomew's、印度医局 25 年、利物浦、诺奖 1902）
03  核心贡献概览 — 蚊传疟疾 / 鸟疟模型 / 数理流行病学 / 热带医学建制
04  早年：印度出生的多才少年 (1857–1881) — 将门长子十兄妹、8 岁回英、诗歌数学绘画、St Bartholomew's 1874（父命学医）
05  印度医局 (1881–1894) — Madras/Bangalore 等地轮驻、1883 班加罗尔控蚊设想、1888-89 回英随 E. E. Klein 学细菌学
06  相遇 Manson (1894–1895) — 1894-04-10 伦敦初见、Manson 的蚊子疟疾假说与"印度是最佳研究地"信念
07  1897-08-20：显微镜下的决定性一天 — Husein Khan 8 annas 粒粒雇喂、"dappled-winged"（按蚊）、蚊胃中疟原虫；发现日诗作（page.md 有英文原诗可引，节选 4 行）
08  加尔各答与鸟疟 (1898) — Manson 劝用鸟模型、Culex 唾液腺 7 月、麻雀传疟完整生命周期
09  诺奖与公案 (1902) — 官方理由全句；委员会原拟 Ross/Grassi 分享、Ross 指控舞弊、Koch 仲裁倾斜（客观呈现）
10  利物浦与全球灭蚊 (1899–1912) — 热带医学院讲师→教授主席（1902-1912）、西非/苏伊士/希腊/毛里求斯
11  数理流行病学 — 1908 毛里求斯报告、《The Prevention of Malaria》1910、1915/16 皇家学会论文（与 Hilda Hudson）
12  晚年与 Ross 研究所 (1917–1932) — 战争部疟疾顾问、1926 Ross Institute 主任直至去世
13  荣誉与个性 — FRS 1901、KCB 1911、Cameron 1902、Albert Medal 1923、Manson Medal 1929、James Tait Black 1923（自传）；"冲动天才"与其终身论战性格（page.md 明载，客观一句）
14  遗产：世界蚊子日 — 8 月 20 日 World Mosquito Day、LSHTM 门楣 23 人之一、加尔各答纪念牌
15  结尾（OpenMathAI 品牌口径）
```

## 七、特殊陷阱表（★ 核心）

| 陷阱 | 说明 |
|------|------|
| 获奖事实口径 | 诺奖针对**鸟疟**传播证明（"did not build his concept ... in humans, but in birds"）；勿写成"发现人疟蚊传机制" |
| Manson 关系定性 | page.md 用 "mentor"，非学位导师；入库用 influence，立传勿写"博士导师" |
| Grassi 之争 | 双向冲突：委员会原拟共享、Ross 指控 Grassi 舞弊、Koch 仲裁倾斜；三方事实并列，勿单方叙事 |
| 8 月 20 日 | 1897-08-20 确认蚊胃中疟原虫（次日 21 日确认增殖）；World Mosquito Day 纪念的是 20 日 |
| 鸟疟载体 | 鸟疟实验用的是 **Culex**（库蚊），人疟发现关涉按蚊（Anopheles）；勿混写 |
| kala-azar 失败 | 1898 阿萨姆调查完全失败（误以为蚊传，实为白蛉）；可写为科学诚实的一页，勿隐去 |
| Cameron Prize 年份 | Ross 的 Cameron Prize 是 **1902**（Behring 是 1894、Finsen 是 1904），三人三届勿串 |
| 妻子/子女 | Rosa 1889 结婚 1931 先逝；子 Ronald Campbell 1914 Le Cateau 阵亡——勿与本人卒年混 |
| 政治敏感 | 无；但勿渲染其与 Manson/同事的私人恩怨细节，page.md 有载可客观一句 |
| 出生国别 | 生于英属印度 Almora，国籍按 Nobel 口径 United Kingdom（manifest 一致） |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| malaria | 疟疾 | 蚊传原虫病 |
| Anopheles | 按蚊 | 人疟主要媒介 |
| Culex | 库蚊 | 鸟疟实验媒介 |
| Plasmodium relictum | 鸟疟原虫 | Ross 1898 传播实验对象 |
| kala-azar / visceral leishmaniasis | 黑热病/内脏利什曼病 | 1898 误判，实为白蛉传播 |
| Leishmania donovani | 杜氏利什曼原虫 | 1903 年由 Ross 命名 |
| mosquito-malaria theory | 蚊疟理论 | Manson 假说 → Ross 证明 |
| mathematical epidemiology | 数理流行病学 | Ross 模型（1915/16） |
| World Mosquito Day | 世界蚊子日 | 8 月 20 日 |

## 九、背景音乐选择

- **选定曲目**：**PAST** — Alex-Productions（manifest 预分配）
- **匹配理由**："历史感/深沉"贴合殖民地印度的漫长求索与显微镜下的孤独二十年；比明快曲风更能承载"二十载挫折一日突破"的史诗质感。
- **本地路径**：music_audio/alex-productions PAST 曲目（执行时按 curated_tracks.md 对应文件复制到本目录）。
