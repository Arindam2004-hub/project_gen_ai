few_shots = [
    {
        'Question': "Find the top 5 customers by total spending (only successful orders), showing their name, city, and total spent?",
        'SQLQuery': """SELECT c.customer_name, 
       c.city, 
       SUM(o.price * o.quantity) AS total_spent
FROM customers_langchain c
JOIN orders_langchain o 
    ON c.customer_id = o.customer_id
WHERE o.order_status = 'Successful'
GROUP BY c.customer_name, c.city
ORDER BY total_spent DESC
LIMIT 5;""",
        'SQLResult': "Result of the SQL query",
        'Answer': "[('Samiha Das', 'Delhi', 80740.13), ('Shayak Apte', 'Kolkata', 76989.51000000001), ('Aradhya Comar', 'Chennai', 71508.94000000002), ('Vidur Srinivas', 'Delhi', 71355.56), ('Hazel Bhalla', 'Kolkata', 70251.92)]"},
    {'Question': "Find the total number of cancelled orders for each city?",
     'SQLQuery': """SELECT c.city, COUNT(*) AS cancelled_orders
FROM customers_langchain c
JOIN orders_langchain o ON c.customer_id = o.customer_id
WHERE o.order_status = 'Cancelled'
GROUP BY c.city
ORDER BY cancelled_orders DESC;
""",
     'SQLResult': "Result of the SQL query",
     'Answer': "[('Delhi', 168), ('Ahmedabad', 164), ('Pune', 157), ('Chennai', 153), ('Kolkata', 149), ('Mumbai', 148), ('Surat', 146), ('Hyderabad', 142), ('Bengaluru', 135), ('Jaipur', 117)]"},
    {'Question': "Show the average price per dish per city for only successful orders?",
     'SQLQuery': """SELECT c.city, o.dish_ordered, 
       ROUND(AVG(o.price), 2) AS avg_price
FROM customers_langchain c
JOIN orders_langchain o ON c.customer_id = o.customer_id
WHERE o.order_status = 'Successful'
GROUP BY c.city, o.dish_ordered
ORDER BY c.city, avg_price DESC;
""",
     'SQLResult': "Result of the SQL query",
     'Answer': "[('Ahmedabad', 'Tandoori Chicken', 566.65), ('Ahmedabad', 'Butter Chicken', 560.1), ('Ahmedabad', 'Samosa', 554.07), ('Ahmedabad', 'Chole Bhature', 553.14), ('Ahmedabad', 'Paneer Tikka', 549.75), ('Ahmedabad', 'Biryani', 537.01), ('Ahmedabad', 'Dosa', 534.01), ('Ahmedabad', 'Pav Bhaji', 529.12), ('Ahmedabad', 'Dal Makhani', 512.09), ('Ahmedabad', 'Aloo Paratha', 498.31), ('Bengaluru', 'Biryani', 577.32), ('Bengaluru', 'Pav Bhaji', 561.79), ('Bengaluru', 'Dosa', 559.35), ('Bengaluru', 'Paneer Tikka', 556.57), ('Bengaluru', 'Aloo Paratha', 554.9), ('Bengaluru', 'Butter Chicken', 539.87), ('Bengaluru', 'Samosa', 539.82), ('Bengaluru', 'Dal Makhani', 519.16), ('Bengaluru', 'Tandoori Chicken', 514.37), ('Bengaluru', 'Chole Bhature', 498.03), ('Chennai', 'Dosa', 576.48), ('Chennai', 'Samosa', 564.3), ('Chennai', 'Biryani', 563.59), ('Chennai', 'Paneer Tikka', 548.42), ('Chennai', 'Pav Bhaji', 547.52), ('Chennai', 'Dal Makhani', 546.43), ('Chennai', 'Chole Bhature', 540.17), ('Chennai', 'Aloo Paratha', 535.75), ('Chennai', 'Butter Chicken', 533.24), ('Chennai', 'Tandoori Chicken', 527.08), ('Delhi', 'Dal Makhani', 563.4), ('Delhi', 'Butter Chicken', 559.83), ('Delhi', 'Chole Bhature', 557.75), ('Delhi', 'Pav Bhaji', 555.12), ('Delhi', 'Samosa', 552.88), ('Delhi', 'Aloo Paratha', 550.34), ('Delhi', 'Biryani', 547.9), ('Delhi', 'Paneer Tikka', 545.86), ('Delhi', 'Dosa', 526.61), ('Delhi', 'Tandoori Chicken', 489.61), ('Hyderabad', 'Dal Makhani', 565.81), ('Hyderabad', 'Dosa', 558.69), ('Hyderabad', 'Paneer Tikka', 546.6), ('Hyderabad', 'Butter Chicken', 543.98), ('Hyderabad', 'Pav Bhaji', 543.86), ('Hyderabad', 'Samosa', 540.81), ('Hyderabad', 'Tandoori Chicken', 539.58), ('Hyderabad', 'Aloo Paratha', 539.4), ('Hyderabad', 'Biryani', 535.07), ('Hyderabad', 'Chole Bhature', 489.02), ('Jaipur', 'Dosa', 575.51), ('Jaipur', 'Biryani', 572.6), ('Jaipur', 'Dal Makhani', 559.54), ('Jaipur', 'Aloo Paratha', 541.72), ('Jaipur', 'Chole Bhature', 530.54), ('Jaipur', 'Samosa', 529.04), ('Jaipur', 'Butter Chicken', 528.15), ('Jaipur', 'Pav Bhaji', 515.13), ('Jaipur', 'Tandoori Chicken', 501.13), ('Jaipur', 'Paneer Tikka', 499.81), ('Kolkata', 'Pav Bhaji', 597.44), ('Kolkata', 'Biryani', 597.02), ('Kolkata', 'Aloo Paratha', 578.19), ('Kolkata', 'Chole Bhature', 576.62), ('Kolkata', 'Samosa', 566.76), ('Kolkata', 'Dal Makhani', 566.4), ('Kolkata', 'Butter Chicken', 560.32), ('Kolkata', 'Tandoori Chicken', 560.23), ('Kolkata', 'Paneer Tikka', 559.64), ('Kolkata', 'Dosa', 549.64), ('Mumbai', 'Paneer Tikka', 585.32), ('Mumbai', 'Biryani', 572.42), ('Mumbai', 'Aloo Paratha', 549.28), ('Mumbai', 'Pav Bhaji', 545.36), ('Mumbai', 'Chole Bhature', 541.81), ('Mumbai', 'Tandoori Chicken', 537.01), ('Mumbai', 'Dosa', 533.14), ('Mumbai', 'Samosa', 514.71), ('Mumbai', 'Dal Makhani', 505.3), ('Mumbai', 'Butter Chicken', 491.19), ('Pune', 'Chole Bhature', 569.01), ('Pune', 'Dal Makhani', 568.13), ('Pune', 'Butter Chicken', 564.47), ('Pune', 'Biryani', 556.11), ('Pune', 'Dosa', 552.33), ('Pune', 'Paneer Tikka', 546.53), ('Pune', 'Samosa', 529.16), ('Pune', 'Tandoori Chicken', 528.77), ('Pune', 'Aloo Paratha', 508.92), ('Pune', 'Pav Bhaji', 498.8), ('Surat', 'Paneer Tikka', 587.17), ('Surat', 'Tandoori Chicken', 573.6), ('Surat', 'Chole Bhature', 559.94), ('Surat', 'Aloo Paratha', 550.6), ('Surat', 'Dal Makhani', 548.15), ('Surat', 'Butter Chicken', 547.68), ('Surat', 'Biryani', 538.37), ('Surat', 'Pav Bhaji', 534.19), ('Surat', 'Samosa', 533.2), ('Surat', 'Dosa', 511.57)]"},
    {'Question': "Find the city with the highest revenue per customer, considering only successful orders.?",
     'SQLQuery': """SELECT city, 
       ROUND(SUM(price * quantity) / COUNT(DISTINCT c.customer_id), 2) AS revenue_per_customer
FROM customers_langchain c
JOIN orders_langchain o ON c.customer_id = o.customer_id
WHERE o.order_status = 'Successful'
GROUP BY city
ORDER BY revenue_per_customer DESC
;
""",
     'SQLResult': "Result of the SQL query",
     'Answer': "[('Kolkata', 47480.01), ('Hyderabad', 45227.38), ('Delhi', 44976.06), ('Surat', 44822.89), ('Chennai', 44608.11), ('Ahmedabad', 43630.37), ('Bengaluru', 43147.7), ('Pune', 42647.88), ('Jaipur', 42499.34), ('Mumbai', 41537.72)]"},
    {'Question': "For each city, find the top-selling dish by quantity sold.?",
     'SQLQuery': """SELECT city, dish_ordered, total_qty
FROM (
    SELECT c.city, o.dish_ordered, SUM(o.quantity) AS total_qty,
           RANK() OVER (PARTITION BY c.city ORDER BY SUM(o.quantity) DESC) AS rnk
    FROM customers_langchain c
    JOIN orders_langchain o ON c.customer_id = o.customer_id
    GROUP BY c.city, o.dish_ordered
) ranked
WHERE rnk = 1;
""",
     'SQLResult': "Result of the SQL query",
     'Answer': "[('Ahmedabad', 'Chole Bhature', Decimal('541')), ('Bengaluru', 'Aloo Paratha', Decimal('493')), ('Chennai', 'Dosa', Decimal('612')), ('Delhi', 'Samosa', Decimal('588')), ('Hyderabad', 'Dosa', Decimal('547')), ('Jaipur', 'Aloo Paratha', Decimal('399')), ('Kolkata', 'Dal Makhani', Decimal('538')), ('Kolkata', 'Biryani', Decimal('538')), ('Mumbai', 'Paneer Tikka', Decimal('503')), ('Pune', 'Butter Chicken', Decimal('474')), ('Surat', 'Pav Bhaji', Decimal('465'))]"
     },
    {'Question': "What is the total revenue generated from all successful orders?",
     'SQLQuery': """SELECT 
    order_status, 
    SUM(price * quantity) AS total_sell
FROM orders_langchain
WHERE order_status = 'Successful'
GROUP BY order_status;
 """,
     'SQLResult': "Result of the SQL query",
     'Answer': "22060271.25000009"
     }

]