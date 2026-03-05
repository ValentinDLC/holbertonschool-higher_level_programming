-- In this script, I’m creating a new MySQL user called user_0d_1.
-- The goal is to give this user full access (all privileges) on the entire MySQL server.
-- The password will be user_0d_1_pwd.
-- If the user already exists, the script should not fail.

-- Create user user_0d_1 if it doesn’t already exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'User_0d_1_Pwd!2025';

-- Grant all privileges on the entire server to this user
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Apply the privilege changes immediately
FLUSH PRIVILEGES;