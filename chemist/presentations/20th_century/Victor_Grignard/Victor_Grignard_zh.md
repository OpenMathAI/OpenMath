# Victor Grignard（维克多·格氏 / 维克多·格里尼亚尔）立传提示词

> qid=Q104582 · 1871-05-06 – 1935-12-13 · 法国化学家 · 20 世纪 · 诺贝尔化学奖（1912，与 Paul Sabatier 共享）
> 本地 Wikipedia 数据源：`chemist/presentations/20th_century/pages/Victor_Grignard/`（page.md + metadata.json + page.html + images.txt）
> 版式基准：**参考 Frederick Sanger（Q151564）的立传提示词与 Beamer 格式**（`chemist/presentations/20th_century/Frederick_Sanger/Frederick_Sanger_zh.{md,tex}`）——身份信息页 + 表格语义化 tabularx + 公式展示框 + 时间线页。

---

## 0. 正文形式说明（参考 Sanger 立传模板，★ 硬性要求）

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框（tikz clip 圆角）+ 姓名小字注（肖像取本地 images/ 目录 `Victor_Grignard.jpg` 1912 年诺奖照，下载后使用；404 则用装饰圆占位并注明）。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{flask}\enspace C–C 键的锻造者\enspace·\enspace 法国`），底部状态栏给出 `国籍 | 机构 | 主要成就` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 2×2 信息网格，至少含：生卒、本名（François Auguste Victor Grignard）、国籍、出生地（Cherbourg）/去世地（Lyon）、教育（University of Lyon）、博士导师（Philippe Barbier）、核心领域（有机化学）、荣誉。事实取自本地 Wikipedia infobox，不得杜撰。
4. **配色 + 气泡背景**：主色 + 强调色 + 四分类色；背景用柔和气泡（稀疏大块实心圆）呼应「格氏试剂 / 有机分子」母题——离散圆点暗示 R-MgX 在无水乙醚中的活性粒子。
5. **表格语义化 + 公式框**（★ 高斯版式精髓，核心贡献页必须使用）：每页用 `tabularx` 三列表格，表头主色白字，第一列加粗用强调色，三列按页面主题语义化（问题 | 方法 | 结果）；表下配**金色边框浅金底公式展示框**（`\fcolorbox` + minipage），公式即最好的具象化。
6. **品牌口径统一**：结尾页底部品牌标注统一写 `OpenMathAI`（不是 `OpenChemist`）；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1–3）

- **全名**：François Auguste Victor Grignard（中文惯称：维克多·格里尼亚尔 / 格氏）
- **生卒**：1871-05-06 生于法国 Cherbourg（瑟堡）→ 1935-12-13 逝于法国 Lyon（里昂），享年 64；葬于里昂 Guillotière 公墓
- **国籍**：France（法国）
- **身份**：化学家（有机化学；格氏试剂与格氏反应以其命名）
- **家庭**：帆船帆具制造商（sailmaker）之子；妻 Augustine Marie Boulant；子 Roger Grignard
- **教育轨迹**：勤奋学生、性情谦和友善、有数学天赋 → 先主修数学，入学考试失利 → 1892 应征入伍（两年役期，升至下士 corporal）→ 1894 复员返里昂，获数学学位 Licencié ès Sciences Mathématiques → 1894-12 转化学，师从 Philippe Barbier（1848–1922）与 Louis Bouveault（1864–1909）
- **导师**：Philippe Barbier（博士导师；立体化学与 énines 方向不合其志趣后，他主动请 Barbier 指新方向）
- **博士**：1901，《Thèses sur les combinaisons organomagnésiennes mixtes et leur application à des synthèses d'acides, d'alcools et d'hydrocarbures》（University of Lyon）
- **研究领域**：有机化学——有机镁化合物、碳–碳键形成、合成方法学

## 2. 核心叙事亮点（用于 Slide 4–9，约 13 条）

1. **瑟堡帆具商之子（1871）**：谦和勤勉、数学见长——两次入学考试失利与一段军旅（1892–1894）之后才回到里昂。
2. **转系转折（1894-12）**：数学学位到手即转入化学，投入 Barbier 与 Bouveault 门下。
3. **Barbier 的难题**：Barbier 建议他研究一个失败的 Saytzeff 反应——用锌不理想、换镁低产率却可行；目标是从卤代烷、醛、酮、烯合成醇。
4. **关键假设与"先反应再加成"（1899–1900）**：Grignard 假设醛/酮的存在妨碍镁与卤代烷反应——于是**先把卤代烷与镁屑在无水乙醚中反应，再加醛/酮**，产率骤增。
5. **格氏试剂问世（1900）**：加热镁屑与异丁基碘、加干乙醚观察反应，分离出中间体——有机镁化合物 R-MgX（R = 烷基/芳基；X = 卤素，通常 Br 或 I）；同年《Compt. Rend.》130 卷 1322 页首篇论文；格氏反应就此得名。
6. **两步机理（1900–1901）**：第一步 R-X + Mg 生成格氏试剂（通式 R-Mg-X，实际结构更复杂）；第二步对羰基亲核加成、酸化水解得醇——碳–碳键的通用锻造法。
7. **博士论文（1901）**：《混合有机镁化合物及其在酸、醇与烃合成中的应用》。
8. **南锡岁月（1909–1910）**：1909 任 University of Nancy 有机化学讲师，1910 晋升正教授。
9. **1912 诺贝尔化学奖（共享）**："for his discovery of the Grignard reagent"（获奖理由页面口径：因其发现格氏试剂），与同胞 Paul Sabatier 共享；同年获 Lavoisier Medal（法国化学会）。
10. **一战：从哨兵到化学战研究员（1914–1918）**：以下士军衔再应征入伍站岗数月；因违规佩戴荣誉军团勋章被上级注意，参谋部查明后调入炸药部门；TNT 减产后转向化学武器——与 Georges Urbain 在索邦研究光气制造与芥子气检测；德方对应者是诺奖得主 Fritz Haber。
11. **战场芥子气检测法（1918）**：发现碘化钠可作芥子气战场检测——转化为更易结晶的二碘二乙硫醚，可检出 1 立方米空气中 0.01 g 芥子气，实战使用。
12. **身后规模（1935）**：逝世时关于格氏反应应用的论文已发表约 6,000 篇。
13. **荣誉军团三阶**：1912 获诺奖当年获 Chevalier（骑士），后晋 Officer，1933 晋 Commander（指挥官级）。

## 3. 配色方案（Sanger 式「主色 + 强调 + 分类色」）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（深藏青 deepnavy） | `#16324F` | 有机合成试剂的沉稳与工业化学的厚重（表头 / 公式文本） |
| 强调色（香槟金，用 OpenChemist 品牌色 coveraccent） | `#C9A227` | 诺贝尔 / 尊崇（公式框边线、字段标签） |
| 分类色 1（格氏试剂 badgeGr） | `#2E5A9E` | 蓝 R-MgX / 无水乙醚 |
| 分类色 2（格氏反应 badgeRx） | `#1B7A43` | 绿羰基加成 / C–C 键 |
| 分类色 3（师承与南锡 badgeAcad） | `#D97B29` | 琥珀 Barbier / Nancy |
| 分类色 4（战时化学 badgeWar） | `#C0395B` | 玫瑰光气 / 芥子气检测 |
| 背景 | `#F7F6F9` | 浅灰白（与 Sanger 一致） |

- **背景母题**：柔和气泡（稀疏大块实心圆，四档大小错落），呼应「格氏试剂 / 有机分子」。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **选定曲目**：**Timeless** — Alex-Productions（清单指定 `music_audio/alex-productions/42-SyPUvzEkPyc-Timeless.wav`）
- **风格**：沉稳 / 纪录片 / 经典长青
- **匹配理由**：
  - "Timeless" 匹配其贡献本质——格氏试剂至今仍是有机合成的基石方法，跨越百年不过时
  - "沉稳" 匹配其气质——帆具商之子、谦和友善、经挫折与军旅后才步入科学正轨的厚积薄发
  - "纪录片" 匹配传记叙事——瑟堡 → 里昂师承 → 1900 试剂问世 → 1912 诺奖 → 一战化学战 → 6,000 篇后续论文
- **时长对齐**：以曲目实际时长 > 15 页 × 7 秒为宜，ffmpeg `-shortest` 自动对齐

## 4. Slide 规划（15 页，Sanger 式结构）

```
00  OpenChemist 项目首页（\input cover/openchemist_page.tex）
01  封面 — C–C 键的锻造者 / Victor Grignard 1871–1935 + 四色 badge + 右上头像 + 国籍行（法国）
02  身份信息页（★ 必做）— 左头像 + 右 2×2 信息网格（生卒/本名/国籍/教育/博士/师承/出生地/去世地/领域/荣誉）
03  格里尼亚尔的一生 — 高斯式时间线（10 节点：1871→1892→1894→1900→1901→1909→1912→1914→1918→1935）
04  瑟堡与军旅 (1871–1894) — 表格「时间|事件|结果」
05  里昂：从数学到化学 (1894–1900) — 表格「问题|方法|结果」
06  格氏试剂 (1900) — 表格「问题|方法|结果」+ 公式框：R–X + Mg → R–MgX（无水乙醚）
07  格氏反应两步机理 (1901) — 表格「步骤|过程|产物」+ 公式框：R–MgX + R'₂C=O → 醇
08  南锡与 1912 诺贝尔化学奖 — 表格「事件|细节|意义」+ 公式框：1912 共享得主（与 Sabatier）
09  一战：从哨兵到研究员 (1914–1917) — 表格「阶段|任务|结果」
10  芥子气检测法 (1918) — 表格「问题|方法|结果」+ 公式框：碘化钠检出 0.01 g/m³
11  师承与同行 — 表格「人物|方向|结果」（Barbier / Bouveault / Urbain / Haber 对手）
12  荣誉与身后 — 高斯式「类别|代表|意义」表格（荣誉军团三阶 + 6,000 篇后续论文）
13  遗产：合成化学的通用工具 — 四分类遗产盒 + 公式框：格氏反应应用规模
14  结尾 — 「一根镁条与无水乙醚，锻造了碳–碳键的百年工具。」（无出处意境句）
```

## 5. 史实陷阱与敏感点（终审必须检查）

| 陷阱 | 正确表述 |
|------|------|
| 1912 共享 | 与 Paul Sabatier **共享**（Sabatier 因催化氢化，Grignard 因格氏试剂）——两人贡献不同，勿混写同一理由 |
| 1912 获奖理由 | 页面口径 "for his discovery of the Grignard reagent"（Honors 节）——**页面无载诺贝尔官方全句 citation**，禁杜撰完整官方措辞 |
| 发明年份 | 格氏反应发现于 **1900**（同年 Compt. Rend. 论文）；博士论文 **1901**——勿颠倒或合并 |
| 假设方向 | 他的假设是"醛/酮妨碍镁与卤代烷反应"→ 先制试剂再加成的两步法——勿写反 |
| 军旅两次 | 1892–1894 义务兵役（升至下士）与 1914 一战再入伍（仍以下士军衔站岗）是**两次不同**的服役——勿混 |
| 荣誉军团缘起 | 一战再入伍时因**违规佩戴荣誉军团勋章**被上级勒令摘下，反被参谋部注意、转入研究岗位——因果链勿写反 |
| 化学战对手 | 德方对应者 Fritz Haber——中性记载，禁加道德评价 |
| 芥子气检测 | 1918 年发现；碘化钠把芥子气转化为二碘二乙硫醚结晶析出——勿写"中和/解毒" |
| 同名区分 | 格氏反应（Grignard reaction）/ 格氏试剂（Grignard reagent）皆以其命名；他的儿子叫 Roger Grignard——勿与 Victor Grignard 混淆 |
| 任职口径 | 1909 Nancy 讲师、1910 正教授；infobox Institutions 仅列 University of Nancy——里昂是教育与博士阶段，勿写为任教机构 |
| metadata 噪声 | frontmatter award_received 含 Jecker Prize（无年份语境）——正文未载其获奖细节，引用需谨慎；Lavoisier Medal 1912 为正文 Honors 明载 |

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q104582 | ✅ |
| name_zh | 维克多·格里尼亚尔 | ✅ |
| name_en | Victor Grignard | ✅（清单 db_id 为空，按 page.md 规范名新建） |
| birth_date | 1871-05-06 | ✅ |
| death_date | 1935-12-13 | ✅ |
| nationality | France | ✅ |
| primary_occupation | chemist | ✅ |
| field_of_work | organic chemistry（person_field 细分：organic chemistry / organomagnesium chemistry / synthetic methodology，带 rank） | ✅ |

## 7. 社会关系入库清单

**师长 / 同行 / 共同得主**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Philippe Barbier | 师→生（博士导师） | 建议研究镁替代锌的 Saytzeff 反应难题 |
| colleague | Louis Bouveault | 无向 | 里昂同期共事的教授（1864–1909） |
| co-honored | Paul Sabatier | 无向 | 1912 诺贝尔化学奖共同得主 |
| colleague | Georges Urbain | 无向 | 一战在索邦共同研究化学战（光气、芥子气检测） |
| competitor | Fritz Haber | 无向 | 一战化学战研究德方对应者（同为诺奖化学家） |

**家人（page.md 正文 / infobox 明载）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| spouse | Augustine Marie Boulant | 无向 | 其妻（infobox） |
| parent-child | Roger Grignard | 家长→子女 | 其子（infobox） |

> 禁入库名单：Kazimierz-类情感线无；无 metadata-only 的师长/学生条目（metadata.json 未见 doctoral_student 字段）；Barbier 1848–1922 生卒可入 note。Bouveault 与 Grignard 为"共事教授"关系（page 明载 "began working with Professors Barbier and Bouveault"），以 colleague 入库。

## 8. 奖项清单

- Nobel Prize in Chemistry（1912，与 Paul Sabatier 共享；获奖理由页面口径 "for his discovery of the Grignard reagent"）
- Lavoisier Medal（1912，法国化学会 Société Chimique de France）
- Legion of Honour：Chevalier（1912）→ Officer → Commander（1933）
- Jecker Prize（frontmatter award_received 载；正文无细节，引用需谨慎）
- 诺贝尔演讲：1912-12-11《The Use of Organomagnesium Compounds in Preparative Organic Chemistry》

## 9. 机构清单

- 教育：University of Lyon / Faculté des Sciences de Lyon（1894 数学学位；1894-12 转化学；1901 博士）
- 任职：University of Nancy 有机化学讲师（1909）→ 正教授（1910）
- 战时：索邦大学化学战研究（与 Georges Urbain，1914–1918）；炸药部门 → 化学武器研究
- 安葬：里昂 Guillotière 公墓

## 10. 终审清单

- [ ] 生卒 1871-05-06 / 1935-12-13，享年 64，出生地 Cherbourg、去世地 Lyon
- [ ] 1912 与 Sabatier 共享表述准确；获奖理由只用页面口径、不杜撰官方全句
- [ ] 1900 反应发现 / 1901 博士论文年份准确；两步法假设方向正确
- [ ] 两次军旅（1892 与 1914）区分清楚；荣誉军团勋章轶事因果链正确
- [ ] 芥子气检测 1918、碘化钠原理、0.01 g/m³ 灵敏度准确
- [ ] Haber 对手关系中性记载；无引语杜撰（全文页面无直接引语）
- [ ] 正文采用 Sanger 式：身份信息页 + 时间线页 + 表格语义化 + 公式框 + 气泡背景 + 品牌 OpenMathAI
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/Victor_Grignard/page.md` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：`images/Victor_Grignard.jpg` 就位（1912 诺奖照）；404 用装饰圆占位并注明
- [ ] **国籍**：封面顶部明示法国
- [ ] **引语核对**：全文无直接引语（页面无载）——如有引号内容须改为间接转述
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Sanger 模板对齐（左头像 + 右 2×2 网格）
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与化学家侧既有格式（Sanger）对齐

---

> **名单状态**：`chemist/generate_20th_century_list.py` 由主控统一收尾；本文件由 chem-batch-01 agent 维护。
> **最重要的事：每写一页就 make，看到溢出就修。**
