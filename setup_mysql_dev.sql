-- Sets up a MySQL server, establishing:
-- A database named hbnb_test_db.
-- An account named hbnb_test with the password hbnb_test_pwd, accessible only from localhost.
-- Full privileges for the hbnb_test user on the hbnb_test_db database.
-- The SELECT privilege specifically granted to the hbnb_test user for the performance_schema.

-- If the database doesn't exist, create it
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- If the user doesn't exist, create it and set the password
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on the hbnb_dev_db database to the hbnb_dev user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';

-- Grant SELECT privilege on the performance_schema database to the hbnb_dev user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';

-- Apply changes by flushing privileges
FLUSH PRIVILEGES;
