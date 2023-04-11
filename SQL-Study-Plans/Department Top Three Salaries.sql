WITH top3 AS
(
  SELECT d.name AS Department ,e.name AS Employee,e.salary AS Salary ,dense_rank() OVER(PARTITION BY E.departmentID ORDER BY e.salary DESC) AS row_num
  FROM Employee e LEFT JOIN Department d on  e.departmentID=d.id 
)

SELECT Department,Employee,Salary
FROM top3 
WHERE row_num BETWEEN 1 and 3;
