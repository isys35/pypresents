>>> MyClass = type('MyClass', (object,), {'my_attribute': 0})
>>> type(MyClass)
<class 'type'>
>>> o = MyClass()
>>> o.my_attribute
0