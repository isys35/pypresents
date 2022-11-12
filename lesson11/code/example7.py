import car
car_a = car.Car()  
print(car_a.name) #corolla
print(car_a._model) #1999
print(car_a.__make) #AttributeError: 'Car' object has no attribute '__make'