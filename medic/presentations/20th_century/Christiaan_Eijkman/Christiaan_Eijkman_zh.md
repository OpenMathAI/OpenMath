# 医学家立传提示词（Christiaan Eijkman）

> 本文件是 OpenMedic 项目（OpenMathAI 诺贝尔生理学或医学奖人物史）20 世纪 1929 年得主 Christiaan Eijkman 的人物专属立传提示词。
> 事实基准：`medic/presentations/pages/20th_century/Christiaan_Eijkman/page.md`（唯一事实来源，metadata.json 仅作参考）。
> 结构对齐标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（11 节合并为 9 节）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Christiaan Eijkman（1858-08-11 生于荷兰尼凯克 ~ 1930-11-05 逝于荷兰乌得勒支，享年 72 岁）
- **气质关键词**：**脚气病饮食病因的证明者、抗神经炎维生素的发现起点、荷兰生理学家** —— 1929 诺贝尔生理学或医学奖获奖理由（逐字引用 `medic/nobel_medicine_citations.json`）：
  > "for his discovery of the antineuritic vitamin"（因其发现抗神经炎维生素）
- **设计母题**：**一锅米饭的对照（the missing grain）**。实验室鸡群因一口军米改换而在患病与康复之间摆动——精米与糙米之差，藏着"抗脚气因子"。视觉语言：完整与缺失的米粒拼图、两只对比的饲料碗，比抽象的"分子式"更贴合这次偶然的伟大观察。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Christiaan_Eijkman/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）
- **关键时间线（身份信息页与时间轴素材，均出自 page.md）**：
  - 1858-08-11 生于尼凯克（父为当地学校校长，与本人同名；七子中最小）
  - 1859 全家迁居赞丹
  - 1875 进阿姆斯特丹大学军医学校（为荷属东印度军队培养军医，各科考试均优等）
  - 1879-1881 任生理学教授 Thomas Place 助手，撰写博士论文
  - 1883-07-13 以优等获博士学位（神经的极化）；同年娶 Aaltje Wigeri van Edema 并赴东印度
  - 1883-1885 荷属东印度军医（Semarang、Tjilatjap、Padang Sidempoean）
  - 1885 患疟疾，病休返欧；在阿姆斯特丹 Forster 实验室与柏林科赫细菌学实验室工作
  - 1886-1887 随 Pekelharing-Winkler 脚气病调查使团赴巴达维亚
  - 1887 出任爪哇医生学校（首所在印尼的医学校）首任所长
  - 1888-01-15 至 1896-03-04 任医学实验室（Geneeskundig Laboratorium）所长；1888 于巴达维亚再娶 Bertha van der Kemp
  - 军米改换事件：实验室鸡群食精米患病、换回糙米数日康复——"抗脚气因子"假说
  - 1890 在东印度医学杂志发表热带生理研究
  - 1898 继任 G. van Overbeek de Meyer 任乌得勒支卫生与法医学教授
  - 1907 任荷兰皇家科学院院士（1895 起为通讯会员）
  - 1929 与 Hopkins 共享诺贝尔生理学或医学奖
  - 1930-11-05 卒于乌得勒支；1970 月球背面 Eijkman 环形山命名

---

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章执行 Beamer 立传，**第 0/1/2/3 步按 medic 路径执行**：
> - 页面与元数据：`medic/presentations/pages/20th_century/Christiaan_Eijkman/`（page.md / metadata.json / images.txt）
> - 目录创建：`medic/presentations/20th_century/Christiaan_Eijkman/` 与 `images/`
> - Makefile：复制 medic 侧同结构模板，设 `MAIN=Christiaan_Eijkman_zh`
> - 肖像：images.txt 内有 Eijkman.jpg 缩略 URL（250px 改 500px，curl 加 `-A "Mozilla/5.0"`，file 验证）；404 则 Commons `Special:FilePath/Eijkman.jpg?width=600` 回退；再失败用装饰圆占位
> 每完成一步汇报，溢出即修（make → pdftoppm 逐页目检）。

---

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | nutrition science | 营养科学 | 诺奖核心：抗神经炎维生素（维生素 B1/硫胺素）的发现起点 | 核心页 |
| 1 | physiology | 生理学 | 本职教授学科；博士论文《神经的极化》；热带生理研究 | 早年页 |
| 2 | bacteriology | 细菌学 | 乌得勒支时期发酵试验（Eijkman 试验）与细菌死亡率研究 | 乌得勒支页 |
| 3 | tropical medicine | 热带医学 | 荷属东印度脚气病调查与爪哇医生学校 | 东印度页 |

