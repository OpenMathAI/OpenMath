# 医学家立传提示词（Alan Lloyd Hodgkin）

> 本文件是 OpenMedic 项目「20 世纪诺贝尔生理学或医学奖得主人物专属立传提示词」。
> 目标人物：Alan Lloyd Hodgkin（1963 年诺贝尔生理学或医学奖得主，英国）。
> 用途：指导后续 Beamer 立传（15 页）与配套视频制作；事实基准为本地 Wikipedia 页面
> `medic/presentations/pages/20th_century/Alan_Lloyd_Hodgkin/page.md`（下称 page.md）。
> 社会关系与研究领域已按本文件第三、四节入库 greatminds 库（yaml 与本文件完全一致）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Sir Alan Lloyd Hodgkin（艾伦·劳埃德·霍奇金，1914-02-05 班伯里 ~ 1998-12-20 剑桥，享年 84 岁）
- **气质关键词**：**动作电位离子机制的解谜者、Hodgkin-Huxley 模型的第一作者、皇家学会第 53 任主席** —— 1963 年诺贝尔生理学或医学奖获奖理由（逐字引自 medic/nobel_medicine_citations.json，与 Huxley、Eccles 三人共享）：
  > "for their discoveries concerning the ionic mechanisms involved in excitation and inhibition in the peripheral and central portions of the nerve cell membrane"
  > （因其关于神经细胞膜外周与中枢部分兴奋和抑制的离子机制的发现）
- **设计母题**：**「电压钳下的离子之舞」**。把膜电压钉在设定值、测量钠钾离子流——视觉隐喻：示波器钠/钾双电流波形与 Hodgkin 循环的正反馈回路。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Alan_Lloyd_Hodgkin/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 **medic 路径**执行：页面用 `medic/presentations/pages/20th_century/Alan_Lloyd_Hodgkin/`，成目录 `medic/presentations/20th_century/Alan_Lloyd_Hodgkin/`，Makefile 复制后设 `MAIN=Alan_Lloyd_Hodgkin_zh`、`VIDEO_NAME=Alan_Lloyd_Hodgkin_zh`，BGM 见第九节。
> 第 4 步（研究领域）与第 4.5 步（社会关系）**已完成入库**，见第三、四节。
> 数据库已置 `has_social_data=1`；`has_biography` 待 Beamer 立传完成后置 1。

## 三、研究领域梳理 + 入库（已完成）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | physiology | 生理学 | 神经冲动传导研究，1963 诺奖核心 | 总览页 |
| 1 | biophysics | 生物物理学 | Hodgkin-Huxley 模型、电压钳、Hodgkin 循环 | 模型页 |
| 2 | electrophysiology | 电生理学 | 枪乌贼巨轴突胞内记录、视觉感受器晚年研究 | 电生理页 |

## 四、社会关系梳理 + 入库（已完成，与 MySQL/data/Alan_Lloyd_Hodgkin.yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Andrew Huxley | — | 1963 诺贝尔生理学或医学奖三人共享（离子机制） |
| co-honored | John Eccles (neurophysiologist) | — | 1963 诺贝尔生理学或医学奖三人共享（离子机制） |
| collaborator | Andrew Huxley | — | 1939 巨轴突胞内记录，1952 五连论文建 Hodgkin-Huxley 模型 |
| collaborator | Bernard Katz | — | 1945 年战后重启合作，确证动作电位期间钠通透性骤增 |
| collaborator | W. A. H. Rushton | — | 1945 年恢复合作，共论神经纤维膜参数测算 |
| collaborator | Richard Keynes | — | 合作证明钠钾逆向转运的分泌机制 |
| collaborator | Kenneth Stewart Cole | — | 洛克菲勒研究所相识并合著论文，其电压钳为关键方法来源 |
| influence | Edgar Adrian | — | 剑桥授课讲师，1945 年为其请豁免兵役，1953 年提名其诺奖 |
| spouse | Marion Rous | — | 1944 年成婚，岳父为 1966 诺奖得主 Peyton Rous |
| parent-child | George Hodgkin | 父 | 贵格会教徒，1918 年殁于巴格达 |
| parent-child | Mary Wilson Hodgkin | 母 | — |
| parent-child | Jonathan Hodgkin | 子 | 剑桥分子生物学家 |
| parent-child | Deborah Hodgkin | 女 | 心理学家 |

> 说明：与 Huxley 同时建 co-honored + collaborator 双边（1963 三人共享+1939/1952 长期合作）。学生 Sarah/Rachel 仅具名无叙事不入库（Jonathan/Deborah 有职业叙事已入库）；父亲友人 Keith Lucas、继父 Lionel Smith、曾叔祖 Thomas Hodgkin（霍奇金淋巴瘤命名者）等家族背景不入库；Gasser（邀请）、Erlanger（挑战性建议）、Lorente de Nó（洛克菲勒同侪）为过场人物不入库；同学 Sanger/Lack/Britten 等仅校友提及不入库；「Cambridge Apostles」「反战传单」等政治叙事一笔带过不建边。

## 五、配色方案 【人物专属】

- **气质**：英式实验物理学的精密、战争工程师的务实、剑桥学统的从容
- **主色**：离子通道蓝紫 `#3E4E8C`（钠钾电流的双色叠加）
- **诺奖色**：香槟金（奖章/年份徽章专用）
- **四分类色（badgeA-D）**：
  - `badgeA` 生理学 — 神经青 `#2E7A8C`
  - `badgeB` 生物物理学 — 模型紫 `#5B4E8E`
  - `badgeC` 电生理学 — 电压钳金橙 `#C08A2E`
  - `badgeD` 视觉研究 — 视网膜绿 `#3A7A5C`
