# 医学家立传提示词（André Michel Lwoff）

> 本文件是 OpenMedic 项目（OpenMathAI 诺贝尔生理学或医学奖人物史）20 世纪 1965 年得主 André Michel Lwoff 的人物专属立传提示词。
> 事实基准：`medic/presentations/pages/20th_century/André_Michel_Lwoff/page.md`（唯一事实来源，metadata.json 仅作参考）。
> 结构对齐标杆：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（11 节合并为 9 节）。

---

## 一、背景信息 【人物专属】

- **目标医学家**：André Michel Lwoff（1902-05-08 生于法国阿列省阿奈堡 ~ 1994-09-30 逝于巴黎，享年 92 岁）
- **气质关键词**：**原病毒的命名者、溶原性机制的破解者、巴斯德研究所的微生物学宗师** —— 1965 年诺贝尔生理学或医学奖（与 Jacob、Monod 共享）获奖理由（逐字引用 `medic/nobel_medicine_citations.json`）：
  > "for their discoveries concerning genetic control of enzyme and virus synthesis"（因其关于酶合成与病毒合成的遗传控制的发现）
- **设计母题**：**沉睡的病毒（the sleeping provirus）**。温和噬菌体把自身的基因组整合进细菌染色体，随宿主静默复制、随诱导而苏醒——Lwoff 为这种"潜伏的病毒"命名为 provirus。视觉语言：细菌染色体上静静嵌入的一段异色片段、紫外线诱导下喷薄而出的噬菌体颗粒。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/André_Michel_Lwoff/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）
- **关键时间线（身份信息页与时间轴素材，均出自 page.md）**：
  - 1902-05-08 生于阿列省阿奈堡（奥弗涅），俄裔波兰犹太家庭（父 Solomon 为精神病学家，母 Marie 原姓 Siminovitch，为画家）
  - 19 岁进入巴黎巴斯德研究所
  - 1932 完成博士；获洛克菲勒基金会资助，携妻赴海德堡凯撒·威廉医学研究所（今马普医学研究所）Otto Meyerhof 处研究鞭毛虫的发育
  - 1937 又一笔洛克菲勒资助赴剑桥大学
  - 1938 任巴斯德研究所部门主任
  - 研究版图：噬菌体、微生物群（microbiota）、脊髓灰质炎病毒的开拓性研究
  - 命名 provirus：某些病毒以原病毒形式感染细菌（溶原性机制的发现）
  - 1958 当选皇家学会外籍会员（ForMemRS）；1960 获荷兰皇家科学院 Leeuwenhoek 奖章
  - 1964 获英国生化学会 Keilin 奖章；多次获法国科学院奖项与 Charles-Leopold Mayer 大奖
  - 1965 与 Jacob、Monod 共享诺贝尔生理学或医学奖
  - 美国 NAS、美国艺术与科学院、美国哲学学会院士
  - 1974 起任欧洲微生物学会联合会（FEMS）主席两年；FEMS-Lwoff 奖以其名命名
  - 与妻子 Marguerite Lwoff（微生物学家、病毒学家）终身合作、合著大量论文
  - 人道主义者，反对死刑
  - 1994-09-30 卒于巴黎

---

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章执行 Beamer 立传，**第 0/1/2/3 步按 medic 路径执行**：
> - 页面与元数据：`medic/presentations/pages/20th_century/André_Michel_Lwoff/`（page.md / metadata.json / images.txt）
> - 目录创建：`medic/presentations/20th_century/André_Michel_Lwoff/` 与 `images/`
> - Makefile：复制 medic 侧同结构模板，设 `MAIN=André_Michel_Lwoff_zh`
> - 肖像：优先 images.txt 缩略 URL（250px 改 500px，curl 加 `-A "Mozilla/5.0"`，file 验证）；404 用 Commons `Special:FilePath` 回退；均失败用装饰圆占位
> 每完成一步汇报，溢出即修（make → pdftoppm 逐页目检）。

---

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | microbiology | 微生物学 | 本职学科（infobox Fields）；巴斯德研究所部门主任 | 身份页 |
| 1 | virology | 病毒学 | 诺奖核心：原病毒与溶原性机制；脊灰病毒研究 | 核心页 |
| 2 | bacteriophage research | 噬菌体研究 | 温和噬菌体与细菌的整合关系 | 核心页 |
| 3 | microbiota research | 微生物群研究 | 微生物群（microbiota）开拓性研究之一 | 研究页 |

---

## 四、社会关系梳理 + 入库 【人物专属】

> 与 `MySQL/data/André_Michel_Lwoff.yaml` 完全一致；只收 page.md 明载的关系。

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | François Jacob | 无向 | 1965 诺贝尔生理学或医学奖共享（酶与病毒合成的遗传控制） |
| co-honored | Jacques Monod | 无向 | 1965 诺贝尔生理学或医学奖共享（酶与病毒合成的遗传控制）；亦为其微生物学引路人 |
| spouse | Marguerite Lwoff | — | 微生物学家、病毒学家，终身合作者与合著者 |
| colleague | Otto Fritz Meyerhof | 无向 | 1932 洛克菲勒资助赴海德堡其研究所研究鞭毛虫发育（库内 id=4621） |
| parent-child | Solomon Lwoff | — | 父，精神病学家 |
| parent-child | Marie Siminovitch | — | 母，画家 |

**不入库裁定**：★Monod 对 Lwoff 亦师亦友（Monod 页明载 "André Lwoff initiated him into the potentials of microbiology"）——该边由 Monod 篇 yaml 以 advisor-student 建立，Lwoff 侧不重复建边；Marguerite 的合作贡献与"他获得的认可远多于她"（正文原话）须在叙事页点明，不另建边；Rockefeller Foundation 系资助机构非关系人。

