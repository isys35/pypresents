>>> class meta(type):
...     def __new__(cls, class_name, parents, attributes):
...         print('meta.__new__')
...         return super().__new__(cls, class_name, parents, attributes)
...     def __call__(self, *args, **kwargs):
...         print('meta.__call__')
...         return super().__call__(*args, **kwargs)
...
>>> class C(metaclass=meta):
...     pass
...
meta.__new__
>>> o = C()
meta.__call__