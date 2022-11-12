
>>> f.__next__() 
# 'x = 2\n'
>>> f.__next__()
# 'print(x ** 32)\n'
>>> f.__next__()
# Traceback (most recent call last):
# File "<stdin>", line 1, in <module>
# Stopiteration
