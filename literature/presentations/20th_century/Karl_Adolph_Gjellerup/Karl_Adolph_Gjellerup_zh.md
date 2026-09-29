# 文学家立传提示词（OpenLiterature：Karl Adolph Gjellerup）

> **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenPhysicist / OpenMathAI 侧共享 GitHub `OpenMathAI/OpenMath`）。
> **本实例**：Karl Adolph Gjellerup（卡尔·阿道夫·耶勒鲁普），1917 年诺贝尔文学奖得主（与同胞 Henrik Pontoppidan 共享）。
> **设计哲学**：文学家立传延续物理学家模板骨架（身份信息页 + 结构化领域表），以**代表作书影 / 引文框 / 意象图式**替代公式框——对耶勒鲁普，即「从自然主义到新浪漫主义、从丹麦到东方」的精神漂泊路线图。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史。
- **本实例**：Karl Adolph Gjellerup（1857–1919），丹麦诗人、小说家，斯堪的纳维亚「现代突破」时期作家，偶用笔名 **Epigonos**，1917 年与同胞 Henrik Pontoppidan 共享诺贝尔文学奖。
- **设计哲学**：以「诚实的真理求索者」为核心叙事——从牧师家庭的国家浪漫理想氛围出走，追随 Brandes 的自然主义，又在 1885 年彻底决裂转向新浪漫主义，最终在佛教与东方文化中安顿晚年，一个在两条战线上都不讨好、却始终诚实的精神轨迹。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Karl Adolph Gjellerup（卡尔·阿道夫·耶勒鲁普，1857-06-02 ~ 1919-10-11，享年 62 岁）
- **官方获奖理由（Nobel 1917，禁止改写）**：
  > "for his varied and rich poetry, which is inspired by lofty ideals"
  > （表彰其受崇高理想启迪的多样而丰富的诗歌）
- **气质关键词**：**现代突破的出走者、新浪漫主义转向者、东方文化的归依者**
- **设计母题**：**两次出走的路线图（the seeker's path）**。地理上从西兰岛牧师宅到德国克洛茨彻，精神上从国家浪漫主义到自然主义再到佛教的轮回世界——以一条贯穿幻灯片的「朝圣之路」视觉主线呼应其代表作 *The Pilgrim Kamanita*。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/literature/presentations/pages/20th_century/Karl_Adolph_Gjellerup/page.md`
- **Wikipedia**：https://en.wikipedia.org/wiki/Karl_Adolph_Gjellerup
- **肖像**：第 0 步从 images.txt / Wikipedia REST API 下载；404 则用装饰圆占位（标注「肖像待补」）。
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）、`literature/presentations/cover/`（统一封面 `\input`）。

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属，已按 page.md 核对】

- **生卒**：1857-06-02 生于 Præstø 的 Roholte 牧师宅（丹麦）～ 1919-10-11 卒于德国 Klotzsche，享年 62 岁。
  - ⚠ frontmatter 卒日有 `10-13 / 10-11` 双值噪声，**以 infobox/正文 1919-10-11 为准**。
- **家庭**：父亲为西兰岛牧师，在耶勒鲁普 3 岁时去世；此后**由 Johannes Fibiger 的叔父（uncle）抚养**，在国家浪漫的理想主义氛围中长大（page.md 原表述 "the uncle of Johannes Fibiger"，勿写成 Fibiger 本人是养父）。
- **婚姻**：妻子是德国人（page.md 未具名，**禁写姓名**）。
- **精神轨迹（三阶段）**：
  1. 1870 年代与出身背景决裂，成为自然主义运动与 **Georg Brandes** 的热烈支持者，写关于自由恋爱与无神论的大胆小说；
  2. 受出身影响渐离 Brandes 路线，**1885 年与自然主义者彻底决裂**，成为新浪漫主义者（其间有瓦格纳风格的戏剧）；
  3. 亲德（Germanophile）是其人生主线——1892 年定居德国，在丹麦左右两翼都不讨好；晚年认同德意志帝国（含其 1914–18 战争目标）。
- **文学师承与影响**：Georg Brandes（自然主义思想引领者，后决裂，page.md 明载）。
- **核心作品与贡献（5 条）**：
  1. *Germanernes Lærling*（《德意志人的学徒》，1882）——半自传体：青年从顺从的神学者到亲德无神论知识分子的成长；
  2. *Minna*（1889）——表面爱情故事，实为女性心理研究；
  3. *Møllen*（《磨坊》，1896）——爱情与嫉妒的阴郁情节剧；
  4. *Der Pilger Kamanita*（《朝圣者迦摩尼陀》，1906）——受佛教与东方文化影响的关键作：印度商人之子历生死轮回终至涅槃；被称『丹麦语写成的最奇特小说之一』；
  5. *Den fuldendtes hustru*（1907，诗剧，受但丁《神曲》启发，写佛陀（悉达多）尘世生活与其妻 Yasodhara）＋ 巨型小说 *Verdensvandrerne*（1910，灵魂在转世间漂泊）＋ 晚期 *Rudolph Stens Landpraksis*（1913）与绝笔 *Das heiligste Tier*（1919，唯一幽默尝试，动物死后自选至福之地的神话讽刺）。
- **诺奖后记（Aftermath）**：在丹麦反响冷淡——他早已被视为德国作家；其提名仍获丹麦支持；因瑞典一战中立，分裂的奖项未引发偏袒猜测，反而显示北欧邻邦的情谊。今日耶勒鲁普在丹麦几乎被遗忘，但文学史家通常视其为诚实的真理求索者。
- **传播**：作品被译成德语（常由其本人自译）、瑞典语、英语、荷兰语、波兰语、泰语等；*The Pilgrim Kamanita* 是译本最广的一种，泰译本（Phraya Anuman Rajadhon 合译）曾长期用于泰国教科书。
- **关键时间线（15 节点）**：
  1857-06-02 生于 Roholte 牧师宅 → 3 岁丧父、由 Fibiger 的叔父抚养 → 1870s 追随 Brandes 与自然主义 → 1882 *Germanernes Lærling* → 1885 与自然主义彻底决裂、转向新浪漫主义 → 1889 *Minna* → 1892 定居德国 → 1896 *Møllen* → 1906 *Der Pilger Kamanita* → 1907 *Den fuldendtes hustru* → 1910 *Verdensvandrerne* → 1913 *Rudolph Stens Landpraksis* → **1917 与 Pontoppidan 共享诺贝尔文学奖** → 1919 *Das heiligste Tier*（绝笔）→ 1919-10-11 卒于 Klotzsche。

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | modern breakthrough | 现代突破（斯堪的纳维亚） | 其文学归属期，后与 Brandes 路线决裂 | 封面、早年页 |
| 1 | psychological novel | 心理小说 | *Minna* 的女性心理研究 | 自然主义页 |
| 2 | romanticism | （新）浪漫主义 | 1885 决裂后的转向 | 决裂页 |
| 3 | Buddhist literature | 佛教题材文学 | *Der Pilger Kamanita*、*Den fuldendtes hustru*、轮回主题 | 东方页 |
| 4 | verse drama | 诗剧 | *Den fuldendtes hustru* 及瓦格纳风格戏剧 | 东方页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Henrik Pontoppidan | 无向 | 1917 年诺贝尔文学奖共享（两位丹麦作家平分） |
| influence | Georg Brandes | 对方 → Gjellerup | 1870s 自然主义思想引领者，Gjellerup 1885 与其路线彻底决裂 |
| influence | Dante | 对方 → Gjellerup | *Den fuldendtes hustru*（1907）受但丁《神曲》启发 |

> 妻子（德国人）page.md 未具名不入库；泰国合译者 Phraya Anuman Rajadhon 属书籍翻译合作，**不入库**（防噪声）；Fibiger 叔父仅为抚养背景，Fibiger 本人与 Gjellerup 无直接关系行。

### 第 5 步：设计配色 【人物专属】

- **主色**：孔雀深青 `#0B5351`（北欧冷冽 + 东方涅槃）
- **诺奖香槟金**：`#C9A227`
- badge 四分类色：
  - `badgeBreak` 现代突破/自然主义 — 钢蓝 `#2C5F8A`
  - `badgeRomance` 新浪漫主义 — 绛紫 `#6B3FA0`
  - `badgeOrient` 东方/佛教 — 恒河金 `#B8860B`
  - `badgeNobel` 诺奖/晚年 — 香槟 `#C9A227`
- **背景母题**：柔和气泡 + 一条贯穿版面的「朝圣之路」细线（从丹麦牧师宅曲线延伸至东方曼陀罗图形），呼应设计母题。

### 第 6 步：规划幻灯片序列 【人物专属，15 页】

