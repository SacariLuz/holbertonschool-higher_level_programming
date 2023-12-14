-- Listar todos los programas y generos vinvulados a ese programa  desde la database btn_0d_tvshows
-- Si un programa no tieen genero, muestra NULL
-- Resultados debem ordenarse de forma ascendente segun el tipode programa y genero
SELECT tv_shows.title, tv_genres.name FROM tv_shows LEFT JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id ORDER BY tv_shows.title ASC, tv_genres.name ASC;
