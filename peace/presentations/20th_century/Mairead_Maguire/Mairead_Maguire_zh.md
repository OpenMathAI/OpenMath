# 和平奖得主立传提示词（OpenPeace：Mairead Corrigan）

> **本文件是 OpenPeace 的「诺贝尔和平奖得主立传提示词」**，以 Mairead Corrigan（Mairead Maguire，1976 诺贝尔和平奖，北爱尔兰和平运动）为实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架），按 OpenPeace 立传执行。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMathAI 其他人物侧共享 GitHub）。
- **模板来源**：综合数学家/物理学家侧标杆（Kenneth G. Wilson 提示词 + tex 结构）与和平奖侧批次经验。
- **本实例**：Mairead Maguire（本名 Mairead Corrigan，又称 Mairead Corrigan Maguire，梅里德·科里根）。
- **设计哲学**：和平活动家立传必须有「身份信息页」（Identity / Bio 速览页），且强调「和平事业」的结构化表达——这两点构成骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标人物**：Mairead Corrigan（1944-01-27 生于北爱尔兰贝尔法斯特，在世）
- **官方获奖理由（1976，与 Betty Williams 共享）**：
  > "for the courageous efforts in founding a movement to put an end to the violent conflict in Northern Ireland."
  > （中译照抄名录：表彰她们为发起终止北爱尔兰暴力冲突运动所表现出的勇气）
- **气质关键词**：**从丧亲之痛走向非暴力的践行者、和平人民社区的终身守护者、全球范围的和平与人权倡导者**
- **设计母题**：**烛光与再教育（the candle & re-education）**。她确信结束暴力最有效的方式不是暴力而是「再教育」——以「烛火照亮课本」的意象呼应其非暴力哲学与 Peace by Peace 报纸、探监班车等日常化和平建设。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Mairead_Maguire/page.md`
- **参考模板**：
  - 立传成品参照：OpenMathAI 各侧 15–16 页 Beamer（封面 `\input` 项目首页）
  - 项目封面模板：OpenPeace 侧共享 `cover/` 目录

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准（已按 page.md 核对）【人物专属】

- 生卒：1944-01-27 生于贝尔法斯特（天主教社区），在世
- 家庭：Andrew 与 Margaret Corrigan 的第二个孩子，八姊妹兄弟中行二；胞姊 Anne Maguire 的三名子女 1976-08-10 死于 Finaghy Road North 车祸；Anne 1980 年 1 月自杀；1981 年 9 月嫁与亡姊遗孀夫 Jackie Maguire，育三继子女与两子 John Francis（1982）、Luke（1984）
- 教育：St. Vincent's Primary School（14 岁因家贫辍学）；Miss Gordon's Commercial College 商科一年；16 岁任工厂记账员；21 岁起任健力士酒厂秘书至 1976-12；后获都柏林三一学院爱尔兰普世神学研究院学位；infobox educated_at 载 Trinity College Dublin
- 早年志愿：长期参加圣母军（Legion of Mary），晚间与周末服务儿童、探望 Long Kesh 监狱囚犯
- 任职/身份：Peace People 荣誉主席（延续至今）；1981 年共同创立司法行政委员会（Committee on the Administration of Justice）；Consistent Life Ethic 成员；国际和平理事会理事
- 关键荣誉：诺贝尔和平奖（1976 年奖，1977 领，时年 32 岁——2014 年 Malala 之前最年轻和平奖得主）；挪威人民和平奖（1976）；Carl von Ossietzky Medal（1976）；耶鲁大学荣誉法学博士（1977）；Golden Plate Award（1977）；College of New Rochelle 荣誉学位（1978）；Pacem in Terris Award（1990）；Nuclear Age Peace Foundation 杰出和平领袖奖（1992）；Regis University 荣誉学位（1998）；罗德岛大学荣誉学位（2000）；Albert Schweitzer 国际大学科学与和平金奖（2006）
- 核心事业清单：
  1. 1976 年与 Betty Williams 共创 Women for Peace（后与 Ciaran McKeown 一道成为 Community of Peace People）
  2. 推动出版双周报 Peace by Peace、为囚犯家庭提供探监班车
  3. 主张以「再教育」而非暴力终结冲突
  4. 1981 年共同创立 CAJ（无宗派人权组织）
  5. 全球政治犯倡导（1993 年与六位得主试图进入缅甸声援昂山素季等）
  6. 2006 年与其他五位和平奖女性得主共创 Nobel Women's Initiative；2010 年出版《The Vision of Peace》
- 关键时间线（15 节点）：1944 生于贝尔法斯特 → 14 岁辍学打工 → 商科一年 → 16 岁记账员 → 21 岁入健力士任秘书 → 圣母军志愿探监 → 1976-08-10 外甥三子女罹难、加入 Williams 的请愿游行 → Women for Peace → Peace People 成立 → 1976（1977 领）诺贝尔和平奖 → 1980-01 姊 Anne 自杀 → 1981 嫁 Jackie Maguire、共创 CAJ → 此后数十年全球和平与人权倡导（缅甸/中东等） → 2006 共创 Nobel Women's Initiative → 2010 出版《The Vision of Peace》

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下建 `Mairead_Maguire/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同项目近邻成品 Makefile，设 `MAIN=Mairead_Maguire_zh`、`VIDEO_NAME` 同名

