# 文学家立传提示词（OpenLiterature：Verner von Heidenstam）

> **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenPhysicist / OpenMathAI 侧共享 GitHub `OpenMathAI/OpenMath`）。
> **本实例**：Carl Gustaf Verner von Heidenstam（韦尔纳·冯·海登斯塔姆），1916 年诺贝尔文学奖得主。
> **设计哲学**：文学家立传延续物理学家模板的骨架（身份信息页 + 结构化领域表），但以**代表作书影 / 名句引文框 / 意象图式**替代公式框——对海登斯塔姆，即瑞典山水的色彩与民族史诗的旗帜。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史。
- **本实例**：Verner von Heidenstam（1859–1940），瑞典诗人、小说家，1916 年诺贝尔文学奖得主，1912 年起任瑞典学院院士。
- **设计哲学**：以「瑞典新时代文学的开端」为核心叙事——一位从东方之旅归来的贵族画家，用一部诗集终结了瑞典自然主义的主导地位，开启民族浪漫主义的新纪元。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Carl Gustaf Verner von Heidenstam（韦尔纳·冯·海登斯塔姆，1859-07-06 ~ 1940-05-20，享年 80 岁）
- **官方获奖理由（Nobel 1916，禁止改写）**：
  > "in recognition of his significance as the leading representative of a new era in our literature"
  > （表彰其作为我们文学新时代主要代表的意义）
