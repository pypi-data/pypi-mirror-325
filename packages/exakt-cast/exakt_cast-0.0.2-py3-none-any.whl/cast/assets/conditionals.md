In DuckDB, the `IF` statement is used to evaluate a condition and return one value if the condition is true, and another value if the condition is false. This is similar to the `IF` function in many other databases or programming languages.

### Syntax:

```sql
IF(condition, true_value, false_value)
```

- **`condition`**: The condition that is evaluated. If this is true, the `true_value` is returned. If it is false, the `false_value` is returned.
- **`true_value`**: The value returned when the condition is true.
- **`false_value`**: The value returned when the condition is false.

### Example 1: Basic `IF` Usage

Suppose you have a `sales` table with columns `amount` and `category`, and you want to label sales amounts as "High" if they are above 1000 and "Low" otherwise.

```sql
SELECT 
    amount, 
    IF(amount > 1000, 'High', 'Low') AS sale_category
FROM sales;
```

In this query:
- If `amount > 1000`, the result will be `'High'`.
- Otherwise, the result will be `'Low'`.

### Example 2: Using `IF` to Handle NULL Values

The `IF` statement can also be used to handle `NULL` values. For instance, if you have a `customers` table with a `city` column, and you want to replace any `NULL` values with `'Unknown'`, you can do:

```sql
SELECT 
    customer_id, 
    IF(city IS NULL, 'Unknown', city) AS customer_city
FROM customers;
```

Here:
- If `city` is `NULL`, `'Unknown'` will be returned.
- If `city` is not `NULL`, the actual city value will be returned.

### Example 3: Conditional Calculation

You can also use the `IF` statement to perform calculations based on conditions. For instance, if you want to apply a 10% discount for amounts greater than 500 in a `transactions` table:

```sql
SELECT 
    transaction_id, 
    amount, 
    IF(amount > 500, amount * 0.90, amount) AS discounted_amount
FROM transactions;
```

Here:
- If `amount > 500`, it applies a 10% discount.
- Otherwise, the original `amount` is returned.

### Summary:
- The `IF` statement in DuckDB allows conditional logic within a query, returning different values based on a condition.
- It works similarly to an `if-else` statement, and can be used for categorizing data, handling `NULL` values, and performing conditional calculations.

