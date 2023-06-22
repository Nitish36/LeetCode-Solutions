# Write your MySQL query statement below
#delivery date = order date Then immediate other wise scheduled
SELECT round(SUM(IF(order_date = customer_pref_delivery_date,1,0))/count(*)*100,2) as immediate_percentage
FROM Delivery
WHERE (customer_id,order_date) IN
(
    SELECT customer_id,min(order_date) FROM Delivery GROUP BY customer_id
)
