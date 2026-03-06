-- Create user_0d_1 with full privileges if not already exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
CREATE USER IF NOT EXISTS 'user_0d_1'@'%'         IDENTIFIED BY 'user_0d_1_pwd';

GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'%';

FLUSH PRIVILEGES;