-- PART_1

create database mysql_capstone;
use mysql_capstone;

CREATE TABLE customers
(
 customer_id INT PRIMARY KEY,
 customer_name VARCHAR(100),
 city VARCHAR(50),
 state VARCHAR(50),
 gender VARCHAR(10),
 membership_type VARCHAR(30)
);

CREATE TABLE products
(
 product_id INT PRIMARY KEY,
 product_name VARCHAR(100),
 category VARCHAR(50),
 price DECIMAL(10,2)
);

CREATE TABLE orders
(
 order_id INT PRIMARY KEY,
 customer_id INT,
 order_date DATE,
 order_status VARCHAR(30)
);

CREATE TABLE order_items
(
 item_id INT PRIMARY KEY,
 order_id INT,
 product_id INT,
 quantity INT
);

CREATE TABLE payments
(
 payment_id INT PRIMARY KEY,
 order_id INT,
 payment_mode VARCHAR(30),
 payment_status VARCHAR(30),
 amount DECIMAL(10,2)
);

CREATE TABLE deliveries
(
 delivery_id INT PRIMARY KEY,
 order_id INT,
 delivery_partner VARCHAR(50),
 delivery_status VARCHAR(30),
 delivery_city VARCHAR(50)
);

alter table orders add foreign key(customer_id) references customers(customer_id);

alter table order_items add foreign key(order_id) references orders(order_id);

alter table order_items add foreign key(product_id) references products(product_id);

alter table payments add foreign key(order_id) references orders(order_id);

alter table deliveries add foreign key(order_id) references orders(order_id);

-- PART_2

insert into customers values
(1,'Rahul Sharma','Hyderabad','Telangana','Male','Gold'),
(2,'Priya Reddy','Bangalore','Karnataka','Female','Silver'),
(3,'Amit Kumar','Mumbai','Maharashtra','Male','Gold'),
(4,'Sneha Patel','Chennai','Tamil Nadu','Female','Bronze'),
(5,'Arjun Verma','Delhi','Delhi','Male','Silver'),
(6,'Neha Singh','Pune','Maharashtra','Female','Gold'),
(7,'Kiran Rao','Hyderabad','Telangana','Male','Bronze'),
(8,'Divya Sharma','Chennai','Tamil Nadu','Female','Silver'),
(9,'Vikram Gupta','Bangalore','Karnataka','Male','Gold'),
(10,'Meera Nair','Kochi','Kerala','Female','Silver');

insert into products values
(101,'Laptop','Electronics',55000),
(102,'Mobile Phone','Electronics',25000),
(103,'Headphones','Electronics',2000),
(104,'T-Shirt','Fashion',1200),
(105,'Shoes','Fashion',3500),
(106,'Watch','Accessories',5000),
(107,'Backpack','Fashion',1800),
(108,'Desk Chair','Furniture',7000),
(109,'Coffee Maker','Home Appliances',4500),
(110,'Bluetooth Speaker','Electronics',3000);

insert into orders values
(1001,1,'2026-01-05','Delivered'),
(1002,2,'2026-01-10','Shipped'),
(1003,3,'2026-01-15','Cancelled'),
(1004,1,'2026-01-18','Delivered'),
(1005,4,'2026-01-20','Pending'),
(1006,5,'2026-01-25','Delivered'),
(1007,6,'2026-02-01','Shipped'),
(1008,7,'2026-02-05','Delivered'),
(1009,8,'2026-02-10','Pending'),
(1010,9,'2026-02-12','Delivered'),
(1011,10,'2026-02-15','Cancelled'),
(1012,2,'2026-02-18','Delivered'),
(1013,3,'2026-02-20','Shipped'),
(1014,5,'2026-02-25','Pending'),
(1015,6,'2026-03-01','Delivered');

