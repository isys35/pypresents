>>> for b in Book.objects.order_by('name'):
...     print(b.pk, ': ', b.name)