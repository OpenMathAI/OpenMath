# Hermann Staudinger（赫尔曼·施陶丁格）立传提示词

> qid=Q48956 · 1881-03-23 – 1965-09-08 · 德国有机化学家 · 20 世纪 · 诺贝尔化学奖（1953，独享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Hermann_Staudinger/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger 立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 高斯式时间线 + 表格语义化 tabularx + 公式展示框，是本次书写的核心版式语言。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像 `images/` 已就位；若无真实肖像按 Review-1 流程先补图，全部 404 才允许装饰圆占位）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace 高分子化学之父\enspace·\enspace 德国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名、国籍、出生地/去世地、教育、博士、师承、核心领域、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「大分子 / 长链」母题——离散圆点首尾相连暗示单体聚合成链。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：Hermann Staudinger（中文惯称：赫尔曼·施陶丁格）
- **生卒**：1881-03-23 生于德国帝国沃尔姆斯（Worms）→ 1965-09-08 逝于西德弗莱堡（Freiburg），享年 84（page.md frontmatter 卒日双值 09-08/09-09，infobox 正文为 8 September 1965，**取 09-08**）
- **国籍**：Germany（德国）
- **身份**：有机化学家、高分子化学奠基人（organic chemist / polymer chemist）
- **家庭**：1906 年娶 Dora Förster（后称 Dora Staudinger，曾为其整理讲稿），育有四子女（含 Eva Lezzi 1907–1993、Klara Kaufmann，二女积极抵抗法西斯崛起），1926 年离婚；Dora 再婚后成为著名和平活动家。1927 年娶拉脱维亚植物学家 Magda Voita（Magda Staudinger，又作 Magda Woit）——她与他合作直至其去世，施陶丁格在诺贝尔奖受奖辞中致谢其贡献
- **教育轨迹**：
  - 最初志向是植物学家，后改学化学
  - 哈勒大学（University of Halle）、达姆施塔特工业大学（Technische Hochschule Darmstadt，获 Verbandsexamen，约硕士）、慕尼黑大学求学
  - 1903 哈勒大学博士（论文 *Anlagerung des Malonesters an ungesättigte Verbindungen*）
  - 1907 斯特拉斯堡大学取得任教资格（habilitation）
