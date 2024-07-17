WITH latest_partitions AS (
    SELECT
        table_name,
        partition_date,
        ROW_NUMBER() OVER (PARTITION BY table_name ORDER BY partition_date DESC) AS rn
    FROM (
        SELECT 
            table_name,
            CAST(partition_name AS DATE) AS partition_date
        FROM information_schema.partitions
        WHERE table_schema = 'your_database'
    )
),
valid_partitions AS (
    SELECT 
        p.table_name,
        p.partition_date,
        COUNT(t.*) AS record_count
    FROM latest_partitions p
    JOIN your_database.your_table t
    ON p.partition_date = t.partition_date
    WHERE p.rn <= 5
    GROUP BY p.table_name, p.partition_date
    HAVING COUNT(t.*) > 0
)
SELECT 
    table_name,
    partition_date,
    record_count
FROM (
    SELECT 
        table_name,
        partition_date,
        record_count,
        ROW_NUMBER() OVER (PARTITION BY table_name ORDER BY partition_date DESC) AS rn
    FROM valid_partitions
)
WHERE rn <= 5
ORDER BY table_name, partition_date DESC;
