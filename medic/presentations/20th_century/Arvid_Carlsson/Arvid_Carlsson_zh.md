# 医学家立传提示词（Arvid Carlsson）

> 本文件是 OpenMedic 项目「20 世纪诺贝尔生理学或医学奖得主人物专属立传提示词」。
> 目标人物：Arvid Carlsson（2000 年诺贝尔生理学或医学奖得主，瑞典）。
> 用途：指导后续 Beamer 立传（15 页）与配套视频制作；事实基准为本地 Wikipedia 页面
> `medic/presentations/pages/20th_century/Arvid_Carlsson/page.md`（下称 page.md）。
> 社会关系与研究领域已按本文件第三、四节入库 greatminds 库（yaml 与本文件完全一致）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Arvid Carlsson（阿维德·卡尔松，1923-01-25 乌普萨拉 ~ 2018-06-29 哥德堡，享年 95 岁）
- **气质关键词**：**确立多巴胺为神经递质的人、L-Dopa 帕金森疗法的奠基者、九旬仍与研究者和女儿并肩的 Sweden 药理学家** —— 2000 年诺贝尔生理学或医学奖获奖理由（逐字引自 medic/nobel_medicine_citations.json，与 Greengard、Kandel 三人共享）：
  > "for their discoveries concerning signal transduction in the nervous system"
  > （因其关于神经系统信号转导的发现）
- **设计母题**：**「利血平与 L-Dopa」**。利血平耗竭多巴胺致运动丧失、补回 L-Dopa 症状缓解——视觉隐喻：一条多巴胺浓度曲线的坠落与回升。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Arvid_Carlsson/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 **medic 路径**执行：页面用 `medic/presentations/pages/20th_century/Arvid_Carlsson/`，成目录 `medic/presentations/20th_century/Arvid_Carlsson/`，Makefile 复制后设 `MAIN=Arvid_Carlsson_zh`、`VIDEO_NAME=Arvid_Carlsson_zh`，BGM 见第九节。
> 第 4 步（研究领域）与第 4.5 步（社会关系）**已完成入库**，见第三、四节。
> 数据库已置 `has_social_data=1`；`has_biography` 待 Beamer 立传完成后置 1。

## 三、研究领域梳理 + 入库（已完成）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | neuropharmacology | 神经药理学 | 多巴胺神经递质地位的确立，2000 诺奖核心 | 总览页 |
| 1 | dopamine signalling | 多巴胺信号 | 基底节多巴胺测定、利血平/L-Dopa 动物模型 | 多巴胺页 |
| 2 | Parkinson's disease | 帕金森病 | L-Dopa 疗法的科学与临床奠基 | 临床页 |

## 四、社会关系梳理 + 入库（已完成，与 MySQL/data/Arvid_Carlsson.yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Paul Greengard | — | 2000 诺贝尔生理学或医学奖三人共享（神经系统信号转导） |
| co-honored | Eric Kandel | — | 2000 诺贝尔生理学或医学奖三人共享（神经系统信号转导） |
| influence | Bernard Brodie | — | 1955-56 年在其 NHI 实验室访学五月，转向精神药理学 |
| spouse | Ulla-Lisa Christoffersson | — | 1945 年成婚，育三子二女 |
| parent-child | Maria Carlsson | 女 | 其实验室管理者 |
| parent-child | Lena Carlsson | 女 | 多巴胺稳定剂 OSU6162 研究合作者 |

> 说明：与 Brodie 用库内既有记录 Bernard Brodie（6134，防 Bernard Beryl Brodie 分裂）建 influence（访学五月转向精神药理学——「eventually led to his Nobel Prize」page 明载）。女儿 Maria/Lena 具名且有角色叙事（实验室管理者/合作者）入库；三子与另一女未具名不入库。父亲（隆德大学历史学教授）未具名不入库。Greengard/Kandel 用 manifest 规范名（med-batch-35）。Montagu（1957 年先证多巴胺存在于人脑）为并行科学史人物，无个人交往不入库。

## 五、配色方案 【人物专属】

- **气质**：北欧的执着、多巴胺的活力橙、九旬不辍的韧劲
- **主色**：多巴胺活力橙 `#C4622D`（儿茶酚胺的标志暖色）
- **诺奖色**：香槟金（奖章/年份徽章专用）
- **四分类色（badgeA-D）**：
  - `badgeA` 神经药理学 — 利血平青 `#1F7A6D`
  - `badgeB` 多巴胺信号 — 突触橙 `#C08A2E`
  - `badgeC` 帕金森病 — L-Dopa 金 `#D9A441`
  - `badgeD` SSRI 先声 — 血清素紫 `#6E5AA0`
