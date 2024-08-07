# Write your MySQL query statement below
SELECT Department.Name AS "Department", e.Name AS "Employee", e.Salary FROM
(SELECT departmentId, Name, Salary, DENSE_RANK() OVER(PARTITION BY DepartmentId ORDER BY Salary DESC) AS r
FROM Employee) AS e
JOIN Department ON e.DepartmentID = Department.Id
WHERE r <= 3