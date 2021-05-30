---
title: "SQL"
---

# SQL
SQL is structured Query Language. It is the main language to help interact with a relational database. SQL is a non procedural language, meaning it cannot be used to create full fledged applications.
It is used to read/retrieve data, and write/update/insert data. Different Database Management Systems (DBMS) will have slightly different syntaxes for SQL.

## Data Model
Database and Tables

| Name | Description |
| ---- | ----------- |
| Database | A container (file or set of files) to store organized data or related data together. |
| Tables | A structured list of data or of specific type. |
| Columns | A single field in a Table. All data in a column is of the same type. A table has multiple columns. |
| Rows | A single data point; a single record in the table. |



**Data Model**: Organizes and stores information in multiple tables. This will help us define relationships between the different tables and how they might combine with each other to yield more data. This model can represent a business process or relationships between business processes. It must closely represent the real world.

Building blocks of a data model

| Type | Description |
| ---- | ----------- |
| Entity | Person, place, thing or event which is uniquely identifiable and distinct. |
| Attribute | Characteristic of an entity, like age, gender etc. |
| Relationship | Describes association between different attributes. |

There are three types of relationships

| Type | Description |
| ---- | ----------- |
| One to Many | List of transactions for a customer falls in this category. One person from the customer table can have several transaction entries in the transaction table. |
| Many to Many | Students to classes is a classic example of such a relationship. One student is mapped to multiple classes and vice versa. |
| One to One | Suppose we have two entities: store and manager, then the relationship between store and manager is one to one since there is a unique manager per store. |

**ER Diagrams** help us show these relationships between different tables visually, and the relationships shown are the keys that can help relate the different tables.

**Primary Key** are columns or set of columns that uniquely identify a single record in the table. For instance, CustomerID in a customer table.
**Foreign Key** on the other hand, are formed by the concatenation of multiple columns to help identify a unique record in the table.

There are multiple notations to represent ER Diagrams

| Type | Description |
| ---- | ----------- |
| Chen Notation | `1` represents one, and `M` represents many. Thus, a many to many relationship will have `M` on either end of the line joining two tables.|
| Crow's Foot Notation | Two perpendicular lines (also called rail track) represent one, while crows foot (isoceles triangle with an altitude from the different length side) represent many. |
| UML Class Diagram Notation | `1.1` represents one and `1.*` represents many. |

## Common Commands
### `SELECT`
The most useful command to retrieve data from a table. The syntax is
```sql
SELECT comma_separated_list_of_fields FROM table_name;
SELECT item_id, item_name from Products;
```
All columns can be selected using `*` wildcard
```sql
SELECT * FROM Products;
```
Select statement will return all records by default.
`FROM` is not always followed by a table name. It could also be a subquery.

### `LIMIT`
Limits the view of the data received. We can specify the number of records that our query must return
```sql
SELECT item_id, item_name from Products LIMIT 10;
```
The returned records are from the top of the table, i.e., `LIMIT 10` returns the first 10 records of the table.
In case the number of records asked for is more than the total records available in the table, all the records are returned and SQL will not raise an error.

### `CREATE TABLE`
Command to create a new table in an existing database. We specify the name and the list of columns (with their data types) in the command.
```sql
CREATE TABLE Products
(id     char(10)     PRIMARY KEY,
 name   char(40)     NOT NULL,
 price  decimal(8,2) NULL);
```
where `NOT NULL` means that this column has to have some value in it. `NULL` means that the entry can be empty (which is presence of nothing, this is different from an empty string). `PRIMARY KEY` specifies that this column will have all unique entries. This is `NOT NULL` by default. Multiple columns can be specified as the `PRIMARY KEY`. All these specifications must be present for the query to work without any error.

To create the table if it does not exists
```sql
CREATE TABLE IF NOT EXISTS table_name (...);
```

