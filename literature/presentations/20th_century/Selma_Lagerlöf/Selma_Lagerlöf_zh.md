# 文学家立传提示词（OpenLiterature：Selma Lagerlöf）

> **本文件是 OpenLiterature 的「文学家立传提示词」**，以 Selma Lagerlöf（1909 诺贝尔文学奖，文学奖首位女性得主）为实例。
> 结构对齐母本 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，内容适配文学家：无公式框——用**意象图式 / 名句引文框 / 书影**替代。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 诺贝尔文学奖得主人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Selma Ottilia Lovisa Lagerlöf（塞尔玛·拉格洛夫），1909 年诺贝尔文学奖得主。
- **设计哲学**：文学家立传强调「代表作与文学世界」+ 身份信息页；拉格洛夫的核心视觉语言是**北欧传说与鹅背之旅**——Mårbacka 庄园的炉边童话、韦姆兰的乡野传说、骑鹅飞越瑞典全境的地理史诗、耶路撒冷的朝圣者。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Selma Lagerlöf（1858-11-20 ~ 1940-03-16，享年 81 岁）
- **气质关键词**：**传说重构者、首位女性文学奖得主、瑞典学院首位女性院士** —— 1909 诺贝尔文学奖获奖理由：
  > EN 原文（官方，禁止改写）: "in appreciation of the lofty idealism, vivid imagination, and spiritual perception that characterize her writings"
  > 中译（CITATION_ZH）: 表彰其作品所体现的崇高理想主义、生动的想象力与心灵的洞见
- **设计母题**：**鹅背与童话（wild goose & fireside tale）**——Nils 缩身骑家鹅 Morten 飞越十三省；《耶路撒冷》的达拉纳朝圣者；Mårbacka 庄园祖母的炉边故事。用候鸟航迹图式替代公式框。
- **本地数据源**：`literature/presentations/pages/20th_century/Selma_Lagerlöf/page.md`（+ `metadata.json`、`images.txt`）
- **Wikipedia URL**：https://en.wikipedia.org/wiki/Selma_Lagerl%C3%B6f （肖像第 0 步**待下载**，infobox 有 1909 年照片、1881 年照片）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（16 页骨架）

---

## 三、任务流程 【逐步执行，每完成一步汇报】

### 第 0 步：事实基准（第一轮已核对 page.md）

- **生卒**：1858-11-20 生于 Mårbacka（韦姆兰）~ 1940-03-16 卒于 Mårbacka（生于斯葬于斯，庄园一生贯穿）
- **国籍**：瑞典
- **家庭**：父 Erik Gustaf Lagerlöf（皇家韦姆兰军团中尉，酗酒——她本人极少提及）；母 Louise（née Wallroth，外祖父为富商兼铁厂主 brukspatron）；六子女中排第五；出生即髋伤，三岁半因病双腿瘸软（后恢复）；1884 家售 Mårbacka 庄园（晚年的她用诺贝尔奖金赎回，定居终老）
- **教育**：家教（Folkskola 尚未普及）→ 1882-1885 斯德哥尔摩 Högre lärarinneseminariet（皇家女子高等师范学院）
- **职业经历**：1885-1895 Landskrona 女子高中乡村教师——教书十年间写出处女作；1895 弃教从文
- **文学师承与影响**：七岁读 Thomas Mayne Reid 的《Osceola》立志作家；对 Strindberg 式写实主义持反抗立场（"reacted against the realism...such as August Strindberg"）；Sophie Elkan 对其创作方向影响至深（page 明载 "strongly influenced"）
- **关键荣誉**：Nobel 1909（文学奖**首位女性**）；1907 乌普萨拉大学荣誉博士；1928 格赖夫斯瓦尔德大学荣誉博士；1904 瑞典学院大金奖；1914 瑞典学院院士（**首位女性**）；Litteris et Artibus 1909；Illis quorum 1926；多国勋位（法/挪/比/芬等）；1991 成为首位登上瑞典纸币的女性（20 克朗）
- **核心作品与贡献**：
  1. 《Gösta Berlings Saga》（1891）——处女作，33 岁成名；《Idun》杂志竞赛获奖得出版合同
  2. 《Antikrists mirakler》（1897，西西里，基督教与社会主义道德的碰撞）
  3. 《Jerusalem》两部（1901-02，达拉纳朝圣者赴耶路撒冷）
  4. 《尼尔斯骑鹅旅行记》（Nils Holgerssons underbara resa, 1906-07）——全国教师协会约稿的地理教科书，译成 30+ 语言
  5. 《Körkarlen》（1912，英译 Thy Soul Shall Bear Witness!）——1921 改编电影《幽灵马车》为瑞典默片经典
  6. Löwenskölds 三部曲（1925-28）
  7. 回忆录三部（Mårbacka, 1922-32）