### 第 3 步：收集图片 【人物专属】

- page.md 载 2009 年 Free Gaza Movement 之行合影（Mairead_Corrigan_reunited_with_her_husband.jpg 为 1981 与丈夫合影）等；按 images.txt/REST API 下载，404 则用装饰圆占位

### 第 4 步：和平事业领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | nonviolence | 非暴力 | 视暴力为后天习得之病的和平主义哲学 | 哲学页 |
| 1 | grassroots peace movement | 草根和平运动 | Peace People 联合创始人、荣誉主席 | 核心页 |
| 2 | human rights | 人权 | CAJ 共创、政治囚犯倡导 | 倡导页 |
| 3 | reconciliation | 和解 | 普世神学、跨教会跨信仰组织工作 | 传承页 |
| 4 | women's rights | 女性权利 | 2006 Nobel Women's Initiative 共同创始人 | 传承页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Betty Williams | 无向 | 1976 诺贝尔和平奖共同得主，Peace People 联合创始人 |
| colleague | Ciaran McKeown | 无向 | 共同将 Women for Peace 发展为 Community of Peace People |
| spouse | Jackie Maguire | 无向 | 1981 年结婚，亡姊 Anne 之遗孀夫 |
| colleague | Shirin Ebadi | 无向 | 2006 Nobel Women's Initiative 共同创始人 |
| colleague | Wangari Maathai | 无向 | 2006 Nobel Women's Initiative 共同创始人 |
| colleague | Jody Williams | 无向 | 2006 Nobel Women's Initiative 共同创始人 |
| colleague | Rigoberta Menchú | 无向 | 2006 Nobel Women's Initiative 共同创始人 |
| colleague | Aung San Suu Kyi | 无向 | 1993 与六位和平奖得主赴缅边境声援其获释 |
| colleague | Adolfo Pérez Esquivel | 无向 | 1999 同访巴格达呼吁解除对伊制裁（page.md 称 colleague） |
| colleague | Desmond Tutu | 无向 | 与其共同发表支持 Chelsea Manning 的公开信 |
| influence | Dorothy Day | 对方→本人 | 自述早年天主教精神偶像之一 |

### 第 5 步：设计配色方案 【人物专属，勿改主色】

