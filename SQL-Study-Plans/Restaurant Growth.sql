# Write your MySQL query statement below
# Write your MySQL query statement below
with cte as (
select 
adddate(visited_on,6) as visited_on,
sum(amount) over(order by visited_on rows between 0 preceding and 6 following) amount,
round(sum(amount) over(order by visited_on rows between 0 preceding and 6 following)/7,2) average_amount
from 
(
  select visited_on,sum(amount) amount from customer group by 1 order by visited_on
) t
)

select * from cte where visited_on in (select visited_on from customer)
order by visited_on
