# 医学家立传提示词（Barry Marshall）

> OpenMedic 项目 · 21 世纪诺贝尔生理学或医学奖 2005 年得主（与 J. Robin Warren 共享）。
> 本文件是 Barry Marshall 的人物专属立传提示词：事实基准唯一来源为本地 Wikipedia 页面，
> 执行方按本提示词产出 15 页 Beamer 立传（本阶段不写 tex，仅沉淀事实与规范）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Barry James Marshall（1951-09-30 生于西澳大利亚卡尔古利，在世）
- **气质关键词**：**以身试菌的斗士、消化性溃疡病因学的颠覆者、幽门螺杆菌的驯服者**
- **诺奖获奖理由（2005，逐字引用 medic/nobel_medicine_citations.json）**：
  > "for their discovery of the bacterium Helicobacter pylori and its role in gastritis and peptic ulcer disease"
  > （因其发现幽门螺杆菌及其在胃炎和消化性溃疡病中的作用）——注意 "their"：与 J. Robin Warren 共享
- **设计母题**：**细菌与酸（bacterium vs acid）**。在人人相信"胃酸杀灭一切细菌"的年代，一株弯曲的螺旋菌
  在强酸环境中存活并致病——视觉上可用强酸环境（暖色）中一道螺旋上升的冷色菌体轨迹，象征"颠覆教条"。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Barry_Marshall/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 medic 路径执行：页面读 `medic/presentations/pages/21th_century/{Dir}/page.md`，
> 产出放 `medic/presentations/21th_century/Barry_Marshall/`，数据库写 greatminds 库（MySQL）。

- **第 0 步**：核对本地 page.md 事实基准（本提示词第三、四、七节已沉淀，执行时再逐句复核）
- **第 1 步**：建目录 `medic/presentations/21th_century/Barry_Marshall/`（含 `images/`）
- **第 2 步**：复制 Makefile，设 `MAIN=Barry_Marshall_zh`、`VIDEO_NAME=Barry_Marshall_zh`
- **第 3 步**：收集肖像（page.md 无 infobox 肖像 URL 时用 Commons Special:FilePath 回退，404 则装饰圆占位）
- **第 4~9 步**：tex 编写 → 编译循环（0 error、vbox≤10pt、hbox≤50pt）→ pdftoppm 逐页目检 → make images/video → Review

## 三、研究领域梳理 + 入库（与 yaml fields 完全一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | microbiology | 微生物学 | 幽门螺杆菌发现与培养，诺奖核心 | 核心页 |
| 1 | medicine | 医学 | 内科医生出身（MBBS 1974 UWA） | 身份页 |
| 2 | gastroenterology | 胃肠病学 | 胃炎/消化性溃疡病因学 | 核心页 |
| 3 | infectious disease | 感染性疾病 | 细菌致病说对"应激说"的颠覆 | 争鸣页 |

## 四、社会关系梳理 + 入库（与 yaml relations 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | J. Robin Warren | 无向 | 2005 诺贝尔生理学或医学奖共享（发现幽门螺杆菌及其在胃炎和消化性溃疡中的作用） |
| spouse | Adrienne Feldman | 无向 | 妻子 Adrienne Joyce Feldman，1972 结婚，育一子三女 |

> 说明：在世者 relations 偏少为诚实值（本篇仅 2 条），防 Review 误判。
> page.md 提到 John Scott Haldane / JBS Haldane / Jonas Salk 只是"自体实验传统"类比，**不是真实关系，不入库**。
> 自查 SQL：`SELECT COUNT(*) FROM person_relation WHERE from_id=<pid> OR to_id=<pid>;` 预期 = 2。

## 五、配色方案

- **气质**：倔强、实证、孤军奋战后的柳暗花明
- **主色**：深海蓝 `#16324F`（西澳的海洋与医生的沉稳）+ 香槟金 `#D4AF37`（诺奖色）
- **四分类色 badge**：
  - `badgeHp` 幽门螺杆菌 — 螺旋青 `#0E7C7B`
  - `badgeUlcer` 消化性溃疡 — 胃液暖橙 `#E07B30`
  - `badgeSelf` 自体实验 — 猩红 `#C4204F`
  - `badgeAward` 荣誉 — 皇家紫 `#52307C`
