-- Group rows by score and show how many have the same score, sorted by number descending
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;