# 医学家立传提示词（Andrew Schally）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1977 年得主 Andrew Schally（安德鲁·沙利）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Andrew_Schally/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Andrzej Viktor "Andrew" Schally（1926-11-30 生于波兰第二共和国维尔诺（今立陶宛维尔纽斯） ~ 2024-10-17 逝于佛州迈阿密海滩，享年 97 岁）
- **气质关键词**：**十万猪脑的坚持者、脑肽激素的共同破译者、前列腺癌 GnRH 疗法的开创者**
- **诺奖获奖理由**（逐字引自 medic/nobel_medicine_citations.json 1977 条目，Guillemin/Schally 共享同句）：
  > "for their discoveries concerning the peptide hormone production of the brain"（因其关于脑内肽类激素生成的发现）
- **设计母题**：**十万猪脑中的微光（a faint signal in ten thousand pig brains）**——从 10 万猪脑中提取 2.8 mg TRH，再解剖 25 万下丘脑定其结构；用「海量组织堆中一粒发亮的分子」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Andrew_Schally/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/20th_century/Andrew_Schally/`（2000 年像，见 images.txt）。Makefile 复制后设 `MAIN=Andrew_Schally_zh`、`VIDEO_NAME=Andrew_Schally_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Schally 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | endocrinology | 内分泌学 | 下丘脑控制垂体激素的发现，1977 诺奖核心 | 封面、核心页 |
| 1 | neuroendocrinology | 神经内分泌学 | TRH/GnRH 的分离与结构测定 | 核心页 |
| 2 | oncology | 肿瘤学 | GnRH 激动剂治疗晚期前列腺癌（1982 首例试验） | 应用页 |
| 3 | biochemistry | 生物化学 | infobox field_of_work；McGill 博士出身 | 职业页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 正文/infobox 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Roger Guillemin | 无向 | 1957-1962 贝勒共事后决裂，各自独立竞赛（猪脑对羊下丘脑）；「Together with Roger Guillemin he described GnRH」 |
| co-honored | Roger Guillemin | 无向 | 1977 诺贝尔生理学或医学奖共享（脑肽激素生成，官方理由句同一） |
| co-honored | Rosalyn Sussman Yalow | 无向 | 1977 诺贝尔生理学或医学奖共享（Yalow 半边理由为放射免疫测定法研发，跨批次 batch-25，用 manifest 形式名） |
| colleague | George Tolis | 无向 | 1982 与其共同开展 GnRH 治疗晚期前列腺癌的首个临床试验 |
| parent-child | Kazimierz Schally | 对方 → 父 | 波兰准将、总统 Moscicki 参谋长 |
| spouse | Margaret Rachel White | 无向 | 第一任（已离异） |
| spouse | Ana Maria de Medeiros-Comaru | 无向 | 第二任（已故） |
| spouse | Maria de Lourdes Schally | 无向 | 第三任（孀居，2004 年其妻因甲状腺癌去世后继续研究） |

**不入库但提示词可叙述**：Rudolf Klimek（frontmatter doctoral_advisor，正文未提——按新纪律不入库）；母亲 Maria（née Lacka）/曾祖父 Jan（市长，仅具名）；总统 Moscicki 与 1939 年流亡内阁（事件叙述）；Charles Brenton Huggins（前列腺癌旧疗法的研究源头，方法学渊源非关系）。

## 五、配色方案 【人物专属】

- **气质**：波兰流徙的坚韧、迈阿密的暖光、十万猪脑的固执
- **主色**：`#173F5F`（流徙深蓝——从维尔纽斯到迈阿密的漫长迁徙）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeTRH` TRH 十万猪脑 — 深蓝 `#173F5F`
  - `badgeGnRH` GnRH 结构 — 深金 `#B8860B`
  - `badgeProst` 前列腺癌疗法 — 暗红 `#7A1E28`
  - `badgeExile` 波兰流徙 — 灰紫 `#52307C`
- **背景母题**：海量组织堆中一粒发亮的分子结晶。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 十万猪脑的坚持者 / Andrew Schally 1926–2024 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、维尔诺出身、McGill 博士 1957、Tulane/迈阿密 VA、
    诺奖 1977、享年 97、核心领域）
