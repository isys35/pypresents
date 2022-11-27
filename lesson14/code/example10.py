class SuperVIPDiscount(VIPDiscount):
    def get_discount(self):
        return super().get_discount() * 2