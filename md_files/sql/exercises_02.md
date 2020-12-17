## Course 02: course name

## Week 01: Some name

***

#### Quiz 01
1. Based on the dataset for this course, what does this query count?
    ```sql
    SELECT
        COUNT(*)
    FROM
        dsv1069.users
    JOIN
        dsv1069.orders
    ON
        users.id = orders.user_id
    ```
    1. Counts the number of users
    2. Counts the number of invoices
    3. Counts the number of users who have ordered an item
    4. Counts the number of rows in orders table

2. Assume you have no information about the data in the example table. When I run the query below,  no rows are returned, but there are no error messages. What are possible reasons for this? (Select all that apply.)
    ```sql
    SELECT *
    FROM example_table
    WHERE id IS NULL
    ```
    1. There are no rows in the example_table - it's empty
    2. There is no column called id
    3. There are no rows with a null id

3. In the events table, (dsv1069.events) for this class, how many rows exist per event_id?
    1. Always more than one
    2. Exactly one
    3. One per parameter_name

4. When you encounter a new dataset, which of the following can you assume? (Select all that apply.)
    1. The data is out-of-date
    2. The table has a primary key
    3. Test usage is unfiltered
    4. The table is empty
    5. There are duplicate rows

5. TROUBLESHOOT THIS ERROR: Based on your exploration of the tables in the course dataset. Why are the results to this specific query empty?
    ```sql
    SELECT *
    FROM
        dsv1069.users
    JOIN
        dsv1069.events
    ON
        users.parent_user_id = events.user_id
    WHERE
        event_name = 'view_item'
    AND
        merged_at is NULL
    ```
    1. The users table is empty
    2. There are no events with this event_name
    3. There are no parent_user_ids that satisfy the WHERE clause

6. TROUBLESHOOT THIS ERROR: Why are the results for this specific query empty?
    ```sql
    SELECT *
    FROM
        dsv1069.events
    WHERE
        event_name = 'item_view'
    ```
    1. There are no events with this event_name
    2. The table is empty
    3. No items have ever been viewed

7. What does this query do? Select all true statements.
    ```sql
    SELECT
        COUNT(*)
    FROM
        dsv1069.events
    WHERE
        event_name = 'view_item'
    ```
    1. The query counts the number of rows in the events table.
    2. The query counts the number of rows corresponding to view_item events.
    3. The query returns all of the rows in the events table.
    4. The query counts the number of view_item events.
    5. The query counts the number of events.

8. Consider the following query: What happens when some rows have a NULL value in the column table_alpha.key?
    ```sql
    SELECT *
    FROM table_alpha
    JOIN table_beta
    ON table_alpha.key = table_beta.column
    ```
    1. Those values aren't included in the result.
    2. Each row with a null value will be joined to every row in table_beta.
    3. Each row with a null value is joined to every row in table_beta where table_beta.column is null.
    4. It is not possible for a join key to be null, the query will return an error.

9. Which of the following are problems with the query below?
    ```sql
    SELECT
        COUNT(*)
    FROM
        dsv1069.users
    JOIN
        dsv1069.orders
    ON
        users.parent_user_id = orders.user_id
    ```
    1. Count(\*) counts rows not unique users
    2. We need a GROUP BY clause
    3. We are missing a comma
    4. The join should be on users.parent_user_id
    5. There are no error messages, so it must be right
    6. The join should be on users.user_id


10. In the users table, the column parent_user_id is ?.
    1. Sometimes NULL
    2. Never NULL
    3. Always NULL

***

#### Answers 01
| Question | Answer |
| -------- | ------ |
| 1 | iv |
| 2 | i, iii |
| 3 | iii |
| 4 |  |
| 5 | iii |
| 6 | i |
| 7 | ii |
| 8 | iii |
| 9 | i |
| 10 | i |

***

#### Quiz 02
1. Which of the following is easier to read?
    1. 
        ```sql
        SELECT
            column_1,
            column_2,
            count(*)
        FROM
            example_table
        WHERE
            column_3 is not null
        GROUP BY
            column_1,
            column_2
        ```
    2.
        ```sql
        select column_1, column_2, count(*) from example_table where 
        column_3 is not null group by column_1, column_2
        ```

2. Suppose in a table you find a column called username, which contains the value kat123. What is the correct data type category for this column?
... username    ...
... kat123  ...
... ... ...
    1. Date
    2. String
    3. Number

3. Suppose in a table you find a column called price, which contains the value $9.99. What is the best data type category for this column?
... price   ...
... 9.99    ...
... ... ...
    1. String
    2. Number
    3. Date

4. Suppose in a table you find a column called created_at, which contains the value 2019-01-01. What is the best data type category for this column?
... created_at  ...
... 2019-01-01  ...
... ... ...
    1. Date
    2. Number
    3. String

5. Suppose in a table you find a column called price, which contains the value $9.99. Of the following options, which is the best data type for this column?
... price   ...
... 9.99    ...
... ... ...
    1. `FLOAT`
    2. `BIGINT`
    3. `INT`

***

#### Answers 02
| Question | Answer |
| -------- | ------ |
| 1 | i |
| 2 | ii |
| 3 | ii |
| 4 | i |
| 5 | i |

***

#### Questions 03
1. ETL stands for:
    1. Extract Transform Language
    2. Extract Transform Load
    3. Extraction Transform Load
    4. Extraction Transaction Load
    5. Extract Transaction Language

2. If I say that table X is dependent on table Y which table should be generated (or refreshed) first?
    1. Table Y
    2. Table X

3. Based on the material covered in this lesson What is a Dependency? which of the following statements is true?
    1. The events table depends on the view_items table
    2. The users table depends on the events table
    3. The view_items table depends on the events table
    4. The view_items table depends on the items table

4. Based on the code snippet below, which statements are definitely true:
    ```sql
    CREATE TABLE table_x AS
    SELECT
        date,
        COUNT(*)
    FROM
         table_y
    GROUP BY
        date
    ```
    1. Table_y has no dependenies
    2. Table_x is dependent on table_y
    3. Table_y is dependent on table_x

***

#### Answers 03
| Question | Answer |
| -------- | ------ |
| 1 | ii |
| 2 | i |
| 3 | iii |
| 4 | ii |

***

#### Quiz 04

1. Which step should happen first in data analysis?
    1. Machine Learning
    2. Cleaning and Labeling Data
    3. Collecting Data

2. TROUBLESHOOT THIS ERROR by selecting appropriate actions to remedy this specific query: Kat ran 9 lines of MySQL (finished in 112ms):
    ```sql
    CREATE TABLE
    example_table
    (
    column1  DATE,
    column2  VARCHAR(30),
    column3  INT
    );

    ERROR 1050 (42S01) at line 1: Table 'example_table' already exists
    ```
    1. There is no error here
    2. Run DESCRIBE TABLE example_table to see if the existing example_table is structured appropriately
    3. Check the syntax, near line 6
    4. Check that the data type for column2 should actually be VARCHAR(30)

3. Based on the code snippet below, which statements are definitely true (select all that apply):
    ```sql
    CREATE TABLE table_x AS
    SELECT
     dates_rollup.date,
     COUNT(*)
    FROM
     Dates_rolluop
    JOIN
     Table_y
    ON
    dates_rollup.date = table_y.date
    GROUP BY
     date
    ```
    1. table_y has no dependencies
    2.  table_y is dependent on table_x
    3. table_x is dependent on table_y and dates_rollup
    4. table_x is dependent on table_y

4. Based on what you know about the orders table for this class, which of the following columns have a suitable datatype?

  **Please note, due to the limitations of the free version of Mode Analytics, you are not able to replicate this data without an Enterprise account.**
    1. Invoice_id
    2. Paid_at
    3. item_name
    4. user_id
    5. Created_at

5. For this class, we are using Mode on a dataset specifically created for this course. Which of these circumstances could be different in a real world situation? (Select all that apply.)
    1. The categories of data types (Number, Date, String)
    2. The specific dialect of SQL
    3. How frequently the data is updated

6. Based on what you know about the items table for this class, which of the following columns have a suitable datatype? (Select all that apply.)
undefined
  **Please note, due to the limitations of the free version of Mode Analytics, you are not able to replicate this data without an Enterprise account.**
    1. created_at
    2. name
    3. category
