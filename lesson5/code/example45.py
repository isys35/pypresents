Point = namedtuple('Point', ['x', 'y'])
p = Point(x=1, y=2)
print(p) # Point(x=1, y=2)
print(p.x) # 1
print(p[0]) # 1