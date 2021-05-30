---
title: "Exercises 01"
---

# SQL Practice Questions

## Course 01: Course Name

### Week 01: Selecting and Retrieving Data
#### Quiz 01
***
1. This statement will return an error. Please list why.
    ```sql
    SELECT TrackID Name AlbumID
    FROM tracks
    ```
    1. It's missing comma after `TrackID`, and `Name`
    1. It doesn't state where to get the data from
    1. It lists too many columns

2. When using SQLite, what datatypes can you assign to a column when creating a new table? Select all that apply.
    1. Real
    1. Integer
    1. Null
    1. Text

3. Primary Keys must be unique values.
    1. True
    1. False

4. What is the query below missing in order to execute?
    1. Select
    1. A Comma
    1. From
    1. The Column Names

***
#### Answers 01

| Question | Answer |
| -------- | ------ |
| 1 | i |
| 2 | i, ii, iv |
| 3 | i |
| 4 | i |

***

#### Quiz 02
***
1. Select the jobs below that may use SQL in their work (select all that apply).
    1. Data Analyst
    1. Backend Developer
    1. Data Scientist
    1. QA Engineer
    1. DBA

2. How does a data scientist and DBA differ in how they use SQL?
    1. DBAs manage the database for other users.
    1. Data scientists don’t write complex queries.
    1. DBA’s are the only ones who merge datasets together.
    1. Data scientists only query the database and don’t create tables.

3. Which of the following statements are true of Entity Relationship (ER) Diagrams?
    1. They speed up your querying time.
    1. They show you the relationships between tables.
    1. They are usually a representation of a business process.
    1. They usually are represented in a visual format.
    1. They only represent entities in the diagram.
    1. They identify the Primary Keys

4. Select the query below that will retrieve all columns from the customers table.

    1. `RETRIEVE * FROM customers`
    1. ```sql
        SELECT
        FirstName
        ,LastName
        ,Address
        ,City
        ,State
        ,ZipCode
        ,PhoneNumber
        FROM customers
        ```
    1. `SELECT * FROM customers`
    1. `SELECT (*) FROM customers`

5. Select the query that will retrieve only the Customer First Name, Last Name, and Company.

    1. ```sql
        SELECT FirstName LastName Company
        FROM customers
        ```
    1. ```sql
        SELECT FirstName LastName Company
        FROM customers
        ```
    1. ```sql
        SELECT * FROM customers
        ```
    1. ```sql
        SELECT FirstName, LastName, Company
        FROM customers
        ```

6. The ER diagram below is depicting what kind of relationship between the EMPLOYEES and CUSTOMERS tables?
    1. One-to-one
    1. One-to-many
    1. Many-to-one
    1. Many-to-many

7. The data model depicted in the ER diagram below could be described as a ?
    1. Transactional Model
    1. Relational Model
    1. Star Schema

8. When using the `CREATE TABLE` command and creating new columns for that table, which of the following statements is true?
    1. You must insert data into all the columns while creating the table
    1. You must assign a data type to each column
    1. You can create the table and then assign data types later

9. Look at the values in the two columns below. Based on the values in each column, which column could potentially be used as a primary key?

    | Column 1 | Column 2 |
    | -------- | -------- |
    | 5 | 2 |
    | 6 | 4 |
    | 1 | 5 |
    | 2 | 5 |
    | 34 | 32 |
    | 8 | 6 |
    | 9 | 4 |

    1. Column 1
    1. Column 2
    1. Column 1 OR Column 2

10. In order to retrieve data from a table with SQL, every SQL statement must contain?
    1. `WHERE`
    1. `CREATE`
    1. `FIND`
    1. `SELECT`


***
#### Answers 02

| Question | Answer |
| -------- | ------ |
| 1 | all |
| 2 | i |
| 3 | ii, iii, iv, vi |
| 4 | iii |
| 5 | iv |
| 6 | ii |
| 7 | ii |
| 8 | ii |
| 9 | i |
| 10 | iv |

***

#### Quiz 03
***
1. For all of the questions in this quiz, we are using the Chinook database. All of the interactive code blocks have been setup to retrieve data only from this database.
Retrieve all the records from the Employees table.

1. Retrieve the FirstName, LastName, Birthdate, Address, City, and State from the Employees table.

1. Retrieve all the columns from the Tracks table, but only return 20 rows.

#### Answers 03
***
1. ```sql
    SELECT * FROM Employees;
    ```
2. ```sql
    SELECT FirstName, LastName, Birthdate, Address, City, State from Employees;
    ```
