# having 
select 
release_year,count(*) as movies_count from movies
group by release_year
having movies_count > 2
order by movies_count desc;

# calculated columns:

select 
*,year(current_date())-birth_year as age from actors;

select *,
case
when unit = 'billions' then revenue*1000
when unit = 'thousands' then revenue/1000
else revenue
end as revenue_mil
from financials;