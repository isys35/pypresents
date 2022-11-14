class Base:
    def price(self):
        return 10

class InterFoo(Base):
    def price(self):
        return Base.price(self) * 1.1

class Discount(InterFoo):  # <-- 
    def price(self):
        return InterFoo.price(self) * 0.8  # <-- 