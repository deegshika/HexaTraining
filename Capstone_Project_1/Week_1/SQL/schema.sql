CREATE DATABASE employee_tracker;
USE employee_tracker;

CREATE TABLE employees(
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_name VARCHAR(100),
    department VARCHAR(50),
    designation VARCHAR(50),
    joining_date DATE
);

CREATE TABLE attendance(
    attendance_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_id INT,
    attendance_date DATE,
    clock_in DATETIME,
    clock_out DATETIME,
    status VARCHAR(20),
    FOREIGN KEY(employee_id)
    REFERENCES employees(employee_id)
);

CREATE TABLE tasks(
    task_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_id INT,
    task_name VARCHAR(100),
    tasks_completed INT,
    task_date DATE,
    FOREIGN KEY(employee_id)
    REFERENCES employees(employee_id)
);
