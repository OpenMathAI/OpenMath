# 医学家立传提示词（Konrad Lorenz）

> OpenMedic 项目 · 20 世纪诺贝尔生理学或医学奖 1973 年得主（三人共享之一） · 本文件是该人物的专属立传提示词，
> 按 9 节结构执行 Beamer 立传；数据库入库（fields/relations）已由批次完成，本文件第四/三节与 yaml 一致。

## 一、背景信息 【人物专属】

- **目标医学家**：Konrad Zacharias Lorenz（1903-11-07 生于维也纳 ~ 1989-02-27 逝于维也纳 Altenberg，享年 85 岁）
- **气质关键词**：**现代动物行为学奠基人之一、灰雁印记的讲述者、King Solomon's Ring 的作者** —— 1973 年获奖理由（逐字引用 medic/nobel_medicine_citations.json，三人共享同一句）：
  > "for their discoveries concerning organization and elicitation of individual and social behaviour patterns"
  > （因他们关于个体与社会行为模式的组织与引发机制的发现）
- **设计母题**：**印记与跟随（imprinting & the following gosling）**。破壳数小时的灰雁把第一眼移动物当作母亲、一列雏雁跟着长靴走——"本能如何被第一眼锁定"。
- **本地 Wikipedia 路径**：medic/presentations/pages/20th_century/Konrad_Lorenz/page.md
- **参考模板**：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）

## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章）

- 第 0/1/2/3 步按 **medic 路径**执行：事实基准 = `medic/presentations/pages/20th_century/Konrad_Lorenz/page.md`；目录 `medic/presentations/20th_century/Konrad_Lorenz/`；Makefile 改 `MAIN=Konrad_Lorenz_zh`；肖像优先 images.txt 所列 Commons 图（Lorenz in 1978、与 Tinbergen 1978 合照、1944 战俘照慎用），失败用装饰圆占位。
- 第 4/4.5 步（入库）**已完成**（第三、四节与 `MySQL/data/Konrad_Lorenz.yaml` 一致，勿重复入库）。
- 第 5-9 步：配色 → 幻灯片 → Beamer → 布局检查（0 error、vbox≤10pt、hbox≤50pt、逐页目检）→ 史实审查（第七节）。

## 三、研究领域梳理 + 入库（rank 0-4 表）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | ethology | 动物行为学 | 奠基人之一，诺奖核心 | 核心页 |
| 1 | ornithology | 鸟类学 | 灰雁/寒鸦研究 | 研究页 |
| 2 | instinct theory | 本能理论 | IRM/固定动作模式/心理水力模型 | 理论页 |
| 3 | philosophy (of biology) | （生物）哲学 | Behind the Mirror 认识论 | 晚年页 |

## 四、社会关系梳理 + 入库（与 yaml 完全一致，已完成）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | Oskar Heinroth | 无向 | 其师，动物行为学前辈（印记议题先行者） |
| colleague | Nikolaas Tinbergen | 无向 | 1936 相识的挚友与合作者，共创行为学期刊与 IRM 理论 |
| co-honored | Nikolaas Tinbergen | 无向 | 1973 诺贝尔生理学或医学奖三人共享（行为模式） |
| co-honored | Karl von Frisch | 无向 | 1973 诺贝尔生理学或医学奖三人共享（行为模式） |
| influence | Julian Huxley | 无向 | 挚友兼学生时代的景仰对象（赫胥黎之孙） |
| colleague | Karl Popper | 无向 | 总角之交，晚年合著《Die Zukunft ist offen》 |
| parent-child | Adolf Lorenz | 父→本人 | 父，富有声望的外科医生 |
| spouse | Margarethe Gebhardt | 无向 | 儿时伴侣，妇科医生，育一子二女 |

> 对手方规范名：`Karl Popper` 沿用库内记录（本批 Medawar 篇已建 stub）；其余按 page.md 形式新建 stub；`Nikolaas Tinbergen`/`Karl von Frisch` 与本批两篇同形式镜像。**relations=8 为诚实值**。

## 五、配色方案

- **气质**：Altenberg 庄园的野趣 + 奥地利学派的叙事魅力 + 复杂的历史背影
- **主色**：灰雁绿 `#3E6B4F`（多瑙河湿地与雁羽）
- **诺奖香槟金**：`#D4AF37`
- **badge 四分类色**：
  - `badgeA` 印记 — 印记金橙 `#C97B2D`
  - `badgeB` 本能与 IRM — 本能蓝 `#2E6E9E`
  - `badgeC` 超常刺激 — 刺激红 `#A63A2B`
  - `badgeD` 科普写作 — 人文紫 `#5E4B8B`