`PARTITION` information can also be added into the create table query as follows
```sql
CREATE TABLE Products
(id     char(10)     PRIMARY KEY,
 name   char(40)     NOT NULL,
 price  decimal(8,2) NULL)
PARTITION BY(
    category char(40)
);
```
Partitioning a table on a column is useful when that column is being frequently used in the queries. Date is a good example of this, wherein we might be using the date column for filtering at several places. Trimming down a subquery by using filters that will utilise the partitioning column can be a real time saver in large data sets.

### `INSERT INTO`
Insert statement allows insertion of data into a table
```sql
INSERT INTO Products (id, name, price)
VALUES ('1234567890', 'A Name', 98.21);
```
It is not necessary to specify the column names after the table name, but it is recommended to avoid any ambiguity, in case we are not inserting values into all columns. This way, we can be sure of which value goes into which column.

We can also use a query to insert data into the table from another existing table.
```sql
INSERT INTO PRODUCTS (id, name, price)
SELECT * FROM PRODUCTS_1;
```

### `CREATE TEMPORARY TABLE`
Temporary tables are deleted when the current session is terminated. These are faster than creating a real table. Useful when we are working with complex joins which require saving intermediate data.
```sql
CREATE TEMPORARY TABLE table_name AS
( SELECT id, name from Products LIMIT 20);
```

### Comments in SQL
As always, write the comments so that anyone else (or even you) are able to understand the code when you look at it again in the future.
Single line comments
```sql
SELECT id
-- ,name
FROM Products;
```

Multi-line Comments
```sql
SELECT id,
/*,name
,price
*/
from Products;
```

### `WHERE`, `BETWEEN`
Helps get a subset of the data that is specific to our analysis. Filter allows increasing query performance, and databases are optimized to run filter operations. Hence, filtering the data first and then doing subsequent operations is preferred.
```sql
SELECT columns_list
FROM table_name
where column_name operator value;
```
Several operators are available for comparison.


| Operator | Description |
| -------- | ----------- |
| `=` | Check for equality. |
| `<>` | Check for inequality. Some DBMS may use `!=`. |
| `>`, `<` | Greater than and less than respectively. |
| `>=`, `<=` | Greater than or equal to, and less than or equal to respectively. |
| `BETWEEN` | Check if the column value is inside an inclusive range. |
| `IS NULL` | Check if the value is NULL. |
| `IN` | Specifies a range of conditions where we use a comma separated list of values enclosed in brackets. Instead of giving a list of values, it is also possible to give another query inside the round brackets. |
| `AND` | Specify multiple conditions for filtering, and all conditions must match. |
| `OR` | Specify multiple conditions for filtering, and at least one must be satisfied for the filter to work. Second condition is not evaluated if the first is met. It is faster and more convenient to use `IN` over `OR`.|
| `NOT` | Negation, can be combined with other operators listed above. |


When using `AND`, `OR` etc, it is better to use brackets to be as specific as possible. Different DBMS may have different order of operation depending on implementation.

```sql
SELECT customer_id from Customers WHERE customer_name = 'JANE';
SELECT customer_id from Customers WHERE age >= 18;
SELECT customer_id from Customers WHERE customer_name <> 'JANE';
SELECT customer_id from Customers WHERE age BETWEEN 18 AND 25;
SELECT customer_id from Customers WHERE customer_name IS NULL;
SELECT customer_id from Customers WHERE customer_name IN ('JANE', 'DOE');

SELECT customer_id from Customers
WHERE (customer_name = 'JANE' OR customer_name 'DOE') AND age >= 18;

SELECT customer_id from Customers WHERE NOT customer_name = 'DOE';
```

### Wildcards
Wildcards allow us to match text expressions partially. We can use a combination of text and wildcards to form our query. Uses `LIKE` as a predicate before specifying the filter condition. Wildcards can only be used with text data.


| Wildcard | Description |
| -------- | ----------- |
| `'%DOE'` | Grabs anything ending with `'DOE'`. |
| `'DOE%'` | Grabs anything starting with `'DOE'`. |
| `'%DOE%'` | Grabs anything containing `'DOE'`. |
| `'A%B'` | Grabs anything starting with `'A'` and ending with `'B'`. |
| `'_DOE'` | Underscore matches a single character (will not workn in DB2). |
| `'[ABC]DOE'` | Matches letters specified in the set of square brackets (does not work in SQLite.) |

