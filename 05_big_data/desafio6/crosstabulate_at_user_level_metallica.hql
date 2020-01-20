select country, gender, age, count(*) as cantidad from user_profile
where usersha in (select user_sha from artists where artist_name = 'metallica')
group by country, gender, age
order by cantidad desc;
