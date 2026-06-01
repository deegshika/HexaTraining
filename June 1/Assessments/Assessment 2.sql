create database mysql_capstone_2;
use mysql_capstone_2;

CREATE TABLE patients 
( 
    patient_id INT PRIMARY KEY, 
    patient_name VARCHAR(100),
    gender VARCHAR(10), 
    age INT, 
    city VARCHAR(50), 
    phone VARCHAR(15) 
); 

CREATE TABLE departments 
( 
    department_id INT PRIMARY KEY, 
    department_name VARCHAR(100) 
); 

CREATE TABLE doctors 
( 
    doctor_id INT PRIMARY KEY,
    doctor_name VARCHAR(100), 
    specialization VARCHAR(100), 
    department_id INT, 
    consultation_fee DECIMAL(10,2) 
); 

CREATE TABLE appointments 
( 
    appointment_id INT PRIMARY KEY,
    patient_id INT, 
    doctor_id INT, 
    appointment_date DATE, 
    appointment_status VARCHAR(30) 
); 

CREATE TABLE treatments 
( 
    treatment_id INT PRIMARY KEY, 
    appointment_id INT, 
    treatment_name VARCHAR(100), 
    treatment_cost DECIMAL(10,2) 
); 

CREATE TABLE bills 
( 
    bill_id INT PRIMARY KEY, 
    patient_id INT, 
    appointment_id INT, 
    bill_date DATE, 
    total_amount DECIMAL(10,2), 
    bill_status VARCHAR(30) 
); 

CREATE TABLE payments 
( 
    payment_id INT PRIMARY KEY, 
    bill_id INT, 
    payment_mode VARCHAR(30), 
    paid_amount DECIMAL(10,2),
    payment_status VARCHAR(30) 
); 

insert into departments values
(1,"Cardiology"),
(2,"Neurology"),
(3,"Orthopedics"),
(4,"Dermatology"),
(5,"Pediatrics");

insert into doctors values
(101,"Dr. Arjun","Cardiology",1,1000),
(102,"Dr. Priya","Neurology",2,900),
(103,"Dr. Rahul","Orthopedics",3,850),
(104,"Dr. Sneha","Dermatology",4,700),
(105,"Dr. Kiran","Pediatrics",5,750),
(106,"Dr. Meena","Cardiology",1,1200),
(107,"Dr. Vikram","Neurology",2,950),
(108,"Dr. Divya","Orthopedics",3,800);

insert into patients values
(1,"Rahul Sharma","Male",35,"Hyderabad","9876543210"),
(2,"Priya Reddy","Female",28,"Bangalore","9876543211"),
(3,"Amit Kumar","Male",45,"Mumbai","9876543212"),
(4,"Sneha Patel","Female",39,"Chennai","9876543213"),
(5,"Arjun Verma","Male",50,"Delhi","9876543214"),
(6,"Neha Singh","Female",33,"Pune","9876543215"),
(7,"Kiran Rao","Male",42,"Hyderabad","9876543216"),
(8,"Divya Sharma","Female",29,"Chennai","9876543217"),
(9,"Vikram Gupta","Male",37,"Bangalore","9876543218"),
(10,"Meera Nair","Female",31,"Kochi","9876543219"),
(11,"Rohan Das","Male",48,"Hyderabad","9876543220"),
(12,"Ananya Iyer","Female",26,"Chennai","9876543221");

insert into appointments values
(1001,1,101,"2026-01-05","Completed"),
(1002,2,102,"2026-01-08","Completed"),
(1003,3,103,"2026-01-10","Cancelled"),
(1004,4,104,"2026-01-12","Completed"),
(1005,5,105,"2026-01-15","Pending"),
(1006,6,106,"2026-01-18","Completed"),
(1007,7,107,"2026-01-20","Completed"),
(1008,8,108,"2026-01-22","Cancelled"),
(1009,9,101,"2026-01-25","Completed"),
(1010,10,102,"2026-01-28","Pending"),
(1011,11,103,"2026-02-01","Completed"),
(1012,12,104,"2026-02-03","Completed"),
(1013,1,105,"2026-02-05","Completed"),
(1014,2,106,"2026-02-08","Cancelled"),
(1015,3,107,"2026-02-10","Completed"),
(1016,4,108,"2026-02-12","Pending"),
(1017,5,101,"2026-02-15","Completed"),
(1018,6,102,"2026-02-18","Completed"),
(1019,7,103,"2026-02-20","Completed"),
(1020,8,104,"2026-02-25","Cancelled");

insert into treatments values
(201,1001,"Heart Checkup",5000),
(202,1002,"Brain Scan",7000),
(203,1004,"Skin Treatment",3000),
(204,1006,"Heart Surgery",25000),
(205,1007,"Neuro Consultation",6000),
(206,1009,"ECG Test",2000),
(207,1011,"Bone Treatment",8000),
(208,1012,"Skin Allergy",2500),
(209,1013,"Vaccination",1500),
(210,1015,"MRI Scan",9000),
(211,1017,"Heart Test",4000),
(212,1018,"Brain Therapy",10000),
(213,1019,"Bone Scan",3500),
(214,1005,"Child Checkup",2000),
(215,1016,"General Treatment",3000);

insert into bills values
(301,1,1001,"2026-01-05",5000,"Paid"),
(302,2,1002,"2026-01-08",7000,"Paid"),
(303,4,1004,"2026-01-12",3000,"Paid"),
(304,6,1006,"2026-01-18",25000,"Paid"),
(305,7,1007,"2026-01-20",6000,"Paid"),
(306,9,1009,"2026-01-25",2000,"Paid"),
(307,11,1011,"2026-02-01",8000,"Paid"),
(308,12,1012,"2026-02-03",2500,"Paid"),
(309,1,1013,"2026-02-05",1500,"Paid"),
(310,3,1015,"2026-02-10",9000,"Pending"),
(311,5,1017,"2026-02-15",4000,"Paid"),
(312,6,1018,"2026-02-18",10000,"Paid"),
(313,7,1019,"2026-02-20",3500,"Pending"),
(314,5,1005,"2026-01-15",2000,"Pending"),
(315,4,1016,"2026-02-12",3000,"Pending");

insert into payments values
(401,301,"UPI",5000,"Success"),
(402,302,"Card",7000,"Success"),
(403,303,"Cash",3000,"Success"),
(404,304,"Net Banking",25000,"Success"),
(405,305,"UPI",6000,"Success"),
(406,306,"Card",2000,"Success"),
(407,307,"Cash",8000,"Success"),
(408,308,"UPI",2500,"Success"),
(409,309,"Card",1500,"Success"),
(410,310,"UPI",0,"Pending"),
(411,311,"Cash",4000,"Success"),
(412,312,"Net Banking",10000,"Success"),
(413,313,"UPI",0,"Pending"),
(414,314,"Cash",0,"Pending"),
(415,315,"Card",0,"Pending");

-- PART_1
-- Exercise 1
select * from patients;

-- Exercise 2
select * from doctors;

-- Exercise 3
select * from patients where city="Hyderabad";

-- Exercise 4
select * from doctors where specialization="Cardiology";

-- Exercise 5
select * from appointments where appointment_date>"2026-01-01";

-- Exercise 6
select * from appointments where appointment_status="Cancelled";

-- Exercise 7
select * from bills where total_amount>5000;

-- Exercise 8
select * from payments where payment_mode="UPI";

-- Exercise 9
select * from patients where age between 30 and 50;

-- Exercise 10
select * from doctors where consultation_fee>800;

-- PART_2
-- Exercise 11
select count(*) from patients;

-- Exercise 12
select count(*) from doctors;

-- Exercise 13
select count(*) from appointments;

-- Exercise 14
select avg(consultation_fee) from doctors;

-- Exercise 15
select max(treatment_cost) from treatments;

-- Exercise 16
select sum(total_amount) from bills;

-- Exercise 17
select sum(paid_amount) from payments;

-- Exercise 18
select city,count(*) from patients group by city;

-- Exercise 19
select specialization,count(*) from doctors group by specialization;

-- Exercise 20
select appointment_status,count(*) from appointments group by appointment_status;

-- PART_3
-- Exercise 21
select p.patient_name,a.appointment_date,a.appointment_status from patients p join appointments a on p.patient_id=a.patient_id;

-- Exercise 22
select d.doctor_name,dp.department_name from doctors d join departments dp on d.department_id=dp.department_id;

-- Exercise 23
select p.patient_name,d.doctor_name,a.appointment_date from patients p join appointments a on p.patient_id=a.patient_id join doctors d on a.doctor_id=d.doctor_id;

-- Exercise 24
select a.appointment_id,t.treatment_name,t.treatment_cost from appointments a join treatments t on a.appointment_id=t.appointment_id;

-- Exercise 25
select b.bill_id,p.patient_name,b.total_amount from bills b join patients p on b.patient_id=p.patient_id;

-- Exercise 26
select b.bill_id, p.payment_mode,p.paid_amount,p.payment_status from bills b join payments p on b.bill_id=p.bill_id;

-- Exercise 27
select p.patient_name, d.doctor_name,dp.department_name,a.appointment_date,a.appointment_status,t.treatment_name,t.treatment_cost,b.total_amount, py.payment_status from patients p join appointments a on p.patient_id=a.patient_id join doctors d on a.doctor_id=d.doctor_id join departments dp on d.department_id=dp.department_id join treatments t on a.appointment_id=t.appointment_id join bills b on a.appointment_id=b.appointment_id join payments py on b.bill_id=py.bill_id;

-- PART_4
-- Exercise 28
select d.doctor_name,count(a.appointment_id) from doctors d join appointments a on d.doctor_id=a.doctor_id group by d.doctor_name;

-- Exercise 29
select dp.department_name,count(a.appointment_id) from departments dp join doctors d on dp.department_id=d.department_id join appointments a on d.doctor_id=a.doctor_id group by dp.department_name;

-- Exercise 30
select dp.department_name,sum(b.total_amount) from departments dp join doctors d on dp.department_id=d.department_id join appointments a on d.doctor_id=a.doctor_id join bills b on a.appointment_id=b.appointment_id group by dp.department_name;

-- Exercise 31
select treatment_name,sum(treatment_cost) from treatments group by treatment_name;

-- Exercise 32
select p.city,sum(b.total_amount) from patients p join bills b on p.patient_id=b.patient_id group by p.city;

-- Exercise 33
select d.doctor_name,count(a.appointment_id) from doctors d join appointments a on d.doctor_id=a.doctor_id group by d.doctor_name having count(a.appointment_id) > 2;

-- Exercise 34
select dp.department_name,sum(b.total_amount) from departments dp join doctors d on dp.department_id=d.department_id join appointments a on d.doctor_id=a.doctor_id join bills b on a.appointment_id=b.appointment_id group by dp.department_name having sum(b.total_amount)>20000;

-- Exercise 35
select city,count(*) from patients group by city having count(*)>2;

-- PART_5
-- Exercise 36
select * from patients where patient_id in(select patient_id from appointments);

-- Exercise 37
select * from patients where patient_id not in(select patient_id from appointments);

-- Exercise 38
select * from doctors where doctor_id not in(select doctor_id from appointments);

-- Exercise 39
select * from bills where total_amount>(select avg(total_amount) from bills);

-- Exercise 40
select * from patients where patient_id in(select patient_id from bills where total_amount=(select max(total_amount) from bills));

-- Exercise 41
select * from doctors where consultation_fee>(select avg(consultation_fee) from doctors);

-- Exercise 42
select * from patients where patient_id in(select a.patient_id from appointments a join doctors d on a.doctor_id=d.doctor_id where d.specialization="Cardiology");

-- Exercise 43
select * from bills where bill_status="Pending";

-- Exercise 44
select * from appointments where appointment_id in(select appointment_id from treatments);

-- Exercise 45
select * from patients where patient_id in(select patient_id from bills group by patient_id having sum(total_amount)>(select avg(total_bill) from(select sum(total_amount) as total_bill from bills group by patient_id) as avg_table));

-- PART_6
-- Exercise 46
select * from appointments where appointment_id not in(select appointment_id from treatments);

-- Exercise 47
select * from bills where bill_id not in(select bill_id from payments);

-- Exercise 48
select * from payments where paid_amount=0 or payment_status="Pending";

-- Exercise 49
select * from appointments where appointment_status="Cancelled" and appointment_id in(select appointment_id from bills where bill_status="Paid");

-- Exercise 50
select * from doctors d join appointments a on d.doctor_id=a.doctor_id where a.appointment_status="Completed" and d.consultation_fee>1000;

-- Exercise 51
select * from patients where age<18 or age>60;

-- Exercise 52
select * from bills where total_amount is null or total_amount=0;
