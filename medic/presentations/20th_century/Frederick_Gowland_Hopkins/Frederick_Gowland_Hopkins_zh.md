# 医学家立传提示词（Frederick Gowland Hopkins）

> 本文件是 OpenMedic 项目（OpenMathAI 诺贝尔生理学或医学奖人物史）20 世纪 1929 年得主 Frederick Gowland Hopkins 的人物专属立传提示词。
> 事实基准：`medic/presentations/pages/20th_century/Frederick_Gowland_Hopkins/page.md`（唯一事实来源，metadata.json 仅作参考）。
> 结构对齐标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（11 节合并为 9 节）。
> ★ 本人在 greatminds 库已有记录（id=3459 'Frederick Gowland Hopkins'，无 qid、has_social_data=0），yaml 走 UPD 回填 Q233976，勿新建。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Sir Frederick Gowland Hopkins（1861-06-20 生于英格兰伊斯特本 ~ 1947-05-16 逝于英格兰剑桥，享年 85 岁）
- **气质关键词**：**维生素的发现者、剑桥生物化学的奠基人、色氨酸与谷胱甘肽的发现者** —— 1929 诺贝尔生理学或医学奖获奖理由（逐字引用 `medic/nobel_medicine_citations.json`）：
  > "for his discovery of the growth-stimulating vitamins"（因其发现生长刺激维生素）
- **设计母题**：**完整配方中缺失的一角（the missing ingredient）**。1912 年的饲养实验证明：纯蛋白、碳水、脂肪、矿物质与水不能维持动物生长——正常膳食里还差"极微量的未知物质"。视觉语言：完整圆盘中缺落的一小块、饲料配方表的空格，呼应"辅助食物因子"（accessory food factors）的命名。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Frederick_Gowland_Hopkins/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）
- **关键时间线（身份信息页与时间轴素材，均出自 page.md）**：
  - 1861-06-20 生于伊斯特本（Eastbourne）
  - City of London School → Alexandra Park College（Hornsey）；经 Birkbeck 夜校修伦敦大学校外课程
  - Guy's Hospital 医学院毕业
  - 1894-1898 在 Guy's 执教生理学与毒理学
  - 1898 娶 Jessie Anne Stephens；同年在生理学会会议上受 Michael Foster 之邀加入剑桥生理学实验室
  - 1900-03 任 Emmanuel College 化学生理学讲师（获荣誉 MA）
  - 1901 发现色氨酸
  - 1902-07 获伦敦大学 D.Sc.；同年任三一学院生物化学 readership
  - 1905 当选 FRS
  - 1907 与 Walter Morley Fletcher 研究乳酸与肌肉收缩（缺氧致乳酸堆积）
  - 1910 任三一学院 Fellow
  - 1912 发表饲养实验，提出 "accessory food factors"（后改名 vitamins）
  - 1914 当选剑桥首任生物化学教授（Chair of Biochemistry）
  - 1918 Royal Medal；1922 Cameron Prize；1924 NAS 外籍院士；1925 授勋；1926 Copley Medal
  - 1921 发现并表征谷胱甘肽；1929 修正为三肽结论
  - 1929 与 Eijkman 共享诺贝尔生理学或医学奖
  - 1930-1935 任皇家学会会长；1933 任英国科学促进会会长
  - 1934 Albert Medal；1935 Order of Merit；1937 当选美国哲学学会
  - 1947-05-16 卒于剑桥，与妻合葬 Parish of the Ascension Burial Ground

---

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章执行 Beamer 立传，**第 0/1/2/3 步按 medic 路径执行**：
> - 页面与元数据：`medic/presentations/pages/20th_century/Frederick_Gowland_Hopkins/`（page.md / metadata.json / images.txt）
> - 目录创建：`medic/presentations/20th_century/Frederick_Gowland_Hopkins/` 与 `images/`
> - Makefile：复制 medic 侧同结构模板，设 `MAIN=Frederick_Gowland_Hopkins_zh`
> - 肖像：优先 images.txt 内 Wikimedia 缩略图 URL（250px 改 500px）；404 用 Commons `Special:FilePath/<文件名>?width=600` 或 REST API 回退；均失败用装饰圆占位
> 每完成一步汇报，溢出即修（make → pdftoppm 逐页目检）。

