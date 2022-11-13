>>> class Meter:
...     def __len__(self):
...         return 1_000
... 
>>> len([1, 2, 3])
3
>>> len("Duck typing...")
14
>>> len(Meter())
1000