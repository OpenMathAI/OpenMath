# 经济学家立传提示词（Lloyd Shapley）

> 本文件是 OpenEcon 项目 21 世纪诺贝尔经济学奖 **2012 年得主 Lloyd Shapley（劳埃德·沙普利）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/21th_century/Lloyd_Shapley/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Lloyd Stowell Shapley（1923-06-02 生于马萨诸塞州剑桥 ~ 2016-03-12 逝于亚利桑那州图森，享年 92 岁）
- **气质关键词**：**博弈论的巨匠、夏普利值的缔造者、稳定匹配的数学家**
- **诺奖获奖理由**（2012，与 Alvin E. Roth 共享；逐字引自 manifest）：
  > "for the theory of stable allocations and the practice of market design"（表彰他们关于稳定配置的理论与市场设计的实践）
- **设计母题**：**价值的分摊（fair division）**——多人合作博弈中把总收益按边际贡献分给每个人：圆环上若干节点以不同粗细的连线连向中心，「夏普利值」即各连线粗细的加权和，构成公平分割的视觉隐喻。
- **本地 Wikipedia 路径**：`economics/presentations/pages/21th_century/Lloyd_Shapley/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/21th_century/Lloyd_Shapley/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Lloyd_Shapley_zh`、`VIDEO_NAME=Lloyd_Shapley_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Shapley 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | game theory | 博弈论 | 自我定义「冲突与合作的数学研究」，2012 诺奖理论翼 | 核心页 |
| 1 | Shapley value | 夏普利值 | 1953 论文与博士工作引入，合作博弈解概念 | 核心页 |
| 2 | mathematical economics | 数理经济学 | non-atomic games、market games、utility theory | 理论页 |
| 3 | matching theory | 匹配理论 | Gale–Shapley 算法与稳定婚姻问题（1962） | 核心页 |
| 4 | stochastic games | 随机博弈 | 1953 年开创的博弈类型 | 理论页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致；共 11 条）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Albert W. Tucker | Shapley → 学生 | 普林斯顿博士导师（1953），论文为可加与非可加集函数 |
| co-honored | Alvin Eliot Roth | 无向 | 2012 诺贝尔经济学奖共享（稳定配置理论与市场设计实践） |
| parent-child | Harlow Shapley | Shapley 父 → 子 | 父，天文学家 |
| parent-child | Martha Betz Shapley | Shapley 母 → 子 | 母，天文学家 |
| spouse | Marian Louise Shapley | 无向 | 1955 年起结婚 |
| collaborator | David Gale | 无向 | Gale–Shapley 算法 1962 合著（稳定婚姻问题） |
| collaborator | John Forbes Nash | 无向 | 1950 桌游 So Long Sucker 共同发明（与 Hausner/Shubik） |
| collaborator | Martin Shubik | 无向 | Shapley–Shubik 权力指数、On Market Games、Assignment Game 合著 |
| collaborator | Robert Aumann | 无向 | non-atomic games 与长期竞争合著；称其为史上最伟大博弈论家 |
| collaborator | Dov Monderer | 无向 | potential games 1996 合著 |
| collaborator | Michael Maschler | 无向 | kernel 与 nucleolus 合著（与 Peleg） |

**不入库但提示词可叙述**：其子（劝他领奖并陪同赴斯德哥尔摩，页面未具名不入库）；Mel Hausner、B. Peleg、R. N. Snow、Samuel Karlin、Xingwei Hu、Manel Baucels 等合作者具名但在行 note 内提及或仅叙述（收敛边数防噪声）；von Neumann/Morgenstern 是思想源头非直接关系；Knuth 著作为后续研究非关系。

## 五、配色方案 【人物专属】

- **气质**：数学家的冷静、RAND 时代的纵深、厚积薄发
- **主色**：`#7A1E28`（配对绛红，与 Roth 篇同色系以呼应共享年份）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeValue` 夏普利值 — 绛红 `#7A1E28`
  - `badgeStoch` 随机博弈 — 靛蓝 `#1E3A5F`
  - `badgeMatch` 稳定匹配 — 琥珀 `#C07A2A`
  - `badgeRand` RAND 岁月 — 灰紫 `#52307C`
- **背景母题**：圆环节点与加权连线（边际贡献的公平分摊），呼应「价值分摊」母题。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 博弈论的巨匠 / Lloyd Shapley 1923–2016 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、剑桥马萨诸塞出身、天文学家双亲、
    Harvard AB 1948 / Princeton PhD 1953、导师 Tucker、RAND 1954–81、UCLA 1981–2016、核心领域）
03  核心贡献概览 — 夏普利值 / 随机博弈 / 核与均衡概念 / 稳定匹配
04  名门与从军 (1923–1948) — 天文学家 Harlow Shapley 之子、Phillips Exeter、哈佛辍学从军、
    成都服役破译苏联气象密码获铜星勋章
