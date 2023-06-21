# Write your MySQL query statement below
WITH CTE AS
(
    SELECT turn,person_id,person_name,weight,SUM(Weight) OVER(ORDER BY turn) as total_weight
    FROM Queue
    ORDER BY turn
)
SELECT person_name 
FROM CTE
WHERE total_weight<=1000
ORDER BY total_weight DESC
LIMIT 1
