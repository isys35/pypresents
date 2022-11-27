from dataclasses import dataclass
 
@dataclass
class Person:
    name: str
    age: int
 
tom = Person("Tom", 38)
print(f"Name: {tom.name}  Age: {tom.age}")      # Name: Tom  Age: 38