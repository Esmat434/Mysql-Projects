# Insert five sample students into the Students table.
'''SELECT * FROM students
LIMIT 5'''

# Insert three sample professors into the Professors table.
'''SELECT * FROM professors
LIMIT 3'''

# Insert three new courses into the Courses table.
'''INSERT INTO courses(professor_id,name,credits,semester)
VALUES(3,'jmx',4,3),
(4,'mbc',1,3),
(2,'bbc',3,1)'''

# Enroll two students in two different courses.
'''INSERT INTO enrollments(student_id,course_id,semester,grade)
VALUES(3,2,1,3),
(1,4,2,1)'''

# Register a new payment for a student.
'''INSERT INTO payments(student_id,amount,payment_date,method,status)
VALUES(4,100,'2025-03-05','online','completed')'''

# Retrieve the list of all students using a SELECT statement.
'''SELECT * FROM students'''

# Display only the first name and email of students.
'''SELECT first_name,email FROM students'''

# Show the names of courses that have more than 3 credits.
'''SELECT * FROM courses WHERE credits>3'''

# Display the names of students who were admitted after 2024.
'''SELECT * FROM students WHERE YEAR(admission_date) > 2024'''

# Update the phone number of a student.
'''UPDATE students SET phone='771250003' WHERE id=3'''

# Update the email of a professor.
'''UPDATE professors SET email='ajmalahmadi@gmail.com' WHERE id=1'''

# Delete a record from the Professors table.
'''DELETE FROM professors WHERE id=4'''

# Delete an enrollment record.
'''DELETE FROM enrollments WHERE id=6'''

# Show all payments made using the online method.
'''SELECT * FROM payments WHERE method="online"'''

# Display all courses taught by a specific professor (professor_id = 2).
'''SELECT * FROM courses WHERE professor_id=2'''

# Retrieve all students enrolled in the Spring 2025 semester.
'''SELECT * FROM students WHERE YEAR(admission_date) = 2025'''

# Show all payments greater than 200 $.
'''SELECT * FROM payments WHERE amount>200'''

# Retrieve students whose first name starts with the letter "A".
'''SELECT * FROM students WHERE first_name LIKE "a%"'''

# Display the names of courses in alphabetical order.
'''SELECT * FROM courses
ORDER BY name'''

# List students ordered by their admission date (newest first).
'''SELECT * FROM students
ORDER BY admission_date DESC'''

# Retrieve all students and their courses using a JOIN.
'''SELECT s.*,c.* FROM enrollments as e
JOIN students as s ON e.student_id = s.id
JOIN courses as c ON c.id = e.course_id'''

# Get the list of students who have not made any payments.
'''SELECT s.* FROM students as s
LEFT JOIN payments as p ON p.student_id = s.id
WHERE p.id IS NULL'''

# Calculate the total number of students using COUNT.
'''SELECT COUNT(*) as total_student FROM students'''

# Calculate the average score of all students using AVG.
'''SELECT AVG(score) as average_score FROM students'''

# Find the highest score recorded.
'''SELECT MAX(score) as max_score FROM students'''

# Show the number of students in each major using GROUP BY major.
'''SELECT major,COUNT(*) as total_students_by_major FROM students
GROUP BY major'''

# Display the number of courses taught by each professor.
'''SELECT p.name as professor_name,COUNT(c.professor_id) as total_courses FROM professors as p
JOIN courses as c ON c.professor_id = p.id
GROUP BY c.professor_id'''

# Get the list of students with an average score higher than 80.
'''SELECT * FROM students WHERE score>80'''

# Generate a payment report grouped by payment method (cash, online, card).
'''SELECT method,COUNT(*) as total_payment_student_by_method FROM payments
GROUP BY method'''

# Create a VIEW that shows the average score of each student.
'''CREATE VIEW show_total_score_of_every_students AS (
	SELECT first_name,AVG(score) as total_students FROM students 
    GROUP BY id
)'''

