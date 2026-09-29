# 和平奖得主立传提示词（人物专属实例：Andrei Sakharov）

> 本文件是 OpenPeace 的「和平奖得主立传提示词」，以 Andrei Sakharov（安德烈·萨哈罗夫，1975 诺贝尔和平奖，苏联氢弹之父转人权活动家）为实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节母本）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 旗下与 physicist/chemist/medic/literature 平级）。
- **模板来源**：Kenneth_G_Wilson_zh.md 结构母本 + 和平奖项目共享工作流 `peace/PROMPTS_WORKFLOW.md`。
- **本实例**：Andrei Dmitrievich Sakharov（1921–1989，苏联理论物理学家与人权活动家）。
- **设计哲学**：和平奖立传同样需要「身份信息页」与「事业领域」结构化表达；本篇是本批唯一的「科学+人权」双轨人物——从核武器总设计师到流放中的和平奖得主，视觉叙事以「从沙罗夫的密室到世界的讲台」为母题；苏联相关内容只作 page.md 明载的客观事实记录，不评价。

---

## 二、背景信息 【人物专属】

- **目标人物**：Andrei Dmitrievich Sakharov（1921-05-21 ~ 1989-12-14，享年 68 岁）
- **诺奖年份与官方获奖理由**（1975，独得；英文原文照抄 `peace/nobel_peace_citations.json`，中译照抄名录，禁止改写）：
  > "for his struggle for human rights in the Soviet Union, for disarmament and cooperation between all nations."（表彰他为苏联人权、裁军以及各国间合作而进行的斗争）
  > （挪威诺奖委员会另称其 "a spokesman for the conscience of mankind"——page.md 明载转述，可用）
