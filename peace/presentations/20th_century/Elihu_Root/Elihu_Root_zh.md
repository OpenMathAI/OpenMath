# 和平奖得主立传提示词（OpenPeace 实例：Elihu Root）

> 本文件是 OpenPeace 项目的「诺贝尔和平奖得主立传提示词」，以 Elihu Root（1912 诺贝尔和平奖，美国政治家/法学家）为完整实例。
> 结构对齐 OpenPhysicist 标杆 `Kenneth_G_Wilson_zh.md`（一~五节）。凡标注【模板通用】可复用，【人物专属】按本人物执行。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Elihu Root（伊莱休·鲁特），1912 诺贝尔和平奖得主，美国第 38 任国务卿、第 41 任战争部长。
- **设计哲学**：和平奖立传的「政治家型」样本——Root 的和平贡献（仲裁条约、美洲关系、卡内基基金会）嵌套在漫长的法律与政治生涯中，立传须以「国际法实践者」为主线剪裁史实，身份信息页必做。

---

## 二、背景信息 【人物专属】

- **目标人物**：Elihu Root（1845-02-15 ~ 1937-02-07，享年 91 岁）
- **气质关键词**：**政坛元老、国际仲裁的推手、美洲团结的缔造者**
- **官方获奖理由（英文原文照抄 nobel_peace_citations.json）**：
  > "for bringing about better understanding between the countries of North and South America and initiating important arbitration agreements between the United States and other countries"
  - **中译（照抄名录 OpenPeace_20th_Century_Nobel_Laureates.md，禁止改写）**：表彰他促进南北美洲各国之间的相互理解，并促成美国与其他国家间的重要仲裁协定
- **设计母题**：**天平与经纬（scale & meridian）**。Root 以律师之术治国、以仲裁之约连美洲——视觉语言宜用天平、地图经纬线、条约签署纹样。
- **本地数据源**：`peace/presentations/pages/20th_century/Elihu_Root/page.md`（Wikipedia 全文 + frontmatter，事实基准唯一来源）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属】

- 生卒：1845-02-15 生于纽约州克林顿 ~ 1937-02-07 卒于纽约市（享年 91）
- 国籍：美国（英裔移民后裔）
- 家庭：父 Oren Root（汉密尔顿学院数学教授）；兄 Oren Root II；妻 Clara Frances Wales（1878 结婚）；三子女 Edith（嫁 Ulysses S. Grant III）、Elihu Jr.、Edward Wales
- 宗教：虔诚的长老会信徒
- 教育：Clinton Grammar School、Williston Seminary（同学 G. Stanley Hall）→ 汉密尔顿学院 BA/MA（Sigma Phi、Phi Beta Kappa）→ 纽约大学法学院 LLB 1867（私塾式随 John Norton Pomeroy 多读一年）
- 任职时间线：
  - 律师（1867–1899：Mann and Parsons 见习 → Strahan & Root → Compton & Root → Root, Howard, Winthrop & Stimson；辩护 Tweed 案；客户含 Jay Gould、E. H. Harriman 等）
  - 纽约南区联邦检察官（1883-03-12 ~ 1885-07-06，Arthur/Cleveland 任内；Ward and Grant 庞氏案公诉）
  - 第 41 任美国战争部长（1899-08-01 ~ 1904-01-31，McKinley/Roosevelt 任内：陆军总参谋部、陆军战争学院、古巴/菲律宾/波多黎各民政政府、Foraker Act、Platt 修正案）
  - 第 38 任美国国务卿（1905-07-19 ~ 1909-01-27，Roosevelt 任内：领事服务改革、门户开放、1906 拉美之行促成各国参加海牙和平会议、Root–Takahira 协定、24 项双边仲裁条约）
  - 纽约州联邦参议员（1909-03-04 ~ 1915-03-03）
  - 卡内基国际和平基金会首任主席（1910–1925）
