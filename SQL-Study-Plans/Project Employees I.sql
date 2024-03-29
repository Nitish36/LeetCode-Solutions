# Write your MySQL query statement below
SELECT P.project_id,ROUND(AVG(experience_years),2) as average_years
FROM Project P
INNER JOIN Employee E
ON P.employee_id = E.employee_id
GROUP BY P.project_id;
