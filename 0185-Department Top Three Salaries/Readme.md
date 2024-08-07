```html
<h2><a href="https://leetcode.com/problems/high-earners">1. High Earners</a></h2><h3>Medium</h3><hr><p>A company's executives are interested in seeing who earns the most money in each of the company's departments. A high earner in a department is an employee who has a salary in the top three unique salaries for that department.</p>

<p>Write a solution to find the employees who are high earners in each of the departments.</p>

<p>Return the result table in any order.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre>
<strong>Input:</strong> 
Employee table:
+----+-------+--------+--------------+
| id | name  | salary | departmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 85000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
| 5  | Janet | 69000  | 1            |
| 6  | Randy | 85000  | 1            |
| 7  | Will  | 70000  | 1            |
+----+-------+--------+--------------+
Department table:
+----+-------+
| id | name  |
+----+-------+
| 1  | IT    |
| 2  | Sales |
+----+-------+
<strong>Output:</strong> 
+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Joe      | 85000  |
| IT         | Randy    | 85000  |
| IT         | Will     | 70000  |
| Sales      | Henry    | 80000  |
| Sales      | Sam      | 60000  |
+------------+----------+--------+
</pre>

<p><strong>Explanation:</strong></p>
<p>In the IT department:</p>
<ul>
<li>Max earns the highest unique salary</li>
<li>Both Randy and Joe earn the second-highest unique salary</li>
<li>Will earns the third-highest unique salary</li>
</ul>
<p>In the Sales department:</p>
<ul>
<li>Henry earns the highest salary</li>
<li>Sam earns the second-highest salary</li>
<li>There is no third-highest salary as there are only two employees</li>
</ul>

<p>&nbsp;</p>
<p><strong>Solution:</strong></p>
<pre>
SELECT d.name as Department, e.name as Employee, e.salary as Salary
FROM Employee e
JOIN Department d ON e.departmentId = d.id
WHERE e.salary IN (
    SELECT DISTINCT salary 
    FROM Employee e2 
    WHERE e2.departmentId = e.departmentId
    ORDER BY salary DESC
    LIMIT 3
)
ORDER BY d.name, e.salary DESC;
</pre>
```