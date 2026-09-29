# Arne Tiselius（阿尔内·蒂塞利乌斯）立传提示词

> qid=Q233026 · 1902-08-10 – 1971-10-29 · 瑞典生物化学家 · 20 世纪 · 诺贝尔化学奖（1948，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Arne_Tiselius/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——表格语义化 tabularx + 公式展示框 + 时间线页，是本次的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（页面实载图为其诺贝尔博物馆放大镜藏品照——若人像缺图则用装饰圆占位并注「肖像暂缺」，勿拿放大镜照片冒充肖像）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{bolt}\enspace 让蛋白质在电场中排队\enspace·\enspace 瑞典`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、全名（Arne Wilhelm Kaurin Tiselius）、国籍、出生地/去世地、教育（Uppsala）、博士导师（Theodor Svedberg）、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「电泳条带」母题——并列圆点暗示电场中分离出的血清蛋白区带。
5. **表格语义化 + 公式框**（★ Sanger 版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如移动界面电泳原理式。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Arne Wilhelm Kaurin Tiselius（中文惯称：阿尔内·蒂塞利乌斯）
- **生卒**：1902-08-10 生于斯德哥尔摩 → 1971-10-29 逝于乌普萨拉（心脏病），享年 69
- **国籍**：Sweden（瑞典）
- **身份**：生物化学家（biochemist；1948 年诺贝尔化学奖独享得主；IUPAC 主席 1951–55；诺贝尔基金会董事会主席 1960–64）
- **家庭**：父亲早逝后随家迁往哥德堡；已婚，育有二子；妻 Ingrid Margareta Dahlén（infobox Spouse）
- **教育轨迹**：
  - 哥德堡当地 Realgymnasium（1921 年毕业）
  - Uppsala University 攻读化学并终老于此（BA→PhD 1930）
- **博士导师**：Theodor Svedberg（1925 年入其实验室任研究助理；1930 年获博士学位）
- **研究领域**：生物化学——电泳（electrophoresis）、吸附分析（adsorption analysis）、血清蛋白

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **斯德哥尔摩失怙（1902）**：生于斯德哥尔摩，幼年丧父，随家迁哥德堡——北欧单亲家庭走出的诺奖得主。
2. **乌普萨拉门下（1921–1925）**：1921 年 Realgymnasium 毕业后入乌普萨拉大学专攻化学——瑞典最古老的大学之一。
3. **Svedberg 实验室（1925）**：成为 Theodor Svedberg（1926 诺贝尔化学奖得主、超速离心机发明者）实验室的研究助理——名师门下起步。
4. **移动界面电泳博士论文（1930）**：博士论文 "The Moving Boundary Method of Studying the Electrophoresis of Proteins"——把物理方法引入蛋白质研究的开山之作。
5. **沸石与吸附（1930–1935）**：1930–35 年间发表多篇关于天然交换性沸石中扩散与吸附的论文——吸附分析的功力在此练成。
6. **普林斯顿一年（1930 年代中）**：获洛克菲勒基金会资助，赴普林斯顿大学 Hugh Stott Taylor 实验室访学一年——国际视野的加成。
7. **回到蛋白质（1935 后）**：回乌普萨拉后重拾蛋白质兴趣，把物理方法应用于生化问题——电泳分析法大幅改进，并在后续岁月持续精化。
8. **血清蛋白的复杂本性**：电泳+吸附分析揭示血清蛋白的复合本性——1948 诺奖理由的核心 discoveries。
9. **1948 诺贝尔化学奖（独享）**："for his research on electrophoresis and adsorption analysis, especially for his discoveries concerning the complex nature of the serum proteins"——页面明载官方理由原句，可直接引用。
10. **战后瑞典科学重建（1945 后）**：积极参与二战后瑞典科研体制重组——从实验室走向科学政策。
11. **IUPAC 与诺贝尔基金会（1951–1964）**：国际纯粹与应用化学联合会主席（1951–55）；诺贝尔基金会董事会主席（1960–64）——从得主变成守门人。
12. **国际荣誉链**：1949 美国 NAS 外籍副教授级成员、1953 美国艺术与科学院、1957 皇家学会外籍院士（ForMemRS）、1961 Paul Karrer Gold Medal、1964 美国哲学学会。
13. **月球命名（1971）**：月球环形山 Tiselius 以其命名；同年 10-29 因心脏病逝于乌普萨拉——以星辰为墓志。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（北欧青） | `#175E54` | 电泳条带的冷冽与瑞典湖泊的沉静（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（电泳 badgeElectrophoresis） | `#1B4F72` | 深蓝移动界面电泳 / 血清蛋白分离 |
| 分类色 2（吸附分析 badgeAdsorption） | `#7D6608` | 琥珀沸石 / 吸附分析 |
| 分类色 3（师门传承 badgeSvedberg） | `#5B2C6F` | 紫 Svedberg 实验室 / 超离心传统 |
| 分类色 4（科学治理 badgeGovernance） | `#148F77` | 青 IUPAC / 诺贝尔基金会 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「电泳条带」的并列排列。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**With Me** — Alex-Productions（`music_audio/alex-productions/83-DXAblXgCK-k-With-Me.wav`；不要复制 wav 文件，Makefile 直接引用路径）
- **风格**：温和 / 陪伴感 / 沉静叙事
- **匹配理由**：
  - "温和" 匹配北欧学者的克制气质——一生几乎未离开乌普萨拉，安静地把一件事做到诺奖级
  - "陪伴感" 匹配师门与合作——Svedberg 实验室五年、Taylor 实验室一年，科学是同行者的旅程
  - "沉静叙事" 匹配其晚年角色转换——从诺奖得主到诺贝尔基金会守门人的从容谢幕
