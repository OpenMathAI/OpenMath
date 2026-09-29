# 医学家立传提示词（Julius Wagner-Jauregg）

> OpenMedic 项目、20 世纪诺贝尔生理学或医学奖 1927 年得主（朱利叶斯·瓦格纳-尧雷格，首位诺奖精神科医生）。
> 本文件是人物专属立传提示词：执行者按其完成 Beamer 立传（pdf + mp4）。事实基准为本地 page.md，
> 获奖理由逐字引自 medic/nobel_medicine_citations.json。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Julius Wagner-Jauregg（1857-03-07 生于上奥地利 Wels ~ 1940-09-27 卒于维也纳，享年 83 岁）
- **气质关键词**：**发热疗法的毕生布道者、首位获诺贝尔奖的精神科医生、荣誉与污点并存的复杂人物** —— 1927 获奖理由（独享）：
  > "for his discovery of the therapeutic value of malaria inoculation in the treatment of dementia paralytica"（因发现疟疾接种在治疗麻痹性痴呆中的疗效）
- **设计母题**：**以热攻毒**。用一种病（疟疾的高热）压制另一种绝症（神经梅毒）——"热"作为视觉隐喻：温度曲线、退烧的奎宁、帝国余晖下的维也纳诊所。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Julius_Wagner-Jauregg/page.md`（同目录有 metadata.json / images.txt）
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架，16 页同构）

## 二、任务流程 【模板通用，逐步执行】

> 执行框架引用立传模板第三章（第 0-9 步），**第 0/1/2/3 步按 medic 路径执行**：

1. **第 0 步 事实基准**：通读 `medic/presentations/pages/20th_century/Julius_Wagner-Jauregg/page.md` 与同目录 `metadata.json`（冲突以 page.md 为准，裁定见第七节）。
2. **第 1 步 建目录**：`medic/presentations/20th_century/Julius_Wagner-Jauregg/`（含 `images/`；目录名含连字符，Makefile 变量照抄目录名）。
3. **第 2 步 复制 Makefile**：参照 `physicist/presentations/20th_century/Kenneth_G_Wilson/Makefile`，设 `MAIN=Julius_Wagner-Jauregg_zh`、`VIDEO_NAME=Julius_Wagner-Jauregg_zh`。
4. **第 3 步 收集图片**：肖像优先取 `pages/20th_century/Julius_Wagner-Jauregg/images.txt`；404 用 Wikipedia REST API `page/summary` 查 infobox 原图名；再失败用装饰圆占位。插图可用 1934 疟疾输血疗法现场照（Pyrotherapy_1934_image.jpg）与 1883 家族纹章图。
5. **第 4 步 研究领域入库**：本文件第三节（yaml 已在 `MySQL/data/Julius_Wagner-Jauregg.yaml`）。
6. **第 4.5 步 社会关系入库**：本文件第四节。
7. **第 5 步 配色**：本文件第五节。
8. **第 6 步 幻灯片序列**：本文件第六节（15 页）。
9. **第 7-9 步 编译与审查**：`make distclean && make`，0 error、vbox≤10pt、hbox≤50pt；`pdftoppm` 逐页目检；史实与术语审查对照第七、八节。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | malariotherapy | 疟疾接种疗法 | 1917 起，1927 诺奖核心 | 诺奖页 |
| 1 | pyrotherapy | 发热疗法 | 1887 起的毕生主线（丹毒/结核菌素→疟疾） | 核心页 |
| 2 | psychiatry | 精神病学 | 维也纳/格拉茨精神科临床，首位诺奖精神科医生 | 身份页 |
| 3 | neurology | 神经学 | 神经病诊所与麻痹性痴呆（神经梅毒） | 核心页 |

## 四、社会关系梳理 + 入库 【人物专属，与 yaml 完全一致】

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Salomon Stricker | 导师 | 维也纳大学普通与实验病理学研究所导师，1880 博士 |
| advisor-student | Wilhelm Reich | 学生 | infobox 明载学生 |
| advisor-student | Constantin von Economo | 学生 | 1893 年起的学生兼助手 |
| colleague | Maximilian Leidesdorf | 无向 | 1883-1887 在其精神科诊所共事 |
| colleague | Richard von Krafft-Ebing | 无向 | 1889 继其出任格拉茨大学神经精神诊所教席 |
| colleague | Theodor Meynert | 无向 | 1893 继其出任维也纳精神病与神经病诊所 |
| colleague | Sigmund Freud | 无向 | 战后调查中为其作证，保全生涯 |
| spouse | Balbine Frumkin | 无向 | 第一任妻子（犹太裔），1903 离异 |
| spouse | Anna Koch | 无向 | 1899 结婚 |

> 不入库：Robert Koch（结核菌素是其方法材料之一，为事实提及非个人关系）；Alexander Pilcz（受其思想影响的学生，页面为红链且内容涉种族精神病学，仅陷阱表记录）；两子（page.md 未具名）。
> 库内当时无上述对手方记录，均由本 yaml 新建 stub（对手方名用 page.md 正文/infobox 形式：Salomon Stricker / Wilhelm Reich / Constantin von Economo / Maximilian Leidesdorf / Richard von Krafft-Ebing / Theodor Meynert / Sigmund Freud / Balbine Frumkin / Anna Koch）。

## 五、配色方案 【人物专属】

- **气质**：帝国黄昏的金褐 + 精神医学的深紫 + 高热的暗红
- **主色**：维也纳深紫 `#46356B`（精神医学的深邃与帝国余晖）
- **香槟金诺奖色**：`#D4AF37`（badge/诺奖徽记通用）
- **四分类色**：
  - `badgeA` 疟疾疗法 — 暗红 `#8C2F1B`
  - `badgeB` 发热疗法 — 琥珀 `#C77F3B`
  - `badgeC` 精神病学 — 深紫 `#46356B`
  - `badgeD` 争议与反思 — 灰蓝 `#4A5A6A`
