# 医学家立传提示词（Charles Richet）

> 本文件是 OpenMedic 项目「20 世纪诺贝尔生理学或医学奖得主人物专属立传提示词」。
> 目标人物：Charles Richet（1913 年诺贝尔生理学或医学奖得主，法国）。
> 用途：指导后续 Beamer 立传（15 页）与配套视频制作；事实基准为本地 Wikipedia 页面
> `medic/presentations/pages/20th_century/Charles_Richet/page.md`（下称 page.md）。
> 社会关系与研究领域已按本文件第三、四节入库 greatminds 库（yaml 与本文件完全一致）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Charles Richet（夏尔·里歇，全名 Charles Robert Richet，1850-08-25 巴黎 ~ 1935-12-04 巴黎，享年 85 岁）
- **气质关键词**：**过敏反应（anaphylaxis）的命名者、免疫学的先驱、一位陷入灵学研究半个世纪的理性主义者** —— 1913 年诺贝尔生理学或医学奖获奖理由（逐字引自 medic/nobel_medicine_citations.json）：
  > "[for] his work on anaphylaxis"
  > （因其关于过敏反应的工作）
- **设计母题**：**「第二次剂量」**。过敏反应的反直觉内核：首次注射引人耐受，第二次却致命——视觉隐喻：两支注射器/两次剂量标记（① 预期保护 → ② 致命逆转）构成的对比构图。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Charles_Richet/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 **medic 路径**执行：页面用 `medic/presentations/pages/20th_century/Charles_Richet/`，成目录 `medic/presentations/20th_century/Charles_Richet/`，Makefile 复制后设 `MAIN=Charles_Richet_zh`、`VIDEO_NAME=Charles_Richet_zh`，BGM 见第九节。
> 第 4 步（研究领域）与第 4.5 步（社会关系）**已完成入库**，见第三、四节。
> 数据库已置 `has_social_data=1`；`has_biography` 待 Beamer 立传完成后置 1。

## 三、研究领域梳理 + 入库（已完成）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | physiology | 生理学 | 法兰西公学院生理学教授（1887–），1913 诺奖核心 | 总览页 |
| 1 | immunology | 免疫学 | 发现并命名 anaphylaxis，过敏研究的起点 | 过敏反应页 |
| 2 | allergology | 变态反应学 | 解释花粉症、哮喘、过敏性猝死等 | 应用页 |
| 3 | parapsychology | 超心理学 | 创刊 Annales des sciences psychiques、命名 ectoplasm、灵学机构要职 | 灵学页 |

## 四、社会关系梳理 + 入库（已完成，与 MySQL/data/Charles_Richet.yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| parent-child | Alfred Richet | 父 | — |
| collaborator | Paul Portier | — | 1901-1902 海上考察合作发现过敏反应 |
| collaborator | Maurice Hanriot | — | 合作发现麻醉药氯醛糖 |
| influence | Jean-Martin Charcot | — | 萨尔佩特里尔实习期间观摩其癔症研究 |
| colleague | Lucien Le Foyer | — | 1902 年起共同领导法国和平主义社团代表团 |
| colleague | Albert von Schrenck-Notzing | — | 灵学研究同侪，保持往来 |
| colleague | Frederic William Henry Myers | — | 灵学研究同侪，保持往来 |
| colleague | Gabriel Delanne | — | 灵学研究同侪，保持往来 |

> 说明：儿子 Charles 与孙子 Gabriel Richet（教授席传承、欧洲肾病学前驱）page.md 明载但儿子无独立可辨专名——「his son Charles」与其父同名，建边必产生同名自环风险，故不入库，仅在幻灯片中以文字带过；博士导师 Charles Philippe Robin 仅 page.md frontmatter 有载、正文无载——按本批「metadata-only 一律不入库」纪律不建边（若后续 Beamer 需提及师承，以文字注记）；受调查的灵媒（Eusapia Palladino、Eva Carrière、Linda Gazzera、Leonora Piper 等）是研究对象非合作关系，不入库；摩纳哥亲王 Albert I 是科考东道主，不入库。

## 五、配色方案 【人物专属】

- **气质**：双重人格的张力——实验室的严谨白与降神会的幽暗紫
- **主色**：灵学紫灰 `#4A3562`（理性与幽冥之间的中间色）
- **诺奖色**：香槟金（奖章/年份徽章专用）
- **四分类色（badgeA-D）**：
  - `badgeA` 生理学 — 实验室青 `#2E7A6E`
  - `badgeB` 免疫学 — 血清红 `#A83A4A`
  - `badgeC` 变态反应学 — 花粉橙 `#C8862E`
  - `badgeD` 超心理学 — 通灵紫 `#6B4E9E`
