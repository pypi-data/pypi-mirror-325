In SQL, comparisons are used to filter and manipulate data based on specific conditions. They allow you to compare values in different rows or columns and return results based on whether those comparisons evaluate as `TRUE`, `FALSE`, or `NULL`.

### Common Comparison Operators

| Operator | Description                                      | Example                                 | Result                                  |
|----------|--------------------------------------------------|-----------------------------------------|-----------------------------------------|
| `=`      | Equal to                                         | `age = 30`                              | Returns rows where `age` is 30          |
| `<>`     | Not equal to (also `!=` in some databases)       | `salary <> 50000`                       | Returns rows where `salary` is not 50000|
| `<`      | Less than                                        | `price < 100`                           | Returns rows where `price` is less than 100 |
| `<=`     | Less than or equal to                            | `age <= 25`                             | Returns rows where `age` is 25 or less  |
| `>`      | Greater than                                     | `experience > 5`                        | Returns rows where `experience` is greater than 5 |
| `>=`     | Greater than or equal to                         | `quantity >= 10`                        | Returns rows where `quantity` is 10 or more |
| `BETWEEN`| Within a range (inclusive)                       | `age BETWEEN 18 AND 30`                 | Returns rows where `age` is between 18 and 30 (inclusive) |
| `LIKE`   | Pattern matching (with `%` and `_` wildcards)    | `name LIKE 'A%'`                        | Returns rows where `name` starts with 'A' |
| `IN`     | Matches any value in a list                      | `country IN ('USA', 'Canada', 'UK')`    | Returns rows where `country` is 'USA', 'Canada', or 'UK' |
| `IS NULL`| Checks for `NULL` values                         | `address IS NULL`                       | Returns rows where `address` is `NULL`  |

### 1. **Equal to (`=`)**

The `=` operator checks if two values are equal. This is the most basic form of comparison.

```sql
SELECT * 
FROM employees
WHERE department = 'HR';
```
- This query returns all employees whose department is `HR`.

### 2. **Not equal to (`<>` or `!=`)**

The `<>` operator checks if two values are *not* equal.

```sql
SELECT * 
FROM employees
WHERE salary <> 50000;
```
- This returns all employees whose salary is not equal to 50,000.

### 3. **Less than (`<`) and Greater than (`>`)**

These operators check if a value is smaller or greater than another value.

```sql
SELECT * 
FROM products
WHERE price < 100;
```
- This returns all products where the price is less than 100.

```sql
SELECT * 
FROM products
WHERE quantity > 50;
```
- This returns products with more than 50 items in stock.

### 4. **Less than or equal to (`<=`) and Greater than or equal to (`>=`)**

These operators extend the less than and greater than operators to include equality.

```sql
SELECT * 
FROM orders
WHERE total_amount >= 500;
```
- This returns orders where the total amount is 500 or more.

```sql
SELECT * 
FROM students
WHERE age <= 21;
```
- This returns students who are 21 years old or younger.

### 5. **BETWEEN**

The `BETWEEN` operator checks if a value lies within a specified range. It is inclusive of the boundary values.

```sql
SELECT * 
FROM employees
WHERE age BETWEEN 25 AND 35;
```
- This returns employees whose age is between 25 and 35, inclusive.

### 6. **LIKE**

The `LIKE` operator is used for pattern matching in string values. It works with two wildcards:
- `%` matches any sequence of characters (zero or more).
- `_` matches exactly one character.

```sql
SELECT * 
FROM customers
WHERE name LIKE 'J%';
```
- This returns customers whose name starts with the letter 'J'.

```sql
SELECT * 
FROM customers
WHERE name LIKE '_a%';
```
- This returns customers whose second letter is 'a'.

### 7. **IN**

The `IN` operator checks if a value exists in a list of specified values, making it useful for comparing against multiple values.

```sql
SELECT * 
FROM employees
WHERE department IN ('Sales', 'HR', 'Marketing');
```
- This returns employees in the `Sales`, `HR`, or `Marketing` departments.

### 8. **IS NULL**

The `IS NULL` operator checks whether a value is `NULL`. Since `NULL` is not equivalent to any other value (including itself), using `=` won't work with `NULL`.

```sql
SELECT * 
FROM customers
WHERE address IS NULL;
```
- This returns all customers where the `address` column has a `NULL` value.

### Combining Comparison Operators

You can combine multiple comparisons using logical operators like `AND` and `OR` to create complex conditions.

```sql
SELECT * 
FROM employees
WHERE salary > 50000 AND department = 'Sales';
```
- This returns employees who are in the Sales department and have a salary greater than 50,000.

```sql
SELECT * 
FROM employees
WHERE department = 'HR' OR age < 30;
```
- This returns employees who are either in the HR department or are younger than 30.

### Summary:
- Comparison operators allow filtering data based on conditions, such as checking for equality, inequality, ranges, or patterns.
- They are essential for retrieving specific subsets of data from SQL queries.
- `IN`, `BETWEEN`, `LIKE`, and `IS NULL` offer more specialized comparisons.
