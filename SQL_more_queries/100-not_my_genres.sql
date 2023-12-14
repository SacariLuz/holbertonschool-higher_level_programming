-- Utilice la database hbtn_0d_tvshows para listar todos los generos no vinculados al programa dexter
-- Tabla tv_shows contiene solo un registro donde title=Dexter
-- Resultados deben estar ordenados de forma ascendente por nombre de genero
SELECT tv_genres.name FROM tv_genres LEFT JOIN (SELECT tv_genres.name AS bad FROM tv_genres INNER JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id WHERE tv_shows.title = 'Dexter' ORDER BY tv_genres.name) AS tb2 ON tv_genres.name = bad WHERE bad IS NULL ORDER BY tv_genres.name ASC;
