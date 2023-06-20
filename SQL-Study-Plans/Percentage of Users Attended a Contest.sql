# Write your MySQL query statement below
WITH CTE AS
(
    SELECT COUNT(DISTINCT user_id)
    FROM users
)
SELECT contest_id,ROUND(COUNT(user_id)/(SELECT * FROM CTE)*100,2) as percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC,contest_id ASC;