- **时长**：以实际文件为准；ffmpeg `-shortest` 自动对齐幻灯片时长

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 让蛋白质在电场中排队 / Arne Tiselius 1902–1971 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/全名/国籍/教育/博士导师/出生地/去世地/领域/荣誉）
03  蒂塞利乌斯的一生 — Sanger 式时间线（10 节点：1902→1921→1925→1930→1935→1948→1951→1957→1960→1971）
04  哥德堡与乌普萨拉 (1902–1925) — 表格「时间|事件|结果」
05  Svedberg 门下 (1925–1930) — 表格「阶段|工作|结果」+ 公式框：移动界面电泳原理
06  沸石、吸附与普林斯顿 (1930–1935) — 表格「方向|方法|结果」（Taylor 实验室访学一年）
07  电泳分析法的精进 (1935–1948) — 表格「问题|方法|结果」+ 公式框：血清蛋白电泳分离
08  1948 诺贝尔化学奖（独享） — 表格「年份|奖项|官方理由」（citation 原句可引）
09  战后瑞典科学重建 (1945–) — 表格「舞台|职务|结果」
10  IUPAC 与诺贝尔基金会 (1951–1964) — Sanger FFT 页式流程图（IUPAC 主席 → ForMemRS → 诺基金会主席）
11  荣誉清单 — Sanger 式「类别|代表|意义」表格（NAS/AAAS/ForMemRS/Karrer 奖章/月球环形山）
12  血清蛋白研究的医学回响 — 四分类遗产盒 + 公式框：电泳 → 临床蛋白分析
13  遗产：物理方法改造生物化学 — 四分类遗产盒 + 公式框：电泳+吸附 双支柱
14  结尾 — 「电场拉开蛋白的队列，也拉开了生物化学的新纪元。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1948 获奖口径 | **独享**；官方理由原句页面明载可引："for his research on electrophoresis and adsorption analysis, especially for his discoveries concerning the complex nature of the serum proteins"——勿改写或缩短 |
| 博士导师 | Theodor Svedberg：1925 年任其实验室研究助理、1930 年获博士——师承明确可入库；勿写"仅同事" |
| Hugh Stott Taylor | 普林斯顿访学一年（洛克菲勒基金会资助）——**colleague/访学关系，勿写成博士导师或合作导师** |
| 配偶 | Ingrid Margareta Dahlén 仅 infobox 明载（正文只写 "married, with two children"）——infobox 属明载可入库；正文勿编造婚礼年份 |
| 博士生 | 页面**无载**任何博士生；metadata 有 Robert Williams 一条——**metadata-only 禁入库** |
| "第一个电泳" | 勿写"发明电泳"——页面口径是"大幅改进电泳分析方法"（much-improved method of electrophoretic analysis）；电泳本身早有发展 |
| 去世缘由 | 心脏病（heart attack），1971-10-29 于乌普萨拉——页面明载可写 |
| Svedberg 获奖年份 | Svedberg 是 1926 年诺贝尔化学奖得主——勿写错年份 |
| 月球环形山 | 页面明载 "The lunar crater Tiselius was named in his honour"——可写 |
| 同名区分 | Arne Tiselius 无常见重名；与 The Svedberg 目录（Theodor_Svedberg）区分即可 |
| 引语红线 | 仅 1948 citation 原句可作引语；其余叙述一律间接转述 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q233026 | ✅ |
| name_zh | 阿尔内·蒂塞利乌斯 | ✅ |
| name_en | Arne Tiselius | ✅ |
| birth_date | 1902-08-10 | ✅ |
| death_date | 1971-10-29 | ✅ |
| nationality | Sweden | ✅ |
| primary_occupation | biochemist | ✅ |
| field_of_work | biochemistry（person_field 细分：biochemistry / electrophoresis / adsorption analysis，带 rank） | ✅ |
| has_biography | false（Beamer 立传后置 1） | ✅ |

