# 医学家立传提示词（Andrew Fire）

> OpenMedic 项目 · 21 世纪诺贝尔生理学或医学奖 2006 年得主（与 Craig Mello 共享）。
> 本文件是 Andrew Fire 的人物专属立传提示词：事实基准唯一来源为本地 Wikipedia 页面，
> 执行方按本提示词产出 15 页 Beamer 立传（本阶段不写 tex，仅沉淀事实与规范）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Andrew Zachary Fire（1959-04-27 生于加州帕洛阿尔托，在世）
- **气质关键词**：**RNA 干扰的发现者、基因沉默的破译者、卡内基胚胎学部的安静革命者**
- **诺奖获奖理由（2006，逐字引用 medic/nobel_medicine_citations.json）**：
  > "for their discovery of RNA interference - gene silencing by double-stranded RNA"
  > （因其发现 RNA 干扰——双链 RNA 引发的基因沉默）——注意 "their"：与 Craig Mello 共享
- **设计母题**：**沉默（silencing）**。一小段双链 RNA 让对应基因安静下来——视觉母题用一条逐渐
  变淡、被"擦除"的 mRNA 长链，与清晰的双链小片段形成对比，象征"以小搏大的调控机制"。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Andrew_Fire/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 medic 路径执行：页面读 `medic/presentations/pages/21th_century/{Dir}/page.md`，
> 产出放 `medic/presentations/21th_century/Andrew_Fire/`，数据库写 greatminds 库（MySQL）。

- **第 0 步**：核对本地 page.md 事实基准（本提示词第三、四、七节已沉淀，执行时再逐句复核）
- **第 1 步**：建目录 `medic/presentations/21th_century/Andrew_Fire/`（含 `images/`）
- **第 2 步**：复制 Makefile，设 `MAIN=Andrew_Fire_zh`、`VIDEO_NAME=Andrew_Fire_zh`
- **第 3 步**：收集肖像（page.md 无 infobox 肖像 URL 时用 Commons Special:FilePath 回退，404 则装饰圆占位）
- **第 4~9 步**：tex 编写 → 编译循环（0 error、vbox≤10pt、hbox≤50pt）→ pdftoppm 逐页目检 → make images/video → Review

## 三、研究领域梳理 + 入库（与 yaml fields 完全一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | genetics | 遗传学 | 基因沉默机制，诺奖核心（infobox fields 首列） | 核心页 |
| 1 | molecular biology | 分子生物学 | dsRNA→mRNA 降解的机制链 | 核心页 |
| 2 | pathology | 病理学 | 斯坦福病理学+遗传学双聘教授 | 身份页 |
| 3 | RNA biology | RNA 生物学 | RNAi 研究纲领的开创 | 核心页 |

## 四、社会关系梳理 + 入库（与 yaml relations 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Phillip Sharp | 师→生（博士导师） | MIT 博士导师（1993 诺奖得主），1983 腺病毒体外转录博士论文 |
| advisor-student | Jenny Hsieh | Fire→学生 | infobox Notable students 明载 |
| colleague | Sydney Brenner | 无向 | 博士后（Helen Hay Whitney Fellow）在 MRC LMB Brenner 课题组 |
| co-honored | Craig Mello | 无向 | 2006 诺贝尔生理学或医学奖共享（发现 RNA 干扰——双链 RNA 引发的基因沉默） |

> 说明：relations=4 为诚实值。Wiley/Massry/Rosenstiel 等奖项的共同获奖者（Tuschl/Baulcombe/Ambros/Ruvkun）
> 虽为 page.md 明载，但属"奖项共享"而非诺奖同届，**一律不入库**防噪声（与主控口径一致：co-honored 仅诺奖同届）。
> 自查 SQL：`SELECT COUNT(*) FROM person_relation WHERE from_id=<pid> OR to_id=<pid>;` 预期 = 4。

## 五、配色方案

- **气质**：安静、精准、机制之美
- **主色**：深紫蓝 `#46356B`（RNA 双链的神秘与分子的沉静）+ 香槟金 `#D4AF37`（诺奖色）
- **四分类色 badge**：
  - `badgeRNAi` RNA 干扰 — 冷青 `#0E7C7B`
  - `badgeDsRNA` 双链 RNA — 靛蓝 `#4C5FD5`
  - `badgeSilence` 基因沉默 — 石墨灰 `#37474F`
  - `badgeAward` 荣誉 — 皇家紫 `#52307C`
