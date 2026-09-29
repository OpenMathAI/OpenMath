# 文学家立传提示词（OpenLiterature：Juan Ramón Jiménez）

> **本文件是 OpenLiterature 的「人物专属立传提示词」**，以 Juan Ramón Jiménez（1956 诺贝尔文学奖，西班牙"纯诗"大师）为传主。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架），内容适配文学家。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenLiterature —— 开放文学家人物史（与 OpenMathAI 各侧共享 GitHub）。
- **模板来源**：物理学家侧标杆（Kenneth G. Wilson）+ 数学家/化学家侧黄金骨架的文学适配版。
- **本实例**：Juan Ramón Jiménez（胡安·拉蒙·希梅内斯）。
- **设计哲学**：文学家立传保留「身份信息页」与「研究领域结构化表达」骨架，但**无公式框**——以**代表作书影 / 名句引文框 / 意象图式**替代。

---

## 二、背景信息 【人物专属】

- **目标文学家**：Juan Ramón Jiménez（1881-12-23 ~ 1958-05-29，享年 76 岁）
- **气质关键词**：**纯诗的殉道者、西班牙语抒情诗的炼金术士、流亡的安达卢西亚人** —— 1956 诺贝尔文学奖获奖理由：
  > "for his lyrical poetry, which in the Spanish language constitutes an example of high spirit and artistic purity"（表彰其抒情诗，以西班牙语构成崇高精神与艺术纯粹的典范）
- **设计母题**：**白银与驴蹄（Platero 之银）**。《小银与我》中那头银灰色小驴与故乡莫格尔的花园，是"纯诗"最温柔的化身——用银白、庭院绿意与书信体留白构成视觉语言。
- **本地数据源**：
  - `literature/presentations/pages/20th_century/Juan_Ramón_Jiménez/page.md`（Wikipedia 全文）
  - `literature/presentations/pages/20th_century/Juan_Ramón_Jiménez/metadata.json`、`images.txt`
  - Wikipedia URL：https://en.wikipedia.org/wiki/Juan_Ram%C3%B3n_Jim%C3%A9nez
- **肖像**：第 0 步待下载（images.txt / Commons Special:FilePath 回退；404 则装饰圆占位）。

---

## 三、任务流程 【模板通用，逐步执行】

> 每完成一步汇报。数据库同步要求：研究领域（第 4 步）+ 社会关系（第 4.5 步）写入 `greatminds` 库（MySQL），与 Beamer 立传并行。

### 第 0 步：事实基准 【人物专属，已核对】

- **生卒**：1881-12-23 生于西班牙安达卢西亚韦尔瓦省莫格尔（Moguer）～ 1958-05-29 卒于波多黎各圣胡安（享年 76 岁）
- **国籍**：西班牙
- **家庭**：妻 Zenobia Camprubí（西班牙裔作家诗人，1916 年结婚于美国，"不可或缺的伴侣与合作者"）；1900 年父亡致其精神崩溃
- **教育**：耶稣会 San Luis Gonzaga 学校（El Puerto de Santa María）；塞维利亚大学修法律与绘画，后转文学
- **文学师承与影响**：受 **Rubén Darío** 与法国**象征主义**影响（page.md 明载）；提倡 "pure poetry"（纯诗）概念；对波多黎各作家 Giannina Braschi、René Marqués、Aurora de Albornoz、Manuel Ramos Otero 有强文学影响（明载）
- **任职/流亡**：马德里前卫杂志《Prometeo》撰稿人（1908–1912）；西班牙内战爆发后与妻流亡，1946 定居波多黎各；波多黎各大学西班牙语言文学教授，亦任教于迈阿密大学（Coral Gables）与马里兰大学（1981 年该校命名 Jimenez Hall）
- **关键荣誉**：1956 诺贝尔文学奖；墨西哥国立自治大学荣誉博士；1980 年西班牙 2000 比塞塔纸币肖像
- **核心作品与贡献**（4–6 条）：
  1. *Platero y yo*（《小银与我》1914/1917）——散文诗，故乡安魂曲，拉美畅销并译遍美国
  2. *Sonetos espirituales 1914–1916*（《精神十四行诗》1917）——与 Zenobia 新婚后
  3. *Diario de un poeta recién casado*（《新婚诗人的日记》1917）——自由诗转向之作
  4. *Piedra y cielo*（《石头与天空》1919）
  5. *La estación total*（《全季节》1946）/ *Animal de fondo*（《深层动物》1949）——晚期"真实诗"阶段
  6. "纯诗"（pure poetry）倡导——对现代西语诗歌最重要的概念贡献
- **关键时间线**（15 节点）：
  1. 1881-12-23 生于莫格尔
  2. 1890s 耶稣会学校 San Luis Gonzaga
  3. 1900 头两部诗集《Ninfeas》《Almas de violeta》出版（18 岁）
  4. 1900 父亲去世，深度抑郁
  5. 1901–1903 马德里修女疗养院；赴法期间经历
  6. 1904–1910 秘鲁人伪造"Georgina Hübner"书信骗局（未遂赴秘鲁）
  7. 1908–1912 《Prometeo》撰稿
  8. 1914 《小银与我》初版（1917 全版）
  9. 1916 与 Zenobia Camprubí 结婚（美国）
  10. 1917 《精神十四行诗》《新婚诗人的日记》
  11. 1920 与妻合译辛格《骑马下海人》
  12. 1936 西班牙内战爆发，开始流亡
  13. 1946 定居波多黎各；波多黎各大学教授
  14. 1956 获诺贝尔文学奖；**两天后** Zenobia 因子宫癌去世
  15. 1958-05-29 卒于妻子去世的同一诊所；夫妇合葬故乡莫格尔

### 第 4 步：文学领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | pure poetry | 纯诗 | 其核心倡导概念，对现代西语诗最重要贡献 | 核心页 |
| 1 | lyrical poetry | 抒情诗 | 1956 诺奖理由主体 | 封面、核心页 |
| 2 | modernismo | 西语现代主义 | 受 Rubén Darío 影响的起点 | 早年页 |
| 3 | prose poetry | 散文诗 | 《小银与我》体裁 | 代表作页 |
| 4 | literary translation | 文学翻译 | 与妻合译辛格《骑马下海人》 | 伴侣页 |

### 第 4.5 步：社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Zenobia Camprubí | 无向 | 1916 年结婚，终身伴侣与合作者，合译辛格 |
| influence | Rubén Darío | 无向 | 早年受其现代主义影响 |
| influence | Giannina Braschi | 无向 | 波多黎各作家，深受其文学影响 |
| influence | René Marqués | 无向 | 波多黎各剧作家，深受其文学影响 |
| influence | Aurora de Albornoz | 无向 | 波多黎各诗人，深受其文学影响 |
| influence | Manuel Ramos Otero | 无向 | 波多黎各作家，深受其文学影响 |
| colleague | John Millington Synge | 无向 | 与妻合译其剧作《Riders to the Sea》(1920) |

### 第 5 步：设计配色方案 【人物专属】

- **气质**：银白、澄澈、哀而不伤
- **配色**：主色 **#17435B**（分批文件预分配）+ 诺奖香槟金 `#C9A227` + 四分类色
  - `badgeA` 纯诗 — 银蓝 `#5B8BA6`
  - `badgeB` 小银与故乡 — 橄榄绿 `#6B8E5A`
  - `badgeC` 流亡与波多黎各 — 珊瑚橙 `#C96F4A`
  - `badgeD` 诺奖与哀悼 — 香槟金 `#C9A227`
- **背景母题**：柔和气泡（稀疏实心圆错落）+ 细线"手稿横线"暗示书信体诗行

### 第 6 步：规划幻灯片序列 【人物专属，12 页】

