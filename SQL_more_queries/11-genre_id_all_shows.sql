-- Listar todos los programas contenidos en la datbase hbtn_0d_tvshows
-- Los resultados deben ordenarse en orden ascendente por tv_shows.title y tv_show_genres.genre_id
-- Muestra NULL si un programa no tiene genre
SELECT s.`title`, g.`genre_id`
  FROM `tv_shows` AS s
       LEFT JOIN `tv_show_genres` AS g
       ON s.`id` = g.`show_id`
 ORDER BY s.`title`, g.`genre_id`;
