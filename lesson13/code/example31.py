def my_metaclass(class_name, parents, attributes):
    print('In metaclass, creating the class.')
    return type(class_name, parents, attributes)


def my_class_decorator(class_):
    print('In decorator, chance to modify the class.')
    return class_


@my_class_decorator
class C(metaclass=my_metaclass):
    def __init__(self):
        print('Creating object.')