```
00  OpenLiterature 项目首页（\input cover/…）
01  封面 — 受崇高理想启迪的诗歌 / Karl Adolph Gjellerup 1857–1919 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒、笔名 Epigonos、国籍、出生地、抚养、定居、荣誉、核心领域）
03  核心贡献概览 — 现代突破 / 心理小说 / 新浪漫主义 / 佛教题材文学
04  早年：牧师宅与 Fibiger 家族 (1857–1877) — 3 岁丧父、国家浪漫氛围
05  现代突破：Brandes 的门徒 (1870s–1885) — 自由恋爱与无神论小说、Germanernes Lærling、Minna
06  1885 决裂 — 新浪漫主义转向、瓦格纳风格戏剧、Møllen（代表作书影框①）
07  定居德国 (1892) — Germanophile、妻子是德国人、丹麦两翼的冷遇
08  Der Pilger Kamanita (1906) — 佛教与东方、生死轮回至涅槃（意象图式②）
09  Den fuldendtes hustru 与 Verdensvandrerne (1907–1910) — 但丁《神曲》启发、转世漂泊
10  晚期 (1913–1919) — Rudolph Stens Landpraksis、绝笔 Das heiligste Tier 的幽默
11  1917 诺贝尔奖 — 与 Pontoppidan 共享（获奖理由 EN 原文引文框）、丹麦冷淡与北欧情谊
12  翻译与传播 — 德语自译、Kamanita 在泰国教科书
13  遗产：诚实的真理求索者
14  结尾
```

> 文学家无公式框：第 6/8/11 页用**代表作书影框 / 意象图式 / 获奖理由原文引文框**替代。

### 第 7–8 步：版式要点与专属陷阱 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方原文 "for his varied and rich poetry, which is inspired by lofty ideals"（json 尾部引号噪声清理后引用），关键词「多样而丰富、崇高理想」 |
| 卒日双值 | frontmatter `1919-10-13 / 1919-10-11` 噪声，一律取 infobox/正文 **10-11** |
| 抚养关系 | page.md 原文是「由 Johannes Fibiger 的叔父抚养」，**勿写成 Fibiger 本人抚养/师承 Fibiger** |
| Brandes 两阶段 | 先热烈追随（1870s 自然主义）后 1885 彻底决裂——两个阶段都要写，勿只写决裂或只写追随 |
| 妻子 | 仅写「妻子是德国人」，未具名**禁写姓名** |
| 一战立场 | 「认同德意志帝国包括其 1914–18 战争目标」按 page.md 客观陈述即可，**不作政治评价、不展开战争叙事** |
| 引语红线 | 唯一可用引语是未具名的评价『one of the oddest novels written in Danish』（"has been called"，转述语气保留）；其余禁杜撰名句 |
| 共享奖区分 | 1917 与 Pontoppidan 共享，两人获奖理由**各不相同**（Gjellerup=诗歌理想、Pontoppidan=丹麦现实描写），勿互串 |
| 佛教题材 | 写「受佛教与东方文化影响」即可，勿写成佛教徒皈依 |
| 笔名 | Epigonos 仅「偶用」，勿写成常用名 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Modern Breakthrough | 现代突破 | 斯堪的纳维亚文学史专名，勿译「现代突破运动」以外的泛称 |
| Germanernes Lærling | 《德意志人的学徒》 | 1882，半自传 |
| Der Pilger Kamanita | 《朝圣者迦摩尼陀》 | 1906，译名最广之作 |
| Den fuldendtes hustru | 《完人之妻》 | 1907 诗剧，但丁启发 |
| Verdensvandrerne | 《世界漫游者》 | 1910，转世主题巨型小说 |
| Møllen | 《磨坊》 | 1896 情节剧 |
| Das heiligste Tier | 《最神圣的动物》 | 1919 绝笔讽刺 |
| Epigonos | 埃皮戈诺斯 | 偶用笔名 |
| Germanophile | 亲德者 | 描述性词汇，非贬义标签 |
| nirvana | 涅槃 | Kamanita 结局 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Nostalgia**（Alex-Productions）
- **风格标签**：怀旧 / 追忆 / 柔和
- **匹配理由**：耶勒鲁普是被祖国逐渐遗忘的漂泊者——「怀旧」匹配其「在丹麦几乎被遗忘、今日文学史家重估」的乡愁底色；也匹配其作品反复回望的转世与前生意象（Nostalgia 的回溯感与轮回主题同构）。
- **本地路径**：`music_audio/` 下 Alex-Productions Nostalgia（对照 `curated_tracks.md`）→ 复制到 `literature/presentations/20th_century/Karl_Adolph_Gjellerup/Nostalgia.wav`。

> **开始执行。每完成一步汇报；无载禁写是最高红线。**
