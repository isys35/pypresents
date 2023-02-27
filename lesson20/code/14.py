def bare_bones():
    print("My first Coroutine!")
    while True:
        value = yield
        print(value)