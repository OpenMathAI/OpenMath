# 和平奖得主立传提示词（OpenPeace：Philip Noel-Baker）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Philip Noel-Baker, Baron Noel-Baker（1959 诺贝尔和平奖，英国裁军运动家）为实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Philip John Noel-Baker, Baron Noel-Baker（菲利普·诺埃尔-贝克，1959 诺贝尔和平奖）——史上唯一同时获得奥运奖牌与诺贝尔奖的人；从国联缔造者到终身裁军运动家。
- **设计哲学**：保留「身份信息页」与「事业领域结构化表达」两大骨架；本篇叙事重心是**双轨迹人生**——跑道的 1500 米与谈判桌上的裁军马拉松，两条轨迹在「持久奋斗」中合一。

---

## 二、背景信息 【人物专属】

- **目标人物**：Philip John Noel-Baker, Baron Noel-Baker（本姓 Baker，1889-11-01 ~ 1982-10-08，享年 92 岁）
- **气质关键词**：**裁军运动家、奥运银牌得主、国联缔造参与者** —— 1959 诺贝尔和平奖获奖理由：
  > "for his longstanding contribution to the cause of disarmament and peace"（表彰他长期对裁军与和平事业的贡献）
- **设计设计母题**：**跑道与谈判桌（the track and the table）**。以奥运跑道弧线与国际会议圆桌交叠的图形语言，呼应「竞技体育的持久力 × 裁军谈判的持久战」。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Philip_Noel-Baker_Baron_Noel-Baker/page.md`
- **参考模板**：标杆提示词 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`；首页模板 `peace/presentations/cover/openpeace_page.tex`

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

### 第 0 步：核对本地页面，建立事实基准 【人物专属】

- ✅ 页面已抓取（frontmatter：QID Q211856 / 生卒（卒日多值噪声，以正文 1982-10-08 为准）/ 国籍 UK / 职业 / 教育经历）
- **事实基准（第一轮已核对，全部以 page.md 为准）**：
  - 生卒：1889-11-01 生于伦敦 Brondesbury Park ~ 1982-10-08 逝于伦敦威斯敏斯特家中，享年 92 岁
  - 国籍：英国
  - 家庭：七个孩子中的第六个；父 Allen Baker 为加拿大出生的贵格会（Quaker）教徒、制造业企业家，1895–1906 伦敦郡议会进步派议员，1905–1918 东芬斯伯里自由党下院议员；母 Elizabeth Balmer Moscrip 为苏格兰人
  - 教育：贵格会学校 Ackworth School、Bootham School（约克）→ 美国贵格背景的 Haverford College（宾州）→ 1908–1912 剑桥 King's College（历史 Tripos Part I 二等 + 经济学 Part II 一等；1912 剑桥辩论社主席；1910–1912 田径俱乐部主席）
  - 体育：1912 斯德哥尔摩奥运 800m/1500m（1500m 进决赛）→ 1920 安特卫普奥运英国田径队队长并掌旗，1500m 银牌（队友 Albert Hill 夺金）→ 1924 巴黎奥运队长未参赛；史上唯一奥运奖牌+诺贝尔奖双得主
  - 任职主线：1912 获 Whewell 国际法奖学金 → 1914 Ruskin College 副校长 → 1915 剑桥 King's College Fellow → 一战组建 Friends' Ambulance Unit（1914–1915 法国前线）→ 1916 起良心拒服兵役者，任意大利第一英国救护队副官（1915–1918，获英法意三国军功章）→ 一战后协助创建国际联盟（Lord Robert Cecil 助理 → 首任秘书长 Sir Eric Drummond 助理，主管委任统治早期工作）→ 1924–1929 LSE 首任 Sir Ernest Cassel 国际关系教授 → 1933–1934 耶鲁讲师 → 1929–1931 与 1936–1970 下院议员（Coventry → Derby → Derby South；共 36 年）→ 二战运输部政务次官（1942-02 起）→ 1945 国务大臣（外交部）→ 1946-10 空军大臣 → 1947 英联邦关系大臣入阁 → 1950 燃料电力大臣 → 1946–1947 工党主席；1948 伦敦奥运会筹办负责大臣 → 1970 退出下院 → 1977-07-22 受封终身贵族 Baron Noel-Baker of the City of Derby（87 岁入上院，1982 年前仍参与福克兰战争辩论）
  - 关键荣誉：Nobel Peace Prize 1959；1920 安特卫普奥运 1500m 银牌；英法意三国军功章
  - 核心事业清单：① 国联创建与委任统治体系早期工作；② 裁军著述与运动（Disarmament 1926/1934、The Private Manufacture of Armaments 1936、The Arms Race 1958 等）；③ 1932–1933 日内瓦世界裁军会议（Henderson 助理）；④ 联合国宪章起草的英国代表团成员（1940s 中期）；⑤ 1979 与 Fenner Brockway 共创 World Disarmament Campaign 并任共同主席至去世；⑥ 1960–1976 国际运动科学与体育教育理事会主席
  - 关键时间线（15–20 节点）：1889 伦敦出生 → 1908 入剑桥 → 1912 Whewell 奖学金+辩论社主席 → 1912 斯德哥尔摩奥运 → 1914 Ruskin 副校长 → 1914–1915 Friends' Ambulance Unit → 1915 与 Irene Noel 结婚+剑桥 Fellow → 1916–1918 意大利救护队 → 1919–1920 国联创建 → 1921 改姓 Noel-Baker → 1924–1929 LSE 首任 Cassel 讲座教授 → 1929 当选 Coventry 议员 → 1932–1933 裁军会议 → 1936 Derby 补选当选 → 1938 反对轰炸德国城市的演说 → 1942 运输部政务次官 → 1945 外交部国务大臣 → 1947 英联邦关系大臣 → 1948 奥运筹办 → 1950 燃料电力大臣 → 1956 妻 Irene 去世 → 1958 出版 The Arms Race → 1959 诺贝尔和平奖 → 1970 退休议员 → 1977 终身贵族 → 1979 World Disarmament Campaign → 1982-10-08 去世（数月前仍在辩论福克兰战争）

