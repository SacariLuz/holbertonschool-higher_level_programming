-- Lista todos los programas contenidos en hbtn_0d_tvshows
-- Resultados clasificarse en orden ascendente por tv_shows.title y tv_show_genres.genre_id
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
        INNER JOIN `tv_show_genres` AS g
	ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;
