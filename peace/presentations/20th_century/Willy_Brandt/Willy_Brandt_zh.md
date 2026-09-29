# 诺贝尔和平奖得主立传提示词（Willy Brandt，1971）

## 一、模板定位

- **目标项目**：OpenPeace —— 诺贝尔和平奖得主人物史（OpenMathAI 共享仓库）。
- **本篇对象**：维利·勃兰特 Willy Brandt（本名 Herbert Ernst Karl Frahm，1913–1992），西德总理（1969–1974）、SPD 主席（1964–1987），1971 年诺贝尔和平奖得主。
- **设计哲学**：政治家立传以"东方政策（Ostpolitik）"为叙事主线——从纳粹流亡者到西柏林市长，从华沙之跪到东西方对话，用和解与条约讲和平。

## 二、背景信息 【人物专属】

- **姓名**：Willy Brandt（维利·勃兰特），本名 Herbert Ernst Karl Frahm；1913-12-18 生于吕贝克（自由市）~ 1992-10-08 逝于莱茵兰-普法尔茨州 Unkel，享年 78 岁（结肠癌）
- **1971 年诺贝尔和平奖，官方获奖理由（EN 原文照抄 Nobel 名录，禁止改写）**：
  > "for paving the way for a meaningful dialogue between East and West."
  > 中译（照抄 `OpenPeace_20th_Century_Nobel_Laureates.md`）：表彰他为东西方之间有意义的对话铺平了道路
- **气质关键词**：**新东方政策的设计师、华沙之跪的政治家、从流亡者到总理**
- **设计母题**：**跨界的桥（bridge across the wall）**——柏林墙、华沙纪念碑前的一跪、条约签字笔，视觉语言用墙的裂隙与桥拱。
- **本地数据源**：`peace/presentations/pages/20th_century/Willy_Brandt/page.md`

## 三、任务流程

### 第 0 步：事实基准 【人物专属，已核对 page.md】

