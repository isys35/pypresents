class Car:  
    def __init__(self):
        print ("Двигатель заведен")
        self.name = "corolla"
        self.__make = "toyota"
        self._model = 1999