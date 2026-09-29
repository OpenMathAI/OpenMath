# 医学家立传提示词（Bernard Katz）

> 本文件是 OpenMedic 项目 20 世纪诺贝尔生理学或医学奖 **1970 年得主 Bernard Katz（伯纳德·卡茨）** 的人物专属立传提示词，供 Beamer 立传 agent 使用。事实基准为本地 Wikipedia 页面 `medic/presentations/pages/20th_century/Bernard_Katz/page.md`，与其冲突时以 page.md 为准。

## 一、背景信息 【人物专属】

- **目标医学家**：Sir Bernard Katz（1911-03-26 生于德国莱比锡 ~ 2003-04-20 逝于英国伦敦，享年 92 岁）
- **气质关键词**：**量子式释放的发现者、突触电信号的解码者、从难民到 UCL 生物物理系主任**
- **诺奖获奖理由**（逐字引自 `medic/nobel_medicine_citations.json` 1970 条目，与 Axelrod、von Euler 三人共享同一理由）：
  > "for their discoveries concerning the humoral transmitters in the nerve terminals and the mechanism for their storage, release and inactivation"（因他们发现神经末梢中的体液递质及其贮存、释放与失活机制）
- **设计母题**：**整数份的释放（quantal release）**——递质总以最小单位的整数倍释放的意象：以等份小包裹逐个释放的图案作背景母题。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Bernard_Katz/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）；项目首页 `medic/presentations/cover/`

## 二、任务流程 【模板通用，逐步执行】

> 引用 `physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md` 第三章；第 0/1/2/3 步按 medic 路径执行：页面已在 `medic/presentations/pages/20th_century/Bernard_Katz/`（肖像见 images.txt）。Makefile 复制后设 `MAIN=Bernard_Katz_zh`、`VIDEO_NAME=Bernard_Katz_zh`。第 4/4.5 步入库已完成，按本文第三、四节核对；第 5 步起按第五至九节执行。

## 三、研究领域梳理 + 入库 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 |
|:--:|------|------|------|
| 0 | neurophysiology | 神经生理学 | 突触传递研究，1970 诺奖核心 |
| 1 | biophysics | 生物物理学 | infobox Fields；UCL 生物物理系主任 1952–1978 |
| 2 | synaptic transmission | 突触传递 | 神经肌肉接头、乙酰胆碱、量子式释放 |
| 3 | electrophysiology | 电生理学 | Goldman–Hodgkin–Katz 通量/电压方程 |

## 四、社会关系梳理 + 入库 【人物专属】

**只收 page.md 明载关系（已入库 person_relation，与 yaml 完全一致）**：

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Archibald Hill | 对方 → 导师 | UCL 导师（1935 起投奔 Hill，PhD 1938）；库内规范名 id=4618 |
| colleague | John Eccles (neurophysiologist) | 无向 | 卡内基奖学金赴悉尼 Kanematsu 研究所随其研究；库内规范名 id=5082 |
| colleague | Paul Fatt | 无向 | 量子式递质释放的共同发现者（诺奖核心发现） |
| colleague | Alan Hodgkin | 无向 | 回英后与其合作（1963 诺奖得主） |
| colleague | Andrew Huxley | 无向 | 回英后与其合作（1963 诺奖得主） |
| spouse | Marguerite Penly Katz | 无向 | 1945 结婚，妻 1999 去世；二子（Jonathan 后任牛津 Public Orator） |
| co-honored | Julius Axelrod | 无向 | 1970 诺贝尔生理学或医学奖三人共享（神经末梢体液递质及贮存释放失活机制） |
| co-honored | Ulf von Euler | 无向 | 1970 诺贝尔生理学或医学奖三人共享（神经末梢体液递质及贮存释放失活机制） |

**不入库但提示词可叙述**：Hill 夫妇（Katz 一家 1946–49 与 Hill 同住 Highgate 顶层的恩情，正文可叙述不建边）；Martin Gildemeister（frontmatter 列为博士导师之一，但 infobox/正文无载——metadata-only 不入库）；Margaret Nash？无。战时皇家澳大利亚空军雷达军官（经历叙述）。

## 五、配色方案 【人物专属】

- **气质**：流亡者的精密、电信号的克制、UCL 的学术厚重
- **主色**：`#2F4F4F`（伦敦板岩灰绿——UCL 生物物理系的沉静）+ 香槟金诺奖色
- **badge 四分类色**：`badgeQuantal` 量子式释放 灰绿 `#2F4F4F`；`badgeGHK` GHK 方程 深蓝 `#1E4E79`；`badgeACh` 乙酰胆碱 青绿 `#0E7C7B`；`badgeRefugee` 莱比锡到伦敦 玫瑰 `#9E2B25`
- **背景母题**：等份小包裹逐个释放的图案，呼应「整数份的释放」。

## 六、幻灯片序列 【人物专属，15 页规划】

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 量子式释放的发现者 / Bernard Katz 1911–2003 + 四色 badge + 右上头像 + 国籍行（United Kingdom）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒 1911-03-26 莱比锡 ~ 2003-04-20 伦敦、
    莱比锡大学医学 1934、UCL PhD 1938、UCL 生物物理系主任 1952–1978、诺奖 1970）
