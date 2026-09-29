# 文学家立传提示词（OpenLiterature 批次实例：Johannes Vilhelm Jensen）

> 本文件是 OpenLiterature 的「文学家立传提示词」，以 Johannes Vilhelm Jensen（1944 诺贝尔文学奖，《国王的失势》）为对象。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`，内容适配文学家：无公式框，以代表作书影/名句引文框/意象图式替代。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（OpenMathAI 共享仓库，结尾页品牌统一 `OpenMathAI`）。
- **本实例**：Johannes Vilhelm Jensen（约翰内斯·威廉·延森，1873–1950），1944 诺贝尔文学奖得主，**丹麦现代主义之父**。
- **设计哲学**：文学家立传以「代表作意象 + 文学领域结构化表达 + 身份信息页」为骨架；Jensen 的核心视觉语言是**荒原之风与进化长旅（the moor wind and the long journey of evolution）**——从日德兰荒原到六卷本「进化的圣经」。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Johannes Vilhelm Jensen（1873-01-20 ~ 1950-11-25，享年 77 岁）
- **气质关键词**：**丹麦现代主义之父、进化史诗的营造者、鲁莽的论战家**
- **官方获奖理由（1944）**：
  > EN: "for the rare strength and fertility of his poetic imagination with which is combined an intellectual curiosity of wide scope and a bold, freshly creative style"
  > 中译：表彰其诗歌想象力的罕见力量与丰饶，兼有广博的求知欲与大胆而清新的创造性风格
  > （来源：`literature/generate_20th_century_list.py` CITATION_ZH[("1944","Johannes Vilhelm Jensen")] + `literature/nobel_literature_citations.json`，禁止改写）
- **设计母题**：**荒原之风与进化长旅**——日德兰荒原的地平线风纹 + 从冰河期到哥伦布的六卷时间轴（*Den lange rejse* 各卷序列作图式）。
- **本地数据源**：
  - `literature/presentations/pages/20th_century/Johannes_Vilhelm_Jensen/page.md`（Wikipedia 全文）
  - 同目录 `metadata.json`、`images.txt`；Wikipedia URL: https://en.wikipedia.org/wiki/Johannes_Vilhelm_Jensen
  - 肖像（第 0 步下载）：`images/` 下待下载（page.md 内嵌 1902 年照，404 则装饰圆占位）

---

## 三、任务流程 【逐步执行】

### 第 0 步：事实基准（已核对 page.md）

- **生卒**：1873-01-20 生于日德兰北部 Farsø 村 ~ 1950-11-25 卒于哥本哈根 Østerbro，享年 77 岁。
- **国籍**：丹麦（Kingdom of Denmark）。
- **出身与教育**：兽医之子，乡村环境长大；Viborg Katedralskole；入哥本哈根大学**学医**（以写作为学费来源），三年后弃医从文。
- **家庭**：胞妹 **Thit Jensen** 亦是知名作家、直言（偶有争议）的早期女权主义者。
- **文学师承与影响**：page.md 明载——**Walt Whitman** 是影响他的作家之一；旅行广泛（如同乡安徒生），赴美之旅催生名诗 "Paa Memphis Station"（孟菲斯车站）。晚年成为无神论者。
- **核心作品与贡献（4–6 条）**：
  1. *Kongens Fald*（The Fall of the King《国王的失势》，1900–1901）——以国王 Christian II 为中心的现代历史小说，被 Seymor-Smith 评为「对丹麦优柔寡断与生命力缺失的控诉」；1999 年被 Politiken 与 Berlingske Tidende 分别评为 20 世纪最佳丹麦小说。
  2. *Den lange rejse*（The Long Journey《漫长的旅途》，1908–22，六卷）——以进化论为骨架的人类史诗，被称为「进化的圣经」（各卷：Den tabte land 1919 / Bræen 1908 / Norne Gæst 1919 / Cimbrernes tog 1922 / Skibet 1912 / Christofer Columbus 1922；1938 两卷版）。
  3. *Himmerland Stories*（希默兰故事，1898–1910）——以故乡 Himmerland 为背景的短篇系列；"Ane og Koen"（1904）1928 年由狱中作家兼译者 Victor Folke Nelson 英译。
  4. *Digte 1906*——首部诗集，奠定其丹麦早期现代主义旗手地位（散文诗、直白语言）。
  5. 早期都市幻灭小说 *Danskere*（1896）、*Einar Elkjær*（1898）——从通俗小说转向严肃文学。
  6. 随笔与科学著述——宏大叙事、未来主义、人类学与进化哲学（1920 年代后致力于以达尔文思想建立伦理体系，试图复兴古典诗歌）。
- **关键荣誉**：Nobel 1944（1945-12-10 斯德哥尔摩颁奖，瑞典学院常秘 Anders Österling 致辞，致辞文本 page.md 实载可引）；生前获诺奖提名 **53 次**（首次 1925，1931–1944 每年提名）。
- **趣味史实**：1900-12 致出版人 Ernst Bojesen 信中画出笑脸与哭脸图示——是 smiley face 最早的身影之一。
- **关键时间线（18 节点）**：
  1. 1873-01-20 生于 Farsø（北日德兰）
  2. 兽医之子，乡村环境成长
  3. 就读 Viborg Katedralskole
  4. 入哥本哈根大学学医，靠写作赚取学费
  5. 三年后弃医从文
  6. 1896 *Danskere*（都市幻灭）
  7. 1898 *Einar Elkjær*；*Himmerlandsfolk*
  8. 1898–1910 希默兰故事系列
  9. 1900-12 致 Bojesen 信中画笑脸图示
  10. 1900–1901 *Kongens Fald*（现代历史小说巅峰）
  11. 1904 "Ane og Koen"（1928 英译）
  12. 1906 *Digte 1906*（现代主义名声确立）
  13. 1908–1922 六卷 *Den lange rejse*
  14. 1920 于 Aars 创立 Museumcentre Aars
  15. 1920 年代后转向生物/动物学式研究，以达尔文主义建伦理体系
  16. 1925–1944 诺奖提名 53 次（1931 起逐年）
  17. 1944 诺贝尔文学奖；1945-12-10 斯德哥尔摩受奖
  18. 1950-11-25 卒于哥本哈根 Østerbro；1999 *Kongens Fald* 获评世纪最佳丹麦小说

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- `literature/presentations/20th_century/Johannes_Vilhelm_Jensen/`（含 `images/`）；Makefile 设 `MAIN=Johannes_Vilhelm_Jensen_zh`；肖像按 `images.txt` 下载，404 用装饰圆占位。

### 第 4 步：文学领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | modernist poetry | 丹麦现代主义诗歌 | Digte 1906、散文诗先驱、直白语言 | 诗歌页 |
| 1 | historical novel | 历史小说 | Kongens Fald，世纪最佳丹麦小说 | 核心页 |
| 2 | evolutionary epic | 进化史诗 | Den lange rejse「进化的圣经」 | 长旅页 |
| 3 | short story | 短篇小说 | 希默兰故事系列 (1898–1910) | 短篇页 |
| 4 | essay | 随笔 | 未来主义、人类学与进化哲学随笔 | 随笔页 |

- 入库：`MySQL/data/Johannes_Vilhelm_Jensen.yaml` → `python3 seed_person.py data/Johannes_Vilhelm_Jensen.yaml`（primary_occupation: writer）。

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| sibling | Thit Jensen | 无向 | 胞妹，同为知名作家、早期女权主义者 |
| influence | Walt Whitman | Whitman → Jensen | 影响延森的作家之一（page.md 明载） |

> page.md 明载仅以上两条家庭/影响关系。Kipling/Hamsun/Sandburg 只是评论者的比较（"bears comparison"），Hans Christian Andersen 只是「同乡皆好旅行」的类比——**均非关系，禁入库**。1912 年他写过题为 *Rudyard Kipling* 的专著，属作家论，不入关系表。

### 第 5 步：设计配色方案

- **主色**（批次预分配）：深藏青 `#1F3A5F`（荒原夜风与史诗纵深）
- **辅色**：诺奖香槟金 `#C9A227`
- **badgeA–D**：badgeA 现代主义诗歌 — 风青 `#2C6E8F`；badgeB 历史小说 — 王旗红 `#8C3A2E`；badgeC 进化史诗 — 冰原灰蓝 `#5E7382`；badgeD 短篇/随笔 — 荒原金 `#B08D3E`
- **背景母题**：地平线风纹曲线 + 六卷时间轴刻度（Den lange rejse 卷序）。

