>>> Book.objects.aggregate(Avg('price'))
{'price__avg': 34.35}