- **气质关键词**：**氢弹之父、人类良知的代言人、不屈服的流放者**
- **设计母题**：**对称与良知（symmetry & conscience）**——其宇宙学「萨哈罗夫条件」的 C/CP 对称意象 + 从聚变火球到人权讲台的明暗转换；物理学与良知两条轨道交汇于一点。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Andrei_Sakharov/page.md`

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

### 第 0 步：事实基准（已按 page.md 核对）

- **生卒**：1921-05-21 生于莫斯科（俄罗斯）；1989-12-14 晚逝于莫斯科家中（尸检结论：扩张型心肌病引发心律失常），享年 68 岁；葬 Vostryakovskoye 公墓。
- **国籍**：苏联（Nobel 名录 country=Soviet Union；frontmatter 另含 Russian SFSR 口径）。
- **家庭**：父 Dmitri Ivanovich Sakharov（第二莫斯科国立大学物理学教授、业余钢琴家）、母 Yekaterina Alekseevna Sofiano（沙俄将军之女）；祖父 Ivan 为律师（主张废除死刑）。1943 与 Klavdia Alekseyevna Vikhireva 结婚（育二女一子，1969 妻去世）；1972 与人权活动家 Yelena Bonner 结婚。
- **教育**：莫斯科大学物理系（1938 入学，1941 疏散后 1942 于阿什哈巴德毕业）→ 乌里扬诺夫斯克弹药厂（发明穿甲弹探伤工艺）→ 1945 入列别捷夫物理研究所（FIAN）理论部，师从 Igor Tamm；1947 通过 Doctor of Sciences 论文（核跃迁理论 0→0 transitions）。
- **核武器计划**：1948 中参加苏联原子弹计划（Kurchatov/Tamm 麾下）；1950 迁 Sarov（closed city）；「分层蛋糕」sloika 构想 →「第三构想」（美方称 Teller–Ulam 设计）；1955 RDS-37 首试；1961-10-30 沙皇炸弹（50 Mt，史上最大核试验）为其设计的放大版。
- **和平利用与基础物理**：1950 与 Tamm 提出 tokamak 受控核聚变构想（基于 Lavrentiev 思想）；1951 发明 MK 磁通压缩发生器；1965 后转向粒子物理与宇宙学——**萨哈罗夫条件**（重子数破坏、C/CP 破坏、偏离热平衡）解释宇宙重子不对称；质子衰变首个理论动机；CPT 对称双子宇宙与「时间箭头反转」模型；诱导重力（induced gravity）。
- **转向人权活动**：1950s 末起关注核试验后果，推动 1963 部分禁止核试验条约；1964 公开反对李森科派 Nuzhdin 入选科学院（KGB 因此建档）；1966 「二十五人公开信」反对部分平反斯大林；1967-07-21 反导系统（ABM）秘密信；1968-05《进步、和平共处与思想自由》反思文章（samizdat 流传、国外发表后被禁军事研究）；1970 与 Valery Chalidze、Andrei Tverdokhlebov 创建苏联人权委员会；1973 起定期会见西方记者。
- **诺奖与流放**：1975-12 获诺贝尔和平奖（**被禁出国**，妻子 Bonner 在奥斯陆代读演讲《Peace, Progress, Human Rights》——含苏联政治犯名单，宣布与所有良心犯共享该奖）；1980-01-22 因抗议苏军入阿被捕，流放高尔基（Nizhny Novgorod，1980–1986）；1980 被剥夺全部苏联奖项（Hero of Socialist Labour×3、Stalin Prize、Lenin Prize 等），公开拒绝领回；1984/1985 两度为妻子出国治病绝食；1985-12 欧洲议会设立 Sakharov Prize；1986-12-19 戈尔巴乔夫电话允许返莫斯科。
- **晚年**：1988 会见里根；1988-12 亚美尼亚/阿塞拜疆调查之旅（纳戈尔诺-卡拉巴赫名言——page.md 明载原文可引）；1989-03 当选全国人民代表大会代表、共同领导跨地区代表团（民主反对派）；1989-12-14 拟定大会发言前夜去世。
- **纪念遗产**：欧洲议会 Sakharov Prize（1988/1990 年代设立口径两说，page.md 正文两处——1985-12 设立、1988 年以荣誉命名，以「欧洲议会以其名设立人权奖」客观写）；APS Andrei Sakharov Prize（2006 起）；耶路撒冷/莫斯科/圣彼得堡等全球街巷广场命名；小行星 1979 Sakharov。
- **关键时间线（19 节点）**：1921 生莫斯科 → 1938 入莫斯科大学 → 1942 阿什哈巴德毕业、军工厂 → 1945 入 FIAN 师从 Tamm → 1947 Doctor of Sciences → 1948 参加核计划 → 1949 苏联首颗原子弹试验 → 1950 迁 Sarov、提出 tokamak → 1951 MK 发生器 → 1953 首次 Hero of Socialist Labour、Stalin Prize → 1955 RDS-37 氢弹 → 1956 Lenin Prize → 1961 沙皇炸弹 → 1963 部分禁止核试验条约 → 1968《反思》文章被禁军事研究 → 1970 共建苏联人权委员会 → 1972 与 Bonner 结婚 → 1975 诺贝尔和平奖（Bonner 代读演讲）→ 1980 流放高尔基 → 1986-12-19 获准返莫斯科 → 1989 当选人民代表 → 1989-12-14 逝于莫斯科。

### 第 4 步：事业领域表（与 yaml `fields` 一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | theoretical physics | 理论物理 | FIAN 理论部、核跃迁理论 | 学术页 |
| 1 | nuclear physics | 核物理 | 苏联热核武器计划、聚变武器设计 | 核计划页 |
| 2 | controlled nuclear fusion | 受控核聚变 | tokamak 构想（与 Tamm） | 聚变页 |
| 3 | physical cosmology | 物理宇宙学 | 萨哈罗夫条件、双子宇宙 | 宇宙学页 |
| 4 | human rights activism | 人权运动 | 苏联人权委员会、诺贝尔演讲 | 核心页 |

### 第 4.5 步：社会关系表（与 yaml `relations` 完全一致）

| 关系类型 | 对方（name_en） | 方向 | note |
|---------|------|------|------|
| advisor-student | Igor Yevgenyevich Tamm | advisor（对方是导师） | FIAN 理论部导师，tokamak 共同提出者 |
| colleague | Igor Kurchatov | 无向 | 苏联核计划负责人 |
| spouse | Klavdia Vikhireva | 无向 | 1943 结婚，1969 去世，育三人 |
| spouse | Yelena Bonner | 无向 | 1972 结婚，同为人权活动家，代读诺贝尔演讲 |
| colleague | Valery Chalidze | 无向 | 1970 共同创建苏联人权委员会 |
| colleague | Andrei Tverdokhlebov | 无向 | 1970 共同创建苏联人权委员会 |
| parent-child | Dmitri Ivanovich Sakharov | 无向 | 父，物理学教授 |

### 第 5 步：配色方案 【manifest 预分配，勿改】

- **主色**：`#750014`（深绯红——聚变火光与抗争意志）
- **诺奖香槟金**：`#C9A227`
- **四分类色（badgeA–D）**：badgeA 核武器计划 `#4A3B2B`；badgeB 基础物理 `#1E4E79`；badgeC 人权运动 `#2E5E4E`；badgeD 流放与诺奖 `#6E2B3B`
- **背景母题**：明暗双轨光带（聚变火球→人权讲台）+ C/CP 对称镜像淡纹

### 第 6 步：幻灯片序列（15 页规划，含身份信息页★必做）

```
00  OpenPeace 项目首页（共享封面）
01  封面 — 人类良知的代言人 / Andrei Sakharov 1921–1989 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、家庭、师承、任职、荣誉、核心领域）
03  莫斯科书香少年 (1921–1945) — 父亲物理学教授、疏散与军工厂
04  Tamm 门下 (1945–1948) — FIAN 理论部、Doctor of Sciences
05  核武器计划 (1948–1961)（核心页）— sloika→第三构想、RDS-37、沙皇炸弹
06  和平利用：tokamak 与 MK 发生器 (1950–1951)
07  基础物理遗产 (1965– ) — 萨哈罗夫条件、质子衰变、双子宇宙
08  良知的转折 (1958–1968) — 反对核试验、Nuzhdin 事件、《反思》文章
09  人权委员会 (1970–1975) — Chalidze/Tverdokhlebov、Bonner、西方记者
10  1975 诺贝尔和平奖（★ 必做专页）— 获奖理由、被禁出国、Bonner 代读演讲、与良心犯共享
11  流放高尔基 (1980–1986) — 绝食、奖项被剥、Sakharov Prize 设立
12  迟来的春天 (1986–1989) — 戈尔巴乔夫电话、人民代表、跨地区代表团
13  荣誉与纪念 — 全球命名、APS 奖、欧洲议会奖
14  结尾
```

### 第 7–8 步：版式要点 + 人物专属陷阱表

- **版式**：对齐 Kenneth_G_Wilson 模板骨架；vbox≤10pt、hbox≤50pt；俄语人名转写统一（Yelena Bonner 非 Elena）；西里尔字母（Андрей Дмитриевич Сахаров）如需展示须专用字体，正文建议只作封面装饰一处。
- **陷阱表**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方为 "for his struggle for human rights in the Soviet Union, for disarmament and cooperation between all nations."；委员会评语 "spokesman for the conscience of mankind" 是转述非获奖理由句 |
| Tamm 规范名 | 库内既有记录为 'Igor Yevgenyevich Tamm'（id=2189），yaml 必须用此全名形式防分裂；勿写 'Igor Tamm' |
| 氢弹设计归属 | 「第三构想」即美方的 Teller–Ulam 设计（page.md 明载并列写）；勿写「萨哈罗夫独自发明氢弹」，也勿写美国侧归属细节 |
| 萨哈罗夫条件 | 是重子不对称生成三条件（B 破坏、C/CP 破坏、偏离热平衡），勿与「禁区条件」等混淆 |
| Oppenheimer/Teller | page.md 只说 Sakharov 自认与二人命运有「惊人相似」——是自述比喻，**不入库建关系** |
| Solzhenitsyn | 曾为其辩护、后有分歧——仅叙述，不入库建关系 |
| 奖项被剥 | 1980 被剥夺苏联奖项、公开拒绝领回；Hero of Socialist Labour 三次（1953/1956/1962）与 Nobel 1975 两条线勿混 |
| 流放地 | Gorky（今 Nizhny Novgorod）1980–1986；「内部流放」表述按 page.md |
| 卒因 | 扩张型心肌病引发心律失常（尸检病理学家 Rapoport 笔记口径），勿写「心脏病发作」泛称 |
| 政治敏感红线 | 苏联体制评价类内容（「癌症细胞」比喻等引语）按 page.md 客观标注为本人言论，不加叙述者评价；阿以冲突立场、阿富汗战争等仅时间线客观一句 |

### 第 9 步：术语审查

| 英文 | 中文 | 风险 |
|------|------|------|
| Sakharov conditions | 萨哈罗夫条件 | 重子生成三条件，宇宙学语境 |
| Teller–Ulam design | 泰勒–乌拉姆设计 | 苏方称「第三构想」 |
| Tsar Bomba | 沙皇炸弹 | 50 Mt，1961-10-30 |
| tokamak | 托卡马克 | 与 Tamm 共同提出 |
| sloika | 分层蛋糕（构型） | 早期聚变装置构想 |
| samizdat | 萨米兹达特（地下出版物） | 《反思》文章传播方式 |
| Committee on Human Rights in the USSR | 苏联人权委员会 | 1970 三人共创 |
| internal exile | 内部流放 | Gorky 1980–1986 |
| Refusenik | 拒绝移民者（苏联犹太人） | 其支持对象之一 |
| Sakharov Prize | 萨哈罗夫奖 | 欧洲议会人权奖，以其名设立 |
| Inter-Regional Deputies Group | 跨地区代表团体 | 1989 共同领导 |
| Vostryakovskoye Cemetery | 沃斯特里亚科夫斯科耶公墓 | 安葬地 |

---

## 四、背景音乐 ✅ 【manifest 预分配，勿改】

- **选定曲目**：**Winds Of Freedom** — Really Slow Motion & Giant Apes（inspiring-electronic 曲库）
- **匹配理由**：英雄式的自由主题管弦乐，匹配「从密室中的聚变火光到为自由吹响的号角」的人生弧线；"Winds Of Freedom" 直接呼应其「自由的风终将吹散高尔基的沉寂」——1986 年重返莫斯科的叙事高点。
- **本地路径**：`music_audio/inspiring-electronic/25-l3Fsk4R6eys-Really Slow Motion & Giant Apes - Winds Of Freedom (Epic Heroic Orchestral).wav`
- **时长处理**：ffmpeg `-shortest` 自动对齐视频长度。

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Andrei_Sakharov/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 名录（中译获奖理由照抄源） |
| `peace/nobel_peace_citations.json` | 官方英文获奖理由 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/PROMPTS_WORKFLOW.md` | 共享工作流与红线 |
| `MySQL/data/Andrei_Sakharov.yaml` | 入库 yaml（fields/relations 与本文一致） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：苏联相关内容只作客观事实记录，每写一页就 make，看到溢出就修。**
