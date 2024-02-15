-- Task 19. Rotten tomatoes (Advanced)
-- This script that lists all shows from "hbtn_0d_tvshows_rate" by their rating
SELECT tv_shows.title, SUM(rating) AS rating_sum
FROM tv_shows
JOIN tv_show_rating ON tv_shows.id = tv_show_rating.show_id
GROUP BY tv_shows.title
ORDER BY rating_sum DESC, tv_shows.title ASC;