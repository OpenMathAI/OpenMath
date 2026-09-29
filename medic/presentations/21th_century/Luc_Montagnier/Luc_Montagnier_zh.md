# 医学家立传提示词（Luc Montagnier）

> OpenMedic 项目 · 21 世纪诺贝尔生理学或医学奖 2008 年得主（HIV 半奖之一） · 本文件是该人物的专属立传提示词，
> 按 9 节结构执行 Beamer 立传；数据库入库（fields/relations）已由批次完成，本文件第四/三节与 yaml 一致。

## 一、背景信息 【人物专属】

- **目标医学家**：Luc Montagnier（1932-08-18 生于沙布里 ~ 2022-02-08 逝于塞纳河畔纳伊，享年 89 岁）
- **气质关键词**：**HIV 的首先分离者、与 Gallo 之争的中心人物、晚年走向争议边缘的诺奖得主** —— 2008 年获奖理由（逐字引用 medic/nobel_medicine_citations.json，与 Barré-Sinoussi 共享同一句）：
  > "for their discovery of human immunodeficiency virus"
  > （因他们发现人类免疫缺陷病毒）
- **设计母题**：**显微镜下的 LAV 颗粒与分叉的小径（virion & forked road）**。1983 Science 论文、优先权之争的分岔路——"发现者与发现权的纠缠"的视觉隐喻。
- **本地 Wikipedia 路径**：medic/presentations/pages/21th_century/Luc_Montagnier/page.md
- **参考模板**：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）

## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章）

- 第 0/1/2/3 步按 **medic 路径**执行：事实基准 = `medic/presentations/pages/21th_century/Luc_Montagnier/page.md`；目录 `medic/presentations/21th_century/Luc_Montagnier/`；Makefile 改 `MAIN=Luc_Montagnier_zh`；肖像优先 images.txt 所列 Commons 图（Montagnier in 2008），失败用装饰圆占位。
- 第 4/4.5 步（入库）**已完成**（第三、四节与 `MySQL/data/Luc_Montagnier.yaml` 一致，勿重复入库）。
- 第 5-9 步：配色 → 幻灯片 → Beamer → 布局检查（0 error、vbox≤10pt、hbox≤50pt、逐页目检）→ 史实审查（第七节）。

## 三、研究领域梳理 + 入库（rank 0-4 表）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | virology | 病毒学 | 职业主领域（infobox Fields） | 封面 |
| 1 | retrovirology | 反转录病毒学 | HIV 分离、干扰素与病毒 | 发现页 |
| 2 | molecular biology | 分子生物学 | metadata 载业、DNA 信号等晚研究对象 | 争议页 |

## 四、社会关系梳理 + 入库（与 yaml 完全一致，已完成）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Françoise Barré-Sinoussi | 无向 | 1983 共同分离 LAV（HIV-1），Science 1983-05-20 |
| co-honored | Françoise Barré-Sinoussi | 无向 | 2008 诺贝尔生理学或医学奖共享（发现 HIV） |
| colleague | Jean-Claude Chermann | 无向 | Pasteur 团队成员，HIV 分离合作 |
| colleague | Willy Rozenbaum | 无向 | 临床医生，1982 提请研究不明综合征 |
| colleague | Robert Gallo | 无向 | 后和解：1987 共享发现者名义，2002 合著系列文章 |
| controversy | Robert Gallo | 无向 | HIV 分离优先权之争（1985-1991），1993 Chang 报告澄清 |
| spouse | Dorothea Ackerman | 无向 | 1961 结婚，育三子 |
| co-honored | Harald zur Hausen | 无向 | 2008 诺奖同届共享（HPV 与 HIV 两半） |

> 对手方规范名：均无库内记录按 page.md 形式新建 stub；Barré-Sinoussi/Zur Hausen 的 co-honored 与两篇镜像幂等合并。Gallo 的 colleague+controversy 双行均系 page.md 明载（先争后和）。

## 五、配色方案

- **气质**：法兰西科学家的锋芒 + 优先权之争的戏剧张力 + 晚年的孤独转向
- **主色**：深紫 `#4A2A6A`（争议与荣耀交织的暮色）
- **诺奖香槟金**：`#D4AF37`
- **badge 四分类色**：
  - `badgeA` HIV 发现 — 艾滋红 `#A63A2B`
  - `badgeB` 优先权之争 — 对峙灰蓝 `#3A4A6B`
  - `badgeC` 干扰素与病毒 — 实验青 `#2E7D8C`
  - `badgeD` 晚年争议 — 警示橙 `#C97B2D`
