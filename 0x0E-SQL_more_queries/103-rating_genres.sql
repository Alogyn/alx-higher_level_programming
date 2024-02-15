-- Task 20. Best genre (Advanced)
-- This script that lists all genres in the database "hbtn_0d_tvshows_rate" by their rating
SELECT tg.name, SUM(tr.rating) AS rating
FROM tv_genres tg
JOIN tv_show_genres tsg ON tg.id = tsg.genre_id
JOIN tv_shows ts ON tsg.show_id = ts.id
JOIN tv_show_ratings tr ON ts.id = tr.show_id
GROUP BY tg.name
ORDER BY rating DESC;