- **背景母题**：稀疏螺旋曲线 + 小圆点（模拟培养皿菌落），四色错落

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover 共享首页）
01  封面 — 以身试菌的人 / Barry Marshall 1951– + 四色 badge + 国籍行（Australia）
02  身份信息页（★ 必做）— 左头像 + 右信息网格：生卒/出生地卡尔古利/教育 UWA MBBS 1974/配偶/任职/核心领域
03  核心贡献概览 — 幽门螺杆菌 / 胃炎与溃疡 / 自体实验 / 根除疗法
04  早年：卡尔古利到珀斯 (1951–1974) — 八岁迁珀斯、Marist College、UWA MBBS 1974
05  皇家珀斯医院：遇见 Warren (1979–1982) — 1979 Registrar；1981 结识病理学家 Warren
06  第 31 个样本 (1982) — 技术员按惯例两天丢弃培养皿，复活节长周末第 31 号样本放置四天，H. pylori 现身
07  被拒稿与被讥笑 (1983) — 投稿 Gastroenterological Society of Australia 位列当年末 10% 被拒
08  自体实验 (1984，核心贡献页) — 基线内镜 → 吞服培养液 → 第 3 天恶心口臭 → 第 5–8 天无酸呕吐 → 第 8 天内镜确诊急性胃炎 → 第 14 天开始抗生素
09  1985 论文与科赫法则 — Medical Journal of Australia 发表；满足 gastritis 的科赫法则（page 明载"but not for peptic ulcers"）
10  根除疗法：抗生素+铋剂 — 杀灭 H. pylori 即治愈十二指肠溃疡（FRS 证书语）
11  弗吉尼亚与回归 UWA (1986– ) — UVA 1986 起、1998–2003 Burnet Fellowship、H. pylori 研究实验室
12  荣誉与认可 — Nobel 2005 · Lasker 1995 · Gairdner 1996 · Paul Ehrlich 1997 · FRS 1999 · Companion of the Order of Australia 2007
13  马歇尔中心与新战线 — 2007 Marshall Centre 联合主任、Penn State 兼职、2017 Noisy Guts Project（IBS）、2020 Brainchip 顾问
14  遗产：从溃疡到胃癌 — H. pylori 感染与胃癌因果链，50 年来医学认知最激进的修正之一
15  结尾
```

## 七、特殊陷阱表（★ 执行时必须核对）

| # | 陷阱 | 说明 |
|---|------|------|
| 1 | 获奖理由 | 逐字 "for their discovery of the bacterium Helicobacter pylori and its role in gastritis and peptic ulcer disease"；"their" 表共享，勿改成 "his" |
| 2 | 年份归属 | 自体实验在 **1984**，论文发表于 **1985**（Medical Journal of Australia），两处年份勿混 |
| 3 | 被拒稿 | 1983 年投稿 Gastroenterological Society of Australia **被拒**（位列末 10%），这不是一次"发表"，勿写成论文问世 |
| 4 | 科赫法则 | 自体实验满足的是 **gastritis** 的科赫法则，page.md 明载 "but not for peptic ulcers"，勿写成"证明溃疡病因" |
| 5 | 第 31 号样本 | 培养成功的关键是技术员按咽喉拭子惯例两天丢弃培养皿、复活节周末第 31 号样本放了四天——H. pylori 生长更慢；勿写成"一次成功" |
| 6 | 角色分工 | Warren 是**病理学家**（读片发现螺旋菌），Marshall 是**内科 registrar**（培养、假设、自体实验），勿互换 |
| 7 | 引语红线 | "everyone was against me, but I knew I was right." 是 page.md 明载的 1998 年引述（有英文原文，可引原文+译文）；但 page.md 同时载有"科学怀疑论正当"的平衡观点，勿单边渲染"全员迫害" |
| 8 | 配偶与子女 | 妻 Adrienne Joyce Feldman，**1972** 结婚，四个孩子（一子三女）；口臭由妻子注意到（第 3 天叙事细节） |
| 9 | 任职线 | Royal Perth Hospital 1979 起；UVA 1986 起并保留教职；1998–2003 UWA Burnet Fellowship；2007 Marshall Centre 联合主任 + Penn State 兼职；勿把 Marshall Centre 写成"创办"（为致敬其而设，他任 Co-Director） |
| 10 | Noisy Guts | 2017 年创立 Noisy Guts Project 研究**肠易激综合征（IBS）**诊断，衍生 Noisy Guts Pty Ltd——与 H. pylori 研究是两条线，勿混淆 |
| 11 | Brainchip | 2020 年 8 月与 Simon J. Thorpe 共同加入 Brainchip 科学顾问委员会——计算机芯片公司，一笔带过即可 |
| 12 | 奖项年份 | Warren Alpert 1994、Lasker 1995、Gairdner 1996、Paul Ehrlich 1997、Heineken/Florey/Buchanan/Golden Plate 1998、FRS 1999、Benjamin Franklin Medal 1999、Keio 2002、Centenary+Macfarlane Burnet Medal 2003、Nobel 2005、WA of the Year 2006、Order of Australia AC 2007、牛津荣誉 DSc 2009、FAHMS 2015、UWA 图书馆改名 Barry J Marshall Library 2015 |
| 13 | 国籍 | Australia（Nobel 官方口径），勿写"澳大利亚/美国"双籍 |

## 八、术语清单

| 英文 | 中文 | 风险点 |
|------|------|--------|
| Helicobacter pylori | 幽门螺杆菌 | 1989 年前旧名 Campylobacter pylori，本篇按 page.md 用现名 |
| peptic ulcer | 消化性溃疡 | 含胃溃疡与十二指肠溃疡 |
| gastritis | 胃炎 | 自体实验证实的是急性胃炎 |
| achlorhydria | 胃酸缺乏症 | 自体实验第 5–8 天症状的机理 |
| Koch's postulates | 科赫法则 | 仅满足 gastritis 一半，勿夸大 |
| endoscopy | 内镜检查 | 实验前后共三次（基线/第 8 天/第 14 天） |
| bismuth salt regimens | 铋剂疗法 | FRS 证书中的根除方案表述 |
| MBBS | 内外全科医学士 | UWA 1974，勿写成 PhD |

## 九、背景音乐选择

- **选定曲目**：**Tragedy** — Alex-Productions（manifest 预分配）
- **匹配理由**：Tragedy 的悲壮底色精确匹配本篇叙事弧线——被拒稿、被讥笑、以健康为赌注吞下细菌的孤勇，
  以及"三天的恶心与八天的呕吐"带来的戏剧张力；结局是柳暗花明（诺奖+根除疗法普及），音乐前抑后扬正合适。
- **备选（未采用）**：Last Hope（希望感强但悲壮不足）、The Flow of Time（叙事性够但张力弱）
- **本地路径**：`music_audio/` 下 alex-productions 曲库按 curated_tracks.md 对应条目复制为
  `medic/presentations/21th_century/Barry_Marshall/Tragedy.wav`
