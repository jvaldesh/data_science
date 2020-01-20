CREATE TABLE user_profile(
    usersha STRING,
    gender STRING,
    age INT,
    country STRING,
    join_date STRING
) ROW FORMAT DELIMITED
FIELDS TERMINATED BY '|';

CREATE TABLE artists(
    user_sha STRING,
    artist_sha STRING,
    artist_name STRING,
    plays INT
) ROW FORMAT DELIMITED
FIELDS TERMINATED BY '|';
