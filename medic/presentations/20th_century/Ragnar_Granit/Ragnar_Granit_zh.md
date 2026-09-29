# 医学家立传提示词（Ragnar Granit）

> OpenMedic 项目 · 20 世纪诺贝尔生理学或医学奖 1967 年得主（与 Hartline、Wald 三人共享）。
> 本文件是 Ragnar Granit 的人物专属立传提示词：事实基准唯一来源为本地 Wikipedia 页面。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Ragnar Arthur Granit（1900-10-30 生于芬兰里希迈基 ~ 1991-03-12 逝于斯德哥尔摩，享年 90）
- **气质关键词**：**视网膜神经生理学的奠基人、 Young-Helmholtz 色觉理论的生理学实证者、芬兰-瑞典"五五开"诺奖得主**
- **诺奖获奖理由（1967，逐字引用 medic/nobel_medicine_citations.json）**：
  > "for their discoveries concerning the primary physiological and chemical visual processes in the eye"
  > （因其关于眼内初级生理与化学视觉过程的发现）——"their"：与 Hartline、Wald 三人共享
- **设计母题**：**三色分解（three colours）**。视网膜电敏感度分蓝/绿/红三群——视觉生理学首次为 19 世纪
  Young-Helmholtz 色觉理论提供神经生理学证据；视觉母题用一束白光经视网膜后分解为三条彩色曲线。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Ragnar_Granit/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 medic 路径执行：页面读 `medic/presentations/pages/20th_century/{Dir}/page.md`，
> 产出放 `medic/presentations/20th_century/Ragnar_Granit/`，数据库写 greatminds 库（MySQL）。
> 第 0 步核对事实基准 → 第 1 步建目录含 images/ → 第 2 步复制 Makefile 设
> `MAIN=Ragnar_Granit_zh`、`VIDEO_NAME=Ragnar_Granit_zh` → 第 3 步收肖像（page.md 正文载 Commons 1967 领奖照 Granit-1967-Nobel.jpg，优先抓取）→
> 第 4~9 步 tex 编写 → 编译循环（0 error、vbox≤10pt、hbox≤50pt）→ pdftoppm 逐页目检 → make images/video → Review。

## 三、研究领域梳理 + 入库（与 yaml fields 完全一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | neurophysiology | 神经生理学 | 视网膜电图与色觉机制，诺奖核心 | 核心页 |
| 1 | physiology | 生理学 | 赫尔辛基生理学 docent→正教授 | 身份页 |
| 2 | ophthalmology | 眼科学 | 视觉研究的临床面向（frontmatter field_of_work） | 身份页 |
| 3 | motor control | 运动控制 | 1940 年代中期后的第二研究纲领（肌肉与突触） | 后期页 |

## 四、社会关系梳理 + 入库（与 yaml relations 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Haldan Keffer Hartline | 无向 | 1967 诺贝尔生理学或医学奖三人共享（眼内初级生理与化学视觉过程） |
| co-honored | George Wald | 无向 | 1967 诺贝尔生理学或医学奖三人共享（眼内初级生理与化学视觉过程） |
| advisor-student | Charles Scott Sherrington | 师→生 | 牛津时期学生，后获 1967 诺贝尔奖（库内既有行沿用，id=5325；page.md 另载"最重要的科学楷模"）
| influence | Eino Kaila | 无向 | 哲学家/心理学家，启发其 student 时期即投入心理生理学实验 |
| collaborator | Per-Olof Therman | 无向 | 共同证明视网膜细胞可对刺激产生抑制性反应（呼应 Sherrington） |
| collaborator | Gunnar Svaetichin | 无向 | 共同发现视网膜电敏感度分蓝/绿/红三群——色觉理论的生理学证据 |
| spouse | Marguerite Emma Bruun | 无向 | 男爵夫人（Daisy），1929 年结婚；合葬于芬兰 Korpo |

