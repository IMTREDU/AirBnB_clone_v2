-- Establishes a MySQL server setup with the following configurations:
-- Database named hbnb_test_db.
-- User named hbnb_test with the password hbnb_test_pwd on the localhost.
-- Grants all privileges for the user hbnb_test on the database hbnb_test_db.
-- Grants SELECT privilege for the user hbnb_test on the performance_schema.

-- Create database if not exists
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- Create user if not exists
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant privileges to the user
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';

-- Grant all privileges on performance_schema to hbnb_test
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';

-- Flush priviliages to apply changes
FLUSH PRIVILEGES;