3. ```sql
    SELECT* FROM Tracks LIMIT 20;
    ```

***

### Week 02: Filtering, Sorting and Math
***
#### Quiz 01
***
For all the questions in this practice set, you will be using the Salary by Job Range Table. This is a single table titled: `salary_range_by_job_classification`. This table contains the following columns:
  * SetID
  * Job_Code
  * Eff_Date
  * Sal_End_Date
  * Salary_setID
  * Sal_Plan
  * Grade
  * Step
  * Biweekly_High_Rate
  * Biweekly_Low_Rate
  * Union_Code
  * Extended_Step
  * Pay_Type

1. Write the query to get distinct values for Extended_step.
2. Write a query to get, excluding $0.00, the minimum Biweekly_High_Rate of pay.
3. Query to get maximum Biweekly_High_Rate of pay.
4. Query to get pay type for all the job codes that start with '03'.
5. Query to find the Effective Date (eff_date) or Salary End Date (sal_end_date) for grade Q90H0.
6. Sort the Biweekly low rate in ascending order.
7. What Step are Job Codes 0110-0400.
8. What is the Biweekly High Rate minus the Biweekly Low Rate for job Code 0170?
9. What is the Extended Step for Pay Types M, H, and D?
10. What is the step for Union Code 990 and a Set ID of SFMTA or COMMN?

***
#### Answers 01
***
1. ```sql
    SELECT DISTINCT Extended_step FROM salary_range_by_job_classification;
    ```

2. ```sql
    Select MIN(Biweekly_high_Rate)
    From salary_range_by_job_classification
    WHERE Biweekly_high_Rate <> '$0.00';
    ```

3. ```sql
    Select MAX(Biweekly_high_Rate)
    From salary_range_by_job_classification;
    ```

4. ```sql
    SELECT job_code, pay_type
    FROM salary_range_by_job_classification
    WHERE Job_Code LIKE '03%';
    ```

5. ```sql
    Select grade, eff_date, sal_end_date
    FROM salary_range_by_job_classification
    wHERE grade = 'Q90H0';
    ```

6. ```sql
    SELECT Biweekly_Low_Rate
    FROM salary_range_by_job_classification
    ORDER BY Biweekly_Low_Rate ASC;
    ```

7. ```sql
    SELECT step, job_code FROM salary_range_by_job_classification
    WHERE job_code BETWEEN '0110' AND '0400';
    ```

8. ```sql
    SELECT Biweekly_High_Rate - Biweekly_Low_Rate
    FROM salary_range_by_job_classification
    WHERE Job_Code = '0170';
    ```

9. ```sql
    SELECT Extended_Step
    FROM salary_range_by_job_classification
    WHERE Pay_Type IN ('M', 'H', 'D');
    ```

10. ```sql
    SELECT Extended_Step, Union_Code, SetID
    FROM salary_range_by_job_classification
    WHERE Union_Code = 990 AND SetID IN ('SFMTA', 'COMMN');
    ```

***
#### Quiz 02
***
1. Filtering data is used to do which of the following? (select all that apply)
    1. Narrows down the results of the data.
    1. Reduce the time it takes to run the query
    1. Reduces the strain on the client application
    1. Helps you understand the contents of your data
    1. Removes unwanted data in a calculation

2. You are doing an analysis on musicians that start with the letter “K”. Select the correct query that would retrieve only the artists whose name starts with this letter.
    1. `SELECT name FROM Artists WHERE name LIKE ‘K%’;`
    2. `SELECT name FROM Artists WHERE name IN ‘K%’;`
    3. `SELECT name FROM Artists WHERE name LIKE ‘%K’;`
    4. `SELECT name FROM Artists WHERE name LIKE ‘%K%’;`

3. A null and a zero value effectively mean the same thing. True or false?
    1. True
    1. False

4. Select all that are true regarding wildcards (Select all that apply.)
    1. Wildcards can be used for non-text data items
    1. Wildcards at the end of search patterns take longer to run
    1. Wildcards take longer to run compared to a logical operator

5. Select the statements below that **ARE NOT** true of the ORDER BY clause (select all that apply).
    1. Cannot sort by a column not retrieved
    1. It's only applied to the column names it directly precedes
    1. Can take the name of one or more columns
    1. Can be anywhere in the select statement

6. Select all of the valid math operators in SQL (select all that apply).
    1. / (division)
    1. * (multiplication)
    1. ^ (exponents)
    1. + (addition)
    1. - (subtraction)

7. Which of the following is an aggregate function? (select all that apply)
    1. MAX()
    1. MIN()
    1. COUNT()
    1. DISTINCT()

8. Which of the following is true of GROUP BY clauses? (Select all that apply.)
1. NULLs will be grouped together if your Group By column contains NULLs
1. GROUP BY clauses can contain multiple columns
1. Every column in your select statement may/can be present in a group by clause, except for aggregated calculations.

9. Select the true statement below.
    1. WHERE filters after the data is grouped
    1. HAVING filters after the data is grouped.

10. Which is the correct order of occurrence in a SQL statement?
    1. select, from, where, order by, having
    1. select, from, where, group by, having
    1. select, group by, from, where, having
    1. select, having, where, group by

***
#### Answers 02
***

| Question | Answer |
| -------- | ------ |
| 1 | all |
| 2 | i |
| 3 | ii |
| 4 | ii, iii |
| 5 | i, iv |
| 6 | i, ii, iv, v |
| 7 | i, ii, iii |
| 8 | i, ii, iii |
| 9 | ii |
| 10 | ii |

***

#### Quiz 03
***
All of the questions in this quiz refer to the open source Chinook Database. Please familiarize yourself with the ER diagram to familiarize yourself with the table and column names to write accurate queries and get the appropriate answers.

1. Count of tracks that have a length of 5,000,000 milliseconds or more.
2. Count of invoices whose total is between $5 and $15 dollars.
3. Find all the customers from the following States: RJ, DF, AB, BC, CA, WA, NY.
4. Find all the invoices for customer 56 and 58 where the total was between $1.00 and $5.00.
5. Count of tracks whose name starts with 'All'.
6. Find all the customer emails that start with "J" and are from gmail.com.
7. Find all the invoices from the billing city Brasília, Edmonton, and Vancouver and sort in descending order by invoice ID.
8. Show the number of orders placed by each customer (hint: this is found in the invoices table) and sort the result by the number of orders in descending order.
9. Find the albums with 12 or more tracks.

***
#### Answers 03
***
1. ```sql
    SELECT COUNT(TrackId) FROM Tracks WHERE MIlliseconds > 5000000;
    ```
2. ```sql
    SELECT COUNT(InvoiceId) FROM Invoices WHERE Total BETWEEN 5 AND 15;
    ```
3. ```sql
    SELECT FirstName, LastName, Company FROM Customers
    WHERE STATE IN ('RJ', 'DF', 'AB', 'BC', 'CA', 'WA', 'NY');
    ```
4. ```sql
    SELECT * FROM Invoices WHERE CustomerId IN (56, 58) AND Total BETWEEN 1 AND 5;
    ```
5. ```sql
    SELECT COUNT(TrackId) FROM Tracks WHERE Name LIKE 'All%';
    ```
6. ```sql
    SELECT Email FROM Customers WHERE Email LIKE 'J%@gmail.com';
    ```
7. ```sql
    SELECT * FROM Invoices WHERE BillingCity IN ('Brasília', 'Edmonton', 'Vancouver') ORDER BY InvoiceId DESC;
    ```
8. ```sql
    SELECT CustomerId, COUNT(InvoiceId) AS total_items
    FROM Invoices GROUP BY CustomerId ORDER BY total_items DESC;
    ```
9. ```sql
    SELECT AlbumId, COUNT(TrackId) as total_tracks
    FROM Tracks GROUP BY AlbumId HAVING total_tracks >= 12;
    ```

***

### Week 03: Advanced Joins: Left, Right, and Full Outer Joins
***

#### Quiz 01
***
All of the questions in this quiz pull from the open source Chinook Database. Please refer to the ER Diagram and familiarize yourself with the table and column names to write accurate queries and get the appropriate answers.

1. How many albums does the artist Led Zeppelin have?
2. Create a list of album titles and the Track Ids for the artist "Audioslave".
3. Find the first and last name of any customer who does not have an invoice. Are there any customers returned from the query?
4. What is the total price for the album "Big Ones"? (assume each track costs $0.99)

***

#### Answers 01
***
1. ```sql
    SELECT COUNT(DISTINCT albums.Albumid)
    FROM albums INNER JOIN artists
    ON albums.Artistid = artists.Artistid
    WHERE artists.Name = 'Led Zeppelin';
    ```

2. ```sql
    SELECT artists.Name, albums.Albumid, tracks.Trackid
    FROM tracks INNER JOIN albums INNER JOIN artists
    ON tracks.Albumid = albums.Albumid AND albums.Artistid = artists.Artistid
    WHERE artists.Name = 'Audioslave';
    ```

3. ```sql
    SELECT FirstName, LastName
    FROM customers LEFT JOIN invoices
    ON customers.Customerid = invoices.Customerid
    WHERE Invoiceid IS NULL;
    ```

4. ```sql
    SELECT albums.Albumid, albums.Title, COUNT(tracks.Trackid)
    FROM tracks INNER JOIN albums
    ON tracks.Albumid = albums.Albumid
    WHERE albums.Title = 'Big Ones'
    GROUP BY albums.Albumid, albums.Title;
    ```

***

#### Quiz 02
***

1. Which of the following statements is true regarding subqueries?
    1. Subqueries will process whichever query you indicate for them to process first.
    1. Subqueries always process the innermost query first and the work outward.
    1. Subqueries always process the outermost query first and the work inward.

2. If you can accomplish the same outcome with a join or a subquery, which one should you always choose?
    1. A join because they are always faster
    1. A subquery because they are always faster
    1. Whichever one you understand better and can write faster.
    1. Joins are usually faster, but subqueries can be more reliable, so it depends on your situation.

3. The following diagram is a depiction of what type of join?
    1. Inner Join
    1. Left Join
    1. Right Join
    1. Full Outer Join

4. Select which of the following statements are true regarding inner joins. (Select all that apply)
    1. Inner joins retrieve all matching and nonmatching rows from a table
    1. Inner joins are one of the most popular types of joins use
    1. There is no limit to the number of table you can join with an inner join.
    1. Performance will most likely worsen with the more joins you make

5. Which of the following is true regarding Aliases? (Select all that apply.)
    1. Aliases are often used to make column names more readable.
    1. SQL aliases are used to give a table, or a column in a table, a temporary name.
    1. An alias only exists for the duration of the query.

6. What is wrong with the following query?

    ```sql
    SELECT Customers.CustomerName, Orders.OrderID
    FROM LEFT JOIN ON Customers.CustomerID = Orders.CustomerID FROM Orders AND Customers
    ORDER BY
    CustomerName;
    ```

    1. Should be using an inner join rather than a left join
    1. Column names do not have an alias
    1. The table name comes after the join condition

7. What is the difference between a left join and a right join?
    1. There is actually no difference between a left and a right join.
    1. A right join is always used before a full outer join, whereas a left join is always used after a full outer join
    1. The only difference between a left and right join is the order in which the tables are relating.
    1. A left join always is used before a right join in a query statement

8. If you perform a cartesian join on a table with 10 rows and a table with 20 rows, how many rows will there be in the output table?
    1. 200
    1. 20
    1. 10
    1. 15

9. Which of the following statements about Unions is true? (select all that apply)
    1. Each SELECT statement within UNION must have the same number of columns
    1. The columns must also have similar data types
    1. The order of the SELECTed columns in a UNION does not matter
    1. The UNION operator is used to combine the result-set of two or more SELECT statements

10. Data scientists need to use joins in order to: (select the best answer)
    1. Filter data from multiple tables.
    1. Retrieve data from multiple tables.
    1. Create new tables.

***

#### Answers 02
***

| Question | Answer |
| -------- | ------ |
| 1 | 2 |
| 2 | 4 |
| 3 | 1 |
| 4 | 2, 3, 4 |
| 5 | all |
| 6 | 3 |
| 7 | 3 |
| 8 | 1 |
| 9 | 1, 2, 4 |
| 10 | 2 |

***

#### Quiz 03
***
1. Using a subquery, find the names of all the tracks for the album "Californication".
2. Find the total number of invoices for each customer along with the customer's full name, city and email.
3. Retrieve the track name, album, artistID, and trackID for Trackid 12.
4. Retrieve a list with the managers last name, and the last name of the employees who report to him or her
5. Find the name and ID of the artists who do not have albums.
6. Use a UNION to create a list of all the employee's and customer's first names and last names ordered by the last name in descending order.
7. See if there are any customers who have a different city listed in their billing city versus their customer city.

***

#### Answers 03
***

1. ```sql
    SELECT Trackid, Name FROM Tracks
    WHERE Albumid IN (SELECT Albumid FROM Albums
                    WHERE Title = 'Californication')
    ORDER BY Trackid;
    ```
2. ```sql
    SELECT Customers.Customerid, FirstName, LastName, Email, COUNT(InvoiceId)
    FROM Customers LEFT JOIN Invoices
    ON Customers.Customerid = Invoices.Customerid
    GROUP BY Customers.Customerid;
    ```
3. ```sql
    SELECT Tracks.Name, Albums.Title, Albums.ArtistID, Tracks.Trackid
    FROM TRACKS INNER JOIN Albums
    ON Tracks.Albumid = Albums.Albumid
    WHERE Tracks.Trackid = 12;
    ```
4. ```sql
    SELECT a.EmployeeID as managerid, a.LastName as managerLastName,
    b.EmployeeID as employeeid, b.LastName as employeeLastName
    FROM EMPLOYEES a LEFT JOIN EMPLOYEES b
    ON b.ReportsTo = a.EmployeeID
    WHERE b.EmployeeID IS NOT NULL;
    ```
5. ```sql
    SELECT Artists.ArtistID, Artists.Name
    FROM Artists LEFT JOIN Albums
    ON Artists.Artistid = Albums.Artistid
    WHERE Albums.Artistid IS NULL;
    ```
6. ```sql
    SELECT Customers.FirstName, Customers.LastName
    FROM Customers
    UNION
    SELECT Employees.FirstName, Employees.LastName
    FROM Employees
    ORDER BY LastName DESC;
    ```
7. ```sql
    SELECT Customers.Customerid, Customers.City, Invoices.BillingCity
    FROM Customers INNER JOIN Invoices
    On Customers.Customerid = Invoices.Customerid
    WHERE Customers.City <> Invoices.BillingCity;
    ```

***

### Week 04: Strings, Date and Time
***

#### Quiz 01

1. Which of the following are supported in SQL when dealing with strings? (Select all that apply)
    1. Upper
    1. Lower
    1. Trim
    1. Substring
    1. Concatenate

2. What will the result of the statement be? `SELECT SUBSTR('You are beautiful.', 3)`
    1. u are beautiful.
    1. You are beautiful.
    1. This will return an error
    1. beautiful.

3. What are the results of the following query? `SELECT * orders WHERE order_date = ‘2017-07-15’`
   Additional information:
   Orders = integer
   Order_date = datetime
    1. You will get all the orders with an order date of 2017-07-15.
    1. You won't get any results.
    1. You will get all of the orders.

4. Case statements can only be used for which of the following statements (select all that apply)?
    1. Delete
    1. Select
    1. Update
    1. Insert

5. Which of the following is FALSE regarding views?
    1. Views are stored in a query
    1. Views will remain after the database connection has ended
    1. Views can be used to encapsulate queries

6. You are only allowed to have one condition in a case statement. True or false?
    1. True
    1. False

7. Select the correct SQL syntax for creating a view.
    1. `CREATE VIEW AS SELECT * FROM customers WHERE Name LIKE '%I';`
    2. `CREATE VIEW customers AS SELECT * FROM customers WHERE Name LIKE '%I';`
    3. `INSERT VIEW customers AS Select * FROM customers WHERE Name LIKE '%I';`

8. Profiling data is helpful for which of the following? (Select all that apply)
    1. Joining tables together
    1. Filter out unwanted data elements
    1. Understanding your data

9. What is the most important step before beginning to write queries?
    1. Understanding your data
    1. Deciding what tables you want to join
    1. Deciding what should be done on the client application vs the RDMS

10. When debugging a query, what should you always remember to do first?
    1. Make sure you didn’t miss any commas.
    1. Start with the inner most query
    1. Start simple and break it down first
    1. Start by examining the joins

***

#### Answers 01
***

| Question | Answer |
| -------- | ------ |
| 1 | all |
| 2 | 1 |
| 3 | 2 |
| 4 | all |
| 5 | 2 |
| 6 | 2 |
| 7 | 2 |
| 8 | 2, 3 |
| 9 | 1 |
| 10 | 3 |

***

#### Quiz 02
1. Pull a list of customer ids with the customer’s full name, and address, along with combining their city and country together. Be sure to make a space in between these two and make it UPPER CASE. (e.g. LOS ANGELES USA)
2. Create a new employee user id by combining the first 4 letters of the employee’s first name with the first 2 letters of the employee’s last name. Make the new field lower case.
3. Show a list of employees who have worked for the company for 15 or more years using the current date function. Sort by lastname ascending.

***

#### Answers 02
1. `SELECT FirstName, LastName, UPPER(City || " " || Country) AS Location FROM Customers;`
2. `SELECT LOWER(SUBSTR(FirstName, 1, 4) || SUBSTR(LastName, 1, 2)) FROM Employees;`
3. `SELECT FirstName, LastName, STRFTIME('%Y', DATE('now')) - STRFTIME('%Y', HireDate) AS Experience FROM Employees WHERE STRFTIME('%Y', DATE('now')) - STRFTIME('%Y', HireDate) > 15 ORDER BY LastName ASC;`

***
