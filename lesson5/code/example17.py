my_tuple = ('a', 'b', 'a')
my_list = list(my_tuple)
my_set = set(my_tuple)		        # теряем индексы и дубликаты элементов!
my_frozenset = frozenset(my_tuple)      # теряем индексы и дубликаты элементов!
print(my_list, my_set, my_frozenset)    # ['a', 'b', 'a'] {'a', 'b'} frozenset({'a', 'b'})