- **关键时间线**（15–20 节点）：1858 生于 Mårbacka → 幼年髋伤与祖母童话 → 1875 寄居 Karlskoga 姑母家 → 1884 家售庄园 → 1882-85 师范学院（反抗 Strindberg 式写实）→ 1885-95 Landskrona 教师 → 1890 《Idun》竞赛首章胜出 → 1891《Gösta Berlings Saga》出版 → 1894 结识 Sophie Elkan（终生友伴）→ 1895 弃教从文 → 1897 迁 Falun、结识 Valborg Olander → 1890s 末与 Elkan 游意大利/巴勒斯坦/埃及（写《Antikrists mirakler》《Jerusalem》素材）→ 1900 访耶路撒冷美国殖民地 → 1902 受约写地理书 → 1906-07《尼尔斯骑鹅旅行记》→ 1907 乌普萨拉荣誉博士 → 1909-12-10 诺贝尔奖（受奖演说"天国见父"故事）→ 1911 斯德哥尔摩国际妇女选举权大会开幕致辞 → 1914 瑞典学院首位女性院士 → 1919 售出未刊作品全部电影版权 → 1920s 用诺奖奖金赎回 Mårbacka → 1930s 回忆录三部 → 1939 冬季战争：将诺奖奖章与学院金奖交芬兰政府筹款（芬方另行筹资并奉还）→ 1939 出面营救挚友 Nelly Sachs 母女离德赴瑞（最后一批航班）→ 1940-03-16 卒于 Mårbacka

### 第 4 步：文学领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | novel | 长篇小说 | Gösta Berling / Jerusalem / 幽灵马车 | 核心页 |
| 1 | children's literature | 儿童文学 | 尼尔斯骑鹅旅行记，30+ 语言译本 | 尼尔斯页 |
| 2 | folklore | 民间传说 | 韦姆兰乡野传说与童话重述 | 传说页 |
| 3 | short story | 短篇小说 | 基督传说集/圣诞故事集 | 短篇页 |
| 4 | women's suffrage | 妇女参政运动 | 全国妇女参政协会演说者（frontmatter field_of_work 明载） | 社会活动页 |

#### 4.1 入库操作
- `MySQL/data/Selma_Lagerlöf.yaml` → `python3 MySQL/seed_person.py data/Selma_Lagerlöf.yaml`
- `primary_occupation='writer'`、occupations：writer(0)/novelist(1)/children's writer(2)；nationality：Sweden
- 校验 fields≥4、relations≥2、has_social_data=1

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| colleague | Sophie Elkan | 无向 | 瑞典作家，1894 结识的终生友伴，互相 critique，对其创作影响至深 |
| colleague | Valborg Olander | 无向 | 教师出身的文学助手与挚友，负责出版事务 |
| colleague | Nelly Sachs | 无向 | 德裔犹太女诗人挚友，1939 助其母女脱纳粹德国赴瑞典 |

### 第 5 步：设计配色

- **主色**：峡湾深蓝 `#14324F` + 诺奖香槟金 `C9A227`
- badgeA 长篇 — 靛蓝 `#4C5FD5`；badgeB 儿童 — 琥珀 `#E07B30`；badgeC 传说 — 青绿 `#0E7C7B`；badgeD 参政运动 — 玫瑰 `#C4204F`
- **背景母题**：候鸟迁徙航迹 + 炉边星火圆点（鹅背之旅与童话的双母题）

### 第 6 步：幻灯片序列（15 页）