## 五、配色方案 【人物专属】

- **气质**：宗师的静默权威——九十二年里看着微生物学换了三次天地
- **主色**：巴斯德深蓝 `#2A4B7C`（与人物气质呼应——老研究所的砖墙与显微镜的黄铜）
- **诺奖色**：香槟金 `#D4AF37`
- **四分类色（badgeA-D）**：
  - `badgeA` 微生物学——培养皿青 `#2E7D6B`
  - `badgeB` 病毒学（原病毒）——潜伏紫 `#6B4E9E`
  - `badgeC` 噬菌体研究——噬斑橙 `#B4632A`
  - `badgeD` 微生物群——菌苔绿 `#C89B3C`
- **背景母题**：染色体上嵌入的异色片段与喷发的噬菌体颗粒（对应"沉睡的病毒"），badge 四色错落

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
01  封面 — 原病毒的命名者 / André Michel Lwoff 1902–1994 + 四色 badge + 右上头像 + 国籍行（France）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、阿奈堡、巴斯德研究所、三院院士、荣誉、核心领域）
03  核心贡献概览 — 原病毒与溶原性 / 噬菌体 / 脊灰病毒 / 微生物群
04  阿奈堡与巴斯德研究所（1902–1932）— 俄裔波兰犹太家庭、19 岁入所、1932 博士
05  海德堡与剑桥（1932–1938）— Meyerhof 门下鞭毛虫发育研究、两笔洛克菲勒资助
06  巴斯德部门主任（1938–）— 噬菌体/微生物群/脊灰病毒三线并进
07  原病毒假说（核心贡献页一）— 温和噬菌体的整合与静默
08  溶原性机制（核心贡献页二）— 诱导苏醒的实验图景；provirus 命名
09  1965 诺贝尔奖 — 三人共享；Lwoff 侧=病毒合成的遗传控制（原病毒）
10  荣誉与认可 — Leeuwenhoek 奖章 1960、Keilin 奖章 1964、ForMemRS 1958、Mayer 大奖
11  宗师与建制 — FEMS 主席（1974 起）、FEMS-Lwoff 奖、三院院士
12  Marguerite — 终身合作者与合著者；"他获得的认可远多于她"（正文原话，叙事页点明）
13  人道主义者 — 反对死刑的公开立场（正文一句，客观呈现）
14  结尾 — 给"沉睡的病毒"起名字的人
```

---

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由措辞 | 官方逐字为 "for their discoveries concerning genetic control of enzyme and virus synthesis"——三人共享同一句；正文奖项段另作"发现某些病毒（他命名为原病毒）感染细菌的机制"——后者是其个人分工表述，两者勿互换 |
| 姓名口径 | citation json 用短名 "André Lwoff"；yaml/页面用 manifest 全名 **André Michel Lwoff** |
| 页面单薄 | 本篇 page.md 较短（49 行正文）——15 页规划已按正文信息密度压缩叙事页，禁止脑补未载事实填补版面 |
| Meyerhof 关系 | 1932 赴海德堡 "to Otto Meyerhof" 研究鞭毛虫——访问研究者关系，用 colleague 而非 advisor-student（其博士在巴斯德完成，导师未载） |
| 与 Monod 双向 | Monod 页明载 Lwoff 是其微生物学引路人（advisor-student 边建在 Monod yaml）；Lwoff yaml 只写 co-honored——两侧不重复建边 |
| Marguerite | 正文原话 "he gained considerably more recognition"——叙事页必须点明妻子贡献被低估，这是正文明载的公平表述 |
| 奖项年份 | Leeuwenhoek Medal 1960（荷兰皇家科学院）、Keilin Medal 1964（英国生化学会）、ForMemRS 1958、FEMS 主席 1974 起两年——勿串 |
| 脊灰病毒 | Lwoff 研究过脊髓灰质炎病毒——与 Landsteiner/Popper 的 1909 发现无涉，勿跨篇混写 |
| metadata 噪声 | metadata occupations 含 botanist（存疑）——primary 按 microbiologist；生卒 1902-05-08 / 1994-09-30 两处一致 |

---

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| provirus | 原病毒 | 其命名，诺奖核心词 |
| lysogeny | 溶原性 | 温和噬菌体与宿主的关系 |
| bacteriophage | 噬菌体 | 实验系统 |
| temperate phage | 温和噬菌体 | 溶原与裂解之别 |
| microbiota | 微生物群 | 其开拓领域之一 |
| flagellate | 鞭毛虫 | 海德堡时期研究对象 |
| poliovirus | 脊髓灰质炎病毒 | 其研究病种之一 |
| Leeuwenhoek Medal | 列文虎克奖章 | 1960，微生物学界最高荣誉之一 |
| FEMS | 欧洲微生物学会联合会 | 1974-76 任主席 |
| Keilin Medal | 凯林奖章 | 1964，英国生化学会 |

---

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Cinematic Experience**（manifest 预分配）
- **匹配理由**：一位横贯二十世纪的旁观者与宗师——从 1902 年的奥弗涅到 1994 年的巴黎，"电影感"贴合其漫长的全景人生；原病毒的"潜伏-苏醒"亦自带戏剧张力
- **本地路径**：`music_audio/` 下检索曲名（参照 `curated_tracks.md`），复制到 `medic/presentations/20th_century/André_Michel_Lwoff/Cinematic Experience.wav`
- **时长**：曲长须 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐

