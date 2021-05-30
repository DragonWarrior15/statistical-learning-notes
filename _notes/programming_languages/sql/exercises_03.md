---
title: "Exercises 03"
---

## Course 03: course name

## Week 01: Some name

***

#### Quiz 01
1. Which of the following are true when it comes to the business value of big data? (Select all that apply.)
    1. The size of the data businesses collect is growing
    1. Businesses are increasingly making data-driven decisions
    1. Automated technologies mean that data scientists and data analysts are no longer needed

2. Spark uses... (Select all that apply.)
    1. One very large computer that is able to run computation against large databases
    1. A distributed cluster of networked computers made of a driver node and many executor nodes
    1. Your database technology (e.g., Postgres or SQL Server) to run Spark queries
    1. A distributed cluster of networked computers made of many driver nodes and many executor nodes
    1. A driver node to distribute work across a number of executor nodes

3. How does Spark execute code backed by DataFrames? (Select all that apply.)
    1. It executes code determined in advance
    1. It optimizes your query by figuring out the best "how" to execute what you want
    1. It iterates over all of the source data to exhaustively evaluate queries
    1. It separates the "logical plan" of what you want to accomplish from the "physical plan" of how to do it so it can optimize the query

4. What are the properties of Spark DataFrames? (Select all that apply.)
    1. Resilient: Fault-tolerant
    1. Distributed: Computed across multiple nodes
    1. Dataset: Collection of partitioned data
    1. Tables: Operates as any table in SQL environments

5. What is the difference between Spark and database technologies? (Select all that apply.)
    1. Spark does not interact with databases but uses its proprietary DataFrame technology instead
    1. Spark is a highly optimized compute engine and is not a database
    1. Spark in an alternative to traditional databases
    1. Spark operates for both data storage and computation
    1. Spark is a computation engine and is not for data storage

6. What is Amdahl's law of scalability? (Select all that apply.)
    1. A formula that gives the theoretical speedup as a function of the percentage of a computation that can be parallelized
    1. Amdahl's law states that the speedup of a task is a function of how much of that task can be parallelized
    1. A formula that gives the number of processors (or other unit of parallelism) needed to complete a task
    1. A formula that gives the theoretical speedup as a function of the size of a partition (or subset) of data
    1. A formula that gives the expected speed of a single processor performing a computation

7. Spark offers a unified approach to analytics. What does this include? (Select all that apply.)
    1. Spark unifies applications such as SQL queries, streaming, and machine learning
    1. Spark allows analysts, data scientists, and data engineers to all use the same core technology
    1. Spark code can be written in the following languages: SQL, Scala, Java, Python, and R
    1. Spark is able to connect to data where it lives in any number of sources, unifying the components of a data application
    1. Spark unifies databases with optimized computation allowing for faster computation against the data it stores

8. What is a Databricks notebook?
    1. A single Spark query
    1. A collaborative, interactive workspace that allows you to execute Spark queries at scale
    1. A cluster that executes Spark code
    1. A Spark instance that executes queries

9. How can you get data into Databricks? (Select all that apply.)
    1. By "mounting" data backed by cloud storage
    1. By registering the data as a table
    1. By connecting to Dropbox or Google Drive
    1. By uploading it through the user interface

10. What are the qualities of big data? (Select all that apply.)
    1. Variety: the diversity of data
    1. Valorous: the positives impact of data
    1. Velocity: the speed of data
    1. Volume: the amount of data
    1. Veracity: the reliability of data

***

#### Answers 01

| Question | Answer |
| -------- | ------ |
| 1 | i, ii |
| 2 | ii, v |
| 3 | ii, iv |
| 4 | i, ii, iii |
| 5 | ii, v |
| 6 | i, ii |
| 7 | all |
| 8 | ii |
| 9 | i, ii, iv |
| 10 | i, iii, iv, v |

***

#### Quiz 02

1. What are the different units of parallelism? (Select all that apply.)
    1. Partition
    1. Task
    1. Executor
    1. Core

2. What is a partition?
    1. A division of computation that executes a query
    1. The result of data filtered by a WHERE clause
    1. A synonym with "task"
    1. A portion of a large distributed set of data

3. What is the difference between in-memory computing and other technologies? (Select all that apply.)
    1. In-memory operations were not realistic in older technologies when memory was more expensive
    1. In-memory operates from RAM while other technologies operate from disk
    1. In-memory computing is slower than other types of computing
    1. Computation not done in-memory (such as Hadoop) reads and writes from disk in between each step

4. Why is caching important?
    1. It improves queries against data read one or more times
    1. It always stores data in-memory to improve performance
    1. It reformats data already stored in RAM for faster access
    1. It stores data on the cluster to improve query performance

5. Which of the following is a wide transformation? (Select all that apply.)
    1. `GROUP BY`
    1. `ORDER BY`
    1. `WHERE`
    1. `SELECT`

6. Broadcast joins...
    1. Shuffle both of the tables, minimizing data transfer by transferring data in parallel
    1. Transfer the smaller of two tables to the larger, increasing data transfer requirements
    1. Transfer the smaller of two tables to the larger, minimizing data transfer
    1. Shuffle both of the tables, minimizing computational resources

7. When is it appropriate to use a shuffle join?
    1. Never. Broadcast joins always out-perform shuffle joins.
    1. When the smaller table is significantly smaller than the larger table
    1. When both tables are very small
    1. When both tables are moderately sized or large

8. Which of the following are bottlenecks you can detect with the Spark UI? (Select all that apply.)
    1. Shuffle writes
    1. Shuffle reads
    1. Incompatible data formats
    1. Data Skew

9. What is a stage boundary?
    1. When all of the slots or available units of processing have to sync with one another
    1. A narrow transformation
    1. An action caused by a SQL query is predicate
    1. Any transition between Spark tasks

10. What happens when Spark code is executed in local mode?
    1. A cluster of virtual machines is used rather than physical machines
    1. The code is executed against a local cluster
    1. The executor and driver are on the same machine
    1. The code is executed in the cloud

***

#### Answers 02

| Question | Answer |
| -------- | ------ |
| 1 | i, ii, iii, iv |
| 2 | iv |
| 3 | ii, iv |
| 4 | iv |
| 5 | i, ii |
| 6 | iii |
| 7 | iv |
| 8 | i, ii, iv |
| 9 | i |
| 10 | iii |

***

#### Quiz 03

1. Decoupling storage and compute means storing data in one location and processing it using a separate resource. What are the benefits of this design principle? (Select all that apply.)
    1. It results in copies of the data in case of a data center outage
    1. Resources are isolated and therefore more manageable and debuggable
    1. It allows for elastic resources so larger storage or compute resources are used only when needed
    1. It makes updates to new software versions easier

2. You want to run a report entailing summary statistics on a large dataset sitting in a database. What is the main resource limitation of this task?
    1. CPU: computation is more demanding than the data transfer
    1. CPU: the transfer of data is more demanding than the computation
    1. IO: the transfer of data is more demanding than the computation
    1. IO: computation is more demanding that the data transfer

3. Processing virtual shopping cart orders in real time is an example of...
    1. Online Analytical Processing (OLAP)
    1. Online Transaction Processing (OLTP)

4. When are BLOB stores an appropriate place to store data? (Select all that apply.)
    1. For online transaction processing on a website
    1. For cheap storage
    1. For storing large files
    1. For a "data lake" of largely unstructured data

5. JDBC is the standard protocol for interacting with databases in the Java environment. How do parallel connections work between Spark and a database using JDBC?
    1. Specify the number of partitions using COALESCE. Spark then creates one parallel connection for each partition.
    1. Specify the number of partitions using REPARTITION. Spark then creates one parallel connection for each partition.
    1. Specify a column, number of partitions, and the column's minimum and maximum values. Spark then divides that range of values between parallel connections.
    1. Specify the numPartitions configuration setting. Spark then creates one parallel connection for each partition.

