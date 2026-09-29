# 医学家立传提示词（Konrad Emil Bloch）

> 本文件是 OpenMedic 项目（OpenMathAI 诺贝尔生理学或医学奖人物史）20 世纪 1964 年得主 Konrad Emil Bloch 的人物专属立传提示词。
> 事实基准：`medic/presentations/pages/20th_century/Konrad_Emil_Bloch/page.md`（唯一事实来源，metadata.json 仅作参考）。
> 结构对齐标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（11 节合并为 9 节）。
> ★ 库内原有 stub 'Konrad E. Bloch'（id=4095）已改名对齐 manifest 'Konrad Emil Bloch'，yaml 走 UPD 回填 Q35698。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Konrad Emil Bloch（1912-01-21 生于德意志帝国普鲁士西里西亚奈斯（今波兰尼萨） ~ 2000-10-15 逝于美国马萨诸塞州伯灵顿，享年 88 岁）
- **气质关键词**：**胆固醇合成之路的测绘者、同位素示踪大师、从纳粹德国流亡的 biochemist** —— 1964 年诺贝尔生理学或医学奖（与 Feodor Lynen 共享）获奖理由（逐字引用 `medic/nobel_medicine_citations.json`）：
  > "for their discoveries concerning the mechanism and regulation of the cholesterol and fatty acid metabolism"（因其关于胆固醇与脂肪酸代谢的机制与调控的发现）
- **设计母题**：**碳原子的归途（tracing every carbon）**。用放射性乙酸作面包霉的饲料，把胆固醇分子里每一个碳原子都追溯回乙酸——一条三十余步的合成之路由此显形。视觉语言：放射性标记的乙酸分子汇入一条通向胆固醇四环骨架的长路。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Konrad_Emil_Bloch/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）
- **关键时间线（身份信息页与时间轴素材，均出自 page.md）**：
  - 1912-01-21 生于奈斯（Neisse，今波兰尼萨），犹太中产家庭（父 Frederich D. "Fritz" Bloch，母 Hedwig，原姓 Striemer）
  - Gymnasium Carolinum（尼萨）就读；1930-1934 慕尼黑工业大学学化学
  - 1934 因纳粹迫害犹太人出逃达沃斯瑞士研究所，1936 移居美国
  - 曾任职耶鲁医学院生物化学系
  - 哥伦比亚大学生物化学博士（1938）
  - 1939-1946 任教哥伦比亚；后转芝加哥大学
  - 1954 任哈佛 Higgins 生物化学教授（至 1982）；1979-1984 兼公共卫生学院教授
  - 哈佛退休后任佛罗里达州立大学 Mack and Effie Campbell Tyner 杰出学者讲席
  - 1964 与 Lynen 共享诺贝尔奖（胆固醇/脂肪酸代谢的机制与调控）
  - 合成链：乙酸（历经多步）→角鲨烯→胆固醇；放射性乙酸+面包霉（真菌亦产角鲨烯）+大鼠验证
  - 与 Lynen 各自证明乙酰辅酶 A→甲羟戊酸→活化异戊二烯
  - 发现胆汁与雌性激素由胆固醇生成→推及所有类固醇均源自胆固醇
  - 1964-12-11 诺贝尔演讲《胆固醇的生物合成》
  - 1941 与 Lore Teutsch 在美国结婚（慕尼黑初识）；子女 Peter Conrad 与 Susan Elizabeth
  - 长居马萨诸塞州列克星敦 Six Moon Hill 中世纪现代主义社区；好滑雪、网球、音乐
  - 1985 当选皇家学会 Fellow；1988 获美国国家科学奖章；AAAS/NAS/美国哲学学会院士
  - 2000-10-15 卒于伯灵顿（充血性心衰）；妻 Lore 2010 卒（享年 98）

---

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章执行 Beamer 立传，**第 0/1/2/3 步按 medic 路径执行**：
> - 页面与元数据：`medic/presentations/pages/20th_century/Konrad_Emil_Bloch/`（page.md / metadata.json / images.txt）
> - 目录创建：`medic/presentations/20th_century/Konrad_Emil_Bloch/` 与 `images/`
> - Makefile：复制 medic 侧同结构模板，设 `MAIN=Konrad_Emil_Bloch_zh`
> - 肖像：正文含 1963 年肖像与 1964 全家福缩略 URL（250px 改 500px，curl 加 `-A "Mozilla/5.0"`，file 验证）；404 用 Commons `Special:FilePath` 回退；均失败用装饰圆占位
> 每完成一步汇报，溢出即修（make → pdftoppm 逐页目检）。

---

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biochemistry | 生物化学 | 诺奖核心：胆固醇与脂肪酸代谢的机制与调控 | 核心页 |
| 1 | lipid metabolism | 脂质代谢 | 胆固醇合成通路（乙酸→角鲨烯→胆固醇） | 核心页 |
| 2 | isotope tracing | 同位素示踪 | 放射性乙酸标记法（面包霉+大鼠验证） | 方法页 |
| 3 | steroid biochemistry | 类固醇生化 | 胆汁/性激素/所有类固醇皆源自胆固醇的推论 | 成就页 |

---

## 四、社会关系梳理 + 入库 【人物专属】

> 与 `MySQL/data/Konrad_Emil_Bloch.yaml` 完全一致；只收 page.md 明载的关系。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Feodor Felix Konrad Lynen | 无向 | 1964 诺贝尔生理学或医学奖共享（胆固醇与脂肪酸代谢的机制与调控） |
| spouse | Lore Teutsch | — | 慕尼黑初识，1941 在美国结婚 |
| parent-child | Peter Conrad Bloch | — | 子 |
| parent-child | Susan Elizabeth Bloch | — | 女 |
| parent-child | Fritz Bloch | — | 父（Frederich D. "Fritz" Bloch） |
| parent-child | Hedwig Striemer | — | 母 |

**不入库裁定**：两名孙辈（Benjamin Nieman Bloch、Emilie Bloch Sondel）不入库；耶鲁医学院任职段无具体关系人不入库；★妻子 Lore Teutsch 姓 Teutsch，与同批 Bloch 无关（防混同）。

## 五、配色方案 【人物专属】

- **气质**：缜密、耐心的路径测绘者，把一个分子拆成三十步的账本
- **主色**：脂质深青 `#175873`（与人物气质呼应——示踪图谱的冷静蓝绿）
- **诺奖色**：香槟金 `#D4AF37`
- **四分类色（badgeA-D）**：
  - `badgeA` 生物化学——代谢琥珀 `#B4632A`
  - `badgeB` 脂质代谢——胆固醇灰蓝 `#3A6FA8`
  - `badgeC` 同位素示踪——放射青 `#2E7D6B`
  - `badgeD` 类固醇生化——四环金 `#C89B3C`
- **背景母题**：放射性标记点沿通路渐次汇入四环骨架（对应"碳原子的归途"），badge 四色错落

### 5.1 医学家格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + 细边框 + 姓名小字注；无真实肖像用装饰圆占位并注明。
2. **封面有国籍**：底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（02 页）：左头像 + 右信息网格，含生卒、出生地、教育、师承、任职、荣誉、核心领域；事实取自 page.md infobox，不得杜撰。
4. **品牌口径统一**：结尾页底部品牌标注写 `OpenMedic`；引号用半角 `" "`。
5. **获奖理由逐字引用** `medic/nobel_medicine_citations.json` 原文 + 中译，不得改写或扩写。

