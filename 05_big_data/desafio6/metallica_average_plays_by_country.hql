select user_profile.country, avg(artists.plays) as promedio from user_profile
inner join artists on artists.user_sha = user_profile.usersha and artist_name = 'metallica'
group by user_profile.country
order by promedio desc;
