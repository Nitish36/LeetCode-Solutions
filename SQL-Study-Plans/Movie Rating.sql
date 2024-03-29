# Write your MySQL query statement be
(SELECT u.name as results
FROM Users u 
INNER JOIN MovieRating M
ON u.user_id = M.user_id
Group By u.user_id 
Order by count(u.user_id) desc, u.name limit 1)

union all
(Select m.title as results
from MovieRating as r, Movies as m
where m.movie_id = r.movie_id 
and r.created_at like "2020-02-%"
Group By r.movie_id 
Order by avg(r.rating) desc, m.title limit 1);
