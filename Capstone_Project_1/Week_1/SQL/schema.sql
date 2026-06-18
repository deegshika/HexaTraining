-- ==========================================
-- Employee Attendance & Productivity Tracker
-- Database Schema
-- ==========================================

CREATE DATABASE IF NOT EXISTS employee_tracker;

USE employee_tracker;

-- ==========================================
-- EMPLOYEES TABLE
-- ==========================================

CREATE TABLE employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_name VARCHAR(100) NOT NULL,
    department VARCHAR(50) NOT NULL,
    designation VARCHAR(50),
    joining_date DATE
);

-- ==========================================
-- ATTENDANCE TABLE
-- ==========================================

CREATE TABLE attendance (
    attendance_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_id INT,
    attendance_date DATE NOT NULL,
    clock_in DATETIME,
    clock_out DATETIME,
    status VARCHAR(20),

    FOREIGN KEY (employee_id)
    REFERENCES employees(employee_id)
);

-- ==========================================
-- TASKS TABLE
-- ==========================================

CREATE TABLE tasks (
    task_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_id INT,
    task_name VARCHAR(100) NOT NULL,
    tasks_completed INT DEFAULT 0,
    task_date DATE,

    FOREIGN KEY (employee_id)
    REFERENCES employees(employee_id)
);
