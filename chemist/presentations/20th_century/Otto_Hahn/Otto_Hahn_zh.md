# Otto Hahn（奥托·哈恩）立传提示词

> qid=Q57065 · 1879-03-08 – 1968-07-28 · 德国放射化学家 · 20 世纪 · 诺贝尔化学奖（1944，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Otto_Hahn/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景，是本次重写的核心版式语言。

---

## 0. 正文形式说明（参考化学家桑格立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像按 images.txt 优先用 1944 诺奖照或与 Meitner 合照；404 则装饰圆占位，图注如实标注）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{radiation}\enspace 核裂变的发现者\enspace·\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、国籍、出生地/去世地、教育、博士（1901 Marburg）、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「放射性衰变链」母题——离散圆点暗示原子核裂变碎片四散飞出的瞬间。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），如铀中子轰击 → 钡同位素判据 → ^{231}Pa 半衰期 32,500 年等具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Otto Hahn（中文惯称：奥托·哈恩；ForMemRS）
- **生卒**：1879-03-08 生于美因河畔法兰克福（普鲁士王国，德意志帝国）→ 1968-07-28 逝于哥廷根（下萨克森，西德），享年 89；葬于哥廷根 Stadtfriedhof（墓志铭指向其核裂变发现）；妻子 Edith 产后仅两周年亦去世——页面原文 "His wife Edith survived him by only a fortnight"
- **国籍**：Germany（德国；历经德意志帝国 / 魏玛 / 纳粹 / 西德四个时期，规范为 Germany）
- **身份**：放射化学家（radiochemist；「核化学之父」、核裂变发现者；1944 年诺贝尔化学奖得主）
- **家庭**：法兰克福 prosperous 玻璃匠 Heinrich Hahn 之幼子（Glasbau Hahn 公司创始人）；有异母兄 Karl 及两位兄长 Heiner、Julius。15 岁起在自家洗衣房做化学实验。1913-03-22 娶 Edith Junghans（1887–1968，柏林皇家艺术学校学生，1911 年 6 月什切青会议初识，1912 年 11 月订婚；其父 Paul Ferdinand Junghans 为什切青高阶法官、市议长）；蜜月于意大利加尔达湖 Punta San Vigilio，随后访问维也纳与布达佩斯——在布达佩斯寓居于 George de Hevesy 家。独子 Hanno Hahn（1922-04-09 生，装甲兵军官失去一臂，战后任罗马艺术史研究者，1960 年 8 月偕妻 Ilse 在法国考察途中车祸罹难，遗子 Dietrich）
- **教育轨迹**：
  - 1897 通过 Abitur，入 Marburg 大学学化学（副科数学、物理、矿物学、哲学）
  - 第三、四学期赴慕尼黑大学：有机化学随 Adolf von Baeyer、物理化学随 Wilhelm Muthmann、无机化学随 Karl Andreas Hofmann
