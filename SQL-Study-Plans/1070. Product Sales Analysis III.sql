# Write your MySQL query statement below
WITH cte AS
(
    SELECT S.product_id as product_id,
    S.year as first_year,S.quantity as quantity,
    S.price as price ,RANK() OVER(PARTITION BY S.product_id ORDER BY S.year ASC) as row_num
    FROM Sales S INNER JOIN Product P
    ON S.product_id = P.product_id
    
)
SELECT product_id,first_year,quantity,price
FROM cte
WHERE row_num = 1;