`NULL` will not match with wildcards. Usage of wildcards can make the query slower. Hence, if possible, they should be substituted with equality check etc. Different DBMS will often have different implementaiton of the wildcards. Hence, it is important to first check how they will work in the DBMS being used.

### `ORDER BY`
After filtering data, we could also want to order/sort the data in a certain way.
```sql
SELECT something
FROM somewhere
ORDER BY some_columns
```
where multiple columns can be used for ordering by writing them in a comma separated manner. It is possible to use a column to sort if it is not present in the SELECT statement. `ORDER BY` must always be the **last clause** in a SELECT statement.

We can also order by column positions. `ORDER BY 2, 4` will sort by the second and fourth columns. To specify the direction of sort, we use the keywords `DESC` or `ASC` just after the column name. The keyword applies only the to the column name it is used just after. `ORDER BY 2 ASC, 4 DSC` will first sort the data in ascending order according to column 2, and then break any remaining ties by sorting with column 4 in descending order.

### Math Calculations
Basic math operations of addition, subtraction etc are available in SQL.
```sql
SELECT item_id, price * units AS TOTAL_PRICE
FROM Products;
```
`AS` is an alias for the new column we are creating. Even an existing column can be renamed using this keyword.

### Aggregation
Aggregation can be used to summarize data with different aggregations like min, max etc

| Function | Description |
| -------- | ----------- |
| `AVG(col)` | Average of a column. Row containing NULL will be ignored.|
| `COUNT()` | Counts the number of NON NULL entries. **Important distinction**, `COUNT(*)` will count all the rows in a table, whether they contain NULL values or not. `COUNT(col)` will ignore the NULL values when counting. |
| `MIN(col)`, `MAX(col)` | Finds the minimum and maximum value respectively. NULL values are ignored by both functions. |
| `SUM(col)` | Totals the column values. |


Note that we can also put a mathematical calculation inside the parentheses.


`DISTINCT` keyword can be used to force THE DBMS to only consider distinct values while doing the Aggregation. This keyword cannot be used with `MIN` and `MAX`.
```sql
SELECT COUNT(DISTINCT item_name) FROM Products;
```
Also note that all the aggregations done so far were on the entire data set.

### `COALESCE`
This operation will can be helpful for filling Null values in a result with other values. For instance, `COALESCE(column1, column2)` will use column1 value if it is not null, and if it is, will refer to the value from column2. We can also use fixed values instead as well, `COALESCE(number_column, 0)`.

### `GROUP BY` and `HAVING`
`GROUP BY` allows us to aggregate the data based on a certain column.
```sql
SELECT SUM(price) as total_price FROM Products
GROUP BY category;
```
will give us the total price grouped by the cateogry of the product. If we did not use the `GROUP BY` clause, the price would be totalled across all the products in the table.
`GROUP BY` can contain multiple columns. Every column in the `GROUP BY` must be present in the SELECT. NULL values will be grouped into a separate category.


`WHERE` will not work with `GROUP BY` as it filters on rows. We will use `HAVING` clause instead. `WHERE` filters before the data is grouped and `HAVING` afterwards. Rows eliminated in `WHERE` are not included in the group.
```sql
SELECT item_category, count(item_id) as total_items
FROM Products
GROUP BY item_category
HAVING count(item_id) > 4;
```
Usually, `ORDER BY` will follow a `GROUP BY` since the grouped data is not sorted.


Thus, a full query will be
```sql
SELECT list_of_columns_comma_separated
FROM table_name
WHERE some_filters_for_table_pre_grouping
GROUP BY list_of_columns_comma_separated
HAVING some_filters_post_grouping
ORDER BY list_of_columns_comma_separated;
```
***

### Subqueries
Queries embedded inside other queries. They are useful to merge data from multiple together, and also help with adding other filter criteria.
```sql
SELECT item_id, item_name from Products
WHERE item_id IN (
    SELECT item_id FROM Orders
    GROUP BY item_id
    HAVING SUM(total_orders) > 1000
);
```
It is usually a good idea to start with the innermost query which we will be using a filter criteria, and work outwards.
Some important points when using subqueries
  * There is no limit on the number of subqueries.
  * Performance will slow down if the nesting is done too deep.
  * **Subquery SELECT** can only have **single column** since it is usually used as a filter criteria.
  * Indentation is preferred for readability.

***

### Aliases
Aliases allow us to give short names to the tables for the duration of the query execution. This can help make column names more readable as we can use the alias to specify which table it is coming from. Furthermore, in case the same column name exists in multiple tables, using the alias will help avoid any confusion both for reader and DBMS.
```sql
SELECT table_alias.column_name
FROM table_name AS table_alias;
```
***

### JOINS
Joins allow associating records from one table with one or more tables. Using joins, we can retrieve data fro multiple tables by joining them together on the basis of certain columns. Joins only exist during the duration of query execution.
RIGHT and FULL OUTER joins are not available in SQLite.

*   `CROSS JOIN`
    Each row of the first table is matched with every record of the second table. Thus, the total records will be rows in first table X rows in second table.
    Cross join will not match on anything, but replicate every record in second table with first. They are most useful when we want to make a table with every store mapped to every category for example.
    ```sql
    SELECT item_name, item_order
    FROM Products CROSS JOIN Orders;
    ```
*   `INNER JOIN`
    Inner join will select records with matching value in both the tables.
    ```sql
    SELECT Products.item_id, Products.item_name, Orders.amount
    FROM Products JOIN Orders
    ON Products.item_id = Orders.item_id;
    ```
    It is possible to join multiple tables in a single query. To do so, we will list all the tables first, and then define the join keys/conditions. However, it should be noted that joining more tables together will decrease the overall database performance.
    ```sql
    SELECT p.item_id, o.amount, c.customer_id
    FROM (( Products p INNER JOIN Orders o
            ON p.item_id = o.item_id)
    INNER JOIN Customers c ON o.item_id = c.item_id);
    ```
    Placing a small alias just after the table name when it first first occurs, helps quickly and efficiently refer that table name in other places throughout the query. Idea is to type as less as possible, while keeping the shorthand logical.
*   `SELF JOIN`
    To do a self join means joining a table with itself. To do this, we can use aliases and denote the same table with two different names
    ```sql
    SELECT a.column AS column1, b.column AS column2
    FROM table AS a INNER JOIN table AS b
    ON a.column = b.column ORDER BY a.column;
    ```
    This query will return a table where for every matching key, we will have created many duplicate entries. Without aliases, this join will not be possible.
*   `LEFT JOIN`
    Returns all the records from the left table, and only those records from the right table which have a matching key in left table. Good for appending information to the left table from the right table.
    ```sql
    SELECT p.item_name, c.item_cost
    FROM Products p LEFT JOIN Costs c
    ON p.item_id = c.item_id ORDER BY p.item_name;
    ```
*   `RIGHT JOIN`
    This is similar to `LEFT JOIN` but returns all records from right table, and only those from left table that have a matching key in the right table.
*   `FULL OUTER JOIN`
    Returns all records from both the left and right table. But, for the ones that are found in left but not in right, the key column corresponding to the right table will be NULL. Keys present in both left and right could cause duplication of records if they are not the primary keys on both sides.

***

### `UNION` and `UNION ALL`
`UNION` is used to combine the results of two SELECT statements together. It is similar to a vertical append/stack operation. Some key points to remember when doing a `UNION`
*   The same number of columns must be selected in both SELECT statements.
*   The order of columns must be same.
*   The data types of corresponding columns must be same.
*   `UNION` does a `SELECT DISTINCT` on the resulting data set by defualt. Thus, if there are any duplicates after combining the datasets (or even in a single data set for that matter), only one unique record will be kept.

```sql
SELECT item_id, item_name FROM Products_CountryA
WHERE item_name LIKE 'SOAP%'
UNION
SELECT item_id, item_name FROM Products_CountryB
WHERE item_name LIKE 'SOAP%';
```

`UNION ALL` on the other hand will not drop any duplicates, and will keep all rows from all the datasets. Thus, if we know the data does not contain any duplicates, `UNION ALL` will be faster since we skip the `SELECT DISTINCT` (in `UNION`).

***

### Working with Text

Common data types for working with text

| Type | Storage Size | Description |
| ---- | ------------ | ----------- |
| `CHAR`(size) | Length of the string bytes long | A fixed length field from 0 to 255 characters long. size specifies the width of the column in characters |
| `VARCHAR`(size) | Length of the string + 1 or 2 bytes | A variable length field from 0 to 65,535 characters long |
| `TEXT` |Length of the string + 2 bytes | A string with a maximum length of 65,535 characters |
| `MEDIUMTEXT` | Length of the string + 3 bytes | A string with a maximum length of 16,777,215 characters |
| `LONGTEXT` | Length of the string + 4 bytes | A string with a maximum length of 4,294,967,295 characters |


Some common string functions

| Function | Description |
| -------- | ----------- |
| `||` | Add string together `column1 || column2` |
| `TRIM`, `LTRIM`, `RTRIM` | Remove begninning or trailing spaces, `TRIM(column) AS column1` |
| `SUBSTR` | Select a subset of characters from string `SUBSTR(column, position, numchars) AS column1` (note that that position is 1 indexed, if string finishes before numchars, all those characters are returned without any extra) |
| `UPPER`, `LOWER` | Change case of all characters of string `UPPER(column)` |

***

### Date and Time
Each DBMS can use different data types for storing date and times. Dates are usually stored as datetypes. If only date is present, things should work fine. If time is also included, extra care must be taken when working this that column.

Common date formats

| Type | Storage Size | Format |
| ---- | ------------ |------- |
| DATE | 3 bytes | `YYYY-MM-DD` |
| DATETIME | 8 bytes | `YYYY-MM-DD HH:MI:SS` |
| TIMESTAMP | 4 bytes | `YYYY-MM-DD HH:MI:SS`, with acceptable range in year 1970 to 2038 |


For instance, if we are filtering data, we need to make sure that the compared value is of the same format as the column.


Different date time functions are available

| Function |
| -------- |
| `DATE(timestring, modifier, modifier)` |
| `TIME(timestring, modifier, modifier)` |
| `DATETIME(timestring, modifier, modifier)` |
| `JULIANDAY(timestring, modifier, modifier)` |
| `STRFTIME(format, timestring, modifier, modifier)` |


`STRFTIME` can be used to extract specific information like year from the date time string.
```sql
SELECT STRFTIME('%Y', Birthdate) as year,
STRFTIME('%m', Birthdate) as month,
STRFTIME('%d', Birthdate) as date
FROM employees;
```

`DATE('now')` will return the current data and can be used with a column to calculate date difference from today. `STRFTIME('%Y-%m-%d', 'now')` can be used to select the date today in the specified format. `now` acts as a modifier here. To get the time, use `STRFTIME('%H %M %S %s', 'now')`.

***

### `CASE` Statements
Useful to create a new column with new categories/bins based on certain conditions on the existing columns. It can be used with the SELECT, INSERT, UPDATE, and DELETE statements.
```sql
CASE
WHEN condition1 THEN expression1
WHEN condition2 THEN expression2
. . .
ELSE expression_default
END
```

```sql
SELECT trackid, trackname, length --length in ms--
CASE
WHEN length < 300000 THEN 'small'
WHEN length >= 300000 AND length < 600000 THEN 'medium'
WHEN length >= 600000 THE 'large'
ELSE 'other' END tracklength
FROM tracks;
```

***

