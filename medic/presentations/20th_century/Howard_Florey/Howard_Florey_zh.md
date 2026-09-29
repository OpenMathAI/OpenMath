# 医学家立传提示词（Howard Florey）

> 本文件是 OpenMedic 项目（OpenMathAI 诺贝尔生理学或医学奖人物史）20 世纪 1945 年得主 Howard Florey 的人物专属立传提示词。
> 事实基准：`medic/presentations/pages/20th_century/Howard_Florey/page.md`（唯一事实来源，metadata.json 仅作参考）。
> 结构对齐标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（11 节合并为 9 节）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Howard Walter Florey, Baron Florey of Adelaide and Marston（1898-09-24 生于南澳大利亚阿德莱德 ~ 1968-02-21 逝于牛津，享年 69 岁）
- **气质关键词**：**把青霉素变成药的人、牛津 Dunn 学派的统帅、澳大利亚最伟大的科学家** —— 1945 年诺贝尔生理学或医学奖（与 Fleming、Chain 共享）获奖理由（逐字引用 `medic/nobel_medicine_citations.json`）：
  > "for the discovery of penicillin and its curative effect in various infectious diseases"（因其发现青霉素及其对多种传染病的疗效）
- **设计母题**：**从培养瓶到病床（from flask to bedside）**。横放的玻璃瓶、伞布过滤、冻干粉末、八只老鼠、一名警员——青霉素不是"看见"的，是被一支团队"制造"出来的。视觉语言：生产流水线式的培养瓶阵列与剂量递增的生死线。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Howard_Florey/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）
- **关键时间线（身份信息页与时间轴素材，均出自 page.md）**：
  - 1898-09-24 生于阿德莱德马拉文（父 Joseph 为英格兰牛津郡移民靴匠；姐 Hilda Gardner 为细菌学与实验室医学先驱）
  - St Peter's College 私校（四份奖学金）；1917 入阿德莱德大学学医（父 1918 心梗去世、鞋厂破产）
  - 1920 获罗德学者（南澳）；1921-12 乘 SS Otira 免费任随船医生赴英
  - 1922 入牛津 Magdalen College，师从 Charles Scott Sherrington（猫大脑皮层研究，1925《Brain》论文）
  - 1924-25 剑桥 John Lucas Walker 学者；1925-26 洛克菲勒基金会奖学金赴美（宾大 Richards、康奈尔 Chambers）
  - 1926 伦敦医院职位；1926-10-19 娶同学 Mary Ethel Hayter Reed
  - 1927 剑桥 Gonville and Caius 学院 fellow；1929 起研究溶菌酶
  - 1932 谢菲尔德大学 Joseph Hunter 病理学讲席教授
  - 1935 任牛津 Sir William Dunn 病理学派主任（Lincoln College fellow）
  - 1936 聘 Margaret Jennings；经 Hopkins 推荐聘 Ernst Chain，Chain 又荐来 Norman Heatley
  - 1939 与 Chain 立项"微生物抗菌物质"；1940-05-25 八鼠实验成功（1940-08-24《柳叶刀》）
  - 1941-02 首例病人警员 Albert Alexander（药量不足复发去世）；1941-06 与 Heatley 赴美争取量产
  - 1941-03 当选 FRS；1943 北非战地试验（与 Cairns）；1943-03-27 187 例临床试验《柳叶刀》
  - 1944-06-08 受封 Knight Bachelor；1944-08 访澳推动医学研究建言
  - 1945 与 Fleming、Chain 共享诺贝尔奖；1945 获 Cameron 奖与 Lister 奖
  - 1945 提出 ANU 医学研究建校方案（John Curtin School）；1948-1953 任代理所长
  - 1953 Newton/Abraham 结晶头孢菌素 C（Florey 拍板继续）
  - 1951 Royal Medal；1957 Copley Medal；1960-1965 任皇家学会会长（迁址 Carlton House Terrace）
  - 1962 任牛津 Queen's College 校长（provost）；1965 授 OM、封终身贵族 Baron Florey of Adelaide and Marston
  - 1965-1968 任 ANU 校长（chancellor）；1967-06-06 娶 Margaret Jennings
  - 1968-02-21 卒于牛津校长寓所（充血性心衰）

---

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章执行 Beamer 立传，**第 0/1/2/3 步按 medic 路径执行**：
> - 页面与元数据：`medic/presentations/pages/20th_century/Howard_Florey/`（page.md / metadata.json / images.txt）
> - 目录创建：`medic/presentations/20th_century/Howard_Florey/` 与 `images/`
> - Makefile：复制 medic 侧同结构模板，设 `MAIN=Howard_Florey_zh`
> - 肖像：正文含 1930s 肖像与 1944 办公室照缩略 URL（250px 改 500px，curl 加 `-A "Mozilla/5.0"`，file 验证）；404 用 Commons `Special:FilePath` 回退；均失败用装饰圆占位
> 每完成一步汇报，溢出即修（make → pdftoppm 逐页目检）。

