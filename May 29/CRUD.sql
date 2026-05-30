create database retail_db;

use retail_db;

create table customers(customerid INT,customername VARCHAR(100), city VARCHAR(100));

INSERT INTO customers values(1,'Rahul','Hyderabad'),(2,'Priya','Bangalore'),(3,'Amit','Mumbai');

SELECT * FROM customers;

UPDATE customers set city='chennai' where customerid=1;

SET SQL_SAFE_UPDATES=0;

UPDATE customers set city='chennai' where customerid=1;

SET SQL_SAFE_UPDATES=1;

delete from customers where city='Bangalore';

create table products(productid INT PRIMARY KEY,product_name varchar(100),category varchar(50),price DECIMAL(10,2),stock INT,supplier_city VARCHAR(50));

INSERT INTO products values(1,'Laptop','Electronics',55000,10,'Hyderabad');

SELECT * FROM products;

SET SQL_SAFE_UPDATES=0;

update products set stock=7 where product_name='Laptop';

delete from products where price=55000;

select * from products;

drop table products;
