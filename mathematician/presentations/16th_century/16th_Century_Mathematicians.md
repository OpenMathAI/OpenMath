# 16 世纪数学史上的巨匠 — OpenMath 收录清单

> **本清单是 OpenMath 数学家立传项目的 16 世纪收录总表，非官方排名，而是按生年排序的收录清单。**
>
> 从 del Ferro、Cardano 到 Viète、Napier：三次/四次方程与代数符号化的创立时代。

---

## 一、收录标准

1. **世纪归属**：以数学家主要学术贡献（代表作 / 成名工作的集中发表年代）所处世纪为准
2. **生年上限**：生年早于 1562 年，核心贡献在 16 世纪完成
3. **数据来源**：维基百科「List of mathematicians」列表及《世纪分类标准》

> 列说明：「**立传**」= 是否已生成 Beamer 演示文稿成品（tex/pdf；mp4 视频待配乐后另行统一制作）；「**Review**」= 是否已完成两轮史实终审与结构优化；「**社会关系入库**」= 是否已将社会关系与研究领域写入 greatminds 数据库（people/person_relation/person_field）。
>
> **核验记录（2026-09-29 · Beamer 立传）**：14 人 Beamer 演示文稿（tex/pdf）全部产出，位于 `{生年}–{Name}/{Name}_zh.tex|pdf`，版式对齐 17 世纪 `1667–Johann_Bernoulli` 黄金参照（共享封面 + 人物封面 + 身份信息页 + 时间线 + 早年与教育 + 贡献页 + 荣誉与传承 + 终章；核验为 **14 页**，Bombelli 按提示词规划 **13 页**：6 贡献页）。`make distclean && make` 全部 **0 error**、Overfull 全部 <10pt（多数 0，仅共享封面固有 0.48–4.67pt）；逐页目检（封面 / 身份页 / 时间线 / 早年 / 全部贡献页 / 荣誉页 / 终章）无遮挡、错位、溢出；品牌行统一 `OpenMathAI`。
>
> **立传前 Review-1 事实终审（14/14，修正写回各人提示词 md §12）关键纠错**：①**Clavius / Stevin / Briggs 原提示词断言「无真实肖像」有误**——三人实有传世版画像，已改用真肖像（另 Viète 首选项改为传世画像、Nunes 改用 1843 年刊像而非纪念碑雕像）；②Viète 删除 page.md 无载的「1593 van Roomen 挑战」年份；③Ferrari 删除「1522 年博洛尼亚属教宗国」的越界推定（原系据 Bombelli 页外推），论战仅写 1545 年爆发（禁 1548 /「胜出」），死因保留「据传说」；④Tartaglia 删除无载的「挑战赛中最终胜出」表述（page.md 只载曾被 Fiore 挑战）；⑤Commandino 克莱孟八世庇护句系条目自身年代矛盾，照录 + 存疑小注；⑥Napier–Briggs 两次爱丁堡会面年份两页各自忠于本人页面（1615 / 1616–1617），互不改写；⑦Clavius 禁写「发明格里高利历」（Lilius 方案 + 委员会辩护者）；Stevin 小数只写「确立」；Harriot 不等号只写「首次广泛使用」+ 1631 身后发表。
>
> **肖像结论（10 真像 + 4 装饰圆）**：塔尔塔利亚、卡尔达诺、努内斯、科门迪诺、克拉维乌斯、韦达、斯蒂文、纳皮尔、哈里奥特（图注必带「传为」）、布里格斯 用真肖像（均经 Wikipedia REST API / Commons 核验并目检）；德尔·费罗、雷科德、费拉里、邦贝利 无存世肖像 → 装饰圆 `\faIcon{user}` 占位，**禁**以书影 / 雕像 / 纪念碑 / 檄文封面冒充头像。
>
> **遗留**：BGM 未复制（出片阶段统一去重：Expedition 被 Nunes/Stevin/Briggs 同选、Lonesome 被 Tartaglia/Harriot 同选、Cinematic Experience 被 Cardano/Viète 同选、PAST 被 del Ferro/Commandino 同选）；立传期目检 `preview/` 图已清理；「Review」列仍为 🔲（两轮史实终审与结构优化待做）。

> **核验记录（2026-09-29）**：14 人「人物专属立传提示词 md」全部完成（位于 `{生年}–{Name}/{Name}_zh.md`，11 节结构对齐 17 世纪 Johann_Bernoulli_zh.md；§5 逐条对照本地 page.md，无载禁写）；社会关系与研究领域已入库 greatminds（MySQL/data/ 下 14 份 yaml，seed_person.py 入库），14/14 `has_social_data=1`，涉及关系行 93 条（含 Tartaglia–Cardano–Ferrari 论战链、Viète–Clavius 历法论战、Napier–Briggs 合作等），对手方零分裂；`has_biography` 全部为 0（立传未做）。关键裁定：Ferrari 享年 43（1522-02-02~1565-10-05）、1548 公开辩论无载禁写；Tartaglia 生年 1499/1500 两说并存；Cardano 卒日 1576-09-21；Bombelli 卒年 1572、"wild thought" 引语无载禁用；Clavius 历法为 Lilius 方案的委员会成员+辩护阐释者禁写「发明」；Recorde 生年 c.1510 带「约」、卒 1558-06 不写具体日；Nunes 生卒取 1502 / 1578-08-11；Commandino 克莱孟八世庇护句存在年代矛盾须存疑注记；Viète 卒日 1603-02-23、非职业数学家；Stevin 生卒只到年、小数只写「确立」禁写「发明」；Napier–Briggs 会面年份两页矛盾各忠本人页面。