---

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input medic 封面模板）
01  封面 — 胆固醇之路的测绘者 / Konrad Emil Bloch 1912–2000 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、奈斯、慕尼黑工大/哥伦比亚博士、哈佛 Higgins 教授、荣誉、核心领域）
03  核心贡献概览 — 胆固醇合成通路 / 脂肪酸代谢 / 同位素示踪方法 / 类固醇同源推论
04  西里西亚与流亡（1912–1936）— 犹太家庭、慕尼黑工大、1934 达沃斯、1936 赴美
05  哥伦比亚与教职链（1936–1954）— 1938 博士、哥伦比亚/芝加哥、耶鲁医学院任职段
06  哈佛岁月（1954–1982）— Higgins 教授、公共卫生学院、FSU 讲席
07  放射性乙酸与面包霉（核心贡献页一）— 每个碳原子皆可追至乙酸；真菌亦产角鲨烯；大鼠验证
08  乙酸→角鲨烯→胆固醇（核心贡献页二）— 多步合成通路的显影
09  与 Lynen 的接力 — 各自证明乙酰辅酶 A→甲羟戊酸→活化异戊二烯；"mostly separately"
10  类固醇同源 — 胆汁与雌性激素源自胆固醇→所有类固醇同源推论
11  1964 诺贝尔奖 — 理由句、演讲《胆固醇的生物合成》（1964-12-11）、诺贝尔委员会的心脑卒中视角
12  荣誉与认可 — FRS 1985、国家科学奖章 1988、AAAS/NAS/APS 院士、Guggenheim
13  家庭与晚年 — Lore Teutsch、Six Moon Hill、滑雪/网球/音乐、2000 卒于伯灵顿
14  结尾 — 一个分子，三十步，一条被完整测绘的路
```

---

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方逐字为 "for their discoveries concerning the mechanism and regulation of the cholesterol and fatty acid metabolism"——注意 **their**（与 Lynen 共享）；citation json 内姓名为短名 "Konrad Bloch"，yaml/页面用 manifest 全名 |
| 分工表述 | 与 Lynen "mostly separately" 各自发现角鲨烯生成与转化步骤；Bloch 侧贡献：全碳原子溯源、面包霉与大鼠验证、类固醇同源推论；Lynen 侧：acetyl-CoA 结构与 biotin——接力勿混 |
| 库内记录 | 原 stub 'Konrad E. Bloch'(id=4095) 已改名 'Konrad Emil Bloch' 对齐 manifest（循 Gasser 主控裁定先例），yaml UPD 回填 Q35698，勿新建 |
| 国籍口径 | metadata 国籍 Germany+United States、citizenship 双列；总表/诺奖口径 **United States**——yaml 只写美国，出生德国在页面呈现 |
| 学位口径 | 博士是哥伦比亚大学生物化学博士（1938）；慕尼黑工大是本科/前期学习（1930-1934，未完成即出逃）——勿写"慕尼黑博士" |
| 师承缺位 | page.md 未载博士导师姓名——**禁止杜撰**；师承页只写"哥伦比亚大学博士（1938）" |
| 任职顺序 | 哥伦比亚任教 1939-1946 → 芝加哥大学 → 1954 哈佛 Higgins 教授；1979-1984 兼公共卫生学院教授（与 Higgins 期末段重叠，按正文表述）；退休后 FSU——勿写乱 |
| 实验材料 | 放射性乙酸实验用**面包霉**（真菌也产角鲨烯），再以**大鼠**确认——两步材料勿混 |
| 生卒双源 | metadata 与正文一致（1912-01-21 / 2000-10-15，充血性心衰，伯灵顿） |
| metadata 噪声 | metadata occupations 未列 physician；primary_occupation 按 biochemist；父母姓名以 page.md 为准（父名含昵称引号 "Fritz"） |

---

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| cholesterol | 胆固醇 | 诺奖核心词 |
| fatty acid metabolism | 脂肪酸代谢 | citation 原文用语 |
| squalene | 角鲨烯 | 胆固醇直接前体 |
| acetate / acetic acid | 乙酸（盐） | 示踪起点 |
| acetyl Coenzyme A | 乙酰辅酶 A | 与 Lynen 分工的关键词 |
| mevalonic acid | 甲羟戊酸 | 通路中间物 |
| isoprene | 异戊二烯 | 活化前体 |
| radioactive tracer | 放射性示踪 | 方法论关键词 |
| steroid | 类固醇 | 同源推论对象 |
| bread mold | 面包霉 | 实验材料（真菌产角鲨烯） |
| Higgins Professor | 希金斯教授 | 哈佛讲席名，勿意译 |

---

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Tragedy**（manifest 预分配）
- **匹配理由**：1934 年的出逃与家族离散是暗线，而通路的测绘是一场漫长的孤独劳动——"悲剧"气质承载流亡的底色；音乐后半宜转向寻得通路的开阔与释然
- **本地路径**：`music_audio/` 下检索曲名（参照 `curated_tracks.md`），复制到 `medic/presentations/20th_century/Konrad_Emil_Bloch/Tragedy.wav`
- **时长**：曲长须 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐

