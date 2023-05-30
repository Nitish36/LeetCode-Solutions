WITH CTE AS
(
    SELECT id,num,LAG(num,1) OVER() as lagged,LEAD(num,1) OVER() as leads
    FROM Logs
)
SELECT DISTINCT num as ConsecutiveNums
FROM CTE
WHERE num = lagged and num = leads;
