-- Lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Records are ordered by descending rating.
SELECT `name`, SUM(`rate`) AS `rating`
  FROM `tv_genres` AS genres
       INNER JOIN `tv_show_genres` AS shows
       ON shows.`genre_id` = genres.`id`

       INNER JOIN `tv_show_ratings` AS rate
       ON rate.`show_id` = shows.`show_id`
 GROUP BY `name`
 ORDER BY `rating` DESC;
