my_list = [1, 2, 2, 2, 2, 3]
print(my_list.index(2))  # первый элемент равный 2 находится по индексу 1 (индексация с нуля!)
print(my_list.index(5))  # ValueError: 5 is not in list - отсутствующий элемент выдаст ошибку!