- **导师**：Daniel Vorländer（哈勒大学博士导师，infobox 明载）
- **研究领域**：有机化学与高分子化学——烯酮（ketenes）、Staudinger 反应、大分子（Macromoleküle）学说、缩聚与加聚
- **晚年驻地**：1926 年起执教弗莱堡大学直至终老

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **沃尔姆斯少年（1881）**：本想当植物学家，却在哈勒、达姆施塔特、慕尼黑之间走上化学之路。
2. **哈勒博士（1903）**：师从 Daniel Vorländer，完成丙二酸酯与不饱和化合物加成研究。
3. **斯特拉斯堡与烯酮（1905–1907）**：发现烯酮（ketenes）这一全新化合物家族——日后青霉素、阿莫西林等 β-内酰胺抗生素合成的重要中间体。
4. **卡尔斯鲁厄岁月（1907–1912）**：任助理教授，分离多种实用有机物；指导出两位未来诺奖得主的研究生——Leopold Ružička（1910）与 Tadeusz Reichstein。
5. **苏黎世联邦理工与 Staudinger 反应（1912–1919）**：与同事 Meyer 报告有机叠氮化物与三苯基膦生成亚氨基膦烷的反应（叠氮 + PPh₃ → 亚氨基膦烷 + N₂↑），高产率，今日仍是化学生物学点击化学的基石。
6. **一战中的 lone voice（1914–1918）**：拒绝签署《九十三人宣言》，与 Max Born、Otto Buek、Albert Einstein 同列谴责者；1917 年撰文预言德国必败并呼吁尽快和谈——遭 Fritz Haber 攻击，他反批 Haber 的化学武器计划。
7. **1920 划时代论文《Über Polymerisation》**：提出橡胶、淀粉、纤维素、蛋白质是由共价键首尾相连的长链大分子——"聚合物如回形针串"。
8. **孤军奋战（1920s）**：Emil Fischer、Heinrich Wieland 等主流有机化学家坚持"高表观分子量只是小分子聚集成胶体"；多数同行拒绝接受共价大分子。
9. **弗莱堡与大分子学说确证（1926–1930s）**：1926 年任弗莱堡大学化学讲师（此后再未离开）；膜渗透压测定、溶液黏度测量、Herman Mark 的 X 射线衍射、Carothers 的尼龙与聚酯合成——1930 年代证据链全面闭合。
10. **黏度法与分子量**：以稀溶液黏度测定大分子分子量，为高分子表征建立标准方法（1933 Faraday Soc. 论文）。
11. **预言合成纤维（1936）**："sooner or later a way will be discovered to prepare artificial fibers from synthetic high-molecular products"——远早于产业 realization。
12. **创办第一本高分子期刊（1940）**：*Die Makromolekulare Chemie* 前身——高分子化学自此有了自己的学术阵地。
13. **1953 诺贝尔化学奖与遗产**：官方理由 "for his discoveries in the field of macromolecular chemistry"（独享）；1999 年 ACS 与德国化学会将其工作定为 International Historic Chemical Landmark；德国化学会 1971 年起设 Hermann Staudinger Prize。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（酒红深棕 burgundy） | `#9E2B25` | 高分子长链的坚韧与工业时代的厚重（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（烯酮化学 badgeKetene） | `#B4632A` | 琥珀烯酮 / Staudinger 反应 |
| 分类色 2（大分子学说 badgeMacro） | `#2E5A9E` | 蓝共价长链 / Makromoleküle |
| 分类色 3（黏度与表征 badgeVisc） | `#1B7A43` | 绿黏度法 / 渗透压 |
| 分类色 4（高分子产业 badgePolymer） | `#6E4E7E` | 紫尼龙 / 合成纤维 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），圆点成链呼应「单体 → 大分子」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Ascension** — Cold Cinema（文件：`music_audio/inspiring-electronic/20-gYUC-sXt_8M-Cinematic Dramatic Epic Orchestra Sci-Fi Trailer by Cold Cinema [No Copyright Music] ⧸ Ascension.wav`；勿复制 wav，视频阶段直接引用路径）
- **风格**：史诗 / 上行 / 恢弘配乐
- **匹配理由**：
  - "上行（Ascension）" 匹配其学术轨迹——从烯酮到 Staudinger 反应再到大分子学说，一步步把"胶体谬误"顶翻成一门新学科
  - "史诗" 匹配其孤军奋战的叙事——主流学界拒绝二十年，证据终于闭合时的正名感
  - "预告片式" 匹配工业遗产——尼龙、合成纤维、塑料时代由他的理论开门
- **时长**：以实际文件为准，视频合成用 ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — 高分子化学之父 / Hermann Staudinger 1881–1965 + 四色 badge + 右上头像 + 国籍行
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  施陶丁格的一生 — 时间线（10 节点：1881→1903→1907→1912→1919→1920→1926→1940→1953→1965）
04  早年：从植物学到化学 (1881–1907) — 表格「时间|事件|结果」
05  烯酮的发现 (1905–1907) — 表格「问题|方法|结果」+ 公式框：烯酮通式 R2C=C=O
06  Staudinger 反应 (1919) — 表格「反应物|条件|产物」+ 公式框：叠氮 + PPh3 → 亚氨基膦烷 + N2
07  一战中的和平之声 (1914–1918) — 表格「时间|事件|结果」（拒签 93 人宣言 / 1917 预言败战 / 与 Haber 论战）
08  1920：大分子学说的诞生 — 表格「旧观念|新假说|证据」+ 公式框：聚合物 = 单体共价长链
09  孤军奋战二十年 (1920s) — 表格「反对者|主张|反转」（Fischer/Wieland 胶体说）
10  弗莱堡与证据闭合 (1926–1940) — 表格「方法|贡献|结果」（渗透压/黏度/X 射线/尼龙）
11  荣誉与承认 — 「类别|代表|意义」表格 + itemize 荣誉清单（1953 诺奖 / Rudolf Diesel Medal 1962 / 历史地标 1999）
12  遗产：高分子改变世界 — 流程图（理论 → 尼龙/纤维/塑料 → 现代生活）
13  科学之外 — 婚姻家庭（Dora/Magda）+ 和平立场 + 敏感点回避说明
14  结尾 — 「回形针串成的长链，串起了整个高分子时代。」
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1953 诺奖 | **独享**；官方措辞 "for his discoveries in the field of macromolecular chemistry"——勿写成"发明塑料"或"与 Carothers 共享" |
| 生卒日 | 1881-03-23 / **1965-09-08**（frontmatter 有 09-09 噪声，以 infobox 正文 8 September 1965 为准） |
| 烯酮年份 | 烯酮发现于斯特拉斯堡时期，1905 年论文《Ketene, eine neue Körperklasse》——勿写成卡尔斯鲁厄时期 |
| Staudinger 反应年份 | **1919**（与 Meyer，苏黎世 ETH 时期）——勿与 1920 大分子论文混淆 |
| 1920 论文 | 《Über Polymerisation》发表于一战后的 1920 年（Ber. Dtsch. Chem. Ges.）——大分子学说起点 |
| 反对者口径 | Emil Fischer 与 Heinrich Wieland 主张**胶体聚集**致高表观分子量——是"学术观点对立"，非人身竞争，勿渲染成"论战骂战" |
| Meyer 其人 | 页面仅载单姓 "colleague Meyer"，无全名——**禁写全名、禁入库**（无法规范匹配） |
| 拒签宣言 | 拒签《九十三人宣言》并与 Born/Buek/Einstein 同列谴责者——是**并列事实**，非合作研究，勿写成"与 Einstein 合作" |
| 敏感点：SS | 页面明载 1935 年成为 SS 的 Patron Member（Förderndes Mitglied der SS）——建议整页回避；若必须写，仅客观一句并置于"争议"小节，禁止渲染 |
| 两位诺奖门生 | Ružička（1910 博士，1939 化学诺奖）与 Reichstein（1950 生理学或医学诺奖）均在卡尔斯鲁厄受博士训练——勿写"在弗莱堡指导" |
| 妻子分工 | 第一任 Dora 为其整理讲稿；第二任 Magda 为合作者且在其诺奖受奖辞中被致谢——勿混淆两位妻子事迹 |
| 姓名拼写 | 第二任 Magda Voita / Magda Woit / Magda Staudinger 三种写法并存，正文统一用 Magda Staudinger |
| Ružička 撞批 | Ružička（1939 化学奖）在本项目 20 世纪名单内（chem-batch-06），对手方名用规范全名 "Leopold Ružička" 防分裂 stub |
| 引语口径 | 1936 合成纤维预言为页面原文引用；无其他直接引语——页面无载的"名言"一律禁写 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q48956 | ✅ |
| name_zh | 赫尔曼·施陶丁格 | ✅ |
| name_en | Hermann Staudinger | ✅ |
| birth_date | 1881-03-23 | ✅ |
| death_date | 1965-09-08 | ✅ |
| nationality | Germany | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | polymer chemistry（person_field 细分：polymer chemistry / macromolecular chemistry / organic chemistry / ketene chemistry，带 rank） | ✅ |

## 7. 社会关系入库清单

