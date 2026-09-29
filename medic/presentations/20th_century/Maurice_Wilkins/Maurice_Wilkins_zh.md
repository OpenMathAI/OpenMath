# 医学家立传提示词（Maurice Wilkins）

> 本文件是 OpenMedic 项目「20 世纪诺贝尔生理学或医学奖得主人物专属立传提示词」。
> 目标人物：Maurice Wilkins（1962 年诺贝尔生理学或医学奖得主，英国）。
> 用途：指导后续 Beamer 立传（15 页）与配套视频制作；事实基准为本地 Wikipedia 页面
> `medic/presentations/pages/20th_century/Maurice_Wilkins/page.md`（下称 page.md）。
> 社会关系与研究领域已按本文件第三、四节入库 greatminds 库（yaml 与本文件完全一致）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Maurice Hugh Frederick Wilkins（莫里斯·休·弗雷德里克·威尔金斯，1916-12-15 新西兰庞加罗阿 ~ 2004-10-05 伦敦布莱克希思，享年 87 岁）
- **气质关键词**：**国王学院 DNA 衍射研究的开创者、「双螺旋第三人」、被历史简写低估的奠基者** —— 1962 年诺贝尔生理学或医学奖获奖理由（逐字引自 medic/nobel_medicine_citations.json，与 Watson、Crick 三人共享）：
  > "for their discoveries concerning the molecular structure of nucleic acids and its significance for information transfer in living material"
  > （因其关于核酸分子结构及其在生命物质信息传递中的意义的发现）
- **设计母题**：**「第三条链」**。双螺旋之外，那条不被讲述的线——视觉隐喻：两根高亮螺旋链旁以低透明度绘出的第三条链与衍射斑点星阵。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Maurice_Wilkins/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 **medic 路径**执行：页面用 `medic/presentations/pages/20th_century/Maurice_Wilkins/`，成目录 `medic/presentations/20th_century/Maurice_Wilkins/`，Makefile 复制后设 `MAIN=Maurice_Wilkins_zh`、`VIDEO_NAME=Maurice_Wilkins_zh`，BGM 见第九节。
> 第 4 步（研究领域）与第 4.5 步（社会关系）**已完成入库**，见第三、四节。
> 数据库已置 `has_social_data=1`；`has_biography` 待 Beamer 立传完成后置 1。

## 三、研究领域梳理 + 入库（已完成）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biophysics | 生物物理学 | 国王学院生物物理单元副主任/主任（1970-72），1962 诺奖核心 | 总览页 |
| 1 | X-ray crystallography | X 射线衍射 | 1948 起主导 DNA 纤维衍射，1950 首批高质量照片 | 衍射页 |
| 2 | molecular biology | 分子生物学 | DNA 双螺旋的实验确证与普适性验证 | 确证页 |

## 四、社会关系梳理 + 入库（已完成，与 MySQL/data/Maurice_Wilkins.yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | John Randall | 师 | 伯明翰博士导师，后携其创建国王学院生物物理单元 |
| co-honored | James Watson | — | 1962 诺贝尔生理学或医学奖三人共享（DNA 结构） |
| co-honored | Francis Crick | — | 1962 诺贝尔生理学或医学奖三人共享（DNA 结构） |
| colleague | Rosalind Franklin | — | 国王学院同实验室，角色分工混乱致紧张，1953 年未询其同意出示 Photo 51 |
| advisor-student | Raymond Gosling | 生 | 其研究生，1950 年合作拍得首批 DNA 衍射图，后转入 Franklin 门下 |
| spouse | Ruth Wilkins | — | 第一任妻子，伯克利结识，后离异 |
| spouse | Patricia Ann Chidgey | — | 1959 年成婚 |

> 说明：Photo 51 出示一幕的三方（Randall 令 Gosling 交图→Wilkins 出示→Watson）均按 page.md 如实入库/叙述，伦理争论在正文两面呈现（「subject of significant ethical and historiographical debate」）。Alex Stokes（螺旋衍射数学）、Rudolf Signer（高纯度 DNA 来源）、Lord Cherwell（揭幕）、Mark Oliphant（荐 Randall）均为背景人物不入库；妹妹 Eithne（译者诗人）无兄弟关系类型不入库；四名子女（Sarah/George/Emily/William）仅具名无叙事不入库。

## 五、配色方案 【人物专属】

- **气质**：沉思、隐忍、被历史简写者的安静坚持
- **主色**：衍射墨蓝 `#2E4A5E`（X 射线底片上的暗场）
- **诺奖色**：香槟金（奖章/年份徽章专用）
- **四分类色（badgeA-D）**：
  - `badgeA` 生物物理学 — 单元灰青 `#41607E`
  - `badgeB` X 射线衍射 — 斑点银白 `#A9B4BE`
  - `badgeC` 分子生物学 — 螺旋绿 `#1F7A6D`
  - `badgeD` 和平与社会责任 — 反战深红 `#7A3A3A`
