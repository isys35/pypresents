class B:
    __count = 0
 
    def __init__(self):
        B.__count += 1
 
    def __del__(self):
        B.__count -= 1
 
 
a = B()
print(B.__count)
# AttributeError: type object 'B' has no 
# attribute '__count'

