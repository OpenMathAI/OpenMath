# 经济学家立传提示词（James Meade）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1977 年得主 James Meade（詹姆斯·米德）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/James_Meade/page.md`，与其冲突时以 page.md 为准。本篇 page.md 较短（约 60 行），幻灯片按 12 页规划宁缺毋滥，无载内容一律禁写。

## 一、背景信息 【人物专属】

- **目标经济学家**：James Edward Meade（1907-06-23 生于英格兰 Swanage ~ 1995-12-22 逝于英格兰剑桥，享年 88 岁）
- **气质关键词**：**国际收支的调音师、凯恩斯乘数的共同塑造者、心怀左右的两栖经济学家**
- **诺奖获奖理由**（1977，与 Bertil Ohlin 共享，逐字引用 manifest）：
  > "for their pathbreaking contribution to the theory of international trade and international capital movements"（表彰他们对国际贸易与国际资本流动理论的开创性贡献）
- **设计母题**：**内外平衡（internal-external balance）**——国内就业与国际收支两条曲线的协同校准：天平与双向流线构成背景母题，呼应其名言「心向左，脑向右」的双重张力。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/James_Meade/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/James_Meade/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位；infobox 照片为 Meade 站于 Phillips Machine/MONIAC 前的合影，可作插图备选）；Makefile 复制后设 `MAIN=James_Meade_zh`、`VIDEO_NAME=James_Meade_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Meade 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | international trade | 国际贸易 | 诺奖核心：国际贸易理论 | 封面、核心页 |
| 1 | welfare economics | 福利经济学 | infobox Discipline 明载的另一支柱 | 核心页 |
| 2 | macroeconomics | 宏观经济学 | 凯恩斯乘数与国际收支政策 | 核心页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Bertil Ohlin | 无向 | 1977 诺贝尔经济学奖共享（国际贸易与国际资本流动理论） |
| colleague | Richard Kahn | 无向 | 剑桥马戏团（Cambridge Circus）成员，共同发展凯恩斯乘数概念 |

**不入库但提示词可叙述（★ 本篇 relations=2 系 page.md 明载诚实值，防 Review 误判）**：约翰·梅纳德·凯恩斯（其思想语境，page.md 无直接师承/同事记载，禁建边）；Margaret Thatcher（1981 年 364 经济学家联名信批评其经济政策——事件非关系）；工党（1930s 顾问）与社民党（1980s 党员）——政党非人物关系；剑桥马戏团其他成员（page.md 仅点名 Kahn）；Phillips Machine/MONIAC（infobox 照片道具非关系）。

## 五、配色方案 【人物专属】

- **气质**：均衡、温和、英式的克制
- **主色**：`#46356B`（深紫罗兰——内外平衡的对称感，与 Ohlin 篇同主色系呼应共享年份）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeTrade` 国际贸易 — 深紫 `#46356B`
  - `badgeWelfare` 福利经济学 — 青绿 `#0E7C7B`
  - `badgeMultiplier` 凯恩斯乘数 — 靛蓝 `#283593`
  - `badgePolicy` 政策顾问 — 玫瑰 `#C4204F`
- **背景母题**：天平与双向流线（国内平衡与国际收支的协同校准）。

## 六、幻灯片序列 【人物专属，12 页规划（page.md 较短，宁缺毋滥）】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 内外平衡的调音师 / James Meade 1907–1995 + 四色 badge + 右上头像 + 国籍行（United Kingdom）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地 Swanage、教育 Lambrook/Malvern/
    Oxford Oriel（古典学→PPE 1928）、任职 LSE 1947–57→Cambridge 1957–68、诺奖 1977、核心领域）
03  核心贡献概览 — 国际贸易理论 / 福利经济学 / 凯恩斯乘数 / 内外平衡
04  从古典学到 PPE (1907–1930) — Swanage 生、Bath 长大、Oriel 学古典学、1928 转新设 PPE 专业
05  牛津讲席与 Hertford Fellow (1930–1937) — 1930 Hertford College Fellow、1931–37 牛津经济学讲师
06  剑桥马戏团与凯恩斯乘数（核心贡献页）— 与 Richard Kahn 共同发展乘数概念
07  国际联盟与战时经济 section (1930s–1946) — EFO 英国政府专项顾问；战时召回战时内阁经济 section，
    1946–47 任主席；1946 获 CB 勋衔
