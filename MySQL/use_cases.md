# greatminds 数据库 · 用例集

> 适用：当前 337 人 / 万级（10000+）人物扩展后同样有效
> 连接：`mysql -u root greatminds`（已配置默认 utf8mb4，中文/法语重音直接显示）
> 性能原则：见文末「万级数据优化」

---

## 用例 1：交叉奖项得主 + 获奖年限 + 研究领域（核心）

**需求**：找到同时获多个奖项的人，并展示每个奖的获奖年份、研究领域。

**一行查询（视图 `v_cross_summary`）**：

```sql
-- 所有多奖得主（含奖项年限 + 研究领域），按获奖数降序
SELECT name_en, award_count, awards_detail, fields_detail
FROM v_cross_summary
WHERE award_count >= 2
ORDER BY award_count DESC;

-- 只看三料及以上
SELECT * FROM v_cross_summary WHERE award_count >= 3;

-- 只看某人（Serre 三冠全貌）
SELECT * FROM v_cross_summary WHERE name_en = 'J.-P. Serre';
```

**结果示例**：
```
J.-P. Serre    3   菲尔兹奖 1954；沃尔夫数学奖 2000；阿贝尔奖 2003   algebra、algebraic geometry、number theory...
John Milnor    3   菲尔兹奖 1962；沃尔夫数学奖 1989；阿贝尔奖 2011   topology、differential topology...
```

**手工 SQL（不用视图时）**：关键点是**奖项和领域分开聚合再 JOIN**，避免多对多笛卡尔积导致奖项重复计数：

```sql
SELECT p.name_en,
       t.n AS award_count,
       t.awards_detail,
       f.fields_detail
FROM people p
JOIN (  -- ① 奖项聚合
    SELECT person_id, COUNT(DISTINCT award_id) n,
           GROUP_CONCAT(CONCAT(a.name_zh,' ',al.year) ORDER BY al.year SEPARATOR '；') awards_detail
    FROM award_laureate al JOIN awards a ON a.id=al.award_id
    GROUP BY person_id
) t ON t.person_id = p.id
LEFT JOIN (  -- ② 领域聚合
    SELECT pf.person_id, GROUP_CONCAT(DISTINCT f.name_en ORDER BY f.name_en SEPARATOR '、') fields_detail
    FROM person_field pf JOIN fields f ON f.id=pf.field_id
    GROUP BY pf.person_id
) f ON f.person_id = p.id
WHERE t.n >= 2
ORDER BY t.n DESC;
```

---

## 用例 2：指定奖项组合的交叉（如 图灵+阿贝尔）

**需求**：找出同时获得指定两个奖项的人。

```sql
SELECT p.name_en,
       MAX(CASE WHEN a.name_en='ACM A.M. Turing Award' THEN al.year END) AS 图灵奖年份,
       MAX(CASE WHEN a.name_en='Abel Prize'             THEN al.year END) AS 阿贝尔奖年份
FROM award_laureate al
JOIN people p ON p.id = al.person_id
JOIN awards a  ON a.id = al.award_id
WHERE a.name_en IN ('ACM A.M. Turing Award','Abel Prize')
GROUP BY p.id
HAVING COUNT(DISTINCT a.id) = 2;
```

> 通用化：把 `IN (...)` 换成任意奖项组合，`HAVING COUNT(DISTINCT a.id) = N` 控制要求命中几个。

---

## 用例 3：某奖项得主池内，谁还拿了别的奖（潜藏信息）

**需求**：给定一个奖项（如菲尔兹奖），找出其中还有第二奖项的人。

```sql
SELECT p.name_en,
       GROUP_CONCAT(CONCAT(a.name_zh,' ',al.year) ORDER BY al.year SEPARATOR '；') AS 全部奖项
FROM award_laureate al
JOIN people p ON p.id = al.person_id
JOIN awards a  ON a.id = al.award_id
WHERE p.id IN (SELECT person_id FROM award_laureate
               WHERE award_id=(SELECT id FROM awards WHERE name_en='Fields Medal'))
GROUP BY p.id
HAVING COUNT(*) > 1;
```

---

## 用例 4：按研究领域反查交叉得主

**需求**：研究领域是「代数几何」的多奖得主。

```sql
SELECT cs.name_en, cs.award_count, cs.awards_detail
FROM v_cross_summary cs
JOIN person_field pf ON pf.person_id = cs.person_id
JOIN fields f ON f.id = pf.field_id
WHERE f.name_en = 'algebraic geometry' AND cs.award_count >= 2;
```

---

## 用例 5：奖项组合矩阵（哪些两两组合真实存在）

```sql
SELECT * FROM v_award_matrix ORDER BY n_persons DESC;
-- 输出如：阿贝尔×沃尔夫 17、菲尔兹×沃尔夫 16、菲尔兹×阿贝尔 7 ...
```

---

## 用例 6：国籍与历史政权

**需求**：人物的国籍，以及国家改名/消失后的统一查询（100 年前 vs 现在）。

**设计**：`countries` 字典存「现代国 + 历史政权」，历史政权 `is_current=0`、`successor` 指向现代后继国；`person_nationality` 多对多（一人多国籍，含 rank 顺序）。

```sql
-- 某人全部国籍（Hilbert: 普鲁士王国→德意志帝国→魏玛共和国→纳粹德国）
SELECT p.name_en, c.name_zh
FROM person_nationality pn
JOIN people p ON p.id = pn.person_id
JOIN countries c ON c.id = pn.country_id
WHERE p.name_en = 'David Hilbert'
ORDER BY pn.`rank`;

-- 按现代国归一：所有德国籍（含历史政权，国家改名/消失也能查全）
SELECT p.name_en
FROM person_nationality pn
JOIN people p ON p.id = pn.person_id
JOIN countries c ON c.id = pn.country_id
WHERE c.name_en = 'Germany' OR c.successor = 'Germany'
GROUP BY p.id;

-- 多重现代国籍（如 von Neumann: 匈牙利 + 美国）
SELECT p.name_en, COUNT(*) n
FROM person_nationality pn
JOIN people p ON p.id = pn.person_id
JOIN countries c ON c.id = pn.country_id
WHERE c.is_current = 1
GROUP BY p.id HAVING n > 1;
```

---

## 万级数据（10000+）优化要点

## 万级数据（10000+）优化要点

1. **索引已就位**：
   - `people.name_en`（名字查询）、`people.qid`、`people.local_dir`
   - `award_laureate(person_id,award_id,year)` 联合主键 + 单列索引
   - `person_field(person_id,field_id)` + `fields.id` 索引
2. **避免多对多笛卡尔积**：涉及「奖项+领域」等多对多时，**分别聚合（子查询）再 JOIN**（见用例 1 手工 SQL）——这是万级数据的关键写法；
3. **用视图简化**：`v_cross_summary` / `v_multi_award` / `v_award_matrix` 已封装，日常查询走视图；
4. **按需过滤**：查询尽量先缩小范围（`WHERE award_count>=2`、指定奖项），再聚合；
5. **新增 10000+ 人时的建议**：`person_field` 和 `award_laureate` 是增长最快的表，务必保留联合主键去重；批量插入用 `INSERT IGNORE` 防重复。
