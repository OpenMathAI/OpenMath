# 医学家立传提示词（Niels Ryberg Finsen）

> OpenMedic 项目 · 20 世纪诺贝尔生理学或医学奖 1903 年得主 · 本文件是该人物的专属立传提示词，
> 按 9 节结构执行 Beamer 立传；数据库入库（fields/relations）已由批次完成，本文件第四/三节与 yaml 一致。

## 一、背景信息 【人物专属】

- **目标医学家**：Niels Ryberg Finsen（1860-12-15 生于法罗群岛 Tórshavn ~ 1904-09-24 逝于哥本哈根，享年 43 岁）
- **气质关键词**：**光疗医学之父、病榻上的科学家、首位斯堪的纳维亚医学诺奖得主** —— 1903 年获奖理由（逐字引用 medic/nobel_medicine_citations.json）：
  > "[for] his contribution to the treatment of diseases, especially lupus vulgaris , with concentrated light radiation, whereby he has opened a new avenue for medical science"
  > （因其对疾病治疗的贡献——特别是用聚光辐射治疗寻常狼疮，由此为医学科学开辟了新途径）
- **设计母题**：**向光（Mod lyset / Towards the Light）**。透镜聚焦的光束、拱起的脖颈面向太阳——以哥本哈根 Rigshospitalet 旁 Tegner 纪念雕塑《Mod lyset》为全篇视觉母题。
- **本地 Wikipedia 路径**：medic/presentations/pages/20th_century/Niels_Ryberg_Finsen/page.md
- **参考模板**：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）

## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章）

- 第 0/1/2/3 步按 **medic 路径**执行：事实基准 = `medic/presentations/pages/20th_century/Niels_Ryberg_Finsen/page.md`；目录 `medic/presentations/20th_century/Niels_Ryberg_Finsen/`；Makefile 改 `MAIN=Niels_Ryberg_Finsen_zh`；肖像优先 images.txt 所列 Commons 图，失败用装饰圆占位。
- 第 4/4.5 步（入库）**已完成**（第三、四节与 `MySQL/data/Niels_Ryberg_Finsen.yaml` 一致，勿重复入库）。
- 第 5-9 步：配色 → 幻灯片 → Beamer → 布局检查（0 error、vbox≤10pt、hbox≤50pt、逐页目检）→ 史实审查（第七节）。

## 三、研究领域梳理 + 入库（rank 0-4 表）

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | phototherapy | 光疗法 | 聚光辐射治疗寻常狼疮，1903 诺奖核心 | 核心页 |
| 1 | dermatology | 皮肤（科）医学 | lupus vulgaris 为皮肤结核 | 核心页 |
| 2 | physiology | 生理学 | 光对活体作用的实验生理研究 | 理论页 |

## 四、社会关系梳理 + 入库（与 yaml 完全一致，已完成）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| parent-child | Hannes Finsen | 父→本人 | 父，法罗群岛 Landfoged/Amtmand，冰岛裔世家 |
| spouse | Ingeborg Balslev | — | 1892-12-29 结婚 |

> 对手方规范名：本篇仅 2 条关系（Hulse relations=2 同例，诚实值）；对手方均按 page.md 形式新建 stub。

## 五、配色方案

- **气质**：北欧的清冽、光的纯净、与病痛共处的静默坚忍
- **主色**：光之蓝 `#1E5A8A`（聚光透镜与北海之蓝）
- **诺奖香槟金**：`#D4AF37`（光疗之"金色阳光"双重呼应）
- **badge 四分类色**：
  - `badgeA` 光疗 — 日光金橙 `#E8A33D`
  - `badgeB` 寻常狼疮 — 皮肤青 `#4A8C8C`（用冷色避免病态红）
  - `badgeC` Finsen 研究所 — 丹麦红 `#9E2B25`
  - `badgeD` 冰岛-法罗源流 — 峡湾蓝 `#2F5D7C`
- **背景母题**：稀疏同心光环与聚焦光束（低透明度），呼应"向光"雕塑的意象。

## 六、幻灯片序列（15 页规划）

