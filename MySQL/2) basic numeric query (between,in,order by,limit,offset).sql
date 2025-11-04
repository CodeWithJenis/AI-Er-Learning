select * 
from movies 
where industry = "bollywood"
order by imdb_rating desc , release_year DESC limit 5 offset 1;