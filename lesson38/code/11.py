>>> Restaurant.objects.prefetch_related('pizzas__toppings')