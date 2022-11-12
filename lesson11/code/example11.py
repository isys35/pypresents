>>> class Test:
>>>     def __call__(self, message):
>>>         print(message)
>>>         return True
>>>
>>> test = Test()
>>> test("Hello World")
... 'Hello World'
... True