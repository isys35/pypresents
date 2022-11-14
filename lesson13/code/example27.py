>>> def my_class_init(self, attr_value):
...     self.my_attribute = attr_value
...
>>> MyClass = type('MyClass', (object,), {'__init__': my_class_init})
>>> o = MyClass('test')
>>> o.my_attribute
'test'