- **背景母题**：钠/钾双电流波形（先升后落的双峰）与 Hodgkin 循环环形箭头，低透明度铺底

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input medic/presentations/cover/）
01  封面 — 动作电位离子机制的解谜者 / Alan Lloyd Hodgkin 1914–1998 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、教育、任职、家庭、荣誉、核心领域）
03  核心贡献概览 — 局部回路理论 / 电压钳与离子流 / Hodgkin-Huxley 模型 / 钠钾泵
04  贵格家庭与丧父 (1914–1932) — 信徒反征兵受迫害、1918 父亲病逝巴格达、博物学与观鸟少年
05  剑桥三一学院 (1932–1935) — 植物动物化学奖学金、Adrian 的生理学课、1934 坐骨神经实验起步
06  洛克菲勒研究所 (1937–1938) — Gasser 邀请、遇 Cole/Lorente de Nó 并合著论文、伍兹霍尔初识枪乌贼巨轴突
07  局部回路理论与圣路易斯之问 (1938) — Erlanger 的验证条件、海水/油体对比实验
08  1939 普利茅斯：胞内记录（核心页）— 与 Huxley 把微插管插入巨轴突、Nature 短讯、二战爆发中断
09  战年雷达 (1939–1945) — 皇家飞机研究院航空医学、TRE 厘米波雷达、Village Inn 机枪瞄准系统、MIT 交流
10  1945-1952：五连论文（核心页）— 与 Huxley/Katz 普利茅斯夏季三连、电压钳、钠钾氯选择性通透、微分方程模型
11  1963 诺贝尔奖（核心页）— citation 原文、三人共享、1961 误报风波（Békésy 得奖）、宴会上代表三人致谢辞
12  皇家学会主席岁月 (1970-1975) — Foulerton 教授、1972 KBE、1973 OM、三一学院 Master (1978-84)、莱斯特校长
13  晚年视觉研究 — 与 Baylor/Detwiler 的龟光感受器系列论文
14  遗产 — Hodgkin-Huxley 模型成为计算神经科学基石；离子通道假说经 patch clamp（Neher/Sakmann 1991、MacKinnon 2003）证实
15  结尾
```

## 七、特殊陷阱表（★ 执行 Beamer 前必读）

| # | 陷阱 | 裁定 |
|---|------|------|
| 1 | 获奖理由表述 | 逐字用 citation 原文（their 三人共享，离子机制+外周与中枢）；Hodgkin/Huxley 部分是动作电位、Eccles 部分是突触——分工勿混 |
| 2 | 三人分工 | page.md Awards 节把 1963 年奖概括为「研究突触」——以 citation 原文为准（外周与中枢离子机制），勿被该行误导 |
| 3 | 钠通道假说 | 离子通道的存在「confirmed only decades later」——patch clamp/通道学界的 1991/2003 诺奖是下游证据，写「预言数十年后证实」 |
| 4 | 1961 误报 | 1961 年 10 月瑞典记者误报三人得奖、实为 von Békésy——趣闻可作一帧细节，勿当真获奖记录 |
| 5 | 岳父 | Marni 之父 Francis Peyton Rous 1966 年诺奖——翁婿两次同席诺奖典礼（1963/1966）可作彩蛋；Rous 本人不建边 |
| 6 | 引语红线 | 自传 Chance and Design 写作动机、贵格家庭叙事为叙述语；「having been brought up as a supporter of the British Labour Party」有原文可引；反战传单段一笔带过不展开 |
| 7 | 战争段 | 战年贡献（雷达/航空医学/Village Inn）是其人生大块——如实体现在时间线帧，列装细节取一二即可 |
| 8 | 贵格与从军 | 因 1932 年德国之行放弃和平主义信念——内心转变 page 明载可写，一句带过 |
| 9 | 师承 | 无博士导师明载（三一 research fellow 起家）——Adrian 建 influence（授课+豁免+提名），勿建师生边 |
| 10 | metadata 冲突 | frontmatter 无 doctoral_advisor；children 列表四人中 Sarah/Rachel 无叙事不入库；occupation 含 biochemist 噪声 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| action potential | 动作电位 | 神经冲动的电信号 |
| Hodgkin–Huxley model | 霍奇金-赫胥黎模型 | 四微分方程的电学等效模型 |
| voltage clamp | 电压钳 | 源自 Cole 的关键技术 |
| Hodgkin cycle | 霍奇金循环 | 去极化-钠内流的正反馈 |
| squid giant axon | 枪乌贼巨轴突 | 普利茅斯的模型系统 |
| local circuit theory | 局部回路理论 | 1937-38 验证的传导理论 |
| Goldman–Hodgkin–Katz equation | GHK 方程 | 与 Goldman/Katz 共同命名 |
| Na+/K+-ATPase | 钠钾 ATP 酶 | Skou 1997 诺奖，钠泵机制 |
| patch clamp | 膜片钳 | 离子通道证实的下游技术 |
| saltatory conduction | 跳跃传导 | 有髓纤维传导（Huxley 与 Stämpfli） |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Daylight** — Alex-Productions（manifest 预分配）
- **匹配理由**：
  - 「白昼/明澈」匹配其科学风格——把毫秒级的黑暗电信号变成清晰的微分方程，是神经科学的「天亮时刻」
  - 明快而有节制的编曲契合其务实、 collaborators 众多的实验室群像
- **备选**（未采用）：Ascension（上升感贴切但物理侧占用）、Eternals（batch-08 Dale 已用）
- **本地路径**：按 music_audio/ 内 Alex-Productions Daylight 曲目复制至 `medic/presentations/20th_century/Alan_Lloyd_Hodgkin/Daylight.wav`，ffmpeg `-shortest` 对齐
