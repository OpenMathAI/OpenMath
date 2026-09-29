# OpenMedic 提示词批量工作流（20 世纪 172 人 + 21 世纪 60 人）

> 本文档是 **agent 批量作业手册**：每个 agent 领取 `prompt_manifest_20th.json`（20 世纪，批次号 med-batch-XX）
> 或 `prompt_manifest_21th.json`（21 世纪，批次号 med21-batch-XX）中的一个批次（5 人），
> 为每人生成「人物专属立传提示词 md」+「greatminds 入库 yaml」并执行入库。
> 本阶段 **不写 Beamer tex**——只产出提示词与数据入库。
>
> **21 世纪批次路径替换规则**：世纪目录一律用 `21th_century`——提示词写在
> `presentations/21th_century/{Dir}/{Dir}_zh.md`，页面读
> `presentations/pages/21th_century/{Dir}/page.md`，其余规则完全相同。
> 21 世纪特有注意：①得主多为在世者，relations 普遍偏少（诚实值可低至 1-2，在提示词注明防 Review 误判）；
> ②2025 年三人为最新得主，page.md 可能偏短，事实基准更严格地逐句对应；③共享年份分组以
> nobel_medicine_citations.json 的拆分为准（如 2011=2+1 Steinman 单独、2015=2+1 屠呦呦单独）。

## 0. 必读参考（开工前依次读完）

| 顺序 | 文件 | 用途 |
|---|---|---|
| 1 | `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | ★ 提示词结构标杆（11 节） |
| 2 | `medic/PROMPTS_WORKFLOW.md`（本文档） | 批量作业规则与陷阱 |
| 3 | `medic/prompt_manifest_20th.json` 中本批次条目 | 人物清单、页面路径、QID、BGM 预分配 |
| 4 | 每人的 `presentations/pages/20th_century/{Dir}/page.md` | ★ 事实基准（唯一事实来源） |
| 5 | 同目录 `metadata.json` | QID/生卒/国籍/导师等结构化参考（仅参考，以 page.md 为准） |

## 1. 每位人物的产出

### 1.1 人物专属提示词：`presentations/20th_century/{Dir}/{Dir}_zh.md`

结构对齐 `Kenneth_G_Wilson_zh.md`（约 180–240 行），节数可合并为以下 9 节：

```
# 医学家立传提示词（{Name}）
> 一句话说明：OpenMedic 项目、20 世纪诺贝尔生理学或医学奖 {year} 年得主、本文件用途
## 一、背景信息 【人物专属】
   - 目标医学家：{Name}（{生卒}）
   - 气质关键词 + 诺奖获奖理由（英文原文 + 中文翻译，逐字引自 page.md/nobel_medicine_citations.json）
   - 设计母题（从其核心发现提炼一个视觉隐喻）
   - 本地 Wikipedia 路径：medic/presentations/pages/20th_century/{Dir}/page.md
   - 参考模板：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）
## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章，注明「第 0/1/2/3 步按 medic 路径执行」）
## 三、研究领域梳理 + 入库（rank 0-4 表：领域 name_en/中文/说明/对应页）
## 四、社会关系梳理 + 入库（表：关系类型/对方/方向/note；与 yaml 完全一致）
## 五、配色方案（主色 HTML{#XXXXXX} 与人物气质呼应 + 香槟金诺奖色 + badgeA-D 四分类色 + 背景母题说明）
## 六、幻灯片序列（15 页规划：00 OpenMedic 首页 → 01 封面 → 02 身份信息页 → … → 结尾）
## 七、特殊陷阱表（★ 核心：从 page.md 提炼 5-10 条易错点：年份归属、共同发现者、机构、奖项混淆、
        获奖理由表述、metadata.json 与 page.md 冲突时以 page.md 为准的裁定）
