-- ---------- Start Date 28-04-2025----------------------
use sakila;

select distinct(rental_duration) from sakila.film;

select distinct release_year, rating from film;

select title, release_year, rating
from film
where release_year = 2006 and rating = 'pg-13';

select film_id, title, rental_duration, rental_rate
from film
order by rental_duration, rental_rate;


select film_id, title, rental_duration, rental_rate, (rental_rate + round((20*rental_rate)/100)) as RENT
from film;


use school;
alter table students
add psp int;




update students
set first_name = "Abhishek", last_name = "Jain", psp=100
where student_id = 1;
select * from students;
select first_name from students where student_id != '102';

show variables like 'sql_safe_updates';

-- ---------- End Date 28-04-2025----------------------


--  ------------- Start Date 07-05-2025 --------

use school;
select * from students;


select avg(psp), batch_id from students
group by batch_id
-- where avg(psp) > 90   It get extecuted row by row not on the group
having avg(psp) > 70;  -- It get extecuted on the group
-- having batch_id = 1




select * from students where psp > (select psp from students where student_id = 4);

select * from students 
-- group by batch_id
where psp > (select min(psp) from students where batch_id = 3);

use sakila;
select * from sakila.film;

select avg(rental_rate)
from film;


select avg(rental_rate), release_year
from film
group by release_year;

use school;

select * from students
where psp > (select min(pspp) from (select avg(psp) as pspp, batch_id from students
group by batch_id) as xyz);

select * from students
where psp > All(select min(pspp) from (select avg(psp) as pspp, batch_id from students
group by batch_id) as xyz);

select * from students
where psp > Any(select min(pspp) from (select avg(psp) as pspp, batch_id from students
group by batch_id) as xyz);

select * from students s
where psp < (select avg(psp) from students
where batch_id = s.batch_id);



select * from sakila.actor a
where exists(select * from film_actor where actor_id = a.actor_id);




select * 
from activity a
where a.event_date = (select min(event_date) as event_date
from activity
group by player_id
order by player_id);


-- Indexing
use sakila;

desc actor;
select * 
from actor
where first_name = 'john';


-- query excution plan without index column
explain select * 
from actor
where first_name = 'john';


-- query excution plan with index column
explain select * 
from actor
where last_name = 'john';

-- query execution time difference on search based on indedexed and non indexed column

explain analyze select * 
from actor
where first_name = 'john';

-- -> Filter: (actor.first_name = 'john')  (cost=20.2 rows=20) (actual time=0.105..0.109 rows=1 loops=1)
     -- -> Table scan on actor  (cost=20.2 rows=200) (actual time=0.033..0.0937 rows=200 loops=1)
 

explain analyze select * 
from actor
where last_name = 'john';

-- -> Index lookup on actor using idx_actor_last_name (last_name='john')  (cost=0.35 rows=1) (actual time=0.0167..0.0167 rows=0 loops=1)
 
explain analyze select * 
from actor
where first_name = 'john' and last_name = 'john';

-- -> Filter: (actor.first_name = 'john')  (cost=0.26 rows=0.1) (actual time=0.0167..0.0167 rows=0 loops=1)
     -- -> Index lookup on actor using idx_actor_last_name (last_name='john')  (cost=0.26 rows=1) (actual time=0.0154..0.0154 rows=0 loops=1)
 
explain analyze select * 
from film
where title = 'adventure trip';


-- -> Index lookup on film using idx_title (title='adventure trip')  (cost=0.35 rows=1) (actual time=0.0187..0.0187 rows=0 loops=1)
 
 show variables like 'autocommit';
 
 