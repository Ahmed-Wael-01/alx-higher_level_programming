-- list rows with some conditions
SELECT score, name FROM second_table WHERE name EXISTS ORDER BY score DESC;
