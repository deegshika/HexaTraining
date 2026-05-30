CREATE TABLE products
(
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category VARCHAR(30),
    price DECIMAL(10,2),
    stock_quantity INT,
    supplier_city VARCHAR(30)
);
INSERT INTO products VALUES
(1,'Laptop','Electronics',55000,10,'Hyderabad'),
(2,'Mobile','Electronics',25000,25,'Bangalore'),
(3,'Printer','Electronics',18000,8,'Pune'),
(4,'Office Chair','Furniture',7500,15,'Mumbai'),
(5,'Desk','Furniture',12000,5,'Chennai'),
(6,'Notebook','Stationery',80,200,'Hyderabad'),
(7,'Pen','Stationery',20,500,'Delhi'),
(8,'Water Bottle','Accessories',500,50,'Bangalore');

select product_name,price from products;

select category from products;

select distinct category from products;

select * from products where price > 10000;

select * from products where price > 10000 and category='Electronics';

select * from products where price > 10000 or category='Electronics';

select * from products where not category='Electronics';

select * from products where supplier_city in ('Hyderabad','Delhi');

select * from products where price between 50 and 20000;

select * from products where product_name like 'P%';

select * from products where product_name like '%k';

select * from products where product_name like '%top%';

select product_name as Product , price as Productprice from products;

select * from products order by price desc;

select count(*) from products;

select count(*) from products where category='Electronics';

select sum(price) from products;

select count(*) as TotalProducts,
SUM(price) as Totalprice,
AVG(price) as Averageprice,
MAX(price) as Highestprice,
MIN(price) as Lowestprice 
from products;

select category,count(*) as ProductCount from products group by category;

select category,sum(price) as Totalprice from products group by category;

drop table customers;