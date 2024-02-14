-- Task 18. Temperatures #0
-- This script that displays the average temperature (Fahrenheit)
-- by city ordered by temperature (descending)
SELECT `city`, AVG(`value`) AS `avg_temp`
FROM `temperatures`
GROUP BY `city`
ORDER BY `avg_temp` DESC;