d = {"price":[1, 2, 3], "count": [10, 20, 30]}
df = pd.DataFrame(d, index=['a', 'b', 'c'])
print(df)
print(df['count'])
print(df.loc['a'])
print(df.iloc[1])
print(df[0:2])
print(df[df['count'] >= 20])