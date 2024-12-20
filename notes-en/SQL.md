## SQL

```SQL
SELECTFROM
WHERE
GROUP BY (separated by spaces)
HAVING (requires an aggregate function)
ORDER BY (separated by spaces)

JOIN
ON (use "and" for multiple conditions)

IFNULL(VAR, NULL=VAR), the right side is the value if it is NULL
LENGTH() checks the length of a string
IS NULL: use IS to check for null values, not = 
CASE statement
CASE VAR/
CASE WHEN 1 THEN 2
    WHEN 3 THEN 4
    …
    ELSE 5
    END

ROUND(COUNT(r.user_id) / (SELECT COUNT(user_id) FROM Users) * 100, 2)
SUM(IF(rating < 3, 1, 0)) # if statements can also be used in SUM for conditions
DATE_ADD(event_date, INTERVAL 1 DAY)
DATE_DIFF(DAY, START_DATE, END_DATE)
COUNT(DISTINCT follower_id)
WHERE (id, name) IN (SELECT id, name FROM ..) # remember to select the primary key here
SELECT * FROM (SELECT * FROM xx) AS newtable
AVG(c.action='confirmed') # this function works like this
DATE_FORMAT(trans_date, "%Y-%m")

CTE (Common Table Expression)
    With a AS (
        SELECT
            *
        FROM
            abc
    )

    CASE
    WHEN x + y > z AND x + z > y AND y + z > x THEN 'Yes'
    ELSE 'No'
    END
    AS triangle

ROW_NUMBER() OVER(PARTITION BY occupation_v ORDER BY age DESC)

Difference between RANK() and DENSE_RANK(): when encountering the same value, DENSE_RANK
Usage: RANK() OVER(ORDER BY score DESC) as 'Rank'
Finding maximum values:
SELECT id
FROM sales
WHERE amount = (SELECT MAX(amount) FROM sales);

SELECT id
FROM sales
ORDER BY amount DESC
LIMIT 1;

SELECT s.id
FROM sales s
JOIN (
  SELECT MAX(amount) AS max_amount
  FROM sales
) AS max_sales ON s.amount = max_sales.max_amount;

Window Functions can analyze a set of data like aggregate functions and return a result. The difference is that window functions do not summarize the data into a single result, but instead return a result for each row of data.

```