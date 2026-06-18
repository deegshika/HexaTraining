// ==========================================
// Retail Sales Analytics System
// MongoDB Indexes
// ==========================================

use("retail_sales_db");

// ==========================================
// CREATE INDEX ON PRODUCT ID
// ==========================================

db.campaign_feedback.createIndex(
{
    product_id: 1
}
);

// ==========================================
// CREATE INDEX ON REGION
// ==========================================

db.campaign_feedback.createIndex(
{
    region: 1
}
);

// ==========================================
// VERIFY INDEXES
// ==========================================

db.campaign_feedback.getIndexes();