- **主色**：`#46356B`（深紫罗兰——坚忍与信念）
- **辅色**：诺奖香槟金 `C9A227` + 四分类色：badgeA 非暴力 `#5B4A8A`；badgeB 和平运动 `#2E7D6B`；badgeC 人权倡导 `#8C6A2F`；badgeD 女性倡议 `#7A3E48`
- **背景母题**：烛光与书页

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. 封面有肖像（或装饰圆占位）+ 姓名小字注；顶部/底部明示国籍（United Kingdom）。
2. 必须有身份信息页：左肖像 + 右信息网格（生卒、本名、家庭、教育、任职、荣誉、核心领域）。
3. 结尾页品牌统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00 OpenPeace 项目首页（\input cover 共享页）
01 封面 — 1976 诺贝尔和平奖 / Mairead Corrigan 1944– + badge + 国籍行
02 身份信息页（★ 必做）
03 核心贡献概览 — 请愿 / Peace People / 再教育 / 人权 / 全球倡导
04 早年：贝尔法斯特天主教家庭 (1944–1976) — 八子女行二、辍学、记账员、健力士秘书、圣母军探监
05 1976-08-10：Finaghy Road North 之殇 — 外甥三子女罹难、加入和平请愿
06 从 Women for Peace 到 Peace People — 与 Williams、McKeown 三人核心
07 万人运动与再教育理念 — 游行、Peace by Peace 报纸、探监班车
08 诺贝尔和平奖 (1976) — 共享理由、32 岁最年轻得主（至 2014 Malala 前）
09 个人的重负与新的家 — Anne 之死、1981 嫁 Jackie Maguire、共创 CAJ
10 非暴力哲学 — Gandhi 式非暴力、呼吁废除军队、The Vision of Peace
11 全球政治囚犯倡导 — 1993 缅甸之行等
12 2006 Nobel Women's Initiative — 六位和平奖女性共同创始
13 荣誉与认可 — Pacem in Terris 1990 / 荣誉学位 / Ossietzky Medal 1976
14 晚年与遗产 — Peace People 荣誉主席至今
15 结尾
```

### 第 7–8 步：Beamer 编写 + 布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}` 定义；写完即 make，`pdftoppm` 截图查溢出；修复优先级：删 `\plainbar` → 缩 inner sep → 缩字号 → 减行距。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Mairead Corrigan 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 姓名演变 | 本名 Mairead Corrigan，1981 婚后通称 Mairead Corrigan Maguire / Mairead Maguire；本地目录与 wiki 标题为 Mairead Maguire，yaml name_en 用 manifest 规范名 Mairead Corrigan——三形式勿混写 |
| 获奖年份口径 | 1976 年奖、1977 年颁发；统一写「1976 诺贝尔和平奖（1977 领奖）」 |
| 与 Williams 分工 | 运动由 Williams 先发起请愿、Corrigan 加入后成为「共同领袖」；两人 1976 年奖共同得主、奖金均分——按 page.md 客观记录，禁比较高低 |
| 家族悲剧链 | 三名外甥子女之死 → 姊 Anne 自杀（1980-01）→ 嫁亡姊遗孀 Jackie（1981-09）——时间顺序勿倒置 |
| 教育口径 | 14 岁辍学、商科一年、16 岁就业为正文口径；都柏林三一学院学位是后来的爱尔兰普世神学研究院学位，勿写成"早年毕业于三一" |
| 获奖年龄 | 32 岁领奖时为当时最年轻和平奖得主，纪录 2014 年被 Malala Yousafzai 打破——勿漏"至 2014 年"限定 |
| 政治红线 | 晚年关于中东、伊拉克战争、个别国家领导人的言论与争议（含各方批评）只可按 page.md 客观简述、双方并列，禁任何评价性语句；争议性引语一律不进入引文框；引文框只用其非暴力哲学段（Santa Clara University 载）与《和平人民宣言》 |
| 与 Betty Williams 篇区分 | 本篇亮点是「终身坚守」（至今任 Peace People 荣誉主席）；Williams 篇亮点是「发起运动后转向全球」——勿写反 |
| 争议批评 | The Times 记者与 Sinn Féin 人士等对诺奖决定的批评、奖金争议——按 page.md 双方观点客观记录，不入引文框 |
| 职业口径 | infobox 载 peace activist 与 politician（frontmatter）；yaml 主业用 peace activist，politician 作次要职业 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| the Troubles | 北爱尔兰问题 | 历史专有名词 |
| Community of Peace People | 和平人民社区 | 组织名 |
| Peace by Peace | 《Peace by Peace》双周报 | 组织刊物，勿意译 |
| Committee on the Administration of Justice | 司法行政委员会（CAJ） | 1981 共创的人权组织 |
| Pacem in Terris | 《地球上的和平》奖 | 拉丁语，源自约翰二十三世 1963 通谕 |
| Legion of Mary | 圣母军 | 天主教平信徒组织 |
| Irish School of Ecumenics | 爱尔兰普世神学研究院 | 三一学院下属 |
| Consistent Life Ethic | 一贯生命伦理 | 反堕胎/反死刑/反安乐死组织 |
| honorary president | 荣誉主席 | Peace People 现任职务 |
| nonviolence | 非暴力 | 其核心哲学 |

---

## 四、背景音乐 ✅ 【人物专属，manifest 预分配，勿改】

- **选定曲目**: **Mirage** — Notan Nigres
- **匹配理由**: 「海市蜃楼→真实」贴合其叙事——在「永远无解」的贝尔法斯特，她坚信和解可能；曲名的幻影感对应世人对和平的怀疑，而她的余生是对这一幻影的逐条反驳（北爱尔兰、缅甸、全球）。
- **本地路径**: `music_audio/inspiring-electronic/04-5gcb94jhG1I-Notan Nigres - Mirage (Audio).wav` → 复制为 `presentations/20th_century/Mairead_Maguire/Mirage.wav`

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Mairead_Maguire/page.md` | 本地 Wikipedia 正文（事实唯一来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 获奖理由中译（照抄，禁改写） |
| `MySQL/data/Mairead_Maguire.yaml` | 入库 yaml（第 4/4.5 步落地） |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