- **背景母题**：稀疏的短双链片段（两条平行短线+横档）+ 渐隐的长单链曲线

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover 共享首页）
01  封面 — 基因的静音键 / Andrew Fire 1959– + 四色 badge + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格：生卒/帕洛阿尔托出身/教育 Berkeley BA 1978 + MIT PhD 1983/任职/核心领域
03  核心贡献概览 — RNA 干扰 / 双链 RNA / 催化式沉默 / 从线虫到医学
04  湾区少年 (1959–1978) — 帕洛阿尔托出生、森尼韦尔长大、Fremont High；19 岁 Berkeley 数学学士
05  MIT：Sharp 门下 (1978–1983) — 转向分子生物学，博士论文 "In vitro transcription studies of adenovirus"（1983）
06  剑桥：LMB 岁月 — Helen Hay Whitney 博士后，Nobel laureate Sydney Brenner 课题组
07  卡内基胚胎学部 (1986–2003) — 巴尔的摩；双链 RNA 基因沉默的最初工作在此完成；1989 兼职 Johns Hopkins
08  1998 Nature 论文（核心贡献页）— Fire & Mello 与 SiQun Xu、Mary Montgomery、Stephen Kostas、Sam Driver；dsRNA 高效关闭特定基因、销毁匹配 mRNA、少量分子即起效→提出催化机制假说
09  "fundamental mechanism" — Karolinska 诺奖引言 "This year's Nobel Laureates have discovered a fundamental mechanism for controlling the flow of genetic information."（page.md 明载英文原句，可引）
10  斯坦福新篇 (2003– ) — 病理学+遗传学教授；NAS（2004）与 American Academy of Arts and Sciences 院士
11  荣誉前奏 — Meyenburg 2002 · NAS 分子生物学奖 2003（与 Mello）· Wiley 2003 · Massry 2005 · Gairdner 2005 · Paul Ehrlich 2006
12  2006 诺贝尔奖 — 理由逐字；诺奖演讲 "Gene Silencing by Double Stranded RNA"
13  机制到医学 — RNAi 打开生物学新领域（引 Nick Hastie 评语，BBC 转引，注明转引）；RNAi 治疗学的深远回响
14  遗产：调控信息流 — 基因表达调控范式的更迭
15  结尾
```

## 七、特殊陷阱表（★ 执行时必须核对）

| # | 陷阱 | 说明 |
|---|------|------|
| 1 | 获奖理由 | 逐字 "for their discovery of RNA interference - gene silencing by double-stranded RNA"；含连字符短语，勿改写 |
| 2 | 1998 论文署名 | 论文是 Fire、Mello 与 SiQun Xu、Mary Montgomery、Stephen Kostas、Sam Driver 六人合著——叙述勿写成"两人论文" |
| 3 | 研究地点 | RNAi 工作在**卡内基华盛顿研究所胚胎学部（巴尔的摩）**完成；斯坦福是 2003 之后；勿写成"斯坦福发现 RNAi" |
| 4 | 博士导师 | Phillip Allen Sharp（1993 诺贝尔奖得主，MIT）；page.md 正文与 infobox 一致；库里规范名 'Phillip Sharp'（id=3791） |
| 5 | 学位年份 | Berkeley 数学 BA **1978**（19 岁完成）；MIT 生物学 PhD **1983**；勿混 |
| 6 | 博士后身份 | Helen Hay Whitney Postdoctoral Fellow 在 MRC LMB，属 **Brenner 领导的课题组**——入 colleague，勿写成"师从 Brenner" |
| 7 | 诺奖引言 | Karolinska 引言为 page.md 明载英文原句（可引原文+译文）；Nick Hastie 评语系 **BBC 转引**，注明"据 BBC 报道" |
| 8 | 在世者 | Fire 在世（1959- ），生卒页留白卒年；relations 偏少为诚实值 |
| 9 | 犹太家庭 | page.md 载 Jewish family 成长背景，可客观一笔，勿展开宗教叙事 |
| 10 | 奖项共同得主 | Wiley Prize 2003 另含 Tuschl/Baulcombe，Massry 2005 另含 Baulcombe，Rosenstiel 2005 另含 Ambros/Ruvkun——均不入库，陷阱注明防 Review 误加 |
| 11 | 卡内基名称 | Carnegie Institution of Washington（今 Carnegie Institution for Science），两种写法 page.md 均出现，正文统一用前者并注今名 |

## 八、术语清单

| 英文 | 中文 | 风险点 |
|------|------|--------|
| RNA interference (RNAi) | RNA 干扰 | 双链 RNA 引发的序列特异基因沉默 |
| double-stranded RNA (dsRNA) | 双链 RNA | 比单链 RNA 干扰高效得多（page.md 明载对比） |
| gene silencing | 基因沉默 | "沉默"指 mRNA 被降解，非基因删除 |
| messenger RNA (mRNA) | 信使 RNA | 被降解对象，不能翻译成蛋白 |
| catalytic process | 催化过程 | 少量 dsRNA 起效→提出催化假说，后被证实 |
| Caenorhabditis elegans | 秀丽隐杆线虫 | 1998 论文模式生物（标题载明） |
| Carnegie Institution | 卡内基科学研究所 | 研究完成地 |
| MRC Laboratory of Molecular Biology | MRC 分子生物学实验室 | 剑桥，博士后站 |

## 九、背景音乐选择

- **选定曲目**：**Eternals** — Alex-Productions（manifest 预分配）
- **匹配理由**：Eternals 的深远感对应 RNAi 作为"调控遗传信息流的基础机制"的恒久意义——从线虫的发现
  到整个 RNA 生物学新领域，属于会被反复引用半个世纪的工作；音乐气质安静而宏大，贴合 Fire 的低调风格。
- **备选（未采用）**：The Flow of Time（时间感好但已被多篇占用）、New Lands（新领域感强但偏昂扬，不如 Eternals 贴合"沉默"母题）
- **本地路径**：`music_audio/` 下 alex-productions 曲库按 curated_tracks.md 对应条目复制为
  `medic/presentations/21th_century/Andrew_Fire/Eternals.wav`
