SELECT 
  ph.page_name, 
  COUNT(*) AS page_views
FROM events AS e
JOIN page_hierarchy AS ph
  ON e.page_id = ph.page_id
WHERE e.event_type = 1 
GROUP BY ph.page_name
ORDER BY page_views DESC