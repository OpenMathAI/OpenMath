# Yann LeCun（杨立昆）立传提示词

> qid=Q3571662 · 1960-07-08 生（在世，死亡日期留白） · 法裔美国计算机科学家 · 20/21 世纪 · 2018 图灵奖（与 Hinton、Bengio 共享）
> 本地 Wikipedia 数据源：`turing/pages/2018/Yann LeCun/`（index.html + metadata.json + images）

---

## 0. 正文形式说明（参考数学家高斯 + 图灵奖硬性要求）

> 本提示词正文（Beamer tex）**采用高斯模板的「表格语义化 + 公式框 + 时间线」版式**（而非 Knuth 卡片式），配色沿用 OpenTuring 图灵紫品牌色。图灵奖得主立传格式硬性要求：

1. **封面有头像**：右上角肖像 + `draw=coveraccent!50` 细边框 + 姓名小字注。
2. **封面有国籍**：顶部副标题明示国籍（`\faIcon{globe}\enspace 法国/美国`），底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（★ 必做）：封面之后、核心贡献之前。左侧头像 + 右侧 `2×2` 信息网格，含至少：生卒、本名、国籍、出生地、教育、师承、任职、主要荣誉、核心领域。事实取自 `index.html` infobox，不得杜撰。
4. **高斯版式**：生平关键事件、核心贡献页采用 `tabularx` 语义化表格 + `\fcolorbox` 公式框（卷积网络 / 着手写数字识别的形式化表达），时间线页用竖线 + 节点。
5. **品牌口径统一**：结尾页底部品牌统一写 `OpenMathAI`；引号用半角 `" "`。

---

## 1. 背景信息（用于 Slide 1-3）

- **全名**：Yann André Le Cun（中文惯称：杨立昆；发音 /lə-ˈkʌn/，法语 [ləkœ̃]；通常拼写 LeCun）
- **生卒**：1960-07-08 生于 Soisy-sous-Montmorency（巴黎郊区，法国）；在世，死亡日期**留白**
- **国籍**：法国 / 美国（French-American，现持有美国国籍）
- **身份**：计算机科学家（AI、机器学习、计算机视觉、机器人学、图像压缩）；NYU Courant 研究所 Jacob T. Schwartz 计算机科学讲席教授；前 Meta 首席 AI 科学家；AMI Labs 执行主席
- **姓氏渊源**：Le Cun 源自布列塔尼古体 Le Cunff，来自北部布列塔尼 Guingamp 地区；Yann 是 Jean 的布列塔尼形式——可作姓氏页小料
- **家庭**：三个儿子；兄弟任职于 Google（页面仅此一句，勿扩展）
- **教育轨迹**：ESIEE Paris 工程师文凭（Diplôme d'Ingénieur，1983）→ Université Pierre et Marie Curie（今索邦大学）计算机科学 PhD（1987），论文 *Modeles connexionnistes de l'apprentissage*（连接主义学习模型）
- **博士导师**：Maurice Milgram
- **博士后**：1987 年起在 University of Toronto 受 Geoffrey Hinton 指导一年
- **研究领域**：人工智能、机器学习、计算机视觉、机器人学、图像压缩

## 2. 核心叙事亮点（用于 Slide 4-13）