> 说明：relations=7 全部 page.md 明载。库内对手方沿用 "Charles Scott Sherrington"(5325)；
> Hartline(费城 Johnson Foundation 同期) 与 Granit 在 1930s 有同地之谊但 page.md 未载合作，仅建 co-honored。
> 自查 SQL：`SELECT COUNT(*) FROM person_relation WHERE from_id=<pid> OR to_id=<pid>;` 预期 = 7。

## 五、配色方案

- **气质**：北欧的清冽、文学少年-turned-科学家的双重底蕴
- **主色**：芬兰湾深蓝 `#16324F`（赫尔辛基与卡罗林斯卡的学统）+ 香槟金 `#D4AF37`（诺奖色）
- **四分类色 badge**：`badgeRetina` 视网膜 — 电光蓝 `#4C5FD5`；`badgeColour` 色觉三色 — 猩红 `#C4204F`；`badgeMotor` 运动控制 — 冷青 `#0E7C7B`；`badgeAward` 荣誉 — 皇家紫 `#52307C`
- **背景母题**：白光入射后分解为蓝/绿/红三条渐变曲线，缀稀疏光点

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页
01  封面 — 视网膜的测绘者 / Ragnar Granit 1900–1991 + 四色 badge + 国籍行（Finland / Sweden）
02  身份信息页 — 生卒/里希迈基出身（生于俄属芬兰大公国）/赫尔辛基大学（1926 学士+licentiate、同日获医学博士学位 1927）/赫尔辛基→卡罗林斯卡/核心领域
03  核心贡献概览 — 视网膜电图 / 色觉三群 / 抑制性反应 / 运动控制
04  瑞典语芬兰的文学少年 (1900–1926) — Korpo 群岛根脉；Oulunkylä 长大；Svenska normallyceum；文学社（诗人 Björling）；Studentbladet 编辑、先锋杂志 Quosego 撰稿；表亲 Ringbom 三兄弟（艺术史/分析化学/作曲）
05  从哲学到医学 (1926–1927) — 初学哲学与心理学（Åbo Akademi）；受 Eino Kaila 启发转入赫尔辛基医科；1926 学士论文 Farbentransformation und Farbenkontrast；1927 licentiate 与医学博士同日获得
06  国际游学：牛津与费城 (1928–1930s) — 谢灵顿（1932 诺奖）为其"最重要的科学楷模"；宾大 Johnson Foundation 世界视觉生理重镇——Hartline 同在；视网膜电图成分与视神经活动的首批重要论文
07  赫尔辛基学派 (1929–1940) — docent 1929、代理教授 1935、正教授 1937；自制仪器；与 Therman：视网膜抑制性反应；与 Svaetichin：蓝/绿/红三群电敏感——Young-Helmholtz 理论的首个神经生理学证据；芬兰首个诺奖水准研究组
08  迁居瑞典 (1941–1946) — 谢绝 Tartu 讲席与哈佛邀请；赫尔辛基芬兰化运动（1930s 末医学院仅另一教授用瑞典语授课）为次要原因；1941 入瑞典籍；卡罗林斯卡神经生理学系主任、诺贝尔研究所首任所长、1946 个人教授（至 1967 退休）
09  运动控制 (1940s 中期起) — 肌肉功能与控制肌收缩的突触——开辟全新领域；1967 诺奖表彰的是早期视网膜工作而非此项（page.md 明载区分）
10  1967 诺贝尔奖 — 理由逐字；"fifty-fifty" 芬兰/瑞典得主自评；1967-12-12 诺奖演讲 "The Development of Retinal Neurophysiology"；自国王古斯塔夫六世手中领奖（1967 照）
11  荣誉与认可 — Björkénska priset 1948 · ForMemRS 1960 · 美国哲学学会国际会员 1954 · 瑞典科学院 1944（第 912 号）· 芬兰科学院 1937 · 美国 NAS 1968 · AAAS 1971 · 芬兰狮勋章/北极星勋章/六翼天使勋章
12  第一位芬兰出生的医学诺奖得主 — 1930s 赫尔辛基研究组为芬兰首个诺奖水准团队；学生多成各国教授（"brain drain"）
13  家庭与身后 — 1929 娶男爵夫人 Daisy Bruun（1902-1991）；终生自认芬兰瑞典人、维持芬瑞两处居所、保留芬兰瑞典口音； directories 居址写 "Stockholm and Korpo"；1991 逝于斯德哥尔摩，合葬 Korpo
14  遗产 — 视网膜电生理从形态学走向机制科学；色觉三色感受器的生理学确认；单细胞记录技术（赫尔辛基研发）惠及全球
15  结尾
```

## 七、特殊陷阱表（★ 执行时必须核对）

| # | 陷阱 | 说明 |
|---|------|------|
| 1 | 获奖理由 | 逐字 "for their discoveries concerning the primary physiological and chemical visual processes in the eye"；三人共享 |
| 2 | 国籍口径 | Nobel 官方（citation json）与 frontmatter 均为 Finland+Sweden（出生时为俄属芬兰大公国）；manifest 仅 Finland——yaml 双籍 Finland(0)+Sweden(1)；本人自称 "fifty-fifty" |
| 3 | 国籍变更线 | Russian Empire (1900-1917) → Finnish (1917-1941) → Swedish (1941-1991)——身份页可作时间轴，勿只写"瑞典人" |
| 4 | 学位表述 | 1927 licentiate 与医学博士（同日）；1926 学士论文为德文题名——勿写成 PhD |
| 5 | 诺奖表彰对象 | 表彰**早期视网膜工作**，非 1940s 后的运动控制研究——page.md 明载区分，勿混 |
| 6 | 迁居动因 | 主因卡罗林斯卡研究资源，赫尔辛基芬兰化（Fennicisation）为次要原因——因果分寸照实 |
| 7 | 与 Hartline | 二人 1930s 同在宾大 Johnson Foundation 工作但 page.md 未载合作——只建 co-honored，勿写同事/师生 |
| 8 | Sherrington | "most important scientific model"（page.md 原短语可引）——影响关系，勿写成导师 |
| 9 | 引语红线 | "fifty-fifty" 与 "most important scientific model" 两处 page.md 有英文原文可引；其余不得造引语 |
| 10 | 肖像 | 正文有 Commons 1967 接受国王授奖照（Granit-1967-Nobel.jpg）——图注写明 1967 领奖 |
| 11 | 政治无涉 | 二战期间 Samfundet Nordens Frihet 董事（1942-1945）仅列表性一句，不做政治展开 |

## 八、术语清单

| 英文 | 中文 | 风险点 |
|------|------|--------|
| electroretinogram | 视网膜电图 (ERG) | 首批重要论文主题 |
| Young-Helmholtz theory | 杨-亥姆霍兹色觉理论 | 三色感受器的心理物理学源头 |
| inhibitorily response | 抑制性反应 | 与 Therman 共同证明，呼应谢灵顿 |
| docent | 无俸讲师（北欧学衔） | 1929 赫尔辛基，勿译"教授" |
| Karolinska Institutet | 卡罗林斯卡学院 | 迁居后的主阵地 |
| Nobel Institute | 诺贝尔研究所 | 1941 年创设时首任所长 |
| motor control | 运动控制 | 后期第二纲领 |
| Finland-Swedish | 芬兰瑞典族 | 母语社群身份，勿译"瑞典芬兰人" |

## 九、背景音乐选择

- **选定曲目**：**Ascension** — Alex-Productions（manifest 预分配）
- **匹配理由**：Ascension 的攀升感对应其双重登顶——从文学少年到芬兰首位医学诺奖得主（芬兰第一个诺奖水准研究组），
  以及视网膜研究从描述走向机制的科学跃升；北欧清冽基调贴合其"五五开"的跨境人生。
- **备选（未采用）**：Eternals（恒久感可用但 batch-03 已占用）、The Flow of Time（时间感可但本篇更重"攀升"）
- **本地路径**：`music_audio/` 曲库按 curated_tracks.md 复制为 `medic/presentations/20th_century/Ragnar_Granit/Ascension.wav`
