In [3]: d = {"price":pd.Series([1, 2, 3], index=['v1', 'v2', 'v3']),
   ...: "count": pd.Series([10, 12, 7], index=['v1', 'v2', 'v3'])}
In [4]: df1 = pd.DataFrame(d)

In [5]: print(df1)
   count price
v1    10     1
v2    12     2
v3     7     3

In [6]: print(df1.index)
Index(['v1', 'v2', 'v3'], dtype='object')

In [7]: print(df1.columns)
Index(['count', 'price'], dtype='object')