1. **2018 图灵奖（共享）**：与 Hinton、Bengio 因深度学习工作共享；三人并称 "Godfathers of AI / Deep Learning"（页面注明 Jürgen Schmidhuber **偶尔**也被列入该称呼——表述保留"有时/偶尔"）。本篇为**CNN/工业落地主叙事篇**。
2. **CNN 的开拓者（侧重页）**：1987 博士论文中提出**早期形式的反向传播**；1985 年已发表非对称阈值网络学习方案（Cognitiva 85）。
3. **Bell Labs 岁月（1988–1996）**：加入 AT&T Bell Labs 自适应系统研究部（Holmdel, NJ，主任 Lawrence D. Jackel），发展出卷积神经网络模型 **LeNet**、"Optimal Brain Damage" 正则化方法、Graph Transformer Networks；应用于手写识别与 OCR。
4. **支票识别系统落地**：协助开发的银行支票识别系统被 NCR 等公司广泛部署——神经网络**第一次大规模商用**之一（侧重页：1989 *Backpropagation Applied to Handwritten Zip Code Recognition*，与 Boser、Denker 等）。
5. **LeNet 论文（1998）**："Gradient-based learning applied to document recognition"（Proceedings of the IEEE，与 Bottou、Bengio、Haffner）——CNN 经典文献。
6. **DjVu 图像压缩**：1996 年起任 AT&T Labs-Research 图像处理研究部主任；与 Léon Bottou、Patrick Haffner 同为主要创建者，被 Internet Archive 用于数字化文本分发；与 Bottou 共同开发 Lush 语言。
7. **NYU（2003–）**：Jacob T. Schwartz 讲席教授（Courant + 神经科学中心）；能量基模型（energy-based models）；2012 年创办 NYU Center for Data Science 并任创始主任（2014 年初卸任）。
8. **Meta/FAIR（2013–2025）**：2013-12-09 成为 Meta AI Research（FAIR）**首任主任**、任首席 AI 科学家十年；与 Bengio 共同创办 ICLR（2013）；1986–2012 年主持雪鸟 "Learning Workshop"；2016 年法兰西公学院年度讲席访问教授。
9. **AMI Labs 创业（2025）**：2025-11-19 宣布离开 Meta，创办 Advanced Machine Intelligence Labs（AMI Labs）专注**世界模型**（world models）与"类人智能"；CEO Alex LeBrun，LeCun 任执行主席；2026-03 完成 10.3 亿美元融资（35 亿美元投前估值）；2026-01 出任 Logical Intelligence 技术研究委员会创始主席（能量基推理）。
10. **技术判断力**：2025 年对《金融时报》直言 LLM 路线的局限："I'm sure there's a lot of people at Meta who would like me to NOT tell the world that LLMs basically are a dead end when it comes to superintelligence."
11. **荣誉**：美国国家科学院/工程院 + 法国科学院三院院士；Turing 2018、Princess of Asturias 2022、法国荣誉军团骑士 2023、VinFuture 2024、QE Prize 2025。

## 3. 配色方案（图灵紫品牌色 + 四分类色）

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（图灵紫） | `#5B2D8E` | OpenTuring 品牌主色 |
| 强调色（红） | `#B03A2E` | 尊崇 / 图灵奖 |
| 分类色 1（卷积网络 — 蓝） | `#2E5A9E` | CNN / LeNet 开拓 |
| 分类色 2（识别落地 — 青绿） | `#1E8E8E` | 手写数字 / 支票识别 / OCR |
| 分类色 3（压缩与工程 — 琥珀） | `#D9A441` | DjVu / Lush / 工业系统 |
| 分类色 4（世界模型 — 玫瑰） | `#C0395B` | FAIR → AMI Labs / 对 LLM 路线的反思 |
| 背景 | `#F7F5FB` | 浅紫灰白 |

- **背景母题**：卷积感受野网格（稀疏方格与滑窗叠加），呼应「卷积扫描图像」的视觉语言。

### 3.5 背景音乐选择 ✅ 【人物专属】

- **气质定位**：沉郁 / 转折（从早期的边缘坚持到中年的路线论辩）
- **选定曲目**：Alex-Productions **Tragedy**（manifest 预分配，沿用勿改）
- **落地文件**：`turing/presentations/Yann_LeCun/Tragedy.wav`（复制自音乐库，不入 git）。

## 4. Slide 规划（约 15 页，高斯版式结构）

1. **封面**（`\titleslide`）：顶部标签「AI 教父 · 法国/美国」+ LeCun 1960– + 右上头像 + 国籍行 + 底部三要素状态栏 + 四色 badge
2. **身份信息页**（`\profileslide`，★ 必做）：左头像 + 右 2×2 信息网格（生卒 / 本名 / 国籍 / 出生地 / 教育 / 师承 / 任职 / 主要荣誉 / 核心领域）
3. **时间线**（`\timelineslide`）：1960– 在世生平纵览
4. **布列塔尼的姓氏与巴黎郊区童年**（1960–）：Le Cunff 渊源、Yann=Jean 的布列塔尼形式
5. **ESIEE 与索邦博士**（1983/1987）：连接主义学习模型、早期反向传播、Milgram 门下
6. **多伦多博后**（1987–1988）：Hinton 门下一年
7. **Bell Labs：LeNet 的诞生**（1988–1996）（侧重页）：Jackel 部门、CNN、Optimal Brain Damage
8. **手写数字与支票识别**（1989–）（侧重页）：Zip Code 论文、NCR 部署、神经网络首次大规模商用
9. **LeNet 经典论文**（1998）：与 Bottou/Bengio/Haffner 合著
10. **DjVu 与 Lush**：图像压缩、Internet Archive、工程多面手
11. **NYU 与数据科学**（2003–）：能量基模型、CDS 创始主任、ICLR 共同创办
12. **Meta/FAIR 十年**（2013–2025）：首任 FAIR 主任、法兰西公学院讲席
13. **AMI Labs：世界模型**（2025–）：离开 Meta、10.3 亿美元融资、LLM "dead end" 之辩
14. **荣誉与共享的荣耀**：Turing 2018（与 Hinton/Bengio）、三院院士、Asturias 2022
15. **结尾**：在世、"Godfathers of AI" 的历史地位与开放的未来

