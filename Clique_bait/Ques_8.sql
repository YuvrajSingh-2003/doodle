SELECT ph.product_category, 
COUNT(CASE WHEN e.event_type = 1 THEN 1 END) AS page_views,
COUNT(CASE WHEN e.event_type = 2 THEN 1 END) AS cart_adds
FROM events e
JOIN page_hierarchy ph ON e.page_id = ph.page_id
WHERE ph.product_category IS NOT NULL
GROUP BY ph.product_category
ORDER BY page_views DESC;