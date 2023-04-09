from django.db.transaction import atomic

@atomic
def edit(request, pk):
		# В этом контроллере будет действовать режим атомарных запросов