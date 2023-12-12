-- Enumera todas las cities contenidas en database hbtn_0d_usa
-- Los resultados debe ordenarse en ascendente por cities.id
SELECT cities-id, cities.name, states.name FROM cities INNER JOIN states ON cities.state_id = states.id;
