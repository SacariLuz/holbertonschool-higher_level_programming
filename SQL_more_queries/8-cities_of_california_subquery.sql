-- Enumera todas las ciudades de California que se encuentren en la database hbtn_0d_usa
-- Ordenar de forma ascendente por cities.id
SELECT id, name FROM cities WHERE state_id IN(SELECT id FROM states WHERE name = 'California') ORDER BY id;
