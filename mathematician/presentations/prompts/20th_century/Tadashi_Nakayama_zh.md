# Tadashi Nakayama（中山正）立传提示词

> 榜单：#90 · 1912-07-26 – 1964-05-21 · 日本数学家
> 数据库主记录：id=90（`Nakayama Tadashi`，与 id=503 `Tadasi Nakayama` 重复已合并）
> ⚠️ 说明：本地 Wikipedia 页面为消歧页（Q7674366），正确页面为 `Tadashi Nakayama (mathematician)`；因用户要求不重新抓取，本提示词基于数据库已有数据 + 学术共识编写，需人工复核细节。

---

## 1. 背景信息（用于 Slide 1-3）

- **姓名**：中山 正（Tadashi Nakayama / Tadasi Nakayama，中山正）
- **生卒**：1912-07-26 → 1964-06-05，享年 51
- **国籍**：日本
- **身份**：数学家（代数学）
- **机构轨迹**：
  - 教育：东京大学 + 大阪大学（师从高木贞治 Teiji Takagi 与正田建次郎 Kenjirō Shōda 双导师）
  - 任职：大阪大学、名古屋大学
- **研究领域**：群论、环论、表示论、抽象代数

## 2. 核心叙事亮点（用于 Slide 4-9）

1. **中山引理（Nakayama lemma）**：交换代数/表示论中最常用的基本工具之一——有限生成模的生成元与极大理想关系的核心引理（与 Nakayama 完备化、Auslander–Nakayama 相关）。
2. **Brauer–Nakayama 理论**：与 Richard Brauer 合作的群表示论工作（Brauer 模块/块理论方向）。
3. **Nakayama 完备化**：局部环完备化的相关概念。
4. **日本代数几何与环论学派**：京都大学代数传统（高木贞治→中山正→其后学）的代表。
5. **中日数学交流**：曾在中国任教（抗战时期）——需谨慎核实。

## 3. 配色方案

| 用途 | 色值 | 说明 |
|---|---|---|
| 主色（京都红） | #8B1A1A | 京都大学传统 |
| 辅助（环论青） | #1E6E6E | 交换代数与环论 |
| 强调（引理金） | #B8860B | 中山引理 |
| 背景 | #FAF6EF | 米白纸色 |

## 4. 12 页 Slide 规划

1. 封面：大标题 + 副标题「中山引理 · Brauer–Nakayama 理论 · 日本代数学」
2. 生平总览：时间轴（1912 → 京都大学 → 名古屋 → 1964 去世）
3. 中山引理：有限生成模与极大理想
4. 中山引理的证明与等价形式
5. Brauer–Nakayama 理论：群表示论合作
6. Nakayama 完备化：局部环
7. 高木贞治与京都代数传统
8. 日本代数学派：环论/表示论
9. 与 Brauer/Artin/Hasse 的交流
10. 学术遗产：Auslander–Nakayama 等后续发展
11. 文献：主要论文与《代数学》讲义
12. 终章：51 岁早逝、历史地位

## 5. 史实陷阱与敏感点（终审必须检查）

- **消歧页限制**：本地页面是消歧页，**本提示词的细节（中日教学经历等）需基于权威来源人工核实**后才可写入立传正文。
- **中山引理归属**：Nakayama lemma 以中山正命名，但引理的精确表述有多个等价版本（Nakayama 1940s）——注意归属。
- **Brauer 合作**：Richard Brauer(63) 的合作关系已在库——"Brauer–Nakayama 理论"共同命名。
- **导师**：高木贞治（Teiji Takagi, 500）——京都代数传统。
- **英年早逝**：1964 年 51 岁去世，事业巅峰期。
- **拼写**：Nakayama Tadashi（日式顺序）/ Tadasi Nakayama（旧罗马字）——库名 Nakayama Tadashi。
- **qid**：当前占位为消歧页 qid=Q7674366，**正确数学家 qid 需后续核实替换**（英文维基数学家页面）。

## 6. 数据库字段核对表（§21.5）

| 字段 | 值 | 状态 |
|---|---|---|
| qid | Q324943（正确数学家页面） | 需更新 |
| name_zh | 中山正 | 保持 |
| birth_date | 1912-07-26 | 已迁移 |
| death_date | 1964-06-05 | 已迁移 |
| has_biography | 0 | 保持 |
| has_social_data | 1 | 本次置 1 |

## 7. 社会关系入库清单（§20，已由 seed 脚本完成）

- 导师：Teiji Takagi（500）
- 合作者：Richard Brauer（63，Brauer–Nakayama）、Emil Artin（13）、Helmut Hasse（409）、Saunders Mac Lane（39）

## 8. 奖项清单

- （metadata 未列，待核）

## 9. 机构清单

- 教育：Kyoto University（新建）
- 任职：Kyoto University（新建）、Nagoya University（新建）

## 10. 终审清单

- [ ] qid 占位需后续核实
- [ ] 中山引理归属表述
- [ ] 中日教学经历需核实
- [ ] 英年早逝叙事
- [ ] has_biography 保持 0
## 11. Review 流程规范（两轮 Review，§16 Wikipedia 终审 + 项目标准）

