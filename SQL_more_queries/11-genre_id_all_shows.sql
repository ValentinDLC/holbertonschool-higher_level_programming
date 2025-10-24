-- This script lists all TV shows and their genre_id if they have one.
-- Shows without genres will display NULL for genre_id.
-- We use LEFT JOIN to include all shows, even those without genres.
-- Results are sorted by tv_shows.title and genre_id ascending.

USE hbtn_0d_tvshows;

SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;