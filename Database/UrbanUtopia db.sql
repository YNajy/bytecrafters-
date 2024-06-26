DROP DATABASE IF EXISTS urbanutopia;
CREATE DATABASE urbanutopia;
USE urbanutopia;

CREATE TABLE Registration (
    UserID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100) UNIQUE,
    Password VARCHAR(100),
    RegistrationDate DATETIME
);

CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100) UNIQUE,
    Password VARCHAR(100),
    City VARCHAR(100),
    Phone VARCHAR(20),
    Location VARCHAR(255)
);
ALTER TABLE Customers
ADD COLUMN RegistrationID INT;

ALTER TABLE Customers
ADD CONSTRAINT fk_customers_registration
FOREIGN KEY (RegistrationID)
REFERENCES Registration(UserID);


CREATE TABLE Employees (
    EmployeeID INT PRIMARY KEY AUTO_INCREMENT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Email VARCHAR(100) UNIQUE,
    Password VARCHAR(100),
    Position VARCHAR(100)
);
ALTER TABLE Employees
ADD COLUMN RegistrationID INT;

ALTER TABLE Employees
ADD CONSTRAINT fk_employees_registration
FOREIGN KEY (RegistrationID)
REFERENCES Registration(UserID);


CREATE TABLE Products (
    ProductID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255),
    Description TEXT,
    Price DECIMAL(10, 2),
    Size VARCHAR(20), 
    Category ENUM('Women Clothing', 'Men Clothing'),
    Available INT DEFAULT 0
);


CREATE TABLE ShoppingCart (
    CartID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerID INT,
    ProductID INT,
    Quantity INT,
    Size VARCHAR(20),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);


CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,
    CustomerID INT,
    OrderDate DATETIME,
    TotalAmount DECIMAL(10, 2),
    Status ENUM('Pending', 'Processing', 'Shipped', 'Delivered'),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);


CREATE TABLE OrderDetails (
    OrderDetailID INT PRIMARY KEY AUTO_INCREMENT,
    OrderID INT,
    ProductID INT,
    Quantity INT,
    Size VARCHAR(20),
    Price DECIMAL(10, 2),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
);


CREATE TABLE Delivery (
    DeliveryID INT PRIMARY KEY AUTO_INCREMENT,
    OrderID INT,
    DeliveryDate DATETIME,
    ShippingAddress VARCHAR(255),
    City VARCHAR(100),
    State VARCHAR(100),
    ZipCode VARCHAR(20),
    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID)
);
ALTER TABLE Delivery
ADD COLUMN UserID INT,
ADD CONSTRAINT fk_delivery_registration FOREIGN KEY (UserID) REFERENCES Registration(UserID);

