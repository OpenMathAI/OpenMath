# 和平奖得主立传提示词（人物专属实例：Eisaku Satō）

> 本文件是 OpenPeace 的「和平奖得主立传提示词」，以 Eisaku Satō（佐藤荣作，1974 诺贝尔和平奖，日本首相）为实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节母本）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 旗下与 physicist/chemist/medic/literature 平级）。
- **模板来源**：Kenneth_G_Wilson_zh.md 结构母本 + 和平奖项目共享工作流 `peace/PROMPTS_WORKFLOW.md`。
- **本实例**：Eisaku Satō（佐藤栄作，1901–1975，日本首相 1964–1972，非核三原则与 NPT）。
- **设计哲学**：和平奖立传同样需要「身份信息页」与「事业领域」结构化表达；本篇以「无核的承诺」为视觉母题；「诺奖争议」「秘密协定被解密」等只作 page.md 明载的客观事实记录，不评价。

---

## 二、背景信息 【人物专属】

- **目标人物**：Eisaku Satō（1901-03-27 ~ 1975-06-03，享年 74 岁）
- **诺奖年份与官方获奖理由**（1974，与 Seán MacBride 共享；英文原文照抄 `peace/nobel_peace_citations.json`，中译照抄名录，禁止改写）：
  > "for his contribution to stabilize conditions in the Pacific rim area and for signing the Nuclear Non-Proliferation Treaty."（表彰他为稳定亚太地区局势做出的贡献以及签署《不扩散核武器条约》）