- 生卒：1913-12-18 吕贝克 ~ 1992-10-08 Unkel，享年 78 岁；葬于柏林 Zehlendorf（国葬）
- 国籍：德意志帝国出生；德国籍 1938 被纳粹政府吊销、1948 恢复；挪威籍 1940–1948
- 家庭：母 Martha Frahm（百货收银员，单身母亲）；父 John Heinrich Möller（汉堡教师，从未见面）；继外祖父 Ludwig Frahm 抚养
- 婚姻：①Anna Carlotta Thorkildsen（1941 结婚，1948 离婚）②Rut Hansen（挪威裔作家，1948 结婚，1980 离婚，此后终生未见）③Brigitte Seebacher（1983-12-09 结婚）；子女四人：Ninja Frahm（1940）、Peter Brandt（1948，历史学家）、Lars Brandt（1951，作家）、Matthias Brandt（1961，演员）
- 教育：Johanneum zu Lübeck（1932 Abitur）；frontmatter educated_at 载 University of Oslo（流亡时期）；**page.md 正文未载大学学位，勿写大学学历细节**
- 党派：1929 社会主义青年团 → 1930 入 SPD（16 岁）→ 1931 转入左翼 SAP（与 Leber 决裂）→ 1948 重返 SPD
- 任职（含年份）：联邦议员（1949–1957、1969–1992）；西柏林市议会议员（1950–1971）；西柏林市长（1957-10–1966）；联邦外交部长兼副总理（1966-12-01–1969-10，Kiesinger 大联合内阁）；SPD 主席（1964-02-16–1987-06-14，后任荣誉主席）；联邦总理（1969-10-22–1974-05-06/07）；联邦议会党团后欧洲议会议员（1979–1983）；社会党国际主席（1976–1992）；北方南问题独立委员会主席（1977–1980，《勃兰特报告》）
- 关键荣誉：Nobel Peace Prize 1971；Time 年度人物 1970（首位获诺奖前一年当选的西德政治家）；Albert Einstein Peace Prize；Son of Peru 等大十字系列（frontmatter 载）
- 核心事业清单：①新东方政策（Ostpolitik）②《莫斯科条约》(1970-08-12)与《华沙条约》(1970-12) ③两德《基础条约》(1972-12-21) ④四国柏林协定(1971-09-03) ⑤《勃兰特报告》与南北对话 ⑥社会党国际复兴
- 关键时间线（15–20 节点）：1913 生于吕贝克 → 1929 入社会主义青年团 → 1930 入 SPD → 1931 转 SAP、结识 Leber（"decisive influence"）→ 1932 Abitur → 1933 流亡挪威、化名 Willy Brandt → 1934 参与创建国际革命青年组织局 → 1936 伪装挪威学生回国 → 1937 西班牙内战记者 → 1938 德国籍被吊销 → 1940 被盖世太保 arrest 后逃瑞典、获挪威籍 → 1941 与 Thorkildsen 结婚 → 1946 底回柏林（挪威政府职员）→ 1948 恢复德国籍、法律上改名 Willy Brandt、重返 SPD、与 Rut Hansen 结婚 → 1949 入联邦议会 → 1957–1966 西柏林市长（1957–58 任联邦参议院主席）→ 1961 柏林墙：公开信批评肯尼迪 → 1964 SPD 主席 → 1966 外长兼副总理 → 1969-10-22 总理（SPD-FDP 联盟）→ 联邦议院首秀 "Wir wollen mehr Demokratie wagen" → 1970-03-19 Erfurt 会 Stoph → 1970-08-12 《莫斯科条约》→ 1970-12 华沙条约+华沙之跪（Kniefall von Warschau）→ 1970 Time 年度人物 → 1971 诺贝尔和平奖 → 1972 建设性不信任案未过（Barzel 247 票）、11 月大选历史性胜利 → 1972-12-21 《基础条约》→ 1973 两德同入联合国 → 1974-04-24 Guillaume 被捕 → 1974-05-06 辞职 → 1976–1992 社会党国际主席 → 1977–1980 北南委员会与《勃兰特报告》(1980) → 1979–1983 欧洲议员 → 1989 呼应统一 "Now grows together what belongs together" → 1990 巴格达人质斡旋（1990-11-09 载 174 人归）→ 1992-10-08 逝于 Unkel

### 第 4 步：事业领域梳理 + 入库 【与 yaml fields 完全一致】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | ostpolitik | 新东方政策 | 与苏联/波兰/东德关系正常化，1971 诺奖核心 |
| 1 | diplomacy | 外交 | 东西方对话、条约体系 |
| 2 | european integration | 欧洲一体化 | 通过 EEC 强化西欧合作（导语明载） |
| 3 | social reform | 社会改革 | "内政改革总理"：教育/福利/住房 |
| 4 | north-south dialogue | 南北对话 | 《勃兰特报告》与南北鸿沟 |

### 第 4.5 步：社会关系梳理 + 入库 【与 yaml relations 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| influence | Julius Leber | 影响者 | 《Volksbote》主编，对其有"decisive influence" |
| spouse | Carlotta Thorkildsen | 无向 | 1941 结婚，1948 离婚 |
| spouse | Rut Brandt | 无向 | 挪威裔作家，1948 结婚 1980 离婚（维基标题 Rut Brandt） |
| spouse | Brigitte Seebacher | 无向 | 1983-12-09 结婚 |
| parent-child | Ninja Frahm | 父→女 | 1940 年生，Thorkildsen 所出 |
| parent-child | Peter Brandt | 父→子 | 1948 年生，历史学家 |
| parent-child | Lars Brandt | 父→子 | 1951 年生，作家 |
| parent-child | Matthias Brandt | 父→子 | 1961 年生，演员 |
| colleague | Helmut Schmidt | 无向 | 内阁国防部长，1974 年继任总理 |
| colleague | Egon Bahr | 无向 | SPD Federal Manager，Ostpolitik 同僚 |
| colleague | Bruno Kreisky | 无向 | 奥地利总理，社会党国际同僚（1983 争议中为其辩护） |
| rival | Herbert Wehner | 无向 | 党内长期对手（page.md 明载 longtime rival） |
| controversy | Günter Guillaume | 无向 | 私人助理被揭为东德特工，1974 年辞职导火索 |

