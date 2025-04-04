Joins in DuckDB (and SQL in general) are used to combine rows from two or more tables based on a related column between them. DuckDB supports several types of joins that allow you to retrieve and manipulate data from multiple tables effectively.

### Types of Joins in DuckDB

1. **INNER JOIN**
2. **LEFT JOIN (or LEFT OUTER JOIN)**
3. **RIGHT JOIN (or RIGHT OUTER JOIN)**
4. **FULL JOIN (or FULL OUTER JOIN)**
5. **CROSS JOIN**

### 1. **INNER JOIN** 

An `INNER JOIN` returns only the rows where there is a match between both tables. If no match is found, the rows are excluded from the result.

**Syntax:**

```sql
SELECT *
FROM table1
INNER JOIN table2
ON table1.column = table2.column;
```

**Example:**
```sql
SELECT *
FROM orders
INNER JOIN customers
ON orders.customer_id = customers.customer_id;
```
- This returns only the orders that have matching customers.

### 2. **LEFT JOIN (LEFT OUTER JOIN)**

A `LEFT JOIN` returns all the rows from the left table, along with the matching rows from the right table. If there’s no match, `NULL` is returned for columns from the right table.

**Syntax:**

```sql
SELECT *
FROM table1
LEFT JOIN table2
ON table1.column = table2.column;
```

**Example:**
```sql
SELECT *
FROM orders
LEFT JOIN customers
ON orders.customer_id = customers.customer_id;
```
- This returns all orders, including those without a matching customer. For orders without a customer, `NULL` is returned in the customer columns.

### 3. **RIGHT JOIN (RIGHT OUTER JOIN)**

A `RIGHT JOIN` is the opposite of a `LEFT JOIN`. It returns all the rows from the right table, along with the matching rows from the left table. If no match is found, `NULL` is returned for columns from the left table.

**Syntax:**

```sql
SELECT *
FROM table1
RIGHT JOIN table2
ON table1.column = table2.column;
```

**Example:**
```sql
SELECT *
FROM orders
RIGHT JOIN customers
ON orders.customer_id = customers.customer_id;
```
- This returns all customers, including those without any matching orders. If a customer doesn’t have an order, the order columns will be `NULL`.

### 4. **FULL JOIN (FULL OUTER JOIN)**

A `FULL JOIN` returns all rows when there is a match in either table. If there’s no match, `NULL` is returned for the missing side. This is a combination of `LEFT JOIN` and `RIGHT JOIN`.

**Syntax:**

```sql
SELECT *
FROM table1
FULL JOIN table2
ON table1.column = table2.column;
```

**Example:**
```sql
SELECT *
FROM orders
FULL JOIN customers
ON orders.customer_id = customers.customer_id;
```
- This returns all orders and customers. If an order doesn't have a customer or if a customer doesn't have an order, `NULL` is returned for the missing columns.

### 5. **CROSS JOIN**

A `CROSS JOIN` returns the Cartesian product of the two tables, meaning every row from the first table is paired with every row from the second table. This join doesn’t require any `ON` condition.

**Syntax:**

```sql
SELECT *
FROM table1
CROSS JOIN table2;
```

**Example:**
```sql
SELECT *
FROM products
CROSS JOIN categories;
```
- This returns every possible combination of a product and category.

### Example Scenario

Let's say you have two tables: `students` and `courses`.

#### Students Table:
| student_id | student_name |
|------------|--------------|
| 1          | Alice        |
| 2          | Bob          |
| 3          | Charlie      |

#### Courses Table:
| course_id | student_id | course_name  |
|-----------|------------|--------------|
| 1         | 1          | Math         |
| 2         | 1          | Science      |
| 3         | 2          | History      |

#### **INNER JOIN** Example:

```sql
SELECT student_name, course_name
FROM students
INNER JOIN courses
ON students.student_id = courses.student_id;
```

**Result:**
| student_name | course_name |
|--------------|-------------|
| Alice        | Math        |
| Alice        | Science     |
| Bob          | History     |

#### **LEFT JOIN** Example:

```sql
SELECT student_name, course_name
FROM students
LEFT JOIN courses
ON students.student_id = courses.student_id;
```

**Result:**
| student_name | course_name |
|--------------|-------------|
| Alice        | Math        |
| Alice        | Science     |
| Bob          | History     |
| Charlie      | NULL        |

In the `LEFT JOIN` example, Charlie has no matching course, so `NULL` is returned for `course_name`.

### Summary of Joins:
- **INNER JOIN**: Returns rows where there is a match in both tables.
- **LEFT JOIN**: Returns all rows from the left table, with `NULL` for unmatched rows from the right table.
- **RIGHT JOIN**: Returns all rows from the right table, with `NULL` for unmatched rows from the left table.
- **FULL JOIN**: Returns all rows from both tables, with `NULL` for unmatched rows from either table.
- **CROSS JOIN**: Returns the Cartesian product of both tables (all combinations).