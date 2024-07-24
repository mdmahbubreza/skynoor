CREATE DATABASE flights;

USE flights;

CREATE TABLE flights (
    id INT AUTO_INCREMENT PRIMARY KEY,
    origin VARCHAR(50),
    destination VARCHAR(50),
    departure_date DATE,
    airline VARCHAR(50),
    price DECIMAL(10, 2)
);

INSERT INTO flights (origin, destination, departure_date, airline, price) VALUES
('Pune', 'Delhi', '2024-08-01', 'Air India', 5000.00),
('Pune', 'Delhi', '2024-08-01', 'SpiceJet', 4500.00),
('Pune', 'Delhi', '2024-08-01', 'IndiGo', 4700.00);
