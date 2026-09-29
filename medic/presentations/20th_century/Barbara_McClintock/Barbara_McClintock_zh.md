# 医学家立传提示词（Barbara McClintock）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1983 年得主 Barbara McClintock（芭芭拉·麦克林托克）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Barbara_McClintock/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Barbara McClintock（本名 Eleanor McClintock，1902-06-16 生于美国康涅狄格州哈特福德 ~ 1992-09-02 逝于纽约州亨廷顿，享年 90 岁）
- **气质关键词**：**转座因子的发现者、玉米田里的独行侠、迟来三十五年的加冕**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1983 条目，**独得**）：
  > "for her discovery of mobile genetic elements"（因她发现可移动遗传因子）
- **设计母题**：**跳跃的基因（Ac/Ds）**——玉米粒花斑色素图案上 Ac/Ds 转座开合的意象：以玉米粒马赛克色斑作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Barbara_McClintock/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；第 0/1/2/3 步按 medic 路径执行：页面已在 `medic/presentations/pages/20th_century/Barbara_McClintock/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Barbara_McClintock_zh`、`VIDEO_NAME=Barbara_McClintock_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | transposable elements | 可移动遗传因子 | Ac/Ds/Spm 转座，1983 诺奖核心 |
| 1 | cytogenetics | 细胞遗传学 | 玉米染色体可视化技术开创者 |
| 2 | genetics | 遗传学 | 交换-重组细胞学证据、断裂融合桥循环 |
| 3 | maize genetics | 玉米遗传学 | 终生模式生物；南美玉米种族研究 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Rollins A. Emerson | 对方 → 导师 | 康奈尔植物育种系主任、博士导师（1927）；库内 stub id=5758 |
| influence | C. B. Hutchison | 对方 → 影响 | 1921 遗传学启蒙教师；1922 一通电话邀其入研究生课，自述"这通电话决定了我的一生" |
| colleague | Harriet Creighton | 无向 | 1931 PNAS 合著：交换的细胞学与遗传学证据 |
| colleague | George Wells Beadle | 无向 | 小组同侪；1944 邀其赴斯坦福做 Neurospora 核型；库内规范名 id=5756 |
| colleague | Marcus Rhoades | 无向 | 玉米细胞遗传学小组同侪 |
| colleague | Lewis Stadler | 无向 | 密苏里夏季合作者，引 X 射线诱变 |

**不入库但提示词可叙述**：E. G. Anderson（加州理工）；Richard B. Goldschmidt（柏林 1933-34）；Milislav Demerec（冷春港职位）；Navashin（环状染色体首报引用）；Jacob/Monod（lac 操纵子概念呼应）；Lederberg/Wright/Auerbach（Legacy 轶话）；Keller/Comfort/Kass 传记作者；家庭成员。

## 五、配色方案 【人物专属】

- **气质**：玉米地的独行、孤勇的耐心、迟来的加冕
- **主色**：`#6A5A2A`（玉米金褐——秋日田野与花斑籽粒）+ 香槟金诺奖色
- **badge 四分类色**：`badgeAcDs` Ac/Ds 转座 玉米金褐 `#6A5A2A`；`badgeBFB` 断裂融合桥 深蓝 `#16324F`；`badgeCross` 交换-重组 青绿 `#0E7C7B`；`badgeSolo` 独行者 玫瑰 `#9E2B25`
- **背景母题**：玉米粒马赛克色斑图案，呼应「跳跃的基因」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 可移动遗传因子的发现者 / Barbara McClintock 1902–1992 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1902-06-16 ~ 1992-09-02、
    康奈尔 BS 1923/MS 1925/PhD 1927、冷春港实验室、1983 独得诺奖、终身未婚）
03  核心贡献概览 — 玉米染色体可视化 / 交换-重组证据 / 断裂融合桥 / Ac-Ds 控制元件
04  本名 Eleanor 的孩子 (1902–1919) — 幼儿期寄住布鲁克林姨妈家、"独处的能力"、
    母亲曾反对她上大学、Erasmus Hall 高中
05  康奈尔：从植物学到细胞遗传学 (1919–1927) — Hutchison 的电话、卡红染色首创
    玉米 10 条染色体形态学、小组成形（Rhoades/Beadle/Creighton）