- **导师**：Theodor Zincke（博士导师；毕业后回 Marburg 任其助手两年）
- **博士**：1901，Marburg 大学，《On Bromine Derivates of Isoeugenol》（经典有机化学方向）
- **研究领域**：放射化学、核化学（infobox Fields: Nuclear chemistry, Radiochemistry）

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **玻璃匠之子的洗衣房实验室（1879–1897）**：法兰克福工匠家庭，15 岁在自家洗衣房做化学实验；父亲想让他学建筑，他说服父亲改从工业化学。
2. **Marburg 博士（1901）**：论文《On Bromine Derivates of Isoeugenol》；因有博士学位只服一年兵役；随后任 Zincke 助手两年。
3. **伦敦：发现 radiothorium（1904–1905）**：为出国练语言到 UCL 随 William Ramsay 做放射化学——1905 年初从钍矿（Thorianite）中发现 radiothorium（钍-228）；Ramsay 在皇家学会代为宣布，《每日电讯报》头版式报道（活性为钍的 25 万倍）。
4. **蒙特利尔：Rutherford 门下（1905–1906）**：随 Rutherford 在 McGill 发现 radioactinium（钍-227）、钍 C、镭 D；Rutherford 评价 "Hahn has a special nose for discovering new elements."
5. **柏林木工房实验室（1906–1912）**：Emil Fischer 把化学研究所地下原木工房给他当实验室；数月内发现 mesothorium I（镭-228）、mesothorium II、ionium（钍-230）；1907 年通过 habilitation——Fischer 质疑「放射性物质少到只能靠放射性检出」，凭鼻子闻不出来，很快服气。
6. **遇见 Meitner（1907-09-28）**：在 Rubens 物理讨论班结识奥地利物理学家 Lise Meitner——开启**三十年合作与终身挚友**；她起初连研究所正门都不能进（普鲁士尚不收女大学生），只能从木工房外侧门进出。
7. **放射性反冲（1909）**：与 Meitner 正确演示并解释 α 衰变放射性反冲（Harriet Brooks 1904 年已观察但解释错误）；Gerlach 评之为「影响深远的物理学重大发现」。
8. **镤的发现（1917/1918）**：与 Meitner（一战中断，她任奥军 X 光护士后返所）找到镤的长寿命同位素（半衰期 32,500 年）；Fajans 认可二人以 protoactinium 命名；Soddy 与 Cranston 1918 年 6 月也提取出样品但承认哈恩—迈特纳优先权。IUPAC 1949 年确认 Hahn 与 Meitner 为发现者。
9. **核同质异能素（1921）**：发现铀 Z——第一个核同质异能素实例；「当时无人理解、后来对核物理意义重大」（Gerlach）；1936 年 von Weizsäcker 才给出理论解释。
10. **《Applied Radiochemistry》（1936）**：1933 康奈尔讲学整理成书——「应用放射化学」奠基之作；Glenn Seaborg 回忆此书是他在伯克利做钚工作时的 "bible"（页面明载整段回忆）。
11. **核裂变（1938）**：与 Strassmann（Meitner 1938 年 7 月流亡瑞典后持续通信，哈恩把母亲遗赠的钻石戒指送她）在 12 月 16–17 日决定性实验中发现「镭」同位素实为**钡**；12 月 19 日致 Meitner 信："We are more and more coming to the awful conclusion that our Ra isotopes behave not like Ra, but like Ba..."；12 月 22 日投稿《Naturwissenschaften》（1939-01-06 刊出）；理论解释由 Meitner 与 Frisch 完成（fission 一词借自生物学）；1939 年 1 月哈恩—施特拉斯曼首次使用 Uranspaltung 并预言裂变释放更多中子。
12. **Farm Hall（1945–1946）**：战时为德国核武器计划编目约百种裂变产物；1945-04-25 被 Alsos Mission 逮捕（"I have them all here" 交出 150 份报告），与 Heisenberg、von Laue、von Weizsäcker 等 10 人囚于英格兰 Farm Hall，谈话被窃听；1945-11-16 诺奖公布时仍在押——从《每日电讯报》上读到自己的获奖（11 月 18 日）；1946-01-03 获释。
13. **重建德国科学与和平呼声（1946–1960）**：KWS 末任主席（1946）→ 马普学会创始主席（1948–1960，预算 1200 万→4700 万马克、员工 1400→近 3000）；1955 年发起**马瑙宣言**（诺贝尔奖得主警告核武器危险）、1957 年联署**哥廷根宣言**反对西德核武装；1944 诺奖独享——"for his discovery of the fission of heavy atomic nuclei."（页面明载），1946-12-10 由瑞典国王 Gustav V 授奖；把 10,000 克朗奖金分给 Strassmann（后者拒绝动用）。

## 3. 配色方案（高斯式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深紫 deepviolet） | `#372A75` | 核裂变的深沉与原子核内部的未知（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（新放射性元素 badgeElements） | `#5E35B1` | 紫 radiothorium / mesothorium / 镤 |
| 分类色 2（核裂变 badgeFission） | `#B71C1C` | 红 1938 钡判据 / Uranspaltung |
| 分类色 3（与 Meitner 的合作 badgeMeitner） | `#00695C` | 青三十年合作 / 镭 D / 同质异能素 |
| 分类色 4（战后重建 badgeRebuild） | `#4527A0` | 深紫马普学会 / 马瑙与哥廷根宣言 |
| 背景 | `#F7F6F9` | 浅灰白（与桑格版一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「裂变碎片与衰变链节点」——一个原子核分裂后四散的新核。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**SEA** — Alex-Productions（文件 `92-WEqfdRXU3IU-SEA.wav`；不要复制 wav 到本目录，Makefile 由主控预置）
- **风格**：深海般辽阔 / 沉稳厚重 / 命运感
- **匹配理由**：
  - "深海" 匹配核裂变之重——一次发现改写人类能源与战争格局的分量
  - "沉稳" 匹配其品格——Max Planck 学会讣告所谓 "integrity and personal humility"（页面明载）
  - "命运感" 匹配 Farm Hall 与战后重建——从囚禁听广播的谷底到马普学会创始主席、两份和平宣言的高峰
