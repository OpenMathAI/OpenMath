# 和平奖得主立传提示词（OpenPeace：Betty Williams）

> **本文件是 OpenPeace 的「诺贝尔和平奖得主立传提示词」**，以 Betty Williams（1976 诺贝尔和平奖，北爱尔兰和平运动）为实例。
> 结构对齐标杆 `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md`（0–11 节骨架），按 OpenPeace 立传执行。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMathAI 其他人物侧共享 GitHub）。
- **模板来源**：综合数学家/物理学家侧标杆（Kenneth G. Wilson 提示词 + tex 结构）与和平奖侧批次经验。
- **本实例**：Betty Williams（伊丽莎白·威廉斯，本名 Elizabeth Smyth，贝蒂·威廉斯）。
- **设计哲学**：和平活动家立传必须有「身份信息页」（Identity / Bio 速览页），且强调「和平事业」的结构化表达——这两点构成骨架，务必保留。

---

## 二、背景信息 【人物专属】

- **目标人物**：Betty Williams（1943-05-22 ~ 2020-03-17，享年 76 岁，北爱尔兰贝尔法斯特生、贝尔法斯特卒）
- **官方获奖理由（1976，与 Mairead Corrigan 共享）**：
  > "for the courageous efforts in founding a movement to put an end to the violent conflict in Northern Ireland."
  > （中译照抄名录：表彰她们为发起终止北爱尔兰暴力冲突运动所表现出的勇气）
- **气质关键词**：**草根和平运动的点燃者、和平人民社区的共同创始人、儿童与跨信仰理解的终身倡导者**
- **设计母题**：**游行的人潮（the march）**。两周之内从 6,000 个签名到 10,000 人、再到 20,000 人走上贝尔法斯特街头——以「行进的队伍与签名卷轴」作为视觉母题，呼应其从个人悲悯到万人运动的组织力。
- **本地 Wikipedia**：`/Users/ericksun/workspace/codebuddy/OpenMathAI/peace/presentations/pages/20th_century/Betty_Williams_Nobel_laureate/page.md`
- **参考模板**：
  - 立传成品参照：OpenMathAI 各侧 15–16 页 Beamer（封面 `\input` 项目首页）
  - 项目封面模板：OpenPeace 侧共享 `cover/` 目录

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准（已按 page.md 核对）【人物专属】

- 生卒：1943-05-22 生于北爱尔兰贝尔法斯特；2020-03-17（圣帕特里克节）卒于贝尔法斯特，享年 76 岁
- 本名：Elizabeth Smyth；infobox 载夫家姓 Williams
- 家庭：父为屠夫（新教徒）、母为家庭主妇（天主教徒）——罕见的跨教派家庭，她自述由此获得宗教宽容与开阔视野
- 子女：2 人
- 教育：贝尔法斯特 St. Teresa Primary School；中学 St Dominic's Grammar School for Girls；毕业后任办公室接待员
- 任职/身份：Global Children's Foundation 主持人；World Centre of Compassion for Children International 主席；华盛顿 Institute for Asian Democracy 主席；Nobel Laureate Summit 创始成员（2000 年起每年举行）
- 关键荣誉：诺贝尔和平奖（1976 年奖，1977 领奖，与 Mairead Corrigan 均分奖金）；People's Peace Prize of Norway（1976）；Golden Plate Award（1977）；Schweitzer Medallion for Courage；Martin Luther King, Jr. Award；Eleanor Roosevelt Award（1984）；Rotary International "Paul Harris Fellowship"（1995）；Together for Peace Building Award（1995）
- 核心事业清单：
  1. 1976-08-10 目击 Andersonstown 事件三名儿童罹难，两日内征集 6,000 个和平请愿签名
  2. 与 Mairead Corrigan 共创 Women for Peace，与 Ciaran McKeown 一道发展为 Community of Peace People
  3. 组织葬礼和平游行（10,000 名新教与天主教妇女）与 Ormeau Park 游行（20,000 人）
  4. 发表《和平人民第一宣言》（Declaration of the Peace People）
  5. 1978 年脱离 Peace People，转向世界其他地区的和平事业
  6. 2006 年与其他五位和平奖女性得主共创 Nobel Women's Initiative
- 关键时间线（14 节点）：1943 生于贝尔法斯特 → 完成学业后任接待员 → 1970 年代初加入新教牧师领导的反暴力运动 → 1976-08-10 Andersonstown 事件 → 两日 6,000 签名 → 创 Women for Peace → 10,000 人葬礼游行遭 IRA 干扰 → 20,000 人 Ormeau Park 游行 → Peace People 成立与宣言 → 1976（1977 领）诺贝尔和平奖 → 1978 与 Peace People 分道、奖金自留受批评 → 1981 与 Ralph Williams 离异 → 1982-12 与 James Perkins 结婚、居美国佛罗里达 → 2004 回北爱尔兰定居 → 2006 共创 Nobel Women's Initiative → 2020-03-17 卒于贝尔法斯特