### `VIEW`
A view is removed after the database connection has ended. Views act like a stored query. We can run a complex query and store the results as a view which can be used in other dowstream queries.
```sql
CREATE VIEW view_name AS
SELECT something FROM somewhere;
```
view_name can be used as a normal table. To remove the table `DROP VIEW view_name`. Views are very useful when one may not have database write access.

### Integer Data Types


| Type | Storage Size | Description |
| ---- | ------------ | ----------- |
| `SMALLINT`(size) | 2 bytes | Range of -32,768 to 32,767 or 0 to 65,535 unsigned, size denotes the column width |
| `MEDIUMINT`(size) | 3 bytes | Range of -8,388,608 to 8,388,607 or 0 to 16,777,215 unsigned |
| `INT`(size) | 4 bytes | Range of -2,147,483,648 to 2,147,483,647 or 0 to 4,294,967,295 |
| `BIGINT`(size) | 8 bytes | Range of -9,233,372,036,854,775,808 to 9,223,372,036,854,775,807 or 0 to 18,446,744,073,709,551,615 unsigned |
| `FLOAT`(size, decimals) | 4 bytes | A small number with floating decimal point |
| `DOUBLE`(size, decimals) | 8 bytes | A large number with a floating decimal point |
| `DECIMAL`(size, decimals) | Length + 1 or 2 bytes | A `DOUBLE` stored as a string, allowing for a fixed decimal point |

### Variables in SQL
The following syntax can be used to define variables and make the script modular/dynamic for repeated use
```sql
SET @ds = '2020-01-01';
SELECT
    id,
FROM
    users
WHERE
    created_at <= '{{ds}}';
```

```sql
{% assign ds = '2020-01-01' %}
SELECT
    id,
FROM
    users
WHERE
    created_at <= '{{ds}}';
```

### Windowing Functions
Suppose we want to get the first order of a user in an orders table (an invoice can contain multiple rows where each row corresponds to a different line item in that invoice, all those lines will share the same row number)
```sql
SELECT
    user_id,
    invoice_id,
    paid_at,
    RANK() OVER (PARTITION BY user_id ORDER BY paid_at ASC) AS order_num,
    DENSE_RANK() OVER (PARTITION BY user_id ORDER BY paid_at ASC) AS dense_order_num,
    ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY paid_at ASC) AS row_num,
FROM
    dsc1069.orders;
```

`RANK` will give the same rank 1 to all the rows of the first invoice, but suppose there are N rows in the first invoice, then the ranking for the rows in next invoice will begin from N+1. Equivalently, one can say that some of the ranks in between are skipped. On the other hand, `DENSE_RANK` will give rank 1 to all the rows of the first invoice, rank 2 to the rows of the second invoice and so on. Thus, no ranks are skipped. Lastly, `ROW_NUMBER` will assign a distinct row number to each entry of the table without skipping any value. Different rows within the same invoice will have different row numbers.

We can use other functions like sum and count with the windows as follows
```sql
SUM(column_1) OVER (PARTITION BY column_2 ORDER BY column_3 ASC) as running_total;
COUNT(column_1) OVER (PARTITION BY column_2 ORDER BY column_3 ASC) as running_count;
```

To actually use the dense row number column created above, we will need to wrap that query as a subquery and proceed
```sql
SELECT
    sub_1.user_id,
    sub_1.invoice_id,
    sub_1.paid_at
FROM(
    SELECT
        user_id,
        invoice_id,
        paid_at,
        -- RANK() OVER (PARTITION BY user_id ORDER BY paid_at ASC) AS order_num,
        DENSE_RANK() OVER (PARTITION BY user_id ORDER BY paid_at ASC) AS dense_order_num,
        -- ROW_NUMBER() OVER (PARTITION BY user_id ORDER BY paid_at ASC) AS row_num,
    FROM
        dsc1069.orders;
) as sub_1
WHERE
    sub_1.dense_order_num = 1;
```

***

## Useful Links
* [SQL Puzzles](https://blog.sqlauthority.com/category/sql-puzzle/)
* [SQL Zoo](https://sqlzoo.net/)

***
