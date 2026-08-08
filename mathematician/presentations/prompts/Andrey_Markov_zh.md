# 马尔可夫 (Andrey Markov) 立传提示词

> 严格遵循 [Mathematician_Biography_Guide.md](./Mathematician_Biography_Guide.md)。

---

## 背景信息

- **目标数学家**: Andrey Markov (1856–1922)
- **气质关键词**: **Markov链之父、随机过程的先驱、Chebyshev的传人、概率论的独立灵魂**
- **Wikipedia 页面**: ✅ 已下载
  - 路径: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Andrey_Markov/`
  - Wikipedia 英文条目: `Andrey Markov`
- **Beamer 文件**: `mathematician/presentations/Andrey_Markov/Andrey_Markov_zh.tex` (12页)
  - 编译: `make distclean && make` — 885KB PDF, 零错误
- **参考模板**: `wiener/`, `ramanujan/`, `hardy/` 的完整源码
  - `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/wiener/Norbert_Wiener_zh.tex` — Wiener 完整源码
  - `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/grothendieck/Makefile` — 构建脚本（直接复制）
- **操作指南**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/presentations/Mathematician_Biography_Guide.md`
- 注意：此 Markov 是 **Andrey Markov Sr. (1856-1922)**，不是他儿子 Andrey Markov Jr. (1903-1979，构造性数学家)

---

## 第 0 步：下载 Wikipedia 页面并校验 ✅

已下载到 `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Andrey_Markov/`

- **全名**: Andrey Andreyevich Markov (Андре́й Андре́евич Ма́рков)
- **生卒日期**: 1856-06-14 ~ 1922-07-20，享年 **66** 岁
- **国籍**: 🇷🇺 Russian Empire / Russian SFSR（俄国→苏联过渡期）
- **出生地**: Ryazan（梁赞），Russia
- **逝世地**: Petrograd（彼得格勒，即圣彼得堡），Russia
- **博士导师**: Pafnuty Chebyshev（帕夫努季·切比雪夫）
- **教育经历**:
  - St. Petersburg Grammar School（除数学外成绩平平，被认为叛逆）
  - St. Petersburg Imperial University（圣彼得堡帝国大学）
  - 1877: 金牌论文 — 用连分数积分微分方程
  - 1880: 硕士论文 "On the Binary Square Forms with Positive Determinant"
  - 1884: 博士论文 "On Certain Applications of the Algebraic Continuous Fractions"
- **主要任职机构**:
  - 1880–1905: St. Petersburg University（讲师→副教授→正教授）
  - 1886: 圣彼得堡科学院 adjunct → 1890 extraordinary → 1896 ordinary member（接替Chebyshev）
  - 1905: merited professor，随即退休（但继续授课至1910）
- **关键荣誉**:
  - Order of Saint Stanislaus, 2nd class
  - Order of Saint Anna, 2nd class
  - 1913: 当选圣彼得堡大学荣誉会员（被教育大臣否决，1917二月革命后才确认）
- **重要学生**:
  - Abram Besicovitch（实分析）
  - Alexander Friedmann（宇宙膨胀方程 — Friedmann 方程！）
  - Nikolai Günther（数学物理）
  - Veniamin Kagan（张量分析/微分几何）
  - Jacob Tamarkin（泛函分析）
  - J. V. Uspensky（概率论/数论）
  - Georgy Voronoy（Voronoi 图！）
- **家族**:
  - 弟弟 Vladimir Markov (1871–1897): Markov 兄弟不等式，25岁死于肺结核
  - 儿子 Andrey Markov Jr. (1903–1979): 构造性数学、递归函数论
- **研究领域**: probability theory, mathematical analysis, number theory, stochastic processes, Markov processes

### 关键时间线（15个节点）：

- 1856: 6月14日生于俄罗斯 Ryazan
- 1874: 进入圣彼得堡帝国大学，师从 Chebyshev, Sokhotski, Korkin, Zolotarev 等人
- 1877: 获大学金牌奖——用连分数积分微分方程
- 1880: 完成硕士论文（Korkin & Zolotarev 指导），秋季开始以 privatdozent 身份授课
- 1884: 完成博士论文 "On Certain Applications of the Algebraic Continuous Fractions"
- 1886: 任圣彼得堡大学 extraordinary professor，当选科学院 adjunct
- 1890: 当选科学院 extraordinary member（接替 Bunyakovsky）
- 1894: 晋升圣彼得堡大学 ordinary professor
- 1896: 当选科学院 ordinary member（接替 Chebyshev）
- 1905: 获 merited professor 头衔并退休（但继续授课至1910）
- 1906: 发表划时代论文 "Extension of the limit theorems of probability theory to a sum of variables connected in a chain" — **Markov 链正式诞生**
- 1908: 因拒绝监控学生被解除教学职务
- 1912: 回应 Tolstoy 被逐出教会——主动请求也被逐出教会（教会照办）
- 1913: 分析 Pushkin《Eugene Onegin》前 20,000 个字母的元音/辅音转移概率 — **Markov 链首次经验应用**
- 1917: 二月革命后重新获准教学，讲授概率论与差分学
- 1922: 7月20日逝世于 Petrograd，享年 66 岁

### 人格特质线索：

- **无神论者+冷幽默** — 1912年托尔斯泰被逐出教会，Markov 写信给神圣宗教会议要求把自己也逐出教会（"我也不同意的你们的教义"），教会照办了
- **拒绝服膺权威** — 1908年拒绝监控学生，宁可被解职也不当"政权的代理人"
- **数学上的反叛者** — Markov 链的动机是反驳 Nekrasov 的宗教论证（大数定律需要独立=自由意志=神），用数学本身反驳神学
- **圣彼得堡学派第二代领袖** — Chebyshev 的指定继承人，概率论从 Chebyshev 到 Markov 到 Kolmogorov 的承上启下者
- **强棋手** — Wikipedia 专门提了一句 "He was also a strong chess player"

### ★ 叙事亮点：

1. **一个意外的诞生** — Markov 链不是被"推导"出来的，而是 Markov 为了挑战一个宗教观点而发明的数学工具。Nekrasov 声称大数定律需要独立性（体现自由意志→上帝存在），Markov 说："我来证明给你看——依赖性也可以。"最终成为信息时代的基础设施。
2. **Eugene Onegin：第一组经验数据** — Markov 亲手统计 Pushkin 长诗中元音和辅音的转移概率。这是 Markov 链的第一次经验应用。从诗歌到 PageRank，100年的跨度。
3. **Chebyshev 的传人** — 概率论史上最辉煌的传承线：Chebyshev → Markov → Kolmogorov。Markov 是承上启下的一环。
4. **Markov 不等式** — $P(X \geq a) \leq E[X]/a$。整个概率论中最优美、最常用的不等式之一。
5. **独立灵魂** — 拒绝监控学生、主动被逐出教会。他的数学独立性是他整个人格的延伸。
6. **Markov 数** — 丢番图方程 $x^2+y^2+z^2=3xyz$ 的解形成一棵美丽的 Markov 树，与双曲几何、Fermat 数之间有着神秘联系。

### ★ 重要区分

| Markov Sr. (1856–1922) | Markov Jr. (1903–1979) |
|------------------------|------------------------|
| Markov 链、随机过程 | 构造性数学、递归函数论 |
| 概率论 | 证明了维数≥4的拓扑流形的同胚分类是算法不可解的 |

---

## 第 5 步：设计配色方案

- **建议配色：链金 + 俄式深红 + 概率红 + 象牙纸** —— 帝国俄罗斯学术传统 + 随机过程的"链"隐喻 + 概率论的温度
- 与已有配色完全不同！

- 主要色值：
  | 用途 | 色名 | 建议色值 | 说明 |
  |------|------|---------|------|
  | 背景 | `bgmain` | `#FCF9F4` | 象牙白 —— 旧俄罗斯学术手稿的颜色 |
  | 主色 | `coverprimary` | `#2D1B0A` | 深棕 —— 皮革装订的学术传统 |
  | 强调色 | `coveraccent` | `#C44536` | 概率红 —— Markov 不等式的颜色 |
  | 深色文本 | `coverdark` | `#2A1A0A` | 暗棕 |
  | 浅色文本 | `covermuted` | `#7A6A58` | 灰棕 |

- 四个分类色，对应 Markov 的四大支柱：
  - **badgeChains** (Markov链) — 链金 `#C4893C`
  - **badgeProbability** (概率论) — 概率红 `#C44536`
  - **badgeNumberTheory** (数论) — 数论青 `#3A6B5C`
  - **badgeLegacy** (遗产) — 石版灰 `#4A5568`

---

## 第 6 步：规划幻灯片序列（12 页）

```
00  OpenMath 项目首页

=== 封面与总览 ===
01  封面 — 《马尔可夫：随机世界的建筑师》 / Andrey Markov 1856–1922
02  Hook — 为什么马尔可夫独一无二

=== 生平与核心贡献 ===
03  早年与教育 (1856–1880) — Ryazan·圣彼得堡大学·Chebyshev门下·金牌论文
04  Markov 链的诞生 (1906) — 挑战宗教论证·Eugene Onegin字母统计·依赖变量的数学
05  从 Pushkin 到 PageRank — Markov 链的世纪之旅·信息时代的地下基石
06  概率论的基石 — Markov 不等式·大数定律·中心极限定理的推广

=== 学派与传承 ===
07  Chebyshev 的传人 — 圣彼得堡概率学派的第二代领袖·从Chebyshev到Kolmogorov
08  数论与连分数 — Markov 数·丢番图逼近·Markov 兄弟不等式

=== 人格与遗产 ===
09  无畏的独立灵魂 — 拒绝监控学生·主动被逐出教会·数学与良知的统一
10  Markov 家族与持久遗产 — 弟弟Vladimir·儿子Markov Jr.·以Markov命名的一切

=== 结尾 ===
11  结束页 — "他只想反驳一个神学的论证——却创造了整个随机世界。"
```

---

## 第 9 步：史实审查

### Markov 特有的史实陷阱

| 陷阱类型 | 高危点 |
|---------|--------|
| **Markov Sr. vs Markov Jr.** | 必须明确区分！证明"维数≥4流形拓扑同胚分类不可解"的是Jr.，不是Sr. |
| **"两个生日"** | 儒略历 6月2日 = 公历 6月14日。用公历。 |
| **Markov 链不是"发明"** | Markov 首次严格定义了相依随机变量的链式结构——不是"发明"而是"发现"或"提出" |
| **Nekrasov 论证** | Nekrasov 的论证涉及神学，但不宜过度渲染其荒谬性。对历史人物保持尊重。 |
| **Markov不等式 ≠ Chebyshev不等式** | Chebyshev 首先发现但Markov 系统化推广。两者密切相关但不同。 |
| **"PageRank 之父"** | 不准确。PageRank 使用了 Markov 链，但 Markov 不可能预知互联网。表述为"PageRank 的数学基础" |
| **主动被逐出教会** | 这是冷幽默式的抗议行为，不是悲剧。语气应是"讽刺"而非"悲壮"。 |

---

## 第 13 步：Wikipedia 本地文档终审（提交前必做）

### 终审清单
- [x] 生卒日期与 metadata.json 一致
- [x] 国籍 "Russian Empire / Russian SFSR" 正确
- [x] 博士导师 Pafnuty Chebyshev 正确
- [x] Markov 链首次发表年份 1906 正确
- [x] Eugene Onegin 分析年份 1913 正确
- [x] 拒绝监控学生事件 1908 正确
- [x] 主动请求逐出教会 1912 正确
- [x] Markov Sr. 与 Jr. 清楚区分
- [x] 编译: `make distclean && make` — 885KB PDF, 零错误

---

> **开始执行。每完成一步向我汇报。**
>
> **特别提醒：**
> 1. Markov 链不是精心设计的成果——它是一个偶然的副产品，源于 Markov 对宗教论证的愤怒
> 2. 不要过度浪漫化 Nekrasov 论证——保持历史学家的冷静
> 3. Markov 的人格和他的数学一样独立——拒绝监控、挑战教会
> 4. Markov 不等式是最优美的简单不等式之一——可以适当突出
> 5. Markov 数是一个容易被忽略但极其优美的数论贡献
> 6. 结尾应回归"偶然与必然"的主题

## 第 14 步：背景音乐选择 ✅

- **选定曲目**: **SEA** — Alex-Productions (75k views)
- **风格**: 流动 / 平稳 / 概率、动力系统、连续叙事
- **匹配理由**:
  - "概率" — 曲目库中唯一标注"概率"标签的曲目，与 Markov 链/随机过程核心领域直接重合
  - "流动" — Markov 链 = 状态之间的流动转移，"链"的隐喻完美匹配 SEA 的平稳律动
  - "连续叙事" — 从 Pushkin 诗歌字母统计到 PageRank 的世纪叙事
  - 不像 "New Lands" 过于宏大，不像 "Savage" 过于紧张——平稳推进的气质正合 Markov 推演数学的风格
- **本地路径**: `music_audio/alex-productions/92-WEqfdRXU3IU-SEA.wav` → `presentations/Andrey_Markov/SEA.wav`
- **时长**: 177 秒 (≈3 分钟) > 12 页 × 7 秒 = 84 秒 → ffmpeg `-shortest` 自动对齐
- **Makefile**: `BGM = $(wildcard *.wav)` — 自动检测并混入