# Display all students who have not enrolled in any course.
'''SELECT s.* 
FROM students s
LEFT JOIN enrollments e ON s.id = e.student_id
WHERE e.id IS NULL;'''

# Use HAVING to get only the professors who teach more than 2 courses.
'''SELECT p.*,COUNT(c.professor_id) as total_courses FROM professors as p
JOIN courses as c ON c.professor_id=p.id
GROUP BY p.id
HAVING total_courses>2'''

# Use IN to get students with IDs (1, 2, 3).
'''SELECT * FROM students WHERE id IN (1,2,3)'''

# Use BETWEEN to display payments between 2024-01-01 and 2024-12-31.
'''SELECT * FROM payments WHERE payment_date BETWEEN '2025-01-01' AND '2025-12-31'''

# Use LIKE to get emails that end with @gmail.com.
'''SELECT * FROM students WHERE email LIKE '%@gmail.com'''

# Write a subquery to find the student who made the highest payment.
'''SELECT * FROM students WHERE id in (
	SELECT student_id FROM payments
    ORDER BY amount DESC
    LIMIT 1
)'''

# Get the list of courses that have no students enrolled.
'''SELECT c.* 
FROM courses c
LEFT JOIN enrollments e ON c.id = e.course_id
WHERE e.id IS NULL;'''

# Count the number of books per author in the Books table.
'''SELECT author,COUNT(*) AS total_books FROM books
group by author'''

# Order all students by their admission date (ORDER BY).
'''SELECT * FROM students 
ORDER BY admission_date'''

# Write a three-table JOIN query to display the student name, course name, and professor name together.
'''SELECT s.first_name as student_name,c.name as course_name,p.name as professor_name FROM enrollments as e
JOIN students as s ON s.id=e.student_id
JOIN courses as c ON c.id=e.course_id
JOIN professors as p ON p.id=c.professor_id'''

# Create a Stored Procedure to register a student in a course.
'''DELIMITER //
CREATE PROCEDURE register_student(
	IN student_id INT, 
    IN course_id INT, 
    IN semester INT, 
    IN grade INT
)
BEGIN
	INSERT INTO enrollments(student_id,course_id,semester,grade)
    VALUES(student_id, course_id, semester, grade);
END//
DELIMITER;'''

# Create a Stored Procedure to calculate the GPA of a student.
'''DELIMITER //
CREATE PROCEDURE count_average_score(
	IN input_student_id INT
)
BEGIN
	SELECT AVG(grade) AS average_score
    FROM enrollments
    WHERE student_id = input_student_id;
END;
DELIMITER //'''

# Create a Trigger to update the student’s GPA in the Students table whenever a new grade is inserted.
'''DELIMITER //
CREATE TRIGGER update_average_score
AFTER INSERT ON enrollments
FOR EACH ROW
BEGIN
	DECLARE avg_score DECIMAL(5,2);
    SELECT AVG(grade) INTO avg_score 
    FROM enrollments 
    WHERE student_id = NEW.student_id;

    UPDATE students 
    SET average_score = avg_score
    WHERE id = NEW.student_id;
END;
DELIMITER//'''

# Create a Trigger to change the student’s status to active when a successful payment is recorded.
'''DELIMITER //
CREATE TRIGGER change_payment_status
AFTER INSERT ON payments
FOR EACH ROW
BEGIN
	UPDATE students
    SET status = 'active'
    WHERE id = NEW.student_id AND NEW.amount > 0;
END;
DELIMITER //'''

# Create a Transaction for: inserting a payment → recording a transaction → updating the student’s status (all or none).
'''START TRANSACTION;

INSERT INTO payments(student_id, amount, payment_date, method, status)
VALUES (1, 200, CURDATE(), 'card', 'success');

INSERT INTO transactions(student_id, amount, trans_date)
VALUES (1, 200, NOW());

UPDATE students SET status='active' WHERE id=1;

COMMIT;'''

# Create an INDEX on the email column in the Students table.
'''CREATE INDEX idx_email ON students (email)'''

# Use the EXPLAIN command to check which queries are slow.
'''EXPLAIN SELECT * FROM students WHERE email='ajmal@gmail.com'''

# Partition the Payments table by year (PARTITION BY YEAR(date)).
'''CREATE TABLE payments(id INT PRIMARY KEY AUTO_INCREMENT,student_id INT,amount INT,payment_date DATE,method VARCHAR(100),status boolean)
PARTITION BY RANGE(YEAR(payment_date)) (
	PARTITION p0 VALUES LESS THAN (2021),
    PARTITION p1 VALUES LESS THAN (2022),
    PARTITION p2 VALUES LESS THAN (2023),
    PARTITION p3 VALUES LESS THAN (2024),
    PARTITION p_future VALUES LESS THAN MAXVALUE
);'''

# Create a Function that returns the number of courses a student is enrolled in.
'''DELIMITER //
CREATE FUNCTION total_course_each_student(input_student_id INT)
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE total_course INT;
    SELECT COUNT(*) INTO total_course 
    FROM enrollments
    WHERE student_id = input_student_id;
    RETURN total_course;
END //
DELIMITER ;'''

# Create a View for the report: “student + number of courses + total payments.”
'''CREATE VIEW global_reports AS
SELECT s.id, s.name, COUNT(e.course_id) AS total_courses, 
       SUM(p.amount) AS total_payments
FROM students s
LEFT JOIN enrollments e ON s.id = e.student_id
LEFT JOIN payments p ON s.id = p.student_id
GROUP BY s.id, s.name;'''

# Create a Role named ProfessorRole that can only view the Courses and Grades tables.
'''CREATE ROLE professorRole;
GRANT SELECT ON university.courses TO professorRole;
GRANT SELECT ON university.grades TO professorRole;'''

# Create a User named student_user who only has SELECT permission on the Courses table.
'''CREATE USER 'student_user'@'%' IDENTIFIED BY 'password123';
GRANT SELECT ON university.courses TO 'student_user'@'%';'''

# Create an Event that runs every night to check overdue payments.
'''CREATE EVENT check_payments_status
ON SCHEDULE EVERY 1 DAY
DO
    UPDATE students 
    SET status = 'inactive'
    WHERE id IN (
        SELECT student_id 
        FROM payments 
        WHERE status='unpaid'
    );'''

# Add a CHECK constraint to ensure grades are between 0 and 100.
'''ALTER TABLE students
ADD CONSTRAINT chk_score CHECK (score>=0 AND score<=100)'''

# Add a CHECK constraint to ensure course credits are between 1 and 6.
'''ALTER TABLE courses
ADD CONSTRAINT chk_credits CHECK (credits >0 AND credits < 7)'''

# Create a FULLTEXT INDEX on the Books table and perform searches on title and author.
'''CREATE FULLTEXT INDEX idx_books_search ON books (title,author)'''

# Create a Stored Procedure to get the list of students with a specific financial status (paid, unpaid).
'''DELIMITER //
CREATE PROCEDURE students_list(IN payment_status VARCHAR(20))
BEGIN
    SELECT s.*, p.status 
    FROM students s
    JOIN payments p ON s.id = p.student_id
    WHERE p.status = payment_status;
END //
DELIMITER ;'''

# Use a CTE (WITH) to display the list of students who are enrolled in more than 3 courses.
'''WITH students_list AS (
    SELECT s.id, s.name, COUNT(e.course_id) AS total_courses
    FROM students s
    JOIN enrollments e ON e.student_id = s.id
    GROUP BY s.id, s.name
    HAVING COUNT(e.course_id) > 3
)
SELECT * FROM students_list;'''

# Add a JSON column named extra_info in the Students table to store additional information (e.g., address, hobbies).
'''ALTER TABLE students ADD COLUMN extra_info JSON;'''