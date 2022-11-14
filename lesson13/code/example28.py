>>> def my_metaclass(name, parents, attributes):
...     return 'Hello'
...
>>> class C(metaclass=my_metaclass):
...     pass
...
>>> C
'Hello'
>>> type(C)
<class 'str'>