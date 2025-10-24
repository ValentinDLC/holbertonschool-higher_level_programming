-- This script creates the cities table in the database hbtn_0d_usa.
-- Each city has a unique id, a name, and a state_id referencing the states table.
-- The id column is primary key, auto-incremented, and cannot be NULL.
-- The state_id column is a foreign key that ensures the city belongs to a valid state.
-- The name column cannot be NULL.

-- Use the database
USE hbtn_0d_usa;

-- Create the cities table if it does not exist
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    CONSTRAINT fk_state
        FOREIGN KEY (state_id)
        REFERENCES states(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);