> 立传完成后按此规范执行两轮 Review（参照 #73 Fredholm Review-1 执行标准）。

### 第 1 轮（Review-1）：事实终审
- [ ] **结合本地 Wikipedia**：读取 `pages/<Name>/page.md` 建立事实基准，逐页对照 Beamer tex 的全部事实（生卒/机构/年份/奖项/荣誉/家族/引语）
- [ ] **头像**：优先使用 Wikipedia infobox 照片（`images.txt` 或 infobox `image` 字段），下载原图到 `images/<name>_portrait.jpg`；无照片时用装饰圆替代
- [ ] **国籍**：封面顶部徽章明确国籍（`\faIcon{globe}\enspace <Country>`），与 Cartan/Borel/Fredholm 立传格式一致
- [ ] **引语核对**：tex 引语必须能在 Wikipedia 原文找到（§14.6 伪引语红线）；找不到则改为忠实转述
- [ ] **编译验证**：`make distclean && make`（latexmk 自动多遍编译；remember picture 需要多遍）
- [ ] **更新提示词**：Review 修正（头像来源/国籍/新细节）写回 `prompts/<Name>_zh.md`
- [ ] **更新排行榜**：`✅/🔲` → `✅/✅✅`

### 第 2 轮（Review-2）：结构优化
- [ ] 检查 Overfull/Underfull 告警（<10pt 可接受）
- [ ] 结束页时间线 ≥7 段拆两行（避免溢出）
- [ ] 中文标点/断行/间距统一
- [ ] 与同榜数学家格式对齐（封面/配色/结构）
- [ ] 排行榜标记 `✅✅/🔲` → `✅✅/✅✅`

---

## Review-1 记录 (2026-08-13)

> 结合本地 Wikipedia (`pages/Tadashi_Nakayama/page.md`) 逐页比对。

- **头像** ✅：`Tadashi_Nakayama.jpg` 原在根目录（`\graphicspath` 只搜 images/ 会找不到），已复制到 `images/Tadashi_Nakayama.jpg` 并采用 Cartan/Sinai 标准格式（圆角矩框 + `\includegraphics[width=1.92cm]` + `yshift=-1.51cm`）
- **国籍** ✅：封面 `\faIcon{globe}\enspace Japan\enspace·\enspace 表示论\enspace·\enspace 中山引理`（原 `\faIcon{globe}\quad Japan...` → 统一 `\enspace Japan`，字号 12/16 → 14/18；Wikidata nationality: ["Japan", "Empire of Japan"]）
- **身份信息页** ✅：已有 `\earlyslide`（Slide 3 "早年与教育"），涵盖东京府出生、双导师、大阪/名古屋任职——无需新增
- **⚠️ 提示词事实错误修正**（tex 内容本身正确，提示词有误）：
  1. **死亡日期**：提示词写 `1964-05-21`（错误）→ Wikipedia 明确 `June 5, 1964`（`1964-06-05`），tex 写"1964 年 6 月 5 日"正确；已修正提示词 death_date
  2. **机构**：提示词写"京都大学"（错误，基于消歧页猜测）→ Wikipedia 明确 `educated_at: University of Tokyo + University of Osaka`，tex 写"东京大学与大阪大学"正确；已修正提示词
  3. **导师**：提示词只写"高木贞治"（不完整）→ Wikipedia 明确 `doctoral_advisor: ["Teiji Takagi", "Kenjirō Shōda"]` 双导师，tex 写"高木贞治与正田建次郎"正确；已补充提示词
  4. **qid**：提示词写 `Q7674366（占位消歧页）` → 正确数学家页面 `Q324943`；已修正
- **修正**：
  1. **头像位置**：根目录 → images/（否则 `\graphicspath` 找不到）
  2. **修正 hookslide badge d 机构错误**：`日本代数学\\Takagi/Shōda\\京都传统` → `日本代数学\\东京/大阪`（中山正机构是东京/大阪，非京都；"京都"系提示词错误渗透）
  3. **封面 badge 统一**：4 个 badge 3 行 → 2 行
  4. **section title 字号**：`\fontsize{17}{20.5}` → `\fontsize{20}{24}`；副标题 `6.5/8.5` → `7.5/9.5`
  5. **封面国籍行字号**：`\fontsize{12}{16}` → `\fontsize{14}{18}`
  6. **去"据 Wikipedia："**：封面引语去前缀
  7. **英文名行**：`1912 -- 1964` → `1912--1964`（去空格）
- **事实复核**（tex 内容与 Wikipedia 一致）：生卒 1912-07-26 ~ 1964-06-05（51 岁）/东京府出生/东京大学+大阪大学学位/双导师 Takagi+Shōda/大阪+名古屋任职/访问 Princeton+Illinois+Hamburg/中山引理/Nakayama 代数/Nakayama 猜想/Murnaghan–Nakayama 规则/拟 Frobenius 代数（1939/1941 Annals 两篇）/日本学士院奖 ✅
- **编译**：`make distclean && make` → ✅ 13页，0错误；hbox 5.33pt + vbox 6.58pt 均 <10pt 可接受 → Review-2 处理
- **排行榜**：#90 保持 `✅/✅✅`（榜单已预标记，本轮完成第1轮实际 review）

