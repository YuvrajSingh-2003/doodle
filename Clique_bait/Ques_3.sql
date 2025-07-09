SELECT COUNT(DISTINCT visit_id) AS unique_visits
FROM events
WHERE event_time >= '2020-03-01' AND event_time < '2020-08-01';