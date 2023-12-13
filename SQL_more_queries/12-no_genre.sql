-- Listar todos los programas contenidos en hbtn_0d_tvshows sin genero vinculado
-- Los resultados deben ordenarse en froma ascendente
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows AS tv_shows
       LEFT JOIN `tv_show_genres` AS tv_show_genres
       ON tv_shows.`id` = tv_show_genres.`show_id`
       WHERE tv_show_genres.`genre_id` IS NULL
 ORDER BY tv_shows.`title`, tv_show_genres.`genre_id`;