- **背景母题**：温度曲线（高热-退烧的双相波形）+ 稀疏大圆，暖冷双色错落呼应"以热攻毒"。

## 六、幻灯片序列（15 页规划） 【人物专属，可微调】

```
00  OpenMedic 项目首页
01  封面 — 首位诺奖精神科医生 / Julius Wagner-Jauregg 1857–1940 + 四色 badge + 右上头像 + 国籍行 Austria
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 Wels/Vienna、教育 Vienna MD 1880、
    导师 Stricker、任职 Vienna/Graz/Steinhof、荣誉 Nobel 1927/Cameron 1935、核心领域）
03  核心贡献概览 — 发热疗法总纲 / 疟疾接种 / 麻痹性痴呆的终结 / 争议的一生
04  韦尔斯与维也纳求学 (1857–1880) — 本名 Julius Wagner、Schottengymnasium、1874-80 学医、
    随 Stricker 于普通与实验病理学研究所、1880 博士论文（心跳加速的起源与功能，法文题）
05  名字与帝国 (1883–1918) — 1883 父封 Ritter von Jauregg 获世袭贵族头衔、
    Julius Wagner Ritter von Jauregg、1918 帝国解体贵族废止后缩为 Wagner-Jauregg
06  精神病理学之路 (1883–1893) — 1883-87 随 Leidesdorf 于精神科诊所、1889 继 Krafft-Ebing
    出任格拉茨神经精神诊所、研究甲状腺肿/呆小症/碘、1893 继 Meynert 任维也纳
    精神病与神经病诊所主任（Economo 为其学生兼助手）
07  发热疗法的起源 (1887–1917) — 1887 研究发热疾病对精神病的影响、丹毒链球菌、
    1890 Koch 发现的结核菌素——效果不佳但不改方向
08  1917：疟疾接种 — 神经梅毒所致麻痹性痴呆（当时绝症）、高热可治梅毒的观察、
    用最温和的间日疟原虫 Plasmodium vivax、后续以奎宁终止疟疾、1917 至 1940s 中叶通行
09  1927 诺贝尔奖 — 首位精神科医生获诺奖、官方理由逐字引用、1931 专著
    《Verhütung und Behandlung der progressiven Paralyse durch Impfmalaria》
10  疗法的代价 — 约 15% 患者死亡、危险性使其今日弃用——伦理与疗效的张力必须呈现
11  战后调查与 Freud — 对"装病"士兵施以极端电休克致大量死亡、德国政府刑事调查、
    Sigmund Freud 出面干预保全其生涯
12  污点与反思 — 主张对精神病人与罪犯强制绝育（1935 奥地利人类学会表态）、
    奥地利种族再生与遗传联盟主席、1938 德奥合并后申请入党因第一任妻子犹太裔被拒
    （去纳粹化委员会裁定 "on grounds of race"）——按 page.md 平衡呈现、不渲染不回避
13  退休岁月与逝世 — 1928 退休后发表近 80 篇论文、1935 Cameron Prize、
    1940-09-27 卒于维也纳（page.md 口径：时属 Nazi Germany）
14  遗产 — 麻痹性痴呆成为医学史上第一种被有效治疗的精神性疾病、
    疗法被青霉素取代的历史坐标、奥地利多处学校道路医院以其命名、结尾
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 获奖理由 | 官方逐字 "for his discovery of the therapeutic value of malaria inoculation in the treatment of dementia paralytica"；长句须完整引用，勿截断 |
| 首位 | 是**首位获诺贝尔生理学或医学奖的精神科医生**——"首位精神科诺奖得主"口径以此为准 |
| 独享 | 1927 无共享者 |
| 名字演变 ★ | Julius Wagner → 1883 贵族化 Wagner von Jauregg（Ritter）→ 1918 帝国解体缩为 Wagner-Jauregg——三个阶段勿混用；幻灯片标题统一用最终形式 |
| 死亡地口径 | 1940-09-27 卒于维也纳，page.md 标注时属 Nazi Germany——照 page.md 口径书写，不额外引申 |
| 敏感内容呈现 ★ | 电休克致死士兵+Freud 作证、强制绝育主张、种族卫生思想、1938 入党申请被拒（因犹太裔前妻）——全部为 page.md 明载，**须平衡客观呈现、不渲染不回避、不加入道德评判性引申** |
|Freud 角色 | Freud 是在 1918 后调查中为其作证/干预——不是师生也不是合作关系，入库 colleague、note 如实 |
| 学生两口径 | Wilhelm Reich 仅 infobox "Notable students" 载；Constantin von Economo 是正文明载"学生兼助手"（1893 起）——两处 note 措辞区分 |
| 疟原虫种 | Plasmodium vivax（间日疟，"least aggressive parasite"）+ 奎宁终止——物种与流程勿错 |
| 结核菌素归属 | 1890 由 Robert Koch 发现——page.md 为事实提及，不建关系 |
| 退休后产量 | 1928 退休、 retirement 期间发表近 80 篇论文、健康状况良好至 83 岁去世——"高龄高产"是正面叙事锚点 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险 |
|------|------|------|
| malariotherapy | 疟疾疗法 | 页面 Known for 用词 |
| pyrotherapy | 发热疗法 | 总纲概念，含疟疾疗法 |
| dementia paralytica | 麻痹性痴呆 | = general paresis of the insane，神经梅毒晚期 |
| neurosyphilis | 神经梅毒 | 病因，勿与普通梅毒混写 |
| Plasmodium vivax | 间日疟原虫 | "least aggressive"（最温和株）是选种理由 |
| quinine | 奎宁 | 终止疟疾的解药，疗法可行性的前提 |
| Ritter von Jauregg | 骑士封号 | 1883 贵族头衔，1918 废止 |
| eugenics / racial hygiene | 优生学/种族卫生 | 争议内容，措辞须中立客观 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Empire Collapse**（manifest 预分配）
- **风格**：帝国黄昏 / 恢弘悲怆 / 史诗反思
- **匹配理由**：其一生横跨奥匈帝国的鼎盛与崩塌——名字从贵族头衔到平民化的变迁正是帝国的缩影；Empire Collapse 的厚重悲剧感匹配"荣誉（诺奖）与污点（绝育主张、纳粹同情）并存"的复杂史诗。
- **本地路径**：`music_audio/inspiring-electronic/12-NTuSqFy4Stc-Cinematic Dramatic Epic Drone Orchestra Film by Cold Cinema [No Copyright Music] ⧸ Empire Collapse.wav` → 复制为 `presentations/20th_century/Julius_Wagner-Jauregg/Empire_Collapse.wav`
- **时长对齐**：ffmpeg `-shortest` 自动对齐（参照 Makefile video 目标）。

> **开始执行。每写一页就 make，看到溢出就修；争议内容务必按 page.md 平衡呈现。**
