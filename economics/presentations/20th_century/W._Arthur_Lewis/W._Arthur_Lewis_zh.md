# 经济学家立传提示词（W. Arthur Lewis）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1979 年得主 Sir W. Arthur Lewis（威廉·阿瑟·刘易斯）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/W._Arthur_Lewis/page.md`，与其冲突时以 page.md 为准。

## 0. 背景信息 【人物专属】

- **目标经济学家**：Sir William Arthur Lewis（1915-01-23 生于圣卢西亚卡斯特里，时属英属向风群岛 ~ 1991-06-15 逝于巴巴多斯布里奇敦，享年 76 岁，安葬于以其命名的圣卢西亚社区学院园区）
- **气质关键词**：**发展经济学之父、二元经济模型的构建者、唯一获经济学诺奖的黑人得主** —— 1979 诺贝尔经济学奖（与 Theodore Schultz 共享）获奖理由：
  > "for their pioneering research into economic development research with particular consideration of the problems of developing countries"（表彰他们对经济发展的开创性研究，尤其着重考虑了发展中国家的问题）
- **设计母题**：**二元经济的两翼（dual sector）**——传统部门（农田、剩余劳动力）与现代资本主义部门（工厂、资本积累）的对置与劳动力转移箭头，构成背景母题：左右分置的几何块 + 从左向右的迁移流线。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/W._Arthur_Lewis/page.md`（同目录 `metadata.json` 仅作结构化参考，冲突以 page.md 为准）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 一、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/W._Arthur_Lewis/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取——page.md 有官方 Nobel Prize 照片 c. 1979 可用，404 则装饰圆占位）；Makefile 复制后设 `MAIN=W._Arthur_Lewis_zh`、`VIDEO_NAME=W._Arthur_Lewis_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库（见下二、三节），无需重复执行；第 5 步起按本文第四至八节执行。

## 二、研究领域梳理 + 入库 【人物专属】

**Lewis 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | development economics | 发展经济学 | infobox Known for 首项；诺奖核心 | 核心页 |
| 1 | dual-sector model | 二元部门模型 | 1954 论文「劳动无限供给下的经济发展」 | 核心页 |
| 2 | development planning | 发展计划 | 加纳第一个五年计划（1959–1963）等实务 | 顾问页 |
| 3 | economic history | 经济史 | 《1870–1913 年的增长与波动》等世界经济史研究 | 著作页 |

## 三、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Arnold Plant | 师→生（本人受教） | LSE 工业经济学博士（1940）导师，正文+infobox 明载 |
| influence | John Hicks | 无向 | LSE 求学时「studied under」，本科/商学士阶段 |
| influence | Lionel Robbins | 无向 | LSE 求学时「studied under」 |
| influence | Friedrich Hayek | 无向 | LSE 求学时「studied under」 |
| spouse | Gladys Jacobs | 无向 | 1947 结婚，格林纳达裔，育二女 |
| co-honored | Theodore Schultz | 无向 | 1979 诺贝尔经济学奖共享（经济发展研究） |

**不入库但提示词可叙述**（防 Review 误判）：
- 女儿 Elizabeth 与 Barbara：仅具名无其他载述，且库内已有同名记录（Elizabeth Lewis id=6055），**不建 parent-child 防误挂**。
- 兄长 Allen Montgomery Lewis：同胞关系不在关系类型白名单，不入库（正文五兄弟、父 George 早逝母 Ida 独抚养可叙述）。
- Eric Williams：少年时代「终生的友谊」、特立尼达和多巴哥首任总理——友谊无对应类型，不入库。
- 各国政府顾问关系（尼日利亚、加纳、特多、牙买加、巴巴多斯）：机构/国家非人物。
- Manchester Literary and Philosophical Society、美国艺术与科学院（1962）、美国哲学会（1966）：会员资格不建关系。

## 四、配色方案 【人物专属】

