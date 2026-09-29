# Francis William Aston（弗朗西斯·威廉·阿斯顿）立传提示词

> qid=Q102291 · 1877-09-01 – 1945-11-20 · 英国化学家/物理学家 · 20 世纪 · 诺贝尔化学奖（1922，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Francis_William_Aston/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页 + 气泡背景。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/` 就位后使用；page.md 实载 "Aston in 1922" 照片与质谱仪复制品图可供选用）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{magnet}\enspace 称量原子的人\enspace·\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）——紫色圆点按质荷比弧线排布，暗示「质谱抛物线轨迹」母题。
5. **表格语义化 + 公式框**（★ 核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 仪器 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）——整数规则是天然公式框素材。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Francis William Aston（中文惯称：弗朗西斯·威廉·阿斯顿；FRS）
- **生卒**：1877-09-01 生于英格兰伯明翰 Harborne（今属伯明翰）→ 1945-11-20 逝于英格兰剑桥，享年 68
- **国籍**：United Kingdom（英国）
- **身份**：化学家兼物理学家（质谱仪发明者；非放射性元素同位素发现者；整数规则提出者）
- **家庭**：父 William Aston 与母 Fanny Charlotte Hollis 之第三子（次子）；**终身未婚**（page.md 明载）
- **教育轨迹**：Harborne Vicarage School → Malvern College（寄宿）→ Mason College（伦敦大学附属外部学院，1893 入学；Poynting 教物理、Frankland 与 Tilden 教化学）→ 伯明翰大学（BSc 1910 / DSc 1914；Forster Scholarship 资助师从 Frankland）
- **导师**：Percy F. Frankland（infobox Doctoral advisor；1898 年起以其奖学金学生身份研究酒石酸光学性质）；J. J. Thomson（卡文迪什邀请人与合作者，infobox Other academic advisors）
- **博士**：无传统 PhD（伯明翰 BSc 1910 / DSc 1914）
- **研究领域**：质谱学、同位素、放电管物理（Aston 暗区）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **伯明翰第三子（1877）**：Harborne 出生，Malvern College 寄宿。
2. **自家实验室（1896–）**：在父亲宅邸的私人实验室研究有机化学。
3. **酿酒与发酵（1898–1903）**：Forster Scholarship 师从 Frankland 研究酒石酸衍生物光学性质；在伯明翰酿酒学校研究发酵化学，1900 年受雇于 W. Butler & Co. 酿酒厂，1903 年返伯明翰大学任 Poynting 的 Associate。
4. **放电管与 Aston 暗区**：自制冷阴极放电管研究气体导电，研究阴极暗区体积——以他命名的 **Aston dark space**。
5. **环游世界与卡文迪什（1908–1910）**：父亲去世后环球旅行；1909 年任伯明翰讲师；1910 年应 J. J. Thomson 之邀赴剑桥卡文迪什实验室。
6. **阳射线分离术（卡文迪什时期）**：Thomson 研究Goldstein 发现的"Kanalstrahlen"；Wien（1908）发现磁场偏转法；磁+电场组合让不同质荷比离子留下抛物线痕迹——**首次证明同一元素的原子可以有不同质量**；第一台扇形场质谱仪由此诞生。
7. **氖 20 与 22（1912）**：发现氖分成两束，对应原子量约 20 与 22；他把 22 的那份命名为 "meta-neon"（名字取自神秘学小册 *Occult Chemistry*）——同位素存在的最初线索。
8. **一战中断（1914–1918）**：在 Farnborough 皇家飞机厂任技术助理，研究航空涂层；质谱研究停滞。
9. **第一台质谱仪（1919）**：战后回卡文迪什建成第一台质谱仪并发表报告；后续第二、第三台不断提高分辨率与精度——借助电磁聚焦共鉴定 **212 种天然同位素**。
10. **整数规则（whole number rule）**：以氧同位素 16 为基准，"所有其他同位素的质量都非常接近整数"；该规则在核能发展中被大量使用；氢质量比平均值高 1% 的精确测量引出亚原子能量之思（1936 年著文 speculation）。
11. **1921 双喜**：当选皇家学会会士（FRS）并加入国际原子量委员会。
12. **1922 诺贝尔化学奖**：官方理由 "for his discovery, by means of his mass spectrograph, of isotopes in many non-radioactive elements and for his enunciation of the whole number rule"；同年获 Hughes Medal；诺奖演讲 1922-12-12 *Mass Spectra and Isotopes*。
13. **运动家与摄影家（私生活）**：滑雪、滑冰、登山、游泳、高尔夫（常与 Rutherford 及剑桥同事挥杆）、网球（公开赛获奖）、1909 年在檀香山学冲浪；1902 年自制内燃机、1903 年参加爱尔兰 Gordon Bennett 汽车赛；会钢琴/小提琴/大提琴并在剑桥音乐会上演奏；多次参加日食观测远征（1925 Benkoeben、1932 苏门答腊与加拿大、1936 北海道）；1945-11-20 逝于剑桥；月球环形山 Aston 与英国质谱学会 Aston Medal 以其命名。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（绛紫 violet） | `#52307C` | 质谱抛物线的深紫（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（质谱仪 badgeMS） | `#2E5A9E` | 蓝质谱仪三代演进 |
| 分类色 2（同位素 badgeIsotope） | `#1B7A43` | 绿 212 种天然同位素 |
| 分类色 3（整数规则 badgeRule） | `#D97B29` | 琥珀 whole number rule |
| 分类色 4（探索 badgeTravel） | `#C0395B` | 玫瑰日食远征 / 环球旅行 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落）——紫色圆点沿弧线排布，暗示「质谱抛物线」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Savage** — Alex-Productions（文件 `music_audio/alex-productions/34-pILVwyuW3jw-Savage.wav`，勿复制 wav）
- **风格**：精密 / 机械律动 / 探索感
- **匹配理由**：
  - "精密" 匹配质谱仪的毫米级聚焦与百万分之一精度的称量
  - "机械律动" 匹配其工程师气质——自制内燃机、自研三代仪器
  - "探索感" 匹配其运动家与远征者的一面——从檀香山冲浪到北海道日食
- **时长**：以实际曲目时长为准，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 称量原子的人 / Francis William Aston 1877–1945 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  阿斯顿的一生 — Sanger 式时间线（10 节点：1877→1893→1900→1909→1910→1912→1919→1921→1922→1945）
04  早年：伯明翰与酿酒厂 (1877–1903) — 表格「时间|事件|结果」
05  放电管与 Aston 暗区 (1903–1909) — 表格「对象|方法|命名」
06  卡文迪什与阳射线 (1910–1912) — 表格「人物|方法|发现」（Thomson / Wien / 抛物线痕迹）
07  氖 20 与 22：meta-neon (1912) — 表格「现象|命名|意义」
08  一战中断 (1914–1918) — 表格「地点|职务|影响」（Farnborough 航空涂层）
09  第一台质谱仪 (1919–1921) — 表格「仪器|原理|战果」+ 公式框：m/z 分离（磁×电场聚焦）
10  整数规则 (1919–1936) — 表格「基准|表述|应用」+ 公式框：m(isotope) ≈ 整数（¹⁶O 基准）
11  1922 诺贝尔化学奖 — 表格「理由|演讲|同年」（官方英文理由原文；1922-12-12；Hughes Medal）
12  运动家·音乐家·远征者 — 表格「领域|事迹|年份」（Gordon Bennett 1903 / 檀香山 1909 / 日食 1925-1936）
13  遗产：从同位素到核时代 — 四分类遗产盒（质谱 / 同位素 / 整数规则 / 仪器谱系）+ Aston crater + Aston Medal
14  结尾 — 「给每一个原子一个准确的重量。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1922 诺奖口径 | 官方英文理由原文："for his discovery, by means of his mass spectrograph, of isotopes in many non-radioactive elements and for his enunciation of the whole number rule"——**独享**；强调"非放射性元素"；勿写成"发明同位素" |
| 博士导师口径 | infobox Doctoral advisor = **Percy F. Frankland**；frontmatter 却列 J. J. Thomson——以正文 infobox 为准：Frankland 为导师，Thomson 是卡文迪什邀请人 + Other academic advisors，入库按 colleague |
| meta-neon 命名 | 名字取自神秘学小册 *Occult Chemistry*——如实提及即可，勿渲染神秘主义；他最初用的是 "meta-neon" 而非今天术语 |
| 同位素概念归属 | "isotope" 术语与概念（放射性元素）属 Soddy（1913）；Aston 的贡献是**用质谱仪证明非放射性元素也有同位素**——两篇勿混 |
| 一战 | 任皇家飞机厂技术助理研究**航空涂层**——勿写成军事武器研发 |
| 212 种同位素 | 是三代仪器累计鉴定的**天然同位素总数**——勿写"一次发现" |
| 氢 1% | "氢质量比其他元素平均值预期高 1%"——是亚原子能量的线索之一（1936 speculation）；勿写"预言核能" |
| 终身未婚 | page.md 明载 "He never married"——身份信息页与私生活页口径一致 |
| 体育与远征 | Gordon Bennett 汽车赛 1903（爱尔兰）、檀香山学冲浪 1909、日食远征 1925/1932×2/1936（北海道 Kamishari，1936-06-19）——年份勿错；原计划 1940 南非、1945 巴西远征未成行 |
| 引语红线 | page.md 几乎无引语——中文引号内不得出现任何无源"原话"，整数规则的英文定义可用 page.md 明载那句 |
| 品牌口径 | 结尾页品牌写 `OpenMathAI`；引号半角 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q102291 | ✅ |
| name_zh | 弗朗西斯·威廉·阿斯顿 | ✅ |
| name_en | Francis William Aston（库内既有记录 id=2952，精确复用回填 QID） | ✅ |
| birth_date | 1877-09-01 | ✅ |
| death_date | 1945-11-20 | ✅ |
| nationality | United Kingdom | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | chemistry（person_field 细分见下表） | ✅ |

**person_field 细分（rank 表）**：

| name_en | rank | name_zh |
|---|---|---|
| mass spectrometry | 0 | 质谱学 |
| isotope research | 1 | 同位素研究 |
| physics | 2 | 物理学 |
| electrochemistry（放电管） | 3 | 气体放电 |

## 7. 社会关系入库清单

**师长 / 同事**（★红线：只收 page.md 正文或 infobox 明载的关系）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Percy F. Frankland | 师→生（导师） | 1898 年起 Forster Scholarship 学生，研究酒石酸光学性质；infobox Doctoral advisor |
| colleague | J. J. Thomson | 无向 | 1910 邀其入卡文迪什；阳射线（Kanalstrahlen）研究合作；infobox Other academic advisors |
| colleague | Ernest Rutherford | 无向 | 剑桥同事，常一起打高尔夫的球友 |

> 禁入库名单（metadata-only / 噪声防入）：John Henry Poynting 与 William A. Tilden（Mason College 授课教师，infobox Other academic advisors，防噪声不入库）；Eugen Goldstein（Kanalstrahlen 发现者，非直接关系）、Wilhelm Wien（偏转法发现者，非直接关系）、Thomas Royds（无关联）、Michael A. Grayson（视频讲者）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1922，独享）
- Mackenzie Davidson Medal（1920）
- Hughes Medal（1922）
- John Scott Medal（1923）；Paterno Medal（1923）
- Royal Medal（1938）
- Duddell Medal and Prize（1944）
- Fellow of the Royal Society（1921 当选）
- International Committee on Atomic Weights 委员（1921）
- 加尔各答大学荣誉博士
- 月球环形山 Aston；英国质谱学会 Aston Medal

## 9. 机构清单

- 教育：Harborne Vicarage School → Malvern College → Mason College（伦敦大学外部学位，1893–）→ University of Birmingham（BSc 1910 / DSc 1914）
- 任职：W. Butler & Co. Brewery（1900–1903）→ University of Birmingham（Associate 1903 / 讲师 1909）→ Cavendish Laboratory, Cambridge（1910–；Trinity College Fellow）→ Royal Aircraft Establishment, Farnborough（一战技术助理）
- 身后：Aston Medal（英国质谱学会）

## 10. 终审清单

- [ ] 生卒 1877-09-01 / 1945-11-20，享年 68，出生地 Harborne、去世地剑桥
- [ ] 1922 独享；获奖理由英文原文完整引用；诺奖演讲 1922-12-12
- [ ] 导师 Frankland / 合作者 Thomson 的口径区分（frontmatter 冲突已裁定）
- [ ] meta-neon、212 种天然同位素、整数规则（¹⁶O 基准）表述准确
- [ ] 与 Soddy 的分工：Soddy 命名同位素（放射性元素）、Aston 证明非放射性元素同位素
- [ ] 终身未婚；体育/音乐/日食远征年份无误
- [ ] 引语全部可在 page.md 溯源，无源处一律间接转述
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Francis_William_Aston/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/` 肖像就位（"Aston in 1922"）或装饰圆占位
- [ ] **国籍**：封面顶部明示英国
- [ ] **引语核对**：引语必须在 page.md 原文找到，否则改间接转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（vbox<10pt、hbox<50pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger）对齐

---

> **名单状态**：本提示词由 chem-batch-02 批次生成；`chemist/generate_20th_century_list.py` 由主控统一收尾，勿改动。
