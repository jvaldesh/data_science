select user_profile.country, corr(user_profile.age, artists.plays) as correlacion from user_profile
inner join artists on artists.user_sha = user_profile.usersha and artist_name = 'metallica'
group by user_profile.country
order by correlacion asc;
