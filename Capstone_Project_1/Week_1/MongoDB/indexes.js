// ==========================================
// Index Creation
// ==========================================

use("employee_tracker");

// Index on employee_id

db.feedback.createIndex(
{
    employee_id: 1
}
);

// Index on department

db.feedback.createIndex(
{
    department: 1
}
);

// Verify Indexes

db.feedback.getIndexes();
