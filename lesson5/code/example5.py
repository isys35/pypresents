my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
print('a' in my_dict)               # True - без указания метода поиск по ключам
print('a' in my_dict.keys())        # True - аналогично примеру выше
print('a' in my_dict.values())      # False - так как 'а' — ключ, не значение
print(1 in my_dict.values())        # True