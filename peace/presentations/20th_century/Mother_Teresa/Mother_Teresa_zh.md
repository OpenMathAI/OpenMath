# 和平奖得主立传提示词（OpenPeace：Mother Teresa / 特蕾莎修女）

> **本文件是 OpenPeace 的「和平奖得主立传提示词」**，以 Mother Teresa（1979 诺贝尔和平奖，加尔各答的贫病者救助者）为实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节母本）。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **模板来源**：物理学家侧标杆 Kenneth G. Wilson 提示词 + Beamer 立传骨架；和平奖侧沿用「身份信息页 + 领域结构化」骨架。
- **本实例**：Mother Teresa / Saint Teresa of Calcutta（特蕾莎修女，本名 Anjezë Gonxhe Bojaxhiu）。
- **设计哲学**：和平奖得主立传与科学家立传的核心差异，在于「事业领域」以**救助对象与行动网络**呈现（而非学科领域），且必须保留「身份信息页」；本篇以「仁爱传教会」的组织成长为主轴。

---

## 二、背景信息 【人物专属】

- **目标人物**：Mother Teresa（1910-08-26 ~ 1997-09-05，享年 87 岁）
- **姓名口径**：本名 Anjezë Gonxhe Bojaxhiu；教名 Teresa 取自里修的德兰（Thérèse de Lisieux，取西班牙拼法）；1979 获奖时通称 Mother Teresa；2016 封圣为 Saint Teresa of Calcutta。
- **官方获奖理由**（照抄名录 `OpenPeace_20th_Century_Nobel_Laureates.md`，禁止改写）：
  > 英文原文（nobel_peace_citations.json，清理引注噪声后）："for her work for bringing help to suffering humanity."
  > 中译：表彰她为救助苦难人类所做的工作
- **气质关键词**：**最贫穷者中的最贫穷者、临终者的守护人、白纱蓝边的行走修会**。
- **设计母题**：**微小的善行（do small things with great love）**——白纱上的两道蓝边、一粒米与一口饭、临终者安详的最后一刻；视觉上用「蓝边白纱」的极简双色作为贯穿全篇的母题。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Mother_Teresa/page.md`（Wikipedia 全文 + frontmatter，QID Q30547）。
- **参考模板**：
  - 物理学家标杆成品：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 和平奖项目首页模板：`peace/presentations/cover/`（统一 `\input`）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步向我汇报，遇到歧义先征求我的意见再继续。
> **数据库同步要求**：包含「研究领域/事业领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL）。

### 第 0 步：事实基准（已核对 page.md，禁止杜撰） 【人物专属】

- 生卒：1910-08-26 生于奥斯曼帝国科索沃州首府斯科普里（今北马其顿首都）～ 1997-09-05 逝于印度加尔各答，享年 87 岁；次日受洗，她自认 08-27 才是「真正的生日」。
- 国籍：阿尔巴尼亚族（名录口径 Albania）；生于奥斯曼帝国，1929 赴印度，1948 取得印度公民身份；frontmatter 亦载 India。家族：科索沃阿尔巴尼亚人家庭，父系源自 Mirdita。
- 家庭：父 Nikollë Bojaxhiu（1919 疑被塞尔维亚特工毒杀，时年她约 8 岁）；母 Dranafile Bojaxhiu（Bernai）；她是家中最小的孩子；恩维尔·霍查统治期间被视为「梵蒂冈的危险代理人」，被拒探亲，母与妹均死于霍查时期。
- 教育：无世俗大学学历；1928 入爱尔兰都柏林 Rathfarnham 洛雷托修道院学英语（为赴印度传教做准备）；1929 大吉岭初学期，习孟加拉语并任教。
- 任职：Sisters of Loreto（1928–1948）；加尔各答恩塔利洛雷托修道院学校任教近 20 年，1944 任校长；1950 起任仁爱传教会总会长（至 1997-03-13 辞任），继任者 Nirmala Joshi。
- 关键荣誉：Ramon Magsaysay Award 1962；Pope John XXIII Peace Prize 1971（首届）；Pacem in Terris Award 1976；Balzan Prize 1978；**Nobel Peace Prize 1979**；Bharat Ratna 1980（印度最高平民荣誉）；Order of Merit 1983；美国荣誉公民 1996-11-16；宣福 2003-10-19（教宗若望保禄二世）；封圣 2016-09-04（教宗方济各）。
- 核心事业清单：
  1. 1950-10-07 获梵蒂冈批准创立**仁爱传教会**（Missionaries of Charity），会服为两道蓝边的白纱，第四愿「全心全意无偿服务最贫穷者中的最贫穷者」。
  2. 1952 把废弃印度教庙宇改建为 **Kalighat 临终者之家**（Nirmal Hriday，纯洁之心之家）：按信仰尊严送终。
  3. 麻风病收容（Shanti Nagar，和平之城）与全城麻风外展诊所；1955 开办 Nirmala Shishu Bhavan 儿童之家。
  4. 国际扩张：1965 委内瑞拉首设海外分会 → 至 1997 遍及逾 100 国、517 处机构，姐妹逾 4000 人。
  5. 1982 贝鲁特围城中斡旋临时停火，救出前线医院 37 名儿童。
  6. 1984 与 Joseph Langford 创立仁爱传教会神父会（Missionaries of Charity Fathers）。
- 关键时间线（19 节点）：1910 生于斯科普里 → 1919 父疑遭毒杀 → 1928 离家赴爱尔兰洛雷托会 → 1929 抵印度（大吉岭）→ 1931-05-24 初愿 → 1937-05-14 终身愿（恩塔利，取号 Mother）→ 1943 孟加拉大饥荒 → 1944 任校长 → 1946-08 直接行动日教派暴力 → 1946-09-10 火车「蒙召中的蒙召」→ 1948 走出修院进入贫民窟（获基本医疗训练，入印度籍）→ 1950-10-07 创仁爱传教会 → 1952 Kalighat 临终者之家 → 1955 儿童之家 → 1963 兄弟会成立 → 1965 海外首站委内瑞拉 → 1969 BBC 纪录片成名 → 1979 诺贝尔和平奖（拒设宴，192,000 美元捐印度贫民）→ 1982 贝鲁特救童 → 1997-09-05 逝于加尔各答（印度国葬）→ 2003 宣福 / 2016-09-04 封圣。
- 可用引语（仅限 page.md 载有英文原文者）：「By blood, I am Albanian. By citizenship, an Indian. …As to my heart, I belong entirely to the Heart of Jesus.」「Go home and love your family.」「A beautiful death is for people who lived like animals to die like angels—loved and wanted.」等，不得从他处补引。

### 第 4 步：事业领域梳理 + 入库 【人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | humanitarian aid | 人道救助 | 服务「最贫穷者中的最贫穷者」，1979 诺奖核心 | 核心页 |
| 1 | poverty relief | 济贫 | 加尔各答贫民窟学校、施食处、收容网络 | 核心页 |
| 2 | hospice care | 临终关怀 | Kalighat 临终者之家（Nirmal Hriday） | 核心页 |
| 3 | leprosy care | 麻风病救助 | Shanti Nagar 与麻风外展诊所 | 核心页 |
| 4 | catholic missionary work | 天主教传教 | 洛雷托会修女 → 仁爱传教会创始人 | 早年页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致） 【人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| founder | Missionaries of Charity | 创始人→机构 | 1950-10-07 获梵蒂冈批准创立，任总会长至 1997 |
| parent-child | Nikollë Bojaxhiu | 无向 | 父亲，科索沃阿尔巴尼亚人，1919 疑被毒杀 |
| parent-child | Dranafile Bojaxhiu | 无向 | 母亲，霍查时期被拒探亲 |
| colleague | Joseph Langford | 无向 | 1984 共同创立仁爱传教会神父会 |
| colleague | Nirmala Joshi | 无向 | 1997-03-13 继任仁爱传教会总会长 |
| colleague | Malcolm Muggeridge | 无向 | 1969 BBC 纪录片 Something Beautiful for God 使其成名 |
| colleague | Navin Chawla | 无向 | 授权传记作者，1992 出版 |
| colleague | Pope John Paul II | 无向 | 1983 会面时心脏病发，2003 为其宣福 |
| influence | Francis of Assisi | 无向 | 页面明载敬慕方济各并受方济各灵修影响 |
| influence | Thérèse de Lisieux | 无向 | 取教名 Teresa 致敬其主保 |
| controversy | Christopher Hitchens | 无向 | 1994 纪录片 Hell's Angel 及其后著述的批评者 |

> 入库：`cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 seed_person.py data/Mother_Teresa.yaml`；校验 has_social_data=1、fields=5、relations=11。

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **主色**：`#1B4D3E`（manifest 预分配，深绿——仁爱、平静、加尔各答街头的一袭白纱绿意），勿改。
- **辅助**：诺奖香槟金 `C9A227` + 四分类色：
  - `badgeA` 人道救助 — 蓝边白纱蓝 `#1F5C8B`
  - `badgeB` 济贫 — 赭土 `#8C5A2B`
  - `badgeC` 临终关怀 — 暖金 `#C9A227`
  - `badgeD` 传教使命 — 深绿 `#1B4D3E`
- **背景母题**：柔和圆点（白纱蓝边意象：白底上稀疏细蓝描边圆圈，四档大小错落）。

### 第 6 步：规划幻灯片序列（12 页规划）

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 最贫穷者中的最贫穷者 / Mother Teresa 1910–1997 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒/本名/国籍/修会/任职/荣誉/核心事业）
03  核心事业概览 — 仁爱传教会 / 临终之家 / 麻风救助 / 国际网络
04  早年：斯科普里的 Anjezë (1910–1928) — 阿尔巴尼亚家庭、父亡、12 岁立志
05  洛雷托岁月 (1928–1948) — 爱尔兰学英语、大吉岭初愿、恩塔利终身愿与执教
06  蒙召中的蒙召 (1946–1950) — 火车启示、入印度籍、1950 创会
07  仁爱传教会：白纱与第四愿（核心贡献页）
08  Kalighat 与 Shanti Nagar — 临终者之家与麻风救助
09  走向世界 (1965–1997) — 委内瑞拉首站、百余国网络、贝鲁特救童
10  荣誉与认可 — Magsaysay 1962 · Nobel 1979 · Bharat Ratna 1980 · 封圣 2016
11  争议与回应 — 批评（医疗条件/镇痛不足）与辩护（Chawla/Pierick），只列事实不评判
12  遗产：封圣与国际慈善日（9-05）
13  结尾
```

### 第 7–8 步：版式要点 + 本篇专属陷阱表 【模板通用 + 人物专属】

| 陷阱 | 说明 |
|------|------|
| 国籍口径 | 名录口径 **Albania**（生于奥斯曼帝国斯科普里），封面/状态栏写 Albania；正文可注「后入印度籍」，勿把 Albania 改成 India 或 North Macedonia |
| 本名拼写 | Anjezë Gonxhe Bojaxhiu（非 Agnes/Agnesa Bojaxhiu）；教名 Teresa 取自里修的德兰、因重名改用西班牙拼法 |
| 生日口径 | 出生 1910-08-26，她自认 08-27（受洗日）为「真正的生日」，两说并列须注明 |
| 诺奖理由 | 官方原文 "for her work for bringing help to suffering humanity."，勿写成颁奖词之外的转述 |
| 拒设宴 | 拒绝 conventional ceremonial banquet、192,000 美元宴席费捐印度贫民——数字勿写错 |
| 政治敏感 | 涉阿尔巴尼亚霍查政权、印度教右翼（RSS/Bhagwat）、堕胎立场、Charles Keating 等内容一律**只作 page.md 明载的客观事实记录**，不加评价性语句；伊斯兰/印度教仪式描述照原文直译 |
| 引语红线 | 只引 page.md 载有英文原文的句子；「Where is my faith?」等灵性黑暗期信件引文可用但须标注出自私人信件 |
| 批评内容 | Larivée 等三人论文与 Hitchens/Chatterjee 的批评、Chawla/Pierick 的辩护双方并列，禁止单侧叙事；McGuire 事件只写「为其辩护→后被判罪→引发批评」链条 |
| 同名区分 | 勿与 2003 意大利电视剧集《Mother Teresa of Calcutta》演员、2025 电影《Mother》等影视条目混淆 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Missionaries of Charity | 仁爱传教会 | 勿译「慈善传教士」 |
| Nirmal Hriday | 纯洁之心之家（Kalighat 临终者之家） | Nirmal Hriday 直译 |
| Shanti Nagar | 和平之城（麻风病收容） | 勿与地名混淆 |
| the poorest of the poor | 最贫穷者中的最贫穷者 | 第四愿核心语 |
| call within a call | 蒙召中的蒙召 | 1946-09-10 火车体验 |
| Sisters of Loreto | 洛雷托修女会 | 勿与圣母访亲会混淆 |
| beatification / canonization | 宣福 / 封圣 | 2003 / 2016 两步勿混 |
| Kalighat | 迦梨迦特（加尔各答地名） | 亦是画派名，勿混 |
| feat day | 瞻礼日 | 9 月 5 日 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**: **Nostalgia** — Alex-Productions（manifest 预分配，勿改）
- **风格**: 怀旧 / 温情 / 纪录片
- **匹配理由**: 平实、克制的叙事节奏匹配其一生「微小善行的累积」——不渲染英雄史诗，而是斯科普里 → 大吉岭 → 加尔各答街头的近半世纪守望；结尾落在封圣与遗产，怀旧曲式正合回望。
- **本地路径**: `music_audio/alex-productions/86-5ETNuoDcBg4-Nostalgia.wav` → `presentations/20th_century/Mother_Teresa/Nostalgia.wav`

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Mother_Teresa/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 名录与官方获奖理由中译 |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆（0–11 节母本） |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 幂等入库引擎 |

> **开始执行。每完成一步向我汇报。**
> **最重要的事：事实全部锚定 page.md，无载禁写。**

---

## 六、第 1–3 步补充（模板通用） 【模板通用骨架】

### 第 1 步：建立目录

- 在 `peace/presentations/20th_century/` 下创建 `Mother_Teresa/` 与 `images/`（提示词本文件已就位）。

### 第 2 步：复制 Makefile

- 复制同目录已立传成品的 `Makefile`（或标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`），设置 `MAIN=Mother_Teresa_zh`、`VIDEO_NAME=Mother_Teresa_zh`。

