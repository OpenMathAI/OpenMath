# 和平奖得主立传提示词（OpenPeace 批次 20 · Carlos Filipe Ximenes Belo）

> 本文件是 OpenPeace 项目「诺贝尔和平奖得主立传提示词」之一，对象为个人：
> 卡洛斯·菲利佩·西门内斯·贝洛（Carlos Filipe Ximenes Belo，1996 诺贝尔和平奖共同得主）。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（一~五节）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMathAI 其他人物侧共享 GitHub）。
- **本实例**：Carlos Filipe Ximenes Belo（东帝汶天主教主教，慈幼会士）。
- **设计哲学**：和平奖得主立传必须保留**「身份信息页」（Identity / Bio 速览页）**与「事业领域」的结构化表达——这两点构成模板骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标人物**：Carlos Filipe Ximenes Belo（1948-02-03 生于葡属帝汶 Vemasse 附近 Wailakama 村，在世）
- **气质关键词**：**沉默教区的发声者、非暴力抗争的牧者、功成身退的隐修者** —— 1996 诺贝尔和平奖获奖理由：
  > "for their work towards a just and peaceful solution to the conflict in East Timor"
  > （中译照抄名录：表彰他们为公正和平地解决东帝汶冲突所做的工作）
- **设计母题**：**烛光与圣堂（candlelight）**。他在军管之下以布道与庇护行动为无声者发声——烛光隐喻黑暗中的微光与见证，是比「鸽子」更贴合其宗教身份的视觉语言。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Carlos_Filipe_Ximenes_Belo/page.md`（Wikipedia 全文 + frontmatter）
- **参考模板**：
  - 物理学家标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`physicist/presentations/cover/openphysicist_page.tex`（OpenPeace 共享封面由主控统一建，若已有 `peace/presentations/cover/` 则优先用之）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：本批已完成「事业领域 + 社会关系入库」（见第 4 / 4.5 步表格），立传时以库内与 yaml 为准，不要另起炉灶。

### 第 0 步：下载并核对数据页面 【人物专属】

- ✅ 已抓取 Wikipedia 页面到 `peace/presentations/pages/20th_century/Carlos_Filipe_Ximenes_Belo/`（四件套）
- 提取 infobox 与正文，**事实基准如下**（第一轮已核对）：
  - 生卒：1948-02-03 生于葡属帝汶（今东帝汶）Baucau 的 Vemasse 附近 Wailakama 村，在世；家中第五子
  - 家庭：父 Domingos Vaz Filipe（教师，贝洛约两岁时去世）；母 Ermelinda Baptista Filipe
  - 教育：Baucau 与 Ossu 天主教学校 → Dare 小修院（1968 毕业）→ 1969–1981 于葡萄牙天主教大学与慈幼宗座大学修哲学（1974–1976 在东帝汶与澳门实习）
  - 圣职：1974-10-06 慈幼会终身愿 → 1980-07-26 由 José Policarpo 祝圣为神父 → 1981 回东帝汶（按占领当局要求入印尼籍）→ Fatumaca 慈幼学院任教 20 个月、任院长 2 个月
  - 主教任内：1988-03-21 获委任为 Lorium 名义主教兼帝力教区宗座署理（东帝汶天主教会最高负责人）；1988-06-19 由驻印尼宗座大使 Francesco Canalini 主礼祝圣；牧徽格言 *Caritas Veritatis-Veritas Caritatis*
  - 关键行动：就职五月后布道谴责 1983 Kraras 惨案并抗议大批逮捕；海外联络行动打破世界对东帝汶暴力的无知；1989-02 致函葡萄牙总统、教宗、联合国秘书长吁请联合国主办监督东帝汶前途公投（4 月公开）；1991 Santa Cruz 惨案后在自家庇护逃亡青年并致力于查明死亡人数
  - 关键荣誉：1995 John Humphrey Freedom Award（加拿大 Rights & Democracy 颁）；1988-08-03 葡萄牙自由勋章大十字；1996-12-10 诺贝尔和平奖（与 José Ramos-Horta 共享，10 月 12 日公布）；2004 CEU Cardinal Herrera 大学荣誉博士；2010 国际葡语运动「年度葡语人物」
  - 晚年：2002-05-20 东帝汶独立后赴葡就医（自述身心俱疲）；2002-11-26 教宗若望·保禄二世接受其辞呈（时年 54 岁）；癌症治疗；2004-05 对葡国 RTP 称「把政治留给政治家」；2004-06 起在莫桑比克马普托教区任「助理本堂神父」传授理课、带青年退省；2024《纽约时报》报道仍在莫桑比克行神职
  - 争议：2022-09-28 荷兰杂志 De Groene Amsterdammer 报道两名男子指控其童年性侵；梵蒂冈证实 2019 接获指控后于 2020 施行纪律制裁（限制行动与职务、禁与未成年人接触、禁返东帝汶），2021 强化和修订
  - 关键时间线（15–20 节点）：1948 生 → 父亡 → Baucau/Ossu 就学 → 1968 小修院毕业 → 1969 赴葡 → 1974 终身愿 → 1980 祝圣神父 → 1981 回国任教 → 1983 Lopes 被撤 → 1988-03 委任 → 1988-06 祝圣主教 → 1988 谴责 Kraras → 1989 致函联合国 → 1991 庇护 Santa Cruz 青年 → 1995 Humphrey 奖 → 1996 诺奖 → 会见各国政要 → 2002 独立与辞职 → 2004 赴莫桑比克 → 2020 梵蒂冈制裁 → 2022 指控报道

### 第 1 步：建立目录 【模板通用】

- `peace/presentations/20th_century/Carlos_Filipe_Ximenes_Belo/` 已在（提示词所在），建 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 参照 OpenPeace 已完成成品或 Kenneth_G_Wilson/Makefile，设置 `MAIN=Carlos_Filipe_Ximenes_Belo_zh`、`VIDEO_NAME` 同名

### 第 3 步：收集图片 【人物专属】

- 从 page.md 图片链接（infobox 有 2016 年贝洛照片）下载 500px 版本到 `images/`，`file` 验证；404 则用 Commons `Special:FilePath` 回退；再失败用装饰圆占位

### 第 4 步：事业领域梳理（已入库） 【模板通用，人物专属内容】

**Belo 的事业领域（按 rank 排序，与 yaml/DB 一致）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | peace advocacy | 和平倡导 | 1996 诺奖核心：为东帝汶寻求公正和平解决 | 诺奖页 |
| 1 | self-determination | 民族自决 | 1989 致函联合国吁办公投 | 致函页 |
| 2 | human rights | 人权 | 谴责惨案、查明伤亡、庇护青年 | 行动页 |
| 3 | reconciliation | 和解 | 和平与和解的不懈追求 | 诺奖页 |
| 4 | pastoral ministry | 牧灵工作 | 帝力教区署理与晚年马普托传教 | 晚年页 |

### 第 4.5 步：社会关系（已入库） 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | José Ramos-Horta | 无向 | 1996 诺贝尔和平奖共同得主 |
| influence | Martinho da Costa Lopes | Lopes→Belo | 前任宗座署理（1983 被撤），贝洛继其路线 |
| parent-child | Domingos Vaz Filipe | 父→子 | 教师，贝洛幼年时去世 |
| parent-child | Ermelinda Baptista Filipe | 母→子 | — |

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：沉静、悲悯、暗中持灯
- **配色**：主色深海军蓝 `#16324F`（manifest 预分配，勿改）+ 诺奖香槟金 `C9A227` + 四分类色：
  - `badgePeace` 和平倡导 — 靛蓝 `#4C5FD5`
  - `badgeRights` 人权行动 — 青绿 `#0E7C7B`
  - `badgeFaith` 圣职牧灵 — 琥珀 `#E07B30`
  - `badgeTimor` 东帝汶事业 — 玫瑰 `#C4204F`