```
00  OpenMedic 项目首页（\input cover/openmedic_page.tex）
01  封面 — 光疗医学之父 / Niels Ryberg Finsen 1860–1904 + 四色 badge + 右上头像 + 国籍行（Denmark）
02  身份信息页（★ 必做）— 左头像 + 右信息网格（生卒、Tórshavn、哥本哈根大学 1890、Finsen 研究所 1896、诺奖 1903）
03  核心贡献概览 — 光疗理论 / 聚光装置治疗狼疮 / Finsen 研究所 / 低盐饮食研究
04  法罗与冰岛少年 (1860–1882) — Tórshavn 出生、4 岁丧母、Herlufsholm 低评（"a boy of good heart but low skills"，page.md 英文原文可引）、1876 雷克雅未克 Lærði skólinn
05  哥本哈根求学 (1882–1890) — 医学 1890 毕业、Regensen 宿舍（冰岛/法罗优待政策）、解剖学 prosector 三年
06  病与光的相遇 (1880s–1893) — Niemann–Pick 病缠身、亲试日光、1893《论光对皮肤的作用》
07  聚光疗法的诞生 (1896) — Finsen 研究所首任所长、1896《浓缩化学光线在医学中的应用》
08  治疗寻常狼疮 — 聚光辐射临床效果、"opened a new avenue for medical science"（官方理由回扣）
09  1903 诺贝尔奖 — 首位斯堪的纳维亚医学诺奖得主、迄今唯一法罗裔得主；官方理由全句
10  病榻上的科学 (1898–1904) — 教授职 1898、Dannebrog 骑士 1899、轮椅上工作"病残其身未残其志"
11  盐与机体的末章研究 — 1904《盐在机体中的蓄积》低盐饮食观察
12  家庭与身后 — Ingeborg Balslev、1904-09-24 逝于哥本哈根（尸检另有包虫病因素）
13  纪念：Mod lyset — 1909 Tegner 雕塑"向光"、Finsen 实验室并入 Rigshospitalet、Tórshavn 街道与伦敦 Finsen Road
14  遗产：光疗与现代皮肤病治疗 — 光疗谱系的起点
15  结尾（OpenMathAI 品牌口径）
```

## 七、特殊陷阱表（★ 核心）

| 陷阱 | 说明 |
|------|------|
| 死亡日期 | metadata.json 双值 1904-09-24 / 10-24；**以 page.md 正文 24 September 1904 为准**（infobox 同） |
| 获奖理由逐字 | citation json 原文以 "[for]" 开头，语气为"贡献/新途径"；page.md 转写作 "in recognition of his contribution..."——引用时统一用 json 版本，勿自行改写 |
| 国籍口径 | Nobel/citation json 列 Faroe Islands，manifest 与总表为 Denmark；yaml 按总表 Denmark 入库，提示词正文写"法罗群岛出生、丹麦国籍"，陷阱表记录裁定 |
| 疾病名 | Niemann–Pick 病系 page.md 后世回溯结论；当时仅知心疾/腹水等症——叙事可用"今推断为"，勿写成"当年确诊" |
| 尸检补充 | 死因含 echinococcosis（包虫病）为促因，page.md 明载，可提 |
| 无师承关系 | page.md 无博士导师/门生记载；**勿虚构**（Finsen 研究所后继者无具名载） |
| Herlufsholm 评语 | 校长评语英文原文 "a boy of good heart but low skills and energy"，引原文 + 译文，勿改写 |
| 毕业排名 | 雷克雅未克毕业 21 岁、15 人中第 11 名——写作时勿美化成优异成绩 |
| Cameron Prize | Finsen 的 Cameron Prize 是 **1904**（身后当年），与 Ross 1902/Behring 1894 区分 |
| 荣誉年份 | 教授职 1898、Dannebrog 骑士 1899，勿与诺奖 1903 混排 |

## 八、术语清单

| 英文 | 中文 | 风险 |
|------|------|------|
| phototherapy | 光疗法 | 聚光辐射治疗，非"光动力疗法(PDT)" |
| lupus vulgaris | 寻常狼疮 | 皮肤结核，非系统性红斑狼疮(SLE) |
| concentrated light radiation | 聚光辐射 | 经透镜/滤光聚焦 |
| Finsen Institute | 芬森研究所 | 1896 创办，后并入 Rigshospitalet |
| Niemann–Pick disease | 尼曼-皮克病 | 后世回溯诊断 |
| prosector | 解剖示教员 | 大学解剖学职位 |
| Mod lyset | 《向光》 | Tegner 1909 纪念雕塑 |
| Order of the Dannebrog | 丹尼布洛勋章 | 1899 骑士级 |

## 九、背景音乐选择

- **选定曲目**：**New Lands** — Alex-Productions（manifest 预分配）
- **匹配理由**："新大陆/曙光"的意象与"向光（Mod lyset）"母题天然契合——光疗为医学开辟新途；北欧清冷基调承载病榻科学家的静默坚忍。
- **本地路径**：music_audio/ 下 Alex-Productions New Lands 曲目（执行时按 curated_tracks.md 对应文件复制到本目录）。
