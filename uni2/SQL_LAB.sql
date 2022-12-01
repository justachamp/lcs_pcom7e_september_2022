mysql;
USE COMPANY1;


/*
  1. Selecting Employee name, Department name and Employee salary
  Left joining DEPT table to get Department name.
  Join is LEFT owing to even if department cannot be found
  we will  get employees with filtered salary.
*/
SELECT EMP.ENAME, DEPT.DNAME, EMP.SAL
FROM EMP
LEFT JOIN DEPT ON DEPT.DEPTNO = EMP.DEPTNO
WHERE EMP.SAL BETWEEN 1000 AND 2000;

/*
  2. Selecting the number of people who receive a salary
  and the number of people who receive a commission
  Filtering by DEPTNO

  ! Note commission with 0.00 is also counted as receiving a commission
*/
SELECT COUNT(EMP.SAL), COUNT(EMP.COMM)
FROM EMP
WHERE EMP.DEPTNO = 30;


/*
  3. Selecting Employee name and salary,
  whose Department location is Dallas
  INNER JOINing DEPT into EMP beacause we need employees within only Dallas

*/
SELECT EMP.ENAME, EMP.SAL
FROM EMP
JOIN DEPT on DEPT.DEPTNO = EMP.DEPTNO
WHERE DEPT.LOC = 'Dallas';

/*
  4. Selecting Department with no employees.
  LEFT JOINing EMP into DEPT and after the join filtering
  the joined rows againts existence of EMP, so we will get
  department with no employees
*/

SELECT DEPT.*
FROM DEPT
LEFT JOIN EMP on EMP.DEPTNO = DEPT.DEPTNO
WHERE EMP.EMPNO IS NULL;

/*
  5. Selecting Department Number and Average Salary by department
  Using builtin function AVG to get average.
  Using GROUP BY to get average salary for each department.
*/

SELECT EMP.DEPTNO, AVG(EMP.SAL)
FROM EMP
GROUP BY EMP.DEPTNO
;
