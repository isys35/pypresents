def repeater(repeat=1):
    """Повторение выполнения кода"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(repeat):
                print(f'{i+1}: ', end='')
                val = func(*args, **kwargs)
            return val
        return wrapper
    return decorator