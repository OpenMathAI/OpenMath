# 经济学家立传提示词（Robert Lucas）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1995 年得主 Robert Lucas（罗伯特·卢卡斯）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Robert_Lucas_Jr./page.md`，与其冲突时以 page.md 为准（同目录 metadata.json 仅作结构化参考）。

## 一、背景信息 【人物专属】

- **目标经济学家**：Robert Emerson Lucas Jr.（1937-09-15 生于华盛顿州雅基马 ~ 2023-05-15 逝于芝加哥，享年 85 岁）
- **气质关键词**：**理性预期革命的主角、卢卡斯批判的提出者、新古典宏观经济学的中心人物**
- **诺奖获奖理由**（1995 独得，manifest citation 逐字）：
  > "for having developed and applied the hypothesis of rational expectations, and thereby having transformed macroeconomic analysis and deepened our understanding of economic policy"（表彰他提出并应用理性预期假说，从而改变了宏观经济分析并深化了人们对经济政策的理解）
- **设计母题**：**预期与反馈（expectation & feedback loop）**——理性预期的本质是「政策改变时，人的预期随之改变，旧的相关性随之失效」：以环形反馈箭头、被重绘的曲线与面具化的"预期之眼"构成背景母题，呼应卢卡斯批判。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Robert_Lucas_Jr./page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

- **关键时间线（事实基准，取自 page.md）**：
  - 1937-09-15 生于华盛顿州雅基马，长子女；父 Robert Emerson Lucas、母 Jane Templeton，经营冰淇淋店，大萧条中倒闭迁西雅图
  - 1959 芝加哥大学历史学 BA；研究生第一年曾在 UC Berkeley，因经济原因返芝加哥
  - 1964 芝加哥经济学 PhD（论文 Substitution Between Labor and Capital in U.S. Manufacturing: 1929–1958，H. Gregg Lewis 与 Dale Jorgenson 联合指导）
  - 1959 与大学同学 Rita Cohen 结婚，育二子 Stephen（1960）与 Joseph（1966）
  - 毕业后执教卡内基梅隆 GSIA（今 Tepper 商学院）至 1975，其间 John Muth 1961 发表理性预期论文于同校前身 Carnegie Tech
  - 1972 "Expectations and the Neutrality of Money"（JET）——理性预期进入动态宏观模型
  - 1976 "Econometric Policy Evaluation: A Critique"——卢卡斯批判
  - 1975 返芝加哥大学任教
  - 1980 当选美国艺术与科学院；1981 获 Guggenheim Fellowship、当选 NAS
  - 1988 "On the Mechanics of Economic Development"——内生增长理论开山之一（与 Paul Romer 并称）
  - 1980s 与 Rita Cohen 离婚；离婚条款载明：若 1995-10-31 前获奖，前妻分得一半奖金——1995 获奖果然应验
  - 再婚 Nancy Stokey（合著增长/公共财政/货币理论论文；1989 三人合著 Recursive Methods in Economic Dynamics）
  - 1995 诺贝尔经济学奖（独得）；1997 当选美国哲学学会
  - 2020 全球被引第 10 的经济学家；2023-05-15 逝于芝加哥，享年 85

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/Robert_Lucas_Jr./`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 取——infobox 明载 "Lucas in 1996" 照片；404 则装饰圆占位）；Makefile 复制后设 `MAIN=Robert_Lucas_Jr._zh`、`VIDEO_NAME=Robert_Lucas_Jr._zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

### 流程要点细化

- **第 0 步**：事实基准已在本文第一、七节固化（page.md 已核对），直接使用，勿再凭记忆改写；
- **第 1 步**：目录 `economics/presentations/20th_century/Robert_Lucas_Jr./` 已存在（本提示词所在），只需建 `images/`；
- **第 2 步**：Makefile 从同世纪已完成篇目复制，仅改 `MAIN`/`VIDEO_NAME` 两行；
- **第 3 步**：infobox 有 "Lucas in 1996" 真实照片，优先下载；
- **第 4/4.5 步**：已入库（见第三节 rank 表与第四节关系表），立传 agent 只读不写库；
- **第 5-9 步**：配色、幻灯片序列、编写、布局检查、史实审查按本文第五、六、七、十一、十二节执行，每写一页就编译一次。

