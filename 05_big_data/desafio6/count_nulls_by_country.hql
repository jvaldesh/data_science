select country, count(*) as cantidad
from user_profile 
where gender = '99999' or age = '99999' 
group by country
order by cantidad desc;
