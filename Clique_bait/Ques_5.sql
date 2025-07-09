WITH total_visits AS (SELECT COUNT(DISTINCT visit_id) AS total 
FROM events)
SELECT (SELECT COUNT(DISTINCT visit_id) 
FROM events e 
JOIN event_identifier ei ON e.event_type = ei.event_type
WHERE ei.event_name = 'Purchase')* 100.0 /(SELECT total FROM total_visits) AS purchase_percentage;