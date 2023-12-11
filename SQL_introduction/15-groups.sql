-- Enumerar el numero de registros con la misma puntuacion en la tabla second_table
SELECT score AS score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY number DESC;