## 5. 史实陷阱与敏感点（终审必须检查）

- **图灵奖理由口径**：LeCun 页表述为深度学习工作共享获奖；三杰统一口径采用 ACM 全句 "conceptual and engineering breakthroughs that have made deep neural networks a critical component of computing"（Hinton 页实载），勿自造表述。
- **共享结构**：2018 三人共享；本篇侧重 **CNN/LeNet/手写数字识别/工业落地**；AlexNet 2012 复兴叙事归 Hinton 篇主写、本篇不展开；禁写三人恩怨（页面无载）。
- **反向传播归属**：LeCun 博士论文提出的是"**早期形式**的反向传播"（页面原话 an early form of backpropagation）；1985 年论文是非对称阈值网络学习方案——**勿写"LeCun 发明反向传播"**，也勿与 Hinton 1986 篇混淆主次。
- **LeNet 时间线**：Bell Labs 1988 年加入后发展 CNN（LeNet）；1989 Zip Code 论文；1998 综述论文——勿把 LeNet 写成 1988 年之前。
- **"Godfathers" 表述**：三人为核心；Schmidhuber 仅"偶尔"被列入（页面原话 occasionally）——保留限定词或干脆不提。
- **名字拼写**：本名 Le Cun（两词），惯用拼写 LeCun——正文统一用 LeCun，封面小字可注本名。
- **Meta 离职表述**：2025-11-19 "确认将离开"创办 AMI Labs——页面未载"被解雇"等情节，勿编造。
- **在世者**：死亡日期留白；家庭仅"三个儿子、兄弟在 Google"，勿扩展。
- **引语**：页面实载直接引语仅 FT 2025 "LLMs basically are a dead end..." 句；其余**勿编造**。
- **融资数字**：AMI 2026-03 融资 **$1.03B**、投前估值 **$3.5B**——两数勿混。
- **职务头衔**：获图灵奖时在任为 NYU 教授 + Meta 首席 AI 科学家（2013 年入职）——勿写"Facebook 研究总监"等其他头衔。

## 6. 数据库字段核对表

| 字段 | 值 | 状态 |
|---|---|---|
| qid | 【待补】 | 待写入 |
| name_zh | 杨立昆（或 扬·勒丘恩） | 待写入 |
| name_en | Yann LeCun | 待写入 |
| birth_date | 1960-07-08 | 待写入 |
| death_date | 在世留白 | 待写入 |
| nationality | France / United States | 待写入 |
| primary_occupation | computer scientist | 待写入 |
| field_of_work | artificial intelligence / machine learning / computer vision / robotics / image compression | 待写入 |
| has_biography | 1 | 本次置 1 |

## 7. 社会关系入库清单

- **博士导师**：Maurice Milgram（UPMC/索邦）
- **博士后导师**：Geoffrey Hinton（University of Toronto，1987–1988）
- **长期合作者**：Léon Bottou（DjVu/Lush/LeNet 论文）、Patrick Haffner（DjVu/LeNet 论文）、Vladimir Vapnik（AT&T 同事）、Yoshua Bengio（1998 LeNet 论文、ICLR 共同创办、2015 Nature 综述）
- **Bell Labs 上级**：Lawrence D. Jackel（自适应系统研究部主任）
- **门生**：页面**无载**（无 notable students 列表）——禁写

## 8. 奖项清单

