# 经济学家立传提示词（Lawrence Klein）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1980 年得主 Lawrence Klein（劳伦斯·克莱因）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Lawrence_Klein/page.md`，与其冲突时以 page.md 为准。

## 0. 背景信息 【人物专属】

- **目标经济学家**：Lawrence Robert Klein（1920-09-14 生于内布拉斯加州奥马哈 ~ 2013-10-20 逝于宾夕法尼亚州格拉德温家中，享年 93 岁）
- **气质关键词**：**宏观经济计量的开拓者、预测模型之父、把凯恩斯经济学装进计算机的人** —— 1980 诺贝尔经济学奖获奖理由：
  > "for the creation of econometric models and the application to the analysis of economic fluctuations and economic policies"（表彰他创建经济计量模型并将其应用于经济波动与经济政策分析）
- **设计母题**：**方程的浪潮（waves of equations）**——联立方程组、时间序列曲线与预测折线在坐标网格上层层展开，代表「把整个国民经济写成一组可估计的方程」；背景母题为错落的坐标网格 + 多条经济曲线的交汇。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Lawrence_Klein/page.md`（同目录 `metadata.json` 仅作结构化参考，冲突以 page.md 为准）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 一、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/Lawrence_Klein/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取——page.md 有 2008 年照片，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Lawrence_Klein_zh`、`VIDEO_NAME=Lawrence_Klein_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库（见下二、三节），无需重复执行；第 5 步起按本文第四至八节执行。

## 二、研究领域梳理 + 入库 【人物专属】

**Klein 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | econometrics | 经济计量学 | infobox Discipline；获奖理由核心词 | 封面、核心页 |
| 1 | macroeconomics | 宏观经济学 | 新凯恩斯学派；Klein 模型传统 | 核心页 |
| 2 | macroeconometric modeling | 宏观经济计量建模 | Klein–Goldberger 模型 / Wharton 模型 / LINK | 模型页 |
| 3 | economic forecasting | 经济预测 | 战后复苏、朝鲜战争后衰退等成功预测 | 预测页 |

## 三、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Paul Samuelson | 师→生（本人受教） | MIT 博士（1944），Samuelson 的首位博士生 |
| influence | Jan Tinbergen | 无向 | 模型思想奠基于 Tinbergen（1969 首届经济学诺奖得主） |
| advisor-student | Arthur Goldberger | 本人→学生 | 博士生（infobox），合作构建 Klein–Goldberger 模型 |
| advisor-student | Bennett Harrison | 本人→学生 | 博士生（infobox 明载） |
| advisor-student | Ignazio Visco | 本人→学生 | 博士生（infobox 明载） |
| advisor-student | E. Roy Weintraub | 本人→学生 | 1960 年代末论文导师，正文明载 |
| collaborator | James Ball | 无向 | 牛津期间合作构建英国经济的 Oxford model |
| controversy | Christopher Sims | 无向 | Sims 1980 批评大型宏观计量模型的假设 |

**不入库但提示词可叙述**（防 Review 误判）：
- Martin Feldstein：对《华尔街日报》评价 Klein「第一个把凯恩斯经济学做成统计模型」——转述评价，非关系。
- Jimmy Carter：1976 协调其经济工作班子（任务团队）， declined 入阁——一次性政治事件非持续关系；其 1940 年代短暂加入美共与麦卡锡时期遭密歇根大学拒绝终身教职按 page.md 客观叙述。
- clients（GE、IBM、Bethlehem Steel）：WEFA 客户，机构非人物。
- Gary Fromm（The Brookings Model 合著者）：书目合著者仅见于出版物列表，正文未叙述合作，不入库。
- MK Evans（Wharton 模型合著者）、M Dutta：同上，书目合著不入库。
- 学会职务（Econometric Society 主席、AEA 主席 1977 等）：不建关系。

## 四、配色方案 【人物专属】

- **气质**：精确、系统、数字里的凯恩斯主义
- **主色**：`#37548D`（manifest 预分配，钢青蓝——计量表格与坐标网格的理性色）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeEcon` 经济计量 — 钢青蓝 `#37548D`
  - `badgeMacro` 宏观模型 — 深靛 `#2A3468`
  - `badgeFore` 经济预测 — 麦金 `#C8922A`
  - `badgeLink` LINK 全球模型 — 青绿 `#1B6B5A`
- **背景母题**：淡淡的坐标网格与多条上扬/回折的经济曲线，四角散布联立方程符号（Y、C、I、G），呼应「国民经济方程化」。

## 五、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover 路径按 economics 执行）
01  封面 — 宏观经济计量之父 / Lawrence Klein 1920–2013 + 四色 badge + 右上头像 + 国籍行
    （United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地奥马哈、教育 LACC/Berkeley 1942/
    MIT 博士 1944、任职 Michigan→Oxford→Pennsylvania、诺奖 1980、核心领域）
03  核心贡献概览 — Klein 模型 / Klein–Goldberger 模型 / Wharton 模型 / Project LINK
04  奥马哈到伯克利 (1920–1942) — 洛杉矶市立学院学微积分；Berkeley 开始计算机建模、
    1942 经济学学士
05  MIT 与 Samuelson 门下 (1942–1944) — Samuelson 的首位博士生；1944 博士
06  考尔斯委员会与战後预测 (1944–1947) — 建美国经济模型；逆主流预期正确预测战后复苏
    而非萧条；朝鲜战争末正确预测温和衰退
07  密歇根与 Klein–Goldberger 模型 — 与 Goldberger 合作；基于 Tinbergen 奠基但改换理论与
    统计技术
08  麦卡锡时代的流离 (1954–1958) — 美共短暂成员曝光、密歇根拒绝终身教职；移牛津建
    Oxford model 与英国储蓄调查
09  宾大与 Wharton 模型 (1958–1969) — 1959 Clark 奖章；1968 Franklin 讲席；1969 创立
    WEFA、开启计量预测产业（客户 GE/IBM/Bethlehem Steel）
10  Brookings-SSRC 与 LINK（核心贡献页）— 1960 年代初领导 Brookings 项目；LINK 联结
    各国模型成首个全球经济模型；1989 移交联合国秘书处、领衔至 2013 去世
11  学界回响 — 诺奖 citation 评价「鲜有实证研究者有如此多后继与如此大影响」；
    Feldstein 评价；Sims 1980 的批评（客观并列）
12  政策与公共服务 — 1976 协调卡特经济工作班子、婉拒入阁；计量学会/AEA 主席（1977）
13  晚年与高频模型 — current quarter models；退休后至去世仍建高频模型
    （美中俄印巴西墨韩港）
14  遗产与结尾 — 中央银行仍在使用的建模传统；Economists for Peace and Security
    创始受托人 + 结尾页
```

## 六、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由两版本 | page.md 开头引作 "for the creation of econometric models **and their** application..."，manifest/nobel json 作 "the application..."；**以 manifest citation 为准**（官方 nobelprize.org 口径），陷阱表备案 |
| 「Samuelson 首位博士生」 | page.md 明载 "Paul Samuelson's first doctoral student"，这是亮点事实，勿遗漏也勿改写为「之一」 |
| Tinbergen 关系 | 是思想奠基（based on foundations laid by）+ infobox Influences，**非师承**；且 Klein 改换了经济理论与统计技术——「差异」要写 |
| 美共与密歇根 | 1940 年代短暂入党、1954 曝光后遭密歇根大学拒绝终身教职（麦卡锡时代背景）——按 page.md 客观叙述，一字一句照录口径，不渲染 |
| LINK 移交年份 | 1989 从宾大移交联合国秘书处；Klein 领衔至 2013 去世；LINK 项目 2020 年才在联合国终止——三个年份勿混 |
| 两次成功预测 | 战后复苏（逆主流衰退预期）+ 朝鲜战争末温和衰退；这是其模型声誉的起点，勿与其他预测混淆 |
| Sims 批评 | Sims 1980「Macroeconomics and Reality」批评大型宏观计量模型假设，属方法论争论——客观并列，勿写成 Klein 理论被推翻 |
| Goldberger 双重身份 | 既是 infobox 博士生又是 Klein–Goldberger 模型合作者——yaml 合并为一条 advisor-student，note 注明合作构建模型 |
| 机构两读 | Cowles Commission 当时在芝加哥大学（后迁耶鲁成 Cowles Foundation）；Tobin 篇的 Cowles 是 Yale 时期——两篇各照本人页面口径 |
| metadata 冲突 | metadata.json 与 page.md 冲突时以 page.md 为准 |
| 引语红线 | page.md 载 Feldstein 转述与诺奖 citation 评价均为英文原文，引用须原文+中译；Klein 本人无直接引语，不得造中文「原话」 |

## 七、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| econometric models | 经济计量模型 | 获奖理由核心词，勿简写「计量模型」失语境 |
| Klein–Goldberger model | 克莱因–戈德伯格模型 | 1955 专著《1929–52 美国经济的一个计量模型》 |
| Wharton Econometric Forecasting Model | 沃顿经济计量预测模型 | 宾大时期代表作 |
| Project LINK | LINK 项目 | 全球模型联结计划，1989 移交联合国 |
| Cowles Commission | 考尔斯委员会 | 时在芝加哥；勿与 Yale 的 Cowles Foundation 混为两处机构名 |
| McCarthyism | 麦卡锡主义 | 1954 密歇根事件的时代背景 |
| current quarter models | 当季模型 | 晚年高频/短周期建模传统 |
| John Bates Clark Medal | 约翰·贝茨·克拉克奖章 | 1959 获得者，经济学两大最高荣誉之一（page.md 口径） |
| Neo-Keynesian economics | 新凯恩斯经济学 | 其学派归属（infobox School or tradition） |
| Oxford model | 牛津模型 | 与 James Ball 合作构建的英国经济模型 |

## 八、背景音乐选择 【人物专属】

- **选定曲目**：**With Me**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：「与我同行」贴合 Klein 的联结者气质——从 Samuelson 门下到 Goldberger/James Ball 的合作建模，再到把几十个国家的模型联结成全球经济的 LINK 项目，一生都在「与模型同行、与同行者同行」；曲目的行进感也呼应经济波动的节律。
- **本地路径**：复制 `music_audio/alex-productions/83-DXAblXgCK-k-With-Me.wav` 到 `economics/presentations/20th_century/Lawrence_Klein/WithMe.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。

