class Table:
    def __init__(self, l, w, h):
        self.length = l
        self.width = w
        self.height = h
 
 
class DeskTable(Table):
    def square(self):
        return self.width * self.length
 
 
class ComputerTable(DeskTable):
    def square(self, monitor=0.0):
        return self.width * self.length - monitor
 
 
t3 = ComputerTable(0.8, 0.6, 0.7)
print(t3.square(0.3))  # вывод: 0.18