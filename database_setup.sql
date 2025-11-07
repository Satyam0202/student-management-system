-- =====================================================
-- Student Management System Database Setup Script
-- Created by: Satyam Kumar (25MCA20346)
-- =====================================================

-- Create database if it doesn't exist
CREATE DATABASE IF NOT EXISTS project_sql;

-- Use the database
USE project_sql;

-- Drop table if exists (for fresh setup)
-- Uncomment the line below if you want to recreate the table
-- DROP TABLE IF EXISTS students;

-- Create students table with enhanced structure
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    roll VARCHAR(20) UNIQUE NOT NULL,
    course VARCHAR(50) NOT NULL,
    semester VARCHAR(10) NOT NULL,
    fees DECIMAL(10,2) NOT NULL DEFAULT 0.00,
    phone VARCHAR(15) NULL,
    email VARCHAR(100) NULL,
    address TEXT NULL,
    date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    
    -- Add indexes for better performance
    INDEX idx_roll (roll),
    INDEX idx_course (course),
    INDEX idx_name (name),
    INDEX idx_date (date)
);

-- Insert sample data (optional)
INSERT INTO students (name, roll, course, semester, fees, phone, email, address, date) VALUES
('Rahul Sharma', 'CS001', 'Computer Science', '6', 50000.00, '9876543210', 'rahul@email.com', 'Delhi, India', '2024-01-15'),
('Priya Singh', 'CS002', 'Computer Science', '6', 50000.00, '9876543211', 'priya@email.com', 'Mumbai, India', '2024-01-16'),
('Amit Kumar', 'ME001', 'Mechanical Engineering', '4', 45000.00, '9876543212', 'amit@email.com', 'Pune, India', '2024-01-17'),
('Sneha Patel', 'EC001', 'Electronics', '2', 48000.00, '9876543213', 'sneha@email.com', 'Bangalore, India', '2024-01-18'),
('Vikash Gupta', 'CS003', 'Computer Science', '8', 50000.00, '9876543214', 'vikash@email.com', 'Hyderabad, India', '2024-01-19');

-- Create a view for student statistics (optional)
CREATE OR REPLACE VIEW student_statistics AS
SELECT 
    COUNT(*) as total_students,
    COUNT(DISTINCT course) as total_courses,
    SUM(fees) as total_fees_collected,
    AVG(fees) as average_fees,
    COUNT(CASE WHEN MONTH(date) = MONTH(CURDATE()) AND YEAR(date) = YEAR(CURDATE()) THEN 1 END) as monthly_admissions
FROM students;

-- Create a view for course-wise statistics (optional)
CREATE OR REPLACE VIEW course_statistics AS
SELECT 
    course,
    COUNT(*) as student_count,
    SUM(fees) as total_fees,
    AVG(fees) as average_fees,
    MIN(date) as first_admission,
    MAX(date) as latest_admission
FROM students 
GROUP BY course
ORDER BY student_count DESC;

-- Show table structure
DESCRIBE students;

-- Display sample data
SELECT * FROM students LIMIT 5;

-- Display statistics
SELECT * FROM student_statistics;

-- Display course-wise statistics
SELECT * FROM course_statistics;

-- =====================================================
-- Additional useful queries for the application
-- =====================================================

-- Query to find students by course
-- SELECT * FROM students WHERE course = 'Computer Science';

-- Query to find students admitted in current month
-- SELECT * FROM students WHERE MONTH(date) = MONTH(CURDATE()) AND YEAR(date) = YEAR(CURDATE());

-- Query to find top fee payers
-- SELECT name, roll, course, fees FROM students ORDER BY fees DESC LIMIT 10;

-- Query to find students by semester
-- SELECT * FROM students WHERE semester = '6';

-- Query to search students by name or roll
-- SELECT * FROM students WHERE name LIKE '%rahul%' OR roll LIKE '%CS%';

-- =====================================================
-- Backup and Maintenance Commands
-- =====================================================

-- Create backup of the database
-- mysqldump -u root -p project_sql > student_backup.sql

-- Restore from backup
-- mysql -u root -p project_sql < student_backup.sql

-- Check table size and row count
-- SELECT 
--     table_name,
--     table_rows,
--     ROUND(((data_length + index_length) / 1024 / 1024), 2) AS 'Size (MB)'
-- FROM information_schema.tables 
-- WHERE table_schema = 'project_sql';

SHOW TABLES;

-- Success message
SELECT 'Database setup completed successfully!' as Status;