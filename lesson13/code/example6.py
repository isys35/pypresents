class Base:
    def price(self):
        return 10

class Discount(Base):
    def price(self):
        return 8