- **气质**：跨越殖民与独立时代、学术与建国实务兼备的开创者
- **主色**：`#2A3468`（manifest 预分配，深蓝紫——加勒比海的深邃与学术的沉稳）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeDual` 二元模型 — 深蓝紫 `#2A3468`
  - `badgePlan` 发展计划 — 加勒比青 `#1B6B5A`
  - `badgeHist` 经济史 — 琥珀 `#C8922A`
  - `badgePub` 建国实务 — 砖红 `#9E4A2B`
- **背景母题**：左「传统部门」几何块（农田色）与右「现代部门」几何块（工业色）对置，中间劳动力转移流线；可点缀东加勒比 100 元纸币意象（其肖像被印其上）。

## 五、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover 路径按 economics 执行）
01  封面 — 发展经济学之父 / Sir W. Arthur Lewis 1915–1991 + 四色 badge + 右上头像 + 国籍行
    （Saint Lucia / United Kingdom）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地卡斯特里、教育 LSE 1933 入学 /
    博士 1940、任职 LSE→Manchester→西印度大学→Princeton、诺奖 1979、核心领域）
03  核心贡献概览 — 二元部门模型 / 刘易斯转折点 / 发展计划实务 / 世界经济史
04  卡斯特里少年 (1915–1932) — 五兄弟之四，七岁丧父，14 岁完成学业做文书，政府奖学金
05  工程师梦的落空与 LSE (1933–1937) — 「政府与白人公司不会雇用黑人工程师」的抉择；
    商学士一等荣誉；师从 Hicks/Plant/Robbins/Hayek
06  LSE 首位黑人教师 (1938–1948) — 1938 教职、1939 助讲；Plant 门下工业经济学博士（1940）
07  曼彻斯特岁月 (1948–1958) — 33 岁正教授、英国首位黑人讲师（1947 教职口径照录正文）；
    发展经济学概念成形；1954 论文
08  二元部门模型（核心贡献页）— 传统部门剩余劳动 → 资本主义部门扩张 → 资本积累自循环
09  刘易斯转折点 — 剩余劳动被吸干、工资上升的临界；近年在中国发展讨论中的回响
10  发展计划与建国实务 — 加纳首任经济顾问、第一个五年发展计划（1959–1963）；
    西印度大学副校长（1959）；加勒比开发银行首任行长（1970–1973）
11  《西非的政治》(1965) — 对多数决赢者通吃模式的批评；比例代表/联邦制/联合政府主张
    （客观转述学术观点）
12  普林斯顿与晚年 (1963–1991) — James Madison 政治经济学教授；1983 退休；
    1991 逝于巴巴多斯
13  荣誉与认可 — Nobel 1979（唯一获经济学诺奖的黑人得主，正文原口径）· 1963 爵士
    （Knight Bachelor）· 2020 Google Doodle
