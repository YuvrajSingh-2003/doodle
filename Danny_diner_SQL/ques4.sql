SELECT 
  menu.product_name,
  COUNT(sales.product_id) AS most_purchased_item
FROM sales
INNER JOIN menu
  ON sales.product_id = menu.product_id
GROUP BY menu.product_name
ORDER BY most_purchased_item DESC