-- Lista todos los programas sin genero comedia en la databse hbtn_0d_tvshows.
-- Cada registro muestre tv_shows.title
-- Resultados deben estar ordenados d forma ascendente segun progrmaa
SELECT tv_shows.title FROM tv_shows LEFT JOIN (SELECT tv_shows.title AS negative FROM tv_shows INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id WHERE tv_genres.name = 'Comedy' ORDER BY tv_shows.title ASC) WHERE tv_genres.name = 'Comedy' ORDER BY tv_shows.title ASC) ORDER BY tv_shows.title ASC;
