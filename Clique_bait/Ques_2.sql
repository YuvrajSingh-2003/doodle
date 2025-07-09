SELECT ROUND(AVG(cookie_count), 0) AS avg_cookies_per_user
FROM (SELECT user_id, 
COUNT(cookie_id) AS cookie_count
FROM users
GROUP BY user_id) 
AS user_cookies;