---

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | nutrition science | 营养科学 | 诺奖核心：1912 饲养实验与"辅助食物因子"（维生素） | 核心页 |
| 1 | biochemistry | 生物化学 | 剑桥首任生物化学教授（1914）；色氨酸（1901）、谷胱甘肽（1921） | 生化页 |
| 2 | muscle biochemistry | 肌肉收缩生化 | 1907 与 Fletcher 证明缺氧致乳酸堆积，铺路 Hill/Meyerhof | 合作页 |

---

## 四、社会关系梳理 + 入库 【人物专属】

> 与 `MySQL/data/Frederick_Gowland_Hopkins.yaml` 完全一致；只收 page.md 明载的关系。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Christiaan Eijkman | 无向 | 1929 诺贝尔生理学或医学奖共享（维生素的发现） |
| advisor-student | Thomas Stevenson | 师→生 | Guy's Hospital 毒理学导师（frontmatter doctoral_advisor） |
| advisor-student | Michael Foster | 师→生 | 1898 生理学会会议上邀其加入剑桥生理学实验室 |
| advisor-student | Judah Hirsch Quastel | 生→ | 剑桥博士生，神经化学先驱 |
| advisor-student | Malcolm Dixon | 生→ | 博士生（infobox 明载） |
| advisor-student | Antoinette Pirie | 生→ | 博士生（infobox 明载） |
| advisor-student | J. B. S. Haldane | 生→ | 其他知名学生（infobox 明载，库内规范名 id=485） |
| advisor-student | Albert Szent-Györgyi | 生→ | 其他知名学生（infobox 明载，1937 诺奖得主，库内 id=3316） |
| advisor-student | Joseph Needham | 生→ | 剑桥学生，胚胎学先驱 |
| collaborator | Walter Morley Fletcher | 无向 | 1907 合作研究乳酸与肌肉收缩 |
| spouse | Jessie Anne Stephens | — | 1898 结婚（1861-1937） |
| parent-child | Jacquetta Hawkes | — | 幼女，著名考古学家（子女三人中唯一具名者） |

**不入库裁定**：Archibald Hill 与 Otto Meyerhof 系"其工作铺路"的后来发现者，非个人关系；Edward Calvin Kendall 谷胱甘肽独立结论一致系学术事件；女婿 J. B. Priestley 为姻亲非白名单类型；一子二女中仅 Jacquetta Hawkes 具名，另二人不入库；Michael Foster 用无敬称形式（page.md 链接文本为 Sir Michael Foster）。

---

## 五、配色方案 【人物专属】

- **气质**：学术、温厚、剑桥老学院的沉静光辉
- **主色**：剑桥深绿 `#175E54`（与人物气质呼应——三一学院草坪、生物化学的生机与克制）
- **诺奖色**：香槟金 `#D4AF37`
- **四分类色（badgeA-D）**：
  - `badgeA` 营养科学（维生素）——麦金 `#C89B3C`
  - `badgeB` 生物化学——分子青 `#2E7D6B`
  - `badgeC` 肌肉收缩生化——肌红深红 `#8C1F28`
  - `badgeD` 学派传承——学院蓝 `#1E4E79`