---

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | bacteriology | 细菌学 | 诺奖核心：青霉素的生长、提纯、量产与临床（infobox Fields 之一） | 核心页 |
| 1 | immunology | 免疫学 | 溶菌酶与淋巴细胞的免疫研究（infobox Fields 之一） | 溶菌酶页 |
| 2 | chemotherapy | 化学治疗 | 头孢菌素 C 与半合成抗生素的开端 | 晚年页 |
| 3 | pathology | 病理学 | 本职讲席学科（Sheffield/Oxford 病理学教授） | 身份页 |

---

## 四、社会关系梳理 + 入库 【人物专属】

> 与 `MySQL/data/Howard_Florey.yaml` 完全一致；只收 page.md 明载的关系。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Alexander Fleming | 无向 | 1945 诺贝尔生理学或医学奖共享（青霉素的发现及其疗效） |
| co-honored | Ernst Chain | 无向 | 1945 诺贝尔生理学或医学奖共享（青霉素的发现及其疗效） |
| advisor-student | Charles Scott Sherrington | 师→生 | 牛津 Magdalen 生理学导师（1922 起，非博士；猫大脑皮层研究） |
| advisor-student | Peter Medawar | 生→ | 牛津 Dunn 学派博士生（1960 诺奖得主） |
| advisor-student | Gordon Sanders | 生→ | 牛津 Dunn 学派博士生 |
| advisor-student | Jean Taylor | 生→ | 牛津 Dunn 学派博士生 |
| collaborator | Norman Heatley | 无向 | 反向萃取与定量 assay 的技术核心（1941 随其赴美） |
| collaborator | Edward Abraham | 无向 | 溶菌酶结晶、青霉素酶、头孢菌素 C 研究主力 |
| colleague | Jim Kent | 无向 | 1926 年起招募的实验室助手，跟随四十年 |
| spouse | Mary Ethel Florey | — | 1926 结婚，1943 年 187 例临床试验负责人，1966 去世 |
| spouse | Margaret Jennings | 无向 | 1936 年聘入团队的同事、1940 起为伴侣，1967 结婚 |
| parent-child | Paquita Florey | — | 女（1929 生，纪念与 Cajal 之行的西班牙昵称） |
| parent-child | Charles du Vé Florey | — | 子（1934 生于谢菲尔德） |
| parent-child | Joseph Florey | — | 父，英格兰牛津郡移民靴匠 |
| parent-child | Bertha Mary Waldham | — | 母，1936-11-27 卒于癌症 |

**不入库裁定**：姐 Hilda Gardner 与侄 Joan Gardner 属 sibling/姻亲不入库；Alan Nigel Drury、Beatrice Pullinger、Paul Fildes、Marjory Stephenson（合作未发表）、Brian Maegraith 等团队同事仅一笔带过，不入库；Hugh Cairns（北非共事）不入库；Giuseppe Brotzu（头孢菌株来源）、Henry Harris（继任者）、Walter Burley Griffin 等不入库。

## 五、配色方案 【人物专属】

- **气质**：冷静的建设者、把"科研好奇"锻造成"救命药"的统帅
- **主色**：Dunn 学派深青 `#0B5351`（与人物气质呼应——牛津病理学大楼的长夜与量产车间的秩序）
- **诺奖色**：香槟金 `#D4AF37`
- **四分类色（badgeA-D）**：
  - `badgeA` 细菌学（青霉素）——量产琥珀 `#B4632A`
  - `badgeB` 免疫学（溶菌酶/淋巴细胞）——免疫青 `#2E7D6B`
  - `badgeC` 化学治疗（头孢菌素）——环式紫 `#6B4E9E`
  - `badgeD` 学派与建制——澳金 `#C89B3C`
