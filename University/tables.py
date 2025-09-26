# Create Student Table
'''CREATE TABLE students(id INT PRIMARY KEY AUTO_INCREMENT, first_name VARCHAR(100) NOT NULL,
					  last_name VARCHAR(100) NOT NULL, email VARCHAR(100) NOT NULL,
                      phone INT NOT NULL,major VARCHAR(100) NOT NULL,
                      admission_date DATE DEFAULT '2025-02-01',
                      status ENUM('active','graduated','suspended')
					);'''

# Create Professors Table
'''CREATE TABLE professors(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100) NOT NULL,
						email VARCHAR(100) UNIQUE NOT NULL, department VARCHAR(100) NOT NULL,
                        hire_date DATE DEFAULT '2025-01-02'
					);'''

# Create Courses Table
'''CREATE TABLE courses(id INT PRIMARY KEY AUTO_INCREMENT, professor_id INT,
					 name VARCHAR(100) NOT NULL, credits INT, semester VARCHAR(100),
                     FOREIGN KEY (professor_id) REFERENCES professors(id) ON DELETE SET NULL ON UPDATE CASCADE 
				);'''
                
# Create Books Table
'''CREATE TABLE books(id INT PRIMARY KEY AUTO_INCREMENT, title VARCHAR(100) NOT NULL, 
				   author VARCHAR(100) NOT NULL, isbn VARCHAR(100) NOT NULL, 
                   available_copies INT
                );'''
                
# Create Enrollments Table
'''CREATE TABLE enrollments(id INT PRIMARY KEY AUTO_INCREMENT, student_id INT NOT NULL, 
						 course_id INT NOT NULL, semester INT NOT NULL, grade INT,
                         FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE ON UPDATE CASCADE,
                         FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE ON UPDATE CASCADE
                    );'''
                    
# Create Payments Table
'''CREATE TABLE payments(id INT PRIMARY KEY AUTO_INCREMENT, student_id INT NOT NULL,
					  amount INT NOT NULL, payment_date DATE DEFAULT '2025-01-02',
                      method ENUM('cash','card','online'), 
                      status ENUM('pending','completed','failed'),
					  FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE ON UPDATE CASCADE
                );'''
                
# Create Dormitories Table
'''CREATE TABLE dormitories(id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(100) NOT NULL,
						 capacity INT, dorm_type ENUM('male','female','mixed')
                    );'''
                    
# Create Rooms Table
'''CREATE TABLE rooms(id INT PRIMARY KEY AUTO_INCREMENT, dorm_id INT, 
				   room_number VARCHAR(100) NOT NULL, capacity INT,
                   FOREIGN KEY (dorm_id) REFERENCES dormitories(id) ON DELETE SET NULL ON UPDATE CASCADE
                );'''
                
# Create Borrowings Table
'''CREATE TABLE borrowings(id INT PRIMARY KEY AUTO_INCREMENT, student_id INT NOT NULL, 
						book_id INT NOT NULL, borrow_date DATE DEFAULT '2025-01-02',
                        return_date DATE DEFAULT '2025-03-04',
                        status ENUM('borrowed','returned','late'),
                        FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE ON UPDATE CASCADE,
                        FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE ON UPDATE CASCADE
                    );'''
                    
# Create Dormreservation Table
'''CREATE TABLE dormreservation(id INT PRIMARY KEY AUTO_INCREMENT, student_id INT NOT NULL,
							 room_id INT UNIQUE NOT NULL, start_date DATE DEFAULT '2025-01-02',
                             end_date DATE DEFAULT '2025-01-02', 
                             status ENUM('active','expired','cancelled'),
                             FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE ON UPDATE CASCADE,
                             FOREIGN KEY (room_id) REFERENCES rooms(id) ON DELETE CASCADE ON UPDATE CASCADE
                        );'''