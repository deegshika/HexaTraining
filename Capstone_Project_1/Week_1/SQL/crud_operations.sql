-- ==========================================
-- CRUD OPERATIONS
-- Employee Attendance & Productivity Tracker
-- ==========================================

USE employee_tracker;

-- ==========================================
-- CREATE
-- ==========================================

INSERT INTO attendance
(employee_id, attendance_date, clock_in, clock_out, status)
VALUES
(1,
'2026-06-20',
'2026-06-20 09:00:00',
'2026-06-20 18:00:00',
'Present');

-- ==========================================
-- READ
-- ==========================================

SELECT * FROM employees;

SELECT * FROM attendance;

SELECT * FROM tasks;

-- ==========================================
-- UPDATE
-- ==========================================

UPDATE attendance
SET clock_out = '2026-06-20 18:30:00'
WHERE attendance_id = 1;

-- ==========================================
-- DELETE
-- ==========================================

DELETE FROM attendance
WHERE attendance_id = 1;