insert into order_items values
(1,1001,101,1),
(2,1001,103,2),
(3,1002,102,1),
(4,1003,104,3),
(5,1004,105,1),
(6,1005,106,2),
(7,1006,107,1),
(8,1007,108,1),
(9,1008,109,1),
(10,1009,110,2),
(11,1010,101,1),
(12,1011,104,2),
(13,1012,102,1),
(14,1013,103,2),
(15,1014,105,1),
(16,1015,106,1),
(17,1002,107,2),
(18,1004,108,1),
(19,1008,109,2),
(20,1012,110,1);

insert into payments values
(201,1001,'UPI','Success',59000),
(202,1002,'Card','Success',25000),
(203,1003,'UPI','Failed',3600),
(204,1004,'Net Banking','Success',3500),
(205,1005,'Cash','Pending',10000),
(206,1006,'UPI','Success',1800),
(207,1007,'Card','Success',7000),
(208,1008,'UPI','Success',4500),
(209,1009,'Cash','Pending',6000),
(210,1010,'Card','Success',55000),
(211,1011,'UPI','Failed',2400),
(212,1012,'Net Banking','Success',28000),
(213,1013,'UPI','Success',4000),
(214,1014,'Cash','Pending',5000),
(215,1015,'Card','Success',5000);

insert into deliveries values
(301,1001,'Delhivery','Delivered','Hyderabad'),
(302,1002,'BlueDart','Shipped','Bangalore'),
(303,1003,'Ecom Express','Cancelled','Mumbai'),
(304,1004,'Delhivery','Delivered','Hyderabad'),
(305,1005,'BlueDart','Pending','Chennai'),
(306,1006,'Ecom Express','Delivered','Delhi'),
(307,1007,'Delhivery','Shipped','Pune'),
(308,1008,'BlueDart','Delivered','Hyderabad'),
(309,1009,'Ecom Express','Pending','Chennai'),
(310,1010,'Delhivery','Delivered','Bangalore'),
(311,1011,'BlueDart','Cancelled','Kochi'),
(312,1012,'Ecom Express','Delivered','Bangalore'),
(313,1013,'Delhivery','Shipped','Mumbai'),
(314,1014,'BlueDart','Pending','Delhi'),
(315,1015,'Ecom Express','Delivered','Pune');

-- PART_3
-- Exercise 1
select * from customers;

-- Exercise 2
select customer_name,city,membership_type from customers;

-- Exercise 3
select * from products order by price desc;

-- Exercise 4
select * from customers where city="Hyderabad";

-- Exercise 5
select * from customers where membership_type="Gold";

-- Exercise 6
select * from products where price between 500 and 5000;

-- Exercise 7
select * from products where category in("Electronics","Fashion");

-- Exercise 8
select * from orders where order_date>"2026-01-01";

-- Exercise 9
select * from payments where payment_mode="UPI";

-- Exercise 10
select * from deliveries where delivery_status="Pending";

-- PART_4
-- Exercise 11
select count(*) from customers;

-- Exercise 12
select count(*) from orders;

-- Exercise 13
select count(*) from products;

-- Exercise 14
select sum(amount) from payments where payment_status="Success";

-- Exercise 15
select avg(amount) from payments;

-- Exercise 16
select max(amount) from payments;

-- Exercise 17
select min(amount) from payments;

-- Exercise 18
select city,count(*) from customers group by city;

-- Exercise 19
select category,count(*) from products group by category;

-- Exercise 20
select order_status,count(*) from orders group by order_status;

-- PART_5
-- Exercise 21
select c.customer_name,o.order_id,o.order_date from customers c join orders o on c.customer_id=o.customer_id;

-- Exercise 22
select oi.order_id,p.product_name,oi.quantity,p.price from order_items oi join products p on oi.product_id=p.product_id;

-- Exercise 23
select c.customer_name,p.product_name,oi.quantity,o.order_date from customers c join orders o on c.customer_id=o.customer_id join order_items oi on o.order_id=oi.order_id join products p on oi.product_id=p.product_id;

-- Exercise 24
select o.order_id,p.payment_mode,p.payment_status,p.amount from orders o join payments p on o.order_id=p.order_id;

-- Exercise 25
select o.order_id,d.delivery_partner,d.delivery_status from orders o join deliveries d on o.order_id=d.order_id;

