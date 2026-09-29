# 医学家立传提示词（Satoshi Ōmura）

> 本文件是 OpenMedic 项目 21 世纪诺贝尔生理学或医学奖 **2015 年得主 Satoshi Ōmura（大村智）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/21th_century/Satoshi_Ōmura/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Satoshi Ōmura（大村 智，1935-07-12 生于日本山梨县韮崎市，**在世**），北里大学名誉教授、卫斯理安大学 Max Tishler 化学讲席教授，发现逾 480 个新化合物
- **气质关键词**：**土壤放线菌的收藏家、480 个化合物的发现者、从夜校教师到诺奖得主**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 2015 条目，Ōmura/Campbell 共享一半；屠呦呦独得另一半）：
  > "for their discoveries concerning a novel therapy against infections caused by roundworm parasites"（因其关于线虫寄生虫感染的新疗法的发现）
- **设计母题**：**一勺土壤中的百万微生物（soil → Streptomyces → 480 compounds）**——大村用独特筛选策略从土源放线菌中淘出药物宝库；用「土粒中放射状生长的菌丝与结晶分子」作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/21th_century/Satoshi_Ōmura/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/21th_century/Satoshi_Ōmura/`（世纪目录一律 `21th_century`，肖像见 images.txt；与 Campbell 合照可作插图）。Makefile 复制后设 `MAIN=Satoshi_Ōmura_zh`、`VIDEO_NAME=Satoshi_Ōmura_zh`（tex 文件名如遇 Ō 字符问题可用 ASCII 变体 Satoshi_Omura_zh，**yaml/入库名保持 "Satoshi Ōmura" 不变**）。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。**在世者注意**：封面写 b.1935。

## 三、研究领域梳理 + 入库 【人物专属】

**Ōmura 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biochemistry | 生物化学 | infobox Fields 明载 | 身份页 |
| 1 | natural products chemistry | 天然产物化学 | 480+ 新化合物、25 种药物试剂在用 | 研究页 |
| 2 | microbiology | 微生物学（放线菌） | 链霉菌属筛选策略，阿维菌素之源 | 核心页 |
| 3 | drug discovery | 药物发现 | staurosporine/lactacystin/cerulenin 等 | 研究页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Koji Nakanishi | 对方 → 导师 | 1960 年旁听其在东京教育大学的课程，后为其门下（infobox Academic advisors 明载） |
| advisor-student | Max Tishler | 对方 → 导师 | 1971 年卫斯理安大学访问期间结缘，共同促成 Merck 合作（库内 id=3982） |
| colleague | William C. Campbell (scientist) | 无向 | 与 Merck 合作，其培养物由 Campbell 团队开发成阿维菌素/伊维菌素 |
| co-honored | William C. Campbell (scientist) | 无向 | 2015 诺贝尔生理学或医学奖共享一半（线虫寄生虫感染的新疗法） |
| co-honored | Tu Youyou | 无向 | 2015 同届诺奖（Ōmura/Campbell 共享线虫半边，屠呦呦独得疟疾半边） |

**不入库但提示词可叙述**：实验室温室培养的"31 位大学教授与 120 位博士"（未具名，不建学生边）；Merck & Co.（机构合作非个人关系）；北里柴三郎（北里研究所创办人，精神渊源非个人关系）；Sophie 月桂勋章等荣誉授予方。

## 五、配色方案 【人物专属】

- **气质**：和纸的素朴、发酵罐的琥珀、韮崎乡土的收藏家气质
- **主色**：`#5C3A1E`（琥珀褐——土壤与发酵培养液）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeSoil` 土壤微生物 — 琥珀褐 `#5C3A1E`
  - `badgeCompound` 天然产物 — 深青 `#0E7490`
  - `badgeAver` 阿维菌素 — 深绿 `#146B3A`
  - `badgeHonor` 荣誉传承 — 暗红 `#7A2430`
- **背景母题**：放射状菌丝与分子骨架图交错。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 土壤微生物的收藏家 / Satoshi Ōmura b.1935 + 四色 badge + 右上头像 + 国籍行（Japan）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生、山梨县韮崎出身、山梨大学/东京理科大学/东京大学、
    北里大学/卫斯理安大学任职、诺奖 2015、核心领域）
