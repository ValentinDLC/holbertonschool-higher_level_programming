-- In this script, I’m creating a MySQL user called user_0d_2.
-- The goal is to give this user only the SELECT privilege on the database hbtn_0d_2.
-- That means user_0d_2 will be able to read data, but not modify or delete it.
-- The password will be user_0d_2_pwd.

-- Create the database if it doesn’t exist yet
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Create the user if it doesn't exist
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'User_0d_2_Pwd!2025';

-- Grant only SELECT privilege on hbtn_0d_2 to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';

-- Apply the changes immediately
FLUSH PRIVILEGES;