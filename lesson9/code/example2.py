def double(function):
    def inner(argument):
        return function(function(argument))
    return inner

def multiply_by_five(x):
    return x * 5

double(multiply_by_five)(3)
# 75