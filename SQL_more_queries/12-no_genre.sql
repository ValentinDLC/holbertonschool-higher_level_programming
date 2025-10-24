-- This script lists all TV shows that have NO genre linked.
-- If a show has no genre, the genre_id will appear as NULL.
-- We use a LEFT JOIN to include all shows, then filter for NULL genres.
-- Results are sorted by tv_shows.title ascending.

USE hbtn_0d_tvshows;

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC;