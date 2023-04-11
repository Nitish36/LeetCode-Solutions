# Write your MySQL query statement below
SELECT ROUND(SUM(tiv_2016),2) as tiv_2016
FROM Insurance
WHERE tiv_2015 IN (SELECT tiv_2015 FROM Insurance GROUP BY tiv_2015 HAVING COUNT(tiv_2015)>1)
AND
CONCAT(LAT,LON) NOT IN (SELECT concat(LAT,LON) FROM Insurance GROUP BY LAT,LON HAVING COUNT(concat(LAT,LON))>1);