- **背景母题**：完整圆环与缺口扇形（对应"缺失的一角"），badge 四色错落

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
01  封面 — 辅助食物因子的发现者 / Frederick Gowland Hopkins 1861–1947 + 四色 badge + 右上头像 + 国籍行（United Kingdom）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、伊斯特本、Guy's Hospital、剑桥首任生化教授、荣誉、核心领域）
03  核心贡献概览 — 维生素（1912）/ 色氨酸（1901）/ 谷胱甘肽（1921）/ 肌肉收缩生化（1907）
04  伊斯特本与求学（1861–1888）— City of London School、伦敦大学校外课程（Birkbeck 夜校）、Guy's Hospital 医学院
05  Guy's 执教与剑桥之邀（1888–1898）— 生理学与毒理学任教、1898 Michael Foster 邀入剑桥生理学实验室
06  剑桥生物化学奠基（1898–1914）— Emmanuel 化学生理学讲师、1902 伦敦大学 D.Sc.、1910 三一学院 Fellow、1914 首任生物化学教授
07  色氨酸与肌肉收缩 — 1901 发现色氨酸；1907 与 Fletcher 证明缺氧致乳酸堆积
08  1912 饲养实验（核心贡献页）— 纯营养素不能维持生长、"accessory food factors" 假说
09  战时营养与人造黄油 — 一战配给下的营养价值研究、黄油优于人造黄油（缺维生素 A 与 D）、1926 强化人造黄油问世
10  谷胱甘肽 — 1921 发现并表征、最初误判二肽、1929 修正为三肽（谷氨酸+半胱氨酸+甘氨酸）
11  门生与传承 — Quastel、Needham、Haldane、Szent-Györgyi、Dixon、Pirie
12  荣誉与认可 — Nobel 1929、FRS 1905、Royal Medal 1918、Cameron 1922、Copley 1926、OM 1935、皇家学会会长 1930-35
13  遗产 — 维生素时代的开端与剑桥生物化学学派
14  结尾 — 微量之物，性命攸关
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方逐字为 "for his discovery of the growth-stimulating vitamins"（生长刺激维生素）；Eijkman 是 antineuritic vitamin——两句不同，勿互换或合并 |
| 获奖理由范围 | 诺奖理由只含维生素；色氨酸（1901）与谷胱甘肽（1921）不在获奖理由内，勿混写 |
| 命名沿革 | 1912 年他命名 "accessory food factors"，后改名 vitamins；勿写成他发明 vitamin 一词（造词归 Casimir Funk） |
| 谷胱甘肽结构 | 最初提出二肽（谷氨酸+半胱氨酸），1929 年结论为三肽（+甘氨酸），与 Kendall 独立工作一致——两阶段勿混 |
| Hill/Meyerhof 定位 | 他们是"碳水化合物代谢循环供能肌肉收缩"的后来发现者，Hopkins-Fletcher 工作只是铺路——勿写成合作或师承 |
| "第一"限定 | 1914 年"剑桥首任生物化学教授"（first Professor in that discipline at Cambridge），不是"世界首位" |
| 两个会长 | 1930-1935 任皇家学会会长；1933 任英国科学促进会会长——勿混年份 |
| 荣誉年份 | FRS 1905、Royal Medal 1918、Cameron 1922、Copley 1926、骑士（George V）1925、Albert Medal 1934、OM 1935、NAS 外籍院士 1924、美国哲学学会 1937——逐一核对勿串 |
| 子女口径 | 一子两女，仅幼女 Jacquetta Hawkes 具名（考古学家，嫁作家 J. B. Priestley）；妻子 1898 结婚、1861-1937 |
| 导师双轨 | metadata doctoral_advisor 只有 Thomas Stevenson；Michael Foster 来自 infobox Academic advisors——两人均 page.md 明载可入库 |
| 库内记录 | 本人已有库记录 id=3459（无 qid）——yaml 以 name_en 'Frederick Gowland Hopkins' 匹配 UPD 回填 Q233976，不得新建重复记录 |
| 战时细节 | 一战食品短缺与配给背景；结论"人造黄油不如黄油（缺维生素 A 和 D）"；1926 指强化人造黄油问世 |
| 共济会 | 正文一句 "initiated into Freemasonry"——幻灯片可略，不必展开 |

---

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| vitamin | 维生素 | 造词归 Casimir Funk |
| accessory food factors | 辅助食物因子 | Hopkins 1912 原词，保留引号 |
| growth-stimulating vitamins | 生长刺激维生素 | 本人诺奖理由用语 |
| tryptophan | 色氨酸 | 1901 发现的氨基酸 |
| glutathione | 谷胱甘肽 | 1921 发现，1929 定三肽 |
| tripeptide | 三肽 | 谷氨酸+半胱氨酸+甘氨酸 |
| lactic acid | 乳酸 | 肌肉收缩生化核心物质 |
| oxygen depletion | 缺氧 | 致乳酸堆积的条件 |
| margarine | 人造黄油 | 战时营养研究对象 |
| D.Sc. | 理学博士 | 1902 伦敦大学 |
| Royal Society | （英国）皇家学会 | 会长任期 1930-1935 |

---

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**New Lands**（manifest 预分配）
- **匹配理由**：从"未知微量物质"的荒原到维生素时代的新大陆——"新大陆"意象贴合 1912 年饲养实验开辟的全新营养学疆域；旋律的开拓感匹配剑桥学派的奠基叙事
- **本地路径**：`music_audio/` 下检索曲名（参照 `curated_tracks.md`），复制到 `medic/presentations/20th_century/Frederick_Gowland_Hopkins/New Lands.wav`
- **时长**：曲长须 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐

