-- Usar atabase hbtn_0d_tvshows para listar todos los genros de la serie Dexter
-- Cada registro muestrs  tv_genres.name
-- Los resultados deben estar ordenados de forma ascendente por el nombre del genero
SELECT tv_genres.name FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.title = 'Dexter' ORDER BY tv_genres.name ASC;