14  遗产与结尾 — 曼彻斯特 Arthur Lewis Building、SALISES、东加勒比 100 元纸币肖像 + 结尾页
```

## 六、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 「唯一黑人经济学诺奖得主」 | page.md 原文口径 "remains the only black person to have won the Nobel Memorial Prize in Economic Sciences"，照录即可，勿扩展为种族议题评论 |
| 获奖理由措辞 | 官方理由 their/they 复数，与 Schultz 共享同一句；官方措辞不含 dual-sector/turning point 字样 |
| 师承分层 | Arnold Plant 是**博士**导师（1940 工业经济学）；Hicks/Robbins/Hayek 是 LSE 求学「studied under」（商学士阶段），入库用 influence 非 advisor-student，勿混淆 |
| 曼彻斯特入职年份 | 1947 当选讲师（ lecturer），1948 年 33 岁升正教授；「英国首位黑人讲师」系 1947 教职口径；正文另有「taught at Manchester until 1957」与机构表「1948–58」两说，幻灯片择一（正文叙述 1957）并保持全篇一致 |
| 女儿不建边 | Elizabeth/Barbara 仅具名；库内已有 Elizabeth Lewis 同名记录，建边有误挂风险——不入库 |
| Eric Williams | 少年时代的终生友谊，特多首任总理——无关系类型，仅叙述；其名言引语照录原文须配中译 |
| 「引语红线」 | page.md 载其原话仅「工程师梦」（but this seemed pointless...）与 1955 书的 "curiosity and of practical need" 两处；引用须英文原文+中译，不得造中文「原话」 |
| 《西非的政治》 | 对多数决的批评与共识民主主张系其学术观点，客观转述；勿上升为对具体国家的政治评价 |
| 生卒地 | 生于圣卢西亚卡斯特里（英属向风群岛），逝于**巴巴多斯布里奇敦**；安葬于圣卢西亚——三地勿混 |
| metadata 冲突 | metadata.json 与 page.md 冲突时一律以 page.md 为准（如荣誉列表、国籍拆分） |
| 国籍口径 | manifest 作 "Saint Lucia / United Kingdom"（拆两条入库）； citizenship 列 Saint Lucian + British 照录 |

## 七、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| dual-sector model | 二元部门模型 | 又称 Lewis model，勿译「双部门」含糊 |
| Lewisian turning point | 刘易斯转折点 | 剩余劳动吸尽、工资上升的临界 |
| unlimited supplies of labour | 劳动无限供给 | 1954 论文标题关键词 |
| subsistence sector | 维生（传统）部门 | 与 capitalist sector 对置 |
| development planning | 发展计划 | 加纳五年计划等实务 |
| Knight Bachelor | 下级勋位爵士 | 1963 授勋，勿写成「诺贝尔爵位」 |
| Reparations | 赔偿/偿还 | 其 1939 著作使其被归为西印度赔偿主张的最早提出者之一，措辞照录 |
| Measure of Economic Welfare | —（非本篇） | 那是 Tobin 概念，勿混入 |
| growth and fluctuations | 增长与波动 | 1870–1913 世界经济史专著 |
| James Madison Professor | 詹姆斯·麦迪逊讲席教授 | 普林斯顿政治经济学讲席，勿与其他讲席混 |

## 八、背景音乐选择 【人物专属】

- **选定曲目**：**Tragedy**（manifest 预分配，与 Schultz 同曲——共享年份同批预分配，允许同曲）
- **匹配理由**：曲目沉郁的开篇对应殖民地出身者面对的层层壁垒（政府与白人公司不雇黑人工程师）、七岁丧父的少年困顿；中段的推进呼应劳动力从传统部门向现代部门的宏大转移叙事；终章的释然对应 1979 斯德哥尔摩之巅与身后遍及加勒比的制度遗产。
- **本地路径**：复制 `music_audio/alex-productions/80-K5f65-22sY4-Tragedy.wav` 到 `economics/presentations/20th_century/W._Arthur_Lewis/Tragedy.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 九、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `economics/presentations/pages/20th_century/W._Arthur_Lewis/page.md` | ★ 事实基准 |
| `economics/presentations/pages/20th_century/W._Arthur_Lewis/metadata.json` | 结构化参考（冲突以 page.md 为准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` | 任务流程第三章 |
| `MySQL/data/W._Arthur_Lewis.yaml` | 已入库 yaml 存档 |
| `economics/PROMPTS_WORKFLOW.md` | 批量作业手册 |

## 十、执行清单 【模板通用】

1. 建目录 `economics/presentations/20th_century/W._Arthur_Lewis/`（`images/` 子目录）。
2. 肖像：page.md 顶部有 Official Nobel Prize photo (c. 1979)；images.txt 有 URL 直接用（250px 改 500px），否则 Commons `Special:FilePath`（curl 加 `-A "Mozilla/5.0"`，`file` 验证），404 则装饰圆占位。东加勒比 100 元纸币图可作遗产页插图。
3. 复制参照 Makefile，设 `MAIN=W._Arthur_Lewis_zh`、`VIDEO_NAME=W._Arthur_Lewis_zh`。
4. 按 §五 写 15 帧；每帧 `make` 编译，`pdftoppm` 截图目检。
5. 编译达标：0 error、vbox ≤ 10pt、hbox ≤ 50pt。
6. `make images && make video` 出 mp4；核对 BGM 时长。
7. Review-1 修正写回本提示词。

## 十一、版式补遗 【模板通用】

- 表格页安全负间距：顶部 `-0.35cm`、`arraystretch 0.78–0.82`；公式框/引语框前 `-0.35 ~ -0.55cm`。
- 二元模型核心页可用两个并排 tcolorbox（传统部门 vs 现代部门）+ 中间箭头 tikz；箭头线宽 ≤0.8pt 防溢出。
- itemize 挤页：`\itemsep -2.5pt` + `\topsep 0pt` + 顶部 `-0.55cm`（勿超 `-0.65cm`，会遮副标题）。
- 引语框英文原文用 `\itshape`，中译下一行 `\small`；半角引号 `" "`。
- 时间线 `\foreach` 分隔符必须 ASCII 逗号；宏名禁数字。

## 十二、生平时间线节点 【人物专属】

> 供时间线页/身份信息页取材（全部出自 page.md，勿外加）：

| 年份 | 事件 |
|------|------|
| 1915-01-23 | 生于圣卢西亚卡斯特里（英属向风群岛），五兄弟之四 |
| 约 1922 | 七岁丧父（George Lewis），母亲 Ida 独自抚养五子 |
| 约 1929 | 14 岁完成学业，做文书等待 1932 政府奖学金考期 |
| 1932 | 获政府奖学金（18 岁）；与 Eric Williams 结下终生友谊 |
| 1933 | 入 LSE 商学士（会计、商管、商法、少量经济与统计） |
| 1937 | 一等荣誉毕业；获 LSE 奖学金读工业经济学博士（Plant 指导） |
| 1938 | 获 LSE 教职——LSE 首位黑人教师 |
| 1939 | 升助理讲师；《西印度群岛的劳工》出版 |
| 1940 | 博士论文《The Economics of Loyalty Contracts》 |
| 1947 | 与 Gladys Jacobs 结婚；当选曼彻斯特讲师（英国首位黑人讲师） |
| 1948 | 33 岁升曼彻斯特正教授；当选 Manchester Literary and Philosophical Society |
| 1954 | 发表《劳动无限供给下的经济发展》（二元部门模型） |
| 1955 | 出版《经济增长理论》 |
| 1957 | 加纳独立，出任首任经济顾问（第一个五年发展计划 1959–1963） |
| 1959 | 回加勒比，任西印度大学副校长 |
| 1962 | 当选美国艺术与科学院院士 |
| 1963 | 受爵士（Knight Bachelor）；任普林斯顿教授（首位黑人正教授） |
| 1966 | 当选美国哲学会会员；任圭亚那大学校长（至 1973） |
| 1970 | 加勒比开发银行首任行长（至 1973） |
| 1979 | 与 Theodore Schultz 共享诺贝尔经济学奖 |
| 1983 | 自普林斯顿退休（荣休教授） |
| 1991-06-15 | 逝于巴巴多斯布里奇敦，享年 76；葬于以其命名的圣卢西亚社区学院 |
| 2020-12-10 | 获诺奖 41 周年之际 Google Doodle 纪念 |

## 十三、肖像与图像素材指引 【人物专属】

- **优先**：page.md 顶部 Official Nobel Prize photo（c. 1979）+ `images.txt` 的 infobox 肖像（250px 改 500px）。
- **备用**：Commons `Special:FilePath/<文件名>?width=600`（curl 加 `-A "Mozilla/5.0"`，`file` 验证为真图）。
- **正文插图**：东加勒比 100 元纸币（East Caribbean dollar 肖像页）可作遗产页插图，图注照录 page.md。
- **404 兜底**：装饰圆占位（姓名首字母 + 主色），图注注明「肖像暂缺」。
- **禁用**：任何无法核实的合成肖像；与 Allen Montgomery Lewis 混淆的照片。

