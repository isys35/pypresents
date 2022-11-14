class A: 
    def myname(self): 
        print("I am a class A") 
 
class B(A): 
    def myname(self): 
        print("I am a class B") 
 
class C(A): 
    def myname(self): 
        print("I am a class C")  
c = C() 
print(c.myname()) 
#  I am a class C 