- **背景母题**：柔和气泡（稀疏大块实心圆，四种大小错落），呼应「烛光与圣堂」母题——暖色圆点如圣堂中的烛光散布深色底面

### 第 6 步：规划幻灯片序列 【人物专属，可微调】

```
00  OpenPeace 项目首页（\input 共享封面）
01  封面 — 沉默教区的发声者 / Carlos Filipe Ximenes Belo 1948– + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地、父母、教育、圣职年表、
    任职、主要荣誉、核心事业）
03  事业概览 — 和平倡导 / 民族自决 / 人权 / 和解 / 牧灵工作
04  早年：Wailakama 男孩 (1948–1968) — 父亲早逝、Baucau/Ossu 就学、Dare 小修院
05  葡萄牙求学与慈幼会 (1969–1981) — 修哲学、终全身愿、澳门实习、1980 祝圣
06  回到被占领的故乡 (1981–1988) — 印尼籍、Fatumaca 任教、Lopes 被撤后空缺五年
07  宗座署理：临危受命 (1988) — 委任与祝圣、牧徽格言 Caritas Veritatis
08  发声的教区 (1988–1991) — 谴责 Kraras 惨案、海外联络行动
09  致函联合国 (1989) — 吁请公投、"dying as a people and a nation"
10  Santa Cruz 之夜 (1991) — 庇护逃亡青年、查明死亡人数
11  1996 诺贝尔和平奖 — 与 Ramos-Horta 共享、Oslo 12-10 领奖、会见各国政要
12  荣誉与认可 — Humphrey 1995、自由勋章大十字 1988、荣誉博士 2004、葡语人物 2010
13  功成身退 (2002–2004) — 独立后辞职、赴葡就医、马普托的「助理本堂神父」
14  争议与晚年 — 2020 梵蒂冈纪律制裁与 2022 指控报道（客观事实记录）＋ 2024 近况
15  遗产：一个主教的非暴力见证
16  结尾
```

