>>> def make_class(class_name):
...     class C:
...         def print_class_name(self):
...             print(class_name)
...     return C
...
>>> C1, C2 = map(make_class, ["C1", "C2"])
>>> c1, c2 = C1(), C2()
>>> c1.print_class_name()
C1
>>> c2.print_class_name()
C2
>>> type(c1)
<class '__main__.make_class.<locals>.C'>
>>> type(c2)
<class '__main__.make_class.<locals>.C'>
>>> c1.print_class_name.__closure__
(<cell at 0x7fae89666558: str object at 0x7fae87e0d340>,)