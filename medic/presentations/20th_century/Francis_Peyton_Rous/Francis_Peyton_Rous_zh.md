# 医学家立传提示词（Francis Peyton Rous）

> OpenMedic 项目 · 20 世纪诺贝尔生理学或医学奖 1966 年得主（同届 Charles Brenton Huggins 各自半奖、理由不同）。
> 本文件是 Peyton Rous 的人物专属立传提示词：事实基准唯一来源为本地 Wikipedia 页面。

---

## 一、背景信息 【人物专属】

- **目标医学家**：Francis Peyton Rous（1879-10-05 生于巴尔的摩 ~ 1970-02-16 逝于纽约，享年 90）
- **气质关键词**：**肿瘤病毒之父、等了 55 年的诺奖得主、史上最年长的医学奖获得者**
- **诺奖获奖理由（1966，逐字引用 medic/nobel_medicine_citations.json）**：
  > "for his discovery of tumour -inducing viruses"
  > （因其发现致瘤病毒）——注意 "his"：Rous 独得该半奖；json 原文 "tumour" 后有一空格排版噪声，页面正文为 "tumour-inducing viruses"，引用以页面干净形式为准并注明
- **设计母题**：**滤过与潜伏（filtrate and latency）**。无细胞滤液让健康鸡长出肉瘤——55 年的学术"潜伏期"；
  视觉母题用一枚滤膜滤下微小雨点状病毒颗粒、在远端催生阴影团块，象征"被延误半个世纪的看见"。
- **本地 Wikipedia 路径**：`medic/presentations/pages/20th_century/Francis_Peyton_Rous/page.md`
- **参考模板**：`physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex`（骨架）

## 二、任务流程（对齐 Physicist_Bio_Prompt_Template.md 第三章）

> 第 0/1/2/3 步按 medic 路径执行：页面读 `medic/presentations/pages/20th_century/{Dir}/page.md`，
> 产出放 `medic/presentations/20th_century/Francis_Peyton_Rous/`，数据库写 greatminds 库（MySQL）。
> 第 0 步核对事实基准（本提示词三、四、七节已沉淀）→ 第 1 步建目录含 images/ → 第 2 步复制 Makefile 设
> `MAIN=Francis_Peyton_Rous_zh`、`VIDEO_NAME=Francis_Peyton_Rous_zh` → 第 3 步收肖像（Commons 回退，404 装饰圆）→
> 第 4~9 步 tex 编写 → 编译循环（0 error、vbox≤10pt、hbox≤50pt）→ pdftoppm 逐页目检 → make images/video → Review。

## 三、研究领域梳理 + 入库（与 yaml fields 完全一致）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | virology | 病毒学 | 劳斯肉瘤病毒，诺奖核心（infobox Fields） | 核心页 |
| 1 | pathology | 病理学 | 本行身份（病理学教师出身） | 身份页 |
| 2 | oncology | 肿瘤学 | 病毒致癌研究纲领 | 核心页 |
| 3 | physiology | 生理学 | 肝与胆囊的消化生理研究 | 生理页 |

## 四、社会关系梳理 + 入库（与 yaml relations 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| co-honored | Charles Brenton Huggins | 无向 | 1966 诺贝尔生理学或医学奖同届各自半奖（Rous=致瘤病毒；Huggins=前列腺癌激素疗法） |
| spouse | Marion Eckford de Kay | 无向 | 1915 年结婚；三女之父 |
| colleague | Simon Flexner | 无向 | 洛克菲勒研究所所长，1909 招其主持癌症研究；晚年为其作传 |
| colleague | Alfred Warthin | 无向 | 密歇根大学病理系主任，劝其赴德深造并告知洛克菲勒奖学金 |
| colleague | Richard Shope | 无向 | 洛克菲勒同事，1933 兔乳头瘤病毒发现者，邀其重返癌症研究 |
| collaborator | Joseph R. Turner | 无向 | 一战输血研究搭档：配血试验与柠檬酸盐-葡萄糖保血法 |
| collaborator | James B. Murphy | 无向 | 劳斯肉瘤致癌性的确证实验合作者 |
| collaborator | W. H. Tytler | 无向 | 1912 年合作实验首次提示滤过性病因为病毒 |
| collaborator | Philip D. McMaster | 无向 | 共同阐明胆囊浓缩胆汁的主功能 |
| collaborator | Louise D. Larimore | 无向 | 共同描述肝损伤条件与胆汁分泌影响 |

> 说明：relations=10 全部 page.md 明载（含多项短期合作，诚实值）。
> 女儿 Marni 嫁诺奖得主 Alan Lloyd Hodgkin——姻亲不入库；Oswald H. Robertson 是技术的前线使用者非合作者，不入库。
> 自查 SQL：`SELECT COUNT(*) FROM person_relation WHERE from_id=<pid> OR to_id=<pid>;` 预期 = 10。

## 五、配色方案

- **气质**：耐心、被误解后的平反、老而弥坚
- **主色**：深绿 `#1B4D3E`（鸡舍与显微镜下的冷静绿）+ 香槟金 `#D4AF37`（诺奖色）
- **四分类色 badge**：`badgeVirus` 致瘤病毒 — 冷青 `#0E7C7B`；`badgeSarcoma` 肉瘤 — 猩红 `#C4204F`；`badgeBlood` 输血 — 暖橙 `#E07B30`；`badgeAward` 荣誉 — 皇家紫 `#52307C`
- **背景母题**：滤膜细孔网格 + 稀疏病毒颗粒小点

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页
01  封面 — 肿瘤病毒之父 / Peyton Rous 1879–1970 + 四色 badge + 国籍行（United States）
02  身份信息页 — 生卒/巴尔的摩出身/Johns Hopkins BA 1900 + MD 1905/洛克菲勒研究所/核心领域
03  核心贡献概览 — 劳斯肉瘤病毒 / 血库 / 消化生理 / 55 年后的诺奖
04  早年与结核 (1879–1905) — 11 岁丧父；Johns Hopkins 奖学金；二年级尸检感染结核（腋窝结核性淋巴结炎）；德州牧场养牛一年疗养；自认不宜行医转向研究
05  密歇根与德累斯顿 (1905–1909) — Warthin 门下病理学讲师；1907 德累斯顿病理解剖课程；归途肺结核复发、阿迪朗达克疗养
06  洛克菲勒与一只母鸡 (1909–1911，核心贡献页) — Flexner 邀其主持癌症研究；1910 普利茅斯洛克母鸡的梭形细胞肉瘤（可移植）；1911 无细胞滤液（Berkefeld 滤器）转移恶性肿物——1911 论文引语（page.md 有英文原文可引）
07  "utter nonsense"：被拒绝的发现 — 德国病理学传统抵制感染致癌说；被指技术污染；Oberling 回顾引语（page.md 有英文原文）；与 Murphy 确证、1912 与 Tytler 首次指向病毒
08  转向与回归 (1915–1933) — 1915 暂别癌症研究；18 年后应 Shope 之邀重返：兔乳头瘤病毒→恶性进展，此后三十年确证病毒乳头瘤可致癌
09  血库的诞生 — 1915 与 Turner 配血方法；1916 柠檬酸盐-葡萄糖溶液使保存从一周延至两周；1917 Robertson 带往前线比利时——世界第一个血库；Landsteiner 血型发现的实用化（page.md 有 Rous 评语英文原文）
10  消化生理 — 与 Larimore：肝损伤与胆汁分泌；与 McMaster：胆囊=胆汁浓缩场所（黄疸与胆结石理解）
11  1966 诺贝尔奖 — 理由逐字；55 年"潜伏期"、87 岁获奖=医学奖最年长得主；1926 起 Landsteiner 等 17 次提名史
12  荣誉与认可 — NAS 1927 · 美国哲学学会 1939 · ForMemRS 1940 · Lasker 1958 · 国家科学奖章 1965 · Paul Ehrlich 1966 · Kovalenko 奖章 · 联合国癌症研究奖 · 美国癌症学会杰出服务奖
13  病毒致癌的胜利 — 1925 Gye（英国 NIMH Hampstead）证实病毒性质；1960 癌基因发现、1970s src 基因鉴定——劳斯肉瘤病毒成为现代癌症生物学基石
14  家庭与身后 — 1915 娶 Marion Eckford de Kay（1985 逝）；三女；长女 Marni 嫁 Alan Lloyd Hodgkin；1970 因腹部癌症逝于纽约 Memorial Sloan Kettering；为 Flexner 与 Landsteiner 作传
15  结尾
```

## 七、特殊陷阱表（★ 执行时必须核对）

| # | 陷阱 | 说明 |
|---|------|------|
| 1 | 获奖理由 | 逐字 "for his discovery of tumour-inducing viruses"；"his" 独得半奖；与 Huggins 同届但**理由不同**，勿写共享理由 |
| 2 | 55 年与 87 岁 | 1911 发现→1966 获奖（医学诺奖史最长"潜伏期"）；87 岁为最年长医学奖得主——两个"最"均 page.md 明载 |
| 3 | 全名 | Francis Peyton Rous，通称 Peyton Rous；发音 /raʊs/，中文作"劳斯" |
| 4 | 结核改道 | 医学院二年级尸检感染结核→自认不宜当 "real doctor"→转向研究；1904 复学、1905 MD——人生分水岭勿省略 |
| 5 | 1910 vs 1911 | 1910-05 首报可移植鸡肉瘤；1911 无细胞滤液实验（诺奖核心理由）——勿混 |
| 6 | 血库归属 | Rous-Turner 发明柠檬酸盐保血法；**Robertson** 1917 前线建立世界第一个血库——应用者勿写成共同发明人 |
| 7 | 引语红线 | 1911 论文句、Oberling 回顾、Landsteiner 评语三处 page.md 有英文原文可引（引原文+译文）；其余不得造引语 |
| 8 | Gye 的角色 | 1925 年 William Ewart Gye 证明病毒性质——署名勿漏 |
| 9 | 死因 | 1970 死于腹部癌症，逝于 Memorial Sloan Kettering |
| 10 | 女儿姻亲 | 长女 Marni（1917-2015，童书编辑）嫁 Alan Lloyd Hodgkin（1963 诺奖）——一句带过，不建边 |
| 11 | 国籍 | United States 单籍（manifest/citation json 同） |

## 八、术语清单

| 英文 | 中文 | 风险点 |
|------|------|--------|
| Rous sarcoma virus | 劳斯肉瘤病毒 | 逆转录病毒，src 癌基因载体 |
| cell-free filtrate | 无细胞滤液 | Berkefeld 滤器除菌后的致病成分 |
| oncovirus | 肿瘤病毒 | Known for 词 |
| citrate | 柠檬酸盐 | 抗凝保血关键 |
| blood bank | 血库 | 前线首次实践归 Robertson |
| sarcoma | 肉瘤 | 梭形细胞肉瘤 |
| papilloma | 乳头瘤 | Shope 兔病毒 |
| ForMemRS | 皇家学会外籍院士 | 1940 当选 |

## 九、背景音乐选择

- **选定曲目**：**The Invisible Light** — Alex-Productions（manifest 预分配）
- **匹配理由**："看不见的光"对应双重隐喻——滤液中看不见的病毒 Agent，与被学界"看不见"了半个世纪的发现；音乐的幽微感贴合其孤证不立、静待时代追认的一生。
- **备选（未采用）**：The Flow of Time（时间感契合但已高频占用）、Tragedy（悲情可用但本篇结局是平反）
- **本地路径**：`music_audio/` 曲库按 curated_tracks.md 复制为 `medic/presentations/20th_century/Francis_Peyton_Rous/The_Invisible_Light.wav`
