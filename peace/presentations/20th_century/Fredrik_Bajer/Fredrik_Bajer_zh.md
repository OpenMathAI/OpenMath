# 和平奖得主立传提示词（OpenPeace 模板实例：Fredrik Bajer）

> **本文件是 OpenPeace 的「人物专属立传提示词」**，以 Kenneth_G_Wilson_zh.md（0–11 节结构母本）为结构标杆，
> 以 Frederick_Sanger.yaml 为 yaml 字段母本，为 Fredrik Bajer（1908 诺贝尔和平奖得主）定制。
> 凡标注 `【模板通用】` 的部分可原样复用；标注 `【人物专属】` 的部分为 Bajer 专属内容。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位 【模板通用】

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 体系，与 OpenPhysicist / OpenChemist / OpenMedic 平级）。
- **模板来源**：物理学家侧标杆 Kenneth_G_Wilson_zh.md 的任务流程骨架 + 诺贝尔奖立传通用版式。
- **本实例**：Fredrik Bajer（弗雷德里克·巴耶，1908 诺贝尔和平奖得主之一，丹麦）。
- **设计哲学**：和平奖得主立传强调「事业与机构」的结构化表达——Bajer 以军官出身的教师/作家/议员三重身份推动国际仲裁与妇女权利，须以身份信息页与事业领域表呈现「从战场到议会」的转型叙事。

---

## 二、背景信息 【人物专属】

- **目标人物**：Fredrik Bajer（1837-04-21 ~ 1922-01-22，享年 84 岁）
- **姓名**：英文 Fredrik Bajer；中文 弗雷德里克·巴耶
- **国籍**：丹麦（Kingdom of Denmark）
- **诺奖年份**：1908（与瑞典的 Klas Pontus Arnoldson 共享）
- **官方获奖理由英文原文**（照抄 nobel_peace_citations.json，禁止改写）：
  > "for their long time work for the cause of peace as politicians, peace society leaders, orators and authors."
- **官方获奖理由中译**（照抄名录 OpenPeace_20th_Century_Nobel_Laureates.md，禁止改写）：
  > 表彰他们以政治家、和平团体领导人、演说家与作家的身份长期为和平事业工作
- **气质关键词**：**从战场归来的和平军官、丹麦议会的外交拓荒者、北欧妇女权利的男性同盟**
- **设计母题**：**剑化为犁（swords to plowshares）**。Bajer 曾在 1864 年普奥战争中作战、升至少尉，退役后转而终身推动国际仲裁——「军刀改铸犁铧」的视觉母题贴合其人生弧线；封面可用剑与麦穗/橄榄枝的对照图形。
- **本地数据源**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Fredrik_Bajer/page.md`（Wikipedia 全文 + frontmatter）
- **参考模板**：
  - 结构标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`
  - 项目首页模板：`peace/presentations/cover/`（OpenPeace 共享封面）
  - yaml 字段母本：`MySQL/data/Frederick_Sanger.yaml`

---

## 三、任务流程 【模板通用骨架 + 人物专属内容】

> 每完成一步汇报，遇到歧义先征求主控意见再继续。
> **数据库同步要求**：包含「研究领域梳理 + 入库」（第 4 步）与「社会关系梳理 + 入库」（第 4.5 步），写入 `greatminds` 库（MySQL）。

### 第 0 步：事实基准 【人物专属，全部取自 page.md，无载禁补】

- 生卒：1837-04-21 生于丹麦奈斯特韦兹（Næstved）~ 1922-01-22 逝于哥本哈根，享年 84 岁
- 国籍：丹麦
- 家庭：牧师之子；配偶 Matilde Bajer（infobox 明载；其余家庭信息无载禁写）
- 教育：Sorø Academy（frontmatter educated_at 明载；专业/年份无载禁写）
- 军旅与退役：丹麦陆军军官，参加 1864 年对普鲁士与奥地利的第二次石勒苏益格战争（Second Schleswig War），晋升少尉（first lieutenant）；1865 年退役
- 任职机构与经历：
  - 1865 年后移居哥本哈根，成为教师、翻译与作家
  - 1872 年进入丹麦议会（Rigsdag） Folketinget（一院/人民院），连任 23 年
- 核心事业清单：
  1. 议员任内推动以国际仲裁解决国家间冲突
  2. 使外交关系成为丹麦议会工作的一部分
  3. 使丹麦自始参与各国议会联盟（Inter-Parliamentary Union）并在成员中赢得突出地位
  4. 支持早期妇女选举权组织（Kvindevalgretsforeningen）与众多和平组织（含国际和平局 IPB），遍及丹麦国内与全欧
  5. 推动丹麦与瑞典、挪威达成仲裁协定的法案通过
- 关键荣誉：1908 年诺贝尔和平奖（与 Klas Pontus Arnoldson 共享）
- 关键时间线（15 节点，全部 page.md/frontmatter 明载）：
  1. 1837-04-21 生于 Næstved，牧师之子
  2. 就读 Sorø Academy
  3. 服役丹麦陆军任军官
  4. 1864 参加第二次石勒苏益格战争（对普鲁士、奥地利）
  5. 战中晋升少尉
  6. 1865 退役
  7. 1865 移居哥本哈根
  8. 成为教师、翻译、作家
  9. 1872 进入丹麦议会 Folketinget
  10. 连任 23 年议员
  11. 推动外交事务进入议会日常工作
  12. 推动丹麦自始参与 Inter-Parliamentary Union
  13. 支持 Kvindevalgretsforeningen 与众多和平组织（含 IPB）
  14. 推动与瑞典、挪威的仲裁协定法案
  15. 1908 获诺贝尔和平奖（与 Arnoldson 共享）
  16. 1922-01-22 逝于哥本哈根

### 第 1–3 步：建目录 / 复制 Makefile / 收集图片 【模板通用】

- 在 `peace/presentations/20th_century/Fredrik_Bajer/` 下建 `images/`
- Makefile 设置 `MAIN=Fredrik_Bajer_zh`、`VIDEO_NAME=Fredrik_Bajer_zh`
- 肖像：page.md 的 images.txt 有 URL 则直接下载（250px 改 500px）；404 或无肖像用装饰圆占位

### 第 4 步：研究领域/事业领域表 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | peace movement | 和平运动 | 支持众多国内外和平组织（含 IPB） | 事业页 |
| 1 | international arbitration | 国际仲裁 | 议会推动仲裁 + 瑞挪仲裁协定 | 事业页 |
| 2 | women's rights | 妇女权利 | 支持早期妇女选举权组织 | 妇女权利页 |
| 3 | politics | 政治 | Folketinget 议员 23 年 | 议会页 |
| 4 | education | 教育 | 退役后任教师、翻译 | 早年页 |

- yaml `fields` 与上表一致（5 条）；入库 `person_field` 带 rank

### 第 4.5 步：社会关系表 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Klas Pontus Arnoldson | 无向 | 1908 诺贝尔和平奖共同得主 |
| spouse | Matilde Bajer | 无向 | 妻子 |
| colleague | Permanent International Peace Bureau | 无向 | 支持并担任国际和平局荣誉主席（IPB 页明载） |

- 对方 name_en 用 manifest 规范名 `Klas Pontus Arnoldson`、`Permanent International Peace Bureau`；`Matilde Bajer` 为新建 stub

### 第 5 步：配色方案 【模板通用，人物专属色彩】

- **气质**：北欧的沉静、军人转和平的坚韧、跨国民间外交
- **配色**：主色 `#145C54`（深青绿，manifest 预分配，勿改）+ 诺奖香槟金 `C9A227` + badgeA–D 四分类色
  - `badgeA` 和平运动 — 青绿 `#0E7C7B`
  - `badgeB` 国际仲裁 — 靛蓝 `#3F51B5`
  - `badgeC` 妇女权利 — 玫瑰 `#C4204F`
  - `badgeD` 议会与教育 — 琥珀 `#E07B30`
- **背景母题**：剑与犁的对照剪影 + 稀疏的橄榄枝圆点，呼应「剑化为犁」母题

### 第 6 步：规划幻灯片序列 【人物专属，12–14 页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 从战场到议会的和平先驱 / Fredrik Bajer 1837–1922 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒、国籍、配偶、教育、军旅、议会、荣誉、诺奖）
03  事业概览 — 和平运动 / 国际仲裁 / 妇女权利 / 议会生涯 / 教育
04  早年与军旅 (1837–1865) — 牧师之子、Sorø、1864 战争、少尉、退役
05  哥本哈根转型 (1865–1872) — 教师、翻译、作家
06  议会 23 年 (1872– ) — Folketinget、外交事务入议会
07  各国议会联盟 — 丹麦自始参与并赢得突出地位
08  国际仲裁事业 — 仲裁解决争端 + 瑞典、挪威仲裁协定法案
09  妇女权利 — Kvindevalgretsforeningen 的支持者
10  和平组织网络 — 国内外众多和平组织与国际和平局
11  1908 诺贝尔和平奖 — 与 Arnoldson 共享，官方理由（二人同句）
12  遗产 — 北欧仲裁与议会和平传统
13  结尾
```

### 第 7–8 步：Beamer 源码 + 布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照标杆 `\profileslide`
- 每写完一页 `make distclean && make`，`pdftoppm` 截图检查溢出/重叠
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标
- 表格页安全负间距：顶部 −0.35cm、`arraystretch` 0.78–0.82

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Bajer 专属陷阱表**：

| 陷阱 | 说明 |
|------|------|
| 军衔口径 | 晋升的是 **first lieutenant（少尉）**，是 1864 战争期间在军中的晋升；勿写成「上尉/中校」 |
| 议会起始年 | 1872 年进入 Folketinget，连任 **23 年**；「议会生涯起点」与「任期长度」两个数字勿混 |
| 战争名称 | 第二次石勒苏益格战争（1864，对普鲁士与奥地利），勿简写为「普丹战争」 |
| 协会名拼写 | 妇女选举权组织 Kvindevalgretsforeningen 保留丹麦语原名，附中译「妇女选举权协会」 |
| IPB 身份 | 国际和平局页面明载其为 IPB **荣誉主席（honorary president）**；Bajer 本人页面只写「支持 IPB」，立传时以本人页面口径「支持/参与」为主、荣誉主席身份可注 IPB 页来源 |
| 获奖理由口径 | 官方理由是 "their long time work"（二人共享、理由同句）；勿写成个人专属理由 |
| 配偶 | 配偶名 Matilde Bajer（infobox 明载）；其生平 page.md 无载，禁展开 |
| 无载禁写清单 | 出生家庭除「牧师之子」外的细节、Sorø 就读年份、退役军衔起点的完整履历、子女、与 Arnoldson 的私人交往、死亡原因——page.md 均无载，一律禁写 |
| 政治敏感红线 | 瑞典/挪威仲裁、石勒苏益格战争均按 page.md 客观表述，不加任何评价性语句 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| pacifist | 和平主义者 | 勿译「反战分子」 |
| Folketinget | 丹麦议会人民院 | 保留丹麦语原名 |
| Inter-Parliamentary Union | 各国议会联盟 | IPU，勿译「国际议会联盟」 |
| Second Schleswig War | 第二次石勒苏益格战争 | 1864 年 |
| first lieutenant | 少尉 | 勿升格军衔 |
| international arbitration | 国际仲裁 | 与 mediation（调停）区分 |
| women's suffrage | 妇女选举权 | Kvindevalgretsforeningen 的目标 |
| honorary president | 荣誉主席 | IPB 页明载身份 |
| Sorø Academy | 索勒学院 | 丹麦历史名校 |

---

## 四、背景音乐选择 【人物专属，manifest 预分配，勿改】

- **选定曲目**：**With Me** — Alex-Productions
- **bgm_path**：`music_audio/alex-productions/83-DXAblXgCK-k-With-Me.wav`
- **匹配理由**：温暖陪伴感的旋律，匹配 Bajer 与妻子 Matilde 并肩投身和平与妇女权利事业的「同行者」形象，以及其在议会内外寻求合作而非对抗的一生。
- **备选**（未采用，仅存档）：Nostalgia（怀旧感偏个人回忆）、Expedition（冒险感不贴合议会工作）。

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Fredrik_Bajer/page.md` | 本地 Wikipedia 正文（唯一事实来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆（0–11 节母本） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex` | Beamer 骨架参考 |
| `peace/presentations/cover/` | OpenPeace 共享封面 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等） |
| `peace/nobel_peace_citations.json` | 官方获奖理由英文原文 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译 |

> **开始执行。每完成一步汇报。**
