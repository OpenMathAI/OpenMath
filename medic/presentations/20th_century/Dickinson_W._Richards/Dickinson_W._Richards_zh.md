# 医学家立传提示词（Dickinson W. Richards）

> OpenMedic 项目、20 世纪诺贝尔生理学或医学奖 1956 年得主（迪金森·理查兹，心导管术的共同发展者）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Dickinson Woodruff Richards Jr.（1895-10-30 生于新泽西州奥兰治 ~ 1973-02-23 卒于康涅狄格州莱克维尔，享年 77 岁）
- **气质关键词**：**心导管术的共同发展者、心肺生理的系统刻画者、从文科生到诺奖生理学家的转轨者** —— 1956 获奖理由（与 André Frédéric Cournand、Werner Forssmann 三人共享）：
  > "for their discoveries concerning heart catheterization and pathological changes in the circulatory system"（因发现心导管术与循环系统的病理变化）
- **设计母题**：**从肺到心的测量**。Richards 与 Cournand 从肺功能测量起步，把福斯曼的孤勇延展成对休克、心衰、先心病的系统生理刻画。视觉隐喻：一组压力曲线从肺野延伸到心腔。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Dickinson_W._Richards/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/20th_century/Dickinson_W._Richards/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准，裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/20th_century/Dickinson_W._Richards/`（含 `images/`）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=Dickinson_W._Richards_zh`、`VIDEO_NAME=Dickinson_W._Richards_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/20th_century/Dickinson_W._Richards/images.txt`；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/Dickinson_W._Richards.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | cardiac catheterization | 心导管术 | 与 Cournand 共同发展，1956 诺奖核心 | 核心页 |
| 1 | pulmonary physiology | 肺生理 | Bellevue 肺功能研究 | 核心页 |
| 2 | circulatory physiology | 循环生理 | 创伤性休克、心衰生理 | 核心页 |
| 3 | cardiology | 心脏病学 | 先天性心脏病诊断技术 | 核心页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | André Frédéric Cournand | 无向 | 1956 诺贝尔生理学或医学奖三人共享（心导管术与循环系统病理变化） |
| co-honored | Werner Forssmann | 无向 | 1956 诺贝尔生理学或医学奖三人共享（心导管术与循环系统病理变化） |
| colleague | André Frédéric Cournand | 无向 | 1928 起 Bellevue 医院长期合作（肺功能→心导管术） |
| advisor-student | Henry Hallett Dale | 导师 | 1927-28 伦敦国家医学研究所（NIMH）在其门下研究肝脏循环调控 |
| advisor-student | Lawrence Joseph Henderson | 导师 | 1928 年后在哈佛 Henderson 指导下开展肺与循环生理研究 |
| spouse | Constance | 无向 | 妻，1990 年去世 |

> relations=6 为诚实值，Review 勿误判虚增。
> 不入库：Scroll and Key 社团；Merck Sharp and Dohme（商业顾问+Merck 手册编辑，机构关系）；《世界宪法》公约签署（全球政策段，政治性事件非个人关系）；子女未载。
> 库内当时无 Henry Hallett Dale / Lawrence Joseph Henderson / Constance 记录，均由本 yaml 新建 stub——**Henry Hallett Dale 系 1936 诺奖得主，若由其他批次（生理学/药理学侧）规范化将按名幂等回填**；Cournand/Forssmann 由本批各自 yaml 幂等覆盖。

## 五、配色方案 【人物专属】

- **气质**：耶鲁书卷的墨蓝 + 生理曲线的精密 + Bellevue 病房的人间烟火
- **主色**：书卷墨蓝 `#1F4E79`（文科出身的书写者气质与临床科学的严谨）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` 心导管术 — 书卷墨蓝 `#1F4E79`
  - `badgeB` 肺生理 — 深青 `#0E7C7B`
  - `badgeC` 循环病理与休克 — 暗红 `#8C2F1B`
  - `badgeD` 荣誉与传承 — 琥珀 `#A0722D`
- **背景母题**：数条平行的生理压力曲线（波峰渐次抬升），badge 圆点嵌于曲线上。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — 心导管术的共同发展者 / Dickinson W. Richards 1895–1973 + 四色 badge + 右上头像 + 国籍行 USA
02  身份信息页（★ 必做）— 左头像 + 右信息网格（出生 Orange NJ、教育 Hotchkiss School/
    Yale BA 1917（英语与希腊语）/哥伦比亚 MA 1922/MD 1923、
    任职长老会医院/NIMH 伦敦/哥伦比亚/Bellevue、荣誉 Nobel 1956/Kober Medal 1970、核心领域）
03  核心贡献概览 — 心导管术共同发展 / 创伤性休克刻画 / 心衰生理 / 先心病诊断
04  文科少年与一战 (1895–1919) — Hotchkiss School、1913 入耶鲁读**英语与希腊语**、
    1917 毕业（Scroll and Key 社）、从军任炮兵教官、1918-19 驻法炮兵军官
