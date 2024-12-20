## SQL

```SQL
SELECTFROM
WHERE
GROUP BY (用空格隔开)
HAVING （这里需要聚合函数）
ORDER BY (用空格隔开)

JOIN
ON （多个用”and”)

IFNULL(VAR,NULL=VAR) , 右边是如果是NULL的值
LENGTH() 检查字符串长度
IS NULL 空要用IS来判断，而不是用=判断
CASE 判断
CASE VAR/
CASE WHEN 1 THEN 2
	WHEN 3 THEN 4
	…
	ELSE 5
	END

ROUND(COUNT(r.user_id)/ (SELECT COUNT(user_id) FROM Users) * 100, 2)
SUM(IF(rating < 3, 1, 0)) # if式子可以再SUM这种进行判断
DATE_ADD(event_date, INTERVAL 1 DAY)
DATE_DIFF(DAY,START_DATE, END_DATE)
COUNT(DISTINCT follower_id)
WHERE (id, name) IN (SELECT id, name FROM ..) # 在这里记得要选择主键
SELECT *  FROM (SELECT * FROM xx) AS newtable
AVG(c.action='confirmed') # 这个函数这样子就可以了
DATE_FORMAT(trans_date,"%Y-%m")

CTE 公共表表达式
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

RANK()和DENSE_RANK()的区别：在遇到相同数值时，DENSE_RANK 
使用方法：RANK() OVER(ORDER BY score DESC) as 'Rank'
三个找最大值
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

窗口函数（Window Function）可以像聚合函数一样对一组数据进行分析并返回结果，二者的不同之处在于，窗口函数不是将一组数据汇总成单个结果，而是为每一行数据都返回一个结果。
```