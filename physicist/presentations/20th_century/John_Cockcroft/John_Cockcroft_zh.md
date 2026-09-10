# John Douglas Cockcroft（约翰·道格拉斯·考克饶夫）立传提示词

> qid=Q62897 · 1897-05-27 – 1967-09-18 · 英国实验物理学家 · 20 世纪 · 1951 诺贝尔物理学奖
> 本地 Wikipedia 数据源：`physicist/presentations/20th_century/20th_century/John_Douglas_Cockcroft/`（page.md + metadata.json + images.txt）

---

## 0. 正文形式说明（参考物理学家标杆 Kenneth G. Wilson）

> 本提示词正文（Beamer tex）**采用 OpenPhysicist 物理学家立传模板标杆 Kenneth G. Wilson 的形式**。物理学家立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。注意：`images.txt` 中**无 Cockcroft 本人肖像**（仅有故居、电压倍增电路图、雷达照片），肖像缺位时用装饰圆 + `\faIcon{user}` 占位（参照已有立传的占位做法）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像位 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、去世地、教育、师承、任职、主要荣誉、核心领域。事实取自 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色（诺奖金）+ 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「粒子束轰击 / 链式反应起点」母题。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：John Douglas Cockcroft（约翰·道格拉斯·考克饶夫），Sir（爵士，1948 Knight Bachelor）
- **生卒**：1897-05-27 生于 Todmorden（英格兰）→ 1967-09-18 逝于剑桥 Churchill College 家中（心脏病），享年 70；葬于剑桥 Ascension Parish Burial Ground（与早夭长子 Timothy 同墓）；1967-10-17 威斯敏斯特教堂举行追思会
- **国籍**：英国（United Kingdom）
- **身份**：实验物理学家、核物理学家、大学教师（infobox occupation：physicist / nuclear physicist / university teacher）
- **家庭**：父 John Arthur Cockcroft（磨坊主），母 Annie Maude Fielden；长子，下有四弟 Eric、Philip、Keith、Lionel；1925-08-26 在 Todmorden Bridge Street 卫理公会教堂与 Eunice Elizabeth Crabtree（中学同学）结婚，育 6 子（长子 Timothy 婴儿期夭折，四女 Thea、Jocelyn、Elisabeth Fielden、Catherine Helena，幼子 Christopher Hugh John）
- **教育轨迹**：
  - 1901-1914 Walsden 教会小学 → Todmorden 小学/中学；1914 获约克郡 West Riding County Major Scholarship 入维多利亚曼彻斯特大学学数学
  - 一战服役后改学电机工程：Manchester Municipal College of Technology（Miles Walker 门下），1922 获 B.Sc.（Technology）；毕业后在 Metropolitan Vickers 当两年学徒兼研究员
  - 1922 获奖学金入剑桥 St John's College，1924-06 考 Tripos 成 Wrangler（B\*），获 B.A.
  - 1924 入卡文迪许实验室读博，1928-09-06 获博士