## 三、研究领域梳理 + 入库 【人物专属】

**Lucas 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | macroeconomics | 宏观经济学 | infobox Discipline；新古典宏观中心人物 | 封面、核心页 |
| 1 | rational expectations | 理性预期 | 诺奖核心假说（1972 引入动态宏观模型） | 核心页 |
| 2 | economic growth | 经济增长 | 1988 内生增长开山；Uzawa–Lucas 模型 | 增长页 |
| 3 | monetary economics | 货币经济学 | 货币中性、货币意外与总供给理论 | 货币页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | H. Gregg Lewis | Lewis → 导师 | 芝加哥博士导师（1964 论文联合指导） |
| advisor-student | Dale W. Jorgenson | Jorgenson → 导师 | 芝加哥博士导师（1964 论文联合指导） |
| spouse | Rita Cohen | 无向 | 1959 结婚、1980s 离异；离婚条款涉诺奖奖金分成 |
| spouse | Nancy Stokey | 无向 | 再婚；合著增长/公共财政/货币论文与 Recursive Methods |
| advisor-student | Marcel Boyer | Lucas → 学生 | 博士生（infobox 明载） |
| advisor-student | Costas Azariadis | Lucas → 学生 | 博士生（infobox 明载） |
| advisor-student | Jean-Pierre Danthine | Lucas → 学生 | 博士生（infobox 明载） |
| advisor-student | Boyan Jovanovic | Lucas → 学生 | 博士生（infobox 明载） |
| advisor-student | Paul Romer | Lucas → 学生 | 博士生（infobox 明载）；内生增长理论并肩者 |
| advisor-student | Esteban Rossi-Hansberg | Lucas → 学生 | 博士生（infobox 明载） |
| advisor-student | Benjamin Moll | Lucas → 学生 | 博士生（infobox 明载） |
| influence | John Muth | 无向 | 1961 理性预期论文；Lucas 1972 将其思想引入动态宏观模型 |
| colleague | Hirofumi Uzawa | 无向 | Uzawa–Lucas 人力资本积累模型共同提出 |
| colleague | Edward Prescott | 无向 | 三人合著 Recursive Methods in Economic Dynamics（1989） |

**不入库但提示词可叙述**：Milton Friedman / Edmund Phelps（page.md 说 Lucas 为其"货币长期中性"观点提供理论基础，是观点呼应非师承/合作）；二子 Stephen 与 Joseph（仅名字，不具姓氏，不入库）；N. Gregory Mankiw（"20 世纪最后四分之一最有影响宏观经济学家"评语是他人转述）；芝加哥学派名单页（sidebar 大名单是模板导航，非个人关系）。

## 五、配色方案 【人物专属】

- **气质**：锐利、颠覆、淡水（freshwater）学派的冷峻理性
- **主色**：`#16324F`（manifest 预分配，普鲁士蓝——芝加哥学派的冷静与锋芒）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeRE` 理性预期 — 普鲁士蓝 `#16324F`
  - `badgeCrit` 卢卡斯批判 — 玫瑰 `#C4204F`
  - `badgeGrowth` 内生增长 — 青绿 `#0E7C7B`
  - `badgeMon` 货币中性 — 琥珀 `#C07A2A`
- **背景母题**：环形反馈箭头与被重绘的曲线（旧菲利普斯曲线碎裂重排的抽象），呼应「政策一变、预期即变」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 理性预期革命的主角 / Robert Lucas 1937–2023 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、雅基马出生、芝加哥 BA 1959/PhD 1964、
    任职卡内基梅隆/芝加哥、诺奖 1995、核心领域）
