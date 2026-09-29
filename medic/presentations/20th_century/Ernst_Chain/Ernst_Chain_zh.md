# 医学家立传提示词（Ernst Chain）

> 本文件是 OpenMedic 项目（OpenMathAI 诺贝尔生理学或医学奖人物史）20 世纪 1945 年得主 Ernst Chain 的人物专属立传提示词。
> 事实基准：`medic/presentations/pages/20th_century/Ernst_Chain/page.md`（唯一事实来源，metadata.json 仅作参考）。
> 结构对齐标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（11 节合并为 9 节）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Sir Ernst Boris Chain（1906-06-19 生于德国柏林 ~ 1979-08-12 逝于爱尔兰梅奥郡卡斯尔巴，享年 73 岁）
- **气质关键词**：**青霉素的提纯者与化学解密者、β-内酰胺结构的理论先知、流亡 biochemist** —— 1945 年诺贝尔生理学或医学奖（与 Fleming、Florey 共享）获奖理由（逐字引用 `medic/nobel_medicine_citations.json`）：
  > "for the discovery of penicillin and its curative effect in various infectious diseases"（因其发现青霉素及其对多种传染病的疗效）
- **设计母题**：**从霉菌到分子（from mould to molecule）**。Fleming 看见抑菌圈，Chain 证明它不是酶而是一种可提纯、可测定的化学物质，并率先设想出 β-内酰胺环。视觉语言：培养皿→棕色冻干粉末→四元环结构式的三级递进。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Ernst_Chain/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）
- **关键时间线（身份信息页与时间轴素材，均出自 page.md）**：
  - 1906-06-19 生于柏林（父 Michael 为来自莫吉廖夫的俄裔犹太化学家与实业家；母 Margarete 出身柏林）
  - 1930 获弗里德里希·威廉大学（洪堡）化学学位
  - 1933-04-02 纳粹上台后携 10 英镑抵英；J. B. S. Haldane 助其获伦敦大学医院职位
  - 剑桥 Fitzwilliam College 攻读博士，师从 Frederick Gowland Hopkins 研究磷脂
  - 1935 任牛津大学病理学讲师（Florey 团队起点）
  - 1939 与 Florey 立项研究微生物天然抗菌物质，重启 Fleming 九年前的青霉素工作
  - 与 Florey、Heatley 一起实现青霉素分离、浓缩与治疗验证
  - 1939-04 入英籍
  - 1942 与 Edward Abraham 理论化青霉素 β-内酰胺结构（1945 由 Dorothy Hodgkin X 射线晶体学证实）
  - 二战将结束时得知母亲与妹妹死于纳粹
  - 1945 与 Fleming、Florey 共享诺贝尔奖
  - 1948-03-17 当选 FRS；1948 娶生物化学家 Anne Beloff
  - 战后赴罗马 Istituto Superiore di Sanità 工作；1964 回英创建帝国理工生化系（发酵技术），至退休
  - 1951 两次被美国拒签（McCarran 国内安全法）
  - 1954 获 Paul Ehrlich and Ludwig Darmstaedter 奖；1954 起任 Weizmann 科学研究所董事会成员
  - 1969 生日荣誉授 Knight Bachelor
  - 1979-08-12 卒于卡斯尔巴 Mayo 总医院

---

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章执行 Beamer 立传，**第 0/1/2/3 步按 medic 路径执行**：
> - 页面与元数据：`medic/presentations/pages/20th_century/Ernst_Chain/`（page.md / metadata.json / images.txt）
> - 目录创建：`medic/presentations/20th_century/Ernst_Chain/` 与 `images/`
> - Makefile：复制 medic 侧同结构模板，设 `MAIN=Ernst_Chain_zh`
> - 肖像：正文含 1944/1945 实验室照缩略 URL（250px 改 500px，curl 加 `-A "Mozilla/5.0"`，file 验证）；404 用 Commons `Special:FilePath` 回退；均失败用装饰圆占位
> 每完成一步汇报，溢出即修（make → pdftoppm 逐页目检）。

