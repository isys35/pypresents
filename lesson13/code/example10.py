class A:
    def __init__(self, x):
        self.x = x

    
class B(A):
    def __init__(self, x):
        super(B, self).__init__(x)
        # теперь это тоже самое: super().__init__(x)