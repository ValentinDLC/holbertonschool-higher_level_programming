-- In this script, I’m creating a table called force_name inside the database hbtn_0d_2.
-- The table will contain two columns: id and name.
-- The id will store an integer value.
-- The name must always have a value — it cannot be NULL.
-- This kind of rule ensures that each record always has a valid name.

-- Select the correct database
USE hbtn_0d_2;

-- Create the table force_name with the required constraints
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);