# 医学家立传提示词（Thomas C. Südhof）

> OpenMedic 项目 · 21 世纪诺贝尔生理学或医学奖 2013 年得主（与 James Rothman、Randy Schekman 三人共享）。
> 本文件是 Thomas C. Südhof 的人物专属立传提示词：事实基准唯一来源为本地 Wikipedia 页面，
> 执行方按本提示词产出 15 页 Beamer 立传（本阶段不写 tex，仅沉淀事实与规范）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Thomas Christian Südhof（1955-12-22 生于德国哥廷根，在世）
- **气质关键词**：**突触前末端的解码者、神经递质释放机器的发现人、从巴松管到突触的双轨人生**
- **诺奖获奖理由（2013，逐字引用 medic/nobel_medicine_citations.json）**：
  > "for their discoveries of machinery regulating vesicle traffic, a major transport system in our cells"
  > （因其发现调节囊泡运输的机制——细胞内的一个主要转运系统）——注意 "their"：与 James Rothman、Randy Schekman 三人共享
- **设计母题**：**突触与钙（synapse and calcium）**。钙离子涌入、synaptotagmin 作钙传感器、囊泡与
  突触前膜融合——视觉母题用一枚囊泡贴近弧形膜的瞬间 + 钙离子小点迸发，象征"神经通讯的最后一毫秒"。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Thomas_C._Südhof/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 medic 路径执行：页面读 `medic/presentations/pages/21th_century/{Dir}/page.md`，
> 产出放 `medic/presentations/21th_century/Thomas_C._Südhof/`，数据库写 greatminds 库（MySQL）。

- **第 0 步**：核对本地 page.md 事实基准（本提示词第三、四、七节已沉淀，执行时再逐句复核）
- **第 1 步**：建目录 `medic/presentations/21th_century/Thomas_C._Südhof/`（含 `images/`）
- **第 2 步**：复制 Makefile，设 `MAIN=Thomas_C_Sudhof_zh`、`VIDEO_NAME=Thomas_C_Sudhof_zh`（宏名禁非 ASCII，ü 转拼音 u）
- **第 3 步**：收集肖像（page.md 无 infobox 肖像 URL 时用 Commons Special:FilePath 回退，404 则装饰圆占位）
- **第 4~9 步**：tex 编写 → 编译循环（0 error、vbox≤10pt、hbox≤50pt）→ pdftoppm 逐页目检 → make images/video → Review

## 三、研究领域梳理 + 入库（与 yaml fields 完全一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | neuroscience | 神经科学 | 突触传递与突触前机制，诺奖核心 | 核心页 |
| 1 | neurobiology | 神经生物学 | frontmatter field_of_work | 身份页 |
| 2 | biochemistry | 生物化学 | 博士训练与 LDL 受体时期的学科底色 | 教育页 |
| 3 | molecular biology | 分子生物学 | SNARE/synaptotagmin/neurexin 等分子发现 | 核心页 |

## 四、社会关系梳理 + 入库（与 yaml relations 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Victor P. Whittaker | 师→生（博士导师） | 哥廷根马普生物物理化学研究所博士导师（肾上腺嗜铬细胞），1982 |
| advisor-student | Michael Stuart Brown | 师→生（博士后导师） | UT Southwestern 分子遗传系博士后（1983–1986） |
| advisor-student | Joseph L. Goldstein | 师→生（博士后导师） | UT Southwestern 分子遗传系博士后（1983–1986），LDL 受体基因克隆 |
| co-honored | James Rothman | 无向 | 2013 诺贝尔生理学或医学奖三人共享（发现调节囊泡运输的机制） |
| co-honored | Randy W. Schekman | 无向 | 2013 诺贝尔生理学或医学奖三人共享（发现调节囊泡运输的机制） |
| spouse | Lu Chen | 无向 | 现任妻子，斯坦福神经外科与精神病学教授，育三子女 |

