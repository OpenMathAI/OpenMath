# 医学家立传提示词（Herbert Spencer Gasser）

> 本文件是 OpenMedic 项目（OpenMathAI 诺贝尔生理学或医学奖人物史）20 世纪 1944 年得主 Herbert Spencer Gasser 的人物专属立传提示词。
> 事实基准：`medic/presentations/pages/20th_century/Herbert_Spencer_Gasser/page.md`（唯一事实来源，metadata.json 仅作参考）。
> 结构对齐标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（11 节合并为 9 节）。
> ★ 库内已有 stub 'Herbert S. Gasser'（id=3487，无 qid、has_social_data=0），与 manifest 'Herbert Spencer Gasser' 不一致——yaml 沿用库内形式 UPD 回填 Q273201 防分裂，裁定见第七节。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Herbert Spencer Gasser（1888-07-05 生于美国威斯康星州普拉特维尔 ~ 1963-05-11 逝于纽约，享年 74 岁）
- **气质关键词**：**单根神经纤维电活动的破译者、动作电位研究的奠基人、洛克菲勒研究所第二任所长** —— 1944 年诺贝尔生理学或医学奖（与 Joseph Erlanger 共享）获奖理由（逐字引用 `medic/nobel_medicine_citations.json`）：
  > "for their discoveries relating to the highly differentiated functions of single nerve fibres"（因其关于单根神经纤维高度分化功能的发现）
- **设计母题**：**单纤维上的电峰（spikes on one fibre）**。用示波器把一束神经里不同直径纤维的动作电位分开——把"神经如何编码"变成可测量的谱。视觉语言：示波屏上分层的尖峰信号、纤维直径与传导速度的对应谱线。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Herbert_Spencer_Gasser/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）
- **关键时间线（身份信息页与时间轴素材，均出自 page.md）**：
  - 1888-07-05 生于普拉特维尔（父 Herman 为来自奥地利福拉尔贝格多恩比恩的医生；母 Jane 有新英格兰与德俄血统）
  - 1907 入威斯康星大学，两年读完动物学本科
  - 1909 入该校医学院，师从 Joseph Erlanger 学生理学、Arthur S. Loevenhart 学药理学
  - 1911 在校期间即被聘为药理学讲师
  - 1913 转入约翰斯·霍普金斯医学院，1915 获医学学位（MD）
  - 1916 转入华盛顿大学（圣路易斯）生理学系
  - 1918 夏加入美国化学战勤务局（一战）
  - 1921 任华盛顿大学药理学教授
  - 1923-1925 获洛克菲勒基金会资助考察伦敦、巴黎、慕尼黑（改进美国医学教育）
  - 1931 任康奈尔医学院生理学教授
  - 1935-1953 任洛克菲勒研究所第二任所长（继 Simon Flexner，后由 Detlev Bronk 接任）
  - 1936 与 Erlanger 在宾夕法尼亚大学系列演讲总结神经细胞研究
  - 1944 与 Erlanger 共享诺贝尔生理学或医学奖（奖金用于后续研究）
  - 任内当选 NAS、美国哲学学会、美国艺术与科学院院士；一生发表论文逾 100 篇
  - 1945-12-12 发表诺贝尔演讲《哺乳动物神经纤维》（二战致颁奖延迟）
  - 1963-05-11 卒于纽约

---

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章执行 Beamer 立传，**第 0/1/2/3 步按 medic 路径执行**：
> - 页面与元数据：`medic/presentations/pages/20th_century/Herbert_Spencer_Gasser/`（page.md / metadata.json / images.txt）
> - 目录创建：`medic/presentations/20th_century/Herbert_Spencer_Gasser/` 与 `images/`
> - Makefile：复制 medic 侧同结构模板，设 `MAIN=Herbert_Spencer_Gasser_zh`
> - 肖像：正文含 1944 年肖像（infobox 图），images.txt 缩略 URL 250px 改 500px（curl 加 `-A "Mozilla/5.0"`，file 验证）；404 用 Commons `Special:FilePath` 或 REST API 回退；均失败用装饰圆占位
> 每完成一步汇报，溢出即修（make → pdftoppm 逐页目检）。

---

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | neurophysiology | 神经生理学 | 诺奖核心：单根神经纤维功能分化（与 Erlanger 合作） | 核心页 |
| 1 | electrophysiology | 电生理学 | 动作电位与阴极射线示波器方法 | 核心页 |
| 2 | physiology | 生理学 | infobox Fields 口径；本职业学科 | 身份页 |
| 3 | pharmacology | 药理学 | 威斯康星/华盛顿大学药理学教授（1921） | 早年页 |

---

## 四、社会关系梳理 + 入库 【人物专属】

> 与 `MySQL/data/Herbert_Spencer_Gasser.yaml` 完全一致；只收 page.md 明载的关系。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Joseph Erlanger | 师→生 | 威斯康星大学生理学导师（1909 起），后为华盛顿大学同事与合作者 |
| co-honored | Joseph Erlanger | 无向 | 1944 诺贝尔生理学或医学奖共享（单根神经纤维高度分化功能） |
| parent-child | Herman Gasser | — | 父，来自奥地利福拉尔贝格多恩比恩的医生 |
| parent-child | Jane Elisabeth Griswold Gasser | — | 母，新英格兰与德俄血统 |

**不入库裁定**：Arthur S. Loevenhart（药理学授课教师，仅一句带过）不入库；Simon Flexner（前任所长）与 Detlev Bronk（继任）系职务沿革非个人关系，不入库。

---

## 五、配色方案 【人物专属】