### 第 6 步：幻灯片序列（15 页）

```
00  OpenLiterature 项目首页（\input cover 共享首页）
01  封面 — 荒原之风与进化长旅 / Johannes V. Jensen 1873–1950 + 主色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒、国籍、出身、教育、家庭、荣誉、核心领域）
03  核心贡献概览 — 国王的失势 / 漫长的旅途 / 希默兰故事 / Digte 1906
04  日德兰之子 (1873–1896) — Farsø、兽医之子、Viborg、哥大学医、弃医从文
05  都市幻灭与转向 (1896–1898) — Danskere、Einar Elkjær
06  希默兰故事 (1898–1910) — 故乡短篇系列、"Ane og Koen"
07  国王的失势 (1900–1901) — Christian II、「丹麦优柔寡断的控诉」、1999 世纪最佳
08  进化长旅 (1908–1922) — 六卷「进化的圣经」卷序图式 + 诺奖自述进化哲学动机（实载引语）
09  官方获奖理由引文框（EN 原文 + 中译，禁止改写）
10  现代主义诗歌 — Digte 1906、散文诗、直白语言、丹麦现代主义之父
11  诺奖与 Österling 致辞 — 53 次提名、1944 获奖周年补授、致辞实载段
12  论战与争议 — polemicist、种族理论争议的客观一笔、「无论证表明法西斯倾向」
13  遗产与趣闻 — 笑脸图示 (1900)、Johannes V. Jensen Land、1960 年代尚有直接影响
14  结尾
```

