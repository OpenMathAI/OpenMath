# 医学家立传提示词（Ralph M. Steinman）

> 本文件是 OpenMedic 项目 21 世纪诺贝尔生理学或医学奖 **2011 年得主 Ralph M. Steinman（拉尔夫·斯坦曼）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/21th_century/Ralph_M._Steinman/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Ralph Marvin Steinman（1943-01-14 生于加拿大蒙特利尔 ~ 2011-09-30 逝于美国纽约曼哈顿，享年 68 岁）
- **气质关键词**：**树突细胞的发现者、免疫学的摆渡人、诺奖史上最悲怆的迟到**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 2011 条目；独享**一半**奖金，死后追授）：
  > "for his discovery of the dendritic cell and its role in adaptive immunity"（因他发现树突细胞及其在适应性免疫中的作用）
  - citation 原文含 "(awarded posthumously)" 注记；另一半授予 Beutler 与 Hoffmann（先天免疫激活）——两层结构务必呈现。
- **设计母题**：**树突的探针（dendrites）**——树突细胞以枝状突起探测抗原、联结先天与适应性免疫的意象：以枝状分叉网络作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Ralph_M._Steinman/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/21th_century/Ralph_M._Steinman/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Ralph_M._Steinman_zh`、`VIDEO_NAME=Ralph_M._Steinman_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | immunology | 免疫学 | 树突细胞与免疫应答，2011 诺奖核心 |
| 1 | dendritic cells | 树突细胞 | 1973 发现并命名，"nature's adjuvants" |
| 2 | cell biology | 细胞生物学 | infobox Fields 明载 |
| 3 | adaptive immunity | 适应性免疫 | DC 联结先天与适应性免疫的摆渡作用 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Elizabeth Hay | 对方 → 导师 | 哈佛阶段的学术导师（infobox Academic advisors 明载） |
| advisor-student | James G. Hirsch | 对方 → 导师 | 洛克菲勒大学学术导师（infobox Academic advisors 与 frontmatter 均明载） |
| advisor-student | Zanvil A. Cohn | 对方 → 导师 | 洛克菲勒大学学术导师；1973 在其实验室以博士后研究员身份发现树突细胞 |
| spouse | Claudia Hoeffel | 无向 | 妻，育三子女（infobox Spouse 明载） |
| co-honored | Bruce Beutler | 无向 | 2011 诺贝尔生理学或医学奖（Beutler/Hoffmann 共享另一半） |
| co-honored | Jules A. Hoffmann | 无向 | 2011 诺贝尔生理学或医学奖（Beutler/Hoffmann 共享另一半） |

**不入库但提示词可叙述**：Charles A. Dinarello（2009 Albany Prize 三人共享，一次性奖项关系）；父 Irving Steinman（Sherbrooke 服装店 "Mozart's" 店主，家世叙述）；2016 舍布鲁克 rue Ralph Steinman 街道命名（致敬事件）。

## 五、配色方案 【人物专属】

- **气质**：悲悯、探索、联结两个世界的摆渡感
- **主色**：`#2F4470`（洛克菲勒深蓝——纽约的学术殿堂）+ 香槟金诺奖色
- **badge 四分类色**：`badgeDC` 树突细胞 深蓝 `#2F4470`；`badgeAdaptive` 适应性免疫 青绿 `#0E7C7B`；`badgeInnate` 先天免疫 苔绿 `#175E54`；`badgeCancer` 癌症免疫 玫瑰 `#9E2B25`
- **背景母题**：枝状分叉网络（dendrites 探测抗原），呼应「树突的探针」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 树突细胞的发现者 / Ralph M. Steinman 1943–2011 + 四色 badge + 右上头像 + 国籍行（Canada）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1943-01-14 蒙特利尔 ~ 2011-09-30 曼哈顿、
    McGill BS 1963、哈佛医学院 MD 1968、洛克菲勒大学、诺奖 2011 死后追授）
03  核心贡献概览 — 树突细胞 1973 / 先天-适应性免疫之桥 / "nature's adjuvants" / 免疫治疗远景
04  蒙特利尔与舍布鲁克 (1943–1960) — 阿什肯纳兹犹太家庭、舍布鲁克高中、外祖父母家
05  McGill 与哈佛医学院 (1960–1968) — BS 1963、MD 1968 magna cum laude、麻省总医院实习住院
06  洛克菲勒与三位导师 — Elizabeth Hay（哈佛）、James G. Hirsch 与 Zanvil A. Cohn（洛克菲勒）
07  1973：发现树突细胞（核心贡献页）— Cohn 实验室博士后、贴壁辅助细胞中的新细胞类型、
    枝状突起命名 dendritic cell
