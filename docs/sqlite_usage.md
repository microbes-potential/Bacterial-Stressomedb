# SQLite Usage

The official StressomeDB release is distributed as a single SQLite database.

## View release information

```sql
SELECT * FROM release_info;
```

## Search records

```sql
SELECT stressome_id, gene_symbol, protein_name, organism, stress_category
FROM stressome_records
WHERE gene_symbol LIKE '%oxyR%' OR protein_name LIKE '%OxyR%'
LIMIT 20;
```

## Category summary

```sql
SELECT higher_order_group, stress_category, COUNT(*) AS records
FROM record_categories
GROUP BY higher_order_group, stress_category
ORDER BY records DESC;
```

## Retrieve sequences

```sql
SELECT r.stressome_id, r.gene_symbol, r.organism, p.sequence
FROM stressome_records r
JOIN protein_sequences p ON r.sequence_md5 = p.sequence_md5
WHERE r.gene_symbol LIKE '%dnaK%'
LIMIT 5;
```

## Full text search

```sql
SELECT stressome_id, gene_symbol, protein_name, organism, stress_category
FROM stressome_fts
WHERE stressome_fts MATCH 'oxidative OR oxyR'
LIMIT 20;
```
