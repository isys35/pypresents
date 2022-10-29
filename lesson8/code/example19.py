def foo(param=[]):
    print(id(param))

>>> foo()
4494207600
>>> id(foo.func_defaults[0])
4494207600