-- In this script, I’m creating a table called id_not_null in the database hbtn_0d_2.
-- The table has two columns: id and name.
-- The id column cannot be NULL and has a default value of 1.
-- This means that if I don’t provide an id value, MySQL will automatically use 1.
-- The name column can store a text value without any restriction.

-- Select the correct database
USE hbtn_0d_2;

-- Create the table id_not_null with default and NOT NULL constraints
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);