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
d = D() 
d.myname() 
# I am a class B 