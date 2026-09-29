# 医学家立传提示词（Max Theiler）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1951 年得主 Max Theiler（马克斯·泰累尔）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Max_Theiler/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Max Theiler（1899-01-30 生于比勒陀利亚，南非共和国 ~ 1972-08-11 逝于美国康涅狄格州纽黑文，享年 73 岁）
- **气质关键词**：**黄热病疫苗的缔造者、17D 减毒株之父、首位非洲出生的诺奖得主**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1951 条目）：
  > "for his discoveries concerning yellow fever and how to combat it"（因其关于黄热病及其防治方法的发现）
- **设计母题**：**减毒的一百代（a hundred passages to attenuation）**——Asibi 毒株在鸡胚中传代 100+ 次终成安全的 17D 疫苗；用「一条病毒谱系沿时间轴渐次褪去毒性色而点亮免疫金色」的渐变图形作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Max_Theiler/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；**第 0/1/2/3 步按 medic 路径执行**：页面已在 `medic/presentations/pages/20th_century/Max_Theiler/`（1951 年像，见 images.txt）。Makefile 复制后设 `MAIN=Max_Theiler_zh`、`VIDEO_NAME=Max_Theiler_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

**Theiler 的研究领域（按 rank 排序，已入库 person_field）**：

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | virology | 病毒学 | 黄热病毒与 17D 疫苗，1951 诺奖核心 | 封面、核心页 |
| 1 | vaccinology | 疫苗学 | 17D 减毒活疫苗与小鼠保护试验 | 核心页 |
| 2 | tropical medicine | 热带医学 | 伦敦热带医学文凭（1922）；阿米巴痢疾研究 | 早年页 |
| 3 | epidemiology | 流行病学 | 耶鲁流行病学与公共卫生教授（1964–1967） | 晚期页 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 正文/infobox 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| parent-child | Arnold Theiler | 对方 → 父 | 兽医细菌学家 |
| colleague | Andrew Sellards | 无向 | 哈佛热带医学院时期的上司；成为其助手后开始黄热病研究；1926 共同否定 Noguchi 假说、1928 共同证明非洲/南美毒株免疫学同一 |
| controversy | Hideyo Noguchi | 无向 | 1926 与 Sellards 共同推翻其「黄热病由钩端螺旋体 Leptospira icteroides 细菌引起」假说（1928 病毒病因确认） |
| colleague | Hugh Smith | 无向 | 洛克菲勒团队同事：共同经 100+ 次鸡胚传代获得 17D 减毒株（1937） |
| colleague | W. G. Downs | 无向 | 合著《The Arthropod-Borne Viruses of Vertebrates》（1973，洛克菲勒基金会病毒项目 1951–1970 总结） |
| spouse | Lillian Graham | 无向 | 1928 结婚（1895–1977），育一女 |

**不入库但提示词可叙述**：Adrian Stokes（恒河猴诱导黄热病实验，前置于其工作）；Ernest Goodpasture（鸡胚培养技术先驱，17D 路线的方法学渊源——仅叙述不建边）；女儿（仅具数量）。

## 五、配色方案 【人物专属】

- **气质**：非洲大地与热带医学、疫苗金与减毒的暗红渐变
- **主色**：`#A34700`（疫苗赭金——黄热病的警示色转为免疫的暖金）+ 香槟金诺奖色
- **badge 四分类色**：
  - `badge17D` 17D 疫苗 — 赭金 `#A34700`
  - `badgeVirus` 病毒学 — 深红 `#8C1F28`
  - `badgeTrop` 热带医学 — 苔绿 `#175E54`
  - `badgeRock` 洛克菲勒岁月 — 深蓝 `#16324F`
- **背景母题**：病毒谱系沿时间轴的毒性褪色/免疫点亮的渐变条带。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 黄热病疫苗的缔造者 / Max Theiler 1899–1972 + 四色 badge + 右上头像 + 国籍行（South Africa）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、比勒陀利亚出身、开普敦大学医学 1918、
    伦敦热带医学文凭 1922、哈佛/洛克菲勒、耶鲁 1964–1967、诺奖 1951、核心领域）
