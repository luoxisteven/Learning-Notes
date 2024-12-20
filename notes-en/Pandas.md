# Pandas
Pandas is a package of `Python`.

```python
pd.merge(customers, orders, left_on="id", right_on="customerId", how="left")
DataFrame.join(other, on=None, how='left', lsuffix='', rsuffix='', sort=False, validate=None)
# Inplace
DataFrame.drop_duplicates(subset=['author_id'], inplace=False) 
DataFrame.rename(columns={"name":"Customers"})
DataFrame.sort_values(by="id",ascending=True)
DataFrame["customerId"].isnull()
```