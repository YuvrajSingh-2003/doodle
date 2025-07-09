SELECT m.customer_id, menu.product_name
FROM members m
INNER JOIN sales s ON m.customer_id = s.customer_id AND s.order_date > m.join_date
INNER JOIN menu ON s.product_id = menu.product_id
WHERE s.order_date = (SELECT MIN(order_date)
FROM sales
WHERE customer_id = m.customer_id AND order_date > m.join_date)
ORDER BY m.customer_id ASC;