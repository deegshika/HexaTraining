// ==========================================
// Retail Sales Analytics System
// Promotional Campaign Feedback Collection
// ==========================================

use("retail_sales_db");

// ==========================================
// INSERT CAMPAIGN FEEDBACK
// ==========================================

db.campaign_feedback.insertMany([

{
    product_id: 1,
    product_name: "Laptop",
    region: "South",
    campaign_name: "Summer Sale",
    feedback: "Sales increased significantly during the campaign.",
    rating: 5,
    feedback_date: new Date("2026-06-20")
},

{
    product_id: 2,
    product_name: "Headphones",
    region: "South",
    campaign_name: "Festival Offer",
    feedback: "Customer response was average.",
    rating: 3,
    feedback_date: new Date("2026-06-20")
},

{
    product_id: 3,
    product_name: "Smart Watch",
    region: "West",
    campaign_name: "New Launch Promotion",
    feedback: "Product received good engagement from customers.",
    rating: 4,
    feedback_date: new Date("2026-06-20")
},

{
    product_id: 1,
    product_name: "Laptop",
    region: "West",
    campaign_name: "Mega Electronics Sale",
    feedback: "High conversion rate and strong customer interest.",
    rating: 5,
    feedback_date: new Date("2026-06-21")
}

]);

// ==========================================
// VIEW DOCUMENTS
// ==========================================

db.campaign_feedback.find();
