class Javatpoint:  
     def __init__(self):  
          self._age = 0 
       # using the get function  
     def get_age(self):  
         print("getter method")  
         return self._age  
       # using the set function  
     def set_age(self, y):  
         print("setter method")  
         self._age = y  
  # using the del function  
     def del_age(self):  
         del self._age  
     age = property(get_age, set_age, del_age)   
   
John = Javatpoint()  
   
John.age = 18 
   
print(John.age)  

# setter method 
# getter method 
# 18 