### 第 7–8 步：版式要点 + 人物专属陷阱表

- 版式：六卷长旅页用时间轴 tikz 图式；致辞引文页注意长引文分行。
- **陷阱**：

| 陷阱 | 说明 |
|------|------|
| 1933 年混排 | 导语段 "The Fall of the King (1933)" 的 1933 是**英译年份**；原著 Kongens Fald 为 1900–1901（对照书目行），勿把 1933 当出版年 |
| 名字形式 | 常用 Johannes V. Jensen；yaml name_en 用 frontmatter 的 Johannes Vilhelm Jensen；勿与丹麦其他 Jensen 同名者混淆（本篇为小说家 J. V. Jensen） |
| 诺奖年份 | 1944 年度奖，1945-12-10 才在斯德哥尔摩补行颁奖（战时/战后时序），勿写成 1945 年度奖 |
| 诺奖理由 | 官方 EN 整句 + CITATION_ZH 中译，禁止改写 |
| 种族理论争议 | page.md 明载 "dubious racial theories have damaged his reputation" + 「从未显露明显法西斯倾向」——只此两句客观口径，不展开政治叙事 |
| 进化哲学动机 | 诺奖自述（page.md 实载英文）：为纠正纳粹对达尔文主义的歪曲而把进化哲学引入文学——可引原文 |
| 比较非关系 | Kipling/Hamsun/Sandburg/Andersen 均为类比或比较，禁入关系库 |
| 医学背景 | 大学学医三年，勿写成医学科班毕业 |

### 第 9 步：术语审查清单

| 英文 | 中文 | 风险 |
|------|------|------|
| Kongens Fald / The Fall of the King | 国王的失势 | 1900–1901 原著；1933 为英译 |
| Den lange rejse / The Long Journey | 漫长的旅途 | 六卷 1908–22，两卷版 1938 |
| Himmerland | 希默兰 | 故乡地区，短篇系列背景 |
| prose poem | 散文诗 | 现代主义引入物 |
| evolutionary bible | 进化的圣经 | Den lange rejse 别称 |
| Christian II | 克里斯蒂安二世 | 历史小说主角国王 |
| Jutland | 日德兰 | 出生地 Farsø 所在半岛 |
| Victor Folke Nelson | 狱中译者 | 1928 英译 "Ane og Koen" |
| Anders Österling | 瑞典学院常秘 | 1945 颁奖致辞人 |
| Johannes V. Jensen Land | 延森地 | 格陵兰北部地名纪念 |
| Museumcentre Aars | 阿尔斯博物馆中心 | 1920 创立 |
| smiley face | 笑脸图示 | 1900 书信实载，趣闻非发明权主张 |

---

## 四、背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Tragedy** — Alex-Productions（批次预分配）
- **匹配理由**：1944 年度文学奖诞生于被战火撕裂的欧洲（次年才补行颁奖），Jensen 自述写「进化史诗」正是为了纠正纳粹对达尔文主义的歪曲——庄重悲剧感匹配这个「在至暗时刻为文明作证」的获奖语境；也呼应《国王的失势》的历史挽歌内核与其论战人生的争议沉重。
- **对照**：`music_audio/curated_tracks.md`（alex-productions 系列）。封面主色 `#1F3A5F`，批次内唯一。