- **气质关键词**：**当时最长的首相任期、非核三原则的提出者、冲绳返还的谈判者**
- **设计母题**：**无核的承诺（non-nuclear pledge）**——三道锁/三原则的几何意象（不产·不持·不带入）+ 环太平洋弧线，呼应获奖理由。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Eisaku_Satō/page.md`

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

### 第 0 步：事实基准（已按 page.md 核对）

- **生卒**：1901-03-27 生于山口县熊毛郡田布施町（第三子，父佐藤秀助酿酒业）；1975-06-03 00:55 逝于东京慈惠会医科大学附属医院（1975-05-19 筑地宴会中突发脑溢血昏迷），享年 74 岁；骨灰葬田布施家族墓。
- **家族**：Satō–Kishi–Abe 家族；长兄 Ichirō Satō（海军中将）、次兄 Nobusuke Kishi（岸信介，首相 1957–1960）；侄孙 Shinzō Abe 亦为首相。1926 与 Hiroko Satō（佐藤宽子，1907–1987）结婚，二子 Ryūtarō 与 Shinji（佐藤信二，后从政）。妻子为堂妹（父 Matsusuke Satō 为其母舅）。
- **教育**：山口县立山口中学 → 第五高等学校 → 东京帝国大学法学部（德国法），1923 高等文官考试合格，1924 毕业入铁道省。
- **官僚生涯**：大阪铁道局局长（1944–1946）、运输省次官（1947–1948）。
- **政务任职**：内阁官房长官（1948–1949）；1949 入国会（自由党，山口 2 区，至 1975）；递信/邮政大臣（1951–1952）、建设大臣（1952–1953）、内阁官房长官（1953–1954，吉田内阁）；大藏大臣（1958–1960，岸信介内阁）；通产大臣（1961–1962，池田内阁）；科学技术厅长官+北海道开发厅长官（1963–1964）；第 39 任首相（1964-11-09 ~ 1972-07-07，三届连任，当时最长）兼 LDP 总裁；1968-10~11 兼外相。
- **首相任内主线**：① 1965 日韩基本条约（邦交正常化）；② 1965 向约翰逊总统公开请求返还冲绳、1969 与尼克松达成返还协议、1972-05-15 冲绳正式返还（含尖阁/钓鱼岛，主权争议客观一句带过或不展开）；③ 1967-12-11 提出「非核三原则」（不产·不持·不带入），1971 国会决议正式采纳；④ 1968 签署 NPT（国会 1970 批准口径见 page.md——获奖理由句用 signing）；⑤ 1970 自动延长日美安保条约；⑥ 1966 参与创建亚洲开发银行、1967 首位访新的日本首相。
- **卸任与晚年**：1972-07 辞职（支持率跌至 19%）；1972-11 获菊花章大绶；1973 出席尼克松连任就职；1974-12-11 获诺贝尔和平奖（首位接受和平奖的亚洲人）；1975-04 出席蒋介石葬礼（「亲善代表」身份）；1975-06-03 去世，追授菊花章颈饰（日本最高荣誉）与正一位。
- **关键时间线（17 节点）**：1901 生田布施 → 1924 入铁道省 → 1944–1946 大阪铁道局局长 → 1947–1948 运输次官 → 1948–1949 内阁官房长官 → 1949 入国会 → 1958–1960 大藏大臣 → 1964-11-09 就任首相 → 1965 日韩基本条约 → 1965 首次访美请求返还冲绳 → 1967-12-11 非核三原则 → 1968 签署 NPT → 1969 与尼克松达成冲绳返还协议 → 1971 国会决议采纳非核三原则 → 1972-05-15 冲绳返还 → 1972-07 辞职 → 1974-12-11 获诺贝尔和平奖 → 1975-06-03 逝于东京。
- **解密争议（客观记录）**：2008 年日本政府解密文件显示 1965 年访美时曾与美方讨论对华使用核武可能性；2009 年其子证实 1969-11 与尼克松会谈中同意冲绳返还后仍允许美军核弹头（危机时）进驻——以上为 page.md 明载解密事实，呈现时置于「争议与解密」专页，客观陈述不评价。

### 第 4 步：事业领域表（与 yaml `fields` 一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | politics | 政治 | 首相 1964–1972、LDP 总裁 | 政务页 |
| 1 | nuclear non-proliferation | 核不扩散 | 非核三原则、签署 NPT | 核心页 |
| 2 | diplomacy | 外交 | 日韩建交、冲绳返还谈判 | 外交页 |
| 3 | foreign policy | 外交政策 | 日美安保延长、对华对台政策 | 外交页 |
| 4 | economic policy | 经济政策 | 高速增长期、凯恩斯主义政策 | 政务页 |

### 第 4.5 步：社会关系表（与 yaml `relations` 完全一致）

| 关系类型 | 对方（name_en） | 方向 | note |
|---------|------|------|------|
| colleague | Nobusuke Kishi | 无向 | 兄长，前首相，其内阁中任大藏大臣 |
| spouse | Hiroko Satō | 无向 | 1926 结婚，二子 |
| co-honored | Seán MacBride | 无向 | 1974 诺贝尔和平奖共同得主 |
| colleague | Richard Nixon | 无向 | 1969 达成冲绳返还协议，互出席对方仪式/葬礼 |
| colleague | Shigeru Yoshida | 无向 | 吉田学校出身，多届吉田内阁任职 |
| colleague | Hayato Ikeda | 无向 | 继池田之后任首相，池田内阁中任通产大臣 |

### 第 5 步：配色方案 【manifest 预分配，勿改】

- **主色**：`#2F4470`（靛青——官僚理性的日式沉静）
- **诺奖香槟金**：`#C9A227`
- **四分类色（badgeA–D）**：badgeA 非核三原则 `#1E6B5A`；badgeB 冲绳返还 `#8C5A2E`；badgeC 日韩建交 `#4A3B76`；badgeD 高速增长 `#2F5D50`
- **背景母题**：三道同心锁环（非核三原则）+ 环太平洋弧线淡纹

### 第 6 步：幻灯片序列（14 页规划，含身份信息页★必做）

```
00  OpenPeace 项目首页（共享封面）
01  封面 — 无核的承诺 / Eisaku Satō 1901–1975 + 四色 badge + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、家族、教育、任职、荣誉、核心领域）
03  山口出身与官僚之路 (1901–1948) — Satō–Kishi–Abe 家族、铁道省、运输次官
04  吉田学校 (1948–1954) — 官房长官、邮政·建设大臣
05  大藏·通产大臣 (1958–1964) — 兄岸信介内阁、池田内阁
06  就任首相 (1964) — 当时最长任期、高速增长
07  日韩邦交正常化 (1965) — 基本条约
08  非核三原则与 NPT (1967–1971)（核心页）— 1967-12-11 三原则、1968 签署 NPT、1971 国会决议
09  冲绳返还 (1965–1972) — 约翰逊、尼克松、1972-05-15
10  1974 诺贝尔和平奖（★ 必做专页）— 获奖理由、首位接受和平奖的亚洲人、与 MacBride 共享
11  争议与解密（客观记录页）— 2008/2009 解密文件、秘密协定
12  卸任与晚年 (1972–1975) — 菊花章、尼克松葬礼、追授颈饰
13  结尾
```

