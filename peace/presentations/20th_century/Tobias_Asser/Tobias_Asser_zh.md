# 和平奖得主立传提示词（OpenPeace 标杆实例：Tobias Asser）

> 本文件是 OpenPeace 项目的「诺贝尔和平奖得主立传提示词」，以 Tobias Asser（1911 诺贝尔和平奖，国际法与仲裁）为完整实例。
> 结构对齐 OpenPhysicist 标杆 `Kenneth_G_Wilson_zh.md`（一~五节）。凡标注【模板通用】可复用，【人物专属】按本人物执行。
> 直接复制本文件到新对话中使用，按步骤执行，每完成一步汇报进度。

---

## 一、模板定位

- **目标项目**：OpenPeace —— 开放诺贝尔和平奖得主人物史（与 OpenMath/OpenPhysicist 共享 GitHub `OpenMathAI/OpenMath`）。
- **本实例**：Tobias Michael Carel Asser（托比亚斯·阿塞尔），1911 诺贝尔和平奖得主（与 Alfred Fried 共享）。
- **设计哲学**：和平奖立传与科学家立传的核心差异，在于**贡献以「制度建设」而非「理论发现」呈现**——Asser 的遗产是常设仲裁法院与国际私法会议两个持久机制，立传须以「机构建设史」为叙事骨架，身份信息页必做。

---

## 二、背景信息 【人物专属】

- **目标人物**：Tobias Michael Carel Asser（1838-04-28 ~ 1913-07-29，享年 75 岁）
- **气质关键词**：**国际私法的奠基者、海牙仲裁制度的缔造者、以法律促和平的先驱**
- **官方获奖理由（英文原文照抄 nobel_peace_citations.json）**：
  > "for his role as co-founder of the Institut de droit international, initiator of the Conferences on International Private Law (Conférences de Droit international privé) at the Hague, and pioneer in the field of international legal relations"
  - **中译（照抄名录 OpenPeace_20th_Century_Nobel_Laureates.md，禁止改写）**：表彰他作为国际法研究院共同创始人、海牙国际私法会议发起人，以及国际法律关系领域的开拓者
  - ★ 1911 为共享年份：与 Alfred Fried 同年获奖，但**两人理由句各自独立**，Fried 篇理由不适用于本篇
- **设计母题**：**条约与天平（treaty & balance）**。Asser 的一生是把跨境私人关系纳入统一法律框架——海牙会议多边条约、常设仲裁法院、国际法研究院，视觉语言宜用条文纹理、天平、多国旗帜色带。
- **本地数据源**：`peace/presentations/pages/20th_century/Tobias_Asser/page.md`（Wikipedia 全文 + frontmatter，事实基准唯一来源）

---

## 三、任务流程 【模板通用，逐步执行】

### 第 0 步：事实基准 【人物专属】

- 生卒：1838-04-28 生于阿姆斯特丹 ~ 1913-07-29 卒于海牙（享年 75）
- 国籍：荷兰（Netherlands）；出生于犹太家庭
- 家庭：父 Carel Daniël Asser（1813–1885）；祖父 Carel Asser（1780–1836）；妻 Johanna Ernestina Asser（1864 结婚）
- 教育：阿姆斯特丹大学 + 莱顿大学；PhD 1860，论文 *Geschiedenis der beginselen van het Nederlandsche Staatsregt omtrent het bestuur der buitenlandsche betrekkingen*；博士导师 Simon Vissering
- 任职：阿姆斯特丹大学法学教授
- 关键荣誉：Nobel Peace Prize 1911；柏林洪堡/博洛尼亚/剑桥/莱顿四所荣誉博士（frontmatter award_received）；1880 荷兰皇家艺术与科学院院士
- 核心事业清单：
  1. 与 John Westlake、Gustave Rolin-Jaequemyns 共同创办 *Revue de Droit International et de Législation Comparée*
  2. 1873 共同创立国际法研究院（Institut de Droit International）
  3. 1893 发起海牙国际私法会议（HCCH）首届外交会议并任主席，连任至第四届（1894/1900/1904）；任内产出 1902 婚姻/离婚/监护、1905 民事诉讼/婚姻效力/剥夺民事权利六部海牙公约
  4. 1899/1907 两届海牙和平会议荷兰代表，推动强制仲裁原则，促成常设仲裁法院（PCA）
  5. 1902 出任 PCA 首案（Pious Fund of the Californias Case）仲裁庭法官
  6. 参与筹建海牙国际法学院（1923 才成立，未能亲见）
