# 和平奖得主立传提示词（OpenPeace 批次 1：Frédéric Passy）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Frédéric Passy（1901 首届诺贝尔和平奖共同得主、欧洲和平运动元老）为实例。
> 凡标注 `【模板通用】` 的部分可原样复用到任何和平奖得主；标注 `【人物专属】` 的部分需按目标人物替换。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenMathAI 数学家/物理学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家侧标杆 Kenneth_G_Wilson_zh.md 的 0–11 节结构，移植到和平事业人物。
- **本实例**：Frédéric Passy（弗雷德里克·帕西）。
- **设计哲学**：和平奖得主立传同样必须有「身份信息页」与「事业领域」的结构化表达；Passy 是「经济学家出身的和平主义者」——用经济理性论证和平，是本届双得主中「和平会议/仲裁」路线的代表。

---

## 二、背景信息 【人物专属】

- **目标人物**：Frédéric Passy（1822-05-20 巴黎 ~ 1912-06-12 按名录口径卒于法国，享年 90 岁；正文一句作"he died in Paris"，身份页以 Neuilly-sur-Seine infobox 口径为准并可不展开）
- **气质关键词**：**欧洲和平运动元老、自由放任的经济学家、议会仲裁的推动者** —— 1901 首届诺贝尔和平奖获奖理由：
  > "for his lifelong work for international peace conferences, diplomacy and arbitration"（表彰他毕生致力于国际和平会议、外交与仲裁事业）
- **设计母题**：**天平与圆桌（scales and the round table）**。用经济学天平衡量战争与和平的成本，用圆桌会议替代战场——仲裁与协商的几何意象，是比「和平鸽」更贴合 Passy 的视觉语言。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Frédéric_Passy/page.md`（含 frontmatter QID Q180409）
- **参考模板**：
  - 物理学家标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`peace/presentations/cover/openpeace_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库要求**：研究领域（第 4 步）与社会关系（第 4.5 步）已按本提示词写入 `greatminds` 库（MySQL），Beamer 立传与其并行。

### 第 0 步：核对 Wikipedia 页面与事实基准 【人物专属】

- ✅ 已下载 `https://en.wikipedia.org/wiki/Frédéric_Passy` 四件套到 `peace/presentations/pages/20th_century/Frédéric_Passy/`（**第一轮已核对，事实基准如下**）：
  - 生卒（1822-05-20 生于巴黎 ~ 1912-06-12 逝，享年 90 岁；infobox 卒地 Neuilly-sur-Seine）
  - 国籍（法国）
  - 家庭（父 Justin Félix Passy 滑铁卢战役老兵；母 Marie Louise Pauline Salleron 1827 年去世；妻 Marie Blanche Sageret 1847 年结婚、1900 年去世；子女 Paul/Jean/Marie Louise/Alix；外孙辈 Mathilde Paulian 1912 埃菲尔铁塔坠亡）
  - 教育（Lycée Condorcet、Lycée Louis-le-Grand；受法律训练）
  - 任职（1846 Conseil de Droit 会计；1848 国民自卫军；1849 辞职转向经济学；1881–1889 巴黎第八区众议员；1874–1898 Seine-et-Oise 省议会议员）
  - 关键荣誉（Nobel Peace Prize 1901；Legion of Honour 1895，1903 晋升 Commander）
  - 核心事业清单（①1867 创立国际永久和平联盟 ②《和平之友法国协会》1872 起 ③议会间会议/各国议会联盟 1889 首任主席 ④经济学讲学与著述 ⑤1901 首届诺贝尔和平奖）
  - 关键时间线（15–20 节点，见第 6 步幻灯片序列）

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下创建 `Frédéric_Passy/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同项目已有成品的 `Makefile`，设置 `MAIN=Frédéric_Passy_zh`、`VIDEO_NAME=Frédéric_Passy_zh`（宏名中勿直接使用带变音符字符时，可改用 ASCII 宏名 Passy）

### 第 3 步：收集图片 【人物专属】

- ✅ 本地 `images.txt` 有真实图像：
  - 主肖像 `Drawing_of_Frédéric_Passy.jpg`（1899 年《纽约新闻报》刊载画像）
  - 备选 Frédéric_Passy_and_Marie_Blanche_Passy.jpg（1855 与妻合影）、Paul_Passy.jpg（长子画像，可作家族页插图）
- 无肖像时用装饰圆占位（本篇不需要）

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

> 把事业领域变成可检索、可图形化的结构化字段（`fields` + `person_field` 表）。以下 5 条已入库。

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | peace movement | 和平运动 | 和平联盟/和平之友协会/仲裁协会创始者 | 联盟页、协会页 |
| 1 | international arbitration | 国际仲裁 | 议会仲裁请愿、仲裁条约倡导 | 议会页 |
| 2 | political economy | 政治经济学 | 讲学著述、道德与政治科学院 1877 | 学术页 |
| 3 | peace education | 和平教育 | 和平教材、1909 和平主义教学课程 | 教育页 |
| 4 | free trade advocacy | 自由贸易倡导 | 反对谷物关税、商业与工业自由保卫协会 | 议会页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> 以下 8 条与 yaml 完全一致，已入库（仅收 page.md 明载关系）。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Henry Dunant | 无向 | 1901 首届诺贝尔和平奖共同得主 |
| colleague | William Randal Cremer | 无向 | 1888–1889 共同创立议会间会议（后各国议会联盟） |
| colleague | Michel Chevalier | 无向 | 1867 共同获准创立国际永久和平联盟 |
| influence | Frédéric Bastiat | 师→受影响 | 自由主义经济学家，最受其思想启发 |
| influence | Richard Cobden | 师→受影响 | 反谷物法同盟的思想源流 |
| spouse | Blanche Sageret | 无向 | 1847 结婚，1900 去世 |
| parent-child | Paul Passy | 父→子 | 长子，国际语音学协会创始人 |
| parent-child | Jean Passy | 父→子 | 次子，继兄任国际语音学协会书记 |

- 方向约定：influence 影响者→本人；parent-child 按 from<to 排序不写 direction（自动归一）
- 对手方 name_en 用 manifest 规范名；缺失人物由 seed_person.py 自动建占位记录

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：理性、温和、法式的克制
- **配色**：深紫罗兰（manifest 预分配主色 `#372A75`，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeLigue` 和平联盟 — 自由紫 `#5E35B1`
  - `badgeArbit` 仲裁事业 — 协商蓝 `#1E6B8C`
  - `badgeEcon` 政治经济学 — 学院绿 `#2E7D52`
  - `badgeNobel` 首届诺奖 — 香槟金 `#C9A227`
- **背景母题**：柔和气泡 + 细圆桌环形意象（低饱和同心圆弧），呼应「圆桌仲裁」的设计母题

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题或底部状态栏明示国籍（France），底部状态栏给出 `国籍 | 事业 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心贡献之前。左侧头像 + 右侧信息网格，含至少：生卒、国籍、出生地、家庭、教育、任职、主要荣誉、核心领域。
4. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 欧洲和平运动元老 / Frédéric Passy 1822–1912 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（含家庭、教育、任职、荣誉、核心领域）
03  核心贡献概览 — 和平联盟 / 和平之友协会 / 议会间会议 / 首届诺奖
04  家世与早年 (1822–1849) — 滑铁卢老兵之家、法律训练、会计与国民自卫军、拒宣誓转向经济学
05  思想的形成 — Bastiat/Cobden/O'Connell、阿尔及利亚战争叙事的触动、经济与道德视角的反战
06  国际永久和平联盟 (1867) — Le Temps 三封信、与 Chevalier 获准创会、600 会员、"war on war"
07  普法战争与挫折 (1870–1871) — 色当之后的外交斡旋、联盟瓦解、两条道路之问
08  和平之友法国协会 (1872–1889) — 仲裁转向、1878 巴黎博览会大会、与 Pratt 协会合并
09  议会生涯 (1873–1889) — Marseille 落选、Seine-et-Oise 1874、1881 众议员、东京征伐之争
10  议会间会议 (1887–1889) — 与 Cremer 的法英请愿、112 签名、1889 首届大会任主席
11  写作与学术 — 政治经济学讲学、道德与政治科学院 1877、科学促进会主席 1881、和平教育 1906/1909
12  1901 首届诺贝尔和平奖 — 与 Dunant 共享各逾 10 万法郎、未赴奥斯陆、身后刊布的批评文章
13  晚年与和解 (1905–1912) — 卢塞恩与德国和平主义者握手、90 寿辰寄语、"faith which removes mountains"
14  遗产 — "欧洲和平运动元老"之誉、长子 1927 回忆录、IPU 2004 设 Passy 档案中心
15  结尾
```

### 第 7–8 步：版式要点与专属陷阱 【模板通用 + 人物专属】

**版式**：每页 `\newcommand{\xxxslide}{...}`；每写完一页 `make`，用 `pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

**Passy 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 诺奖理由措辞 | 官方理由 "for his lifelong work for international peace conferences, diplomacy and arbitration"，强调**和平会议/外交/仲裁**，与 Dunant 的人道主义口径分立，勿互换 |
| 与 Dunant 分工 | 1901 分奖树立「和平会议派 vs 人道主义派」两类先例——这一分析是 page.md 明载的，可写；但勿写成委员会内部投票细节 |
| 目录名变音符 | 目录 Frédéric_Passy 含 é；LaTeX 宏名与文件名避免变音符，页面文字用 XeLaTeX 原生支持 |
| 三个协会名 | Ligue Internationale et Permanente de la Paix（1867）≠ Société Française des Amis de la Paix（1872）≠ Société Française pour l'Arbitrage entre Nations（1889 合并后），勿混写 |
| 与自由联盟区分 | 同年 Charles Lemonnier 在日内瓦创 Peace and Freedom League，政治性更强；Passy 刻意与其划清界限——勿合并叙述 |
| 议员任期 | 众议员 1881–1889（infobox In office），1889 连任失败败给 Marius Martin；Seine-et-Oise 省议员 1874–1898；勿写"终身议员" |
| 宗教立场 | 生于天主教家庭，1870 后转非宗派自由派新教——客观记录，不加评价 |
| 引语使用 | 仅 page.md 明载英文译文引语可入引文框（如 1868 演讲、1877 科学院申请文、1912 遗言寄语），须注明为译文 |
| 家族悲剧 | 外孙女 Mathilde Paulian 1912 埃菲尔铁塔坠亡仅一句客观带过，不渲染 |
| 无载禁写 | 不写其经济学著述的具体影响范围、不编造与拿破仑三世的关系、不写 Nobel 奖金的具体去向（Cooper 注为"很可能用于和平活动"须带推断语气） |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Inter-Parliamentary Union | 各国议会联盟 | 1889 首届议会间会议后身，Passy 任首届主席 |
| international arbitration | 国际仲裁 | Passy 的核心方法论，与"裁军"区分 |
| Ligue Internationale et Permanente de la Paix | 国际永久和平联盟 | 1867 创立，普法战争后瓦解 |
| Société Française des Amis de la Paix | 和平之友法国协会 | 1872 复兴期创立 |
| peace education | 和平教育 | 1906/1909 两部教学作品 |
| political economy | 政治经济学 | 与"经济学"表述统一为该词条 |
| Académie de sciences morales et politiques | 道德与政治科学院 | 1877 入选 |
| dean of European peace activists | 欧洲和平运动元老 | page.md 明载之誉 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Timeless** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 沉稳 / 纪念 / 长期主义
- **匹配理由**:
  - "Timeless" 呼应获奖理由中的 "lifelong work"——毕生事业跨越 60 年（1867 创会到 1912 谢世），正是时间尺度上的永恒感
  - 沉稳气质匹配 Passy 的法式克制与经济理性，非戏剧化的渐进改良路线
- **本地路径**: `music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav` → `presentations/20th_century/Frédéric_Passy/Timeless.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Frédéric_Passy/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/pages/20th_century/Frédéric_Passy/images.txt` | 肖像与插图 URL |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄，勿改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `MySQL/data/Frédéric_Passy.yaml` | 社会关系/领域入库母本 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