08  LSE 与剑桥 (1947–1968) — LSE 教授 1947–57、剑桥教授 1957–68；皇家经济学会会长 1964–66
09  政治光谱的独特坐标 — 「心向左，脑向右」；1930s 顾问工党、1980s 加入社民党；1981 年 364 人联名信
10  1977 诺贝尔经济学奖 — 与 Bertil Ohlin 共享（国际贸易与国际资本流动理论）
11  遗产与结尾 — 国际贸易与福利理论的交汇处 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 生卒 | 1907-06-23 Swanage 生 ~ 1995-12-22 剑桥逝（享年 88）；中间名 Edward，全名 James Edward Meade |
| 学历线 | Lambrook 预科 → Malvern College → **Oriel College, Oxford**（先读古典学 Literae humaniores，**1928 年**转入新设 PPE）；1930 当选 **Hertford College** Fellow——Oriel 求学与 Hertford 任职两校勿混 |
| 无博士导师记载 | page.md 全文无 doctoral advisor；frontmatter educated_at 各校亦未给出导师——禁杜撰师承 |
| 凯恩斯禁建边 | Meade 参与剑桥马戏团、发展凯恩斯乘数，但 page.md 对凯恩斯本人无师承/同事的直接表述——乘数归属写「与 Richard Kahn 一起」（Along with Richard Kahn），勿写成凯恩斯亲授 |
| Richard Kahn 辨名 | Richard Kahn, Baron Kahn（剑桥经济学家、卡恩勋爵）库内不存在，与互联网先驱 Robert E. Kahn(260) 无关——新建 stub 用规范名 Richard Kahn |
| 1977 共享理由 | 与 Ohlin 共享，官方理由复数 "for **their** pathbreaking contribution..."；两人工作互不隶属，勿写合作；Ohlin 批次已建反向 co-honored 边，按名匹配幂等 |
| 名言引语 | "my heart to the left, and my brain to the right"（he once said——page.md 载英文原文可用，译作「我的心向着左边，我的头脑向着右边」） |
| 1981 联名信 | 364 位经济学家致函《泰晤士报》质疑撒切尔经济政策、警告将加深萧条——Meade 是签名人之一；客观简述、不作政治评价 |
| 战时机构名 | 战时内阁（War Cabinet）秘书处经济 section（Economic Section），1946–47 由其主持——「section」是小写普通名词，勿当机构专名大写混译 |
| 政党归属漂移 | 1930s 为工党提供咨询、1980s 为社民党（SDP）成员——两党皆非终身归属，勿写成「工党经济学家」 |
| CB 勋衔 | 1946 获 Companion of the Order of the Bath（三等勋爵士），frontmatter award_received 有载；1976 Bath 大学荣誉博士——两个 Bath（勋衔/大学）勿混 |
| 学会任职 | Royal Economic Society 会长 1964–1966；FBA（英国科学院院士）——勿与其他学会混淆 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| Keynesian multiplier | 凯恩斯乘数 | 与 Richard Kahn 共同发展 |
| Cambridge Circus | 剑桥马戏团 | 凯恩斯《通论》的青年评论圈子，勿译作地名 |
| international capital movements | 国际资本流动 | 诺奖理由关键词 |
| welfare economics | 福利经济学 | infobox Discipline 明载 |
| internal-external balance | 内外平衡 | 其国际收支政策分析框架（叙述用语） |
| Phillips Machine / MONIAC | 菲利普斯机/MONIAC | 水力宏观经济模型机，infobox 照片背景 |
| PPE (Philosophy, Politics and Economics) | 哲学、政治学与经济学 | 牛津 1928 新设课程，其转专业去向 |
| Companion of the Order of the Bath | 巴斯三等勋章 | 1946 获授，缩写 CB |
| Royal Economic Society | 皇家经济学会 | 1964–66 会长 |
| neo-Keynesian economics | 新凯恩斯经济学 | infobox School or tradition 明载 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Daylight**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`；与 Ohlin 篇同曲，共享年份同音乐带的设计惯例）
- **匹配理由**：米德一生在天平两端寻找均衡——心与脑、左与右、国内与国际；「Daylight」的清澈对称感贴合其内外平衡的理论气质，也呼应 1977 两位得主共享同一缕瑞典晨光。
- **本地路径**：复制 `music_audio/alex-productions/44-JoyIRE5k2Yo-Daylight.wav` 到 `economics/presentations/20th_century/James_Meade/Daylight.wav`
- **时长核对**：确认 ≥ 12 页 × 7 秒 ≈ 84 秒，ffmpeg `-shortest` 自动对齐。
