-- This script lists all Comedy shows.
-- We join tv_shows with tv_show_genres and tv_genres.
-- We filter for shows where the genre name is 'Comedy'.
-- Results are sorted by show title ascending.

USE hbtn_0d_tvshows;

SELECT tv_shows.title
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;