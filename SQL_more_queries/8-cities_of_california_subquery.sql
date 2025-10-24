-- This script lists all cities of California in the hbtn_0d_usa database.
-- We use a subquery to get California's id from the states table.
-- Then we select all cities where state_id matches that id.
-- The results are sorted by cities.id in ascending order.

USE hbtn_0d_usa;

SELECT id, name
FROM cities
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
);