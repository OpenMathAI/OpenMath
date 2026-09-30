# 经济学家立传提示词（Bertil Ohlin）

> 本文件是 OpenEcon 项目 20 世纪诺贝尔经济学奖 **1977 年得主 Bertil Ohlin（贝蒂尔·奥林）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `economics/presentations/pages/20th_century/Bertil_Ohlin/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标经济学家**：Bertil Gotthard Ohlin（1899-04-23 生于瑞典 Klippan ~ 1979-08-03 逝于瑞典 Åre，享年 80 岁）
- **气质关键词**：**要素禀赋的测绘者、自由贸易的旗手、书斋与议会之间的双重人生**
- **诺奖获奖理由**（1977，与 James Meade 共享，逐字引用 manifest）：
  > "for their pathbreaking contribution to the theory of international trade and international capital movements"（表彰他们对国际贸易与国际资本流动理论的开创性贡献）
- **设计母题**：**要素禀赋的交换（factor endowments）**——资本丰裕国与劳动丰裕国各自出口密集使用其丰裕要素的产品：双向对称的交换箭头与色块构成背景母题，呼应 Heckscher–Ohlin 定理的镜像结构。
- **本地 Wikipedia 路径**：`economics/presentations/pages/20th_century/Bertil_Ohlin/page.md`（同目录 `metadata.json` 仅作结构化参考）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `economics/presentations/cover/`（OpenEcon 统一封面）

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章的完整流程；**第 0/1/2/3 步按 economics 路径执行**：页面已在 `economics/presentations/pages/20th_century/Bertil_Ohlin/`（含 page.md / page.html / metadata.json / images.txt，肖像从 images.txt 或 Commons `Special:FilePath` 取，404 则装饰圆占位）；Makefile 复制后设 `MAIN=Bertil_Ohlin_zh`、`VIDEO_NAME=Bertil_Ohlin_zh`。第 4 步（研究领域）与第 4.5 步（社会关系）已由本批次完成入库，无需重复执行；第 5 步起按本文第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Ohlin 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | international trade | 国际贸易 | Heckscher–Ohlin 模型与定理，诺奖核心 | 封面、核心页 |
| 1 | international finance | 国际金融 | 国际资本流动理论，诺奖理由另一半 | 核心页 |
| 2 | macroeconomics | 宏观经济学 | 1930s 大萧条与扩张政策研究（ League 报告） | 政策页 |
| 3 | economic history | 经济史 | 1929 德国赔款论战与单边国际支付理论 | 早年页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Gustav Cassel | Ohlin → 学生 | 斯德哥尔摩大学博士导师（1924，25 岁获博士学位） |
| influence | Eli Heckscher | 无向 | 其师；1930 继其出任斯德哥尔摩经济学院经济学教授 |
| collaborator | Eli Heckscher | 无向 | 共同发展 Heckscher–Ohlin 贸易模型与定理 |
| co-honored | James Meade | 无向 | 1977 诺贝尔经济学奖共享（国际贸易与国际资本流动理论） |
| controversy | John Maynard Keynes | 无向 | 1929 年关于德国战争赔款负担的著名论战（凯恩斯预言债务引发战争，奥林认为德国承受得起） |
| colleague | Oskar Morgenstern | 无向 | 国际联盟经济财政组织外聘专家共事（1930s 大萧条研究） |
| colleague | Jacques Rueff | 无向 | 国际联盟经济财政组织外聘专家共事 |
| parent-child | Anne Wibble | Ohlin → 子 | 女儿，同党籍，1991–1994 任瑞典财政大臣 |

**不入库但提示词可叙述**：父亲 Elis（公务员兼执法官）与母亲 Ingeborg（左翼自由派思想启蒙，仅名无姓不入库）；七个兄弟姐妹（仅具数量）；Leontief（其实证研究构成 Leontief paradox 挑战 H-O 定理——学术事件非人际，禁建边）；Karl Staaff（母亲的思想偶像）；Per Albin Hansson（战时联合政府首相，任职关系非学术关系）；Gunnar Myrdal（1944–45 继其出任商业与工业大臣——任职先后非社会关系，且 Myrdal 已有库内记录，勿混建）。

## 五、配色方案 【人物专属】

- **气质**：开阔、对称、北欧的清朗
- **主色**：`#46356B`（深紫罗兰——北欧贸易理论的沉静深邃）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badgeTrade` 国际贸易 — 深紫 `#46356B`
  - `badgeCap` 资本流动 — 靛蓝 `#283593`
  - `badgePol` 议会生涯 — 玫瑰 `#C4204F`
  - `badgeNord` 北欧合作 — 青绿 `#0E7C7B`
- **背景母题**：双向对称交换箭头与色块（资本丰裕与劳动丰裕两国的镜像贸易）。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenEcon 项目首页（\input cover/openecon_page.tex）
01  封面 — 要素禀赋的测绘者 / Bertil Ohlin 1899–1979 + 四色 badge + 右上头像 + 国籍行（Sweden）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、出生地 Klippan、教育 Lund BA/斯德哥尔摩经济学院 MSc/
    Harvard MA/Stockholm University PhD 1924、任职哥本哈根 1925–30→斯德哥尔摩经济学院 1930–65、诺奖 1977、核心领域）
03  核心贡献概览 — Heckscher–Ohlin 模型 / H-O 定理 / 国际资本流动 / 德国赔款论战
04  斯堪尼亚少年 (1899–1917) — Klippan 长大、七手足、父亲 Elis、母亲 Ingeborg 的自由派启蒙
05  神速的学业 (1917–1924) — 18 岁 Lund BA、1919 MSc、1923 Harvard MA、1924 斯德哥尔摩大学博士（25 岁）
06  哥本哈根教授 (1925–1930) — 26 岁出任哥本哈根大学教授
07  1929 论战凯恩斯 — 德国赔款问题的著名交锋、单边国际支付现代理论的重要一环
08  Heckscher–Ohlin 模型（核心贡献页）—《区际与国际贸易》1933、比较优势与要素禀赋
09  H-O 定理（核心贡献页）— 资本丰裕国出口资本密集品、劳动丰裕国出口劳动密集品；五前提条件
10  Leontief paradox — 列昂惕夫之谜对定理的实证挑战与理论生命力
11  国际联盟岁月 (1937) — Berkeley 访问教授、EFO 外聘专家（与 Morgenstern/Rueff 共事）
12  议会与政党三十年 (1938–1970) — 人民党领袖 1944–67、战时商业与工业大臣 1944–45、北欧理事会主席 1959/1964
13  1977 诺贝尔经济学奖 — 与 James Meade 共享；1977-12-08 诺奖演讲 1933 and 1977
14  遗产与结尾 — 标准贸易模型的常青骨架 + 女儿 Anne Wibble 的新一代 + 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 全名与瑞典语读音 | Bertil **Gotthard** Ohlin（瑞典语读音 [ˈbæ̌ʈːɪl ʊˈliːn]，注意页注 IPA，非英语式读法） |
| 生卒 | 1899-04-23 Klippan 生 ~ 1979-08-03 Åre 逝（享年 80）；勿把 Åre 误作出生地 |
| 学位时间线 | 1917 Lund BA（18 岁）→ 1919 斯德哥尔摩经济学院 MSc → 1923 Harvard MA → **1924 Stockholm University PhD**；「博士导师 Cassel」挂斯德哥尔摩大学，勿错挂 Harvard；Harvard MA 年代勿与博士混淆 |
| Heckscher 双边 | Heckscher 既是「his teacher」（influence）又与之共同发展模型（collaborator）——两条边并存合法，note 各自聚焦，勿合并成一条丢失信息 |
| 模型命名 | Heckscher–Ohlin model 与 theorem 均以两人命名；模型「developed together with Eli Heckscher」，定理由 Ohlin 本人从模型导出——两处表述有差，勿写「Ohlin 独立发明模型」 |
| 1977 共享理由 | 与 Meade 共享，官方理由复数 "for **their** pathbreaking contribution..."；两人工作分属贸易理论与国际收支/政策，互不隶属，勿写合作 |
| Keynes 论战 | 1929 年凯恩斯预言赔款负担将引发战争、奥林认为德国承受得起——论战「在现代单边国际支付理论中地位重要」；controversy 边成立，但禁写胜负裁决（page.md 未载） |
| 政治生涯边界 | 人民党（Liberal People's Party，社会自由主义）领袖 1944–1967、议员 1938–1970、战时联合政府商业与工业大臣 1944–1945、北欧理事会主席 1959 与 1964 两届——年份勿混；政治内容客观简述 |
| 继任关系两则 | 1930 继 Heckscher 出任斯德哥尔摩经济学院教授（师承脉络）；1945 其商业与工业大臣职由 **Gunnar Myrdal** 接任（任职先后，非社会关系，禁建边） |
| 女儿 | Anne Wibble（1991–1994 财政大臣，同属人民党）入库 parent-child；父母仅名（Elis/Ingeborg）不入库 |
| 荣誉 |北极星勋章司令大十字（Commander Grand Cross of the Order of the Polar Star，1965-06-04）；格勒诺布尔大学与巴黎大学荣誉博士——勿与诺奖混淆 |
| 无直接引语 | page.md 无 Ohlin 原话引语，全篇禁写「原话」；引用仅限获奖理由与论著名 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| Heckscher–Ohlin model | 赫克歇尔–奥林模型 | 标准贸易模型，两人命名勿漏 Heckscher |
| Heckscher–Ohlin theorem | 赫克歇尔–奥林定理 | 资本/劳动丰裕与出口结构的预言 |
| factor endowments | 要素禀赋 | 设计母题核心词 |
| capital-abundant / labor-abundant | 资本丰裕/劳动丰裕 | 定理的前提分类 |
| Leontief paradox | 列昂惕夫之谜 | 实证挑战，非定理证伪 |
| international capital movements | 国际资本流动 | 诺奖理由另一半 |
| unilateral international payments | 单边国际支付 | 1929 论战的理论意义 |
| Interregional and International Trade | 《区际与国际贸易》 | 1933 代表作 |
| People's Party | 人民党 | 瑞典社会自由主义政党，勿译「人民党」产生误读 |
| Nordic Council | 北欧理事会 | 1959/1964 两任主席 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Daylight**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：奥林的理论把国际贸易还原为要素禀赋的天然对称——白天与黑夜、资本与劳动互为镜像；「Daylight」的明快开阔贴合北欧自由贸易旗手的气质，也呼应其从书斋到议会的双重人生里始终清醒的现实感。
- **本地路径**：复制 `music_audio/alex-productions/44-JoyIRE5k2Yo-Daylight.wav` 到 `economics/presentations/20th_century/Bertil_Ohlin/Daylight.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