- 关键时间线（15–20 节点）：1838 生于阿姆斯特丹 → 阿姆斯特丹/莱顿求学 → 1860 博士（导师 Vissering）→ 1862 丹麦国王 Award（frontmatter 有载）→ 1864 结婚 → 1873 共创 Institut de Droit International → 1880 荷兰皇家科学院院士 → 1893 HCCH 首届主席 → 1894/1900/1904 连任 → 1902 六部海牙公约 → 1899 第一届海牙和平会议 → 1902 PCA 首案仲裁庭 → 1904 第三届 HCCH → 1907 第二届海牙和平会议 → 1911 获诺贝尔和平奖（12-10 颁奖演说，Løvland 称其为「格劳秀斯的继承者」）→ 1913-07-29 卒于海牙

### 第 4 步：研究领域/事业领域表 【人物专属】

| rank | 领域（name_en） | 中文 | 说明 | 对应页 |
|:--:|------|------|------|------|
| 0 | private international law | 国际私法 | 核心领域，HCCH 的创立依据 | HCCH 页 |
| 1 | public international law | 国际公法 | 国际法研究院共同创始人的立身之学 | 早年页 |
| 2 | international arbitration | 国际仲裁 | PCA 制度缔造与首案法官 | PCA 页 |
| 3 | legal scholarship | 国际法学 | 期刊共创、法学教授、荣誉博士群 | 早年/荣誉页 |

### 第 4.5 步：社会关系表（与 yaml 完全一致）

| 关系类型 | 对方 | 方向 | note |
|---------|------|------|------|
| advisor-student | Simon Vissering | advisor | 阿姆斯特丹/莱顿博士导师，1860 博士论文 |
| spouse | Johanna Ernestina Asser | 无向 | 1864 结婚 |
| parent-child | Carel Daniël Asser | 无向 | 父亲（1813–1885） |
| parent-child | Carel Asser | 无向 | 祖父（1780–1836） |
| colleague | John Westlake | 无向 | 共同创办 Revue de Droit International et de Législation Comparée |
| colleague | Gustave Rolin-Jaequemyns | 无向 | 共同创办同上期刊 |
| founder | Institut de Droit International | 无向 | 1873 共同创立 |
| founder | Hague Conference on Private International Law | 无向 | 1893 发起首届外交会议并任主席 |
| founder | Permanent Court of Arbitration | 无向 | 1899 海牙和平会议促成设立 |
| co-honored | Alfred Fried | 无向 | 1911 诺贝尔和平奖共同得主 |

### 第 5 步：设计配色方案 【模板通用，人物专属色彩】

- **气质**：稳健、法度、跨国的秩序感
- **主色**：墨绿 `#1E4D3B`（manifest 预分配，勿改）+ 诺奖香槟金 `C9A227` + 四分类色
  - `badgePIL` 国际私法 — 靛蓝 `#3F5E9E`
  - `badgeARB` 国际仲裁 — 青绿 `#0E7C7B`
  - `badgeHCCH` 海牙会议 — 琥珀 `#C9821F`
  - `badgePCA` 常设仲裁法院 — 玫瑰 `#B5495B`
- **背景母题**：条文纹理底纹 + 稀疏圆点，呼应「多边条约的签署网络」

### 第 6 步：规划幻灯片序列 【人物专属，10–16 页】

```
00  OpenPeace 项目首页（\input cover/openpeace_page.tex）
01  封面 — 以法律促和平的先驱 / Tobias Asser 1838–1913 + 四色 badge + 右上肖像 + 国籍行
02  身份信息页（★ 必做）— 左肖像 + 右信息网格（生卒/本名/国籍/家庭/教育/师承/任职/荣誉/核心领域）
03  核心贡献概览 — HCCH / PCA / Institut de Droit International / 法学教育
04  阿姆斯特丹法学家世家 (1838–1873) — 犹太家庭、三代法学、Amsterdam+Leiden、1860 博士
05  国际法研究院与期刊共创 (1873–1892) — Revue、Institut、皇家科学院
06  海牙国际私法会议：六部公约 (1893–1905) — 首届主席、连任四届、1902/1905 公约群
07  海牙和平会议与常设仲裁法院 (1899–1907) — 强制仲裁主张、PCA 设立
08  PCA 首案：Pious Fund of the Californias (1902) — 首个全球性国家间仲裁机制的首案
09  荣誉与认可 — Nobel 1911、四所荣誉博士、皇家科学院
10  颁奖时刻 — Løvland 演说要点、理由句原文呈现
11  遗产：从 HCCH 到今日国际私法 — T.M.C. Asser Instituut、海牙国际法学院
12  结尾
```

