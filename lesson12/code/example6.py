class B:
    count = 0
 
    def __init__(self):
        B.count += 1
 
    def __del__(self):
        B.count -= 1
 
 
a = B()
b = B()
print(B.count)  # выведет 2
 
del a
print(B.count)  # выведет 1