08  与巨噬细胞划界（核心贡献页）— 不表达 FcR、高表达 MHC II、不贴壁、不吞噬——双重区分
09  免疫学的摆渡人 — DC 呈递抗原启动 afferent limb；体外可见适应性免疫发生；"nature's adjuvants"
10  成熟与耐受 — 未成熟 DC 摄取抗原；成熟联结先天与适应性；steady state 下的外周耐受
11  荣誉与认可 — Coley 1998、Robert Koch 1999、Gairdner 2003、Lasker 2007、Heineken 2010
12  2011-10-03：迟到三天的诺奖 — 09-30 胰腺癌去世；委员会不知情；章程不追授；
    "made in good faith" 维持决定（须按陷阱表口径精确呈现）
13  家人的告别 — 与家人玩笑"撑到公布那天"的原话（page.md 明载英文可引）；BBC 治愈癌症叙事线
14  遗产与结尾 — DC 疫苗与免疫治疗；2016 舍布鲁克 rue Ralph Steinman；树突细胞学共同体
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 死后授奖细节 | 委员会 2011-10-03 公布时不知其已于 09-30 去世；诺奖章程原则上不追授；委员会裁定"决定出于善意（made in good faith）"维持原议——三步链条须精确，勿简化为"死后追授" |
| 2011 两半结构 | Steinman 独享一半（树突细胞，个人理由）；Beutler+Hoffmann 共享另一半（先天免疫激活）——勿写"三人共享同一理由" |
| 发现年份与地点 | 1973 年在 **Zanvil A. Cohn 实验室**（洛克菲勒大学）以博士后研究员身份发现并命名树突细胞——年份/地点/身份三要素勿错 |
| 与巨噬细胞划界 | DC 不表达 FcR、高表达 MHC II、不贴壁、不吞噬；巨噬细胞相反——这是发现的关键论证，勿写反 |
| DC 不杀微生物 | 与巨噬细胞不同，DC 不吞噬不杀 microbes，而是呈递抗原启动 T 细胞应答——"nature's adjuvants" 的本义 |
| 奖项年份 | Coley 1998、Koch 1999、Gairdner 2003、Debrecen 2006、Lasker 2007、Albany 2009（与 Dinarello、Beutler）、Heineken 2010、Nobel 2011——勿串 |
| 国籍口径 | Nobel 官方（citations json）=Canada；frontmatter [Canada, United States]——yaml 取 Canada(0)+US(1)，封面国籍行 Canada |
| 引语红线 | 与家人"撑到公布"的玩笑话为 page.md 明载英文可引原文+译文；其余叙述勿造引语 |
| 卒因 | 胰腺癌（pancreatic cancer），卒地曼哈顿——BBC 叙事"治愈癌症——包括他自己的"可用作标题意象 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| dendritic cell (DC) | 树突细胞 | 1973 发现并命名；勿缩写混淆"树突"与"轴突" |
| accessory cell | 辅助细胞 | DC 最初藏身之处 |
| adaptive immunity | 适应性免疫 | 获奖理由核心词 |
| nature's adjuvants | 天然的佐剂 | DC 帮助诱导 T 细胞应答的比喻 |
| antigen presentation | 抗原呈递 | DC 的核心功能 |
| cross-presentation | 交叉呈递 | MHC I/CD1 通路 |
| major histocompatibility complex II | 主要组织相容性复合体 II | DC 区别于巨噬细胞的分子标记 |
| peripheral tolerance | 外周耐受 | steady state DC 的功能 |
| cytokine / chemokine | 细胞因子 / 趋化因子 | 成熟 DC 的分泌产物 |
| afferent limb | 传入臂 | DC 启动免疫应答的阶段 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**PAST**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Steinman 的故事是一部回望式的挽歌——1973 年显微镜下的枝状细胞、四十年免疫学长跑、与诺奖错过三天的历史瞬间；"PAST" 的怀旧质感承载这份迟到而永恒的致敬。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/21th_century/Ralph_M._Steinman/PAST.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