### 第 7 步：编写 Beamer 源码 【模板通用】

- 每页 `\newcommand{\xxxslide}{...}` 定义；身份信息页实现模式参照 OpenPhysicist 成品 `\profileslide`。

### 第 8 步：布局检查 【模板通用】

- 每写完一页 `make clean && make`，用 `pdftoppm` 截图检查溢出/重叠。
- 修复优先级：删 `\plainbar` → 缩 `inner sep` → 缩字号 → 减行距 → 调 y 坐标。

### 第 9 步：史实审查 + 术语审查 【人物专属】

**Asser 特殊陷阱**：

| 陷阱 | 说明 |
|------|------|
| 卒日双值 | frontmatter 有 1913-07-29 与 1913-06-29 两值，**以 infobox/正文 1913-07-29 为准** |
| 格劳秀斯比喻 | 颁奖演说中 Løvland 称其为「荷兰 17 世纪国际法先驱的继承者、他那个时代的 Hugo Grotius」，这是演说修辞，**禁写与 Grotius 的师承/影响关系** |
| 共享年份 | 1911 与 Alfred Fried 共享但理由句各自独立；Fried 的「揭露无政府状态」理由禁入本篇 |
| PCA 归属 | infobox 作 "Founder of the Permanent Court of Arbitration"，正文作「促成设立」，行文用「促成/缔造」，勿夸张为独力创办 |
| HCCH 名称 | 1893 年首届会议当时并无今日 HCCH 之名，行文以「海牙国际私法会议」制度史叙述，勿写「1893 年成立 HCCH 组织」 |
| 犹太家庭 | page.md 明载「出生于犹太家庭」，仅作事实陈述，不加评价 |
| 无载禁写 | 子女情况、晚年细节、与 Suttner 的交往 page.md 均无载，一律禁写 |

**术语清单**：

| 英文 | 中文 | 风险 |
|------|------|------|
| Permanent Court of Arbitration | 常设仲裁法院 | 勿与海牙的 Permanent Court of International Justice（1922）混淆 |
| Hague Conference on Private International Law | 海牙国际私法会议 | 简称 HCCH |
| Institut de Droit International | 国际法研究院 | 1873 创立，1904 亦获诺贝尔和平奖 |
| private international law | 国际私法 | 非「国际公法」 |
| compulsory arbitration | 强制仲裁 | Asser 在海牙会议力推的原则 |
| Pious Fund of the Californias Case | 加利福尼亚虔诚基金案 | PCA 首案 |
| The Hague Academy of International Law | 海牙国际法学院 | 1923 成立，Asser 未能亲见 |
| Revue de Droit International et de Législation Comparée | 国际法与比较立法杂志 | 三人共创 |
| T.M.C. Asser Instituut | 阿塞尔研究所 | 以其全名 Tobias Michael Carel 命名 |

---

## 四、背景音乐选择 【人物专属】

- **选定曲目**: **Nostalgy** — AShamaluevMusic（manifest 预分配，勿改）
- **风格**: 忧郁 / 怀旧 / 纪录片
- **匹配理由**: 19 世纪末海牙会议的旧世界外交氛围与「未能亲见 1923 海牙国际法学院」的遗憾感，与 Nostalgy 的怀旧沉思气质契合；叙事从阿姆斯特丹法学世家到海牙机制遗产，是制度演进的纪录而非英雄史诗
- **本地路径**: `music_audio/inspiring-electronic/17-_DA0mdtL-jI-Nostalgy - by AShamaluevMusic ｜ Sad Cinematic Music For Videos, Documentaries & Films.wav`
- **时长对齐**: ffmpeg `-shortest` 自动对齐

---

## 五、关键参考文件清单 【模板通用】

| 文件 | 用途 |
|------|------|
| `peace/presentations/pages/20th_century/Tobias_Asser/page.md` | 本地 Wikipedia 正文（事实基准） |
| `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | 提示词结构标杆 |
| `MySQL/data/Frederick_Sanger.yaml` | yaml 字段母本 |
| `peace/presentations/20th_century/OpenPeace_20th_Century_Nobel_Laureates.md` | 官方获奖理由中译 |
| `peace/nobel_peace_citations.json` | 官方获奖理由英文原文 |
| `MySQL/seed_person.py` | 研究领域 + 社会关系入库引擎 |

> **开始执行。每完成一步汇报。**
> **最重要的事：每写一页就 make，看到溢出就修；所有事实以 page.md 为准，无载禁写。**
