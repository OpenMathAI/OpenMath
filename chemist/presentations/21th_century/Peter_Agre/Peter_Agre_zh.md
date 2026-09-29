# Peter Agre（彼得·阿格雷）立传提示词

> qid=Q102250 · 1949-01-30 生于美国明尼苏达州 Northfield（在世，卒日留白） · 美国医师/分子生物学家 · 21 世纪 · 诺贝尔化学奖（2003，与 Roderick MacKinnon 共享当年奖项，理由各不同）
> 本地 Wikipedia 数据源：`chemist/presentations/21th_century/pages/Peter_Agre/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 表格语义化 tabularx + 金框公式展示框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注。肖像：`images.txt` 有 **AgreLindau.png**（2011 年第 61 届林道诺奖得主会议讲授疟疾照片）——下载时 250px 改 500px 重抓原图；404 则装饰圆占位并在 Review-1 记录。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{tint}\enspace 细胞水管道的发现者\enspace·\enspace 美国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素（美国 | Johns Hopkins | 水通道蛋白 Aquaporin-1）。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名 Peter Courtland Agre、国籍、出生地、教育（Augsburg BA / JHU MD 1974）、临床训练、核心领域、现任（JHU 疟疾研究所所长 / Bloomberg 杰出教授）、荣誉。事实取自本地 page.md infobox，不得杜撰；在世——卒栏写「在世（1949– ）」。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「水分子穿越膜通道」母题——离散水滴暗示水通道的选择性水流。
5. **表格语义化 + 公式框**（★ 高斯/Sanger 版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage）——AQP1 = 28 kDa 红细胞膜蛋白、爪蟾卵母细胞渗爆实验即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Peter Courtland Agre（中文惯称：彼得·阿格雷）
- **生卒**：1949-01-30 生于明尼苏达州 Northfield（在世，卒日页面无载——全篇卒处一律留白）
- **国籍**：United States（美国）
- **身份**：医师（physician）、分子生物学家；Johns Hopkins Bloomberg 公共卫生学院及医学院 Bloomberg 杰出教授、Johns Hopkins 疟疾研究所所长
- **家庭**：六孩中的次子，挪威/瑞典裔，信义宗教徒；父亲是学院化学教授（科学兴趣起点）；妻 Mary（1975 年结婚，页面仅载名 Mary），三女一子（子 Clarke 为公辩护律师，亦鹰级童军）；2012 年确诊帕金森病，减少活动
- **教育轨迹**：
  - Roosevelt High School（明尼苏达）；高中露营穿越苏联，点燃国际视野
  - Augsburg University（Minneapolis）：化学 BA
  - Johns Hopkins School of Medicine：MD 1974
- **师承/临床训练**：1975–1978 Case Western Reserve 内科住院医训练（Charles C.J. Carpenter）→ UNC Chapel Hill 血液肿瘤 fellowship → 1981 回 JHU 入 Vann Bennett 细胞生物学实验室（博士后）
- **研究领域**：生物化学/分子生物学——膜蛋白、水通道蛋白（aquaporins）、红细胞膜、疟疾

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **明尼苏达少年（1949）**：挪威/瑞典裔大家庭，父亲化学教授——科学志向的起点；国际视野自高中苏联之行萌芽。
2. **JHU 医学博士（1974）**：Augsburg 化学 BA → Johns Hopkins MD；医学院期间曾在 Brad Sack 与 Pedro Cuatrecasas 实验室研究肠毒素致泻。
3. **临床岁月（1975–1981）**：Case Western 内科训练（Carpenter）→ UNC 血液肿瘤 fellowship → 1981 回 JHU Vann Bennett 实验室。
4. **红细胞膜（1981–1984）**：鉴定 spectrin 缺陷为遗传性球形红细胞症的常见病因——脆而球形的红细胞的溶血性贫血。
5. **独立建组（1984）**：受 Victor A. McKusick 招入内科系，后转 Dan Lane 领导的生物化学系；1992 升正教授。
6. **RhD 与意外发现**：纯化 Rh 血型抗原 32 kDa 核心亚基时，意外发现 28 kDa 红细胞膜蛋白——在肾小管也丰富，序列与果蝇脑、晶状体、细菌、植物蛋白同源。
7. **Parker 的点拨**：请教 UNC 时代血液学教授 John C. Parker——后者提出这可能是寻找已久的快速水通道。
8. **爪蟾卵母细胞实验**：与生理学系 William Guggino 合作，博士后 Gregory Preston 把 cRNA 表达到非洲爪蟾卵母细胞——细胞渗吸膨胀至爆裂，水通道功能确证。
9. **AQP1 与家族**：28 kDa 蛋白即 aquaporin-1（AQP1）——人体内已知 12 个水通道蛋白；"细胞的管道系统"（自述，页面明载可引）；脑脊液、泪液、汗液、肾浓缩皆有赖。
10. **2003 诺贝尔化学奖**：与 Roderick MacKinnon 共享当年奖项，共享理由 "discoveries concerning channels in cell membranes"；Agre 因**发现水通道蛋白**获承认；得奖清晨 5:30 接到斯德哥尔摩电话，母亲回应 "That's very nice but don't let it go to his head."（页面明载可引）。
11. **Duke 与回归 JHU（2005–2008）**：Duke 医学中心科研副校长 → 2008 回 JHU 任疟疾研究所（JHMRI）所长——赞比亚 Macha 田间合作，青蒿素联合疗法+药浸蚊帐后当地幼儿疟疾负担降 96%。
12. **科学外交（2009–2011 AAAS 主席）**：古巴六访（会卡斯特罗，客观一句）、朝鲜 2009 访问国家科学院、缅甸 2010、伊朗 2012（德黑兰多校讲学）——为和平科学项目破冰。
13. **公共事务**：Thomas Butler 案辩护、2008 明尼苏达参议员试探后 2007-08 宣布不参选、48 诺奖得主联署挺 Kerry、奥巴马过渡团队、2015 林道 Mainau 气候宣言联署；自称 "I identify more with Huckleberry Finn than with Albert Einstein."（页面明载可引）。

## 3. 配色方案（高斯/Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（靛蓝 indigo） | `#283593` | 膜生物化学的深湛（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（水通道 badgeAQP） | `#1B7A43` | 绿 AQP1 / 水通道家族 |
| 分类色 2（红细胞膜 badgeRBC） | `#C0395B` | 玫瑰 spectrin / RhD |
| 分类色 3（疟疾与全球卫生 badgeMal） | `#D97B29` | 琥珀 JHMRI / 赞比亚田间 |
| 分类色 4（科学外交 badgeDip） | `#2E5A9E` | 蓝 AAAS / 古巴·朝鲜·缅甸·伊朗 |
| 背景 | `#F7F6F9` | 浅灰白（与高斯一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「水分子列队穿越通道」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Expedition** — Alex-Productions（`music_audio/alex-productions/33--_CEmB_dHpA-Expedition.wav`，不要复制 wav 文件，Makefile 里直接引用该路径）
- **风格**：进取 / 探索 / 明亮的行进感
- **匹配理由**：
  - "探索" 匹配水通道发现——从 RhD 纯化的意外观察到功能确证，是一次典范的意外之旅
  - "行进感" 匹配其人生轨迹——明尼苏达 → 巴尔的摩 → 达勒姆 → 再回巴尔的摩，再到全球卫生与科学外交的第一线
  - 林道讲学、赞比亚田间、古巴/朝鲜破冰——诺奖得主中的 "Expedition" 式人物
- **时长**：以实际 wav 为准，> 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 细胞水管道的发现者 / Peter Agre 1949– + 四色 badge + 右上头像 + 国籍行（美国）
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/临床训练/任职/领域/荣誉）
03  阿格雷的一生 — Sanger 式时间线（10 节点：1949→1974→1975→1981→1984→1992→2003→2005→2008→2009）
04  明尼苏达少年与 JHU 医学路 (1949–1974) — 表格「时间|事件|结果」
05  临床与红细胞膜 (1975–1984) — 表格「阶段|环境|结果」
06  意外的 28 kDa 蛋白 (1984–) — 表格「问题|方法|结果」+ 公式框：AQP1 = 28 kDa 膜蛋白
07  水通道功能确证 — 表格「合作者|实验|结果」+ 公式框：爪蟾卵母细胞渗爆实验
08  Aquaporin 家族与生理 — 表格「组织|功能|缺陷」（12 个人类 aquaporin / 水通道甘油酯蛋白）
09  2003 诺贝尔化学奖 — 金框 citation 原文页（channels in cell membranes）+ 与 MacKinnon 理由各不同的标注
10  疟疾与全球卫生 — 高斯 FFT 页式流程图（2008 JHMRI → Macha 合作 → 负担降 96% → ICEMR 扩展）
11  科学外交 — 表格「国家|年份|形式」（古巴/朝鲜/缅甸/伊朗）
12  公共事务 — 表格「议题|角色|结果」（Butler 案 / 参议员试探 / Mainau 2015）
13  荣誉与人格 — 高斯式「类别|代表|意义」表格（NAS 2000 / AAAS 主席 2009 / 19 个荣誉博士；鹰级童军与 Huckleberry Finn 自述）
14  结尾 — 「生命以水写成，而他找到了水的那扇门。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 2003 奖项口径 | 与 Roderick MacKinnon **共享当年奖项**（共享理由 "discoveries concerning channels in cell membranes"），但**两人理由不同**：Agre=水通道蛋白的发现、MacKinnon=钾离子通道的结构与运作——co-honored 关系可建，note 必须注明「理由各不同」 |
| 获奖理由原文 | 共享理由 "for discoveries concerning channels in cell membranes"（Agre 页明载）；**页面无 Agre 单人官方 citation 全句**——勿编造 "for the discovery of water channels" 之类官方口径 |
| AQP1 分子量 | 28 kilodalton（RhD 是 32 kDa）——两个数字勿混 |
| Parker 角色 | John C. Parker 是 UNC 时代血液学教授，**提议**该蛋白可能是水通道——勿写「P的共同发现者」 |
| 卵母细胞实验 | 表达 cRNA 的是 Agre 的博士后 **Gregory Preston**（与 Guggino 合作）——勿写 Agre 亲手做 |
| 家庭细节 | 妻 Mary 页面仅载名（1975 结婚）；子 Clarke 是公辩护律师；兄弟中两位是医师且皆鹰级童军——仅页面所载范围 |
| 帕金森 | 2012 年确诊，减少活动——一句客观，不渲染 |
| 政治内容 | Kerry 联署、批评布什政府、古巴/朝鲜/伊朗行——仅按页面客观一句带过，**不做立场发挥**；"2026 代言护肤品" 一句系页面边缘内容，建议略过 |
| 引语白名单 | 仅三条可引：Huckleberry Finn 自述、母亲 "don't let it go to his head."、"the plumbing system for cells"——其余一律间接转述 |
| 同名/相关人物 | Gheorghe Benga 仅见 See also（页面正文无其优先权争议叙述）——**不写 Benga，不建关系** |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q102250 | ✅ |
| name_zh | 彼得·阿格雷 | ✅ |
| name_en | Peter Agre | ✅ |
| birth_date | 1949-01-30 | ✅ |
| death_date | （在世，留空） | ✅ |
| nationality | United States | ✅ |
| primary_occupation | molecular biologist | ✅ |
| field_of_work | biochemistry（person_field 细分：biochemistry / molecular biology / membrane protein / medicine，带 rank） | ✅ |
| has_biography | 0（待 Beamer 立传后由主控置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 合作者 / 共同得主**（仅 page.md 正文或 infobox 明载者）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Charles C.J. Carpenter | 师→生 | 1975–1978 Case Western Reserve 内科临床训练导师 |
| advisor-student | Vann Bennett | 师→生（博士后导师） | 1981– 回 JHU 入其细胞生物学实验室，研究红细胞膜 |
| advisor-student | Brad Sack | 师→生 | JHU 医学生阶段实验室导师（肠毒素致泻研究） |
| advisor-student | Pedro Cuatrecasas | 师→生 | JHU 医学生阶段实验室导师（肠毒素致泻研究） |
| advisor-student | John C. Parker | 师→生 | UNC 时代血液学教授；提议 28 kDa 蛋白可能是寻找已久的水通道 |
| advisor-student | Gregory Preston | 生→师（本人学生） | 博士后，爪蟾卵母细胞表达 cRNA 确证水通道功能 |
| colleague | William Guggino | 无向 | JHU 生理学系合作者，共同完成水通道功能验证 |
| colleague | Norman P. Neureiter | 无向 | AAAS 科学外交多次同行（伊朗 2012 等） |
| co-honored | Roderick MacKinnon | 无向 | 2003 诺贝尔化学奖共享当年奖项；理由各不同（Agre 水通道 / MacKinnon 离子通道） |
| spouse | Mary Agre | 无向 | 妻，1975 年结婚（页面仅载名 Mary） |
| influence | Linus Pauling | 无向 | 页面明载自述敬佩 Pauling（诺奖得主与和平活动家；库内 #2034，规范名 Linus Pauling） |

> **禁入库（metadata-only / 页面非关系）**：Gheorghe Benga（仅 See also）；Michael Bloomberg（捐赠人非学术关系）；政治人物（Castro、Ahmadinejad、Obama、Coleman、Franken、Kerry）；Dan Lane / Victor A. McKusick（仅科室领导与招募语境）。

## 8. 奖项清单

- Nobel Prize in Chemistry（2003，与 MacKinnon 共享当年奖项；理由口径见 §5）
- National Academy of Sciences 院士（2000）
- American Academy of Arts and Sciences 院士（2003）
- American Philosophical Society 院士（2004）
- Golden Plate Award，American Academy of Achievement（2004）
- National Academy of Medicine 院士（2005）
- American Society for Microbiology 院士（2011）
- Bloomberg Distinguished Professorships（2014）
- George M. Kober Medal；Karl Landsteiner Memorial Award；Distinguished Eagle Scout Award（infobox 另载）
- 19 个荣誉博士（日、挪威、希腊、墨西哥、匈牙利、美国等地高校）

## 9. 机构清单

- 教育：Roosevelt High School → Augsburg University（BA 化学）→ Johns Hopkins School of Medicine（MD 1974）
- 临床：Case Western Reserve / Case Medical Center 内科（1975–1978）→ UNC Chapel Hill 北卡纪念医院血液肿瘤 fellowship
- 任职：Johns Hopkins 细胞生物学系 Bennett 实验室（1981–）；内科系（1984，McKusick 招募）→ 生物化学系（Dan Lane）；1992 正教授，至 2005 留 JHU；Duke University Medical Center 科研副校长（2005–）；2008 回 JHU：Johns Hopkins Malaria Research Institute 所长 + 医学院联合聘任、Bloomberg Distinguished Professor（2014）
- 其他：AAAS 主席兼董事会主席（2009–2011）；美国科学家与工程师组织（SEA）创始成员

## 10. 终审清单

- [ ] 生卒 1949-01-30 / 在世留白，出生地 Northfield, Minnesota
- [ ] 2003 与 MacKinnon 共享奖项、理由各不同；citation "discoveries concerning channels in cell membranes" 逐字准确
- [ ] 28 kDa（AQP1）vs 32 kDa（RhD）勿混；Parker 提议 / Preston 实验角色准确
- [ ] 引语仅三条白名单；政治内容仅客观一句
- [ ] 家庭表述限于页面所载（Mary / 三女一子 / 帕金森 2012）
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Peter_Agre/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：AgreLindau.png 500px 重抓；404 则装饰圆占位并记录
- [ ] **国籍**：封面顶部明示美国
- [ ] **引语核对**：仅三条白名单引语
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与 21 世纪批次各篇格式对齐
