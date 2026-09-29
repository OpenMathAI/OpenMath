# 医学家立传提示词（Andrew Huxley）

> 本文件是 OpenMedic 项目「20 世纪诺贝尔生理学或医学奖得主人物专属立传提示词」。
> 目标人物：Andrew Huxley（1963 年诺贝尔生理学或医学奖得主，英国）。
> 用途：指导后续 Beamer 立传（15 页）与配套视频制作；事实基准为本地 Wikipedia 页面
> `medic/presentations/pages/20th_century/Andrew_Huxley/page.md`（下称 page.md）。
> 社会关系与研究领域已按本文件第三、四节入库 greatminds 库（yaml 与本文件完全一致）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Sir Andrew Fielding Huxley（安德鲁·菲尔丁·赫胥黎，1917-11-22 伦敦汉普斯特德 ~ 2012-05-30 剑桥，享年 94 岁）
- **气质关键词**：**动作电位方程的书写者、肌丝滑行理论的共同奠基人、赫胥黎科学世家里自建设备的巧手工程师** —— 1963 年诺贝尔生理学或医学奖获奖理由（逐字引自 medic/nobel_medicine_citations.json，与 Hodgkin、Eccles 三人共享）：
  > "for their discoveries concerning the ionic mechanisms involved in excitation and inhibition in the peripheral and central portions of the nerve cell membrane"
  > （因其关于神经细胞膜外周与中枢部分兴奋和抑制的离子机制的发现）
- **设计母题**：**「滑行的细丝」**。肌动蛋白与肌球蛋白细丝相互滑行、横桥划桨——视觉隐喻：双排平行细丝与横桥小桨，叠加神经波形作底纹。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Andrew_Huxley/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 **medic 路径**执行：页面用 `medic/presentations/pages/20th_century/Andrew_Huxley/`，成目录 `medic/presentations/20th_century/Andrew_Huxley/`，Makefile 复制后设 `MAIN=Andrew_Huxley_zh`、`VIDEO_NAME=Andrew_Huxley_zh`，BGM 见第九节。
> 第 4 步（研究领域）与第 4.5 步（社会关系）**已完成入库**，见第三、四节。
> 数据库已置 `has_social_data=1`；`has_biography` 待 Beamer 立传完成后置 1。

## 三、研究领域梳理 + 入库（已完成）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | physiology | 生理学 | 神经与肌肉两大主题，1963 诺奖核心 | 总览页 |
| 1 | biophysics | 生物物理学 | Hodgkin-Huxley 方程、干涉显微镜、横桥方程 | 建模页 |
| 2 | muscle physiology | 肌肉生理学 | 1954 肌丝滑行理论、1957 力产生机制、1966 理论证明 | 肌肉页 |

## 四、社会关系梳理 + 入库（已完成，与 MySQL/data/Andrew_Huxley.yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Alan Lloyd Hodgkin | — | 1963 诺贝尔生理学或医学奖三人共享（离子机制） |
| co-honored | John Eccles (neurophysiologist) | — | 1963 诺贝尔生理学或医学奖三人共享（离子机制） |
| collaborator | Alan Lloyd Hodgkin | — | 1939 巨轴突胞内记录，1952 共建动作电位数学模型 |
| collaborator | Rolf Niedergerke | — | 1954 年合作发现肌丝滑行机制 |
| collaborator | Robert Stämpfli | — | 合作证明有髓神经纤维的跳跃传导 |
| colleague | Hugh Huxley | — | 无亲缘，1954 年同期独立观察到肌丝滑行，Nature 同期发表 |
| spouse | Jocelyn Richenda Gammell Pease | — | 1947 年成婚，2003 年卒 |
| parent-child | Leonard Huxley | 父 | 作家兼编辑 |

> 说明：与 Hodgkin 同时建 co-honored + collaborator 双边。Hugh Huxley（3805，库内既有）与本人**无亲缘关系**（分属不同 Huxley 支系）——colleague 边 note 已注明「无亲缘」，立传中必须明确区分；Jean Hanson 是 Hugh Huxley 一侧的合作者，不入本篇。家庭叙事：同父异母兄 Aldous（作家）/Julian（生物学家）、祖父 T.H. Huxley——无兄妹/祖孙关系类型不入库，仅在家族帧文字呈现；六名子女仅具名与出生日期、无职业叙事，不入库；岳父 Michael Pease（遗传学家）不入库。

## 五、配色方案 【人物专属】

- **气质**：工程师的巧手、数学家的缜密、维多利亚科学世家的底色
- **主色**：肌丝绯红 `#9E3542`（肌动蛋白染色的深红）
- **诺奖色**：香槟金（奖章/年份徽章专用）
- **四分类色（badgeA-D）**：
  - `badgeA` 生理学 — 神经青 `#2E7A8C`
  - `badgeB` 生物物理学 — 方程紫 `#5B4E8E`
  - `badgeC` 肌肉生理学 — 滑丝红 `#9E3542`
  - `badgeD` 干涉显微镜 — 光学银 `#8A98A8`
- **背景母题**：平行双排细丝与横桥短桨阵列、稀疏干涉条纹，低透明度铺底

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input medic/presentations/cover/）
01  封面 — 书写神经方程的人 / Andrew Huxley 1917–2012 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像（1963 照）+ 右信息网格（生卒、教育、任职、家庭、荣誉、核心领域）
03  核心贡献概览 — Hodgkin-Huxley 方程 / 肌丝滑行理论 / 干涉显微镜 / 跳跃传导
04  赫胥黎家的工程师 (1917–1935) — 作家父亲、车床与内燃机少年、Westminster King's Scholar
05  剑桥与转向生理学 (1935–1939) — 本欲学工程、选修生理课后改道、1939 加入 Hodgkin
06  普利茅斯：巨轴突 (1939)（核心页）— 微插管插入枪乌贼巨轴突、首次胞内动作电位记录、Nature 短讯
07  战年 (1939–1945) — 防空高炮指挥部雷达控制、海军部火炮工作组（Blackett 麾下）、为 Hodgkin 造瞄准具零件
08  1946-1952：方程之年（核心页）— 重启合作、电压钳测量钠钾流、1952 五连论文与最早的生物数学模型之一
09  1963 诺贝尔奖（核心页）— citation 原文、三人共享（Hodgkin/Huxley 动作电位、Eccles 突触）、诺奖讲坛
10  另一个战场：肌肉 (1952-1954) — 干涉显微镜自制、1953 Niedergerke、1954-05-22 Nature 双论文与 Hugh Huxley/Hanson 同期发表
11  滑丝理论与证明 (1957–1966) — 横桥方程新范式、1966 年团队给出理论证明
12  行政与学会 — UCL 生理系主任 (1960)、Royal Society Research Professor (1969)、1980-85 Royal Society 主席、达尔文演说捍卫进化论
13  三一学院 Master (1984–1990) — 接替长期合作者 Hodgkin、打破文理交替传统、「三一的诺奖得主比全法国多」
14  遗产 — 电压门控通道研究的地基、肌肉生理学现代范式、Copley 1973 · OM 1983 · HonFREng 1986
15  结尾
```

## 七、特殊陷阱表（★ 执行 Beamer 前必读）

| # | 陷阱 | 裁定 |
|---|------|------|
| 1 | 获奖理由表述 | 逐字用 citation 原文（their 三人共享）；Huxley 与 Hodgkin 份额是外周动作电位的实验与数学工作、Eccles 是突触传递——正文分工表述与 Hodgkin 篇对齐 |
| 2 | 两个 Huxley | Hugh Huxley（肌肉，无亲缘）与 Andrew Huxley 同期分别与 Hanson/Niedergerke 合作提出滑丝理论，1954-05-22 同期 Nature 四人两文——「Huxley」姓氏重合是本篇最大混淆点，行文必须全名区分；库内 Hugh Huxley(3805) 已有记录，colleague 边注明无亲缘 |
| 3 | 赫胥黎家族 | 祖父 T.H. Huxley（达尔文斗犬）、同父异母兄 Aldous（《美丽新世界》）/Julian（生物学家）——家族帧一句带过；1981 年主席演说捍卫达尔文进化论呼应曾祖 1860 年之辩（page 明载可写） |
| 4 | 无博士导师 | Huxley 是 Hodgkin 的 postgraduate student/合作者，非正式博士生——两人建 collaborator+co-honored，勿建师生边 |
| 5 | 战时细节 | 防空指挥部→海军部（Blackett 团队）；Hodgkin 有瞄准具难题找他画草图借车床造零件——科学友谊的战时插曲，可作趣闻帧 |
| 6 | 引语红线 | 「Trinity 拥有比全法国更多的诺奖得主」为访谈转述可引（英文原意）；其余叙事无直接引语，禁编造；Margaret Thatcher 当选 FRS 的辩护属学会内部争议，一句史实带过或不提 |
| 7 | 生卒 | 1917-11-22 Hampstead ~ 2012-05-30 剑桥 Addenbrooke's 医院，享年 94——无日期冲突 |
| 8 | 子女 | 六名子女（Janet/Stewart/Camilla/Eleanor/Henrietta/Clare）仅具名与生日，无叙事——不入库，家族帧只写「一子五女」 |
| 9 | 荣誉年代链 | FRS 1955 · Nobel 1963 · Copley 1973 · Knight Bachelor 1974 · OM 1983 · HonFREng 1986 · RS 主席 1980-85 · Trinity Master 1984-90，勿错置 |
| 10 | metadata 冲突 | frontmatter occupation 含 physicist（本欲学工程出身，可在正文叙述）；field 单一 physiology，yaml fields 加 biophysics/muscle physiology 均为正文明载 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| Hodgkin–Huxley model | 霍奇金-赫胥黎模型 | 动作电位微分方程模型 |
| sliding filament theory | 肌丝滑行理论 | 1954 年四人两文同期发表 |
| interference microscopy | 干涉显微镜 | 其自制主力设备 |
| cross-bridge | 横桥 | 肌球蛋白划桨结构 |
| actin / myosin | 肌动蛋白 / 肌球蛋白 | 滑丝理论的两类细丝 |
| saltatory conduction | 跳跃传导 | 有髓纤维传导方式 |
| voltage clamp | 电压钳 | 与 Hodgkin 共用的测量技术 |
| giant axon | 巨轴突 | 长鳍近岸枪乌贼 |
| Order of Merit | 功绩勋章 | 1983 授予 |
| Trinity College, Cambridge | 剑桥三一学院 | 其一生学术主场 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Savage** — Alex-Productions（manifest 预分配）
- **匹配理由**：
  - 「野性/力量」罕见地匹配肌肉主题——滑丝理论的每一次收缩都是分子马达的爆发，Savage 的节奏能量贴合横桥划桨的力学意象
  - 强劲推进感也契合其「自建设备攻克两个巨大难题」的工程师韧性
- **备选**（未采用）：Ascension（上升感贴切但物理侧占用）、Daylight（本批 Hodgkin 已用，双人组曲目须区分）
- **本地路径**：按 music_audio/ 内 Alex-Productions Savage 曲目复制至 `medic/presentations/20th_century/Andrew_Huxley/Savage.wav`，ffmpeg `-shortest` 对齐