05  哥伦比亚转轨医学 (1919–1927) — MA 1922/MD 1923、长老会医院任职至 1927
06  伦敦：Dale 门下 (1927–1928) — 国家医学研究所（NIMH）、Sir Henry Dale（1936 诺奖得主）
    指导下研究肝脏循环调控
07  哈佛与转肺生理 (1928) — 回美后在哈佛 Lawrence Henderson 指导下
    开展肺与循环生理研究——人生方向的定锚
08  Bellevue：与 Cournand 的长期合作 — 1928 起合作肺功能研究
    （肺病患者的肺功能测量方法）、1945 实验室迁入 Bellevue
09  导管术：从设想到系统 — 发展心导管技术、研究并刻画创伤性休克与心衰生理、
    测量心脏药物效应、描述慢性心肺疾病各型功能障碍与治疗、
    发展先天性心脏病诊断技术
10  1956 诺贝尔奖 — 三人共享（Forssmann 首创+CouRNAND/Richards 发展）、
    官方理由逐字引用
11  教职与荣誉 — 1947 哥伦比亚 Lambert 医学讲席（1925 起任教）、
    1961 自 Bellevue 与哥伦比亚退休、John Phillips 奖 1960、
    法国荣誉军团骑士 1963、Trudeau 奖章 1968、Kober Medal 1970
12  Merck 顾问与 Merck 手册 — Merck Sharp and Dohme 顾问、《Merck 手册》编辑——
    临床知识工程的另一面
13  全球政策与个人生活 — 《世界宪法》公约签署人（世界制宪会议召集，客观一句）、
    妻 Constance（1990 逝）、1973-02-23 卒于 Lakeville（77 岁）
14  遗产 — 心导管术成为现代心脏病学的通用语言、
    从文科生到诺奖生理学家的转轨样本、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方逐字 "for their discoveries concerning heart catheterization and pathological changes in the circulatory system"（三人共享、their）；page.md 另有半句 "and the characterisation of a number of cardiac diseases"——表述以 citation json 为准 |
| 文科出身 ★ | 耶鲁本科读**英语与希腊语**（1917）——非理科生，是本篇最反直觉的事实，务必保留；Scroll and Key 为高级社团可一句 |
| 双导师 | Dale（伦敦 NIMH，1927-28，肝脏循环）+ Henderson（哈佛，1928 起，肺循环生理）——两条 advisor-student 边，note 区分地点与课题；Dale 为 1936 诺奖得主 |
| 三人分工 | Forssmann 首创、Cournand+Richards 发展——本篇与 Cournand 篇视角相近，注意区分：本篇多写个人脉络（耶鲁/一战/Dale/Henderson/Merck） |
| 《世界宪法》 | 全球政策段：世界制宪公约签署人、《地球联邦宪法》制宪会议——page.md 明载，**客观一句带过、不评价** |
| Merck 双职 | Merck Sharp and Dohme 顾问 + 《Merck 手册》编辑——知识工程面向，勿写成"药企代言" |
| 妻子姓名 | 仅载 "his wife Constance"（无姓）——yaml 存 'Constance'，勿杜撰全名 |
| 时间锚点 | 1913 入耶鲁/1917 毕业/1918-19 驻法/1922 MA/1923 MD/1927-28 伦敦/1928 回美/1945 迁 Bellevue/1947 Lambert 讲席/1961 退休——数字链勿错位 |
| Kober Medal | 1970 年 Association of American Physicians 的 Kober Medal——infobox 载为 George M. Kober Medal，同一奖项两称，照 page.md 正文 Kober Medal |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| cardiac catheterization | 心导管术 | 1956 诺奖核心 |
| characterisation | 刻画 | 理由句中"病理变化刻画"的动词 |
| traumatic shock | 创伤性休克 | 研究对象 |
| heart failure | 心力衰竭 | 生理研究对象 |
| congenital heart disease | 先天性心脏病 | 诊断技术贡献 |
| NIMH (London) | （英国）国家医学研究所 | 1927-28 游学地，勿与美国 NIMH 混淆 |
| Scroll and Key | 斯克罗尔与基社团 | 耶鲁高级社团 |
| Merck Manual | 默克诊疗手册 | 其编辑职务 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Last Hope**（manifest 预分配）
- **风格**：深沉 / 希望 / 守夜人
- **匹配理由**：心导管术诞生的年代，心衰与先心病近乎绝症——Richards 与 Cournand 把测量变成诊断、把诊断变成治疗依据，是"最后的希望"从隐喻变成生理曲线的过程；Last Hope 的深沉希望感匹配这一从绝症叙事到可测量的转折。
- **本地路径**：`music_audio/` 下 Last Hope 对应文件（执行时以 `find music_audio -iname "*Last Hope*"` 实际定位）→ 复制为 `presentations/20th_century/Dickinson_W._Richards/Last_Hope.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；文科出身与双导师线索务必保留。**