06  交换的细胞学证据 (1930–1931)（核心贡献页）— 同源染色体十字形交互首述、
    与 Creighton 证明交换与性状重组对应、姊妹染色单体交换亦证
07  X 射线与环状染色体 (1931–1936) — Stadler 引入诱变、环状染色体、端粒保护假说、
    核仁组织区
08  密苏里与断裂融合桥 (1936–1941) — 断裂-融合-桥循环、大规模突变来源、
    密苏里去职（客观叙述，含 Kass 2024 新证）
09  冷春港与 Neurospora (1941–1944) — Demerec 相邀、NAS 第三位女性院士 1944、
    遗传学会首位女主席、Beadle 相邀斯坦福厘清 Neurospora 细胞学
10  1944–1950：发现控制元件（核心贡献页）— 花斑籽粒、Ds 与 Ac、1948 发现可转座、
    基因调控假说、1950 PNAS 论文
11  1953–1967：停发的岁月 — "puzzlement, even hostility"、1953 停发、
    转向南美玉米种族研究；1967 荣休、1973 引语"必须等待概念变革的时机"
12  重被发现 — Jacob/Monod 操纵子呼应与 1961 对比论文、细菌/酵母/噬菌体转座证实、
    Ac/Ds 克隆为 II 类转座子；荣誉线：Kimber 1967、国家科学奖章 1970（首位女性）、
    MacArthur 首位 1981、Lasker/Wolf/Morgan 1981、Horwitz 1982
13  1983：独得诺奖 — 该奖史上首位独得女性；瑞典科学院以孟德尔相比；
    1989 ForMemRS、1993 富兰克林奖章、1986 全国女性名人堂
14  遗产与结尾 — 转座子与基因组进化、McClintock Prize、2005 邮票、2022 康奈尔
    McClintock Hall；三代传记与"McClintock Myth"之辨（见陷阱表）
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 1983 独得 | 生理学或医学奖史上唯一独得该奖的女性（as of 2025）——"unshared" 必须保留 |
| 博士导师 | frontmatter doctoral_advisor=Emerson，正文载其为系主任"supported these efforts"并雇为助手——导师边用 Emerson（库内 stub 5758）；"Cornell 拒聘女教授"属未证实传说（Kass 2024 有新证），勿写成史实 |
| 首图讹传 | "McClintock 1931 首张玉米遗传图谱"系讹传——page.md 明确：染色体 9 首张连锁图是 Hutchison 1921/1922，McClintock 图谱与之一致——勿写反 |
| 停发论文 | 1953 年起停发控制元件详细研究，与同年 Genetics 统计论文并存——两件事勿混 |
| Hutchison 边 | 用 influence（启蒙+转折电话），导师边只给 Emerson |
| Creighton 论文 | 1931 PNAS 合著（Creighton 一作）；Stern 数周后在果蝇独立证明——Stern 未合作不建边 |
| Beadle 规范名 | 用库内 "George Wells Beadle"(id=5756)，勿用裸名 |
| 史学争议 | Keller 1983"边缘化"叙事 vs Comfort 2001"McClintock Myth"反驳（同行早年即敬重）——两说并立客观呈现，勿单采 |
| 生卒双值 | frontmatter 双值，取正文 1902-06-16 / 1992-09-02 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| mobile genetic elements | 可移动遗传因子 | 获奖理由核心词 |
| transposon | 转座子 | Ac/Ds/Spm |
| Ac / Ds | 激活-解离元件 | Ac 完整（转座酶+）、Ds 缺转座酶需 Ac |
| Spm | 抑制-突变子 | 更复杂的元件家族 |
| controlling elements | 控制元件 | McClintock 早期命名 |
| breakage-fusion-bridge cycle | 断裂-融合-桥循环 | 大规模突变来源 |
| crossing-over | 染色体交叉互换 | 1931 细胞学证据 |
| telomere / centromere | 端粒 / 着丝粒 | 早期功能证明 |
| nucleolus organizer region | 核仁组织区 | 玉米第 6 染色体 |
| McClintock Myth | 麦克林托克神话 | Comfort 提出的史学概念 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Tragedy**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：三十年"puzzlement and hostility"的沉默、独自穿过的沙漠——"Tragedy" 承载被时代辜负的孤独；1983 年加冕正是悲剧叙事的最终翻页，音乐的低回与转折对应她人生的两个半场。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Barbara_McClintock/Tragedy.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