### 第 1 步：建立目录 【模板通用】

- 在 `peace/presentations/20th_century/` 下建 `Betty_Williams_Nobel_laureate/` 与 `images/`

### 第 2 步：复制 Makefile 【模板通用】

- 复制同项目近邻成品 Makefile，设 `MAIN=Betty_Williams_Nobel_laureate_zh`、`VIDEO_NAME` 同名

### 第 3 步：收集图片 【人物专属】

- page.md 载三幅可核肖像：1978 年联邦档案照（Betty_Williams_W_134_Nr_105602v_Bild_1）、领奖时期照（Betty_Williams.jpg）、2009 Women's World Awards 照；按 images.txt/REST API 下载，404 则用装饰圆占位

### 第 4 步：和平事业领域梳理 + 入库

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | grassroots peace movement | 草根和平运动 | Peace People 运动发起人 | 核心页 |
| 1 | nonviolence | 非暴力 | 拒绝炸弹与子弹的一切暴力手段 | 宣言页 |
| 2 | peace education | 和平教育 | 讲授和平、教育、跨文化与跨信仰理解 | 晚年页 |
| 3 | children's rights | 儿童权利 | Global Children's Foundation 等儿童事业 | 晚年页 |
| 4 | women's rights | 女性权利 | 2006 Nobel Women's Initiative 共同创始人 | 传承页 |

### 第 4.5 步：社会关系梳理 + 入库（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Mairead Corrigan | 无向 | 1976 诺贝尔和平奖共同得主，Peace People 联合创始人 |
| colleague | Ciaran McKeown | 无向 | 共同将 Women for Peace 发展为 Community of Peace People |
| spouse | Ralph Williams | 无向 | 第一任丈夫，1981 年婚姻解除 |
| spouse | James Perkins | 无向 | 1982 年 12 月结婚，定居美国佛罗里达 |
| colleague | Shirin Ebadi | 无向 | 2006 Nobel Women's Initiative 共同创始人 |
| colleague | Wangari Maathai | 无向 | 2006 Nobel Women's Initiative 共同创始人 |
| colleague | Jody Williams | 无向 | 2006 Nobel Women's Initiative 共同创始人 |
| colleague | Rigoberta Menchú | 无向 | 2006 Nobel Women's Initiative 共同创始人 |

### 第 5 步：设计配色方案 【人物专属，勿改主色】

- **主色**：`#1B4D6B`（深海军蓝——运动的沉静与坚毅）
- **辅色**：诺奖香槟金 `C9A227` + 四分类色：badgeA 和平运动 `#2E7D6B`；badgeB 非暴力 `#8C6A2F`；badgeC 儿童事业 `#7A3E48`；badgeD 女性倡议 `#3E5C7A`
- **背景母题**：行进人潮的抽象弧线与签名卷轴

### 5.1 格式硬要求 【模板通用，★ 必须满足】