### 第 1–3 步：目录 / Makefile / 图片 【模板通用】

- 在 `peace/presentations/20th_century/Philip_Noel-Baker_Baron_Noel-Baker/` 下建 `images/`；Makefile 复制同项目成品并设 `MAIN=Philip_Noel-Baker_Baron_Noel-Baker_zh`
- 肖像：优先 page.md/images.txt 中的 1942 照片；下载失败用装饰圆占位并记录

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | disarmament | 裁军 | 终身事业：著述、会议、运动，1959 和平奖核心 | 核心页 |
| 1 | international relations | 国际关系 | 国联创建、联合国宪章起草参与 | 国联页 |
| 2 | international law | 国际法 | Whewell 奖学金、英属自治领法律地位专著 | 学术页 |
| 3 | peace activism | 和平运动 | World Disarmament Campaign 等 | 运动页 |
| 4 | athletics | 田径运动 | 1920 奥运 1500m 银牌、英国队队长掌旗 | 体育页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）【人物专属】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Irene Noel | 无向 | 1915-06 结婚，因妻姓于 1921 改姓 Noel-Baker，妻 1956 去世 |
| parent-child | Francis Noel-Baker | 无向 | 独子，同为工党下院议员，父子同院 |
| colleague | Robert Cecil, 1st Viscount Cecil of Chelwood | 无向 | 一战后协助创建国际联盟时任其助理 |
| colleague | James Eric Drummond | 无向 | 国联首任秘书长助理，主管委任统治早期工作 |
| colleague | Arthur Henderson | 无向 | 1929–1931 任外交大臣 Henderson 政务次官，1932–33 日内瓦裁军会议续任其助理 |
| colleague | Fenner Brockway | 无向 | 1979 共同创立 World Disarmament Campaign，任共同主席至去世 |

