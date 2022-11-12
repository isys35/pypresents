def gen():
    for i in range (10) :
        x = yield i
        print(x)
G = gen()
print(next(G))
# 0
print(G.send(77))
# 1
# 77
print(G.send(88))
# 2
# 88
print(next(G))
# 3
# None