- **时长**：以曲目实际时长为准 > 15 页 × 7 秒 ≈ 105 秒 → ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，高斯式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 核裂变的发现者 / Otto Hahn 1879–1968 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  哈恩的一生 — 高斯式时间线（10 节点：1879→1901→1905→1906→1907→1918→1938→1944→1948→1968）
04  早年与 Marburg 博士 (1879–1904) — 表格「时间|事件|结果」
05  伦敦与蒙特利尔 (1904–1906) — 表格「地点|导师|发现」+ 公式框：radiothorium 228Th
06  柏林木工房与遇见 Meitner (1906–1912) — 表格「问题|方法|结果」
07  镤与核同质异能素 (1917–1921) — 表格「挑战|方法|结果」+ 公式框：镤 231Pa 半衰期 32,500 年
08  应用放射化学 (1936) — 表格「对象|内容|影响」（Seaborg "bible" 回忆）
09  核裂变 (1938–1939) — 表格「问题|方法|结果」+ 公式框：U + n → Ba 判据 · Uranspaltung
10  Farm Hall 与 1944 诺奖 — 表格「处境|事件|结果」（获释/授奖/分奖金给 Strassmann）
11  马普学会与和平呼声 — 高斯式「类别|代表|意义」表格（马瑙宣言 1955 / 哥廷根宣言 1957）
12  传承与命名 — 高斯式流程图（核化学之父 → 奥托哈恩号核动力船 / Otto Hahn 奖章与奖项 / 月面 Hahn 环形山 / 105 号元素命名之争终归 dubnium）
13  遗产：原子时代的第一页 — 四分类遗产盒 + 公式框：1999《Focus》 poll 20 世纪最重要科学家第三位（爱因斯坦、普朗克之后）
14  结尾 — 「他打开了原子核，也用余生守住了良知。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1944 诺奖理由 | 官方措辞 "for his discovery of the fission of heavy atomic nuclei."（页面明载整句，1945-11-16 公布）；**独享**——勿写成与 Meitner/Strassmann 共享 |
| 诺奖时序 | 1945-11-18 在 Farm Hall 从《每日电讯报》读到获奖；**1946-12-10** 才由 Gustav V 授奖（囚禁不能赴会 + 旅行许可拖延）——三个年份勿混 |
| 裂变分工 | 化学证据（钡）出自 Hahn 与 Strassmann；理论解释（fission）出自 **Meitner 与 Frisch**——页面同时载有后世批评（Meitner 落选反映诺贝尔委员会的性别歧视与反犹、化学家/物理学家分歧等），如实并述、勿单边洗白 |
| Meitner 关系 | 三十年合作 + 终身挚友，**非师非偶**——1938 年流亡前哈恩赠其母亲遗钻戒（细节可写，勿升格关系性质） |
| 一战化学战 | 哈恩在 Haber 化学战部队服役（与 Franck、Hertz 侦察毒气阵地、亲历毒气回流与俄军惨状）——按页面如实叙述，勿回避亦勿渲染 |
| 1933 言论 | 哈恩 1933 年对多伦多《Star Weekly》吹捧希特勒的访谈为页面明载——敏感：如引用须完整交代后文（他是纳粹反对者、战时保护犹太同僚家属），否则整段略过 |
| 名言红线 | 可引原文仅限页面明载整句：1938-12-19 致 Meitner 信、"I have them all here"、"Hahn has a special nose for discovering new elements."（Rutherford）、Seaborg "bible" 回忆、马普学会讣告——其余一律间接转述 |
| protactinium 优先权 | Fajans 与 Göhring 首先发现该元素（短半衰期 brevium）；哈恩—迈特纳发现的是**长寿命母同位素**并获命名权；Soddy/Cranston 承认其优先——三层关系勿混 |
| habilitation | 1907 年初通过，无需论文（以一篇放射性论文代之）——勿写 "habilitation 论文《……》" |
| 死亡细节 | 1962 年下车折断颈椎、渐衰，1968-07-28 逝于哥廷根；妻 Edith 仅比他多活两周——勿写「同年去世」模糊表述 |
| 1951 枪击 | 1951 年 10 月被一心怀不满的发明家背后开枪（为唤起对其构想被忽视的注意）——如使用需克制一笔带过 |
| 同名区分 | 月面 Hahn 环形山与其同名者 **Friedrich von Hahn** 共享；105 号元素 hahnium 提案 1997 年被 IUPAC 否决定为 dubnium；108 号元素最终名 hassium——三个化学元素命名结局勿混 |
| 学生口径 | infobox Doctoral students 七人：Born、Seelmann-Eggebert、Flügge、von Grosse、Riehl、Rosenblum、Strassmann；metadata 另有 Abdul Hafeez、Clara Lieber 无正文载，**不予入库** |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q57065 | ✅ |
| name_zh | 奥托·哈恩 | ✅ |
| name_en | Otto Hahn（复用库内 #2055 记录形式） | ✅ |
| birth_date | 1879-03-08 | ✅ |
| death_date | 1968-07-28 | ✅ |
| nationality | Germany（帝国/魏玛/纳粹/西德四期规范为 Germany） | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | radiochemistry（person_field 细分：radiochemistry / nuclear chemistry / nuclear fission，带 rank） | ✅ |
| has_biography | false（Beamer 立传完成后由主控置 1） | ✅ |