03  核心贡献概览 — 量子式释放 / 神经肌肉接头 / GHK 方程 / 乙酰胆碱酶循环
04  莱比锡少年 (1911–1935) — 俄国犹太裔家庭、Albert 文理中学、莱比锡大学医学 1934 毕业、
    1935 年 2 月逃离纳粹德国
05  UCL 与 Hill 门下 (1935–1939) — 初投 A. V. Hill、PhD 1938、
    卡内基奖学金赴悉尼
06  悉尼岁月 (1938–1942) — Kanematsu 研究所随 Eccles；1941 入籍英国、
    1942 加入皇家澳大利亚空军任太平洋战区雷达军官
07  重返 UCL (1946–1952) — Hill 邀回任助理主任（与 Hill 夫妇同住 Highgate 三年）、
    与 Hodgkin/Huxley 合作；1952 正教授兼生物物理系主任、FRS
08  乙酰胆碱与终板电位 (1950s) — 运动神经元-肌肉突触的信号分子、
    有机磷/有机氯研究的即时影响（神经毒剂与杀虫剂的酶循环破坏）
09  量子式释放 (与 Fatt)（核心贡献页）— 递质释放总以最小单位的整数倍发生、
    后世解释：突触小泡以胞吐方式整份释放
10  GHK 方程 — Goldman–Hodgkin–Katz 通量方程与电压方程（跨膜离子电流的定量语言）
11  1970 诺奖 — 与 von Euler（递质身份与贮存）、Axelrod（再摄取）共享；
    神经末梢体液递质贮存-释放-失活全链条
12  荣誉与认可 — FRS 1952、Copley Medal 1967、下级勋位爵士 1969、Nobel 1970、
    Gerard 奖 1990、Pour le Mérite、Cothenius 奖章、Baly 奖章、澳大利亚科学院院士
13  家庭与晚年 — 1945 与 Marguerite Penly 结婚、二子；1978 荣休；
    2003 儿子 Jonathan 将其档案捐 UCL
14  遗产与结尾 — 从突触小泡到现代突触生物学：量子式假说的验证之路
```

## 七、特殊陷阱表 【人物专属，★ 核心】

| 陷阱 | 说明 |
|------|------|
| 三人分工 | Katz：突触释放的量子式性质（神经肌肉接头）；von Euler：NA 递质身份与贮存；Axelrod：再摄取与失活——citation 同一句，侧重分层勿互串 |
| 量子式发现归属 | "his discovery with Paul Fatt"——与 Fatt 共同发现，勿写成 Katz 独得；Fatt 不入诺奖但必须在发现叙述中具名 |
| 量子释放的现代解释 | 递质以突触小泡（等份）经胞吐释放——page.md 明载的现代理解（"Scientists now understand"），表述分层：Katz 当时是统计推论 |
| 导师单边 | infobox Academic advisors 仅 Archibald Hill；frontmatter 另列 Martin Gildemeister 系 metadata 噪声——以 infobox 为准只建 Hill 边 |
| Eccles 关系 | 卡内基奖学金"study with Eccles"（悉尼）——用 colleague 边（访学研究），勿写成师生 |
| Hill 重复 | UCL 导师 Archibald Hill 是 1922 诺奖得主（库内 id=4618）；与 von Euler 1934 游学的 A. V. Hill 是同一人——两篇各自建边，注明库内规范名 |
| 战时身份 | 1941 获英国国籍、1942 加入皇家澳大利亚空军任雷达军官（太平洋战区）——国别与军种勿混 |
| 国籍口径 | citations json "West Germany United Kingdom"、正文 "German-born British"——yaml 取 UK(0)+Germany(1)，封面国籍行 UK |
| 卒地 | 逝于伦敦（2003-04-20，92 岁），与莱比锡生地对照 |

## 八、术语清单 【人物专属】

| 英文 | 中文 | 风险点 |
|------|------|------|
| quantal release | 量子式释放 | 获奖核心发现（与 Fatt） |
| synaptic vesicle | 突触小泡 | 量子单位的现代解释 |
| end-plate potential | 终板电位 | 神经肌肉接头电信号 |
| acetylcholine | 乙酰胆碱 | 神经肌肉突触递质 |
| Goldman–Hodgkin–Katz flux equation | GHK 通量方程 | 跨膜离子流定量 |
| Goldman–Hodgkin–Katz voltage equation | GHK 电压方程 | 静息电位定量 |
| neuromuscular junction | 神经肌肉接头 | 研究体系 |
| exocytosis | 胞吐 | 小泡释放机制 |
| organophosphate | 有机磷 | 酶循环破坏的毒理学延伸 |
| nerve agent | 神经毒剂 | 有机磷研究的战后背景 |

## 九、背景音乐选择 【人物专属】

- **选定曲目**：**Nostalgia**（manifest 预分配，音乐库 `music_audio/`，选曲参考 `curated_tracks.md`）
- **匹配理由**：从莱比锡到伦敦的流亡、Hill 家屋檐下的战后岁月、UCL 半个世纪的突触长跑——"Nostalgia" 匹配这条离散而坚韧的回望式人生与跨世纪师友情谊。
- **本地路径**：复制 `music_audio/` 下对应 wav 到 `medic/presentations/20th_century/Bernard_Katz/Nostalgia.wav`
- **时长核对**：确认 ≥ 15 页 × 7 秒 ≈ 105 秒，ffmpeg `-shortest` 自动对齐。
