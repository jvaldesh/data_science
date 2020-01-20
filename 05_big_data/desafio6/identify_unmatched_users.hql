select count(*) from user_profile 
where usersha not in (select user_sha from artists);
