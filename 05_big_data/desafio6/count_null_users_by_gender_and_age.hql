select gender, age, count(*) 
from user_profile 
where gender = '99999' and age = '99999' 
group by gender, age;
