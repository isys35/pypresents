list_a = [-2, -1, 0, 1, 2, 3, 4, 5]
my_gen = (i for i in list_a)    # выражение-генератор
print(next(my_gen))     # -2 - получаем очередной элемент генератора
print(next(my_gen))     # -1 - получаем очередной элемент генератора