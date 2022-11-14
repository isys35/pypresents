class A:
    def __init__(self):
        self.x = 10

class B(A):
    def __init__(self):
        self.y = self.x + 5

# print(B().y)  # ошибка! AttributeError: 'B' object has no attribute 'x'

# правильно:

class B(A):
    def __init__(self):
        super().__init__()  # <- не забудь!
        self.y = self.x + 5

print(B().y)  # 15