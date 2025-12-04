INSERT INTO Products (id, code, name, price, entry_date, brand) VALUES
(1, 'PROD001', 'Gaming Laptop', 150000, '2023-01-15', 'MSI'),
(2, 'PROD002', 'Mechanical Keyboard', 8500, '2023-01-20', 'Razer'),
(3, 'PROD003', 'Wireless Mouse', 5000, '2023-02-01', 'Logitech'),
(4, 'PROD004', 'Curved Monitor', 80000, '2023-02-10', 'Samsung'),
(5, 'PROD005', 'Gaming Headset', 15000, '2023-03-05', 'HyperX');

INSERT INTO Users (id, username, email, registration_date) VALUES
(1, 'Juan Perez', 'juan.perez@example.com', '2022-01-10'),
(2, 'Maria Gonzalez', 'maria.gonzalez@example.com', '2022-02-15'),
(3, 'Pedro Rodriguez', 'pedro.rodriguez@example.com', '2022-03-20');

INSERT INTO Reviews (id, comment, rating, date, product_id) VALUES
(1, 'Excellent laptop, very fast for gaming.', 5, '2023-03-20', 1),
(2, 'The battery drains quickly, but performance is top-notch.', 4, '2023-03-25', 1),
(3, 'Very comfortable keyboard with good feedback.', 5, '2023-04-01', 2),
(4, 'Monitor with vibrant colors and great immersion.', 4, '2023-04-10', 4),
(5, 'Headset with clear sound and a decent microphone.', 3, '2023-04-15', 5);

INSERT INTO PaymentMethod (id, payment_method, bank_name) VALUES
(1, 'Credit Card', 'Banco Nacional'),
(2, 'Sinpe Móvil', 'BAC'),
(3, 'PayPal', NULL);

INSERT INTO Invoices (id, invoice_number, purchase_date, total_amount, user_id, payment_method_id) VALUES
(101, 'INV001', '2023-03-10', 167000, 1, 2),
(102, 'INV002', '2023-03-12', 170000, 2, 1),
(103, 'INV003', '2023-03-15', 15000, 3, 3);

INSERT INTO InvoiceDetails (id, invoice_id, product_id, quantity, total_amount) VALUES
(1, 101, 1, 1, 150000),
(2, 101, 2, 2, 17000),
(3, 102, 4, 2, 160000),
(4, 102, 3, 2, 10000),
(5, 103, 5, 1, 15000),
(6, 103, 3, 1, 5000);

INSERT INTO CartEmail (id, email) VALUES
(1, 'juan.perez@example.com'),
(2, 'maria.gonzalez@example.com'),
(3, 'pedro.rodriguez@example.com');

INSERT INTO ShoppingCart (id, cart_id, product_id, quantity) VALUES
(1, 1, 1, 1),
(2, 1, 2, 2),
(3, 2, 3, 2),
(4, 2, 4, 2),
(5, 3, 3, 1),
(6, 3, 5, 1);


UPDATE Invoices
SET buyer_phone = '69453125',
    cashier_employee_code = '54603'
WHERE id = 101;

UPDATE Invoices
SET buyer_phone = '84569713',
    cashier_employee_code = '67981'
WHERE id = 102;

UPDATE Invoices
SET buyer_phone = '61294834',
    cashier_employee_code = '56813'
WHERE id = 103;
