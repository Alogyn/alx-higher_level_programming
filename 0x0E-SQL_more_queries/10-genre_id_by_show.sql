-- Task 10. Genre ID by show
-- This script that lists all shows contained in "hbtn_0d_tvshows"
-- that have at least one genre linked
SELECT ts.title, tsg.genre_id
FROM tv_shows AS ts
JOIN tv_show_genres AS tsg ON ts.id = tsg.show_id
ORDER BY ts.title ASC, tsg.genre_id ASC;