- **博士导师**：Ernest Rutherford（卡文迪许实验室）
- **博士论文**：*On phenomena occurring in the condensation of molecular streams on surfaces*（分子束在表面凝聚的现象，1928）——**主题是表面凝聚而非核物理**（见陷阱表）
- **研究领域**：核物理、粒子加速器、原子能、低温物理（博士期间任 Kapitza 助手，参与氦液化器设计建造）

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **一战经历与转向**：西线皇家野战炮兵信号兵→军官（1918-10-17 授中尉），历经推进兴登堡防线与第三次伊普尔战役；战后弃数学改学电机工程——工程训练日后成为造加速器的本钱。
2. **入卡文迪许与 Kapitza 助手**（1924-1928）：经 Miles Walker 推荐，Rutherford 收其为学生；任俄国物理学家 Peter Kapitza 的助手，参与强磁场/极低温物理与氦液化器设计。
3. **人工加速粒子嬗变原子核（1932，诺奖工作）**：Rutherford 1919 曾用镭 α 粒子使氮核嬗变；他指派 Cockcroft、Thomas Allibone、Ernest Walton 攻关人工加速器。Cockcroft 读到 **George Gamow 量子隧穿**论文后意识到所需电压远低于预期（算出约 30 万电子伏质子即可穿透硼核）；Rutherford 为他们申请到 1000 英镑购置变压器等设备。Mark Oliphant 为其设计质子源。
4. **分裂锂核**（1932-03 开始运行；1932-04-14 Walton 轰击锂靶首先观察到 α 粒子，Cockcroft 与 Rutherford 随即确认）：当晚在 Rutherford 家写成致 *Nature* 的信——首次人工核嬗变，反应为 $^{7}\mathrm{Li} + p \to 2\,^{4}\mathrm{He} + 17.2\ \mathrm{MeV}$，俗称 "splitting the atom"（分裂原子）。
5. **Cockcroft–Walton 生成器**：与 Walton（及 Oliphant）建造的电压倍增加速器，开启粒子加速器时代的实验核物理；随后嬗变碳、氮、氧，并制得放射性同位素（碳-11、氮-13）。
6. **1938 Hughes Medal**（与 Walton 共享，获奖理由"发现核可被人工产生的轰击粒子所嬗变"）——1951 诺奖的先声。
7. **卡文迪许的组织者角色**：1935 任 Mond Laboratory 研究主任（Kapitza 回苏联后），主持低温设备安装；1936 当选皇家学会会士（FRS）；1939 任 Jacksonian 自然哲学教授；力促卡文迪许引进回旋加速器（Lord Austin 捐 25 万英镑建 36 英寸回旋加速器，1938-10 运行）。
8. **二战雷达与国防科技**：供应部科研副总监，推动 Chain Home 预警雷达网全面运转；1940 参与 Frisch–Peierls 备忘录评估委员会及其后继 **MAUD 委员会**（判定原子弹技术上可行）。
9. **Tizard 使团**（1940-08）：赴美分享英国尖端技术——空腔磁控管（被美国史家 James Phinney Baxter III 称为"运抵我们海岸的最有价值货物"）、近炸引信、Whittle 喷气发动机、Frisch–Peierls 备忘录等；战后 SCR-584 雷达与近炸引信反哺英国，用于打击 V-1 飞弹（击落率 97%），1944-06 获 CBE。
10. **蒙特利尔实验室主任**（1944-05 起）：主管加拿大重水反应堆项目，建成 ZEEP（1945-09-05 临界，美国以外首座运行反应堆）与 NRX（1947-07-21，当时世界最强研究堆），创建 Chalk River 实验室。
11. **AERE 哈威尔首任所长**（1946 任命）：GLEEP（1947-08-15 启动，西欧第一座核反应堆）、BEPO（1948）；参与 Windscale 反应堆与后处理厂设计；主导 ZETA 聚变计划（1958 与美国同步发布结果）；谈判 1948 *Modus Vivendi* 恢复对美核合作。
12. **"考克饶夫的蠢举"（Cockcroft's Folly）**：力主 Windscale 反应堆烟囱加装高性能过滤器，曾被讥讽为多此一举；1957 年 Windscale 火灾中过滤器大幅减轻放射性泄漏——Terence Price 评述"事故之后，folly 一词看来不再恰当"。**远见被验证的科学家形象高光**。
13. **学术领导晚年**：1959-1967 剑桥 Churchill College 首任院长（Master，主持建校；教堂选址争议致 Francis Crick 辞院士职）；1961-1965 澳大利亚国立大学校监；英国物理学会会长（1954-1956）、英国科学促进会会长；CERN 理事会英国代表。

## 3. 配色方案

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（剑桥深蓝） | `#123C5B` | 卡文迪许 / 工程实干 / 大科学组织者 |
| 强调色（诺奖金） | `#C9A227` | 诺贝尔奖 / 尊崇 |
| 分类色 1（原子嬗变 — 原子橙） | `#E07B30` | 加速器 / 分裂锂核 / 同位素 |
| 分类色 2（战时科技 — 军绿） | `#4A7C3F` | 雷达 / Tizard 使团 / MAUD 委员会 |
| 分类色 3（核能时代 — 深青） | `#0E7C7B` | ZEEP / NRX / 哈威尔 / ZETA |
| 分类色 4（学术传承 — 玫瑰） | `#C4204F` | Churchill College / 荣誉与纪念 |
| 背景 | `#F7F6F9` | 浅灰白 |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「加速管道中的粒子束 / 链式反应的起点」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：探索 / 远征 / 开创（从战壕到分裂原子，再到核能时代的远征式组织者）
- **选定曲目**：Alex-Productions **Expedition**（探索 / 史诗），匹配"远征式叙事"——以工程师之躯完成物理学远征，再率队开辟核能时代。
- **落地文件**：`physicist/presentations/20th_century/John_Cockcroft/Expedition.wav`（复制自音乐库，不入 git）。
- **匹配理由**：Cockcroft 一生是"工程 + 科学"的远征：一战炮兵 → 电机工程 → 分裂原子 → 雷达与原子能工程 → 建校立所；Expedition 的开阔推进感契合其组织者与开拓者气质。

## 4. Slide 规划（约 15 页，Wilson 式结构）