- **气质**：精确、克制、示波屏荧光下的冷静
- **主色**：神经深蓝 `#2F4470`（与人物气质呼应——电信号的长夜与研究所的沉默治理）
- **诺奖色**：香槟金 `#D4AF37`
- **四分类色（badgeA-D）**：
  - `badgeA` 神经生理学——峰电位橙 `#B4632A`
  - `badgeB` 电生理学——荧光青 `#2E7D6B`
  - `badgeC` 生理学——学院蓝 `#3A6FA8`
  - `badgeD` 药理学——药剂紫 `#6B4E9E`
- **背景母题**：示波屏网格与分层尖峰（对应"单纤维上的电峰"），badge 四色错落

### 5.1 医学家格式硬要求 【模板通用，★ 必须满足】

1. **封面有头像**：右上角肖像 + 细边框 + 姓名小字注；无真实肖像用装饰圆占位并注明。
2. **封面有国籍**：底部状态栏给出 `国籍 | 机构 | 主要奖项` 三要素。
3. **必须有身份信息页**（02 页）：左头像 + 右信息网格，含生卒、出生地、教育、师承、任职、荣誉、核心领域；事实取自 page.md infobox，不得杜撰。
4. **品牌口径统一**：结尾页底部品牌标注写 `OpenMedic`；引号用半角 `" "`。
5. **获奖理由逐字引用** `medic/nobel_medicine_citations.json` 原文 + 中译，不得改写或扩写。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input medic 封面模板）
01  封面 — 单纤维电密码的破译者 / Herbert Spencer Gasser 1888–1963 + 四色 badge + 右上头像 + 国籍行（United States）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、普拉特维尔、威斯康星/霍普金斯、洛克菲勒研究所第二任所长、荣誉、核心领域）
03  核心贡献概览 — 单纤维功能分化 / 动作电位方法 / 药理学教授 / 洛克菲勒研究所治理
04  普拉特维尔与威斯康星（1888–1913）— 医生之子、两年读完动物学、在校即任药理学讲师（1911）
05  霍普金斯与华盛顿大学（1913–1921）— 1915 MD、1916 生理学系、一战化学战勤务（1918）、1921 药理学教授
06  与 Erlanger 的合作 — 师生变同事：阴极射线示波器分辨单纤维动作电位
07  欧洲考察（1923–1925）— 洛克菲勒基金会资助，伦敦/巴黎/慕尼黑医学教育调研
08  康奈尔与洛克菲勒研究所（1931–1953）— 1931 康奈尔教授、1935 接替 Flexner 任第二任所长 18 年
09  单纤维的分化功能（核心贡献页）— 纤维直径、传导速度与功能的对应谱
10  1936 宾大系列演讲 → 1944 诺贝尔奖 — 奖金全部投入后续研究
11  研究所岁月 — NAS/美国哲学学会/美国艺术与科学院；百篇论文
12  荣誉与认可 — Nobel 1944（与 Erlanger 共享）、Kober 奖章、巴黎大学荣誉博士、皇家学会外籍会员
13  诺奖演讲与遗产 — 1945-12-12《哺乳动物神经纤维》；电生理学的方法论起点
14  结尾 — 把"神经"变成可测量的谱
```

---

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方逐字为 "for their discoveries relating to the highly differentiated functions of single nerve fibres"——注意 **their**（两人共享），勿改成 his |
| 共享结构 | 1944 与导师 Joseph Erlanger 共享——同一人兼 advisor-student 与 co-honored 两行，类型不同不入 uq_rel 冲突 |
| 学位口径 | 最高学位是约翰斯·霍普金斯 **MD（1915）**，不是 PhD；勿写"博士" |
| 在校任教 | 1911 年仍是学生即被聘为药理学讲师——正文明载，勿改成毕业后 |
| 年度与演讲 | 奖为 **1944 年度**；诺贝尔演讲 1945-12-12 才发表（二战延迟）——两个年份勿混 |
| 所长排序 | 洛克菲勒研究所**第二任**所长（1935-1953），前任 Simon Flexner（创始所长）、继任 Detlev Bronk——职务沿革不入关系 |
| 军旅片段 | 1918 夏任职于华盛顿的化学战勤务局——一战背景，勿写成二战 |
| 奖金去向 | 正文明载他把奖金用于该主题的进一步研究——可作叙事点缀 |
| 库内记录名 | manifest name_en 为 'Herbert Spencer Gasser'，库内 stub 为 'Herbert S. Gasser'（id=3487）——yaml 用库内形式 UPD 回填 Q273201，防止同名分裂；总表如需全名由主控裁定 |
| metadata 噪声 | metadata 无父母载；父母姓名以 page.md 为准；生卒 1888-07-05 / 1963-05-11 两处一致 |

---

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| action potential | 动作电位 | 诺奖核心词 |
| nerve fibre | 神经纤维 | citation 用英式 fibre |
| single fibre analysis | 单纤维分析 | 把神经束分解到单根 |
| oscillograph / cathode ray | 示波器 / 阴极射线 | 方法论关键词（正文语境） |
| differentiated functions | 分化（特化）功能 | 勿写成"分化发育" |
| chemical warfare service | 化学战勤务局 | 一战机构名 |
| pharmacology | 药理学 | 其教授职学科 |
| Rockefeller Institute | 洛克菲勒研究所 | 今洛克菲勒大学 |

---

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Pathfinder**（manifest 预分配）
- **匹配理由**：在没人看见的地方先走出一条测量之路——"探路者"贴合用示波器劈开神经束、为电生理学开路的生涯；后半生执掌洛克菲勒研究所，亦是为美国医学研究"探路"的治理者
- **本地路径**：`music_audio/` 下检索曲名（参照 `curated_tracks.md`），复制到 `medic/presentations/20th_century/Herbert_Spencer_Gasser/Pathfinder.wav`
- **时长**：曲长须 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐

