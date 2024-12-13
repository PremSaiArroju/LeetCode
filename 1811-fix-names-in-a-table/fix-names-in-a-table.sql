# Write your MySQL query statement below
SELECT
    user_id,
    CONCAT(UPPER(SUBSTRING(TRIM(name), 1, 1)), LOWER(SUBSTRING(TRIM(name), 2))) AS name
FROM
    Users
ORDER BY
    user_id;