## 九、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `economics/presentations/pages/20th_century/Lawrence_Klein/page.md` | ★ 事实基准 |
| `economics/presentations/pages/20th_century/Lawrence_Klein/metadata.json` | 结构化参考（冲突以 page.md 为准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` | 任务流程第三章 |
| `MySQL/data/Lawrence_Klein.yaml` | 已入库 yaml 存档 |
| `economics/PROMPTS_WORKFLOW.md` | 批量作业手册 |

## 十、执行清单 【模板通用】

1. 建目录 `economics/presentations/20th_century/Lawrence_Klein/`（`images/` 子目录）。
2. 肖像：images.txt 有 URL 直接用（250px 改 500px）；无 URL 用 Commons `Special:FilePath`（curl 加 `-A "Mozilla/5.0"`，`file` 验证），404 则装饰圆占位。
3. 复制参照 Makefile，设 `MAIN=Lawrence_Klein_zh`、`VIDEO_NAME=Lawrence_Klein_zh`。
4. 按 §五 写 15 帧；每帧 `make` 编译，`pdftoppm` 截图目检。
5. 编译达标：0 error、vbox ≤ 10pt、hbox ≤ 50pt。
6. `make images && make video` 出 mp4；核对 BGM 时长。
7. Review-1 修正写回本提示词。

## 十一、版式补遗 【模板通用】

- 表格页安全负间距：顶部 `-0.35cm`、`arraystretch 0.78–0.82`；公式框/引语框前 `-0.35 ~ -0.55cm`。
- 模型谱系页（Klein 模型 → K–G → Brookings → Wharton → LINK）用 tikz 时间线，节点 ≤5 个防溢出；`\foreach` 分隔符 ASCII 逗号。
- itemize 挤页：`\itemsep -2.5pt` + `\topsep 0pt` + 顶部 `-0.55cm`（勿超 `-0.65cm`）。
- 术语（Klein–Goldberger、Brookings-SSRC）含 en-dash/连字符，注意 CJK 断行；必要时 `\mbox{}`。
- itemize 深色背景反白字体下避免 ★ 等缺字符号；引语框英文原文用 `\itshape` + 中译 `\small`。

## 十二、生平时间线节点 【人物专属】

> 供时间线页/身份信息页取材（全部出自 page.md，勿外加）：

| 年份 | 事件 |
|------|------|
| 1920-09-14 | 生于内布拉斯加州奥马哈，父 Leo Byron Klein、母 Blanche（née Monheit） |
| 1940 前后 | 洛杉矶市立学院（AA，学微积分） |
| 1942 | 伯克利加州大学经济学学士（BA）；在校开始计算机建模 |
| 1944 | MIT 经济学博士——Paul Samuelson 的首位博士生 |
| 1944–47 | 考尔斯委员会（时在芝加哥大学）；建美国经济模型 |
| 战后 | 逆主流预期正确预测经济复苏而非萧条 |
| 1950s 初 | 朝鲜战争末正确预测温和衰退 |
| 1940s | 曾短暂加入美国共产党（多年后带来麻烦） |
| 1954 | 美共成员曝光，密歇根大学拒绝终身教职（麦卡锡时代） |
| 1954–58 | 移英国牛津；与 James Ball 建 Oxford model；协助创建英国储蓄调查 |
| 1958 | 回美国，入职宾夕法尼亚大学经济系 |
| 1959 | 获约翰·贝茨·克拉克奖章 |
| 1960s 初 | 领导 Brookings-SSRC 项目（美国经济详细计量模型） |
| 1960s 后期 | 构建 Wharton Econometric Forecasting Model |
| 1968 | 任宾大 Benjamin Franklin 经济与金融讲席教授 |
| 1969 | 创立 WEFA（今 Global Insight），开启美国计量预测产业 |
| 1976 | 协调卡特经济工作班子；婉拒入阁 |
| 1977 | 出任美国经济学会（AEA）主席 |
| 1980 | 获诺贝尔经济学奖（计量模型的创建及其对波动与政策分析的应用） |
| 1989 | LINK 系统自宾大移交联合国秘书处；领衔至 2013 去世 |
| 2013-10-20 | 逝于宾夕法尼亚州格拉德温家中，享年 93 |

## 十三、肖像与图像素材指引 【人物专属】

- **优先**：`images.txt` 列出的 infobox 肖像（page.md 有 2008 年照片，250px 改 500px 下载）。
- **备用**：Commons `Special:FilePath/<文件名>?width=600`（curl 加 `-A "Mozilla/5.0"`，`file` 验证为真图）。
- **404 兜底**：装饰圆占位（姓名首字母 + 主色），图注注明「肖像暂缺」。
- **禁用**：宏观经济学导航框内任何人物头像；与 Felix Klein / Viola Klein 等同姓者混淆的照片。

