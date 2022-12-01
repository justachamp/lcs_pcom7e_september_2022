### SQL LAB
1. Selecting Employee name, Department name and Employee salary
Left joining DEPT table to get Department name.
Join is LEFT owing to even if department cannot be found
we will  get employees with filtered salary.  

```sql
   SELECT EMP.ENAME, DEPT.DNAME, EMP.SAL
   FROM EMP
   LEFT JOIN DEPT ON DEPT.DEPTNO = EMP.DEPTNO
   WHERE EMP.SAL BETWEEN 1000 AND 2000;
```
   
Alternatively we could filter result in the following way  
    
 ```sql
       SELECT EMP.ENAME, DEPT.DNAME, EMP.SAL
       FROM EMP
       LEFT JOIN DEPT ON DEPT.DEPTNO = EMP.DEPTNO
       WHERE EMP.SAL > 1000 
         AND EMP.SAL < 2000;
```

2. Selecting the number of people who receive a salary
and the number of people who receive a commission
Filtering by DEPTNO  
! Note commission with 0.00 is also counted as receiving a commission

 ```sql
    SELECT COUNT(EMP.SAL), COUNT(EMP.COMM)
    FROM EMP
    WHERE EMP.DEPTNO = 30;
```  


3. Selecting Employee name and salary,
whose Department location is Dallas
INNER JOINing DEPT into EMP because we need employees within only Dallas

 ```sql
    SELECT EMP.ENAME, EMP.SAL
    FROM EMP
    JOIN DEPT on DEPT.DEPTNO = EMP.DEPTNO
    WHERE DEPT.LOC = 'Dallas';
```  

4. Selecting Department with no employees.
LEFT JOINing EMP into DEPT and after the join filtering
the joined rows againts existence of EMP, so we will get
department with no employees
 ```sql
    SELECT DEPT.*
    FROM DEPT
    LEFT JOIN EMP on EMP.DEPTNO = DEPT.DEPTNO
    WHERE EMP.EMPNO IS NULL;
 ```  

Alternatively we could select all employee departments and then filter them against department id  
```sql
    SELECT DEPT.*
    FROM DEPT
    WHERE DEPT.DEPTNO NOT IN (SELECT EMP.DEPTNO FROM EMP)
```

5. Selecting Department Number and Average Salary by department
Using builtin function AVG to get average.
Using GROUP BY to get average salary for each department.  
If not using GROUP BY we will get the average for all departments, which is incorrect.   

```sql
    SELECT EMP.DEPTNO, AVG(EMP.SAL)
    FROM EMP
    GROUP BY EMP.DEPTNO;
```  