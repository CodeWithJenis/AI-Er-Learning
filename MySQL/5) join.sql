select
m.movie_id,title,budget,revenue,currency,unit
from movies m left join financials f 
on m.movie_id = f.budget

