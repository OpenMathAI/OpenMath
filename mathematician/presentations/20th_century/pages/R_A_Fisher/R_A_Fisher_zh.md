# 费舍尔 (R.A. Fisher) 立传提示词

> 严格遵循 [Mathematician_Biography_Guide.md](./Mathematician_Biography_Guide.md)。参考: cartan, weyl, lebesgue, milnor, morse, zariski, whitney, chevalley, hopf, chern, deligne, witt 的版式。

---

## 背景信息

- **目标**: Sir Ronald Aylmer Fisher (1890–1962)
- **气质关键词**: **现代统计学的数学奠基人、最大似然法的系统化者、数量遗传学和群体遗传学的创始人、抽烟斗的好斗天才、优生学的争议人物**
- **Wikipedia**: `/Users/ericksun/workspace/codebuddy/OpenMathAI/mathematician/pages/Ronald_Fisher/`

## 第 0 步：Wikipedia 校验

- **全名**：Sir Ronald Aylmer Fisher, FRS
- **生卒**：1890-02-17 ~ 1962-07-29，享年 72 岁
- **国籍**：英国
- **出生地**：East Finchley, London, England
- **去世地**：Adelaide, South Australia
- **教育**：Harrow School → Gonville and Caius College, Cambridge (1912 一等荣誉数学)
- **学位导师**：James Hopwood Jeans 和 F.J.M. Stratton（不是"无正式导师"！）
- **任职**：Rothamsted 实验站 (1919–1933) → UCL Galton 优生学教授 (1933–1943) → 剑桥大学遗传学教授 (1943–1957) → 退休后移居 Adelaide
- **荣誉**：FRS (1929)、 Knight Bachelor (1952 封爵)、 Royal Medal (1938)、 Darwin Medal (1948)、 Copley Medal (1955)、 Guy Medal Gold (1946)、 Darwin–Wallace Medal (1958)
- **学生**：C.R. Rao（统计学巨匠）、 Mary F. Lyon（X 染色体失活发现者）、 Walter Bodmer、 D.J. Finney
- **争议一**：与 Karl Pearson 长达 20 年的统计学方法之争——χ² 优先权、自由度定义。Fisher 赢了。
- **争议二**：与 Jerzy Neyman 关于 fiducial 推断 vs 置信区间的争论——从未和解。
- **争议三**：1957 年 BBC 采访否认吸烟与肺癌的因果关联——被历史证明错误。
- **争议四**：**优生学**——Fisher 是 Galton 优生学教授、Annals of Eugenics 主编、终身相信优生学。近年多所机构移除他的纪念。如实呈现，不过度美化也不过度审判。
- **配偶**：Ruth Eileen Guinness (1917 结婚)，2 子 6 女。
- **视力**：终身严重近视——因此被拒绝参加一战。但也因此发展了不依赖纸笔证明的几何直觉。

### 时间线
- 1890-02-17: 生于伦敦 East Finchley 中产阶级家庭
- 1904: 母因腹膜炎去世 (14岁)；18 个月后父亲生意失败
- 1909: 获剑桥 Gonville & Caius 学院奖学金
- 1912: 剑桥数学一等荣誉毕业
- 1913–1919: 在伦敦金融城做统计师 + 公立学校教书
- 1915: 发表《性偏好的进化》——性选择的早期研究
- 1917: 与 Ruth Eileen Guinness 结婚
- 1918: **发表里程碑论文**：《基于孟德尔遗传的亲属间相关性》——引入"方差"(variance) 概念，统一孟德尔遗传与 Darwin 自然选择，开创数量遗传学
- 1919: 拒绝 Karl Pearson 的 Galton 实验室邀请，加入 Rothamsted 实验站
- 1921: 引入"似然"(likelihood) 概念；发表 ANOVA 首篇应用论文
- 1922: 《理论统计学的数学基础》——现代统计学奠基之作
- 1924: 引入 F-分布（当时称 Fisher's z-distribution）
- 1925: 《研究者的统计方法》——经典教材，引入 Fisher 信息量
- 1930: 《自然选择的遗传理论》——群体遗传学的圣经，Darwin 和 Mendel 的数学综合
- 1933: 接替 Karl Pearson 任 Galton 优生学教授 (UCL)
- 1935: 《实验设计》——随机化、区组设计、拉丁方、**"女士品茶"**（Fisher 精确检验的起源故事）
- 1943–1957: 剑桥大学遗传学教授 (Arthur Balfour Chair)
- 1947: 与 Cyril Darlington 共同创办 *Heredity* 期刊
- 1952: 封爵——Sir Ronald Fisher
- 1957: BBC 采访中否认吸烟与肺癌因果关联（后来被流行病学证明错误）
- 1957: 退休后移居澳大利亚 Adelaide，在 CSIRO 做研究员
- 1962-07-29: 在 Adelaide 因结肠癌去世，享年 72 岁
- 1998: 女儿 Joan Fisher Box 出版传记《R.A. Fisher: The Life of a Scientist》

### 人格画像
Fisher 可能是 20 世纪科学家中最好斗的天才。他抽烟斗（经典英国绅士形象），但性格极度暴躁、从不妥协。他与 Karl Pearson 的统计学战争持续了 20 年——从 1910s 到 Pearson 1936 年去世。他与 Neyman 关于 fiducial 推断的争论从未和解。他的统计学无可挑剔——但他在吸烟争议中的立场被历史证明是错误的。他终身相信优生学——这是他的履历中最难面对的部分。但他也是现代统计学的缔造者——最大似然、ANOVA、实验设计、Fisher 信息量、充分统计量、p 值……没有 Fisher，就没有现代统计学。Richard Dawkins 称他为"达尔文之后最伟大的进化生物学家"。统计学界称他为"20 世纪统计学最重要的人物"。

## 第 0.5 步：数据库字段核对（★ 补全 greatminds，规范见工作指南 §二十一）

> 对照 metadata.json 逐项核对下表并填值。缺失项按 §21.5 写 `MySQL/seed_fisher_full.py` 补齐。

| # | 表 | 字段 | 核对值 | 库中现状 |
|:--:|---|------|--------|:--:|
| 1 | `people` | qid | `Q216723` | ⚠️ 待核 |
| 2 | `people` | name_zh | `罗纳德·艾尔默·费希尔` | ⚠️ NULL |
| 3 | `people` | name_variants | `["统计学的巨人","现代统计学的奠基人","R.A. Fisher","遗传学与统计学之父"]` | ⚠️ 空 |
| 4 | `people` | gender | `male` | ⚠️ NULL |
| 5 | `people` | birth_date / death_date | `1890-02-17` / `1962-07-29` | ⚠️ **NULL 全缺** |
| 6 | `people` | description | `British statistician and geneticist (1890–1962)` | ⚠️ 待核 |
| 7 | `person_occupation` | 职业 | `mathematician(0)`、`statistician(1)`、`geneticist(2)`、`astronomer(3)`、`biostatistician(4)` | ⚠️ 需补（biostatistician 补字典） |
| 8 | `person_field` | 领域 | `statistics`、`genetics` | ⚠️ 待核 |
| 9 | `award_laureate` | 获奖 ★全部收录 | `Weldon 1930`、`Royal Medal 1938`、`Guy Gold 1946`、`Darwin 1948`、`Copley 1955`、`FRS`、`Knight Bachelor`、`Darwin–Wallace`、`Croonian` | ⚠️ 空 |
| 10 | `person_institution` | 教育/任职 | `education: Cambridge、Harrow`；`employment: Rothamsted(1919–1933)、UCL(1933–1943)、Cambridge(1943–1957)、Adelaide(1959–1962)` | ⚠️ 全空 |
| 11 | `person_nationality` | 国籍 | `United Kingdom` | ⚠️ 待核 |
| 12 | `person_relation` | 社会关系 | 见第 4.5 步（8 条） | ⚠️ 全空 |
| 13 | `rankings` | 榜单 | `OpenMath_20th_Century_Top50` 待查 | ⚠️ |

## 第 4.5 步：社会关系梳理 + 数据库入库 ★（数据库同步）

> 完整规范见工作指南 **§二十**。新建 `MySQL/seed_fisher_relations.py`。

**入库范围（8 条）**：

| 关系类型 | 人物 | 方向 | 状态 |
|---|---|---|---|
| 导师 | James Hopwood Jeans → Fisher | 有向 | ⚠️ 占位 |
| 导师 | F. J. M. Stratton → Fisher | 有向 | ⚠️ 占位 |
| 学生 | Fisher → C. R. Rao | 有向 | ⚠️ 占位 |
| 学生 | Fisher → Walter Bodmer | 有向 | ⚠️ 占位 |
| 同事 | Karl Pearson | 无向 | ⚠️ 占位（统计学两大巨头之争） |
| 同事 | Jerzy Neyman | 无向 | ⚠️ 占位（Fisher–Neyman 频率学派之争） |
| 同事 | William Sealy Gosset | 无向 | ⚠️ 占位（Student's t，长期通信） |
| 同事 | J. B. S. Haldane | 无向 | ⚠️ 占位（群体遗传学三巨头） |

- 缺失人物（8 人）先建占位，note 加 `[材料待展开]`；幂等 `INSERT IGNORE`

---

## 核心贡献

| 领域 | 具体贡献 | 年代 |
|------|---------|:--:|
| 统计学 | **最大似然估计**的系统化与推广 | 1921–1925 |
| 统计学 | **方差分析 (ANOVA)** | 1918–1921 |
| 统计学 | **Fisher 信息量** | 1925 |
| 统计学 | **充分统计量**、辅助统计量 | 1920s |
| 统计学 | **F-分布** (Fisher's z-distribution → F-distribution) | 1924 |
| 统计学 | **Fisher 精确检验** (女士品茶) | 1935 |
| 统计学 | **fiducial 推断** (争议性) | 1930s |
| 实验设计 | **随机化、区组设计、拉丁方**、因子设计 | 1920s–1935 |
| 遗传学 | **数量遗传学**——Mendel 与 Darwin 的数学统一 | 1918 |
| 遗传学 | **群体遗传学**——与 Haldane, Wright 并称三巨头 | 1930 |
| 遗传学 | **Fisher 自然选择基本定理** | 1930 |
| 遗传学 | **Fisherian runaway**——性选择的失控模型 | 1915/1930 |
| 生物学 | **基因映射 (linkage analysis)** 先驱 | 1930s |
| 信息论 | **Fisher 信息**——与 Shannon 并行发展的信息理论 | 1925 |

### ★ 叙事主线
1. **现代统计学的建筑师** — 在 Fisher 之前，统计学是直觉和公式的混合物。之后，它成为了一门严格的数学学科。最大似然、ANOVA、充分统计量、随机化——他创建了统计学的语言。
2. **Mendel 与 Darwin 的统一 (1918)** — 这篇论文证明了离散遗传（孟德尔颗粒）可以产生连续变异（达尔文自然选择的基础）。这是现代进化生物学的数学起源。同时发明了"方差"一词和 ANOVA。
3. **Rothamsted 的农业革命** — 14 年时间，从 1840s 以来的数百万条农田数据中，提炼出了实验设计的全部原则。随机化、区组、拉丁方——这些都来自对萝卜和小麦的实验。
4. **与 Pearson 的战争** — 长达 20 年的统计学方法之争。Pearson 是当时英国统计学的霸主——Fisher 是挑战他的年轻人。关于 χ² 的自由度、最大似然 vs 矩估计、充分统计量——Fisher 几乎在所有论战中都赢了。
5. **女士品茶与 Fisher 精确检验** — 统计学的经典起源故事：一位女士声称她能分辨茶是先加牛奶还是先加茶。Fisher 设计了一个实验来检验——这就是 Fisher 精确检验的起点。统计学从"女士品茶"开始。
6. **吸烟争议 (1957)** — Fisher 用他一生捍卫的方法论——"相关不等于因果"——来否认吸烟与肺癌的因果关联。这一次，他是错的。这个故事提醒我们：即使是最伟大的方法论者，也可能被自己的偏见所蒙蔽。
7. **优生学的阴影** — Fisher 是 Galton 优生学教授、Annals of Eugenics 主编、终身优生学倡导者。2020s 以来，多所机构移除了对他的纪念。这是一个必须如实面对的争议——他的科学成就是伟大的，但他的优生学信念是不可否认的。

## ⚠️ 史实陷阱
- **"发明"最大似然** — Gauss (1821) 和 Edgeworth (1908) 早已使用。Fisher 的贡献是系统化、推广和证明渐近性质。
- **F-分布命名** — Fisher 本人称之为 "z-distribution"。Snedecor 在 1934 年重新命名为 F-分布（F = Fisher）。所以 F 是 Snedecor 命名的——Fisher 自己没用这个名字。
- **吸烟争议** — 1957 年 BBC 广播 "The Cancer Controversy"。Fisher 的论点是"相关≠因果"——方法论上严格，但被流行病学证据压倒。正确叙述：他固守了统计学的严格标准，但这次标准错了。
- **优生学** — Fisher 是 Galton 优生学教授，编辑 Annals of Eugenics，终身优生学倡导者。如实呈现——不美化，不过度审判。
- **学位导师** — 不是"无正式导师"！James Hopwood Jeans 和 F.J.M. Stratton 是正式学位导师。虽然没有正式"PhD"（剑桥当时系统不同），但有学术指导者。
- **方差一词** — Fisher 在 1918 年论文中创造了 "variance" 这个词。
- **p 值** — Fisher 推广了 p 值概念（p < 0.05 作为显著性标准来自他），但他后来也警告不要机械地使用 p 值。

## ⚠️ 终审高危
| 高危点 | 正确值 | 常见错误 |
|--------|--------|----------|
| 学位导师 | James Jeans + F.J.M. Stratton | "无正式导师" |
| 最大似然 | 系统化推广, 非首创 | "发明"最大似然 |
| F-分布 | Fisher 称 z-distribution, Snedecor 命名 F | Fisher 自己命名 |
| 吸烟争议 | 1957 BBC, Fisher 错了 | 弱化为"有争议" |
| 优生学 | Galton 教授, Annals of Eugenics 主编 | 遗漏 |
| 方差一词 | Fisher 1918 创造 "variance" | 遗漏 |

## 配色：统计蓝 + 烟斗褐 + 遗传绿 + 象牙白
- **badgeStat** (统计学) — 统计蓝 `#003366`
- **badgeGenet** (遗传学/进化) — 烟斗褐 `#8B5A2B`
- **badgeDesign** (实验设计) — 遗传绿 `#2E5A40`
- **badgeLegacy** (遗产) — 象牙白 `#E8DCC8`
- **coveraccent** — 统计蓝 `#003366`
- **coverprimary** — 墨色 `#111827`
- **bgmain** — 暖象牙白 `RGB{248,246,243}`

## 幻灯片（15 页内容 + 封面 + 结束 = 17 页）

### 0. OpenMath 项目首页
### 1. 封面 — 《费舍尔：统计学的数学奠基人》
### 2. Hook — 四面板：最大似然 · ANOVA · Mendel-Darwin统一 · 实验设计
### 3. 早年：伦敦天才少年 (1890–1912)
### 4. 1918: 一篇论文改变一切 — Mendel × Darwin, 方差, ANOVA 同时诞生
### 5. Rothamsted 14 年 (1919–1933) — 从农田数据中提炼统计学
### 6. 最大似然与 Fisher 信息 (1921–1925) — 统计学的方法论革命
### 7. 女士品茶与实验设计 (1935) — 随机化·区组·拉丁方·Fisher精确检验
### 8. 《自然选择的遗传理论》(1930) — 群体遗传学的圣经
### 9. Fisherian Runaway — 为什么孔雀有那么长的尾巴？
### 10. 与 Pearson 的 20 年战争 — 统计学的霸主争夺战
### 11. Galton 优生学教授 (1933–1943) — 优生学的争议
### 12. 吸烟争议 (1957) — 伟大的方法论者为何犯了错？
### 13. Knight Bachelor & 大满贯荣誉 — FRS · Copley · Darwin · Guy 金质奖章
### 14. 遗产：以 Fisher 命名的概念 — 从 F-分布到 Fisher 信息
### 15. 结束页 — "To call in the statistician after the experiment is done..."

## 音乐: Timeless + Expedition

## Round 2 高危: 学位导师 Jeans+Stratton、最大似然非首创、F-分布命名者 Snedecor、吸烟争议 1957、优生学身份。

> **开始执行。**
