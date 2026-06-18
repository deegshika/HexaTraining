USE employee_tracker;

-- ==========================================
-- SAMPLE EMPLOYEE DATA
-- ==========================================

INSERT INTO employees
(employee_name, department, designation, joining_date)
VALUES
('Rahul Sharma', 'IT', 'Developer', '2023-01-10'),
('Priya Singh', 'HR', 'Executive', '2022-05-15'),
('Karthik Kumar', 'Finance', 'Analyst', '2021-03-20'),
('Ananya Patel', 'IT', 'Software Engineer', '2024-02-12'),
('Vikram Reddy', 'Sales', 'Sales Executive', '2023-08-05');

-- ==========================================
-- SAMPLE ATTENDANCE DATA
-- ==========================================

INSERT INTO attendance
(employee_id, attendance_date, clock_in, clock_out, status)
VALUES
(1, '2026-06-15', '2026-06-15 09:00:00', '2026-06-15 18:00:00', 'Present'),
(1, '2026-06-16', '2026-06-16 09:10:00', '2026-06-16 18:15:00', 'Present'),

(2, '2026-06-15', '2026-06-15 09:30:00', '2026-06-15 17:30:00', 'Present'),
(2, '2026-06-16', NULL, NULL, 'Absent'),

(3, '2026-06-15', '2026-06-15 08:50:00', '2026-06-15 17:45:00', 'Present'),
(3, '2026-06-16', '2026-06-16 09:00:00', '2026-06-16 18:00:00', 'Present'),

(4, '2026-06-15', '2026-06-15 09:20:00', '2026-06-15 18:10:00', 'Present'),
(4, '2026-06-16', '2026-06-16 09:25:00', '2026-06-16 18:00:00', 'Present'),

(5, '2026-06-15', '2026-06-15 09:45:00', '2026-06-15 17:00:00', 'Present'),
(5, '2026-06-16', NULL, NULL, 'Absent');

-- ==========================================
-- SAMPLE TASK DATA
-- ==========================================

INSERT INTO tasks
(employee_id, task_name, tasks_completed, task_date)
VALUES
(1, 'Bug Fixing', 12, '2026-06-15'),
(1, 'Code Review', 8, '2026-06-16'),

(2, 'Recruitment Screening', 5, '2026-06-15'),
(2, 'Interview Scheduling', 4, '2026-06-16'),

(3, 'Financial Analysis', 10, '2026-06-15'),
(3, 'Budget Planning', 7, '2026-06-16'),

(4, 'Feature Development', 15, '2026-06-15'),
(4, 'API Integration', 11, '2026-06-16'),

(5, 'Lead Follow-up', 6, '2026-06-15'),
(5, 'Client Calls', 5, '2026-06-16');