## 7. 社会关系入库清单

**红线：只收 page.md 正文或 infobox 明载的关系；metadata.json-only 一律不入库。**

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Theodor Svedberg | 师→生（博士导师） | 1925 入其实验室任研究助理；1930 博士（移动界面电泳） |
| colleague | Hugh Stott Taylor | 无向 | 洛克菲勒基金会资助赴普林斯顿其实验室访学一年 |
| spouse | Ingrid Margareta Dahlén | 无向 | 妻（infobox Spouse）；育有二子 |

> **禁入库名单（metadata-only 或无载）**：Robert Williams（metadata doctoral_student，页面 infobox/正文均无——不入库）；诺贝尔基金会/IUPAC 相关人物（机构职务非个人关系）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1948，独享）
- Björkénska priset / Björkén Prize（1940）
- Centenary Prize（1953）
- Franklin Medal（1955）
- August Wilhelm von Hofmann Medal（年份页面无载，如实标注）
- Paul Karrer Gold Medal（1961）
- 美国 NAS 外籍成员（1949）；美国艺术与科学院（1953）；皇家学会外籍院士 ForMemRS（1957）；美国哲学学会（1964）
- 巴黎大学、里昂大学、马德里康普顿斯大学荣誉博士
- 月球环形山 Tiselius 命名纪念

## 9. 机构清单

- 教育：哥德堡 Realgymnasium（1921）；Uppsala University（化学；1930 PhD "The Moving Boundary Method of Studying the Electrophoresis of Proteins"）
- 访学：Princeton University Hugh Stott Taylor 实验室（洛克菲勒基金会资助，一年）
- 任职：Uppsala University（一生主线）；IUPAC 主席（1951–1955）；诺贝尔基金会董事会主席（1960–1964）

## 10. 终审清单

- [ ] 生卒 1902-08-10 / 1971-10-29，享年 69，出生地斯德哥尔摩、去世地乌普萨拉（心脏病）
- [ ] 1948 独享；citation 原句完整可溯源
- [ ] 1925 助理 / 1930 博士 / 1930-35 沸石吸附 / 普林斯顿一年 / 1948 诺奖 / 1951-55 IUPAC / 1960-64 诺基金会 年份链准确
- [ ] 博士生不入库（页面无载）；Taylor 仅 colleague
- [ ] 全书仅 citation 一处引语，其余间接转述
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误，溢出达标

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Arne_Tiselius/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：页面实载图为诺贝尔博物馆放大镜藏品照——**勿冒充肖像**，缺人像用装饰圆占位并注记
- [ ] 国籍：封面顶部明示瑞典
- [ ] 引语核对：仅 1948 citation 原句
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾，本文件不改动该脚本。
> **最重要的事：每写一页就 make，看到溢出就修。**
