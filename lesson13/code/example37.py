>>> class A(SingletonBaseMeta):
...     pass
...
>>> class B(A):
...     pass
...
>>> print(A())
<__main__.A object at 0x1101f6358>
>>> print(A())
<__main__.A object at 0x1101f6358>
>>> print(B())
<__main__.B object at 0x1101f6eb8>