---

## 二、数学家清单（按生年排序）

| # | 英文名 | 中文名 | 国籍 | 生卒 | 核心贡献 | 立传 | Review | 社会关系入库 |
|:--:|------|:--:|------|:--:|------|:--:|:--:|:--:|
| 1 | [Scipione del Ferro](https://en.wikipedia.org/wiki/Scipione_del_Ferro) | 德尔·费罗 | 意大利 | 1465–1526 | 首解三次方程（缺二次项型） | ✅ | 🔲 | ✅ |
| 2 | [Niccolò Tartaglia](https://en.wikipedia.org/wiki/Niccol%C3%B2_Tartaglia) | 塔尔塔利亚 | 意大利 | 1500–1557 | 三次方程解法、弹道学、《新星》 | ✅ | 🔲 | ✅ |
| 3 | [Gerolamo Cardano](https://en.wikipedia.org/wiki/Gerolamo_Cardano) | 卡尔达诺 | 意大利 | 1501–1576 | 《大术》、三四次方程、概率论先驱 | ✅ | 🔲 | ✅ |
| 4 | [Pedro Nunes](https://en.wikipedia.org/wiki/Pedro_Nunes) | 努内斯 | 葡萄牙 | 1502–1578 | 斜驶线（loxodrome）、nonius 游标 | ✅ | 🔲 | ✅ |
| 5 | [Federico Commandino](https://en.wikipedia.org/wiki/Federico_Commandino) | 科门迪诺 | 意大利 | 1509–1575 | 阿基米德/欧几里得/阿波罗尼奥斯拉丁译本 | ✅ | 🔲 | ✅ |
| 6 | [Robert Recorde](https://en.wikipedia.org/wiki/Robert_Recorde) | 雷科德 | 英国（威尔士） | 1512–1558 | 等号 = 的发明、《砺智石》代数教材 | ✅ | 🔲 | ✅ |
| 7 | [Lodovico Ferrari](https://en.wikipedia.org/wiki/Lodovico_Ferrari) | 费拉里 | 意大利 | 1522–1565 | 四次方程一般解法 | ✅ | 🔲 | ✅ |
| 8 | [Rafael Bombelli](https://en.wikipedia.org/wiki/Rafael_Bombelli) | 邦贝利 | 意大利 | 1526–1572 | 《代数》、复数运算规则 | ✅ | 🔲 | ✅ |
| 9 | [Christopher Clavius](https://en.wikipedia.org/wiki/Christopher_Clavius) | 克拉维乌斯 | 德国 | 1538–1612 | 格里高利历改革、欧几里得注释 | ✅ | 🔲 | ✅ |
| 10 | [François Viète](https://en.wikipedia.org/wiki/Fran%C3%A7ois_Vi%C3%A8te) | 韦达 | 法国 | 1540–1603 | 代数符号化、韦达定理 | ✅ | 🔲 | ✅ |
| 11 | [Simon Stevin](https://en.wikipedia.org/wiki/Simon_Stevin) | 斯蒂文 | 佛兰德 | 1548–1620 | 十进小数、《算术》、力学 | ✅ | 🔲 | ✅ |
| 12 | [John Napier](https://en.wikipedia.org/wiki/John_Napier) | 纳皮尔 | 苏格兰 | 1550–1617 | 对数、纳皮尔骨牌 | ✅ | 🔲 | ✅ |
| 13 | [Thomas Harriot](https://en.wikipedia.org/wiki/Thomas_Harriot) | 哈里奥特 | 英国 | 1560–1621 | 代数记号（< > 不等号）、方程论 | ✅ | 🔲 | ✅ |
| 14 | [Henry Briggs (mathematician)](https://en.wikipedia.org/wiki/Henry_Briggs_(mathematician)) | 布里格斯 | 英国 | 1561–1630 | 常用对数（以 10 为底） | ✅ | 🔲 | ✅ |

## 三、目录对应关系

| 文件夹 | 中文名 |
|------|:--:|
| `pages/Scipione_del_Ferro/` | 德尔·费罗 |
| `pages/Niccolò_Tartaglia/` | 塔尔塔利亚 |
| `pages/Gerolamo_Cardano/` | 卡尔达诺 |
| `pages/Pedro_Nunes/` | 努内斯 |
| `pages/Federico_Commandino/` | 科门迪诺 |
| `pages/Robert_Recorde/` | 雷科德 |
| `pages/Lodovico_Ferrari/` | 费拉里 |
| `pages/Rafael_Bombelli/` | 邦贝利 |
| `pages/Christopher_Clavius/` | 克拉维乌斯 |
| `pages/François_Viète/` | 韦达 |
| `pages/Simon_Stevin/` | 斯蒂文 |
| `pages/John_Napier/` | 纳皮尔 |
| `pages/Thomas_Harriot/` | 哈里奥特 |
| `pages/Henry_Briggs/` | 布里格斯 |
