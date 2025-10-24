-- List all rows where name is not empty, showing score then name, sorted by score descending
Select score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
 ORDER BY score DESC;