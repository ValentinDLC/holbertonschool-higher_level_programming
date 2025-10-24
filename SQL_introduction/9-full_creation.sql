-- Create second_table with id, name, score if missing, then insert multiple rows
DROP TABLE IF EXISTS second_table;
CREATE TABLE second_table (
    id INT,
    name VARCHAR(256),
    score INT
);
INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8);