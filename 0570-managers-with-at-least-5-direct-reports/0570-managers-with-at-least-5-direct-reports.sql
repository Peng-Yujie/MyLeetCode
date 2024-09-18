/* Write your T-SQL query statement below */
select name from Employee
where id in (
    select managerId from Employee
    group by managerId
    having count(managerID)>4
)