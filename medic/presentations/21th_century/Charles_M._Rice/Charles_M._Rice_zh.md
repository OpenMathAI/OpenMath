# 医学家立传提示词（Charles M. Rice）

> OpenMedic 项目、21 世纪诺贝尔生理学或医学奖 2020 年得主（查尔斯·赖斯，丙肝病毒感染性克隆的构建者）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Charles Moen Rice（1952-08-25 生于加州萨克拉门托，在世）
- **气质关键词**：**RNA 病毒的驯兽师、HCV 感染性克隆的构建者、丙肝致病性因果链的补全者** —— 2020 获奖理由（与 Harvey J. Alter、Michael Houghton 三人共享）：
  > "for the discovery of Hepatitis C virus"（因发现丙型肝炎病毒）
- **设计母题**：**让病毒在试管里活过来**。1997 年构建首个 HCV 感染性克隆并在黑猩猩体内验证致病——"第三棒"补齐科赫法则式的因果闭环。视觉隐喻：一支由 RNA 链点亮、在培养皿中活过来的病毒。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Charles_M._Rice/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/21th_century/Charles_M._Rice/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准，裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/21th_century/Charles_M._Rice/`（含 `images/`）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=Charles_M._Rice_zh`、`VIDEO_NAME=Charles_M._Rice_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/21th_century/Charles_M._Rice/images.txt`（2024 诺奖周照）；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/Charles_M._Rice.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | virology | 病毒学 | HCV 感染性克隆，2020 诺奖核心 | 核心页 |
| 1 | RNA viruses | RNA 病毒 | Sindbis 与 RNA 病毒复制研究 | 早年页 |
| 2 | hepatitis C | 丙型肝炎 | 致病性与疫苗靶点研究 | 核心页 |
| 3 | flaviviruses | 黄病毒 | 黄病毒科独立成科的确立 | 早年页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | James Strauss | 导师 | Caltech 生物化学博士导师（1981，Sindbis 病毒结构蛋白研究） |
| co-honored | Michael Houghton (virologist) | 无向 | 2020 诺贝尔生理学或医学奖三人共享（发现丙型肝炎病毒） |
| co-honored | Harvey J. Alter | 无向 | 2020 诺贝尔生理学或医学奖三人共享（发现丙型肝炎病毒） |
| colleague | Ralf F. W. Bartenschlager | 无向 | 2016 Lasker-DeBakey 临床医学研究奖三人共享 |
| colleague | Michael J. Sofia | 无向 | 2016 Lasker-DeBakey 临床医学研究奖三人共享 |

> 在世者、page.md 篇幅所限，relations=5 为诚实值（1 导师 + 2 同享 + 2 Lasker 共享），Review 勿误判缺漏。
> 不入库：Stephen Feinstone（建议其将 RNA 技术转向 HCV——单向建议事件，非持续关系）；实验室成员与编辑职务合作者；ČT24 采访主持人。
> 库内当时无 James Strauss / Ralf F. W. Bartenschlager / Michael J. Sofia 记录，均由本 yaml 新建 stub；Alter/Houghton 由本批各自 yaml 规范化。

## 五、配色方案 【人物专属】

- **气质**：加州阳光的底色 + 病毒实验室的冷调 + 因果闭环的确定感
- **主色**：墨绿 `#2F5D50`（洛克菲勒常春藤与培养皿的沉着）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` 感染性克隆 — 墨绿 `#2F5D50`
  - `badgeB` RNA 病毒与黄病毒 — 钢蓝 `#2E4A66`
  - `badgeC` 丙肝致病性 — 暗红 `#8C2F1B`
  - `badgeD` 编辑与学会 — 琥珀 `#A0722D`
- **背景母题**：一条环状 RNA 链细线（病毒基因组）+ 三段接力刻度（确认→克隆→致病）。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — 让病毒现形的第三棒 / Charles M. Rice 1952– + 四色 badge + 右上头像 + 国籍行 USA
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生 Sacramento、教育 UC Davis BS 1974/
    Caltech MS/PhD 1981、导师 Strauss、任职 Washington Univ./Rockefeller/Cornell、
    荣誉 Nobel 2020/Lasker 2016/NAS 2005、核心领域）
03  核心贡献概览 — RNA 病毒方法学 / 感染性克隆 / HCV 致病性证明 / 学术服务
04  萨克拉门托与 UC Davis (1952–1974) — Sacramento 出生、Rio Americano High School、
    UC Davis 动物学 BS 1974（Phi Beta Kappa）
05  Caltech：Strauss 门下 (1974–1986) — MS/PhD 1981 生物化学、Sindbis 病毒结构蛋白研究、
    RNA 病毒实验室训练、留校四年博后