7. Which of the following table methods allows you to specify data types?
    1.
        ```sql
        MAKE NEW TABLE
        example_table
        AS …
        ```
    2. 
        ```sql
        SELECT *
        FROM
        example_table
        AS … 
        ```
    3.
        ```sql
        CREATE TABLE
        example_table
        AS …
        ```
    4.
        ```sql
        CREATE TABLE    
         example_table
        (column_name1 ….)
        ```

8. When creating a user info table we used a variable in place of which column?
    1. The date
    2. The order id
    3. The user

9. Suppose in a table, you find a column called email which contains the value user@domain.com. What is the correct data type category for this column?
... email   ...
... user@domain.com ...
... ... ...
    1. Number
    2. Date
    3. String

10. In this module, we created a table specifically of item view events. What level of the hierarchy of data does this belong on?
    1. Explore and Transform
    2. Collecting Data
    3. Learn and Optimize

11. Suppose in a table you find a column called event_id, which contains the value z87df6ab4waoa756b3. What is the correct data type category for this column?
... event_id    ...
... z87df6ab4waoa756b3  ...
... ... ...
    1. Number
    2.  Date
    3. String

***

#### Answers 04
| Question | Answer |
| -------- | ------ |
| 1 | iii |
| 2 | ii |
| 3 | iii, iv |
| 4 | i, iii, iv |
| 5 | ii, iii |
| 6 | ii, iii |
| 7 | iv |
| 8 | i |
| 9 | iv |
| 10 | i |
| 11 | iii |

***

#### Quiz 05
1. Which of the following attributes distinguish a work-in-progress from a “polished” final query? (Select all that apply.)
    1. Every column has a descriptive name
    2. Every join is an inner join
    3. Every column is listed in a GROUP BY clause
    4. The query is formatted consistently, or according to a style guide

2. In which of the following sections did we perform analysis to directly guide decision making?
    1. Creating a view items table
    2. Pulling email addresses and item_ids for a promo email
    3. Answering a question about reordering items

3. Which of the following are uses of a dates rollup table?
    1. Efficiently computing aggregates over a rolling time period
    2. For keeping track of your meeting schedule
    3. Creating dashboards with a complete set of dates

4. We’ve decided to only use the items and users tables to answer the following questions:
   How many items have been purchased?
   How many items do we have?
   Which join type and order will allow us to correctly compute the columns Item_count, items_ever_purchased_count?
    1. 
        ```sql
        SELECT *
        FROM
            dsv1069.orders
        LEFT JOIN
            dsv1069.items
        ON
            items.id = orders.item;
        ```
    2. 
        ```sql
        SELECT *
        FROM
            dsv1069.users
        JOIN
            dsv1069.orders
        ON
            items.id = orders.item
        ```
    3.
        ```sql
        SELECT   *
        FROM  
            dsv1069.items
        LEFT OUTER JOIN
            dsv1069.orders
        ON
            items.id = orders.item
        ```

5. For this statement, fill in the __ with the appropriate inequality (<, <=, =, >=, >):
   For days in any given week
   Daily unique visitors _ Weekly Unique visitors
    1. <=
    2. <
    3. =
    4. \>
    5. \>=

6. Select the best definition of a windowing function?
    1. It allows you to make your own windows of data.
    2. It allows you to compute aggregations with a rolling date period.
    3. It is a function that computes a value on a certain partition, or window, of the data that is specified in the `PARTITION BY` statement.

7. Folks at the company wonder if our product catalog is too small. What are some related questions that you could directly answer with our dataset? (Select all that apply.)
    1. How many products do our competitors carry?
    2. How many items have been viewed?
    3. How many items have been viewed but not ordered?
    4. How many items have been purchased?
    5. What work would need to be done to remove products from the catalog?
    6. How many items do we have?
    7. How many users have purchased an item?

8. Which of the following tasks can be accomplished with a windowing function? (Select all that apply.)
    1. Find the price of each item
    2. Find the email address of each user
    3. Find the most expensive item per order
    4. Find the most recently viewed item

9.  Let’s suppose we want to write a query to answer both of these questions:
    How many users have made a purchase?
    How many users do we have?
    Please choose the best set of columns for a final query that would answer these questions:
    1. Item_count
       user_count
       order count
    2. User_count
       view_count
       order_count
    3. user_count
       users_with_purchases
    4. Category
       item_count

