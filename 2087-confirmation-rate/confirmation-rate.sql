# Write your MySQL query statement below
WITH ConfirmationStats AS (
    SELECT 
        s.user_id,
        COUNT(CASE WHEN c.action = 'confirmed' THEN 1 END) AS confirmed_count,
        COUNT(c.user_id) AS total_requests
    FROM 
        Signups s
    LEFT JOIN 
        Confirmations c
    ON 
        s.user_id = c.user_id
    GROUP BY 
        s.user_id
)
SELECT 
    user_id,
    ROUND(COALESCE(confirmed_count * 1.0 / total_requests, 0), 2) AS confirmation_rate
FROM 
    ConfirmationStats;