- 关键荣誉：Nobel Peace Prize 1912；比利时王冠大十字；ABA 第 38 任主席；美国国际法学会（1923）创始人之一；外交关系协会（CFR）创始主席（1918）
- 核心事业清单：
  1. 24 项双边国际仲裁条约（促成常设国际法院PCIJ的思路源头）
  2. 1906 拉美之行，促成拉美国家参加 1907 海牙和平会议
  3. 卡内基国际和平基金会首任主席（与 Andrew Carnegie 合作为国际和平与科学）
  4. 参与创建常设国际法院（PCIJ）法学家委员会
  5. 帮助创建海牙国际法学院；美国国际法学会创始人之一；美国和平学会副会长
  6. 1917 Root 使团赴俄（Wilson 派遣，与克伦斯基临时政府交涉）
- 关键时间线（15–20 节点）：1845 生于克林顿 → 汉密尔顿学院 → 1867 NYU LLB 取得律师资格 → 1868 Strahan & Root → 1871–73 Tweed 案辩护 → 1881 联邦最高法院出庭资格 → 1883–85 南区联邦检察官 → 1899 战争部长 → 1900 Foraker Act → 1901 Platt 修正案 → 1903 阿拉斯加边界仲裁（美方三人之一） → 1904 辞职 → 1905 国务卿 → 1906 拉美之行 → 1908 Root–Takahira 协定 → 1909 参议员 → 1910 卡内基基金会主席 → 1912 获诺贝尔和平奖 → 1913 参议员卸任 → 1917 Root 使团赴俄 → 1918 创立 CFR → 1919–20 支持国际联盟（附保留条款） → 1922 华盛顿海军会议代表 → 1923 美国国际法学会创立 → 1937-02-07 卒于纽约

### 第 4 步：研究领域/事业领域表 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | international arbitration | 国际仲裁 | 24 项双边条约 + PCIJ 法学家委员会 | 国务卿/晚年页 |
| 1 | international law | 国际法 | 开创美国国际法实务、ASIL/ALI | 律师/晚年页 |
| 2 | diplomacy | 外交 | 国务卿五年、美洲关系、对日对华 | 国务卿页 |
| 3 | military reform | 军事改革 | 总参谋部、陆军战争学院、民防转型 | 战争部长页 |

### 第 4.5 步：社会关系表（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | John Norton Pomeroy | advisor | NYU 法学院私塾式导师（多读一年） |
| spouse | Clara Frances Wales | 无向 | 1878 结婚 |
| parent-child | Oren Root | 无向 | 父亲，汉密尔顿学院数学教授 |
| parent-child | Edith Root | 无向 | 长女，嫁 Ulysses S. Grant III |
| parent-child | Elihu Root Jr. | 无向 | 长子，汉密尔顿学院毕业，律师 |
| parent-child | Edward Wales Root | 无向 | 幼子 |
| colleague | G. Stanley Hall | 无向 | Williston Seminary 同窗 |
| colleague | Theodore Roosevelt | 无向 | 长期政治盟友，两届内阁共事 |
| colleague | William Howard Taft | 无向 | 战争部长继任者、1912 共和党大会主席之争的伙伴 |
| colleague | Henry Cabot Lodge | 无向 | 阿拉斯加边界仲裁同僚、1919 国联保留条款同盟 |
| colleague | Woodrow Wilson | 无向 | 1917 派 Root 使团赴俄 |
| colleague | Andrew Carnegie | 无向 | 卡内基国际和平基金会首任主席（1910–1925） |
| influence | Joseph Hodges Choate | 无向 | 政界导师，1917 接任其 National Security League 主席 |
| founder | Council on Foreign Relations | 无向 | 1918 创始主席 |
| founder | American Law Institute | 无向 | 1923 创始人之一 |
| founder | The Hague Academy of International Law | 无向 | 帮助创建 |

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：庄重、法度、跨美洲的格局
- **主色**：蓝灰 `#37548D`（manifest 预分配，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgeARB` 国际仲裁 — 靛蓝 `#3F5E9E`
  - `badgeLAW` 国际法 — 青绿 `#0E7C7B`
  - `badgeDIP` 外交 — 琥珀 `#C9821F`
  - `badgeMIL` 军事改革 — 玫瑰 `#A34700`