**师长 / 门生 / 学术对手**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Daniel Vorländer | 师→生（博士导师） | 哈勒大学，1903 博士论文 |
| advisor-student | Leopold Ružička | Staudinger → 学生 | 卡尔斯鲁厄 1910 博士；1939 诺贝尔化学奖 |
| advisor-student | Tadeusz Reichstein | Staudinger → 学生 | 卡尔斯鲁厄受博士训练；1950 诺贝尔生理学或医学奖 |
| advisor-student | Werner Kern | Staudinger → 学生 | infobox Doctoral students |
| advisor-student | Rudolf Signer | Staudinger → 学生 | infobox Doctoral students |
| spouse | Dora Staudinger | 无向 | 1906 结婚，1926 离婚；曾整理其讲稿 |
| spouse | Magda Staudinger | 无向 | 1927 结婚；植物学家，合作至终老，诺奖受奖辞致谢 |
| competitor | Hermann Emil Fischer | 无向 | 反对大分子共价学说，主张胶体聚集说 |
| competitor | Heinrich Wieland | 无向 | 同上，主流"胶体说"阵营 |
| other | Fritz Haber | 无向 | 一战公开论战：Haber 指责其 1917 文章危害德国，Staudinger 反批其化学武器计划 |

> **禁入库名单**（页面有载但无法/不宜入库）：Meyer（页面仅载单姓，无法规范匹配全名）；Max Born、Otto Buek、Albert Einstein（仅"并列拒签 93 人宣言"，非个人关系）；Rolf Mülhaupt、Herman Mark、Wallace Carothers（文献综述语境提及，非直接关系）。

## 8. 奖项清单

- Nobel Prize in Chemistry（1953，独享）
- Emil Fischer Medal（德国化学会）
- Fresenius Prize
- Rudolf-Diesel-Medaille（1962）
- Commander's Cross of the Order of Merit of the Federal Republic of Germany
- Great Cross with Star and Sash of the Order of Merit of the Federal Republic of Germany
- 斯特拉斯堡大学荣誉博士；法兰克福物理学会荣誉会员
- International Historic Chemical Landmark（1999，ACS + 德国化学会，授其大分子学说）
- 德国化学会 Hermann Staudinger Prize（1971 年设立，以其命名）

## 9. 机构清单

- 教育：University of Halle（PhD 1903）、Technische Hochschule Darmstadt（Verbandsexamen）、Ludwig-Maximilians-Universität München
- 任职：University of Strasbourg（1907 任教资格）、Technical University of Karlsruhe（1907 助理教授）、ETH Zurich（1912–）、University of Freiburg（1926–1965，终老）
- 命名遗产：*Die Makromolekulare Chemie*（1940 创办，首本高分子期刊）；Hermann Staudinger Prize（1971–）

## 10. 终审清单

- [ ] 生卒 1881-03-23 / 1965-09-08（享年 84），出生地 Worms、去世地 Freiburg
- [ ] 1953 独享表述准确；获奖理由用官方原文口径
- [ ] 烯酮 1905（斯特拉斯堡）/ Staudinger 反应 1919（ETH）/ 大分子论文 1920 三条时间线不错位
- [ ] Ružička、Reichstein 博士训练在卡尔斯鲁厄；Werner Kern、Rudolf Signer 仅 infobox 明载
- [ ] Meyer 仅单姓不入库；Einstein/Born/Buek 仅并列拒签不入库
- [ ] 1935 SS Patron Member 敏感点按 §5 口径处理（回避或一句客观）
- [ ] 引语仅 1936 合成纤维预言（页面原文）；其余无直接引语
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] 结合本地 Wikipedia：读取 `pages/Hermann_Staudinger/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] 头像：`images/` 肖像就位与图注核对（Commons 404 则用 Wikipedia REST API page/summary 查 infobox 原图名）
- [ ] 国籍：封面顶部明示德国
- [ ] 引语核对：引语必须在 Wikipedia 原文找到（1936 预言、1953 获奖理由）
- [ ] 编译验证：`make distclean && make`
- [ ] 更新提示词：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger 黄金骨架）对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾，本提示词不改动该文件。
> **数据入库**：yaml 见 `MySQL/data/Hermann_Staudinger.yaml`（新建记录 NEW，含 5 fields / 10 relations）。