- 入库规则：仅收 page.md 明载关系；Nixon/Kennedy/Adenauer/Kissinger/Gorbachev 等外交对手或同台者**不建关系**（仅会面/事件）；Markus Wolf 是 Guillaume 的上级非 Brandt 关系，不入库；Rudolf Bahro（会见+声援）为事件性接触不入库。

### 第 5 步：设计配色方案 【manifest 预分配，勿改主色】

- **主色**：`#52307C`（深紫——SPD 紫与冷战铁幕间的庄重）
- **辅助**：诺奖香槟金 `#C9A227` + 四分类色：
  - badgeA Ostpolitik — 钢蓝 `#3A7CA5`
  - badgeB 柏林岁月 — 军蓝 `#2F4470`
  - badgeC 社会改革 — 橄榄绿 `#6A8532`
  - badgeD 南北对话 — 琥珀 `#E07B30`
- **背景母题**：墙缝光束 + 柔和圆点。

### 第 6 步：幻灯片序列（10–16 页规划）

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 新东方政策的设计师 / Willy Brandt 1913–1992 + 四色 badge + 肖像位
02  身份信息页（★ 必做）— 本名/生卒/国籍变迁/婚姻/任职/荣誉/核心领域
03  核心贡献概览 — Ostpolitik / 莫斯科·华沙条约 / 基础条约 / 南北对话
04  早年：吕贝克与化名 (1913–1933) — 私生子、16 岁入党、SAP 决裂、流亡
05  流亡北欧 (1933–1945) — 挪威/瑞典记者、吊销国籍、盖世太保 arrest
06  西柏林市长 (1957–1966) — 城市重建、柏林墙、1961 公开信
07  外长与总理之路 (1964–1969) — SPD 主席、大联合、"mehr Demokratie wagen"
08  新东方政策 (1969–1973) — Erfurt/Stoph、六点方案、莫斯科与华沙条约（核心贡献页）
09  华沙之跪 (1970-12-07) — 纪念碑前一跪、世界反响与国内争议
10  1971 诺贝尔和平奖 — 官方理由原文 + 中译
11  1972 政治危机与大选 — 不信任案、Willy-Wahl、基础条约与入联
12  内政改革总理 — 教育/福利/住房数据一页
13  Guillaume 事件与辞职 (1974) — 客观记录、"I was exhausted"
14  后总理时代 — 社会党国际 16 年、《勃兰特报告》、巴格达人质
15  荣誉与遗产 — 1971 诺奖 · Time 1970 · 柏林机场冠名 · 华沙纪念碑
16  结尾
```

### 第 7 步：版式要点 【模板通用骨架 + 人物专属】

- 每页 `\newcommand{\xxxslide}{...}`；身份信息页参照成品 `\profileslide` 实现（信息量大，用双栏网格 + `arraystretch 0.62`）。
- 配色宏统一 `mainclr/accentclr/badgeA..D/panelA..D`，注释写语义。
- 表格页安全负间距：顶部 -0.35cm、`arraystretch 0.78–0.82`。

### 第 8 步：本人物专属陷阱表 【人物专属】

| 陷阱 | 说明 |
|------|------|
| 本名与化名 | 生于 Herbert Ernst Karl Frahm，1933 起化名 Willy Brandt 避纳粹追踪，1948 法律改名——三阶段勿混 |
| 获奖理由口径 | 官方 "for paving the way for a meaningful dialogue between East and West"；导语另有 "for his efforts to strengthen cooperation in Western Europe through the EEC and to achieve reconciliation…"，两口径勿混用 |
| 总理任期 | 1969-10-22–1974-05-06（辞职递交 5-06，页面 office 栏作 5-07 结束）——正文写 5 月 6 日辞职 |
| 华沙之跪 | 1970-12 访华沙纪念碑期间"unexpectedly and apparently spontaneously"下跪；国内争议大、国际反响正面——两面并写勿单边叙事 |
| 1948 情报背景 | 2021 年披露的 CIC 付费线人（1948–1952）是 page.md 明载，**只可一句客观事实，禁引申评价**；Hirschfeld 一并提及但细节不展开 |
| 冷战叙事红线 | Ostpolitik 两德/苏联/波兰条约、Radikalenerlass、越南战争沉默等均为历史事实，**只客观简述禁评价**；批评阵营（Heimatvertriebenen "high treason" 等）转述即可 |
| Guillaume | 1974-04-24 被捕、判 13 年；辞职为"触发因素而非根本原因"（Brandt 自述 "I was exhausted" 可引）；Wolf 事后说法可客观转述 |
| 家庭口径 | 三婚四子；离婚后与 Rut Brandt "never saw each other again"；1980 离婚年勿写 1981 |
| 无载禁写 | 大学学历（仅 frontmatter educated_at）、1961 大选票数细节、与 Adenauer/Kennedy 的私下关系评价 page.md 未载一律不写 |

### 第 9 步：术语清单

| 英文 | 中文 | 风险点 |
|------|------|------|
| Ostpolitik | 新东方政策 | (Neue) Ostpolitik，1969 后主线 |
| Kniefall von Warschau | 华沙之跪 | 1970-12，Warschauer Kniefall 同义 |
| Basic Treaty | 两德基础条约 | 1972-12-21 |
| Treaty of Moscow | 莫斯科条约 | 1970-08-12 |
| Treaty of Warsaw | 华沙条约 | 1970-12，奥得-尼斯线 |
| Four Power Agreement | 四国柏林协定 | 1971-09-03 |
| Grand Coalition | 大联合政府 | 1966–1969 Kiesinger 内阁 |
| constructive vote of no confidence | 建设性不信任投票 | 1972-04 Barzel 未过 |
| Brandt Report | 勃兰特报告 | 1980，南北鸿沟 |
| Socialist International | 社会党国际 | 1976–1992 任主席 |
| Radikalenerlass | 反激进法令 | 1972，国内争议政策 |
| Guillaume affair | 纪尧姆事件 | 1974 辞职导火索 |

---

## 四、背景音乐 ✅ 【manifest 预分配，勿改】

- **选定曲目**：**Through the Darkness** — Audiomachine
- **匹配理由**："穿越黑暗" 直白贴合其人生弧线——纳粹流亡的黑暗岁月、冷战的铁幕、1970 年代东西方破冰；史诗配乐气质匹配条约签署与华沙之跪的历史重量。
- **本地路径**：`music_audio/inspiring-electronic/14-Trn1cSsY2t8-Audiomachine - Through the Darkness.wav`

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Willy_Brandt/page.md` | 本地 Wikipedia 正文（事实基准） |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译（照抄） |
| `peace/nobel_peace_citations.json` | 官方获奖理由英文原文 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `MySQL/seed_person.py` | 入库引擎（幂等；本篇 UPD 复用库内 id=5828 回填 QID） |

---

## 六、执行清单

1. 建 `peace/presentations/20th_century/Willy_Brandt/` 目录 + `images/`；下载 Brandt 肖像（page.md 图库 1959 市长照/官方 1980 照，无 URL 则装饰圆占位）。
2. 复制 Makefile，设 `MAIN=Willy_Brandt_zh`、`VIDEO_NAME=Willy_Brandt_zh`。
3. 按 §三 第 6 步序列写 tex；每写一页 make 检查溢出（vbox≤10pt、hbox≤50pt）。
4. `pdftoppm` 逐页目检 → make images/video。
5. yaml 入库：`cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 seed_person.py data/Willy_Brandt.yaml`；验证 has_social_data=1（应命中库内 id=5828）。

---

## 七、版式补遗

- 页数上限 16 页：第 12 内政页与第 14 后总理时代页若溢出可各压至半页表格。
- 结尾页底部品牌统一 `OpenMathAI`；引号用半角 `" "`（"Wir wollen mehr Demokratie wagen" 与 "I was exhausted" 为 page.md 英文原文可引）。
- \foreach 时间线分隔符必须 ASCII 逗号；宏名禁数字。
