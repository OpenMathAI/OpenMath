# 文学家立传提示词（OpenLiterature 实例：Grazia Deledda）

> 本文件是 OpenLiterature 的「文学家立传提示词」人物专属实例，以 Grazia Deledda（1926 诺贝尔文学奖，撒丁岛书写者）为对象。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`；文学家适配：无公式框，以**代表作书影 / 名句引文框 / 意象图式**替代。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMath/OpenPhysicist 侧共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Grazia Maria Cosima Damiana Deledda（格拉齐亚·黛莱达）。
- **设计哲学**：文学家立传与物理学家立传共享「身份信息页（Identity / Bio 速览页）」骨架；差异在于以**文学领域表**替代研究领域表、以**引文框/书影/意象图式**替代公式框，务必保留这两点。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Grazia Deledda（1871-09-27 ~ 1936-08-15，享年 64 岁）
- **气质关键词**：**撒丁岛的女儿、真实主义的继承者、贫困与宿命的书写者** —— 1926 诺贝尔文学奖获奖理由：
  > "for her idealistically inspired writings which with plastic clarity picture the life on her native island and with depth and sympathy deal with human problems in general"
  > （官方中译，照 `literature/generate_20th_century_list.py` CITATION_ZH，禁止改写）：表彰其理想主义启迪下的写作，以鲜明的笔触描绘故乡岛屿的生活，并以深度与同情处理普遍的人类问题
- **设计母题**：**风中的芦苇（Canne al vento）**。芦苇易折而不倒、随风暴俯仰却根扎岩土——正合 Deledda 笔下撒丁岛人物在贫困、孤独与宿命面前的沉默坚韧；背景母题可用海岸芦苇丛、剪影式山丘与柔和暮色圆。
- **本地数据源**：`literature/presentations/pages/20th_century/Grazia_Deledda/page.md`（Wikipedia 全文，事实基准已核对）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Grazia_Deledda
- **肖像**：第 0 步待下载（images.txt 有 infobox 照 `Grazia_Deledda.jpg`，1926 年像）

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报；数据库同步包含「文学领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL），与 Beamer 立传并行。

### 第 0 步：事实基准（人物专属，第一轮已核对）

- 生卒：1871-09-27 生于撒丁岛努奥罗（Nuoro）～ 1936-08-15 逝于罗马（乳腺癌），享年 64 岁
- 国籍：意大利王国（撒丁岛出身，意大利口径）
- 家庭：父 Giovanni Antonio Deledda、母 Francesca Cambosu，七个兄弟姐妹中排行第四；丈夫 Palmiro Madesani（1900 年结婚，财政部职员），长子 Sardus（1901）、次子 Francesco "Franz"（1904）
- 教育：仅小学（当时最低年限），私塾家庭教师后自学文学——"homeschooling" 口径，勿写「大学求学」
- 文学师承与影响（page.md 明载）：Verga 的真实主义（verism）影响明显，兼有 D'Annunzio 的颓废主义（decadentism）影响，但其文体 "not so ornate"（不如后者华丽）
- 任职/流亡：无流亡经历；1900 年婚后移居罗马，写作生涯在努奥罗与罗马两地展开
- 关键荣誉：Nobel Literature 1926（瑞典学院院士 Henrik Schück 提名）；第一位获诺奖的意大利女性，继 Selma Lagerlöf（1909）之后第二位女性得主
- 核心作品与贡献（4–6 条）：
  1. *Fior di Sardegna*（1892，首部长篇）
  2. *Elias Portolu*（1903，商业与批评双成功的成名作）
  3. *Cenere*（1904，灰烬；1916 改编默片，Eleonora Duse 唯一一次银幕出演）
  4. *Canne al vento*（1913，风中的芦苇；她最受欢迎的作品）
  5. *La madre*（1920，英文译名 *The Woman and the Priest* / *The Mother*）
  6. *La chiesa della solitudine*（1936，绝笔）与 *Cosima*（1937 遗作，半自传）
- 关键时间线（15–20 节点）：
  1. 1871-09-27 生于努奥罗中产家庭
  2. 13 岁第一篇故事发表于当地期刊（老师鼓励投稿）
  3. 1888–1889 早期作品刊于时尚杂志 *L'ultima moda*
  4. 1890 首部短篇集 *Nell'azzurro*（Trevisani 出版）
  5. 1892 首部长篇 *Fior di Sardegna*
  6. 1894 短篇集 *Racconti sardi* 与民俗研究 *Tradizioni popolari di Nuoro*
  7. 1896 *La via del male*
  8. 1899-10 在卡利亚里结识 Palmiro Madesani
  9. 1900 结婚并移居罗马；*Il vecchio della montagna*
  10. 1901 长子 Sardus 出生；此后约每年一部长篇的高产期
  11. 1903 *Elias Portolu* 成名
  12. 1904 *Cenere*；1904 次子 Franz 出生
  13. 1908 *L'edera*（常春藤）
  14. 1913 *Canne al vento*（代表作）
  15. 1916 *Cenere* 改编默片（Duse 主演）
  16. 1919 为女性杂志 *Lidel* 撰稿
  17. 1926 获诺贝尔文学奖；初闻反应 "Già?"（"Already?"）
  18. 1930 *La casa del poeta*；1933 *Sole d'estate*（健康恶化仍写作，笔调转乐观）
  19. 1936-08-15 卒于罗马；*La chiesa della solitudine* 同年出版
  20. 1937 遗作 *Cosima* 出版

### 第 1 步：建立目录 【模板通用】

- 在 `literature/presentations/20th_century/` 下创建 `Grazia_Deledda/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 参照同侧已成品目录的 Makefile，设置 `MAIN=Grazia_Deledda_zh`、`VIDEO_NAME=Grazia_Deledda_zh`

### 第 3 步：收集图片 【人物专属】

- 肖像：待下载（Commons `Grazia_Deledda.jpg`，1926 年像；下载后 `file` 验证）
- 备选插图：Pincio 的 Amelia Camboni 半身像（page.md 有图）

### 第 4 步：文学领域梳理 + 入库 【模板通用，人物专属内容】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | verismo | 真实主义 | 承 Verga 一脉，page.md 明载其影响 | 核心页 |
| 1 | sardinian literature | 撒丁岛文学 | 故乡岛屿的生活、习俗与地理 | 主题页 |
| 2 | novel | 长篇小说 | 约每年一部的高产长篇 | 作品页 |
| 3 | short story | 短篇小说 | *Nell'azzurro*、*Racconti sardi* 等 | 早年页 |
| 4 | decadentism | 颓废主义 | D'Annunzio 影响，风格较收敛 | 主题页 |

#### 4.1 入库操作（yaml 见 `MySQL/data/Grazia_Deledda.yaml`）

- 新建 people 主记录（`name_en='Grazia Deledda'`，qid=Q7728），`primary_occupation='writer'`、`has_social_data=1`
- 关联职业 writer(rank 0)/novelist/playwright；国籍 Italy
- 5 个领域写入 `person_field`（缺失领域先在 `fields` 建字典项）
- 校验：`SELECT f.name_en, pf.rank FROM person_field pf JOIN fields f ON f.id=pf.field_id WHERE pf.person_id=<id> ORDER BY pf.rank`

### 第 4.5 步：社会关系梳理 + 入库 【模板通用，人物专属内容】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Palmiro Madesani | 无向 | 1900 年结婚，财政部职员，随夫移居罗马 |
| influence | Giovanni Verga | 无向 | 真实主义（verismo）影响明显，page.md 明载 |
| influence | Gabriele D'Annunzio | 无向 | 颓废主义影响（偶见），风格较不华丽 |
| influence | Sergio Atzeni | 无向 | 受其影响的撒丁作家，「撒丁文学春天」代表 |
| influence | Giulio Angioni | 无向 | 受其影响的撒丁作家，「撒丁文学春天」代表 |
| influence | Salvatore Mannuzzu | 无向 | 受其影响的撒丁作家，「撒丁文学春天」代表 |

#### 4.5.1 入库操作

- 以 `name_en='Grazia Deledda'` 为中心写入 `person_relation`；influence 无向；缺失人物建占位（不编造 qid）
- ⚠️ Eleonora Duse 仅是 *Cenere* 电影改编主演，非私人交谊，**不入库**

### 第 5 步：设计配色方案 【人物专属色彩】

- **气质**：沉静、泥土色、海岛暮光
- **配色**：深海蓝（主色，预分配 `#2A4B7C`）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeA` verismo 真实主义 — 橄榄绿 `#4E5D42`
  - `badgeB` sardinian literature 撒丁岛文学 — 赭石 `#B0713A`
  - `badgeC` novel 长篇小说 — 石板青 `#3E6B6B`
  - `badgeD` short story 短篇小说 — 玫瑰灰 `#9C5A63`

### 5.1 文学家格式硬要求 【模板通用，★ 必须满足】

1. 封面有头像（右上角肖像 + 细边框 + 姓名小字注）。
2. 封面明示国籍；底部状态栏 `国籍 | 代表作 | 主要奖项` 三要素。
3. 必须有身份信息页（封面后、核心贡献前）：左头像 + 右信息网格（生卒、本名、国籍、出生地、家庭、定居地、荣誉、核心领域），事实取自 page.md infobox，不得杜撰。
4. 品牌口径统一：结尾页底部品牌标注 `OpenMathAI`；引号用半角 `" "`。
5. 无公式框——以**代表作书影 / 名句引文框 / 意象图式**替代（本篇用「芦苇意象图式」页）。

### 第 6 步：规划幻灯片序列 【人物专属】

```
00  OpenLiterature 项目首页
01  封面 — 撒丁岛的女儿 / Grazia Deledda 1871–1936 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格
03  核心贡献概览 — verismo / 撒丁岛书写 / 长篇高产 / 遗作
04  努奥罗童年 (1871–1900) — 小学后自学、13 岁发表、L'ultima moda
05  罗马岁月：婚姻与高产 (1900–1913) — Madesani、Elias Portolu、Cenere
06  Canne al vento：风中的芦苇（代表作书影 + 引文框）
07  意象图式页 — 撒丁岛：贫困、孤独、罪与宿命
08  1926 诺贝尔奖 — Schück 提名、"Già?"、Mussolini 赠照（一句带过）
09  晚年与遗作 (1930–1937) — 病中写作、La chiesa della solitudine、Cosima
10  遗产 — 撒丁文学春天、Museo Deleddiano、Google Doodle 2017
11  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照成品 `\profileslide`。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make`，`pdftoppm` 截图检查溢出/重叠；修复优先级：删装饰条 → 缩 inner sep → 缩字号 → 减行距 → 调坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Deledda 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 生卒双值 | frontmatter 生日有 1871-09-27 与 1871-11-11 两值、卒日 08-15/08-16 两值，以 infobox 09-27 / 08-15 为准 |
| 获奖理由 | 只用官方原文与 CITATION_ZH 中译，勿意译改写；"plastic clarity" 勿译成「如画」 |
| 女性第一/第二 | 第一位意大利女性诺奖得主；第二位女性得主（继 1909 Lagerlöf）——page.md 明载，勿写「世界第一位」 |
| Mussolini | 赠签名照一事仅客观一句，不展开政治叙事、不作评价 |
| Duse | 仅电影改编合作，无私人交谊记载，勿建关系页 |
| 引语红线 | 全文仅 "Già?"（"Already?"）有英文原注可引；勿杜撰其它「原话」 |
| 影响者 | Verga/D'Annunzio 影响为 page.md 明载，但「文体不如后者华丽」勿删；勿夸大为「师承」 |
| 女性主义 | page.md 明文 she has not been considered a feminist writer，勿拔高 |
| 代表作年份 | *Elias Portolu* 商业成功 1903；作品全目中该条误标 1900，以正文 1903 为准 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| verismo | 真实主义 | 与 Verga 关联，非「现实主义」泛称 |
| decadentism | 颓废主义 | 与 D'Annunzio 关联 |
| *Canne al vento* | 《风中的芦苇》 | 1913，代表作 |
| *Cenere* | 《灰烬》 | 1904；1916 默片改编 |
| *Cosima* | 《科西玛》 | 1937 遗作，半自传 |
| Sardinian Literary Spring | 撒丁文学春天 | Atzeni/Angioni/Mannuzzu 等后辈 |
| Nuoro | 努奥罗 | 出生城镇；故居今为 Museo Deleddiano |

---

## 四、背景音乐选择 【人物专属，预分配】

- **选定曲目**: **With Me**
- **风格**: 温情 / 陪伴 / 舒缓
- **匹配理由**:
  - "陪伴" 匹配其叙事内核——丈夫 Madesani 与她罗马岁月的同舟共济，以及《风中的芦苇》中家族在风暴中的相互扶持
  - "温情" 匹配官方获奖理由中的 "with depth and sympathy deal with human problems in general"（以深度与同情处理人类问题）
  - 舒缓节奏匹配撒丁岛慢镜头式地理书写，与芦苇意象的呼吸感一致
- **本地路径**: `music_audio/` 对应曲目拷贝至 `literature/presentations/20th_century/Grazia_Deledda/With Me.wav`
- **时长**: 按ffmpeg `-shortest` 自动对齐页数 × 7 秒

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Grazia_Deledda/page.md` | 本地 Wikipedia 正文（事实基准） |
| `literature/presentations/pages/20th_century/Grazia_Deledda/metadata.json` / `images.txt` | 辅助属性 + 图片线索 |
| `literature/generate_20th_century_list.py` | 官方获奖理由中译 CITATION_ZH（禁止改写） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构母本 |
| `MySQL/data/Kenneth_G_Wilson.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
| `music_audio/curated_tracks.md` | BGM 曲库标签对照 |

> **开始执行。每完成一步汇报。最重要的事：事实只写 page.md 明载内容。**
