a = (1, [2, 3], 4)
print(type(a))   # <type 'tuple'>
b = {a: 1}       # TypeError: unhashable type: 'list'