03  核心贡献概览 — 链霉菌筛选 / 阿维菌素→伊维菌素 / 480+ 化合物 / 天然药物宝库
04  夜校教师的转身 (1935–1961) — 山梨大学毕业、东京都立墨田工业高中理科教师、旁听 Nakanishi 课程
05  双博士之路 (1961–1970) — 东京理科大学 MS、东京大学药学博士（1968）、东京理科大学理学博士（1970）
06  北里研究所 (1965– ) — 抗生素实验室主任（1973）、药学院教授（1975）、培养 31 教授 120 博士
07  卫斯理安与 Merck 之缘 (1971–1973) — 访问教授、结识 Tishler、共同争取 Merck 研究经费
08  阿维菌素的发现（核心贡献页）— *S. avermitilis* 菌株、大环内酯、与 Merck 合作、Campbell 开发伊维菌素
09  从兽用到人用（核心页）— 1981 兽用上市、1987-88 Mectizan 人用抗河盲症、内外兼杀剂（endectocide）
10  480 个化合物 — staurosporine（蛋白激酶抑制剂）、lactacystin（蛋白酶体抑制剂）、cerulenin 等
11  2015 诺奖：与 Campbell 共享一半 — 获奖理由逐字呈现、屠呦呦独得另一半（结构讲清）
12  荣誉与认可 — 日本学士院奖 1990、Koch 金奖 1997、Gairdner 全球健康奖 2014、文化勋章 2015 等
13  收藏家与美育 — 韮崎大村美术馆（2007）、女子美术大学理事长两任、北里重建与医学中心
14  遗产与结尾 — 领路孩童青铜雕像（WHO/卡特中心/布基纳法索）、阿维菌素→消除河盲症 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 姓名与在世口径 | **yaml/入库用 manifest 形式 "Satoshi Ōmura"**（带长音符 Ō）；1935-07-12 生于韮崎，**在世**——封面写 b.1935；日文名汉字"大村 智" |
| 2015 的"一半"结构 | **Ōmura/Campbell 共享一半（线虫新疗法）+ 屠呦呦独得另一半（疟疾）**——三人勿平分；Ōmura 页开头的"shared with Tu Youyou and with William C. Campbell"是同届叙述，两半结构以奖项页/屠呦呦页口径为准 |
| 双博士 | 东京大学药科学博士（1968，Dissertation PhD）+ 东京理科大学理学博士（1970）——两个 PhD 并存，勿删并 |
| 两条师承 | infobox Academic advisors=Koji Nakanishi + Max Tishler；Nakanishi 始于 1960 年旁听课程（东京教育大学），Tishler 始于 1971 年卫斯理安访问与 ACS 主席身份——两条边并行勿合并；**正文未载东京大学博士导师姓名，勿杜撰第三条** |
| Tishler 规范名 | 库内已有 "Max Tishler"（id=3982），直接用，未新建 stub |
| 分工链路 | **Ōmura 分离 *S. avermitilis* 并产出阿维菌素 → Campbell 团队开发伊维菌素**——Ōmura 篇强调"发现菌株与阿维菌素"，勿把伊维菌素的药化改造归给自己 |
| 引语红线 | page.md **无任何直接引语**——全篇禁引语，用忠实转述 |
| 480 化合物 | 1970 年代以来发现 480+ 新化合物、其中 25 种药物/试剂在用——两个数字勿混 |
| 雕像叙事 | 描绘孩童引领盲人的雕像立于北里大学、WHO 日内瓦总部、Carter Center、Merck、世界银行与布基纳法索——本篇独有素材 |
| 教育timeline | 山梨大学 1958 → 高中理科教师 → 1960 旁听 → 1961 东京理科大学 → 北里 1965——"夜校教师出身"叙事是本篇反差主线 |
| 学会头衔 | NAS 外籍院士 1999、日本学士院会员 2001、法国科学院/俄罗斯科学院/中国工程院外籍等——列 honoree 页时择要，勿全铺 |
| 对手方名 | Campbell="William C. Campbell (scientist)"、屠呦呦="Tu Youyou"——yaml 均按此形式 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| roundworm parasites | 线虫寄生虫 | 获奖理由核心词 |
| Streptomyces | 链霉菌属 | 土源放线菌，斜体 |
| avermectin | 阿维菌素 | 1979 论文报道的新家族 |
| ivermectin | 伊维菌素 | 阿维菌素衍生物（Campbell 侧开发） |
| endectocide | 内外兼杀剂 | 世界首个，兼具抗内寄生虫与外寄生虫 |
| staurosporine | 星形孢菌素 | 蛋白激酶特异性抑制剂 |
| lactacystin | 乳酸胞苷（蛋白酶体抑制剂） | Ōmura 发现 |
| cerulenin | 浅蓝菌素 | 脂肪酸生物合成抑制剂 |
| Kitasato Institute | 北里研究所/北里大学 | 1965 年起供职 |
| natural products chemistry | 天然产物化学 | 480+ 化合物的学科归属 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**With Me**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：Ōmura 的一生是"与人同行"的一生——与 Nakanishi/Tishler 的师承、与 Merck 的三十年合作、与 Campbell 的跨洋接力、以及北里大学门下 31 教授 120 博士的传承；With Me 的陪伴感对应其"发现者+培育者"的双重身份，也对应那份跨越山海的科学协作。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/21th_century/Satoshi_Ōmura/WithMe.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
