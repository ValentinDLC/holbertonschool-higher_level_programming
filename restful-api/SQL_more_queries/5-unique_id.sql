-- In this script, I’m creating a table called unique_id in the database hbtn_0d_2.
-- The goal is to make sure each record has a unique identifier that automatically increases.
-- The id column will be the unique and auto-incremented primary key.
-- The name column will store text data (up to 256 characters).

-- Select the correct database
USE hbtn_0d_2;

-- Create the table unique_id with an auto-incremented and unique id
CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL AUTO_INCREMENT UNIQUE,
    name VARCHAR(256),
    PRIMARY KEY (id)
);