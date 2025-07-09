SELECT 
  sales.customer_id, 
  menu.product_name
FROM sales
INNER JOIN menu
  ON sales.product_id = menu.product_id
WHERE sales.order_date = (
  SELECT MIN(order_date)
  FROM sales AS s
  WHERE s.customer_id = sales.customer_id
)
GROUP BY sales.customer_id, menu.product_name;