10. According to the methodology suggested in this module, which step comes last?
    1. Present the data in the appropriate context
    2. Format your query according to the style guide
    3. Understand the decisions that are at stake

***

#### Answers 05
| Question | Answer |
| -------- | ------ |
| 1 | i, iv |
| 2 | iii |
| 3 | i, iii |
| 4 | iii |
| 5 | i |
| 6 | iii |
| 7 | ii, iii, iv, vi |
| 8 | iii, iv |
| 9 | iii |
| 10 | i |

***

#### Quiz 06
1. Which of the following are the purpose of AB testing? (Select all that apply).
    1. Clean and label data
    2. Provide evidence for or disprove a hypothesis
    3. Learn from data

2. Which of the following are necessary components of a user-level test assignment table? (Select all that apply).
    1. The user's email address
    2. The assignment (treatment or control?)
    3. The user_id
    4. The date or time of assignment
    5. A test name or number

3. Which of the following are necessary components of an item-level test assignment table? (Select all that apply).
    1. The item id
    2. The assignment (treatment or control?)
    3. The date or time of assignment
    4. A test name or number
    5. The user_id
    6. The item category

4. In the final project we’ll be doing AB testing at an item level. Check out the table final_assignment_qa. What other pieces of data will you need to compute the 30-day order binary. (Select all that apply).
  Please note: 30-day order binary means show a 1 if the item was ordered at any point the 30 day period after treatment, and 0 if the item was never ordered.
    1. I'm still missing something
    2. The item category
    3. The users table
    4. The user_id
    5. The orders table

5. Use this [AB testing calculator](!https://thumbtack.github.io/abba/demo/abba.html). Enter the numbers seen in the table, and use the results to determine if the results are statistically significant.
undefined
    | Label | Number of Successes | Number of Trials |
    | ----- | ------------------- | ---------------- |
    | Control | 100 | 1000 |
    | Treatment | 101 | 1000 |
    Interval Confidence Interval : 0.95
  Are the results statistically significant?
    1. No
    2. Yes

6. For the previous data and AB test, what are the correct interpretations ?
    1. We have not collected enough samples to be able to detect statistically significant lift of 1%
    2. The treatment caused a 1% lift in the success metric
    3. There is no detectable change in this metric
    4. The treatment caused a lift of as much as 27% in the success metric

7. Use this [AB testing calculator](!https://thumbtack.github.io/abba/demo/abba.html). Enter the numbers seen in the table. In this calculation, what is the observed success rate in control?
    | Label | Number of Successes | Number of Trials |
    | ----- | ------------------- | ---------------- |
    | Control | 216 | 2549 |
    | Treatment | 324 | 2371 |
    Interval Confidence Interval : 0.95
    1. 12% to 15%
    2. 8.5%
    3. 40% to 81%
    4. 61%
    5. 14%
    6. 7.5% to 9.6%

8. For the previous data and AB test, what is the observed success rate in treatment?
    1. 61%
    2. 14%
    3. 8.5%
    4. 40% to 81%
    5. 12% to 15%
    6. 7.5% to 9.6%

9. For the previous data and AB test, what is the observed relative lift in success rate between control and treatment?
    1. 12% to 15%
    2. 14%
    3. 8.5%
    4. 61%
    5. 7.5% to 9.6%
    6. 40% to 81%

10. For the previous data and AB test, what is the range of improvement that is likely to have been caused by the treatment?
    1. 7.5% to 9.6%
    2. 61%
    3. 12% to 15%
    4. 40% to 81%
    5. 14%
    6. 8.5%

11. Which of the following queries would meet the coding standards for the final project?
    1.
        ```sql
        SELECT
            COUNT(*) AS user_count
        FROM dsv1069.users
        ```
    2.
        ```sql
        SELECT
            COUNT(*)
        FROM dsv1069.users
        ```

***

#### Answers 05
| Question | Answer |
| -------- | ------ |
| 1 | ii, iii |
| 2 | ii, iii, iv, v |
| 3 | i, ii, iii, iv |
| 4 | i, v |
| 5 | i |
| 6 | i, iv |
| 7 | ii |
| 8 | ii |
| 9 | iv |
| 10 | iv |
| 10 | i |

***