- **气质关键词**：**民族浪漫主义的旗手、自然主义的终结者、瑞典山水的歌者**
- **设计母题**：**北欧之光（Nordic light）**。其诗文「充满巨大的生命之乐，时而浸透着对瑞典历史与山水（尤其自然风貌）的热爱」——以瑞典四季光线（雪原白、森林绿、湖蓝、夏夜金）构成视觉母题，呼应其民族浪漫主义诗学。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/literature/presentations/pages/20th_century/Verner_von_Heidenstam/page.md`
- **Wikipedia**：https://en.wikipedia.org/wiki/Verner_von_Heidenstam
- **肖像**：第 0 步从 images.txt / Wikipedia REST API 下载；404 则用装饰圆占位（标注「肖像待补」）。
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）、`literature/presentations/cover/`（统一封面 `\input`）。

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属，已按 page.md 核对】

- **生卒**：1859-07-06 生于 Olshammar（Örebro County，瑞典）～ 1940-05-20 卒于故居 Övralid（瑞典），享年 80 岁。
  - ⚠ frontmatter 生卒有双值噪声（`1859-07-06 / 1859-01-01`、`1940-05-20 / 1940-01-01`），**以 infobox/正文精确日期为准**。
- **本名**：Carl Gustaf Verner von Heidenstam；出身贵族（noble family）。
- **家庭**：父 Gustaf von Heidenstam 为**工程师**；母 Magdalena Charlotta（娘家姓 Rütterskiöld）。
- **婚姻（三段，均 page.md infobox 明载）**：Emilia Uggla（1880–1893）、Olga Wiberg（1893–1903）、Greta Sjöberg（1903–1906）。婚姻区间外的性质（离异/丧偶）page.md 无载，**禁写**。
- **教育**：Stockholm 的 *Beskowska skolan*；后在斯德哥尔摩皇家美术学院学画，**因健康不佳辍学**；随后游历欧洲、非洲与东方。
- **文学师承与影响**：page.md 无载任何导师/影响者，**禁写**。
- **任职/荣誉**：1912 年起瑞典学院院士；Nobel 1916；Heidelberg 大学荣誉博士；Samfundet De Nio 大奖；Goethe 艺术与科学勋章。
- **核心作品与贡献（5 条）**：
  1. *Vallfart och vandringsår*（《朝圣与漫游岁月》，1888）——首部诗集，取材东方之旅，标志对瑞典自然主义主导地位的告别；
  2. *Hans Alienus*（1892）——长篇叙事诗，展现其对美的爱；
  3. *Karolinerna*（《查理的士兵》，1897–98 两卷）——国王卡尔十二世与其骑士的历史群像，洋溢强烈的民族热情；
  4. *Folkungaträdet*（《芬根家族之树》，1905–07 两卷）——中世纪瑞典酋长氏族的灵感性史诗故事；
  5. *Nya Dikter*（《新诗集》，1915）——哲思主题：人从孤独向更善人性的升华。
- **1910 年论战**：瑞典报纸上关于文学「无产阶级化堕落的论战」——对阵双方主将为 **August Strindberg 与 von Heidenstam**，教授 Lidforss 与 Böök 亦参与；Heidenstam 的主要贡献是小册子 *Proletärfilosofiens upplösning och fall*（"The Decline and Fall of the Proletarian Philosophy"，矛头主要指向 Strindberg）。
- **关键时间线（16 节点）**：
  1859-07-06 生于 Olshammar → 贵族家庭、Beskowska skolan → 皇家美术学院学画因病因健康辍学 → 游历欧洲/非洲/东方 → 1888 *Vallfart och vandringsår* 一举成名 → 1889 *Renässans*、*Endymion* → 1892 *Hans Alienus* → 1895 *Dikter* → 1897–98 *Karolinerna* → 1900 *Sankt Göran och draken* → 1901 *Heliga Birgittas pilgrimsfärd*（同年海德堡讲学背景见德文著作）→ 1902 *Ett folk*、英译 *A King and his Campaigners* → 1904 *Skogen susar* → 1905–07 *Folkungaträdet* → 1908–10 *Svenskarna och deras hövdingar* → 1910 与 Strindberg 论战 → 1912 入瑞典学院 → 1915 *Nya Dikter* → **1916 诺贝尔文学奖** → 1919–25 英译系列出版 → 1940-05-20 卒于 Övralid。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | national romanticism | 民族浪漫主义 | 瑞典新时代文学的代表立场 | 封面、核心页 |
| 1 | lyric poetry | 抒情诗 | *Vallfart och vandringsår* / *Dikter* / *Nya Dikter* | 诗集页 |
| 2 | historical novel | 历史小说 | *Karolinerna*、卡尔十二世群像 | 史诗页 |
| 3 | epic narrative | 史诗叙事 | *Folkungaträdet*、中世纪氏族史诗 | 史诗页 |
| 4 | travel writing | 旅行文学 | *Från Col di Tenda till Blocksberg*、东方之旅 | 早年页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| controversy | August Strindberg | 无向 | 1910 年瑞典报纸文学论战对阵主将（"Proletärfilosofiens upplösning och fall" 矛头所指） |
| spouse | Emilia Uggla | 无向 | 1880–1893 |
| spouse | Olga Wiberg | 无向 | 1893–1903 |
| spouse | Greta Sjöberg | 无向 | 1903–1906 |

> Lidforss 与 Böök 仅「参与论战」，非对手主将，**不入库**（防噪声）。1916 为独得，无 co-honored。

### 第 5 步：设计配色 【人物专属】

- **主色**：森林深绿 `#1B4D3E`（瑞典山水/民族浪漫）
- **诺奖香槟金**：`#C9A227`
- badge 四分类色：
  - `badgePoem` 抒情诗 — 湖蓝 `#2E6E8E`
  - `badgeEpic` 史诗叙事 — 琥珀 `#C98A2D`
  - `badgeHistory` 历史小说 — 铁锈红 `#9E3B2B`
  - `badgeDebate` 论战/晚期 — 石墨 `#4A4A55`
- **背景母题**：柔和气泡 + 四季光线色块（雪原白/森林绿/湖蓝/夏夜金），呼应「北欧之光」设计母题。

### 第 6 步：规划幻灯片序列 【人物专属，15 页】

```
00  OpenLiterature 项目首页（\input cover/…）
01  封面 — 瑞典文学新时代的代表 / Verner von Heidenstam 1859–1940 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒、本名、国籍、出生地、教育、瑞典学院、荣誉、核心领域）
03  核心贡献概览 — 抒情诗 / 历史小说 / 史诗叙事 / 民族浪漫主义纲领
04  早年：Olshammar 贵族之子 (1859–1887) — 工程师之子、学画辍学、欧非东方之旅
05  《朝圣与漫游岁月》(1888) — 东方之旅入诗、告别自然主义（代表作书影/意象框①）
06  Renässans 与 Hans Alienus (1889–1895) — 美的宣言、长篇叙事诗
07  Karolinerna：卡尔十二世的士兵 (1897–98) — 历史群像与民族热情（意象框②）
08  民族史诗十年 (1900–1910) — Sankt Göran / Heliga Birgitta / Ett folk / Folkungaträdet / Svenskarna och deras hövdingar
09  1910 年论战 — 与 Strindberg 的报纸论战、小册子、Lidforss 与 Böök 参与
10  瑞典学院与诺贝尔奖 (1912–1916) — 1912 院士、1916 获奖（获奖理由 EN 原文引文框）
11  Nya Dikter (1915) — 从孤独向更善人性的哲思升华
12  荣誉与认可 — Heidelberg 荣誉博士、Samfundet De Nio 大奖、Goethe 勋章、英译传播
13  遗产：瑞典文学的转折点
14  结尾
```