06  黄病毒科的确立 — 参与 Establish flaviviruses 为独立病毒科、
    其黄热病毒株后来用于黄热疫苗开发——基础分类学的深远回响
07  华盛顿大学岁月 (1986–2001) — 携研究组转 St. Louis、1989 The New Biologist 论文：
    实验室产生感染性黄病毒 RNA——方法学突破
08  Feinstone 的建议 — 研究丙肝病毒的 Feinstone 注意到该技术、
    建议用于丙肝疫苗开发——第三棒的起点
09  1997：首个 HCV 感染性克隆 — 构建首个感染性克隆、黑猩猩实验（病毒 endemic 宿主）
    证明 HCV 单独致病——因果链闭环
10  2005：急性株的实验室复制 — 参与证明人类患者体内急性株可在实验室强制复制、
    HCV 研究的工具箱齐备
11  2016 Lasker → 2020 Nobel — Lasker-DeBakey 临床奖（与 Bartenschlager/Sofia）为前奏、
    2020 与 Alter/Houghton 三人共享诺奖——三人接力合龙
12  荣誉与认可 — Pew 1986、AAAS Fellow 2004、NAS 院士 2005、
    Beijerinck 奖 2007、Robert Koch Prize 2015、Artois-Baillet Latour 2016、Lasker 2016
13  学术服务 — JEM 编辑（2003-07）、Journal of Virology 编辑（2003-08）、
    PLoS Pathogens 编辑（2005-）、ASV 主席（2002-03）、FDA/NIH/WHO 委员会、
    400+ 同行评审论文
14  遗产与现在 — Rockefeller Greenberg 讲席教授（2001 起）、Cornell/WashU 兼职教授、
    丙肝从绝症到可治愈（DAA 时代）的技术地基、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方逐字 "for the discovery of Hepatitis C virus"（三人共享） |
| 三棒分工 | Alter 确认未知病毒存在 → Houghton 鉴定病毒 → **Rice 构建感染性克隆证明其单独致病**——本篇以因果闭环为主线，勿越位 |
| 感染性克隆年份 | 1997 构建 + 黑猩猩实验；2005 急性株实验室复制——两个年份都要出现，勿合并 |
| Feinstone 定位 | 其 1989 The New Biologist 论文引起 Feinstone 注意并**建议**转向 HCV——单向建议、page.md 未载后续私人关系，不入库 |
| 黄热疫苗措辞 | "其使用的黄热病毒株最终被用于黄热疫苗开发"——是株的后续用途，勿写成"Rice 研发黄热疫苗" |
| Lasker 届别 | Rice 的是 2016 Lasker-DeBakey **临床**奖（与 Bartenschlager/Sofia）；Alter/Houghton 的是 2000 临床奖——两届勿混 |
| 编辑职务 | JEM 2003-07 / J Virol 2003-08 / PLoS Pathogens 2005 起——三刊年份勿错位 |
| 学位口径 | UC Davis 动物学 BS（1974，Phi Beta Kappa）；Caltech 生物化学 PhD 1981——勿写成病毒学博士 |
| 在世者关系 | relations=5 为诚实值；与 Alter/Houghton 仅 co-honored 边（page.md 无私人交往记载） |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| infectious clone | 感染性克隆 | 1997 年构建的 HCV cDNA 衍生物 |
| Sindbis virus | 辛德毕斯病毒 | 博士论文对象 |
| flavivirus | 黄病毒 | 科级分类的确立 |
| chimpanzee model | 黑猩猩模型 | HCV endemic 宿主 |
| replicon / replication | 复制子/复制 | 2005 急性株实验 |
| Koch-style causality | 科赫式因果 | 第三棒的逻辑角色 |
| DAA（语境词） | 直接抗病毒药物 | 结尾页背景语境，page.md 未载该缩写、慎用 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Empire Collapse**（manifest 预分配）
- **风格**：厚重 / 张力 / 史诗推演
- **匹配理由**：丙肝曾是盘踞全球的"无形帝国"——数以百万计的慢性感染；Rice 的感染性克隆让这个帝国第一次在实验室里被观察、被拆解、终被 DAA 时代攻破。Empire Collapse 的厚重张力匹配"终结一个隐形帝国"的收官棒叙事。
- **本地路径**：`music_audio/inspiring-electronic/12-NTuSqFy4Stc-Cinematic Dramatic Epic Drone Orchestra Film by Cold Cinema [No Copyright Music] ⧸ Empire Collapse.wav` → 复制为 `presentations/21th_century/Charles_M._Rice/Empire_Collapse.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；感染性克隆的年份与因果角色务必精确。**
