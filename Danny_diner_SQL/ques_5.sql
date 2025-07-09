SELECT cpc.customer_id, cpc.product_name, cpc.order_count
FROM (
SELECT sales.customer_id, menu.product_name, COUNT(*) AS order_count
FROM sales
INNER JOIN menu ON sales.product_id = menu.product_id
GROUP BY sales.customer_id, menu.product_name
) AS cpc
JOIN (
SELECT customer_id, MAX(order_count) AS max_count
FROM (
SELECT sales.customer_id, menu.product_name, COUNT(*) AS order_count
FROM sales
INNER JOIN menu ON sales.product_id = menu.product_id
GROUP BY sales.customer_id, menu.product_name
) AS sub
GROUP BY customer_id
) AS mc ON cpc.customer_id = mc.customer_id AND cpc.order_count = mc.max_count
ORDER BY cpc.customer_id;