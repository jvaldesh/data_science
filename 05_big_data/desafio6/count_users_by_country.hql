select country, count(*) as cantidad from user_profile group by country order by cantidad desc;