- **背景母题**：多巴胺分子线稿与基底节剪影、坠落回升的浓度曲线，低透明度铺底

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input medic/presentations/cover/）
01  封面 — 确立多巴胺的人 / Arvid Carlsson 1923–2018 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像（2011 照）+ 右信息网格（生卒、教育、任职、家庭、荣誉、核心领域）
03  核心贡献概览 — 多巴胺递质地位 / 利血平-L-Dopa 模型 / 帕金森疗法 / SSRI 先声
04  乌普萨斯-隆德 (1923–1944) — 历史学教授之子转学医、1941 入隆德大学
05  1944：白船行动的检验者 — 参与检查贝尔纳多特亲王营救至瑞典的纳粹集中营囚徒（一句史实）
06  隆德到哥德堡 (1951–1959) — 1951 MD 与药理学 PhD、副教授、1955-56 赴 Bethesda Brodie 实验室五月
07  Brodie 访学的转折 — 转向精神药理学（「eventually led to his Nobel Prize」）、1959 哥德堡教授
08  多巴胺：不止是前体（核心页）— 1957 Montagu 先证其存在于人脑；同年 Carlsson 证明其为脑内神经递质
09  利血平与 L-Dopa 模型（核心页）— 耗竭-运动丧失-补回缓解、基底节高浓度测定法
10  2000 诺贝尔奖（核心页）— citation 原文、与 Greengard/Kandel 三人共享、诺奖演讲 A Half-Century of Neurotransmitter Research
11  L-Dopa 的临床接力 — 其他医生将其推入帕金森病人、至今仍是最常用疗法的基础
12  SSRI 的先声 — 与 Astra 合作从溴苯那敏 derives 齐美利定（首个上市 SSRI）、后因罕见格林-巴利综合征撤市、铺路 Prozac
13  九旬不辍 — 与女儿 Lena 研发多巴胺稳定剂 OSU6162 改善卒中后疲乏
14  公共立场与荣誉 — 反对饮水加氟、反对顺势疗法入药典；Wolf 1979 · Japan Prize 1994 · Feltrinelli 1999 · Nobel 2000
15  结尾
```

## 七、特殊陷阱表（★ 执行 Beamer 前必读）

| # | 陷阱 | 裁定 |
|---|------|------|
| 1 | 获奖理由表述 | 逐字用 citation 原文 "for their discoveries concerning signal transduction in the nervous system"（their 三人共享同一理由）；三人分工：Carlsson 多巴胺/Greengard 磷酸化级联/Kandel 学习记忆——各段勿混 |
| 2 | Montagu 优先权 | 1957 年 Katharine Montagu 先证多巴胺存在于人脑，同年 Carlsson 证明其为脑内神经递质（递质地位而非仅前体）——两步归属勿混， Montagu 无个人交往不建边 |
| 3 | 白船行动 | 1944 年参与检查 Bernadotte 亲王营救的集中营囚徒——page 明载，一句史实带过，克制呈现不渲染细节 |
| 4 | Brodie 边 | 库内规范名 Bernard Brodie（6134），勿用 page 链接全名 Bernard Beryl Brodie 新建（防分裂）；访学仅五个月建 influence |
| 5 | zimelidine 撤市 | 首个上市 SSRI 因罕见格林-巴利综合征撤市、但铺路 Prozac——两面如实，撤市原因勿略去 |
| 6 | 引语红线 | 本篇 page.md 无直接引语，禁编造；诺奖演讲题可用作页面标题 |
| 7 | 公共立场 | 反对饮水加氟、反对顺势疗法按药典管理——page 明载的科学立场，一句带过、不展开瑞典政策论战 |
| 8 | 家庭 | 妻 Ulla-Lisa 1945 年成婚；女儿 Maria（实验室管理者）与 Lena（OSU6162 合作者）具名有叙事入库；三子一女未具名不入库 |
| 9 | 九旬科研 | 90+ 岁仍活跃讲演、与女儿开发 OSU6162（卒中后疲乏的多巴胺稳定剂）——本篇特色帧 |
| 10 | metadata 冲突 | frontmatter field_of_work 有 chemistry/molecular biology 泛化值；yaml fields 按正文三主题；生卒 1923-01-25/2018-06-29（哥德堡）一致 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| dopamine | 多巴胺 | 递质地位的确立者 |
| L-Dopa | 左旋多巴 | 多巴胺前体、帕金森标准疗法 |
| reserpine | 利血平 | 耗竭多巴胺的模型药 |
| basal ganglia | 基底节 | 运动相关脑区 |
| norepinephrine | 去甲肾上腺素 | 多巴胺曾被误认只是其前体 |
| SSRI | 选择性血清素再摄取抑制剂 | zimelidine 为首个上市者 |
| zimelidine | 齐美利定 | 后因罕见副作用撤市 |
| OSU6162 | OSU6162 | 多巴胺稳定剂 |
| Wolf Prize | 沃尔夫奖 | 1979 医学奖 |
| Japan Prize | 日本国际奖 | 1994 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Last Hope** — Alex-Productions（manifest 预分配）
- **匹配理由**：
  - 「最后的希望」精准对应 L-Dopa 的临床意义——帕金森病人从运动锁死中被一段化学分子唤回行动，是神经病学史上「给绝望者的希望」
  - 渐明的编曲结构契合利血平坠落→L-Dopa 回升的双段曲线
- **备选**（未采用）：The Invisible Light（本批 Furchgott 已用）、Awaken（batch-11 Hess 已用）
- **本地路径**：按 music_audio/ 内 Alex-Productions Last Hope 曲目复制至 `medic/presentations/20th_century/Arvid_Carlsson/Last_Hope.wav`，ffmpeg `-shortest` 对齐
