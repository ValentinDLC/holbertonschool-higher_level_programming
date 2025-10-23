-- Create first_table with id and name, only if it doesn't exist yet
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);