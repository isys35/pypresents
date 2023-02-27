def bare_bones():
    print("My first Coroutine!")
    while True:
        value = yield
        print(value)

coroutine = bare_bones()
next(coroutine)