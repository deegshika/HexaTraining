-- ==========================================
-- Retail Sales Analytics System
-- Database Schema
-- ==========================================

CREATE DATABASE IF NOT EXISTS retail_sales_db;

USE retail_sales_db;

-- ==========================================
-- STORES TABLE
-- ==========================================

CREATE TABLE stores (
    store_id INT PRIMARY KEY AUTO_INCREMENT,
    store_name VARCHAR(100) NOT NULL,
    region VARCHAR(50) NOT NULL
);

-- ==========================================
-- PRODUCTS TABLE
-- ==========================================

CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    price DECIMAL(10,2)
);

-- ==========================================
-- EMPLOYEES TABLE
-- ==========================================

CREATE TABLE employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_name VARCHAR(100) NOT NULL,
    designation VARCHAR(50),
    store_id INT,

    FOREIGN KEY (store_id)
    REFERENCES stores(store_id)
);

-- ==========================================
-- SALES TABLE
-- ==========================================

CREATE TABLE sales (
    sale_id INT PRIMARY KEY AUTO_INCREMENT,
    product_id INT,
    store_id INT,
    quantity INT,
    sale_date DATE,
    total_amount DECIMAL(10,2),

    FOREIGN KEY (product_id)
    REFERENCES products(product_id),

    FOREIGN KEY (store_id)
    REFERENCES stores(store_id)
);

-- ==========================================
-- VERIFY TABLES
-- ==========================================

SHOW TABLES;
