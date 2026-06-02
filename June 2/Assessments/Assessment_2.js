//PART_1
// Exercise 1
db.learners.find()

// Exercise 2
db.courses.find()

// Exercise 3
db.learners.find({},{name:1,city:1,goal:1,_id:0})

// Exercise 4
db.learners.find({city:"Hyderabad"})

// Exercise 5
db.learners.find({goal:"AI Engineer"})

// Exercise 6
db.courses.find({category:"Data Engineering"})

// Exercise 7
db.courses.find({price:{$gt:10000}})

// Exercise 8
db.courses.find({level:"Beginner"})

// Exercise 9
db.enrollments.find({"payment.status":"Success"})

// Exercise 10
db.learners.find({phone:null})

//PART_2
// Exercise 11
db.learners.find({experience_years:{$gt:2}})

// Exercise 12
db.courses.find({price:{$gte:8000,$lte:18000}})

// Exercise 13
db.courses.find({level:{$in:["Beginner","Intermediate"]}})

// Exercise 14
db.enrollments.find({"progress.completion_percent":{$gte:80}})

// Exercise 15
db.enrollments.find({"payment.status":{$ne:"Success"}})

// Exercise 16
db.learners.find({city:{$in:["Hyderabad","Bangalore","Pune"]}})

// Exercise 17
db.courses.find({category:{$ne:"Cloud"}})

//PART_3
// Exercise 18
db.instructors.find({expertise:"AI"})

// Exercise 19
db.instructors.find({expertise:"SQL"})

// Exercise 20
db.courses.find({tools:"Python"})

// Exercise 21
db.courses.find({tools:"Databricks"})

// Exercise 22
db.enrollments.find({quiz_scores:95})

// Exercise 23
db.enrollments.find({quiz_scores:{$gt:85}})

//PART_4
// Exercise 24
db.courses.find().sort({price:-1})

// Exercise 25
db.courses.find().sort({price:-1}).limit(3)

// Exercise 26
db.learners.find().sort({experience_years:-1})

// Exercise 27
db.learners.find().sort({experience_years:-1}).limit(2)

// Exercise 28
db.instructors.find().sort({rating:-1})

//PART_5
// Exercise 29
db.learners.updateOne({learner_id:1},{$set:{city:"Secunderabad"}})

// Exercise 30
db.courses.updateOne({course_id:203},{$set:{price:9000}})

// Exercise 31
db.enrollments.updateOne({enrollment_id:1006},{$set:{"progress.completion_percent":30}})

// Exercise 32
db.enrollments.updateOne({enrollment_id:1005},{$set:{status:"Inactive"}})

// Exercise 33
db.learners.updateMany({},{$set:{active:true}})

// Exercise 34
db.learners.updateMany({},{$unset:{active:""}})

// Exercise 35
db.courses.updateOne({course_id:201},{$push:{tools:"MongoDB"}})

//PART_6

// Exercise 36
db.enrollments.deleteMany({"payment.status":"Failed"})

// Exercise 37
db.learners.deleteMany({experience_years:0})

//PART_7
// Exercise 38
db.learners.countDocuments()

// Exercise 39
db.courses.countDocuments()

// Exercise 40
db.enrollments.countDocuments({"payment.status":"Success"})

// Exercise 41
db.learners.distinct("city")

// Exercise 42
db.courses.distinct("category")

// Exercise 43
db.enrollments.distinct("payment.mode")

//PART_8
// Exercise 44
db.enrollments.aggregate([{$group:{_id:"$payment.mode",total_revenue:{$sum:"$payment.amount"}}}])

// Exercise 45
db.enrollments.aggregate([{$group:{_id:"$course_id",total_revenue:{$sum:"$payment.amount"}}}])

// Exercise 46
db.learners.aggregate([{$group:{_id:"$goal",total_learners:{$sum:1}}}])

// Exercise 47
db.courses.aggregate([{$group:{_id:"$category",average_price:{$avg:"$price"}}}])

// Exercise 48
db.enrollments.aggregate([{$group:{_id:"$course_id",average_completion:{$avg:"$progress.completion_percent"}}}])

// Exercise 49
db.enrollments.aggregate([{$group:{_id:"$status",total_enrollments:{$sum:1}}}])

// Exercise 50
db.enrollments.aggregate([{$group:{_id:"$course_id",total_revenue:{$sum:"$payment.amount"}}},{$match:{total_revenue:{$gt:15000}}}])

//PART_9

// Exercise 51
db.enrollments.aggregate([{$lookup:{from:"learners",localField:"learner_id",foreignField:"learner_id",as:"learner_details"}},{$unwind:"$learner_details"},{$project:{_id:0,enrollment_id:1,learner_name:"$learner_details.name",city:"$learner_details.city",course_id:1,status:1}}])

// Exercise 52
db.enrollments.aggregate([{$lookup:{from:"courses",localField:"course_id",foreignField:"course_id",as:"course_details"}},{$unwind:"$course_details"},{$project:{_id:0,enrollment_id:1,course_name:"$course_details.course_name",category:"$course_details.category",amount:"$payment.amount",payment_status:"$payment.status"}}])

// Exercise 53
db.courses.aggregate([{$lookup:{from:"instructors",localField:"instructor_id",foreignField:"instructor_id",as:"instructor_details"}},{$unwind:"$instructor_details"},{$project:{_id:0,course_name:1,category:1,instructor_name:"$instructor_details.instructor_name",instructor_rating:"$instructor_details.rating"}}])

// Exercise 54
db.enrollments.aggregate([{$lookup:{from:"learners",localField:"learner_id",foreignField:"learner_id",as:"learner_details"}},{$unwind:"$learner_details"},{$lookup:{from:"courses",localField:"course_id",foreignField:"course_id",as:"course_details"}},{$unwind:"$course_details"},{$lookup:{from:"instructors",localField:"course_details.instructor_id",foreignField:"instructor_id",as:"instructor_details"}},{$unwind:"$instructor_details"},{$project:{_id:0,enrollment_id:1,learner_name:"$learner_details.name",city:"$learner_details.city",goal:"$learner_details.goal",course_name:"$course_details.course_name",category:"$course_details.category",instructor_name:"$instructor_details.instructor_name",payment_amount:"$payment.amount",payment_status:"$payment.status",completion_percent:"$progress.completion_percent",enrollment_status:"$status"}}])