## 7. 社会关系入库清单

**师长 / 合作者 / 共事者**（仅收 page.md 正文或 infobox 明载）：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Theodor Zincke | 师→生（博士导师） | 1901 年 Marburg 博士，毕业后任其助手两年 |
| advisor-student | William Ramsay | 师→生（infobox other academic advisors） | 1904–1905 伦敦 UCL 随其做放射化学，发现 radiothorium |
| advisor-student | Ernest Rutherford | 师→生（infobox other academic advisors） | 1905–1906 McGill 随其工作 |
| colleague | Adolf von Baeyer | 无向 | 慕尼黑第三、四学期随其学有机化学（课程语境，非博导） |
| colleague | Emil Fischer | 无向 | 柏林化学研究所所长，拨地下木工房为其实验室 |
| colleague | Lise Meitner | 无向 | 1907 相识，三十年合作与终身挚友；共发现镤、反冲、同质异能素；1938 共证裂变化学证据 |
| colleague | Fritz Haber | 无向 | 一战在其化学战部队服役；柏林学界同侪 |
| colleague | James Franck | 无向 | 一战化学战部队同侪（共赴佛兰德斯侦察阵地）；战后代存其诺奖奖章 |
| colleague | George de Hevesy | 无向 | 柏林—布达佩斯学界友人，1913 年蜜月期间借住其布达佩斯寓所 |
| influence | Glenn Seaborg | 哈恩→塞博格 | Seaborg 自述《Applied Radiochemistry》是其在伯克利做钚工作时的 "bible" |
| advisor-student | Fritz Strassmann | 哈恩 → 学生 | infobox Doctoral students；1938 共同发现核裂变化学证据 |
| advisor-student | Hans-Joachim Born | 哈恩 → 学生 | infobox Doctoral students |
| advisor-student | Walter Seelmann-Eggebert | 哈恩 → 学生 | infobox Doctoral students |
| advisor-student | Siegfried Flügge | 哈恩 → 学生 | infobox Doctoral students |
| advisor-student | Aristid von Grosse | 哈恩 → 学生 | infobox Doctoral students |
| advisor-student | Nikolaus Riehl | 哈恩 → 学生 | infobox Doctoral students |
| advisor-student | Salomon Rosenblum | 哈恩 → 学生 | infobox Doctoral students |
| spouse | Edith Junghans | 无向 | 1913-03-22 结婚于什切青，1968 仅比哈恩多活两周 |
| parent-child | Hanno Hahn | 哈恩 → 子 | 独子，艺术史研究者，1960 年车祸罹难 |

