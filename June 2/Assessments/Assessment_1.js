//PART_1
// Exercise 1
db.customers.find()

// Exercise 2
db.restaurants.find()

// Exercise 3
db.customers.find({},{name:1,city:1,membership:1,_id:0})

// Exercise 4
db.customers.find({city:"Hyderabad"})

// Exercise 5
db.customers.find({membership:"Gold"})

// Exercise 6
db.restaurants.find({rating:{$gt:4.5}})

// Exercise 7
db.orders.find({order_amount:{$gt:500}})

// Exercise 8
db.orders.find({order_status:"Delivered"})

// Exercise 9
db.orders.find({order_status:"Cancelled"})

// Exercise 10
db.customers.find({phone:null})

//PART_2
// Exercise 11
db.orders.find({order_amount:{$gte:400,$lte:700}})

// Exercise 12
db.customers.find({city:{$in:["Hyderabad","Delhi","Mumbai"]}})

// Exercise 13
db.restaurants.find({cuisine:{$in:["Indian","Fast Food"]}})

// Exercise 14
db.orders.find({"payment.status":{$ne:"Success"}})

// Exercise 15
db.orders.find({delivery_time_minutes:null})

// Exercise 16
db.orders.find({order_rating:{$gte:4}})

// Exercise 17
db.restaurants.find({city:{$nin:["Bangalore","Chennai"]}})

//PART_3
// Exercise 18
db.orders.find({"items.item_name":"Biryani"})

// Exercise 19
db.orders.find({"items.item_name":"Pizza"})

// Exercise 20
db.orders.find({"items.quantity":{$gt:1}})

// Exercise 21
db.orders.find({"items.price":{$gt:300}})

// Exercise 22
db.orders.find({},{order_id:1,items:1,_id:0})

//PART_4
// Exercise 23
db.restaurants.find().sort({rating:-1})

// Exercise 24
db.restaurants.find().sort({rating:-1}).limit(3)

// Exercise 25
db.orders.find().sort({order_amount:-1})

// Exercise 26
db.orders.find().sort({order_amount:-1}).limit(2)

// Exercise 27
db.delivery_partners.find().sort({rating:-1})

//PART_5
// Exercise 28
db.customers.updateOne({customer_id:1},{$set:{membership:"Platinum"}})

// Exercise 29
db.restaurants.updateOne({restaurant_id:104},{$set:{rating:4.1}})

// Exercise 30
db.orders.updateOne({order_id:1003},{$set:{order_status:"Delivered"}})

// Exercise 31
db.orders.updateOne({order_id:1003},{$set:{delivery_time_minutes:45}})

// Exercise 32
db.customers.updateMany({},{$set:{active:true}})

// Exercise 33
db.customers.updateMany({},{$unset:{active:""}})

// Exercise 34
db.orders.updateOne({order_id:1006},{$push:{items:{item_name:"Curd Rice",quantity:1,price:120}}})

//PART_6
// Exercise 35
db.orders.deleteMany({order_status:"Cancelled"})

// Exercise 36
db.restaurants.deleteMany({rating:{$lt:4.0}})

//PART_7
// Exercise 37
db.customers.countDocuments()

// Exercise 38
db.orders.countDocuments()

// Exercise 39
db.orders.countDocuments({order_status:"Delivered"})

// Exercise 40
db.orders.countDocuments({"payment.status":"Failed"})

// Exercise 41
db.customers.distinct("city")

// Exercise 42
db.restaurants.distinct("cuisine")

// Exercise 43
db.orders.distinct("payment.mode")


//PART_8
// Exercise 44
db.orders.aggregate([{$group:{_id:"$payment.mode",total_revenue:{$sum:"$order_amount"}}}])

// Exercise 45
db.orders.aggregate([{$group:{_id:"$order_status",total_revenue:{$sum:"$order_amount"}}}])

// Exercise 46
db.orders.aggregate([{$match:{order_status:"Delivered"}},{$group:{_id:null,average_delivery_time:{$avg:"$delivery_time_minutes"}}}])

// Exercise 47
db.orders.aggregate([{$group:{_id:"$customer_id",total_orders:{$sum:1},total_amount:{$sum:"$order_amount"}}}])

// Exercise 48
db.orders.aggregate([{$group:{_id:"$restaurant_id",total_orders:{$sum:1},total_revenue:{$sum:"$order_amount"}}}])

// Exercise 49
db.orders.aggregate([{$group:{_id:"$restaurant_id",average_rating:{$avg:"$order_rating"}}}])

// Exercise 50
db.orders.aggregate([{$group:{_id:"$customer_id",total_spending:{$sum:"$order_amount"}}},{$match:{total_spending:{$gt:700}}}])

//PART_9
// Exercise 51
db.orders.aggregate([{$lookup:{from:"customers",localField:"customer_id",foreignField:"customer_id",as:"customer_details"}},{$unwind:"$customer_details"},{$project:{_id:0,order_id:1,customer_name:"$customer_details.name",city:"$customer_details.city",order_amount:1,order_status:1}}])

// Exercise 52
db.orders.aggregate([{$lookup:{from:"restaurants",localField:"restaurant_id",foreignField:"restaurant_id",as:"restaurant_details"}},{$unwind:"$restaurant_details"},{$project:{_id:0,order_id:1,restaurant_name:"$restaurant_details.name",cuisine:"$restaurant_details.cuisine",order_amount:1}}])

// Exercise 53
db.orders.aggregate([{$lookup:{from:"delivery_partners",localField:"partner_id",foreignField:"partner_id",as:"partner_details"}},{$unwind:"$partner_details"},{$project:{_id:0,order_id:1,partner_name:"$partner_details.partner_name",delivery_time:"$delivery_time_minutes",order_status:1}}])

// Exercise 54
db.orders.aggregate([{$lookup:{from:"customers",localField:"customer_id",foreignField:"customer_id",as:"customer_details"}},{$unwind:"$customer_details"},{$lookup:{from:"restaurants",localField:"restaurant_id",foreignField:"restaurant_id",as:"restaurant_details"}},{$unwind:"$restaurant_details"},{$lookup:{from:"delivery_partners",localField:"partner_id",foreignField:"partner_id",as:"partner_details"}},{$unwind:{path:"$partner_details",preserveNullAndEmptyArrays:true}},{$project:{_id:0,order_id:1,customer_name:"$customer_details.name",restaurant_name:"$restaurant_details.name",cuisine:"$restaurant_details.cuisine",partner_name:"$partner_details.partner_name",order_amount:1,payment_mode:"$payment.mode",payment_status:"$payment.status",order_status:1,delivery_time:"$delivery_time_minutes",rating:"$order_rating"}}])
