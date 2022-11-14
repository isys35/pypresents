>>> class C:
...     def __init__(self, s):
...         print(s)
...
>>> MyClass = C
>>> type(C)
<class 'type'>
>>> type(MyClass)
<class 'type'>
>>> MyClass(2)
2
<__main__.C object at 0x7fae87e0d208>
>>> list(map(MyClass, [1,2,3]))
1
2
3
[<__main__.C object at 0x7fae87e0d2e8>, <__main__.C object at 0x7fae87e0d358>, <__main__.C object at 0x7fae87e0d390>]
>>> list(map(C, [1,2,3]))
1
2
3
[<__main__.C object at 0x7fae87e0d3c8>, <__main__.C object at 0x7fae87e0d400>, <__main__.C object at 0x7fae87e0d438>]
>>> C.test_attribute = True
>>> MyClass.test_attribute
True