---

## 四、社会关系梳理 + 入库 【人物专属】

> 与 `MySQL/data/Christiaan_Eijkman.yaml` 完全一致；只收 page.md 明载的关系。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Thomas Place | 师→生 | 阿姆斯特丹大学生理学教授（1879-1881 助手），1883 博士论文《神经的极化》 |
| co-honored | Frederick Gowland Hopkins | 无向 | 1929 诺贝尔生理学或医学奖共享（维生素的发现） |
| colleague | Adolphe Vorderman | 无向 | 友人；其对照调查证实精米与脚气病的关联 |
| colleague | Robert Koch | 无向 | 1885-86 病休期间在柏林科赫细菌学实验室工作 |
| colleague | Cornelis Adrianus Pekelharing | 无向 | 巴达维亚脚气病调查委员会（Pekelharing-Winkler 使团）共事 |
| colleague | Tiberius Cornelis Winkler | 无向 | 同上使团成员 |
| colleague | M. B. Romeny | 无向 | 随使团同行共事的同事（正文明载 colleague） |
| spouse | Aaltje Wigeri van Edema | — | 1883 结婚，1886 去世 |
| spouse | Bertha Julie Louise van der Kemp | — | 1888 于巴达维亚结婚 |
| parent-child | Pieter Hendrik Eijkman | — | 独子（1890 生），后成为医生 |
| parent-child | Johanna Alida Pool | — | 母 |

**不入库裁定**：父亲与本人同名（均 Christiaan Eijkman，当地学校校长），同名人建 parent-child 会自环，不入库并在幻灯片中仅文字提及；兄 Johann Frederik Eijkman（物理化学家）为 sibling 无类型不入库；Casimir Funk 造词 "vitamin" 系学术史事件，两人无个人关系记载不入库；G. van Overbeek de Meyer 为乌得勒支教席前任非关系。

---

## 五、配色方案 【人物专属】

- **气质**：朴素、实证、殖民地实验室里的偶然之光
- **主色**：荷兰蓝 `#1E4E79`（与人物气质呼应——代尔夫特陶蓝、军医制服、冷静的对照实验）
- **诺奖色**：香槟金 `#D4AF37`
- **四分类色（badgeA-D）**：
  - `badgeA` 营养科学（维生素）——米金 `#C89B3C`
  - `badgeB` 生理学——神经蓝 `#3A6FA8`
  - `badgeC` 细菌学——培养皿青 `#2E7D6B`
  - `badgeD` 热带医学——爪哇赭 `#A6531E`
- **背景母题**：稀疏米粒圆点与对照天平弧线（对应"一锅米饭的对照"），badge 四色错落

### 5.1 医学家格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + 细边框 + 姓名小字注；无真实肖像用装饰圆占位并注明。
2. **封面有国籍**：底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（02 页）：左头像 + 右信息网格，含生卒、出生地、教育、师承、任职、荣誉、核心领域；事实取自 page.md infobox，不得杜撰。
4. **品牌口径统一**：结尾页底部品牌标注写 `OpenMathAI`；引号用半角 `" "`。
5. **获奖理由逐字引用** `medic/nobel_medicine_citations.json` 原文 + 中译，不得改写或扩写。

