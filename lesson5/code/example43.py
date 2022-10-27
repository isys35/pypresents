import collections
c = collections.Counter()
for word in ['spam', 'egg', 'spam', 'counter', 'counter', 'counter']:
    c[word] += 1

print(c) # Counter({'counter': 3, 'spam': 2, 'egg': 1})
print(c['counter']) # 3
print(c['collections']) #0