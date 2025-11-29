-- Write a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating
-- You can use only one SELECT statement
-- The database name will be passed as an argument of the mysql command
SELECT tv_genres.name AS name, SUM(ratings.rating) AS rating_sum FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
JOIN ratings ON tv_show_genres.show_id = ratings.show_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
