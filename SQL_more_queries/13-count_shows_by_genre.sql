-- This script counts the number of shows linked to each genre.
-- We join tv_genres with tv_show_genres to count shows per genre.
-- Only genres with at least one show are displayed.
-- Results are sorted by number of shows descending.

USE hbtn_0d_tvshows;

SELECT tv_genres.name AS genre,
       COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;