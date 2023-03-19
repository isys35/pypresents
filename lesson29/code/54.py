>>> Book.objects.aggregate(average_price=Avg('price'))
{'average_price': 34.35}