6. What are some of the advantages of the file format Parquet over CSV? (Select all that apply.)
    1. Compression
    1. Parallelism
    1. Corruptible
    1. Columnar

7. SQL is normally used to query tabular (or "structured") data. Semi-structured data like JSON is common in big data environments. Why? (Select all that apply.)
    1. It allows for data change over time
    1. It allows for easy joins between relational JSON tables
    1. It allows for complex data types
    1. It does not need a formal structure
    1. It allows for missing data

8. Data writes in Spark can happen in serial or in parallel. What controls this parallelism?
    1. The number of stages in a write operation
    1. The number of data partitions in a DataFrame
    1. The numPartitions setting in the Spark configuration
    1. The number of jobs in a write operation

9. Fill in the blanks with the appropriate response below:
   A _______ table manages _______and a DROP TABLE command will result in data loss.
    1. Managed, both the data and metadata such as the schema and data location
    1. Unmanaged, only the metadata such as the schema and data location
    1. Unmanaged, both the data and metadata such as the schema and data location
    1. Managed, only the metadata such as the schema and data location

***

#### Answers 03

| Question | Answer |
| -------- | ------ |
| 1 | ii, iii, iv |
| 2 | iii |
| 3 | ii |
| 4 | ii, iii, iv |
| 5 | iii |
| 6 | i, ii, iv |
| 7 | i, ii, v |
| 8 | ii |
| 9 | i |

***

#### Quiz 04

1. Machine learning is suited to solve which of the following tasks? (Select all that apply.)
    1. Image Recognition
    1. A/B Testing
    1. Fraud Detection
    1. Churn Analysis
    1. Natural Language Processing
    1. Reporting
    1. Financial Forecasting

2. Is a model that is 99% accurate at predicting breast cancer a good model?
    1. Likely yes because it accounts for false negatives and we'd want to make sure we catch every case of cancer
    1. Likely yes because this is generally a high score
    1. Likely no because there are too many false positives
    1. Likely no because there are not many cases of cancer in a general population

3. What is an appropriate baseline model to compare a machine learning solution to?
    1. The average of the dataset
    1. The minimum value of the dataset
    1. Zero

4. What is Machine Learning? (Select all that apply.)
    1. Statistical moments calculated against a dataset
    1. Learning patterns in your data without being explicitly programmed
    1. Hand-coded logic
    1. A function that maps features to an output

5. (Fill in the blanks with the appropriate answer below.)
    Predicting whether a website user is fraudulent or not is an example of _________ machine learning. It is a __________ task.
    1. unsupervised, classification
    1. supervised, classification
    1. supervised, regression
    1. unsupervised, regression

6. (Fill in the blanks with the appropriate answer below.)
Grouping similar users together based on past activity is an example of _________ machine learning. It is a _________ task.
    1. unsupervised, clustering
    1. unsupervised, classification
    1. supervised, clustering
    1. supervised, classification

7. Predicting the next quarter of a company's earnings is an example of...
    1. Reinforcement
    1. Clustering
    1. Classification
    1. Semi-supervised
    1. Regression

8. Why do we want to perform a train/test split before we train a machine learning model? (Select all that apply.)
    1. To calculate a baseline model
    1. To evaluate how our model performs on unseen data
    1. To give us subsets of our data so we can compare a model trained on one versus the model trained on the other
    1. To keep the model from "overfitting" where it memorizes the data it has seen

9. What is a linear regression model learning about your data?
    1. The best split points in a decision tree
    1. The average of the data
    1. The value of the closest points to the one you're trying to predict
    1. The formula for the line of best fit

10. How do you define a custom function not already part of core Spark?
    1. You can't write your own functions in Spark
    1. By extending the open source code base
    1. With a User-Defined Function

***

#### Answers 04

| Question | Answer |
| -------- | ------ |
| 1 | i, ii, iii, iv, v, vii |
| 2 | iv |
| 3 | i |
| 4 | ii, iv |
| 5 | ii |
| 6 | i |
| 7 | iv |
| 8 | ii, iv |
| 9 | iv |
| 10 | iv |

***
