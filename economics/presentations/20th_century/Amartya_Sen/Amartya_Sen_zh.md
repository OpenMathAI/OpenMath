# 经济学家立传提示词（Amartya Sen）

> 本文件是 OpenMathAI OpenEcon 项目 20 世纪诺贝尔经济学奖 **1998 年得主 Amartya Sen（阿马蒂亚·森）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Amartya_Sen/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Amartya Kumar Sen（1933-11-03 生于英属印度孟加拉圣蒂尼克坦，在世）
- **气质关键词**：**福利经济学的良心、能力方法的缔造者、饥荒的权利分析法**
- **诺奖获奖理由**（1998 独得，逐字引用）：
  > "for his contributions to welfare economics"（表彰他对福利经济学的贡献）
- **设计母题**：**可行能力与自由（capability & freedom）**——把发展的度量从收入转向人真实拥有的"可行能力"（functionings→capabilities），视觉隐喻：从收入标尺延展成多维自由空间的能力网格（教育、健康、政治参与各占一维）。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Amartya_Sen/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**路径按 economics 执行**：页面已在 `economics/presentations/pages/20th_century/Amartya_Sen/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Amartya_Sen_zh`、`VIDEO_NAME=Amartya_Sen_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Sen 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | welfare economics | 福利经济学 | 诺奖理由核心词 | 封面、核心页 |
| 1 | social choice theory | 社会选择理论 | 自由悖论、阿罗不可能性定理的条件研究 | 核心页 |
| 2 | development economics | 发展经济学 | 《以自由看待发展》、人类发展报告 | 核心页 |
| 3 | capability approach | 可行能力方法 | "Equality of What?"（1979）提出 | 核心页 |
| 4 | philosophy | 哲学 | 《正义的理念》（2009）、伦理与经济学 | 应用页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致，共 29 条）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Joan Robinson | Robinson → Sen | 剑桥博士论文指导（后凯恩斯主义者） |
| advisor-student | A. K. Dasgupta | Dasgupta → Sen | 印度兼职导师（adjunct supervisor） |
| advisor-student | Lawrence Hamilton | Sen → 学生 | infobox Doctoral students 明载 |
| advisor-student | Ravi Kanbur | Sen → 学生 | infobox 明载 |
| advisor-student | Felicia Knaul | Sen → 学生 | infobox 明载 |
| advisor-student | Prasanta Pattanaik | Sen → 学生 | infobox 明载 |
| advisor-student | Ingrid Robeyns | Sen → 学生 | infobox 明载 |
| influence | Gautama Buddha | 无向 | infobox Influences 明载 |
| influence | Adam Smith | 无向 | infobox Influences；《正义的理念》受其启发 |
| influence | John Rawls | 无向 | infobox Influences；正义理论的对话对象 |
| influence | John Maynard Keynes | 无向 | infobox Influences 明载 |
| influence | B. R. Ambedkar | 无向 | infobox Influences 明载 |
| influence | Kenneth Arrow | 无向 | 社会选择理论奠基人；其《社会选择与个人价值》是 Sen 大学时代最着迷的书 |
| influence | Piero Sraffa | 无向 | infobox Influences 明载 |
| influence | Maurice Dobb | 无向 | Dobb–Sen 策略：其研究与 Sen《技艺的选择》互补 |
| influence | Mary Wollstonecraft | 无向 | infobox Influences 明载 |
| influence | Karl Marx | 无向 | infobox Influences 明载 |
| influence | Sabina Alkire | 无向 | infobox Influenced 明载（Sen 影响对方） |
| influence | Thomas Piketty | 无向 | infobox Influenced 明载（Sen 影响对方） |
| influence | Max Roser | 无向 | Roser 自述因 Sen 的工作创办 Our World in Data |
| colleague | Jean Drèze | 无向 | 《Hunger and Public Action》《An Uncertain Glory》等多部合著 |
| colleague | Martha Nussbaum | 无向 | 合编《The Quality of Life》；能力方法共同发展 |
| spouse | Nabaneeta Dev Sen | 无向 | 1958 结婚、1976 离异；印度作家 |
| spouse | Eva Colorni | 无向 | 1978 结婚、1985 病逝；意大利经济学家 |
| spouse | Emma Rothschild | 无向 | 1991 结婚；哈佛历史学教授 |
| parent-child | Ashutosh Sen | 父 → Sen | 达卡大学化学教授 |
| parent-child | Amita Sen | 母 → Sen | 梵文学者 Kshiti Mohan Sen 之女 |
| parent-child | Antara Dev Sen | Sen → 女 | 记者、出版人 |
| parent-child | Nandana Sen | Sen → 女 | 演员 |

**不入库但提示词可叙述**：外祖父 Kshiti Mohan Sen（隔代不入 parent-child）；次妻子女 Indrani 与 Kabir（有具名但无维基链接，循例不入）；Tagore 为其取名（命名事件，非关系类型）；Manmohan Singh/K. N. Raj/Jagdish Bhagwati（"companion of distinguished economists" 泛述，且涉政人物从谨慎，不建边）；Bernard Williams/Stiglitz/Fitoussi（仅书目合编）。

## 五、配色方案 【人物专属】

- **气质**：温润、思辨、跨越经济学与哲学的人文关怀
- **主色**：`#0F4C5C`（manifest 预分配——深孔雀青，孟加拉水乡与人文主义的沉稳底色）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeWel` 福利经济学 — 深青 `#0F4C5C`
  - `badgeSoc` 社会选择 — 靛蓝 `#372A75`
  - `badgeCap` 可行能力 — 青绿 `#0E7C7B`
  - `badgeFam` 家学与传记 — 琥珀 `#C07A2A`
- **背景母题**：多维能力网格与上升阶梯（从收入标尺到自由空间），呼应"以自由看待发展"。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 福利经济学的良心 / Amartya Sen 1933– + 四色 badge + 右上头像 + 国籍行（India）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒圣蒂尼克坦、Tagore 取名、三段婚姻、
    Presidency College BA、剑桥 Trinity BA/PhD、哈佛 Lamont 大学教授、诺奖 1998）
03  核心贡献概览 — 社会选择 / 自由悖论 / 饥荒的权利分析法 / 可行能力方法
04  圣蒂尼克坦的童年 (1933–1951) — Tagore 取名（意为"永生"）、外祖父与泰戈尔的交谊
05  Presidency 与口癌劫难 (1951–1953) — 经济学一等第一 + 数学辅修；放射治疗幸存
06  剑桥与哲学转向 (1953–1959) — Trinity Prize Fellowship 选哲学；博士论文《技艺的选择》
    （Robinson 指导、Dasgupta 印度兼职指导）
07  22 岁的系主任 (1956–1963) — Jadavpur 大学经济系创始主任；德里经济学院黄金岁月
    （《集体选择与社会福利》1969）
08  社会选择与自由悖论（核心贡献页）— 1970 "The Impossibility of a Paretian Liberal"；
    帕累托与最小自由权的冲突（Lewd/Prude 思想实验）
09  饥荒的权利分析法 — 《贫困与饥荒》1981；孟加拉饥荒=城市繁荣推高粮价；
    "No famine has ever taken place ... in a functioning democracy"（1999，英文原文）
10  可行能力方法 — "Equality of What?"（1979）；functionings→capabilities；
    《以自由看待发展》1999 五类自由
11  正义的理念 (2009) — 对 Rawls 先验制度论的替代；比较的、实现导向的正义观；不偏不倚旁观者
12  三所学院与一位院长 — LSE 1971–77、牛津 Nuffield/All Souls（Drummond 教授 1980）、
    哈佛 1987、Trinity 院长 1998（牛桥首位亚洲院长）、2004 回哈佛
13  荣誉与认可 — 诺奖 1998、Bharat Ratna 1999、National Humanities Medal 2011、
    Skytte 2017、德国书业和平奖 2020、90+ 荣誉博士
14  遗产与结尾 — 人类发展报告与 HDI 的思想源头 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| **政治观点节禁写** | page.md "Political views" 一节（Modi 评价、克什米尔、BJP、Ram Mandir 等）**全部禁写**；学术生涯叙事止于机构与著作 |
| 国籍口径 | frontmatter 有 British Raj/Dominion of India/India/United Kingdom 四值（Wikidata 噪声）；nationalities 按 manifest 只填 India |
| 双导师并存 | Joan Robinson（剑桥正式导师，正文"brilliant but vigorously intolerant"引语可用）与 A. K. Dasgupta（印度兼职导师）并列，勿漏后者 |
| 引语红线 | 仅 page.md 载英文原话者可引：诺奖演讲前 1999 名言 "No famine has ever taken place ... in a functioning democracy"、Trinity 选哲学的解释、"I read a lot and like arguing with people"；其余叙述禁伪引语 |
| "Terminator" 误称 | 页面载的绰号是 "the Conscience of the profession" 与 "the Mother Teresa of Economics"（他本人否认后者的比较）——勿杜撰其他绰号 |
| 关系方向标注 | influence 类型在库中为无向：前 10 条 note 写"影响 Sen"，后 3 条 note 写"Sen 影响对方"，以 note 区分方向 |
| Kenneth Arrow | 库内既有记录 id=2639（图灵奖/经济侧重叠），复用规范名 'Kenneth Arrow'，勿新建 stub |
| 饥荒成因 | 孟加拉饥荒=城市经济繁荣推高粮价、农村工人工资跟不上——按 page.md 口径转述，勿引申 |
| 100 Million Women | "More Than 100 Million Women Are Missing"（1990）是"controversial article"——保留争议标注；Emily Oster 曾持异议后撤回，可一句带过 |
| 生卒 | 1933-11-03 生于 Santiniketan（时属英属印度孟加拉）；在世，卒年留白 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| welfare economics | 福利经济学 | 获奖理由核心词 |
| social choice theory | 社会选择理论 | 阿罗开创、Sen 拓展 |
| liberal paradox | 自由悖论 | 又称 Sen 悖论（Sen's paradox） |
| capability approach | 可行能力方法 | 与 Nussbaum 共同发展 |
| functionings | 功能性活动 | 能力的构成要素 |
| entitlement approach | 权利分析法 | 饥荒成因的分析框架 |
| famine | 饥荒 | 勿泛译"饥荒问题"弱化理论含义 |
| human development theory | 人类发展理论 | HDI 的思想源头 |
| Arrow's impossibility theorem | 阿罗不可能性定理 | Sen 研究其适用条件并拓展 |
| Bharat Ratna | 印度国宝勋章 | 1999 年印度最高平民荣誉 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**PAST**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**："历史感/深沉"贴合 Sen 的思想史气质——从圣蒂尼克坦的泰戈尔传统到亚当·斯密与阿马蒂亚式正义论的对话；深沉的人文底色也呼应其饥荒与贫困研究的悲悯主题。
- **本地路径**：复制 `music_audio/alex-productions/89-geyy8_WXDK0-PAST.wav` 到 `economics/presentations/20th_century/Amartya_Sen/PAST.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