---

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | biochemistry | 生物化学 | 诺奖核心：青霉素的分离、浓缩与化学组成 | 核心页 |
| 1 | enzymology | 酶学 | 溶菌酶、蛇毒、青霉素酶等酶类研究 | 牛津页 |
| 2 | fermentation technology | 发酵技术 | 帝国理工时期的专长；战后抗生素工业化 | 晚年页 |

---

## 四、社会关系梳理 + 入库 【人物专属】

> 与 `MySQL/data/Ernst_Chain.yaml` 完全一致；只收 page.md 明载的关系。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Alexander Fleming | 无向 | 1945 诺贝尔生理学或医学奖共享（青霉素的发现及其疗效） |
| co-honored | Howard Florey | 无向 | 1945 诺贝尔生理学或医学奖共享（青霉素的发现及其疗效） |
| advisor-student | Frederick Gowland Hopkins | 师→生 | 剑桥 Fitzwilliam 博士导师（磷脂研究，库内 id=3459）；后经其推荐入牛津 Dunn 学派 |
| colleague | J. B. S. Haldane | 无向 | 抵英之初助其获伦敦大学医院职位（库内规范名 id=485） |
| colleague | Albert Neuberger | 无向 | 1930 年代柏林结识的终生挚友（库内 id=1123） |
| collaborator | Edward Abraham | 无向 | 1942 共同理论化青霉素 β-内酰胺结构（库内 id=3614） |
| collaborator | Norman Heatley | 无向 | 其点名邀入牛津团队的关键技术合作者 |
| spouse | Anne Beloff | — | 1948 结婚，本人亦是知名生物化学家 |
| parent-child | Michael Chain | — | 父，化学家与实业家，俄裔犹太移民（莫吉廖夫） |
| parent-child | Margarete Eisner | — | 母，柏林人；与 Chain 之妹同死于纳粹（二战末得知） |

**不入库裁定**：Dorothy Hodgkin（1945 X 射线证实 β-内酰胺，学术事件非个人关系）不入库；三位子女（仅记数字）不入库；Anne Beloff 的兄弟姐妹（Renee/Max/John/Nora Beloff）仅系姻亲背景不入库。

---

## 五、配色方案 【人物专属】

- **气质**：锋利、执拗、从流亡行李箱里长出的化学
- **主色**：流亡深褐 `#5D4037`（与人物气质呼应——实验室棕色粉末、离散与重建）
- **诺奖色**：香槟金 `#D4AF37`
- **四分类色（badgeA-D）**：
  - `badgeA` 生物化学（青霉素）——内酰胺青 `#2E7D6B`
  - `badgeB` 酶学——酶金 `#C89B3C`
  - `badgeC` 发酵技术——发酵罐琥珀 `#B4632A`
  - `badgeD` 流亡与身份——深邃蓝 `#1E4E79`
- **背景母题**：四元环结构式与培养瓶剪影（对应"从霉菌到分子"），badge 四色错落

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input medic 封面模板）
01  封面 — 把霉菌变成分子的人 / Ernst Boris Chain 1906–1979 + 四色 badge + 右上头像 + 国籍行（United Kingdom）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、柏林、洪堡/剑桥、牛津 Dunn 学派、帝国理工、荣誉、核心领域）
03  核心贡献概览 — 青霉素提纯与治疗验证 / β-内酰胺结构 / 溶菌酶与酶学 / 发酵技术
04  柏林与流亡（1906–1933）— 化学家实业家之子、洪堡化学学位、1933-04-02 携 10 英镑抵英
05  剑桥师从 Hopkins（1933–1935）— Haldane 助职于伦敦大学医院、Fitzwilliam 博士（磷脂）
06  牛津 Dunn 学派（1935–1939）— Florey 点将、蛇毒/肿瘤代谢/溶菌酶多线研究
07  重启青霉素（1939–1940，核心贡献页）— 与 Florey 立项、Heatley 反向萃取、冻干成粉
08  化学解密 — 1942 与 Abraham 理论化 β-内酰胺结构、1945 Hodgkin X 射线证实
09  1945 诺贝尔奖 — 三人共享同一句理由；Heatley 的贡献与其 1990 荣誉 MD
10  家国之殇 — 二战末得知母亲与妹妹死于纳粹；入英籍（1939-04）与身份认同
11  罗马与帝国理工（1948–1973）— Istituto Superiore di Sanità、1964 创建帝国理工生化系（发酵技术）
12  荣誉与认可 — FRS 1948、Paul Ehrlich 奖 1954、Knight Bachelor 1969、荣誉博士
13  身份与信念 — Weizmann 研究所董事会（1954 起）、1965 "Why I am a Jew" 演讲（客观一句）
14  结尾 — 链条上的第二环：没有 Chain，便没有 Florey
```

---

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方逐字为 "for the discovery of penicillin and its curative effect in various infectious diseases"——三人共享同一句 |
| 分工定位 | Fleming 发现 → Chain/Florey 提纯验证 → Heatley 关键技术；Chain 团队"证明治疗作用并测定化学组成"——勿把提纯全归 Florey |
| 专利分歧 | Chain 主张申请专利（防他人垄断，非为牟利），Florey/Dale 反对；美国深潜培养工艺专利化——叙事页按正文客观呈现，勿写成品德评判 |
| 与 Florey 的裂痕 | 1941 Florey 携 Heatley 赴美未事先告知 Chain（"underhand trick" 引语）——正文明载，可写但须平衡（两人仍共获诺奖） |
| 博士导师 | 博士在**剑桥**（Fitzwilliam College）师从 **Frederick Gowland Hopkins**（磷脂），不是在牛津；Hopkins 是库内 id=3459 规范记录 |
| 国籍口径 | 出生德国；1939-04 入英籍（citizenship German until 1939, British from 1939）——总表/诺奖口径为 United Kingdom，yaml 只写英国，出生地与改籍在页面呈现 |
| 家族悲剧 | 母亲与妹妹死于纳粹（二战末得知）——正文明载，客观一句，不渲染 |
| McCarran 拒签 | 1951 两次被美国拒签（1950 年国内安全法）——正文明载可写一句 |
| 犹太身份 | 热诚的犹太复国主义者、Weizmann 研究所董事会、"Why I am a Jew"（1965）——按正文客观处理，不引申政治立场 |
| Heatley 定位 | Chain 邀请 Heatley 加入（"he had one in mind"）；Heatley 后直接向 Florey 汇报并差点赴哥本哈根——三人关系细节以 page.md 为准，勿写成 Chain 的学生 |
| 名言归属 | "Good God! I thought he was dead." 是 Chain 听说 Fleming 要来访时所说（Fleming 页载）——引语页须注明说话人 |
| metadata 噪声 | metadata 无父母/配偶载；父母、妻子 Anne Beloff、三子女以 page.md 为准；生卒 1906-06-19 / 1979-08-12 一致 |

---

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| beta-lactam | β-内酰胺 | 1942 理论化、1945 证实 |
| penicillinase | 青霉素酶 | Abraham/Chain 发现的分解酶 |
| phospholipid | 磷脂 | 博士课题 |
| lysozyme | 溶菌酶 | 牛津时期研究对象之一 |
| snake venom | 蛇毒 | 早期研究线 |
| freeze drying | 冷冻干燥 | Chain 提出的干燥保存法 |
| reverse extraction | 反向萃取 | Heatley 的回收方法 |
| fermentation technology | 发酵技术 | 帝国理工时期专长 |
| Istituto Superiore di Sanità | （意大利）高级卫生研究所 | 战后工作单位 |
| McCarran Act | 麦卡伦国内安全法 | 1951 拒签依据 |

---

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Falling Apart**（manifest 预分配）
- **匹配理由**：流亡、家国之殇、与 Florey 的信任裂痕——"崩解"意象贯穿 Chain 的 1930-40 年代；但崩解之后是重建（罗马→帝国理工），音乐的情绪弧线须由破碎走向坚定
- **本地路径**：`music_audio/` 下检索曲名（参照 `curated_tracks.md`），复制到 `medic/presentations/20th_century/Ernst_Chain/Falling Apart.wav`
- **时长**：曲长须 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐

