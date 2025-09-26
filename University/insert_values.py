# Insert Data in Students Table
'''INSERT INTO students(first_name,last_name,email,phone,major,admission_date,status)
VALUES('ali','ahmadi','aliahmadi@gmail.com',0771230009,'bba','2025-01-02','active'),
('ahmad','ahmadi','ahmadhmadi@gmail.com',0774430239,'ccna','2025-05-04','graduated'),
('ajmal','mohmmadi','ajmalmohammadi@gmail.com',0791230049,'bcs','2025-02-02','suspended'),
('omar','mohmmadi','omarmohammadi@gmail.com',0791220143,'ccna','2025-03-02','active'),
('khan','khani','khankhani@gmail.com',0321133249,'bba','2025-01-02','graduated'),
('akmal','mohmmadi','akmalmohammadi@gmail.com',0511321443,'cna','2025-03-01','suspended')'''

# Insert Data in Professors Table
'''INSERT INTO professors(name,email,department)
VALUES('ajmal','ajmal@gmail.com','bba'),
('omar','omar@gmail.com','bcs'),
('khan','khan@gmail.com','ccna'),
('jan','jan@gmail.com','cna')'''

# Insert Data in Courses Table
'''INSERT INTO courses(professor_id,name,credits,semester)
VALUES(1,'klh',2,4),
(2,'fa',3,1),
(3,'k',4,2),
(4,'m',3,3)'''

# Insert Data in Books Table
'''INSERT INTO books(title,author,isbn,available_copies)
VALUES('darkness','alex','24313',3),
('moon','jack','9087',5),
('noon','rex','6075',12),
('day','max','8976',23),
('ai','rayan','7964',43)'''

# Insert Data in Enrollments Table
'''INSERT INTO enrollments(student_id,course_id,semester,grade)
VALUES(1,1,2,2),
(2,2,1,3),
(3,3,3,1),
(4,4,3,4)'''

# Insert Data in Payments Table
'''INSERT INTO payments(student_id,amount,method,status)
VALUES(1,200,'cash','pending'),
(2,400,'card','completed'),
(3,800,'online','failed')'''

# Insert Data in Dormitories Table
'''INSERT INTO dormitories(name,capacity,dorm_type)
VALUES('a4',3,'male'),
('b3',5,'female'),
('c5',4,'mixed')'''

# Insert Data in Rooms Table
'''INSERT INTO rooms(dorm_id,room_number,capacity)
VALUES(1,23,3),
(2,12,4),
(3,45,5)'''

# Insert Data in Borrowings Table
'''INSERT INTO borrowings(student_id,book_id,status)
VALUES(1,1,'borrowed'),
(2,2,'returned'),
(3,3,'late')'''

# Insert Data in Dormreservation Table
'''INSERT INTO dormreservation(student_id,room_id,status)
VALUES(1,1,'active'),
(2,2,'expired'),
(3,3,'cancelled')'''