# OpenEcon 提示词批量工作流（诺贝尔经济学奖 99 位：20 世纪 46 + 21 世纪 53）

> 本文档是 **agent 批量作业手册**：每个 agent 领取 `prompt_manifest_20th.json`（批次号 econ20th-batch-XX）
> 或 `prompt_manifest_21th.json`（批次号 econ21th-batch-XX）中的一个批次（5 人），
> 为每人生成「人物专属立传提示词 md」+「greatminds 入库 yaml」并执行入库。
> 本阶段 **不写 Beamer tex**——只产出提示词与数据入库。
>
> 学科背景：诺贝尔经济学奖（瑞典央行纪念阿尔弗雷德·诺贝尔经济学奖）1969 年起每年颁发，
> 无未颁奖年份；得主多为在世者，relations 普遍偏少（诚实值可低至 0-2，在提示词注明防 Review 误判）。

## 0. 必读参考（开工前依次读完）

| 顺序 | 文件 | 用途 |
|---|---|---|
| 1 | `physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.md` | ★ 提示词结构标杆（0-11 节） |
| 2 | `medic/presentations/20th_century/Robert_Bárány/Robert_Bárány_zh.md` | 9 节合并版样例（医侧口径） |
| 3 | `economics/PROMPTS_WORKFLOW.md`（本文档） | 批量作业规则与陷阱 |
| 4 | `economics/prompt_manifest_20th.json` / `_21th.json` 中本批次条目 | 人物清单、页面路径、QID、库内 id、BGM/主色预分配 |
| 5 | 每人的 `economics/presentations/pages/{20th,21th}_century/{Dir}/page.md` | ★ 事实基准（唯一事实来源） |
| 6 | 同目录 `metadata.json` | QID/生卒/国籍/导师等结构化参考（仅参考，以 page.md 为准） |

## 1. 每位人物的产出

### 1.1 人物专属提示词：`economics/presentations/{20th,21th}_century/{Dir}/{Dir}_zh.md`

结构对齐 `Kenneth_G_Wilson_zh.md`（约 190–240 行，9-11 节），要点：

```
# 经济学家立传提示词（{Name}）
> 一句话说明：OpenEcon 项目、诺贝尔经济学奖 {year} 年得主、本文件用途
## 0/一、背景信息 【人物专属】
   - 目标经济学家：{Name}（{生卒}）
   - 气质关键词 + 获奖理由（英文原文 + 中文翻译，逐字引用，见下「获奖理由引用规则」）
   - 设计母题（从其核心贡献提炼一个视觉隐喻）
   - 本地 Wikipedia 路径：economics/presentations/pages/{世纪}/{Dir}/page.md
   - 参考模板：physicist/presentations/20th_century/Kenneth_G_Wilson/Kenneth_G_Wilson_zh.tex（骨架）
## 二、任务流程（引用 Physicist_Bio_Prompt_Template.md 第三章，注明「路径按 economics 执行」：
   physicist/presentations/20th_century/Physicist_Bio_Prompt_Template.md）
## 三/5.5、研究领域梳理 + 入库（rank 0-4 表：领域 name_en/中文/说明/对应页）
## 四/5.6、社会关系梳理 + 入库（表：关系类型/对方/方向/note；与 yaml 完全一致）
## 五、配色方案（主色 HTML{#XXXXXX} = manifest 的 main_color，与人物气质呼应；
   香槟金诺奖色 + badgeA-D 四分类色 + 背景母题说明）
## 六、幻灯片序列（15 页规划：00 OpenEcon 共享首页 → 01 封面 → 02 身份信息页 → … → 结尾）
## 七、特殊陷阱表（★ 核心：5-10 条易错点：年份归属、共同研究者、机构、奖项混淆、
        获奖理由表述、metadata.json 与 page.md 冲突时以 page.md 为准的裁定）
## 八、术语清单（英文/中文/风险点，6-10 条）
## 九、背景音乐选择（manifest 预分配 BGM + 匹配理由；音乐库 music_audio/，参考 curated_tracks.md）
```

**获奖理由引用规则**：
- 共享理由年份：manifest 条目 `citation_en`/`citation_zh` 已直接给出，逐字用。
- **拆分理由年份（2000 / 2002 / 2003 / 2009 / 2018 / 2021 / 2025）**：manifest 中 citation 为空，
  必须从 `economics/nobel_economics_citations.json` 按 `year`+`name` 找到**本人那一条**citation
  （中文翻译参照 `economics/economics_list_data.py` 中该年 `||` 拆分后的对应段，与获奖者顺序一一对应）。
- 引言红线：中文引号内不得写「原话」，除非 page.md 有英文原文（引原文+译文）。
- 目录名 `{Dir}` 与 yaml 文件名必须与 `pages/{世纪}/{Dir}` 完全一致（manifest 已给出，勿改名）。

硬性要求：
- **只写 page.md 有载的事实**；metadata-only 的导师/学生一律不入库，可在陷阱表注明「metadata 有载不入库」。

### 1.2 入库 yaml：`MySQL/data/{Dir}.yaml`

格式照抄 `MySQL/data/Steven_Chu.yaml`（字段：name_en/qid/name_zh/gender/birth_date/description/
primary_occupation/has_biography/occupations/fields/nationalities/relations）：

- `name_en`：**与 manifest 的 `db_name_en`（库内既有者）或 `name`（新建者）逐字一致**（数据库匹配键）
- `qid`：manifest 已给出，直接填
- `name_zh`：manifest 的 name_zh
- `primary_occupation: economist`（或按 page.md 实际取最主要者，如 statistician）
- `has_biography: false`（Beamer 未做；立传后另置 1）
- `occupations`：2-4 条（rank 0 为主职业）
- `fields`：3-5 条，与提示词第三节一致（rank 0 = 获奖核心领域）
- `nationalities`：manifest `country` 字段按 " / " 拆成多条（Wikipedia 口径）
- `relations`：**只收 page.md 明载的关系**；类型白名单：`advisor-student`（direction: advisor=对方是导师 /
  student=对方是学生）、`colleague`、`co-honored`（同届共享得主必写，note 写官方理由短语）、`spouse`、
  `parent-child`、`influence`、`controversy`、`collaborator`
- **note 陷阱**：note 若以双引号开头或含「: 」，整条 note 用单引号包裹；note 首选中文、简洁（≤40 字）
- **对手方规范名**：写 yaml 前先查库确定对手方 name_en：
  ```bash
  cd /Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL && python3 -c "
  import sys; sys.path.insert(0,'.')
  from db_mysql import get_conn
  conn=get_conn(); cur=conn.cursor()
  cur.execute(\"SELECT id,name_en FROM people WHERE name_en LIKE %s\", ('%Friedman%',))
  print(cur.fetchall())
  "
  ```
  库内有规范记录的对手方**必须用库内 name_en**（防止分裂 stub）；库内没有的用 page.md frontmatter
  形式新建（seed_person 自动建 stub）。注意经济学家可能与图灵奖/数学/物理侧库内记录重叠（如
  Herbert A. Simon、Kenneth Arrow、John von Neumann），一律复用库内记录。
- 共享年份的 `co-honored` 关系对手方写同届共享得主（manifest 同年份者），对手方 yaml 归属其本人批次写反向边。

### 1.3 特殊裁定：已入库者跳过

- **manifest `db_social=1` 者（如 Herbert A. Simon，图灵奖 1975 侧已完整入库）：照常写提示词 md 与 yaml
  （yaml 存档不入库，文件头注明「已由图灵奖侧入库，此 yaml 仅存档」），不执行 seed_person。**
- `db_social=0` 但有库内记录者（如 Kenneth Arrow id=2639、Wassily Leontief id=1453、Gunnar Myrdal id=7062、
  Oliver E. Williamson id=1408、Lloyd Shapley id=968）：正常入库，seed_person 幂等 UPD 回填 qid。

### 1.4 入库执行（每人）

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

方向约定（seed_person.py 实现语义）：`advisor-student` + `direction: advisor` = 对方是导师
（from=对方, to=本人）；`direction: student` = 对方是学生（from=本人, to=对方）；`parent-child` 同理
（parent/child）；其余类型无向（from<to 自动归一）。

预期：`has_social_data=1`、fields/relations 条数与 yaml 一致。**若对手方撞唯一键报错，参照 merge 规则：
删冲突行→改指→from<to 归一→去重→删 stub。**

## 2. 批次纪律

- 每人完成后在批次报告记录：`{Dir} | fields=N | relations=M | 对手方规范名调整情况 | 特殊裁定`。
- 批次全部完成后 send_message 向主控汇报（一行/人 + 遇到的裁定）。
- **禁止**：改动总表 md、改名/挪动 pages/ 下任何文件、写 tex/Beamer、给 metadata-only 关系建边。
- 遇 page.md 与总表国籍/理由不一致：以 page.md 为准，并在提示词第七节记录裁定。

## 3. 已知全局陷阱（历史经验，直接沿用）

| 陷阱 | 处理 |
|---|---|
| page.md frontmatter 双值（生卒两说） | 以 page.md 正文为准，yaml 填正文值，陷阱表注明 |
| 同名/消歧义目录（Oliver_Hart_economist 等） | name_en 用 manifest 形式（label 无消歧义后缀）；对手方查库用规范名 |
| 共享年份 co-honored | 同届两两互写，note 用官方理由短语（拆分年份注意本人那条 citation） |
| metadata.json 有载但 page.md 无载的家人/学生/导师 | 一律不入库 |
| note 含「: 」或以引号开头 | yaml 用单引号包裹 |
| 21 世纪得主在世、relations 少 | 诚实值，提示词注明「仅 page.md 明载 X 条」防 Review 误判 |
| write_to_file 长内容故障 | filePath 放参数首位；单次写入 ≤8KB，超长用 heredoc 分块落盘 |
| 跨学科库内重叠（Simon/Arrow/von Neumann 等） | 对手方复用库内记录，勿新建分裂 stub |