05  RAND 与普林斯顿 (1949–1953) — RAND 一年 → Princeton 博士、Procter Fellow、夏普利值与核的诞生
06  夏普利值（核心贡献页一）— 1953 A Value for n-person Games、边际贡献分摊、效用视角（Roth 的再诠释）
07  RAND 二十年 (1954–1981) — 随机博弈、Shapley–Shubik 权力指数、kernel 与 nucleolus、Bondareva–Shapley
08  稳定婚姻问题（核心贡献页二）— 1962 与 Gale 的 College Admissions 论文、延迟接受算法
09  命名成果清单 — Aumann–Shapley / Harsanyi–Shapley / Snow–Shapley / Shapley–Folkman / potential games
10  合作者群像 — Nash/Shubik/Aumann/Gale/Monderer/Maschler 六线并进
11  荣誉与学会 — von Neumann Theory Prize 1981、NAS 1978、Distinguished Fellow AEA 2007、
    AMS Fellow 2012
12  2012 斯德哥尔摩 — 与儿子们的获奖之争、与 Roth 共享、以数学家身份领经济学奖
13  身后评价 — Aumann「史上最伟大博弈论家」、AEA「博弈论与经济理论的巨人」（引语原文）
14  遗产与结尾 — 从核到匹配市场：算法进入真实世界 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 身份口径 | 页面首句「American mathematician and Nobel Memorial Prize-winning economist」——mathematician 在前；The Economist 与 AEA 评价均提到他自认数学家；primary_occupation 取 mathematician 是忠于页面的裁定，勿被 Review 改回 economist |
| 获奖理由归属 | 2012 与 Roth 共享同一句；Shapley 是「理论翼」（稳定配置理论），Roth 是「实践翼」（市场设计），页文结构与 Nobel citation 呼应，勿互换 |
| 领奖插曲 | 与儿子们争论是否领奖、认为父亲 Harlow 更值得获奖、被劝服赴斯德哥尔摩——客观记录，勿作心理推测与评价 |
| 军旅细节 | 二战在美国陆军航空队驻中国成都服役、1944 获铜星勋章的理由是「破译苏联气象密码」——照录，勿写成「情报官」等衍生说法 |
| 对手方规范名 | Nash 用库内 John Forbes Nash(967)（非 John F. Nash Jr. / John Nash）；Gale 用库内 David Gale(969)；Tucker 用库内 Albert W. Tucker(98)；Muth 无涉；Roth 用 Alvin Eliot Roth(8110) |
| So Long Sucker | 1950 与 Mel Hausner、John Nash、Martin Shubik 四人共同发明——Hausner 红链不入库，note 内提及即可 |
| 学生边 | 页面无 Doctoral students 行（infobox 亦无）——Shapley 无师生边是诚实值，勿杜撰门生 |
| 合著收敛 | Aumann/Shubik/Gale/Monderer/Maschler 五条 collaborator 是正文与 selected publications 明载的核心合作；Snow/Karlin/Hu/Baucells/Peleg 等仅叙述防噪声 |
| 生卒日期 | 1923-06-02 / 2016-03-12（图森，髋部骨折后），享年 92；逝因措辞「after suffering from a broken hip」照录勿渲染 |
| 引语红线 | game theory 定义句、Aumann 评价句、von Neumann Theory Prize 授奖词均有英文原文，引语框引原文+译文；「greatest game theorist of all time」是 Aumann 所说，勿写成自述 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| Shapley value | 夏普利值 | 合作博弈解概念，1953 |
| core (game theory) | 核 | 与核空相关的 Bondareva–Shapley 定理 |
| stable marriage problem | 稳定婚姻问题 | 1962 论文语境 |
| Gale–Shapley algorithm | Gale–Shapley 算法 | 延迟接受算法 |
| stochastic games | 随机博弈 | 1953 开创 |
| Shapley–Shubik power index | Shapley–Shubik 权力指数 | 投票权力测量 |
| non-atomic games | 非原子博弈 | 与 Aumann 合著 |
| nucleolus | 核仁 | 与 Maschler/Peleg 合著 |
| potential game | 势博弈 | 与 Monderer 1996 |
| Shapley–Folkman lemma | Shapley–Folkman 引理 | 凸性近似结果 |
| Kriegspiel | 暗棋（克里格spiel） | Shapley 精于此道的棋类 |
| RAND Corporation | 兰德公司 | 1949-50 与 1954-81 两段 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Through the Darkness**（manifest 预分配，与 Roth 篇同曲以呼应共享年份；音乐库 `music_audio/`）
- **匹配理由**：Shapley 的黄金年代在 RAND 的保密帷幕之后——冷战深处的数学突围；「穿越黑暗」的史诗推进感对应其从战火中破译密码到博弈论奠基的纵深人生，也与 Roth 篇形成理论-实践两翼的音乐呼应。
- **本地路径**：复制 `music_audio/inspiring-electronic/14-Trn1cSsY2t8-Audiomachine - Through the Darkness.wav` 到 `economics/presentations/21th_century/Lloyd_Shapley/Through the Darkness.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