> 只收 page.md 明载的关系：Albert Hill（队友夺金）、Michael Foot（NEC 席位接替者）非社会关系不入库；Megan Lloyd George 婚外情事 page.md 虽有载，属私生活敏感面，不入关系表、正文亦不展开；Bertrand Russell 仅为撰文致敬者，不入库。

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **主色（manifest 预分配，勿改）**：深海蓝绿 `#0E4D64`
- 辅色：诺奖香槟金 `#C9A227`
- 四分类色：`badgeDisarm` 裁军 — 靛蓝 `#1F3A5F`；`badgeLeague` 国联/国际 — 青绿 `#0E7C7B`；`badgeSport` 奥运 — 琥珀 `#E07B30`；`badgeMP` 议会生涯 — 玫瑰红 `#C4204F`
- **背景母题**：柔和气泡 + 跑道弧线与圆桌同心圆交叠，呼应「跑道与谈判桌」

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上肖像 + 细边框 + 姓名小字注）与国籍行。
2. 必须有身份信息页（★）：左头像 + 右信息网格（生卒、本姓与改姓、国籍、出生地、教育、任职、奥运与诺奖双荣誉、核心领域）。
3. 品牌口径统一：结尾页底部写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 裁军的马拉松 / Philip Noel-Baker 1889–1982 + badge + 头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心事业概览 — 国联 / 裁军著述与会议 / 联合国宪章 / 奥运双轨迹
04  贵格之家：Ackworth 到剑桥 (1889–1912) — 父亲的议会生涯与贵格教育
05  奥运跑道 (1912–1924) — 斯德哥尔摩、安特卫普银牌、巴黎队长
06  良心与救护 (1914–1918) — Friends' Ambulance Unit、意大利、三国军功章
07  国联缔造者 (1919–1924) — Cecil 与 Drummond 助理、委任统治
08  学者与议员 (1924–1938) — LSE 首任 Cassel 讲座、Coventry/Derby
09  裁军会议与著述 (1932–1958)（核心贡献页）— 1932–33 日内瓦、Hawkers of Death、The Arms Race
10  战时与阁员 (1942–1951) — 运输部/外交部/空军/英联邦关系/燃料电力
11  1948 伦敦奥运筹办 — 议员中的体育大臣角色
12  诺贝尔和平奖 1959 — 获奖理由 + 唯一奥运奖牌+诺奖双得主的特殊性
13  终身贵族与最后的运动 (1970–1982) — 87 岁入上院、World Disarmament Campaign、福克兰辩论
14  遗产：裁军理想的百年接力
15  结尾
```

### 第 7–8 步：Beamer 源码与布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}`；身份信息页参照成品 `\profileslide` 模式。
- 每写完一页 `make` 并 `pdftoppm` 目检；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Noel-Baker 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 姓氏系统 | 本名 Philip John Baker；1915 与 Irene Noel 结婚后 1921 年依契约（deed poll）改复合姓 Noel-Baker——行文首次出现注明，勿写「笔名」 |
| 卒日噪声 | frontmatter date_of_death 三值（1982-10-08/10-09/01-01），以正文 1982-10-08 为准 |
| 「唯一」表述 | "the only person to have won an Olympic medal and received a Nobel Prize"——page.md 明载可直接写；勿扩写成「唯一诺奖得主运动员」之外的变体 |
| 银牌归属 | 1920 安特卫普 1500m 银牌，金牌是队友 Albert Hill——提银牌须带此语境，勿写成「惜败于外国选手」 |
| 议席变迁 | Coventry 1929–1931 → 1935 Coventry 落选 → 1936-07 Derby 补选当选 → 1950 选区拆分后转 Derby South 至 1970——四段勿混 |
| 裁军立场 | 他主张多边核裁军而非单边裁军（unilateral disarmament 的反对者）、1950 年代反对 Bevanite 左翼路线——须客观并陈，勿写成「反战和平主义者」笼统标签 |
| 1938 演说 | 反对轰炸德国城市基于道义理由，可引 "The only way to prevent atrocities from the air is to abolish air warfare and national air forces altogether."（page.md 明载原文）——仅此一句可引 |
| 战时角色 | 一战是救护队组织者+良心拒服兵役者（conscientious objector），二战是运输部政务次官——两战角色勿混 |
| 私生活 | 婚姻不睦与 Megan Lloyd George 一事 page.md 有载，但属私生活，正文不展开、关系表不入 |
| 同名区分 | 与 Frederick Sanger 无关；其子 Francis Noel-Baker 亦为议员，引用 Hansard 记录时注意父子区分 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| disarmament | 裁军 | 全篇核心词，勿混「军控 arms control」 |
| League of Nations | 国际联盟 | 勿译「国家联盟」 |
| mandates system | 委任统治体系 | 国联早期工作 |
| Friends' Ambulance Unit | 教友派救护队 | 贵格会背景 |
| conscientious objector | 良心拒服兵役者 | 1916 起身份 |
| World Disarmament Conference | 世界裁军会议 | 1932–1933 日内瓦 |
| World Disarmament Campaign | 世界裁军运动 | 1979 与 Brockway 共创 |
| life peer | 终身贵族 | 1977 受封 Baron Noel-Baker |
| Queen's/Silver Jubilee Honours | 银禧荣誉 | 1977 授勋名册 |
| International Council of Sport Science and Physical Education | 国际运动科学与体育教育理事会 | 1960–1976 任主席 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Expedition** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 进取 / 长途 / 纪录片
- **匹配理由**:
  - 「长途」匹配其「长期贡献」的获奖理由——从 1919 国联到 1982 福克兰辩论，裁军事业纵贯 60 余年
  - 「进取」匹配双轨迹人生的持续奔跑——奥运跑道与议会走廊同构
  - 「纪录片」匹配文献式叙事——著作、会议记录、议会辩论构成生平材料
- **本地路径**: `music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav` → 复制为 `presentations/20th_century/Philip_Noel-Baker_Baron_Noel-Baker/Expedition.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Philip_Noel-Baker_Baron_Noel-Baker/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄勿改） |
| `peace/prompt_manifest.json` | batch=peace-batch-11（主色/BGM 预分配） |
| `MySQL/data/Philip_Noel-Baker_Baron_Noel-Baker.yaml` | 研究领域+社会关系入库文件 |
| `MySQL/seed_person.py` | 幂等入库引擎 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