1. **封面**（`\titleslide`）：顶部标签「分裂原子的人 · 英国」+ Cockcroft 1897–1967 + 右上头像位 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像位 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 去世地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **核心贡献概览**（`\hookslide`）：人工核嬗变 / 战时科技 / 核能时代 / 学术传承
4. **时间线页**：1897 Todmorden → 1915-1918 西线 → 1922 B.Sc. → 1928 博士 → 1932 分裂锂核 → 1936 FRS → 1940 Tizard 使团 → 1944 蒙特利尔 → 1946 哈威尔 → 1951 诺奖 → 1959 Churchill College → 1967 逝世
5. **早年：Todmorden 与一战**（1897–1919）：磨坊主之子、奖学金、炮兵信号兵
6. **从电机工程到卡文迪许**（1919–1928）：Metropolitan Vickers 学徒、Tripos Wrangler、Rutherford 门下、Kapitza 助手
7. **Gamow 隧穿与加速器决策**（1929–1931）：低电压方案的物理学洞见、Rutherford 的 1000 英镑、Oliphant 质子源
8. **1932 年 4 月 14 日：分裂锂核**：Walton 首先观察、当晚致 *Nature* 信、$^{7}\mathrm{Li}+p\to 2\,^{4}\mathrm{He}+17.2\ \mathrm{MeV}$ 公式框
9. **Cockcroft–Walton 生成器与加速器时代**：电压倍增电路图、放射性同位素、推动引进回旋加速器
10. **二战：雷达与 Tizard 使团**（1939–1943）：Chain Home、MAUD 委员会、空腔磁控管、SCR-584 与近炸引信
11. **蒙特利尔与 Chalk River**（1944–1946）：ZEEP、NRX、Nunn May 间谍案与请愿憾事
12. **哈威尔：英国核能的摇篮**（1946–1959）：GLEEP、BEPO、ZETA、"Cockcroft's Folly" 与 1957 Windscale 火灾
13. **Churchill College 与晚年**（1959–1967）：首任院长、ANU 校监、CERN 理事会代表
14. **荣誉与遗产**：1951 诺奖、Hughes/Royal/Faraday/Niels Bohr 各奖章、OM/KCB、月球背面 Cockcroft 环形山、各大学 Cockcroft 楼
15. **结尾**：70 岁、"以人工加速粒子分裂原子之人"的历史地位与遗产

## 5. 史实陷阱与敏感点（终审必须检查）

- **姓名与目录名**：输出目录为 `John_Cockcroft`，数据目录为 `John_Douglas_Cockcroft`，通称 John Cockcroft——行文用"考克饶夫"，勿与数据目录名混淆。
- **诺奖表述**：1951 与 **Ernest Walton 共享**，理由（总名单中文）："表彰他们利用人工加速的原子粒子实现原子核嬗变的开创性工作"；英文原文 "For their pioneer work on the transmutation of atomic nuclei by artificially accelerated atomic particles"（page.md 载）。勿写"考克饶夫独得"。
- **1932 年实验分工**：1932-04-14 **Walton 轰击锂靶并首先观察到 α 粒子**，Cockcroft 与随后赶到的 Rutherford 确认；加速器 1932-03 开始运行。写"两人合作完成"，勿写成 Cockcroft 单人操作。
- **分裂的是锂核**：反应为锂-7 + 质子 → 两个 α 粒子 + 17.2 MeV（page.md 明载）；先前预期 γ 射线未出现，Chadwick 1932-02 证实中子后才转向寻找 α 粒子——勿把发现中子混入其功绩。
- **博士论文主题**：1928 博士论文是**分子束在表面凝聚**（表面物理），非核物理——常被误写为"核物理博士论文"。
- **电压数字**：Cockcroft 依 Gamow 理论算出约 **30 万电子伏质子可穿透硼核**（Cockcroft 页）；Walton 页另载加速管电压 **700 千伏**——两个数字语境不同（理论阈值 vs 装置工作电压），勿混用。
- **"原子之父"外号**：page.md **无载**，禁写。
- **Cockcroft's Folly**：讥称指 Windscale 烟囱过滤器；1957 火灾中过滤器确实减轻泄漏。引语 "the word folly did not seem appropriate after the accident" 出自 Terence Price（page.md 有载），非 Cockcroft 本人语。
- **"最有价值货物"引语**：出自美国史家 James Phinney Baxter III 对**空腔磁控管**的评价（page.md 有载），勿安到 Cockcroft 头上。
- **国籍**：英国（United Kingdom），出生地 Todmorden 在英格兰——封面用「英国」。
- **死亡**：1967-09-18 心脏病逝于 Churchill College 家中，享年 70；葬 Ascension Parish Burial Ground，与子 Timothy 同墓。
- **Nunn May 请愿**：1947 年曾签名请求减刑，"later regretted"（page.md 有载）——表述为历史憾事，勿美化亦勿苛责。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q62897 | 待写入 |
| name_zh | 考克饶夫（或 约翰·道格拉斯·考克饶夫） | 待写入 |
| name_en | John Cockcroft | 待写入 |
| birth_date | 1897-05-27 | 待写入 |
| death_date | 1967-09-18 | 待写入 |
| nationality | United Kingdom | 待写入 |
| primary_occupation | nuclear physicist | 待写入 |
| field_of_work | physics / nuclear physics | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Ernest Rutherford（卡文迪许实验室）
- **共同得主（co-honored）**：Ernest Walton（1951 诺贝尔物理学奖共享；1938 Hughes Medal 亦共享）
- **合作者（collaborator）**：Ernest Walton（加速器与核嬗变实验）；Mark Oliphant（设计质子源、共建加速器、战后共勘 Harwell 址址）；Thomas Allibone（同组攻关加速器）
- **导师侧同事**：Peter Kapitza（Cockcroft 任其助手，参与氦液化器设计）
- **著名学生**：R. S. Krishnan（page.md infobox）；Don Misener（metadata.json doctoral_student）
- **战时同事**：Henry Tizard（使团）、John Cockcroft 与 Oliphant 的 Harwell 筹建组合（Klaus Fuchs 任理论物理组长，后以苏联间谍被捕——只作历史事实陈述）
- **诺贝尔奖同届**：1951 年诺贝尔物理学奖仅 Cockcroft 与 Walton 两人共享，无第三位得主

