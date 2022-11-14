class A: 
 def myname(self): 
    print(" I am a class A") 
class B(A): 
 def myname(self): 
    print(" I am a class B") 
class C(A): 
 def myname(self): 
    print("I am a class C") 
 
# classes ordering 
class D(B, C): 
 pass 
 
 
# it prints the lookup order 
print(D.__mro__) 
print(C.mro()) 
# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>) 
# [<class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
