SELECT 
sales.customer_id, 
COUNT(*) AS items_purchased, 
SUM(menu.price) AS total_spent
FROM sales
JOIN members ON sales.customer_id = members.customer_id AND sales.order_date < members.join_date
JOIN menu ON sales.product_id = menu.product_id
GROUP BY sales.customer_id
ORDER BY sales.customer_id;