- **背景母题**：衍射斑点星阵（中心对称分布的亮点）与暗场底片边框，低透明度铺底

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input medic/presentations/cover/）
01  封面 — 双螺旋第三人 / Maurice Wilkins 1916–2004 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、教育、任职、家庭、荣誉、核心领域）
03  核心贡献概览 — DNA 衍射开创 / Photo 51 链条 / 双螺旋实验确证 / 社会责任运动
04  新西兰-伯明翰 (1916–1938) — 医生之子、6 岁移英、剑桥圣约翰学院物理学
05  博士与曼哈顿计划 (1938–1946) — Randall 门下磷光研究、战时雷达屏、伯克利同位素分离
06  国王学院生物物理单元 (1946–1951) — Randall 副手、 Signer 高纯度 DNA、1950 首批衍射照片、那不勒斯报告震动 Watson
07  双线并行的国王学院 (1951–1953) — Franklin 到任与角色混乱（Randall 的信）、与 Stokes 的螺旋证据、B 型样本
08  Photo 51 事件（核心页）— Randall 令 Gosling 交图→Wilkins 出示→Watson；伦理与史学争论两面并陈
09  1953：三篇 Nature（核心页）— Watson-Crick 主论文 + Wilkins/Stokes/Wilson 验证文 + Franklin/Gosling 数据文，连续页码同期发表
10  1962 诺贝尔奖（核心页）— citation 原文、三人共享、Franklin 1958 逝世无缘提名、Wilkins 著述中始终承认其工作
11  确证与普适性 (1953–1972) — 多物种/活体验证、1955 副主任、1970-72 主任
12  战时与和平 — 曼哈顿计划的幻灭、广岛后「very disgusted」、剑桥反战小组与短期党员经历、2010 解密档案
13  社会责任科学运动 (1969–1991) — 创立 British Society for Social Responsibility in Science 并任首任主席
14  遗产 — 2000 年 Franklin-Wilkins Building（他坚持 Franklin 名列前）、奥克兰 Maurice Wilkins Centre、自传 The Third Man of the Double Helix
15  结尾
```

## 七、特殊陷阱表（★ 执行 Beamer 前必读）

| # | 陷阱 | 裁定 |
|---|------|------|
| 1 | 获奖理由表述 | 逐字用 citation 原文（their 三人共享）；勿写成「因拍出 Photo 51」——Photo 51 是 Franklin/Gosling 拍摄、Wilkins 出示 |
| 2 | Photo 51 归属 | 摄于 1952 年 5 月、拍摄者 Franklin（Gosling 参与）、1953 年初由 Wilkins 出示给 Watson「without notifying or receiving authorization」——每个环节归属勿错 |
| 3 | 国籍口径 | citation json country "New Zealand United Kingdom" 为 rowspan 噪声；manifest/总表口径 United Kingdom，正文叙述新西兰出生 |
| 4 | Randall 双面性 | Randall 的任命信埋下 Franklin/Wilkins 角色混乱（Wilkins 多年后才知信件内容），Wilkins 自传批评 Randall「modeled himself on Napoleon」——可引英文原文；对 Randall 的批评属自传观点，注明出处 |
| 5 | 与 Franklin 关系 | 同事+角色紧张+出示照片未经同意——colleague 边 note 已涵盖；勿写成合作破裂或单纯友好；Wilkins 晚年著述承认 Franklin 贡献（正文有载） |
| 6 | 「第三人」自定 | 自传书名 The Third Man of the Double Helix 是其自题——可用作本篇标题意象，注明出自其自传 |
| 7 | 党籍段 | 战前加入英共至 1939 年 9 月苏军入侵波兰后退党、军情五处监视至 1953 年——page 明载，一句史实带过，不展开 |
| 8 | 死亡日期 | 1916-12-15 ~ 2004-10-05，前后一致无冲突 |
| 9 | 子女 | 四名子女仅具名（Sarah/George/Emily/William），Ruth 离异后所生子未具名——均不入库不展开 |
| 10 | metadata 冲突 | frontmatter doctoral_advisor=John Turton Randall 与 infobox John Randall 同一人（两种写法），yaml 用 John Randall（正文链接形式）；occupation 的 physician 为噪声 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| X-ray diffraction | X 射线衍射 | 其方法主线 |
| Photo 51 | 51 号照片 | B 型 DNA 衍射图，拍摄归属勿错 |
| B-form / A-form | B 型 / A 型 DNA | 含水 B 型 vs 低水 A 型，Wilkins 主攻 B 型 |
| Biophysics Unit | 生物物理单元 | MRC 资助、Randall 创建 |
| phosphorescence | 磷光 | 其博士课题 |
| isotope separation | 同位素分离 | 曼哈顿计划工作 |
| ram sperm / sepia sperm | 公羊精液 / 乌贼精液 | 其 DNA/生物样本来源 |
| Patterson synthesis | 帕特森合成 | Franklin 的分析路线（对照） |
| The Third Man of the Double Helix | 《双螺旋第三人》 | 2003 自传 |
| Franklin-Wilkins Building | 富兰克林-威尔金斯楼 | 2000 年命名，Franklin 名列前 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Expedition** — Alex-Productions（manifest 预分配）
- **匹配理由**：
  - 「远征」匹配其人生轨迹——从新西兰牧场小镇到伯克利曼哈顿计划再到伦敦国王学院的科学远征，以及二十年不被讲述的坚持
  - 行进感与秩序感契合衍射斑点的几何之美
- **备选**（未采用）：SEA（本批 Watson 已用）、Lonesome（孤独感贴切但已用于相邻批次更孤绝人物）
- **本地路径**：按 music_audio/ 内 Alex-Productions Expedition 曲目复制至 `medic/presentations/20th_century/Maurice_Wilkins/Expedition.wav`，ffmpeg `-shortest` 对齐