- **背景母题**：低透明度病毒颗粒 + 一条分叉路径细线（争论与和解两枝）。

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — HIV 的首先分离者 / Luc Montagnier 1932–2022 + badge + 右上头像 + 国籍行（France）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Chabris、Poitiers/巴黎大学、Pasteur 研究所、2008 诺奖）
03  核心贡献概览 — LAV 分离 / 软琼脂培养 / 优先权之争 / 晚年争议
04  沙布里少年与求学 (1932–1960) — 少年时代对科学着迷、Poitiers 理学院、索邦助手获博士
05  英伦岁月 (1960–1965) — Carshalton MRC 病毒研究组博士后、格拉斯哥病毒学研究所、发明软琼脂培养基培养病毒
06  Curie 与巴斯德 (1965–1982) — 居里研究所实验室主任 7 年、1972 转巴斯德研究干扰素抗病毒
07  1982：Rozenbaum 之问 — Bichat 医院临床医生求助、GRID→AIDS、反转录病毒假说、团队（Barré-Sinoussi/Chermann）
08  1983-05-20 Science：LAV — 淋巴结活检分离、命名 LAV、"其对 AIDS 的作用仍待确定"（page.md 实载转述）
09  Gallo 之争 (1983–1993) — 同期 Science 发表、HTLV-III、指控与"minor misconduct"、1993 Chang 报告（美样本源自法实验室污染）、今日共识：法组首先分离、Gallo 组证明致病——客观呈现
10  和解与命名 — 1986 LAV/HTLV-III 统一为 HIV、1987 两国政府 50-50 调停（密特朗-里根会晤）、2002 Science 合著文章互认
11  2008 诺贝尔奖 — 与 Barré-Sinoussi 共享 HIV 半、同届 zur Hausen HPV 半；"为 Gallo 遗憾"表态（page.md 英文原句可引）；Nobel Assembly Masucci 答复
12  晚年争议（客观一页，克制）— DNA 电磁信号论文（2009）、顺势疗法倾向（2010 Lindau）、2017 百余名学者公开信"叫停"；叙事仅 page.md 实载，勿加嘲讽笔调
13  家庭与身后 — 1961 娶 Dorothea Ackerman 育三子；2022-02-08 逝于 Neuilly-sur-Seine，89 岁
14  遗产：诊断之基与双面人生 — HIV 检测、抗艾科学的地基；Nobel disease 的注脚（一句）
15  结尾（OpenMathAI 品牌口径）
```

## 七、特殊陷阱表（★ 核心）

| 陷阱 | 说明 |
|------|------|
| 两半结构 | 2008 = Montagnier/Barré-Sinoussi 共享 HIV 半 + zur Hausen 独享 HPV 半；勿写 Gallo 同奖（他未获奖，Montagnier 仅公开表示遗憾） |
| Gallo 双边 | colleague（1987 共享名义、2002 合著）+ controversy（优先权之争）双行并存——叙事按时间轴展开，勿只取一面 |
| Chang 报告 | 1993 Roche 小组结论：美国样本源自法国实验室培养物污染（一个病人病毒污染另一培养物）；Gallo 实验室 1991/1992 "misconduct" 判定被 1993 报告澄清——因果链勿倒置 |
| 首句口径 | 今日共识（page.md 原文）：法组首先分离 HIV；Gallo 组证明其致 AIDS 并贡献 T 细胞培养等技术——分工表述勿混 |
| 发现初的保留 | 1983 论文原文称 HIV 致病作用 "remains to be determined"——勿写成立即断言因果 |
| 命名时间线 | LAV（1983）→ 1986 统一命名 HIV；HTLV-III 为 Gallo 方名称——三者勿混 |
| 政治敏感 | COVID-19 实验室起源相关争议**一律禁写**（涉及地缘政治，超出科学叙事边界）；晚年争议只写 DNA 电磁信号/顺势疗法/2017 公开信三件 page.md 实载事 |
| 争议笔调 | 晚年争议页保持中性客观（"被批评/被拒资助/自称 intellectual terror"），勿使用嘲讽词汇；"Nobel disease"一词可用但一笔带过 |
| 家庭 | 妻 Dorothea Ackerman 1961 结婚（三子）；卒地 Neuilly-sur-Seine——勿与巴黎混 |
| 引语红线 | 可引 page.md 有英文原文的句子（"surprised"、致 Gallo 遗憾句、CBC 答问句）；其余禁杜撰 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| LAV | 淋巴结病相关病毒 | 1983 法方命名 |
| HTLV-III | 人 T 淋巴细胞病毒 III 型 | Gallo 方命名 |
| HIV-1 | 人类免疫缺陷病毒 1 型 | 1986 统一命名 |
| soft agar culture | 软琼脂培养基 | 格拉斯哥时期发明 |
| interferon | 干扰素 | 巴斯德早期研究方向 |
| Office of Research Integrity | 美国研究诚信办公室 | 1990s 调查主体 |
| Chang report | Chang 报告 | 1993 Nature 样本溯源结论 |
| Nobel disease | 诺贝尔病 | 晚年争议的注脚词 |

## 九、背景音乐选择

- **选定曲目**：**Last Hope** — Alex-Productions（manifest 预分配）
- **匹配理由**："最后的希望"贴合 1980s 艾滋绝症阴影下分离 HIV 的历史时刻——发现本身就是绝望中的希望；同时容纳其一生"荣耀与争议并存"的复杂弧线，弦乐的张力匹配优先权之争的戏剧性。
- **本地路径**：music_audio/ 下 Alex-Productions Last Hope 曲目（执行时按 curated_tracks.md 对应文件复制到本目录）。