- **背景母题**：横置培养瓶阵列与剂量刻度线（对应"从培养瓶到病床"），badge 四色错落

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
01  封面 — 把青霉素变成药的人 / Howard Florey 1898–1968 + 四色 badge + 右上头像 + 国籍行（Australia）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、阿德莱德、罗德学者、牛津 Dunn 学派主任、皇家学会会长、荣誉、核心领域）
03  核心贡献概览 — 青霉素量产与临床 / 溶菌酶与淋巴细胞 / 头孢菌素 C / ANU 与皇家学会建制
04  阿德莱德与罗德学者（1898–1922）— 靴匠之子、四份奖学金、1921 随船医生赴英
05  Sherrington 门下与游学（1922–1926）— 猫大脑皮层研究、剑桥/美国 Fellowship、娶 Ethel Reed
06  剑桥—谢菲尔德—牛津（1926–1935）— 溶菌酶起步、Sheffield 讲席、1935 执掌 Dunn 学派
07  组建跨学科团队（1935–1939）— Jennings/Chain/Heatley 到位、淋巴/黏液多线并进
08  八鼠实验与首例病人（核心贡献页一）— 1940-05-25 小鼠实验、1941-02 Albert Alexander（药量不足）
09  量产突围 — 1941 美国之行、Pearl Harbor 后的深潜发酵、D-Day 前的充足供应
10  临床与战场 — 187 例《柳叶刀》（1943）、北非战地试验、淋病 48 小时治愈
11  荣誉与认可（核心贡献页二）— 1945 诺奖（与 Fleming/Chain）、Knight Bachelor 1944、Cameron/Lister 1945
12  皇家学会与上议院 — 会长 1960-65（Carlton House Terrace）、1965 OM 与终身贵族
13  澳大利亚遗产 — John Curtin School、ANU 校长、Florey Building、澳 50 元钞票（1973-95）
14  结尾 — 8000 万条性命与 Menzies 之评：澳大利亚所生最重要的人
```

---

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方逐字为 "for the discovery of penicillin and its curative effect in various infectious diseases"——三人共享同一句 |
| 分工定位 | "Fleming 发现、Florey 团队成药"是 page.md 导语原话；但他自陈"青霉素项目最初由科学兴趣驱动，药用价值是 bonus"（Florey 引语可引）——两种口径并存须同时呈现 |
| 首例病人 | 1941-02 警员 Albert Alexander 开始好转后因药量不足复发去世——勿写成治愈；此后转向儿童病人 |
| 与 Chain 的裂痕 | 1941 赴美带 Heatley 未事先告知 Chain（Chain 引语 "underhand trick...bad faith"）——正文明载，须与"两人 1945 共享诺奖"平衡呈现，勿丑化任何一方 |
| 专利立场 | Chain 主张申请专利、Florey/Dale 认为研究者牟利不道德；美国深潜工艺专利化后英国反付专利费（促生 NRDC 1948）——客观呈现，勿品德评判 |
| 导师性质 | Sherrington 是牛津 Magdalen 的本科/研究生导师（非博士导师；其学位论文 1925 由 J. S. Haldane 与 Priestley 审查）——关系 note 已注明"非博士" |
| 年份锚点 | FRS 1941-03、Knight Bachelor 1944-06-08、Cameron/Lister 1945、Royal Medal 1951、Copley 1957、会长 1960-11-30 就任、1965 封终身贵族（2-04）与 OM（7-15）——逐一核对 |
| 溶菌酶结论 | Florey 1930 论文结论"溶菌酶在天然免疫中作用甚微"——与 Fleming 的重视形成对照，勿写反 |
| 家族 | 姐 Hilda Gardner 是细菌学先驱（sibling 不入库）；母 Bertha 1936-11-27 卒于癌症；两妻一伴侣（Ethel 1966 卒；Jennings 1940 起为伴侣、1967-06-06 结婚——按正文客观） |
| 死亡口径 | 正文 "died ... of congestive heart failure"（链接指向心梗）——写"充血性心衰"即可；葬礼在 Marston 教堂（因他公开的不可知论，纪念碑只能放墙外），Westminster Abbey 追思会约 500 人 |
| 数字口径 | "青霉素发展估计挽救逾 8000 万条命"——勿夸大到其他数字；Menzies 引语 "In terms of world well-being, Florey was the most important man ever born in Australia." 可引 |
| metadata 噪声 | metadata occupations 含 politician（因 ANU chancellor 等职务）；主职业按 pathologist；配偶/子女/父母以 page.md 为准 |

---

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| Sir William Dunn School | （牛津）邓恩病理学院 | 团队大本营 |
| deep submergence | 深层（沉没）发酵 | 美国量产关键工艺 |
| reverse extraction | 反向萃取 | Heatley 方法 |
| Oxford unit | 牛津单位 | 早期效价单位 |
| penicillinase | 青霉素酶 | Abraham/Chain 发现 |
| cephalosporin C | 头孢菌素 C | 1953 结晶；源自 Brotzu 撒丁岛菌株 |
| lysozyme | 溶菌酶 | Florey 1930 结论"作用甚微" |
| Rhodes Scholarship | 罗德奖学金 | 1920 获得 |
| John Curtin School | 约翰·卡廷医学研究院 | ANU 首个研究院 |
| Order of Merit | 功绩勋章 | 1965 |
| life peer | 终身贵族 | Baron Florey of Adelaide and Marston |

---

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Through the Darkness**（manifest 预分配）
- **匹配理由**：战争阴云下的量产突围——空袭中的牛津、北非的战地病房、首例病人的死亡与八只小鼠的奇迹；"穿越黑暗"正贴合 1939-1945 这条从冷遇到 D-Day 的叙事线
- **本地路径**：`music_audio/` 下检索曲名（参照 `curated_tracks.md`），复制到 `medic/presentations/20th_century/Howard_Florey/Through the Darkness.wav`
- **时长**：曲长须 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐

