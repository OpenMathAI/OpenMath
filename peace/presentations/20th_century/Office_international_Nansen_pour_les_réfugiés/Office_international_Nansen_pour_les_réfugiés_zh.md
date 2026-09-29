# 和平奖得主立传提示词（OpenPeace 批次 9：Nansen International Office for Refugees）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Nansen International Office for Refugees（南森国际难民办公室，1938 诺贝尔和平奖得主、国际联盟下属难民救援机构）为实例。
> 凡标注 `【模板通用】` 的部分可原样复用到任何和平奖得主；标注 `【人物专属】` 的部分需按目标替换。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（与 OpenMathAI 数学家/物理学家侧共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家侧标杆 Kenneth_G_Wilson_zh.md 的 0–11 节结构，移植到和平事业主体。
- **本实例**：Nansen International Office for Refugees（南森国际难民办公室，法文 Office International Nansen pour les Réfugiés）。**本篇主体是机构（is_org=true），不是个人**。
- **设计哲学**：机构立传同样必须有「机构概览页」（替代个人身份信息页）与「事业领域」的结构化表达；本篇的叙事灵魂是「一个人身后的名字，变成一张护照与一份公约」——南森 1930 年去世，以他命名的办公室把个人遗产转化为制度性救援。

---

## 二、背景信息 【人物专属】

- **目标机构**：Nansen International Office for Refugees（1930 年成立 ~ 1939 年解散，总部日内瓦）
- **气质关键词**：**南森遗产的继承者、无国籍者的护照、欧洲难民的庇护所** —— 1938 诺贝尔和平奖获奖理由：
  > "for having carried on the work of Fridtjof Nansen to the benefit of refugees across Europe"（表彰它继承弗里乔夫·南森的事业，惠及全欧洲的难民）
- **设计母题**：**南森护照（Nansen passport）**。一本让无国籍者得以跨越国界的旅行证件、一纸 1933 年《难民公约》、一枚盖在护照上的办公室印章——「证件即通行权」是比「和平鸽」更贴合本机构的视觉语言。本地已有南森护照封面照与办公室印章照可用作核心视觉元素。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Office_international_Nansen_pour_les_réfugiés/page.md`（含 frontmatter QID Q743558）
- **参考模板**：
  - 物理学家标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`peace/presentations/cover/openpeace_page.tex`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库要求**：事业领域（第 4 步）与社会关系（第 4.5 步）已按本提示词写入 `greatminds` 库（MySQL），Beamer 立传与其并行。

### 第 0 步：核对 Wikipedia 页面与事实基准 【人物专属】

- ✅ 已下载 `https://en.wikipedia.org/wiki/Office_international_Nansen_pour_les_réfugiés` 四件套到 `peace/presentations/pages/20th_century/Office_international_Nansen_pour_les_réfugiés/`（**第一轮已核对，事实基准如下**）：
  - 机构成立/解散（1930 年由国际联盟设立，1939 年解散；与国际联盟难民事务高级专员公署〔1933 设立〕同时解散）
  - 得名（得名于 Fridtjof Nansen，在其去世后不久设立，继承其国际难民救援事业）
  - 前身（延续南森 1921 年在日内瓦创立的难民救援组织）
  - 经费（国际联盟负担行政开支——仅来自南森护照收费；福利救济经费来自私人捐助）
  - 关键成就（①南森护照体系 ②1933《难民公约》获 14 国采纳 ③在叙利亚与黎巴嫩 specially constructed houses 安置 4 万亚美尼亚人、另 1 万安置于埃里温 ④1935 萨尔重归德国后在巴拉圭重新安置萨尔难民）
  - 局限（对来自第三帝国的难民与西班牙内战难民，南森援助不适用，而许多国家拒绝接收这些难民）
  - 诺奖（1938 年获奖；因机构随后解散，奖金由国际联盟新设的难民组织领取）
  - 延续（1938 年设难民事务高级专员取代本办公室，该职为联合国难民事务高级专员公署 UNHCR 的前身）
  - 关键时间线（10–15 节点，见第 6 步幻灯片序列）

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下创建 `Office_international_Nansen_pour_les_réfugiés/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同项目已有成品的 `Makefile`，设置 `MAIN=Office_international_Nansen_pour_les_réfugiés_zh`、`VIDEO_NAME` 同名

### 第 3 步：收集图片 【人物专属】

- ✅ 本地 `images.txt` 可用（**无机构肖像照，用以下两张作核心视觉**）：
  - `Nansen_cs_cover.jpg`（南森护照封面，布拉格警察局 1930）——**机构概览页与封面徽章首选**
  - `Nansen_cs_stamp.jpg`（南森国际难民办公室护照印章）——插图页
  - `No-nb_bldsa_6d244.jpg`（南森任国联战俘与难民事务高级专员期间在索非亚的照片）——作「得名由来」插图，图注须写明是南森本人而非机构
- 机构无「肖像」，封面右上角用南森护照封面图或装饰圆 + 护照印章意象占位

### 第 4 步：事业领域梳理 + 入库 【模板通用，人物专属内容】

> 把事业领域变成可检索、可图形化的结构化字段（`fields` + `person_field` 表）。以下 4 条已入库。

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | refugee protection | 难民保护 | 南森护照体系让无国籍者得以跨国旅行 | 核心页、护照页 |
| 1 | humanitarian aid | 人道主义援助 | 为难民提供物资与政治支持 | 机构概览页 |
| 2 | international law | 国际法 | 1933《难民公约》获 14 国采纳 | 公约页 |
| 3 | refugee resettlement | 难民重新安置 | 叙利亚/黎巴嫩 4 万亚美尼亚人、萨尔难民迁巴拉圭 | 成就页 |

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

> 以下 3 条与 yaml 完全一致，已入库（仅收 page.md 明载关系）。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| founder | League of Nations | 机构→机构 | 1930 年由国际联盟设立并负担行政开支 |
| other | Fridtjof Nansen | — | 得名于南森；延续其 1921 年在日内瓦创立的难民救援组织 |
| other | United Nations High Commissioner for Refugees | — | 1938 年设难民事务高级专员取代本办公室，该职为 UNHCR 前身 |

- 方向约定：founder（缔造者→机构）有向；other 为机构谱系关系，note 写清语义
- 对手方 name_en 用 manifest 规范名；缺失主体由 seed_person.py 自动建占位记录

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：建制、务实、乱世中的秩序
- **配色**：深紫（manifest 预分配主色 `#52307C`，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgePassport` 南森护照 — 靛蓝 `#2E4A7D`
  - `badgeConv` 1933 难民公约 — 外交青 `#0E6B5C`
  - `badgeRelief` 救援与安置 — 赭金 `#8C6A2F`
  - `badgeNobel` 1938 诺奖 — 香槟金 `#C9A227`
- **背景母题**：柔和气泡 + 低饱和的护照页网格线与印章圆环意象，呼应「证件即通行权」的设计母题

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. **封面有机构视觉**：右上角用南森护照封面图或装饰圆 + `draw=coveraccent!50` 细边框（无机构肖像照）。
2. **封面有属性标注**：顶部副标题或底部状态栏明示 `International organization | League of Nations, Geneva`，底部状态栏给出 `属性 | 主管机构 | 主要奖项` 三要素。
3. **必须有机构概览页**（替代个人身份信息页）：封面之后、核心贡献之前。左护照封面图 + 右信息网格，含至少：成立/解散年份、得名由来、总部（日内瓦）、主管机构（国际联盟）、经费来源、主要成就、核心领域。
4. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 南森的遗产 / Nansen International Office for Refugees 1930–1939 + 四色 badge + 护照封面图
02  机构概览页（★ 必做，替代身份信息页）— 左护照封面图 + 右信息网格（成立/解散、得名、总部、主管、经费、成就）
03  核心贡献概览 — 南森护照 / 1933 公约 / 亚美尼亚安置 / 萨尔难民 / 1938 诺奖
04  得名由来：南森身后的名字 (1921–1930) — 南森 1921 日内瓦创组织、1930 去世后国联设办公室承其事业
05  南森护照：证件即通行权 — 无国籍者跨国旅行的旅行证件体系
06  1933《难民公约》：一部温和的权利宪章 — 获 14 国采纳
07  亚美尼亚人的新家 (叙利亚与黎巴嫩) — 特建村落安置 4 万人、另 1 万人安置于埃里温
08  萨尔难民与巴拉圭 (1935) — 萨尔重归德国后的重新安置
09  经费与组织的现实 — 国联仅付行政开支（护照收费）、救济靠私人捐助
10  局限：第三帝国与西班牙难民 — 南森援助不适用、多国拒收（客观呈现）
11  1938 诺贝尔和平奖 — 获奖理由、机构随后解散、奖金由国联新设难民组织领取
12  延续：从高级专员到 UNHCR — 1933 设高级专员公署、1938 取代本办公室、UNHCR 前身
13  遗产：一份护照背后的人道法传统
14  结尾
```

### 第 7–8 步：版式要点与专属陷阱 【模板通用 + 人物专属】

**版式**：每页 `\newcommand{\xxxslide}{...}`；每写完一页 `make`，用 `pdftoppm` 截图检查溢出/重叠；修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

**本机构特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 创始人归属 | infobox 明载 Founder = League of Nations（国际联盟设立）；南森是**得名由来与前身组织创立者**，勿写成「南森创立了本办公室」 |
| 高级专员公署年份 | 国际联盟难民事务高级专员公署 established in 1933；1938 年「以任命一位难民事务高级专员取代本办公室」——两个年份勿混 |
| 解散与奖金 | 机构在获奖后不久解散，奖金由国际联盟新设的难民组织领取；勿写「奖金无人领取」或归入本机构名下 |
| UNHCR 表述 | page.md 明载 1938 年的高级专员是 UNHCR 的 **precursor（前身）**；勿写「本办公室后改组为 UNHCR」 |
| 援助局限 | 对第三帝国难民与西班牙内战难民「南森援助不适用」，且许多国家拒绝接收——按 page.md 客观记录，不加评价 |
| 得名书写 | 法文原名 Office International Nansen pour les Réfugiés；封面用英文名，机构概览页注法文原名 |
| 亚美尼亚安置 | 数字口径：叙利亚与黎巴嫩 specially constructed houses 安置 **40,000** 人、埃里温 **10,000** 人；勿写「共 5 万于同一地区」 |
| 政治敏感 | 涉及第三帝国、西班牙内战、萨尔公投等只作 page.md 明载的客观事实记录，不加任何评价性语句 |
| 无载禁写 | 不编造历任主席/领导人名单（正文仅书目提到 Michael Hansson 任理事会前主席，不入正文叙事）、不写年度预算数字、不从诺奖颁奖词反推关系 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Nansen passport | 南森护照 | 让无国籍者得以跨国旅行的旅行证件 |
| statelessness | 无国籍状态 | 护照服务的核心人群 |
| Refugee Convention (1933) | 1933《难民公约》 | 「a modest charter of human rights」，14 国采纳 |
| League of Nations | 国际联盟 | 本办公室的设立者与行政经费负担者 |
| High Commissioner for Refugees | 难民事务高级专员 | 1938 取代本办公室；UNHCR 前身 |
| Office International Nansen pour les Réfugiés | 南森国际难民办公室（法文原名） | 封面用英文名 |
| resettlement | 重新安置 | 叙利亚/黎巴嫩/埃里温/巴拉圭四处 |
| governing body | 理事会 | 仅书目提及 Michael Hansson 任前主席，正文勿展开 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Through the Darkness** — Audiomachine（manifest 预分配，勿改）
- **风格**: 深沉 / 穿越黑暗 / 史诗感
- **匹配理由**:
  - "Through the Darkness" 呼应本机构的时代处境——大萧条与二战前夜的欧洲，一批批无国籍者在黑暗中寻找通行权，本机构是黑暗年代里的制度性微光
  - 曲名的「穿越」感与南森护照的意象互文：一纸证件让人穿越国界与黑暗
- **本地路径**: `music_audio/inspiring-electronic/14-Trn1cSsY2t8-Audiomachine - Through the Darkness.wav` → `presentations/20th_century/Office_international_Nansen_pour_les_réfugiés/Through_the_Darkness.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Office_international_Nansen_pour_les_réfugiés/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/pages/20th_century/Office_international_Nansen_pour_les_réfugiés/images.txt` | 插图 URL（护照封面/印章/南森照） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄，勿改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |
| `MySQL/data/Office_international_Nansen_pour_les_réfugiés.yaml` | 社会关系/领域入库母本 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
