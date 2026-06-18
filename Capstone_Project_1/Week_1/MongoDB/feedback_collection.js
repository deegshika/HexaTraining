// ==========================================
// Employee Feedback Collection
// ==========================================

use("employee_tracker");

// Insert Sample Feedback Documents

db.feedback.insertMany([
{
    employee_id: 1,
    employee_name: "Rahul Sharma",
    department: "IT",
    feedback: "Completed all assigned tasks before deadline.",
    note: "Excellent performance and teamwork.",
    feedback_date: new Date("2026-06-15")
},

{
    employee_id: 2,
    employee_name: "Priya Singh",
    department: "HR",
    feedback: "Attendance needs improvement.",
    note: "Frequently arrives late.",
    feedback_date: new Date("2026-06-15")
},

{
    employee_id: 3,
    employee_name: "Karthik Kumar",
    department: "Finance",
    feedback: "Accurate financial reporting.",
    note: "Good analytical skills.",
    feedback_date: new Date("2026-06-15")
},

{
    employee_id: 4,
    employee_name: "Ananya Patel",
    department: "IT",
    feedback: "Delivered feature development successfully.",
    note: "Consistent performer.",
    feedback_date: new Date("2026-06-15")
},

{
    employee_id: 5,
    employee_name: "Vikram Reddy",
    department: "Sales",
    feedback: "Needs improvement in client follow-up.",
    note: "Missed a few deadlines.",
    feedback_date: new Date("2026-06-15")
}
]);

// View Documents

db.feedback.find();