03  核心贡献概览 — 理性预期 / 卢卡斯批判 / 内生增长 / 货币中性
04  雅基马与大萧条家庭 (1937–1955) — 冰淇淋店倒闭迁西雅图；父亲造船厂与制冷公司焊接工
05  芝加哥历史学士 (1955–1959) — BA in history；Berkeley 一年后因经济原因返芝加哥
06  转向经济学与博士论文 (1960–1964) — "准马克思主义"动机：经济学才是历史真正的驱动力
07  卡内基梅隆岁月 (1964–1975) — GSIA 教职；与 Muth 的理性预期思想同校相逢
08  理性预期：1972 货币中性（核心贡献页一）— Expectations and the Neutrality of Money；菲利普斯曲线无政策取舍
09  卢卡斯批判：1976（核心贡献页二）— 参数随政策而变；宏观模型需微观基础
10  内生增长与 Uzawa–Lucas 模型 (1988) — On the Mechanics of Economic Development；与 Romer 并称
11  卢卡斯悖论与卢卡斯楔 — 资本为何不流向穷国；合意政策下的 GDP 差距
12  1995 诺贝尔经济学奖 — 独得；理性预期假说改变宏观分析
13  婚姻与那纸离婚条款 — Rita Cohen 1959 结婚、二子；1980s 离异；1995-10-31 条款应验分半奖；再婚 Nancy Stokey
14  遗产与结尾 — Mankiw 评语、2020 被引第 10；2023-05-15 逝于芝加哥 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 独得年份 | 1995 **独得**（非共享）；page.md 无共享者，勿与 1994/1996 批混淆 |
| 姓名规范 | 正文 Robert Emerson Lucas Jr.；入库 name_en 用 manifest 形式 **Robert Lucas**（dir 为 Robert_Lucas_Jr.）；行文标题用 Robert Lucas，避免与 George Lucas/Keith Lucas 等库内他人混淆 |
| 获奖理由句 | 引用 manifest 完整句 "for having developed and applied the hypothesis..."——三个动作（developed / applied / transformed）缺一不可，勿截半句 |
| Muth 的位置 | 理性预期思想**源头是 John Muth（1961，Carnegie Tech 同校）**，Lucas 是"发展并应用于宏观"——行文勿写成 Lucas 首创该假说 |
| Friedman/Phelps | page.md 说 Lucas 为两人"货币长期中性"观点提供理论基础——是理论支撑关系，**不是师承或合作**，不入库 |
| 离婚条款 | 1995-10-31 前获奖前妻分一半奖金——page.md 明载轶事，可作第 13 页花絮；表述客观，勿渲染 |
| 内生增长归属 | "Lucas and Paul Romer heralded the birth of endogenous growth theory"——两人并列（1988 Lucas 论文 + 1986/1990 Romer），勿写 Romer 是其"合作者"（Romer 是其学生兼并肩者，正文无合著） |
| Uzawa–Lucas | 该模型与 Hirofumi Uzawa 共同命名提出——page.md 明载 "with"，可写合作 |
| 芝加哥学派 sidebar | page.md 含芝加哥学派导航模板大名单（Alchian/Becker/Fama 等）——**那是 Wikipedia 模板导航，不是 Lucas 的个人关系**，一律不建边 |
| 2003 发言 | "central problem of depression-prevention has been solved"（2003，大衰退前约五年）——引用时注明年份与语境，勿作立场评价 |
| 死亡日期 | 2023-05-15 逝于芝加哥，享年 85；NYT/华盛顿邮报讣告为参考来源，按 page.md 口径即可 |
| metadata 噪声 | metadata.json educated_at 有重复 University of Chicago 两值；以 page.md 正文（BA 1959 / PhD 1964）为准 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| rational expectations | 理性预期 | 思想源头 Muth；Lucas 是宏观应用者 |
| Lucas critique | 卢卡斯批判 | 政策改变会改变行为参数 |
| new classical macroeconomics | 新古典宏观经济学 | Lucas 所属学派 |
| microfoundations | 微观基础 | 1976 批判的方法论后果 |
| Phillips curve | 菲利普斯曲线 | 实证相关 ≠ 政策取舍 |
| neutrality of money | 货币中性 | Friedman/Phelps 观点的理论基础 |
| Uzawa–Lucas model | 宇泽–卢卡斯模型 | 人力资本积累的两部门增长模型 |
| Lucas paradox | 卢卡斯悖论 | 资本不从富国流向穷国 |
| Lucas wedge | 卢卡斯楔 | 合意政策下的 GDP 差距度量 |
| Recursive Methods in Economic Dynamics | 《经济动态的递归方法》 | 与 Stokey、Prescott 三人合著（1989） |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Eternals**（manifest 预分配，音乐库 `music_audio/alex-productions/76-V5T_kW2PH_s-Eternals.wav`）
- **匹配理由**：「永恒」贴合理性预期假说的范式地位——它不是单一结论，而是重写了整个宏观经济分析底层假设的永恒遗产；曲名的深远感也呼应其从 1972 论文到 2023 离世仍居被引前列的持久影响。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `economics/presentations/20th_century/Robert_Lucas_Jr./Eternals.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 十、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `economics/presentations/pages/20th_century/Robert_Lucas_Jr./page.md` | ★ 事实基准（唯一事实来源） |
| `economics/presentations/pages/20th_century/Robert_Lucas_Jr./metadata.json` | QID/生卒/国籍结构化参考（educated_at 噪声以 page.md 为准） |
| `economics/presentations/pages/20th_century/Robert_Lucas_Jr./images.txt` | 肖像候选 URL（infobox "Lucas in 1996"） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照（身份信息页/配色宏/页序列） |
| `economics/presentations/cover/` | OpenEcon 共享封面（`\input` 统一首页） |
| `MySQL/data/Robert_Lucas_Jr..yaml` | 本人物入库 yaml（fields/relations 与本文第三、四节一致） |
| `economics/PROMPTS_WORKFLOW.md` | 批量作业手册（入库命令、note 引号规则、对手方规范名） |

## 十一、执行清单与验收标准 【模板通用】

1. 复制同世纪已完成篇目 Makefile，改 `MAIN=Robert_Lucas_Jr._zh`、`VIDEO_NAME=Robert_Lucas_Jr._zh`。
2. 下载肖像（images.txt 有 URL 直接用；无则 Commons `Special:FilePath/<File>?width=600`，404 则装饰圆占位）。
3. 配色宏按第五节：`mainclr=#16324F`，badgeA-D 四色照抄；宏名统一 `mainclr/accentclr/badgeA..D`，注释写语义。
4. 幻灯片序列按第六节 15 页规划逐页实现；身份信息页（02）必做。
5. 编译循环：`make distclean && make`（latexmk 多遍），0 error；溢出指标 vbox ≤ 10pt / hbox ≤ 50pt。
6. `pdftoppm` 逐页目检，修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。
7. 全篇事实回查：每条陈述可溯源到 page.md；引语仅限 page.md 载英文原文者（2003 发言与 Mankiw 评语均带年份归属）。
8. 品牌口径：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。
9. 验收：pdfinfo 页数 = 规划页数；BGM wav（Eternals）已复制到本目录。

## 十二、版式补遗（Beamer 实现要点） 【模板通用】

- 时间线 `\foreach` 分隔符必须 ASCII 逗号（中文逗号会吞条目）。
- 表格页安全负间距：顶部 -0.35cm、`arraystretch` 0.78-0.82；公式框前 -0.35 ~ -0.55cm。
- 反馈环母题用 tikz 弧形箭头（bend left）三层嵌套，线宽 0.6pt、低透明度，避免喧宾夺主。
- `remember picture` 需两遍编译；取日志单遍 xelatex 后必须重新 `make pdf`。
- `\newcommand` 宏名禁数字；文本模式希腊字母必须进数学模式。
