-- ==========================================
-- SAMPLE DATA
-- Retail Sales Analytics System
-- ==========================================

USE retail_sales_db;

-- ==========================================
-- INSERT STORES
-- ==========================================

INSERT INTO stores
(store_name, region)
VALUES
('Chennai Central', 'South'),
('Bangalore Mall', 'South'),
('Mumbai Plaza', 'West');

-- ==========================================
-- INSERT PRODUCTS
-- ==========================================

INSERT INTO products
(product_name, category, price)
VALUES
('Laptop', 'Electronics', 55000),
('Headphones', 'Electronics', 2500),
('Smart Watch', 'Electronics', 6000);

-- ==========================================
-- INSERT EMPLOYEES
-- ==========================================

INSERT INTO employees
(employee_name, designation, store_id)
VALUES
('Rahul Sharma', 'Manager', 1),
('Priya Singh', 'Sales Executive', 2),
('Karthik Kumar', 'Cashier', 3);

-- ==========================================
-- INSERT SALES
-- ==========================================

INSERT INTO sales
(product_id, store_id, quantity, sale_date, total_amount)
VALUES
(1, 1, 2, '2026-06-20', 110000),
(2, 2, 5, '2026-06-20', 12500),
(3, 3, 3, '2026-06-20', 18000);

-- ==========================================
-- VERIFY DATA
-- ==========================================

SELECT * FROM stores;
SELECT * FROM products;
SELECT * FROM employees;
SELECT * FROM sales;
