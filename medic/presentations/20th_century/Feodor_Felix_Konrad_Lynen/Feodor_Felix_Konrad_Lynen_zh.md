# 医学家立传提示词（Feodor Felix Konrad Lynen）

> 本文件是 OpenMedic 项目（OpenMathAI 诺贝尔生理学或医学奖人物史）20 世纪 1964 年得主 Feodor Felix Konrad Lynen 的人物专属立传提示词。
> 事实基准：`medic/presentations/pages/20th_century/Feodor_Felix_Konrad_Lynen/page.md`（唯一事实来源，metadata.json 仅作参考）。
> 结构对齐标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（11 节合并为 9 节）。
> ★ 库内已有同名 stub 'Feodor Felix Konrad Lynen'（id=3540，无 qid），yaml 走 UPD 回填 Q44597。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Feodor Felix Konrad Lynen（1911-04-06 生于德意志帝国慕尼黑 ~ 1979-08-06 逝于西德慕尼黑，享年 68 岁）
- **气质关键词**：**乙酰辅酶 A 的解构者、活化乙酸通路的阐明者、马克斯·普朗克细胞化学研究所首任所长** —— 1964 年诺贝尔生理学或医学奖（与 Konrad Emil Bloch 共享）获奖理由（逐字引用 `medic/nobel_medicine_citations.json`）：
  > "for their discoveries concerning the mechanism and regulation of the cholesterol and fatty acid metabolism"（因其关于胆固醇与脂肪酸代谢的机制与调控的发现）
- **设计母题**：**被激活的乙酸（activated acetic acid）**。乙酸本身惰性，挂上辅酶 A 才成为代谢的通货——Lynen 解出了乙酰辅酶 A 的化学结构，为整条脂代谢通路提供了钥匙。视觉语言：乙酸分子扣上 CoA"手柄"的瞬间、由此铺开的萜类与脂肪酸岔路。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Feodor_Felix_Konrad_Lynen/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）
- **关键时间线（身份信息页与时间轴素材，均出自 page.md）**：
  - 1911-04-06 生于慕尼黑（父 Wilhelm Lynen 为机械工程教师；母 Frieda，原姓 Prym，实业家之女）
  - 1930 入慕尼黑大学（LMU）化学系
  - 1937-03 在 Heinrich Wieland 指导下毕业，论文《鬼笔鹅膏中的毒性物质》
  - 1937-05-14 娶导师之女 Eva Wieland（1915-2002）；1938-1946 间育有五子女
  - 二战全程留在德国；1942 任 LMU 化学讲师
  - 1947 任助理教授；1953 任生物化学教授
  - 1954 起任马克斯·普朗克细胞化学研究所所长（该职为其而设，由 Otto Warburg 与 Otto Hahn 促成）
  - 1972 该所并入新成立的马克斯·普朗克生物化学研究所；同年任德国化学会（GDCh）主席
  - 1964 与 Bloch 共享诺贝尔奖（胆固醇/脂肪酸代谢）；诺奖委员会视角：甾醇与脂肪酸代谢有助理解胆固醇对心脏病与卒中的影响
  - 1964-12-11 诺贝尔演讲《从"活化乙酸"到萜类与脂肪酸之路》
  - 贡献：乙酸须经辅酶 A 活化方能起步；解出乙酰辅酶 A 化学结构；发现 biotin（维生素 B7）参与该过程
  - 1962 当选美国艺术与科学院、美国 NAS；1963 Otto Warburg 奖章；1965 联邦大十字佩星绶带；1966 美国哲学学会；1967 德国油脂研究学会 Norman 奖章；1971 Pour le Mérite；1972 奥地利科学与艺术勋章
  - ForMemRS（皇家学会外籍会员）；雷根斯堡/迈阿密/巴黎笛卡尔大学荣誉博士
  - 亚历山大·冯·洪堡基金会设 Feodor Lynen Research Fellowships 以其名命名
  - 1979-08-06 卒于慕尼黑（动脉瘤手术后六周）

---

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章执行 Beamer 立传，**第 0/1/2/3 步按 medic 路径执行**：
> - 页面与元数据：`medic/presentations/pages/20th_century/Feodor_Felix_Konrad_Lynen/`（page.md / metadata.json / images.txt）
> - 目录创建：`medic/presentations/20th_century/Feodor_Felix_Konrad_Lynen/` 与 `images/`
> - Makefile：复制 medic 侧同结构模板，设 `MAIN=Feodor_Felix_Konrad_Lynen_zh`
> - 肖像：正文含 1964 斯德哥尔摩全家福缩略 URL（250px 改 500px，curl 加 `-A "Mozilla/5.0"`，file 验证）；404 用 Commons `Special:FilePath` 回退；均失败用装饰圆占位
> 每完成一步汇报，溢出即修（make → pdftoppm 逐页目检）。

---

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biochemistry | 生物化学 | 诺奖核心：胆固醇与脂肪酸代谢的机制与调控 | 核心页 |
| 1 | coenzyme biochemistry | 辅酶生化 | 乙酰辅酶 A 化学结构的解出；biotin 参与 | 核心页 |
| 2 | lipid metabolism | 脂质代谢 | 活化乙酸→萜类/脂肪酸通路的起点 | 核心页 |
| 3 | toxicology | 毒理学 | 博士论文：鬼笔鹅膏的毒性物质 | 早年页 |

---

## 四、社会关系梳理 + 入库 【人物专属】

> 与 `MySQL/data/Feodor_Felix_Konrad_Lynen.yaml` 完全一致；只收 page.md 明载的关系。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Konrad Emil Bloch | 无向 | 1964 诺贝尔生理学或医学奖共享（胆固醇与脂肪酸代谢的机制与调控） |
| advisor-student | Heinrich Otto Wieland | 师→生 | 慕尼黑大学博士导师（1937 鹅膏毒素论文，库内规范全名 id=3534） |
| advisor-student | Dieter Oesterhelt | 生→ | 博士生（infobox 明载，库内 id=4032） |
| colleague | Otto Heinrich Warburg | 无向 | 与 Hahn 共同促成其为马克斯·普朗克细胞化学研究所所长（库内 id=4628） |
| colleague | Otto Hahn | 无向 | 同上（库内 id=2055） |
| spouse | Eva Wieland | — | 1937-05-14 结婚，博士导师之女（1915-2002） |
| parent-child | Wilhelm Lynen | — | 父，机械工程教师 |
| parent-child | Frieda Prym | — | 母，实业家之女 |

**不入库裁定**：五名子女（仅记数量与年份段）不入库；战后德国科学界同侪（除 Warburg/Hahn 促成所长一事）不入库；★岳父即博士导师 Wieland——师生边已建在 Wieland 记录上，Eva 行仅 spouse，勿重复建边。

## 五、配色方案 【人物专属】

- **气质**：德国学院派的沉稳手工，把一个"活化"步骤变成整条通路的钥匙
- **主色**：辅酶琥珀 `#5C3A21`（与人物气质呼应——CoA 分子的暖褐与慕尼黑研究所的木色年代感）
- **诺奖色**：香槟金 `#D4AF37`
- **四分类色（badgeA-D）**：
  - `badgeA` 生物化学——代谢琥珀 `#B4632A`
  - `badgeB` 辅酶生化——CoA 金绿 `#C89B3C`
  - `badgeC` 脂质代谢——脂滴灰蓝 `#3A6FA8`
  - `badgeD` 毒理学——鹅膏紫褐 `#6B4E9E`
- **背景母题**：CoA"手柄"扣合乙酸的小图式与岔路谱线（对应"活化乙酸"），badge 四色错落

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
01  封面 — 活化乙酸的解钥人 / Feodor Felix Konrad Lynen 1911–1979 + 四色 badge + 右上头像 + 国籍行（Germany）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、慕尼黑、LMU/Wieland 门下、马普细胞化学研究所所长、荣誉、核心领域）
03  核心贡献概览 — 乙酰辅酶 A 结构 / biotin 参与 / 活化乙酸→萜类与脂肪酸 / 鹅膏毒素博士论文
04  慕尼黑与 Wieland 门下（1911–1937）— 化学系、1937 毒素论文、同年娶导师之女 Eva
05  战时与战后讲席（1937–1953）— 留德全程、1942 讲师、1947 助理教授、1953 教授
06  马克斯·普朗克细胞化学研究所（1954–1972）— Warburg 与 Hahn 促成设职、1972 并入生化所、GDCh 主席
07  活化的乙酸（核心贡献页一）— 乙酸须挂辅酶 A 才能起步
08  乙酰辅酶 A 的结构（核心贡献页二）— 化学结构解出；biotin（维生素 B7）的参与
09  与 Bloch 的接力 — "mostly separately"：角鲨烯生成与转化的两半拼图
10  1964 诺贝尔奖 — 理由句、诺奖委员会的心脑卒中视角、演讲《从"活化乙酸"到萜类与脂肪酸之路》
11  荣誉与认可 — 1962 AAAS/NAS、1963 Otto Warburg 奖章、1965 大十字、1966 APS、1971 Pour le Mérite、1972 奥地利勋章
12  国际认可 — ForMemRS、三校荣誉博士、洪堡基金会 Lynen Fellowship
13  家庭 — Eva Wieland 与五子女（1938-1946）、1964 斯德哥尔摩全家福
14  结尾 — 1979-08-06 卒于慕尼黑（动脉瘤术后六周）；一把钥匙开一条通路
```

---

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方逐字为 "for their discoveries concerning the mechanism and regulation of the cholesterol and fatty acid metabolism"；citation json 内姓名为短名 "Feodor Lynen"，yaml/页面用 manifest 全名 |
| 分工表述 | 与 Bloch "working mostly separately"：Lynen 侧=辅酶 A 活化必需、acetyl-CoA 结构、biotin；Bloch 侧=全碳溯源与角鲨烯→胆固醇——接力勿混 |
| 库内记录 | 库内同名 stub id=3540，yaml UPD 回填 Q44597，勿新建 |
| 导师规范名 | 博士导师用库内全名 **'Heinrich Otto Wieland'**（id=3534，有 QID）；库内另有分裂 stub 'Heinrich Wieland'(id=3848)——勿引用，已上报主控 |
| 岳父=导师 | Eva Wieland 是博士导师之女（1937-05-14 结婚）——两人关系各自建边，勿在 Eva 行重复 |
| 战时表述 | "remained in Germany throughout World War II"——按正文一句客观，勿引申 |
| 年份锚点 | 1942 讲师、1947 助理教授、1953 教授、1954 所长、1972 并所+GDCh 主席；奖项 1962/1963/1964/1965/1966/1967/1971/1972——逐一核对 |
| 获奖理由双版本 | 荣誉列表里引语作 "...metabolism of cholesterol and fatty acids"（词序不同）——以 citation json 版本为准，列表版本不用于正文 |
| 死因口径 | 动脉瘤手术后六周去世（1979-08-06）——勿写成动脉瘤直接致死 |
| metadata 噪声 | metadata educated_at 有噪声 QID 项（Q2324614），以正文 LMU 为准；配偶/子女/父母以 page.md 为准 |

---

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| acetyl-coenzyme A | 乙酰辅酶 A | 其标志性成果 |
| biotin | 生物素（维生素 B7） | 参与该过程的发现 |
| activated acetic acid | "活化乙酸" | 诺奖演讲题目关键词，保留引号 |
| terpene | 萜类 | 通路终点之一 |
| fatty acid | 脂肪酸 | citation 用语 |
| Amanita | 鹅膏（毒蘑菇属） | 博士论文对象 |
| Max-Planck Institute for Cellular Chemistry | 马克斯·普朗克细胞化学研究所 | 1954 为其而设 |
| GDCh | 德国化学会 | 1972 任主席 |
| Pour le Mérite | 功勋勋章（Pour le Mérite） | 1971，保留原文 |

---

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**With Me**（manifest 预分配）
- **匹配理由**：与 Bloch 各自工作却共享同一座奖台，与妻子/岳父一门两代的化学姻缘——"与我同行"贴合这条"接力与陪伴"的叙事线；音乐宜温厚克制
- **本地路径**：`music_audio/` 下检索曲名（参照 `curated_tracks.md`），复制到 `medic/presentations/20th_century/Feodor_Felix_Konrad_Lynen/With Me.wav`
- **时长**：曲长须 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐

