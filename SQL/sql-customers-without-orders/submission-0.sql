-- Write your query below
SELECT c.name
FROM customers As c
LEFT JOIN orders AS o ON c.id = o.customer_id
WHERE o.customer_id IS NULL