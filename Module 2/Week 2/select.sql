SELECT *
FROM Products;


SELECT *
FROM Products
WHERE price > 50000;


SELECT *
FROM InvoiceDetails
WHERE product_id = 3;


SELECT 
    product_id,
    SUM(quantity) AS total_quantity,
    SUM(total_amount) AS total_amount
FROM InvoiceDetails
GROUP BY product_id;


SELECT *
FROM Invoices
WHERE user_id = 3;


SELECT *
FROM Invoices
ORDER BY total_amount DESC;


SELECT *
FROM Invoices
WHERE invoice_number = 'INV002';