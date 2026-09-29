# 和平奖得主立传提示词（OpenPeace 实例：International Committee of the Red Cross）

> 本文件是 OpenPeace 项目的「诺贝尔和平奖得主立传提示词」，以红十字国际委员会（ICRC，1917/1944/1963 三度获奖）为完整实例。
> 结构对齐 OpenPhysicist 标杆 `Kenneth_G_Wilson_zh.md`（一~五节）。凡标注【模板通用】可复用，【组织机构专属】按本机构执行。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：International Committee of the Red Cross（红十字国际委员会，ICRC）——**本篇为组织机构篇（is_org=true）**：1917/1944/1963 三度获诺贝尔和平奖，全项目唯一三次获奖主体，只做一次提示词 + 一条 DB 记录。
- **设计哲学**：机构篇以「机构概览页」替代人物身份信息页；叙事骨架是「一场战役（索尔费里诺）→ 一本书 → 一个委员会 → 一部公约 → 三座诺贝尔奖」的制度演化史。

---

## 二、背景信息 【组织机构专属】

- **目标机构**：International Committee of the Red Cross（成立 1863-02-17，日内瓦；至 2025 年雇员 17,337 人）
- **气质关键词**：**战地中立的守护者、日内瓦公约的推动者、三次诺贝尔和平奖得主**
- **官方获奖理由（三次，英文原文照抄 nobel_peace_citations.json，中译照抄名录，禁止改写）**：
  - **1917**：> "for the efforts to take care of wounded soldiers and prisoners of war and their families" —— 表彰其为照顾伤兵、战俘及其家属所付出的努力
  - **1944**：> "for the great work it has performed during the war on behalf of humanity" —— 表彰它在战争期间为人道事业所做的卓越工作
  - **1963**：> "for promoting the principles of the Geneva Convention and cooperation with the UN" —— 表彰其推广《日内瓦公约》原则并与联合国开展合作（与红十字会协会 League of Red Cross Societies 共享）
- **设计母题**：**白底红十字（the emblem）**。瑞士国旗反色而成的保护标志——视觉语言宜用红白双色块、公约条文纹理、日内瓦湖岸轮廓。
- **本地数据源**：`peace/presentations/pages/20th_century/International_Committee_of_the_Red_Cross/page.md`（Wikipedia 全文 + frontmatter，事实基准唯一来源）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【组织机构专属】

- 成立：1863-02-17（日内瓦五人委员会首次会议，宣布成立「常设国际委员会」）
- 性质：总部位于瑞士日内瓦的人道援助组织；国际红十字与红新月运动成员；瑞士民间协会（cooptation 制，成员限瑞士公民至 1923 年扩至瑞士全国）
- 口号：*Inter Arma Caritas*（战时慈善犹存）；三官方语言（英/法/西）
- 创立脉络：
  1. 1859-06-24 索尔费里诺战役（一日约四万伤亡）；Henry Dunant 目睹惨状，组织当地民众救治
  2. 1862 Dunant 自费出版 *A Memory of Solferino*，倡导志愿救护组织 + 战地伤员保护条约
  3. 1863-02-09 日内瓦公益学会五人小组委员会成立（Dunant、Gustave Moynier、Louis Appia、Théodore Maunoir、Guillaume-Henri Dufour）
  4. 1863-10-26/29 日内瓦国际会议通过决议（国家救护协会、伤员中立、白底红十字标志等）
  5. 1864-08-22 首部日内瓦公约签署（12 国签署）
- 关键史实清单：
  - 1867 Dunant 因阿尔及利亚生意破产被逐出委员会（与 Moynier 冲突）；1901 首届诺奖授予 Dunant 与 Passy，ICRC 官方致贺标志 Dunant 正名
  - 1876 定名「红十字国际委员会」（ICRC）
  - 一战：1914-10-15 设国际战俘局（至战争结束转交约 2000 万封信件/190 万包裹/约 1800 万瑞士法郎；促成约 20 万战俘交换；卡片索引约 700 万张，识别约 200 万战俘）；524 座战俘营视察；抗议化学武器；1917 获诺贝尔和平奖（1914–18 间唯一）
  - 1919 红十字会协会成立（Henry P. Davison 推动，意欲取代 ICRC 主导权，关系长期紧张）
  - 1923 成员资格从日内瓦市民扩至瑞士公民
  - 二战：179 名代表视察 41 国 12,750 次战俘营；中央情报局 3,000 员工/4,500 万张卡片/1.2 亿条讯息；1944-11 后向集中营囚犯寄送约 110 万包裹（登记约 10.5 万人）；1942 年公开谴责动议被否、对纳粹灭绝营信息保持沉默——**ICRC 自认其历史上最大失败（2005 官方声明明载）**；1944 获第二次诺贝尔和平奖（1939–45 主战期间唯一）
  - 1949 四部日内瓦公约修订；1963 百年之际与红十字会协会共享第三次诺贝尔和平奖
  - 1965 七项基本原则；1990 联大观察员地位（首个获此地位的私人组织）；1993 协议确立对瑞士的独立
  - 1994 公开谴责卢旺达种族灭绝；1995 斯雷布雷尼察自省声明；2007 公开批评缅甸军方
  - 2023-10-04 发布平民黑客行为规则
- 领导人谱系（ presidents，page.md 明载）：1863–64 Henri Dufour → 1864–1910 Gustave Moynier（任期最长） → 1910–28 Gustave Ador → 1928–44 Max Huber → 1945–48 Carl Jacob Burckhardt → … → 2022– Mirjana Spoljaric Egger（首位女性主席）
- 关键时间线（15–20 节点）：1859 索尔费里诺 → 1862 《索尔费里诺回忆录》 → 1863-02-17 五人委员会 → 1863-10 日内瓦国际会议 → 1864-08-22 首部日内瓦公约 → 1867 Dunant 出局 → 1876 定名 ICRC → 1901 Dunant 获首届诺奖 → 1906/1907 公约修订与海牙十号公约 → 1914 战俘局 → 1917 首次诺奖 → 1919 协会成立与主导权之争 → 1923 成员扩至瑞士全国 → 1929 战俘公约 → 1939–45 二战行动 → 1944 第二次诺奖 → 1949 四公约 → 1955 接管国际寻人服务局 → 1963 第三次诺奖（与协会共享） → 1965 七原则 → 1977/2005 附加议定书 → 1990 联大观察员 → 1993 瑞士独立协议 → 1994–2007 公开谴责三案 → 2023 平民黑客规则

### 第 4 步：使命领域表 【组织机构专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | humanitarian aid | 人道援助 | 战伤救护、战俘保护、灾荒救济 | 使命页 |
| 1 | international humanitarian law | 国际人道法 | 日内瓦公约体系的推动与守护 | 公约页 |
| 2 | conflict mediation | 冲突调解 | 交战方之间的中立中介 | 特征页 |
| 3 | disaster relief | 灾害救济 | 法律授权之外的自然灾害救援 | 使命页 |

### 第 4.5 步：社会关系表（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| founder | Henry Dunant | 无向 | 创始人，*A Memory of Solferino* 作者，1901 首届诺奖 |
| founder | Gustave Moynier | 无向 | 共同创始人，1864–1910 任主席（任期最长） |
| founder | Louis Appia | 无向 | 共同创始人，战地外科医生 |
| founder | Théodore Maunoir | 无向 | 共同创始人，日内瓦卫生委员会医生 |
| founder | Guillaume Henri Dufour | 无向 | 共同创始人，瑞士名将，首任主席 |
| co-honored | League of Red Cross Societies | 无向 | 1963 诺贝尔和平奖共同得主 |
| controversy | Henry Pomeroy Davison | 无向 | 1919 创立红十字会协会意欲取代 ICRC 主导权 |
| colleague | Max Huber | 无向 | 1928–1944 任主席，法理学家 |
| other | International Red Cross and Red Crescent Movement | 无向 | 上级运动之成员（与 IFRC 并列） |

### 第 5 步：设计配色方案 【模板通用，组织机构专属色彩】

- **主色**：深青 `#0B5351`（manifest 预分配，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeICRC` 红十字标志 — 红色 `#C8102E`（标志色例外使用）
  - `badgeIHL` 国际人道法 — 靛蓝 `#3F5E9E`
  - `badgeMED` 医疗救护 — 青绿 `#0E7C7B`
  - `badgePOW` 战俘保护 — 琥珀 `#C9821F`
- **背景母题**：白底红十字几何底纹 + 稀疏圆点，呼应「中立保护标志」

### 第 6 步：规划幻灯片序列 【组织机构专属，10–16 页，机构概览页替代身份信息页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 战地中立的守护者 / ICRC 1863– + 三次诺奖 badge + 右上标志 + 「International organization」行
02  机构概览页（★ 必做，替代身份信息页）— 左标志 + 右信息网格（成立/总部/性质/口号/三奖/领导谱系/使命领域）
03  制度贡献概览 — 日内瓦公约 / 战俘保护 / 中立中介 / 三次诺奖
04  索尔费里诺与一个构想 (1859–1863) — Dunant、五人委员会、白底红十字
05  首部日内瓦公约 (1864) — 12 国签署、十条款、国家协会的诞生
06  早期风雨 (1867–1901) — Dunant 出局与正名、1876 定名、1906/1907 修订
07  一战：国际战俘局 (1914–1918) — 700 万张卡片、20 万战俘交换、化学武器抗议
08  1917：第一次诺贝尔和平奖 — 理由句原文呈现、战时唯一
09  主导权之争 (1919–1944) — Davison 与红十字会协会、1923 扩员
10  二战与最大的失败 (1939–1945) — 战俘营视察、集中营包裹、1942 沉默与 2005 官方反省
11  1944 与 1963：第二、三次诺贝尔奖 — 理由句原文呈现、百年共享
12  战后建制 (1949–1993) — 四公约、七原则、联大观察员、对瑞士独立
13  当代行动与争议 (1994–2023) — 卢旺达/斯雷布雷尼察/缅甸公开谴责、平民黑客规则
14  遗产：一部公约史与一个标志
15  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；机构概览页实现模式参照人物篇 `\profileslide` 改制。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【组织机构专属】

**ICRC 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 三次获奖并列 | 1917/1944 独享（均为大战期间唯一颁发的和平奖），1963 与红十字会协会共享——三条理由句必须分开呈现，勿混写 |
| 创始人勿写错 | 创始人是五人小组（Dunant/Moynier/Appia/Maunoir/Dufour）；Dunant 是创始人但 1867 被逐出委员会——两件事分开叙述；**勿把某任主席（如 Ador/Huber）写成创始人** |
| 主席勿当创始人 | Moynier 既是共同创始人也是任期最长主席；其余主席仅是领导人，非创始人 |
| 政治敏感红线 | 二战/纳粹/集中营/卢旺达/缅甸/巴以相关内容一律按 page.md **客观事实记录，不加评价性语句**；Dunant 破产与 Moynier 冲突仅陈述事实 |
| ICRC 自认失败 | 「对纳粹灭绝营沉默是其历史上最大失败」出自 ICRC 2005-01-27 官方声明（page.md 明载），可引用并注明是 ICRC 自我反省口径 |
| Haefliger 事件 | Louis Haefliger 1945 独行预警救下 Mauthausen 约 6 万人、被 ICRC 谴责、1990 由 Sommaruga 正名——按 page.md 三段事实平铺，勿加评判 |
| 标志问题 | 红十字/红新月/红水晶三标志的演进（1863→奥斯曼红新月→2005 红水晶）；Magen David Adom 2006 才入会——按史实陈述，敏感符号争议客观记录 |
| 与 IFRC 关系 | 1919 成立的 League of Red Cross Societies 即今日 IFRC；1963 共享诺奖时的名称是 League of Red Cross Societies；Seville Agreement 1997 分工——三者勿混名 |
| 数字核对 | 战俘局 700 万张卡片/约 200 万识别；二战 4,500 万张卡片/1.2 亿条讯息/12,750 次视察——两战数字勿互换 |
| 无载禁写 | 1917/1944 颁奖细节（演说、颁奖人）page.md 无载，勿杜撰 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| International Committee of the Red Cross | 红十字国际委员会 | 法语 CICR，勿与红十字会协会混淆 |
| Geneva Conventions | 日内瓦公约 | 1864/1906/1929/1949 各版须注年份 |
| First Geneva Convention | 首部日内瓦公约 | 1864-08-22，12 国签署 |
| International Prisoners-of-War Agency | 国际战俘局 | 1914-10-15 设立 |
| Restoring Family Links | 重连家庭联系 | 寻人服务 |
| Central Information Agency | 中央情报局 | 二战战俘信息机构，勿与国家情报机构混淆 |
| International Tracing Service | 国际寻人服务局 | 1955 起由 ICRC 接管 |
| Seville Agreement | 塞维利亚协议 | 1997，运动内部分工 |
| Inter Arma Caritas | 战时慈善犹存 | ICRC 保留的原口号 |
| Red Crystal | 红水晶 | 2005 新增标志 |
| cooptation | 内部遴选 | ICRC 成员产生方式 |

---

## 四、背景音乐选择 【组织机构专属】

- **选定曲目**: **Ascension** — Cold Cinema（manifest 预分配，勿改）
- **风格**: 史诗 / 铺陈 / 科幻感管弦
- **匹配理由**: 从索尔费里诺战场到三次诺贝尔奖——「Ascension」的阶梯式铺陈匹配一个组织跨越三个世纪的制度攀升；管弦质感匹配日内瓦公约体系的庄重
- **本地路径**: `music_audio/inspiring-electronic/20-gYUC-sXt_8M-Cinematic Dramatic Epic Orchestra Sci-Fi Trailer by Cold Cinema [No Copyright Music] ⧸ Ascension.wav`
- **时长对齐**: ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/International_Committee_of_the_Red_Cross/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构标杆 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（1917/1944/1963 三条） |
| `peace/nobel_peace_citations.json` | 官方获奖理由英文原文 |
| `MySQL/seed_person.py` | 研究领域 + 社会关系入库引擎（组织机构记录） |

> **开始执行。每完成一步汇报。**
> **最重要的事：每写一页就 make，看到溢出就修；三次获奖理由分开呈现；政治敏感内容只作客观事实记录；无载禁写。**
