/* Write your T-SQL query statement below */
select a.name
from Employee a 
join Employee b 
on a.id=b.managerId
group by a.name
having count(*)>=5