-- Exercise 26
select c.customer_name,c.city,o.order_id,o.order_date,p.product_name,p.category,oi.quantity,p.price,py.payment_status,d.delivery_status
from customers c
join orders o on c.customer_id=o.customer_id
join order_items oi on o.order_id=oi.order_id
join products p on oi.product_id=p.product_id
join payments py on o.order_id=py.order_id
join deliveries d on o.order_id=d.order_id;

-- PART_6
-- Exercise 27
select c.city,sum(py.amount) from customers c join orders o on c.customer_id=o.customer_id join payments py on o.order_id=py.order_id where py.payment_status="Success" group by c.city;

-- Exercise 28
select c.customer_name,sum(py.amount) from customers c join orders o on c.customer_id=o.customer_id join payments py on o.order_id=py.order_id where py.payment_status="Success" group by c.customer_name;

-- Exercise 29
select p.product_name,sum(oi.quantity) from products p join order_items oi on p.product_id=oi.product_id group by p.product_name;

-- Exercise 30
select p.category,sum(py.amount) from products p join order_items oi on p.product_id=oi.product_id join orders o on oi.order_id=o.order_id join payments py on o.order_id=py.order_id where py.payment_status="Success" group by p.category;

-- Exercise 31
select c.customer_name,count(o.order_id) from customers c join orders o on c.customer_id=o.customer_id group by c.customer_name;

-- Exercise 32
select c.customer_name,count(o.order_id) from customers c join orders o on c.customer_id=o.customer_id group by c.customer_name having count(o.order_id)>1;

-- Exercise 33
select p.category,sum(py.amount) from products p join order_items oi on p.product_id=oi.product_id join orders o on oi.order_id=o.order_id join payments py on o.order_id=py.order_id where py.payment_status="Success" group by p.category having sum(py.amount)>10000;

-- Exercise 34
select city,count(*) from customers group by city having count(*)>2;

-- Exercise 35
select p.product_name, sum(oi.quantity) from products p join order_items oi on p.product_id=oi.product_id group by p.product_name having sum(oi.quantity)>3;

-- PART_7
-- Exercise 36
select * from customers where customer_id in(select customer_id from orders);

-- Exercise 37
select * from customers where customer_id not in(select customer_id from orders);

-- Exercise 38
select * from products where product_id not in(select product_id from order_items);

-- Exercise 39
select * from orders where order_id in(select order_id from payments where amount>(select avg(amount) from payments));

-- Exercise 40
select * from customers where customer_id in(select customer_id from orders where order_id in(select order_id from payments where amount=(select max(amount) from payments)));

-- Exercise 41
select * from products where price>(select avg(price) from products);

-- Exercise 42
select * from customers where customer_id in(select customer_id from orders where order_id in(select order_id from order_items where product_id in(select product_id from products where category="Electronics")));

-- Exercise 43	
select * from orders where order_id in(select order_id from payments where payment_status="Success");

-- Exercise 44
select * from orders where order_id in(select order_id from deliveries where delivery_status!="Delivered");

-- Exercise 45
select * from customers where customer_id in(select o.customer_id from orders o join payments p on o.order_id=p.order_id group by o.customer_id having sum(p.amount)>(select avg(total_spending) from (select sum(p.amount) as total_spending from orders o join payments p on o.order_id=p.order_id group by o.customer_id) as avg_table));

-- PART_8
-- Exercise 46
select * from orders where order_id not in(select order_id from payments);

-- Exercise 47
select * from orders where order_id not in(select order_id from deliveries);

-- Exercise 48
select * from payments where amount is null or amount=0;

-- Exercise 49
select * from orders o join payments p on o.order_id=p.order_id where o.order_status="Cancelled" and p.payment_status="Success";

-- Exercise 50
select * from orders o join payments p on o.order_id=p.order_id join deliveries d on o.order_id=d.order_id where d.delivery_status="Delivered" and p.payment_status="Failed";

-- Exercise 51
select * from order_items where product_id not in(select product_id from products);

-- Exercise 52
select * from orders where customer_id not in(select customer_id from customers);