1. 封面有肖像（或装饰圆占位）+ 姓名小字注；顶部/底部明示国籍（United Kingdom）。
2. 必须有身份信息页：左肖像 + 右信息网格（生卒、本名、家庭、教育、任职、荣誉、核心领域）。
3. 结尾页品牌统一写 `OpenMathAI`；引号用半角 `" "`。

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00 OpenPeace 项目首页（\input cover 共享页）
01 封面 — 1976 诺贝尔和平奖 / Betty Williams 1943–2020 + badge + 国籍行
02 身份信息页（★ 必做）
03 核心贡献概览 — 请愿 / 游行 / Peace People / 宣言 / 后半程事业
04 早年：跨教派家庭 (1943–1976) — 屠夫父亲与天主教母亲、接待员、反暴力运动
05 十天改写历史：1976-08-10 Andersonstown 事件 — 目击三名儿童罹难、6,000 签名
06 从 Women for Peace 到 Peace People — 与 Corrigan、McKeown 三人核心
07 万人游行 — 10,000 人葬礼游行 / 20,000 人 Ormeau Park
08 和平人民第一宣言 — 八条宣言逐条摘录（page.md 明载原文）
09 诺贝尔和平奖 (1976) — 共享理由、1977 领奖、领奖演说要点
10 奖金争议与分道 (1978) — 奖金自留受批评、与 Corrigan 1976 后无往来、脱离运动
11 全球和平事业 — Global Children's Foundation / World Centre of Compassion / 亚洲民主研究所
12 其他荣誉 — People's Peace Prize 1976 / Golden Plate 1977 / Eleanor Roosevelt 1984 / Paul Harris 1995
13 Nobel Women's Initiative (2006) — 六位和平奖女性得主共同创始
14 晚年与遗产 — 2004 回北爱尔兰、2000 年起 Nobel Laureate Summit、2020 卒
15 结尾
```

### 第 7–8 步：Beamer 编写 + 布局检查 【模板通用】

- 每页 `\newcommand{\xxxslide}` 定义；写完即 make，`pdftoppm` 截图查溢出；修复优先级：删 `\plainbar` → 缩 inner sep → 缩字号 → 减行距。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Betty Williams 专属陷阱**：

| 陷阱 | 说明 |
|------|------|
| 获奖年份口径 | 1976 年奖、1977 年颁发；正文统一写「1976 诺贝尔和平奖（1977 领奖）」，勿混用 |
| 共享与分工 | 与 Corrigan 共享同一理由句；奖金均分；Williams 自留奖金曾受批评——按 page.md 客观记录，禁评价 |
| 两人关系 | page.md 明载 1976 年后两人再无往来；勿写成"终身挚友" |
| 宗教背景 | 父新教、母天主教，是跨教派家庭——这铺垫其宗教宽容；勿写成"虔诚的天主教徒" |
| Andersonstown 事件 | 司机 Danny Lennon（IRA 成员）先被士兵击毙，车辆失控碾压 Maguire 三名儿童；三名儿童之母 Anne Maguire 1980 年 1 月自杀——全部按 page.md 客观记录 |
| 游行人数 | 葬礼游行 10,000 人（遭 IRA 干扰）、Ormeau Park 20,000 人；勿混用或夸大 |
| 组织名称演变 | Women for Peace →（McKeown 加入后）Community of Peace People；宣言题为 First Declaration of the Peace People |
| 政治言论红线 | 晚年演讲涉及战争伤亡等政治敏感内容一律不进入引文框、不作评价；引文框只用《和平人民第一宣言》与 1977 领奖演说中 page.md 明载原文 |
| 与 Jody Williams 区分 | 本篇主角 Betty Williams（1943–2020）≠ 1997 年得主 Jody Williams；同现于 2006 Initiative 页时须注全名 |
| 流行文化 | Nickelback《If Everyone Cared》MV 与法语歌《Deux Femmes à Dublin》有载，可作花絮小字，不作主页面 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| the Troubles | 北爱尔兰问题（动荡年代） | 历史专有名词，直译「麻烦」错误 |
| Community of Peace People | 和平人民社区 | 组织名，勿译「和平人民公社」 |
| prisoners of conscience | 良心犯 | 本篇不涉及，勿混入 |
| petition | 和平请愿 | 两日 6,000 签名 |
| peace march | 和平游行 | 区分两场人数 |
| cross-conflict family | 跨教派家庭 | 父新教/母天主教 |
| Nobel Women's Initiative | 诺贝尔女性倡议 | 2006 年六人共创 |
| co-recipient | 共同得主 | 与 Corrigan 共享 |
| People's Peace Prize of Norway | 挪威人民和平奖 | 1976，区别于诺贝尔奖 |
| humanitarian | 人道主义者 | infobox 职业之一 |

---

## 四、背景音乐 ✅ 【人物专属，manifest 预分配，勿改】

- **选定曲目**: **Falling Apart** — Michael FK & Andy Leech
- **匹配理由**: 「撕裂与重建」贴合其叙事——1976 年那个下午的死亡撕裂了贝尔法斯特，而两周内两场万人游行把悲恸改写为运动；曲名的破碎感对应事件的创痛，推进感对应签名与游行的集结。
- **本地路径**: `music_audio/inspiring-electronic/03-qtNSLNUd1VE-Michael FK & Andy Leech - Falling Apart.wav` → 复制为 `presentations/20th_century/Betty_Williams_Nobel_laureate/Falling_Apart.wav`

---

## 五、关键参考文件清单

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Betty_Williams_Nobel_laureate/page.md` | 本地 Wikipedia 正文（事实唯一来源） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 结构标杆 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 获奖理由中译（照抄，禁改写） |
| `MySQL/data/Betty_Williams_Nobel_laureate.yaml` | 入库 yaml（第 4/4.5 步落地） |
| `MySQL/seed_person.py` | 入库引擎（幂等） |

> **开始执行。每完成一步汇报。最重要的事：每写一页就 make，看到溢出就修。**
