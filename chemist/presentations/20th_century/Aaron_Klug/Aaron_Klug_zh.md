# Aaron Klug（阿龙·克卢格）立传提示词

> qid=Q190626 · 1926-08-11 – 2018-11-20 · 英国生物物理学家与化学家 · 20 世纪 · 诺贝尔化学奖（1982，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Aaron_Klug/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + Sanger 式时间线 + 表格语义化 tabularx + 金色公式框 + 气泡背景。

---

## 0. 正文形式说明（参考 Sanger 模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像从 page.md 图注照片取：1979 年与荷兰王储妃同框照需裁右取 Klug 与夫人或改用其他实照；若下载失败用装饰圆占位并注记）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 晶体电子显微镜的奠基人\enspace·\enspace 英国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「晶体 / 二维投影重建三维」母题——离散圆点暗示从不同角度拍摄的晶面序列。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化（晶体电子显微术：二维投影序列 → 三维重构；螺旋链分子衍射理论）。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Sir Aaron Klug（OM FRS FMedSci HonFRMS；中文惯称：阿龙·克卢格）
- **生卒**：1926-08-11 生于立陶宛 Želva → 2018-11-20 逝于英格兰剑桥，享年 92
- **国籍**：United Kingdom（英国；生于立陶宛、2 岁随父母移居南非成长受教育）
- **身份**：生物物理学家与化学家（biophysicist and chemist）
- **家庭**：立陶宛犹太家庭；父 Lazar 为牧牛人、母 Bella（娘家姓 Silin）；2 岁随父母移民南非；在南非曾遭受歧视但终生保持宗教信仰（据 Sydney Brenner，晚年愈发虔诚）；1948 年娶 Liebe Bobrow，育两子（其中一子 2000 年先逝）
- **教育轨迹**：
  - 南非 Durban High School（Paul de Kruif 1926 年《Microbe Hunters》唤起微生物学兴趣；参加过 Hashomer Hatzair 犹太复国主义青年运动）
  - University of the Witwatersrand 理学学士（BSc；随 Reginald W. James 学物理，从微生物学转入物理与数学）
  - University of Cape Town 理学硕士（MSc）
  - 获 1851 Research Fellowship 赴英：Trinity College, Cambridge 研究物理博士（PhD 1953，论文 *The kinetics of phase changes in solids*；infobox 记 doctoral advisor 为 Douglas Hartree）
- **导师**：Douglas Hartree（infobox 口径）
- **博士**：1953，University of Cambridge（Trinity College）
- **研究领域**：生物物理学、晶体电子显微术（crystallographic electron microscopy）、病毒结构、核酸-蛋白质复合物结构

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **从立陶宛到南非（1926–1928）**：生于 Želva 犹太家庭，2 岁随父母移民南非。
2. **Microbe Hunters 的启蒙（少年）**：Paul de Kruif 的 1926 年著作唤起对微生物学的终生兴趣。
3. **转向物理与数学（1940s）**：Witwatersrand 随 Reginald W. James 学物理获 BSc；Cape Town 获 MSc。
4. **1851 奖学金赴英（1953）**：Trinity College, Cambridge 研究物理博士——固相变的动力学。
5. **Birkbeck 与 Franklin（1953–1962）**：1953 年末入 Birkbeck College，在晶体学家 J. D. Bernal 实验室与化学家、X 射线晶体学家 Rosalind Franklin 共事——点燃对病毒研究的终生兴趣；烟草花叶病毒（TMV）结构发现。
6. **入主 LMB（1962）**：迁入新建的 MRC 分子生物学实验室（LMB）；同年当选 Peterhouse, Cambridge Fellow（后为荣誉 Fellow）。
7. **晶体电子显微术（1960s）**：融合 X 射线衍射、显微术与结构建模——从不同角度拍摄的二维晶体图像序列合成为目标的三维图像；这是 1982 诺奖的核心。
8. **球状病毒理论（与 Caspar）**：与 Donald Caspar 共同发展「由不对称单元规则阵列构筑的球状壳层」的普适理论，并以 X 射线与电镜证实——FRS 当选证书重点表彰。
9. **1982 诺贝尔化学奖（独享）**：理由 "for his development of crystallographic electron microscopy and his structural elucidation of biologically important nucleic acid-protein complexes"——晶体电子显微术的发明与重要核酸-蛋白质复合物的结构解析。
10. **tRNA、锌指与神经原纤维**：研究转移 RNA 结构；发现「锌指」（zinc fingers）；发现阿尔茨海默病的神经原纤维。
11. **执掌 LMB 与皇家学会（1986–2000）**：LMB 主任（1986–1996）；皇家学会会长（1995–2000）；OM 勋章 1995（皇家学会会长的惯例荣誉）。
12. **Sanger 研究所的缔造者之一**：与 Dai Rees 共同接洽 Wellcome Trust 创办 Wellcome Sanger Institute——人类基因组计划的关键力量。
13. **身后纪念（2013）**：以色列本-古里安大学将其结构生物学中心命名为 Aaron Klug Integrated Centre for Biomolecular Structure。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深绿 deep green） | `#146B3A` | 晶格的秩序与生命结构的沉稳（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（电子显微术 badgeEM） | `#2E5A9E` | 蓝晶体电子显微术 / 三维重构 |
| 分类色 2（病毒结构 badgeVirus） | `#C0395B` | 玫瑰球状病毒理论 / TMV |
| 分类色 3（复合物结构 badgeComplex） | `#D97B29` | 琥珀核酸-蛋白质复合物 / tRNA / 锌指 |
| 分类色 4（学术领导 badgeLeadership） | `#1E4E79` | 藏青 LMB / 皇家学会 / Sanger 研究所 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「晶面投影 / 角度序列」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Daylight** — Alex-Productions（`music_audio/alex-productions/44-JoyIRE5k2Yo-Daylight.wav`；执行 Beamer 时复制为本目录 `Daylight.wav`，勿直接引用外部路径）
- **风格**：明亮 / 上行 / 释然
- **匹配理由**：
  - "Daylight（天光）" 匹配晶体电子显微术的本质——把看不见的分子结构照进光里、从二维投影重构三维真相
  - "明亮上行" 匹配其生涯弧线——从立陶宛小镇到开普敦再到剑桥 LMB 的持续攀升，92 岁高龄辞世前荣誉满盈
  - "释然" 匹配其学术领导者的从容——LMB 主任与皇家学会会长的十年沉静治理
