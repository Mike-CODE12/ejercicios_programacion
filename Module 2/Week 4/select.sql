SELECT Books.name AS book_name, Authors.name AS author_name
FROM Books AS Books
INNER JOIN Authors AS Authors
ON Books.author_id = Authors.id;


SELECT Books.name AS book_name
FROM Books AS Books
LEFT JOIN Authors AS Authors
ON Books.author_id = Authors.id
WHERE Authors.id IS NULL;


SELECT Authors.name AS author_name
FROM Books AS Books
RIGHT JOIN Authors AS Authors
ON Books.author_id = Authors.id
WHERE Books.id IS NULL;


SELECT Books.name AS book_name
FROM Books AS Books
INNER JOIN Rents AS Rents
ON Books.id = Rents.book_id;


SELECT Books.name AS book_name
FROM Books AS Books
LEFT JOIN Rents AS Rents
ON Books.id = Rents.book_id
WHERE Rents.id IS NULL;


SELECT Customers.name AS customer_name, Customers.email
FROM Rents AS Rents
RIGHT JOIN Customers AS Customers
ON Rents.customer_id = Customers.id
WHERE Rents.customer_id IS NULL;


SELECT Books.name AS book_name
FROM Books AS Books
INNER JOIN Rents AS Rents
ON Books.id = Rents.book_id
WHERE Rents.state = 'Overdue';