def func1():
    a = 1
    b = 'line'
    c = [1, 2, 3]

    def func2():
        c.append(4)
        a = a + 1
        return a, b, c

    return func2


call_func = func1()
call_func()
# (2, 'line', [1, 2, 3, 4])