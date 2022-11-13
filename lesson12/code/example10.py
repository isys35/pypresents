class DoubleList:
    def __init__(self, l):
        self.double = DoubleList.__make_double(l)
 
    def __make_double(old):
        new = []
        for i in old:
            new.append(i)
            new.append(i)
        return new
 
 
nums = DoubleList([1, 6, 12])
print(nums.double)
print(DoubleList.__make_double([1, 2]))
# [1, 1, 6, 6, 12, 12]
# Traceback (most recent call last):
#   ...
#     print(DoubleList.__make_double([1, 2]))
# AttributeError: type object 'DoubleList' 
# has no attribute '__make_double'