> 文学家无公式框：第 5/7/10 页用**代表作书影框 / 意象图式 / 获奖理由原文引文框**替代。

### 第 7–8 步：版式要点与专属陷阱 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方原文 "in recognition of his significance as the leading representative of a new era in our literature"（数据源 json 尾部有多余引号噪声，引用时清理为标准一句），强调「新时代的主要代表」，勿写成「民族史诗」或「山水诗人」 |
| 生卒日期 | frontmatter 有 `1859-01-01 / 1940-01-01` 噪声双值，一律取 infobox/正文 07-06 与 05-20 |
| 论战性质 | 1910 是**报纸上的文学论战**（无产阶级化之争），非政治事件，勿升级叙事；Heidenstam 小册子矛头"chiefly"指向 Strindberg，勿写成单方面攻击 |
| 婚姻区间 | 三段婚姻只写区间（1880–1893 / 1893–1903 / 1903–1906），离异或丧偶 page.md 无载**禁写** |
| 父亲职业 | Gustaf von Heidenstam 是**工程师**，勿写成军官/地主 |
| 学历 | 无大学学位；皇家美术学院学画**因健康不佳辍学**；Heidelberg 是**荣誉**博士，勿写成正式学位 |
| 无引语红线 | page.md 无任何原话引语，全篇禁杜撰名句；引文框只用作品题名（附英译）与获奖理由官方原文 |
| 无师承 | page.md 未载任何导师/影响者/弟子，社会关系仅论战 + 三段婚姻，勿添油 |
| 1917 共享奖区分 | 1917 共享奖是 Gjellerup 与 Pontoppidan；Heidenstam 的 1916 为独得，勿混 |
| 姓名 | 简称统一「von Heidenstam / 海登斯塔姆」，全名 Carl Gustaf Verner von Heidenstam 首次出现后不必重复 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| national romanticism | 民族浪漫主义 | 与"民族主义"政治概念区分 |
| Vallfart och vandringsår | 《朝圣与漫游岁月》 | 1888 首部诗集 |
| Karolinerna | 《查理的士兵》 | The Charles Men，指卡尔十二世的士兵 |
| Folkungaträdet | 《芬根家族之树》 | The Tree of the Folkungs，两卷 1905–07 |
| Nya Dikter | 《新诗集》 | 1915，哲思主题 |
| Swedish Academy | 瑞典学院 | 1912 入选，勿与诺奖委员会混同 |
| naturalism | 自然主义 | 其 1888 诗集所告别的流派 |
| Övralid | 厄弗拉利德 | 晚年故居与去世地 |
| Olshammar | 乌尔沙马尔 | 出生地（Örebro County） |
| Samfundet De Nio | 九人协会 | 瑞典文学社团，其大奖非诺奖 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Timeless**（Alex-Productions）
- **风格标签**：沉稳 / 纪录片 / 长期纲领
- **匹配理由**：海登斯塔姆的叙事是从贵族庄园到东方、从论战到瑞典学院的**漫长文学生涯**——「纪录片」式思想演进而非戏剧性突变；「沉稳」匹配民族浪漫主义的庄重气质；「长期纲领」呼应其作为「新时代代表」的文学史定位。
- **本地路径**：`music_audio/` 下 Alex-Productions Timeless（对照 `curated_tracks.md`）→ 复制到 `literature/presentations/20th_century/Verner_von_Heidenstam/Timeless.wav`。

> **开始执行。每完成一步汇报；无载禁写是最高红线。**
