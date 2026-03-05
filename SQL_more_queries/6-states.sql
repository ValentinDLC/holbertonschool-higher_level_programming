-- This script creates the database hbtn_0d_usa if it does not exist.
-- Then it creates a table called states in that database.
-- The states table has two columns: id and name.
-- The id column is the primary key, unique, auto-incremented, and cannot be NULL.
-- The name column cannot be NULL, ensuring that every state has a name.

-- Create the database if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Use the database
USE hbtn_0d_usa;

-- Create the states table
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);