> 说明：Richard Scheller 与 Südhof 共享 Spencer 1993/NAS 分子生物学奖 1997/Kavli 2010/Lasker 2013
> 等多项非诺奖奖项——按口径**不建边**（co-honored 仅诺奖同届），陷阱表注明防 Review 误加。
> 前妻 Annette Südhof（育四子女）page.md 有载但不入库（防噪声，家族叙事一句带过）。
> 对手方规范名：库内无 Whittaker/Brown/Goldstein/Rothman，本侧按 page.md 形式新建 stub
> （"Michael Stuart Brown"/"Joseph L. Goldstein" 用 page.md 正文形式）。
> 自查 SQL：`SELECT COUNT(*) FROM person_relation WHERE from_id=<pid> OR to_id=<pid>;` 预期 = 6。

## 五、配色方案

- **气质**：精密、双轨（音乐与科学）、直面争议的坦率
- **主色**：德意志深蓝 `#16324F`（哥廷根学统与突触间隙的深邃）+ 香槟金 `#D4AF37`（诺奖色）
- **四分类色 badge**：
  - `badgeSynapse` 突触传递 — 电光蓝 `#4C5FD5`
  - `badgeCalcium` 钙传感 — 暖橙 `#E07B30`
  - `badgeSNARE` SNARE 机器 — 冷青 `#0E7C7B`
  - `badgeAward` 荣誉 — 皇家紫 `#52307C`