- **背景母题**：经纬网格底纹 + 疏朗圆点，呼应「以条约连接美洲」的地理尺度

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 以法律缔造和平的政治家 / Elihu Root 1845–1937 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒/本名/国籍/家庭/教育/任职/荣誉/核心领域）
03  核心贡献概览 — 仲裁条约 / 美洲关系 / 卡内基基金会 / 国际法建制
04  克林顿律师之路 (1845–1899) — 汉密尔顿学院、Pomeroy 门下、Tweed 案、南区检察官
05  战争部长：军队现代化 (1899–1904) — 总参谋部、陆军战争学院、领地民政
06  国务卿：仲裁与美洲 (1905–1909) — 24 项条约、1906 拉美之行、Root–Takahira
07  参议员与 1912 (1909–1915) — 宪政保守立场、1912 共和党大会主席
08  诺贝尔和平奖 (1912) — 理由句原文呈现、卡内基基金会背景
09  一战与国际秩序 (1914–1920) — 备战运动、Root 使团赴俄、国联保留条款
10  晚年建制 (1918–1937) — CFR、PCIJ 法学家委员会、海牙国际法学院、ALI
11  争议与评价 — 反对妇女选举权（page.md 明载立场，客观简述）、Hearst 报系攻击
12  遗产：美国国际法的奠基人
13  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照 OpenPhysicist 成品 `\profileslide`。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Root 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖理由口径 | 诺奖理由=「美洲理解 + 仲裁协定」；正文另有 "for his efforts for spreading the use of arbitration in resolving international disputes" 的转述——两处均 page.md 明载，但官方理由句以 citations json 为准，勿混排 |
| 政治敏感 | Root 的菲律宾/古巴殖民治理、反妇女选举权立场、「布尔什维克/十月革命」相关叙述，一律**客观事实简述、不加评价**；Page/Insular Cases 等只作制度史陈述 |
| 1912 大会 | Root 任大会主席把提名计给 Taft，导致 Roosevelt 党内分裂——按 page.md 平铺史实，勿作党派评判 |
| 引语使用 | Tweed 案法官评语、1930 律政言论、1910 所得税信件等引语须核对 page.md 原文才可引用；「judicial review 是美国对政治学最有价值的贡献」为 page.md 转述，可引但注明出处 |
| 家庭 | 三子女与兄 Oren Root II 均明载；父 Oren Root 是数学教授；勿写母亲姓名外的杜撰细节（母 Nancy Whitney Buttrick 明载可写） |
| 职位序号 | 战争部长是第 41 任、国务卿是第 38 任、参议员为纽约州——序号勿互换 |
| 无载禁写 | 与 La Fontaine 提名世界法院候选人一事仅见于 La Fontaine 篇材料，本篇不建关系 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| arbitration treaty | 仲裁条约 | 24 项双边条约是其诺奖核心 |
| Root–Takahira Agreement | 《鲁特–高平协定》 | 1908，美日 |
| Platt Amendment | 普拉特修正案 | 1901，古巴 |
| Foraker Act | 福拉克法案 | 1900，波多黎各 |
| Carnegie Endowment for International Peace | 卡内基国际和平基金会 | 首任主席 |
| Council on Foreign Relations | 外交关系协会 | 1918 创始主席 |
| Permanent Court of International Justice | 常设国际法院 | 法学家委员会成员 |
| Preparedness Movement | 备战运动 | 1915 前后 |
| wise man | 政坛元老 | 20 世纪 wise man 原型（page.md 口径） |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Last Hope** — Victor Cooper（manifest 预分配，勿改）
- **风格**: 戏剧性 / 恢弘 / 有力
- **匹配理由**: 从战争部长到和平奖得主的身份张力——「Last Hope」的戏剧性弧线匹配其在战与和之间以法律架桥的一生；恢弘气质匹配卡内基基金会与 CFR 的建制格局
- **本地路径**: `music_audio/inspiring-electronic/24-ie5iLcdKiqk-Victor Cooper - Last Hope (Dramatic Powerful Epic Copyright Free Music).wav`
- **时长对齐**: ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Elihu_Root/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构标杆 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译 |
| `peace/nobel_peace_citations.json` | 官方获奖理由英文原文 |
| `MySQL/seed_person.py` | 研究领域 + 社会关系入库引擎 |

> **开始执行。每完成一步汇报。**
> **最重要的事：每写一页就 make，看到溢出就修；政治相关内容只作客观事实记录，无载禁写。**