- **背景母题**：左半浅色网格（实验室记录纸）与右半稀疏幽光圆斑（降神会氛围）的拼接底纹，低透明度

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input medic/presentations/cover/）
01  封面 — 过敏反应的命名者 / Charles Richet 1850–1935 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像（1922 照）+ 右信息网格（生卒巴黎、索邦教育、法兰西公学院、家庭、荣誉、核心领域）
03  核心贡献概览 — 过敏反应 / 免疫学 / 生理学 / 超心理学
04  早年巴黎 (1850–1878) — Alfred Richet 之子、Lycée Bonaparte、1878 胃液论文
05  萨尔佩特里尔 — 实习期观摩 Charcot 的「癔症」病人研究
06  法兰西公学院教授 (1887–) — 神经化学、消化、体温调节、呼吸的广泛探索；1898 医学科学院、1914 科学院
07  海上考察 (1901) — Princesse Alice II 号、摩纳哥亲王 Albert I、刺胞动物毒素 hypnotoxin
08  「第二次剂量」：发现过敏反应（核心页）— 首注耐受、再注致命；aphylaxis→anaphylaxis 命名过程
09  1913 诺贝尔奖（核心页）— citation 原文 "[for] his work on anaphylaxis"、1913-12-11 诺奖演讲 Anaphylaxis
10  免疫学的分水岭 — von Pirquet 1906「allergy」一词、花粉症/哮喘/过敏性猝死的解释框架
11  灵学的半个世纪 — 1891 创刊、1894 命名 ectoplasm、1905 SPR 主席、1919/1930 灵学研究所；被灵媒与骗子愚弄的记录（Gazzera 1911 被揭穿、Argamasilla 1924 被 Houdini 揭穿）
12  第六感假说 — 拒斥灵魂说、主张生理学解释的「第六感」；Traité de Métapsychique 1922
13  和平主义与晚年立场 — 1902 年起领导和平社团代表团；优生学主张与种族观点的如实记载
14  遗产 — 教授席三代传承（子 Charles、孙 Gabriel）；anaphylaxis 进入现代医学词典
15  结尾
```

## 七、特殊陷阱表（★ 执行 Beamer 前必读）

| # | 陷阱 | 裁定 |
|---|------|------|
| 1 | 获奖理由表述 | 逐字用 citation 原文 "[for] his work on anaphylaxis"——只有一件事：anaphylaxis；勿加「免疫学贡献」等扩充 |
| 2 | 生卒日期双值 | frontmatter 有 1850-08-26/1850-08-25/1850-01-01 与 1935-12-04/1935-12-03/1935-01-01 多值；正文与 infobox 均为 25 August 1850 – 4 December 1935，以正文为准 |
| 3 | 命名演变 | 1902 年先造 aphylaxis，后因音感改 anaphylaxis；词源 ana-（against）+ phylaxis（protection）——「防保护」的本义须写清，勿译成「无保护反应」之类别名 |
| 4 | 与 Portier 的分工 | 二人 1902-02-15 在巴黎生物学会联合报告；1901 年海上考察由亲王 Albert I 资助——勿把发现写成 Richet 独立完成 |
| 5 | allergy 一词 | 由 Clemens von Pirquet 1906 年创造——Richet 是过敏现象发现者而非「allergy」命名者，勿混淆 |
| 6 | 灵学内容 | page.md 大量明载且是后半生主叙事：如实、克制记载（创刊/命名 ectoplasm/被灵媒愚弄的记录/Brandon 批评引语有原文可引）；立场用「他主张生理学解释、拒斥灵魂假说」的原文口径，勿美化亦勿嘲讽 |
| 7 | 种族与优生观点 | page.md 明载其优生学主张、1920-1926 任法国优生学会主席及种族主义言论（经史家 Jahoda 转述）。立传以「史实记载」口径一句带过（第七节之外不展开），不转述其种族言论内容，不作任何认同性表述 |
| 8 | 和平主义 | 1902 年起参与法国和平主义运动、与 Le Foyer 共组常设代表团——page.md 明载可写，属史实叙述 |
| 9 | 儿子同名 | 「his son Charles」与本人同名——幻灯片只写「其子 Charles 与其孙 Gabriel 延续了里歇家的医学教授席」，禁为儿子单独建卡或建关系边 |
| 10 | 博士导师 Robin | Charles Philippe Robin 仅 page.md frontmatter（metadata）有载、正文无载——metadata-only 关系不入库；师承如需提及仅作文字注记，勿建关系边或单独卡片 |
| 11 | 引语红线 | anaphylaxis 节、第六感节、Brandon 批评各有英文原文可引；其余叙事（Charcot 观摩等）为叙述性内容，禁编造引语 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| anaphylaxis | 过敏反应（严重速发型超敏反应） | 本义「反保护」，勿译「无反应性」 |
| prophylaxis | 预防（保护） | 与 anaphylaxis 对照的词源 |
| hypnotoxin | 催眠毒素 | 刺胞动物毒素的早期命名 |
| cnidarian | 刺胞动物 | 僧帽水母/海葵来源 |
| ectoplasm | 外质（灵学语境：通灵外质） | Richet 1894 命名，勿作细胞生物学 ectoplasm |
| chloralose | 氯醛糖 | 与 Hanriot 共同发现的麻醉镇痛药 |
| metapsychics | 超心理学（灵学） | Richet 用语，与 parapsychology 同域 |
| medium | 灵媒 | 被调查对象，非合作者 |
| Societé de Biologie | 巴黎生物学会 | 1902-02-15 联合报告场合 |
| Collège de France | 法兰西公学院 | 勿译「法兰西学院」泛称 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Lonesome** — Alex-Productions（manifest 预分配）
- **匹配理由**：
  - 「孤独/游离」精准匹配其双重人生的孤旅——在免疫学上站上诺奖殿堂，却把后半生押在同行视为异端的灵学上，两头都不合群
  - 幽暗缓慢的音色也贴合降神会场景与「被骗子环绕的孤独研究者」意象
- **备选**（未采用）：Tragedy（本批次 Kocher 已用）、Falling Apart（过于破碎，与其晚年多产著述不符）
- **本地路径**：按 music_audio/ 内 Alex-Productions Lonesome 曲目复制至 `medic/presentations/20th_century/Charles_Richet/Lonesome.wav`，ffmpeg `-shortest` 对齐