```
00  OpenLiterature 项目首页（\input cover 共享封面）
01  封面 — 文学奖首位女性得主 / Selma Lagerlöf 1858–1940 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒/教育/教师十年/荣誉/核心领域）
03  核心贡献概览 — Gösta Berling / 尼尔斯 / 耶路撒冷 / 幽灵马车
04  Mårbacka 童年 (1858–1884) — 髋伤与瘸腿/祖母炉边童话/七岁立志/庄园易主
05  师范与教师十年 (1882–1895) — 斯德哥尔摩/Landskrona/反抗写实主义
06  Gösta Berling 的诞生 (1890–1891) — Idun 竞赛/出版合同/初期冷遇
07  Georg Brandes 的推介 — 丹麦译本好评后声名鹊起/与 Elkan 的旅行写作
08  耶路撒冷与圣地 (1899–1902) — 美国殖民地/巴勒斯坦素材/批评家以 Homer、Shakespeare 相比
09  尼尔斯骑鹅旅行记 (1906–1907) — 教师协会约稿/地理与童话合一/30+ 语言（航迹图式页）
10  1909 诺贝尔奖 — 官方理由 EN+中译/首位女性/受奖演说"天国见父"（引文框）
11  瑞典学院首位女性院士 (1914) — 1904 大金奖/1914 入院/院内斗争背景一句
12  挚友与助手 — Elkan 与 Olander 双重关系/相互 critique/书信集《Du lär mig att bli fri》
13  电影与默片时代 — 1919 售出电影权/《幽灵马车》(1921)/Sjöström 的乡村影像
14  晚年：奖章与救援 (1939–1940) — 冬季战争捐奖章/营救 Nelly Sachs/1940 卒于 Mårbacka + 结尾
```

### 第 7–8 步：版式要点 + 专属陷阱

| 陷阱 | 说明 |
|------|------|
| 诺奖理由 | 三要素（崇高理想主义/生动想象/心灵洞见）全引官方句；勿写"因尼尔斯获奖" |
| 两个"首位" | 文学奖首位女性（1909）与瑞典学院首位女性院士（1914）是两件事，勿混 |
| 获奖年月 | 1909-12-10 领奖；诺奖决定前学院内部有激烈斗争（page 明载），可一句带过 |
| 私生活 | 与 Elkan/Olander 的关系：page 表述为"friendship and love 边界模糊、当时女同性恋关系违法故从未公开"——**按 page.md 措辞谨慎转述，不加现代标签、不下断言**；关系类型统一用 colleague |
| Nelly Sachs | 救援发生于 1940 年初（"last flight from Germany to Sweden"）；Sachs 1966 年获文学奖——可作呼应注 |
| 芬兰奖章 | 1939 冬季战争捐出奖章，芬兰政府另行筹资后**原物奉还**——方向勿写反 |
| 引语红线 | 受奖演说"天国见父"仅按 page.md 概述转述；书名《Du lär mig att bli fri》/《En riktig författarhustru》直用原题；其余禁杜撰 |
| 同名区分 | Sophie Elkan（作家友伴）≠ Valborg Olander（助手）；Georg Brandes 仅"书评助推"一事，**不建关系** |

### 第 9 步：术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| Gösta Berling's Saga | 《约斯塔·贝林的故事》 | 1891 处女作 |
| The Wonderful Adventures of Nils | 尼尔斯骑鹅旅行记 | 原题直译"尼尔斯·霍尔格森在瑞典的奇妙旅行" |
| Mårbacka | Mårbacka 庄园 | 出生地与终老地，保留原名 |
| Phantom Carriage | 幽灵马车 | 1921 改编片名 |
| Värmland | 韦姆兰 | 大部分故事背景地 |
| Idun | 《Idun》杂志 | 竞赛出道平台 |
| brukspatron | 铁厂主 | 外祖父身份词 |
| Högre lärarinneseminariet | 皇家女子高等师范学院 | 保留瑞典原名 |

---

## 四、BGM 建议

- **选定曲目**: **Savage** — Alex-Productions（52k views，高受众 / 强推进 / 紧张）
- **匹配理由**: "强推进" 匹配拉格洛夫在男性主导文学界的破冰之力——33 岁凭竞赛一举成名、1895 弃教从文的孤注一掷、1911 国际妇女选举权大会开幕致辞与两个"首位"的开拓；"紧张" 呼应《幽灵马车》的道德张力与骑鹅之旅的冒险
- **备选**（未采用）: Daylight（明亮贴切但已分配给 Eucken）；The Flow of Time（时间感合适但已分配给 Kipling）
- **时长对齐**: ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件

| 文件 | 用途 |
|------|------|
| `literature/presentations/pages/20th_century/Selma_Lagerlöf/page.md` | 事实基准 |
| `MySQL/data/Selma_Lagerlöf.yaml` | 入库 yaml |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参照 |

> **开始执行。每写一页就 make，看到溢出就修。**