03  核心贡献概览 — 下丘脑控制垂体 / TRH 分离 / GnRH 结构 / 前列腺癌 GnRH 疗法
04  维尔诺与 1939 流亡 (1926–1945) — 准将之子；随总统与内阁流亡罗马尼亚被拘；经意法赴英改名 Andrew
05  苏格兰英国与加拿大 (1945–1957) — 受教育于苏格兰英格兰；1952 迁加拿大；McGill 内分泌学博士 1957
06  贝勒岁月 (1957–1962) — 与 Guillemin 共事五年；决裂；迁新奥尔良 VA 医院
07  十万猪脑中的 2.8 毫克 (1966)（核心贡献页一）— 分离 TRH；诺奖演讲回溯再解剖 25 万下丘脑定结构
08  与 Guillemin 的竞赛 — 两线独立；TRH/GnRH 结构分立鉴定；「Together with Roger Guillemin he described GnRH」
09  1977 三人共享的结构 — Guillemin/Schally 同句（脑肽激素生成）+ Yalow 另句（放射免疫测定）
10  荣誉年表 — Van Meter 1969 / Lasker 1975 / 诺贝尔 1977 / Golden Plate 1978；波兰功勋指挥官勋章、法国军团勋章
11  GnRH 激动剂与前列腺癌 (1972–1982) — 大鼠抑瘤→与 Tolis 首个临床试验；今为晚期前列腺癌首选（约 70% 患者一线）
12  旧疗法的源头 — Huggins 的去势/雌激素研究（方法学渊源叙述）
13  波兰情结 — Kosciuszko 基金会杰出波裔科学家会士；雅盖隆大学荣誉博士；波兰功勋勋章
14  百岁边缘的谢幕 — 晚年节育与癌症治疗研究；2024-10-17 卒于迈阿密海滩 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 1977 三人共享但理由句不同 | Guillemin/Schally 同句 "for their discoveries concerning the peptide hormone production of the brain"；**Yalow 另句** "for the development of radioimmunoassays of peptide hormones"——Yalow 的获奖理由与脑肽激素无关，note 与叙述勿混 |
| 页面标题与 yaml 名 | page.md 标题 **Andrew V. Schally**；本名 **Andrzej Viktor Schally**；yaml/manifest 用 **Andrew Schally**（正文三种形式勿混用） |
| 博士导师不入库 | Rudolf Klimek 仅载于 frontmatter（doctoral_advisor），正文只写「McGill 博士 1957」——按新纪律不入库，陷阱表注明 |
| 三任妻子 | Margaret Rachel White（离异）/Ana Maria de Medeiros-Comaru（已故）/Maria de Lourdes Schally（孀居）——三行 spouse 分立，状态写入 note；「妻因甲状腺癌去世后以继续研究自遣」呼应其科研人格 |
| 决裂叙事 | 与 Guillemin 共事五年后决裂（进展停滞与个人冲突）→独立竞赛→共享诺奖——事实弧线完整呈现，不作贬抑；《The Nobel Duel》仅书讯 |
| GnRH 的「共同描述」 | page.md 明载 "Together with Roger Guillemin he described GnRH"——GnRH 可写共同描述；TRH 结构鉴定则两实验室各自完成，勿互换 |
| 癌症疗法的数据 | GnRH 激动剂 1972–1978 研发、1981 大鼠抑瘤、1982 与 Tolis 首个临床试验；今为晚期前列腺癌首选、约 70% 患者一线——数字勿混 |
| Huggins 的定位 | 旧疗法（去势/雌激素）基于 Huggins 研究——方法学渊源仅叙述，非 Schally 合作对象 |
| 流亡叙事分寸 | 1939 年随总统 Moscicki 与内阁流亡罗马尼亚被拘——史实克制陈述其个人流徙轨迹，不展开二战政治渲染 |
| 数字锚点 | 1966 年 10 万猪脑→2.8 mg TRH；诺奖演讲称再解剖 25 万猪下丘脑→5 mg 定结构——三组数字勿混 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| peptide hormone production of the brain | 脑内肽类激素生成 | 获奖理由核心词，逐字对应 |
| hypothalamus / pituitary gland | 下丘脑/垂体 | 控制链两端 |
| TRH (thyrotropin-releasing hormone) | 促甲状腺激素释放激素 | 10 万猪脑 2.8 mg |
| GnRH (gonadotropin-releasing hormone) | 促性腺激素释放激素 | 与 Guillemin 共同描述 |
| GnRH agonist analogs | GnRH 激动剂类似物 | 前列腺癌疗法 |
| porcine hypothalami | 猪下丘脑 | 其原料（对 Guillemin 的羊） |
| FSH / LH | 促卵泡激素/黄体生成素 | GnRH 控制的两激素 |
| prostate cancer | 前列腺癌 | 1982 临床应用 |
| orchiectomy / estrogens | 去势/雌激素疗法 | 旧疗法（Huggins 源头） |
| Kosciuszko Foundation | 科希丘什科基金会 | 波裔杰出科学家会士 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Last Hope**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：1939 年随内阁流亡的少年、政府经费将断时的 TRH 突破、妻子病逝后以研究自遣——「最后的希望」是其一生三次绝境的共通底色；曲名的深沉也贴合十万猪脑中那一撮 2.8 毫克的执着。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Andrew_Schally/LastHope.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