- ACM A.M. Turing Award（2018，与 Hinton、Bengio 共享）
- AAAI Fellow（2019）
- IEEE Neural Network Pioneer Award（2014）；PAMI Distinguished Researcher Award（2015）
- IRI Medal（2018）；Harold Pender Award（宾大，2018）
- Golden Plate Award, American Academy of Achievement（2019）
- 美国国家科学院院士（2021）
- Princess of Asturias Award, Scientific Research（2022，与 Bengio/Hinton/Hassabis）
- Chevalier de la Légion d'Honneur（法国荣誉军团骑士，2023，马克龙总统授勋）
- Global Swiss AI Award 2023（2024 达沃斯 WEF 授予）
- VinFuture Prize 大奖（2024，与 Bengio/Hinton/Huang/Fei-Fei Li）
- Queen Elizabeth Prize for Engineering（2025，与 Bengio/Dally/Hinton/Hopfield/Huang/Fei-Fei Li）
- 美国国家工程院院士、法国科学院院士；荣誉博士：IPN 墨西哥城（2016）、EPFL（2018）、Université Côte d'Azur（2021）、Siena（2023）、HKUST（2023）

## 9. 机构清单

- 教育：ESIEE Paris（工程师文凭 1983）；Université Pierre et Marie Curie（PhD 1987，今索邦大学）
- 博后：University of Toronto（1987–1988，Hinton 指导）
- 任职：AT&T Bell Labs 自适应系统研究部（1988–1996）；AT&T Labs-Research 图像处理研究部主任（1996–）；NEC Research Institute 短暂 Fellow；New York University（2003–，Jacob T. Schwartz 讲席教授；NYU CDS 创始主任 2012）；Meta/Facebook 首席 AI 科学家、FAIR 首任主任（2013–2025）；AMI Labs 执行主席（2025–）；Logical Intelligence 技术研究委员会创始主席（2026–）；Kyutai 科学顾问；CIFAR Learning in Machines & Brains 联合主任

## 10. 终审清单

- [ ] 生卒 1960-07-08 Soisy-sous-Montmorency；在世留白
- [ ] 图灵奖 2018 三人共享 + ACM 全句获奖理由（与 Hinton/Bengio 篇口径一致）
- [ ] 本篇侧重：CNN/LeNet、1989 Zip Code、支票识别商用、DjVu；AlexNet 不展开
- [ ] 反向传播表述为"博士论文中早期形式"，勿写发明人
- [ ] Bell Labs 1988–1996、NYU 2003 起、Meta 2013–2025、AMI Labs 2025 时间线准确
- [ ] AMI 融资 $1.03B 与投前估值 $3.5B 两数勿混
- [ ] 引语仅 FT 2025 "dead end" 句，标注出处
- [ ] 国籍用「法国/美国」，封面底部状态栏 `法国/美国 | Bell Labs · NYU · Meta · AMI Labs | Turing 2018`
- [ ] 正文采用高斯版式：表格语义化 + 公式框 + 时间线 + 身份信息页 + 品牌 OpenMathAI
- [ ] 头像使用 `images/960px-Yann_LeCun_at_the_University_of_Minnesota.jpg` 或 `500px-Laura_Chaubard_Yann_Le_Cun_-_2024_53814052697_cropped_.jpg`（真实肖像，取其一，优先 2024 年新照）
- [ ] `make distclean && make` 编译通过，0 错误

## 11. Review 流程规范（两轮 Review）

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `turing/pages/2018/Yann LeCun/index.html` 建立事实基准，逐页对照 Beamer tex 全部事实
- [ ] **头像**：使用 2024 年照（`images/500px-Laura_Chaubard_Yann_Le_Cun_-_2024_53814052697_cropped_.jpg`，备选 `960px-Yann_LeCun_at_the_University_of_Minnesota.jpg` 2014 年照）
- [ ] **国籍**：封面顶部徽章明示法国/美国
- [ ] **引语核对**：引语必须在 Wikipedia 原文找到
- [ ] **编译验证**：`make distclean && make`
- [ ] **更新提示词**：Review 修正写回本文件

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 身份信息页布局与 Marvin_Minsky 模板对齐
- [ ] 中文标点 / 断行 / 间距统一
- [ ] 与同批次（Bengio / Hinton）格式对齐、共同部分表述不重复（CNN 主叙事归本篇）

---

> **开始执行。每完成一步向我汇报。**
> **最重要的事：每写一页就 make，看到溢出就修。**
