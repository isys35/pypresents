>>> for b in Book.objects.filter(name='Идиот'):
...     print(b.pk, ': ', b.name)