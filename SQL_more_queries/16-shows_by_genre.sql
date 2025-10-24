-- This script lists all shows and their genres.
-- Shows without genres will display NULL for the genre name.
-- We use LEFT JOINs to include all shows, even those without genres.
-- Results are sorted by show title and genre name ascending.

USE hbtn_0d_tvshows;

SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;