---

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input medic 封面模板）
01  封面 — 一锅米饭的启示 / Christiaan Eijkman 1858–1930 + 四色 badge + 右上头像 + 国籍行（Netherlands）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、尼凯克、阿姆斯特丹军医学校、乌得勒支教授、荣誉、核心领域）
03  核心贡献概览 — 脚气病饮食病因 / 抗神经炎维生素 / Eijkman 试验 / 热带医学教育
04  尼凯克与阿姆斯特丹（1858–1883）— 七子之家最小者、军医学校全优、1883 博士《神经的极化》
05  荷属东印度军医（1883–1885）— 三马林多/芝拉扎/巴东昔班、疟疾缠身、病休返欧
06  科赫实验室与调查委员会（1885–1887）— 柏林进修、Pekelharing–Winkler 脚气病使团随行
07  巴达维亚建校（1887–1896）— 爪哇医生学校首任所长、医学实验室所长（1888-01-15~1896-03-04）、热带生理纠偏
08  偶然的发现（核心贡献页）— 实验室鸡群与军米改换、患病与康复的翻转
09  精米与脚气病 — "抗脚气因子"假说、Vorderman 调查证实、后确认为维生素 B1（硫胺素）
10  乌得勒支教授（1898–1930）— 卫生与法医学教授、发酵试验（Eijkman 试验）、细菌死亡率非对数曲线
11  公共卫生 — 健康委员会、抗酒精与抗结核斗争、创建防痨协会
12  荣誉与认可 — Nobel 1929（与 Hopkins 共享）、荷兰皇家科学院 1907、John Scott 奖、NAS 外籍院士
13  遗产 — 月球背面 Eijkman 环形山（1970）、印尼 Eijkman 分子生物学研究所、Eijkman 奖章
14  结尾 — 从病鸡到维生素时代
```

---

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方逐字为 "for his discovery of the antineuritic vitamin"；Hopkins 同届理由是另一句 "for his discovery of the growth-stimulating vitamins"——两句不同，勿互换 |
| 共享而非同工 | 与 Hopkins 共享 1929，但两人发现互不相同（Eijkman=抗神经炎维生素，Hopkins=生长刺激维生素）；Wikipedia 导语 "for the discovery of vitamins" 是合并表述 |
| 父子同名 | 父亲 Christiaan Eijkman 与本人同名（当地学校校长），建 parent-child 会自环——不入库，页面只文字提及 |
| 发现的偶然性 | 鸡群患病系新厨师拒用军米的偶发事件；他最初怀疑是"未知细菌"——勿写成一开始就认定营养缺乏 |
| 因果链分工 | Eijkman 假说→Vorderman 对照调查证实→最终锁定维生素 B1/硫胺素；Casimir Funk 将 "vital amine" 缩为 "vitamin"；正文评 Funk "perhaps unfairly, was never given full credit"——可写，但 Funk 无个人关系不入库 |
| 论文与日期 | 博士论文 *Over Polarisatie in de Zenuwen*（神经的极化），1883-07-13 以优等（with distinction）获博士学位 |
| 精确日期 | 医学实验室所长任期 1888-01-15 至 1896-03-04；乌得勒支就职演讲 *Over Gezondheid en Ziekten in Tropische Gewesten* |
| 教席前任 | 1898 继任 G. van Overbeek de Meyer 任乌得勒支卫生与法医学教授 |
| 学界职务 | 1907 任荷兰皇家科学院院士（1895 起为通讯会员）；NAS 为外籍院士（foreign associate） |
| metadata 噪声 | metadata.json 无配偶/子女载；两任妻子与独子 Pieter Hendrik 以 page.md 为准 |
| 遗产命名 | 月球背面 Eijkman 环形山 1970 年命名；印尼以其名命名 Eijkman 分子生物学研究所——勿写成"以其名命名诺贝尔奖" |
| 健康伏笔 | 1885 疟疾致健康受损被迫返欧，反而开启科赫实验室机遇——"因祸得福"是正文明载叙事 |

---

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| beriberi | 脚气病 | 周围神经疾病，勿与足癣混 |
| polished rice | 精米 | 致病饲料 |
| unpolished rice | 糙米 | 康复饲料 |
| antineuritic vitamin | 抗神经炎维生素 | 即维生素 B1 |
| thiamine | 硫胺素 | 维生素 B1 的学名 |
| "anti-beriberi factor" | "抗脚气因子" | Eijkman 当年命名，保留引号 |
| fermentation test | 发酵试验 | 即 Eijkman 试验，检水与人畜粪便污染 |
| coli bacilli | 大肠杆菌 | 水污染指示菌 |
| auxanographic method | 生长谱法 | 源自 Beijerinck（正文作 Beyerinck）的方法 |
| arrack | 亚力酒 | 发酵研究对象 |
| Geneeskundig Laboratorium | （巴达维亚）医学实验室 | 荷兰语原名保留 |

---

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**PAST**（manifest 预分配）
- **风格**：历史感 / 深沉
- **匹配理由**：从 19 世纪殖民地军营到维生素时代的黎明——"历史感/深沉"匹配这段跨越东西印度的漫长因果链；偶然的鸡舍观察最终撬动营养学的奠基，配乐宜沉稳克制
- **本地路径**：`music_audio/alex-productions/89-geyy8_WXDK0-PAST.wav`（以 curated_tracks.md 为准），复制到 `medic/presentations/20th_century/Christiaan_Eijkman/PAST.wav`
- **时长**：曲长须 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐
