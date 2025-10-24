-- This script lists all cities in hbtn_0d_usa with their state names.
-- We use a JOIN to combine cities and states.
-- Each city shows its id, name, and the name of its state.
-- Results are sorted by cities.id ascending.

USE hbtn_0d_usa;

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;