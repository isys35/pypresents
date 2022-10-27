my_set = {1, 2, 3}
my_set_2 = my_set.copy()
print(my_set_2 == my_set)  # True - коллекции равны - содержат одинаковые значения
print(my_set_2 is my_set)  # False - коллекции не идентичны - это разные объекты с разными id