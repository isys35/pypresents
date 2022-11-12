>>> f = open('script2.ру') 
>>> f.__next__() 
# 'import sys\n'
>>> f.__next__() 
# 'print(sys.path)\n'

>>> f = open('script2.ру') 
>>> next(f) 
# 'import sys\n'
>>> next(f) 
# 'print(sys.path)\n'

