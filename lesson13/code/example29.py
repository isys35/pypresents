def log_everything_metaclass(class_name, parents, attributes):
    print('Creating class', class_name)
    myattributes = {}
    for name, attr in attributes.items():
        myattributes[name] = attr
        if hasattr(attr, '__call__'):
            myattributes[name] = logged(
                "%b %d %Y - %H:%M:%S", class_name + "."
            )(attr)
    return type(class_name, parents, myattributes)


class C(metaclass=log_everything_metaclass):

    def __init__(self, x):
        self.x = x

    def print_x(self):
        print(self.x)
# Usage:
print('Starting object creation')
c = C('Test')
c.print_x()