### 第 7–8 步：版式要点 + 人物专属陷阱表

- **版式**：对齐 Kenneth_G_Wilson 模板骨架；vbox≤10pt、hbox≤50pt；日语罗马字长音符（Satō/Satō Eisaku）用 ō 完整渲染；姓名汉字（佐藤栄作/佐藤荣作）须 CJK 字体。
- **陷阱表**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方为 "for his contribution to stabilize conditions in the Pacific rim area and for signing the Nuclear Non-Proliferation Treaty."；NPT 签署年份口径：1968 签署（获奖理由用 signing）、1970 批准、1976 日本批准生效——正文只按 page.md 的 1968 签署+1971 国会决议两处写 |
| 首位亚洲得主口径 | Thọ 1973 首位**获**奖（拒领）；Satō 1974 首位**接受**奖的亚洲人——勿混 |
| 姓名 | 英文形式 Eisaku Satō（罗马字 Satō Eisaku），汉字佐藤栄作（新字体）；日文名序 vs 西名序统一用西名序 |
| 兄长 | Nobusuke Kishi 是兄长（同为首相）——无 sibling 关系类型，yaml 用 colleague+note「兄长」；勿写 parent-child |
| 妻子 | Hiroko Satō 为堂妹（母舅之女），此亲缘细节可叙述；1974-11 刊物风波（妻子访谈指控）按 page.md 客观一句或不写 |
| 与 MacBride 后续 | page.md 明载获奖后加入 Amnesty International 与 MacBride 合作——可叙述；除 co-honored 外不入库其他关系 |
| 政治敏感 | 对台对华政策、蒋介石葬礼、主权争议一律按 page.md 客观陈述，不作评价 |
| 卒日 | 1975-06-03（05-19 中风昏迷后），勿与中风日混淆 |

### 第 9 步：术语审查

| 英文 | 中文 | 风险 |
|------|------|------|
| Three Non-Nuclear Principles | 非核三原则 | 不产·不持·不带入，1967-12-11 |
| Nuclear Non-Proliferation Treaty (NPT) | 不扩散核武器条约 | 1968 签署 |
| Okinawa reversion | 冲绳返还 | 1972-05-15 |
| Treaty on Basic Relations | 日韩基本条约 | 1965-06-22 |
| U.S.–Japan Security Treaty | 日美安全保障条约 | 1970 自动延长 |
| Yoshida school | 吉田学校 | 吉田茂门下的政治谱系 |
| LDP (Liberal Democratic Party) | 自民党 | 总裁 1964–1972 |
| Chief Cabinet Secretary | 内阁官房长官 | 1948–1949、1953–1954 两段 |
| Order of the Chrysanthemum | 菊花章 | 大绶 1972、颈饰 1975 追授 |
| Tsukiji | 筑地 | 1975-05-19 中风地，勿写成卒地 |

---

## 四、背景音乐 ✅ 【manifest 预分配，勿改】

- **选定曲目**：**The Invisible Light** — Infraction（inspiring-electronic 曲库）
- **匹配理由**：纪录片式的冷静铺陈，匹配「官僚出身→长期执政→非核承诺→诺奖」的克制叙事；"Invisible Light"（不可见之光）暗合「核」的不可见威慑与「无核化」的道德选择之间的张力。
- **本地路径**：`music_audio/inspiring-electronic/19-tGxXsgSKPiQ-Documentary Cinematic by Infraction [No Copyright Music] ⧸ The Invisible Light.wav`
- **时长处理**：ffmpeg `-shortest` 自动对齐视频长度。

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Eisaku_Satō/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 名录（中译获奖理由照抄源） |
| `peace/nobel_peace_citations.json` | 官方英文获奖理由 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/PROMPTS_WORKFLOW.md` | 共享工作流与红线 |
| `MySQL/data/Eisaku_Satō.yaml` | 入库 yaml（fields/relations 与本文一致） |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
