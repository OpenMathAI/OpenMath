# 图灵奖得主 社会关系入库 · 共享工作流（1975–2025 批次，68 人）

> 并行 agent 共享规范。目标：为每人写一份 YAML 数据文件（**只写 yaml，不碰数据库**），主控随后统一用 `seed_person.py` 顺序灌库。

## 1. 交付物

每人一个文件：`/Users/ericksun/workspace/codebuddy/OpenMathAI/MySQL/data/{DirName}.yaml`
- `{DirName}` 与提示词目录名一致（如 `Allen_Newell.yaml`、`Tim_Berners-Lee.yaml`）
- 格式黄金参照：`MySQL/data/Johann_Bernoulli.yaml`（先读它）

## 2. 事实来源与优先级

1. 各人提示词 `turing/presentations/{DirName}/{DirName}_zh.md` 的 **§1 背景 / §6 字段表 / §7 社会关系清单 / §8 奖项 / §9 机构**——这是主要来源（已据本地 Wikipedia 提炼）
2. 需要补充细节（领域全称、任职年份、获奖年份）时读本地 Wikipedia 文本：先用 PROMPTS_WORKFLOW §2 的 bs4 配方把 `turing/pages/{year}/{Title}/index.html` 转文本再读
3. 冲突以本地 Wikipedia 为准；提示词 §5 明令禁写的关系（如"恩怨无载"）**绝不入库**

## 3. YAML 字段规范（全字段）

```yaml
name_en: <必填！用 §4 映射表的库内名，勿用 Wikipedia 标题>
qid: <turing/qid_map.json 中该人的 QID，必填>
name_zh: <中文惯称>
name_variants: [别名拼写]          # 可选，来自 Wikipedia 别名
gender: male|female                # 女性：Allen / Liskov / Goldwasser
birth_date: 'YYYY-MM-DD'           # 提示词 §6；仅知年时写 'YYYY-01-01' 禁止——写 'YYYY' 也禁止，只填确定精度，月日未知则不填该字段并加注释
death_date: 'YYYY-MM-DD'           # 在世者整个字段省略
description: American computer scientist (1930-2002)   # 英文一句，含生卒年
primary_occupation: computer scientist
has_biography: true
occupations:                       # rank 0 = computer scientist，其余按 Wikipedia
- name_en: computer scientist
  name_zh: 计算机科学家
  rank: 0
fields:                            # 研究领域，rank 0 = 主领域；4-8 条；enwiki 常用名 + 中文
- name_en: algorithms
  name_zh: 算法
  rank: 0
nationalities:                     # 按 Wikipedia/提示词，多重国籍并列
- name_en: United States
  name_zh: 美国
  rank: 0
institutions:                      # education + employment（带年份，未知年份省略 start/end_year）
- name_en: Carnegie Mellon University
  name_zh: 卡内基梅隆大学
  relation: education
- name_en: IBM
  name_zh: IBM
  relation: employment
  start_year: 1956
awards:                            # 提示词 §8 全部奖项；共享奖项用 share_type
- name_en: ACM Turing Award
  name_zh: 图灵奖
  year: 1975
  share_type: 共享                  # 独享/共享
  note: 与 Herbert A. Simon 共获    # 可选
relations:                         # 提示词 §7 全部条目；类型见 §5
- type: advisor-student
  person: George Polya             # person 用 §4 映射表的规范名
  note: 博士导师
  direction: advisor               # advisor=对方是本人导师 / student=对方是本人学生 / 省略=无向
```

**日期精度规则**：月日齐全才写完整日期；只有年份时该字段省略（不要编造月日）。Wigderson/Barto/Sutton/Bennett 等页面只有年份者照此处理。

## 4. name_en 映射（★最重要）

yaml 的 `name_en` 必须与 greatminds 库内记录一致，否则会重复建人。68 人映射：

- **与 Wikipedia 标题不同（6 人，注意！）**：
  - Stephen Cook → `Stephen A. Cook`
  - Jim Gray (computer scientist) → `Jim Gray`
  - Robert Kahn → `Robert E. Kahn`
  - Martin Hellman → `Martin E. Hellman`
  - David Patterson (computer scientist) → `David A. Patterson`
  - Charles H. Bennett (physicist) → `Charles H. Bennett`
- **其余 62 人 name_en = Wikipedia 标题**（如 Allen Newell、Tony Hoare、Butler W. Lampson、Ronald Rivest、Frances E. Allen、Fernando J. Corbató（含重音）、Tim Berners-Lee 等）
- relations 中引用另一位得主义务必用上表规范名（如引 Hoare 写 `Tony Hoare`、引 Kahn 写 `Robert E. Kahn`）；引用库外人物用标准英文名（如 Claude Shannon、Alan Turing、Richard Bellman）

## 5. 关系类型与方向（seed_person 语义）

| type | direction | 含义 |
|---|---|---|
| advisor-student | advisor | person 是本人的导师 |
| advisor-student | student | person 是本人的学生 |
| advisor-student | （省略） | 无向师生（少用） |
| parent-child | parent / child | 父母 / 子女 |
| collaborator | （省略） | 合作者（无向，自动归一 from<to） |
| colleague | （省略） | 同事 |
| rival / controversy | （省略） | 竞争/论战（须页面实载） |
| spouse | （省略） | 配偶 |

- 每条关系必须有 note（一句中文，含事实依据，如"1959 论文《Finite Automata and Their Decision Problem》合作者"）
- 只录提示词 §7 与本地 Wikipedia 实载的关系；"无载禁写"者不入库

## 6. 领域与职业用词（保持库内一致性）

- 职业（occupations）常用：computer scientist 计算机科学家 / mathematician 数学家 / physicist 物理学家 / engineer 工程师 / university teacher 大学教师 / entrepreneur 企业家 / inventor 发明家
- 领域（fields）用 enwiki 常用小写名：artificial intelligence 人工智能 / algorithms 算法 / computational complexity theory 计算复杂性理论 / cryptography 密码学 / database 数据库 / operating systems 操作系统 / programming language 编程语言 / computer architecture 计算机体系结构 / machine learning 机器学习 / computer graphics 计算机图形学 / distributed computing 分布式计算 / numerical analysis 数值分析 / formal verification 形式化验证 / quantum information science 量子信息科学 等。拿不准先查 `SELECT name_en FROM fields` 现有词条（只读查询允许），避免同义分裂（如 cryptography vs cryptology 二选一，优先已存在者）

## 7. 禁止事项

- **禁止连接数据库写库**（seed 由主控统一执行）；只读 SELECT 允许
- 禁止编造提示词/Wikipedia 之外的关系、奖项、年份
- 禁止在 relations 里给"无直接互动记载"的两位得主观造关系（如同域≠关系）
- 共享奖得主之间：合作/同奖关系可写 `collaborator`（note 注明"同获 YYYY 图灵奖"）仅当页面实载有实质合作；否则不入库
- YAML 中日期一律加引号（'1930-05-11'），避免 YAML 把 05 当八进制

## 8. 汇报

全部写完后向 main 汇报：完成清单、每人的 relations 条数、fields 条数、发现的事实疑点。