```
00  OpenLiterature 项目首页（共享封面 \input）
01  封面 — 纯诗大师 / Juan Ramón Jiménez 1881–1958 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、本名、国籍、出生地、伴侣、任职、荣誉、核心领域）
03  核心贡献概览 — 纯诗 / 抒情诗 / 散文诗 / 文学翻译
04  莫格尔少年 (1881–1900) — 耶稣会学校、18 岁两本处女作、父亡与抑郁
05  疗养院与骗局 (1901–1912) — 马德里疗养、"Georgina Hübner"书信事件、Prometeo
06  小银与我 (1914) — 散文诗代表作书影页 + 名句引文框
07  Zenobia：伴侣与合作者 (1916) — 婚礼、《精神十四行诗》、合译辛格
08  纯诗的炼金术 — "pure poetry" 概念页（意象图式：水晶/银）
09  流亡：从内战到加勒比 (1936–1946) — 波多黎各、迈阿密、马里兰
10  晚期风格 — La estación total / Animal de fondo
11  诺贝尔与告别 (1956–1958) — 领奖两日后丧妻、同诊所离世、合葬莫格尔
12  结尾
```

### 第 7–8 步：版式要点 + 专属陷阱表 【人物专属】

**陷阱**：

| 陷阱 | 说明 |
|------|------|
| 生日双值 | frontmatter 有 12-23/12-24 两值，正文与 infobox 均作 **1881-12-23**，取正文 |
| 全名 | Juan Ramón Jiménez Mantecón；yaml name_en 用 frontmatter 形式 `Juan Ramón Jiménez` |
| 获奖理由 | 官方 EN 为 "…an example of high spirit and artistic purity"，勿改写 |
| 丧妻时点 | 获诺奖**两天后**妻子死于子宫癌；1958 年他死于**妻子去世的同一诊所**——勿写成"同年"或"数月后" |
| 任职地 | 教授职位是波多黎各大学（1946 定居后），迈阿密/马里兰是兼职，勿写"波多黎各大学诺贝尔教授" |
| 疗养院 | 1901–1903 马德里修女办疗养院，非精神病院泛称；法国期间的经历按 page.md 客观简述即可 |
| 骗局事件 | "Georgina Hübner"是秘鲁三人伪造，按 page.md 客观叙述，勿加渲染 |
| 波多黎各影响 | 四位作家名单（Braschi/Marqués/Albornoz/Ramos Otero）明载，勿增删 |
| 无载禁写 | 不写"27 代诗歌分期三阶段"等教科书分类法（page.md 无载）；不写具体师生弟子（无载） |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| pure poetry | 纯诗 | 非瓦雷里同名概念的直接照搬，勿混写 |
| lyrical poetry | 抒情诗 | 诺奖理由主体 |
| prose poetry | 散文诗 | 《小银与我》体裁 |
| modernismo | 西语现代主义 | 与英式 modernism 区分 |
| Platero y yo | 《小银与我》 | 小银是驴（donkey），勿写"小马" |
| Spiritual Sonnets | 《精神十四行诗》 | 1914–1916 期 |
| exile | 流亡 | 内战起，1946 定居波多黎各 |
| Zenobia Camprubí | 泽诺比亚·坎普鲁维 | 伴侣兼合作者，勿只写"妻子" |
| Prometeo | 《普罗米修斯》杂志 | 马德里前卫杂志 1908–1912 |
| Riders to the Sea | 《骑马下海人》 | 辛格剧作，夫妇合译 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**：**Daylight**（分批文件预分配）
- **风格**：明亮 / 温润 / 抒情
- **匹配理由**：契合"小银与我"的银白晨光与安达卢西亚花园意象；纯诗的澄澈感与 Daylight 的透明质感同构；中段哀而不伤的转折呼应丧妻之痛后的流亡岁月。
- **备选**：Nostalgia（乡愁线，但本篇母题以"澄澈"为先）。

---

> **开始执行。每完成一步汇报。**
> **最重要的事：文学家无公式框——用书影/名句引文框/意象图式；每写一页就 make。**
