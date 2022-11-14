# A program to read the value from private method 
class Javatpoint: 
   def __init__(self, year=27): 
      self._year = year 
 
   @property 
   def property_year(self): 
      return self.__year 
 
   @property_year.setter 
   def setter_year(self, x): 
      self.__year = x 
 
grad_obj = Javatpoint() 
print(grad_obj._year) 
 
grad_obj.year = 2020 
print(grad_obj.year) 

# 27
# 2020