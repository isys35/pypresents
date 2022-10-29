def foo(param=None):
    """
    :type param: list
    """
    param = [] if param is None else param
    param.append(1)
    print(param)

>>> foo()
[1]
>>> foo()
[1]