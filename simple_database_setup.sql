-- =====================================================
-- Simple Database Setup (Compatible with Original Code)
-- Student Management System
-- =====================================================

-- Create database
CREATE DATABASE IF NOT EXISTS project_sql;

-- Use the database
USE project_sql;

-- Create students table (original structure)
CREATE TABLE IF NOT EXISTS students (
    name VARCHAR(100) NOT NULL,
    roll VARCHAR(20) PRIMARY KEY,
    course VARCHAR(50) NOT NULL,
    semester VARCHAR(10) NOT NULL,
    fees DECIMAL(10,2) NOT NULL,
    date DATE NOT NULL
);

-- Insert sample data
INSERT IGNORE INTO students (name, roll, course, semester, fees, date) VALUES
('Satyam Kumar', '25MCA20346', 'MCA', '2', 75000.00, '2024-01-15'),
('Rahul Sharma', 'CS001', 'Computer Science', '6', 50000.00, '2024-01-16'),
('Priya Singh', 'CS002', 'Computer Science', '6', 50000.00, '2024-01-17'),
('Amit Kumar', 'ME001', 'Mechanical Engineering', '4', 45000.00, '2024-01-18'),
('Sneha Patel', 'EC001', 'Electronics', '2', 48000.00, '2024-01-19');

-- Show the table structure
DESCRIBE students;

-- Display all records
SELECT * FROM students;

-- Show success message
SELECT 'Simple database setup completed!' as Status;