### 第 3 步：收集图片 【人物专属】

- **肖像**：`pages/Mother_Teresa/images.txt` 中未见单人肖像（首条为签名图）；优先用 Wikipedia REST API `page/summary/Mother_Teresa` 查 infobox 原图名（infobox 为 1995 年照片），Commons `Special:FilePath/<文件名>?width=600` 下载 500px；404/HTML 则装饰圆占位（主色描边）。
- **插图备选**（images.txt 有 URL 的直接用，250px 改 500px）：
  - `Missionaries_of_Charity_Mother_House.jpg`（加尔各答母院）
  - `Sisters_of_Charity.jpg`（蓝边白纱姐妹合影）
  - `Nirmal_Hriday_facade.jpg`（临终者之家外观，2007）
  - `Memorial_house_of_Mother_Teresa.jpg`（斯科普里纪念馆）
- curl 加 `-A "Mozilla/5.0"`，下载后 `file` 验证为真图。

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注；装饰圆占位时同样位置与尺寸。
2. **封面有国籍**：顶部副标题或底部状态栏明示 Albania；底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**：封面之后、核心事业之前；左头像 + 右信息网格，至少含生卒/本名/国籍/修会/任职/主要荣誉/核心事业，事实取自 page.md infobox，不得杜撰。
4. **品牌口径统一（共享 GitHub）**：结尾页底部品牌标注统一写 `OpenMathAI`；引号用半角 `" "`；共享封面 `\input` 继承，子 deck 不重复。

---

## 七、执行清单（Checklist） 【模板通用】

1. 通读 `pages/Mother_Teresa/page.md` 全文（本文件第 0 步已核对，执行时复核即可）。
2. 建目录 + 复制 Makefile + 下载肖像/插图（`file` 验证）。
3. 复制 BGM：`music_audio/alex-productions/86-5ETNuoDcBg4-Nostalgia.wav` → 目录内 `Nostalgia.wav`。
4. 按 §4 领域表 + §4.5 关系表核对已入库 DB 字段（fields=5 / relations=11，勿改）。
5. 编写 Beamer 源码（每页 `\newcommand{\xxxslide}`，骨架参照标杆成品 tex）。
6. 编译循环：0 error、vbox ≤ 10pt、hbox ≤ 50pt；每写完一页即 make + `pdftoppm` 目检。
7. 页数对账：按 §6 规划逐帧核对（缺帧/合并帧都要能对上页数）。
8. 引语逐条核对 §0 白名单；无原文一律转述。
9. 陷阱表逐条自查（尤其国籍口径与政治敏感红线）。
10. `make images && make video` 出片后，提示词回写 Review 备注（肖像来源/事实修正）。

