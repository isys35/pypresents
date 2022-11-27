class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def __repr__(self):
        return f"Person(name={self.name!r}, age={self.age!r}"
     
    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return (self.name, self.age) == (other.name, other.age)
        return NotImplemented