## 八、术语清单（英文/中文/风险点，6-10 条）
## 九、背景音乐选择（用 manifest 预分配的 BGM，写明匹配理由；音乐库 music_audio/，选曲参考 curated_tracks.md）
```

硬性要求：
- **只写 page.md 有载的事实**；metadata-only 的导师/学生一律不入库、可在陷阱表注明「metadata 有载不入库」。
- 获奖理由必须逐字引用 `medic/nobel_medicine_citations.json` 中该年份的 citation（共享年份注意分组拆分后的归属）。
- 引言红线：中文引号内不得写"原话"，除非 page.md 有英文原文（引原文+译文）。
- 目录名 `{Dir}` 与 yaml 文件名必须与 `pages/20th_century/{Dir}` 完全一致（manifest 已给出，勿改名）。

### 1.2 入库 yaml：`MySQL/data/{Dir}.yaml`

格式照抄 `MySQL/data/Steven_Chu.yaml`（字段：name_en/qid/name_zh/gender/birth_date/description/primary_occupation/has_biography/occupations/fields/nationalities/relations）：

- `name_en`：**与 manifest 的 name_en 逐字一致**（数据库匹配键）
- `qid`：manifest 已给出（已抓取 Wikidata），直接填
- `name_zh`：manifest 的 name_zh
- `primary_occupation: scientist`（或 physician/physiologist 等按 page.md 实际，取最主要者）
- `has_biography: false`（Beamer 未做；立传后另置 1）
- `occupations`：2-4 条（rank 0 为主职业）
- `fields`：3-5 条，与提示词第三节一致（rank 0 = 诺奖核心领域）
- `nationalities`：按 Nobel 官方口径（即总表国籍列）
- `relations`：**只收 page.md 明载的关系**；类型白名单：`advisor-student`（direction: advisor=对方是导师 / student=对方是学生）、`colleague`、`co-honored`（同届共享得主必写，note 写官方理由短语）、`spouse`、`parent-child`、`influence`、`controversy`、`collaborator`
- **note 陷阱**：note 若以双引号开头或含「: 」，整条 note 用单引号包裹；note 首选中文、简洁（≤40 字）
- **对手方规范名**：写 yaml 前先查库确定对手方 name_en：
  ```bash
  cd MySQL && python3 -c "
  import sys; sys.path.insert(0,'.')
  from db_mysql import get_conn
  conn=get_conn(); cur=conn.cursor()
  cur.execute(\"SELECT id,name_en FROM people WHERE name_en LIKE %s\", ('%Krebs%',))
  print(cur.fetchall())
  "
  ```
  库内有规范记录的对手方（如 Francis Crick、James Watson）**必须用库内 name_en**（防止分裂 stub）；库内没有的用 page.md frontmatter 形式新建（seed_person 自动建 stub）。
- 共享年份的 `co-honored` 关系对手方写同届共享得主（manifest 同年份者），对手方 yaml 归属其本人批次写反向边。

### 1.3 入库执行（每人）

```bash
cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL
python3 seed_person.py data/{Dir}.yaml --dry-run   # 先预览
python3 seed_person.py data/{Dir}.yaml             # 幂等入库
```

入库后自验（每人必做）：

```bash
python3 -c "
import sys; sys.path.insert(0,'.')
from db_mysql import get_conn
conn=get_conn(); cur=conn.cursor()
cur.execute('SELECT id,name_en,qid,has_social_data FROM people WHERE name_en=%s', ('{Name}',))
print(cur.fetchall())
cur.execute('SELECT COUNT(*) FROM person_relation WHERE from_id=%s OR to_id=%s', (pid, pid))
print('relations:', cur.fetchone())
"
```

方向约定（seed_person.py 实现语义）：`advisor-student` + `direction: advisor` = 对方是导师（from=对方, to=本人）；`direction: student` = 对方是学生（from=本人, to=对方）；`parent-child` 同理（parent/child）；其余类型无向（from<to 自动归一）。

预期：`has_social_data=1`、fields/relations 条数与 yaml 一致。**若对手方撞唯一键报错，参照 merge 规则：删冲突行→改指→from<to 归一→去重→删 stub。**

## 2. 批次纪律

- 每人完成后在批次报告记录：`{Dir} | fields=N | relations=M | 对手方规范名调整情况 | 特殊裁定`。
- 五人全部完成后 send_message 向主控汇报（一行/人 + 遇到的裁定）。
- **禁止**：改动总表 md、改名/挪动 pages/ 下任何文件、写 tex/Beamer、给 metadata-only 关系建边。
- 遇 page.md 与总表国籍/理由不一致：以 page.md 为准，并在提示词第七节记录裁定。

## 3. 已知全局陷阱（历史经验，直接沿用）

| 陷阱 | 处理 |
|---|---|
| page.md frontmatter 双值（生卒两说） | 以 page.md 正文为准，yaml 填正文值，陷阱表注明 |
| 同名人物（如 "John Macleod (physiologist)"） | name_en 用 manifest 形式；对手方查库用规范名 |
| 共享年份 co-honored | 三人组两两互写，note 用官方理由短语（medic/nobel_medicine_citations.json 已按组拆分） |
| metadata.json 无载但 page.md 亦无载的家人/学生 | 一律不入库 |
| note 含「: 」或以引号开头 | yaml 用单引号包裹 |