03  核心贡献概览 — 17D 疫苗 / 小鼠保护试验 / 病因修正 / 泰累尔鼠脑脊髓炎病毒
04  比勒陀利亚与家学 (1899–1922) — 父 Arnold 为兽医细菌学家；罗德斯学院→开普敦医学
05  伦敦与热带医学 (1918–1922) — St Thomas's / 国王学院 / 热带医学与卫生学院；1922 文凭
06  哈佛岁月 (1922–1930) — 阿米巴痢疾与鼠咬热疫苗尝试；成为 Sellards 助手后转向黄热病
07  推翻 Noguchi 假说 (1926)（争议页）— 与 Sellards 共同否定钩端螺旋体病因说
08  病毒确认与免疫同一 (1928) — 非洲/南美毒株免疫学同一；本人感染黄热病幸存获免疫（叙事高点）
09  洛克菲勒与小鼠传代 (1930–1937) — 病毒实验室主任；小鼠传代减毒→恒河猴免疫
10  小鼠保护试验 — 疫苗效力检验法，战后之前沿用
11  17D 的诞生 (1937)（核心贡献页）— Asibi 毒株鸡胚 100+ 传代（Goodpasture 技术）；与 Hugh Smith 获减毒株
12  2800 万剂与诺奖 (1940–1951) — 洛克菲勒量产终结黄热病大流行；1951 独得诺奖、首位非洲出生得主
13  泰累尔鼠脑脊髓炎病毒 (1937) — 小鼠瘫痪病原；今为多发性硬化标准模型
14  遗产与结尾 — 耶鲁岁月（1964–1967）、诺奖演讲（1951-12-11）+ 结尾页
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 1951 独得 | 单独得主，无 co-honored；理由句 "for his discoveries concerning yellow fever and how to combat it"（黄热病**及其防治**），勿写成「发现黄热病病毒」（病毒病因 1928 年才确认且非其独功） |
| 首个非洲出生诺奖 | "becoming the first African-born Nobel laureate"——「非洲出生」口径勿扩大为「非洲裔」 |
| 国籍口径 | yaml/总表按 manifest **South Africa**；frontmatter United States+South Africa 双值，正文 South African-American——叙述可双提，yaml 只填 South Africa |
| 生卒双值 | frontmatter 有 1899-00-00/1972-00-00 噪声——以正文 **1899-01-30 ~ 1972-08-11** 为准 |
| Noguchi 争议的表述 | 推翻的是其**病因假说**（细菌说），否定其学术主张而非否定其人格；1928 年黄热病被确认为病毒所致——时间线：1926 否定→1928 病毒确认 |
| 感染叙事 | Theiler 在研究中**感染黄热病但幸存并获得免疫**——本人成为活证据，叙事高点但勿夸大为「以身为试验」 |
| 17D 的团队属性 | 与 **Hugh Smith** 共同经 100+ 次鸡胚传代获得减毒株；鸡胚技术承 Goodpasture——「团队成果」口径，个人独享诺奖的张力可在提示词中点明 |
| 2800 万剂 | 1940–1947 年洛克菲勒基金会生产逾 2800 万剂，「finally ended yellow fever as a major disease」——数字与年份勿混 |
| 泰累尔病毒 | Theiler's murine encephalomyelitis virus（1937 发现）今为**多发性硬化标准模型**——与黄热病是两条独立成果线 |
| 职务时间线 | 洛克菲勒基金会病毒实验室主任（1930 起）→ 耶鲁流行病学与公共卫生教授（1964–1967）——退休后教职勿提前 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| 17D | 17D 减毒株 | Asibi 毒株 100+ 代鸡胚传代产物 |
| yellow fever | 黄热病 | 诺奖理由核心词 |
| attenuated strain | 减毒株 | 疫苗学核心概念 |
| mouse protection test | 小鼠保护试验 | 其设计的效力检验法 |
| Leptospira icteroides | 黄疸出血型钩端螺旋体 | Noguchi 的（被推翻的）病因假说 |
| rhesus macaque | 恒河猴 | 实验动物模型 |
| Asibi strain | Asibi 毒株 | 西非强毒株起点 |
| murine encephalomyelitis virus | 鼠脑脊髓炎病毒 | 多发性硬化模型 |
| chick embryo | 鸡胚 | 传代培养载体（Goodpasture 技术） |
| tropical medicine | 热带医学 | 1922 伦敦文凭 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Savage**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：黄热病是热带的「野蛮」疫病——夺走包括研究者在内的无数生命；Theiler 以一百代传代的耐心驯服了它；Savage 的原始张力对应病毒与人类之战，而疫苗的成功则是驯化野性的终章。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Max_Theiler/Savage.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
