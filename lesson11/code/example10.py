>>> class Test:
>>>     def __bool__(self):
>>>         return True
>>>
>>> test = Test()
>>>
>>> if test:
>>>    print("Hello World")
>>>
... 'Hello World'