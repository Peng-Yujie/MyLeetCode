/* Write your T-SQL query statement below */
select w1.id
from weather w1
join weather w2
on w1.recordDate = dateadd(day, 1, w2.recordDate)
where w1.temperature > w2.temperature