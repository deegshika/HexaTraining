
// Use Database

use retail_db


// Create Collection

db.createCollection("customers")


// Insert One Data

db.customers.insertOne({
    customer_id:1,
    name:"Rahul Sharma",
    city:"Hyderabad",
    phone:"9894152145",
    membership:"Gold"
})


// Insert Many Data

db.customers.insertMany([
{
    customer_id:2,
    name:"Priya Reddy",
    city:"Bangalore",
    phone:"9876543211",
    membership:"Silver"
},
{
    customer_id:3,
    name:"Amit Kumar",
    city:"Mumbai",
    phone:null,
    membership:"Gold"
},
{
    customer_id:4,
    name:"Sneha Patel",
    city:"Chennai",
    phone:"9876543213",
    membership:"Bronze"
}
])


// Find by City

db.customers.find({
    city:"Hyderabad"
})


// Greater Than

db.customers.find({
    customer_id:{$gt:2}
})


// Less Than Equal To

db.customers.find({
    customer_id:{$lte:3}
})


// IN Operator

db.customers.find({
    city:{$in:["Hyderabad","Bangalore"]}
})


// OR Condition

db.customers.find({
    $or:[
        {city:"Hyderabad"},
        {membership:"Gold"}
    ]
})


// Select Specific Fields

db.customers.find(
{},
{
    name:1,
    city:1,
    _id:0
}
)


// Sort Ascending

db.customers.find().sort({
    customer_id:1
})


// Sort Descending

db.customers.find().sort({
    customer_id:-1
})


// Limit

db.customers.find().limit(3)