- **时长对齐**：ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 把分子照进光里的人 / Aaron Klug 1926–2018 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/国籍/出生地/去世地/教育/博士/师承/领域/荣誉）
03  克卢格的一生 — Sanger 式时间线（10 节点：1926→1928→1953→1953→1962→1966→1982→1986→1995→2018）
04  从立陶宛到南非 (1926–1953) — 表格「时间|事件|结果」
05  剑桥博士与 Birkbeck 岁月 (1953–1962) — 表格「时间|事件|结果」（Franklin/Bernal/TMV）
06  LMB 与晶体电子显微术 (1962–1982) — 表格「问题|方法|结果」+ 公式框：二维投影序列→三维重构
07  球状病毒理论（与 Caspar） — 表格「问题|方法|结果」+ 公式框：不对称单元规则阵列壳层
08  1982 诺贝尔化学奖 — 表格「主题|内容|意义」+ 官方理由公式框（独享）
09  tRNA、锌指与神经原纤维 — 表格「对象|发现|意义」
10  LMB 主任与皇家学会会长 — 表格「职务|任期|意义」（1986–1996 / 1995–2000 / OM 1995）
11  Sanger 研究所与身后纪念 — Sanger FFT 页式流程图（Wellcome Trust → Sanger Institute → HGP → 2013 本-古里安命名中心）
12  荣誉清单 — Sanger 式「类别|代表|意义」表格（FRS 1969 / Copley 1985 / 骑士 1988 / OM 1995 / Mapungubwe 金章 2005）
13  遗产：结构生物学的方法革命 — 四分类遗产盒 + 公式框：晶体电子显微术的普适性
14  结尾 — 「从二维的影子，重构三维的真实。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1982 独享 | 诺贝尔化学奖 **独享**（无共同得主）——勿写共享 |
| 获奖理由 | "for his development of crystallographic electron microscopy and his structural elucidation of biologically important nucleic acid-protein complexes"——逐字对照 page.md，勿简写成"发明电镜" |
| 出生地与国籍 | 生于立陶宛 Želva（非俄罗斯、非波兰）；metadata 国籍仅 United Kingdom；南非是成长/受教育地（幼年移居），封面国籍行写英国 |
| 姓名 | **Sir Aaron Klug**（1988 年封骑士、1995 年获 OM）——头衔勿混 |
| OM 年份与缘由 | 1995 年获 Order of Merit——**皇家学会会长之惯例**；会长任期 1995–2000——勿写反 |
| Franklin 关系 | Rosalind Franklin 是 Birkbeck 时期的**共事者**（其介绍他进入 TMV 的 X 射线研究——出自 FRS 当选证书）；Franklin 已于 1958 年去世，非导师非配偶 |
| Hartree 口径 | 博士导师 Douglas Hartree 出自 infobox/metadata；正文只载 1851 奖学金 + Trinity College PhD 1953——两处口径并列呈现，不互相矛盾 |
| Caspar 理论 | 与 D. Caspar 共同发展球状壳层理论——出自 FRS 当选证书，可写"共同" |
| 锌指 | page.md 表述 "found what is known as zinc fingers"——"发现锌指"；勿写"发明"或展开机制（页面无载） |
| 博士生 | metadata 另有 Daniela Rhodes、John Thomas Finch，但**正文 infobox 未列**——禁入库禁写入门生页 |
| 引语 | FRS 当选证书英文段落可节选直引；**其余中文引号内容一律间接转述**（页面无其个人原话） |
| 妻子 | Liebe Bobrow（1948 年结婚；1979 年照片同框者即其夫人）——两子其一 2000 年先逝 |
| 同名区分 | Sir Aaron Klug 与别处 "Klug" 缩写（如 Doron Klug 等）无关；本篇只用 Aaron Klug |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q190626 | ✅ |
| name_zh | 阿龙·克卢格 | ✅ |
| name_en | Aaron Klug | ✅ |
| birth_date | 1926-08-11 | ✅ |
| death_date | 2018-11-20 | ✅ |
| nationality | United Kingdom（rank 0）/ South Africa（rank 1，成长与受教育地） | ✅ |
| primary_occupation | biophysicist | ✅ |
| field_of_work | biophysics（person_field 细分：biophysics / crystallographic electron microscopy / structural biology / molecular biology，带 rank） | ✅ |
| has_biography | 0（立传后置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 合作者 / 家人**（只收 page.md 正文或 infobox 明载；metadata-only 一律不入库）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Douglas Hartree | 师→生（博士导师，infobox 口径） | 剑桥 PhD 1953 |
| influence | Reginald W. James | 影响 | Witwatersrand 本科物理教师（BA 语境，非 advisor-student） |
| colleague | Rosalind Franklin | 无向 | Birkbeck 共事，引导其进入 TMV 的 X 射线研究 |
| colleague | J. D. Bernal | 无向 | Birkbeck 实验室主持人（晶体学家） |
| colleague | Donald Caspar | 无向 | 共同发展球状病毒壳层理论 |
| colleague | David Allan Rees | 无向 | 共同接洽 Wellcome Trust 创办 Wellcome Sanger Institute |
| spouse | Liebe Bobrow | 无向 | 1948 年结婚 |

> **禁入库名单（metadata.json-only）**：doctoral_student 含 Daniela Rhodes、John Thomas Finch，正文 infobox 无此二人——**不予入库**。Sydney Brenner 仅系转述其晚年信仰的来源人物，非学术关系，不入库。Cochran 与 Crick 仅出现在 FRS 证书对他人理论的引用中，非直接合作关系，不入库。

## 8. 奖项清单

- Nobel Prize in Chemistry（1982，独享）
- Louisa Gross Horwitz Prize, Columbia University（1981）
- Fellow of the Royal Society, FRS（1969）；Copley Medal（1985）
- Knight Bachelor（1988，伊丽莎白二世册封）
- Order of Merit, OM（1995；皇家学会会长惯例）
- Order of Mapungubwe in Gold, South Africa（2005）
- Fellow of the Academy of Medical Sciences, FMedSci（2005）
- Dr H.P. Heineken Prize for Biochemistry and Biophysics；Baly Medal；Croonian Medal and Lecture；Leeuwenhoek Lecture；Silliman Memorial Lectures
- Golden Plate Award of the American Academy of Achievement（2000）
- American Academy of Arts and Sciences / American Philosophical Society 会员
- 荣誉博士：Louis Pasteur University 等

## 9. 机构清单

- 教育：Durban High School、University of the Witwatersrand（BSc）、University of Cape Town（MSc）、Trinity College, University of Cambridge（PhD 1953）
- 任职：Birkbeck College, University of London（1953 年末–1962）；MRC Laboratory of Molecular Biology, Cambridge（1962–；主任 1986–1996）；Peterhouse, Cambridge Fellow（1962–）
- 学术服务：Advisory Council for the Campaign for Science and Engineering；The Scripps Research Institute 科学治理委员会；皇家学会会长（1995–2000）
- 命名机构：Aaron Klug Integrated Centre for Biomolecular Structure（Ben-Gurion University of the Negev，2013）

## 10. 终审清单

- [ ] 生卒 1926-08-11 / 2018-11-20（享年 92），出生地 Želva（立陶宛）、去世地剑桥
- [ ] 1982 **独享**、获奖理由逐字对照 page.md
- [ ] Hartree 口径（infobox）与正文 1851 奖学金并列不冲突
- [ ] OM 1995 = 皇家学会会长惯例；骑士 1988
- [ ] 博士生 Rhodes/Finch 仅存在于 metadata——已排除
- [ ] 引语仅 FRS 证书英文段落可节选；其余全为间接转述
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Aaron_Klug/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：`images/` 肖像已就位或装饰圆占位并注记（1979 同框照注意裁切或换图）
- [ ] 国籍：封面顶部明示英国
- [ ] 引语核对：仅 FRS 证书段落可直引
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐

---

> **名单状态**：由主控统一更新 `chemist/generate_20th_century_list.py`（执行者不改）。
