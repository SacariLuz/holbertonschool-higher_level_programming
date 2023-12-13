-- Lista todos los genros de hbtn_0d_tvshows y muestra el numero de programas vinculados a cada uno
-- No muestra generos sin programas vinculados
-- Los registros estan ordenadis por ascendente de programas
SELECT tv_genres.name AS genre, COUNT(*) AS number_of_shows FROM tv_genres AS tv_genres INNER JOIN tv_show_genres AS tv_show_genres ON tv_genres.id = tv_show_genres.genre_id GROUP BY tv_genres.name ORDER BY number_of_shows DESC;
