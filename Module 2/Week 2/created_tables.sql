CREATE TABLE Products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code CHAR(6) UNIQUE NOT NULL,
    name VARCHAR(80) NOT NULL,
    price INTEGER NOT NULL,
    entry_date TIMESTAMP  NOT NULL,           
    brand VARCHAR(25) NOT NULL
);
CREATE TABLE Reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    comment VARCHAR(255) NOT NULL,
    rating SMALLINT NOT NULL,                  
    date TIMESTAMP NOT NULL,
    product_id INT NOT NULL REFERENCES Products(id)
);
CREATE TABLE Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(25) UNIQUE NOT NULL ,
    email VARCHAR(25) UNIQUE NOT NULL,
    registration_date TIMESTAMP NOT NULL
);
CREATE TABLE PaymentMethod (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    payment_method VARCHAR(20) NOT NULL,
    bank_name VARCHAR(20)
);
CREATE TABLE Invoices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_number CHAR(6) UNIQUE NOT NULL,
    purchase_date TIMESTAMP NOT NULL,
    total_amount INTEGER NOT NULL,
    buyer_phone CHAR(8) NOT NULL,
    cashier_employee_code CHAR(5) NOT NULL,
    user_id INTEGER NOT NULL REFERENCES Users(id),
    payment_method_id INTEGER NOT NULL REFERENCES PaymentMethod(id)
);
CREATE TABLE InvoiceDetails (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    invoice_id INTEGER NOT NULL REFERENCES Invoices(id),
    product_id INTEGER NOT NULL REFERENCES Products(id),
    quantity SMALLINT NOT NULL CHECK (quantity > 0),
    total_amount INTEGER NOT NULL CHECK (total_amount > 0)
);
CREATE TABLE CartEmail (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(25) UNIQUE NOT NULL
);
CREATE TABLE ShoppingCart (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cart_id INTEGER NOT NULL REFERENCES CartEmail(id),
    product_id INTEGER NOT NULL REFERENCES Products(id),
    quantity SMALLINT NOT NULL CHECK (quantity > 0)
);