> **禁入库名单**（metadata.json 有、page.md 正文与 infobox 无）：Abdul Hafeez、Clara Lieber（metadata doctoral_student）。Gustav Hertz、Max von Laue、Werner Heisenberg、Otto Robert Frisch、Niels Bohr、Max Planck 等仅在事件叙述中出现（同囚 Farm Hall / 讨论班合影 / 书信往来），无明确合作或师承关系，**不入库**。

## 8. 奖项清单

- Nobel Prize in Chemistry（1944，独享；1946-12-10 授奖；诺奖演讲标题页面未载，勿杜撰）
- Emil Fischer Medal（1922）；Cannizaro Prize（1938）；Copernicus Prize（1941）；Cothenius Medal（1943）
- Max Planck Medal（1949，与 Lise Meitner 同获）；Goethe Medal of Frankfurt（1949）
- Golden Paracelsus Medal（1953）；Faraday Lectureship Prize（1956）；Grotius Medal（1956）
- Wilhelm Exner Medal（1958）；Helmholtz Medal（1959）；Harnack Medal in Gold（1959）
- Legion of Honour, Officer（1959）；Grand Cross 1st Class, Order of Merit of the Federal Republic of Germany（1959）
- Enrico Fermi Award（1966，与 Lise Meitner、Fritz Strassmann 同获）
- Foreign Member of the Royal Society（1957）；Honorary Fellow, University College London；荣誉市民：法兰克福与哥廷根（1959）、柏林（1968）

## 9. 机构清单

- 教育：Klinger Oberrealschule（法兰克福）→ Marburg 大学（1897–；1901 博士）→ 慕尼黑大学（第三、四学期）
- 任职：Marburg（Zincke 助手两年）→ University College London（1904–1905，Ramsay）→ McGill University（1905–1906，Rutherford）→ 柏林弗里德里希-威廉大学化学研究所（1906–；1907 habilitation；1910 教授）→ 威廉皇帝化学研究所 KWIC（1912 放射性部主任；1928 所长；1944-02-15 大楼被炸后迁 Tailfingen）→ 威廉皇帝学会末任主席（1946）→ 马普学会创始主席（1948–1960，1962 起荣誉主席）
- 战时：德国核武器计划（编目约百种裂变产物同位素）；1945-04-25 被 Alsos Mission 逮捕，囚于 Farm Hall（1945-07 至 1946-01-03）

## 10. 终审清单

- [ ] 生卒 1879-03-08 / 1968-07-28，享年 89，出生地法兰克福、去世地哥廷根；Edith 多活两周
- [ ] 1901 Marburg 博士《On Bromine Derivates of Isoeugenol》，博导 Zincke
- [ ] radiothorium 1905（Ramsay 门下）；radioactinium / ionium；mesothorium I/II 1906–07（柏林）
- [ ] 镤 1917/1918（与 Meitner，Fajans 认可命名，Soddy/Cranston 承认优先）；铀 Z 1921 首例核同质异能素
- [ ] 1938-12-16/17 决定性实验 → 钡判据 → 12-19 致 Meitner 信 → 12-22 投稿；理论解释属 Meitner/Frisch
- [ ] 1944 诺奖**独享**，理由 "for his discovery of the fission of heavy atomic nuclei."；1946-12-10 授奖；10,000 克朗分给 Strassmann（其拒用）
- [ ] Farm Hall 1945-07 至 1946-01-03；马普学会创始主席 1948–1960；马瑙 1955 / 哥廷根 1957 宣言
- [ ] 引语全部可在本地 Wikipedia 原文找到（1938 信、"special nose"、Seaborg 回忆、讣告等页面明载句）
- [ ] 正文采用高斯式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Otto_Hahn/page.md`（639 行，超长注意分段）建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：按 images.txt 装载（诺奖照或哈恩—迈特纳 1913 合照优先；404 则装饰圆占位并如实标注）
- [ ] **国籍**：封面顶部明示德国
- [ ] **引语核对**：所有引号内原话须在 Wikipedia 原文找到；其余不得出现引号内"原话"
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与桑格模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式对齐
