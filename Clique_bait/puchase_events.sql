SELECT DISTINCT e.visit_id
FROM events e 
JOIN event_identifier ei ON e.event_type = ei.event_type
WHERE ei.event_name = 'Purchase';