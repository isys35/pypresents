>>> class A(SingletonBase):
...     pass
...
>>> class B(A):
...     pass
...
>>> print(A())
<__main__.A object at 0x10c8d8710>
>>> print(A())
<__main__.A object at 0x10c8d8710>
>>> print(B())
<__main__.A object at 0x10c8d8710>