SELECT s.customer_id, 
SUM(CASE WHEN s.product_id = 1 THEN m.price * 20 
ELSE m.price * 10                         
END) AS total_points
FROM sales s
JOIN menu m ON s.product_id = m.product_id
GROUP BY s.customer_id
ORDER BY s.customer_id;