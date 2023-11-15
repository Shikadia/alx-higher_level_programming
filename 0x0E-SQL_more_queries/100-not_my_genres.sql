-- Lists all genres of the database hbtn_0d_tvshows unlinked to the show Dexter.
-- Records are sorted by ascending genre name.
SELECT DISTINCT `name`
    FROM `tv_genres`
    WHERE `name` NOT IN
        (SELECT `name` FROM tv_genres
            LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id

            LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
            WHERE tv_shows.title = 'Dexter')
ORDER BY tv_genres.`name`;