- **背景母题**：低透明度雁列飞行队形 + 一串跟随的雏雁脚印。

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 现代动物行为学奠基人 / Konrad Lorenz 1903–1989 + badge + 右上头像 + 国籍行（Austria）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、维也纳、哥大一年/维也纳 MD 1928+PhD 1933、柯尼斯堡教授 1940、马普所 1950/1958、诺奖 1973）
03  核心贡献概览 — 印记 / 固定动作模式与 IRM / 超常刺激 / 《所罗门王的指环》
04  Altenberg 庄园的孩子 (1903–1922) — 外科名医之父与医生之母、"对动物无节制之爱"得到双亲容忍、塞尔玛·拉格洛夫《尼尔斯骑鹅旅行记》点燃野雁痴迷（自传自述可引）
05  医学与动物暖房 (1922–1935) — 父命先赴哥伦比亚大学一年、维也纳 MD 1928、解剖学助教、学生时代宿舍养鱼到卷尾猴 Gloria 的私人动物园、1933 完成动物学第二博士
06  1935：印记（Prägung）的奠基描述 — 早成鸟与第一移动物结合；Umwelt 概念（Uexküll）的运用；鹰/雁效应与内在驱力溢出
07  1936：与 Tinbergen 相遇 — 本能研讨会结识挚友、共同研究野雁/家鹅/杂交鹅、共创行为学第一份专业期刊
08  理论工具箱（核心页）— 固定动作模式、先天释放机制（与 Tinbergen 共同发展）、超常刺激（巨蛋/红腹木鱼模型）、心理水力模型（受 McDougall 影响，Dawkins 对其群体选择倾向的批评注记）
09  二战岁月（克制一页）— 1941 征入伍任军医、1944 东线被俘、苏属亚美尼亚战俘营四年行医、携《镜中背后》手稿与宠物椋鸟归乡——仅此框架，细节从略（见第七节）
10  1950-1973：建制与诺奖 — 马普行为生理学研究所 Buldern 建所 1950、Seewiesen 1958、1973 退休仍研究；1973 与 Frisch/Tinbergen 共享诺奖、官方理由全句
11  科普经典 — 《所罗门王的指环》《攻击与人性》《狗遇人》：把行为学带给公众；2002 排名 20 世纪被引 65 位
12  荣誉矩阵 — Kalinga 1969、Cino Del Duca 首奖 1969、Pour le Mérite、ForMemRS、德国联邦大十字；三所以其命名的奥地利研究所（KLI/KLF/KIE）
13  晚年生态行动 — 支持奥地利绿党、1984 领衔 Hainburg 多瑙河电站抗议的 Konrad Lorenz Volksbegehren（环保公民运动，page.md 明载）
14  家庭与身后 — 妻 Margarethe Gebhardt（儿时伴侣、妇科医生）一子二女；1989-02-27 逝于 Altenberg；埋骨家族庄园之地
15  结尾（OpenMathAI 品牌口径）
```

## 七、特殊陷阱表（★ 核心）

| 陷阱 | 说明 |
|------|------|
| 共享结构 | 1973 三人共享同一句理由；分工：Lorenz=印记与本能理论综合、Frisch=蜜蜂感觉与通讯、Tinbergen=实验设计验证——勿混写 |
| 印记归属 | 印记现象由 **Douglas Spalding** 在 19 世纪发现、其师 **Heinroth** 亦有研究；Lorenz 的贡献是 1935《鸟之伴侣》的奠基性描述（Prägung）——"发现"与"描述"勿混 |
| 纳粹时期（★ 最高敏感）| 入党 1938、波森种族研究参与、战后一度否认、2015 萨尔茨堡大学撤销荣誉博士、反犹玩笑信件等——**涉纳粹与种族主义政治敏感，立传一律不展开、不设专页**；如须提及仅限一句中性陈述"其二战期间经历复杂、晚年曾表示悔恨"，其余由主控/Review 裁定 |
| 战俘叙事 | 1944 被俘/亚美尼亚战俘营/椋鸟与手稿是 page.md 明载的文学性段落，可写；其自述被俘年份（1942）与史实（1944）有出入——以史实为准并注记 |
| 家鹅退化论 | 杂交鹅观察引出的"文明人类退化"忧虑与两篇论文——系其纳粹时期观点的思想源头，**不写**；仅保留其纯粹动物学结论 |
| 群体选择争议 | Dawkins 批评其"good of the species"思维违反正统达尔文主义——page.md 明载，可客观一句（学术争议非政治） |
| 生态运动 | Hainburg 反电站公民运动系环保议题（非政党政治），可客观一页——1984 Volksbegehren |
| 家庭 | 妻 Margarethe 系儿时伴侣+妇科医生（园丁之女）——岳家反对婚事的细节 page.md 无载勿杜撰；一子二女不入库 |
| 引语红线 | 可引：诺奖自传（父母容忍、尼尔斯骑鹅）、Tinbergen 对其贡献的总结、Popper 合著书名；纳粹相关段落即使 page.md 有英文原文（入党申请等）**一律不引** |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| imprinting (Prägung) | 印记 | 早期结合现象，Spalding 先发现 |
| fixed action pattern | 固定动作模式 | 本能行为的单位 |
| innate releasing mechanism (IRM) | 先天释放机制 | 与 Tinbergen 共同发展 |
| supernormal stimulus | 超常刺激 | 巨蛋/红腹模型实验 |
| psychohydraulic model | 心理水力模型 | 动机模型（有争议） |
| greylag goose | 灰雁 | 标志性研究对象 |
| Umwelt | 周围世界（环境界） | 源自 Uexküll |
| ethology | 动物行为学 | 本届诺奖共同领域 |

## 九、背景音乐选择

- **选定曲目**：**Daylight** — Alex-Productions（manifest 预分配）
- **匹配理由**："白昼/破晓"贴合 Altenberg 湿地清晨跟着灰雁散步的画面——行为学从"看动物"开始；明快温暖的曲式承载《所罗门王的指环》式的亲和叙事，与其复杂历史背影形成克制平衡。
- **本地路径**：music_audio/ 下 Alex-Productions Daylight 曲目（执行时按 curated_tracks.md 对应文件复制到本目录）。
