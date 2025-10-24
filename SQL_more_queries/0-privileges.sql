-- In this script, I’m listing all privileges of MySQL users user_0d_1 and user_0d_2.
-- The goal is to check what these users are allowed to do on my MySQL server.
-- For example: SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, etc.

-- Show all privileges granted to user_0d_1
SHOW GRANTS FOR 'user_0d_1'@'localhost';

-- Show all privileges granted to user_0d_2
SHOW GRANTS FOR 'user_0d_2'@'localhost';