- **背景母题**：弧形突触膜 + 囊泡圆点 + 钙离子小点迸发

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover 共享首页）
01  封面 — 突触前的最后一毫秒 / Thomas C. Südhof 1955– + 四色 badge + 国籍行（Germany / United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格：生卒/哥廷根出身/教育 RWTH Aachen + Harvard + 哥廷根 MD 1982/任职 UT Southwestern→Stanford/核心领域
03  核心贡献概览 — synaptotagmin / SNARE 机器 / 突触形成分子 / 诺奖
04  哥廷根与巴松管 (1955–1982) — 童年在哥廷根与汉诺威；Waldorf 学校 1975；巴松管教师 Herbert Tauscher 被其称为 "most influential teacher"（page.md 明载原短语）；人智学家庭出身、青年时离开该信仰
05  马普研究所：Whittaker 门下 (1982) — 博士论文研究嗜铬细胞的肾上腺素/去甲肾上腺素释放（战斗或逃跑反应的细胞基础）
06  达拉斯：Brown/Goldstein 时期 (1983–1986) — 博士后；克隆 LDL 受体基因、解释其转录的胆固醇调控；LDL 受体功能→受体介导内吞原理（Brown/Goldstein 1985 诺奖的工作）
07  从胆固醇到突触 (1986) — 结束博士后、HHMI investigator、UT Southwestern 建组；甾醇调节元件工作（与他汀类药物研发的因果链——Atorvastatin/Lipitor 曾是 2008 年全球销量第一处方药）
08  突触前机制的发现（核心贡献页）— synaptotagmin（钙传感器触发囊泡融合）、RIM/Munc13/Munc18、SNARE 复合体成员（synaptobrevin/syntaxin/SNAP25）；破伤风与肉毒毒素作用机制
09  突触的形成 — neurexin（突触前）×neuroligin（突触后）跨突触蛋白桥；SynCAM/Latrophilins；这些蛋白突变与遗传性自闭症的关联
10  2013 诺贝尔奖 — 理由逐字；21 年 UT Southwestern 岁月总结一句
11  荣誉与认可 — Spencer 1993（与 Scheller）· Feldberg 1994 · NAS 分子生物学奖 1997（与 Scheller）· NAS 院士 2002 · Bristol-Myers Squibb 2004 · Bernhard Katz 奖 2008（与 Jahn）· Kavli 2010（与 Scheller/Rothman）· Lasker 2013（与 Scheller）· Nobel 2013 · ForMemRS 2017
12  斯坦福与医学回响 — 2008 年转斯坦福（Avram Goldstein 讲席教授）；与 Marius Wernig 合作诱导神经元技术；阿尔茨海默/精神分裂/自闭症的机制知识；HHMI 小鼠模型项目
13  科学诚信的公开讨论 — PubPeer 上 30 余篇论文受质疑；撤回 2017 Neuron 与 2023 PNAS 两篇论文；Südhof 认为绝大多数批评不成立或属琐碎错误，并主动发起"老论文该不该公开纠错"的行业讨论——page.md 明载，须两面平衡呈现
14  公共事务 — 2023 年获联合国秘书长古特雷斯任命进入联合国科学咨询委员会；PLOS Biology 与华盛顿邮报上的科学政策文章
15  结尾
```

## 七、特殊陷阱表（★ 执行时必须核对）

| # | 陷阱 | 说明 |
|---|------|------|
| 1 | 获奖理由 | 逐字 "for their discoveries of machinery regulating vesicle traffic, a major transport system in our cells" |
| 2 | 国籍 | 德国出生德美双籍（Nobel 官方口径 "Germany United States"，page.md frontmatter 同）；勿写单籍 |
| 3 | 学位 | 哥廷根 1982 年 **MD（Dr.med.）**——医学科学博士，非 PhD；主课题在马普生物物理化学研究所 Whittaker 实验室完成 |
| 4 | 双博士后导师 | Brown 与 Goldstein 并列（1985 诺奖得主），研究 LDL 受体——这是胆固醇代谢线，与后来的突触线是两段人生，勿混 |
| 5 | Scheller 口径 | Spencer/NAS/Kavli/Lasker 四奖均与 Richard Scheller 共享——全部**不建库边**；且 Lasker 2013 共享者是 Scheller 而非 Rothman，勿写错 |
| 6 | Kavli 2010 | 共享者为 Scheller 与 James Rothman（非 Schekman）——Kavli 三人与 Nobel 三人不是同一组 |
| 7 | 引语红线 | "most influential teacher" 指**巴松管教师 Herbert Tauscher**（非科学导师）——page.md 有英文原短语可引，勿张冠李戴给 Whittaker |
| 8 | PubPeer 段 | 须两面平衡：批评存在（30 余篇）+ 撤稿两篇（2017 Neuron、2023 PNAS）+ 本人回应（批评多不成立、原始数据支持结论）+ 他发起的科学诚信讨论——不得单边写成"造假"或"无懈可击" |
| 9 | 他汀因果链 | LDL 甾醇调节元件→他汀类药物（Lipitor 2008 销量第一）——因果表述按 page.md "led to the subsequent development" 分寸，勿写成"发明他汀" |
| 10 | 人智学 | 出生于人智学（anthroposophical）家庭、青年时离开——一句客观带过，勿展开宗教评价 |
| 11 | 联合国任命 | 2023 年由古特雷斯任命进入联合国科学咨询委员会——职务性事实一笔，政治人物不做延伸 |
| 12 | 家庭 | 现妻 Lu Chen（斯坦福）三子女 + 前妻 Annette Südhof 四子女——前妻不入库，正文一句即可 |

## 八、术语清单

| 英文 | 中文 | 风险点 |
|------|------|--------|
| synaptic transmission | 突触传递 | 研究主轴 |
| presynaptic nerve terminal | 突触前神经末梢 | 其视角特色（此前学界重突触后） |
| synaptotagmin | 突触结合蛋白 | 钙传感器，触发囊泡融合 |
| SNARE complex | SNARE 复合体 | synaptobrevin+syntaxin+SNAP25 四螺旋束 |
| neurexin / neuroligin | 神经连接蛋白 / 神经配蛋白 | 跨突触配对，突变关联自闭症 |
| chromaffin cells | 嗜铬细胞 | 博士论文对象 |
| LDL receptor | 低密度脂蛋白受体 | 博士后时期成果 |
| receptor-mediated endocytosis | 受体介导的内吞 | 该时期阐明的普适原理 |
| sterol regulatory element | 甾醇调节元件 | 他汀药物研发的科学基础 |

## 九、背景音乐选择

- **选定曲目**：**Expedition** — Alex-Productions（manifest 预分配）
- **匹配理由**：Expedition 的探索感对应贯穿其生涯的两段远征——从哥廷根经达拉斯到斯坦福的地理迁徙，
  与从嗜铬细胞到 LDL 受体再到突触前机制的学科跨越；音乐的行进感贴合"解码神经通讯最后一毫秒"的纵深。
- **备选（未采用）**：Eternals（恒久感可用但 batch-03 已用于 Fire 篇，避开）、The Invisible Light（微观感好但基调偏暗）
- **本地路径**：`music_audio/` 下 alex-productions 曲库按 curated_tracks.md 对应条目复制为
  `medic/presentations/21th_century/Thomas_C._Südhof/Expedition.wav`
