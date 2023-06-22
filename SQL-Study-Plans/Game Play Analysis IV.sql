select round(count(distinct player_id )/(select count(distinct player_id) from activity),2) as fraction
from (
select player_id,event_date,
min(event_date) over (partition by player_id order by event_date) firstlog
from activity ) a
where datediff(event_date,firstlog) = 1