## 8. 奖项清单

- 诺贝尔物理学奖（1951，与 Walton 共享）
- Hughes Medal（1938，与 Walton 共享）
- James Alfred Ewing Medal（1947）
- Royal Medal（1954）
- Faraday Medal（1955）
- Niels Bohr International Gold Medal（1958）
- Wilhelm Exner Medal（1961）
- Atoms for Peace Award（1961）
- CBE（1944）、Knight Bachelor（1948）、KCB（1953）、Order of Merit（1957）、法国荣誉军团骑士（1952）
- FRS（1936）；新西兰皇家学会荣誉会士（Honorary Fellow of the Royal Society Te Apārangi）

## 9. 机构清单

- 教育：维多利亚曼彻斯特大学（数学，1914-1915）、Manchester Municipal College of Technology（电机工程 B.Sc. 1922）、Metropolitan Vickers（学徒）、剑桥 St John's College（B.A. 1924；博士 1928）
- 任职：卡文迪许实验室（1924-1939，含 Kapitza 助手、Mond Laboratory 研究主任 1935）、Jacksonian 自然哲学教授（1939）、供应部科研副总监（二战）、ADRDE 首席总监（1941 起）、蒙特利尔实验室主任（1944）、Chalk River 实验室、AERE 哈威尔所长（1946-1959）、Churchill College 首任院长（1959-1967）
- 兼职：英国物理学会会长（1954-1956）、英国科学促进会会长、澳大利亚国立大学校监（1961-1965）、CERN 理事会英国代表、DSIR 核物理小组委员会主席

## 10. 终审清单

- [ ] 生卒 1897-05-27 / 1967-09-18，享年 70，出生地 Todmorden，去世地 Cambridge（Churchill College）
- [ ] 诺奖"1951 与 Walton 共享"及总名单中文理由表述准确
- [ ] 1932-04-14 实验"Walton 首先观察、Cockcroft 与 Rutherford 确认"分工准确
- [ ] 锂-7 + p → 2 α + 17.2 MeV 反应式准确
- [ ] 博士论文"表面凝聚"主题准确，勿写核物理
- [ ] "原子之父"外号未出现（page.md 无载）
- [ ] 引语（Baxter III / Terence Price）出处人物正确
- [ ] 正文采用 Wilson 式：身份信息页 + 封面头像位 + 国籍行 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `John_Douglas_Cockcroft/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images.txt` 无本人肖像——用装饰圆占位，或经确认后从 Commons Special:FilePath 另行取图（如 "John Cockcroft.jpg"，需 404/HTML 验证）
- [ ] **国籍**：封面顶部徽章明示英国
- [ ] **引语核对**：引语必须在 page.md 原文找到（Baxter III、Terence Price 两处）
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Wilson 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同世纪物理学家（Wilson / Wigner / Heisenberg）格式对齐

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
