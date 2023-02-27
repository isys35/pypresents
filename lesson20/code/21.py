def test():
    while True:
        value = yield
        print(value)
try:
    cor = test()
    next(cor)
    cor.close()
    cor.send("So Good")
except StopIteration:
    print("Done with the basics")