### 第 7–8 步：版式要点 + 人物专属陷阱表 【模板通用 + 人物专属】

**Belo 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 姓名写法 | 全名 Carlos Filipe Ximenes Belo（SDB=慈幼会缩写），常称 Carlos Belo 或 Ximenes Belo——篇内统一一种写法并在首次出现注明 |
| 头衔措辞 | 他是帝力教区**宗座署理**（apostolic administrator）兼 Lorium **名义主教**，不是帝力正权主教——勿升格头衔 |
| 诺奖「共同」 | 1996 与 Ramos-Horta **共同**获奖，理由句用 "their work"（their=两人）；公布日 10-12、颁授日 12-10 两个日期勿混 |
| 生年噪声 | frontmatter date_of_birth 有 1948-02-03 与 1948-01-01 两值，以正文/infobox **1948-02-03** 为准 |
| 任职前史 | 前任宗座署理 Martinho da Costa Lopes 1983 被撤后职位空缺，1988 才委任贝洛——勿写成「直接继任」或「1983 年上任」 |
| Kraras 布道 | 谴责的是 **1983 年** Kraras 惨案，布道发生在就职五月后（1988 年）——事件年与言论年勿混 |
| 国籍 | 出生于葡属帝汶、1981 年按占领当局要求入印尼籍、frontmatter 国籍 Timor-Leste——三者并列客观陈述，勿单选 |
| 性侵指控 | 2022 荷兰杂志报道 + 梵蒂冈 2020/2021 纪律制裁为 page.md 明载事实，只作客观记录并列梵蒂冈说法（「他接受了规则」），不加评价不引申 |
| 政治红线 | 涉及印尼占领、独立公投等只作 page.md 明载客观事实记录，不加评价性语句；引语只录 page.md 有英文原文者 |
| 引语 | 可用引语：1989 信中 "dying as a people and a nation"、2004 "decided to leave politics to politicians"、Maputo 自述 "I do pastoral work..."——除此之外勿杜撰 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| apostolic administrator | 宗座署理 | 非正权主教 |
| titular bishop of Lorium | Lorium 名义主教 | 荣衔，Lorium 为罗马近郊古址 |
| Salesians of Don Bosco | 慈幼会 | SDB 缩写 |
| ordination | 祝圣为神父 | 1980-07-26 |
| episcopal consecration | 主教祝圣礼 | 1988-06-19 |
| apostolic nuncio | 宗座大使 | Canalini 驻印尼 |
| Santa Cruz massacre | Santa Cruz 惨案 | 1991 帝力 |
| Kraras massacre | Kraras 惨案 | 1983 |
| referendum | 公投 | 1989 致函诉求 |
| Caritas Veritatis | 真理之爱 | 牧徽格言，拉丁语 |
| John Humphrey Freedom Award | 汉弗莱自由奖 | 1995 加拿大 |
| Order of Liberty | 自由勋章 | 葡萄牙，大十字 |

---

## 四、背景音乐选择 【人物专属，manifest 预分配勿改】

- **选定曲目**: **New Lands** — Alex-Productions
- **风格**: 开阔 / 希望 / 新生
- **匹配理由**: 「新地」匹配东帝汶民族自决的最终实现与其后半生远赴莫桑比克重新开始的人生轨迹；开阔感匹配其海外联络行动把小岛的声音带向世界；希望感匹配非暴力抗争的底色
- **本地路径**: `music_audio/alex-productions/74-oK8HN0FsZmc-New-Lands.wav`
- **时长**: 与 16 页成片用 ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Carlos_Filipe_Ximenes_Belo/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄勿改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆（0–11 节） |
| `MySQL/data/Carlos_Filipe_Ximenes_Belo.yaml` | 领域/关系入库母本 |
| `music_audio/curated_tracks.md` | BGM 曲库 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
