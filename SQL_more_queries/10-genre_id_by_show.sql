-- Lista todos los programas contenidos en hbtn_0d_tvshows
-- Resultados clasificarse en orden ascendente por tv_shows.title y tv_show_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows AS tv_shows INNER JOIN tv_show_genres AS tv_show_genres ON tv_shows.id = tv_show_genres.show_id GROUP BY tv_shows.title, tv_show_genres.genre_id;
